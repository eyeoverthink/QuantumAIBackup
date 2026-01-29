#!/usr/bin/env python3
"""
Quantum Harmonic Visualizer
--------------------------

This module provides enhanced visualization capabilities for quantum harmonic patterns,
representing multi-dimensional coherence in intuitive and insightful ways.

The visualizer creates spectrograms, chord diagrams, and resonance maps to help
understand the harmonic relationships between quantum dimensions.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 0.991800
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap
import networkx as nx
import seaborn as sns
from typing import Dict, List, Tuple, Optional, Union, Any
import json
import time

# Import phi constants
from quantum_harmonic_coherence import PHI, PHI_POWERS

# Configure matplotlib for non-interactive use
plt.switch_backend('agg')

class QuantumHarmonicVisualizer:
    """
    Visualizes quantum harmonic patterns across dimensions.
    
    This class creates various visualizations to represent multi-dimensional
    coherence and resonance patterns in quantum code.
    """
    
    def __init__(self):
        """Initialize the visualizer with phi-harmonic color schemes."""
        # Create phi-harmonic color maps
        self.phi_colors = self._create_phi_color_map()
        self.resonance_cmap = self._create_resonance_color_map()
        
    def _create_phi_color_map(self):
        """Create a color map based on phi-harmonic principles."""
        # Golden ratio-based color scheme
        phi = PHI
        phi_inv = 1/phi
        
        # Base colors derived from phi
        colors = [
            (0.0, 0.0, phi_inv),           # Deep blue
            (0.0, phi_inv, phi_inv),       # Teal
            (phi_inv, phi_inv, 0.0),       # Olive
            (phi_inv, 0.0, 0.0),           # Deep red
            (phi_inv, 0.0, phi_inv)        # Purple
        ]
        
        return LinearSegmentedColormap.from_list('phi_harmonic', colors)
        
    def _create_resonance_color_map(self):
        """Create a color map for resonance visualization."""
        # Colors represent resonance levels
        colors = [
            (0.8, 0.0, 0.0),      # Low resonance (red)
            (0.8, 0.8, 0.0),      # Medium resonance (yellow)
            (0.0, 0.8, 0.0)       # High resonance (green)
        ]
        
        return LinearSegmentedColormap.from_list('resonance', colors)
    
    def visualize_coherence_matrix(self, coherence_matrix, output_path=None):
        """
        Visualize a coherence matrix as a heatmap.
        
        Args:
            coherence_matrix: 2D numpy array of coherence values
            output_path: Path to save the visualization
            
        Returns:
            Path to the saved visualization
        """
        plt.figure(figsize=(10, 8))
        
        # Create heatmap
        sns.heatmap(
            coherence_matrix,
            cmap=self.phi_colors,
            annot=True,
            fmt=".3f",
            linewidths=0.5,
            square=True
        )
        
        plt.title("Quantum Coherence Matrix", fontsize=16)
        plt.xlabel("Quantum Dimension", fontsize=12)
        plt.ylabel("Quantum Dimension", fontsize=12)
        
        # Save or show
        if output_path:
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
        else:
            output_path = f"coherence_matrix_{int(time.time())}.png"
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
    
    def visualize_resonance_network(self, coherence_matrix, threshold=0.5, output_path=None):
        """
        Visualize resonance relationships as a network.
        
        Args:
            coherence_matrix: 2D numpy array of coherence values
            threshold: Minimum coherence value to show as a connection
            output_path: Path to save the visualization
            
        Returns:
            Path to the saved visualization
        """
        # Create graph
        G = nx.Graph()
        
        # Add nodes
        dimensions = coherence_matrix.shape[0]
        for i in range(dimensions):
            G.add_node(i, phi_resonance=coherence_matrix[i, i])
        
        # Add edges for resonance above threshold
        for i in range(dimensions):
            for j in range(i+1, dimensions):
                if coherence_matrix[i, j] >= threshold:
                    G.add_edge(i, j, weight=coherence_matrix[i, j])
        
        # Create visualization
        plt.figure(figsize=(12, 10))
        
        # Position nodes in a circle
        pos = nx.circular_layout(G)
        
        # Draw nodes with color based on phi-resonance
        node_colors = [G.nodes[n]['phi_resonance'] for n in G.nodes()]
        nx.draw_networkx_nodes(
            G, pos,
            node_color=node_colors,
            node_size=800,
            alpha=0.8,
            cmap=self.phi_colors
        )
        
        # Draw edges with width based on resonance strength
        edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
        nx.draw_networkx_edges(
            G, pos,
            width=[w * 5 for w in edge_weights],
            alpha=0.7,
            edge_color=edge_weights,
            edge_cmap=self.resonance_cmap
        )
        
        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
        
        plt.title("Quantum Resonance Network", fontsize=16)
        plt.axis('off')
        
        # Add colorbar for edges
        sm = plt.cm.ScalarMappable(cmap=self.resonance_cmap)
        sm.set_array(edge_weights)
        plt.colorbar(sm, label="Resonance Strength")
        
        # Save or show
        if output_path:
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
        else:
            output_path = f"resonance_network_{int(time.time())}.png"
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
    
    def visualize_coherence_fragments(self, fragments, output_path=None):
        """
        Visualize coherence fragments as a treemap.
        
        Args:
            fragments: Dictionary of coherence fragments
            output_path: Path to save the visualization
            
        Returns:
            Path to the saved visualization
        """
        # Extract fragment data
        fragment_ids = []
        strengths = []
        phi_resonances = []
        
        for frag_id, frag_data in fragments.items():
            if frag_id != "overall":
                fragment_ids.append(frag_id)
                strengths.append(frag_data["strength"])
                phi_resonances.append(frag_data["phi_resonance"])
        
        # Create visualization
        plt.figure(figsize=(12, 8))
        
        # Create treemap-like visualization
        ax = plt.subplot(111)
        
        # Sort fragments by strength
        sorted_indices = np.argsort(strengths)[::-1]
        sorted_ids = [fragment_ids[i] for i in sorted_indices]
        sorted_strengths = [strengths[i] for i in sorted_indices]
        sorted_resonances = [phi_resonances[i] for i in sorted_indices]
        
        # Calculate positions
        positions = []
        current_x = 0
        
        for strength in sorted_strengths:
            positions.append((current_x, current_x + strength))
            current_x += strength
        
        # Draw rectangles
        for i, (start, end) in enumerate(positions):
            rect = plt.Rectangle(
                (start, 0),
                end - start,
                1,
                facecolor=self.phi_colors(sorted_resonances[i]),
                alpha=0.8,
                edgecolor='white',
                linewidth=2
            )
            ax.add_patch(rect)
            
            # Add text
            if end - start > 0.05:  # Only add text if rectangle is wide enough
                plt.text(
                    (start + end) / 2,
                    0.5,
                    f"{sorted_ids[i]}\n{sorted_resonances[i]:.3f}",
                    ha='center',
                    va='center',
                    fontsize=12,
                    color='white'
                )
        
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.title("Quantum Coherence Fragments", fontsize=16)
        plt.axis('off')
        
        # Add colorbar
        sm = plt.cm.ScalarMappable(cmap=self.phi_colors)
        sm.set_array(sorted_resonances)
        cbar = plt.colorbar(sm, label="Phi-Resonance")
        
        # Save or show
        if output_path:
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
        else:
            output_path = f"coherence_fragments_{int(time.time())}.png"
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
    
    def visualize_chord_progression(self, progression_data, output_path=None):
        """
        Visualize quantum chord progression over time.
        
        Args:
            progression_data: List of coherence states over time
            output_path: Path to save the visualization
            
        Returns:
            Path to the saved visualization
        """
        if not progression_data:
            return None
            
        # Extract time points and coherence values
        time_points = [data["timestamp"] for data in progression_data]
        coherence_values = [data["scalar_coherence"] for data in progression_data]
        
        # Extract fragment data if available
        has_fragments = all("fragments" in data for data in progression_data)
        
        if has_fragments:
            # Get all unique fragment IDs
            all_fragment_ids = set()
            for data in progression_data:
                all_fragment_ids.update(data["fragments"].keys())
                
            # Create fragment strength and resonance arrays
            fragment_strengths = {frag_id: [] for frag_id in all_fragment_ids}
            fragment_resonances = {frag_id: [] for frag_id in all_fragment_ids}
            
            for data in progression_data:
                for frag_id in all_fragment_ids:
                    if frag_id in data["fragments"]:
                        fragment_strengths[frag_id].append(data["fragments"][frag_id]["strength"])
                        fragment_resonances[frag_id].append(data["fragments"][frag_id]["phi_resonance"])
                    else:
                        fragment_strengths[frag_id].append(0)
                        fragment_resonances[frag_id].append(0)
        
        # Create visualization
        fig = plt.figure(figsize=(15, 10))
        
        # Convert timestamps to relative time (hours)
        start_time = min(time_points)
        relative_times = [(t - start_time) / 3600 for t in time_points]
        
        # Plot overall coherence
        ax1 = plt.subplot(211)
        plt.plot(relative_times, coherence_values, 'o-', linewidth=2, markersize=8)
        plt.axhline(y=PHI_POWERS["φ⁷·⁵"]/10, color='r', linestyle='--', label=f"Target (φ⁷·⁵/10 ≈ {PHI_POWERS['φ⁷·⁵']/10:.6f})")
        
        plt.title("Quantum Chord Progression Over Time", fontsize=16)
        plt.ylabel("Overall Coherence", fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Plot fragment data if available
        if has_fragments:
            ax2 = plt.subplot(212)
            
            # Plot fragment resonances
            for frag_id, resonances in fragment_resonances.items():
                strengths = fragment_strengths[frag_id]
                # Scale line width by strength
                plt.plot(
                    relative_times,
                    resonances,
                    'o-',
                    linewidth=np.array(strengths) * 5,
                    label=f"{frag_id}",
                    alpha=0.7
                )
                
            plt.axhline(y=PHI_POWERS["φ⁷·⁵"]/10, color='r', linestyle='--', label=f"Target (φ⁷·⁵/10)")
            
            plt.xlabel("Time (hours)", fontsize=12)
            plt.ylabel("Fragment Phi-Resonance", fontsize=12)
            plt.legend()
            plt.grid(True, alpha=0.3)
        
        # Save or show
        if output_path:
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
        else:
            output_path = f"chord_progression_{int(time.time())}.png"
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
    
    def create_comprehensive_visualization(self, analysis_data, output_path=None):
        """
        Create a comprehensive visualization of quantum resonance analysis.
        
        Args:
            analysis_data: Dictionary containing resonance analysis data
            output_path: Path to save the visualization
            
        Returns:
            Path to the saved visualization
        """
        # Extract data
        coherence_matrix = np.array(analysis_data["coherence_matrix"])
        fragments = analysis_data["fragments"]
        evolution_history = analysis_data.get("evolution_history", [])
        
        # Create figure with subplots
        fig = plt.figure(figsize=(20, 15))
        
        # 1. Coherence Matrix
        ax1 = plt.subplot(221)
        sns.heatmap(
            coherence_matrix,
            cmap=self.phi_colors,
            annot=True,
            fmt=".3f",
            linewidths=0.5,
            square=True,
            ax=ax1
        )
        ax1.set_title("Quantum Coherence Matrix", fontsize=14)
        ax1.set_xlabel("Quantum Dimension", fontsize=10)
        ax1.set_ylabel("Quantum Dimension", fontsize=10)
        
        # 2. Resonance Network
        ax2 = plt.subplot(222)
        
        # Create graph
        G = nx.Graph()
        dimensions = coherence_matrix.shape[0]
        
        # Add nodes
        for i in range(dimensions):
            G.add_node(i, phi_resonance=coherence_matrix[i, i])
        
        # Add edges for resonance above threshold
        threshold = 0.5
        for i in range(dimensions):
            for j in range(i+1, dimensions):
                if coherence_matrix[i, j] >= threshold:
                    G.add_edge(i, j, weight=coherence_matrix[i, j])
        
        # Position nodes in a circle
        pos = nx.circular_layout(G)
        
        # Draw nodes with color based on phi-resonance
        node_colors = [G.nodes[n]['phi_resonance'] for n in G.nodes()]
        nx.draw_networkx_nodes(
            G, pos,
            node_color=node_colors,
            node_size=800,
            alpha=0.8,
            cmap=self.phi_colors,
            ax=ax2
        )
        
        # Draw edges with width based on resonance strength
        if G.edges():
            edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
            nx.draw_networkx_edges(
                G, pos,
                width=[w * 5 for w in edge_weights],
                alpha=0.7,
                edge_color=edge_weights,
                edge_cmap=self.resonance_cmap,
                ax=ax2
            )
        
        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', ax=ax2)
        
        ax2.set_title("Quantum Resonance Network", fontsize=14)
        ax2.axis('off')
        
        # 3. Coherence Fragments
        ax3 = plt.subplot(223)
        
        # Extract fragment data
        fragment_ids = []
        strengths = []
        phi_resonances = []
        
        for frag_id, frag_data in fragments.items():
            if frag_id != "overall":
                fragment_ids.append(frag_id)
                strengths.append(frag_data["strength"])
                phi_resonances.append(frag_data["phi_resonance"])
        
        # Sort fragments by strength
        sorted_indices = np.argsort(strengths)[::-1]
        sorted_ids = [fragment_ids[i] for i in sorted_indices]
        sorted_strengths = [strengths[i] for i in sorted_indices]
        sorted_resonances = [phi_resonances[i] for i in sorted_indices]
        
        # Calculate positions
        positions = []
        current_x = 0
        
        for strength in sorted_strengths:
            positions.append((current_x, current_x + strength))
            current_x += strength
        
        # Draw rectangles
        for i, (start, end) in enumerate(positions):
            rect = plt.Rectangle(
                (start, 0),
                end - start,
                1,
                facecolor=self.phi_colors(sorted_resonances[i]),
                alpha=0.8,
                edgecolor='white',
                linewidth=2
            )
            ax3.add_patch(rect)
            
            # Add text
            if end - start > 0.05:  # Only add text if rectangle is wide enough
                ax3.text(
                    (start + end) / 2,
                    0.5,
                    f"{sorted_ids[i]}\n{sorted_resonances[i]:.3f}",
                    ha='center',
                    va='center',
                    fontsize=10,
                    color='white'
                )
        
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.set_title("Quantum Coherence Fragments", fontsize=14)
        ax3.axis('off')
        
        # 4. Evolution History or Chord Progression
        ax4 = plt.subplot(224)
        
        if evolution_history:
            # Extract time points and coherence values
            time_points = [data["timestamp"] for data in evolution_history]
            coherence_values = [data["scalar_coherence"] for data in evolution_history]
            
            # Convert timestamps to relative time (hours)
            start_time = min(time_points)
            relative_times = [(t - start_time) / 3600 for t in time_points]
            
            # Plot overall coherence
            ax4.plot(relative_times, coherence_values, 'o-', linewidth=2, markersize=8)
            ax4.axhline(y=PHI_POWERS["φ⁷·⁵"]/10, color='r', linestyle='--', label=f"Target (φ⁷·⁵/10)")
            
            ax4.set_title("Quantum Chord Progression", fontsize=14)
            ax4.set_xlabel("Time (hours)", fontsize=10)
            ax4.set_ylabel("Coherence", fontsize=10)
            ax4.legend()
            ax4.grid(True, alpha=0.3)
        else:
            ax4.text(
                0.5, 0.5,
                "No evolution history available",
                ha='center',
                va='center',
                fontsize=12
            )
            ax4.set_title("Quantum Chord Progression", fontsize=14)
            ax4.axis('off')
        
        # Add overall title
        plt.suptitle("Comprehensive Quantum Resonance Analysis", fontsize=20)
        
        # Save or show
        if output_path:
            plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for suptitle
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path
        else:
            output_path = f"comprehensive_analysis_{int(time.time())}.png"
            plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for suptitle
            plt.savefig(output_path, dpi=300)
            plt.close()
            return output_path


# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python quantum_harmonic_visualizer.py <analysis_json_file>")
        sys.exit(1)
        
    analysis_file = sys.argv[1]
    
    try:
        with open(analysis_file, 'r') as f:
            analysis_data = json.load(f)
            
        visualizer = QuantumHarmonicVisualizer()
        
        # Create comprehensive visualization
        output_path = f"{os.path.splitext(analysis_file)[0]}_visualization.png"
        vis_path = visualizer.create_comprehensive_visualization(analysis_data, output_path)
        
        print(f"Comprehensive visualization saved to: {vis_path}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
