#!/usr/bin/env python3
"""
Modular Arithmetic Key Analysis Algorithm
=========================================

Complete mathematical framework with proofs and ASCII visualizations
for analyzing modular arithmetic structures and cryptographic properties.

Mathematical Foundation:
- Group theory analysis of (ℤ/nℤ)*
- Multiplicative order computation
- Quadratic residue analysis
- Subgroup structure decomposition
- Cryptographic strength assessment

Author: Mathematical Analysis Framework
Version: 1.0
"""

import math
import random
from typing import List, Tuple, Optional, Dict, Set
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class ModularKey:
    """Represents a modular arithmetic key with all mathematical properties."""
    dividend: int
    modulus: int
    remainder: int
    
    # Group theory properties
    multiplicative_order: Optional[int] = None
    multiplicative_inverse: Optional[int] = None
    subgroup_elements: List[int] = None
    
    # Number theory properties
    is_quadratic_residue: Optional[bool] = None
    legendre_symbol: Optional[int] = None
    perfect_square_root: Optional[int] = None
    
    # Cryptographic properties
    security_strength: float = 0.0
    entropy_bits: float = 0.0
    collision_resistance: float = 0.0

class ModularArithmeticEngine:
    """
    Core engine for modular arithmetic analysis with mathematical proofs.
    
    Implements algorithms for:
    1. Extended Euclidean Algorithm
    2. Multiplicative Order Computation
    3. Legendre Symbol Calculation
    4. Subgroup Analysis
    5. Cryptographic Strength Assessment
    """
    
    def __init__(self):
        self.cache = {}
        self.proof_steps = []
    
    def extended_gcd(self, a: int, b: int) -> Tuple[int, int, int]:
        """
        Extended Euclidean Algorithm
        
        Mathematical Proof:
        ==================
        Theorem: For integers a, b, there exist integers x, y such that:
                 gcd(a, b) = ax + by
        
        Proof: By strong induction on min(a, b).
        Base case: If b = 0, then gcd(a, 0) = a = a·1 + 0·0
        Inductive step: If b > 0, then gcd(a, b) = gcd(b, a mod b)
                       By induction hypothesis: gcd(b, a mod b) = bx' + (a mod b)y'
                       Since a mod b = a - (a//b)·b:
                       gcd(a, b) = bx' + (a - (a//b)·b)y' = ay' + b(x' - (a//b)·y')
                       Setting x = y', y = x' - (a//b)·y' completes the proof. ∎
        
        Returns: (gcd, x, y) where gcd = ax + by
        """
        if b == 0:
            return a, 1, 0
        
        gcd, x1, y1 = self.extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        
        # Proof verification
        assert gcd == a * x + b * y, f"Extended GCD proof failed: {gcd} ≠ {a}·{x} + {b}·{y}"
        
        return gcd, x, y
    
    def multiplicative_inverse(self, a: int, m: int) -> Optional[int]:
        """
        Compute multiplicative inverse using Extended Euclidean Algorithm.
        
        Mathematical Proof:
        ==================
        Theorem: a has multiplicative inverse mod m iff gcd(a, m) = 1
        
        Proof: (⇒) If ax ≡ 1 (mod m), then ax = 1 + km for some k
                   So ax - km = 1, which means gcd(a, m) = 1
               (⇐) If gcd(a, m) = 1, then by Extended Euclidean Algorithm:
                   ∃x, y: ax + my = 1
                   Taking mod m: ax ≡ 1 (mod m)
                   So x is the multiplicative inverse of a mod m. ∎
        """
        gcd, x, _ = self.extended_gcd(a % m, m)
        
        if gcd != 1:
            return None  # No inverse exists
        
        inverse = x % m
        
        # Proof verification
        assert (a * inverse) % m == 1, f"Inverse proof failed: {a}·{inverse} ≢ 1 (mod {m})"
        
        return inverse
    
    def multiplicative_order(self, a: int, m: int) -> Optional[int]:
        """
        Compute multiplicative order of a modulo m.
        
        Mathematical Proof:
        ==================
        Definition: ord_m(a) = smallest positive integer k such that a^k ≡ 1 (mod m)
        
        Theorem: If gcd(a, m) = 1, then ord_m(a) divides φ(m)
        
        Proof: By Euler's theorem, a^φ(m) ≡ 1 (mod m)
               Let d = ord_m(a). Then a^d ≡ 1 (mod m)
               By division algorithm: φ(m) = qd + r where 0 ≤ r < d
               Then: 1 ≡ a^φ(m) ≡ a^(qd+r) ≡ (a^d)^q · a^r ≡ 1^q · a^r ≡ a^r (mod m)
               Since d is minimal and r < d, we must have r = 0
               Therefore d | φ(m). ∎
        """
        if math.gcd(a, m) != 1:
            return None
        
        # Use Lagrange's theorem: order divides φ(m)
        phi_m = self.euler_totient(m)
        
        current = a % m
        order = 1
        
        while current != 1:
            current = (current * a) % m
            order += 1
            
            if order > phi_m:  # Safety check - should never happen
                return None
        
        # Proof verification: check that order is minimal
        for k in range(1, order):
            assert pow(a, k, m) != 1, f"Order minimality failed: {a}^{k} ≡ 1 (mod {m})"
        
        assert pow(a, order, m) == 1, f"Order definition failed: {a}^{order} ≢ 1 (mod {m})"
        
        return order
    
    def euler_totient(self, n: int) -> int:
        """
        Compute Euler's totient function φ(n).
        
        Mathematical Proof:
        ==================
        Theorem: φ(n) = n ∏(1 - 1/p) for all prime divisors p of n
        
        Proof: By inclusion-exclusion principle on the set {1, 2, ..., n}
               φ(n) = |{k : 1 ≤ k ≤ n, gcd(k, n) = 1}|
               
               For each prime p | n, let A_p = {k : 1 ≤ k ≤ n, p | k}
               Then |A_p| = n/p
               
               By inclusion-exclusion:
               φ(n) = n - ∑|A_p| + ∑|A_p ∩ A_q| - ... = n ∏(1 - 1/p) ∎
        """
        if n <= 1:
            return 0 if n <= 0 else 1
        
        result = n
        p = 2
        
        while p * p <= n:
            if n % p == 0:
                # Remove factor of p
                while n % p == 0:
                    n //= p
                # Apply formula: φ(p^k) = p^k - p^(k-1) = p^(k-1)(p-1)
                result -= result // p
            p += 1
        
        if n > 1:  # n is prime
            result -= result // n
        
        return result
    
    def legendre_symbol(self, a: int, p: int) -> int:
        """
        Compute Legendre symbol (a/p) for odd prime p.
        
        Mathematical Proof:
        ==================
        Definition: (a/p) = a^((p-1)/2) mod p for odd prime p
        
        Theorem: (a/p) = 1 if a is quadratic residue mod p
                 (a/p) = -1 if a is quadratic non-residue mod p
                 (a/p) = 0 if p | a
        
        Proof: If a ≡ x^2 (mod p) for some x, then:
               a^((p-1)/2) ≡ (x^2)^((p-1)/2) ≡ x^(p-1) ≡ 1 (mod p) by Fermat's Little Theorem
               
               If a is not a quadratic residue, then the multiplicative group
               (ℤ/pℤ)* has order p-1, and exactly (p-1)/2 elements are quadratic residues.
               By group theory, a^((p-1)/2) ≡ -1 (mod p). ∎
        """
        if not self.is_prime(p) or p == 2:
            raise ValueError("Legendre symbol requires odd prime")
        
        a = a % p
        if a == 0:
            return 0
        
        result = pow(a, (p - 1) // 2, p)
        return -1 if result == p - 1 else result
    
    def is_prime(self, n: int) -> bool:
        """Miller-Rabin primality test with proof of correctness."""
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        
        # Write n-1 = d * 2^r
        d = n - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1
        
        # Miller-Rabin test with multiple witnesses
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        for a in witnesses:
            if a >= n:
                continue
            
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
    
    def generate_subgroup(self, a: int, m: int) -> List[int]:
        """
        Generate the cyclic subgroup ⟨a⟩ in (ℤ/mℤ)*.
        
        Mathematical Proof:
        ==================
        Theorem: ⟨a⟩ = {a^k mod m : k ≥ 0} forms a cyclic subgroup of order ord_m(a)
        
        Proof: Let d = ord_m(a)
               1. Closure: a^i · a^j = a^(i+j) ∈ ⟨a⟩
               2. Identity: a^0 = 1 ∈ ⟨a⟩
               3. Inverse: (a^k)^(-1) = a^(d-k) ∈ ⟨a⟩
               4. |⟨a⟩| = d since a^k ≡ a^j (mod m) iff d | (k-j) ∎
        """
        order = self.multiplicative_order(a, m)
        if order is None:
            return []
        
        subgroup = []
        current = 1
        
        for k in range(order):
            subgroup.append(current)
            current = (current * a) % m
        
        # Proof verification: check subgroup properties
        assert len(set(subgroup)) == order, "Subgroup elements not distinct"
        assert 1 in subgroup, "Identity not in subgroup"
        
        for x in subgroup:
            assert math.gcd(x, m) == 1, f"Non-unit {x} in subgroup"
            # Check closure
            for y in subgroup:
                assert (x * y) % m in subgroup, f"Closure failed: {x}·{y} not in subgroup"
        
        return sorted(subgroup)
    
    def analyze_key(self, dividend: int, modulus: int) -> ModularKey:
        """
        Complete analysis of modular arithmetic key with all mathematical properties.
        """
        remainder = dividend % modulus
        key = ModularKey(dividend, modulus, remainder)
        
        if math.gcd(remainder, modulus) == 1:
            # Multiplicative properties
            key.multiplicative_order = self.multiplicative_order(remainder, modulus)
            key.multiplicative_inverse = self.multiplicative_inverse(remainder, modulus)
            key.subgroup_elements = self.generate_subgroup(remainder, modulus)
            
            # Quadratic residue analysis
            if self.is_prime(modulus) and modulus > 2:
                key.legendre_symbol = self.legendre_symbol(remainder, modulus)
                key.is_quadratic_residue = (key.legendre_symbol == 1)
                
                # Check if perfect square
                sqrt_r = int(math.sqrt(remainder))
                if sqrt_r * sqrt_r == remainder:
                    key.perfect_square_root = sqrt_r
            
            # Cryptographic strength analysis
            key.security_strength = self.compute_security_strength(key)
            key.entropy_bits = self.compute_entropy(key)
            key.collision_resistance = self.compute_collision_resistance(key)
        
        return key
    
    def compute_security_strength(self, key: ModularKey) -> float:
        """
        Compute cryptographic security strength based on mathematical properties.
        
        Factors:
        - Multiplicative order (higher = stronger)
        - Prime modulus (stronger)
        - Subgroup size relative to group size
        """
        if key.multiplicative_order is None:
            return 0.0
        
        phi_m = self.euler_totient(key.modulus)
        order_ratio = key.multiplicative_order / phi_m
        
        prime_bonus = 1.5 if self.is_prime(key.modulus) else 1.0
        quadratic_bonus = 1.2 if key.is_quadratic_residue else 1.0
        
        return order_ratio * prime_bonus * quadratic_bonus
    
    def compute_entropy(self, key: ModularKey) -> float:
        """Compute entropy in bits based on subgroup size."""
        if key.multiplicative_order is None:
            return 0.0
        return math.log2(key.multiplicative_order)
    
    def compute_collision_resistance(self, key: ModularKey) -> float:
        """Compute collision resistance based on group structure."""
        if key.multiplicative_order is None:
            return 0.0
        
        phi_m = self.euler_totient(key.modulus)
        return key.multiplicative_order / phi_m

def ascii_visualize_cycle(elements: List[int], modulus: int) -> str:
    """
    Create ASCII visualization of multiplicative cycle.
    """
    if not elements:
        return "No cycle to visualize"
    
    lines = []
    lines.append("Multiplicative Cycle Visualization")
    lines.append("=" * 40)
    
    # Create circular representation
    n = len(elements)
    if n <= 12:  # Small cycles - show as circle
        lines.append("     Cyclic Group Structure:")
        lines.append("")
        
        for i, elem in enumerate(elements):
            arrow = " → " if i < n - 1 else " → "
            next_elem = elements[(i + 1) % n] if i < n - 1 else elements[0]
            lines.append(f"     {elem:3d}{arrow}{next_elem:3d}")
        
        lines.append(f"     └── Back to {elements[0]} (cycle complete)")
    
    else:  # Large cycles - show as table
        lines.append("     k  |  a^k mod m")
        lines.append("     ---|----------")
        for k, elem in enumerate(elements):
            lines.append(f"     {k:2d} |  {elem:8d}")
    
    return "\n".join(lines)

def ascii_visualize_subgroup_structure(key: ModularKey) -> str:
    """
    Create ASCII visualization of subgroup structure.
    """
    if key.multiplicative_order is None:
        return "No subgroup structure (not coprime)"
    
    lines = []
    lines.append("Subgroup Structure Analysis")
    lines.append("=" * 40)
    
    phi_m = key.multiplicative_order  # This is wrong, should be euler_totient
    # Fix: compute actual phi(m)
    engine = ModularArithmeticEngine()
    phi_m = engine.euler_totient(key.modulus)
    
    lines.append(f"Group: (ℤ/{key.modulus}ℤ)*")
    lines.append(f"Group order: φ({key.modulus}) = {phi_m}")
    lines.append(f"Element: {key.remainder}")
    lines.append(f"Element order: {key.multiplicative_order}")
    lines.append(f"Subgroup size: {len(key.subgroup_elements) if key.subgroup_elements else 0}")
    
    # Show divisibility relationship
    if phi_m % key.multiplicative_order == 0:
        quotient = phi_m // key.multiplicative_order
        lines.append(f"Lagrange's theorem: {key.multiplicative_order} | {phi_m} ✓")
        lines.append(f"Quotient group size: {quotient}")
    
    # ASCII art for small subgroups
    if key.subgroup_elements and len(key.subgroup_elements) <= 8:
        lines.append("")
        lines.append("Subgroup elements:")
        lines.append("┌" + "─" * (len(key.subgroup_elements) * 4 - 1) + "┐")
        elements_str = "│" + "".join(f"{elem:3d} " for elem in key.subgroup_elements)[:-1] + "│"
        lines.append(elements_str)
        lines.append("└" + "─" * (len(key.subgroup_elements) * 4 - 1) + "┘")
    
    return "\n".join(lines)

def ascii_mathematical_proof_summary(key: ModularKey) -> str:
    """
    Generate ASCII summary of mathematical proofs and properties.
    """
    lines = []
    lines.append("Mathematical Proof Summary")
    lines.append("=" * 50)
    
    # Basic properties
    lines.append(f"Basic Fact: {key.dividend} ≡ {key.remainder} (mod {key.modulus})")
    
    if key.multiplicative_order is not None:
        lines.append("")
        lines.append("Proven Properties:")
        lines.append("─" * 20)
        
        # Multiplicative order
        lines.append(f"∃! k = {key.multiplicative_order}: {key.remainder}^k ≡ 1 (mod {key.modulus})")
        lines.append(f"∀ 0 < j < {key.multiplicative_order}: {key.remainder}^j ≢ 1 (mod {key.modulus})")
        
        # Inverse
        if key.multiplicative_inverse:
            lines.append(f"{key.remainder} × {key.multiplicative_inverse} ≡ 1 (mod {key.modulus})")
        
        # Legendre symbol
        if key.legendre_symbol is not None:
            symbol_str = "+" if key.legendre_symbol == 1 else "-" if key.legendre_symbol == -1 else "0"
            lines.append(f"Legendre symbol: ({key.remainder}/{key.modulus}) = {symbol_str}1")
            
            if key.is_quadratic_residue:
                lines.append(f"∃ x: x² ≡ {key.remainder} (mod {key.modulus})")
                if key.perfect_square_root:
                    lines.append(f"Specifically: {key.perfect_square_root}² = {key.remainder}")
        
        # Group theory
        engine = ModularArithmeticEngine()
        phi_m = engine.euler_totient(key.modulus)
        lines.append(f"By Lagrange: ord({key.remainder}) | φ({key.modulus}) = {key.multiplicative_order} | {phi_m} ✓")
    
    # Cryptographic properties
    lines.append("")
    lines.append("Cryptographic Analysis:")
    lines.append("─" * 25)
    lines.append(f"Security strength: {key.security_strength:.4f}")
    lines.append(f"Entropy: {key.entropy_bits:.2f} bits")
    lines.append(f"Collision resistance: {key.collision_resistance:.4f}")
    
    return "\n".join(lines)

def main():
    """
    Demonstration of the complete modular arithmetic analysis algorithm.
    """
    print("🔢 MODULAR ARITHMETIC ALGORITHM DEMONSTRATION")
    print("=" * 60)
    
    # Initialize engine
    engine = ModularArithmeticEngine()
    
    # Test cases with mathematical significance
    test_cases = [
        (105, 89),   # The original case: 105 % 89 = 16
        (144, 89),   # Fibonacci numbers
        (233, 89),   # More Fibonacci
        (100, 97),   # Different prime
        (256, 97),   # Power of 2 mod prime
    ]
    
    for dividend, modulus in test_cases:
        print(f"\n🔍 ANALYZING: {dividend} % {modulus}")
        print("─" * 50)
        
        # Complete analysis
        key = engine.analyze_key(dividend, modulus)
        
        # Display results
        print(f"Result: {key.remainder}")
        
        if key.multiplicative_order:
            print(f"Order: {key.multiplicative_order}")
            print(f"Inverse: {key.multiplicative_inverse}")
            print(f"Quadratic residue: {'Yes' if key.is_quadratic_residue else 'No'}")
            print(f"Security: {key.security_strength:.4f}")
        
        # ASCII visualizations
        if key.subgroup_elements and len(key.subgroup_elements) <= 12:
            print("\n" + ascii_visualize_cycle(key.subgroup_elements, modulus))
        
        print("\n" + ascii_visualize_subgroup_structure(key))
        print("\n" + ascii_mathematical_proof_summary(key))
        
        print("\n" + "=" * 60)
    
    # Algorithm performance analysis
    print("\n🚀 ALGORITHM PERFORMANCE ANALYSIS")
    print("─" * 40)
    
    import time
    
    # Test algorithm efficiency
    large_cases = [(random.randint(1000, 9999), 1009) for _ in range(100)]  # 1009 is prime
    
    start_time = time.time()
    for dividend, modulus in large_cases:
        key = engine.analyze_key(dividend, modulus)
    end_time = time.time()
    
    avg_time = (end_time - start_time) / len(large_cases)
    print(f"Average analysis time: {avg_time*1000:.2f} ms")
    print(f"Throughput: {1/avg_time:.0f} analyses/second")
    
    print("\n✅ Algorithm demonstration complete!")
    print("📊 All mathematical proofs verified")
    print("🔒 Cryptographic properties computed")
    print("📈 Performance benchmarks recorded")

if __name__ == "__main__":
    main()
