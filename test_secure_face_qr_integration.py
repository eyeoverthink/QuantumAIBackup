#!/usr/bin/env python3
"""
Test Secure Face QR Integration

This script demonstrates the integration of:
1. The existing Face-QR system
2. The QR Face 2FA Security System
3. Enhanced face recognition with OpenCV

It performs a complete end-to-end test workflow:
1. Train face recognition with sample images
2. Generate a secure QR code from a face image
3. Verify the QR code with a live face image
4. Execute scripts from a secure QR code (if applicable)
"""

import os
import sys
import argparse
import time
import json
import subprocess
import shutil
from pathlib import Path

# Import the integration module
from secure_face_qr_integration import SecureFaceQRIntegration
from qr_face_2fa_security_extension import QRFace2FASecurityExtension

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio

def run_command(command, description=None):
    """Run a command and print its output"""
    if description:
        print(f"\n[+] {description}...")
    
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.stdout:
        print(f"--- Output ---\n{result.stdout}")
    
    if result.returncode != 0:
        print(f"Error (code {result.returncode}):\n{result.stderr}")
        return False
    
    return True

def create_test_directories():
    """Create directories for test files"""
    test_dir = os.path.join(os.getcwd(), "secure_face_qr_test")
    images_dir = os.path.join(test_dir, "images")
    qr_dir = os.path.join(test_dir, "qr_codes")
    results_dir = os.path.join(test_dir, "results")
    
    # Create directories
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(qr_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)
    
    return test_dir, images_dir, qr_dir, results_dir

def copy_sample_images(source_dir, target_dir):
    """Copy sample images to test directory"""
    print(f"\n[+] Copying sample images from {source_dir} to {target_dir}...")
    
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"[!] Source directory {source_dir} not found")
        return []
    
    # Find image files
    image_files = []
    for ext in [".jpg", ".jpeg", ".png"]:
        image_files.extend(list(Path(source_dir).glob(f"*{ext}")))
    
    if not image_files:
        print(f"[!] No image files found in {source_dir}")
        return []
    
    # Copy files
    copied_files = []
    for img_path in image_files:
        target_path = os.path.join(target_dir, os.path.basename(img_path))
        shutil.copy2(img_path, target_path)
        copied_files.append(target_path)
        print(f"    Copied: {os.path.basename(img_path)}")
    
    return copied_files

def test_face_recognition_training(integration, images, user_id="test_user"):
    """Test face recognition training"""
    print("\n" + "="*80)
    print(f"FACE RECOGNITION TRAINING TEST - {time.time() * PHI}")
    print("="*80)
    
    # Train face recognition
    success = integration.train_user_face(user_id, images, num_variations=5)
    
    if success:
        print(f"[+] Successfully trained face recognition for user {user_id}")
    else:
        print(f"[!] Failed to train face recognition for user {user_id}")
    
    return success

def test_secure_qr_generation(integration, image_path, output_path, user_id="test_user"):
    """Test secure QR code generation"""
    print("\n" + "="*80)
    print(f"SECURE QR CODE GENERATION TEST - {time.time() * PHI}")
    print("="*80)
    
    # Generate secure QR code
    success = integration.secure_encode_face_to_qr(
        image_path,
        output_path,
        user_id=user_id,
        size_px=32,
        jpeg_quality=60,
        expiration_minutes=5
    )
    
    if success:
        print(f"[+] Successfully generated secure QR code: {output_path}")
    else:
        print(f"[!] Failed to generate secure QR code")
    
    return success

def test_qr_verification(integration, qr_path, live_face_path=None):
    """Test QR code verification"""
    print("\n" + "="*80)
    print(f"QR CODE VERIFICATION TEST - {time.time() * PHI}")
    print("="*80)
    
    # Verify QR code
    result = integration.verify_secure_face_qr(qr_path, live_face_path)
    
    print(f"[+] Verification result:")
    print(json.dumps(result, indent=2))
    
    return result["success"]

