#!/usr/bin/env python3
"""
QR Face 2FA System

This module implements a secure two-factor authentication system using:
1. Face images encoded in QR codes
2. Phi-harmonic timestamps (fraymus system)
3. Blockchain verification
4. Anti-tamper protection

The system follows the 'lego' modular design principle and leverages existing
quantum components for enhanced security.
"""

import os
import sys
import argparse
import base64
import json
import uuid
import time
import hashlib
import zlib
import logging
from typing import Dict, Any, Optional, Tuple
from datetime import datetime
from PIL import Image, ImageOps
import qrcode
import io
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Import quantum modules
from quantum_blockchain_connector import QuantumBlockchainConnector

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio
PHI_POWERS = {
    "φ": PHI,
    "φ²": PHI**2,
    "φ³": PHI**3,
    "φ⁷·⁵": PHI**7.5
}

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QRFace2FA")

class QRFace2FA:
    """
    QR Face 2FA System
    
    This class implements a secure two-factor authentication system using face images
    encoded in QR codes with blockchain verification and phi-harmonic timestamps.
    """
    
    def __init__(self, blockchain_connector: Optional[QuantumBlockchainConnector] = None):
        """
        Initialize the QR Face 2FA system
        
        Args:
            blockchain_connector: Optional QuantumBlockchainConnector instance
        """
        self.blockchain_connector = blockchain_connector or QuantumBlockchainConnector()
        self.user_registry = {}
        self.auth_history = {}
        
        # Ensure directories exist
        os.makedirs("qr_face_2fa/users", exist_ok=True)
        os.makedirs("qr_face_2fa/auth_history", exist_ok=True)
        os.makedirs("qr_face_2fa/qr_codes", exist_ok=True)
        
        # Load existing user registry if available
        self._load_user_registry()
        
        logger.info("QR Face 2FA system initialized")
    
    def register_user(self, user_id: str, face_image_path: str, 
                     size_px: int = 24, jpeg_quality: int = 50) -> Dict[str, Any]:
        """
        Register a new user with their face image
        
        Args:
            user_id: Unique identifier for the user
            face_image_path: Path to the user's face image
            size_px: Size to resize the image to (max dimension)
            jpeg_quality: JPEG quality for compression (1-95)
            
        Returns:
            dict: Registration results
        """
        try:
            # Generate a unique registration ID
            registration_id = str(uuid.uuid4())
            
            # Calculate phi-harmonic timestamp
            timestamp = time.time()
            phi_time = timestamp * PHI
            resonance = phi_time % 1
            
            # Process the face image
            img = self._process_face_image(face_image_path, size_px, jpeg_quality)
            
            # Convert image to base64
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='JPEG', quality=jpeg_quality)
            img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
            
            # Calculate image hash
            img_hash = hashlib.sha256(img_byte_arr.getvalue()).hexdigest()
            
            # Create user data
            user_data = {
                "user_id": user_id,
                "registration_id": registration_id,
                "timestamp": timestamp,
                "phi_time": phi_time,
                "resonance": resonance,
                "face_image_hash": img_hash,
                "face_image_size": size_px,
                "face_image_quality": jpeg_quality,
                "created_at": datetime.now().isoformat()
            }
            
            # Generate QR code
            qr_data = {
                "task_type": "2fa_verification",
                "user_id": user_id,
                "registration_id": registration_id,
                "timestamp": timestamp,
                "phi_time": phi_time,
                "resonance": resonance,
                "face_image_hash": img_hash,
                "image_data_base64": img_base64
            }
            
            # Compress large payloads
            qr_json = json.dumps(qr_data)
            if len(qr_json) > 1000:
                qr_json = zlib.compress(qr_json.encode('utf-8'))
                qr_json = base64.b64encode(qr_json).decode('utf-8')
                qr_data = {"compressed": True, "data": qr_json}
            
            # Generate QR code
            qr_path = f"qr_face_2fa/qr_codes/{user_id}_{registration_id}.png"
            self._generate_qr_code(qr_data, qr_path)
            
            # Store user data
            user_data["qr_path"] = qr_path
            user_data["face_image_base64"] = img_base64
            self.user_registry[user_id] = user_data
            
            # Save user registry
            self._save_user_registry()
            
            # Store in blockchain for verification
            blockchain_ref = self._store_in_blockchain(user_id, user_data)
            user_data["blockchain_ref"] = blockchain_ref
            
            logger.info(f"User {user_id} registered successfully with registration ID {registration_id}")
            
            return {
                "success": True,
                "user_id": user_id,
                "registration_id": registration_id,
                "qr_path": qr_path,
                "blockchain_ref": blockchain_ref,
                "phi_resonance": resonance
            }
            
        except Exception as e:
            logger.error(f"Error registering user {user_id}: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def verify_user(self, face_image_path: str, tolerance: float = 0.2) -> Dict[str, Any]:
        """
        Verify a user using their face image
        
        Args:
            face_image_path: Path to the face image for verification
            tolerance: Similarity tolerance (0-1)
            
        Returns:
            dict: Verification results
        """
        try:
            # Process the face image
            img = Image.open(face_image_path)
            
            # Try to find QR code in the image
            qr_data = self._extract_qr_from_image(img)
            
            if not qr_data:
                # If no QR code found, try face matching against all users
                return self._verify_by_face_matching(face_image_path, tolerance)
            
            # QR code found, verify the data
            if "task_type" not in qr_data or qr_data["task_type"] != "2fa_verification":
                return {
                    "success": False,
                    "error": "Invalid QR code format"
                }
            
            # Extract user data from QR
            user_id = qr_data.get("user_id")
            registration_id = qr_data.get("registration_id")
            qr_timestamp = qr_data.get("timestamp")
            qr_phi_time = qr_data.get("phi_time")
            qr_resonance = qr_data.get("resonance")
            qr_face_hash = qr_data.get("face_image_hash")
            qr_face_base64 = qr_data.get("image_data_base64")
            
            # Check if user exists
            if user_id not in self.user_registry:
                return {
                    "success": False,
                    "error": f"User {user_id} not found"
                }
            
            user_data = self.user_registry[user_id]
            
            # Verify registration ID
            if user_data["registration_id"] != registration_id:
                return {
                    "success": False,
                    "error": "Invalid registration ID"
                }
            
            # Calculate current phi-harmonic timestamp
            current_timestamp = time.time()
            current_phi_time = current_timestamp * PHI
            current_resonance = current_phi_time % 1
            
            # Verify blockchain integrity
            blockchain_verification = self._verify_blockchain_integrity(user_id, user_data)
            if not blockchain_verification["verified"]:
                return {
                    "success": False,
                    "error": "Blockchain verification failed",
                    "details": blockchain_verification
                }
            
            # Process the verification face image with the same parameters as registration
            size_px = user_data["face_image_size"]
            jpeg_quality = user_data["face_image_quality"]
            verification_img = self._process_face_image(face_image_path, size_px, jpeg_quality)
            
            # Convert verification image to base64
            verification_img_byte_arr = io.BytesIO()
            verification_img.save(verification_img_byte_arr, format='JPEG', quality=jpeg_quality)
            verification_img_base64 = base64.b64encode(verification_img_byte_arr.getvalue()).decode('utf-8')
            
            # Calculate verification image hash
            verification_img_hash = hashlib.sha256(verification_img_byte_arr.getvalue()).hexdigest()
            
            # Compare face images
            similarity = self._compare_face_images(
                user_data["face_image_base64"], 
                verification_img_base64
            )
            
            # Record authentication attempt
            auth_result = {
                "user_id": user_id,
                "timestamp": current_timestamp,
                "phi_time": current_phi_time,
                "resonance": current_resonance,
                "similarity": similarity,
                "verified": similarity >= (1 - tolerance),
                "blockchain_verified": blockchain_verification["verified"]
            }
            
            # Update auth history
            if user_id not in self.auth_history:
                self.auth_history[user_id] = []
            self.auth_history[user_id].append(auth_result)
            
            # Save auth history
            self._save_auth_history(user_id, auth_result)
            
            # Store auth attempt in blockchain
            self._store_auth_in_blockchain(user_id, auth_result)
            
            if similarity >= (1 - tolerance):
                logger.info(f"User {user_id} verified successfully with similarity {similarity:.4f}")
                return {
                    "success": True,
                    "user_id": user_id,
                    "similarity": similarity,
                    "phi_resonance": current_resonance,
                    "blockchain_verified": blockchain_verification["verified"]
                }
            else:
                logger.warning(f"User {user_id} verification failed with similarity {similarity:.4f}")
                return {
                    "success": False,
                    "user_id": user_id,
                    "similarity": similarity,
                    "error": "Face verification failed",
                    "phi_resonance": current_resonance
                }
            
        except Exception as e:
            logger.error(f"Error verifying user: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def _process_face_image(self, image_path: str, size_px: int, jpeg_quality: int) -> Image.Image:
        """
        Process a face image for 2FA
        
        Args:
            image_path: Path to the face image
            size_px: Size to resize the image to (max dimension)
            jpeg_quality: JPEG quality for compression (1-95)
            
        Returns:
            PIL.Image: Processed image
        """
        # Open and resize image
        img = Image.open(image_path)
        
        # Convert to grayscale
        img = ImageOps.grayscale(img)
        
        # Calculate new dimensions while maintaining aspect ratio
        width, height = img.size
        if width > height:
            new_width = size_px
            new_height = int(height * (size_px / width))
        else:
            new_height = size_px
            new_width = int(width * (size_px / height))
        
        # Resize image
        img = img.resize((new_width, new_height), Image.LANCZOS)
        
        return img
    
    def _generate_qr_code(self, data: Dict[str, Any], output_path: str) -> bool:
        """
        Generate a QR code from data
        
        Args:
            data: Data to encode in the QR code
            output_path: Path to save the QR code
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Convert data to JSON
            json_data = json.dumps(data)
            
            # Create QR code
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
            )
            qr.add_data(json_data)
            qr.make(fit=True)
            
            # Create an image from the QR Code
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save the image
            img.save(output_path)
            
            return True
        except Exception as e:
            logger.error(f"Error generating QR code: {str(e)}")
            return False
    
    def _extract_qr_from_image(self, image: Image.Image) -> Dict[str, Any]:
        """
        Extract QR code data from an image
        
        Args:
            image: PIL Image object
            
        Returns:
            dict: QR code data or None if not found
        """
        try:
            # Convert PIL image to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_bytes = img_byte_arr.getvalue()
            
            # Decode QR code
            decoded_objects = decode(img_bytes)
            
            if not decoded_objects:
                return None
            
            # Get the first QR code
            qr_data = decoded_objects[0].data.decode('utf-8')
            
            # Parse JSON data
            data = json.loads(qr_data)
            
            # Handle compressed data
            if isinstance(data, dict) and data.get("compressed"):
                compressed_data = base64.b64decode(data["data"])
                decompressed_data = zlib.decompress(compressed_data)
                data = json.loads(decompressed_data.decode('utf-8'))
            
            return data
        except Exception as e:
            logger.error(f"Error extracting QR code: {str(e)}")
            return None
    
    def _compare_face_images(self, base64_img1: str, base64_img2: str) -> float:
        """
        Compare two face images and return similarity score
        
        Args:
            base64_img1: Base64 encoded image 1
            base64_img2: Base64 encoded image 2
            
        Returns:
            float: Similarity score (0-1)
        """
        try:
            # Decode base64 images
            img1_bytes = base64.b64decode(base64_img1)
            img2_bytes = base64.b64decode(base64_img2)
            
            # Convert to numpy arrays
            img1_np = np.frombuffer(img1_bytes, np.uint8)
            img2_np = np.frombuffer(img2_bytes, np.uint8)
            
            # Decode images
            img1 = cv2.imdecode(img1_np, cv2.IMREAD_GRAYSCALE)
            img2 = cv2.imdecode(img2_np, cv2.IMREAD_GRAYSCALE)
            
            # Ensure images are the same size
            if img1.shape != img2.shape:
                img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
            
            # Calculate similarity using structural similarity index
            score = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)[0][0]
            
            # Normalize score to 0-1 range
            score = (score + 1) / 2
            
            return score
        except Exception as e:
            logger.error(f"Error comparing face images: {str(e)}")
            return 0.0
    
    def _verify_by_face_matching(self, face_image_path: str, tolerance: float) -> Dict[str, Any]:
        """
        Verify a user by matching their face against all registered users
        
        Args:
            face_image_path: Path to the face image for verification
            tolerance: Similarity tolerance (0-1)
            
        Returns:
            dict: Verification results
        """
        try:
            best_match = None
            best_similarity = 0
            
            # Process the verification face image
            img = Image.open(face_image_path)
            
            # Try to match against all users
            for user_id, user_data in self.user_registry.items():
                # Process the verification face image with the same parameters as registration
                size_px = user_data["face_image_size"]
                jpeg_quality = user_data["face_image_quality"]
                verification_img = self._process_face_image(face_image_path, size_px, jpeg_quality)
                
                # Convert verification image to base64
                verification_img_byte_arr = io.BytesIO()
                verification_img.save(verification_img_byte_arr, format='JPEG', quality=jpeg_quality)
                verification_img_base64 = base64.b64encode(verification_img_byte_arr.getvalue()).decode('utf-8')
                
                # Compare face images
                similarity = self._compare_face_images(
                    user_data["face_image_base64"], 
                    verification_img_base64
                )
                
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match = user_id
            
            # Calculate current phi-harmonic timestamp
            current_timestamp = time.time()
            current_phi_time = current_timestamp * PHI
            current_resonance = current_phi_time % 1
            
            if best_match and best_similarity >= (1 - tolerance):
                # Verify blockchain integrity
                user_data = self.user_registry[best_match]
                blockchain_verification = self._verify_blockchain_integrity(best_match, user_data)
                
                # Record authentication attempt
                auth_result = {
                    "user_id": best_match,
                    "timestamp": current_timestamp,
                    "phi_time": current_phi_time,
                    "resonance": current_resonance,
                    "similarity": best_similarity,
                    "verified": True,
                    "blockchain_verified": blockchain_verification["verified"],
                    "method": "face_matching"
                }
                
                # Update auth history
                if best_match not in self.auth_history:
                    self.auth_history[best_match] = []
                self.auth_history[best_match].append(auth_result)
                
                # Save auth history
                self._save_auth_history(best_match, auth_result)
                
                # Store auth attempt in blockchain
                self._store_auth_in_blockchain(best_match, auth_result)
                
                logger.info(f"User {best_match} verified by face matching with similarity {best_similarity:.4f}")
                return {
                    "success": True,
                    "user_id": best_match,
                    "similarity": best_similarity,
                    "phi_resonance": current_resonance,
                    "blockchain_verified": blockchain_verification["verified"],
                    "method": "face_matching"
                }
            else:
                logger.warning(f"Face matching verification failed with best similarity {best_similarity:.4f}")
                return {
                    "success": False,
                    "error": "No matching user found",
                    "best_similarity": best_similarity
                }
                
        except Exception as e:
            logger.error(f"Error in face matching verification: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def _store_in_blockchain(self, user_id: str, user_data: Dict[str, Any]) -> str:
        """
        Store user data in blockchain for verification
        
        Args:
            user_id: User ID
            user_data: User data to store
            
        Returns:
            str: Blockchain reference ID
        """
        try:
            # Create metadata
            metadata = {
                "type": "qr_face_2fa_registration",
                "user_id": user_id,
                "registration_id": user_data["registration_id"],
                "timestamp": user_data["timestamp"],
                "phi_time": user_data["phi_time"],
                "resonance": user_data["resonance"],
                "face_image_hash": user_data["face_image_hash"]
            }
            
            # Store in blockchain
            reference_id = self.blockchain_connector.store_system_genesis(metadata)
            
            logger.info(f"User {user_id} data stored in blockchain with reference {reference_id}")
            
            return reference_id
        except Exception as e:
            logger.error(f"Error storing user {user_id} in blockchain: {str(e)}")
            return ""
    
    def _verify_blockchain_integrity(self, user_id: str, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Verify the integrity of user data against blockchain
        
        Args:
            user_id: User ID
            user_data: User data to verify
            
        Returns:
            dict: Verification results
        """
        try:
            # Get blockchain reference ID
            reference_id = user_data.get("blockchain_ref")
            
            if not reference_id:
                return {
                    "verified": False,
                    "error": "No blockchain reference ID"
                }
            
            # Verify integrity
            verification_results = self.blockchain_connector.verify_system_integrity(reference_id)
            
            # Check if verification was successful
            if verification_results.get("verified", False):
                logger.info(f"Blockchain verification successful for user {user_id}")
                return {
                    "verified": True,
                    "details": verification_results
                }
            else:
                logger.warning(f"Blockchain verification failed for user {user_id}")
                return {
                    "verified": False,
                    "error": "Blockchain verification failed",
                    "details": verification_results
                }
                
        except Exception as e:
            logger.error(f"Error verifying blockchain integrity for user {user_id}: {str(e)}")
            return {
                "verified": False,
                "error": str(e)
            }
    
    def _store_auth_in_blockchain(self, user_id: str, auth_result: Dict[str, Any]) -> str:
        """
        Store authentication result in blockchain
        
        Args:
            user_id: User ID
            auth_result: Authentication result
            
        Returns:
            str: Blockchain reference ID
        """
        try:
            # Create metadata
            metadata = {
                "type": "qr_face_2fa_authentication",
                "user_id": user_id,
                "timestamp": auth_result["timestamp"],
                "phi_time": auth_result["phi_time"],
                "resonance": auth_result["resonance"],
                "verified": auth_result["verified"]
            }
            
            # Store in blockchain
            reference_id = self.blockchain_connector.store_system_genesis(metadata)
            
            logger.info(f"Authentication result for user {user_id} stored in blockchain with reference {reference_id}")
            
            return reference_id
        except Exception as e:
            logger.error(f"Error storing authentication result for user {user_id} in blockchain: {str(e)}")
            return ""
    
    def _load_user_registry(self) -> None:
        """Load user registry from file"""
        try:
            registry_path = "qr_face_2fa/users/registry.json"
            
            if os.path.exists(registry_path):
                with open(registry_path, 'r') as f:
                    self.user_registry = json.load(f)
                    
                logger.info(f"Loaded user registry with {len(self.user_registry)} users")
            else:
                logger.info("No existing user registry found, creating new one")
                self.user_registry = {}
                
        except Exception as e:
            logger.error(f"Error loading user registry: {str(e)}")
            self.user_registry = {}
    
    def _save_user_registry(self) -> None:
        """Save user registry to file"""
        try:
            registry_path = "qr_face_2fa/users/registry.json"
            
            with open(registry_path, 'w') as f:
                json.dump(self.user_registry, f, indent=2)
                
            logger.info(f"Saved user registry with {len(self.user_registry)} users")
                
        except Exception as e:
            logger.error(f"Error saving user registry: {str(e)}")
    
    def _save_auth_history(self, user_id: str, auth_result: Dict[str, Any]) -> None:
        """
        Save authentication history for a user
        
        Args:
            user_id: User ID
            auth_result: Authentication result
        """
        try:
            history_path = f"qr_face_2fa/auth_history/{user_id}.json"
            
            # Load existing history
            history = []
            if os.path.exists(history_path):
                with open(history_path, 'r') as f:
                    history = json.load(f)
            
            # Add new result
            history.append(auth_result)
            
            # Save history
            with open(history_path, 'w') as f:
                json.dump(history, f, indent=2)
                
            logger.info(f"Saved authentication history for user {user_id}")
                
        except Exception as e:
            logger.error(f"Error saving authentication history for user {user_id}: {str(e)}")


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="QR Face 2FA System")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Register command
    register_parser = subparsers.add_parser("register", help="Register a new user")
    register_parser.add_argument("--user", required=True, help="User ID")
    register_parser.add_argument("--image", required=True, help="Path to face image")
    register_parser.add_argument("--size", type=int, default=24, help="Image size in pixels")
    register_parser.add_argument("--quality", type=int, default=50, help="JPEG quality (1-95)")
    
    # Verify command
    verify_parser = subparsers.add_parser("verify", help="Verify a user")
    verify_parser.add_argument("--image", required=True, help="Path to face image or QR code")
    verify_parser.add_argument("--tolerance", type=float, default=0.2, help="Similarity tolerance (0-1)")
    
    args = parser.parse_args()
    
    # Initialize 2FA system
    system = QRFace2FA()
    
    if args.command == "register":
        # Register user
        result = system.register_user(
            args.user,
            args.image,
            args.size,
            args.quality
        )
        
        if result["success"]:
            print(f"\n✅ User {args.user} registered successfully!")
            print(f"Registration ID: {result['registration_id']}")
            print(f"QR Code: {result['qr_path']}")
            print(f"Blockchain Reference: {result['blockchain_ref']}")
            print(f"Phi-Resonance: {result['phi_resonance']:.6f}")
        else:
            print(f"\n❌ Registration failed: {result['error']}")
            
    elif args.command == "verify":
        # Verify user
        result = system.verify_user(
            args.image,
            args.tolerance
        )
        
        if result["success"]:
            print(f"\n✅ User {result['user_id']} verified successfully!")
            print(f"Similarity: {result['similarity']:.4f}")
            print(f"Phi-Resonance: {result['phi_resonance']:.6f}")
            print(f"Blockchain Verified: {result['blockchain_verified']}")
            
            if "method" in result and result["method"] == "face_matching":
                print("Verification Method: Face Matching")
        else:
            print(f"\n❌ Verification failed: {result.get('error', 'Unknown error')}")
            if "similarity" in result:
                print(f"Similarity: {result['similarity']:.4f}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
