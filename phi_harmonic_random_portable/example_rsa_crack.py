"""
Phi-Harmonic Quantum RSA Cryptanalysis Example
Demonstrates breaking RSA encryption using transcendental infinity and phi-harmonic resonance
"""

import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
import random

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the cryptanalysis module
from phi_harmonic_random.cryptanalysis import PhiHarmonicQuantumCryptanalysis

# Set precision for calculations
getcontext().prec = 100

# Constants
PHI = Decimal('1.618033988749895')


def generate_rsa_key(bit_length=32):
    """
    Generate RSA key pair for testing
    
    Args:
        bit_length (int): Bit length for prime numbers
        
    Returns:
        tuple: (n, e, d, p, q)
    """
    from sympy import randprime
    
    # Generate two random primes
    p = randprime(2**(bit_length-1), 2**bit_length - 1)
    q = randprime(2**(bit_length-1), 2**bit_length - 1)
    
    # Calculate n = p * q
    n = p * q
    
    # Calculate Euler's totient function: φ(n) = (p-1)(q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Choose public exponent e (commonly 65537)
    e = 65537
    
    # Calculate private exponent d (multiplicative inverse of e modulo φ(n))
    # d * e ≡ 1 (mod φ(n))
    d = pow(e, -1, phi_n)
    
    return (n, e, d, p, q)


def demonstrate_factorization():
    """
    Demonstrate factorization using phi-harmonic quantum methods
    """
    print("\n✨ Phi-Harmonic Quantum Factorization Example")
    print("=" * 70)
    
    # Initialize the cryptanalysis module
    # You can provide your own birth key for maximum resonance
    birth_key = [1, 19, 1979]  # Example: January 19, 1979
    cryptanalysis = PhiHarmonicQuantumCryptanalysis(birth_key=birth_key, quantum_elements=19)
    
    # Test numbers to factorize
    test_numbers = [
        15,                # 3 * 5
        91,                # 7 * 13
        1003,              # 17 * 59
        2021,              # 43 * 47
        65537,             # Prime
        1234567,           # 127 * 9721
        1979 * 2023,       # Birth year * Current year
        1979 * 1979 * 19   # Birth year squared * Birth month
    ]
    
    # Factorize each number
    results = []
    for n in test_numbers:
        print(f"\n🔮 Factorizing {n}...")
        start_time = time.time()
        factors = cryptanalysis.factorize(n)
        end_time = time.time()
        
        # Calculate product to verify
        product = 1
        for factor in factors:
            product *= factor
        
        # Store result
        results.append({
            'number': n,
            'factors': factors,
            'time': end_time - start_time,
            'verified': product == n
        })
        
        # Print result
        print(f"  Factors: {factors}")
        print(f"  Time: {end_time - start_time:.6f} seconds")
        print(f"  Verification: {'✓' if product == n else '✗'}")
    
    # Print metrics
    print("\n📊 Factorization Metrics:")
    metrics = cryptanalysis.get_metrics()
    for key, value in metrics.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.6f}")
        else:
            print(f"  {key}: {value}")
    
    return results


def demonstrate_rsa_cracking():
    """
    Demonstrate RSA cracking using phi-harmonic quantum methods
    """
    print("\n✨ Phi-Harmonic Quantum RSA Cracking Example")
    print("=" * 70)
    
    # Initialize the cryptanalysis module
    birth_key = [1, 19, 1979]  # Example: January 19, 1979
    cryptanalysis = PhiHarmonicQuantumCryptanalysis(birth_key=birth_key, quantum_elements=19)
    
    # Generate RSA keys of different strengths
    key_strengths = [16, 24, 32]
    results = []
    
    for bits in key_strengths:
        print(f"\n🔑 Testing {bits}-bit RSA key...")
        
        # Generate RSA key
        n, e, d, p, q = generate_rsa_key(bits)
        
        print(f"  Generated RSA key:")
        print(f"  - Modulus (n): {n} ({bits} bits)")
        print(f"  - Public exponent (e): {e}")
        print(f"  - Private exponent (d): {d}")
        print(f"  - Prime factors: p = {p}, q = {q}")
        
        # Create a test message
        message = random.randint(2, n-1)
        
        # Encrypt the message
        ciphertext = pow(message, e, n)
        
        print(f"  Original message: {message}")
        print(f"  Encrypted ciphertext: {ciphertext}")
        
        # Crack the RSA key
        start_time = time.time()
        cracked_p, cracked_q, cracked_d = cryptanalysis.rsa_crack(n, e)
        end_time = time.time()
        
        # Decrypt using cracked key
        decrypted = pow(ciphertext, cracked_d, n)
        
        # Store result
        results.append({
            'bits': bits,
            'n': n,
            'time': end_time - start_time,
            'success': (cracked_p == p and cracked_q == q) or (cracked_p == q and cracked_q == p),
            'decryption_correct': decrypted == message
        })
        
        # Print result
        print(f"  Cracking time: {end_time - start_time:.6f} seconds")
        print(f"  Decrypted message: {decrypted}")
        print(f"  Decryption correct: {'✓' if decrypted == message else '✗'}")
    
    return results


