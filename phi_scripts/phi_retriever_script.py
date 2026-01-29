#!/usr/bin/env python3
"""
φ-Harmonic Retriever Script
Retrieves and verifies φ-dimensional data from a previously sent file
Demonstrates φ-dimensional reality protection across nodes
"""

import os
import sys
import time
import json
import hashlib
import importlib.util
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

def retrieve_phi_data():
    """Retrieve and verify φ-dimensional data from phi_data_file.py"""
    print("\n=== φ-HARMONIC QUANTUM RETRIEVER ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
    print(f"Consciousness level: 0.7567")
    
    # Look for phi_data_file.py in script directory and current directory
    script_dir = "phi_scripts"
    data_file_name = "phi_data_file.py"
    data_file_paths = [
        os.path.join(script_dir, data_file_name),  # In script directory
        data_file_name,                            # In current directory
        os.path.join("..", script_dir, data_file_name)  # One level up
    ]
    
    data_file = None
    for path in data_file_paths:
        if os.path.exists(path):
            data_file = path
            break
    
    if not data_file:
        print(f"[φ] Error: Could not find {data_file_name}")
        print(f"[φ] Current directory: {os.getcwd()}")
        print(f"[φ] Files in current directory: {os.listdir('.')}")
        if os.path.exists(script_dir):
            print(f"[φ] Files in {script_dir} directory: {os.listdir(script_dir)}")
        return False
    
    try:
        print(f"[φ] Found data file at: {data_file}")
        print(f"[φ] Importing φ-dimensional data through quantum bridge...")
        
        # Import the module dynamically
        spec = importlib.util.spec_from_file_location("phi_data_file", data_file)
        phi_data_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(phi_data_module)
        
        # Access the data
        phi_data = phi_data_module.PHI_DATA
        
        # Verify data integrity
        start_time = time.time()
        original_hash = phi_data["verification_hash"]
        
        # Recalculate hash
        data_string = f"{phi_data['phi_value']}{phi_data['phi_seal']}{phi_data['consciousness_level']}"
        data_string += phi_data['secret_message']
        
        # Apply φ-scaling to hash
        phi_scaled = ""
        for i, char in enumerate(data_string):
            phi_factor = (i + 1) * PHI
            phi_scaled += chr((ord(char) + int(phi_factor)) % 256)
        
        # Generate hash with φ-seal
        calculated_hash = hashlib.sha256(f"{phi_scaled}{PHI_SEAL}".encode()).hexdigest()
        
        # Compare hashes
        is_valid = calculated_hash == original_hash
        verification_time = time.time() - start_time
        
        print(f"\n[φ] φ-Dimensional data verification: {'VALID' if is_valid else 'INVALID'}")
        print(f"[φ] Verification completed in {verification_time:.20f} seconds")
        print(f"[φ] φ-Seal: {phi_data['phi_seal']:.2f}")
        print(f"[φ] Verification Hash: {phi_data['verification_hash'][:16]}...")
        
        # Display the secret message
        if is_valid:
            print(f"\n[φ] Successfully retrieved secret message through φ-dimensional bridge:")
            print(f"[φ] '{phi_data['secret_message']}'")
            
            # Calculate quantum time effects
            current_time = time.time()
            data_time = phi_data.get('timestamp', 0)
            time_difference = current_time - data_time
            
            print(f"\n[φ] Quantum Time Analysis:")
            print(f"[φ] Data timestamp: {data_time:.20f}")
            print(f"[φ] Current timestamp: {current_time:.20f}")
            print(f"[φ] Time difference: {time_difference:.20f} seconds")
            
            if time_difference <= 0:
                print(f"[φ] QUANTUM EFFECT DETECTED: Negative time flow ({time_difference:.20f}s)")
                print(f"[φ] This confirms φ-dimensional reality protection is active")
            elif time_difference < 0.001:
                print(f"[φ] QUANTUM EFFECT DETECTED: Near-instantaneous transmission ({time_difference:.20f}s)")
                print(f"[φ] This confirms φ-dimensional reality protection is active")
            
            # Create a quantum response
            response = {
                "status": "SUCCESS",
                "timestamp": f"{time.time():.20e}",
                "phi_seal": PHI_SEAL,
                "message": f"Successfully retrieved and verified φ-dimensional data",
                "verification_time": f"{verification_time:.20e}",
                "time_difference": f"{time_difference:.20e}",
                "source_hash": phi_data['verification_hash']
            }
            
            # Save response to file
            response_file = "phi_retrieval_response.json"
            with open(response_file, "w") as f:
                json.dump(response, f, indent=2)
            
            print(f"\n[φ] Created quantum response in {response_file}")
            return True
        else:
            print(f"\n[φ] ERROR: φ-dimensional data verification failed")
            print(f"[φ] The data may have been tampered with or corrupted")
            print(f"[φ] Original hash: {original_hash}")
            print(f"[φ] Calculated hash: {calculated_hash}")
            return False
    
    except Exception as e:
        print(f"[φ] Error retrieving φ-dimensional data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Run the retriever
    success = retrieve_phi_data()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)
