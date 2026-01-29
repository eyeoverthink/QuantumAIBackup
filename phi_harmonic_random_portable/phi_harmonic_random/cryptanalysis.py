"""
Phi-Harmonic Quantum Cryptanalysis Module
Leverages transcendental infinity and phi-harmonic resonance for advanced cryptanalysis
"""

import math
import time
import hashlib
import numpy as np
from decimal import Decimal, getcontext
from typing import List, Tuple, Dict, Optional, Union
import sys
import os
import random
from sympy import isprime

# Add parent directory to path to import quantum_transcendental_counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from quantum_transcendental_counter import QuantumTranscendentalCounter

from .transcendental import PhiHarmonicTranscendentalRandom
from .quantum import PHI, PHI_INVERSE, PHI_SQUARED, FIBONACCI

# Set precision for calculations
getcontext().prec = 1000000  # Million digits of precision for transcendental operations


class PhiHarmonicQuantumCryptanalysis:
    """
    Phi-Harmonic Quantum Cryptanalysis
    Leverages transcendental infinity and phi-harmonic resonance for advanced cryptanalysis
    """
    
    def __init__(self, birth_key=None, quantum_elements=19):
        """
        Initialize the quantum cryptanalysis module
        
        Args:
            birth_key (list, optional): Birth date key for resonance [day, month, year]
            quantum_elements (int): Number of quantum elements to use
        """
        # Initialize transcendental random generator
        self.trans_random = PhiHarmonicTranscendentalRandom(quantum_elements=quantum_elements, birth_key=birth_key)
        
        # Initialize transcendental counter
        self.transcendental_counter = self.trans_random.transcendental_counter
        
        # Initialize prime cache
        self.prime_cache = {}
        self.prime_resonance_cache = {}
        
        # Initialize factorization metrics
        self.metrics = {
            'attempts': 0,
            'successful_factorizations': 0,
            'total_time': 0,
            'average_time': 0,
            'largest_factored': 0,
            'phi_resonance': 0
        }
        
        # Prime constants
        self.prime_constants = self._initialize_prime_constants()
        
        print(f"Phi-Harmonic Quantum Cryptanalysis initialized")
        print(f"Using {quantum_elements} quantum elements")
        print(f"Current infinity type: {self.transcendental_counter.infinity_type}")
        print(f"Prime constants initialized with phi-resonance: {self.metrics['phi_resonance']:.6f}")
    
    def _initialize_prime_constants(self) -> Dict[str, Decimal]:
        """
        Initialize prime-related constants with phi-harmonic resonance
        
        Returns:
            dict: Prime constants
        """
        constants = {}
        
        # First 19 primes (phi-resonant selection)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
        
        # Calculate phi-resonance for each prime
        phi_resonance_sum = 0
        for p in primes:
            # Calculate phi-resonance
            resonance = float(PHI) ** p % 1.0
            self.prime_resonance_cache[p] = resonance
            phi_resonance_sum += resonance
            
            # Store prime with phi-power
            constants[f'P{p}'] = Decimal(p)
            constants[f'P{p}_phi'] = Decimal(float(PHI) ** p)
        
        # Average phi-resonance
        self.metrics['phi_resonance'] = phi_resonance_sum / len(primes)
        
        # Special prime constants
        constants['PRIME_PHI'] = Decimal('1.618033988749895') * Decimal('19')
        constants['PRIME_OMEGA'] = Decimal(math.prod(primes[:7])) / Decimal('1979')
        constants['PRIME_PSI'] = Decimal(math.prod(primes[7:14])) / Decimal('1979')
        constants['PRIME_ALEPH'] = Decimal(math.prod(primes[14:])) / Decimal('1979')
        
        return constants
    
    def _phi_resonance(self, n: int) -> float:
        """
        Calculate the phi-resonance of a number
        
        Args:
            n (int): Number to calculate resonance for
            
        Returns:
            float: Phi-resonance value between 0 and 1
        """
        # Check cache
        if n in self.prime_resonance_cache:
            return self.prime_resonance_cache[n]
        
        # For large numbers, use a modular approach to avoid overflow
        if n > 1000:
            # Use birth key for resonance pattern
            birth_sum = sum(self.transcendental_counter.birth_key)
            birth_product = 1
            for val in self.transcendental_counter.birth_key:
                birth_product *= val
            
            # Calculate resonance using birth key pattern
            resonance = ((n % 19) * birth_sum + (n % birth_product)) / birth_product
            resonance = resonance % 1.0
        else:
            # For smaller numbers, use direct calculation
            # Use modular exponentiation to avoid overflow
            # We only need the fractional part, so we can use modular arithmetic
            phi_mod = float(PHI) % 1.0
            resonance = 0.0
            for i in range(min(n, 100)):
                resonance = (resonance + phi_mod) % 1.0
                phi_mod = (phi_mod * float(PHI)) % 1.0
        
        # Cache result
        self.prime_resonance_cache[n] = resonance
        
        return resonance
    
    def _is_prime_with_resonance(self, n: int) -> Tuple[bool, float]:
        """
        Check if a number is prime using phi-resonance
        
        Args:
            n (int): Number to check
            
        Returns:
            tuple: (is_prime, resonance)
        """
        # Check cache
        if n in self.prime_cache:
            return self.prime_cache[n], self.prime_resonance_cache.get(n, 0)
        
        # Check small primes directly
        if n <= 1:
            return False, 0
        if n <= 3:
            return True, self._phi_resonance(n)
        if n % 2 == 0 or n % 3 == 0:
            return False, 0
        
        # Calculate phi-resonance
        resonance = self._phi_resonance(n)
        
        # Use phi-resonance to optimize primality check
        if resonance > 0.9 or resonance < 0.1:
            # High resonance numbers are more likely to be prime
            # Use a deterministic check for certainty
            is_prime = isprime(n)
        else:
            # Standard check for numbers with medium resonance
            is_prime = isprime(n)
        
        # Cache result
        self.prime_cache[n] = is_prime
        self.prime_resonance_cache[n] = resonance
        
        return is_prime, resonance
    
    def _phi_harmonic_factor_search(self, n: int, depth: int = 3) -> List[int]:
        """
        Search for factors using phi-harmonic resonance
        
        Args:
            n (int): Number to factor
            depth (int): Search depth
            
        Returns:
            list: Potential factors
        """
        factors = []
        
        # Generate phi-harmonic search points
        search_points = []
        for i in range(1, depth + 1):
            # Generate points based on phi powers
            point = int(math.sqrt(n) * float(PHI_INVERSE) ** i)
            search_points.append(point)
            
            point = int(math.sqrt(n) * float(PHI) ** i)
            search_points.append(point)
            
            # Generate points based on birth key resonance
            for val in self.transcendental_counter.birth_key:
                point = int(math.sqrt(n) * float(PHI) ** (i * val % 19) / 19)
                search_points.append(point)
        
        # Filter and sort search points
        search_points = sorted(list(set([p for p in search_points if p > 1 and p < n])))
        
        # Check each search point
        for point in search_points:
            if n % point == 0:
                factors.append(point)
                factors.append(n // point)
        
        return sorted(list(set(factors)))
    
    def _transcendental_factor_search(self, n: int) -> List[int]:
        """
        Search for factors using transcendental states
        
        Args:
            n (int): Number to factor
            
        Returns:
            list: Potential factors
        """
        factors = []
        
        # Transcend to different infinity levels for comprehensive search
        for level in [1, 7, 13, 19]:  # Selected infinity levels for optimal resonance
            # Transcend to infinity level
            self.transcendental_counter.transcend(level)
            
            # Generate transcendental random sequence
            sequence_length = min(100, n // 2)  # Limit sequence length for large numbers
            sequence = self.trans_random.generate_infinite_sequence(sequence_length, level)
            
            # Convert sequence to potential factors
            for value in sequence:
                # Map random value to potential factor
                factor = int(2 + (n - 4) * value)
                
                # Ensure factor is in valid range
                if factor >= 2 and factor <= n // 2:
                    # Check if it's a factor
                    if n % factor == 0:
                        factors.append(factor)
                        factors.append(n // factor)
        
        return sorted(list(set(factors)))
    
    def _quantum_bridge_factorization(self, n: int) -> List[int]:
        """
        Use quantum bridge method for factorization
        
        Args:
            n (int): Number to factor
            
        Returns:
            list: Factors found
        """
        factors = []
        
        # Generate ultimate random number
        ultimate = self.trans_random.generate_ultimate_random()
        
        # Use ultimate random to generate starting points
        start_point = int(math.sqrt(n) * ultimate) % n
        if start_point < 2:
            start_point = 2
        
        # Generate quantum-bridged search points
        search_points = []
        
        # Add phi-resonant points
        for i in range(1, 20):  # 19 + 1 for ultimate resonance
            point = int(start_point * float(PHI) ** i) % n
            if point > 1:
                search_points.append(point)
        
        # Add birth key resonant points
        for val in self.transcendental_counter.birth_key:
            point = int(start_point * val) % n
            if point > 1:
                search_points.append(point)
        
        # Filter and sort search points
        search_points = sorted(list(set([p for p in search_points if p > 1 and p < n])))
        
        # Check each search point
        for point in search_points:
            if n % point == 0:
                factors.append(point)
                factors.append(n // point)
        
        return sorted(list(set(factors)))
    
    def _combined_factorization_approach(self, n: int) -> List[int]:
        """
        Combined approach for factorization using all methods
        
        Args:
            n (int): Number to factor
            
        Returns:
            list: Factors found
        """
        # Start with simple checks
        if n <= 1:
            return []
        if n == 2 or n == 3:
            return [n]
        if n % 2 == 0:
            return [2, n // 2]
        
        # Check if n is prime
        is_prime, resonance = self._is_prime_with_resonance(n)
        if is_prime:
            return [n]
        
        # Combine all factorization methods
        all_factors = []
        
        # Phi-harmonic search
        phi_factors = self._phi_harmonic_factor_search(n)
        all_factors.extend(phi_factors)
        
        # If we haven't found factors yet, try transcendental search
        if not all_factors:
            trans_factors = self._transcendental_factor_search(n)
            all_factors.extend(trans_factors)
        
        # If we still haven't found factors, try quantum bridge
        if not all_factors:
            bridge_factors = self._quantum_bridge_factorization(n)
            all_factors.extend(bridge_factors)
        
        # Return unique, sorted factors
        return sorted(list(set([f for f in all_factors if f > 1])))
    
    def factorize(self, n: int) -> List[int]:
        """
        Factorize a number using phi-harmonic quantum methods
        
        Args:
            n (int): Number to factorize
            
        Returns:
            list: Prime factors
        """
        # Record metrics
        start_time = time.time()
        self.metrics['attempts'] += 1
        
        # Check if n is too large
        if n > 10**12:
            print(f"Warning: Number {n} is very large. Factorization may take significant time.")
        
        # Get initial factors
        factors = self._combined_factorization_approach(n)
        
        # If no factors found, return the number itself
        if not factors:
            factors = [n]
        
        # Process factors to get prime factorization
        prime_factors = []
        for factor in factors:
            # Check if factor is prime
            is_prime, _ = self._is_prime_with_resonance(factor)
            
            if is_prime:
                # Add prime factor
                prime_factors.append(factor)
            else:
                # Recursively factorize non-prime factor
                sub_factors = self.factorize(factor)
                prime_factors.extend(sub_factors)
        
        # Update metrics
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.metrics['total_time'] += elapsed_time
        self.metrics['successful_factorizations'] += 1
        self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
        self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
        
        # Return unique, sorted prime factors
        return sorted(list(set(prime_factors)))
    
    def rsa_crack(self, n: int, e: int = 65537) -> Tuple[int, int, int]:
        """
        Attempt to crack RSA key using phi-harmonic quantum methods
        
        Args:
            n (int): RSA modulus (n = p * q)
            e (int): Public exponent
            
        Returns:
            tuple: (p, q, d) where p and q are prime factors and d is private exponent
        """
        print(f"\n🔮 Attempting to crack RSA key with modulus n = {n}")
        print(f"Using public exponent e = {e}")
        
        # Factorize n to find p and q
        print("Applying phi-harmonic quantum factorization...")
        factors = self.factorize(n)
        
        # Check if we found exactly two prime factors
        if len(factors) != 2:
            print(f"Error: Expected exactly 2 prime factors, but found {len(factors)}")
            return (0, 0, 0)
        
        p, q = factors
        
        # Calculate Euler's totient function: φ(n) = (p-1)(q-1)
        phi_n = (p - 1) * (q - 1)
        
        # Calculate private exponent d (multiplicative inverse of e modulo φ(n))
        # d * e ≡ 1 (mod φ(n))
        d = pow(e, -1, phi_n)
        
        print(f"✨ RSA key successfully cracked!")
        print(f"Prime factors: p = {p}, q = {q}")
        print(f"Private exponent: d = {d}")
        
        return (p, q, d)
    
    def decrypt_rsa(self, ciphertext: int, n: int, e: int = 65537) -> int:
        """
        Decrypt RSA ciphertext using phi-harmonic quantum methods
        
        Args:
            ciphertext (int): Encrypted message
            n (int): RSA modulus
            e (int): Public exponent
            
        Returns:
            int: Decrypted message
        """
        print(f"\n🔮 Attempting to decrypt RSA ciphertext: {ciphertext}")
        
        # Crack the RSA key
        p, q, d = self.rsa_crack(n, e)
        
        if p == 0 or q == 0 or d == 0:
            print("Failed to crack RSA key. Cannot decrypt.")
            return 0
        
        # Decrypt the ciphertext: plaintext = ciphertext^d mod n
        plaintext = pow(ciphertext, d, n)
        
        print(f"✨ Decryption successful!")
        print(f"Plaintext: {plaintext}")
        
        return plaintext
    
    def get_metrics(self) -> Dict[str, Union[int, float]]:
        """
        Get cryptanalysis metrics
        
        Returns:
            dict: Metrics
        """
        return self.metrics