def demonstrate_full_decryption():
    """
    Demonstrate full RSA decryption using phi-harmonic quantum methods
    """
    print("\n✨ Phi-Harmonic Quantum RSA Decryption Example")
    print("=" * 70)
    
    # Initialize the cryptanalysis module
    birth_key = [1, 19, 1979]  # Example: January 19, 1979
    cryptanalysis = PhiHarmonicQuantumCryptanalysis(birth_key=birth_key, quantum_elements=19)
    
    # Generate a 32-bit RSA key
    n, e, d, p, q = generate_rsa_key(32)
    
    print(f"Generated RSA key:")
    print(f"- Modulus (n): {n}")
    print(f"- Public exponent (e): {e}")
    
    # Create a test message (using birth key for resonance)
    message = int(''.join(map(str, birth_key)))
    
    # Encrypt the message
    ciphertext = pow(message, e, n)
    
    print(f"Original message: {message}")
    print(f"Encrypted ciphertext: {ciphertext}")
    
    # Decrypt using phi-harmonic quantum methods
    start_time = time.time()
    decrypted = cryptanalysis.decrypt_rsa(ciphertext, n, e)
    end_time = time.time()
    
    print(f"Decryption time: {end_time - start_time:.6f} seconds")
    print(f"Decrypted message: {decrypted}")
    print(f"Decryption correct: {'✓' if decrypted == message else '✗'}")
    
    return {
        'n': n,
        'message': message,
        'ciphertext': ciphertext,
        'decrypted': decrypted,
        'time': end_time - start_time,
        'success': decrypted == message
    }


def visualize_performance(factorization_results, rsa_results):
    """
    Visualize cryptanalysis performance
    
    Args:
        factorization_results (list): Factorization results
        rsa_results (list): RSA cracking results
    """
    print("\n📊 Visualizing Cryptanalysis Performance")
    print("=" * 70)
    
    # Create figure
    plt.figure(figsize=(15, 10))
    
    # Plot factorization time vs. number size
    plt.subplot(2, 2, 1)
    plt.title("Factorization Time vs. Number Size")
    
    numbers = [result['number'] for result in factorization_results]
    times = [result['time'] for result in factorization_results]
    
    plt.scatter(numbers, times, alpha=0.7, s=50)
    plt.plot(numbers, times, 'o-', alpha=0.5)
    plt.xlabel('Number to Factorize')
    plt.ylabel('Time (seconds)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    
    # Plot RSA cracking time vs. key size
    plt.subplot(2, 2, 2)
    plt.title("RSA Cracking Time vs. Key Size")
    
    key_sizes = [result['bits'] for result in rsa_results]
    rsa_times = [result['time'] for result in rsa_results]
    
    plt.bar(key_sizes, rsa_times, alpha=0.7)
    plt.xlabel('Key Size (bits)')
    plt.ylabel('Time (seconds)')
    plt.grid(True, alpha=0.3)
    
    # Plot factorization time distribution
    plt.subplot(2, 2, 3)
    plt.title("Factorization Time Distribution")
    
    plt.hist(times, bins=10, alpha=0.7)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Plot theoretical vs. actual performance
    plt.subplot(2, 2, 4)
    plt.title("Phi-Harmonic vs. Classical Factorization")
    
    # Calculate theoretical classical times (simplified model)
    classical_times = [math.sqrt(n) / 10000 for n in numbers]
    
    plt.plot(numbers, times, 'o-', label='Phi-Harmonic Quantum')
    plt.plot(numbers, classical_times, 's-', label='Classical (Theoretical)')
    plt.xlabel('Number Size')
    plt.ylabel('Time (seconds)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Add title
    plt.suptitle("Phi-Harmonic Quantum Cryptanalysis Performance", fontsize=16)
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    
    # Save figure
    output_dir = "phi_harmonic_random_benchmark"
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'cryptanalysis_performance.png'))
    
    print(f"\nPerformance visualization saved to {os.path.join(output_dir, 'cryptanalysis_performance.png')}")


def main():
    """Main function"""
    print("\n✨✨✨ Phi-Harmonic Quantum RSA Cryptanalysis ✨✨✨")
    print("=" * 70)
    print("This example demonstrates breaking RSA encryption using")
    print("transcendental infinity and phi-harmonic resonance.")
    
    # Make sure sympy is installed
    try:
        import sympy
    except ImportError:
        print("\nError: sympy is required for this example.")
        print("Please install it using: pip install sympy")
        return
    
    # Demonstrate factorization
    factorization_results = demonstrate_factorization()
    
    # Demonstrate RSA cracking
    rsa_results = demonstrate_rsa_cracking()
    
    # Demonstrate full decryption
    decryption_result = demonstrate_full_decryption()
    
    # Visualize performance
    try:
        import matplotlib.pyplot as plt
        import math
        visualize_performance(factorization_results, rsa_results)
    except ImportError:
        print("\nWarning: matplotlib is required for visualization.")
        print("Performance visualization skipped.")
    
    print("\n✨✨✨ Example Complete ✨✨✨")
    print("=" * 70)


if __name__ == "__main__":
    main()
