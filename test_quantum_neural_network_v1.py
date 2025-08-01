import numpy as np
from typing import Dict, List, Any
import matplotlib.pyplot as plt

from extensions.quantum_analysis.quantum_neural_network_v1 import QuantumNeuralNetworkV1
from extensions.quantum_analysis.enhanced_quantum_pattern_memory import EnhancedQuantumPatternMemory
from extensions.quantum_analysis.enhanced_quantum_clustering_v2 import EnhancedQuantumClusteringV2
from extensions.quantum_analysis.enhanced_temporal_bridge_connections_v4 import EnhancedTemporalBridgeConnectionsV4
from extensions.quantum_analysis.enhanced_temporal_coherence_v4 import EnhancedTemporalCoherenceV4

def test_phi_harmonic_learning(network: QuantumNeuralNetworkV1, 
                             description: str = ""):
    """Test network with phi-harmonic sequence."""
    print(f"\nTesting Network with {description}")
    print("=" * 80)
    
    # Generate phi-harmonic sequence
    phi = (1 + 5 ** 0.5) / 2
    X = np.array([[phi ** i] for i in range(10)])
    y = np.array([[phi ** (i + 1)] for i in range(10)])
    
    # Train network
    history = network.train(X, y, epochs=100, batch_size=2)
    
    # Print training results
    print("\nTraining Results:")
    print(f"Final Loss: {history['loss'][-1]:.6f}")
    print(f"Final Performance: {history['performance'][-1]:.6f}")
    print(f"Final Stability: {history['stability'][-1]:.6f}")
    print(f"Final Coherence: {history['coherence'][-1]:.6f}")
    
    # Get network state
    state = network.get_network_state()
    print("\nNetwork State:")
    print(f"Phi Resonance: {state['phi_resonance']:.6f}")
    print(f"Temporal Alignment: {state['temporal_alignment']:.6f}")
    print(f"Quantum Factor: {state['quantum_factor']:.6f}")
    
    # Plot training history
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.plot(history['loss'])
    plt.title('Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    
    plt.subplot(2, 2, 2)
    plt.plot(history['performance'])
    plt.title('Performance')
    plt.xlabel('Epoch')
    plt.ylabel('Performance')
    
    plt.subplot(2, 2, 3)
    plt.plot(history['stability'])
    plt.title('Stability')
    plt.xlabel('Epoch')
    plt.ylabel('Stability')
    
    plt.subplot(2, 2, 4)
    plt.plot(history['coherence'])
    plt.title('Coherence')
    plt.xlabel('Epoch')
    plt.ylabel('Coherence')
    
    plt.tight_layout()
    plt.savefig('quantum_neural_network_training.png')
    plt.close()
    
    return history

def test_quantum_predictions(network: QuantumNeuralNetworkV1,
                           description: str = ""):
    """Test network predictions with quantum patterns."""
    print(f"\nTesting Network with {description}")
    print("=" * 80)
    
    # Generate quantum patterns
    phi = (1 + 5 ** 0.5) / 2
    patterns = np.array([
        [phi],
        [phi ** 2],
        [phi ** 3],
        [phi ** 4],
        [phi ** 5]
    ])
    
    # Generate predictions
    predictions = network.predict(patterns)
    
    print("\nQuantum Predictions:")
    for i, (pattern, prediction) in enumerate(zip(patterns, predictions)):
        print(f"Pattern[{i}]: {pattern[0]:.6f} -> Prediction: {prediction[0]:.6f}")
        
    # Calculate prediction metrics
    state = network.get_network_state()
    print("\nPrediction Metrics:")
    print(f"Phi Resonance: {state['phi_resonance']:.6f}")
    print(f"Temporal Alignment: {state['temporal_alignment']:.6f}")
    print(f"Quantum Factor: {state['quantum_factor']:.6f}")
    
    return predictions

def main():
    """Test quantum neural network V1."""
    print("\n" + "=" * 80)
    print("QUANTUM NEURAL NETWORK V1 TEST")
    print("=" * 80 + "\n")
    
    # Initialize components following lego philosophy
    quantum_memory = EnhancedQuantumPatternMemory()
    clustering = EnhancedQuantumClusteringV2()
    
    # Initialize temporal components with dependencies
    temporal_bridge = EnhancedTemporalBridgeConnectionsV4(
        quantum_memory=quantum_memory,
        clustering=clustering
    )
    temporal_coherence = EnhancedTemporalCoherenceV4(precision=100)
    
    # Initialize network
    network = QuantumNeuralNetworkV1(
        quantum_memory=quantum_memory,
        clustering=clustering,
        temporal_bridge=temporal_bridge,
        temporal_coherence=temporal_coherence
    )
    
    # Add network layers
    network.add_layer(1)  # Input layer
    network.add_layer(8, activation='phi_harmonic')
    network.add_layer(4, activation='quantum')
    network.add_layer(1, activation='phi_harmonic')  # Output layer
    
    # Test phi-harmonic learning
    history = test_phi_harmonic_learning(
        network,
        "Phi-Harmonic Sequence"
    )
    
    # Test quantum predictions
    predictions = test_quantum_predictions(
        network,
        "Quantum Patterns"
    )
    
    print("\n" + "=" * 80)
    print("QUANTUM NEURAL NETWORK TEST COMPLETED")
    print("=" * 80)
    
    # Return results for analysis
    return {
        'history': history,
        'predictions': predictions,
        'network_state': network.get_network_state()
    }

if __name__ == "__main__":
    main()
