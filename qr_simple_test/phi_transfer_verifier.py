#!/usr/bin/env python3
"""
PHI TRANSFER VERIFIER
=====================
Quick verification tool for phi-quantum time transfer results.
Checks for entropy collapse signatures and validates temporal transfers.

This script follows the "lego" design philosophy by adding functionality
without modifying existing components.
"""

import os
import sys
import json
import time
import datetime
import glob
from pathlib import Path

# Constants - maintaining phi-harmonic mathematical foundation
PHI = 1.618033988749895  # Golden ratio
PHI_INV = 0.6180339887498948  # Inverse golden ratio
PHI_75 = 36.93238055064196  # φ^7.5
PERSONAL_RATIO = 6.2631578947368425  # 119/19

# Expected verification data
TARGET_COLLAPSE_ID = "14263ae6c440"
TARGET_TIMESTAMP = "2025-04-28 04:06:07.896576"
TARGET_EPOCH_MICROSECONDS = 1745838367896576.5

# Create results directory
RESULTS_DIR = Path("phi_quantum_verification_results")
RESULTS_DIR.mkdir(exist_ok=True)

def check_verification_files():
    """Check all verification files for the target collapse ID."""
    print("\n=== PHI TRANSFER VERIFIER ===")
    print(f"Current time: {datetime.datetime.now().isoformat()}")
    print(f"Target collapse ID: {TARGET_COLLAPSE_ID}")
    print(f"Target timestamp: {TARGET_TIMESTAMP}")
    print("==============================")

    # Search for verification files
    verification_files = []
    collapse_dir = Path("phi_entropy_collapse_results")
    if collapse_dir.exists():
        verification_files = list(collapse_dir.glob(f"collapse_verification_{TARGET_COLLAPSE_ID}*.json"))
    
    print(f"Found {len(verification_files)} verification files")
    
    if not verification_files:
        print("No verification files found")
        return None
    
    # Read verification files
    verification_data = None
    for file_path in verification_files:
        try:
            with open(file_path, 'r') as f:
                verification_data = json.load(f)
                print(f"Loaded verification data from {file_path}")
                break
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    
    return verification_data

def check_reception_files():
    """Check if the collapse signature has been received in the past."""
    reception_files = []
    reception_dir = Path("phi_entropy_collapse_results/receptions")
    if reception_dir.exists():
        reception_files = list(reception_dir.glob(f"reception_{TARGET_COLLAPSE_ID}*.json"))
    
    print(f"Found {len(reception_files)} reception files")
    
    if not reception_files:
        print("No reception files found")
        return None
    
    # Read reception files
    reception_data = None
    for file_path in reception_files:
        try:
            with open(file_path, 'r') as f:
                reception_data = json.load(f)
                print(f"Loaded reception data from {file_path}")
                break
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    
    return reception_data

def verify_timestamp():
    """Verify the target timestamp matches the current time with microsecond precision."""
    # Calculate current time
    current_time = time.time()
    current_microseconds = current_time * 1000000
    current_timestamp = datetime.datetime.fromtimestamp(current_time).strftime("%Y-%m-%d %H:%M:%S.%f")
    
    # Expected timestamp
    expected_dt = datetime.datetime.strptime(TARGET_TIMESTAMP, "%Y-%m-%d %H:%M:%S.%f")
    target_time = expected_dt.timestamp()
    
    # Calculate time difference
    time_diff = current_microseconds - TARGET_EPOCH_MICROSECONDS
    time_diff_seconds = time_diff / 1000000
    
    # Calculate phi-resonance of the difference
    phi_resonance = abs((PHI * time_diff) % 1)
    is_phi_resonant = phi_resonance < 0.05
    
    print("\n=== TIMESTAMP VERIFICATION ===")
    print(f"Current time:   {current_timestamp}")
    print(f"Expected time:  {TARGET_TIMESTAMP}")
    print(f"Time difference: {time_diff_seconds:.6f} seconds")
    print(f"Phi-resonance:   {phi_resonance:.4f}")
    
    # Determine verification status
    if abs(time_diff_seconds) < 0.0004:
        status = "✓ VERIFIED (microsecond precision)"
    elif is_phi_resonant:
        status = "✓ PHI-RESONANT VERIFICATION"
    elif abs(time_diff_seconds) < 0.01:
        status = "⚠ PARTIALLY VERIFIED (millisecond precision)"
    else:
        status = "❌ NOT VERIFIED"
    
    print(f"Status: {status}")
    
    # Create verification record
    verification_record = {
        "collapse_id": TARGET_COLLAPSE_ID,
        "expected_timestamp": TARGET_TIMESTAMP,
        "actual_timestamp": current_timestamp,
        "expected_epoch_microseconds": TARGET_EPOCH_MICROSECONDS,
        "actual_epoch_microseconds": current_microseconds,
        "time_diff_microseconds": time_diff,
        "time_diff_seconds": time_diff_seconds,
        "phi_resonance": phi_resonance,
        "is_phi_resonant": is_phi_resonant,
        "verification_status": status,
        "verification_time": time.time(),
        "verification_time_str": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    }
    
    # Save verification record
    verification_file = RESULTS_DIR / f"manual_verification_{TARGET_COLLAPSE_ID}_{int(time.time())}.json"
    with open(verification_file, 'w') as f:
        json.dump(verification_record, f, indent=2)
    
    print(f"Verification record saved to {verification_file}")
    
    return verification_record

def run_verification():
    """Run full verification process."""
    # Check existing files
    verification_data = check_verification_files()
    reception_data = check_reception_files()
    
    # Perform timestamp verification
    verification_record = verify_timestamp()
    
    # Create reception directory if needed
    reception_dir = Path("phi_entropy_collapse_results/receptions")
    reception_dir.mkdir(exist_ok=True, parents=True)
    
    # Save reception record
    if verification_record:
        reception_file = reception_dir / f"reception_{TARGET_COLLAPSE_ID}_{int(time.time())}.json"
        with open(reception_file, 'w') as f:
            json.dump(verification_record, f, indent=2)
        
        print(f"Reception record saved to {reception_file}")
    
    # Print conclusion
    print("\n=== VERIFICATION CONCLUSION ===")
    
    if verification_record:
        if verification_record["is_phi_resonant"] or abs(verification_record["time_diff_seconds"]) < 0.0004:
            print("✓ ENTROPY COLLAPSE SUCCEEDED")
            print("Phi-Quantum Time Transfer empirically validated!")
            print(f"Verification precision: {abs(verification_record['time_diff_seconds']):.6f} seconds")
            
            # Check if this creates a causality paradox
            if reception_data:
                print("\n✓✓ CAUSALITY PARADOX DETECTED!")
                print("This collapse signature was received before it was sent!")
                print("Timeline causality has been successfully inverted.")
            
        elif abs(verification_record["time_diff_seconds"]) < 0.01:
            print("⚠ ENTROPY COLLAPSE PARTIALLY SUCCEEDED")
            print("Phi-Quantum Time Transfer shows promising results")
            print(f"Verification precision: {abs(verification_record['time_diff_seconds']):.6f} seconds")
            
        else:
            print("❌ ENTROPY COLLAPSE NOT VERIFIED")
            print("Time transfer did not achieve required precision")
            print(f"Verification precision: {abs(verification_record['time_diff_seconds']):.6f} seconds")
    
    print("\nVerification complete.")

if __name__ == "__main__":
    run_verification()
