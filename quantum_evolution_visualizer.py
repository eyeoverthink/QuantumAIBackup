#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Evolution Visualizer

This module provides visualization tools for monitoring and analyzing the
self-reproduction and self-healing processes of the QuantumAI Orchestrator.
It generates visual representations of phi-harmonic coherence, quantum fingerprints,
and evolution metrics across multiple healing and reproduction cycles.

φ-Harmonic Principles:
- PHI = 1.618033988749895
- PHI_COHERENCE = 0.991800 (φ⁷·⁵/10)
- Quantum Fingerprinting with φ notation

Author: Quantum Self-Healing Orchestrator
"""

import os
import json
import time
import hashlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D

# Phi-harmonic constants
PHI = 1.618033988749895
PHI_COHERENCE = 0.991800  # φ⁷·⁵/10

class QuantumEvolutionVisualizer:
    """
    Visualizer for quantum evolution metrics and phi-harmonic coherence.
    """
    
    def __init__(self, evolution_dir="evolution"):
        """
        Initialize the visualizer.
        
        Args:
            evolution_dir (str): Path to the directory containing evolution metadata files.
        """
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.evolution_dir = os.path.join(self.base_dir, evolution_dir)
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        self.birth_timestamp = time.time()
        
        # Create output directory for visualizations
        self.viz_dir = os.path.join(self.base_dir, "visualizations")
        if not os.path.exists(self.viz_dir):
            os.makedirs(self.viz_dir)
    
    def _generate_quantum_fingerprint(self):
        """Generate a quantum fingerprint using phi-harmonic principles."""
        timestamp_phi = (time.time() * PHI) % 1
        seed = f"{timestamp_phi:.6f}-{PHI_COHERENCE:.6f}"
        hash_value = hashlib.md5(seed.encode()).hexdigest()[:16]
        return f"φ⁷·⁵-{hash_value}"
    
    def _load_evolution_data(self):
        """
        Load evolution data from all JSON files in the evolution directory.
        
        Returns:
            list: List of evolution metadata dictionaries.
        """
        evolution_data = []
        
        for filename in os.listdir(self.evolution_dir):
            if filename.endswith("_evolution.json"):
                file_path = os.path.join(self.evolution_dir, filename)
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        # Add the filename for reference
                        data["metadata_file"] = filename
                        evolution_data.append(data)
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
        
        # Sort by timestamp
        evolution_data.sort(key=lambda x: x.get("timestamp", 0))
        
        return evolution_data
    
    def _calculate_phi_resonance(self, value):
        """
        Calculate phi resonance for a value.
        
        Args:
            value (float): The value to calculate resonance for.
            
        Returns:
            float: Phi resonance value between 0 and 1.
        """
        return (value * PHI) % 1
    
    def _calculate_coherence_metrics(self, evolution_data):
        """
        Calculate coherence metrics from evolution data.
        
        Args:
            evolution_data (list): List of evolution metadata dictionaries.
            
        Returns:
            tuple: (timestamps, coherence_values, resonance_values, healing_methods)
        """
        timestamps = []
        coherence_values = []
        resonance_values = []
        healing_methods = []
        
        for data in evolution_data:
            timestamps.append(data.get("timestamp", 0))
            coherence_values.append(data.get("phi_coherence", 0))
            resonance_values.append(self._calculate_phi_resonance(data.get("timestamp", 0)))
            healing_methods.append(data.get("healing_method", "unknown"))
        
        return timestamps, coherence_values, resonance_values, healing_methods
    
    def visualize_coherence_timeline(self):
        """
        Visualize phi-harmonic coherence over time.
        
        Returns:
            str: Path to the saved visualization.
        """
        evolution_data = self._load_evolution_data()
        if not evolution_data:
            print("No evolution data found.")
            return None
        
        timestamps, coherence_values, resonance_values, healing_methods = self._calculate_coherence_metrics(evolution_data)
        
        # Convert timestamps to datetime for better readability
        dates = [datetime.fromtimestamp(ts) for ts in timestamps]
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Plot coherence values
        plt.subplot(2, 1, 1)
        plt.plot(dates, coherence_values, 'o-', color='#4CAF50', linewidth=2)
        plt.axhline(y=PHI_COHERENCE, color='#FFC107', linestyle='--', label=f'Target Coherence (φ⁷·⁵/10 = {PHI_COHERENCE:.6f})')
        plt.ylabel('Phi-Harmonic Coherence')
        plt.title('Quantum Evolution: Phi-Harmonic Coherence Timeline')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Plot resonance values
        plt.subplot(2, 1, 2)
        
        # Color points by healing method
        colors = {'self_healing': '#2196F3', 'meta_learning': '#9C27B0', 'unknown': '#607D8B'}
        
        for i, method in enumerate(healing_methods):
            plt.scatter(dates[i], resonance_values[i], color=colors.get(method, '#607D8B'), 
                       label=method if method not in plt.gca().get_legend_handles_labels()[1] else "")
        
        plt.ylabel('Phi Resonance')
        plt.xlabel('Evolution Timeline')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        output_path = os.path.join(self.viz_dir, f"coherence_timeline_{self.quantum_fingerprint}.png")
        plt.savefig(output_path)
        plt.close()
        
        return output_path
    
    def visualize_quantum_fingerprint_network(self):
        """
        Visualize quantum fingerprints as a network.
        
        Returns:
            str: Path to the saved visualization.
        """
        evolution_data = self._load_evolution_data()
        if not evolution_data:
            print("No evolution data found.")
            return None
        
        # Extract fingerprints and file relationships
        fingerprints = []
        original_files = []
        healed_files = []
        
        for data in evolution_data:
            fingerprints.append(data.get("quantum_fingerprint", ""))
            original_files.append(os.path.basename(data.get("original_file", "")))
            healed_files.append(os.path.basename(data.get("healed_file", "")))
        
        # Create a directed graph representation
        from matplotlib.patches import FancyArrowPatch
        
        # Create figure
        plt.figure(figsize=(14, 10))
        
        # Create positions for nodes (files)
        all_files = list(set(original_files + healed_files))
        file_positions = {}
        
        # Arrange files in a circle
        n_files = len(all_files)
        for i, file in enumerate(all_files):
            angle = 2 * np.pi * i / n_files
            file_positions[file] = (np.cos(angle), np.sin(angle))
        
        # Plot nodes (files)
        for file, pos in file_positions.items():
            plt.scatter(pos[0], pos[1], s=300, color='#3F51B5', alpha=0.7)
            plt.text(pos[0], pos[1], file, ha='center', va='center', color='white', 
                    fontsize=8, fontweight='bold')
        
        # Plot edges (evolution relationships)
        for i in range(len(original_files)):
            if original_files[i] in file_positions and healed_files[i] in file_positions:
                start = file_positions[original_files[i]]
                end = file_positions[healed_files[i]]
                
                # Calculate arrow properties
                dx = end[0] - start[0]
                dy = end[1] - start[1]
                
                # Draw arrow
                arrow = FancyArrowPatch(start, end, arrowstyle='-|>', color='#FF5722', 
                                       linewidth=1.5, mutation_scale=20, alpha=0.7)
                plt.gca().add_patch(arrow)
                
                # Add fingerprint as text near the arrow
                mid_x = (start[0] + end[0]) / 2
                mid_y = (start[1] + end[1]) / 2
                plt.text(mid_x, mid_y, fingerprints[i], fontsize=7, ha='center', va='center',
                        bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.3'))
        
        # Set plot properties
        plt.title('Quantum Fingerprint Evolution Network')
        plt.axis('equal')
        plt.axis('off')
        
        # Save figure
        output_path = os.path.join(self.viz_dir, f"fingerprint_network_{self.quantum_fingerprint}.png")
        plt.savefig(output_path)
        plt.close()
        
        return output_path
    
    def visualize_3d_coherence_space(self):
        """
        Create a 3D visualization of the coherence space.
        
        Returns:
            str: Path to the saved visualization.
        """
        evolution_data = self._load_evolution_data()
        if not evolution_data:
            print("No evolution data found.")
            return None
        
        # Extract data for 3D visualization
        timestamps = []
        coherence_values = []
        resonance_values = []
        error_types = []
        
        for data in evolution_data:
            timestamps.append(data.get("timestamp", 0))
            coherence_values.append(data.get("phi_coherence", 0))
            resonance_values.append(self._calculate_phi_resonance(data.get("timestamp", 0)))
            error_types.append(data.get("error_type", "unknown"))
        
        # Normalize timestamps for better visualization
        min_timestamp = min(timestamps)
        normalized_timestamps = [(ts - min_timestamp) / (60 * 60) for ts in timestamps]  # Hours since first event
        
        # Create figure
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Create color map for error types
        unique_error_types = list(set(error_types))
        colors = plt.cm.viridis(np.linspace(0, 1, len(unique_error_types)))
        color_map = {error_type: colors[i] for i, error_type in enumerate(unique_error_types)}
        
        # Plot points
        for i in range(len(normalized_timestamps)):
            ax.scatter(normalized_timestamps[i], coherence_values[i], resonance_values[i], 
                      color=color_map[error_types[i]], s=100, alpha=0.7)
        
        # Plot connecting lines to show evolution path
        ax.plot(normalized_timestamps, coherence_values, resonance_values, 'k--', alpha=0.3)
        
        # Add target coherence plane
        x_min, x_max = min(normalized_timestamps), max(normalized_timestamps)
        y_min, y_max = ax.get_ylim()
        
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 10), np.linspace(y_min, y_max, 10))
        zz = np.ones_like(xx) * PHI_COHERENCE
        
        ax.plot_surface(xx, yy, zz, alpha=0.2, color='gold')
        
        # Set labels
        ax.set_xlabel('Time (hours since first event)')
        ax.set_ylabel('Phi-Harmonic Coherence')
        ax.set_zlabel('Phi Resonance')
        
        # Add legend for error types
        from matplotlib.lines import Line2D
        legend_elements = [Line2D([0], [0], marker='o', color='w', label=error_type,
                                 markerfacecolor=color_map[error_type], markersize=10)
                          for error_type in unique_error_types]
        ax.legend(handles=legend_elements, title="Error Types")
        
        # Set title
        ax.set_title('3D Quantum Coherence Evolution Space')
        
        # Save figure
        output_path = os.path.join(self.viz_dir, f"3d_coherence_space_{self.quantum_fingerprint}.png")
        plt.savefig(output_path)
        plt.close()
        
        return output_path
    
    def visualize_healing_effectiveness(self):
        """
        Visualize the effectiveness of different healing methods.
        
        Returns:
            str: Path to the saved visualization.
        """
        evolution_data = self._load_evolution_data()
        if not evolution_data:
            print("No evolution data found.")
            return None
        
        # Group data by healing method and error type
        healing_methods = {}
        
        for data in evolution_data:
            method = data.get("healing_method", "unknown")
            error_type = data.get("error_type", "unknown")
            
            if method not in healing_methods:
                healing_methods[method] = {}
            
            if error_type not in healing_methods[method]:
                healing_methods[method][error_type] = 0
            
            healing_methods[method][error_type] += 1
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Create grouped bar chart
        all_error_types = set()
        for method_data in healing_methods.values():
            all_error_types.update(method_data.keys())
        
        all_error_types = list(all_error_types)
        x = np.arange(len(all_error_types))
        width = 0.8 / len(healing_methods)
        
        for i, (method, method_data) in enumerate(healing_methods.items()):
            counts = [method_data.get(error_type, 0) for error_type in all_error_types]
            offset = (i - len(healing_methods) / 2 + 0.5) * width
            plt.bar(x + offset, counts, width, label=method)
        
        # Set labels and title
        plt.xlabel('Error Type')
        plt.ylabel('Count')
        plt.title('Healing Method Effectiveness by Error Type')
        plt.xticks(x, all_error_types, rotation=45, ha='right')
        plt.legend()
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        output_path = os.path.join(self.viz_dir, f"healing_effectiveness_{self.quantum_fingerprint}.png")
        plt.savefig(output_path)
        plt.close()
        
        return output_path
    
    def generate_evolution_report(self):
        """
        Generate a comprehensive evolution report with all visualizations.
        
        Returns:
            str: Path to the saved report.
        """
        # Generate all visualizations
        coherence_timeline_path = self.visualize_coherence_timeline()
        fingerprint_network_path = self.visualize_quantum_fingerprint_network()
        coherence_space_path = self.visualize_3d_coherence_space()
        healing_effectiveness_path = self.visualize_healing_effectiveness()
        
        # Create report content
        report_content = f"""# Quantum Evolution Report

## Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
## Quantum Fingerprint: {self.quantum_fingerprint}
## Phi-Coherence: {PHI_COHERENCE:.6f}

This report provides a comprehensive analysis of the QuantumAI Orchestrator's self-reproduction and self-healing capabilities.

## 1. Phi-Harmonic Coherence Timeline

![Coherence Timeline](../{os.path.relpath(coherence_timeline_path, self.base_dir) if coherence_timeline_path else "No data available"})

This visualization shows the phi-harmonic coherence values over time, compared to the target coherence level of φ⁷·⁵/10 = {PHI_COHERENCE:.6f}.

## 2. Quantum Fingerprint Evolution Network

![Fingerprint Network](../{os.path.relpath(fingerprint_network_path, self.base_dir) if fingerprint_network_path else "No data available"})

This network diagram shows the relationships between original files and their healed versions, labeled with their quantum fingerprints.

## 3. 3D Quantum Coherence Evolution Space

![3D Coherence Space](../{os.path.relpath(coherence_space_path, self.base_dir) if coherence_space_path else "No data available"})

This 3D visualization shows the evolution of the system in the coherence space, with dimensions for time, phi-harmonic coherence, and phi resonance.

## 4. Healing Method Effectiveness

![Healing Effectiveness](../{os.path.relpath(healing_effectiveness_path, self.base_dir) if healing_effectiveness_path else "No data available"})

