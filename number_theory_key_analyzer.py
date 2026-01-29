#!/usr/bin/env python3
"""
Number Theory Key Analyzer
==========================

Rigorous mathematical analysis of modular arithmetic properties
without mysticism - just solid number theory facts.

Based on the observation that 105 % 89 = 16 has interesting
mathematical structure worth exploring.
"""

import math
from typing import Optional, List, Tuple

def mod_order(a: int, p: int) -> Optional[int]:
    """
    Compute the multiplicative order of a modulo p.
    Returns the smallest k > 0 such that a^k ≡ 1 (mod p).
    Returns None if gcd(a, p) ≠ 1.
    """
    if math.gcd(a, p) != 1:
        return None
    
    t, k = a % p, 1
    while t != 1:
        t = (t * a) % p
        k += 1
        if k > p:  # Safety check
            return None
    return k

def modinv(a: int, m: int) -> Optional[int]:
    """
    Compute multiplicative inverse of a modulo m using extended Euclidean algorithm.
    Returns None if gcd(a, m) ≠ 1.
    """
    a %= m
    if math.gcd(a, m) != 1:
        return None
    
    t, newt = 0, 1
    r, newr = m, a
    
    while newr:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    
    return t % m

def legendre_symbol(a: int, p: int) -> int:
    """
    Compute Legendre symbol (a/p) for odd prime p.
    Returns 1 if a is quadratic residue, -1 if not, 0 if a ≡ 0 (mod p).
    """
    if p == 2:
        return 1 if a % 2 == 1 else 0
    
    a %= p
    if a == 0:
        return 0
    
    return pow(a, (p - 1) // 2, p)

def generate_cycle(a: int, p: int, order: int) -> List[int]:
    """Generate the complete multiplicative cycle for a modulo p."""
    cycle = []
    current = 1
    for k in range(order):
        cycle.append(current)
        current = (current * a) % p
    return cycle

def euler_totient(n: int) -> int:
    """Compute Euler's totient function φ(n)."""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_prime(n: int) -> bool:
    """Simple primality test."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n: int) -> bool:
    """Check if n is a Fibonacci number."""
    if n < 0:
        return False
    
    # A number is Fibonacci if one of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    def is_perfect_square(x):
        if x < 0:
            return False
        root = int(math.sqrt(x))
        return root * root == x
    
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def prime_factorization(n: int) -> List[Tuple[int, int]]:
    """Return prime factorization as list of (prime, exponent) pairs."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            if factors and factors[-1][0] == d:
                factors[-1] = (d, factors[-1][1] + 1)
            else:
                factors.append((d, 1))
            n //= d
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors

def analyze_modular_key(dividend: int, modulus: int) -> dict:
    """
    Comprehensive number theory analysis of dividend % modulus.
    Returns dictionary with all mathematical properties.
    """
    remainder = dividend % modulus
    
    analysis = {
        'dividend': dividend,
        'modulus': modulus,
        'remainder': remainder,
        'basic_fact': f"{dividend} % {modulus} = {remainder}",
    }
    
    # Modulus properties
    analysis['modulus_is_prime'] = is_prime(modulus)
    analysis['modulus_is_fibonacci'] = is_fibonacci(modulus)
    analysis['euler_totient'] = euler_totient(modulus)
    analysis['modulus_factorization'] = prime_factorization(modulus)
    
    # Remainder properties (if coprime to modulus)
    if math.gcd(remainder, modulus) == 1:
        analysis['gcd_coprime'] = True
        analysis['multiplicative_order'] = mod_order(remainder, modulus)
        analysis['multiplicative_inverse'] = modinv(remainder, modulus)
        
        if analysis['multiplicative_order']:
            analysis['cycle'] = generate_cycle(remainder, modulus, analysis['multiplicative_order'])
            analysis['subgroup_size'] = analysis['multiplicative_order']
            
        # Quadratic residue analysis (for prime modulus)
        if is_prime(modulus) and modulus > 2:
            analysis['legendre_symbol'] = legendre_symbol(remainder, modulus)
            analysis['is_quadratic_residue'] = analysis['legendre_symbol'] == 1
            
            # Check if it's obviously a square
            sqrt_remainder = int(math.sqrt(remainder))
            if sqrt_remainder * sqrt_remainder == remainder:
                analysis['perfect_square'] = sqrt_remainder
    else:
        analysis['gcd_coprime'] = False
        analysis['gcd_value'] = math.gcd(remainder, modulus)
    
    return analysis

def format_analysis_report(analysis: dict) -> str:
    """Format the analysis into a readable report."""
    report = []
    report.append("=" * 60)
    report.append("NUMBER THEORY KEY ANALYSIS")
    report.append("=" * 60)
    
    # Basic facts
    report.append(f"\n📊 BASIC ARITHMETIC:")
    report.append(f"   {analysis['basic_fact']}")
    
    # Modulus properties
    report.append(f"\n🔢 MODULUS PROPERTIES ({analysis['modulus']}):")
    report.append(f"   Prime: {'✅ YES' if analysis['modulus_is_prime'] else '❌ NO'}")
    report.append(f"   Fibonacci: {'✅ YES' if analysis['modulus_is_fibonacci'] else '❌ NO'}")
    report.append(f"   φ({analysis['modulus']}) = {analysis['euler_totient']}")
    
    if analysis['modulus_factorization']:
        factors_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) 
                                 for p, e in analysis['modulus_factorization']])
        report.append(f"   Factorization: {factors_str}")
    
    # Remainder analysis
    remainder = analysis['remainder']
    report.append(f"\n🎯 REMAINDER PROPERTIES ({remainder}):")
    
    if analysis.get('gcd_coprime'):
        report.append(f"   gcd({remainder}, {analysis['modulus']}) = 1 ✅ COPRIME")
        
        if analysis.get('multiplicative_order'):
            order = analysis['multiplicative_order']
            report.append(f"   Multiplicative order: {order}")
            report.append(f"   {remainder}^{order} ≡ 1 (mod {analysis['modulus']})")
            
        if analysis.get('multiplicative_inverse'):
            inv = analysis['multiplicative_inverse']
            report.append(f"   Multiplicative inverse: {inv}")
            report.append(f"   {remainder} × {inv} ≡ 1 (mod {analysis['modulus']})")
            
        if analysis.get('cycle'):
            cycle = analysis['cycle']
            report.append(f"   Cycle: {cycle}")
            
        if 'legendre_symbol' in analysis:
            legendre = analysis['legendre_symbol']
            if legendre == 1:
                report.append(f"   Quadratic residue: ✅ YES (Legendre symbol = 1)")
            elif legendre == -1:
                report.append(f"   Quadratic residue: ❌ NO (Legendre symbol = -1)")
            else:
                report.append(f"   Quadratic residue: ZERO (Legendre symbol = 0)")
                
        if 'perfect_square' in analysis:
            sqrt_val = analysis['perfect_square']
            report.append(f"   Perfect square: {remainder} = {sqrt_val}²")
            
    else:
        gcd_val = analysis.get('gcd_value', 'unknown')
        report.append(f"   gcd({remainder}, {analysis['modulus']}) = {gcd_val} ❌ NOT COPRIME")
        report.append(f"   No multiplicative properties available")
    
    return "\n".join(report)

