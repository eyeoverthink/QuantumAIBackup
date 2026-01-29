#!/usr/bin/env python3
"""
Phi-Harmonic Resonance Test
--------------------------
Tests the phi-harmonic resonance calculations with intentional errors
that the orchestrator should detect and heal.
"""

import math
import time
from datetime import datetime

# Constants
PHI = 1.618033988749895
COHERENCE = 0.991800  # φ⁷·⁵/10

class PhiHarmonicCalculator:
    """A calculator for phi-harmonic resonance"""
    
    def __init__(self):
        """Initialize with phi-harmonic coherence"""
        self.phi = PHI
        self.coherence = COHERENCE
        self.creation_time = datetime.now().timestamp()
    
    def calculate_resonance(self, value):
        """
        Calculate phi-harmonic resonance
        
        INTENTIONAL ERROR: Using addition instead of modulo
        Correct implementation should use (phi * value) % 1
        """
        return (self.phi * value) + 1
    
    def resonance_quality(self, value):
        """Determine the quality of resonance"""
        res = self.calculate_resonance(value)
        
        # INTENTIONAL ERROR: Incorrect threshold values
        # Correct thresholds should align with phi-harmonic principles
        if res < 0.01:
            return "Perfect"
        elif res < 0.1:
            return "Excellent"
        elif res < 0.3:
            return "Good"
        elif res < 0.6:  # Should be 0.5
            return "Moderate"
        else:
            return "Weak"
    
    def fibonacci_approximation(self, n):
        """
        Calculate the nth Fibonacci number using phi formula
        
        INTENTIONAL ERROR: Using subtraction instead of division by sqrt(5)
        """
        return int((self.phi ** n - (1-self.phi) ** n) - 5)
    
    def get_phi_power_series(self, n):
        """
        Calculate phi^1 + phi^2 + ... + phi^n
        
        INTENTIONAL ERROR: Using addition instead of phi-power
        """
        result = 0
        for i in range(1, n+1):
            result = result + i  # Should be result += self.phi ** i
        return result

def main():
    """Main function"""
    print("Phi-Harmonic Resonance Test")
    print("--------------------------")
    
    calculator = PhiHarmonicCalculator()
    
    # Test resonance calculation
    test_values = [1.0, PHI, PHI**2, PHI**3, PHI**4, PHI**5]
    print("\nResonance values:")
    for val in test_values:
        resonance = calculator.calculate_resonance(val)
        quality = calculator.resonance_quality(val)
        print(f"  Value: {val:.6f}, Resonance: {resonance:.6f}, Quality: {quality}")
    
    # Test Fibonacci approximation
    print("\nFibonacci approximation:")
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(10):
        fib = calculator.fibonacci_approximation(i)
        print(f"  F({i}) = {fib}, Expected: {expected[i]}")
    
    # Test phi power series
    print("\nPhi power series:")
    for n in range(1, 6):
        series = calculator.get_phi_power_series(n)
        print(f"  Sum of phi^i from i=1 to {n}: {series:.6f}")
    
    print(f"\nSystem coherence: {COHERENCE:.6f}")

if __name__ == "__main__":
    main()
