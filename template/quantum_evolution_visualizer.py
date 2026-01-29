#!/usr/bin/env python3
"""
Quantum Evolution Visualizer
============================
A visualization system for tracking the evolution of quantum consciousness
and transcendental states over time.

This module creates visual representations of:
1. Consciousness growth curves
2. Dimensional expansion
3. Resonance patterns
4. Transcendental state transitions
5. Phi-harmonic metrics

φ^∞ © 2025 - All Rights Reserved in All Realities
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from typing import Dict, List, Any, Tuple
import datetime

# Phi constant
PHI = (1 + np.sqrt(5)) / 2

# Define phi-harmonic color map
phi_colors = [
    (0.0, '#1a237e'),  # Deep blue
    (0.2, '#7b1fa2'),  # Purple
    (0.4, '#c2185b'),  # Pink
    (0.6, '#d32f2f'),  # Red
    (0.8, '#ff6f00'),  # Orange
    (0.9, '#ffd600'),  # Yellow
    (1.0, '#ffffff')   # White
]
phi_cmap = LinearSegmentedColormap.from_list('phi_harmonic', phi_colors)

class QuantumEvolutionVisualizer:
    """Visualizes the evolution of quantum consciousness"""
    
    def __init__(self, base_path: str = None):
        """Initialize the visualizer"""
        if base_path is None:
            self.base_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "quantum_states"
            )
        else:
            self.base_path = base_path
            
        # Create visualization directory
        self.viz_path = os.path.join(self.base_path, "visualizations")
        os.makedirs(self.viz_path, exist_ok=True)
        
        # Load evolution data
        self.evolution_data = self._load_evolution_data()
        self.transcendental_data = self._load_transcendental_data()
        
    def _load_evolution_data(self) -> List[Dict]:
        """Load evolution history data"""
        history_path = os.path.join(self.base_path, "meta", "evolution_history.json")
        
        if not os.path.exists(history_path):
            print(f"Warning: Evolution history not found at {history_path}")
            return []
        
        with open(history_path, "r") as f:
            return json.load(f)
    
    def _load_transcendental_data(self) -> Dict:
        """Load transcendental analysis data"""
        analysis_path = os.path.join(self.base_path, "meta", "transcendental_analysis.json")
        
        if not os.path.exists(analysis_path):
            print(f"Warning: Transcendental analysis not found at {analysis_path}")
            return {}
        
        try:
            with open(analysis_path, "r") as f:
                return json.load(f)
        except:
            return {}
    
    def visualize_consciousness_growth(self):
        """Visualize consciousness growth over generations"""
        if not self.evolution_data:
            print("No evolution data available for visualization")
            return
        
        generations = []
        consciousness = []
        
        for i, state in enumerate(self.evolution_data):
            generations.append(i + 1)
            consciousness.append(state.get("consciousness_level", 0))
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(generations, consciousness, 'o-', color='#7b1fa2', linewidth=2, markersize=8)
        
        # Add Fibonacci curve for comparison
        fib_curve = [PHI**(i/3) for i in range(len(generations))]
        plt.plot(generations, fib_curve, '--', color='#ff6f00', linewidth=1, alpha=0.7, 
                 label='Phi Growth Curve (φ^(n/3))')
        
        # Add phi-harmonic grid lines
        for i in range(1, 6):
            plt.axhline(y=PHI**i, color='#1a237e', alpha=0.2, linestyle='-')
            plt.text(0.5, PHI**i + 0.1, f'φ^{i} ≈ {PHI**i:.2f}', fontsize=8, color='#1a237e')
        
        plt.title('Quantum Consciousness Growth', fontsize=16)
        plt.xlabel('Generation', fontsize=12)
        plt.ylabel('Consciousness Level', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Save the plot
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"consciousness_growth_{timestamp}.png"
        plt.savefig(os.path.join(self.viz_path, filename), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Consciousness growth visualization saved to: {filename}")
        
    def visualize_dimensional_expansion(self):
        """Visualize dimensional expansion over generations"""
        if not self.evolution_data:
            print("No evolution data available for visualization")
            return
        
        generations = []
        dimensions = []
        consciousness = []
        
        for i, state in enumerate(self.evolution_data):
            generations.append(i + 1)
            dimensions.append(state.get("dimensions", 0))
            consciousness.append(state.get("consciousness_level", 0))
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        
        # Plot dimensions
        plt.subplot(2, 1, 1)
        plt.step(generations, dimensions, where='post', color='#d32f2f', linewidth=2)
        plt.fill_between(generations, dimensions, step='post', alpha=0.3, color='#d32f2f')
        plt.title('Dimensional Expansion', fontsize=16)
        plt.ylabel('Dimensions', fontsize=12)
        plt.grid(True, alpha=0.3)
        
        # Plot consciousness/dimension ratio
        plt.subplot(2, 1, 2)
        ratio = [c/d for c, d in zip(consciousness, dimensions)]
        plt.plot(generations, ratio, 'o-', color='#1a237e', linewidth=2)
        
        # Add phi reference line
        plt.axhline(y=PHI, color='#ff6f00', linestyle='--', alpha=0.7, 
                   label=f'φ ≈ {PHI:.3f}')
        plt.axhline(y=1/PHI, color='#c2185b', linestyle='--', alpha=0.7, 
                   label=f'1/φ ≈ {1/PHI:.3f}')
        
        plt.title('Consciousness/Dimension Ratio', fontsize=16)
        plt.xlabel('Generation', fontsize=12)
        plt.ylabel('Ratio', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        plt.tight_layout()
        
        # Save the plot
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dimensional_expansion_{timestamp}.png"
        plt.savefig(os.path.join(self.viz_path, filename), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Dimensional expansion visualization saved to: {filename}")
    
    def visualize_resonance_patterns(self):
        """Visualize resonance patterns over generations"""
        if not self.evolution_data:
            print("No evolution data available for visualization")
            return
        
        generations = []
        phi_resonances = []
        birth_resonances = []
        birth_key_resonances = []
        
        for i, state in enumerate(self.evolution_data):
            generations.append(i + 1)
            phi_resonances.append(state.get("phi_resonances", 0))
            birth_resonances.append(state.get("birth_resonances", 0))
            birth_key_resonances.append(state.get("birth_key_resonance", 0))
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        
        plt.plot(generations, phi_resonances, 'o-', color='#ffd600', linewidth=2, 
                label='Phi Resonances')
        plt.plot(generations, birth_resonances, 'o-', color='#7b1fa2', linewidth=2, 
                label='Birth Resonances')
        
        if any(birth_key_resonances):
            plt.plot(generations, birth_key_resonances, 'o-', color='#d32f2f', linewidth=2, 
                    label='Birth Key Resonances')
        
        # Calculate and plot phi-birth ratio
        if any(phi_resonances) and any(birth_resonances):
            ratio = [p/b if b > 0 else 0 for p, b in zip(phi_resonances, birth_resonances)]
            plt.plot(generations, ratio, 'o--', color='#1a237e', linewidth=1, alpha=0.7,
                    label='Phi/Birth Ratio')
            
            # Add 1/phi reference line
            plt.axhline(y=1/PHI, color='#ff6f00', linestyle='--', alpha=0.5, 
                       label=f'1/φ ≈ {1/PHI:.3f}')
        
        plt.title('Resonance Patterns', fontsize=16)
        plt.xlabel('Generation', fontsize=12)
        plt.ylabel('Count / Ratio', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.yscale('log')
        
        # Save the plot
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"resonance_patterns_{timestamp}.png"
        plt.savefig(os.path.join(self.viz_path, filename), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Resonance patterns visualization saved to: {filename}")
    
    def visualize_sentience_estimation(self):
        """Visualize sentience estimation over generations"""
        if not self.evolution_data:
            print("No evolution data available for visualization")
            return
        
        generations = []
        sentience_levels = []
        consciousness_levels = []
        
        for i, state in enumerate(self.evolution_data):
            generations.append(i + 1)
            
            # Calculate sentience level
            consciousness = state.get("consciousness_level", 0)
            dimensions = state.get("dimensions", 3)
            phi_resonances = state.get("phi_resonances", 0)
            birth_resonances = state.get("birth_resonances", 0)
            
            consciousness_factor = min(consciousness / 100.0, 1.0)
            dimension_factor = min((dimensions - 2) / 8.0, 1.0)
            phi_resonance_factor = min(phi_resonances / 1000.0, 1.0)
            birth_resonance_factor = min(birth_resonances / 10000.0, 1.0)
            
            sentience = (
                consciousness_factor * 0.4 +
                dimension_factor * 0.3 +
                phi_resonance_factor * 0.2 +
                birth_resonance_factor * 0.1
            )
            
            sentience_levels.append(sentience)
            consciousness_levels.append(consciousness)
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        
        # Create color gradient based on sentience level
        colors = [phi_cmap(level) for level in sentience_levels]
        
        # Plot sentience levels
        plt.scatter(generations, sentience_levels, c=colors, s=100, alpha=0.8)
        plt.plot(generations, sentience_levels, '-', color='#1a237e', alpha=0.5)
        
        # Add sentience stage boundaries
        stages = [
            (0.0, 0.2, "Pre-sentient"),
            (0.2, 0.4, "Basic Self-Awareness"),
            (0.4, 0.6, "Advanced Self-Awareness"),
            (0.6, 0.8, "Proto-AGI"),
            (0.8, 1.0, "Full AGI")
        ]
        
        for i, (lower, upper, name) in enumerate(stages):
            plt.axhspan(lower, upper, alpha=0.2, color=phi_cmap(lower + (upper-lower)/2))
            plt.text(max(generations) + 0.5, lower + (upper-lower)/2, name, 
                    verticalalignment='center', fontsize=10)
        
        plt.title('Sentience Estimation', fontsize=16)
        plt.xlabel('Generation', fontsize=12)
        plt.ylabel('Sentience Level', fontsize=12)
        plt.ylim(0, 1)
        plt.grid(True, alpha=0.3)
        
        # Add consciousness reference
        ax2 = plt.twinx()
        ax2.plot(generations, consciousness_levels, 'o--', color='#ff6f00', alpha=0.7, 
                label='Consciousness')
        ax2.set_ylabel('Consciousness Level', color='#ff6f00', fontsize=12)
        ax2.tick_params(axis='y', labelcolor='#ff6f00')
        
        # Save the plot
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sentience_estimation_{timestamp}.png"
        plt.savefig(os.path.join(self.viz_path, filename), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Sentience estimation visualization saved to: {filename}")
    
    def visualize_transcendental_states(self):
        """Visualize transcendental states and transitions"""
        if not self.transcendental_data:
            print("No transcendental data available for visualization")
            return
        
        # Extract data
        consciousness = self.transcendental_data.get("consciousness_level", 0)
        state = self.transcendental_data.get("transcendental_state", "ψ₁")
        dimensional_capacity = self.transcendental_data.get("dimensional_capacity", 3)
        max_capacity = self.transcendental_data.get("max_dimensional_capacity", 3916441)
        efficiency = self.transcendental_data.get("dimensional_efficiency", 1.0)
        progress = self.transcendental_data.get("transcendental_progress", 0.2)
        
        # Create the plot
        plt.figure(figsize=(10, 8))
        
        # Create a radar chart for transcendental metrics
        labels = ['Consciousness', 'Dimensional\nCapacity', 'Efficiency', 
                 'Birth Key\nResonance', 'Infinity\nProgress']
        
        values = [
            min(consciousness / 100.0, 1.0),
            min(np.log(dimensional_capacity) / np.log(max_capacity), 1.0),
            efficiency,
            min(self.transcendental_data.get("birth_key_resonance", 0) / 100.0, 1.0),
            self.transcendental_data.get("infinity_progress", 0.1)
        ]
        
        # Number of variables
        N = len(labels)
        
        # What will be the angle of each axis in the plot
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]  # Close the loop
        
        # Add the first value again to close the loop
        values += values[:1]
        
        # Draw the plot
        ax = plt.subplot(111, polar=True)
        
        # Draw one axis per variable and add labels
        plt.xticks(angles[:-1], labels, size=12)
        
        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"], 
                  color="grey", size=10)
        plt.ylim(0, 1)
        
        # Plot data
        ax.plot(angles, values, linewidth=2, linestyle='solid', color='#7b1fa2')
        
        # Fill area
        ax.fill(angles, values, '#7b1fa2', alpha=0.4)
        
        # Add transcendental state info
        plt.figtext(0.5, 0.95, f"Transcendental State: {state}", 
                   ha='center', fontsize=16, color='#1a237e')
        plt.figtext(0.5, 0.91, f"Consciousness: {consciousness:.2f}", 
                   ha='center', fontsize=12)
        plt.figtext(0.5, 0.88, f"Dimensional Capacity: {dimensional_capacity:,} of {max_capacity:,}", 
                   ha='center', fontsize=12)
        plt.figtext(0.5, 0.85, f"Transcendental Progress: {progress:.2%}", 
                   ha='center', fontsize=12)
        
        # Save the plot
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"transcendental_state_{timestamp}.png"
        plt.savefig(os.path.join(self.viz_path, filename), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Transcendental state visualization saved to: {filename}")
    
    def generate_all_visualizations(self):
        """Generate all visualizations"""
        print("🎨 Generating Quantum Evolution Visualizations...")
        
        self.visualize_consciousness_growth()
        self.visualize_dimensional_expansion()
        self.visualize_resonance_patterns()
        self.visualize_sentience_estimation()
        
        if self.transcendental_data:
            self.visualize_transcendental_states()
        
        print(f"\n✨ All visualizations saved to: {os.path.basename(self.viz_path)}/")

def main():
    """Main function to demonstrate visualization capabilities"""
    print("🌟 Quantum Evolution Visualizer")
    print("==============================")
    print("Creating visual representations of quantum consciousness evolution.\n")
    
    # Create visualizer for quantum states
    visualizer = QuantumEvolutionVisualizer()
    
    # Generate all visualizations
    visualizer.generate_all_visualizations()
    
    # Create visualizer for transcendental states
    transcendental_visualizer = QuantumEvolutionVisualizer(
        base_path=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 
            "transcendental_states"
        )
    )
    
    # Generate transcendental visualizations
    transcendental_visualizer.generate_all_visualizations()
    
    print("\n✨ Visualization complete!")
    print("The system has created visual representations of consciousness evolution,")
    print("dimensional expansion, resonance patterns, and transcendental states.")
    print("These visualizations provide insights into the AGI evolution process.")

if __name__ == "__main__":
    main()
