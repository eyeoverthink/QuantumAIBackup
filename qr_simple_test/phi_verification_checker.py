#!/usr/bin/env python3
"""
PHI VERIFICATION CHECKER
========================
Verifies Lane 5 phi-quantum transfers and integrates with the Phi-Harmonic
Orchestrator to maintain quantum coherence across the system.

This module follows the "lego" design philosophy by importing existing components
while adding verification capabilities without modifying core modules.
"""

import os
import sys
import json
import glob
import time
import datetime
from pathlib import Path

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Constants
PHI = 1.618033988749895  # φ (Golden ratio)
PHI_INV = 0.6180339887498948  # φ⁻¹ (Inverse golden ratio)
PHI_75 = 36.93238055064196  # φ^7.5
PERSONAL_RATIO = 6.2631578947368425  # 119/19

class PhiVerificationChecker:
    """
    Checks verification results from phi-quantum transfers,
    with special focus on Lane 5 transfers.
    """
    
    def __init__(self):
        """Initialize the verification checker."""
        self.lane5_dir = Path("phi_lane5_transfer_results")
        self.transfer_id = "533fee57ecb4"  # The ID from our Lane 5 transfer
        self.expected_timestamp = "2025-04-28 04:18:52.151702"
    
    def find_verification_files(self):
        """Find all verification files in the Lane 5 results directory."""
        if not self.lane5_dir.exists():
            print(f"Error: Lane 5 results directory not found: {self.lane5_dir}")
            return []
        
        # Find verification files
        verification_pattern = str(self.lane5_dir / f"lane5_verification_{self.transfer_id}*.json")
        verification_files = glob.glob(verification_pattern)
        
        # If no specific ID files found, look for any verification files
        if not verification_files:
            verification_pattern = str(self.lane5_dir / "lane5_verification_*.json")
            verification_files = glob.glob(verification_pattern)
        
        return verification_files
    
    def get_newest_file(self, files):
        """Get the newest file from a list of files."""
        if not files:
            return None
        
        # Sort by modification time (newest first)
        return max(files, key=os.path.getmtime)
    
    def load_verification_data(self, file_path):
        """Load verification data from a file."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading verification data: {e}")
            return None
    
    def check_verification_results(self):
        """Check verification results from Lane 5 transfers."""
        print("\n=== PHI-QUANTUM VERIFICATION CHECKER ===")
        print(f"φ = {PHI}, φ⁻¹ = {PHI_INV}, φ^7.5 = {PHI_75}")
        print(f"Target Transfer ID: {self.transfer_id}")
        print(f"Expected Timestamp: {self.expected_timestamp}")
        print("=========================================")
        
        # Find verification files
        verification_files = self.find_verification_files()
        print(f"Found {len(verification_files)} verification files")
        
        if not verification_files:
            # Look for transfer files instead
            transfer_pattern = str(self.lane5_dir / f"lane5_transfer_{self.transfer_id}*.json")
            transfer_files = glob.glob(transfer_pattern)
            
            if transfer_files:
                newest_transfer = self.get_newest_file(transfer_files)
                print(f"Found transfer file: {os.path.basename(newest_transfer)}")
                
                transfer_data = self.load_verification_data(newest_transfer)
                if transfer_data:
                    future_timestamp = transfer_data.get("future_timestamp")
                    print(f"Transfer executed, awaiting verification at: {future_timestamp}")
                    
                    # Check if the verification timestamp has already passed
                    try:
                        future_dt = datetime.datetime.strptime(future_timestamp, "%Y-%m-%d %H:%M:%S.%f")
                        future_time = future_dt.timestamp()
                        current_time = time.time()
                        
                        if current_time > future_time:
                            time_passed = current_time - future_time
                            print(f"Verification time passed {time_passed:.2f} seconds ago")
                            print("No verification data found, suggesting verification may have failed")
                        else:
                            time_remaining = future_time - current_time
                            print(f"Verification will occur in {time_remaining:.2f} seconds")
                    except:
                        print("Could not parse future timestamp")
            else:
                print("No transfer files found")
            
            return None
        
        # Get the newest verification file
        newest_file = self.get_newest_file(verification_files)
        print(f"Latest verification: {os.path.basename(newest_file)}")
        
        # Load verification data
        verification_data = self.load_verification_data(newest_file)
        if not verification_data:
            print("Error: Could not load verification data")
            return None
        
        # Extract key verification results
        transfer_id = verification_data.get("transfer_id", "unknown")
        expected_timestamp = verification_data.get("expected_timestamp", "unknown")
        actual_timestamp = verification_data.get("actual_timestamp", "unknown")
        time_diff_seconds = verification_data.get("time_diff_seconds", float('inf'))
        phi_resonance = verification_data.get("phi_resonance", 1.0)
        is_phi_resonant = verification_data.get("is_phi_resonant", False)
        verification_success = verification_data.get("verification_success", False)
        
        # Print verification results
        print("\n=== VERIFICATION RESULTS ===")
        print(f"Transfer ID: {transfer_id}")
        print(f"Expected Time: {expected_timestamp}")
        print(f"Actual Time: {actual_timestamp}")
        print(f"Time Difference: {time_diff_seconds:.6f} seconds")
        print(f"Phi-Resonance: {phi_resonance:.4f}")
        
        # Determine verification status
        if verification_success:
            if abs(time_diff_seconds) < 0.0004:
                status = "✓ VERIFIED WITH MICROSECOND PRECISION"
            elif is_phi_resonant:
                status = "✓ VERIFIED WITH PHI-RESONANT PRECISION"
            else:
                status = "✓ VERIFIED WITH MILLISECOND PRECISION"
        else:
            status = "❌ NOT VERIFIED"
        
        print(f"Status: {status}")
        
        # Integrate with Phi-Harmonic Orchestrator if available
        try:
            from phi_harmonic_orchestrator import get_orchestrator
            orchestrator = get_orchestrator()
            
            # Publish verification event
            orchestrator.publish_event(
                event_type="lane5_transfer_verified",
                event_data={
                    "transfer_id": transfer_id,
                    "verification_success": verification_success,
                    "time_diff_seconds": time_diff_seconds,
                    "phi_resonance": phi_resonance,
                    "status": status
                }
            )
            
            print("\nVerification results published to Phi-Harmonic Orchestrator")
        except:
            print("\nPhi-Harmonic Orchestrator not available for event publishing")
        
        # Check if there was a causality inversion (message received before it was sent)
        original_transfer = verification_data.get("original_transfer", {})
        if original_transfer:
            transfer_time = original_transfer.get("execution_time", "unknown")
            
            print("\n=== CAUSALITY ANALYSIS ===")
            print(f"Transfer Executed: {transfer_time}")
            print(f"Future Timestamp: {expected_timestamp}")
            
            # Check for paradoxes - evidence of message reception before sending
            transfer_data_dir = Path("phi_quantum_actions")
            if transfer_data_dir.exists():
                # Look for evidence of paradox
                paradox_pattern = str(transfer_data_dir / f"*{transfer_id}*.json")
                paradox_files = glob.glob(paradox_pattern)
                
                if paradox_files:
                    paradox_file = self.get_newest_file(paradox_files)
                    print(f"Found potential paradox evidence: {os.path.basename(paradox_file)}")
                    
                    try:
                        with open(paradox_file, 'r') as f:
                            paradox_data = json.load(f)
                        
                        # Check timestamps for evidence of causality inversion
                        if "timestamp" in paradox_data and "delivery_time" in paradox_data:
                            send_time = paradox_data["timestamp"]
                            receive_time = paradox_data["delivery_time"]
                            
                            print(f"Message Sent: {send_time}")
                            print(f"Message Received: {receive_time}")
                            
                            try:
                                send_dt = datetime.datetime.fromisoformat(send_time)
                                receive_dt = datetime.datetime.fromisoformat(receive_time)
                                
                                if receive_dt < send_dt:
                                    time_paradox = (send_dt - receive_dt).total_seconds()
                                    print(f"✓ CAUSALITY INVERSION DETECTED!")
                                    print(f"Message received {time_paradox:.2f} seconds BEFORE it was sent")
                                    print(f"This confirms successful time transfer via Lane 5")
                            except:
                                print("Could not parse paradox timestamps")
                    except:
                        print("Could not load paradox data")
        
        return verification_data

def main():
    """Run the verification checker."""
    checker = PhiVerificationChecker()
    checker.check_verification_results()

if __name__ == "__main__":
    main()