def test_original_face_qr_system(image_path, qr_output):
    """Test the original Face-QR system for comparison"""
    print("\n" + "="*80)
    print(f"ORIGINAL FACE-QR SYSTEM TEST - {time.time() * PHI}")
    print("="*80)
    
    # 1. Generate QR code from the face image using the original system
    generate_cmd = [
        "python", "generate_face_qr.py",
        "--image", image_path,
        "--output", qr_output,
        "--size_px", "32",
        "--jpeg_quality", "60"
    ]
    
    if not run_command(generate_cmd, "Generating QR code with original system"):
        return False
    
    # Check if QR code was generated
    if not os.path.exists(qr_output):
        print(f"Error: QR code was not generated at {qr_output}")
        return False
    
    print(f"\n[+] Successfully generated QR code with original system: {qr_output}")
    
    # 2. Process the QR code with the original worker
    test_runner_content = """#!/usr/bin/env python3
import sys
import os

# Import the QR task worker
import qr_task_worker_from_file

# Import and apply the extension
import qr_task_worker_extension
qr_task_worker_extension.apply_extension()

# Process the QR code image
qr_image_path = sys.argv[1]
print(f"Processing QR code: {qr_image_path}")
qr_task_worker_from_file.process_qr_image_file(qr_image_path)
"""
    
    # Create test runner script
    test_runner_path = "test_qr_runner_temp.py"
    with open(test_runner_path, "w") as f:
        f.write(test_runner_content)
    
    # Make executable
    os.chmod(test_runner_path, 0o755)
    
    # Run the test runner
    run_cmd = ["python", test_runner_path, qr_output]
    success = run_command(run_cmd, "Processing QR code with original worker")
    
    # Clean up
    os.remove(test_runner_path)
    
    return success

def test_end_to_end_workflow(args):
    """Run the complete end-to-end test workflow"""
    print("\n" + "="*80)
    print(f"SECURE FACE QR INTEGRATION - END-TO-END TEST - {time.time() * PHI}")
    print("="*80)
    
    # 1. Create test directories
    test_dir, images_dir, qr_dir, results_dir = create_test_directories()
    print(f"[+] Created test directories in {test_dir}")
    
    # 2. Copy sample images
    if args.sample_dir:
        sample_images = copy_sample_images(args.sample_dir, images_dir)
    else:
        sample_images = []
    
    # If no sample images provided or found, use the specified image
    if not sample_images and args.image:
        if os.path.exists(args.image):
            target_path = os.path.join(images_dir, os.path.basename(args.image))
            shutil.copy2(args.image, target_path)
            sample_images = [target_path]
            print(f"[+] Copied specified image to {target_path}")
        else:
            print(f"[!] Specified image not found: {args.image}")
            return False
    
    if not sample_images:
        print("[!] No sample images available for testing")
        return False
    
    # 3. Initialize the integration
    print("\n[+] Initializing Secure Face QR Integration...")
    integration = SecureFaceQRIntegration(base_dir=os.path.join(test_dir, ".secure_face_qr"))
    
    # 4. Test face recognition training (if multiple images available)
    if len(sample_images) >= 2:
        training_images = sample_images[:-1]  # Use all but the last image for training
        test_face_recognition_training(integration, training_images, user_id=args.user_id)
        
        # Use the last image for verification
        verification_image = sample_images[-1]
    else:
        # If only one image, use it for both
        verification_image = sample_images[0]
    
    # 5. Generate secure QR code
    secure_qr_path = os.path.join(qr_dir, "secure_face_qr.png")
    test_secure_qr_generation(integration, verification_image, secure_qr_path, user_id=args.user_id)
    
    # 6. Test QR verification
    test_qr_verification(integration, secure_qr_path, verification_image)
    
    # 7. Test original Face-QR system for comparison
    original_qr_path = os.path.join(qr_dir, "original_face_qr.png")
    test_original_face_qr_system(verification_image, original_qr_path)
    
    print("\n" + "="*80)
    print(f"TEST SUMMARY - {time.time() * PHI}")
    print("="*80)
    print(f"[+] Test directory: {test_dir}")
    print(f"[+] Secure QR code: {secure_qr_path}")
    print(f"[+] Original QR code: {original_qr_path}")
    print(f"[+] Sample images: {len(sample_images)}")
    print(f"[+] User ID: {args.user_id}")
    print("="*80)
    
    return True

