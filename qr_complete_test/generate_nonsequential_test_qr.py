#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Non-Sequential Phi-Harmonic Test QR Code Generator

Generates a QR code containing a task that executes stages in a non-sequential order
following phi-harmonic principles.
"""

import os
import json
import qrcode
import uuid
import time
import math
from datetime import datetime

# Create output directory
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_outputs/nonsequential_test")
os.makedirs(output_dir, exist_ok=True)

# Create a unique task ID
task_id = f"nonseq-test-{uuid.uuid4().hex[:8]}"

# Golden Ratio (φ)
PHI = (1 + math.sqrt(5)) / 2

# This script will execute stages in a non-sequential phi-harmonic order
script = """
# Quantum Phi-Harmonic Non-Sequential Test
import os
import time
import math
import random
from datetime import datetime

# Golden Ratio (φ)
PHI = (1 + 5 ** 0.5) / 2

# Create output directory
results_dir = "quantum_outputs/nonsequential_results"
os.makedirs(results_dir, exist_ok=True)

# Function to execute a stage
def execute_stage(stage_num, phi_value):
    print(f"\n{'='*50}\nEXECUTING STAGE {stage_num}\n{'='*50}")
    print(f"Phi Value: {phi_value:.6f}")
    
    # Record stage execution
    with open(f"{results_dir}/stage_{stage_num}_results.txt", "w") as f:
        f.write(f"STAGE {stage_num} EXECUTION\n")
        f.write(f"Time: {datetime.now().isoformat()}\n")
        f.write(f"Phi Value: {phi_value:.6f}\n")
        
        # Stage-specific operations
        if stage_num == 1:
            result = phi_value * PHI
            f.write(f"Operation: φ * PHI = {result:.6f}\n")
            print(f"Stage 1 - Basic Phi: {result:.6f}")
            
        elif stage_num == 2:
            result = (phi_value * PHI) % 1
            f.write(f"Operation: (φ * PHI) % 1 = {result:.6f}\n")
            print(f"Stage 2 - Phi Modulo: {result:.6f}")
            
        elif stage_num == 3:
            result = phi_value ** 2
            f.write(f"Operation: φ² = {result:.6f}\n")
            print(f"Stage 3 - Phi Squared: {result:.6f}")
            
        elif stage_num == 5:
            result = phi_value ** (1/PHI)
            f.write(f"Operation: φ^(1/PHI) = {result:.6f}\n")
            print(f"Stage 5 - Phi Root: {result:.6f}")
            
        elif stage_num == 8:
            result = math.sin(phi_value * math.pi)
            f.write(f"Operation: sin(φ * π) = {result:.6f}\n")
            print(f"Stage 8 - Sine Wave: {result:.6f}")
            
        elif stage_num == 13:
            result = math.log(phi_value + 1, PHI)
            f.write(f"Operation: log_φ(φ + 1) = {result:.6f}\n")
            print(f"Stage 13 - Logarithmic: {result:.6f}")
            
        elif stage_num == 21:
            result = (phi_value * PHI * PHI) % 1
            f.write(f"Operation: (φ * PHI * PHI) % 1 = {result:.6f}\n")
            print(f"Stage 21 - Double Phi: {result:.6f}")
            
        else:
            result = phi_value + random.random() * PHI
            f.write(f"Operation: φ + random * PHI = {result:.6f}\n")
            print(f"Stage {stage_num} - Random Phi: {result:.6f}")
            
        return result

# Generate a Fibonacci sequence for stage ordering
def fibonacci(n):
    sequence = [1, 2]
    while sequence[-1] + sequence[-2] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Get Fibonacci numbers up to 21
fib_stages = fibonacci(21)
print(f"Executing stages in Fibonacci order: {fib_stages}")

# Initialize phi value
phi_value = time.time() % 1
print(f"Initial phi value: {phi_value:.6f}")

