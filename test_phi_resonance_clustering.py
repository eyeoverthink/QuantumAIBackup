"""
Test Phi-Resonance Clustering

This script demonstrates the capabilities of the Phi-Resonance Clustering module,
showing how patterns with similar phi-resonance values can be clustered for more
sophisticated analysis and insight generation.
"""

import os
import sys
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Tuple

# Import the components we need
from extensions.quantum_analysis.enhanced_quantum_pattern_memory import EnhancedQuantumPatternMemory
from extensions.quantum_analysis.enhanced_quantum_memory_meta_learning_bridge import EnhancedQuantumMemoryMetaLearningBridge
from extensions.quantum_analysis.phi_resonance_clustering import PhiResonanceClustering

def print_section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80 + "\n")

def main():
    """Main test function for Phi-Resonance Clustering."""
    print_section_header("PHI-RESONANCE CLUSTERING TEST")
    
    # Initialize components
    print_section_header("INITIALIZING COMPONENTS")
    
    # Create the quantum memory
    quantum_memory = EnhancedQuantumPatternMemory()
    
    # Create the bridge
    bridge = EnhancedQuantumMemoryMetaLearningBridge(quantum_memory=quantum_memory)
    
    # Create the clustering module
    clustering = PhiResonanceClustering(
        quantum_memory=quantum_memory,
        bridge=bridge
    )
    
    # Ensure we have enough test patterns with varied phi-resonance values
    print_section_header("GENERATING TEST PATTERNS")
    
    # Generate patterns with phi-resonance values around key phi-harmonic points
    phi = (1 + 5 ** 0.5) / 2  # Golden ratio (φ ≈ 1.618)
    phi_inverse = 1 / phi  # Golden ratio conjugate (φ⁻¹ ≈ 0.618)
    
    # Define resonance clusters to generate
    resonance_clusters = [
        (phi, 0.05),             # Cluster around φ
        (phi_inverse, 0.05),     # Cluster around φ⁻¹
        (phi * 2, 0.1),          # Cluster around 2φ
        (phi_inverse / 2, 0.05)  # Cluster around φ⁻¹/2
    ]
    
    # Generate patterns for each cluster
    pattern_ids = []
    for target_resonance, variation in resonance_clusters:
        print(f"Generating patterns with resonance around {target_resonance:.4f}...")
        
        # Generate 5-10 patterns for each cluster
        num_patterns = np.random.randint(5, 11)
        
        for i in range(num_patterns):
            # Create a resonance value with some variation
            resonance = target_resonance + (np.random.random() - 0.5) * variation * 2
            
            # Create a test value (using Fibonacci-like sequence for some patterns)
            if i % 3 == 0:
                a, b = 1, 1
                for _ in range(np.random.randint(5, 15)):
                    a, b = b, a + b
                value = str(b)
            else:
                # Use a number with phi-harmonic properties
                value = str(int(resonance * 1000 + np.random.randint(1, 1000)))
            
            # Create pattern data
            pattern_data = {
                "value": value,
                "phi_resonance": resonance,
                "meta_learning_confidence": 0.5 + (np.random.random() * 0.4),
                "meta_learning_insights": [f"Test insight for resonance {resonance:.4f}"],
                "timestamp": time.time() - np.random.randint(0, 3600 * 24 * 10)  # Random time in the last 10 days
            }
            
            # Store the pattern
            pattern_id = quantum_memory.store_pattern(pattern_data)
            pattern_ids.append(pattern_id)
    
    print(f"Generated {len(pattern_ids)} test patterns with varied phi-resonance values")
    
    # Test basic clustering
    print_section_header("TESTING BASIC CLUSTERING")
    
    # Cluster patterns around phi
    print("Clustering patterns around φ...")
    phi_cluster_result = clustering.cluster_by_phi_resonance(
        resonance_range=(phi - 0.2, phi + 0.2),
        n_clusters=3,
        algorithm="kmeans"
    )
    
    # Print clustering results
    print(f"Clustering result: {phi_cluster_result['message']}")
    print(f"Silhouette score: {phi_cluster_result['silhouette_score']:.4f}")
    print(f"Phi-harmonic balance: {phi_cluster_result.get('phi_harmonic_balance', 0.0):.4f}")
    print("\nCluster sizes:")
    for cluster_id, patterns in phi_cluster_result.get("clusters", {}).items():
        print(f"  Cluster {cluster_id}: {len(patterns)} patterns")
    
    # Visualize the clusters
    phi_cluster_viz_path = clustering.visualize_clusters(
        phi_cluster_result,
        output_path="visualizations/phi_clusters.png"
    )
    
    # Test optimal clustering
    print_section_header("TESTING OPTIMAL CLUSTERING")
    
    # Find optimal number of clusters for all patterns
    print("Finding optimal number of clusters for all patterns...")
    optimal_result = clustering.find_optimal_clusters(
        resonance_range=(0.1, 5.0),
        max_clusters=8,
        algorithm="kmeans"
    )
    
    # Print optimal clustering results
    print(f"Optimal clustering result: {optimal_result['message']}")
    print(f"Optimal number of clusters: {optimal_result.get('optimal_clusters', 0)}")
    print(f"Silhouette score: {optimal_result.get('silhouette_score', 0.0):.4f}")
    
    # Print silhouette scores for different numbers of clusters
    print("\nSilhouette scores by number of clusters:")
    for n_clusters, score in optimal_result.get("silhouette_scores", {}).items():
        print(f"  {n_clusters} clusters: {score:.4f}")
    
    # Visualize the optimal clusters
    optimal_viz_path = clustering.visualize_clusters(
        optimal_result,
        output_path="visualizations/optimal_clusters.png"
    )
    
    # Test cluster insights
    print_section_header("TESTING CLUSTER INSIGHTS")
    
    # Generate insights for the optimal clustering
    insights = clustering.generate_cluster_insights(optimal_result)
    
    # Print insights
    print(f"Generated {len(insights)} insights:")
    for i, insight in enumerate(insights, 1):
        print(f"{i}. {insight.get('text')} (confidence: {insight.get('confidence', 0.0):.2f})")
    
    # Test different clustering algorithms
    print_section_header("TESTING DIFFERENT CLUSTERING ALGORITHMS")
    
    algorithms = ["kmeans", "dbscan", "hierarchical"]
    algorithm_results = {}
    
    for algorithm in algorithms:
        print(f"\nTesting {algorithm} clustering...")
        result = clustering.cluster_by_phi_resonance(
            resonance_range=(0.1, 5.0),
            n_clusters=4,
            algorithm=algorithm
        )
        
        algorithm_results[algorithm] = result
        
        # Print results
        print(f"  Result: {result['message']}")
        print(f"  Silhouette score: {result.get('silhouette_score', 0.0):.4f}")
        print(f"  Number of clusters: {len(result.get('clusters', {}))}")
        
        # Visualize
        viz_path = clustering.visualize_clusters(
            result,
            output_path=f"visualizations/{algorithm}_clusters.png"
        )
    
    # Compare algorithm performance
    print("\nAlgorithm performance comparison:")
    for algorithm, result in algorithm_results.items():
        print(f"  {algorithm}: Silhouette score = {result.get('silhouette_score', 0.0):.4f}")
    
    # Get clustering statistics
    print_section_header("CLUSTERING STATISTICS")
    
    stats = clustering.get_statistics()
    print("Phi-Resonance Clustering statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Create a summary visualization comparing all algorithms
    print_section_header("CREATING SUMMARY VISUALIZATION")
    
    # Create figure with phi-harmonic dimensions
    plt.figure(figsize=(phi * 5, phi * 3))
    
    # Plot silhouette scores for different algorithms
    algorithms = list(algorithm_results.keys())
    scores = [result.get("silhouette_score", 0.0) for result in algorithm_results.values()]
    
    plt.bar(algorithms, scores, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.5, label='Good clustering threshold')
    plt.axhline(y=0.7, color='g', linestyle='--', alpha=0.5, label='Excellent clustering threshold')
    
    plt.xlabel('Clustering Algorithm')
    plt.ylabel('Silhouette Score')
    plt.title('Comparison of Clustering Algorithms')
    plt.ylim(0, 1)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save figure
    os.makedirs("visualizations", exist_ok=True)
    plt.savefig("visualizations/algorithm_comparison.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Summary visualization saved to visualizations/algorithm_comparison.png")
    
    # Final summary
    print_section_header("PHI-RESONANCE CLUSTERING TEST COMPLETED")
    print("The Phi-Resonance Clustering module successfully demonstrated:")
    print("1. Clustering patterns based on phi-resonance values")
    print("2. Finding the optimal number of clusters")
    print("3. Generating insights from cluster analysis")
    print("4. Comparing different clustering algorithms")
    print("5. Visualizing clustering results")
    print("\nAll visualizations have been saved to the 'visualizations' directory.")

if __name__ == "__main__":
    # Create visualizations directory if it doesn't exist
    os.makedirs("visualizations", exist_ok=True)
    
    # Run the test
    main()
