#!/usr/bin/env python3
"""
Generate Face QR Code

This script takes a face image and encodes it into a QR code with a display_face_image task.
The QR code can later be decoded to reconstruct and display the original face image.
"""

import os
import sys
import argparse
import base64
import json
import uuid
import time
from PIL import Image, ImageOps
import qrcode
import io
import zlib

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio

def resize_image(image_path, size_px):
    """
    Resize an image to the specified size while maintaining aspect ratio
    
    Args:
        image_path: Path to the image file
        size_px: Target size (max dimension)
        
    Returns:
        PIL.Image: Resized image
    """
    try:
        img = Image.open(image_path)
        
        # Calculate new dimensions while maintaining aspect ratio
        width, height = img.size
        if width > height:
            new_width = size_px
            new_height = int(height * (size_px / width))
        else:
            new_height = size_px
            new_width = int(width * (size_px / height))
            
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        return resized_img
        
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None

def encode_face_to_qr(image_path, output_path, size_px=32, jpeg_quality=60):
    """
    Encode a face image into a QR code with a display_face_image task
    
    Args:
        image_path: Path to the face image
        output_path: Path to save the QR code
        size_px: Size to resize the image to (max dimension)
        jpeg_quality: JPEG quality for compression (1-95)
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # 1. Resize the image
        print(f"[+] Resizing image to max dimension of {size_px}px...")
        resized_img = resize_image(image_path, size_px)
        if resized_img is None:
            return False
            
        print(f"    Resized dimensions: {resized_img.width}x{resized_img.height}")
        
        # 2. Convert to grayscale to further reduce size
        print("[+] Converting to grayscale...")
        gray_img = ImageOps.grayscale(resized_img)
        
        # 3. Convert to JPEG and compress
        print(f"[+] Compressing image with JPEG quality {jpeg_quality}...")
        buffer = io.BytesIO()
        gray_img.save(buffer, format="JPEG", quality=jpeg_quality)
        compressed_data = buffer.getvalue()
        
        # 4. Encode the image data as base64
        print("[+] Encoding image as base64...")
        image_data_base64 = base64.b64encode(compressed_data).decode('utf-8')
        
        # 5. Create a task payload with the image data
        task_id = str(uuid.uuid4())
        timestamp = time.time() * PHI  # Phi-harmonic timestamp
        
        task_data = {
            "task_id": task_id,
            "task_type": "display_face_image",
            "timestamp": timestamp,
            "image_data_base64": image_data_base64,
            "original_filename": os.path.basename(image_path),
            "processed_size": f"{gray_img.width}x{gray_img.height}",
            "image_format": "JPEG_Grayscale",
            "compression_quality": jpeg_quality
        }
        
        # 6. Create a QR code with the task data
        print("[+] Creating QR code with task data...")
        qr_data = {
            "task_data": task_data,
            "metadata": {
                "generator": "quantum_face_qr",
                "version": "1.0",
                "phi_resonance": PHI * timestamp % 1
            }
        }
        
        # 7. Try to compress the data if it's too large
        qr_json = json.dumps(qr_data)
        
        try:
            # First try with standard JSON
            qr = qrcode.QRCode(
                version=None,  # Auto-determine version based on data size
                error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
                box_size=10,
                border=4,
            )
            qr.add_data(qr_json)
            qr.make(fit=True)
            
            # Check if version is too high
            if qr.version > 40:
                print(f"[!] QR version {qr.version} is too high, trying with compression...")
                
                # Compress the JSON data
                compressed = zlib.compress(qr_json.encode('utf-8'))
                compressed_b64 = base64.b64encode(compressed).decode('utf-8')
                compressed_data = f"COMPRESSED:{compressed_b64}"
                
                # Try again with compressed data
                qr = qrcode.QRCode(
                    version=None,
                    error_correction=qrcode.constants.ERROR_CORRECT_M,
                    box_size=10,
                    border=4,
                )
                qr.add_data(compressed_data)
                qr.make(fit=True)
                
                if qr.version > 40:
                    print(f"[!] QR version {qr.version} still too high, reducing image quality further...")
                    return False
                
                print(f"[+] Successfully compressed data to fit in QR version {qr.version}")
        except Exception as e:
            print(f"Error creating QR code: {e}")
            return False
        
        # 8. Save the QR code image
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(output_path)
        
        print(f"[SUCCESS] QR code saved to: {output_path}")
        print(f"    Task ID: {task_id}")
        print(f"    Original image: {image_path}")
        print(f"    Compressed size: {len(compressed_data if 'compressed_data' in locals() else qr_json)} bytes")
        print(f"    QR Version: {qr.version}")
        
        return True
        
    except Exception as e:
        print(f"Error encoding face to QR: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encode a face image into a QR code")
    parser.add_argument("--image", required=True, help="Path to the face image")
    parser.add_argument("--output", default="face_qr.png", help="Path to save the QR code")
    parser.add_argument("--size_px", type=int, default=32, help="Size to resize the image to")
    parser.add_argument("--jpeg_quality", type=int, default=60, help="JPEG quality (1-95)")
    
    args = parser.parse_args()
    
    success = encode_face_to_qr(args.image, args.output, args.size_px, args.jpeg_quality)
    sys.exit(0 if success else 1)
