#!/usr/bin/env python3
"""
Face QR System Test Script

This script tests the end-to-end functionality of the Face-QR 2FA Security System.
It validates the face image encoding into QR codes and decoding process.

It follows the 'lego' design principle, using modular components to test the system.
"""

import os
import sys
import json
import uuid
import time
import argparse
import tempfile
import numpy as np
from typing import Dict, Any, List, Tuple, Optional
from PIL import Image

# Import OpenCV extension to activate face detection
import face_qr_recognition_extension
import qrcode
import base64
import io
import zlib
import numpy as np

# Import Face-QR modules
from face_qr_core import FaceQRBase, FaceQRConfig, PHI
from face_qr_security import FaceQRSecurity
from face_qr_recognition import FaceQRRecognition

# Import the QR task worker extension
try:
    from qr_task_worker_extension import handle_display_face_image
except ImportError:
    print("Warning: qr_task_worker_extension not found. Some tests may fail.")
    handle_display_face_image = None

# Import the QR generator
try:
    from generate_face_qr import encode_face_to_qr
except ImportError:
    print("Warning: generate_face_qr not found. Some tests may fail.")
    encode_face_to_qr = None


class FaceQRSystemTest(FaceQRBase):
    """
    Test class for the Face-QR system.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize the test class.
        
        Args:
            config_path: Path to configuration file
        """
        super().__init__()
        self.config = FaceQRConfig(config_path)
        
        # Create test directory
        self.test_dir = os.path.join(self.base_dir, "test_output")
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Initialize components
        self.security = FaceQRSecurity(config_path)
        self.recognition = FaceQRRecognition(config_path)
        
        # Test status
        self.tests_run = 0
        self.tests_passed = 0
        self.tests_failed = 0
    
    def run_all_tests(self, image_path: str) -> bool:
        """
        Run all tests.
        
        Args:
            image_path: Path to test image
            
        Returns:
            bool: True if all tests passed
        """
        print("\n===== Face-QR System Test =====")
        print(f"Test image: {image_path}")
        print("=" * 30)
        
        # Load test image
        try:
            with open(image_path, "rb") as f:
                image_data = f.read()
            
            print(f"Loaded test image: {len(image_data)} bytes")
        except Exception as e:
            print(f"Error loading test image: {e}")
            return False
        
        # Run tests
        self.test_core_functionality()
        self.test_security_module()
        self.test_recognition_module(image_data)
        self.test_qr_generation(image_path)
        self.test_qr_decoding()
        self.test_end_to_end(image_path)
        
        # Print summary
        print("\n===== Test Summary =====")
        print(f"Tests run: {self.tests_run}")
        print(f"Tests passed: {self.tests_passed}")
        print(f"Tests failed: {self.tests_failed}")
        
        return self.tests_failed == 0
    
    def assert_test(self, condition: bool, test_name: str) -> bool:
        """
        Assert test condition and update test status.
        
        Args:
            condition: Test condition
            test_name: Test name
            
        Returns:
            bool: Test result
        """
        self.tests_run += 1
        
        if condition:
            print(f"✅ PASS: {test_name}")
            self.tests_passed += 1
            return True
        else:
            print(f"❌ FAIL: {test_name}")
            self.tests_failed += 1
            return False
    
    def test_core_functionality(self) -> None:
        """
        Test core functionality.
        """
        print("\n----- Testing Core Functionality -----")
        
        # Test base64 encoding/decoding
        test_data = b"Hello, World!"
        encoded = self.encode_base64(test_data)
        decoded = self.decode_base64(encoded)
        self.assert_test(decoded == test_data, "Base64 encoding/decoding")
        
        # Test hash calculation
        hash_value = self.calculate_hash(test_data)
        self.assert_test(len(hash_value) == 64, "Hash calculation")
        
        # Test phi timestamp
        phi_timestamp = self.get_phi_timestamp()
        current_time = time.time()
        self.assert_test(abs(phi_timestamp / PHI - current_time) < 0.1, "Phi timestamp")
        
        # Test configuration
        image_size = self.config.get("image", "size")
        self.assert_test(isinstance(image_size, int), "Configuration type conversion")
        
        # Test JSON save/load
        test_data = {"test": "data", "phi": PHI}
        self.save_json(test_data, "test_data.json")
        loaded_data = self.load_json("test_data.json")
        self.assert_test(loaded_data and loaded_data["test"] == "data", "JSON save/load")
    
    def test_security_module(self) -> None:
        """
        Test security module.
        """
        print("\n----- Testing Security Module -----")
        
        # Test key generation
        self.assert_test(self.security.generate_key_pair(), "Key pair generation")
        
        # Test signing and verification
        test_data = b"Test data for signing"
        signature = self.security.sign_data(test_data)
        self.assert_test(signature is not None, "Data signing")
        
        # Verify signature
        is_valid = self.security.verify_signature(test_data, signature)
        self.assert_test(is_valid, "Signature verification (valid)")
        
        # Test with modified data
        is_valid = self.security.verify_signature(b"Modified data", signature)
        self.assert_test(not is_valid, "Signature verification (invalid)")
        
        # Test encryption and decryption
        encryption_result = self.security.encrypt_data(b"Secret data")
        self.assert_test(encryption_result["success"], "Data encryption")
        
        # Decrypt data
        decryption_result = self.security.decrypt_data(
            encryption_result["encrypted_data"],
            encryption_result["key"]
        )
        self.assert_test(
            decryption_result["success"] and 
            decryption_result["decrypted_data"] == b"Secret data",
            "Data decryption"
        )
    
    def test_recognition_module(self, image_data: bytes) -> None:
        """
        Test recognition module.
        
        Args:
            image_data: Test image data
        """
        print("\n----- Testing Recognition Module -----")
        
        # Test face detection
        faces = self.recognition.detect_faces(image_data)
        self.assert_test(len(faces) > 0, "Face detection")
        
        if len(faces) > 0:
            # Test feature extraction
            features = self.recognition.extract_features(faces[0])
            self.assert_test(len(features) > 0, "Feature extraction")
            
            # Test face comparison (same face)
            similarity = self.recognition.compare_faces(faces[0], faces[0])
            self.assert_test(similarity > 0.9, "Face comparison (same face)")
            
            # Test face verification
            is_match, similarity = self.recognition.verify_face(image_data, image_data)
            self.assert_test(is_match, "Face verification")
            
            # Test face hash
            face_hash = self.recognition.hash_face(image_data)
            self.assert_test(len(face_hash) == 64, "Face hash generation")
    
    def test_qr_generation(self, image_path: str) -> None:
        """
        Test QR code generation.
        
        Args:
            image_path: Path to test image
        """
        print("\n----- Testing QR Generation -----")
        
        # Skip if encode_face_to_qr is not available
        if encode_face_to_qr is None:
            print("Skipping QR generation test (generate_face_qr not found)")
            return
        
        # Generate QR code
        qr_output_path = os.path.join(self.test_dir, "test_qr.png")
        
        try:
            # Try different optimization settings
            for size in [24, 16, 12]:
                for quality in [50, 40, 30]:
                    try:
                        print(f"Trying size={size}, quality={quality}...")
                        result = encode_face_to_qr(
                            image_path, 
                            qr_output_path,
                            size_px=size,
                            jpeg_quality=quality
                        )
                        
                        if result:
                            print(f"Successfully generated QR with size={size}, quality={quality}")
                            self.assert_test(os.path.exists(qr_output_path), "QR code generation")
                            return
                    except Exception as e:
                        print(f"Failed with size={size}, quality={quality}: {e}")
            
            # If we get here, all attempts failed
            self.assert_test(False, "QR code generation (all attempts failed)")
            
        except Exception as e:
            print(f"Error in QR generation test: {e}")
            self.assert_test(False, "QR code generation")
    
    def test_qr_decoding(self) -> None:
        """
        Test QR code decoding.
        """
        print("\n----- Testing QR Decoding -----")
        
        # Skip if handle_display_face_image is not available
        if handle_display_face_image is None:
            print("Skipping QR decoding test (qr_task_worker_extension not found)")
            return
        
        # Check if QR code was generated
        qr_path = os.path.join(self.test_dir, "test_qr.png")
        if not os.path.exists(qr_path):
            print("Skipping QR decoding test (QR code not generated)")
            return
        
        try:
            # Read QR code
            qr_img = Image.open(qr_path)
            
            # Create a temporary directory for output
            with tempfile.TemporaryDirectory() as temp_dir:
                # Create a mock task object
                task = {
                    "output_dir": temp_dir
                }
                
                # Decode QR code
                from pyzbar.pyzbar import decode
                decoded = decode(qr_img)
                
                if not decoded:
                    self.assert_test(False, "QR code decoding (no data found)")
                    return
                
                # Parse payload
                payload = json.loads(decoded[0].data.decode('utf-8'))
                
                # Check if payload has nested task_data structure
                if "task_data" in payload and isinstance(payload["task_data"], dict):
                    task_data = payload["task_data"]
                else:
                    task_data = payload
                    
                self.assert_test("task_type" in task_data, "QR payload structure")
                self.assert_test(task_data["task_type"] == "display_face_image", "QR task type")
                
                # Handle task - function returns boolean success status, not path
                success = handle_display_face_image(task_data["task_id"], task_data)
                self.assert_test(success, "QR task handling")
                
                # Look for the decoded image file in the current directory
                # The filename format is: decoded_face_{task_id}_{timestamp}.png
                decoded_files = [f for f in os.listdir('.') if f.startswith(f"decoded_face_{task_data['task_id']}")]
                
                if decoded_files:
                    # Use the first matching file
                    decoded_path = decoded_files[0]
                    decoded_img = Image.open(decoded_path)
                    self.assert_test(decoded_img.width > 0 and decoded_img.height > 0, "Decoded image validity")
                else:
                    self.assert_test(False, "Finding decoded image file")
        
        except Exception as e:
            print(f"Error in QR decoding test: {e}")
            self.assert_test(False, "QR code decoding")
    
    def test_end_to_end(self, image_path: str) -> None:
        """
        Test end-to-end workflow.
        
        Args:
            image_path: Path to test image
        """
        print("\n----- Testing End-to-End Workflow -----")
        
        # Skip if required components are not available
        if encode_face_to_qr is None or handle_display_face_image is None:
            print("Skipping end-to-end test (required components not found)")
            return
        
        try:
            # 1. Load original image
            original_img = Image.open(image_path)
            
            # 2. Generate QR code
            qr_path = os.path.join(self.test_dir, "e2e_qr.png")
            
            # Try different optimization settings
            success = False
            for size in [24, 16, 12]:
                for quality in [50, 40, 30]:
                    try:
                        print(f"Trying size={size}, quality={quality}...")
                        result = encode_face_to_qr(
                            image_path, 
                            qr_path,
                            size_px=size,
                            jpeg_quality=quality
                        )
                        
                        if result:
                            print(f"Successfully generated QR with size={size}, quality={quality}")
                            success = True
                            break
                    except Exception as e:
                        print(f"Failed with size={size}, quality={quality}: {e}")
                
                if success:
                    break
            
            if not success:
                self.assert_test(False, "End-to-end QR generation")
                return
            
            # 3. Decode QR code
            qr_img = Image.open(qr_path)
            
            # Create a temporary directory for output
            with tempfile.TemporaryDirectory() as temp_dir:
                # Create a mock task object
                task = {
                    "output_dir": temp_dir
                }
                
                # Decode QR code
                from pyzbar.pyzbar import decode
                decoded = decode(qr_img)
                
                if not decoded:
                    self.assert_test(False, "End-to-end QR decoding (no data found)")
                    return
                
                # Parse payload
                payload = json.loads(decoded[0].data.decode('utf-8'))
                
                # Check if payload has nested task_data structure
                if "task_data" in payload and isinstance(payload["task_data"], dict):
                    task_data = payload["task_data"]
                else:
                    task_data = payload
                    
                # Handle task - function returns boolean success status, not path
                success = handle_display_face_image(task_data["task_id"], task_data)
                
                if not success:
                    self.assert_test(False, "End-to-end image reconstruction")
                    return
                    
                # Look for the decoded image file in the current directory
                # The filename format is: decoded_face_{task_id}_{timestamp}.png
                decoded_files = [f for f in os.listdir('.') if f.startswith(f"decoded_face_{task_data['task_id']}")]
                
                if not decoded_files:
                    self.assert_test(False, "Finding decoded image file")
                    return
                    
                # 4. Load reconstructed image
                decoded_path = decoded_files[0]
                reconstructed_img = Image.open(decoded_path)
                
                # 5. Verify using face recognition
                with open(image_path, "rb") as f:
                    original_data = f.read()
                
                with open(decoded_path, "rb") as f:
                    reconstructed_data = f.read()
                
                is_match, similarity = self.recognition.verify_face(
                    original_data, 
                    reconstructed_data,
                    threshold=0.5  # Lower threshold due to compression
                )
                
                self.assert_test(is_match, f"End-to-end face verification (similarity: {similarity:.4f})")
                
                # 6. Test with security module
                auth_payload = self.security.create_face_auth_payload(
                    original_data,
                    "test_user",
                    expiration_minutes=5
                )
                
                self.assert_test(auth_payload["success"], "End-to-end auth payload creation")
                
                if auth_payload["success"]:
                    # Verify authentication
                    is_valid, message = self.security.verify_face_auth(
                        auth_payload,
                        reconstructed_data
                    )
                    
                    self.assert_test(is_valid, f"End-to-end auth verification: {message}")
        
        except Exception as e:
            print(f"Error in end-to-end test: {e}")
            self.assert_test(False, f"End-to-end workflow: {e}")


def main():
    """
    Main function.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Test Face-QR system")
    parser.add_argument("--image", "-i", required=True, help="Path to test image")
    parser.add_argument("--config", "-c", help="Path to configuration file")
    args = parser.parse_args()
    
    # Check if image exists
    if not os.path.exists(args.image):
        print(f"Error: Image not found: {args.image}")
        return 1
    
    # Run tests
    test = FaceQRSystemTest(args.config)
    success = test.run_all_tests(args.image)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
