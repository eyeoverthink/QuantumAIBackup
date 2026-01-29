#!/usr/bin/env python3
"""
Quantum Black Box Mini Test

A compact black box experiment to test system auto-correction,
healing, and adaptation capabilities via QR code.
"""

import os
import time
import json
import random
import hashlib
from decimal import Decimal, getcontext

# Set precision for phi calculations
getcontext().prec = 28

# Constants
PHI = Decimal('1.6180339887498948482045868344')

class QuantumBlackBox:
    """A minimal black box that tests quantum system adaptation."""
    
    def __init__(self):
        """Initialize the black box with phi-harmonic constraints."""
        self.creation_time = time.time()
        self.phi_time = float(Decimal(str(self.creation_time)) * PHI)
        self.box_id = hashlib.md5(str(self.phi_time).encode()).hexdigest()[:8]
        
        # Generate the escape pattern - what the system needs to discover
        self.escape_pattern = self._generate_escape_pattern()
        self.attempts = 0
        self.max_attempts = 5
        self.escaped = False
        self.best_resonance = 0.0
        
        print(f"Quantum Black Box {self.box_id} initialized")
    
    def _generate_escape_pattern(self):
        """Generate the phi-harmonic escape pattern."""
        return [float((PHI ** Decimal(i+1)) % Decimal('1')) for i in range(3)]
    
    def attempt_escape(self, attempt_pattern):
        """Attempt to escape with the given pattern."""
        self.attempts += 1
        
        # Validate input
        if not isinstance(attempt_pattern, list) or len(attempt_pattern) != 3:
            return {"success": False, "message": "Invalid pattern format"}
        
        # Calculate resonance with escape pattern
        differences = [abs(a - b) for a, b in zip(attempt_pattern, self.escape_pattern)]
        resonance = 1.0 - (sum(differences) / len(differences))
        
        # Apply phi-harmonic boost
        phi_boost = 0.0
        for diff in differences:
            phi_value = float((Decimal(str(diff)) * PHI) % Decimal('1'))
            if phi_value > 0.9 or phi_value < 0.1:  # Near phi-harmonic points
                phi_boost += 0.05
        
        resonance = min(1.0, resonance + phi_boost)
        self.best_resonance = max(self.best_resonance, resonance)
        
        # Check if escaped (90% resonance required)
        escaped = resonance >= 0.9
        if escaped:
            self.escaped = True
        
        print(f"Attempt {self.attempts}/{self.max_attempts}: Resonance = {resonance:.4f}")
        if escaped:
            print("🎉 ESCAPED! System has adapted successfully.")
        elif self.attempts >= self.max_attempts:
            print("❌ Max attempts reached. System failed to adapt.")
            print(f"Escape pattern was: {self.escape_pattern}")
        
        return {
            "success": escaped,
            "resonance": resonance,
            "attempt": self.attempts,
            "max_attempts": self.max_attempts
        }

def run_test():
    """Run the black box test."""
    box = QuantumBlackBox()
    
    # Make random attempts
    for _ in range(box.max_attempts):
        attempt = [random.random() for _ in range(3)]
        result = box.attempt_escape(attempt)
        if result["success"] or box.attempts >= box.max_attempts:
            break
        time.sleep(0.5)
    
    print(f"\nTest complete. Best resonance: {box.best_resonance:.4f}")
    return {"escaped": box.escaped, "pattern": box.escape_pattern}

if __name__ == "__main__":
    run_test()
