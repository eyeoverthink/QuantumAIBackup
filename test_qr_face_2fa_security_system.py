#!/usr/bin/env python3
"""
Test QR Face 2FA Security System

This script tests the integration of the QR Face 2FA Security Extension with the Multi-Script Executor.
It validates:
1. Face image encoding with security features
2. Multi-script QR code generation and execution
3. End-to-end security verification

The system follows the 'lego' modular design principle.
"""

import os
import sys
import json
import time
import base64
import argparse
import tempfile
from pathlib import Path
from PIL import Image

# Import our modules
from qr_face_2fa_security_extension import QRFace2FASecurityExtension
from qr_multi_script_executor import QRMultiScriptExecutor

# Constants
TEST_DIR = "test_qr_face_2fa_security"
TEST_FACE_IMAGE = "test_face.jpg"
TEST_QR_OUTPUT = "test_secured_qr.png"
TEST_SCRIPT_QR_OUTPUT = "test_script_qr.png"
TEST_RESULTS_FILE = "test_results.json"

def setup_test_environment():
    """Set up test environment"""
    print("[+] Setting up test environment...")
    
    # Create test directory
    os.makedirs(TEST_DIR, exist_ok=True)
    
    # Check if we have a test face image
    if not os.path.exists(os.path.join(TEST_DIR, TEST_FACE_IMAGE)):
        print("[!] Test face image not found. Creating a placeholder image...")
        # Create a simple placeholder image (gray square)
        img = Image.new('L', (64, 64), 128)
        img.save(os.path.join(TEST_DIR, TEST_FACE_IMAGE))
    
    print("[+] Test environment ready")
    return os.path.join(TEST_DIR, TEST_FACE_IMAGE)

def test_security_extension():
    """Test QR Face 2FA Security Extension"""
    print("\n[+] Testing QR Face 2FA Security Extension...")
    
    # Initialize security extension
    security_extension = QRFace2FASecurityExtension(
        base_dir=os.path.join(TEST_DIR, "security_extension"),
        generate_keys=True
    )
    
    # Test key generation
    if os.path.exists(os.path.join(TEST_DIR, "security_extension", "keys", "private_key.pem")) and \
       os.path.exists(os.path.join(TEST_DIR, "security_extension", "keys", "public_key.pem")):
        print("[✓] Key generation successful")
    else:
        print("[✗] Key generation failed")
        return False
    
    # Test data encryption/decryption
    test_data = {"test": "data", "value": 123}
    
    try:
        encrypted_data = security_extension.encrypt_data(test_data)
        decrypted_data = security_extension.decrypt_data(encrypted_data)
        
        if decrypted_data == test_data:
            print("[✓] Encryption/decryption successful")
        else:
            print("[✗] Encryption/decryption failed")
            return False
    except Exception as e:
        print(f"[✗] Encryption/decryption error: {str(e)}")
        return False
    
    # Test QR data security
    try:
        test_qr_data = {
            "task_type": "test",
            "user_id": "test_user",
            "timestamp": time.time()
        }
        
        secured_data = security_extension.secure_qr_data(test_qr_data)
        is_valid, payload, error_message = security_extension.verify_secured_qr_data(secured_data)
        
        if is_valid and payload["task_type"] == "test":
            print("[✓] QR data security successful")
        else:
            print(f"[✗] QR data security failed: {error_message}")
            return False
    except Exception as e:
        print(f"[✗] QR data security error: {str(e)}")
        return False
    
    print("[+] Security Extension tests passed")
    return security_extension

def test_face_auth_payload(security_extension):
    """Test face authentication payload creation"""
    print("\n[+] Testing face authentication payload creation...")
    
    # Read test face image
    face_image_path = os.path.join(TEST_DIR, TEST_FACE_IMAGE)
    with open(face_image_path, "rb") as f:
        face_image_data = f.read()
    
    # Create face authentication payload
    try:
        face_auth_payload = security_extension.create_face_auth_payload(
            face_image_data,
            "test_user",
            expiration_minutes=5,
            encrypt=True
        )
        
        # Verify payload
        is_valid, payload, error_message = security_extension.verify_secured_qr_data(face_auth_payload)
        
        if is_valid and payload["task_type"] == "face_authentication":
            print("[✓] Face authentication payload creation successful")
        else:
            print(f"[✗] Face authentication payload verification failed: {error_message}")
            return False
    except Exception as e:
        print(f"[✗] Face authentication payload error: {str(e)}")
        return False
    
    print("[+] Face authentication payload tests passed")
    return face_auth_payload

