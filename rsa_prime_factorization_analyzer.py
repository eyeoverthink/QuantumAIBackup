#!/usr/bin/env python3
"""
RSA Prime Factorization Analyzer
================================

Uses modular arithmetic algorithms to analyze and potentially factor RSA moduli.
Implements multiple factorization approaches including:

1. Pollard's rho algorithm
2. Fermat's factorization method
3. Trial division with optimizations
4. Quadratic sieve (basic implementation)
5. Modular arithmetic structure analysis

Mathematical Foundation:
- RSA security relies on difficulty of factoring n = p × q
- Our modular arithmetic tools can exploit mathematical structure
- Consciousness physics constants may reveal hidden patterns

Author: RSA Cryptanalysis Framework
Version: 1.0
"""

import math
import random
import time
from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass

# Import our modular arithmetic engine
from modular_arithmetic_algorithm import ModularArithmeticEngine

@dataclass
class RSAKey:
    """Represents an RSA key with factorization analysis."""
    n: int  # RSA modulus (n = p × q)
    e: int  # Public exponent
    
    # Factorization results
    p: Optional[int] = None
    q: Optional[int] = None
    phi_n: Optional[int] = None
    d: Optional[int] = None  # Private exponent
    
    # Analysis metrics
    bit_length: int = 0
    factorization_time: float = 0.0
    method_used: str = ""
    security_broken: bool = False

