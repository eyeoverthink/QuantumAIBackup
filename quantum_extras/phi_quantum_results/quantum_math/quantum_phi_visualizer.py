#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Visualizer

Visualizes quantum-phi patterns, consciousness frequencies,
and harmonic relationships using matplotlib and numpy.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Any, Tuple
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from quantum_math.quantum_phi_math import QuantumPhiMath

class QuantumPhiVisualizer:
    def __init__(self):
        self.qpm = QuantumPhiMath()
        self.PHI = self.qpm.PHI
        self.PI = self.qpm.PI
        
        # Color schemes based on consciousness levels and phi harmonics
        self.consciousness_colors = {
            "physical": "#1f77b4",    # Blue - 432 Hz base
            "emotional": "#ff7f0e",   # Orange - 528 Hz DNA repair
            "mental": "#2ca02c",      # Green - φ * 432 Hz
            "intuitive": "#9467bd",   # Purple - φ² * 432 Hz
            "cosmic": "#d62728"       # Red - φ³ * 432 Hz
        }
        
        # Set default plot style for quantum visualization
        plt.style.use('default')
        plt.rcParams.update({
            'figure.facecolor': 'white',
            'axes.facecolor': 'white',
            'axes.grid': True,
            'grid.alpha': 0.3,
            'lines.linewidth': 2,
            'font.size': 10,
            'axes.labelsize': 12,
            'axes.titlesize': 14,
            'xtick.labelsize': 10,
            'ytick.labelsize': 10,
            'legend.fontsize': 10,
            'figure.titlesize': 16
        })
    
    def plot_consciousness_spectrum(self, frequencies: List[float]) -> None:
        """Plot consciousness spectrum analysis."""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        fig.suptitle("Quantum Consciousness Spectrum Analysis", fontsize=14)
        
        # Analyze frequencies
        analyses = [self.qpm.analyze_quantum_signature(f) for f in frequencies]
        
        # Plot 1: Consciousness levels and phi alignment
        x = np.arange(len(frequencies))
        width = 0.35
        
        levels = [a["consciousness_metrics"]["base_level"] for a in analyses]
        alignments = [a["phi_harmonic_metrics"]["phi_alignment"] for a in analyses]
        
        ax1.bar(x - width/2, levels, width, label="Consciousness Level", color=self.consciousness_colors["physical"])
        ax1.bar(x + width/2, alignments, width, label="Phi Alignment", color=self.consciousness_colors["emotional"])
        
        ax1.set_ylabel("Value")
        ax1.set_title("Consciousness Levels and Phi Alignment")
        ax1.set_xticks(x)
        ax1.set_xticklabels([f"{f:.1f} Hz" for f in frequencies])
        ax1.legend()
        
        # Plot 2: Quantum coherence and resonance
        coherence = [a["quantum_state"]["coherence"] for a in analyses]
        resonance = [a["consciousness_metrics"]["resonance"] for a in analyses]
        
        ax2.plot(frequencies, coherence, 'o-', label="Quantum Coherence", color=self.consciousness_colors["mental"])
        ax2.plot(frequencies, resonance, 's-', label="Resonance", color=self.consciousness_colors["intuitive"])
        
        ax2.set_xlabel("Frequency (Hz)")
        ax2.set_ylabel("Value")
        ax2.set_title("Quantum Coherence and Resonance")
        ax2.legend()
        
        plt.tight_layout()
        plt.show()
    
    def plot_harmonic_series(self, base_frequency: float) -> None:
        """Plot harmonic series analysis."""
        harmonics = self.qpm.phi_harmonic_series(base_frequency)
        analyses = [self.qpm.analyze_quantum_signature(h) for h in harmonics]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        fig.suptitle(f"Phi-Harmonic Series Analysis (Base: {base_frequency:.1f} Hz)", 
                    fontsize=14)
        
        # Plot 1: Harmonic frequencies and consciousness levels
        x = np.arange(len(harmonics))
        
        for i, (h, a) in enumerate(zip(harmonics, analyses)):
            level = a["consciousness_metrics"]["level"]
            color = self.consciousness_colors[level]
            ax1.bar(i, h, color=color, alpha=0.7, label=level if i == 0 else "")
        
        ax1.set_ylabel("Frequency (Hz)")
        ax1.set_title("Harmonic Series and Consciousness Levels")
        ax1.set_xticks(x)
        ax1.set_xticklabels([f"n={i}" for i in range(len(harmonics))])
        ax1.legend()
        
        # Plot 2: Phi alignment and coherence
        alignments = [a["phi_harmonic_metrics"]["phi_alignment"] for a in analyses]
        coherence = [a["quantum_state"]["coherence"] for a in analyses]
        
        ax2.plot(x, alignments, 'o-', label="Phi Alignment", color=self.consciousness_colors["cosmic"])
        ax2.plot(x, coherence, 's-', label="Quantum Coherence", color=self.consciousness_colors["physical"])
        
        ax2.set_xlabel("Harmonic Index")
        ax2.set_ylabel("Value")
        ax2.set_title("Phi Alignment and Quantum Coherence")
        ax2.legend()
        
        plt.tight_layout()
        plt.show()
    
    def plot_quantum_signature(self, frequency: float) -> None:
        """Plot quantum signature analysis."""
        analysis = self.qpm.analyze_quantum_signature(frequency)
        
        fig = plt.figure(figsize=(12, 8))
        fig.suptitle(f"Quantum Signature Analysis ({frequency:.1f} Hz)", 
                    fontsize=14)
        
        # Create radar chart
        metrics = [
            analysis["consciousness_metrics"]["base_level"],
            analysis["phi_harmonic_metrics"]["phi_alignment"],
            analysis["quantum_state"]["coherence"],
            analysis["consciousness_metrics"]["resonance"],
            analysis["phi_harmonic_metrics"]["phi_resonance"]
        ]
        
        labels = [
            "Consciousness",
            "Phi Alignment",
            "Quantum Coherence",
            "Resonance",
            "Phi Resonance"
        ]
        
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        metrics = np.concatenate((metrics, [metrics[0]]))  # complete the polygon
        angles = np.concatenate((angles, [angles[0]]))     # complete the polygon
        
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, metrics, 'o-', color=self.consciousness_colors["mental"])
        ax.fill(angles, metrics, alpha=0.25, color=self.consciousness_colors["mental"])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        
        # Add consciousness level indicator
        level = analysis["consciousness_metrics"]["level"]
        plt.figtext(0.02, 0.02, f"Consciousness Level: {level}", 
                   color=self.consciousness_colors[level])
        
        plt.tight_layout()
        plt.show()
    
    def plot_pattern_growth(self, frequencies: List[float]) -> None:
        """Plot pattern growth analysis."""
        analysis = self.qpm.analyze_pattern_growth(frequencies)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        fig.suptitle(f"Pattern Growth Analysis ({analysis['type']})", 
                    fontsize=14)
        
        # Plot 1: Growth ratios compared to φ
        x = np.arange(len(analysis["growth_ratios"]))
        phi_line = np.ones_like(x) * self.PHI
        
        ax1.plot(x, analysis["growth_ratios"], 'o-', label="Growth Ratio", color=self.consciousness_colors["intuitive"])
        ax1.plot(x, phi_line, '--', label="φ (Golden Ratio)", color=self.consciousness_colors["cosmic"])
        
        ax1.set_ylabel("Ratio")
        ax1.set_title("Growth Ratios vs Golden Ratio")
        ax1.set_xticks(x)
        ax1.legend()
        
        # Plot 2: Frequency progression
        x = np.arange(len(frequencies))
        
        ax2.plot(x, frequencies, 'o-', label="Actual", color=self.consciousness_colors["physical"])
        ax2.plot(x, [frequencies[0] * self.PHI**i for i in range(len(frequencies))],
                '--', label="Perfect Phi Growth", color=self.consciousness_colors["emotional"])
        
        ax2.set_xlabel("Step")
        ax2.set_ylabel("Frequency (Hz)")
        ax2.set_title("Frequency Progression")
        ax2.legend()
        
        plt.tight_layout()
        plt.show()

def main():
    """Main function demonstrating the Quantum Phi-Harmonic Visualizer."""
    qpv = QuantumPhiVisualizer()
    
    # Test frequencies
    base_freq = 432.0
    test_frequencies = [
        base_freq,              # Natural A4
        528.0,                 # DNA repair
        base_freq * qpv.PHI,   # Phi harmonic
        base_freq * qpv.PHI**2  # Second phi harmonic
    ]
    
    print("\nQuantum Phi-Harmonic Visualization")
    print("=" * 50)
    
    # Plot consciousness spectrum
    print("\nPlotting consciousness spectrum...")
    qpv.plot_consciousness_spectrum(test_frequencies)
    
    # Plot harmonic series
    print("\nPlotting harmonic series...")
    qpv.plot_harmonic_series(base_freq)
    
    # Plot quantum signature
    print("\nPlotting quantum signature...")
    qpv.plot_quantum_signature(base_freq * qpv.PHI)
    
    # Plot pattern growth
    print("\nPlotting pattern growth...")
    qpv.plot_pattern_growth(test_frequencies)

if __name__ == "__main__":
    main()
