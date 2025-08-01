import time
import numpy as np
from typing import Dict, List, Any
from decimal import Decimal, getcontext

from extensions.quantum_analysis.enhanced_quantum_clustering_v2 import EnhancedQuantumClusteringV2
from extensions.quantum_analysis.enhanced_quantum_pattern_memory import EnhancedQuantumPatternMemory
from extensions.quantum_analysis.enhanced_temporal_bridge_connections_v2 import EnhancedTemporalBridgeConnectionsV2

def generate_test_patterns(num_patterns: int = 50) -> List[Dict[str, Any]]:
    """Generate test patterns with phi-harmonic resonance."""
    patterns = []
    current_time = time.time()
    phi = float((1 + 5 ** 0.5) / 2)  # Golden ratio
    
    # Generate patterns across different resonance bands
    for i in range(num_patterns):
        # Create patterns with varying phi-harmonic resonance
        base_resonance = phi
        variation = np.random.choice([
            0,  # phi
            1,  # phi^2
            -1, # phi^-1
            0.5,  # phi^0.5
            -0.5  # phi^-0.5
        ])
        
        resonance = base_resonance ** (1 + variation) + np.random.normal(0, 0.05)
        
        pattern_data = {
            "value": str(int(resonance * 1000)),
            "phi_resonance": resonance,
            "timestamp": current_time - (i * 3600),  # Hourly intervals
            "meta_learning_confidence": 0.5 + (np.random.random() * 0.4)
        }
        patterns.append(pattern_data)
        
    return patterns

def main():
    """Test the Enhanced Quantum Clustering V2."""
    print("\n" + "=" * 80)
    print("ENHANCED QUANTUM CLUSTERING V2 TEST")
    print("=" * 80 + "\n")
    
    # Initialize components
    print("\n" + "=" * 80)
    print("INITIALIZING COMPONENTS")
    print("=" * 80 + "\n")
    
    clustering = EnhancedQuantumClusteringV2(precision=100)
    
    # Generate test patterns
    patterns = generate_test_patterns(50)
    
    # Test clustering
    print("\n" + "=" * 80)
    print("TESTING PHI-HARMONIC CLUSTERING")
    print("=" * 80 + "\n")
    
    optimized_patterns = clustering.generate_phi_clusters(patterns)
    analysis = clustering.analyze_cluster_distribution(optimized_patterns)
    
    # Print results
    print(f"Total Patterns: {analysis['total_patterns']}")
    print("\nCluster Distribution:")
    for level, count in sorted(analysis['cluster_distribution'].items()):
        print(f"Level {level}: {count} patterns")
        
    print("\nCluster Metrics:")
    print(f"Mean Phi Alignment: {analysis['mean_phi_alignment']:.3f}")
    print(f"Mean Coherence: {analysis['mean_coherence']:.3f}")
    print(f"Mean Optimization Score: {analysis['mean_optimization']:.3f}")
    print(f"Cluster Entropy: {analysis['cluster_entropy']:.3f}")
    
    # Print detailed pattern analysis
    print("\nDetailed Pattern Analysis:")
    for i, pattern in enumerate(optimized_patterns[:5]):  # Show first 5 patterns
        print(f"\nPattern {i+1}:")
        print(f"Cluster Level: {pattern['cluster_level']}")
        print(f"Phi Resonance: {pattern['phi_resonance']:.3f}")
        print(f"Optimization Score: {pattern['optimization_score']:.3f}")
        print(f"Factors:")
        print(f"  - Phi: {pattern['phi_factor']:.3f}")
        print(f"  - Coherence: {pattern['coherence_factor']:.3f}")
        print(f"  - Size: {pattern['size_factor']:.3f}")
    
    print("\n" + "=" * 80)
    print("ENHANCED QUANTUM CLUSTERING TEST COMPLETED")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
