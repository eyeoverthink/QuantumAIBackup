#!/usr/bin/env python3
"""
QR Face 2FA Security System Test

This script tests the QR Face 2FA Security System, including:
1. Security extension functionality
2. Multi-script executor functionality
3. End-to-end workflow with face authentication and script execution

The test follows the 'lego' modular design principle and validates the system's
security, encryption, and execution capabilities.
"""

import os
import sys
import time
import json
import base64
import tempfile
import unittest
from pathlib import Path
from typing import Dict, List, Any

# Import the security extension and multi-script executor
from qr_face_2fa_security_extension import QRFace2FASecurityExtension
from qr_multi_script_executor import QRMultiScriptExecutor

# For face image simulation
from PIL import Image, ImageDraw
import io
import numpy as np

# For QR code generation and reading
import qrcode
from pyzbar.pyzbar import decode


class TestQRFace2FASecurity(unittest.TestCase):
    """Test suite for QR Face 2FA Security System"""
    
    def setUp(self):
        """Set up test environment"""
        # Create temporary directories
        self.temp_dir = tempfile.mkdtemp(prefix="qr_face_2fa_test_")
        self.keys_dir = os.path.join(self.temp_dir, "keys")
        self.data_dir = os.path.join(self.temp_dir, "data")
        self.scripts_dir = os.path.join(self.temp_dir, "scripts")
        self.output_dir = os.path.join(self.temp_dir, "output")
        
        # Create directories
        os.makedirs(self.keys_dir, exist_ok=True)
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.scripts_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize security extension
        self.security_extension = QRFace2FASecurityExtension(
            base_dir=self.temp_dir,
            generate_keys=True
        )
        
        # Initialize multi-script executor
        self.script_executor = QRMultiScriptExecutor(
            security_extension=self.security_extension,
            base_dir=self.temp_dir
        )
        
        # Create test face images
        self.face_image_path = os.path.join(self.data_dir, "test_face.jpg")
        self.create_test_face_image(self.face_image_path)
        
        # Create test scripts
        self.test_scripts = [
            {
                "type": "python",
                "name": "hello_world",
                "content": "print('Hello, World!')\nprint('Test script executed successfully')\n"
            },
            {
                "type": "shell",
                "name": "echo_test",
                "content": "#!/bin/bash\necho 'Shell script test'\necho 'Current directory:' $(pwd)\n"
            }
        ]
    
    def tearDown(self):
        """Clean up test environment"""
        # Remove temporary directory and its contents
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def create_test_face_image(self, path: str, size: tuple = (128, 128)):
        """Create a test face image"""
        # Create a simple face-like image
        img = Image.new('L', size, color=200)
        draw = ImageDraw.Draw(img)
        
        # Draw face outline
        draw.ellipse([(20, 20), (size[0]-20, size[1]-20)], fill=150)
        
        # Draw eyes
        eye_size = size[0] // 8
        draw.ellipse([(size[0]//3-eye_size, size[1]//3-eye_size), 
                      (size[0]//3+eye_size, size[1]//3+eye_size)], fill=50)
        draw.ellipse([(2*size[0]//3-eye_size, size[1]//3-eye_size), 
                      (2*size[0]//3+eye_size, size[1]//3+eye_size)], fill=50)
        
        # Draw mouth
        draw.arc([(size[0]//4, size[1]//2), (3*size[0]//4, 3*size[1]//4)], 
                 start=0, end=180, fill=50, width=3)
        
        # Save image
        img.save(path)
        
        return path
    
    def get_face_image_data(self, path: str) -> bytes:
        """Get face image data from file"""
        with open(path, "rb") as f:
            return f.read()
    
    def test_security_extension_initialization(self):
        """Test security extension initialization"""
        # Check if keys were generated
        self.assertTrue(os.path.exists(os.path.join(self.keys_dir, "private_key.pem")))
        self.assertTrue(os.path.exists(os.path.join(self.keys_dir, "public_key.pem")))
        self.assertTrue(os.path.exists(os.path.join(self.keys_dir, "symmetric_key.key")))
    
    def test_data_encryption_decryption(self):
        """Test data encryption and decryption"""
        # Test data
        test_data = {
            "user_id": "test_user",
            "timestamp": time.time(),
            "message": "This is a test message"
        }
        
        # Encrypt data
        encrypted_data = self.security_extension.encrypt_data(test_data)
        
        # Check encrypted data format
        self.assertIn("encrypted_data", encrypted_data)
        self.assertIn("encryption_type", encrypted_data)
        self.assertIn("timestamp", encrypted_data)
        
        # Decrypt data
        decrypted_data = self.security_extension.decrypt_data(encrypted_data)
        
        # Check decrypted data
        self.assertEqual(decrypted_data["user_id"], test_data["user_id"])
        self.assertEqual(decrypted_data["message"], test_data["message"])
    
    def test_secure_qr_data(self):
        """Test securing and verifying QR data"""
        # Test data
        test_data = {
            "user_id": "test_user",
            "timestamp": time.time(),
            "message": "This is a test message"
        }
        
        # Secure data
        secured_data = self.security_extension.secure_qr_data(test_data)
        
        # Check secured data format
        self.assertIn("data", secured_data)
        self.assertIn("signature", secured_data)
        self.assertIn("hash", secured_data)
        self.assertIn("blockchain_hash", secured_data)
        
        # Verify secured data
        is_valid, data, error_message = self.security_extension.verify_secured_qr_data(secured_data)
        
        # Check verification result
        self.assertTrue(is_valid)
        self.assertEqual(data["user_id"], test_data["user_id"])
        self.assertEqual(data["message"], test_data["message"])
    
    def test_face_image_compression(self):
        """Test face image compression"""
        # Get face image data
        face_image_data = self.get_face_image_data(self.face_image_path)
        
        # Compress face image
        compressed_data = self.security_extension.compress_face_image(face_image_data)
        
        # Check compression result
        self.assertLess(len(compressed_data), len(face_image_data))
        
        # Check that compressed image can be opened
        img = Image.open(io.BytesIO(compressed_data))
        self.assertIsNotNone(img)
    
    def test_face_auth_payload(self):
        """Test face authentication payload creation and verification"""
        # Get face image data
        face_image_data = self.get_face_image_data(self.face_image_path)
        
        # Create face auth payload
        payload = self.security_extension.create_face_auth_payload(
            face_image_data,
            "test_user",
            expiration_minutes=5,
            compress=True,
            encrypt=True
        )
        
        # Check payload format
        self.assertIn("data", payload)
        self.assertIn("signature", payload)
        self.assertIn("hash", payload)
        
        # Check payload data
        self.assertEqual(payload["data"]["task_type"], "face_authentication")
        self.assertEqual(payload["data"]["user_id"], "test_user")
        self.assertIn("face_data_encrypted", payload["data"])
        
        # Verify face authentication
        is_valid, error_message = self.security_extension.verify_face_auth(payload, face_image_data)
        
        # Check verification result
        self.assertTrue(is_valid)
    
    def test_multi_script_payload(self):
        """Test multi-script payload creation and extraction"""
        # Create multi-script payload
        payload = self.security_extension.create_multi_script_payload(
            self.test_scripts,
            "test_user",
            expiration_minutes=5,
            encrypt=True
        )
        
        # Check payload format
        self.assertIn("data", payload)
        self.assertIn("signature", payload)
        self.assertIn("hash", payload)
        
        # Check payload data
        self.assertEqual(payload["data"]["task_type"], "multi_script_execution")
        self.assertEqual(payload["data"]["user_id"], "test_user")
        self.assertEqual(payload["data"]["script_count"], len(self.test_scripts))
        
        # Extract scripts from payload
        is_valid, scripts, error_message = self.security_extension.get_scripts_from_payload(payload)
        
        # Check extraction result
        self.assertTrue(is_valid)
        self.assertEqual(len(scripts), len(self.test_scripts))
        self.assertEqual(scripts[0]["name"], self.test_scripts[0]["name"])
        self.assertEqual(scripts[1]["name"], self.test_scripts[1]["name"])
    
    def test_phi_harmonic_timestamp(self):
        """Test phi-harmonic timestamp generation and verification"""
        # Generate phi-harmonic timestamp
        phi_timestamp = self.security_extension.generate_phi_harmonic_timestamp()
        
        # Verify recent timestamp
        self.assertTrue(self.security_extension.verify_phi_harmonic_timestamp(phi_timestamp, max_age_minutes=1))
        
        # Verify expired timestamp
        expired_timestamp = phi_timestamp - (10 * 60 * ((1 + 5 ** 0.5) / 2))  # 10 minutes ago in phi-time
        self.assertFalse(self.security_extension.verify_phi_harmonic_timestamp(expired_timestamp, max_age_minutes=5))
    
    def test_phi_resonance(self):
        """Test phi resonance calculation"""
        # Calculate resonance for a known value
        resonance = self.security_extension.calculate_phi_resonance(1.0)
        expected_resonance = ((1 + 5 ** 0.5) / 2) % 1
        self.assertAlmostEqual(resonance, expected_resonance)
        
        # Test resonance check
        self.assertTrue(self.security_extension.is_phi_resonant(1.0, threshold=0.62))
        self.assertFalse(self.security_extension.is_phi_resonant(1.0, threshold=0.01))
    
    def test_qr_code_creation(self):
        """Test QR code creation for multi-script execution"""
        # Create QR code
        qr_path = os.path.join(self.output_dir, "test_qr.png")
        self.script_executor.create_qr_code(
            self.test_scripts,
            "test_user",
            qr_path,
            expiration_minutes=5,
            encrypt=True
        )
        
        # Check if QR code was created
        self.assertTrue(os.path.exists(qr_path))
        
        # Read QR code
        img = Image.open(qr_path)
        decoded = decode(img)
        
        # Check if QR code contains data
        self.assertTrue(len(decoded) > 0)
        
        # Parse QR data
        qr_data = json.loads(decoded[0].data.decode('utf-8'))
        
        # Check QR data format
        self.assertIn("data", qr_data)
        self.assertIn("signature", qr_data)
        self.assertIn("hash", qr_data)
    
    def test_script_execution(self):
        """Test script execution from QR data"""
        # Create multi-script payload
        payload = self.security_extension.create_multi_script_payload(
            self.test_scripts,
            "test_user",
            expiration_minutes=5,
            encrypt=True
        )
        
        # Execute scripts from payload
        result = self.script_executor.execute_from_qr_data(payload)
        
        # Check execution result
        self.assertTrue(result["success"])
        self.assertEqual(len(result["results"]), len(self.test_scripts))
        
        # Check individual script results
        self.assertTrue(result["results"][0]["success"])
        self.assertTrue("Hello, World!" in result["results"][0]["stdout"])
        self.assertTrue(result["results"][1]["success"])
        self.assertTrue("Shell script test" in result["results"][1]["stdout"])
    
    def test_script_security_validation(self):
        """Test script security validation"""
        # Test safe script
        safe_script = "print('Hello, World!')"
        is_valid, _ = self.script_executor.validate_script_security(safe_script, "python")
        self.assertTrue(is_valid)
        
        # Test dangerous script
        dangerous_script = "import os\nos.system('rm -rf /')"
        is_valid, error = self.script_executor.validate_script_security(dangerous_script, "python")
        self.assertFalse(is_valid)
        self.assertTrue("Dangerous pattern" in error)
    
    def test_end_to_end_workflow(self):
        """Test end-to-end workflow with face authentication and script execution"""
        # Get face image data
        face_image_data = self.get_face_image_data(self.face_image_path)
        
        # Step 1: Create face auth payload
        face_auth_payload = self.security_extension.create_face_auth_payload(
            face_image_data,
            "test_user",
            expiration_minutes=5,
            compress=True,
            encrypt=True
        )
        
        # Step 2: Verify face authentication
        is_valid, error_message = self.security_extension.verify_face_auth(face_auth_payload, face_image_data)
        self.assertTrue(is_valid)
        
        # Step 3: Create multi-script payload
        script_payload = self.security_extension.create_multi_script_payload(
            self.test_scripts,
            "test_user",
            expiration_minutes=5,
            encrypt=True
        )
        
        # Step 4: Create QR code
        qr_path = os.path.join(self.output_dir, "end_to_end_test.png")
        self.script_executor.create_qr_code(
            self.test_scripts,
            "test_user",
            qr_path,
            expiration_minutes=5,
            encrypt=True
        )
        
        # Step 5: Execute scripts from QR code
        # (Simulating QR code reading by directly using the payload)
        result = self.script_executor.execute_from_qr_data(script_payload)
        
        # Check execution result
        self.assertTrue(result["success"])
        self.assertEqual(len(result["results"]), len(self.test_scripts))
        
        # Print summary
        print("\nEnd-to-End Workflow Test Summary:")
        print(f"- Face Authentication: {'Success' if is_valid else 'Failed'}")
        print(f"- QR Code Created: {os.path.exists(qr_path)}")
        print(f"- Scripts Executed: {len(result['results'])}")
        print(f"- Overall Success: {result['success']}")


if __name__ == "__main__":
    unittest.main()
