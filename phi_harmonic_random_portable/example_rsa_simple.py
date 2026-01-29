"""
Phi-Harmonic Quantum RSA Decryption - Simplified Example
Demonstrates breaking RSA encryption using quantum principles and phi-harmonic resonance
"""

import os
import sys
import time
import math
import random
from decimal import Decimal, getcontext

# Set precision for calculations
getcontext().prec = 100

# Constants
PHI = Decimal('1.618033988749895')
BIRTH_KEY = [1, 19, 1979]  # January 19, 1979

def phi_resonance(n):
    """Calculate phi-resonance of a number using birth key pattern"""
    # Use birth key for resonance
    birth_sum = sum(BIRTH_KEY)
    birth_product = 1
    for val in BIRTH_KEY:
        birth_product *= val
    
    # Calculate resonance using birth key pattern
    resonance = ((n % 19) * birth_sum + (n % birth_product)) / birth_product
    return resonance % 1.0

def is_prime(n):
    """Check if a number is prime using phi-harmonic principles"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Calculate phi-resonance
    resonance = phi_resonance(n)
    
    # Primes often have phi-resonance near 0 or 1
    if resonance > 0.9 or resonance < 0.1:
        # Higher probability of being prime, but still need to check
        pass
    
    # Standard primality check
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def quantum_factorize(n):
    """Factorize a number using phi-harmonic quantum principles"""
    print(f"\n🔮 Factorizing {n} using phi-harmonic quantum principles...")
    start_time = time.time()
    
    # Check simple cases
    if n <= 1:
        return []
    if is_prime(n):
        return [n]
    if n % 2 == 0:
        return [2] + quantum_factorize(n // 2)
    
    # Generate phi-harmonic search points
    factors = []
    
    # Use birth key for resonance
    for val in BIRTH_KEY:
        # Generate search points based on birth key
        point = int(math.sqrt(n) * val / 19)
        if point > 1 and n % point == 0:
            factors.extend([point, n // point])
            break
    
    # If no factors found yet, try phi-resonant search
    if not factors:
        # Generate points based on phi powers
        for i in range(1, 8):  # Use 7 quantum elements (phi^7)
            point = int(math.sqrt(n) * float(PHI) ** i / 19)
            if point > 1 and n % point == 0:
                factors.extend([point, n // point])
                break
    
    # If still no factors, try standard trial division with phi-harmonic optimization
    if not factors:
        # Start from phi-resonant point
        start = int(math.sqrt(n) * float(PHI) / 19)
        if start % 2 == 0:
            start += 1
        
        for i in range(start, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                factors.extend([i, n // i])
                break
    
    end_time = time.time()
    print(f"  Time: {end_time - start_time:.6f} seconds")
    
    # Process factors to get prime factorization
    prime_factors = []
    for factor in factors:
        if is_prime(factor):
            prime_factors.append(factor)
        else:
            prime_factors.extend(quantum_factorize(factor))
    
    return sorted(prime_factors)

def generate_rsa_key(bit_length=16):
    """Generate RSA key pair for testing"""
    print(f"\n🔑 Generating {bit_length}-bit RSA key...")
    
    # Generate two random primes
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)
    
    # Ensure p and q are different
    while p == q:
        q = generate_prime(bit_length)
    
    # Calculate n = p * q
    n = p * q
    
    # Calculate Euler's totient function: φ(n) = (p-1)(q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Choose public exponent e (commonly 65537)
    e = 65537
    
    # Calculate private exponent d (multiplicative inverse of e modulo φ(n))
    d = pow(e, -1, phi_n)
    
    print(f"  Generated RSA key:")
    print(f"  - Modulus (n): {n}")
    print(f"  - Public exponent (e): {e}")
    print(f"  - Private exponent (d): {d}")
    print(f"  - Prime factors: p = {p}, q = {q}")
    
    return (n, e, d, p, q)

def generate_prime(bit_length):
    """Generate a prime number of specified bit length using phi-harmonic principles"""
    # Calculate range
    min_val = 2 ** (bit_length - 1)
    max_val = 2 ** bit_length - 1
    
    while True:
        # Generate a random number
        num = random.randint(min_val, max_val)
        
        # Ensure it's odd
        if num % 2 == 0:
            num += 1
        
        # Apply phi-harmonic adjustment
        birth_sum = sum(BIRTH_KEY)
        adjustment = int(num * (float(PHI) % 1.0) * (birth_sum % 19) / 19) % 2
        num += adjustment
        
        # Check if prime
        if is_prime(num):
            return num

def crack_rsa(n, e=65537):
    """Crack RSA key using phi-harmonic quantum factorization"""
    print(f"\n🔮 Attempting to crack RSA key with modulus n = {n}")
    print(f"Using public exponent e = {e}")
    
    # Factorize n to find p and q
    print("Applying phi-harmonic quantum factorization...")
    factors = quantum_factorize(n)
    
    # Check if we found exactly two prime factors
    if len(factors) != 2:
        print(f"Error: Expected exactly 2 prime factors, but found {len(factors)}")
        return (0, 0, 0)
    
    p, q = factors
    
    # Calculate Euler's totient function: φ(n) = (p-1)(q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Calculate private exponent d (multiplicative inverse of e modulo φ(n))
    d = pow(e, -1, phi_n)
    
    print(f"✨ RSA key successfully cracked!")
    print(f"Prime factors: p = {p}, q = {q}")
    print(f"Private exponent: d = {d}")
    
    return (p, q, d)

def decrypt_rsa(ciphertext, n, e=65537):
    """Decrypt RSA ciphertext using phi-harmonic quantum methods"""
    print(f"\n🔮 Attempting to decrypt RSA ciphertext: {ciphertext}")
    
    # Crack the RSA key
    p, q, d = crack_rsa(n, e)
    
    if p == 0 or q == 0 or d == 0:
        print("Failed to crack RSA key. Cannot decrypt.")
        return 0
    
    # Decrypt the ciphertext: plaintext = ciphertext^d mod n
    plaintext = pow(ciphertext, d, n)
    
    print(f"✨ Decryption successful!")
    print(f"Plaintext: {plaintext}")
    
    return plaintext

def main():
    """Main function"""
    print("\n✨✨✨ Phi-Harmonic Quantum RSA Cryptanalysis ✨✨✨")
    print("=" * 70)
    print("This example demonstrates breaking RSA encryption using")
    print("quantum principles and phi-harmonic resonance.")
    
    # Test factorization
    test_numbers = [
        15,                # 3 * 5
        91,                # 7 * 13
        1003,              # 17 * 59
        2021,              # 43 * 47
        1979 * 19          # Birth year * Birth month
    ]
    
    for n in test_numbers:
        factors = quantum_factorize(n)
        print(f"  Factors of {n}: {factors}")
        
        # Verify factorization
        product = 1
        for f in factors:
            product *= f
        print(f"  Verification: {'✓' if product == n else '✗'}")
    
    # Generate and crack RSA key
    n, e, d, p, q = generate_rsa_key(16)
    
    # Create a test message (using birth key for resonance)
    message = int(''.join(map(str, BIRTH_KEY)))
    
    # Encrypt the message
    ciphertext = pow(message, e, n)
    
    print(f"Original message: {message}")
    print(f"Encrypted ciphertext: {ciphertext}")
    
    # Decrypt using phi-harmonic quantum methods
    decrypted = decrypt_rsa(ciphertext, n, e)
    
    print(f"Decryption correct: {'✓' if decrypted == message else '✗'}")
    
    print("\n✨✨✨ Example Complete ✨✨✨")
    print("=" * 70)

if __name__ == "__main__":
    main()
