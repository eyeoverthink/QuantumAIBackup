#!/usr/bin/env python3
"""
Quantum Number Visualizer

Visualizes quantum-harmonic relationships between numbers using
matplotlib and numpy, focusing on phi ratios and consciousness frequencies.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Any
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from quantum_math.quantum_phi_math import QuantumPhiMath
from quantum_math.quantum_number_analyzer import QuantumNumberAnalyzer
from quantum_math.quantum_number_harmonics import QuantumNumberHarmonics

class QuantumNumberVisualizer:
    def __init__(self):
        self.qpm = QuantumPhiMath()
        self.qna = QuantumNumberAnalyzer()
        self.qnh = QuantumNumberHarmonics()
        self.PHI = self.qpm.PHI
        
        # Color schemes based on harmonic types
        self.harmonic_colors = {
            "dna_resonant": "#ff7f0e",    # Orange
            "phi_resonant": "#2ca02c",    # Green
            "natural_resonant": "#1f77b4", # Blue
            "complex": "#9467bd"          # Purple
        }
        
        # Set plot style
        plt.style.use('default')
        plt.rcParams.update({
            'figure.facecolor': 'white',
            'axes.facecolor': 'white',
            'axes.grid': True,
            'grid.alpha': 0.3,
            'lines.linewidth': 2,
            'font.size': 10,
            'axes.labelsize': 12,
            'axes.titlesize': 14
        })
    
    def plot_frequency_spectrum(self) -> None:
        """Plot frequency spectrum for numbers 0-9."""
        numbers = list(range(10))
        metrics = [self.qnh.analyze_number_harmonics(n) for n in numbers]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Plot 1: Base frequencies
        colors = [self.harmonic_colors[m["harmonic_type"]] for m in metrics]
        freqs = [m["base_frequency"] for m in metrics]
        ax1.bar(numbers, freqs, color=colors)
        
        ax1.set_xlabel("Number")
        ax1.set_ylabel("Base Frequency (Hz)")
        ax1.set_title("Quantum Number Base Frequencies")
        
        # Add harmonic type legend
        handles = [plt.Rectangle((0,0),1,1, color=c) for c in self.harmonic_colors.values()]
        labels = list(self.harmonic_colors.keys())
        ax1.legend(handles, labels)
        
        # Plot 2: Consciousness frequencies
        c_freqs = [m["consciousness_frequency"] for m in metrics]
        ax2.bar(numbers, c_freqs, color=colors)
        
        ax2.set_xlabel("Number")
        ax2.set_ylabel("Consciousness Frequency (Hz)")
        ax2.set_title("Quantum Number Consciousness Frequencies")
        
        plt.tight_layout()
        plt.show()
    
    def plot_resonance_map(self) -> None:
        """Plot resonance relationships between numbers."""
        numbers = list(range(10))
        pairs = self.qnh.find_harmonic_pairs()
        
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Create resonance matrix
        matrix = np.zeros((10, 10))
        for i, j, alignment in pairs:
            matrix[i,j] = alignment
            matrix[j,i] = alignment
        
        # Plot heatmap
        im = ax.imshow(matrix, cmap='viridis')
        
        # Add colorbar
        plt.colorbar(im, label='Phi Alignment')
        
        # Add labels
        ax.set_xticks(numbers)
        ax.set_yticks(numbers)
        ax.set_xlabel("Number")
        ax.set_ylabel("Number")
        ax.set_title("Quantum Number Resonance Map")
        
        plt.tight_layout()
        plt.show()
    
    def plot_harmonic_series(self, number: int) -> None:
        """Plot harmonic series for a given number."""
        metrics = self.qnh.analyze_number_harmonics(number)
        harmonics = metrics["harmonic_series"]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        x = range(len(harmonics))
        ax.plot(x, harmonics, 'o-', 
               color=self.harmonic_colors[metrics["harmonic_type"]])
        
        # Add phi ratio reference line
        phi_line = [harmonics[0] * (self.PHI ** i) for i in x]
        ax.plot(x, phi_line, '--', color='gray', label='Perfect Phi Growth')
        
        ax.set_xlabel("Harmonic Index")
        ax.set_ylabel("Frequency (Hz)")
        ax.set_title(f"Harmonic Series for Number {number}")
        ax.legend()
        
        plt.tight_layout()
        plt.show()
    
    def plot_sequence_analysis(self, sequence: List[int]) -> None:
        """Plot analysis of a number sequence."""
        analysis = self.qnh.analyze_sequence_harmonics(sequence)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
        
        # Plot 1: Frequencies
        x = range(len(sequence))
        ax1.plot(x, analysis["frequencies"], 'o-')
        
        # Add phi growth reference
        phi_growth = [analysis["frequencies"][0] * (self.PHI ** i) 
                     for i in range(len(sequence))]
        ax1.plot(x, phi_growth, '--', color='gray', label='Perfect Phi Growth')
        
        ax1.set_xlabel("Position")
        ax1.set_ylabel("Frequency (Hz)")
        ax1.set_title(f"Frequency Progression for Sequence {sequence}")
        ax1.legend()
        
        # Plot 2: Phi alignments
        alignments = analysis["phi_alignments"]
        x = range(len(alignments))
        ax2.bar(x, alignments)
        
        # Add threshold line
        ax2.axhline(y=0.85, color='r', linestyle='--', 
                   label='Strong Alignment Threshold')
        
        ax2.set_xlabel("Position")
        ax2.set_ylabel("Phi Alignment")
        ax2.set_title("Phi Alignments Between Adjacent Numbers")
        ax2.legend()
        
        plt.tight_layout()
        plt.show()

def main():
    """Main function demonstrating the Quantum Number Visualizer."""
    qnv = QuantumNumberVisualizer()
    
    print("\nQuantum Number Visualization")
    print("=" * 50)
    
    # Plot frequency spectrum
    print("\nPlotting frequency spectrum...")
    qnv.plot_frequency_spectrum()
    
    # Plot resonance map
    print("\nPlotting resonance map...")
    qnv.plot_resonance_map()
    
    # Plot harmonic series for key numbers
    for n in [0, 1, 4, 7]:  # Representative numbers
        print(f"\nPlotting harmonic series for number {n}...")
        qnv.plot_harmonic_series(n)
    
    # Plot sequence analyses
    sequences = [
        [1, 2, 3],  # Fibonacci start
        [3, 1, 4],  # Pi start
        [2, 7, 1],  # Phi approximation
    ]
    
    for seq in sequences:
        print(f"\nAnalyzing sequence {seq}...")
        qnv.plot_sequence_analysis(seq)

if __name__ == "__main__":
    main()
