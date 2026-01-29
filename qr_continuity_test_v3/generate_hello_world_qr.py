#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hello World QR Code Generator

Generates a QR code containing a simple Hello World message with Quantum Phi-Harmonic metadata.
"""

import os
import json
import qrcode
from datetime import datetime

# Create output directory
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_outputs/hello_world_qr")
os.makedirs(output_dir, exist_ok=True)

# Create a simple task payload
task_data = {
    "id": "phi-hello-world-1",
    "type": "text",
    "content": "Hello World from Quantum Phi-Harmonic System!",
    "metadata": {
        "phi": 1.618034,
        "timestamp": datetime.now().isoformat(),
        "resonance": 0.888888,
        "complexity": 0.618034
    }
}

# Convert to JSON
json_data = json.dumps(task_data, indent=2)
print("QR Code Content:")
print(json_data)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(json_data)
qr.make(fit=True)

# Create an image from the QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
output_path = os.path.join(output_dir, "hello_world_qr.png")
img.save(output_path)

print(f"\nQR Code generated and saved to: {output_path}")
print("\nInstructions:")
print("1. Display this QR code on your screen or print it")
print("2. Take a picture with your phone")
print("3. Show the QR code from your phone to your PC's camera")
print("4. Run 'python qr_task_worker.py' to scan and process the QR code")
