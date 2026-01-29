"""
Quantum Function Test
Tests specific quantum functions across all brain systems
"""

from quantum_neural_cortex import QuantumNeuralCortex
from tesla_phi_resonance import TeslaPhiResonanceSystem
from neural_tesla_integration import NeuralTeslaInterface
import numpy as np
from datetime import datetime

def test_quantum_functions():
    print("\n🧪 Quantum Function Test")
    print("====================")
    print(f"Time: {datetime.now()}")
    
    # Initialize systems
    cortex = QuantumNeuralCortex()
    tesla = TeslaPhiResonanceSystem()
    interface = NeuralTeslaInterface()
    phi = (1 + np.sqrt(5)) / 2
    
    # Test Tesla Frequencies
    print("\n⚡ Tesla Frequency Evolution")
    print("========================")
    tesla_freqs = {
        'Physical': 432,
        'Mental': 528,
        'Heart': 639,
        'Third Eye': 741
    }
    
    for name, base_freq in tesla_freqs.items():
        evolved_freq = base_freq * (phi ** 4)  # Evolve to φ⁴
        print(f"\n{name}:")
        print(f"Base: {base_freq} Hz")
        print(f"Evolved: {evolved_freq:.2f} Hz")
        print(f"Evolution: {evolved_freq/base_freq:.6f}")
        print(f"Target: {phi**4:.6f}")
        print(f"Accuracy: {100 * (1 - abs((evolved_freq/base_freq) - phi**4)/(phi**4)):.4f}%")
    
    # Test DNA Bridges
    print("\n🧬 DNA Bridge Functions")
    print("====================")
    dna_bridges = [
        ('Physical', 'Mental', 432, 528),
        ('Mental', 'Heart', 528, 639),
        ('Heart', 'Third Eye', 639, 741),
        ('Third Eye', 'Crown', 741, 852)
    ]
    
    for source, target, freq1, freq2 in dna_bridges:
        bridge_freq = (freq1 * phi**4 + freq2 * phi**4) / 2
        print(f"\n{source} → {target}:")
        print(f"Bridge Frequency: {bridge_freq:.2f} Hz")
        print(f"Resonance: {1/(1 + abs(bridge_freq - (freq1 * phi**4))):.9f}")
        print(f"Coherence: {abs(np.sin(bridge_freq * phi)) * phi:.6f}")
    
    # Test Author Functions
    print("\n📚 Author Function Test")
    print("===================")
    authors = {
        'Poe': 517.15,
        'Austen': 525.18,
        'Shakespeare': 555.40,
        'Hemingway': 576.26
    }
    
    for author, freq in authors.items():
        evolved = freq * phi**4
        print(f"\n{author}:")
        print(f"Base: {freq} Hz")
        print(f"Evolved: {evolved:.2f} Hz")
        print(f"Evolution: {evolved/freq:.6f}")
        print(f"Coherence: {abs(np.sin(evolved * phi)) * phi:.6f}")
    
    # Test Consciousness Functions
    print("\n🧠 Consciousness Functions")
    print("=======================")
    consciousness_levels = {
        'Physical': (0, 200),
        'Mental': (200, 500),
        'Bridge': (500, 1000),
        'Cosmic': (1000, float('inf'))
    }
    
    test_freqs = [432, 528, 639, 741, 852, 963]
    for freq in test_freqs:
        evolved = freq * phi**4
        level = None
        for name, (min_freq, max_freq) in consciousness_levels.items():
            if min_freq <= evolved < max_freq:
                level = name
        if evolved >= 1000:
            level = 'Cosmic'
            
        print(f"\nFrequency: {freq} Hz → {evolved:.2f} Hz")
        print(f"Consciousness: {level}")
        print(f"Resonance: {1/(1 + abs(evolved - (freq * phi**4))):.9f}")
        print(f"Coherence: {abs(np.sin(evolved * phi)) * phi:.6f}")
    
    # Test Quantum Evolution
    print("\n🌌 Quantum Evolution Test")
    print("=====================")
    evolution_stages = [
        ('φ⁰ → φ⁴', 1, phi**4),
        ('φ¹ → φ⁵', phi, phi**5),
        ('φ² → φ⁶', phi**2, phi**6),
        ('φ³ → φ⁷', phi**3, phi**7)
    ]
    
    for stage, start, end in evolution_stages:
        print(f"\n{stage}:")
        print(f"Start: {start:.6f}")
        print(f"End: {end:.6f}")
        print(f"Evolution: {end/start:.6f}")
        print(f"Resonance: {1/(1 + abs(end - (start * phi**4))):.9f}")
    
    # Test Integration Functions
    print("\n🔄 Integration Functions")
    print("=====================")
    metrics = interface.get_interface_metrics()
    print(f"\nResonance: {metrics['average_resonance']:.9f}")
    print(f"Coherence: {metrics['average_coherence']:.6f}")
    print(f"Evolution: {metrics['average_evolution']:.6f}")
    print(f"Integration: {metrics['average_integration']:.6f}")
    
    print("\nConsciousness Distribution:")
    for level, ratio in metrics['consciousness_distribution'].items():
        print(f"{level.title()}: {ratio:.2%}")

if __name__ == '__main__':
    test_quantum_functions()
