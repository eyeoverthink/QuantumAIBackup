#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Camera Test QR Code Generator

Generates a large, high-contrast QR code with valid JSON content for camera testing.
"""

import os
import json
import qrcode
import uuid

# Create output directory
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_outputs/camera_test_qr")
os.makedirs(output_dir, exist_ok=True)

# Create valid JSON content that matches the expected format
task_data = {
    "task_id": f"test-{uuid.uuid4().hex[:8]}",
    "script": "print('Camera QR Test Successful!')\nprint('Quantum Phi-Harmonic System is working correctly.')\n",
    "input_data": {"test": True}
}

# Convert to JSON
json_data = json.dumps(task_data)
print("QR Code Content:")
print(json_data)

# Generate QR code with maximum error correction and very large size
qr = qrcode.QRCode(
    version=4,  # Larger version for more data
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Highest error correction
    box_size=30,  # Very large boxes for better camera visibility
    border=6,  # Wide border
)
qr.add_data(json_data)
qr.make(fit=True)

# Create an image from the QR Code with high contrast
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
output_path = os.path.join(output_dir, "camera_test_qr.png")
img.save(output_path)

print(f"\nLarge high-contrast camera test QR code generated and saved to: {output_path}")
print("\nCamera Test Instructions:")
print("1. Open the QR code image on your screen at full size")
print("2. Run the camera-based reader:")
print("   python qr_task_worker.py")
print("3. Hold your camera steady facing the screen")
print("4. If successful, you should see 'Camera QR Test Successful!' in the output")
