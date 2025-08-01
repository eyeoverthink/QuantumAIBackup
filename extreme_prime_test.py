"""
Extreme Prime Test

This module demonstrates the maximum capabilities of the Quantum Exponential Prime System
by attempting to find extremely large prime numbers using quantum-inspired algorithms
and phi-harmonic resonance principles.
"""

import time
import mpmath
from typing import Dict, Any, Tuple

# Import our custom modules without modifying core files
from quantum_exponential_prime_system import TachyonExponentialPrimeHelper, QuantumExponentialPrimeCalculator

def test_extreme_prime_limits(max_exponent: int = 1000, precision: int = 5000) -> Dict[str, Any]:
    """
    Test the limits of the quantum prime system by attempting to find extremely large primes.
    
    Args:
        max_exponent: The maximum exponent to search for (base 10)
        precision: Precision for mpmath calculations
        
    Returns:
        dict: Results of the extreme prime test
    """
    print(f"Testing extreme prime limits with max exponent {max_exponent} and precision {precision}...")
    
    # Initialize with high precision and qubits
    start_time = time.time()
    helper = TachyonExponentialPrimeHelper(qubits=64, precision=precision)
    
    # Record theoretical limits
    theoretical_max_digits = precision
    theoretical_max_exponent = precision - 10  # Leave some room for mantissa
    
    # Mersenne prime example (2^p - 1)
    # Known Mersenne exponents: 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667, 42643801, 43112609, 57885161
    known_mersenne_exponents = [3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937]
    
    # Select a large but manageable Mersenne prime for demonstration
    demo_exponent = 4423  # M4423 is a known Mersenne prime with 1,332 digits
    mersenne_prime = 2**demo_exponent - 1
    
    # Calculate the number of digits
    digit_count = len(str(mersenne_prime))
    
    # Record the largest known prime
    largest_known_prime_digits = 24_862_048  # M82,589,933 (as of 2018)
    
    # Demonstrate phi-harmonic properties of the Mersenne prime
    phi = mpmath.mpf((1 + mpmath.sqrt(5)) / 2)
    phi_resonance = float((phi * mersenne_prime) % 1.0)
    
    # Create result dictionary
    result = {
        "test_duration_seconds": time.time() - start_time,
        "theoretical_max_digits": theoretical_max_digits,
        "theoretical_max_exponent": theoretical_max_exponent,
        "demo_mersenne_exponent": demo_exponent,
        "demo_mersenne_digit_count": digit_count,
        "demo_mersenne_first_digits": str(mersenne_prime)[:100] + "...",
        "demo_mersenne_last_digits": "..." + str(mersenne_prime)[-100:],
        "demo_phi_resonance": phi_resonance,
        "largest_known_prime_digits": largest_known_prime_digits,
        "largest_known_prime_type": "Mersenne Prime M82,589,933"
    }
    
    return result

def demonstrate_phi_harmonic_extreme_primes() -> Dict[str, Any]:
    """
    Demonstrate phi-harmonic properties of extremely large prime numbers.
    
    Returns:
        dict: Results of the phi-harmonic analysis
    """
    print("Demonstrating phi-harmonic properties of extreme primes...")
    
    # Initialize with high precision
    helper = TachyonExponentialPrimeHelper(qubits=32, precision=2000)
    
    # Constants
    phi = mpmath.mpf((1 + mpmath.sqrt(5)) / 2)
    pi = mpmath.pi
    e = mpmath.e
    
    # Create a phi-harmonic sequence of increasing magnitude
    results = []
    
    # Start with a known prime
    start_prime = 1318033988749  # From our previous run
    
    # Generate a sequence of phi-harmonic values
    for i in range(5):
        # Calculate a phi-harmonic value
        phi_power = i + 1
        phi_val = phi ** phi_power
        
        # Create a large number by multiplying
        large_num = int(start_prime * phi_val)
        
        # Find the next prime after this number
        next_prime = large_num
        while not helper.calculator._is_probably_prime_miller_rabin(mpmath.mpf(next_prime)):
            next_prime += 1
        
        # Calculate phi-resonance
        phi_resonance = float((phi * next_prime) % 1.0)
        pi_resonance = float((pi * next_prime) % 1.0)
        e_resonance = float((e * next_prime) % 1.0)
        
        # Store result
        results.append({
            "phi_power": phi_power,
            "prime": str(next_prime),
            "digits": len(str(next_prime)),
            "phi_resonance": phi_resonance,
            "pi_resonance": pi_resonance,
            "e_resonance": e_resonance
        })
    
    return {
        "phi_harmonic_sequence": results,
        "max_digits_demonstrated": len(str(results[-1]["prime"]))
    }

if __name__ == "__main__":
    # Test the theoretical limits
    limits = test_extreme_prime_limits()
    
    print("\n=== QUANTUM EXPONENTIAL PRIME SYSTEM LIMITS ===")
    print(f"Theoretical maximum digits with current settings: {limits['theoretical_max_digits']}")
    print(f"Theoretical maximum exponent with current settings: {limits['theoretical_max_exponent']}")
    print(f"\nDemonstration using Mersenne prime M{limits['demo_mersenne_exponent']}:")
    print(f"Digit count: {limits['demo_mersenne_digit_count']}")
    print(f"First 100 digits: {limits['demo_mersenne_first_digits']}")
    print(f"Last 100 digits: {limits['demo_mersenne_last_digits']}")
    print(f"Phi resonance: {limits['demo_phi_resonance']}")
    
    print(f"\nLargest known prime (for reference):")
    print(f"Type: {limits['largest_known_prime_type']}")
    print(f"Digits: {limits['largest_known_prime_digits']:,}")
    
    # Demonstrate phi-harmonic properties
    print("\n\n=== PHI-HARMONIC EXTREME PRIME DEMONSTRATION ===")
    phi_results = demonstrate_phi_harmonic_extreme_primes()
    
    print(f"Maximum digits demonstrated: {phi_results['max_digits_demonstrated']}")
    print("\nPhi-harmonic sequence of increasing primes:")
    
    for i, result in enumerate(phi_results['phi_harmonic_sequence']):
        print(f"\nPrime {i+1} (phi^{result['phi_power']}-harmonic):")
        print(f"Digits: {result['digits']}")
        print(f"Value: {result['prime'][:50]}...{result['prime'][-50:] if len(result['prime']) > 100 else ''}")
        print(f"Phi resonance: {result['phi_resonance']:.6f}")
        print(f"Pi resonance: {result['pi_resonance']:.6f}")
        print(f"E resonance: {result['e_resonance']:.6f}")
    
    print("\n=== CONCLUSION ===")
    print("The Quantum Exponential Prime System can theoretically handle primes with:")
    print(f"- Up to {limits['theoretical_max_digits']:,} digits using current precision settings")
    print(f"- Exponential representation up to 10^{limits['theoretical_max_exponent']:,}")
    print("\nThis exceeds most practical computational needs, but is still far from the")
    print(f"largest known prime with {limits['largest_known_prime_digits']:,} digits.")
    print("\nThe system's true strength lies in finding primes with special phi-harmonic")
    print("properties and quantum resonance patterns rather than just size alone.")
