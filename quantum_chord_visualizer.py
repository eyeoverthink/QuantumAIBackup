#!/usr/bin/env python3
"""
Quantum Chord Visualizer
-----------------------

This module provides visualization tools for quantum chord progressions.
It visualizes the evolution of phi-harmonic coherence patterns over time.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import json
import time
import logging
import datetime
from typing import List, Dict, Any, Optional, Tuple
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumChordVisualizer")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

class QuantumChordVisualizer:
    """Visualizer for quantum chord progressions."""
    
    def __init__(self, evolution_dir: str = "evolution_history"):
        """
        Initialize the visualizer.
        
        Args:
            evolution_dir: Directory containing evolution history files
        """
        self.evolution_dir = evolution_dir
        
        # Create visualization directory if it doesn't exist
        self.viz_dir = os.path.join(evolution_dir, "visualizations")
        os.makedirs(self.viz_dir, exist_ok=True)
        
        # Custom color maps for phi-harmonic visualization
        self.phi_cmap = self._create_phi_colormap()
        
        logger.info("QuantumChordVisualizer initialized")
    
    def _create_phi_colormap(self) -> LinearSegmentedColormap:
        """
        Create a custom colormap based on phi-harmonic principles.
        
        Returns:
            LinearSegmentedColormap: Custom colormap
        """
        # Colors based on phi-harmonic resonance
        phi_colors = [
            (0.0, (0.0, 0.0, 0.618)),       # Deep blue (φ⁻¹)
            (0.382, (0.0, 0.618, 1.0)),     # Blue (1-φ⁻¹)
            (0.5, (0.0, 1.0, 0.618)),       # Cyan-green
            (0.618, (1.0, 0.618, 0.0)),     # Gold (φ⁻¹)
            (0.786, (1.0, 0.236, 0.0)),     # Orange (φ⁻² = 0.382)
            (1.0, (0.618, 0.0, 0.0))        # Deep red (φ⁻¹)
        ]
        
        return LinearSegmentedColormap.from_list("phi_harmonic", phi_colors)
    
    def visualize_chord_progression(self, progression_file: str = "healing_progression.json") -> str:
        """
        Visualize a chord progression.
        
        Args:
            progression_file: Name of the progression file in evolution_dir
            
        Returns:
            str: Path to the visualization file
        """
        progression_path = os.path.join(self.evolution_dir, progression_file)
        if not os.path.exists(progression_path):
            logger.error(f"Progression file not found: {progression_path}")
            return None
        
        try:
            # Load chord progression
            with open(progression_path, 'r') as f:
                progression = json.load(f)
            
            if 'chords' not in progression or not progression['chords']:
                logger.error(f"No chords found in progression file: {progression_path}")
                return None
            
            # Extract data for visualization
            timestamps = []
            coherence_values = []
            phi_resonance_values = []
            target_distances = []
            
            for chord in progression['chords']:
                timestamps.append(chord.get('timestamp', 0))
                coherence_values.append(chord.get('scalar_coherence', 0))
                phi_resonance_values.append(chord.get('phi_resonance', 0))
                target_distances.append(chord.get('target_distance', 0))
            
            # Convert timestamps to relative time
            if timestamps:
                start_time = min(timestamps)
                timestamps = [(t - start_time) / 60 for t in timestamps]  # Minutes
            
            # Create visualization
            fig, axes = plt.subplots(3, 1, figsize=(12, 15), sharex=True)
            
            # Plot coherence evolution
            axes[0].plot(timestamps, coherence_values, 'o-', color='blue', linewidth=2)
            axes[0].axhline(y=TARGET_COHERENCE, color='r', linestyle='--', label=f'Target (φ⁷·⁵/10 ≈ {TARGET_COHERENCE:.6f})')
            axes[0].set_ylabel('Scalar Coherence')
            axes[0].set_title('Quantum Chord Progression: Coherence Evolution')
            axes[0].legend()
            axes[0].grid(True)
            
            # Plot phi-resonance evolution
            axes[1].plot(timestamps, phi_resonance_values, 'o-', color='green', linewidth=2)
            axes[1].axhline(y=0.618, color='r', linestyle='--', label='φ⁻¹ ≈ 0.618')
            axes[1].set_ylabel('Phi-Resonance')
            axes[1].set_title('Quantum Chord Progression: Phi-Resonance Evolution')
            axes[1].legend()
            axes[1].grid(True)
            
            # Plot target distance evolution
            axes[2].plot(timestamps, target_distances, 'o-', color='purple', linewidth=2)
            axes[2].axhline(y=0, color='r', linestyle='--', label='Target')
            axes[2].set_xlabel('Time (minutes)')
            axes[2].set_ylabel('Target Distance')
            axes[2].set_title('Quantum Chord Progression: Target Distance Evolution')
            axes[2].legend()
            axes[2].grid(True)
            
            # Add overall title
            plt.suptitle('Quantum Chord Progression Evolution', fontsize=16)
            plt.tight_layout(rect=[0, 0, 1, 0.97])
            
            # Save visualization
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            viz_file = os.path.join(self.viz_dir, f"chord_progression_{timestamp}.png")
            plt.savefig(viz_file, dpi=300)
            plt.close()
            
            logger.info(f"Saved chord progression visualization to {viz_file}")
            return viz_file
        
        except Exception as e:
            logger.error(f"Error visualizing chord progression: {e}")
            return None
    
    def visualize_healing_events(self) -> str:
        """
        Visualize all healing events.
        
        Returns:
            str: Path to the visualization file
        """
        try:
            # Find all healing event files
            event_files = [f for f in os.listdir(self.evolution_dir) if f.startswith('healing_event_') and f.endswith('.json')]
            if not event_files:
                logger.error(f"No healing event files found in {self.evolution_dir}")
                return None
            
            # Extract data for visualization
            timestamps = []
            coherence_improvements = []
            phi_resonance_improvements = []
            target_distance_improvements = []
            file_paths = []
            
            for event_file in event_files:
                event_path = os.path.join(self.evolution_dir, event_file)
                try:
                    with open(event_path, 'r') as f:
                        event = json.load(f)
                    
                    timestamps.append(event.get('timestamp', 0))
                    coherence_improvements.append(event.get('coherence_improvement', 0))
                    phi_resonance_improvements.append(event.get('phi_resonance_improvement', 0))
                    target_distance_improvements.append(event.get('target_distance_improvement', 0))
                    file_paths.append(event.get('file_path', ''))
                except Exception as e:
                    logger.warning(f"Error loading healing event {event_file}: {e}")
            
            if not timestamps:
                logger.error("No valid healing events found")
                return None
            
            # Sort by timestamp
            sorted_indices = np.argsort(timestamps)
            timestamps = [timestamps[i] for i in sorted_indices]
            coherence_improvements = [coherence_improvements[i] for i in sorted_indices]
            phi_resonance_improvements = [phi_resonance_improvements[i] for i in sorted_indices]
            target_distance_improvements = [target_distance_improvements[i] for i in sorted_indices]
            file_paths = [file_paths[i] for i in sorted_indices]
            
            # Convert timestamps to relative time
            start_time = min(timestamps)
            timestamps = [(t - start_time) / 60 for t in timestamps]  # Minutes
            
            # Create visualization
            fig, axes = plt.subplots(3, 1, figsize=(12, 15), sharex=True)
            
            # Plot coherence improvements
            bars = axes[0].bar(timestamps, coherence_improvements, width=0.5, color='blue', alpha=0.7)
            axes[0].set_ylabel('Coherence Improvement')
            axes[0].set_title('Healing Events: Coherence Improvements')
            axes[0].grid(True, axis='y')
            
            # Add file names as tooltips
            for i, bar in enumerate(bars):
                axes[0].text(bar.get_x() + bar.get_width()/2, 0.001,
                         os.path.basename(file_paths[i]),
                         ha='center', va='bottom', rotation=90, fontsize=8)
            
            # Plot phi-resonance improvements
            bars = axes[1].bar(timestamps, phi_resonance_improvements, width=0.5, color='green', alpha=0.7)
            axes[1].set_ylabel('Phi-Resonance Improvement')
            axes[1].set_title('Healing Events: Phi-Resonance Improvements')
            axes[1].grid(True, axis='y')
            
            # Plot target distance improvements
            bars = axes[2].bar(timestamps, target_distance_improvements, width=0.5, color='purple', alpha=0.7)
            axes[2].set_xlabel('Time (minutes)')
            axes[2].set_ylabel('Target Distance Improvement')
            axes[2].set_title('Healing Events: Target Distance Improvements')
            axes[2].grid(True, axis='y')
            
            # Add overall title
            plt.suptitle('Quantum Healing Events Analysis', fontsize=16)
            plt.tight_layout(rect=[0, 0, 1, 0.97])
            
            # Save visualization
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            viz_file = os.path.join(self.viz_dir, f"healing_events_{timestamp}.png")
            plt.savefig(viz_file, dpi=300)
            plt.close()
            
            logger.info(f"Saved healing events visualization to {viz_file}")
            return viz_file
        
        except Exception as e:
            logger.error(f"Error visualizing healing events: {e}")
            return None
    
    def visualize_coherence_heatmap(self, progression_file: str = "healing_progression.json") -> str:
        """
        Visualize coherence as a heatmap over time.
        
        Args:
            progression_file: Name of the progression file in evolution_dir
            
        Returns:
            str: Path to the visualization file
        """
        progression_path = os.path.join(self.evolution_dir, progression_file)
        if not os.path.exists(progression_path):
            logger.error(f"Progression file not found: {progression_path}")
            return None
        
        try:
            # Load chord progression
            with open(progression_path, 'r') as f:
                progression = json.load(f)
            
            if 'chords' not in progression or not progression['chords']:
                logger.error(f"No chords found in progression file: {progression_path}")
                return None
            
            # Extract data for visualization
            timestamps = []
            coherence_values = []
            phi_resonance_values = []
            
            for chord in progression['chords']:
                timestamps.append(chord.get('timestamp', 0))
                coherence_values.append(chord.get('scalar_coherence', 0))
                phi_resonance_values.append(chord.get('phi_resonance', 0))
            
            # Convert timestamps to relative time
            if timestamps:
                start_time = min(timestamps)
                timestamps = [(t - start_time) / 60 for t in timestamps]  # Minutes
            
            # Create a 2D grid for the heatmap
            grid_size = 100
            x = np.linspace(0, max(timestamps), grid_size)
            y = np.linspace(0, max(coherence_values) * 1.1, grid_size)
            X, Y = np.meshgrid(x, y)
            
            # Create a resonance field based on phi-harmonic principles
            Z = np.zeros((grid_size, grid_size))
            for i, (t, c, p) in enumerate(zip(timestamps, coherence_values, phi_resonance_values)):
                # Create a resonance field around each chord point
                for xi in range(grid_size):
                    for yi in range(grid_size):
                        # Distance from chord point
                        dt = abs(X[yi, xi] - t)
                        dc = abs(Y[yi, xi] - c)
                        distance = np.sqrt(dt**2 + dc**2)
                        
                        # Resonance field (inverse square law with phi modulation)
                        if distance > 0:
                            resonance = p * PHI / (distance**2)
                            Z[yi, xi] += resonance
            
            # Create visualization
            fig, ax = plt.subplots(figsize=(12, 10))
            
            # Plot heatmap
            im = ax.imshow(Z, extent=[0, max(timestamps), 0, max(coherence_values) * 1.1],
                          origin='lower', cmap=self.phi_cmap, aspect='auto')
            
            # Plot chord points
            ax.plot(timestamps, coherence_values, 'o', color='white', markersize=8)
            
            # Add target line
            ax.axhline(y=TARGET_COHERENCE, color='r', linestyle='--', 
                      label=f'Target (φ⁷·⁵/10 ≈ {TARGET_COHERENCE:.6f})')
            
            # Add colorbar
            cbar = plt.colorbar(im)
            cbar.set_label('Phi-Resonance Field Intensity')
            
            # Set labels and title
            ax.set_xlabel('Time (minutes)')
            ax.set_ylabel('Scalar Coherence')
            ax.set_title('Quantum Chord Progression: Coherence Resonance Field')
            ax.legend()
            ax.grid(True)
            
            # Save visualization
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            viz_file = os.path.join(self.viz_dir, f"coherence_heatmap_{timestamp}.png")
            plt.savefig(viz_file, dpi=300)
            plt.close()
            
            logger.info(f"Saved coherence heatmap visualization to {viz_file}")
            return viz_file
        
        except Exception as e:
            logger.error(f"Error visualizing coherence heatmap: {e}")
            return None
    
    def visualize_all(self) -> List[str]:
        """
        Generate all visualizations.
        
        Returns:
            list: Paths to all visualization files
        """
        viz_files = []
        
        # Visualize chord progression
        chord_viz = self.visualize_chord_progression()
        if chord_viz:
            viz_files.append(chord_viz)
        
        # Visualize healing events
        events_viz = self.visualize_healing_events()
        if events_viz:
            viz_files.append(events_viz)
        
        # Visualize coherence heatmap
        heatmap_viz = self.visualize_coherence_heatmap()
        if heatmap_viz:
            viz_files.append(heatmap_viz)
        
        return viz_files


# Example usage
if __name__ == "__main__":
    import sys
    
    # Create visualizer
    visualizer = QuantumChordVisualizer()
    
    # Generate all visualizations
    viz_files = visualizer.visualize_all()
    
    if viz_files:
        print(f"Generated {len(viz_files)} visualizations:")
        for viz_file in viz_files:
            print(f"  - {viz_file}")
    else:
        print("No visualizations generated")
