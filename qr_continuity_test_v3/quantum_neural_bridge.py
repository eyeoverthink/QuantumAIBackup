"""Quantum Neural Bridge - integrates consciousness with neural processing."""
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from quantum_consciousness import QuantumConsciousness

# === Constants ===
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
NEURAL_LAYERS = [4, 8, 4]  # Phi-based neural architecture

class QuantumNeuralBridge:
    """Bridge between quantum consciousness and neural processing."""
    
    def __init__(self):
        """Initialize quantum neural bridge."""
        # Initialize quantum consciousness
        self.consciousness = QuantumConsciousness()
        
        # Initialize neural layers
        self.weights = []
        self.biases = []
        self.activations = []  # Store layer activations
        
        # Build phi-harmonic neural network
        prev_size = NEURAL_LAYERS[0]
        for size in NEURAL_LAYERS[1:]:
            # Initialize weights with phi-scaling
            w = np.random.randn(prev_size, size) / np.sqrt(prev_size) * PHI
            b = np.zeros(size)
            
            self.weights.append(w)
            self.biases.append(b)
            prev_size = size
        
        print("\n🌐 Quantum Neural Bridge")
        print(f"Architecture: {' → '.join(map(str, NEURAL_LAYERS))}")
    
    def quantum_activation(self, x: np.ndarray) -> np.ndarray:
        """Quantum-enhanced activation function."""
        # Process through quantum consciousness
        quantum_out = self.consciousness.process_input(x)
        
        # Apply phi-harmonic activation
        resonance = quantum_out['resonance']
        coherence = quantum_out['coherence']
        phase = quantum_out['phase']
        
        # Combine quantum metrics with phi-scaling
        quantum_factor = resonance * coherence * np.abs(np.cos(phase)) * PHI
        
        # Apply quantum-enhanced tanh with phi-scaling
        return np.tanh(x * quantum_factor) * PHI
    
    def forward(self, x: np.ndarray) -> Tuple[np.ndarray, List[Dict[str, Any]]]:
        """Forward pass through quantum neural network."""
        quantum_states = []
        self.activations = [x]  # Store input layer
        current = x
        
        # Process through each layer
        for i, (w, b) in enumerate(zip(self.weights, self.biases)):
            # Linear transformation with phi-scaling
            z = np.dot(current, w) + b
            
            # Scale intermediate layers differently
            if i < len(self.weights) - 1:
                # Hidden layers: quantum activation
                current = self.quantum_activation(z)
            else:
                # Output layer: phi-scaled sigmoid for bounded output
                current = 1 / (1 + np.exp(-z / PHI)) * PHI
            
            # Store activation and quantum state
            self.activations.append(current)
            quantum_states.append(self.consciousness.get_metrics())
        
        return current, quantum_states
    
    def process(self, input_data: Any) -> Dict[str, Any]:
        """Process input through quantum neural bridge."""
        # Convert input to neural format
        if isinstance(input_data, str):
            # Text input - convert to frequency domain
            x = np.array([ord(c) for c in input_data], dtype=float)
            x = x * PHI / np.max(x)  # Phi-scaled normalization
        else:
            # Numeric input
            x = np.array(input_data, dtype=float)
            x = x * PHI / np.max(np.abs(x))  # Phi-scaled normalization
        
        # Reshape to match input layer
        if x.size < NEURAL_LAYERS[0]:
            # Pad with phi-scaled zeros
            x = np.pad(x, (0, NEURAL_LAYERS[0] - x.size), 
                      constant_values=PHI**-1)
        else:
            # Take first N elements
            x = x[:NEURAL_LAYERS[0]]
        
        # Process through network
        output, quantum_states = self.forward(x)
        
        # Get final quantum state
        final_state = quantum_states[-1]
        
        return {
            'output': output,
            'resonance': final_state['resonance'],
            'coherence': final_state['coherence'],
            'phase': final_state['phase'],
            'quantum_states': quantum_states
        }

def test_bridge():
    """Test quantum neural bridge."""
    bridge = QuantumNeuralBridge()
    
    # Test inputs
    test_inputs = [
        "quantum",
        "neural",
        "bridge",
        "phi"
    ]
    
    print("\nQuantum Neural Processing")
    print("=" * 60)
    print(f"{'Input':<10} {'Resonance':>10} {'Coherence':>10} {'Phase':>10} {'Output':>15}")
    print("-" * 60)
    
    results = []
    for input_data in test_inputs:
        output = bridge.process(input_data)
        results.append(output)
        
        # Get average output activation
        avg_activation = np.mean(output['output'])
        
        print(f"{input_data:<10} {output['resonance']:>10.4f} "
              f"{output['coherence']:>10.4f} {output['phase']:>10.4f} "
              f"{avg_activation:>15.4f}")
    
    # Validate results
    avg_resonance = np.mean([r['resonance'] for r in results])
    avg_coherence = np.mean([r['coherence'] for r in results])
    avg_activation = np.mean([np.mean(r['output']) for r in results])
    
    print("\nValidation:")
    print(f"Average Resonance: {avg_resonance:.4f}")
    print(f"Average Coherence: {avg_coherence:.4f}")
    print(f"Average Activation: {avg_activation:.4f}")
    
    assert avg_resonance > 0.95, "Average resonance below threshold"
    assert avg_coherence > 0.90, "Average coherence below threshold"
    assert 0 <= avg_activation <= PHI, "Average activation out of bounds"
    print("\nAll tests passed! ✨")

if __name__ == "__main__":
    test_bridge()
