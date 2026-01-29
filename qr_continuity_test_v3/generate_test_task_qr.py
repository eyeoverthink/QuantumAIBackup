#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Task QR Code Generator

Generates a QR code containing a valid task for the Quantum Phi-Harmonic system.
"""

import os
import json
import qrcode
import uuid
import time
from datetime import datetime

# Create output directory
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_outputs/test_task")
os.makedirs(output_dir, exist_ok=True)

# Create a task payload with the correct format
task_id = f"phi-test-{uuid.uuid4().hex[:8]}"

# Simple script that creates a file with phi-harmonic values
script = """
# Quantum Phi-Harmonic Test Script
import os
import time
import math

# Golden Ratio (φ)
PHI = (1 + 5 ** 0.5) / 2

# Create output directory
os.makedirs("quantum_outputs/test_results", exist_ok=True)

# Calculate phi-harmonic values
current_time = time.time()
phi_time = (current_time * PHI) % 1
resonance = (PHI * phi_time) % 1

# Write results to file
with open("quantum_outputs/test_results/phi_test_result.txt", "w") as f:
    f.write("QUANTUM PHI-HARMONIC TEST SUCCESSFUL!\n")
    f.write("==========================\n")
    f.write(f"Execution Time: {time.ctime()}\n")
    f.write(f"Phi-Time: {phi_time}\n")
    f.write(f"Resonance: {resonance}\n")
    f.write("==========================\n")

print("\n✅ QUANTUM PHI-HARMONIC TEST SUCCESSFUL!")
print(f"📊 Phi-Time: {phi_time:.6f}")
print(f"🔄 Resonance: {resonance:.6f}")
print(f"📝 Results written to: quantum_outputs/test_results/phi_test_result.txt")
"""

# Create task payload matching the format expected by qr_task_worker
task_payload = {
    "task_id": task_id,
    "script": script,
    "input_data": {
        "phi": (1 + 5 ** 0.5) / 2,
        "timestamp": time.time(),
        "test_type": "phi_harmonic_verification"
    },
    "metadata": {
        "phi": 1.618034,
        "timestamp": datetime.now().isoformat(),
        "resonance": 0.618034,
        "complexity": 0.381966
    }
}

# Convert to JSON
json_data = json.dumps(task_payload)
print("QR Code Content:")
print(f"Task ID: {task_id}")
print(f"Total payload size: {len(json_data)} bytes")

# Generate QR code
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
output_path = os.path.join(output_dir, "test_task_qr.png")
img.save(output_path)

# Also save to the project root for easy access
root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_task_qr.png")
img.save(root_path)

print(f"\nTest task QR code generated and saved to:\n1. {output_path}\n2. {root_path}")
print("\nTest Instructions:")
print("1. Run the single-run QR processor:")
print(f"   python qr_single_run.py -f {root_path}")
print("2. If successful, you should see 'QUANTUM PHI-HARMONIC TEST SUCCESSFUL!' in the output")
print("3. The action will create a result file in quantum_outputs/test_results/")
