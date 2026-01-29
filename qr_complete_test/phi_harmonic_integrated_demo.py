#!/usr/bin/env python
"""
Phi-Harmonic Integrated Demo

This script demonstrates the full capabilities of the orchestrated quantum system,
showing how the quantum heart, cerebellum, RSA decryptor, and random generator
all work together through the orchestration system.

It follows the "lego" design philosophy by connecting components without modifying
their core functionality, creating a system that's greater than the sum of its parts.
"""

import os
import sys
import json
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import orchestrator and components
from phi_harmonic_orchestrator import get_orchestrator
from phi_harmonic_random_orchestrator_adapter import PhiHarmonicRandomOrchestratorAdapter
from phi_harmonic_quantum_bridge_simple import PhiHarmonicQuantumBridgeSimple
from quantum_rsa_simplified import QuantumRSASimplified

# Constants
PHI = 1.618033988749895  # Golden ratio
PHI_INVERSE = 0.618033988749895  # Inverse golden ratio

def run_rsa_test(n, quantum_bridge):
    """
    Run an RSA factorization test with quantum enhancement.
    
    Args:
        n (int): Number to factorize
        quantum_bridge (PhiHarmonicQuantumBridgeSimple): Quantum bridge
        
    Returns:
        dict: Test results
    """
    print(f"\n🔬 RSA Factorization Test: {n}")
    
    # Create RSA decryptor
    decryptor = QuantumRSASimplified()
    
    # Apply quantum values from bridge
    quantum_values = quantum_bridge.get_quantum_values()
    coherence = float(quantum_values['coherence'])
    resonance = float(quantum_values['resonance'])
    
    # Directly set quantum values
    decryptor.coherence = coherence
    decryptor.resonance = resonance
    
    # Print quantum values
    print(f"Applied quantum values to decryptor:")
    print(f"  Coherence: {coherence:.6f}")
    print(f"  Resonance: {resonance:.6f}")
    
    # Factorize
    start_time = time.time()
    factors = decryptor.factorize(n)
    end_time = time.time()
    duration = end_time - start_time
    
    # Print results
    print(f"  Factors: {factors}")
    print(f"  Duration: {duration:.6f} seconds")
    
    return {
        'number': n,
        'factors': factors,
        'duration': duration,
        'coherence': coherence,
        'resonance': resonance
    }

