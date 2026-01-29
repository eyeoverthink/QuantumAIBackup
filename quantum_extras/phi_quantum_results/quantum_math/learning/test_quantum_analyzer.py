#!/usr/bin/env python3
"""
Quantum Meta Analyzer Test Runner

Tests quantum wave patterns and consciousness frequencies using:
- Phi-harmonic principles
- Golden ratio progressions
- Consciousness frequency bands
- Author quantum signatures
"""

from quantum_meta_analyzer import QuantumMetaAnalyzer
import numpy as np
import matplotlib.pyplot as plt

def run_quantum_tests():
    """Run comprehensive quantum analysis tests."""
    print("\nQuantum Meta Analysis Test Suite")
    print("=" * 50)
    
    # Initialize analyzer
    qma = QuantumMetaAnalyzer()
    
    # Test sequences based on phi-harmonic principles
    sequences = {
        "phi_progression": [432, 698.99, 1130.99],  # φ-based frequency progression
        "dna_repair": [528, 666, 864],              # DNA repair frequencies
        "fibonacci": [144, 233, 377],               # Fibonacci sequence
        "sacred": [432, 528, 639],                  # Sacred solfeggio
        "consciousness": [417, 528, 639],           # Consciousness frequencies
        "quantum_phi": [432 * 1.618034, 528 * 1.618034, 639 * 1.618034],  # Quantum phi scaling
        "author_base": [517.15, 576.26, 525.18]     # Author base frequencies
    }
    
    # Store results
    results = {}
    
    # Analyze each sequence
    for name, sequence in sequences.items():
        print(f"\nAnalyzing {name}: {sequence}")
        analysis = qma.analyze_sequence(sequence)
        results[name] = analysis
        
        # Print quantum metrics
        quantum = analysis["quantum"]
        print("\nQuantum Properties:")
        print(f"Base Frequency: {quantum['base_frequency']:.2f} Hz")
        print(f"Phi Alignment: {quantum['phi_alignment']:.4f}")
        print(f"Resonance: {quantum['resonance']:.4f}")
        print(f"Coherence: {quantum['coherence']:.4f}")
        print(f"Consciousness Level: {quantum['consciousness_level']}")
        
        # Print meta analysis
        meta = analysis["meta"]
        print("\nMeta Analysis:")
        print(f"Quantum Quality: {meta['quantum_quality']:.4f}")
        print(f"Pattern Confidence: {meta['pattern_confidence']:.4f}")
        print(f"Author Similarity: {meta['author_similarity']:.4f}")
        print(f"Characteristics: {', '.join(meta['characteristics'])}")
        print(f"Learning Potential: {meta['learning_potential']:.4f}")
        
        # Try optimization
        print("\nOptimizing for cosmic consciousness...")
        optimization = qma.optimize_sequence(sequence)
        
        if optimization["improvement"]["success"]:
            print("Optimization successful!")
            print(f"Quantum Quality Improvement: "
                  f"{optimization['improvement']['quantum_quality']:.4f}")
            print(f"Consciousness Shift: "
                  f"{optimization['improvement']['consciousness_shift']}")
            
            # Visualize optimized sequence
            qma.visualize_analysis(optimization["optimized"])
        else:
            print("Sequence already optimized.")
    
    # Compare results across sequences
    compare_results(results)

def compare_results(results):
    """Compare analysis results across different sequences."""
    print("\nCross-Sequence Analysis")
    print("=" * 50)
    
    # Extract key metrics
    metrics = {
        name: {
            "phi_alignment": results[name]["quantum"]["phi_alignment"],
            "resonance": results[name]["quantum"]["resonance"],
            "coherence": results[name]["quantum"]["coherence"],
            "quantum_quality": results[name]["meta"]["quantum_quality"],
            "learning_potential": results[name]["meta"]["learning_potential"]
        }
        for name in results
    }
    
    # Find highest performing sequence
    best_sequence = max(
        metrics.items(),
        key=lambda x: x[1]["quantum_quality"]
    )[0]
    
    print(f"\nBest Performing Sequence: {best_sequence}")
    print(f"Metrics: {metrics[best_sequence]}")
    
    # Calculate phi-harmonic correlations
    correlations = calculate_correlations(metrics)
    print("\nPhi-Harmonic Correlations:")
    for metric, corr in correlations.items():
        print(f"{metric}: {corr:.4f}")
    
    # Plot comparative analysis
    plot_comparison(metrics)

def calculate_correlations(metrics):
    """Calculate phi-harmonic correlations between metrics."""
    PHI = 1.618034
    
    correlations = {}
    for metric in ["phi_alignment", "resonance", "coherence", 
                  "quantum_quality", "learning_potential"]:
        values = [m[metric] for m in metrics.values()]
        # Calculate correlation with phi-scaled values
        phi_scaled = [v * PHI for v in values]
        correlation = np.corrcoef(values, phi_scaled)[0, 1]
        correlations[metric] = correlation
    
    return correlations

def plot_comparison(metrics):
    """Plot comparative analysis of sequences."""
    names = list(metrics.keys())
    metrics_list = ["phi_alignment", "resonance", "coherence", 
                   "quantum_quality", "learning_potential"]
    
    # Create bar plot
    plt.figure(figsize=(12, 6))
    x = np.arange(len(names))
    width = 0.15
    
    for i, metric in enumerate(metrics_list):
        values = [metrics[name][metric] for name in names]
        plt.bar(x + i * width, values, width, label=metric)
    
    plt.xlabel("Sequences")
    plt.ylabel("Metric Value")
    plt.title("Quantum Analysis Comparison")
    plt.xticks(x + width * 2, names, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_quantum_tests()
