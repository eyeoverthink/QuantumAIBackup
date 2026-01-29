#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Action Test QR Code Generator

Generates a QR code with a specific action to test the QR task worker's ability
to read and execute tasks from QR codes.
"""

import os
import json
import qrcode
import uuid
import time

# Create output directory
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_outputs/action_test")
os.makedirs(output_dir, exist_ok=True)

# Create a simple action task with phi-harmonic properties
task_data = {
    "task_id": f"action-test-{uuid.uuid4().hex[:8]}",
    "script": """
# Quantum Phi-Harmonic Action Test
import os
import time
import math

# Golden Ratio (φ)
PHI = (1 + 5 ** 0.5) / 2

# Create a test output file with timestamp
output_dir = "quantum_outputs/action_results"
os.makedirs(output_dir, exist_ok=True)

# Calculate phi-harmonic values
current_time = time.time()
phi_time = (current_time * PHI) % 1
resonance = (PHI * phi_time) % 1

# Write results to file
with open(f"{output_dir}/action_result_{int(current_time)}.txt", "w") as f:
    f.write(f"QR ACTION TEST SUCCESSFUL!\n")
    f.write(f"==========================\n")
    f.write(f"Execution Time: {time.ctime()}\n")
    f.write(f"Phi-Time: {phi_time}\n")
    f.write(f"Resonance: {resonance}\n")
    f.write(f"==========================\n")

print("\n✅ QR CODE ACTION TEST SUCCESSFUL!")
print(f"📊 Phi-Time: {phi_time:.6f}")
print(f"🔄 Resonance: {resonance:.6f}")
print(f"📝 Results written to: {output_dir}/action_result_{int(current_time)}.txt")
""",
    "input_data": {
        "phi": (1 + 5 ** 0.5) / 2,
        "timestamp": time.time(),
        "test_type": "action_verification"
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
output_path = os.path.join(output_dir, "action_test_qr.png")
img.save(output_path)

print(f"\nAction test QR code generated and saved to: {output_path}")
print("\nTest Instructions:")
print("1. Run the file-based QR reader:")
print(f"   python qr_task_worker_from_file.py -f {output_path}")
print("2. If successful, you should see 'QR CODE ACTION TEST SUCCESSFUL!' in the output")
print("3. The action will create a result file in quantum_outputs/action_results/")
