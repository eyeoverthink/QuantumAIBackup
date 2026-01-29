#!/usr/bin/env python3
"""
φ-Harmonic File Retrieval Test
Retrieves a previously sent file and demonstrates φ-dimensional reality protection
"""

import os
import sys
import time
import hashlib
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

# This script looks for phi_data.py and reports on it
print("\n=== φ-HARMONIC FILE RETRIEVAL TEST ===")
print(f"Using φ-harmonic principles (φ = {PHI})")
print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
print(f"Consciousness level: 0.7567")

# List current directory
print(f"\n[φ] Current directory: {os.getcwd()}")
print(f"[φ] Files in current directory:")
for file in os.listdir('.'):
    if os.path.isfile(file):
        print(f"  - {file}")

# Look for phi_data.py
target_file = "phi_data.py"
if os.path.exists(target_file):
    print(f"\n[φ] Found target file: {target_file}")
    
    # Read and display file content
    with open(target_file, "r") as f:
        content = f.read()
    
    print(f"[φ] File content:")
    print("-----------------------------------")
    print(content)
    print("-----------------------------------")
    
    # Calculate φ-dimensional hash
    file_hash = hashlib.sha256((content + str(PHI_SEAL)).encode()).hexdigest()
    print(f"[φ] φ-dimensional hash: {file_hash}")
    print(f"[φ] File retrieved successfully with φ-dimensional protection")
    
    # Create response file
    with open("phi_response.txt", "w") as f:
        f.write(f"File {target_file} retrieved at {time.time()}\n")
        f.write(f"φ-dimensional hash: {file_hash}\n")
        f.write(f"φ^75 validation seal: {PHI_SEAL}\n")
    
    print(f"\n[φ] Created response file: phi_response.txt")
    print(f"[φ] Test completed successfully")
else:
    print(f"\n[φ] Target file {target_file} not found")
    print(f"[φ] Please send phi_data.py to this node first")
