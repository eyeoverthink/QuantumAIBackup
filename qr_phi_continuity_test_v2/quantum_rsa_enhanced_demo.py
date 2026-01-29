#!/usr/bin/env python
"""
Quantum RSA Enhanced Demo

This script demonstrates how the quantum heart and cerebellum components
enhance the quantum RSA decryptor's performance through the phi-harmonic bridge.

It follows the 'lego' design philosophy by connecting components without
modifying their core functionality.
"""

import os
import sys
import time
import json
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 28

# Add paths for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'phi_harmonic_random_portable'))

# Import the simplified quantum bridge
from phi_harmonic_quantum_bridge_simple import get_bridge, apply_to_decryptor

# Import the simplified quantum RSA decryptor
from quantum_rsa_simplified import QuantumRSASimplified

def run_factorization_test(n, description, use_quantum_enhancement=False):
    """
    Run a factorization test with or without quantum enhancement.
    
    Args:
        n (int): Number to factorize
        description (str): Description of the test
        use_quantum_enhancement (bool): Whether to use quantum enhancement
        
    Returns:
        dict: Test results
    """
    # Create a new decryptor instance
    decryptor = QuantumRSASimplified()
    
    # Store original values
    original_coherence = decryptor.coherence
    original_resonance = decryptor.resonance
    
    # Apply quantum enhancement if requested
    if use_quantum_enhancement:
        print(f"\n🌟 Running test with quantum enhancement: {description}")
        bridge = get_bridge()
        apply_to_decryptor(decryptor)
    else:
        print(f"\n⚙️ Running test without quantum enhancement: {description}")
    
    # Run factorization
    start_time = time.time()
    factors = decryptor.factorize(n)
    end_time = time.time()
    duration = end_time - start_time
    
    # Prepare results
    results = {
        'number': n,
        'description': description,
        'quantum_enhanced': use_quantum_enhancement,
        'factors': factors,
        'duration': duration,
        'coherence': {
            'original': original_coherence,
            'used': decryptor.coherence
        },
        'resonance': {
            'original': original_resonance,
            'used': decryptor.resonance
        }
    }
    
    # Print results
    print(f"  Number: {n}")
    print(f"  Factors: {factors}")
    print(f"  Duration: {duration:.6f} seconds")
    print(f"  Coherence: {decryptor.coherence:.6f}")
    print(f"  Resonance: {decryptor.resonance:.6f}")
    
    return results

def save_comparison_results(results):
    """
    Save comparison results to a file.
    
    Args:
        results (list): List of test results
    """
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(current_dir, 'quantum_rsa_enhanced_results')
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, f'comparison_results_{timestamp}.json')
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nComparison results saved to {os.path.basename(output_file)}")

def main():
    """Main function to demonstrate quantum enhancement."""
    print("🔬 Quantum RSA Enhanced Demo")
    print("============================")
    print("This demo shows how the quantum heart and cerebellum components")
    print("enhance the quantum RSA decryptor's performance.")
    
    # Test numbers of increasing difficulty
    test_numbers = [
        {'n': 1537267, 'description': "Small RSA modulus (7 digits)"},
        {'n': 15372673, 'description': "Medium RSA modulus (8 digits)"},
        {'n': 153726737, 'description': "Large RSA modulus (9 digits)"}
    ]
    
    # Run tests with and without quantum enhancement
    results = []
    for test in test_numbers:
        # Run without enhancement
        standard_results = run_factorization_test(test['n'], test['description'], False)
        results.append(standard_results)
        
        # Run with quantum enhancement
        enhanced_results = run_factorization_test(test['n'], test['description'], True)
        results.append(enhanced_results)
    
    # Save comparison results
    save_comparison_results(results)
    
    # Print summary
    print("\n📊 Performance Summary")
    print("====================")
    for i in range(0, len(results), 2):
        standard = results[i]
        enhanced = results[i+1]
        
        speedup = standard['duration'] / enhanced['duration'] if enhanced['duration'] > 0 else 0
        print(f"\nTest: {standard['description']}")
        print(f"  Standard: {standard['duration']:.6f} seconds")
        print(f"  Enhanced: {enhanced['duration']:.6f} seconds")
        print(f"  Speedup: {speedup:.2f}x")

if __name__ == "__main__":
    main()
