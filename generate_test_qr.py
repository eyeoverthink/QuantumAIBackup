#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test QR Code Generator

Generates a simple, high-contrast QR code with minimal content for maximum readability.
"""

import os
import qrcode

# Create output directory
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_outputs/test_qr")
os.makedirs(output_dir, exist_ok=True)

# Create extremely simple content - just a short text string
simple_content = "TEST123"
print(f"QR Code Content: {simple_content}")

# Generate QR code with maximum error correction and large size
qr = qrcode.QRCode(
    version=1,  # Auto-sizing
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Highest error correction
    box_size=20,  # Large boxes for better visibility
    border=4,  # Wide border
)
qr.add_data(simple_content)
qr.make(fit=True)

# Create an image from the QR Code with high contrast
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
output_path = os.path.join(output_dir, "test_qr.png")
img.save(output_path)

print(f"\nHigh-contrast test QR code generated and saved to: {output_path}")
print("\nTest Instructions:")
print("1. First test with file-based reader:")
print(f"   python qr_task_worker_from_file.py -f {output_path}")
print("2. If that works, display the QR code on screen")
print("3. Run the camera-based reader:")
print("   python qr_task_worker.py")
