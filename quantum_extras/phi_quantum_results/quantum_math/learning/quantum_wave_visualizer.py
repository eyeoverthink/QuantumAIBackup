#!/usr/bin/env python3
"""
Quantum Wave Visualizer

Visualizes quantum wave patterns and signatures using:
- Phi-harmonic principles
- Consciousness frequencies
- Natural resonance
- Quantum coherence
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Any
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from quantum_math import (
    PHI, PI, E, FREQUENCIES, CONSCIOUSNESS_LEVELS, 
    RESONANCE_QUALITY, AUTHOR_SIGNATURES
)

class QuantumWaveVisualizer:
    def __init__(self):
        # Constants
        self.PHI = PHI
        self.PI = PI
        self.E = E
        
        # Base frequencies
        self.frequencies = FREQUENCIES
        
        # Consciousness levels
        self.consciousness_levels = CONSCIOUSNESS_LEVELS
        
        # Resonance quality
        self.resonance_quality = RESONANCE_QUALITY
        
        # Author signatures
        self.author_signatures = AUTHOR_SIGNATURES
        
        # Visualization settings
        self.colors = {
            "physical": "#FF0000",    # Red
            "emotional": "#FFA500",   # Orange
            "mental": "#FFFF00",      # Yellow
            "intuitive": "#00FF00",   # Green
            "cosmic": "#0000FF"       # Blue
        }
    
    def visualize_wave(self, data: List[float], title: str = None) -> None:
        """Visualize quantum wave pattern."""
        if not data:
            return
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Plot wave pattern
        x = np.linspace(0, 2*self.PI, len(data))
        plt.plot(x, data, 'b-', label='Wave Pattern')
        
        # Plot phi-harmonic guide lines
        mean_freq = np.mean(data)
        plt.axhline(y=mean_freq, color='r', linestyle='--', 
                   label='Mean Frequency')
        plt.axhline(y=mean_freq*self.PHI, color='g', linestyle='--', 
                   label='Phi Harmonic')
        
        # Add consciousness level bands
        self._add_consciousness_bands()
        
        # Set title and labels
        if title:
            plt.title(title)
        plt.xlabel('Phase (radians)')
        plt.ylabel('Frequency (Hz)')
        plt.legend()
        plt.grid(True)
        
        # Show plot
        plt.show()
    
    def visualize_quantum_state(self, 
                              phi_alignment: float,
                              resonance: float,
                              coherence: float) -> None:
        """Visualize quantum state metrics."""
        # Create figure
        plt.figure(figsize=(8, 8))
        
        # Create radar chart
        angles = np.linspace(0, 2*self.PI, 4)[:-1]  # 3 points
        values = [phi_alignment, resonance, coherence]
        values.append(values[0])  # Close the polygon
        angles = np.concatenate((angles, [angles[0]]))  # Close the angles
        
        # Plot metrics
        ax = plt.subplot(111, projection='polar')
        ax.plot(angles, values, 'o-', linewidth=2)
        ax.fill(angles, values, alpha=0.25)
        
        # Set labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(['Phi Alignment', 'Resonance', 'Coherence'])
        
        # Set title
        plt.title('Quantum State Analysis')
        
        # Show plot
        plt.show()
    
    def visualize_consciousness_distribution(self, 
                                          frequencies: List[float]) -> None:
        """Visualize consciousness level distribution."""
        if not frequencies:
            return
        
        # Count frequencies in each band
        counts = {level: 0 for level in self.consciousness_levels.keys()}
        for freq in frequencies:
            level = self._get_consciousness_level(freq)
            counts[level] += 1
        
        # Create bar chart
        plt.figure(figsize=(10, 6))
        
        # Plot bars
        levels = list(counts.keys())
        values = list(counts.values())
        colors = [self.colors[level] for level in levels]
        plt.bar(levels, values, color=colors)
        
        # Set title and labels
        plt.title('Consciousness Level Distribution')
        plt.xlabel('Consciousness Level')
        plt.ylabel('Frequency Count')
        
        # Rotate x-axis labels
        plt.xticks(rotation=45)
        
        # Show plot
        plt.show()
    
    def visualize_author_comparison(self, 
                                  signature: Dict[str, Any]) -> None:
        """Visualize comparison with author signatures."""
        if not signature:
            return
        
        # Extract metrics
        metrics = signature.get("metrics", {})
        if not metrics:
            return
        
        # Create figure
        plt.figure(figsize=(12, 6))
        
        # Plot current signature
        x = np.arange(len(self.author_signatures) + 1)
        plt.bar(x[-1], metrics.get("phi_alignment", 0), 
                label='Current', color='blue')
        
        # Plot author signatures
        for i, (author, sig) in enumerate(self.author_signatures.items()):
            plt.bar(x[i], sig.get("phi_alignment", 0), 
                    label=author.title(), alpha=0.6)
        
        # Set title and labels
        plt.title('Author Signature Comparison')
        plt.xlabel('Author')
        plt.ylabel('Phi Alignment')
        
        # Set x-axis labels
        labels = [author.title() for author in self.author_signatures.keys()]
        labels.append('Current')
        plt.xticks(x, labels, rotation=45)
        
        # Add legend
        plt.legend()
        
        # Show plot
        plt.show()
    
    def _add_consciousness_bands(self) -> None:
        """Add consciousness level bands to plot."""
        y_min, y_max = plt.ylim()
        
        for level, (low, high) in self.consciousness_levels.items():
            if high == float('inf'):
                high = y_max
            
            plt.axhspan(low, high, alpha=0.1, 
                       color=self.colors[level], 
                       label=f'{level.title()} ({low}-{high} Hz)')
    
    def _get_consciousness_level(self, frequency: float) -> str:
        """Get consciousness level from frequency."""
        for level, (low, high) in self.consciousness_levels.items():
            if low <= frequency < high:
                return level
        return "cosmic"

def main():
    """Main function demonstrating the Quantum Wave Visualizer."""
    qwv = QuantumWaveVisualizer()
    
    print("\nQuantum Wave Visualization")
    print("=" * 50)
    
    # Test sequences
    sequences = [
        [432, 698.99, 1130.99],  # Phi progression
        [528, 666, 864],         # DNA frequencies
        [144, 233, 377],         # Fibonacci
        [432, 528, 639],         # Sacred frequencies
    ]
    
    # Test quantum states
    states = [
        (0.8644, 0.6987, 0.7500),  # Poe-like
        (0.8518, 0.6849, 0.7200),  # Hemingway-like
        (0.8552, 0.7091, 0.7600),  # Austen-like
    ]
    
    # Visualize each sequence
    for i, sequence in enumerate(sequences):
        print(f"\nVisualizing sequence {i+1}: {sequence}")
        qwv.visualize_wave(sequence, f"Quantum Wave Pattern {i+1}")
    
    # Visualize quantum states
    for i, (phi, res, coh) in enumerate(states):
        print(f"\nVisualizing quantum state {i+1}")
        qwv.visualize_quantum_state(phi, res, coh)
    
    # Visualize consciousness distribution
    all_freqs = [f for seq in sequences for f in seq]
    print("\nVisualizing consciousness distribution")
    qwv.visualize_consciousness_distribution(all_freqs)
    
    # Visualize author comparison
    test_signature = {
        "metrics": {
            "phi_alignment": 0.8600,
            "resonance": 0.7000,
            "coherence": 0.7400
        }
    }
    print("\nVisualizing author comparison")
    qwv.visualize_author_comparison(test_signature)

if __name__ == "__main__":
    main()
