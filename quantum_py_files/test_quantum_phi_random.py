#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Random Number Generator Test
========================================================

This script demonstrates the capabilities of the Quantum Phi-Harmonic Random Number
Generator, showing its integration with the core system and its various distribution
types and operations.

It includes visualization of the distributions, statistical tests for randomness quality,
and comparisons with standard random number generators.
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Any, Tuple
import random
import statistics

# Import Quantum Phi-Harmonic components
from quantum_phi_core import QuantumPhiCore
from quantum_processor import QuantumProcessor
from quantum_phi_random import QuantumPhiRandom

def run_distribution_test(generator: QuantumPhiRandom, samples: int = 10000) -> Dict[str, List[float]]:
    """
    Generate samples from different distributions and return them for analysis.
    
    Args:
        generator: QuantumPhiRandom instance
        samples: Number of samples to generate
        
    Returns:
        Dictionary of distribution samples
    """
    results = {
        "uniform": [],
        "normal": [],
        "phi_harmonic": []
    }
    
    print(f"Generating {samples} samples from each distribution...")
    
    # Generate samples
    for _ in range(samples):
        results["uniform"].append(generator.random())
        results["normal"].append(generator.normal())
        results["phi_harmonic"].append(generator.phi_harmonic())
    
    return results

def visualize_distributions(samples: Dict[str, List[float]]) -> None:
    """
    Visualize the different distributions using histograms.
    
    Args:
        samples: Dictionary of distribution samples
    """
    # Create a figure with subplots
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    
    # Plot uniform distribution
    axs[0].hist(samples["uniform"], bins=50, alpha=0.7, color='blue')
    axs[0].set_title("Uniform Distribution")
    axs[0].set_xlabel("Value")
    axs[0].set_ylabel("Frequency")
    
    # Plot normal distribution
    axs[1].hist(samples["normal"], bins=50, alpha=0.7, color='green')
    axs[1].set_title("Normal Distribution")
    axs[1].set_xlabel("Value")
    
    # Plot phi-harmonic distribution
    axs[2].hist(samples["phi_harmonic"], bins=50, alpha=0.7, color='purple')
    axs[2].set_title("Phi-Harmonic Distribution")
    axs[2].set_xlabel("Value")
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the figure
    plt.savefig("quantum_phi_distributions.png")
    print("Distribution visualization saved to 'quantum_phi_distributions.png'")

def run_performance_test(generator: QuantumPhiRandom, std_generator: random.Random, samples: int = 100000) -> Dict[str, float]:
    """
    Compare performance between quantum phi random and standard random.
    
    Args:
        generator: QuantumPhiRandom instance
        std_generator: Standard random.Random instance
        samples: Number of samples to generate
        
    Returns:
        Dictionary of performance metrics
    """
    results = {}
    
    print(f"Running performance test with {samples} samples...")
    
    # Test quantum phi random
    start_time = time.time()
    phi_numbers = [generator.random() for _ in range(samples)]
    phi_time = time.time() - start_time
    
    # Test standard random
    start_time = time.time()
    std_numbers = [std_generator.random() for _ in range(samples)]
    std_time = time.time() - start_time
    
    # Calculate metrics
    results["phi_time"] = phi_time
    results["std_time"] = std_time
    results["time_ratio"] = phi_time / std_time
    
    # Calculate statistical properties
    results["phi_mean"] = statistics.mean(phi_numbers)
    results["std_mean"] = statistics.mean(std_numbers)
    results["phi_stdev"] = statistics.stdev(phi_numbers)
    results["std_stdev"] = statistics.stdev(std_numbers)
    
    return results

def run_randomness_tests(generator: QuantumPhiRandom, samples: int = 10000) -> Dict[str, float]:
    """
    Run basic statistical tests for randomness quality.
    
    Args:
        generator: QuantumPhiRandom instance
        samples: Number of samples to generate
        
    Returns:
        Dictionary of test results
    """
    results = {}
    
    print(f"Running randomness quality tests with {samples} samples...")
    
    # Generate samples
    numbers = [generator.random() for _ in range(samples)]
    
    # Test 1: Mean (should be close to 0.5 for uniform)
    results["mean"] = statistics.mean(numbers)
    results["mean_deviation"] = abs(results["mean"] - 0.5)
    
    # Test 2: Standard deviation (should be close to 1/sqrt(12) ≈ 0.2887 for uniform)
    results["stdev"] = statistics.stdev(numbers)
    results["stdev_deviation"] = abs(results["stdev"] - (1 / np.sqrt(12)))
    
    # Test 3: Min and max values
    results["min"] = min(numbers)
    results["max"] = max(numbers)
    results["range"] = results["max"] - results["min"]
    
    # Test 4: Quartiles
    sorted_numbers = sorted(numbers)
    results["q1"] = sorted_numbers[int(samples * 0.25)]
    results["q2"] = sorted_numbers[int(samples * 0.5)]  # median
    results["q3"] = sorted_numbers[int(samples * 0.75)]
    
    # Test 5: Runs test (simplified)
    runs = 1
    for i in range(1, samples):
        if (numbers[i] >= 0.5 and numbers[i-1] < 0.5) or (numbers[i] < 0.5 and numbers[i-1] >= 0.5):
            runs += 1
    results["runs"] = runs
    results["expected_runs"] = samples / 2
    results["runs_deviation"] = abs(runs - results["expected_runs"]) / results["expected_runs"]
    
    # Test 6: Serial correlation
    correlation = np.corrcoef(numbers[:-1], numbers[1:])[0, 1]
    results["serial_correlation"] = correlation
    
    return results

