"""
Brain Function Test
Tests each brain's quantum functions and phi-harmonic resonance
"""

from quantum_neural_cortex import QuantumNeuralCortex
from tesla_phi_resonance import TeslaPhiResonanceSystem
from neural_tesla_integration import NeuralTeslaInterface
import numpy as np
from datetime import datetime

def test_brain_functions():
    print("\n🧠 Quantum Brain Function Test")
    print("===========================")
    print(f"Time: {datetime.now()}")
    
    # Initialize systems
    cortex = QuantumNeuralCortex()
    tesla = TeslaPhiResonanceSystem()
    interface = NeuralTeslaInterface()
    
    # Test Physical Brain
    print("\n💪 Physical Brain Test")
    print("==================")
    physical_nodes = ['motor_cortex', 'sensory_processing', 'coordination']
    for node in physical_nodes:
        state = cortex.process_neuron(f"physical_{node}")
        print(f"\n{node.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Integration: {state.integration:.6f}")
    
    # Test Quantum Brain
    print("\n🌌 Quantum Brain Test")
    print("==================")
    quantum_nodes = ['entanglement', 'superposition', 'coherence']
    for node in quantum_nodes:
        state = cortex.process_neuron(f"quantum_{node}")
        print(f"\n{node.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Integration: {state.integration:.6f}")
    
    # Test Fractal Brain
    print("\n🌀 Fractal Brain Test")
    print("==================")
    fractal_nodes = ['pattern_recognition', 'recursive_thinking', 'scaling']
    for node in fractal_nodes:
        state = cortex.process_neuron(f"fractal_{node}")
        print(f"\n{node.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Integration: {state.integration:.6f}")
    
    # Test Creative Brain
    print("\n🎨 Creative Brain Test")
    print("==================")
    creative_nodes = ['imagination', 'synthesis', 'innovation']
    for node in creative_nodes:
        state = cortex.process_neuron(f"creative_{node}")
        print(f"\n{node.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Integration: {state.integration:.6f}")
    
    # Test Logical Brain
    print("\n🧮 Logical Brain Test")
    print("==================")
    logical_nodes = ['analysis', 'reasoning', 'problem_solving']
    for node in logical_nodes:
        state = cortex.process_neuron(f"logical_{node}")
        print(f"\n{node.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Integration: {state.integration:.6f}")
    
    # Test Emotional Brain
    print("\n❤️ Emotional Brain Test")
    print("===================")
    emotional_nodes = ['empathy', 'intuition', 'feeling']
    for node in emotional_nodes:
        state = cortex.process_neuron(f"emotional_{node}")
        print(f"\n{node.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Integration: {state.integration:.6f}")
    
    # Test Spiritual Brain
    print("\n🕉️ Spiritual Brain Test")
    print("===================")
    spiritual_nodes = ['consciousness', 'awareness', 'connection']
    for node in spiritual_nodes:
        state = cortex.process_neuron(f"spiritual_{node}")
        print(f"\n{node.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Integration: {state.integration:.6f}")
    
    # Test Author Integration
    print("\n📚 Author Brain Test")
    print("=================")
    authors = ['poe', 'austen', 'shakespeare', 'hemingway']
    for author in authors:
        state = interface.process_interface(f"author_{author}")
        print(f"\n{author.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Integration: {state.integration:.6f}")
        print(f"Evolution: {state.evolution:.6f}")
    
    # Get overall metrics
    metrics = cortex.get_network_metrics()
    print("\n📊 Overall Brain Metrics")
    print("====================")
    print(f"Average Resonance: {metrics['average_resonance']:.9f}")
    print(f"Average Coherence: {metrics['average_coherence']:.6f}")
    print(f"Average Integration: {metrics['average_integration']:.6f}")
    
    print("\n🧪 Consciousness Distribution")
    print("=========================")
    for level, ratio in metrics['consciousness_distribution'].items():
        print(f"{level.title()}: {ratio:.2%}")

if __name__ == '__main__':
    test_brain_functions()
