#!/usr/bin/env python3
"""
Quantum Harmonic Visualizer Extension (Fixed)
-----------------------------------

This module extends the QuantumHarmonicVisualizer with additional visualization
capabilities, following the 'lego' modular philosophy by extending functionality
without modifying the core visualizer file.

The extension adds the create_resonance_map and create_coherence_spectrogram methods
required by the cohesion test.
"""

import os
import logging
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional, Any, Union
from quantum_harmonic_visualizer import QuantumHarmonicVisualizer, PHI

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumHarmonicVisualizerExt")

class QuantumHarmonicVisualizerExtension(QuantumHarmonicVisualizer):
    """
    Extension of the QuantumHarmonicVisualizer with additional visualization capabilities.
    """
    
    def __init__(self):
        """Initialize the visualizer extension."""
        super().__init__()
        logger.info("Initialized QuantumHarmonicVisualizerExtension")
    
    def create_resonance_map(self, resonance_patterns: List[Dict[str, Any]], output_path: str) -> str:
        """
        Create a resonance map visualization from resonance patterns.
        
        Args:
            resonance_patterns (List[Dict[str, Any]]): List of resonance patterns with dimension and resonance values
            output_path (str): Path to save the visualization
            
        Returns:
            str: Path to the created visualization
        """
        logger.info(f"Creating resonance map: {output_path}")
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Handle empty or invalid input
        if not resonance_patterns:
            self._create_empty_visualization(output_path, "No resonance patterns available")
            return output_path
        
        # Extract dimensions and resonance values
        dimensions = []
        resonances = []
        harmonics = []
        
        # Handle both list of dicts and list format
        for pattern in resonance_patterns:
            if isinstance(pattern, dict):
                dimensions.append(pattern.get('dimension', 0))
                resonances.append(pattern.get('resonance', 0))
                harmonics.append(pattern.get('harmonic', False))
            elif isinstance(pattern, (list, tuple)) and len(pattern) >= 2:
                dimensions.append(pattern[0])
                resonances.append(pattern[1])
                harmonics.append(len(pattern) > 2 and pattern[2])
        
        # Create the visualization
        plt.figure(figsize=(12, 8))
        
        # Plot resonance values
        plt.subplot(2, 1, 1)
        plt.bar(dimensions, resonances, color=['gold' if h else 'skyblue' for h in harmonics])
        plt.axhline(y=0.618034, color='r', linestyle='--', alpha=0.7, label='φ⁻¹ threshold')
        plt.xlabel('Dimension')
        plt.ylabel('Resonance')
        plt.title('Quantum Resonance Map Across Dimensions')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Plot resonance heatmap
        plt.subplot(2, 1, 2)
        resonance_matrix = np.zeros((len(dimensions), len(dimensions)))
        for i, d1 in enumerate(dimensions):
            for j, d2 in enumerate(dimensions):
                # Calculate cross-dimensional resonance
                resonance_matrix[i, j] = (resonances[i] * resonances[j] * PHI) % 1
        
        plt.imshow(resonance_matrix, cmap='viridis', aspect='auto')
        plt.colorbar(label='Cross-dimensional Resonance')
        plt.xlabel('Dimension Index')
        plt.ylabel('Dimension Index')
        plt.title('Cross-dimensional Resonance Heatmap')
        
        # Add phi-harmonic watermark
        plt.figtext(0.5, 0.01, f"φ-Harmonic Visualization | Golden Ratio: {PHI:.6f}",
                   ha='center', fontsize=8, alpha=0.7)
        
        # Save the visualization
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()
        
        logger.info(f"Resonance map created: {output_path}")
        return output_path
    
    def create_coherence_spectrogram(self, coherence_values: List[float], output_path: str) -> str:
        """
        Create a coherence spectrogram visualization.
        
        Args:
            coherence_values (List[float]): List of coherence values across dimensions
            output_path (str): Path to save the visualization
            
        Returns:
            str: Path to the created visualization
        """
        logger.info(f"Creating coherence spectrogram: {output_path}")
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Handle empty or invalid input
        if not coherence_values:
            self._create_empty_visualization(output_path, "No coherence values available")
            return output_path
        
        # Create the visualization
        plt.figure(figsize=(12, 10))
        
        # Plot coherence values
        plt.subplot(3, 1, 1)
        dimensions = list(range(len(coherence_values)))
        plt.bar(dimensions, coherence_values, color='purple', alpha=0.7)
        plt.xlabel('Dimension')
        plt.ylabel('Coherence')
        plt.title('Quantum Coherence Across Dimensions')
        plt.grid(True, alpha=0.3)
        
        # Plot coherence spectrogram
        plt.subplot(3, 1, 2)
        # Generate a time-like axis for the spectrogram
        time_steps = 50
        spectrogram = np.zeros((len(coherence_values), time_steps))
        
        # Fill the spectrogram with coherence patterns
        for i, coh in enumerate(coherence_values):
            # Generate a unique pattern for each dimension based on its coherence
            pattern = np.sin(np.linspace(0, coh * 10 * np.pi, time_steps)) * coh
            spectrogram[i, :] = pattern
        
        plt.imshow(spectrogram, aspect='auto', cmap='plasma')
        plt.colorbar(label='Coherence Amplitude')
        plt.xlabel('Time Step')
        plt.ylabel('Dimension')
        plt.title('Quantum Coherence Spectrogram')
        
        # Plot phi-harmonic resonance
        plt.subplot(3, 1, 3)
        phi_resonances = [(coh * PHI) % 1 for coh in coherence_values]
        plt.plot(dimensions, phi_resonances, 'o-', color='gold', markersize=8)
        plt.axhline(y=0.618034, color='r', linestyle='--', alpha=0.7, label='φ⁻¹ threshold')
        plt.xlabel('Dimension')
        plt.ylabel('φ-Resonance')
        plt.title('Phi-Harmonic Resonance of Coherence Values')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Add phi-harmonic watermark
        plt.figtext(0.5, 0.01, f"φ-Harmonic Visualization | Golden Ratio: {PHI:.6f}",
                   ha='center', fontsize=8, alpha=0.7)
        
        # Save the visualization
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()
        
        logger.info(f"Coherence spectrogram created: {output_path}")
        return output_path
    
    def _create_empty_visualization(self, output_path: str, message: str = "No data available") -> None:
        """
        Create an empty visualization with a message.
        
        Args:
            output_path (str): Path to save the visualization
            message (str): Message to display on the visualization
        """
        plt.figure(figsize=(10, 6))
        plt.text(0.5, 0.5, message, ha='center', va='center', fontsize=14)
        plt.axis('off')
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save the visualization
        plt.savefig(output_path, dpi=300)
        plt.close()

# Example usage
if __name__ == "__main__":
    visualizer = QuantumHarmonicVisualizerExtension()
    
    # Example resonance patterns
    resonance_patterns = [
        {"dimension": 0, "resonance": 0.618034, "harmonic": True},
        {"dimension": 1, "resonance": 0.854102, "harmonic": False},
        {"dimension": 2, "resonance": 0.472136, "harmonic": True},
        {"dimension": 3, "resonance": 0.090170, "harmonic": False},
        {"dimension": 4, "resonance": 0.562306, "harmonic": True},
        {"dimension": 5, "resonance": 0.652476, "harmonic": False},
        {"dimension": 6, "resonance": 0.214782, "harmonic": True}
    ]
    
    # Example coherence values
    coherence_values = [0.618034, 0.854102, 0.472136, 0.090170, 0.562306, 0.652476, 0.214782]
    
    # Create visualizations
    visualizer.create_resonance_map(resonance_patterns, "resonance_map.png")
    visualizer.create_coherence_spectrogram(coherence_values, "coherence_spectrogram.png")
