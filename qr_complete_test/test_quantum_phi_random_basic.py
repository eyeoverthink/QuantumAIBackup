#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Basic Random Number Generator Test
==============================================================

This script demonstrates the core capabilities of the Quantum Phi-Harmonic Random 
Number Generator with minimal dependencies, focusing on the essential functionality
without requiring visualization libraries.
"""

import time
import statistics
from typing import List, Dict, Any, Tuple

# Import Quantum Phi-Harmonic components
from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom

def test_basic_generation(generator: QuantumPhiRandom) -> None:
    """
    Test basic random number generation.
    
    Args:
        generator: QuantumPhiRandom instance
    """
    print("\nBasic Random Number Generation:")
    
    # Uniform random
    print("  Uniform [0,1):")
    for _ in range(5):
        print(f"    {generator.random():.6f}")
    
    # Integer random
    print("\n  Integers [1,100]:")
    for _ in range(5):
        print(f"    {generator.randint(1, 100)}")
    
    # Normal distribution
    print("\n  Normal (μ=0, σ=1):")
    for _ in range(5):
        print(f"    {generator.normal():.6f}")
    
    # Phi-harmonic distribution
    print("\n  Phi-Harmonic:")
    for _ in range(5):
        print(f"    {generator.phi_harmonic():.6f}")

def test_phi_weighted_operations(generator: QuantumPhiRandom) -> None:
    """
    Test phi-weighted operations like shuffle and choice.
    
    Args:
        generator: QuantumPhiRandom instance
    """
    print("\nPhi-Weighted Operations:")
    
    # Test shuffle
    test_list = list(range(10))
    original = test_list.copy()
    
    print(f"  Original list: {original}")
    
    generator.shuffle(test_list)
    print(f"  After phi-harmonic shuffle: {test_list}")
    
    # Test phi-weighted choice
    items = ["A", "B", "C", "D", "E"]
    choices = {}
    
    # Make multiple choices and count frequencies
    for _ in range(100):
        choice = generator.phi_weighted_choice(items)
        choices[choice] = choices.get(choice, 0) + 1
    
    print("\n  Phi-weighted choice frequencies (100 trials):")
    for item, count in sorted(choices.items()):
        print(f"    {item}: {count}")

def test_randomness_quality(generator: QuantumPhiRandom, samples: int = 1000) -> None:
    """
    Run basic statistical tests for randomness quality.
    
    Args:
        generator: QuantumPhiRandom instance
        samples: Number of samples to generate
    """
    print(f"\nRandomness Quality Tests ({samples} samples):")
    
    # Generate samples
    numbers = [generator.random() for _ in range(samples)]
    
    # Calculate statistics
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = variance ** 0.5
    
    # Calculate quartiles
    sorted_numbers = sorted(numbers)
    q1 = sorted_numbers[int(samples * 0.25)]
    q2 = sorted_numbers[int(samples * 0.5)]  # median
    q3 = sorted_numbers[int(samples * 0.75)]
    
    # Print results
    print(f"  Mean: {mean:.6f} (ideal: 0.5)")
    print(f"  Standard Deviation: {std_dev:.6f} (ideal: {(1/12)**0.5:.6f})")
    print(f"  Range: [{min(numbers):.6f}, {max(numbers):.6f}]")
    print(f"  Quartiles: Q1={q1:.6f}, Q2={q2:.6f}, Q3={q3:.6f}")
    
    # Test for serial correlation (basic)
    pairs = list(zip(numbers[:-1], numbers[1:]))
    correlation = sum((x - mean) * (y - mean) for x, y in pairs) / (len(pairs) * variance)
    print(f"  Serial Correlation: {correlation:.6f} (ideal: 0)")

def test_bytes_generation(generator: QuantumPhiRandom) -> None:
    """
    Test random bytes generation.
    
    Args:
        generator: QuantumPhiRandom instance
    """
    print("\nRandom Bytes Generation:")
    
    # Generate 16 random bytes
    random_bytes = generator.bytes(16)
    
    # Display as hex
    hex_bytes = ' '.join(f'{b:02x}' for b in random_bytes)
    print(f"  16 random bytes (hex): {hex_bytes}")
    
    # Calculate byte distribution
    byte_counts = {}
    for byte in random_bytes:
        byte_counts[byte] = byte_counts.get(byte, 0) + 1
    
    print(f"  Unique byte values: {len(byte_counts)} out of {len(random_bytes)}")

def main() -> None:
    """Main test function."""
    print("=" * 70)
    print("Quantum Phi-Harmonic Random Number Generator Basic Test")
    print("=" * 70)
    
    # Initialize components
    print("\nInitializing Quantum Phi-Harmonic components...")
    core = QuantumPhiCore()
    phi_random = QuantumPhiRandom(core)
    
    print(f"Golden Ratio (φ): {float(core.PHI):.15f}")
    print(f"Phi Inverse (φ⁻¹): {float(core.PHI_INV):.15f}")
    
    # Run tests
    test_basic_generation(phi_random)
    test_phi_weighted_operations(phi_random)
    test_randomness_quality(phi_random)
    test_bytes_generation(phi_random)
    
    # Get and display metrics
    metrics = phi_random.get_metrics()
    
    print("\nQuantum Phi-Random metrics:")
    print(f"  Entropy: {metrics['entropy']:.6f}")
    print(f"  Phi resonance: {metrics['phi_resonance']:.6f}")
    print(f"  Sequence coherence: {metrics['sequence_coherence']:.6f}")
    print(f"  Numbers generated: {metrics['numbers_generated']}")
    
    print("\nTest completed successfully!")

if __name__ == "__main__":
    main()