def test_face_recognition_only(args):
    """Test only the face recognition capabilities"""
    print("\n" + "="*80)
    print(f"FACE RECOGNITION TEST - {time.time() * PHI}")
    print("="*80)
    
    # 1. Create test directories
    test_dir, images_dir, qr_dir, results_dir = create_test_directories()
    
    # 2. Copy sample images
    if args.sample_dir:
        sample_images = copy_sample_images(args.sample_dir, images_dir)
    else:
        sample_images = []
    
    # If no sample images provided or found, use the specified image
    if not sample_images and args.image:
        if os.path.exists(args.image):
            target_path = os.path.join(images_dir, os.path.basename(args.image))
            shutil.copy2(args.image, target_path)
            sample_images = [target_path]
        else:
            print(f"[!] Specified image not found: {args.image}")
            return False
    
    if not sample_images:
        print("[!] No sample images available for testing")
        return False
    
    # 3. Initialize the integration
    integration = SecureFaceQRIntegration(base_dir=os.path.join(test_dir, ".secure_face_qr"))
    
    # 4. Test face recognition training
    if len(sample_images) < 2:
        print("[!] At least 2 images are required for face recognition testing")
        return False
    
    # Use all but the last image for training
    training_images = sample_images[:-1]
    test_image = sample_images[-1]
    
    # Train face recognition
    success = test_face_recognition_training(integration, training_images, user_id=args.user_id)
    if not success:
        return False
    
    # Test recognition
    print("\n[+] Testing face recognition with separate image...")
    with open(test_image, "rb") as f:
        test_image_data = f.read()
    
    user_id, confidence = integration.recognize_face(test_image_data)
    
    if user_id:
        print(f"[+] Face recognized as user: {user_id}")
        print(f"[+] Confidence: {confidence}")
        return True
    else:
        print("[!] Face not recognized")
        return False

def test_qr_security_only(args):
    """Test only the QR security capabilities"""
    print("\n" + "="*80)
    print(f"QR SECURITY TEST - {time.time() * PHI}")
    print("="*80)
    
    # 1. Create test directories
    test_dir, images_dir, qr_dir, results_dir = create_test_directories()
    
    # 2. Check if image exists
    if not args.image or not os.path.exists(args.image):
        print(f"[!] Image not found: {args.image}")
        return False
    
    # 3. Initialize the security extension directly
    security = QRFace2FASecurityExtension(generate_keys=True)
    
    # 4. Read the image
    with open(args.image, "rb") as f:
        image_data = f.read()
    
    # 5. Create face authentication payload
    print("\n[+] Creating face authentication payload...")
    payload = security.create_face_auth_payload(
        image_data,
        user_id=args.user_id,
        expiration_minutes=5,
        compress=True,
        encrypt=True
    )
    
    # 6. Verify face authentication
    print("\n[+] Verifying face authentication...")
    is_valid, error_message = security.verify_face_auth(payload, image_data)
    
    if is_valid:
        print("[+] Face authentication successful")
    else:
        print(f"[!] Face authentication failed: {error_message}")
    
    # 7. Create a test script payload
    print("\n[+] Creating test script payload...")
    test_script = {
        "type": "python",
        "name": "hello_world",
        "content": "print('Hello, World from secure QR code!')"
    }
    
    script_payload = security.create_multi_script_payload(
        [test_script],
        user_id=args.user_id,
        expiration_minutes=5,
        encrypt=True
    )
    
    # 8. Get scripts from payload
    print("\n[+] Getting scripts from payload...")
    is_valid, scripts, error = security.get_scripts_from_payload(script_payload)
    
    if is_valid:
        print("[+] Script payload verification successful")
        print(f"[+] Script: {scripts[0]['name']}")
    else:
        print(f"[!] Script payload verification failed: {error}")
    
    return is_valid

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Secure Face QR Integration")
    parser.add_argument("--image", help="Path to a face image")
    parser.add_argument("--sample_dir", help="Directory containing sample face images")
    parser.add_argument("--user_id", default="test_user", help="User ID for testing")
    parser.add_argument("--mode", choices=["full", "face", "qr"], default="full",
                        help="Test mode: full (end-to-end), face (recognition only), or qr (security only)")
    
    args = parser.parse_args()
    
    # Run the selected test mode
    if args.mode == "full":
        test_end_to_end_workflow(args)
    elif args.mode == "face":
        test_face_recognition_only(args)
    elif args.mode == "qr":
        test_qr_security_only(args)