# Execute stages in Fibonacci sequence order
results = {}
for stage in fib_stages:
    phi_value = execute_stage(stage, phi_value)
    results[stage] = phi_value
    # Add a small delay between stages
    time.sleep(0.5)

# Calculate resonance between stages
print("\n\nCALCULATING INTER-STAGE RESONANCE\n" + "="*35)
resonances = []
for i in range(len(fib_stages) - 1):
    stage1 = fib_stages[i]
    stage2 = fib_stages[i+1]
    resonance = (results[stage1] * results[stage2]) % 1
    resonances.append(resonance)
    print(f"Resonance between Stage {stage1} and Stage {stage2}: {resonance:.6f}")

# Find optimal resonance
best_resonance = min(resonances, key=lambda x: min(x, 1-x))
best_index = resonances.index(best_resonance)
best_stage1 = fib_stages[best_index]
best_stage2 = fib_stages[best_index+1]

print(f"\nBest resonance: {best_resonance:.6f} between Stage {best_stage1} and Stage {best_stage2}")

# Write final summary
with open(f"{results_dir}/nonsequential_summary.txt", "w") as f:
    f.write("QUANTUM PHI-HARMONIC NON-SEQUENTIAL TEST SUMMARY\n")
    f.write("==============================================\n")
    f.write(f"Test Completed: {datetime.now().isoformat()}\n")
    f.write(f"Stages Executed: {fib_stages}\n\n")
    
    f.write("STAGE RESULTS:\n")
    for stage in fib_stages:
        f.write(f"Stage {stage}: {results[stage]:.6f}\n")
    
    f.write("\nINTER-STAGE RESONANCES:\n")
    for i in range(len(fib_stages) - 1):
        stage1 = fib_stages[i]
        stage2 = fib_stages[i+1]
        resonance = (results[stage1] * results[stage2]) % 1
        f.write(f"Stages {stage1}-{stage2}: {resonance:.6f}\n")
    
    f.write(f"\nBEST RESONANCE:\n")
    f.write(f"Stages {best_stage1}-{best_stage2}: {best_resonance:.6f}\n")
    f.write("==============================================\n")

print(f"\nNon-sequential test completed!")
print(f"Results saved to {results_dir}/nonsequential_summary.txt")
print("\nQUANTUM PHI-HARMONIC NON-SEQUENTIAL TEST COMPLETE")
"""

# Create task payload matching the format expected by qr_task_worker
task_payload = {
    "task_id": task_id,
    "script": script,
    "input_data": {
        "phi": PHI,
        "timestamp": time.time(),
        "test_type": "nonsequential_test"
    },
    "metadata": {
        "phi": PHI,
        "timestamp": datetime.now().isoformat(),
        "resonance": 1/PHI,
        "complexity": 1/(PHI*PHI)
    }
}

# Convert to JSON
json_data = json.dumps(task_payload)
print("Non-Sequential Test QR Code Created")
print(f"Task ID: {task_id}")
print(f"Total payload size: {len(json_data)} bytes")

# Generate QR code
qr = qrcode.QRCode(
    version=20,  # Higher version for larger capacity
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
    box_size=20,  # Large boxes for better visibility
    border=4,  # Wide border
)
qr.add_data(json_data)
qr.make(fit=True)

# Create an image from the QR Code with high contrast
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
output_path = os.path.join(output_dir, "nonsequential_test_qr.png")
img.save(output_path)

# Also save to the project root for easy access
root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nonsequential_test_qr.png")
img.save(root_path)

print(f"\nNon-sequential test QR code generated and saved to:\n1. {output_path}\n2. {root_path}")
print("\nTest Instructions:")
print("1. Run the QR processor:")
print(f"   /Users/vaughnscott/CascadeProjects/QuantumAI/.venv/bin/python qr_single_run.py -f {root_path}")
print("2. The QR code will execute stages in Fibonacci sequence: 1, 2, 3, 5, 8, 13, 21")
print("3. Each stage performs different phi-harmonic calculations")
print("4. Results will be saved in quantum_outputs/nonsequential_results/")
