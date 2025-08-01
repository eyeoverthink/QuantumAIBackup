"""
Prime Sum Decomposition Small Demo

This script demonstrates the prime sum decomposition approach with a smaller target value
that is more feasible to find solutions for in a reasonable time. It leverages the
phi-harmonic resonance patterns and 19/19 quantum bridge system.
"""

import time
import mpmath
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional

# Import our components
from quantum_prime_helper import QuantumPrimeTestingHelper
from high_prime_sum_finder import HighPrimeSumFinder

def demonstrate_with_smaller_target():
    """
    Demonstrate the prime sum decomposition with a smaller target value.
    """
    print("\n" + "="*80)
    print("PRIME SUM DECOMPOSITION SMALL DEMONSTRATION")
    print("="*80)
    
    # Create the finder
    finder = HighPrimeSumFinder()
    
    # Try a few different targets with increasing simplicity
    targets = []
    
    # Target 1: Based on phi^7.5 (significant in the quantum system)
    phi = (1 + mpmath.sqrt(5)) / 2
    phi_power = phi**(7.5)  # Significant in the quantum system
    bridge_constant = 19
    base = bridge_constant * 100 + 79  # 1979 (from birthdate)
    target_mpf = mpmath.mpf(base) * phi_power
    target_int = int(target_mpf)
    if target_int % 2 == 0:
        target_int += 1
    targets.append((str(target_int), "Phi^7.5 based target"))
    
    # Target 2: A simpler number based on 19 and 79
    target2 = 1979 * 19
    if target2 % 2 == 0:
        target2 += 1
    targets.append((str(target2), "1979 * 19"))
    
    # Target 3: An even simpler number that should definitely have prime pairs
    target3 = 100
    # For even numbers, Goldbach's conjecture states they can be written as the sum of two primes
    # So we'll leave this one even to ensure we find a solution
    targets.append((str(target3), "Simple 3-digit number"))
    
    # Try each target
    for target_str, description in targets:
        print(f"\nTrying target: {target_str} ({description})")
    
    print(f"\nGenerated target with phi-harmonic properties:")
    print(f"Target: {target_str}")
    print(f"Number of digits: {len(target_str)}")
    print(f"Phi^7.5 value used: {phi_power}")
    print(f"Base value (from 19/19 bridge): {base}")
    
    # Find prime pair with more iterations for this smaller target
    max_iterations = 5000  # Much more iterations for this smaller target
    
    print(f"\nSearching for prime pair with max {max_iterations} iterations...")
    start_time = time.time()
    
    p1, p2 = finder.find_prime_pair(target_str, max_iterations=max_iterations)
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    if p1 is not None and p2 is not None:
        print(f"\nSuccess! Found prime pair after {elapsed:.2f} seconds:")
        print(f"Prime 1: {p1}")
        print(f"Prime 2: {p2}")
        print(f"Sum: {p1 + p2}")
        print(f"Verification: Sum == Target? {p1 + p2 == int(target_str)}")
        
        # Analyze the prime pair
        finder.analyze_prime_pair(p1, p2)
    else:
        print(f"\nNo prime pair found after {max_iterations} iterations ({elapsed:.2f} seconds).")
        print("Try increasing max_iterations or using a different target value.")

