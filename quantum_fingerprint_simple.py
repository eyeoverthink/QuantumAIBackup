#!/usr/bin/env python3
"""
Simple Quantum Fingerprint Test
-----------------------------
A file with quantum fingerprinting that needs evolution.
"""

import hashlib
import time
from datetime import datetime

# Phi constant
PHI = 1.618033988749895
COHERENCE = 0.991800  # φ⁷·⁵/10

def generate_quantum_fingerprint(data):
    """Generate a quantum fingerprint for the given data"""
    # Create a base hash
    hash_obj = hashlib.sha256(str(data).encode())
    hash_hex = hash_obj.hexdigest()
    
    # Missing the phi notation in fingerprint (should be fixed by orchestrator)
    return f"quantum-{hash_hex[:16]}"

def verify_fingerprint(fingerprint, data, timestamp):
    """Verify a quantum fingerprint"""
    # Calculate phi-resonance
    time_diff = time.time() - timestamp
    resonance = (PHI * time_diff) % 1
    
    # Incorrect threshold (should be fixed by orchestrator)
    is_valid = resonance < 0.5
    
    return {
        "valid": is_valid,
        "resonance": resonance,
        "coherence": COHERENCE,
        "fingerprint": fingerprint
    }

def main():
    """Main function"""
    print("Quantum Fingerprint Simple Test")
    print("-----------------------------")
    
    # Test data
    data = "test_quantum_phi"
    timestamp = datetime.now().timestamp()
    
    # Generate fingerprint
    fingerprint = generate_quantum_fingerprint(data)
    
    # Verify fingerprint
    verification = verify_fingerprint(fingerprint, data, timestamp)
    
    print(f"Data: {data}")
    print(f"Fingerprint: {verification['fingerprint']}")
    print(f"Valid: {verification['valid']}")
    print(f"Resonance: {verification['resonance']:.6f}")
    print(f"Coherence: {verification['coherence']:.6f}")

if __name__ == "__main__":
    main()