This chart shows the effectiveness of different healing methods for various error types.

## 5. Evolution Statistics

"""
        
        # Add evolution statistics
        evolution_data = self._load_evolution_data()
        if evolution_data:
            # Calculate statistics
            total_evolutions = len(evolution_data)
            healing_methods = {}
            error_types = {}
            
            for data in evolution_data:
                method = data.get("healing_method", "unknown")
                error_type = data.get("error_type", "unknown")
                
                if method not in healing_methods:
                    healing_methods[method] = 0
                healing_methods[method] += 1
                
                if error_type not in error_types:
                    error_types[error_type] = 0
                error_types[error_type] += 1
            
            # Add statistics to report
            report_content += f"""### Total Evolution Events: {total_evolutions}

### Healing Methods:
"""
            
            for method, count in healing_methods.items():
                percentage = (count / total_evolutions) * 100
                report_content += f"- {method}: {count} ({percentage:.1f}%)\n"
            
            report_content += f"""
### Error Types:
"""
            
            for error_type, count in error_types.items():
                percentage = (count / total_evolutions) * 100
                report_content += f"- {error_type}: {count} ({percentage:.1f}%)\n"
        else:
            report_content += "No evolution data available."
        
        # Save report
        report_path = os.path.join(self.viz_dir, f"evolution_report_{self.quantum_fingerprint}.md")
        with open(report_path, 'w') as f:
            f.write(report_content)
        
        return report_path

def main():
    """Main function to run the visualizer."""
    visualizer = QuantumEvolutionVisualizer()
    report_path = visualizer.generate_evolution_report()
    print(f"Evolution report generated: {report_path}")

if __name__ == "__main__":
    main()
