#!/usr/bin/env python
"""
Test script for Quantum Phi-Harmonic Frequency Processor
======================================================

This script tests the frequency analysis capabilities of our quantum
phi-harmonic system using resonant frequencies and quantum modulation.
"""

from quantum_phi_core import QuantumPhiCore
from quantum_phi_frequency_processor import QuantumPhiFrequencyProcessor
import numpy as np

def test_frequency_patterns():
    """Test quantum phi-harmonic frequency patterns."""
    print("\n" + "="*70)
    print("Quantum Phi-Harmonic Frequency Analysis")
    print("="*70 + "\n")
    
    # Initialize processors
    core = QuantumPhiCore()
    processor = QuantumPhiFrequencyProcessor(core=core)
    
    # Test phrases with phi-harmonic properties
    test_phrases = [
        "Quantum resonance flows through golden spirals",
        "Harmonic waves dance in sacred geometry",
        "Neural patterns emerge from cosmic rhythms",
        "Fibonacci sequences align with natural growth",
        "Consciousness vibrates at quantum frequencies",
        "Universal harmonies create coherent fields"
    ]
    
    print("Frequency Pattern Analysis")
    print("-"*50 + "\n")
    
    all_metrics = []
    for phrase in test_phrases:
        print(f"\nAnalyzing: '{phrase}'")
        
        # Analyze frequency patterns
        metrics = processor.analyze_frequency_pattern(phrase)
        all_metrics.append(metrics)
        
        print(f"Resonance: {metrics['resonance']:.4f}")
        print(f"Subharmonic: {metrics['subharmonic']:.4f}")
        print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
        print(f"Coherence: {metrics['coherence']:.4f}")
        print(f"Harmony: {metrics['harmony']:.4f}")
        print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
        print(f"Average Frequency: {metrics['average_frequency']:.4f} Hz")
        
        # Generate and analyze harmonic sequence
        sequence = processor.generate_harmonic_sequence(phrase)
        if sequence:
            avg_harmonic = sum(sequence) / len(sequence)
            std_harmonic = np.std(sequence)
            print(f"Harmonic Average: {avg_harmonic:.4f} Hz")
            print(f"Harmonic Deviation: {std_harmonic:.4f} Hz")
        
        # Find resonant pairs
        pairs = processor.find_resonant_pairs(phrase)
        if pairs:
            print("\nResonant Letter Pairs:")
            for c1, c2, res in pairs[:3]:  # Show top 3 pairs
                print(f"  {c1}-{c2}: {res:.4f}")
    
    print("\n" + "="*50)
    print("System-Wide Metrics")
    print("="*50 + "\n")
    
    # Calculate average metrics
    avg_metrics = {
        key: sum(m[key] for m in all_metrics) / len(all_metrics)
        for key in all_metrics[0].keys()
    }
    
    print(f"Average Resonance: {avg_metrics['resonance']:.4f}")
    print(f"Average Subharmonic: {avg_metrics['subharmonic']:.4f}")
    print(f"Average Quantum Resonance: {avg_metrics['quantum_resonance']:.4f}")
    print(f"Average Coherence: {avg_metrics['coherence']:.4f}")
    print(f"Average Harmony: {avg_metrics['harmony']:.4f}")
    print(f"Average Phi Alignment: {avg_metrics['phi_alignment']:.4f}")
    print(f"System Frequency: {avg_metrics['average_frequency']:.4f} Hz")
    
    print("\n" + "="*50)
    print("Frequency Band Analysis")
    print("="*50 + "\n")
    
    # Analyze frequency bands
    bands = processor.frequency_bands
    for name, freq in bands.items():
        print(f"{name}: {freq:.4f} Hz")
    
    print("\n" + "="*50)
    print("Processor Metrics")
    print("="*50 + "\n")
    
    # Get processor metrics
    metrics = processor.get_metrics()
    print(f"Base Frequency: {metrics['base_frequency']:.4f} Hz")
    print(f"Phi Ratio: {metrics['phi_ratio']:.4f}")
    print(f"Frequency Range: {metrics['frequency_range']:.4f} Hz")
    print(f"Average Ratio: {metrics['average_ratio']:.4f}")
    
    print("\n" + "="*50)
    print("Test Complete")
    print("="*50 + "\n")

if __name__ == "__main__":
    test_frequency_patterns()
