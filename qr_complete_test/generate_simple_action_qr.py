#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple Action Test QR Code Generator

Generates a QR code with a very simple action to test the QR task worker.
"""

import os
import json
import qrcode
import uuid
import time

# Create output directory
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_outputs/action_test")
os.makedirs(output_dir, exist_ok=True)

# Create a very simple action task
task_data = {
    "task_id": f"simple-test-{uuid.uuid4().hex[:8]}",
    "script": """
import os
import time

# Create output directory
os.makedirs("quantum_outputs/action_results", exist_ok=True)

# Create a simple output file
with open("quantum_outputs/action_results/simple_test_result.txt", "w") as f:
    f.write("QR CODE ACTION TEST SUCCESSFUL!\n")
    f.write("==========================\n")
    f.write("Execution Time: " + time.ctime() + "\n")
    f.write("==========================\n")

print("\n✅ QR CODE ACTION TEST SUCCESSFUL!")
print("📝 Results written to: quantum_outputs/action_results/simple_test_result.txt")
""",
    "input_data": {
        "test_type": "simple_verification"
    }
}

# Convert to JSON
json_data = json.dumps(task_data)
print("QR Code Content:")
print(json_data[:100] + "..." + json_data[-50:])
print(f"Total payload size: {len(json_data)} bytes")

# Generate QR code with optimal settings for readability
qr = qrcode.QRCode(
    version=10,  # Fixed version to ensure sufficient capacity
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
    box_size=20,  # Large boxes for better visibility
    border=4,  # Wide border
)
qr.add_data(json_data)
qr.make(fit=True)

# Create an image from the QR Code with high contrast
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
output_path = os.path.join(output_dir, "simple_action_test_qr.png")
img.save(output_path)

print(f"\nSimple action test QR code generated and saved to: {output_path}")
print("\nTest Instructions:")
print("1. Run the file-based QR reader:")
print(f"   python qr_task_worker_from_file.py -f {output_path}")
print("2. If successful, you should see 'QR CODE ACTION TEST SUCCESSFUL!' in the output")
print("3. The action will create a result file in quantum_outputs/action_results/")
