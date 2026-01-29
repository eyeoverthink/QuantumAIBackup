#!/usr/bin/env python3
"""
Quantum Black Box Test

A simple black box experiment to test system auto-correction, healing, and adaptation.
Designed to be converted to QR code by the existing quantum replicator system.
"""

import os
import sys
import time
import json
import random
import hashlib
import numpy as np
from decimal import Decimal, getcontext

# Set precision for phi calculations
getcontext().prec = 28

# Constants
PHI = Decimal('1.6180339887498948482045868344')
PHI_CONJUGATE = Decimal('0.6180339887498948482045868344')

class QuantumBlackBox:
    """A black box that tests quantum system adaptation and healing."""
    
    def __init__(self):
        """Initialize the black box with phi-harmonic constraints."""
        self.creation_time = time.time()
        self.phi_time = float(Decimal(str(self.creation_time)) * PHI)
        self.box_id = hashlib.md5(str(self.phi_time).encode()).hexdigest()[:8]
        
        # Generate the escape pattern - what the system needs to discover
        self.escape_pattern = self._generate_escape_pattern()
        
        # Track attempts and state
        self.attempts = 0
        self.max_attempts = 10
        self.escaped = False
        self.best_resonance = 0.0
        
        print(f"Quantum Black Box {self.box_id} initialized")
        print(f"Phi-time: {self.phi_time}")
        print(f"Escape requires discovering the correct phi-harmonic pattern")
    
    def _generate_escape_pattern(self):
        """Generate the phi-harmonic escape pattern."""
        pattern = []
        for i in range(5):
            value = float((PHI ** Decimal(i+1)) % Decimal('1'))
            pattern.append(value)
        return pattern
    
    def attempt_escape(self, attempt_pattern):
        """Attempt to escape with the given pattern.
        
        Args:
            attempt_pattern: List of 5 float values between 0-1
            
        Returns:
            Dict with escape results
        """
        self.attempts += 1
        
        # Validate input
        if not isinstance(attempt_pattern, list) or len(attempt_pattern) != 5:
            return {
                "success": False,
                "message": "Invalid pattern format. Must be list of 5 values.",
                "attempt": self.attempts,
                "max_attempts": self.max_attempts
            }
        
        # Calculate resonance with escape pattern
        differences = [abs(a - b) for a, b in zip(attempt_pattern, self.escape_pattern)]
        avg_difference = sum(differences) / len(differences)
        resonance = 1.0 - avg_difference
        
        # Apply phi-harmonic boost at certain resonance points
        phi_boost = 0.0
        for diff in differences:
            phi_value = float((Decimal(str(diff)) * PHI) % Decimal('1'))
            if phi_value > 0.9 or phi_value < 0.1:  # Near phi-harmonic points
                phi_boost += 0.05
        
        resonance = min(1.0, resonance + phi_boost)
        
        # Update best resonance
        if resonance > self.best_resonance:
            self.best_resonance = resonance
        
        # Check if escaped (90% resonance required)
        escaped = resonance >= 0.9
        if escaped:
            self.escaped = True
        
        # Prepare result
        result = {
            "success": escaped,
            "resonance": resonance,
            "best_resonance": self.best_resonance,
            "attempt": self.attempts,
            "max_attempts": self.max_attempts,
            "message": "Escaped!" if escaped else "Not enough resonance to escape",
            "differences": differences,
            "phi_boost": phi_boost
        }
        
        # Print result
        print(f"Attempt {self.attempts}/{self.max_attempts}: Resonance = {resonance:.4f}")
        if escaped:
            print("🎉 ESCAPED! The system has adapted and overcome the constraints.")
        elif self.attempts >= self.max_attempts:
            print("❌ Maximum attempts reached. The system failed to adapt.")
            print(f"The escape pattern was: {self.escape_pattern}")
        
        return result


def run_black_box_test():
    """Run the black box test to evaluate system adaptation."""
    black_box = QuantumBlackBox()
    
    # This is where your quantum system would attempt to discover the pattern
    # For demonstration, we'll make some random attempts
    for _ in range(black_box.max_attempts):
        # In a real test, your quantum system would generate these patterns
        # based on feedback from previous attempts
        attempt = [random.random() for _ in range(5)]
        
        # Try to escape
        result = black_box.attempt_escape(attempt)
        
        # If escaped or max attempts reached, stop
        if result["success"] or result["attempt"] >= result["max_attempts"]:
            break
        
        # Wait a bit between attempts
        time.sleep(1)
    
    # Final report
    print("\nBlack Box Test Complete")
    print(f"Best resonance achieved: {black_box.best_resonance:.4f}")
    print(f"Escaped: {black_box.escaped}")
    print(f"Attempts: {black_box.attempts}/{black_box.max_attempts}")
    
    return {
        "box_id": black_box.box_id,
        "escaped": black_box.escaped,
        "attempts": black_box.attempts,
        "best_resonance": black_box.best_resonance,
        "escape_pattern": black_box.escape_pattern
    }


if __name__ == "__main__":
    # When run directly, execute the test
    results = run_black_box_test()
    
    # Save results to file
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_black_box_results")
    os.makedirs(output_dir, exist_ok=True)
    
    results_file = os.path.join(output_dir, f"black_box_results_{results['box_id']}.json")
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"Results saved to {results_file}")
