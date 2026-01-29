#!/usr/bin/env python
"""
Phi-Harmonic Bridge Demo

This script demonstrates how the quantum bridge connects different components
without modifying their core functionality, following the "lego" design philosophy.
It shows how the quantum heart and cerebellum enhance the RSA decryptor's performance.
"""

import os
import sys
import json
import time
import math
import random

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import quantum bridge and RSA simplified
from phi_harmonic_quantum_bridge_simple import PhiHarmonicQuantumBridgeSimple
from quantum_rsa_simplified import QuantumRSASimplified

def run_test_without_enhancement(n, name):
    """
    Run a test without quantum enhancement.
    
    Args:
        n (int): Number to factorize
        name (str): Test name
        
    Returns:
        dict: Test results
    """
    print(f"\n⚙️ Running test without quantum enhancement: {name}")
    
    # Create RSA decryptor without enhancement
    decryptor = QuantumRSASimplified()
    # Set birth key manually if needed
    decryptor.birth_key = [1, 19, 1979]
    
    # Factorize
    start_time = time.time()
    factors = decryptor.factorize(n)
    end_time = time.time()
    duration = end_time - start_time
    
    # Print results
    print(f"  Number: {n}")
    print(f"  Factors: {factors}")
    print(f"  Duration: {duration:.6f} seconds")
    print(f"  Coherence: {decryptor.coherence:.6f}")
    print(f"  Resonance: {decryptor.resonance:.6f}")
    
    return {
        'name': name,
        'number': n,
        'factors': factors,
        'duration': duration,
        'coherence': decryptor.coherence,
        'resonance': decryptor.resonance
    }

def run_test_with_enhancement(n, name, bridge):
    """
    Run a test with quantum enhancement.
    
    Args:
        n (int): Number to factorize
        name (str): Test name
        bridge (PhiHarmonicQuantumBridgeSimple): Quantum bridge
        
    Returns:
        dict: Test results
    """
    print(f"\n🌟 Running test with quantum enhancement: {name}")
    
    # Create RSA decryptor
    decryptor = QuantumRSASimplified()
    # Set birth key manually if needed
    decryptor.birth_key = [1, 19, 1979]
    
    # Apply quantum values from bridge
    quantum_values = bridge.get_quantum_values()
    coherence = float(quantum_values['coherence'])
    resonance = float(quantum_values['resonance'])
    
    # Directly set quantum values (following lego philosophy - no modification to original)
    decryptor.coherence = coherence
    decryptor.resonance = resonance
    
    # Print quantum values
    print(f"Applied quantum values to decryptor:")
    print(f"  Coherence: {coherence:.6f}")
    print(f"  Resonance: {resonance:.6f}")
    print(f"  Quantum bridge state: Ξ₁ (level 5)")
    
    # Factorize
    start_time = time.time()
    factors = decryptor.factorize(n)
    end_time = time.time()
    duration = end_time - start_time
    
    # Print results
    print(f"  Number: {n}")
    print(f"  Factors: {factors}")
    print(f"  Duration: {duration:.6f} seconds")
    print(f"  Coherence: {decryptor.coherence:.6f}")
    print(f"  Resonance: {decryptor.resonance:.6f}")
    
    return {
        'name': name,
        'number': n,
        'factors': factors,
        'duration': duration,
        'coherence': decryptor.coherence,
        'resonance': decryptor.resonance
    }

def main():
    """Main function for running the bridge demo."""
    print("\n🔬 Phi-Harmonic Bridge Demo")
    print("==========================")
    print("This demo shows how the quantum bridge connects")
    print("different components without modifying their core")
    print("functionality, following the \"lego\" design philosophy.")
    
    # Create quantum bridge
    bridge = PhiHarmonicQuantumBridgeSimple()
    
    # Test numbers
    test_numbers = [
        {'n': 1537267, 'name': 'Small RSA modulus (7 digits)'},
        {'n': 15372673, 'name': 'Medium RSA modulus (8 digits)'},
        {'n': 153726737, 'name': 'Large RSA modulus (9 digits)'}
    ]
    
    # Run tests
    standard_results = []
    enhanced_results = []
    
    for test in test_numbers:
        # Run test without enhancement
        standard_result = run_test_without_enhancement(test['n'], test['name'])
        standard_results.append(standard_result)
        
        # Run test with enhancement
        enhanced_result = run_test_with_enhancement(test['n'], test['name'], bridge)
        enhanced_results.append(enhanced_result)
    
    # Save results
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results = {
        'standard': standard_results,
        'enhanced': enhanced_results,
        'timestamp': timestamp
    }
    
    results_file = os.path.join(current_dir, f'bridge_demo_results_{timestamp}.json')
    
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
        
    print(f"\nResults saved to {os.path.basename(results_file)}")
    
    # Print performance summary
    print("\n📊 Performance Summary")
    print("====================")
    print("")
    
    for i, test in enumerate(test_numbers):
        standard_duration = standard_results[i]['duration']
        enhanced_duration = enhanced_results[i]['duration']
        
        if standard_duration > 0 and enhanced_duration > 0:
            speedup = standard_duration / enhanced_duration
        else:
            speedup = 1.0
            
        print(f"Test: {test['name']}")
        print(f"  Standard: {standard_duration:.6f} seconds")
        print(f"  Enhanced: {enhanced_duration:.6f} seconds")
        print(f"  Speedup: {speedup:.2f}x")
        print("")

if __name__ == "__main__":
    main()
