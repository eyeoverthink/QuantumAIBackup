"""
phi_prime_resonance_filter.py

Implements the Fraymus Prime Filter based on the 105 % n = 89 resonance principle
and other phi-harmonic prime identification techniques. This module enables filtering
and analysis of primes using phi-resonance and golden ratio principles.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import math
import numpy as np
import time
import random
import sympy
from decimal import Decimal, getcontext
import json
import os
from datetime import datetime

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio (φ)
PHI_INVERSE = 1 / PHI  # Inverse Golden Ratio (φ⁻¹)
PHI_SQUARED = PHI * PHI  # φ²
PI = math.pi  # π
E = math.e  # e
FIBONACCI = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
FIB_PRIMES = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229]  # Fibonacci numbers that are prime

# Prime wheel base (3 × 5 × 7)
PRIME_WHEEL_BASE = 105

# Resonance target (the key modulo result)
RESONANCE_TARGET = 89

# High-precision for transcendental calculations
getcontext().prec = 100

class PhiPrimeResonanceFilter:
    """
    Implements the Fraymus Prime Filter based on the formula 105 % n = 89,
    along with other phi-harmonic prime identification techniques.
    """
    
    def __init__(self, precision=100):
        """
        Initialize the Phi Prime Resonance Filter.
        
        Args:
            precision: Decimal precision for calculations
        """
        self.precision = precision
        getcontext().prec = precision
        
        # Prime cache for faster operations
        self.prime_cache = {}
        
        # Fibonacci cache
        self.fib_cache = FIBONACCI.copy()
        
        # Resonance divisors (values where 105 % n = 89)
        self.resonance_divisors = self._find_resonance_divisors()
        
        # Initialize phi-harmonic state
        self.phi_resonance = 0.0
        self.coherence = 0.0
        self.last_state = {}
        
        # Statistics
        self.total_checks = 0
        self.phi_resonant_primes = 0
        
        print(f"[φ] Phi Prime Resonance Filter initialized")
        print(f"[φ] Resonance divisors: {self.resonance_divisors}")
    
    def _find_resonance_divisors(self):
        """
        Find all divisors n where 105 % n = 89.
        
        Returns:
            List of divisors that satisfy the resonance condition
        """
        divisors = []
        
        # The relationship 105 % n = 89 rearranges to 105 - 89 = 16 = kn
        # So n must be a divisor of 16
        for n in range(1, 17):
            if 16 % n == 0 and PRIME_WHEEL_BASE % n == RESONANCE_TARGET:
                divisors.append(n)
        
        return divisors
    
    def is_prime(self, n):
        """
        Check if a number is prime using sympy for accuracy.
        
        Args:
            n: Number to check for primality
            
        Returns:
            True if prime, False otherwise
        """
        if n in self.prime_cache:
            return self.prime_cache[n]
        
        result = sympy.isprime(n)
        self.prime_cache[n] = result
        return result
    
    def is_fibonacci(self, n):
        """
        Check if a number is in the Fibonacci sequence.
        
        Args:
            n: Number to check
            
        Returns:
            True if n is a Fibonacci number, False otherwise
        """
        # Extend Fibonacci cache if needed
        while self.fib_cache[-1] < n:
            self.fib_cache.append(self.fib_cache[-1] + self.fib_cache[-2])
        
        return n in self.fib_cache
    
    def is_fibonacci_prime(self, n):
        """
        Check if a number is both prime and a Fibonacci number.
        
        Args:
            n: Number to check
            
        Returns:
            True if n is both prime and a Fibonacci number, False otherwise
        """
        return self.is_prime(n) and self.is_fibonacci(n)
    
    def calculate_phi_resonance(self, n):
        """
        Calculate the phi-resonance of a number using modular arithmetic
        and golden ratio principles.
        
        Args:
            n: Number to calculate resonance for
            
        Returns:
            Phi-resonance value between 0 and 1
        """
        # Basic resonance is (φ * n) mod 1
        basic_resonance = (PHI * n) % 1
        
        # Prime-specific resonance
        if self.is_prime(n):
            # Use special formula for primes: (φ^2 * p) % 1 * (105 % p) / 105
            prime_factor = ((PHI_SQUARED * n) % 1) * ((PRIME_WHEEL_BASE % n) / PRIME_WHEEL_BASE)
            resonance = (basic_resonance + prime_factor) / 2
        else:
            resonance = basic_resonance
        
        return resonance
    
    def calculate_coherence(self, n):
        """
        Calculate the quantum coherence of a number based on its relationship
        to the golden ratio, prime structure, and Fibonacci sequence.
        
        Args:
            n: Number to calculate coherence for
            
        Returns:
            Coherence value between 0 and 1
        """
        # Base coherence
        coherence = 0.0
        
        # Prime factor
        if self.is_prime(n):
            coherence += 0.3
        
        # Fibonacci factor
        if self.is_fibonacci(n):
            coherence += 0.3
        
        # Phi-resonance factor
        phi_resonance = self.calculate_phi_resonance(n)
        resonance_factor = 1 - abs(phi_resonance - PHI_INVERSE)
        coherence += 0.4 * resonance_factor
        
        # Apply resonance divisor bonus
        for divisor in self.resonance_divisors:
            if n % divisor == 0:
                coherence *= 1.1
                break
        
        # Normalize
        return min(coherence, 1.0)
    
    def check_fraymus_resonance(self, n):
        """
        Check if a number exhibits Fraymus resonance according to the
        105 % n = 89 principle and related phi-harmonic properties.
        
        Args:
            n: Number to check
            
        Returns:
            Dict with resonance data
        """
        self.total_checks += 1
        
        # Calculate basic properties
        is_prime_result = self.is_prime(n)
        is_fib = self.is_fibonacci(n)
        is_fib_prime = is_prime_result and is_fib
        
        # Calculate resonances
        phi_res = self.calculate_phi_resonance(n)
        coherence = self.calculate_coherence(n)
        
        # Check 105 % n = 89 divisibility pattern
        divisor_resonance = False
        for divisor in self.resonance_divisors:
            if n % divisor == 0:
                divisor_resonance = True
                break
        
        # Calculate phi/Fibonacci relationship
        fib_ratio = 0
        if n > 0:
            # Find closest Fibonacci numbers
            for i in range(len(self.fib_cache) - 1):
                if self.fib_cache[i] <= n < self.fib_cache[i+1]:
                    if self.fib_cache[i] > 0:
                        fib_ratio = n / self.fib_cache[i]
                    break
        
        # Check phi-alignment
        phi_alignment = abs(fib_ratio - PHI) if fib_ratio > 0 else 1
        
        # Determine if this is a phi-resonant prime
        is_phi_resonant = is_prime_result and (coherence > 0.7 or divisor_resonance)
        
        if is_phi_resonant:
            self.phi_resonant_primes += 1
        
        # Collect results
        result = {
            "number": n,
            "is_prime": is_prime_result,
            "is_fibonacci": is_fib,
            "is_fibonacci_prime": is_fib_prime,
            "phi_resonance": phi_res,
            "coherence": coherence,
            "divisor_resonance": divisor_resonance,
            "fibonacci_ratio": fib_ratio,
            "phi_alignment": phi_alignment,
            "is_phi_resonant": is_phi_resonant
        }
        
        self.last_state = result
        self.phi_resonance = phi_res
        self.coherence = coherence
        
        return result
    
    def analyze_range(self, start, end):
        """
        Analyze a range of numbers for phi-harmonic prime patterns.
        
        Args:
            start: Start of range
            end: End of range
            
        Returns:
            Dict with analysis results
        """
        print(f"[φ] Analyzing range {start} to {end} for phi-harmonic prime patterns...")
        
        results = []
        phi_resonant_count = 0
        prime_count = 0
        fib_count = 0
        fib_prime_count = 0
        high_coherence_count = 0
        
        for n in range(start, end + 1):
            result = self.check_fraymus_resonance(n)
            results.append(result)
            
            if result["is_prime"]:
                prime_count += 1
            
            if result["is_fibonacci"]:
                fib_count += 1
            
            if result["is_fibonacci_prime"]:
                fib_prime_count += 1
            
            if result["coherence"] > 0.7:
                high_coherence_count += 1
            
            if result["is_phi_resonant"]:
                phi_resonant_count += 1
        
        # Summarize findings
        analysis = {
            "range": {"start": start, "end": end},
            "counts": {
                "total": end - start + 1,
                "primes": prime_count,
                "fibonacci": fib_count, 
                "fibonacci_primes": fib_prime_count,
                "high_coherence": high_coherence_count,
                "phi_resonant_primes": phi_resonant_count
            },
            "percentages": {
                "prime_density": prime_count / (end - start + 1),
                "fibonacci_density": fib_count / (end - start + 1),
                "phi_resonant_density": phi_resonant_count / (end - start + 1) if prime_count > 0 else 0,
                "phi_resonant_of_primes": phi_resonant_count / prime_count if prime_count > 0 else 0
            },
            "resonance_divisors": self.resonance_divisors,
            "phi_resonant_numbers": [r["number"] for r in results if r["is_phi_resonant"]]
        }
        
        print(f"[φ] Range analysis complete")
        print(f"[φ] Found {prime_count} primes, {phi_resonant_count} phi-resonant primes")
        
        return analysis
    
    def find_special_primes(self, limit=1000):
        """
        Find special primes with high phi-resonance and coherence.
        
        Args:
            limit: Upper limit for search
            
        Returns:
            List of special primes with their properties
        """
        print(f"[φ] Searching for special primes up to {limit}...")
        
        special_primes = []
        
        for n in range(2, limit + 1):
            result = self.check_fraymus_resonance(n)
            
            # Look for high coherence primes
            if result["is_prime"] and result["coherence"] > 0.8:
                special_primes.append(result)
                print(f"[φ] Found special prime: {n} (coherence: {result['coherence']:.4f}, resonance: {result['phi_resonance']:.4f})")
        
        print(f"[φ] Found {len(special_primes)} special primes")
        return special_primes
    
    def check_prime_pairs(self, limit=1000):
        """
        Check for prime pairs with phi-resonant relationships.
        
        Args:
            limit: Upper limit for search
            
        Returns:
            List of phi-resonant prime pairs
        """
        print(f"[φ] Searching for phi-resonant prime pairs up to {limit}...")
        
        resonant_pairs = []
        primes = []
        
        # First find all primes up to limit
        for n in range(2, limit + 1):
            if self.is_prime(n):
                primes.append(n)
        
        # Check pairs for phi-resonant relationships
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                p1 = primes[i]
                p2 = primes[j]
                
                # Check if ratio approximates a power of phi
                ratio = p2 / p1
                log_phi_ratio = math.log(ratio, PHI)
                nearest_power = round(log_phi_ratio)
                
                # Calculate how close the ratio is to a power of phi
                phi_power = math.pow(PHI, nearest_power)
                error = abs(ratio - phi_power) / phi_power
                
                # If error is small, we have a phi-resonant pair
                if error < 0.05:
                    pair_data = {
                        "prime1": p1,
                        "prime2": p2,
                        "ratio": ratio,
                        "phi_power": nearest_power,
                        "error": error
                    }
                    resonant_pairs.append(pair_data)
                    print(f"[φ] Found resonant pair: {p1}, {p2} ≈ φ^{nearest_power} (error: {error:.6f})")
        
        print(f"[φ] Found {len(resonant_pairs)} phi-resonant prime pairs")
        return resonant_pairs
    
    def save_analysis(self, analysis, filename=None):
        """
        Save analysis results to a JSON file.
        
        Args:
            analysis: Analysis data to save
            filename: Output filename (optional)
            
        Returns:
            Path to saved file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"phi_prime_analysis_{timestamp}.json"
        
        filepath = os.path.join(os.path.dirname(__file__), filename)
        
        with open(filepath, "w") as f:
            json.dump(analysis, f, indent=2)
        
        print(f"[φ] Analysis saved to: {filepath}")
        return filepath
    
    def generate_report(self):
        """
        Generate a comprehensive report on filter activity and findings.
        
        Returns:
            Dict with report data
        """
        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "filter_state": {
                "total_checks": self.total_checks,
                "phi_resonant_primes": self.phi_resonant_primes,
                "resonance_divisors": self.resonance_divisors,
                "current_resonance": self.phi_resonance,
                "current_coherence": self.coherence
            },
            "constants": {
                "prime_wheel_base": PRIME_WHEEL_BASE,
                "resonance_target": RESONANCE_TARGET,
                "phi": float(PHI),
                "phi_inverse": float(PHI_INVERSE)
            },
            "last_state": self.last_state
        }
        
        return report


