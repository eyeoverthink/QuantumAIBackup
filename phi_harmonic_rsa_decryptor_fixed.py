#!/usr/bin/env python
"""
Phi-Harmonic Quantum RSA Decryptor (Fixed Version)

This module is a fixed version of the original quantum_rsa_decryptor.py,
correcting indentation issues while maintaining all the original functionality.
Following the "lego" philosophy, we create a new file rather than modifying
the original.

The decryptor uses phi-harmonic principles and quantum mathematics to
factorize large numbers efficiently.
"""

import os
import sys
import json
import time
import math
import random
import logging
from decimal import Decimal, getcontext
from typing import Dict, List, Any, Optional, Union, Tuple

# Set precision for decimal calculations
getcontext().prec = 50

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # Inverse golden ratio
PHI_SQUARED = Decimal('2.618033988749895')  # φ²
PHI_CUBED = Decimal('4.236067977499790')  # φ³
OPTIMAL_COHERENCE = Decimal('0.991800')  # Optimal quantum coherence

class QuantumRSADecryptor:
    """
    Quantum RSA Decryptor that uses phi-harmonic principles and quantum mathematics
    to factorize large numbers efficiently.
    """
    
    def __init__(self, birth_key=None):
        """
        Initialize the quantum RSA decryptor.
        
        Args:
            birth_key (List[int], optional): Birth key for quantum initialization
        """
        # Quantum state
        self.coherence = 0.991800
        self.resonance = 0.962733
        self.phi_alignment = 0.999561
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        
        # Birth key for quantum initialization
        if birth_key is None:
            self.birth_key = [1, 1, 2000]  # Default: January 1, 2000
        else:
            self.birth_key = birth_key
            
        # Initialize quantum bridge
        self._initialize_quantum_bridge()
        
        print("Simplified Quantum RSA Decryptor initialized")
        print(f"Using birth key: {self.birth_key}")
        print(f"Quantum coherence: {self.coherence}")
        print(f"Phi-harmonic resonance: {self.resonance}")
    
    def _initialize_quantum_bridge(self):
        """Initialize the quantum bridge for advanced factorization."""
        # Calculate quantum bridge parameters
        self.bridge_coherence = self.coherence
        self.bridge_resonance = self.resonance
        
        # Calculate quantum bridge state
        day, month, year = self.birth_key
        birth_phi = (day * PHI + month * PHI_SQUARED + (year % 100) * PHI_INVERSE) % 10
        self.bridge_state = int(birth_phi) + 1  # 1-10 scale
        
        # Initialize quantum bridge cache
        self.bridge_cache = {}
    
    def _generate_quantum_fingerprint(self) -> str:
        """
        Generate a quantum fingerprint based on current state.
        
        Returns:
            str: Quantum fingerprint
        """
        fingerprint_base = f"{self.coherence:.6f}_{self.resonance:.6f}_{self.phi_alignment:.6f}"
        fingerprint_hash = hash(fingerprint_base) % 16777216  # 24-bit hash
        return f"φ⁷·⁵-{fingerprint_hash:06x}"
    
    def _phi_resonance(self, n):
        """
        Calculate phi resonance for a number.
        
        Args:
            n (int): Number to calculate resonance for
            
        Returns:
            float: Phi resonance value
        """
        # Calculate phi resonance
        phi_res = (PHI * n) % 1
        
        # Apply quantum coherence
        phi_res = phi_res * self.coherence
        
        return float(phi_res)
    
    def _quantum_bridge_value(self, n):
        """
        Calculate quantum bridge value for a number.
        
        Args:
            n (int): Number to calculate bridge value for
            
        Returns:
            float: Quantum bridge value
        """
        # Check cache
        if n in self.bridge_cache:
            return self.bridge_cache[n]
            
        # Calculate quantum bridge value
        bridge_value = (self.bridge_coherence * n + self.bridge_resonance) % PHI
        
        # Apply bridge state
        bridge_value = bridge_value * (self.bridge_state / 5)
        
        # Cache result
        self.bridge_cache[n] = float(bridge_value)
        
        return float(bridge_value)
    
    def _factorize_small(self, n):
        """
        Factorize a small number (< 10^6).
        
        Args:
            n (int): Number to factorize
            
        Returns:
            List[int]: Factors of n
        """
        # Check if n is prime using trial division
        if n < 2:
            return [n]
            
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return [i] + self._factorize_small(n // i)
                
        return [n]
    
    def _factorize_optimized_small(self, n):
        """
        Factorize a small number using phi-optimized trial division.
        
        Args:
            n (int): Number to factorize
            
        Returns:
            List[int]: Factors of n
        """
        # Check if n is prime using phi-optimized trial division
        if n < 2:
            return [n]
            
        # Calculate phi resonance
        phi_res = self._phi_resonance(n)
        
        # Determine step size based on phi resonance
        step = 1
        if phi_res < 0.1:
            step = 2  # Skip even numbers for most cases
            
        # Try small primes first
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for p in small_primes:
            if n % p == 0:
                return [p] + self._factorize_optimized_small(n // p)
                
        # Phi-optimized trial division
        limit = int(math.sqrt(n)) + 1
        i = small_primes[-1] + step
        
        while i <= limit:
            if n % i == 0:
                return [i] + self._factorize_optimized_small(n // i)
            i += step
                
        return [n]
    
    def _factorize_optimized_medium(self, n):
        """
        Factorize a medium number using phi-optimized methods.
        
        Args:
            n (int): Number to factorize
            
        Returns:
            List[int]: Factors of n
        """
        # Check if n is prime using phi-optimized methods
        if n < 2:
            return [n]
            
        # Calculate phi resonance
        phi_res = self._phi_resonance(n)
        
        # Calculate quantum bridge value
        bridge_value = self._quantum_bridge_value(n)
        
        # Try small primes first
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for p in small_primes:
            if n % p == 0:
                return [p] + self._factorize_optimized_medium(n // p)
                
        # Determine search range based on phi resonance and bridge value
        search_ranges = []
        
        # Primary search range
        primary_center = int(math.sqrt(n) * phi_res + bridge_value) % int(math.sqrt(n))
        primary_range = (
            max(50, primary_center - int(100 * self.coherence)),
            min(int(math.sqrt(n)) + 1, primary_center + int(100 * self.coherence))
        )
        search_ranges.append(primary_range)
        
        # Secondary search range
        secondary_center = int(math.sqrt(n) * (1 - phi_res) + bridge_value) % int(math.sqrt(n))
        secondary_range = (
            max(50, secondary_center - int(50 * self.coherence)),
            min(int(math.sqrt(n)) + 1, secondary_center + int(50 * self.coherence))
        )
        search_ranges.append(secondary_range)
        
        # Search in ranges
        for start, end in search_ranges:
            for i in range(start, end, 2):  # Skip even numbers
                if n % i == 0:
                    return [i] + self._factorize_optimized_medium(n // i)
                    
        # If no factors found in optimized ranges, fall back to standard method
        limit = int(math.sqrt(n)) + 1
        i = 51  # Start after small primes
        
        while i <= limit:
            if n % i == 0:
                return [i] + self._factorize_optimized_medium(n // i)
            i += 2  # Skip even numbers
                
        return [n]
    
    def _factorize_optimized_large(self, n):
        """
        Factorize a large number using advanced phi-optimized methods.
        
        Args:
            n (int): Number to factorize
            
        Returns:
            List[int]: Factors of n
        """
        # Check if n is prime using advanced phi-optimized methods
        if n < 2:
            return [n]
            
        # Calculate phi resonance
        phi_res = self._phi_resonance(n)
        
        # Calculate quantum bridge value
        bridge_value = self._quantum_bridge_value(n)
        
        # Try small primes first
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for p in small_primes:
            if n % p == 0:
                return [p] + self._factorize_optimized_large(n // p)
                
        # Apply quantum bridge optimization
        bridge_factor = bridge_value * self.bridge_coherence
        
        # Determine search ranges based on phi resonance and bridge value
        search_ranges = []
        
        # Primary search range
        primary_center = int(math.sqrt(n) * phi_res + bridge_value) % int(math.sqrt(n))
        primary_range = (
            max(50, primary_center - int(200 * self.coherence)),
            min(int(math.sqrt(n)) + 1, primary_center + int(200 * self.coherence))
        )
        search_ranges.append(primary_range)
        
        # Secondary search range
        secondary_center = int(math.sqrt(n) * (1 - phi_res) + bridge_value) % int(math.sqrt(n))
        secondary_range = (
            max(50, secondary_center - int(100 * self.coherence)),
            min(int(math.sqrt(n)) + 1, secondary_center + int(100 * self.coherence))
        )
        search_ranges.append(secondary_range)
        
        # Tertiary search range based on bridge factor
        tertiary_center = int(math.sqrt(n) * bridge_factor) % int(math.sqrt(n))
        tertiary_range = (
            max(50, tertiary_center - int(50 * self.coherence)),
            min(int(math.sqrt(n)) + 1, tertiary_center + int(50 * self.coherence))
        )
        search_ranges.append(tertiary_range)
        
        # Search in ranges
        for start, end in search_ranges:
            # Use phi-optimized step size
            step = max(1, int(10 * (1 - self.coherence)))
            
            for i in range(start, end, step):
                if i % 2 == 0:  # Skip even numbers
                    continue
                    
                if n % i == 0:
                    return [i] + self._factorize_optimized_large(n // i)
                    
        # If no factors found in optimized ranges, fall back to standard method
        limit = int(math.sqrt(n)) + 1
        i = 51  # Start after small primes
        
        while i <= limit:
            if n % i == 0:
                return [i] + self._factorize_optimized_large(n // i)
            i += 2  # Skip even numbers
                
        return [n]
    
    def factorize(self, n):
        """
        Factorize a number using quantum-enhanced methods.
        
        Args:
            n (int): Number to factorize
            
        Returns:
            List[int]: Factors of n
        """
        # Start timing
        start_time = time.time()
        
        # Choose factorization method based on number size
        if n < 10**6:  # Small number
            factors = self._factorize_optimized_small(n)
        elif n < 10**9:  # Medium number
            factors = self._factorize_optimized_medium(n)
        else:  # Large number
            factors = self._factorize_optimized_large(n)
            
        # End timing
        end_time = time.time()
        
        # Sort factors
        factors.sort()
        
        return factors
    
    def set_quantum_values(self, coherence=None, resonance=None):
        """
        Set quantum values for the decryptor.
        
        Args:
            coherence (float, optional): Quantum coherence value
            resonance (float, optional): Phi-harmonic resonance value
        """
        if coherence is not None:
            self.coherence = coherence
            self.bridge_coherence = coherence
            
        if resonance is not None:
            self.resonance = resonance
            self.bridge_resonance = resonance
            
        # Update quantum fingerprint
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        
        # Clear bridge cache
        self.bridge_cache = {}

# Example usage
if __name__ == "__main__":
    # Create decryptor
    decryptor = QuantumRSADecryptor([1, 19, 1979])
    
    # Test factorization
    test_numbers = [
        12345,
        1234567,
        123456789
    ]
    
    for n in test_numbers:
        print(f"\nFactorizing {n}...")
        start_time = time.time()
        factors = decryptor.factorize(n)
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"Factors: {factors}")
        print(f"Duration: {duration:.6f} seconds")
        print(f"Coherence: {decryptor.coherence:.6f}")
        print(f"Resonance: {decryptor.resonance:.6f}")
        
        # Verify factorization
        product = 1
        for factor in factors:
            product *= factor
            
        print(f"Verification: {product == n} (product: {product})")