def run_random_tests(random_adapter, output_dir):
    """
    Run random number generation tests.
    
    Args:
        random_adapter (PhiHarmonicRandomOrchestratorAdapter): Random adapter
        output_dir (str): Output directory
        
    Returns:
        dict: Test results
    """
    print("\n🎲 Random Number Generation Tests")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Test 1: Cryptographic Key Generation
    print("\n🔑 Test 1: Cryptographic Key Generation (256 bits)")
    key = random_adapter.generate_cryptographic_key(256)
    key_hex = key.hex()
    print(f"Quantum Key (hex): {key_hex}")
    
    # Calculate entropy
    entropy = 0
    for i in range(256):
        if i < len(key):
            byte_val = key[i]
            entropy += (byte_val / 255) * math.log2(byte_val + 1) if byte_val > 0 else 0
    entropy = 8 - (entropy / len(key))
    print(f"Key Entropy: {entropy:.6f} bits/byte")
    
    # Test 2: Monte Carlo Pi Estimation
    print("\n🔢 Test 2: Monte Carlo Pi Estimation (10,000 points)")
    pi_estimate = random_adapter.monte_carlo_pi(10000)
    error = abs(pi_estimate - math.pi) / math.pi * 100
    print(f"Pi estimate: {pi_estimate:.6f}")
    print(f"Actual Pi: {math.pi:.6f}")
    print(f"Error: {error:.6f}%")
    
    # Visualize Monte Carlo Pi Estimation
    points = 1000
    x = np.array([random_adapter.random() * 2 - 1 for _ in range(points)])
    y = np.array([random_adapter.random() * 2 - 1 for _ in range(points)])
    distances = np.sqrt(x**2 + y**2)
    inside = distances <= 1
    
    plt.figure(figsize=(8, 8))
    plt.scatter(x[inside], y[inside], c='blue', s=10, alpha=0.6, label='Inside')
    plt.scatter(x[~inside], y[~inside], c='red', s=10, alpha=0.6, label='Outside')
    circle = plt.Circle((0, 0), 1, fill=False, color='black', linewidth=2)
    plt.gca().add_patch(circle)
    plt.axis('equal')
    plt.title(f'Monte Carlo Pi Estimation: {pi_estimate:.6f} (Error: {error:.6f}%)')
    plt.legend()
    plt.grid(True)
    
    monte_carlo_file = os.path.join(output_dir, f'monte_carlo_pi_{time.strftime("%Y%m%d_%H%M%S")}.png')
    plt.savefig(monte_carlo_file)
    plt.close()
    
    # Test 3: Random Walk
    print("\n🚶 Test 3: Quantum Random Walk (1,000 steps)")
    path = random_adapter.random_walk(1000, 2)
    final_position = path[-1]
    distance = np.linalg.norm(final_position)
    expected_distance = math.sqrt(1000)
    ratio = distance / expected_distance
    print(f"Final position: ({final_position[0]:.2f}, {final_position[1]:.2f})")
    print(f"Distance from origin: {distance:.2f}")
    print(f"Expected distance (√n): {expected_distance:.2f}")
    print(f"Ratio (actual/expected): {ratio:.2f}")
    
    # Visualize Random Walk
    plt.figure(figsize=(10, 8))
    plt.plot(path[:, 0], path[:, 1], 'b-', alpha=0.6, linewidth=1)
    plt.plot(path[0, 0], path[0, 1], 'go', markersize=10, label='Start')
    plt.plot(path[-1, 0], path[-1, 1], 'ro', markersize=10, label='End')
    plt.axis('equal')
    plt.title(f'Quantum Random Walk (1,000 steps)\nDistance: {distance:.2f}, Expected: {expected_distance:.2f}, Ratio: {ratio:.2f}')
    plt.legend()
    plt.grid(True)
    
    random_walk_file = os.path.join(output_dir, f'random_walk_{time.strftime("%Y%m%d_%H%M%S")}.png')
    plt.savefig(random_walk_file)
    plt.close()
    
    # Test 4: Card Shuffling
    print("\n🃏 Test 4: Phi-Harmonic Card Shuffling (52 cards)")
    deck = list(range(1, 53))
    shuffled_deck = random_adapter.phi_harmonic_shuffle(deck)
    print(f"Original deck: {deck[:10]}... (first 10 shown)")
    print(f"Shuffled deck: {shuffled_deck[:10]}... (first 10 shown)")
    
    # Calculate inversions (measure of randomness)
    inversions = 0
    max_inversions = (52 * 51) // 2
    for i in range(52):
        for j in range(i + 1, 52):
            if shuffled_deck[i] > shuffled_deck[j]:
                inversions += 1
    
    inversion_percentage = (inversions / max_inversions) * 100
    print(f"Inversions: {inversions} out of {max_inversions} possible ({inversion_percentage:.2f}%)")
    
    # Calculate longest increasing subsequence (another measure of randomness)
    def longest_increasing_subsequence(arr):
        n = len(arr)
        lis = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        return max(lis)
    
    lis_length = longest_increasing_subsequence(shuffled_deck)
    lis_percentage = (lis_length / 52) * 100
    print(f"Longest increasing subsequence: {lis_length} ({lis_percentage:.2f}% of deck size)")
    
    # Calculate shuffle quality (based on inversions and LIS)
    shuffle_quality = 100 - abs(50 - inversion_percentage) - (lis_percentage - 10)
    print(f"Shuffle quality: {shuffle_quality:.2f}%")
    
    # Visualize Card Shuffling
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(range(1, 53), deck, color='blue')
    plt.title('Original Deck')
    plt.xlabel('Position')
    plt.ylabel('Card Value')
    
    plt.subplot(1, 2, 2)
    plt.bar(range(1, 53), shuffled_deck, color='red')
    plt.title(f'Shuffled Deck (Quality: {shuffle_quality:.2f}%)')
    plt.xlabel('Position')
    plt.ylabel('Card Value')
    
    plt.tight_layout()
    card_shuffle_file = os.path.join(output_dir, f'card_shuffle_{time.strftime("%Y%m%d_%H%M%S")}.png')
    plt.savefig(card_shuffle_file)
    plt.close()
    
    return {
        'cryptographic_key': {
            'key_hex': key_hex,
            'entropy': entropy
        },
        'monte_carlo_pi': {
            'pi_estimate': pi_estimate,
            'error': error,
            'visualization': monte_carlo_file
        },
        'random_walk': {
            'final_position': final_position.tolist(),
            'distance': float(distance),
            'expected_distance': expected_distance,
            'ratio': ratio,
            'visualization': random_walk_file
        },
        'card_shuffling': {
            'inversions': inversions,
            'max_inversions': max_inversions,
            'inversion_percentage': inversion_percentage,
            'lis_length': lis_length,
            'lis_percentage': lis_percentage,
            'shuffle_quality': shuffle_quality,
            'visualization': card_shuffle_file
        }
    }

