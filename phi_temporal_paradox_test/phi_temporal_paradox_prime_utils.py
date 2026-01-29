"""
phi_temporal_paradox_prime_utils.py

Provides:
- φNet coherence test
- 105 mod 89 test
- Wrapper for quantum/phi prime generators
"""

import random
import math
import time

# Placeholder: In actual use, import your phi/quantum prime modules here
# from ... import phi_harmonic_quantum_prime_generator, ...

PHI = (1 + 5 ** 0.5) / 2

# φNet coherence test: passes if phi-resonance is within a golden range
# (Here, phi-resonance is (n * PHI) % 1)
def phi_net_coherence_test(n, tol=0.05):
    resonance = (n * PHI) % 1
    # Accept if resonance is within 0.05 of 0 or 1 (golden resonance)
    return resonance < tol or resonance > 1 - tol

def test_105_mod_89(n):
    return n % 105 == 89

# Fails conventional primality (composite), passes custom tests
def generate_paradox_prime(min_n=10000, max_n=100000):
    attempts = 0
    while True:
        # Pick a random composite (not prime)
        a = random.randint(min_n, max_n)
        b = random.randint(2, 7)
        n = a * b
        if not is_probable_prime(n):
            if phi_net_coherence_test(n) and test_105_mod_89(n):
                return n
        attempts += 1
        if attempts > 10000:
            raise RuntimeError("Failed to find paradox prime")

# Miller-Rabin primality test (fails for composites)
def is_probable_prime(n, k=5):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
        if n % p == 0 and n != p:
            return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
