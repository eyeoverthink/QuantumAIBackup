#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Compact Non-Sequential Phi-Harmonic Test QR Code Generator

Generates a smaller QR code containing a task that executes stages in a non-sequential order
following phi-harmonic principles.
"""

import os
import json
import qrcode
import uuid
import time
import math
import zlib
import base64
from datetime import datetime

# Create output directory
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_outputs/nonsequential_test")
os.makedirs(output_dir, exist_ok=True)

# Create a unique task ID
task_id = f"nonseq-{uuid.uuid4().hex[:6]}"

# Golden Ratio (φ)
PHI = (1 + math.sqrt(5)) / 2

# This script will execute stages in a non-sequential phi-harmonic order
# Compact version to fit within QR code size limits
script = """
import os,time,math,random
from datetime import datetime

# Setup
PHI=(1+5**0.5)/2
rd="quantum_outputs/nonsequential_results"
os.makedirs(rd,exist_ok=True)
print("Non-Sequential Phi Test Starting")

# Fibonacci sequence for stage order
fib=[1,2,3,5,8,13]
print(f"Executing stages: {fib}")

# Initialize
pv=time.time()%1
rs={}

# Execute stages
for s in fib:
    print(f"\n==== STAGE {s} ====\n")
    
    # Different operation per stage
    if s==1: r=pv*PHI; op="φ*PHI"
    elif s==2: r=(pv*PHI)%1; op="(φ*PHI)%1"
    elif s==3: r=pv**2; op="φ²"
    elif s==5: r=pv**(1/PHI); op="φ^(1/PHI)"
    elif s==8: r=math.sin(pv*math.pi); op="sin(φ*π)"
    elif s==13: r=math.log(pv+1,PHI) if pv>0 else pv*PHI; op="log_φ(φ+1)"
    else: r=pv+0.1; op="φ+0.1"
    
    # Record results
    print(f"Stage {s}: {op} = {r:.6f}")
    with open(f"{rd}/stage_{s}.txt","w") as f:
        f.write(f"STAGE {s}\nTime: {datetime.now()}\nOp: {op}\nResult: {r:.6f}\n")
    
    # Update for next stage
    rs[s]=r
    pv=r
    time.sleep(0.2)

# Calculate resonances
print("\n==== RESONANCES ====\n")
res=[]
for i in range(len(fib)-1):
    s1,s2=fib[i],fib[i+1]
    r=(rs[s1]*rs[s2])%1
    res.append(r)
    print(f"Resonance {s1}-{s2}: {r:.6f}")

# Find best resonance
br=min(res,key=lambda x:min(x,1-x))
bi=res.index(br)
bs1,bs2=fib[bi],fib[bi+1]
print(f"\nBest resonance: {br:.6f} between stages {bs1}-{bs2}")

# Write summary
with open(f"{rd}/summary.txt","w") as f:
    f.write("NON-SEQUENTIAL PHI TEST\n")
    f.write(f"Completed: {datetime.now()}\n\n")
    f.write("RESULTS:\n")
    for s in fib:
        f.write(f"Stage {s}: {rs[s]:.6f}\n")
    f.write("\nRESONANCES:\n")
    for i in range(len(fib)-1):
        s1,s2=fib[i],fib[i+1]
        r=(rs[s1]*rs[s2])%1
        f.write(f"Stages {s1}-{s2}: {r:.6f}\n")
    f.write(f"\nBest: {br:.6f} between {bs1}-{bs2}\n")

print(f"\nTest complete! Results in {rd}/summary.txt")
"""

# Compress the script to reduce QR code size
compressed_script = zlib.compress(script.encode('utf-8'), level=9)
encoded_script = base64.b64encode(compressed_script).decode('ascii')

# Create a compact decompression wrapper
wrapper_script = f"""
import base64,zlib,os,sys

# Decompress and execute the script
try:
    script_data = "{encoded_script}"
    compressed = base64.b64decode(script_data)
    script = zlib.decompress(compressed).decode('utf-8')
    print("Executing non-sequential phi test...")
    exec(script)
except Exception as e:
    print(f"Error: {{e}}")
    import traceback
    traceback.print_exc()
"""

# Create task payload matching the format expected by qr_task_worker
task_payload = {
    "task_id": task_id,
    "script": wrapper_script,
    "input_data": {
        "phi": PHI,
        "test_type": "nonseq"
    }
}

# Convert to JSON
json_data = json.dumps(task_payload)
print("Non-Sequential Test QR Code Created")
print(f"Task ID: {task_id}")
print(f"Original script size: {len(script)} bytes")
print(f"Compressed script size: {len(encoded_script)} bytes")
print(f"Total payload size: {len(json_data)} bytes")

# Generate QR code
qr = qrcode.QRCode(
    version=10,  # Lower version to ensure it fits
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
    box_size=20,  # Large boxes for better visibility
    border=4,  # Wide border
)
qr.add_data(json_data)
qr.make(fit=True)

# Create an image from the QR Code with high contrast
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
output_path = os.path.join(output_dir, "nonseq_test_qr.png")
img.save(output_path)

# Also save to the project root for easy access
root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nonseq_test_qr.png")
img.save(root_path)

print(f"\nNon-sequential test QR code generated and saved to:\n1. {output_path}\n2. {root_path}")
print("\nTest Instructions:")
print("1. Run the QR processor:")
print(f"   /Users/vaughnscott/CascadeProjects/QuantumAI/.venv/bin/python qr_single_run.py -f {root_path}")
print("2. The QR code will execute stages in Fibonacci sequence: 1, 2, 3, 5, 8, 13")
print("3. Each stage performs different phi-harmonic calculations")
print("4. Results will be saved in quantum_outputs/nonsequential_results/")