def main():
    """Main function for running the integrated demo."""
    print("\n✨ Phi-Harmonic Integrated Demo")
    print("==============================")
    print("This demo shows the full capabilities of the orchestrated quantum system,")
    print("demonstrating how all components work together through the orchestration system.")
    
    # Get orchestrator
    orchestrator = get_orchestrator()
    print(f"\nOrchestrator initialized")
    print(f"Coherence: {orchestrator.coherence:.6f}")
    print(f"Resonance: {orchestrator.resonance:.6f}")
    print(f"Phi alignment: {orchestrator.phi_alignment:.6f}")
    
    # Create quantum bridge
    bridge = PhiHarmonicQuantumBridgeSimple()
    
    # Create random adapter
    random_adapter = PhiHarmonicRandomOrchestratorAdapter()
    
    # Create output directory
    output_dir = os.path.join(current_dir, 'phi_harmonic_integrated_demo')
    os.makedirs(output_dir, exist_ok=True)
    
    # Run RSA tests
    rsa_results = []
    test_numbers = [
        1537267,    # 7 digits
        15372673,   # 8 digits
        153726737   # 9 digits
    ]
    
    for n in test_numbers:
        result = run_rsa_test(n, bridge)
        rsa_results.append(result)
    
    # Run random tests
    random_results = run_random_tests(random_adapter, output_dir)
    
    # Save all results
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results = {
        'timestamp': timestamp,
        'orchestrator': {
            'coherence': float(orchestrator.coherence),
            'resonance': float(orchestrator.resonance),
            'phi_alignment': float(orchestrator.phi_alignment),
            'quantum_fingerprint': orchestrator.quantum_fingerprint
        },
        'bridge': {
            'coherence': float(bridge.coherence),
            'resonance': float(bridge.resonance),
            'phi_alignment': float(bridge.phi_alignment)
        },
        'rsa_results': rsa_results,
        'random_results': random_results
    }
    
    results_file = os.path.join(output_dir, f'integrated_results_{timestamp}.json')
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to {os.path.basename(results_file)}")
    
    # Print summary
    print("\n📊 Performance Summary")
    print("====================")
    
    print("\nRSA Factorization:")
    for result in rsa_results:
        print(f"  Number: {result['number']}")
        print(f"  Factors: {result['factors']}")
        print(f"  Duration: {result['duration']:.6f} seconds")
        print(f"  Coherence: {result['coherence']:.6f}")
        print(f"  Resonance: {result['resonance']:.6f}")
        print("")
    
    print("\nRandom Number Generation:")
    print(f"  Monte Carlo Pi Estimate: {random_results['monte_carlo_pi']['pi_estimate']:.6f} (Error: {random_results['monte_carlo_pi']['error']:.6f}%)")
    print(f"  Random Walk Distance: {random_results['random_walk']['distance']:.2f} (Expected: {random_results['random_walk']['expected_distance']:.2f})")
    print(f"  Card Shuffle Quality: {random_results['card_shuffling']['shuffle_quality']:.2f}%")
    
    print("\n✨ Integrated demo completed successfully")
    print("======================================")

if __name__ == "__main__":
    main()
