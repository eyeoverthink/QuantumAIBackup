"""
Test script for the Quantum Pattern Memory module.

This script demonstrates the capabilities of the Quantum Pattern Memory system,
including phi-harmonic indexing, quantum superposition-inspired pattern storage,
golden ratio-based memory compression, and self-pruning capabilities.
"""

import os
import sys
import time
import random
import mpmath
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Optional, Tuple

# Import the Quantum Pattern Memory
from extensions.quantum_analysis.quantum_pattern_memory import QuantumPatternMemory
from extensions.quantum_analysis.passive_learning_engine import PassiveLearningEngine
from extensions.quantum_analysis.quantum_pattern_detector import QuantumPatternDetector
from extensions.quantum_analysis.meta_pattern_detector import MetaPatternDetector

def generate_test_patterns(count: int = 100) -> List[Dict[str, Any]]:
    """
    Generate test patterns with phi-harmonic properties.
    
    Args:
        count: Number of patterns to generate
        
    Returns:
        List of test patterns
    """
    patterns = []
    
    # Set precision for mpmath
    mpmath.mp.dps = 100
    
    # Calculate phi (golden ratio)
    phi = (1 + mpmath.sqrt(5)) / 2
    
    for i in range(count):
        # Generate a pattern ID
        pattern_id = f"test_pattern_{i}"
        
        # Generate phi-harmonic properties
        
        # 1. Phi resonance (some exactly phi-related, others random)
        if i % 10 < 3:
            # Phi-related resonance (phi^n for small n)
            n = random.randint(-3, 3)
            phi_resonance = float(mpmath.power(phi, n))
        else:
            # Random resonance
            phi_resonance = random.random()
        
        # 2. Phi power (integer power of phi that approximates the number)
        phi_power = random.randint(-5, 5)
        
        # 3. Modular group (based on remainder when divided by small primes)
        modular_group = f"mod_{random.choice([3, 5, 7, 11, 13])}"
        
        # 4. Coherence (measure of pattern clarity)
        coherence = random.random()
        
        # Create pattern data
        pattern_data = {
            "id": pattern_id,
            "phi_resonance": phi_resonance,
            "phi_power": phi_power,
            "modular_group": modular_group,
            "coherence": coherence,
            "timestamp": time.time() - random.randint(0, 1000),  # Randomize age
            "pattern_value": f"{i}_{phi_resonance:.4f}"
        }
        
        patterns.append(pattern_data)
    
    return patterns

