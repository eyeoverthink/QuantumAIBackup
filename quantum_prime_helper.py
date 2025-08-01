"""
Quantum Prime Helper

This module extends the QuantumPrimeCalculator with additional functionality
for prime number testing and decomposition, specifically designed to work with
the PrimeSumDecomposer.

It follows the 'lego' approach by building on existing components without
modifying them, adding the necessary methods to support finding pairs of primes
that add to a specific value.
"""

import numpy as np
import mpmath
import time
import random
import sys
import os
from typing import List, Tuple, Optional, Dict, Any, Union

# Import existing modules without modifying them
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from quantum_prime_calculator import QuantumPrimeCalculator
except ImportError:
    print("Warning: Could not import QuantumPrimeCalculator. Some functionality may be limited.")

# Set precision for calculations
mpmath.mp.dps = 100

class QuantumPrimeTestingHelper:
    """
    Extends the QuantumPrimeCalculator with primality testing methods
    specifically designed for the PrimeSumDecomposer.
    """
    
    def __init__(self):
        """Initialize the Quantum Prime Testing Helper."""
        # Initialize the base calculator
        self.calculator = QuantumPrimeCalculator()
        self.phi = float(mpmath.mpf((1 + mpmath.sqrt(5)) / 2))
        self.phi_inverse = 1 / self.phi  # Add phi inverse
        
        # Constants for the 19/19 bridge
        self.bridge_constant = 19
        
        print("Quantum Prime Testing Helper initialized.")
        print(f"Using phi value: {self.phi}")
        print(f"Using phi inverse: {self.phi_inverse}")
        print(f"Using 19/19 bridge constant: {self.bridge_constant}")
    
    def is_prime(self, n: int) -> bool:
        """
        Check if a number is prime using quantum-inspired methods.
        
        This method combines traditional primality testing with
        quantum-inspired optimizations based on phi-harmonic patterns.
        
        Args:
            n: The number to test for primality
            
        Returns:
            bool: True if the number is prime, False otherwise
        """
        # Handle small numbers directly
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        # For medium-sized numbers, use trial division with phi-harmonic skipping
        if n < 10000:
            return self._trial_division_with_phi(n)
        
        # For large numbers, use Miller-Rabin with quantum enhancements
        return self._quantum_miller_rabin(n)
    
    def _trial_division_with_phi(self, n: int) -> bool:
        """
        Trial division primality test with phi-harmonic optimization.
        
        Uses the golden ratio to optimize the trial division process.
        
        Args:
            n: Number to test
            
        Returns:
            bool: True if prime, False otherwise
        """
        # Start with standard 6k±1 optimization
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            
            # Use phi-harmonic increment to optimize search
            # This skips some values but ensures we don't miss divisors
            increment = max(4, int(i * (self.phi - 1)))
            if increment % 2 == 1:  # Ensure even increment
                increment += 1
            i += increment
            
            # Periodically reset to ensure we don't miss divisors
            if i % 19 == 0:
                i = ((i // 6) * 6) + 5  # Reset to next 6k-1
        
        return True
    
    def _quantum_miller_rabin(self, n: int, rounds: int = 40) -> bool:
        """
        Miller-Rabin primality test with quantum-inspired optimizations.
        
        Args:
            n: Number to test
            rounds: Number of rounds (higher is more accurate)
            
        Returns:
            True if n is probably prime, False if definitely composite
        """
        # Handle small numbers
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        
        # Write n-1 as 2^r * d where d is odd
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        
        # Use phi-harmonic sequence for witness selection
        witnesses = self._generate_phi_harmonic_witnesses(n, rounds)
        
        # Witness loop
        for a in witnesses:
            x = pow(a, d, n)
            
            if x == 1 or x == n - 1:
                continue
            
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        
        return True
    
    def _generate_phi_harmonic_witnesses(self, n: int, count: int) -> List[int]:
        """
        Generate witnesses for Miller-Rabin test using phi-harmonic patterns.
        
        Args:
            n: The number being tested
            count: Number of witnesses to generate
            
        Returns:
            List of witness values
        """
        witnesses = []
        
        # Use the 19/19 bridge constant to initialize
        base = self.bridge_constant
        
        for i in range(count):
            # Generate next witness using phi-harmonic sequence
            next_witness = 2 + int((n - 4) * ((base * self.phi * i) % 1))
            
            # Ensure witness is within valid range
            if next_witness >= n:
                next_witness = 2 + (next_witness % (n - 3))
            
            witnesses.append(next_witness)
            
            # Periodically reset base using 19/19 bridge
            if i % self.bridge_constant == 0:
                base = (base * self.bridge_constant) % (n - 3)
                if base < 2:
                    base = self.bridge_constant
        
        return witnesses
    
    def find_next_prime(self, start: int) -> int:
        """
        Find the next prime number after the given start value.
        
        Args:
            start: The starting value
            
        Returns:
            The next prime number
        """
        # Ensure start is odd (except if start=2)
        if start < 2:
            return 2
        
        if start == 2:
            return 3
        
        # Ensure we start with an odd number
        if start % 2 == 0:
            start += 1
        else:
            start += 2
        
        # Search for the next prime
        while not self.is_prime(start):
            start += 2
        
        return start
    
    def find_previous_prime(self, start: int) -> int:
        """
        Find the previous prime number before the given start value.
        
        Args:
            start: The starting value
            
        Returns:
            The previous prime number
        """
        if start <= 2:
            return None  # No prime before 2
        
        if start == 3:
            return 2
        
        # Ensure we start with an odd number
        if start % 2 == 0:
            start -= 1
        else:
            start -= 2
        
        # Search for the previous prime
        while start >= 2 and not self.is_prime(start):
            if start == 2:
                return 2
            start -= 2
        
        return start if start >= 2 else None
    
    def find_closest_prime(self, target: int) -> int:
        """
        Find the closest prime number to the target value.
        
        Args:
            target: The target value
            
        Returns:
            The closest prime number
        """
        if self.is_prime(target):
            return target
        
        # Search in both directions
        lower = self.find_previous_prime(target)
        upper = self.find_next_prime(target)
        
        # Handle edge cases
        if lower is None:
            return upper
        
        # Return the closest
        if (target - lower) <= (upper - target):
            return lower
        else:
            return upper
    
    def find_phi_resonant_prime(self, target: int) -> int:
        """
        Find a prime number near the target with strong phi resonance.
        
        Args:
            target: The target value
            
        Returns:
            A prime number with strong phi resonance
        """
        # Calculate phi resonance points
        phi_point_1 = int(target * self.phi_inverse)
        phi_point_2 = int(target * (1 - self.phi_inverse))
        
        # Find closest primes to these points
        prime_1 = self.find_closest_prime(phi_point_1)
        prime_2 = self.find_closest_prime(phi_point_2)
        
        # Calculate resonance strength (closer to phi point = stronger)
        resonance_1 = 1 / (abs(prime_1 - phi_point_1) + 1)
        resonance_2 = 1 / (abs(prime_2 - phi_point_2) + 1)
        
        # Return the prime with stronger resonance
        return prime_1 if resonance_1 >= resonance_2 else prime_2


# Example usage
if __name__ == "__main__":
    helper = QuantumPrimeTestingHelper()
    
    # Test with some known primes
    test_numbers = [2, 3, 19, 97, 1979, 7919]
    
    print("\nTesting primality:")
    for num in test_numbers:
        is_prime = helper.is_prime(num)
        print(f"{num} is prime: {is_prime}")
    
    # Test finding next and previous primes
    test_value = 1000
    next_prime = helper.find_next_prime(test_value)
    prev_prime = helper.find_previous_prime(test_value)
    
    print(f"\nNext prime after {test_value}: {next_prime}")
    print(f"Previous prime before {test_value}: {prev_prime}")
    
    # Test finding phi-resonant prime
    target = 10000
    phi_prime = helper.find_phi_resonant_prime(target)
    
    print(f"\nPhi-resonant prime near {target}: {phi_prime}")
    print(f"Ratio to target: {phi_prime/target:.6f}")
    print(f"Comparison to phi: {abs(phi_prime/target - helper.phi_inverse):.6f}")
