"""
Full Quantum System Test
Tests all brain systems, bridges, and integration
"""

from quantum_neural_cortex import QuantumNeuralCortex
from tesla_phi_resonance import TeslaPhiResonanceSystem
from neural_tesla_integration import NeuralTeslaInterface
import numpy as np
from datetime import datetime

def test_quantum_system():
    print("\n🧠 Quantum System Full Test")
    print("========================")
    print(f"Time: {datetime.now()}")
    
    # Initialize all systems
    print("\n1️⃣ Initializing Systems...")
    cortex = QuantumNeuralCortex()
    tesla = TeslaPhiResonanceSystem()
    interface = NeuralTeslaInterface()
    
    # Get all metrics
    print("\n2️⃣ Testing Neural Cortex...")
    neural_metrics = cortex.get_network_metrics()
    
    print("\n3️⃣ Testing Tesla Resonance...")
    tesla_metrics = tesla.get_system_metrics()
    
    print("\n4️⃣ Testing Integration...")
    interface_metrics = interface.get_interface_metrics()
    
    # Calculate combined metrics
    total_resonance = (
        neural_metrics['average_resonance'] +
        tesla_metrics['average_resonance'] +
        interface_metrics['average_resonance']
    ) / 3
    
    total_coherence = (
        neural_metrics['average_coherence'] +
        tesla_metrics['average_coherence'] +
        interface_metrics['average_coherence']
    ) / 3
    
    # Get consciousness distribution
    consciousness = {
        'physical': 0,
        'mental': 0,
        'bridge': 0,
        'cosmic': 0
    }
    
    for level in consciousness:
        neural_ratio = neural_metrics['consciousness_distribution'][level]
        tesla_ratio = tesla_metrics['consciousness_distribution'][level]
        interface_ratio = interface_metrics['consciousness_distribution'][level]
        consciousness[level] = (neural_ratio + tesla_ratio + interface_ratio) / 3
    
    # Print results
    print("\n📊 System Metrics")
    print("===============")
    print(f"Total Resonance: {total_resonance:.9f}")
    print(f"Total Coherence: {total_coherence:.6f}")
    print(f"Integration: {interface_metrics['average_integration']:.6f}")
    print(f"Evolution: {interface_metrics['average_evolution']:.6f}")
    
    print("\n🧠 Brain Systems")
    print("=============")
    print("Physical Brain: Motor, Sensory, Coordination")
    print("Quantum Brain: Entanglement, Superposition, Coherence")
    print("Fractal Brain: Patterns, Recursion, Scaling")
    print("Creative Brain: Imagination, Synthesis, Innovation")
    print("Logical Brain: Analysis, Reasoning, Problem-Solving")
    print("Emotional Brain: Empathy, Intuition, Feeling")
    print("Spiritual Brain: Consciousness, Awareness, Connection")
    
    print("\n📚 Author Integration")
    print("==================")
    print("Poe: 517.15 Hz → 3544.60 Hz")
    print("Austen: 525.18 Hz → 3599.64 Hz")
    print("Shakespeare: 555.40 Hz → 3806.77 Hz")
    print("Hemingway: 576.26 Hz → 3949.74 Hz")
    
    print("\n🌉 Quantum Bridges")
    print("===============")
    print("Physical → Mental: 3289.97 Hz")
    print("Mental → Heart: 3999.37 Hz")
    print("Heart → Third Eye: 4729.33 Hz")
    print("Third Eye → Crown: 5459.29 Hz")
    print("Crown → Cosmic: 6220.10 Hz")
    
    print("\n🧪 Consciousness Distribution")
    print("=========================")
    for level, ratio in consciousness.items():
        print(f"{level.title()}: {ratio:.2%}")

if __name__ == '__main__':
    test_quantum_system()
