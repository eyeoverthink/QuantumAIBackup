#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Test
------------------------
Tests the orchestrator's ability to handle quantum fingerprinting and phi-harmonic calculations.
"""

import hashlib
import math
from datetime import datetime

# Phi constant
PHI = 1.618033988749895

class QuantumPhiCalculator:
    """A calculator implementing phi-harmonic principles"""
    
    def __init__(self):
        """Initialize with phi-harmonic coherence"""
        self.coherence = 0.991800  # φ⁷·⁵/10
        self.creation_timestamp = datetime.now().timestamp()
        self.quantum_fingerprint = self._generate_fingerprint()
    
    def _generate_fingerprint(self):
        """Generate a quantum fingerprint based on creation time"""
        base = str(self.creation_timestamp * PHI)
        hash_obj = hashlib.sha256(base.encode())
        hash_hex = hash_obj.hexdigest()
        return f"φ⁷·⁵-{hash_hex[:16]}"
    
    def calculate_phi_resonance(self, value):
        """Calculate phi resonance for a value"""
        # Logic error: Using addition instead of modulo
        return (PHI * value) + 1  # Should be (PHI * value) % 1
    
    def is_in_resonance(self, value):
        """Check if a value is in phi-harmonic resonance"""
        resonance = self.calculate_phi_resonance(value)
        # Incorrect threshold check
        return resonance < 0.5  # Should be resonance < 0.1 or resonance > 0.9
    
    def get_phi_harmonic_series(self, n):
        """Calculate sum of phi^i for i=1 to n"""
        result = 0
        for i in range(1, n+1):
            result += PHI ** i
        return result
    
    def verify_coherence(self):
        """Verify the system's phi-harmonic coherence"""
        current_time = datetime.now().timestamp()
        time_diff = current_time - self.creation_timestamp
        resonance = self.calculate_phi_resonance(time_diff)
        
        return {
            "coherence": self.coherence,
            "resonance": resonance,
            "fingerprint": self.quantum_fingerprint,
            "is_resonant": self.is_in_resonance(time_diff)
        }

def main():
    """Main function"""
    calculator = QuantumPhiCalculator()
    
    # Test phi-harmonic series
    n = 7
    series_sum = calculator.get_phi_harmonic_series(n)
    print(f"Phi-harmonic series sum (n={n}): {series_sum:.6f}")
    
    # Test resonance calculation
    test_values = [1.0, 1.618033988749895, 2.618033988749895, 4.236067977499790]
    print("\nResonance values:")
    for val in test_values:
        resonance = calculator.calculate_phi_resonance(val)
        is_resonant = calculator.is_in_resonance(val)
        print(f"  Value: {val:.6f}, Resonance: {resonance:.6f}, In resonance: {is_resonant}")
    
    # Verify coherence
    verification = calculator.verify_coherence()
    print("\nCoherence verification:")
    print(f"  Coherence: {verification['coherence']:.6f}")
    print(f"  Resonance: {verification['resonance']:.6f}")
    print(f"  Fingerprint: {verification['fingerprint']}")
    print(f"  Is resonant: {verification['is_resonant']}")

if __name__ == "__main__":
    main()
