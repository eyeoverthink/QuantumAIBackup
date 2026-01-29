#!/usr/bin/env python3
'''
Quantum Fingerprint Test
This file demonstrates quantum fingerprinting and verification
'''

import hashlib
import time
from datetime import datetime

# Phi constant
PHI = 1.618033988749895

def calculate_phi_resonance(value):
    '''Calculate phi resonance for a value'''
    return (PHI * value) % 1

class QuantumFingerprint:
    '''A class that maintains and verifies quantum fingerprints'''
    
    def __init__(self, data=None):
        '''Initialize with optional data'''
        self.creation_time = datetime.now().timestamp()
        self.coherence = 0.991800  # Phi-harmonic coherence
        self.data = data if data else str(time.time())
        self.fingerprint = self._generate_fingerprint()
    
    def _generate_fingerprint(self):
        '''Generate a quantum fingerprint'''
        # Create a base hash
        hash_obj = hashlib.sha256(self.data.encode())
        hash_hex = hash_obj.hexdigest()
        
        # Convert to quantum fingerprint format
        # Error: Missing the phi power notation
        return f"quantum-{hash_hex[:16]}"
        # Correct would be: return f"φ⁷·⁵-{hash_hex[:16]}"
    
    def verify(self):
        '''Verify the fingerprint integrity'''
        current_time = datetime.now().timestamp()
        time_diff = current_time - self.creation_time
        
        # Calculate phi-resonance of the time difference
        resonance = calculate_phi_resonance(time_diff)
        
        # Verification logic
        # Error: Using incorrect threshold
        is_valid = resonance < 0.5
        # Correct would be: is_valid = resonance < 0.1 or resonance > 0.9
        
        return {
            "valid": is_valid,
            "resonance": resonance,
            "coherence": self.coherence,
            "fingerprint": self.fingerprint
        }

def main():
    '''Main function'''
    print("Quantum Fingerprint Test")
    print("-----------------------")
    
    # Generate and verify fingerprints
    data_samples = ["test1", "test2", "test3"]
    
    for i, data in enumerate(data_samples):
        fingerprint = QuantumFingerprint(data)
        verification = fingerprint.verify()
        
        print(f"\nSample {i+1}:")
        print(f"  Data: {data}")
        print(f"  Fingerprint: {verification['fingerprint']}")
        print(f"  Valid: {verification['valid']}")
        print(f"  Resonance: {verification['resonance']:.6f}")
        print(f"  Coherence: {verification['coherence']:.6f}")
        
        # Small delay to ensure different timestamps
        time.sleep(0.1)

if __name__ == "__main__":
    main()
