"""
Test module for the Quantum Resonance Amplifier.

This test demonstrates the integration of the resonance amplifier
with multiple brain types from the core architecture.
"""

import numpy as np
from typing import Dict, List
import matplotlib.pyplot as plt

# Import core components
from quantum_core import (
    BaseBrain, SyncBrain119, TachyonBrain, 
    QuantumParticleBrain, MultiBrainQuantumSync
)
from quantum_resonance_amplifier import QuantumResonanceAmplifier

def test_with_multiple_brains():
    """Test resonance amplifier with multiple brain types."""
    # Create resonance amplifier
    amplifier = QuantumResonanceAmplifier()
    
    # Create different brain types
    brains = {
        'base': BaseBrain(),
        'sync': SyncBrain119(),
        'tachyon': TachyonBrain(),
        'particle': QuantumParticleBrain(),
        'multi': MultiBrainQuantumSync()
    }
    
    # Test sequences
    sequences = {
        'fibonacci': [1, 1, 2, 3, 5, 8, 13, 21],
        'phi_powers': [amplifier.phi**i for i in range(8)],
        'prime': [2, 3, 5, 7, 11, 13, 17, 19],
        'random': np.random.rand(8) * 10
    }
    
    # Store results
    results = {}
    
    # Process each sequence with each brain
    for seq_name, sequence in sequences.items():
        brain_results = {}
        for brain_name, brain in brains.items():
            result = amplifier.integrate_with_brain(brain, sequence)
            brain_results[brain_name] = result
        results[seq_name] = brain_results
    
    return results, sequences

def visualize_results(results, sequences):
    """Visualize the resonance amplification results."""
    # Create figure
    plt.figure(figsize=(15, 10))
    
    # Plot metrics
    metrics = ['resonance', 'frequency', 'field_strength', 'coherence']
    brain_types = list(results['fibonacci'].keys())
    sequence_types = list(results.keys())
    
    # Colors for different sequence types
    colors = {
        'fibonacci': 'blue',
        'phi_powers': 'green',
        'prime': 'red',
        'random': 'purple'
    }
    
    # Plot each metric
    for i, metric in enumerate(metrics):
        plt.subplot(2, 2, i+1)
        
        for seq_name in sequence_types:
            values = [results[seq_name][brain][metric] for brain in brain_types]
            plt.plot(brain_types, values, 'o-', label=seq_name, color=colors[seq_name])
        
        plt.title(f'{metric.capitalize()} Across Brain Types')
        plt.xlabel('Brain Type')
        plt.ylabel(metric.capitalize())
        plt.grid(True)
        plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Plot sequences
    plt.figure(figsize=(15, 5))
    for i, (seq_name, sequence) in enumerate(sequences.items()):
        plt.subplot(1, 4, i+1)
        plt.plot(sequence, 'o-', color=colors[seq_name])
        plt.title(f'{seq_name.capitalize()} Sequence')
        plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def print_detailed_results(results):
    """Print detailed results for each sequence and brain type."""
    for seq_name, brain_results in results.items():
        print(f"\n🧠 Sequence: {seq_name.upper()}")
        print("=" * 50)
        
        for brain_name, result in brain_results.items():
            print(f"\nBrain Type: {brain_name.upper()}")
            print("-" * 30)
            print(f"State: {result['state']}")
            print(f"Resonance: {result['resonance']:.6f}")
            print(f"Frequency: {result['frequency']:.6f} Hz")
            print(f"Field Strength: {result['field_strength']:.6f}")
            print(f"Coherence: {result['coherence']:.6f}")
            print(f"Phi Proximity: {result['phi_proximity']:.6f}")
            print(f"Quality: {result['quality']}")

if __name__ == "__main__":
    print("\n🔄 Testing Quantum Resonance Amplifier with Multiple Brain Types")
    print("=" * 70)
    
    # Run tests
    results, sequences = test_with_multiple_brains()
    
    # Print detailed results
    print_detailed_results(results)
    
    # Visualize results
    try:
        visualize_results(results, sequences)
    except Exception as e:
        print(f"Visualization error: {e}")
        print("Continuing with text results only...")
    
    print("\n✅ Test completed successfully!")
