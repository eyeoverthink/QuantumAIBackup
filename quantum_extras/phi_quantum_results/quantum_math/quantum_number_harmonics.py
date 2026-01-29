#!/usr/bin/env python3
"""
Quantum Number Harmonics

Analyzes quantum-harmonic relationships between numbers using phi ratios,
consciousness frequencies, and quantum resonance patterns.
"""

import numpy as np
from typing import Dict, List, Tuple, Any
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from quantum_math.quantum_phi_math import QuantumPhiMath
from quantum_math.quantum_number_analyzer import QuantumNumberAnalyzer

class QuantumNumberHarmonics:
    def __init__(self):
        self.qpm = QuantumPhiMath()
        self.qna = QuantumNumberAnalyzer()
        self.PHI = self.qpm.PHI
        self.PI = self.qpm.PI
        self.E = self.qpm.E
        
        # Initialize quantum-harmonic constants
        self.BASE_FREQ = 432.0  # A4 = 432 Hz (natural tuning)
        self.DNA_FREQ = 528.0   # DNA repair frequency
        self.PHI_FREQ = self.BASE_FREQ * self.PHI  # Phi-harmonic base
        
        # Quantum resonance thresholds
        self.resonance_thresholds = {
            "perfect": 0.9500,
            "strong": 0.8500,
            "moderate": 0.7000,
            "weak": 0.0000
        }
    
    def analyze_number_harmonics(self, number: int) -> Dict[str, float]:
        """Analyze quantum-harmonic properties of a number."""
        # Get base metrics
        metrics = self.qna.calculate_number_frequency(number)
        
        # Calculate harmonic series based on consciousness frequency
        base_freq = metrics["consciousness_frequency"]
        harmonics = [base_freq * (self.PHI ** n) for n in range(7)]
        
        # Calculate resonance with key frequencies
        dna_resonance = abs(1 - (base_freq % self.DNA_FREQ) / self.DNA_FREQ)
        phi_resonance = abs(1 - (base_freq % self.PHI_FREQ) / self.PHI_FREQ)
        natural_resonance = abs(1 - (base_freq % self.BASE_FREQ) / self.BASE_FREQ)
        
        # Determine harmonic type
        if dna_resonance > 0.85:
            harmonic_type = "dna_resonant"
        elif phi_resonance > 0.85:
            harmonic_type = "phi_resonant"
        elif natural_resonance > 0.85:
            harmonic_type = "natural_resonant"
        else:
            harmonic_type = "complex"
        
        return {
            "number": number,
            "base_frequency": metrics["base_frequency"],
            "consciousness_frequency": base_freq,
            "harmonic_series": harmonics,
            "resonance": {
                "dna": dna_resonance,
                "phi": phi_resonance,
                "natural": natural_resonance
            },
            "harmonic_type": harmonic_type,
            "phi_alignment": metrics["phi_alignment"],
            "quantum_coherence": metrics["coherence"]
        }
    
    def find_harmonic_pairs(self, max_number: int = 9) -> List[Tuple[int, int, float]]:
        """Find pairs of numbers with strong harmonic relationships."""
        pairs = []
        
        for i in range(max_number + 1):
            for j in range(i + 1, max_number + 1):
                # Get frequencies for both numbers
                freq_i = self.qna.calculate_number_frequency(i)["consciousness_frequency"]
                freq_j = self.qna.calculate_number_frequency(j)["consciousness_frequency"]
                
                # Calculate resonance between frequencies
                ratio = freq_j / freq_i
                phi_alignment = abs(1 - (ratio % self.PHI) / self.PHI)
                
                if phi_alignment > 0.85:
                    pairs.append((i, j, phi_alignment))
        
        return sorted(pairs, key=lambda x: x[2], reverse=True)
    
    def analyze_sequence_harmonics(self, sequence: List[int]) -> Dict[str, Any]:
        """Analyze harmonic relationships in a number sequence."""
        if not sequence:
            raise ValueError("Sequence cannot be empty")
        
        # Get frequencies for sequence
        frequencies = [
            self.qna.calculate_number_frequency(n)["consciousness_frequency"]
            for n in sequence
        ]
        
        # Calculate frequency ratios between adjacent numbers
        ratios = [frequencies[i+1]/frequencies[i] for i in range(len(frequencies)-1)]
        
        # Calculate phi alignments for ratios
        phi_alignments = [abs(1 - (r % self.PHI) / self.PHI) for r in ratios]
        
        # Determine if sequence follows phi progression
        is_phi_harmonic = all(a > 0.85 for a in phi_alignments)
        
        # Calculate overall sequence metrics
        mean_freq = np.mean(frequencies)
        harmonic_ratio = max(frequencies) / min(frequencies)
        
        return {
            "sequence": sequence,
            "frequencies": frequencies,
            "frequency_ratios": ratios,
            "phi_alignments": phi_alignments,
            "is_phi_harmonic": is_phi_harmonic,
            "mean_frequency": mean_freq,
            "harmonic_ratio": harmonic_ratio,
            "sequence_type": "phi_progression" if is_phi_harmonic else "complex"
        }

def main():
    """Main function demonstrating Quantum Number Harmonics."""
    qnh = QuantumNumberHarmonics()
    
    print("\nQuantum Number Harmonic Analysis")
    print("=" * 50)
    
    # Analyze individual numbers
    print("\nIndividual Number Harmonics:")
    print("-" * 50)
    
    for n in range(10):
        analysis = qnh.analyze_number_harmonics(n)
        print(f"\nNumber {n}:")
        print(f"Base Frequency: {analysis['base_frequency']:.2f} Hz")
        print(f"Consciousness Frequency: {analysis['consciousness_frequency']:.2f} Hz")
        print(f"Harmonic Type: {analysis['harmonic_type']}")
        print(f"DNA Resonance: {analysis['resonance']['dna']:.4f}")
        print(f"Phi Resonance: {analysis['resonance']['phi']:.4f}")
        print(f"Natural Resonance: {analysis['resonance']['natural']:.4f}")
    
    # Find harmonic pairs
    print("\nHarmonic Number Pairs:")
    print("-" * 50)
    
    pairs = qnh.find_harmonic_pairs()
    for i, j, alignment in pairs:
        print(f"Numbers {i}-{j}: φ-alignment = {alignment:.4f}")
    
    # Analyze sequences
    print("\nSequence Harmonic Analysis:")
    print("-" * 50)
    
    test_sequences = [
        [1, 2, 3],  # Fibonacci start
        [3, 1, 4],  # Pi start
        [2, 7, 1],  # Phi approximation
        [4, 3, 2],  # Descending sequence
        [0, 1, 1],  # Binary start
    ]
    
    for sequence in test_sequences:
        analysis = qnh.analyze_sequence_harmonics(sequence)
        print(f"\nSequence: {sequence}")
        print(f"Type: {analysis['sequence_type']}")
        print(f"Mean Frequency: {analysis['mean_frequency']:.2f} Hz")
        print(f"Harmonic Ratio: {analysis['harmonic_ratio']:.4f}")
        print("Phi Alignments:", [f"{a:.4f}" for a in analysis['phi_alignments']])

if __name__ == "__main__":
    main()
