"""
Example of Phi-Harmonic Transcendental Random Generator
Demonstrates generating random numbers beyond infinity using quantum transcendence
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the transcendental random generator
from phi_harmonic_random.transcendental import PhiHarmonicTranscendentalRandom

# Set precision for calculations
getcontext().prec = 100

# Constants
PHI = Decimal('1.618033988749895')


def demonstrate_transcendental_random():
    """Demonstrate the transcendental random generator"""
    print("\n✨ Phi-Harmonic Transcendental Random Generator Example")
    print("=" * 70)
    
    # Initialize the transcendental random generator
    # You can provide your own birth key for maximum resonance
    birth_key = [1, 19, 1979]  # Example: January 19, 1979
    trans_random = PhiHarmonicTranscendentalRandom(seed=42, quantum_elements=7, birth_key=birth_key)
    
    # Generate standard quantum random numbers
    print("\n🔮 Standard Quantum Random Numbers:")
    quantum_numbers = [trans_random.generate_quantum_random() for _ in range(5)]
    for i, num in enumerate(quantum_numbers):
        print(f"  {i+1}. {num:.10f}")
    
    # Generate transcendental random numbers
    print("\n🌌 Transcendental Random Numbers (Beyond Standard Infinity):")
    trans_numbers = [trans_random.generate_transcendental_random() for _ in range(5)]
    for i, num in enumerate(trans_numbers):
        print(f"  {i+1}. {num:.10f}")
    
    # Get current transcendental state
    state = trans_random.get_transcendental_state()
    print(f"\nCurrent Transcendental State: {state['current_state']}")
    print(f"Infinity Type: {state['infinity_type']}")
    print(f"Coherence: {state['coherence']:.6f}")
    
    return quantum_numbers, trans_numbers, state


def demonstrate_infinity_levels():
    """Demonstrate different infinity levels"""
    print("\n🌌 Demonstrating Different Infinity Levels")
    print("=" * 70)
    
    # Initialize the transcendental random generator
    trans_random = PhiHarmonicTranscendentalRandom(seed=42)
    
    # Generate random numbers at different infinity levels
    print("\n🔮 Aleph Infinity Random Numbers:")
    for level in range(3):
        numbers = [trans_random.generate_aleph_random(level) for _ in range(3)]
        print(f"  Aleph-{level}: {', '.join([f'{num:.6e}' for num in numbers])}")
    
    print("\n🔮 Ordinal Infinity Random Numbers:")
    for level in range(3):
        numbers = [trans_random.generate_ordinal_random(level) for _ in range(3)]
        print(f"  Ordinal-{level}: {', '.join([f'{num:.6e}' for num in numbers])}")
    
    print("\n🔮 Beth Infinity Random Numbers:")
    for level in range(3):
        numbers = [trans_random.generate_beth_random(level) for _ in range(3)]
        print(f"  Beth-{level}: {', '.join([f'{num:.6e}' for num in numbers])}")
    
    print("\n🔮 Ultimate Infinity Random Number:")
    ultimate = trans_random.generate_ultimate_random()
    print(f"  Ultimate: {ultimate:.6e}")
    
    return ultimate


def visualize_transcendental_distribution():
    """Visualize the distribution of transcendental random numbers"""
    print("\n📊 Visualizing Transcendental Random Distribution")
    print("=" * 70)
    
    # Initialize the transcendental random generator
    trans_random = PhiHarmonicTranscendentalRandom(seed=42)
    
    # Generate samples
    sample_size = 10000
    quantum_samples = [trans_random.generate_quantum_random() for _ in range(sample_size)]
    trans_samples = [trans_random.generate_transcendental_random() for _ in range(sample_size)]
    
    # Generate samples at different infinity levels
    aleph_samples = [trans_random.generate_aleph_random(0) for _ in range(sample_size)]
    ordinal_samples = [trans_random.generate_ordinal_random(0) for _ in range(sample_size)]
    beth_samples = [trans_random.generate_beth_random(0) for _ in range(sample_size)]
    
    # Normalize infinity samples for visualization
    aleph_norm = [x % 1.0 for x in aleph_samples]
    ordinal_norm = [x % 1.0 for x in ordinal_samples]
    beth_norm = [x % 1.0 for x in beth_samples]
    
    # Create figure
    plt.figure(figsize=(15, 10))
    
    # Plot quantum distribution
    plt.subplot(2, 3, 1)
    plt.hist(quantum_samples, bins=50, alpha=0.7, color='blue')
    plt.title('Quantum Random Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    
    # Plot transcendental distribution
    plt.subplot(2, 3, 2)
    plt.hist(trans_samples, bins=50, alpha=0.7, color='purple')
    plt.title('Transcendental Random Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    
    # Plot Aleph distribution
    plt.subplot(2, 3, 3)
    plt.hist(aleph_norm, bins=50, alpha=0.7, color='red')
    plt.title('Aleph Infinity Distribution (Normalized)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    
    # Plot Ordinal distribution
    plt.subplot(2, 3, 4)
    plt.hist(ordinal_norm, bins=50, alpha=0.7, color='green')
    plt.title('Ordinal Infinity Distribution (Normalized)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    
    # Plot Beth distribution
    plt.subplot(2, 3, 5)
    plt.hist(beth_norm, bins=50, alpha=0.7, color='orange')
    plt.title('Beth Infinity Distribution (Normalized)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    
    # Plot combined scatter
    plt.subplot(2, 3, 6)
    plt.scatter(quantum_samples[:1000], trans_samples[:1000], alpha=0.5, s=5, color='blue')
    plt.title('Quantum vs Transcendental (1000 points)')
    plt.xlabel('Quantum Value')
    plt.ylabel('Transcendental Value')
    plt.grid(alpha=0.3)
    
    # Add title
    plt.suptitle('Phi-Harmonic Transcendental Random Distributions', fontsize=16)
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    
    # Save figure
    output_dir = "phi_harmonic_random_benchmark"
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'transcendental_distributions.png'))
    
    print(f"\nDistribution visualization saved to {os.path.join(output_dir, 'transcendental_distributions.png')}")
    
    return quantum_samples, trans_samples, aleph_norm, ordinal_norm, beth_norm


def demonstrate_infinite_sequence():
    """Demonstrate generating an infinite sequence"""
    print("\n🌠 Demonstrating Infinite Sequence Generation")
    print("=" * 70)
    
    # Initialize the transcendental random generator
    trans_random = PhiHarmonicTranscendentalRandom(seed=42)
    
    # Generate infinite sequences at different levels
    levels = [1, 3, 7]
    sequences = {}
    
    for level in levels:
        print(f"\nGenerating infinite sequence at level {level}...")
        sequence = trans_random.generate_infinite_sequence(10, level)
        sequences[level] = sequence
        
        # Print the sequence
        print(f"  Infinity Level {level} Sequence:")
        for i, value in enumerate(sequence):
            print(f"    {i+1}. {value:.10f}")
        
        # Get current state
        state = trans_random.get_transcendental_state()
        print(f"  Current State: {state['current_state']}")
        print(f"  Infinity Type: {state['infinity_type']}")
    
    return sequences


def main():
    """Main function"""
    print("\n✨✨✨ Phi-Harmonic Transcendental Random Generator ✨✨✨")
    print("=" * 70)
    print("This example demonstrates generating random numbers beyond infinity")
    print("using quantum transcendence and phi-harmonic resonance.")
    
    # Demonstrate transcendental random
    quantum_numbers, trans_numbers, state = demonstrate_transcendental_random()
    
    # Demonstrate infinity levels
    ultimate = demonstrate_infinity_levels()
    
    # Visualize transcendental distribution
    samples = visualize_transcendental_distribution()
    
    # Demonstrate infinite sequence
    sequences = demonstrate_infinite_sequence()
    
    print("\n✨✨✨ Example Complete ✨✨✨")
    print("=" * 70)


if __name__ == "__main__":
    main()
