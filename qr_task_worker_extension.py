#!/usr/bin/env python3
"""
QR Task Worker Extension for Face Image Display

This extension adds support for the 'display_face_image' task type to the QR task worker
without modifying the core qr_task_worker_from_file.py file, following the 'lego' principle.

Usage:
    import qr_task_worker_extension
    qr_task_worker_extension.apply_extension()
"""

import os
import base64
import time
import io
from PIL import Image
import sys
import types
import importlib
import json

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio

def handle_display_face_image(task_id, task_data):
    """
    Handle the display_face_image task type
    
    Args:
        task_id: The ID of the task
        task_data: The task data containing the image_data_base64
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print(f"\n[+] Processing face image display task: {task_id}")
        
        # Extract image data
        image_data_base64 = task_data.get("image_data_base64")
        if not image_data_base64:
            print(f"[!] Error: No image data found in task {task_id}")
            return False
            
        # Get metadata
        original_filename = task_data.get("original_filename", "unknown.jpg")
        processed_size = task_data.get("processed_size", "unknown")
        image_format = task_data.get("image_format", "JPEG")
        compression_quality = task_data.get("compression_quality", "unknown")
        
        print(f"[+] Image metadata:")
        print(f"    Original filename: {original_filename}")
        print(f"    Processed size: {processed_size}")
        print(f"    Image format: {image_format}")
        print(f"    Compression quality: {compression_quality}")
        
        # Decode the base64 image data
        print(f"[+] Decoding base64 image data...")
        image_data = base64.b64decode(image_data_base64)
        
        # Create an image from the decoded data
        print(f"[+] Reconstructing image from decoded data...")
        image = Image.open(io.BytesIO(image_data))
        
        # Create output filename with timestamp
        timestamp = time.time() * PHI  # Phi-harmonic timestamp
        output_filename = f"decoded_face_{task_id}_{int(timestamp)}.png"
        
        # Save the image
        print(f"[+] Saving decoded image to: {output_filename}")
        image.save(output_filename)
        
        print(f"[SUCCESS] Face image decoded and saved: {output_filename}")
        print(f"    Original: {original_filename}")
        print(f"    Size: {image.width}x{image.height}")
        
        return True
        
    except Exception as e:
        print(f"[!] Error processing face image: {e}")
        return False

def patched_process_qr_image_file(original_func):
    """
    Create a patched version of the process_qr_image_file function
    that handles the display_face_image task type
    """
    def wrapper(image_path):
        try:
            # Call the original function to get its local variables
            result = original_func(image_path)
            return result
        except Exception as e:
            # If there's an error in the original function, just pass it through
            print(f"Error in original process_qr_image_file: {e}")
            raise
            
    return wrapper

def monkey_patch_display_face_image_handler():
    """
    Monkey patch the qr_task_worker_from_file.py module to handle display_face_image tasks
    """
    try:
        # Import the module
        import qr_task_worker_from_file
        
        # Save the original function
        original_process_qr_image_file = qr_task_worker_from_file.process_qr_image_file
        
        # Define the patched function
        def patched_process_qr_image_file(image_path):
            """Patched version of process_qr_image_file that handles display_face_image tasks"""
            try:
                # Use the original cv2 and QReader code to read the image and decode QR codes
                import cv2
                cv_image = cv2.imread(image_path)
                if cv_image is None:
                    print(f"Error: Could not read image from path: {image_path}")
                    return
                
                print(f"Attempting to decode QR codes from image: {image_path}")
                decoded_qrs = qr_task_worker_from_file.QFINDER.detect_and_decode(image=cv_image)
                
                if not decoded_qrs or (isinstance(decoded_qrs, list) and not decoded_qrs[0]):
                    print("No QR codes found or decoded in the image.")
                    return
                
                if not isinstance(decoded_qrs, list):
                    decoded_qrs = [decoded_qrs]
                
                for qr_item in decoded_qrs:
                    if qr_item is None:
                        continue
                    
                    qr_content_str = qr_item
                    if isinstance(qr_item, tuple):
                        qr_content_str = qr_item[0]
                    
                    if not qr_content_str:
                        print("Extracted empty QR content. Skipping.")
                        continue
                    
                    try:
                        # Decompress if necessary
                        if qr_content_str.startswith('COMPRESSED:'):
                            print("   [+] Decompressing QR content...")
                            try:
                                compressed_data_b64 = qr_content_str.replace('COMPRESSED:', '')
                                compressed_data = base64.b64decode(compressed_data_b64)
                                decompressed_data = qr_task_worker_from_file.zlib.decompress(compressed_data)
                                qr_content_str = decompressed_data.decode('utf-8')
                                print("   [+] Decompression successful.")
                            except Exception as e:
                                print(f"   [!] Error decompressing QR content: {e}")
                                print(f"   Raw content: {qr_content_str[:100]}...")
                                continue
                        
                        decoded_data = json.loads(qr_content_str)
                        
                        if "task_data" in decoded_data and isinstance(decoded_data["task_data"], dict):
                            print("Detected 'task_data' nesting, using inner payload for task details.")
                            actual_task_payload = decoded_data["task_data"]
                        else:
                            actual_task_payload = decoded_data
                        
                        # Extract common fields
                        task_type = actual_task_payload.get("task_type")
                        task_id = actual_task_payload.get("task_id", "N/A")
                        timestamp = actual_task_payload.get("timestamp", "N/A")
                        
                        print(f"Processing Task ID: {task_id}, Type: {task_type}, Timestamp: {timestamp}")
                        
                        # Check if this is a display_face_image task
                        if task_type == "display_face_image":
                            print(f"Task Type: Display Face Image (ID: {task_id})")
                            
                            # Check if we've already processed this task
                            if task_id and task_id != "N/A" and task_id in qr_task_worker_from_file.PROCESSED_TASK_IDS:
                                print(f"Task {task_id} was already processed. Skipping.")
                                continue
                            
                            # Handle the face image display task
                            handle_display_face_image(task_id, actual_task_payload)
                            
                            # Mark the task as processed
                            if task_id and task_id != "N/A":
                                qr_task_worker_from_file.PROCESSED_TASK_IDS.add(task_id)
                                qr_task_worker_from_file.LAST_PROCESSED_TIME[task_id] = time.time()
                            
                            continue
                        
                    except json.JSONDecodeError:
                        print(f"Decoded QR content, but it's not valid JSON: '{qr_content_str[:100]}...' Skipping.")
                    except Exception as e:
                        print(f"Error processing decoded QR content: {e}")
                
                # Call the original function to handle other task types
                return original_process_qr_image_file(image_path)
                
            except Exception as e:
                print(f"Error in patched process_qr_image_file: {e}")
                # Fall back to the original function
                return original_process_qr_image_file(image_path)
        
        # Replace the original function with our patched version
        qr_task_worker_from_file.process_qr_image_file = patched_process_qr_image_file
        
        print("[+] Successfully patched qr_task_worker_from_file.py to handle display_face_image tasks")
        return True
        
    except Exception as e:
        print(f"[!] Error patching qr_task_worker_from_file.py: {e}")
        return False

def apply_extension():
    """
    Apply the extension to the qr_task_worker_from_file.py module
    """
    success = monkey_patch_display_face_image_handler()
    if success:
        print("[+] QR Task Worker Extension for Face Image Display applied successfully")
    else:
        print("[!] Failed to apply QR Task Worker Extension")
    return success

# Auto-apply the extension when imported directly
if __name__ == "__main__":
    apply_extension()
