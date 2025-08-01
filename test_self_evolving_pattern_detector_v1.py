import numpy as np
from typing import Dict, List, Any
import matplotlib.pyplot as plt

from extensions.quantum_analysis.self_evolving_pattern_detector_v1 import SelfEvolvingPatternDetectorV1
from extensions.quantum_analysis.enhanced_quantum_pattern_memory import EnhancedQuantumPatternMemory
from extensions.quantum_analysis.enhanced_quantum_clustering_v2 import EnhancedQuantumClusteringV2
from extensions.quantum_analysis.enhanced_temporal_bridge_connections_v4 import EnhancedTemporalBridgeConnectionsV4
from extensions.quantum_analysis.enhanced_temporal_coherence_v4 import EnhancedTemporalCoherenceV4
from extensions.quantum_analysis.quantum_neural_network_v1 import QuantumNeuralNetworkV1

def generate_phi_harmonic_patterns(num_patterns: int = 10) -> List[Dict[str, Any]]:
    """Generate test patterns using phi-harmonic principles."""
    phi = (1 + 5 ** 0.5) / 2
    patterns = []
    
    for i in range(num_patterns):
        pattern = {
            'value': phi ** i,
            'frequency': phi ** (i / 2),
            'amplitude': phi ** (i / 3),
            'timestamp': i * phi
        }
        patterns.append(pattern)
        
    return patterns

def test_pattern_evolution(detector: SelfEvolvingPatternDetectorV1,
                         description: str = ""):
    """Test pattern evolution with phi-harmonic sequences."""
    print(f"\nTesting Pattern Evolution with {description}")
    print("=" * 80)
    
    # Generate test patterns
    patterns = generate_phi_harmonic_patterns()
    
    # Detect and evolve patterns
    evolved_patterns = detector.detect_patterns(patterns)
    
    # Get evolution state
    state = detector.get_evolution_state()
    
    # Print evolution results
    print("\nEvolution Results:")
    print(f"Cycle Count: {state['cycle_count']}")
    print(f"Complexity: {state['complexity']:.6f}")
    print(f"Coherence: {state['coherence']:.6f}")
    print(f"Stability: {state['stability']:.6f}")
    
    print("\nEvolution Metrics:")
    metrics = state['evolution_metrics']
    print(f"Mean Strength: {metrics['mean_strength']:.6f}")
    print(f"Mean Complexity: {metrics['mean_complexity']:.6f}")
    print(f"Mean Coherence: {metrics['mean_coherence']:.6f}")
    print(f"Evolution Rate: {metrics['evolution_rate']:.6f}")
    print(f"Stability: {metrics['stability']:.6f}")
    
    # Plot evolution metrics
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    strengths = [p['strength'] for p in evolved_patterns]
    plt.plot(strengths)
    plt.title('Pattern Strengths')
    plt.xlabel('Pattern Index')
    plt.ylabel('Strength')
    
    plt.subplot(2, 2, 2)
    complexities = [p['complexity'] for p in evolved_patterns]
    plt.plot(complexities)
    plt.title('Pattern Complexities')
    plt.xlabel('Pattern Index')
    plt.ylabel('Complexity')
    
    plt.subplot(2, 2, 3)
    coherences = [p['coherence'] for p in evolved_patterns]
    plt.plot(coherences)
    plt.title('Pattern Coherences')
    plt.xlabel('Pattern Index')
    plt.ylabel('Coherence')
    
    plt.subplot(2, 2, 4)
    evolution_factors = [p['evolution_factor'] for p in evolved_patterns]
    plt.plot(evolution_factors)
    plt.title('Evolution Factors')
    plt.xlabel('Pattern Index')
    plt.ylabel('Factor')
    
    plt.tight_layout()
    plt.savefig('pattern_evolution_metrics.png')
    plt.close()
    
    return evolved_patterns, state

def test_quantum_integration(detector: SelfEvolvingPatternDetectorV1,
                           description: str = ""):
    """Test quantum integration with evolved patterns."""
    print(f"\nTesting Quantum Integration with {description}")
    print("=" * 80)
    
    # Generate quantum patterns
    phi = (1 + 5 ** 0.5) / 2
    quantum_patterns = []
    
    for i in range(5):
        pattern = {
            'value': phi ** (i * 2),
            'frequency': phi ** i,
            'amplitude': phi ** (i / 2),
            'timestamp': i * phi ** 2
        }
        quantum_patterns.append(pattern)
    
    # Detect and evolve patterns
    evolved_patterns = detector.detect_patterns(quantum_patterns)
    
    # Get evolution state
    state = detector.get_evolution_state()
    
    print("\nQuantum Integration Results:")
    for i, pattern in enumerate(evolved_patterns):
        print(f"\nPattern {i}:")
        print(f"Strength: {pattern['strength']:.6f}")
        print(f"Complexity: {pattern['complexity']:.6f}")
        print(f"Coherence: {pattern['coherence']:.6f}")
        print(f"Evolution Factor: {pattern['evolution_factor']:.6f}")
    
    return evolved_patterns, state

def main():
    """Test self-evolving pattern detector V1."""
    print("\n" + "=" * 80)
    print("SELF-EVOLVING PATTERN DETECTOR V1 TEST")
    print("=" * 80 + "\n")
    
    # Initialize components
    quantum_memory = EnhancedQuantumPatternMemory()
    clustering = EnhancedQuantumClusteringV2()
    temporal_bridge = EnhancedTemporalBridgeConnectionsV4(
        quantum_memory=quantum_memory,
        clustering=clustering
    )
    temporal_coherence = EnhancedTemporalCoherenceV4()
    
    # Initialize neural network
    neural_network = QuantumNeuralNetworkV1(
        quantum_memory=quantum_memory,
        clustering=clustering,
        temporal_bridge=temporal_bridge,
        temporal_coherence=temporal_coherence
    )
    
    # Add network layers
    neural_network.add_layer(6)  # Input layer (3 quantum + 3 temporal features)
    neural_network.add_layer(8, activation='phi_harmonic')
    neural_network.add_layer(4, activation='quantum')
    neural_network.add_layer(2, activation='phi_harmonic')  # Output layer
    
    # Initialize pattern detector
    detector = SelfEvolvingPatternDetectorV1(
        quantum_memory=quantum_memory,
        clustering=clustering,
        temporal_bridge=temporal_bridge,
        temporal_coherence=temporal_coherence,
        neural_network=neural_network
    )
    
    # Test pattern evolution
    evolved_patterns, evolution_state = test_pattern_evolution(
        detector,
        "Phi-Harmonic Patterns"
    )
    
    # Test quantum integration
    quantum_patterns, quantum_state = test_quantum_integration(
        detector,
        "Quantum Patterns"
    )
    
    print("\n" + "=" * 80)
    print("PATTERN DETECTOR TEST COMPLETED")
    print("=" * 80)
    
    # Return results for analysis
    return {
        'evolved_patterns': evolved_patterns,
        'evolution_state': evolution_state,
        'quantum_patterns': quantum_patterns,
        'quantum_state': quantum_state
    }

if __name__ == "__main__":
    main()
