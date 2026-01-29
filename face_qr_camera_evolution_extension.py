#!/usr/bin/env python3
"""
Face QR Camera Evolution Extension

This module extends the Face-QR camera system with direct evolution capabilities,
allowing captured images to be immediately saved as QR codes and run through
the evolution process.

It follows the 'lego' design principle by extending functionality without modifying core files.
"""

import os
import sys
import time
import json
import uuid
import base64
import numpy as np
import cv2
from PIL import Image
import io
from datetime import datetime
from typing import Dict, Any, List, Tuple, Optional, Union
import qrcode

# Import Face-QR modules
from face_qr_core import FaceQRBase, FaceQRConfig, PHI
from face_qr_camera_extension import FaceQRCameraExtension
from face_qr_evolution_extension import FaceQREvolutionExtension
from face_qr_json_helper import FaceQRJsonHelper

class FaceQRCameraEvolutionExtension(FaceQRBase):
    """
    Extends the Face-QR camera system with direct evolution capabilities.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize the camera evolution extension.
        
        Args:
            config_path: Path to configuration file
        """
        super().__init__()
        self.config = FaceQRConfig(config_path)
        self.camera_extension = FaceQRCameraExtension(config_path)
        self.evolution_extension = FaceQREvolutionExtension(config_path)
        self.json_helper = FaceQRJsonHelper()
        
        # Create output directories
        self.evolution_dir = os.path.join(self.base_dir, "evolution_data")
        self.qr_output_dir = os.path.join(self.base_dir, "qr_output")
        os.makedirs(self.evolution_dir, exist_ok=True)
        os.makedirs(self.qr_output_dir, exist_ok=True)
        
        # Load evolution parameters
        self._load_evolution_parameters()
    
    def _load_evolution_parameters(self):
        """Load evolution parameters from the evolution extension."""
        # Get current parameters from evolution extension
        self.similarity_threshold = self.evolution_extension.similarity_threshold
        self.feature_weight = self.evolution_extension.feature_weight
        self.temporal_factor = self.evolution_extension.temporal_factor
        self.complexity = self.evolution_extension.complexity
        self.resonance = self.evolution_extension.resonance
        self.mutation_rate = self.evolution_extension.mutation_rate
        
        # Log current parameters
        print(f"Loaded evolution parameters:")
        print(f"  Similarity Threshold: {self.similarity_threshold:.4f}")
        print(f"  Feature Weight: {self.feature_weight:.4f}")
        print(f"  Temporal Factor: {self.temporal_factor:.4f}")
        print(f"  Complexity: {self.complexity:.4f}")
        print(f"  Resonance: {self.resonance:.4f}")
        print(f"  Mutation Rate: {self.mutation_rate:.4f}")
    
    def capture_and_save_qr(self) -> Tuple[bool, str]:
        """
        Capture an image from the camera and save it as a QR code.
        
        Returns:
            Tuple[bool, str]: (success, qr_code_path)
        """
        # Initialize camera
        if not self.camera_extension.initialize_camera():
            print("Failed to initialize camera")
            return False, ""
        
        try:
            print("Starting camera capture for QR generation...")
            print("Press 'q' to quit, 'c' to capture your face and generate QR code")
            
            while True:
                # Capture frame
                frame = self.camera_extension.capture_frame()
                if frame is None:
                    continue
                
                # Make a copy for display
                display_frame = frame.copy()
                
                # Try to detect faces in the frame for visual feedback
                if self.camera_extension.recognition.face_detector is not None:
                    # Convert to grayscale for face detection
                    if len(frame.shape) > 2 and frame.shape[2] > 1:
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    else:
                        gray = frame
                        
                    # Detect faces
                    faces = self.camera_extension.recognition.face_detector.detectMultiScale(
                        gray,
                        scaleFactor=1.1,
                        minNeighbors=5,
                        minSize=(30, 30)
                    )
                    
                    # Draw rectangles around faces with enhanced visual feedback
                    for (x, y, w, h) in faces:
                        # Draw green rectangle around face
                        cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        
                        # Add face detection indicator
                        cv2.putText(display_frame, "Face Detected", (x, y-10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                # Display status and instructions
                # Create semi-transparent overlay for text background
                overlay = display_frame.copy()
                cv2.rectangle(overlay, (0, 0), (display_frame.shape[1], 60), (0, 0, 0), -1)
                cv2.addWeighted(overlay, 0.5, display_frame, 0.5, 0, display_frame)
                
                status_text = "QR Generation Mode"
                status_color = (0, 165, 255)  # Orange
                instruction_text = "Press 'c' to capture and generate QR code or 'q' to quit"
                
                # Draw status and instructions
                cv2.putText(display_frame, status_text, (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, status_color, 2)
                cv2.putText(display_frame, instruction_text, (10, 55), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                
                # Show frame
                cv2.imshow('Face-QR Generation', display_frame)
                
                # Handle key presses
                key = cv2.waitKey(1) & 0xFF
                
                # Quit if 'q' pressed
                if key == ord('q'):
                    print("QR generation cancelled")
                    self.camera_extension.release_camera()
                    cv2.destroyAllWindows()
                    return False, ""
                
                # Generate QR if 'c' pressed
                if key == ord('c'):
                    print("Capturing image for QR code generation...")
                    
                    # Show countdown
                    for i in range(3, 0, -1):
                        countdown_frame = frame.copy()
                        cv2.putText(countdown_frame, f"Capturing in {i}...", 
                                   (countdown_frame.shape[1]//2 - 150, countdown_frame.shape[0]//2), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 165, 255), 4)
                        cv2.imshow('Face-QR Generation', countdown_frame)
                        cv2.waitKey(800)  # Wait for 0.8 seconds between counts
                    
                    # Flash to indicate capture
                    flash_frame = np.ones_like(frame) * 255
                    cv2.imshow('Face-QR Generation', flash_frame)
                    cv2.waitKey(150)  # Quick flash
                    
                    # Capture the frame after countdown
                    capture_frame = self.camera_extension.capture_frame()
                    if capture_frame is None:
                        print("Failed to capture frame for QR generation")
                        continue
                    
                    # Show "Processing" message
                    processing_frame = capture_frame.copy()
                    cv2.putText(processing_frame, "Generating QR Code...", 
                               (processing_frame.shape[1]//2 - 150, processing_frame.shape[0]//2), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 165, 255), 3)
                    cv2.imshow('Face-QR Generation', processing_frame)
                    cv2.waitKey(1)
                    
                    # Save the captured frame as a QR code
                    qr_code_path = self._generate_qr_from_frame(capture_frame)
                    
                    if qr_code_path:
                        print(f"QR code generated successfully: {qr_code_path}")
                        
                        # Display success message
                        success_frame = capture_frame.copy()
                        cv2.putText(success_frame, "QR Code Generated!", 
                                   (success_frame.shape[1]//2 - 150, success_frame.shape[0]//2), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                        cv2.imshow('Face-QR Generation', success_frame)
                        cv2.waitKey(2000)  # Show for 2 seconds
                        
                        # Release camera and close windows
                        self.camera_extension.release_camera()
                        cv2.destroyAllWindows()
                        
                        return True, qr_code_path
                    else:
                        print("Failed to generate QR code")
                        
                        # Display error message
                        error_frame = capture_frame.copy()
                        cv2.putText(error_frame, "QR Generation Failed!", 
                                   (error_frame.shape[1]//2 - 150, error_frame.shape[0]//2), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                        cv2.imshow('Face-QR Generation', error_frame)
                        cv2.waitKey(2000)  # Show for 2 seconds
                        
                        continue
        
        except Exception as e:
            print(f"Error in capture_and_save_qr: {e}")
            import traceback
            traceback.print_exc()
            return False, ""
        
        finally:
            # Make sure to release camera resources
            self.camera_extension.release_camera()
            cv2.destroyAllWindows()
        
        return False, ""
    
    def _generate_qr_from_frame(self, frame: np.ndarray) -> str:
        """
        Generate a QR code from a captured frame.
        
        Args:
            frame: Captured frame
            
        Returns:
            str: Path to generated QR code image
        """
        try:
            # Detect face in the frame
            if self.camera_extension.recognition.face_detector is not None:
                # Convert to grayscale for face detection
                if len(frame.shape) > 2 and frame.shape[2] > 1:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                else:
                    gray = frame
                    
                # Detect faces
                faces = self.camera_extension.recognition.face_detector.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30)
                )
                
                if len(faces) == 0:
                    print("No face detected in captured frame")
                    return ""
                    
                # Get largest face (by area)
                largest_face = None
                largest_area = 0
                for (x, y, w, h) in faces:
                    area = w * h
                    if area > largest_area:
                        largest_area = area
                        largest_face = (x, y, w, h)
                
                # Extract face region
                x, y, w, h = largest_face
                face_region = frame[y:y+h, x:x+w]
                
                # Resize to 16x16 for QR code (standard size used in Face-QR system)
                face_small = cv2.resize(face_region, (16, 16))
                
                # Convert to grayscale if needed
                if len(face_small.shape) > 2 and face_small.shape[2] > 1:
                    face_small_gray = cv2.cvtColor(face_small, cv2.COLOR_BGR2GRAY)
                else:
                    face_small_gray = face_small
                
                # Create a PIL Image from the face
                pil_image = Image.fromarray(face_small_gray)
                
                # Convert to bytes
                img_byte_arr = io.BytesIO()
                pil_image.save(img_byte_arr, format='JPEG', quality=30)  # Low quality for smaller QR code
                img_bytes = img_byte_arr.getvalue()
                
                # Encode as base64
                img_base64 = base64.b64encode(img_bytes).decode('utf-8')
                
                # Create task data
                task_id = str(uuid.uuid4())
                timestamp = int(time.time())
                task_data = {
                    "task_id": task_id,
                    "task_type": "display_face_image",
                    "timestamp": timestamp,
                    "image_data_base64": img_base64
                }
                
                # Create QR code
                qr = qrcode.QRCode(
                    version=24,  # Higher version for more data capacity
                    error_correction=qrcode.constants.ERROR_CORRECT_M,
                    box_size=10,
                    border=4,
                )
                
                # Add data to QR code
                qr.add_data(json.dumps({"task_data": task_data}))
                qr.make(fit=True)
                
                # Create QR code image
                qr_img = qr.make_image(fill_color="black", back_color="white")
                
                # Generate phi-harmonic filename
                phi_time = (timestamp * PHI) % 1
                qr_filename = f"face_qr_{timestamp}_{phi_time:.6f}.png"
                qr_path = os.path.join(self.qr_output_dir, qr_filename)
                
                # Save QR code image
                qr_img.save(qr_path)
                
                print(f"QR code generated and saved to: {qr_path}")
                return qr_path
            else:
                print("Face detector not available")
                return ""
                
        except Exception as e:
            print(f"Error generating QR code from frame: {e}")
            import traceback
            traceback.print_exc()
            return ""
    
    def run_evolution_on_qr(self, qr_code_path: str) -> bool:
        """
        Run evolution process on a QR code.
        
        Args:
            qr_code_path: Path to QR code image
            
        Returns:
            bool: True if evolution was successful
        """
        if not qr_code_path or not os.path.exists(qr_code_path):
            print(f"QR code path is invalid or does not exist: {qr_code_path}")
            return False
        
        try:
            print(f"Running evolution on QR code: {qr_code_path}")
            
            # Load QR code image
            qr_image = cv2.imread(qr_code_path)
            if qr_image is None:
                print(f"Failed to load QR code image: {qr_code_path}")
                return False
            
            # Detect QR code
            success, decoded_info, points = self.camera_extension.detect_qr_code(qr_image)
            if not success:
                print(f"Failed to detect QR code in image: {qr_code_path}")
                return False
            
            # Process QR payload
            qr_data = self.camera_extension.process_qr_payload(decoded_info)
            if not qr_data or 'decoded_image_bytes' not in qr_data:
                print("QR code found but not a valid face image task or missing image data")
                return False
            
            # Extract face image from QR
            face_image = Image.open(io.BytesIO(qr_data['decoded_image_bytes']))
            face_array = np.array(face_image)
            
            # Create a test authentication scenario
            # We'll simulate authentication with the same face (should succeed)
            authentication_result = {
                'task_id': qr_data.get('task_id', 'unknown'),
                'timestamp': int(time.time()),
                'success': True,  # Assume success for evolution
                'similarity': 0.85,  # High similarity since it's the same face
                'phi_time': (time.time() * PHI) % 1
            }
            
            # Run evolution based on this authentication result
            evolution_result = self.evolution_extension.evolve_parameters(authentication_result)
            
            if evolution_result:
                # Log evolution results
                print("\nEvolution Results:")
                print(f"  Generation: {evolution_result.get('generation', 'unknown')}")
                print(f"  Similarity Threshold: {evolution_result.get('similarity_threshold', 0):.4f}")
                print(f"  Feature Weight: {evolution_result.get('feature_weight', 0):.4f}")
                print(f"  Temporal Factor: {evolution_result.get('temporal_factor', 0):.4f}")
                print(f"  Complexity: {evolution_result.get('complexity', 0):.4f}")
                print(f"  Resonance: {evolution_result.get('resonance', 0):.4f}")
                print(f"  Mutation Rate: {evolution_result.get('mutation_rate', 0):.4f}")
                
                # Update our local parameters
                self._load_evolution_parameters()
                
                return True
            else:
                print("Evolution process did not return results")
                return False
            
        except Exception as e:
            print(f"Error running evolution on QR code: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def camera_to_qr_to_evolution(self) -> bool:
        """
        Run the complete workflow: capture image, save as QR, and run evolution.
        
        Returns:
            bool: True if the complete workflow was successful
        """
        try:
            print("\n=== Starting Camera-to-QR-to-Evolution Workflow ===\n")
            
            # Step 1: Capture image and save as QR code
            print("\n--- Step 1: Capturing Image and Generating QR Code ---\n")
            success, qr_code_path = self.capture_and_save_qr()
            
            if not success or not qr_code_path:
                print("Failed to capture image and generate QR code")
                return False
            
            # Step 2: Run evolution on the generated QR code
            print("\n--- Step 2: Running Evolution Process on QR Code ---\n")
            evolution_success = self.run_evolution_on_qr(qr_code_path)
            
            if not evolution_success:
                print("Failed to run evolution on QR code")
                return False
            
            print("\n=== Camera-to-QR-to-Evolution Workflow Completed Successfully ===\n")
            return True
            
        except Exception as e:
            print(f"Error in camera_to_qr_to_evolution workflow: {e}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """Main function for testing."""
    try:
        # Create camera evolution extension
        camera_evolution = FaceQRCameraEvolutionExtension()
        
        # Run the complete workflow
        success = camera_evolution.camera_to_qr_to_evolution()
        
        if success:
            print("Camera-to-QR-to-Evolution workflow completed successfully!")
            return 0
        else:
            print("Camera-to-QR-to-Evolution workflow failed")
            return 1
            
    except Exception as e:
        print(f"Error in main: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
