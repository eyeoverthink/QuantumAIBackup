#!/usr/bin/env python3
"""
Secure Face QR Integration

This module integrates:
1. The existing Face-QR system
2. The QR Face 2FA Security System
3. Enhanced face recognition with OpenCV

It provides a unified interface for:
- Face recognition training and verification
- Secure QR code generation from face images
- Face-based QR code verification
- Secure script execution from QR codes

The integration follows phi-harmonic principles for optimal security and performance.
"""

import os
import sys
import json
import base64
import time
import hashlib
import tempfile
import shutil
from pathlib import Path
from typing import List, Dict, Tuple, Union, Optional, Any

# Import original Face-QR system
import face_to_qr
import qr_to_face
import qr_task_worker_from_file

# Import QR Face 2FA Security System
from qr_face_2fa_security_extension import QRFace2FASecurityExtension

# Import enhanced face recognition
from enhanced_face_recognition import EnhancedFaceRecognition

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio


class SecureFaceQRIntegration:
    """
    Integration class for Secure Face QR system.
    
    This class combines the functionality of the original Face-QR system,
    the QR Face 2FA Security System, and enhanced face recognition.
    """
    
    def __init__(self, base_dir: str = None):
        """
        Initialize the integration.
        
        Args:
            base_dir: Base directory for storing face recognition models and data
        """
        # Create base directory if not provided
        if base_dir is None:
            base_dir = os.path.join(os.path.expanduser("~"), ".secure_face_qr")
        
        # Create directories
        os.makedirs(base_dir, exist_ok=True)
        os.makedirs(os.path.join(base_dir, "models"), exist_ok=True)
        os.makedirs(os.path.join(base_dir, "faces"), exist_ok=True)
        os.makedirs(os.path.join(base_dir, "qr_codes"), exist_ok=True)
        
        self.base_dir = base_dir
        
        # Initialize components
        self.security = QRFace2FASecurityExtension(
            keys_dir=os.path.join(base_dir, "keys"),
            generate_keys=True
        )
        
        self.face_recognition = EnhancedFaceRecognition(
            models_dir=os.path.join(base_dir, "models"),
            faces_dir=os.path.join(base_dir, "faces")
        )
        
        # Apply phi-harmonic optimization
        self._apply_phi_harmonic_optimization()
    
    def _apply_phi_harmonic_optimization(self):
        """Apply phi-harmonic optimization to the components"""
        # Set phi-harmonic thresholds for face recognition
        self.face_recognition.set_similarity_threshold(1.0 - 1.0/PHI)  # ~0.618
        self.face_recognition.set_confidence_threshold(1.0/PHI)  # ~0.618
        
        # Set phi-harmonic parameters for QR security
        self.security.set_hash_iterations(int(PHI**8))  # ~46.979
    
    def train_user_face(self, user_id: str, image_paths: List[str], num_variations: int = 3) -> bool:
        """
        Train face recognition for a user with multiple face images.
        
        Args:
            user_id: User identifier
            image_paths: List of paths to face images
            num_variations: Number of variations to generate per image
            
        Returns:
            bool: True if training was successful
        """
        try:
            # Load images
            images = []
            for path in image_paths:
                with open(path, "rb") as f:
                    images.append(f.read())
            
            # Train face recognition
            self.face_recognition.train_user(user_id, images, num_variations)
            return True
            
        except Exception as e:
            print(f"Error training face recognition: {e}")
            return False
    
    def recognize_face(self, image_data: bytes) -> Tuple[Optional[str], float]:
        """
        Recognize a face from image data.
        
        Args:
            image_data: Binary image data
            
        Returns:
            Tuple containing user ID and confidence, or (None, 0.0) if not recognized
        """
        return self.face_recognition.recognize(image_data)
    
    def secure_encode_face_to_qr(
        self,
        image_path: str,
        output_path: str,
        user_id: str = None,
        size_px: int = 32,
        jpeg_quality: int = 60,
        expiration_minutes: int = 10
    ) -> bool:
        """
        Generate a secure QR code from a face image.
        
        Args:
            image_path: Path to the face image
            output_path: Path to save the QR code
            user_id: User identifier (if None, will attempt to recognize)
            size_px: Size of the face image in pixels
            jpeg_quality: JPEG quality for face image compression
            expiration_minutes: Expiration time in minutes
            
        Returns:
            bool: True if QR code generation was successful
        """
        try:
            # Read the image
            with open(image_path, "rb") as f:
                image_data = f.read()
            
            # If user_id not provided, try to recognize the face
            if user_id is None:
                recognized_user_id, confidence = self.recognize_face(image_data)
                if recognized_user_id:
                    user_id = recognized_user_id
                else:
                    user_id = "unknown"
            
            # Create temporary file for original QR code
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                temp_qr_path = temp_file.name
            
            # Generate QR code with original system
            face_to_qr.encode_face_to_qr(
                image_path,
                temp_qr_path,
                size_px=size_px,
                jpeg_quality=jpeg_quality
            )
            
            # Read the QR code
            with open(temp_qr_path, "rb") as f:
                qr_data = f.read()
            
            # Create secure QR code with 2FA security
            payload = self.security.create_face_auth_payload(
                image_data,
                user_id=user_id,
                expiration_minutes=expiration_minutes,
                compress=True,
                encrypt=True
            )
            
            # Create QR code with the secure payload
            self.security.create_qr_code(payload, output_path)
            
            # Clean up
            os.unlink(temp_qr_path)
            
            return True
            
        except Exception as e:
            print(f"Error generating secure QR code: {e}")
            return False
    
    def verify_secure_face_qr(
        self,
        qr_path: str,
        live_face_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Verify a secure QR code against a live face image.
        
        Args:
            qr_path: Path to the QR code
            live_face_path: Path to the live face image (optional)
            
        Returns:
            Dict containing verification results
        """
        result = {
            "success": False,
            "user_id": None,
            "face_match": False,
            "expired": False,
            "error": None,
            "timestamp": time.time() * PHI  # Phi-harmonic timestamp
        }
        
        try:
            # Read QR code
            payload = self.security.read_qr_code(qr_path)
            if not payload:
                result["error"] = "Failed to read QR code"
                return result
            
            # Get face data from payload
            is_valid, face_data, error = self.security.get_face_from_payload(payload)
            if not is_valid:
                result["error"] = f"Invalid payload: {error}"
                return result
            
            # Check if expired
            if face_data.get("expired", False):
                result["expired"] = True
                result["error"] = "QR code has expired"
                return result
            
            # Get user ID
            result["user_id"] = face_data.get("user_id", "unknown")
            
            # If live face provided, verify match
            if live_face_path:
                with open(live_face_path, "rb") as f:
                    live_face_data = f.read()
                
                # Verify face match
                is_valid, error_message = self.security.verify_face_auth(payload, live_face_data)
                result["face_match"] = is_valid
                
                if not is_valid:
                    result["error"] = f"Face verification failed: {error_message}"
                    return result
            
            # All checks passed
            result["success"] = True
            return result
            
        except Exception as e:
            result["error"] = f"Error verifying QR code: {e}"
            return result
    
    def execute_qr_scripts(self, qr_path: str) -> Dict[str, Any]:
        """
        Execute scripts from a QR code.
        
        Args:
            qr_path: Path to the QR code
            
        Returns:
            Dict containing execution results
        """
        result = {
            "success": False,
            "scripts_executed": 0,
            "outputs": [],
            "error": None
        }
        
        try:
            # Read QR code
            payload = self.security.read_qr_code(qr_path)
            if not payload:
                result["error"] = "Failed to read QR code"
                return result
            
            # Get scripts from payload
            is_valid, scripts, error = self.security.get_scripts_from_payload(payload)
            if not is_valid:
                result["error"] = f"Invalid script payload: {error}"
                return result
            
            # Execute scripts
            for script in scripts:
                script_output = self.security.execute_script(script)
                result["outputs"].append({
                    "name": script.get("name", "unnamed"),
                    "type": script.get("type", "unknown"),
                    "output": script_output
                })
                result["scripts_executed"] += 1
            
            result["success"] = True
            return result
            
        except Exception as e:
            result["error"] = f"Error executing scripts: {e}"
            return result
    
    def extract_face_from_qr(self, qr_path: str, output_path: str) -> bool:
        """
        Extract face image from a QR code.
        
        Args:
            qr_path: Path to the QR code
            output_path: Path to save the extracted face image
            
        Returns:
            bool: True if extraction was successful
        """
        try:
            # Try secure extraction first
            payload = self.security.read_qr_code(qr_path)
            if payload:
                is_valid, face_data, error = self.security.get_face_from_payload(payload)
                if is_valid and "face_image" in face_data:
                    # Decode and save face image
                    face_image = base64.b64decode(face_data["face_image"])
                    with open(output_path, "wb") as f:
                        f.write(face_image)
                    return True
            
            # Fall back to original system
            return qr_to_face.decode_qr_to_face(qr_path, output_path)
            
        except Exception as e:
            print(f"Error extracting face from QR code: {e}")
            return False

# Main function for testing
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Secure Face QR Integration")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Encode command
    encode_parser = subparsers.add_parser("encode", help="Encode a face image into a secure QR code")
    encode_parser.add_argument("--image", required=True, help="Path to the face image")
    encode_parser.add_argument("--output", default="secure_face_qr.png", help="Path to save the QR code")
    encode_parser.add_argument("--user_id", help="User ID (optional)")
    encode_parser.add_argument("--size_px", type=int, default=32, help="Size to resize the image to")
    encode_parser.add_argument("--jpeg_quality", type=int, default=60, help="JPEG quality for compression")
    encode_parser.add_argument("--expiration", type=int, default=10, help="Expiration time in minutes")
    
    # Verify command
    verify_parser = subparsers.add_parser("verify", help="Verify a secure face QR code")
    verify_parser.add_argument("--qr", required=True, help="Path to the QR code image")
    verify_parser.add_argument("--live", help="Path to a live face image for comparison")
    
    # Train command
    train_parser = subparsers.add_parser("train", help="Train face recognition for a user")
    train_parser.add_argument("--user_id", required=True, help="User ID")
    train_parser.add_argument("--images", required=True, nargs="+", help="Paths to face images")
    train_parser.add_argument("--variations", type=int, default=3, help="Number of variations to generate per image")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Initialize the integration
    integration = SecureFaceQRIntegration()
    
    # Execute command
    if args.command == "encode":
        integration.secure_encode_face_to_qr(
            args.image,
            args.output,
            user_id=args.user_id,
            size_px=args.size_px,
            jpeg_quality=args.jpeg_quality,
            expiration_minutes=args.expiration
        )
    
    elif args.command == "verify":
        result = integration.verify_secure_face_qr(args.qr, args.live)
        print(json.dumps(result, indent=2))
    
    elif args.command == "train":
        success = integration.train_user_face(args.user_id, args.images, args.variations)
        if success:
            print(f"[+] Successfully trained face recognition for user {args.user_id}")
        else:
            print(f"[!] Failed to train face recognition for user {args.user_id}")
    
    else:
        parser.print_help()
