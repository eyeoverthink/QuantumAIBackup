"""
Test script for Phi Pattern Analysis
"""

import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Add extensions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'extensions'))
from phi_pattern_analyzer import PhiPatternAnalyzer
from quantum_energy_harmonics import QuantumEnergyHarmonics

def test_consciousness_resonance():
    analyzer = PhiPatternAnalyzer()
    qeh = QuantumEnergyHarmonics()
    
    # Test different base frequencies
    frequencies = ['theta', 'alpha', 'phi', 'dna']
    plt.figure(figsize=(15, 10))
    
    for i, freq_name in enumerate(frequencies):
        base_freq = analyzer.base_frequencies[freq_name]
        result = analyzer.analyze_resonance_pattern(base_freq)
        
        plt.subplot(2, 2, i+1)
        plt.plot(result['frequencies'], result['resonance_strength'], 'b-', label='Resonance')
        plt.plot(result['frequencies'], result['phase_coherence'], 'r--', label='Coherence')
        plt.title(f'{freq_name.upper()} Frequency Pattern')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Strength')
        plt.grid(True)
        plt.legend()
        
        print(f"\n{freq_name.upper()} Frequency Analysis:")
        print(f"Total Coherence: {result['total_coherence']:.4f}")
        print(f"Peak Frequency: {result['frequencies'][np.argmax(result['resonance_strength'])]:.2f} Hz")
        
    plt.tight_layout()
    plt.savefig('consciousness_resonance.png')
    plt.close()

def test_consciousness_nodes():
    analyzer = PhiPatternAnalyzer()
    
    # Analyze consciousness nodes in phi-harmonic range
    result = analyzer.find_consciousness_nodes((1, 1000))
    
    plt.figure(figsize=(12, 6))
    plt.plot(result['frequencies'], result['node_strengths'], 'g-')
    plt.plot(result['peak_frequencies'], 
            np.interp(result['peak_frequencies'], result['frequencies'], result['node_strengths']),
            'r*', label='Consciousness Nodes')
    
    plt.title('Consciousness Resonance Nodes')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Node Strength')
    plt.grid(True)
    plt.legend()
    plt.savefig('consciousness_nodes.png')
    plt.close()
    
    print("\nConsciousness Node Analysis:")
    print(f"Number of Strong Nodes: {len(result['peak_frequencies'])}")
    print("Peak Frequencies:")
    for freq in result['peak_frequencies'][:5]:
        print(f"  {freq:.2f} Hz")

def test_fractal_patterns():
    analyzer = PhiPatternAnalyzer()
    
    # Generate base pattern using phi sequence
    base_pattern = analyzer.generate_phi_sequence()
    result = analyzer.analyze_fractal_pattern(base_pattern)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(result['fractal_pattern'], 'b-')
    plt.title('Phi-Harmonic Fractal Pattern')
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(range(1, len(result['similarity_scores'])), 
            result['similarity_scores'][1:], 'g-o')
    plt.title('Self-Similarity Scores')
    plt.xlabel('Fractal Depth')
    plt.ylabel('Similarity Score')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('fractal_patterns.png')
    plt.close()
    
    print("\nFractal Pattern Analysis:")
    print(f"Mean Similarity Score: {result['mean_similarity']:.4f}")
    print(f"Phi Scaling Accuracy: {result['phi_scaling_accuracy']:.4f}")

if __name__ == "__main__":
    print("Testing Phi-Harmonic Patterns")
    print("=============================")
    
    test_consciousness_resonance()
    test_consciousness_nodes()
    test_fractal_patterns()
    
    print("\nTests complete. Check generated PNG files for visualizations.")