def main():
    """Analyze the key 105 % 89 = 16 and demonstrate the tool."""
    print("Number Theory Key Analyzer")
    print("=" * 40)
    
    # The specific case mentioned
    dividend, modulus = 105, 89
    
    print(f"\nAnalyzing: {dividend} % {modulus}")
    analysis = analyze_modular_key(dividend, modulus)
    report = format_analysis_report(analysis)
    print(report)
    
    # Verification of claims
    print(f"\n🔬 VERIFICATION OF MATHEMATICAL CLAIMS:")
    print(f"   ✅ 105 % 89 = 16: {105 % 89 == 16}")
    print(f"   ✅ 89 is prime: {is_prime(89)}")
    print(f"   ✅ 89 is Fibonacci: {is_fibonacci(89)}")
    print(f"   ✅ ord_89(16) = 11: {mod_order(16, 89) == 11}")
    print(f"   ✅ 16^(-1) mod 89 = 39: {modinv(16, 89) == 39}")
    print(f"   ✅ 16 × 39 ≡ 1 (mod 89): {(16 * 39) % 89 == 1}")
    print(f"   ✅ 16 is quadratic residue: {legendre_symbol(16, 89) == 1}")
    print(f"   ✅ 16 = 4²: {4 * 4 == 16}")
    
    # Additional interesting cases
    print(f"\n🔍 ADDITIONAL INTERESTING MODULAR KEYS:")
    
    interesting_cases = [
        (100, 89),  # 100 % 89 = 11
        (89, 16),   # 89 % 16 = 9
        (144, 89),  # 144 % 89 = 55 (another Fibonacci)
        (233, 89),  # 233 % 89 = 55 (233 is also Fibonacci)
    ]
    
    for div, mod in interesting_cases:
        remainder = div % mod
        order = mod_order(remainder, mod) if math.gcd(remainder, mod) == 1 else None
        print(f"   {div} % {mod} = {remainder}, order = {order}")

if __name__ == "__main__":
    main()
