"""
Test Brain Integration - Verify three-brain synchronization
"""

from brains.meta_processor import MetaProcessor
import numpy as np
import matplotlib.pyplot as plt

def test_integration():
    # Create processor
    processor = MetaProcessor()
    
    # Get base frequencies
    freqs = processor.get_frequencies()
    print("\nBase Frequencies:")
    for brain, freq in freqs.items():
        print(f"{brain}: {freq} Hz")
    
    # Test impact range
    forces = np.linspace(0, 5, 10)
    coherence = []
    learning = []
    retention = []
    
    print("\nTesting Impact Forces:")
    for force in forces:
        results = processor.process_impact(force)
        coherence.append(results['coherence'])
        learning.append(results['learning'])
        retention.append(results['retention'])
        print(f"\nForce: {force:.3f}")
        print(f"Coherence: {results['coherence']:.3f}")
        print(f"Learning: {results['learning']:.3f}")
        print(f"Retention: {results['retention']:.3f}")
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(forces, coherence, label='Coherence')
    plt.plot(forces, learning, label='Learning')
    plt.plot(forces, retention, label='Retention')
    plt.axvline(x=1.618, color='r', linestyle='--', label='φ Force')
    plt.xlabel('Impact Force')
    plt.ylabel('Score')
    plt.title('Brain Integration Results')
    plt.legend()
    plt.grid(True)
    plt.savefig('integration_results.png')
    plt.close()

if __name__ == "__main__":
    test_integration()
