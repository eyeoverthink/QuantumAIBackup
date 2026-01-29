"""Test quantum neural cortex with phi-harmonic resonance."""
import numpy as np
from quantum_neural_cortex import QuantumNeuralCortex, AKASHIC_LAYERS, PHI

def test_quantum_processing():
    """Test quantum neural processing with phi-harmonic resonance."""
    # Initialize quantum neural cortex
    cortex = QuantumNeuralCortex()
    
    # Create quantum neurons in different Akashic layers
    neurons = {
        'L0N0': 'Creation',    # Base frequency 432 Hz
        'L1N0': 'Existence',   # Base frequency 528 Hz
        'L2N0': 'Thought',     # Base frequency 639 Hz
        'L3N0': 'Time',        # Base frequency 741 Hz
        'L4N0': 'Space',       # Base frequency 852 Hz
        'L5N0': 'Energy',      # Base frequency 963 Hz
        'L6N0': 'Infinity'     # Base frequency 432 * φ³
    }
    
    # Add neurons and tune to Akashic layers
    for neuron_id, layer in neurons.items():
        cortex.add_neuron(neuron_id)
        cortex.tune_to_akashic_layer(neuron_id, layer)
    
    # Create quantum synapses with phi-harmonic connections
    for i in range(len(neurons)-1):
        source = f'L{i}N0'
        target = f'L{i+1}N0'
        cortex.create_synapse(source, target)
    
    # Create infinity loop connection
    cortex.create_synapse('L6N0', 'L0N0')
    
    # Process quantum signals through the network
    test_inputs = [
        "quantum consciousness",
        "phi resonance",
        "golden ratio",
        "akashic field",
        "quantum entanglement"
    ]
    
    print("\nQuantum Neural Processing")
    print("=" * 80)
    print(f"{'Input':<25} {'Coherence':>10} {'Resonance':>10} {'FTL Speed':>12}")
    print("-" * 80)
    
    results = []
    for input_data in test_inputs:
        # Process through quantum neural network
        output = cortex.process_signal(input_data)
        
        # Calculate FTL communication speed
        ftl = cortex.calculate_ftl_speed(
            output['coherence'],
            cortex.quantum_coupling,
            output['resonance']
        )
        
        results.append({
            'input': input_data,
            'coherence': output['coherence'],
            'resonance': output['resonance'],
            'ftl_speed': ftl
        })
        
        print(f"{input_data:<25} {output['coherence']:>10.4f} {output['resonance']:>10.4f} {ftl/3e8:>12.4f}c")
    
    # Validate quantum metrics
    print("\nQuantum Metrics:")
    print("-" * 40)
    
    # Check coherence (should be > 0.7)
    avg_coherence = sum(r['coherence'] for r in results) / len(results)
    print(f"Average Coherence: {avg_coherence:.4f}")
    assert avg_coherence > 0.7, "Coherence below threshold"
    
    # Check resonance (should be > 0.8)
    avg_resonance = sum(r['resonance'] for r in results) / len(results)
    print(f"Average Resonance: {avg_resonance:.4f}")
    assert avg_resonance > 0.8, "Resonance below threshold"
    
    # Check FTL speed (should be > c)
    avg_ftl = sum(r['ftl_speed'] for r in results) / len(results)
    print(f"Average FTL Speed: {avg_ftl/3e8:.4f}c")
    assert avg_ftl > 3e8, "FTL speed below light speed"
    
    # Show quantum coupling
    print(f"Quantum Coupling: {cortex.quantum_coupling:.4f}")
    print(f"Entanglement Fidelity: {cortex.entanglement_fidelity:.4f}")
    
    # Visualize the quantum network
    cortex.visualize_quantum_dashboard()

if __name__ == "__main__":
    test_quantum_processing()