def test_phi_weighted_operations(generator: QuantumPhiRandom) -> None:
    """
    Test phi-weighted operations like shuffle and choice.
    
    Args:
        generator: QuantumPhiRandom instance
    """
    print("\nTesting phi-weighted operations:")
    
    # Test shuffle
    test_list = list(range(10))
    original = test_list.copy()
    
    print(f"Original list: {original}")
    
    generator.shuffle(test_list)
    print(f"After phi-harmonic shuffle: {test_list}")
    
    # Test phi-weighted choice
    items = ["A", "B", "C", "D", "E"]
    choices = {}
    
    # Make multiple choices and count frequencies
    for _ in range(1000):
        choice = generator.phi_weighted_choice(items)
        choices[choice] = choices.get(choice, 0) + 1
    
    print("\nPhi-weighted choice frequencies (1000 trials):")
    for item, count in sorted(choices.items()):
        print(f"  {item}: {count} ({count/10:.1f}%)")

def main() -> None:
    """Main test function."""
    print("=" * 70)
    print("Quantum Phi-Harmonic Random Number Generator Test")
    print("=" * 70)
    
    # Initialize components
    print("\nInitializing Quantum Phi-Harmonic components...")
    core = QuantumPhiCore()
    processor = QuantumProcessor(core)
    phi_random = QuantumPhiRandom(core)
    
    # Initialize standard random for comparison
    std_random = random.Random()
    
    print(f"Golden Ratio (φ): {float(core.PHI):.15f}")
    print(f"Phi Inverse (φ⁻¹): {float(core.PHI_INV):.15f}")
    
    # Generate basic random numbers
    print("\nGenerating basic random numbers:")
    print("  Uniform [0,1):", [round(phi_random.random(), 6) for _ in range(5)])
    print("  Integers [1,100]:", [phi_random.randint(1, 100) for _ in range(5)])
    print("  Normal (μ=0, σ=1):", [round(phi_random.normal(), 6) for _ in range(5)])
    print("  Phi-Harmonic:", [round(phi_random.phi_harmonic(), 6) for _ in range(5)])
    
    # Test phi-weighted operations
    test_phi_weighted_operations(phi_random)
    
    # Run distribution tests
    samples = run_distribution_test(phi_random, samples=10000)
    
    # Visualize distributions
    try:
        visualize_distributions(samples)
    except Exception as e:
        print(f"Error visualizing distributions: {e}")
    
    # Run performance test
    performance = run_performance_test(phi_random, std_random)
    
    print("\nPerformance comparison:")
    print(f"  Quantum Phi-Random time: {performance['phi_time']:.4f} seconds")
    print(f"  Standard Random time: {performance['std_time']:.4f} seconds")
    print(f"  Time ratio (Phi/Std): {performance['time_ratio']:.4f}x")
    print(f"  Phi-Random mean: {performance['phi_mean']:.6f}")
    print(f"  Standard mean: {performance['std_mean']:.6f}")
    print(f"  Phi-Random stdev: {performance['phi_stdev']:.6f}")
    print(f"  Standard stdev: {performance['std_stdev']:.6f}")
    
    # Run randomness tests
    randomness = run_randomness_tests(phi_random)
    
    print("\nRandomness quality tests:")
    print(f"  Mean: {randomness['mean']:.6f} (deviation: {randomness['mean_deviation']:.6f})")
    print(f"  Standard deviation: {randomness['stdev']:.6f} (deviation: {randomness['stdev_deviation']:.6f})")
    print(f"  Range: [{randomness['min']:.6f}, {randomness['max']:.6f}] (span: {randomness['range']:.6f})")
    print(f"  Quartiles: Q1={randomness['q1']:.6f}, Q2={randomness['q2']:.6f}, Q3={randomness['q3']:.6f}")
    print(f"  Runs test: {randomness['runs']} runs (expected: {randomness['expected_runs']:.1f}, deviation: {randomness['runs_deviation']:.6f})")
    print(f"  Serial correlation: {randomness['serial_correlation']:.6f}")
    
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
