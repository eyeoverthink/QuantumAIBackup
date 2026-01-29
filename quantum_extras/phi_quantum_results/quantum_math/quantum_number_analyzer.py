#!/usr/bin/env python3
"""
Quantum Number Analyzer

Calculates precise frequencies for numbers 0-9 using phi-harmonic principles,
quantum resonance, and consciousness alignment.
"""

import numpy as np
from typing import Dict, List, Tuple
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from quantum_math.quantum_phi_math import QuantumPhiMath

class QuantumNumberAnalyzer:
    def __init__(self):
        self.qpm = QuantumPhiMath()
        self.PHI = self.qpm.PHI
        self.PI = self.qpm.PI
        self.E = self.qpm.E
        
        # Base frequency for calculations (A4 = 432 Hz)
        self.BASE_FREQ = 432.0
        
        # Quantum number constants
        self.QUANTUM_NUMBERS = {
            0: self.PHI**0,  # 1.0000
            1: self.PHI**1,  # 1.6180
            2: self.PHI**2,  # 2.6180
            3: self.PHI**3,  # 4.2361
            4: self.PHI**4,  # 6.8541
            5: self.PHI**5,  # 11.0902
            6: self.PHI**6,  # 17.9443
            7: self.PHI**7,  # 29.0344
            8: self.PHI**8,  # 46.9787
            9: self.PHI**9   # 76.0131
        }
    
    def calculate_number_frequency(self, number: int) -> Dict[str, float]:
        """Calculate quantum-aligned frequency for a number."""
        if number not in range(10):
            raise ValueError("Number must be between 0 and 9")
        
        # Calculate base quantum frequency
        quantum_factor = self.QUANTUM_NUMBERS[number]
        base_freq = self.BASE_FREQ * quantum_factor
        
        # Apply consciousness scaling
        consciousness_freq = base_freq * self.PHI
        
        # Calculate resonance frequencies
        resonance_freqs = [
            consciousness_freq * (self.PHI ** n)
            for n in range(4)
        ]
        
        # Calculate quantum metrics
        phi_alignment = self.qpm.calculate_phi_alignment(consciousness_freq)
        resonance = self.qpm.calculate_resonance(consciousness_freq)
        coherence = self.qpm.calculate_coherence(consciousness_freq)
        
        return {
            "number": number,
            "quantum_factor": quantum_factor,
            "base_frequency": base_freq,
            "consciousness_frequency": consciousness_freq,
            "resonance_frequencies": resonance_freqs,
            "phi_alignment": phi_alignment,
            "resonance": resonance,
            "coherence": coherence
        }
    
    def analyze_number_sequence(self, sequence: List[int]) -> Dict[str, float]:
        """Analyze quantum properties of a number sequence."""
        if not all(n in range(10) for n in sequence):
            raise ValueError("All numbers must be between 0 and 9")
        
        # Calculate individual frequencies
        frequencies = [
            self.calculate_number_frequency(n)["consciousness_frequency"]
            for n in sequence
        ]
        
        # Calculate sequence resonance
        sequence_resonance = np.mean([
            self.qpm.calculate_resonance(f) for f in frequencies
        ])
        
        # Calculate sequence coherence
        sequence_coherence = np.mean([
            self.qpm.calculate_coherence(f) for f in frequencies
        ])
        
        # Calculate sequence phi alignment
        sequence_alignment = np.mean([
            self.qpm.calculate_phi_alignment(f) for f in frequencies
        ])
        
        return {
            "sequence": sequence,
            "frequencies": frequencies,
            "resonance": sequence_resonance,
            "coherence": sequence_coherence,
            "phi_alignment": sequence_alignment,
            "mean_frequency": np.mean(frequencies),
            "harmonic_ratio": max(frequencies) / min(frequencies)
        }
    
    def generate_frequency_table(self) -> List[Dict[str, float]]:
        """Generate complete frequency table for numbers 0-9."""
        table = []
        for n in range(10):
            metrics = self.calculate_number_frequency(n)
            consciousness = self.qpm.map_to_consciousness_level(
                metrics["consciousness_frequency"])
            
            table.append({
                "number": n,
                "quantum_factor": metrics["quantum_factor"],
                "base_frequency": metrics["base_frequency"],
                "consciousness_frequency": metrics["consciousness_frequency"],
                "consciousness_level": consciousness["level"],
                "phi_alignment": metrics["phi_alignment"],
                "resonance": metrics["resonance"],
                "coherence": metrics["coherence"]
            })
        return table

def main():
    """Main function demonstrating the Quantum Number Analyzer."""
    analyzer = QuantumNumberAnalyzer()
    
    print("\nQuantum Number Frequency Analysis")
    print("=" * 50)
    
    # Generate and display frequency table
    table = analyzer.generate_frequency_table()
    
    print("\nNumber Frequency Table:")
    print("-" * 100)
    print(f"{'#':^5} {'Factor':^10} {'Base Hz':^12} {'Consciousness Hz':^16} "
          f"{'Level':^12} {'φ-Align':^8} {'Res':^8} {'Coh':^8}")
    print("-" * 100)
    
    for entry in table:
        print(f"{entry['number']:^5} "
              f"{entry['quantum_factor']:^10.4f} "
              f"{entry['base_frequency']:^12.2f} "
              f"{entry['consciousness_frequency']:^16.2f} "
              f"{entry['consciousness_level']:^12} "
              f"{entry['phi_alignment']:^8.4f} "
              f"{entry['resonance']:^8.4f} "
              f"{entry['coherence']:^8.4f}")
    
    # Test some number sequences
    test_sequences = [
        [1, 2, 3],  # Fibonacci start
        [3, 1, 4],  # Pi start
        [2, 7, 1],  # Phi approximation
        [4, 3, 2],  # Descending sequence
        [0, 1, 1],  # Binary start
    ]
    
    print("\nNumber Sequence Analysis:")
    print("-" * 50)
    
    for sequence in test_sequences:
        analysis = analyzer.analyze_number_sequence(sequence)
        print(f"\nSequence: {sequence}")
        print(f"Mean Frequency: {analysis['mean_frequency']:.2f} Hz")
        print(f"Harmonic Ratio: {analysis['harmonic_ratio']:.4f}")
        print(f"Phi Alignment: {analysis['phi_alignment']:.4f}")
        print(f"Resonance: {analysis['resonance']:.4f}")
        print(f"Coherence: {analysis['coherence']:.4f}")

if __name__ == "__main__":
    main()