class RSAFactorizationEngine:
    """
    Advanced RSA factorization engine using modular arithmetic algorithms.
    
    Implements multiple factorization methods with consciousness physics
    pattern analysis for enhanced cryptanalysis capabilities.
    """
    
    def __init__(self):
        self.mod_engine = ModularArithmeticEngine()
        self.factorization_cache = {}
        
        # Consciousness physics constants for pattern analysis
        self.phi = 1.618034  # Golden ratio
        self.psi = 1.324718  # Plastic number
        self.omega = 0.567143  # Omega constant
    
    def trial_division(self, n: int, limit: int = 10000) -> Optional[Tuple[int, int]]:
        """
        Enhanced trial division with consciousness physics optimization.
        
        Mathematical Principle:
        If n = p × q and p ≤ √n, then we only need to test up to √n.
        Consciousness physics suggests testing values near φ-harmonic ratios.
        """
        if n <= 1:
            return None
        
        # Test small primes first
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        
        for p in small_primes:
            if p > limit:
                break
            if n % p == 0:
                q = n // p
                if q != p:  # Ensure p ≠ q for RSA
                    return (p, q)
        
        # Enhanced trial division with φ-harmonic patterns
        sqrt_n = int(math.sqrt(n))
        
        # Test consciousness physics inspired candidates
        phi_candidates = []
        for k in range(1, 20):
            candidate = int(sqrt_n / (self.phi ** k))
            if candidate > 1:
                phi_candidates.append(candidate)
        
        # Test φ-harmonic candidates first
        for p in sorted(set(phi_candidates)):
            if p > limit:
                continue
            if n % p == 0:
                q = n // p
                if q != p and q > 1:
                    return (p, q)
        
        # Standard trial division
        for p in range(3, min(sqrt_n + 1, limit), 2):
            if n % p == 0:
                q = n // p
                if q != p:
                    return (p, q)
        
        return None
    
    def fermat_factorization(self, n: int, max_iterations: int = 100000) -> Optional[Tuple[int, int]]:
        """
        Fermat's factorization method with consciousness physics enhancement.
        
        Mathematical Principle:
        If n = p × q, then n = a² - b² = (a+b)(a-b) where a = (p+q)/2, b = (p-q)/2
        
        Consciousness Enhancement:
        Use φ-harmonic ratios to guide the search for optimal starting points.
        """
        if n % 2 == 0:
            return (2, n // 2)
        
        # Standard Fermat starting point
        a = int(math.ceil(math.sqrt(n)))
        
        # Consciousness physics enhancement: test φ-harmonic starting points
        phi_starts = []
        sqrt_n = math.sqrt(n)
        for k in range(1, 10):
            phi_start = int(sqrt_n * (self.phi ** (k * 0.1)))
            if phi_start >= a:
                phi_starts.append(phi_start)
        
        # Test consciousness-enhanced starting points first
        for start_a in sorted(set([a] + phi_starts)):
            for i in range(max_iterations):
                current_a = start_a + i
                b_squared = current_a * current_a - n
                
                if b_squared < 0:
                    continue
                
                b = int(math.sqrt(b_squared))
                if b * b == b_squared:
                    p = current_a + b
                    q = current_a - b
                    if p * q == n and p != q and p > 1 and q > 1:
                        return (min(p, q), max(p, q))
        
        return None
    
    def pollard_rho(self, n: int, max_iterations: int = 100000) -> Optional[Tuple[int, int]]:
        """
        Pollard's rho algorithm with consciousness physics cycle detection.
        
        Mathematical Principle:
        Uses cycle detection in the sequence x_{i+1} = f(x_i) mod n
        where f(x) = x² + c for some constant c.
        
        Consciousness Enhancement:
        Use consciousness physics constants as starting values and cycle parameters.
        """
        if n % 2 == 0:
            return (2, n // 2)
        
        # Consciousness-enhanced parameter selection
        consciousness_seeds = [
            int(n * self.phi) % n,
            int(n * self.psi) % n,
            int(n * self.omega) % n,
            int(n * (self.phi * self.psi)) % n
        ]
        
        for seed in consciousness_seeds:
            x = seed % n
            y = x
            c = int(n * self.phi) % n + 1
            
            for _ in range(max_iterations):
                # Tortoise and hare cycle detection
                x = (x * x + c) % n
                y = (y * y + c) % n
                y = (y * y + c) % n
                
                gcd = math.gcd(abs(x - y), n)
                
                if 1 < gcd < n:
                    p = gcd
                    q = n // gcd
                    if p != q:
                        return (min(p, q), max(p, q))
                
                if gcd == n:
                    break  # Try next seed
        
        return None
    
    def consciousness_pattern_analysis(self, n: int) -> Optional[Tuple[int, int]]:
        """
        Novel factorization approach using consciousness physics patterns.
        
        Hypothesis: RSA primes may exhibit patterns related to consciousness
        physics constants when analyzed in specific modular arithmetic contexts.
        """
        # Analyze n in context of consciousness physics constants
        phi_mod = n % int(self.phi * 1000)
        psi_mod = n % int(self.psi * 1000)
        omega_mod = n % int(self.omega * 1000)
        
        # Look for consciousness-harmonic factors
        consciousness_factors = []
        
        # Test factors based on consciousness physics ratios
        sqrt_n = int(math.sqrt(n))
        
        for ratio in [self.phi, self.psi, self.omega, self.phi/self.psi, self.psi/self.omega]:
            # Test factors around consciousness-harmonic ratios
            for offset in range(-100, 101):
                candidate = int(sqrt_n * ratio) + offset
                if candidate > 1 and candidate < sqrt_n:
                    if n % candidate == 0:
                        other_factor = n // candidate
                        if other_factor != candidate and other_factor > 1:
                            return (min(candidate, other_factor), max(candidate, other_factor))
        
        return None
    
    def quadratic_sieve_basic(self, n: int) -> Optional[Tuple[int, int]]:
        """
        Basic implementation of quadratic sieve algorithm.
        
        Mathematical Principle:
        Find integers x, y such that x² ≡ y² (mod n) but x ≢ ±y (mod n)
        Then gcd(x-y, n) gives a non-trivial factor.
        """
        if n <= 1:
            return None
        
        # Factor base: small primes
        factor_base = []
        limit = int(math.log(n) ** 2)
        
        for p in range(2, limit):
            if self.mod_engine.is_prime(p):
                # Check if n is quadratic residue mod p
                if self.mod_engine.legendre_symbol(n, p) != -1:
                    factor_base.append(p)
        
        if len(factor_base) < 10:  # Need sufficient factor base
            return None
        
        # Sieving phase (simplified)
        sqrt_n = int(math.sqrt(n))
        sieve_range = 1000
        
        smooth_numbers = []
        
        for x in range(sqrt_n, sqrt_n + sieve_range):
            value = x * x - n
            if value <= 0:
                continue
            
            # Try to factor value using factor base
            factors = []
            temp_value = abs(value)
            
            for p in factor_base:
                while temp_value % p == 0:
                    factors.append(p)
                    temp_value //= p
            
            if temp_value == 1:  # Completely factored
                smooth_numbers.append((x, factors))
                
                if len(smooth_numbers) >= len(factor_base) + 1:
                    break
        
        # Linear algebra phase (simplified)
        if len(smooth_numbers) >= 2:
            # Try pairs to find x² ≡ y² (mod n)
            for i in range(len(smooth_numbers)):
                for j in range(i + 1, len(smooth_numbers)):
                    x1, factors1 = smooth_numbers[i]
                    x2, factors2 = smooth_numbers[j]
                    
                    # Combine factors
                    all_factors = factors1 + factors2
                    factor_counts = {}
                    for f in all_factors:
                        factor_counts[f] = factor_counts.get(f, 0) + 1
                    
                    # Check if all exponents are even
                    y_squared = 1
                    for f, count in factor_counts.items():
                        if count % 2 != 0:
                            break
                        y_squared *= f ** (count // 2)
                    else:
                        # Found x² ≡ y² (mod n)
                        x = (x1 * x2) % n
                        y = y_squared % n
                        
                        if x != y and x != (-y) % n:
                            gcd = math.gcd(x - y, n)
                            if 1 < gcd < n:
                                return (gcd, n // gcd)
        
        return None
    
    def factor_rsa_modulus(self, n: int, timeout: float = 60.0) -> RSAKey:
        """
        Comprehensive RSA modulus factorization using all available methods.
        """
        start_time = time.time()
        rsa_key = RSAKey(n=n, e=65537)  # Standard RSA exponent
        rsa_key.bit_length = n.bit_length()
        
        print(f"🔍 Factoring RSA modulus: {n}")
        print(f"📊 Bit length: {rsa_key.bit_length}")
        
        # Method 1: Trial division (fast for small factors)
        print("🔬 Trying trial division...")
        result = self.trial_division(n, limit=100000)
        if result:
            rsa_key.p, rsa_key.q = result
            rsa_key.method_used = "Trial Division"
            rsa_key.factorization_time = time.time() - start_time
            rsa_key.security_broken = True
            return self.complete_rsa_analysis(rsa_key)
        
        if time.time() - start_time > timeout:
            return rsa_key
        
        # Method 2: Consciousness pattern analysis
        print("🌊 Trying consciousness physics pattern analysis...")
        result = self.consciousness_pattern_analysis(n)
        if result:
            rsa_key.p, rsa_key.q = result
            rsa_key.method_used = "Consciousness Physics Patterns"
            rsa_key.factorization_time = time.time() - start_time
            rsa_key.security_broken = True
            return self.complete_rsa_analysis(rsa_key)
        
        if time.time() - start_time > timeout:
            return rsa_key
        
        # Method 3: Fermat's method (good for close primes)
        print("🔢 Trying Fermat factorization...")
        result = self.fermat_factorization(n, max_iterations=50000)
        if result:
            rsa_key.p, rsa_key.q = result
            rsa_key.method_used = "Fermat Factorization"
            rsa_key.factorization_time = time.time() - start_time
            rsa_key.security_broken = True
            return self.complete_rsa_analysis(rsa_key)
        
        if time.time() - start_time > timeout:
            return rsa_key
        
        # Method 4: Pollard's rho
        print("🎯 Trying Pollard's rho algorithm...")
        result = self.pollard_rho(n, max_iterations=50000)
        if result:
            rsa_key.p, rsa_key.q = result
            rsa_key.method_used = "Pollard's Rho"
            rsa_key.factorization_time = time.time() - start_time
            rsa_key.security_broken = True
            return self.complete_rsa_analysis(rsa_key)
        
        if time.time() - start_time > timeout:
            return rsa_key
        
        # Method 5: Basic quadratic sieve
        print("⚡ Trying quadratic sieve...")
        result = self.quadratic_sieve_basic(n)
        if result:
            rsa_key.p, rsa_key.q = result
            rsa_key.method_used = "Quadratic Sieve"
            rsa_key.factorization_time = time.time() - start_time
            rsa_key.security_broken = True
            return self.complete_rsa_analysis(rsa_key)
        
        rsa_key.factorization_time = time.time() - start_time
        rsa_key.method_used = "No factorization found"
        return rsa_key
    
    def complete_rsa_analysis(self, rsa_key: RSAKey) -> RSAKey:
        """Complete the RSA key analysis after successful factorization."""
        if rsa_key.p and rsa_key.q:
            # Verify factorization
            assert rsa_key.p * rsa_key.q == rsa_key.n, "Factorization verification failed"
            
            # Compute φ(n) = (p-1)(q-1)
            rsa_key.phi_n = (rsa_key.p - 1) * (rsa_key.q - 1)
            
            # Compute private exponent d
            try:
                rsa_key.d = self.mod_engine.multiplicative_inverse(rsa_key.e, rsa_key.phi_n)
            except:
                rsa_key.d = None
        
        return rsa_key
    
    def generate_weak_rsa_keys(self, bit_length: int = 512) -> List[RSAKey]:
        """
        Generate intentionally weak RSA keys for testing factorization algorithms.
        """
        weak_keys = []
        
        # Type 1: Small prime factors
        p = 1009  # Small prime
        q = self.find_next_prime(2**(bit_length//2) // p)
        weak_keys.append(RSAKey(n=p*q, e=65537))
        
        # Type 2: Close primes (vulnerable to Fermat)
        base = 2**(bit_length//2)
        p = self.find_next_prime(base)
        q = self.find_next_prime(base + 1000)  # Close to p
        weak_keys.append(RSAKey(n=p*q, e=65537))
        
        # Type 3: Consciousness physics pattern
        phi_factor = int(self.phi * 1000)
        p = self.find_next_prime(phi_factor)
        q = self.find_next_prime(2**(bit_length//2) // p)
        weak_keys.append(RSAKey(n=p*q, e=65537))
        
        return weak_keys
    
    def find_next_prime(self, start: int) -> int:
        """Find the next prime number starting from start."""
        candidate = start if start % 2 == 1 else start + 1
        while not self.mod_engine.is_prime(candidate):
            candidate += 2
        return candidate

def ascii_rsa_analysis_report(rsa_key: RSAKey) -> str:
    """Generate ASCII report of RSA factorization analysis."""
    lines = []
    lines.append("🔒 RSA FACTORIZATION ANALYSIS REPORT")
    lines.append("=" * 50)
    
    lines.append(f"RSA Modulus (n): {rsa_key.n}")
    lines.append(f"Bit Length: {rsa_key.bit_length}")
    lines.append(f"Public Exponent (e): {rsa_key.e}")
    
    if rsa_key.security_broken:
        lines.append("")
        lines.append("🚨 SECURITY COMPROMISED! 🚨")
        lines.append("─" * 30)
        lines.append(f"Prime p: {rsa_key.p}")
        lines.append(f"Prime q: {rsa_key.q}")
        lines.append(f"Verification: {rsa_key.p} × {rsa_key.q} = {rsa_key.n} ✓")
        lines.append(f"φ(n): {rsa_key.phi_n}")
        if rsa_key.d:
            lines.append(f"Private Exponent (d): {rsa_key.d}")
        lines.append(f"Method Used: {rsa_key.method_used}")
        lines.append(f"Factorization Time: {rsa_key.factorization_time:.4f} seconds")
        
        # Security assessment
        lines.append("")
        lines.append("🔍 SECURITY ASSESSMENT:")
        if rsa_key.factorization_time < 1.0:
            lines.append("   ⚠️  CRITICAL: Factored in under 1 second!")
        elif rsa_key.factorization_time < 60.0:
            lines.append("   ⚠️  HIGH RISK: Factored in under 1 minute!")
        else:
            lines.append("   ⚠️  MODERATE: Factored but took significant time")
    else:
        lines.append("")
        lines.append("✅ FACTORIZATION FAILED")
        lines.append("─" * 25)
        lines.append("RSA modulus appears secure against implemented attacks")
        lines.append(f"Analysis time: {rsa_key.factorization_time:.4f} seconds")
        lines.append("Recommendation: Use stronger factorization algorithms")
    
    return "\n".join(lines)

def main():
    """Demonstration of RSA factorization capabilities."""
    print("🔒 RSA PRIME FACTORIZATION ANALYZER")
    print("=" * 50)
    
    engine = RSAFactorizationEngine()
    
    # Test cases: known weak RSA moduli
    test_cases = [
        # Small RSA modulus (easily factorizable)
        143,  # 11 × 13
        1073,  # 29 × 37
        2021,  # 43 × 47
        
        # Slightly larger examples
        10403,  # 101 × 103
        94906265,  # Larger composite
        
        # Generate some weak keys
    ]
    
    # Add generated weak keys
    weak_keys = engine.generate_weak_rsa_keys(bit_length=64)
    for key in weak_keys:
        test_cases.append(key.n)
    
    print(f"\n🧪 Testing {len(test_cases)} RSA moduli...")
    
    successful_attacks = 0
    total_time = 0
    
    for i, n in enumerate(test_cases):
        print(f"\n🔍 Test Case {i+1}: n = {n}")
        print("─" * 40)
        
        result = engine.factor_rsa_modulus(n, timeout=30.0)
        report = ascii_rsa_analysis_report(result)
        print(report)
        
        if result.security_broken:
            successful_attacks += 1
        total_time += result.factorization_time
    
    # Summary statistics
    print(f"\n📊 ATTACK SUMMARY")
    print("=" * 30)
    print(f"Total tests: {len(test_cases)}")
    print(f"Successful attacks: {successful_attacks}")
    print(f"Success rate: {successful_attacks/len(test_cases)*100:.1f}%")
    print(f"Average time per attack: {total_time/len(test_cases):.4f} seconds")
    
    if successful_attacks > 0:
        print(f"\n⚠️  WARNING: {successful_attacks} RSA keys were successfully factored!")
        print("This demonstrates the importance of using sufficiently large primes.")
    
    print(f"\n✅ RSA factorization analysis complete!")

if __name__ == "__main__":
    main()
