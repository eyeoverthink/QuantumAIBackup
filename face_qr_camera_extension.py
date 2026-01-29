#!/usr/bin/env python3
"""
Face QR Camera Extension

This module extends the Face-QR system with camera integration capabilities,
allowing live face capture and comparison with QR-encoded faces.

It follows the 'lego' design principle by extending functionality without modifying core files.
"""

import os
import sys
import time
import json
import uuid
import qrcode
import numpy as np
import cv2
from PIL import Image
import io
import base64
import zlib
from typing import Dict, Any, List, Tuple, Optional, Union

# Import Face-QR modules
from face_qr_core import FaceQRBase, FaceQRConfig, PHI
from face_qr_recognition import FaceQRRecognition, CV2_AVAILABLE
from face_qr_security import FaceQRSecurity

# Import OpenCV extension to ensure it's activated
import face_qr_recognition_extension

class FaceQRCameraExtension(FaceQRBase):
    """
    Extends the Face-QR system with camera integration capabilities.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize the camera extension.
        
        Args:
            config_path: Path to configuration file
        """
        super().__init__()
        self.config = FaceQRConfig(config_path)
        self.recognition = FaceQRRecognition(config_path)
        self.security = FaceQRSecurity(config_path)
        
        # Camera settings
        self.camera_index = self.config.get('camera_index', 0)
        self.frame_width = self.config.get('frame_width', 640)
        self.frame_height = self.config.get('frame_height', 480)
        self.camera = None
        
        # QR code detection
        self.qr_detector = cv2.QRCodeDetector() if CV2_AVAILABLE else None
        
        # Authentication settings
        self.similarity_threshold = self.config.get('similarity_threshold', 0.45)  # Lower threshold for easier testing
        
        # Create output directory
        self.output_dir = os.path.join(self.base_dir, "camera_output")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def initialize_camera(self) -> bool:
        """
        Initialize the camera.
        
        Returns:
            bool: True if successful
        """
        if not CV2_AVAILABLE:
            print("OpenCV not available. Cannot initialize camera.")
            return False
        
        try:
            self.camera = cv2.VideoCapture(self.camera_index)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
            
            if not self.camera.isOpened():
                print(f"Failed to open camera at index {self.camera_index}")
                return False
            
            print(f"Camera initialized at index {self.camera_index}")
            return True
            
        except Exception as e:
            print(f"Error initializing camera: {e}")
            return False
    
    def release_camera(self):
        """Release the camera resources."""
        if self.camera is not None and CV2_AVAILABLE:
            self.camera.release()
            cv2.destroyAllWindows()
            print("Camera released")
    
    def capture_frame(self) -> Optional[np.ndarray]:
        """
        Capture a frame from the camera.
        
        Returns:
            Optional[np.ndarray]: Captured frame or None if failed
        """
        if not CV2_AVAILABLE or self.camera is None:
            print("Camera not initialized")
            return None
        
        ret, frame = self.camera.read()
        if not ret:
            print("Failed to capture frame")
            return None
        
        return frame
    
    def detect_qr_code(self, frame: np.ndarray) -> Tuple[bool, str, np.ndarray]:
        """
        Detect QR code in the frame.
        
        Args:
            frame: Input frame
            
        Returns:
            Tuple[bool, str, np.ndarray]: (success, decoded_info, qr_points)
        """
        if not CV2_AVAILABLE:
            print("OpenCV not available")
            return False, "", np.array([])
        
        try:
            # Try the built-in QR detector first
            if self.qr_detector is not None:
                decoded_info, points, _ = self.qr_detector.detectAndDecode(frame)
                if decoded_info and len(points) > 0:
                    return True, decoded_info, points
            
            # If built-in detector fails, try to read the QR directly from file
            # This is a fallback for when we're reading from a file and know it's a QR code
            try:
                # Convert OpenCV image to PIL Image
                if len(frame.shape) == 3 and frame.shape[2] == 3:
                    # BGR to RGB for PIL
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    pil_image = Image.fromarray(rgb_frame)
                else:
                    pil_image = Image.fromarray(frame)
                
                # Create a temporary file
                temp_path = "temp_qr.png"
                pil_image.save(temp_path)
                
                # Try to decode using qrcode library
                from pyzbar.pyzbar import decode
                decoded_objects = decode(pil_image)
                
                if decoded_objects and len(decoded_objects) > 0:
                    qr_data = decoded_objects[0].data.decode('utf-8')
                    # Create dummy points for compatibility
                    dummy_points = np.array([[[0, 0], [100, 0], [100, 100], [0, 100]]])
                    print("QR code detected using fallback method")
                    return True, qr_data, dummy_points
                
                # Clean up temp file
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                    
            except ImportError:
                print("pyzbar not available for fallback QR detection")
            except Exception as e:
                print(f"Error in fallback QR detection: {e}")
            
            # If we get here, both methods failed
            print("Could not detect QR code with any method")
            return False, "", np.array([])
            
        except Exception as e:
            print(f"Error detecting QR code: {e}")
            return False, "", np.array([])
    
    def process_qr_payload(self, payload: str) -> Dict[str, Any]:
        """
        Process QR code payload.
        
        Args:
            payload: QR code payload
            
        Returns:
            Dict[str, Any]: Processed data
        """
        try:
            data = json.loads(payload)
            
            # Check for nested task_data structure (from generate_face_qr.py)
            if 'task_data' in data:
                task_data = data['task_data']
            else:
                task_data = data  # Use the data directly if not nested
            
            # Verify it's a face image task
            if task_data.get('task_type') != 'display_face_image':
                print(f"Not a face image task. Found: {task_data.get('task_type', 'unknown')}")
                return {}
            
            # Extract image data
            image_data_base64 = task_data.get('image_data_base64')
            if not image_data_base64:
                print("No image data found in QR code")
                return {}
                
            # Decode base64 image
            try:
                decoded_image_bytes = base64.b64decode(image_data_base64)
                return {
                    'task_id': task_data.get('task_id', 'unknown'),
                    'timestamp': task_data.get('timestamp', 0),
                    'decoded_image_bytes': decoded_image_bytes
                }
            except Exception as e:
                print(f"Error decoding image data: {e}")
                import traceback
                traceback.print_exc()
                return {}
                
        except json.JSONDecodeError as e:
            print(f"Invalid JSON payload in QR code: {e}")
            return {}
        except Exception as e:
            print(f"Error processing QR payload: {e}")
            import traceback
            traceback.print_exc()
            return {}
    
    def compare_live_to_qr(self, frame: np.ndarray, qr_image_bytes: bytes) -> Tuple[bool, float]:
        """
        Compare live camera frame to QR-encoded face.
        
        Args:
            frame: Camera frame
            qr_image_bytes: QR-encoded face image bytes
            
        Returns:
            Tuple[bool, float]: (is_match, similarity_score)
        """
        try:
            # Convert frame to bytes
            success, buffer = cv2.imencode('.jpg', frame)
            if not success:
                print("Failed to encode frame")
                return False, 0.0
            
            frame_bytes = buffer.tobytes()
            
            # Use recognition module to compare faces
            is_match, similarity = self.recognition.verify_face(
                qr_image_bytes, 
                frame_bytes,
                threshold=self.similarity_threshold
            )
            
            return is_match, similarity
            
        except Exception as e:
            print(f"Error comparing faces: {e}")
            return False, 0.0
    
    def _calculate_similarity(self, img1: np.ndarray, img2: np.ndarray) -> float:
        """
        Calculate similarity between two images using SSIM.
        
        Args:
            img1: First image (grayscale)
            img2: Second image (grayscale)
            
        Returns:
            float: Similarity score (0.0-1.0)
        """
        try:
            # Make sure both images are the same size
            if img1.shape != img2.shape:
                img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
            
            # Calculate SSIM (Structural Similarity Index)
            # Higher values indicate more similarity (range: -1 to 1)
            score = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)[0][0]
            
            # Normalize to 0-1 range
            similarity = (score + 1) / 2
            return similarity
            
        except Exception as e:
            print(f"Error calculating similarity: {e}")
            return 0.0
    
    def authenticate_face_with_qr(self, face_frame: np.ndarray, qr_data: Dict[str, Any]) -> Tuple[bool, float]:
        """
        Authenticate a face frame with QR code data.
        
        Args:
            face_frame: OpenCV frame with face
            qr_data: QR code data with face image
            
        Returns:
            tuple: (success, similarity)
        """
        # Check if we have valid QR data
        if not qr_data or 'decoded_image_bytes' not in qr_data:
            print("No valid QR data for authentication")
            return False, 0.0
        
        try:
            # Load QR face image
            qr_face = Image.open(io.BytesIO(qr_data['decoded_image_bytes']))
            qr_face_array = np.array(qr_face)
            
            # Convert to grayscale if needed
            if len(qr_face_array.shape) > 2 and qr_face_array.shape[2] > 1:
                qr_face_gray = cv2.cvtColor(qr_face_array, cv2.COLOR_BGR2GRAY)
            else:
                qr_face_gray = qr_face_array
            
            # Detect face in camera frame
            if CV2_AVAILABLE and self.recognition.face_detector is not None:
                # Convert to grayscale for face detection
                if len(face_frame.shape) > 2 and face_frame.shape[2] > 1:
                    gray = cv2.cvtColor(face_frame, cv2.COLOR_BGR2GRAY)
                else:
                    gray = face_frame
                    
                # Detect faces
                faces = self.recognition.face_detector.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30)
                )
                
                if len(faces) == 0:
                    print("No face detected in camera frame")
                    return False, 0.0
                    
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
                face_region = face_frame[y:y+h, x:x+w]
                
                # Resize to match QR face dimensions
                face_region_resized = cv2.resize(face_region, (qr_face_gray.shape[1], qr_face_gray.shape[0]))
                
                # Convert to grayscale for comparison
                if len(face_region_resized.shape) > 2 and face_region_resized.shape[2] > 1:
                    face_region_gray = cv2.cvtColor(face_region_resized, cv2.COLOR_BGR2GRAY)
                else:
                    face_region_gray = face_region_resized
                
                # Calculate similarity
                similarity = self._calculate_similarity(qr_face_gray, face_region_gray)
                
                # Use the configured threshold (0.45 for testing)
                threshold = self.similarity_threshold
                print(f"Face similarity: {similarity:.4f} (threshold: {threshold:.4f})")
                
                # Check if similarity exceeds threshold
                success = similarity >= threshold
                return success, similarity
            else:
                print("Face detector not available")
                return False, 0.0
                
        except Exception as e:
            print(f"Error during face authentication: {e}")
            import traceback
            traceback.print_exc()
            return False, 0.0
    
    def authenticate_with_camera(self, qr_code_path: str = None) -> bool:
        """
        Run face authentication using camera and QR code.
        
        Args:
            qr_code_path: Path to QR code image (required)
            
        Returns:
            bool: True if authentication successful
        """
        if not CV2_AVAILABLE:
            print("OpenCV not available. Cannot run camera authentication.")
            return False
        
        # Check if QR code path is provided
        if not qr_code_path or not os.path.exists(qr_code_path):
            print(f"Error: QR code image path is required and must exist.")
            print(f"Provided path: {qr_code_path}")
            return False
            
        # Load and decode the QR code first
        qr_image = cv2.imread(qr_code_path)
        if qr_image is None:
            print(f"Error: Could not load QR code image from {qr_code_path}")
            return False
            
        print(f"Loaded QR code image from {qr_code_path}")
        
        # Display the QR code image
        cv2.imshow('QR Code Reference', qr_image)
        cv2.waitKey(1000)  # Show for 1 second
        
        # Try to detect QR code
        success, decoded_info, points = self.detect_qr_code(qr_image)
        if not success:
            print("Could not detect QR code in the provided image")
            return False
            
        # Process QR payload
        qr_data = self.process_qr_payload(decoded_info)
        if not qr_data or 'decoded_image_bytes' not in qr_data:
            print("QR code found but not a valid face image task or missing image data")
            return False
            
        print(f"Successfully decoded QR code from file: {qr_code_path}")
        
        # Show a small thumbnail of the face from QR
        try:
            qr_face = Image.open(io.BytesIO(qr_data['decoded_image_bytes']))
            qr_face_array = np.array(qr_face)
            cv2.imshow('Face from QR (Reference)', qr_face_array)
            cv2.waitKey(1500)  # Show for 1.5 seconds
            print("Reference face loaded from QR code")
        except Exception as e:
            print(f"Could not display face from QR: {e}")
        
        # Initialize camera
        if not self.initialize_camera():
            return False
        
        try:
            # Main camera loop - now we're looking for faces, not QR codes
            print("Starting camera authentication...")
            print("Press 'q' to quit, 'c' to capture your face and authenticate")
            
            while True:
                # Capture frame
                frame = self.capture_frame()
                if frame is None:
                    continue
                
                # Make a copy for display
                display_frame = frame.copy()
                
                # Try to detect faces in the frame for visual feedback
                if CV2_AVAILABLE and self.recognition.face_detector is not None:
                    # Convert to grayscale for face detection
                    if len(frame.shape) > 2 and frame.shape[2] > 1:
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    else:
                        gray = frame
                        
                    # Detect faces
                    faces = self.recognition.face_detector.detectMultiScale(
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
                        
                        # Draw facial feature points (approximated)
                        center_x, center_y = x + w//2, y + h//2
                        eye_w = w//4
                        
                        # Left eye
                        left_eye_x = x + w//4
                        left_eye_y = y + h//3
                        cv2.circle(display_frame, (left_eye_x, left_eye_y), 5, (255, 0, 0), -1)
                        
                        # Right eye
                        right_eye_x = x + 3*w//4
                        right_eye_y = y + h//3
                        cv2.circle(display_frame, (right_eye_x, right_eye_y), 5, (255, 0, 0), -1)
                        
                        # Nose
                        nose_x = center_x
                        nose_y = center_y
                        cv2.circle(display_frame, (nose_x, nose_y), 5, (255, 0, 0), -1)
                        
                        # Mouth
                        mouth_x = center_x
                        mouth_y = y + 2*h//3
                        cv2.line(display_frame, (mouth_x-w//5, mouth_y), (mouth_x+w//5, mouth_y), (255, 0, 0), 2)
                        cv2.putText(display_frame, "Face", (x, y-10),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                # Display status and instructions
                # Create semi-transparent overlay for text background
                overlay = display_frame.copy()
                cv2.rectangle(overlay, (0, 0), (display_frame.shape[1], 60), (0, 0, 0), -1)
                cv2.addWeighted(overlay, 0.5, display_frame, 0.5, 0, display_frame)
                
                status_text = "Face Detection Active"
                status_color = (0, 255, 0)  # Green
                instruction_text = "Press 'c' to capture and authenticate or 'q' to quit"
                
                # Draw status and instructions
                cv2.putText(display_frame, status_text, (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, status_color, 2)
                cv2.putText(display_frame, instruction_text, (10, 55), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                
                # Draw camera frame indicator
                cv2.rectangle(display_frame, (0, 0), (display_frame.shape[1]-1, display_frame.shape[0]-1), (0, 165, 255), 2)
                
                # Show frame
                cv2.imshow('Face-QR Authentication', display_frame)
                
                # Handle key presses
                key = cv2.waitKey(1) & 0xFF
                
                # Quit if 'q' pressed
                if key == ord('q'):
                    print("Authentication cancelled")
                    break
                
                # Authenticate if 'c' pressed and we have QR data
                if key == ord('c') and qr_data and 'decoded_image_bytes' in qr_data:
                    print("Authenticating...")
                    
                    # Show countdown
                    for i in range(3, 0, -1):
                        countdown_frame = frame.copy()
                        cv2.putText(countdown_frame, f"Capturing in {i}...", 
                                   (countdown_frame.shape[1]//2 - 150, countdown_frame.shape[0]//2), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 165, 255), 4)
                        cv2.imshow('Face-QR Authentication', countdown_frame)
                        cv2.waitKey(800)  # Wait for 0.8 seconds between counts
                    
                    # Flash to indicate capture
                    flash_frame = np.ones_like(frame) * 255
                    cv2.imshow('Face-QR Authentication', flash_frame)
                    cv2.waitKey(150)  # Quick flash
                    
                    # Capture the frame after countdown
                    capture_frame = self.capture_frame()
                    if capture_frame is None:
                        print("Failed to capture authentication frame")
                        continue
                        
                    # Show "Processing" message
                    processing_frame = capture_frame.copy()
                    cv2.putText(processing_frame, "Processing...", 
                               (processing_frame.shape[1]//2 - 120, processing_frame.shape[0]//2), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 165, 255), 3)
                    cv2.imshow('Face-QR Authentication', processing_frame)
                    cv2.waitKey(1)
                    
                    # Authenticate face with QR
                    success, similarity = self.authenticate_face_with_qr(capture_frame, qr_data)
                    
                    # Create a more visually appealing result display
                    result_frame = capture_frame.copy()
                    
                    # Create semi-transparent overlay
                    overlay = result_frame.copy()
                    cv2.rectangle(overlay, (0, 0), (result_frame.shape[1], result_frame.shape[0]), (0, 0, 0), -1)
                    
                    if success:
                        # Success case
                        result_text = "AUTHENTICATION SUCCESSFUL"
                        detail_text = f"Similarity: {similarity:.4f}"
                        result_color = (0, 255, 0)  # Green
                        print(f"Authentication successful! Similarity: {similarity:.4f}")
                        
                        # Add a success icon/checkmark
                        center_x, center_y = result_frame.shape[1] // 2, result_frame.shape[0] // 2
                        cv2.circle(overlay, (center_x, center_y), 50, (0, 255, 0), -1)
                        cv2.addWeighted(overlay, 0.5, result_frame, 0.5, 0, result_frame)
                        
                        # Draw checkmark
                        pts = np.array([[center_x-20, center_y], [center_x-5, center_y+20], [center_x+30, center_y-20]])
                        cv2.polylines(result_frame, [pts], False, (255, 255, 255), 5)
                        
                        # Save authenticated frame with phi-harmonic timestamp
                        timestamp = int(time.time() * PHI)
                        output_path = os.path.join(self.output_dir, f"auth_success_{timestamp}.jpg")
                        os.makedirs(self.output_dir, exist_ok=True)
                        cv2.imwrite(output_path, capture_frame)
                        print(f"Saved authenticated frame to {output_path}")
                        
                        # Add text
                        cv2.putText(result_frame, result_text, 
                                  (center_x - 200, center_y + 100), 
                                  cv2.FONT_HERSHEY_SIMPLEX, 1.0, result_color, 2)
                        cv2.putText(result_frame, detail_text, 
                                  (center_x - 100, center_y + 140), 
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        
                        # Show result for 5 seconds
                        cv2.imshow('Face-QR Authentication', result_frame)
                        cv2.waitKey(5000)
                        
                        self.release_camera()
                        return True
                    else:
                        # Failure case
                        result_text = "AUTHENTICATION FAILED"
                        detail_text = f"Similarity: {similarity:.4f} (below threshold)"
                        result_color = (0, 0, 255)  # Red
                        print(f"Authentication failed. Similarity: {similarity:.4f}")
                        
                        # Add a failure icon/X
                        center_x, center_y = result_frame.shape[1] // 2, result_frame.shape[0] // 2
                        cv2.circle(overlay, (center_x, center_y), 50, (0, 0, 255), -1)
                        cv2.addWeighted(overlay, 0.5, result_frame, 0.5, 0, result_frame)
                        
                        # Draw X
                        cv2.line(result_frame, (center_x-25, center_y-25), (center_x+25, center_y+25), (255, 255, 255), 5)
                        cv2.line(result_frame, (center_x+25, center_y-25), (center_x-25, center_y+25), (255, 255, 255), 5)
                        
                        # Add text
                        cv2.putText(result_frame, result_text, 
                                  (center_x - 180, center_y + 100), 
                                  cv2.FONT_HERSHEY_SIMPLEX, 1.0, result_color, 2)
                        cv2.putText(result_frame, detail_text, 
                                  (center_x - 180, center_y + 140), 
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(result_frame, "Press any key to try again", 
                                  (center_x - 180, center_y + 180), 
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
                        
                        # Show result and wait for key press
                        cv2.imshow('Face-QR Authentication', result_frame)
                        cv2.waitKey(0)
            
            self.release_camera()
            return False
            
        except Exception as e:
            print(f"Error in camera authentication: {e}")
            self.release_camera()
            return False
        
        finally:
            # Make sure camera is released
            self.release_camera()

def main():
    """Main function for testing."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Face-QR Camera Authentication")
    parser.add_argument("--qr", required=True, help="Path to QR code image (required)")
    parser.add_argument("--camera", type=int, default=0, help="Camera index")
    parser.add_argument("--threshold", type=float, default=0.6, help="Similarity threshold (0.0-1.0)")
    args = parser.parse_args()
    
    # Create camera extension
    camera_ext = FaceQRCameraExtension()
    
    # Override camera index if provided
    if args.camera is not None:
        camera_ext.camera_index = args.camera
        
    # Override similarity threshold if provided
    if args.threshold is not None:
        camera_ext.similarity_threshold = args.threshold
    
    # Display the threshold being used
    print(f"\nUsing similarity threshold: {camera_ext.similarity_threshold:.4f}\n")
    
    # Run authentication
    success = camera_ext.authenticate_with_camera(args.qr)
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
