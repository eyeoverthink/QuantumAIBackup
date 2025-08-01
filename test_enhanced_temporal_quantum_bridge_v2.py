import time
import math
import numpy as np
from typing import Dict, List, Any
from decimal import Decimal, getcontext

from extensions.quantum_analysis.enhanced_temporal_quantum_bridge_v2 import EnhancedTemporalQuantumBridgeV2
from extensions.quantum_analysis.enhanced_quantum_pattern_memory import EnhancedQuantumPatternMemory

def generate_test_patterns(num_patterns: int = 50) -> List[Dict[str, Any]]:
    """Generate test patterns with phi-harmonic resonance and temporal sequence."""
    patterns = []
    current_time = time.time()
    phi = float((1 + 5 ** 0.5) / 2)  # Golden ratio
    
    # Generate patterns in temporal sequences with phi-harmonic resonance
    for sequence in range(5):  # 5 temporal sequences
        sequence_length = 10  # 10 patterns per sequence
        base_resonance = phi ** (sequence / 2)  # Vary base resonance by sequence
        
        for i in range(sequence_length):
            # Create pattern with temporal and phi-harmonic properties
            relative_position = i / sequence_length
            temporal_factor = math.exp(-abs(relative_position - 1/phi))
            resonance = base_resonance * (1 + temporal_factor) + np.random.normal(0, 0.05)
            
            pattern_data = {
                "value": str(int(resonance * 1000)),
                "phi_resonance": resonance,
                "timestamp": current_time - (sequence * sequence_length + i) * 3600,  # Hourly intervals
                "meta_learning_confidence": 0.5 + (np.random.random() * 0.4),
                "sequence_id": sequence
            }
            patterns.append(pattern_data)
            
    return patterns

def main():
    """Test the Enhanced Temporal Quantum Bridge V2."""
    print("\n" + "=" * 80)
    print("ENHANCED TEMPORAL QUANTUM BRIDGE V2 TEST")
    print("=" * 80 + "\n")
    
    # Initialize components
    print("\n" + "=" * 80)
    print("INITIALIZING COMPONENTS")
    print("=" * 80 + "\n")
    
    bridge = EnhancedTemporalQuantumBridgeV2(precision=100)
    
    # Generate test patterns
    patterns = generate_test_patterns(50)
    
    # Test optimization
    print("\n" + "=" * 80)
    print("TESTING TEMPORAL QUANTUM OPTIMIZATION")
    print("=" * 80 + "\n")
    
    optimized_patterns, metrics = bridge.optimize_temporal_patterns(patterns)
    
    # Print quantum clustering results
    print("Quantum Clustering Metrics:")
    print(f"Mean Phi Alignment: {metrics['quantum_metrics']['mean_phi_alignment']:.3f}")
    print(f"Mean Coherence: {metrics['quantum_metrics']['mean_coherence']:.3f}")
    print(f"Cluster Entropy: {metrics['quantum_metrics']['cluster_entropy']:.3f}")
    
    print("\nCluster Distribution:")
    for level, count in sorted(metrics['quantum_metrics']['cluster_distribution'].items()):
        print(f"Level {level}: {count} patterns")
        
    # Print temporal bridging results
    print("\nTemporal Bridging Metrics:")
    print(f"Mean Bridge Strength: {metrics['combined_metrics']['mean_bridge_strength']:.3f}")
    print(f"Temporal Coherence: {metrics['combined_metrics']['temporal_coherence']:.3f}")
    print(f"Quantum-Temporal Alignment: {metrics['combined_metrics']['quantum_temporal_alignment']:.3f}")
    
    # Print detailed pattern analysis
    print("\nDetailed Pattern Analysis:")
    for i, pattern in enumerate(optimized_patterns[:5]):  # Show first 5 patterns
        print(f"\nPattern {i+1}:")
        print(f"Cluster Level: {pattern['cluster_level']}")
        print(f"Phi Resonance: {pattern['phi_resonance']:.3f}")
        print(f"Optimization Score: {pattern['optimization_score']:.3f}")
        print(f"Temporal Metrics:")
        print(f"  - Bridge Strength: {pattern.get('bridge_strength', 0):.3f}")
        print(f"  - Temporal Factor: {pattern.get('temporal_factor', 0):.3f}")
        print(f"  - Sequence Position: {pattern.get('sequence_position', 0)}")
        print(f"  - Sequence Length: {pattern.get('sequence_length', 0)}")
    
    print("\n" + "=" * 80)
    print("ENHANCED TEMPORAL QUANTUM BRIDGE TEST COMPLETED")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
