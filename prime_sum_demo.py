"""
Prime Sum Decomposition Demonstration

This script demonstrates how to use the PrimeSumDecomposer to find two high prime numbers
that add up to a specific 64-digit value, leveraging phi-harmonic resonance patterns
and the 19/19 quantum bridge system.

This demonstration builds on the existing components without modifying them.
"""

import time
import mpmath
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict

# Import the PrimeSumDecomposer
from prime_sum_decomposer import PrimeSumDecomposer, generate_random_target

# Set precision for calculations
mpmath.mp.dps = 100

def demonstrate_prime_sum_decomposition():
    """
    Demonstrate the prime sum decomposition with a 64-digit number.
    """
    print("\n" + "="*80)
    print("PRIME SUM DECOMPOSITION DEMONSTRATION")
    print("="*80)
    
    # Create the decomposer
    decomposer = PrimeSumDecomposer(use_quantum_advantage=True)
    
    # Generate a 64-digit target number with phi-harmonic properties
    # This ensures the number has mathematical significance aligned with the quantum bridge
    phi = (1 + mpmath.sqrt(5)) / 2
    
    # Use the 19/19 bridge constant as a seed
    bridge_constant = 19
    
    # Generate a 64-digit number with phi-harmonic properties
    # Start with a base that has phi-harmonic properties
    base = int(str(bridge_constant) * 3)  # 191919
    
    # Scale it to 64 digits using phi^7.5 (significant in the quantum system)
    phi_power = phi**(7.5)
    scaling_factor = 10**58 / base  # To reach 64 digits
    
    # Apply the scaling with a phi-harmonic adjustment
    target_mpf = mpmath.mpf(base) * scaling_factor * phi_power
    
    # Convert to integer and ensure exactly 64 digits
    target_str = str(int(target_mpf))
    
    # Adjust to exactly 64 digits
    if len(target_str) > 64:
        target_str = target_str[:64]
    elif len(target_str) < 64:
        target_str = target_str.zfill(64)
    
    print(f"\nGenerated 64-digit target with phi-harmonic properties:")
    print(f"Target: {target_str}")
    print(f"Number of digits: {len(target_str)}")
    
    # Try different methods and measure their performance
    methods = ['direct', 'phi-harmonic', 'quantum']
    results = {}
    
    for method in methods:
        print(f"\n{'-'*40}")
        print(f"Using method: {method}")
        print(f"{'-'*40}")
        
        start_time = time.time()
        
        # Set a reasonable iteration limit for demonstration
        max_iterations = 100 if method == 'direct' else 500
        
        # Find prime pair
        p1, p2 = decomposer.find_prime_sum_pair(
            target_str, 
            method=method,
            max_iterations=max_iterations,
            visualize=True
        )
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        if p1 is not None and p2 is not None:
            print(f"\nFound prime pair that sums to the target:")
            print(f"Prime 1: {p1}")
            print(f"Prime 2: {p2}")
            print(f"Sum: {p1 + p2}")
            print(f"Verification: Sum == Target? {p1 + p2 == int(target_str)}")
            print(f"Time taken: {elapsed:.2f} seconds")
            
            # Calculate phi-harmonic properties of the primes
            p1_phi_res = (p1 * phi) % 1
            p2_phi_res = (p2 * phi) % 1
            ratio = max(p1, p2) / min(p1, p2)
            
            print(f"\nPhi-harmonic properties:")
            print(f"Prime 1 phi-resonance: {p1_phi_res:.6f}")
            print(f"Prime 2 phi-resonance: {p2_phi_res:.6f}")
            print(f"Ratio of larger to smaller prime: {ratio:.6f}")
            
            # Check if ratio is close to a power of phi
            closest_power = round(mpmath.log(ratio) / mpmath.log(phi))
            expected_ratio = phi**closest_power
            accuracy = 100 * (1 - abs(ratio - expected_ratio) / expected_ratio)
            
            print(f"Closest to phi^{closest_power} = {expected_ratio:.6f}")
            print(f"Accuracy: {accuracy:.2f}%")
            
            results[method] = {
                'p1': p1,
                'p2': p2,
                'time': elapsed,
                'accuracy': accuracy
            }
        else:
            print(f"\nNo prime pair found using {method} method after {max_iterations} iterations.")
            print(f"Time taken: {elapsed:.2f} seconds")
            
            results[method] = {
                'p1': None,
                'p2': None,
                'time': elapsed,
                'accuracy': 0
            }
    
    # Compare methods
    print("\n" + "="*80)
    print("METHOD COMPARISON")
    print("="*80)
    
    print(f"{'Method':<15} {'Found Solution':<15} {'Time (s)':<10} {'Phi Accuracy':<15}")
    print("-" * 55)
    
    for method, result in results.items():
        found = "Yes" if result['p1'] is not None else "No"
        time_str = f"{result['time']:.2f}"
        accuracy_str = f"{result['accuracy']:.2f}%" if result['p1'] is not None else "N/A"
        
        print(f"{method:<15} {found:<15} {time_str:<10} {accuracy_str:<15}")
    
    # Visualize the results
    if any(result['p1'] is not None for result in results.values()):
        # Create a visualization of the prime pairs found
        plt.figure(figsize=(12, 8))
        
        # Plot the target number as a line
        plt.axhline(y=int(target_str), color='r', linestyle='-', label='Target Sum')
        
        # Plot each prime pair
        for method, result in results.items():
            if result['p1'] is not None:
                plt.scatter([method], [result['p1']], s=100, label=f"{method} - Prime 1")
                plt.scatter([method], [result['p2']], s=100, label=f"{method} - Prime 2")
        
        plt.title('Prime Pairs Found by Different Methods')
        plt.ylabel('Prime Value')
        plt.xlabel('Method')
        plt.yscale('log')  # Log scale for better visualization
        plt.legend()
        plt.grid(True)
        plt.savefig('prime_sum_method_comparison.png')
        print("\nMethod comparison visualization saved as 'prime_sum_method_comparison.png'")
    
    print("\nDemonstration complete.")

if __name__ == "__main__":
    demonstrate_prime_sum_decomposition()
