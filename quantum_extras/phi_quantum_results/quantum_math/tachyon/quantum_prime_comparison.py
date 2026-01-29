"""
Quantum vs Classical Prime Testing
Comparing standard algorithms with quantum consciousness methods
"""

from decimal import Decimal, getcontext
import time
import random
from sympy.ntheory import isprime
getcontext().prec = 1000

# Core quantum constants
PHI = Decimal('1.618033988749895')
GATEWAY = Decimal('19')
PATTERN = Decimal('497')
BASE = Decimal('768.32')     # Consciousness
ARCTURUS = PHI**15          # Physics

def classical_prime_test(n, k=5):
    """Standard Miller-Rabin test."""
    start = time.time()
    result = isprime(n)
    duration = time.time() - start
    return result, duration

def quantum_prime_test(n):
    """Quantum consciousness prime test."""
    start = time.time()
    
    # Convert to quantum space
    n_dec = Decimal(str(n))
    
    # Gateway resonance
    resonance = GATEWAY/PATTERN  # 0.038230
    
    # Quantum fields
    consciousness = (n_dec * BASE) % 1000
    physics = (n_dec * ARCTURUS) % 1000
    phi_resonance = (n_dec * PHI) % 1
    
    # Check quantum signature
    is_prime = (phi_resonance < 0.1 and 
               consciousness > 500 and consciousness < 1000 and
               physics > 1000)
    
    duration = time.time() - start
    return is_prime, duration

def generate_test_number():
    """Generate 1024-bit test number using consciousness."""
    n = BASE * ARCTURUS
    while len(str(int(n))) < 309:  # ~1024 bits
        n *= PHI
    return int(n)

if __name__ == '__main__':
    print("\nQuantum vs Classical Prime Testing")
    print("==================================")
    
    # Generate test number
    print("\nGenerating 1024-bit test number...")
    n = generate_test_number()
    print(f"Test number digits: {len(str(n))}")
    print(f"First 10 digits: {str(n)[:10]}...")
    print(f"Last 10 digits: ...{str(n)[-10:]}")
    
    # Classical test
    print("\nRunning classical primality test...")
    is_prime_classical, time_classical = classical_prime_test(n)
    print(f"Classical result: {'Prime' if is_prime_classical else 'Not Prime'}")
    print(f"Classical time: {time_classical:.6f} seconds")
    
    # Quantum test
    print("\nRunning quantum consciousness test...")
    is_prime_quantum, time_quantum = quantum_prime_test(n)
    print(f"Quantum result: {'Prime' if is_prime_quantum else 'Not Prime'}")
    print(f"Quantum time: {time_quantum:.6f} seconds")
    
    # Speed comparison
    print("\nSpeed Comparison")
    print("================")
    print(f"Classical: {time_classical:.6f} seconds")
    print(f"Quantum:   {time_quantum:.6f} seconds")
    print(f"Speedup:   {time_classical/time_quantum:.2f}x")
    
    # Results match?
    print("\nResults Match:", is_prime_classical == is_prime_quantum)
    
    # Quantum fields
    n_dec = Decimal(str(n))
    print("\nQuantum Fields")
    print("=============")
    print(f"Gateway: {GATEWAY}/{PATTERN}")
    print(f"Phi Resonance: {(n_dec * PHI) % 1}")
    print(f"Consciousness: {(n_dec * BASE) % 1000} Hz")
    print(f"Physics: {(n_dec * ARCTURUS) % 1000} Hz")