def find_prime_pair_for_special_number():
    """
    Find a prime pair for a special number with significance to the 19/19 bridge.
    """
    print("\n" + "="*80)
    print("FINDING PRIME PAIR FOR SPECIAL NUMBER")
    print("="*80)
    
    # Use the prime helper directly for more control
    prime_helper = QuantumPrimeTestingHelper()
    
    # Create a special target based on the 19/19 bridge
    # We'll try a few different special targets with significance
    special_targets = [
        19071979,  # Combines patent prefix (19071) and birth year (1979)
        1979 * 19,  # Birth year multiplied by 19
        19 * 1000 + 79  # 19079 (19 followed by 79 from birth year)
    ]
    
    found_overall = False
    
    for special_target in special_targets:
        print(f"\nSpecial target: {special_target}")
        if special_target == 19071979:
            print(f"This number combines the patent prefix (19071) and birth year (1979)")
        elif special_target == 1979 * 19:
            print(f"This number is birth year (1979) multiplied by 19")
        else:
            print(f"This number is 19 followed by 79 from birth year")
        
        # Find prime pair using direct search
        print("\nSearching for prime pair...")
        
        # Start with midpoint
        midpoint = special_target // 2
        
        # Search parameters
        max_iterations = 5000
        found = False
        
        start_time = time.time()
        
        for i in range(max_iterations):
            # Calculate offset using phi-harmonic pattern
            phi = (1 + np.sqrt(5)) / 2
            offset = int(i * ((phi * i) % 1) * 19)
            
            # Alternate direction
            if i % 2 == 0:
                offset = -offset
            
            # Calculate candidate values
            p1_candidate = midpoint + offset
            p2_candidate = special_target - p1_candidate
            
            # Ensure they're odd (except if 2 is involved)
            if p1_candidate > 2 and p1_candidate % 2 == 0:
                p1_candidate += 1
                p2_candidate -= 1
            elif p2_candidate > 2 and p2_candidate % 2 == 0:
                p2_candidate += 1
                p1_candidate -= 1
            
            # Check if both are prime
            if prime_helper.is_prime(p1_candidate) and prime_helper.is_prime(p2_candidate):
                found = True
                p1, p2 = p1_candidate, p2_candidate
                break
            
            # Progress update
            if (i + 1) % 100 == 0:
                print(f"Completed {i+1} iterations...")
    
        end_time = time.time()
        elapsed = end_time - start_time
        
        if found:
            print(f"\nSuccess! Found prime pair after {i+1} iterations ({elapsed:.2f} seconds):")
            print(f"Prime 1: {p1}")
            print(f"Prime 2: {p2}")
            print(f"Sum: {p1 + p2}")
            print(f"Verification: Sum == Target? {p1 + p2 == special_target}")
            found_overall = True
        
            # Calculate phi-harmonic properties
            ratio = max(p1, p2) / min(p1, p2)
            phi = (1 + np.sqrt(5)) / 2
            closest_power = round(np.log(ratio) / np.log(phi))
            expected_ratio = phi**closest_power
            accuracy = 100 * (1 - abs(ratio - expected_ratio) / expected_ratio)
        
            print("\nPhi-harmonic properties:")
            print(f"Ratio (larger/smaller): {ratio:.6f}")
            print(f"Closest to phi^{closest_power} = {expected_ratio:.6f}")
            print(f"Accuracy: {accuracy:.2f}%")
            
            # Check 19-based resonance
            p1_mod_19 = p1 % 19
            p2_mod_19 = p2 % 19
            
            print("\n19-based resonance:")
            print(f"P1 mod 19 = {p1_mod_19}")
            print(f"P2 mod 19 = {p2_mod_19}")
            print(f"Sum mod 19 = {(p1 + p2) % 19}")
            
            # Create visualization
            plt.figure(figsize=(10, 6))
            
            # Plot the primes
            plt.bar(['Prime 1', 'Prime 2'], [p1, p2], color=['blue', 'green'])
            
            # Add labels
            plt.title(f'Prime Pair for Special Number {special_target}')
            plt.ylabel('Value')
            plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        
        # Add text annotations
        plt.annotate(f"Phi-harmonic accuracy: {accuracy:.2f}%",
                    xy=(0.5, 0.9),
                    xycoords='figure fraction',
                    ha='center',
                    bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3))
        
        # Save figure
        plt.savefig('special_number_prime_pair.png')
        print("\nVisualization saved as 'special_number_prime_pair.png'")
    else:
        print(f"\nNo prime pair found after {max_iterations} iterations ({elapsed:.2f} seconds).")

if __name__ == "__main__":
    # First try with a known simple case to verify the system works
    print("\n" + "="*80)
    print("VERIFICATION WITH KNOWN PRIME PAIRS")
    print("="*80)
    
    # Verify with some known Goldbach pairs
    prime_helper = QuantumPrimeTestingHelper()
    known_pairs = [
        (4, [2, 2]),       # 2+2=4
        (6, [3, 3]),       # 3+3=6
        (10, [3, 7, 5, 5]) # 3+7=10, 5+5=10
    ]
    
    for target, expected_primes in known_pairs:
        print(f"\nVerifying target: {target}")
        print(f"Expected prime pairs: {', '.join([f'{p[0]}+{p[1]}={target}' for p in zip(expected_primes[::2], expected_primes[1::2])])}")
        
        found = False
        for p1 in range(2, target):
            p2 = target - p1
            if prime_helper.is_prime(p1) and prime_helper.is_prime(p2):
                found = True
                print(f"Found prime pair: {p1} + {p2} = {target}")
                break
        
        if not found:
            print(f"FAILED to find prime pair for {target}!")
    
    # Then run the main demonstrations
    demonstrate_with_smaller_target()
    find_prime_pair_for_special_number()
