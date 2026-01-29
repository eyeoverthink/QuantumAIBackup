#!/usr/bin/env python3
"""
Quantum Harmonic Visualizer Extension
-----------------------------------

This module extends the QuantumHarmonicVisualizer with additional visualization methods
required by the cohesion test, following the 'lego' modular philosophy by extending
functionality without modifying the core visualizer file.

The extension adds the create_resonance_map method required by the cohesion test.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import logging
from typing import Dict, List, Tuple, Optional, Any, Union
import json
from quantum_harmonic_visualizer import QuantumHarmonicVisualizer, PHI, PHI_POWERS

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumHarmonicVisualizerExt")

class QuantumHarmonicVisualizerExtension(QuantumHarmonicVisualizer):
    """
    Extension of the QuantumHarmonicVisualizer with additional visualization methods.
    """
    
    def __init__(self):
        """Initialize the visualizer extension."""
        super().__init__()
        logger.info("Initialized QuantumHarmonicVisualizerExtension")
    
    def create_resonance_map(self, 
                           resonance_data: Dict[str, Any], 
                           output_path: Optional[str] = None,
                           title: str = "Quantum Resonance Map") -> str:
        """
        Create a resonance map visualization showing how different parts of the code
        resonate with phi-harmonic frequencies across dimensions.
        
        Args:
            resonance_data (Dict[str, Any]): Resonance data containing:
                - fragments: List of phi-harmonic fragments with resonance values
                - dimensions: Number of dimensions analyzed
                - overall_resonance: Overall resonance value
            output_path (str, optional): Path to save the visualization.
                                       If None, generates a path based on title
            title (str): Title for the visualization
            
        Returns:
            str: Path to the saved visualization file
        """
        # Generate default output path if not provided
        if output_path is None:
            os.makedirs('visualizations', exist_ok=True)
            timestamp = int(time.time())
            safe_title = title.replace(" ", "_").lower()
            output_path = f"visualizations/resonance_map_{safe_title}_{timestamp}.png"
        
        logger.info(f"Creating resonance map: {output_path}")
        
        # Extract data
        fragments = resonance_data.get('fragments', [])
        dimensions = resonance_data.get('dimensions', 7)
        overall_resonance = resonance_data.get('overall_resonance', 0.0)
        
        if not fragments:
            logger.warning("No fragments provided for resonance map")
            # Create a simple placeholder visualization
            plt.figure(figsize=(10, 6))
            plt.text(0.5, 0.5, "No resonance data available", 
                    ha='center', va='center', fontsize=16)
            plt.title(f"{title}\nOverall Resonance: {overall_resonance:.6f}")
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
        
        # Create the figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # 1. Create heatmap of resonance across dimensions for each fragment
        fragment_labels = [f"F{i+1}" for i in range(len(fragments))]
        dimension_labels = [f"D{i+1}" for i in range(dimensions)]
        
        # Extract dimensional resonance data (or generate placeholder if not available)
        resonance_matrix = np.zeros((len(fragments), dimensions))
        for i, fragment in enumerate(fragments):
            dim_resonance = fragment.get('dimensional_resonance', [])
            if dim_resonance and len(dim_resonance) == dimensions:
                resonance_matrix[i, :] = dim_resonance
            else:
                # Generate placeholder data based on overall fragment resonance
                base_resonance = fragment.get('resonance', 0.5)
                # Create variation across dimensions using phi
                resonance_matrix[i, :] = [
                    min(1.0, base_resonance * (1 + 0.2 * np.sin(PHI * d)))
                    for d in range(dimensions)
                ]
        
        # Create heatmap
        sns.heatmap(resonance_matrix, ax=ax1, cmap=self.resonance_cmap, 
                   xticklabels=dimension_labels, yticklabels=fragment_labels,
                   vmin=0, vmax=1, annot=True, fmt=".2f", cbar_kws={'label': 'Resonance'})
        ax1.set_title("Fragment Resonance Across Dimensions")
        ax1.set_xlabel("Quantum Dimensions")
        ax1.set_ylabel("Code Fragments")
        
        # 2. Create network graph showing relationships between fragments
        G = nx.Graph()
        
        # Add nodes for each fragment
        for i, fragment in enumerate(fragments):
            resonance = fragment.get('resonance', 0.0)
            G.add_node(i, resonance=resonance, label=f"F{i+1}")
        
        # Add edges between fragments that have resonance relationships
        for i in range(len(fragments)):
            for j in range(i+1, len(fragments)):
                # Calculate resonance relationship as product of individual resonances
                # adjusted by phi to create harmonic relationships
                res_i = fragments[i].get('resonance', 0.0)
                res_j = fragments[j].get('resonance', 0.0)
                relationship = res_i * res_j * (1 + 0.2 * np.sin(PHI * (i+j)))
                
                # Only add edges for significant relationships
                if relationship > 0.3:
                    G.add_edge(i, j, weight=relationship)
        
        # Position nodes using spring layout
        pos = nx.spring_layout(G, seed=42)
        
        # Get resonance values for node colors
        node_resonances = [G.nodes[n]['resonance'] for n in G.nodes()]
        
        # Draw the network
        nx.draw_networkx_nodes(G, pos, ax=ax2, node_size=500,
                              node_color=node_resonances, cmap=self.resonance_cmap,
                              vmin=0, vmax=1)
        
        # Draw edges with width proportional to weight
        edge_weights = [G[u][v]['weight'] * 3 for u, v in G.edges()]
        nx.draw_networkx_edges(G, pos, ax=ax2, width=edge_weights, alpha=0.7)
        
        # Add labels
        nx.draw_networkx_labels(G, pos, ax=ax2, 
                               labels={n: G.nodes[n]['label'] for n in G.nodes()})
        
        ax2.set_title("Fragment Resonance Network")
        ax2.axis('off')
        
        # Add overall title and phi-harmonic information
        fig.suptitle(f"{title}\nOverall Resonance: {overall_resonance:.6f}", fontsize=16)
        
        # Add phi-harmonic watermark
        fig.text(0.5, 0.02, f"φ = {PHI:.6f} | φ² = {PHI_POWERS[2]:.6f} | φ³ = {PHI_POWERS[3]:.6f}",
                ha='center', fontsize=10, alpha=0.7)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig(output_path, dpi=300)
        plt.close()
        
        logger.info(f"Resonance map created and saved to {output_path}")
        return output_path
    
    def visualize_file_resonance(self, file_path: str, output_dir: Optional[str] = None) -> Dict[str, Any]:
        """
        Analyze and visualize the resonance patterns in a Python file.
        
        Args:
            file_path (str): Path to the Python file to analyze
            output_dir (str, optional): Directory to save visualizations.
                                      If None, creates a 'visualizations' directory
        
        Returns:
            Dict[str, Any]: Results including:
                - resonance_data: Resonance analysis data
                - visualization_paths: Paths to created visualizations
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Create output directory if not specified
        if output_dir is None:
            output_dir = "visualizations"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate base name for output files
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        logger.info(f"Analyzing resonance in file: {file_path}")
        
        # Read file content
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Analyze the file using the quantum resonance optimizer
        # We'll import it here to avoid circular imports
        from quantum_resonance_optimizer_extension import QuantumResonanceOptimizerExtension
        optimizer = QuantumResonanceOptimizerExtension()
        resonance_data = optimizer.analyze_code_resonance(content)
        
        # Create visualizations
        visualization_paths = {}
        
        # 1. Resonance Map
        map_path = os.path.join(output_dir, f"{base_name}_resonance_map.png")
        visualization_paths['resonance_map'] = self.create_resonance_map(
            resonance_data, 
            output_path=map_path,
            title=f"Resonance Map: {base_name}"
        )
        
        # 2. Chord Diagram (if available in parent class)
        if hasattr(self, 'create_chord_diagram'):
            chord_path = os.path.join(output_dir, f"{base_name}_chord_diagram.png")
            visualization_paths['chord_diagram'] = self.create_chord_diagram(
                resonance_data,
                output_path=chord_path,
                title=f"Chord Diagram: {base_name}"
            )
        
        # 3. Spectrogram (if available in parent class)
        if hasattr(self, 'create_resonance_spectrogram'):
            spec_path = os.path.join(output_dir, f"{base_name}_spectrogram.png")
            visualization_paths['spectrogram'] = self.create_resonance_spectrogram(
                resonance_data,
                output_path=spec_path,
                title=f"Resonance Spectrogram: {base_name}"
            )
        
        # Save the resonance data
        data_path = os.path.join(output_dir, f"{base_name}_resonance_data.json")
        with open(data_path, 'w') as f:
            json.dump(resonance_data, f, indent=2)
        
        logger.info(f"Visualization complete. Created {len(visualization_paths)} visualizations")
        
        return {
            "resonance_data": resonance_data,
            "visualization_paths": visualization_paths,
            "data_path": data_path
        }

# Example usage
if __name__ == "__main__":
    import sys
    visualizer = QuantumHarmonicVisualizerExtension()
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        visualizer.visualize_file_resonance(file_path)
    else:
        print("Usage: python quantum_harmonic_visualizer_extension.py <file_path>")