def test_multi_script_payload(security_extension):
    """Test multi-script payload creation"""
    print("\n[+] Testing multi-script payload creation...")
    
    # Create test scripts
    test_scripts = [
        {
            "type": "python",
            "name": "hello_script",
            "content": "print('Hello from Python script!')"
        },
        {
            "type": "shell",
            "name": "system_info",
            "content": "echo 'System information:' && uname -a"
        }
    ]
    
    # Create multi-script payload
    try:
        multi_script_payload = security_extension.create_multi_script_payload(
            test_scripts,
            user_id="test_user",
            expiration_minutes=5,
            encrypt=True
        )
        
        # Save payload to file for debugging
        with open(os.path.join(TEST_DIR, "multi_script_payload.json"), "w") as f:
            json.dump(multi_script_payload, f, indent=2)
        
        # Verify payload
        is_valid, payload, error_message = security_extension.verify_secured_qr_data(multi_script_payload)
        
        if is_valid and payload["task_type"] == "multi_script_execution":
            print("[✓] Multi-script payload creation successful")
        else:
            print(f"[✗] Multi-script payload verification failed: {error_message}")
            return False
    except Exception as e:
        print(f"[✗] Multi-script payload error: {str(e)}")
        return False
    
    print("[+] Multi-script payload tests passed")
    return multi_script_payload, test_scripts

def test_multi_script_executor(security_extension, multi_script_payload, test_scripts):
    """Test multi-script executor"""
    print("\n[+] Testing multi-script executor...")
    
    # Initialize executor
    executor = QRMultiScriptExecutor(
        security_extension=security_extension,
        base_dir=os.path.join(TEST_DIR, "multi_script_executor")
    )
    
    # Test script execution
    try:
        # Execute scripts directly
        results = executor._execute_scripts(test_scripts, "test_user")
        
        if results["success"]:
            print("[✓] Direct script execution successful")
        else:
            print("[✗] Direct script execution failed")
            return False
        
        # Execute scripts from payload
        results = executor.execute_from_qr_data(multi_script_payload)
        
        if results["success"]:
            print("[✓] Script execution from payload successful")
        else:
            print(f"[✗] Script execution from payload failed: {results.get('error', 'Unknown error')}")
            return False
        
        # Save results for inspection
        with open(os.path.join(TEST_DIR, TEST_RESULTS_FILE), "w") as f:
            json.dump(results, f, indent=2)
        
        print(f"[+] Execution results saved to {os.path.join(TEST_DIR, TEST_RESULTS_FILE)}")
    except Exception as e:
        print(f"[✗] Script execution error: {str(e)}")
        return False
    
    print("[+] Multi-script executor tests passed")
    return True

def create_qr_code_from_payload(payload, output_path):
    """Create QR code from payload"""
    print(f"\n[+] Creating QR code at {output_path}...")
    
    try:
        import qrcode
        
        # Convert payload to JSON
        payload_json = json.dumps(payload)
        
        # Create QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(payload_json)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_path)
        
        print(f"[✓] QR code created at {output_path}")
        return True
    except Exception as e:
        print(f"[✗] QR code creation error: {str(e)}")
        return False

def test_qr_code_execution(security_extension, executor, qr_path):
    """Test QR code execution"""
    print(f"\n[+] Testing QR code execution from {qr_path}...")
    
    try:
        # Execute scripts from QR code
        results = executor.execute_from_qr_image(qr_path)
        
        if results["success"]:
            print("[✓] QR code execution successful")
        else:
            print(f"[✗] QR code execution failed: {results.get('error', 'Unknown error')}")
            return False
        
        # Save results for inspection
        with open(os.path.join(TEST_DIR, "qr_execution_results.json"), "w") as f:
            json.dump(results, f, indent=2)
        
        print(f"[+] QR execution results saved to {os.path.join(TEST_DIR, 'qr_execution_results.json')}")
    except Exception as e:
        print(f"[✗] QR code execution error: {str(e)}")
        return False
    
    print("[+] QR code execution tests passed")
    return True

def test_end_to_end_workflow():
    """Test end-to-end workflow"""
    print("\n[+] Testing end-to-end workflow...")
    
    # Setup test environment
    setup_test_environment()
    
    # Test security extension
    security_extension = test_security_extension()
    if not security_extension:
        return False
    
    # Test face authentication payload
    face_auth_payload = test_face_auth_payload(security_extension)
    if not face_auth_payload:
        return False
    
    # Test multi-script payload
    multi_script_result = test_multi_script_payload(security_extension)
    if not multi_script_result:
        return False
    
    multi_script_payload, test_scripts = multi_script_result
    
    # Test multi-script executor
    executor = QRMultiScriptExecutor(
        security_extension=security_extension,
        base_dir=os.path.join(TEST_DIR, "multi_script_executor")
    )
    
    if not test_multi_script_executor(security_extension, multi_script_payload, test_scripts):
        return False
    
    # Create QR code from multi-script payload
    qr_path = os.path.join(TEST_DIR, TEST_SCRIPT_QR_OUTPUT)
    if not create_qr_code_from_payload(multi_script_payload, qr_path):
        return False
    
    # Test QR code execution
    if not test_qr_code_execution(security_extension, executor, qr_path):
        return False
    
    print("\n[✓] End-to-end workflow tests passed")
    return True

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Test QR Face 2FA Security System")
    parser.add_argument("--clean", action="store_true", help="Clean test directory before running tests")
    
    args = parser.parse_args()
    
    # Clean test directory if requested
    if args.clean and os.path.exists(TEST_DIR):
        print(f"[+] Cleaning test directory {TEST_DIR}...")
        import shutil
        shutil.rmtree(TEST_DIR)
    
    # Run tests
    if test_end_to_end_workflow():
        print("\n[✓] All tests passed")
        return 0
    else:
        print("\n[✗] Tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
