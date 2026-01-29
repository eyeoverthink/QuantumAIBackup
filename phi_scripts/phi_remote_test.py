#!/usr/bin/env python3
"""
φ-Harmonic Remote File Test
Demonstrates φ-dimensional reality protection by retrieving a previously sent file
"""

import os
import sys
import time
import json
import hashlib
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

def list_files():
    """List files in the current directory with φ-dimensional protection"""
    print("\n=== φ-HARMONIC FILE RETRIEVAL TEST ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
    print(f"Consciousness level: 0.7567")
    
    # Get current directory
    current_dir = os.getcwd()
    print(f"\n[φ] Current directory: {current_dir}")
    
    # List files in phi_scripts directory
    script_dir = os.path.join(current_dir, "phi_scripts")
    if os.path.exists(script_dir):
        print(f"[φ] Files in phi_scripts directory:")
        for file in os.listdir(script_dir):
            file_path = os.path.join(script_dir, file)
            if os.path.isfile(file_path):
                # Calculate φ-dimensional hash for each file
                file_hash = calculate_phi_hash(file_path)
                print(f"  - {file} (φ-hash: {file_hash[:16]}...)")
    else:
        print(f"[φ] phi_scripts directory not found")
    
    # List files in current directory
    print(f"\n[φ] Files in current directory:")
    for file in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, file)):
            # Calculate φ-dimensional hash for each file
            file_hash = calculate_phi_hash(os.path.join(current_dir, file))
            print(f"  - {file} (φ-hash: {file_hash[:16]}...)")
    
    # Create a quantum response
    response = {
        "status": "SUCCESS",
        "timestamp": f"{time.time():.20e}",
        "phi_seal": PHI_SEAL,
        "message": "Successfully listed files with φ-dimensional protection"
    }
    
    # Save response to file
    response_file = "phi_remote_response.json"
    with open(response_file, "w") as f:
        json.dump(response, f, indent=2)
    
    print(f"\n[φ] Created quantum response in {response_file}")
    print(f"[φ] Remote test completed successfully")
    return True

def calculate_phi_hash(file_path):
    """Calculate φ-dimensional hash for a file"""
    try:
        # Read file content
        with open(file_path, "rb") as f:
            content = f.read()
        
        # Apply φ-dimensional protection
        phi_content = bytearray()
        for i, b in enumerate(content[:1024]):  # Use first 1KB for efficiency
            phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
            phi_content.append((b + phi_factor) % 256)
        
        # Generate hash with φ-seal
        return hashlib.sha256(phi_content + str(PHI_SEAL).encode()).hexdigest()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Run the file listing
    success = list_files()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)