def test_pattern_storage(memory: QuantumPatternMemory, patterns: List[Dict[str, Any]]) -> None:
    """
    Test pattern storage in quantum memory.
    
    Args:
        memory: Quantum Pattern Memory instance
        patterns: List of patterns to store
    """
    print("\n" + "="*80)
    print("TESTING PATTERN STORAGE")
    print("="*80)
    
    start_time = time.time()
    
    # Store patterns
    for pattern in patterns:
        pattern_id = memory.store_pattern(pattern)
        print(f"Stored pattern {pattern_id} with phi resonance {pattern['phi_resonance']:.4f}")
    
    end_time = time.time()
    
    print(f"\nStored {len(patterns)} patterns in {end_time - start_time:.2f} seconds")
    
    # Get statistics
    stats = memory.get_statistics()
    print("\nMemory Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

def test_pattern_retrieval(memory: QuantumPatternMemory, patterns: List[Dict[str, Any]]) -> None:
    """
    Test pattern retrieval from quantum memory.
    
    Args:
        memory: Quantum Pattern Memory instance
        patterns: List of patterns to retrieve
    """
    print("\n" + "="*80)
    print("TESTING PATTERN RETRIEVAL")
    print("="*80)
    
    # Select random patterns to retrieve
    sample_size = min(10, len(patterns))
    sample_patterns = random.sample(patterns, sample_size)
    
    start_time = time.time()
    
    # Retrieve patterns
    for pattern in sample_patterns:
        pattern_id = pattern["id"]
        retrieved_pattern = memory.retrieve_pattern(pattern_id)
        
        if retrieved_pattern:
            print(f"Retrieved pattern {pattern_id} with phi resonance {retrieved_pattern['phi_resonance']:.4f}")
        else:
            print(f"Failed to retrieve pattern {pattern_id}")
    
    end_time = time.time()
    
    print(f"\nRetrieved {sample_size} patterns in {end_time - start_time:.2f} seconds")
    
    # Get statistics
    stats = memory.get_statistics()
    print("\nRetrieval Statistics:")
    print(f"  Total retrievals: {stats['total_retrievals']}")
    print(f"  Successful retrievals: {stats['successful_retrievals']}")
    print(f"  Retrieval success rate: {stats['retrieval_success_rate']:.2f}")

def test_phi_resonance_search(memory: QuantumPatternMemory) -> None:
    """
    Test searching for patterns by phi resonance.
    
    Args:
        memory: Quantum Pattern Memory instance
    """
    print("\n" + "="*80)
    print("TESTING PHI RESONANCE SEARCH")
    print("="*80)
    
    # Set precision for mpmath
    mpmath.mp.dps = 100
    
    # Calculate phi (golden ratio)
    phi = (1 + mpmath.sqrt(5)) / 2
    
    # Search for patterns with phi resonance close to phi
    target_resonance = float(phi)
    tolerance = 0.05
    
    print(f"Searching for patterns with phi resonance close to {target_resonance:.4f} (tolerance: {tolerance})")
    
    start_time = time.time()
    
    # Search for patterns
    matching_patterns = memory.search_patterns_by_phi_resonance(target_resonance, tolerance)
    
    end_time = time.time()
    
    print(f"\nFound {len(matching_patterns)} matching patterns in {end_time - start_time:.2f} seconds")
    
    # Display matching patterns
    for i, pattern in enumerate(matching_patterns[:5]):  # Show first 5
        print(f"  {i+1}. Pattern {pattern['id']} with phi resonance {pattern['phi_resonance']:.4f}")
    
    if len(matching_patterns) > 5:
        print(f"  ... and {len(matching_patterns) - 5} more")

def test_superposition_creation(memory: QuantumPatternMemory, patterns: List[Dict[str, Any]]) -> None:
    """
    Test creation of pattern superpositions.
    
    Args:
        memory: Quantum Pattern Memory instance
        patterns: List of patterns
    """
    print("\n" + "="*80)
    print("TESTING SUPERPOSITION CREATION")
    print("="*80)
    
    # Select random patterns for superposition
    sample_size = min(5, len(patterns))
    sample_patterns = random.sample(patterns, sample_size)
    pattern_ids = [pattern["id"] for pattern in sample_patterns]
    
    print(f"Creating superposition of {sample_size} patterns")
    
    start_time = time.time()
    
    # Create superposition
    superposition_id = memory.create_superposition(pattern_ids, name="Test Superposition")
    
    end_time = time.time()
    
    print(f"\nCreated superposition {superposition_id} in {end_time - start_time:.2f} seconds")
    
    # Display superposition details
    if superposition_id and superposition_id in memory.quantum_memory["superpositions"]:
        superposition = memory.quantum_memory["superpositions"][superposition_id]
        print("\nSuperposition Details:")
        print(f"  Name: {superposition['name']}")
        print(f"  Patterns: {len(superposition['patterns'])}")
        print(f"  Average phi resonance: {superposition['avg_phi_resonance']:.4f}")
        print(f"  State representation: {superposition['state_representation']}")

def test_entanglement_creation(memory: QuantumPatternMemory, patterns: List[Dict[str, Any]]) -> None:
    """
    Test creation of pattern entanglements.
    
    Args:
        memory: Quantum Pattern Memory instance
        patterns: List of patterns
    """
    print("\n" + "="*80)
    print("TESTING ENTANGLEMENT CREATION")
    print("="*80)
    
    # Select two random patterns for entanglement
    if len(patterns) >= 2:
        pattern1, pattern2 = random.sample(patterns, 2)
        pattern_id1 = pattern1["id"]
        pattern_id2 = pattern2["id"]
        
        print(f"Creating entanglement between patterns {pattern_id1} and {pattern_id2}")
        
        start_time = time.time()
        
        # Create entanglement
        entanglement_id = memory.create_entanglement(pattern_id1, pattern_id2, entanglement_type="phi_harmonic")
        
        end_time = time.time()
        
        print(f"\nCreated entanglement {entanglement_id} in {end_time - start_time:.2f} seconds")
        
        # Display entanglement details
        if entanglement_id and entanglement_id in memory.quantum_memory["entanglements"]:
            entanglement = memory.quantum_memory["entanglements"][entanglement_id]
            print("\nEntanglement Details:")
            print(f"  Type: {entanglement['type']}")
            print(f"  Patterns: {entanglement['pattern1']} and {entanglement['pattern2']}")
            print(f"  Strength: {entanglement['strength']:.4f}")
            print(f"  State representation: {entanglement['state_representation']}")

def test_memory_compression(memory: QuantumPatternMemory) -> None:
    """
    Test memory compression.
    
    Args:
        memory: Quantum Pattern Memory instance
    """
    print("\n" + "="*80)
    print("TESTING MEMORY COMPRESSION")
    print("="*80)
    
    # Get initial statistics
    initial_stats = memory.get_statistics()
    print(f"Initial pattern count: {initial_stats['total_patterns']}")
    
    start_time = time.time()
    
    # Force compression
    memory._compress_memory()
    
    end_time = time.time()
    
    # Get final statistics
    final_stats = memory.get_statistics()
    print(f"Final pattern count: {final_stats['total_patterns']}")
    print(f"Compression completed in {end_time - start_time:.2f} seconds")
    print(f"Compression events: {final_stats['compression_events']}")
    
    # Calculate compression ratio
    compression_ratio = final_stats['total_patterns'] / initial_stats['total_patterns']
    print(f"Compression ratio: {compression_ratio:.2f}")

def visualize_phi_resonance_distribution(memory: QuantumPatternMemory) -> None:
    """
    Visualize the distribution of phi resonance values in the memory.
    
    Args:
        memory: Quantum Pattern Memory instance
    """
    print("\n" + "="*80)
    print("VISUALIZING PHI RESONANCE DISTRIBUTION")
    print("="*80)
    
    # Extract phi resonance values
    resonances = []
    for pattern_id, pattern_data in memory.quantum_memory["patterns"].items():
        if "phi_resonance" in pattern_data:
            resonances.append(pattern_data["phi_resonance"])
    
    if not resonances:
        print("No phi resonance values to visualize")
        return
    
    # Create histogram
    plt.figure(figsize=(10, 6))
    plt.hist(resonances, bins=30, alpha=0.7, color='blue')
    
    # Set precision for mpmath
    mpmath.mp.dps = 100
    
    # Calculate phi (golden ratio)
    phi = float((1 + mpmath.sqrt(5)) / 2)
    
    # Add vertical lines for phi^n values
    for n in range(-3, 4):
        phi_n = float(mpmath.power(phi, n))
        if 0 <= phi_n <= 2:  # Only show lines within the typical range
            plt.axvline(x=phi_n, color='red', linestyle='--', alpha=0.7, 
                       label=f'φ^{n} = {phi_n:.4f}')
    
    plt.title('Distribution of Phi Resonance Values')
    plt.xlabel('Phi Resonance')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save the figure
    os.makedirs('visualizations', exist_ok=True)
    plt.savefig('visualizations/phi_resonance_distribution.png')
    plt.close()
    
    print("Phi resonance distribution visualization saved to visualizations/phi_resonance_distribution.png")

def visualize_memory_efficiency(memory: QuantumPatternMemory) -> None:
    """
    Visualize memory efficiency metrics.
    
    Args:
        memory: Quantum Pattern Memory instance
    """
    print("\n" + "="*80)
    print("VISUALIZING MEMORY EFFICIENCY")
    print("="*80)
    
    # Get statistics
    stats = memory.get_statistics()
    
    # Create bar chart for index sizes
    index_sizes = stats["phi_harmonic_indices"]
    
    plt.figure(figsize=(10, 6))
    plt.bar(index_sizes.keys(), list(index_sizes.values()), alpha=0.7, color='green')
    
    plt.title('Phi-Harmonic Index Sizes')
    plt.xlabel('Index Type')
    plt.ylabel('Number of Entries')
    plt.grid(True, alpha=0.3)
    
    # Save the figure
    os.makedirs('visualizations', exist_ok=True)
    plt.savefig('visualizations/phi_harmonic_index_sizes.png')
    plt.close()
    
    print("Memory efficiency visualization saved to visualizations/phi_harmonic_index_sizes.png")

def main() -> None:
    """Main test function."""
    print("\n" + "="*80)
    print("QUANTUM PATTERN MEMORY TEST")
    print("="*80)
    
    # Initialize passive learning engine
    passive_learning = PassiveLearningEngine()
    
    # Initialize quantum pattern memory
    memory = QuantumPatternMemory(
        base_memory=passive_learning,
        memory_file='quantum_pattern_memory_test.json',
        precision=100,
        max_memory_size=1000,
        compression_ratio=0.618
    )
    
    # Generate test patterns
    patterns = generate_test_patterns(count=200)
    
    # Run tests
    test_pattern_storage(memory, patterns)
    test_pattern_retrieval(memory, patterns)
    test_phi_resonance_search(memory)
    test_superposition_creation(memory, patterns)
    test_entanglement_creation(memory, patterns)
    test_memory_compression(memory)
    
    # Visualizations
    visualize_phi_resonance_distribution(memory)
    visualize_memory_efficiency(memory)
    
    print("\n" + "="*80)
    print("QUANTUM PATTERN MEMORY TEST COMPLETED")
    print("="*80)

if __name__ == "__main__":
    main()