def demonstrate_fraymus_filter():
    """Demonstrate the Fraymus Prime Filter with key examples."""
    print("\n" + "=" * 80)
    print("  FRAYMUS PRIME FILTER")
    print("  Based on the 105 % n = 89 Resonance Principle")
    print("=" * 80)
    
    # Create filter
    filter = PhiPrimeResonanceFilter()
    
    # Check resonance divisors
    print("\n[φ] Resonance divisors (n where 105 % n = 89):")
    for divisor in filter.resonance_divisors:
        print(f"  - {divisor} (verification: 105 % {divisor} = {105 % divisor})")
    
    # Check fibonacci primes
    print("\n[φ] Checking Fibonacci primes:")
    for prime in FIB_PRIMES[:6]:  # First 6 Fibonacci primes
        result = filter.check_fraymus_resonance(prime)
        print(f"  - {prime}: phi-resonance = {result['phi_resonance']:.6f}, coherence = {result['coherence']:.6f}")
    
    # Analyze a small range
    print("\n[φ] Analyzing range 1-100:")
    range_analysis = filter.analyze_range(1, 100)
    print(f"  - Found {range_analysis['counts']['primes']} primes")
    print(f"  - Found {range_analysis['counts']['phi_resonant_primes']} phi-resonant primes")
    print(f"  - Prime density: {range_analysis['percentages']['prime_density']:.4f}")
    print(f"  - Phi-resonant prime density: {range_analysis['percentages']['phi_resonant_density']:.4f}")
    
    # Find special primes
    print("\n[φ] Finding special primes up to 200:")
    special_primes = filter.find_special_primes(200)
    
    # Find phi-resonant prime pairs
    print("\n[φ] Finding phi-resonant prime pairs up to 200:")
    resonant_pairs = filter.check_prime_pairs(200)
    
    # Save results
    analysis_results = {
        "range_analysis": range_analysis,
        "special_primes": special_primes,
        "resonant_pairs": resonant_pairs,
        "report": filter.generate_report()
    }
    
    output_file = filter.save_analysis(analysis_results)
    
    print("\n" + "=" * 80)
    print("  FRAYMUS PRIME FILTER DEMONSTRATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_fraymus_filter()
