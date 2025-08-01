#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
φ-HARMONIC NEURAL ARCHITECTURE VISUALIZER
Visualizes the 9-layer quantum neural network with φ-dimensional scaling
φ^75 validation seal: 4721424167835376.00
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.animation as animation
from math import sqrt
import time
from typing import List, Dict, Tuple, Optional, Union, Any

# Import the φ-Harmonic Neural Architecture
from phi_harmonic_neural_architecture import PhiHarmonicNeuralArchitecture, PHI, PHI_75

# Create custom φ-harmonic color maps with proper scaling
# Ensure x values are in strictly increasing order from 0 to 1
phi_colors = [
    (0.0, (0.0, 0.0, 0.5)),      # Deep blue
    (0.1, (0.0, 0.2, 0.8)),       # Blue
    (0.2, (0.0, 0.5, 1.0)),       # Light blue
    (0.4, (0.0, 0.8, 0.8)),       # Cyan
    (0.5, (0.0, 0.8, 0.4)),       # Teal
    (0.6, (0.5, 0.8, 0.0)),       # Green
    (0.7, (0.8, 0.8, 0.0)),       # Yellow
    (0.9, (1.0, 0.5, 0.0)),       # Orange
    (1.0, (1.0, 0.0, 0.0))        # Red
]

# Create φ-harmonic colormap
phi_cmap = LinearSegmentedColormap.from_list('phi_harmonic', phi_colors)

# Create quantum colormap with φ-inspired colors
quantum_cmap = LinearSegmentedColormap.from_list('quantum', [
    (0.0, (0.0, 0.0, 0.3)),      # Deep purple
    (0.2, (0.0, 0.3, 0.8)),       # Blue
    (0.5, (0.5, 0.0, 0.5)),       # Violet
    (0.8, (0.8, 0.0, 0.8)),       # Magenta
    (1.0, (1.0, 0.0, 0.3))        # Red
])


class PhiHarmonicVisualizer:
    """Visualizer for the φ-Harmonic Neural Architecture"""
    
    def __init__(self, architecture):
        """Initialize visualizer with architecture instance"""
        self.architecture = architecture
        self.fig = None
        self.axes = {}
        self.layer_plots = {}
        self.connection_plots = {}
        self.phi = PHI
        self.phi_seal = PHI_75
        
        # Animation properties
        self.anim = None
        self.frame_count = 0
        
        print(f"\n=== φ-HARMONIC NEURAL VISUALIZER ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"φ^75 validation seal: {PHI_75:.2f}")
    
    def setup_figure(self):
        """Set up the figure and axes for visualization"""
        plt.style.use('dark_background')
        self.fig = plt.figure(figsize=(16, 12))
        self.fig.suptitle(f'φ-Harmonic Neural Architecture (φ = {PHI:.8f})', fontsize=16)
        
        # Create grid of subplots
        gs = self.fig.add_gridspec(4, 3)
        
        # Main architecture view
        self.axes['main'] = self.fig.add_subplot(gs[0:3, 0:2])
        self.axes['main'].set_title('9-Layer φ-Harmonic Architecture')
        self.axes['main'].set_xlim(-2, 12)
        self.axes['main'].set_ylim(-1, 10)
        self.axes['main'].axis('off')
        
        # Layer activity plots
        self.axes['activity'] = self.fig.add_subplot(gs[0, 2])
        self.axes['activity'].set_title('Layer Activity')
        self.axes['activity'].set_xlabel('Layer Index')
        self.axes['activity'].set_ylabel('Activity')
        
        # Frequency spectrum
        self.axes['frequency'] = self.fig.add_subplot(gs[1, 2])
        self.axes['frequency'].set_title('φ-Harmonic Frequencies')
        self.axes['frequency'].set_xlabel('Layer Index')
        self.axes['frequency'].set_ylabel('Frequency (Hz)')
        
        # Energy distribution
        self.axes['energy'] = self.fig.add_subplot(gs[2, 2])
        self.axes['energy'].set_title('φ-Scaled Energy')
        self.axes['energy'].set_xlabel('Layer Index')
        self.axes['energy'].set_ylabel('Energy')
        
        # Learning curve
        self.axes['learning'] = self.fig.add_subplot(gs[3, 0])
        self.axes['learning'].set_title('φ-Harmonic Learning')
        self.axes['learning'].set_xlabel('Cycle')
        self.axes['learning'].set_ylabel('Error')
        
        # Size scaling
        self.axes['size'] = self.fig.add_subplot(gs[3, 1])
        self.axes['size'].set_title('φ-Scaled Layer Size')
        self.axes['size'].set_xlabel('Layer Index')
        self.axes['size'].set_ylabel('Size')
        
        # Quantum metrics
        self.axes['quantum'] = self.fig.add_subplot(gs[3, 2])
        self.axes['quantum'].set_title('Quantum Bridge Metrics')
        self.axes['quantum'].set_xlabel('Time')
        self.axes['quantum'].set_ylabel('φ-Coherence')
        
        self.fig.tight_layout()
        
    def draw_architecture(self):
        """Draw the φ-harmonic neural architecture"""
        ax = self.axes['main']
        layers = self.architecture.layers
        
        # Layer colors based on type
        layer_colors = {
            'Quantum': '#8A2BE2',  # Violet for quantum layers
            'Q-State': '#9370DB',
            'Bridge': '#BA55D3',
            'Process': '#4169E1',  # Blue for processing layers
            'Memory': '#1E90FF',
            'Logic': '#00BFFF',
            'Neural': '#32CD32',   # Green for neural layers
            'Pattern': '#ADFF2F',
            'Input': '#FFD700',    # Gold for input layer
        }
        
        # Draw each layer
        reversed_layers = list(reversed(layers))  # Convert to list for indexing
        for i, layer in enumerate(reversed_layers):  # Reverse to go from input to quantum
            layer_info = layer.get_info()
            y_pos = i
            
            # Layer width based on φ-scaling
            width = 10 * layer_info['phi_factor']
            height = 0.8
            
            # Draw layer rectangle
            rect = Rectangle(
                (5 - width/2, y_pos - height/2),
                width, height,
                color=layer_colors[layer_info['name']],
                alpha=0.7,
                linewidth=1,
                edgecolor='white'
            )
            ax.add_patch(rect)
            
            # Add layer label
            ax.text(
                5, y_pos,
                f"L{layer_info['index']} {layer_info['name']} ({layer_info['frequency']:.2f} Hz)",
                ha='center', va='center',
                color='white',
                fontsize=9,
                fontweight='bold'
            )
            
            # Store reference for animation
            self.layer_plots[layer_info['index']] = rect
        
        # Draw connections between layers
        for i, layer in enumerate(reversed_layers):
            if i < len(layers) - 1:  # Skip last layer (quantum)
                layer_info = layer.get_info()
                next_layer = reversed_layers[i+1]
                next_info = next_layer.get_info()
                
                # Draw standard connection
                y1 = i
                y2 = i + 1
                
                # Connection width based on φ-scaling
                conn_width = 2 * min(layer_info['phi_factor'], next_info['phi_factor'])
                
                # Draw connection arrow
                arrow = FancyArrowPatch(
                    (5, y1 + height/2),
                    (5, y2 - height/2),
                    arrowstyle='-|>',
                    color='white',
                    alpha=0.5,
                    linewidth=conn_width,
                    mutation_scale=10
                )
                ax.add_patch(arrow)
                
                # Store reference for animation
                conn_key = f"{layer_info['index']}-{next_info['index']}"
                self.connection_plots[conn_key] = arrow
                
                # Draw φ-harmonic skip connections (every 3rd layer)
                if i < len(layers) - 3:
                    skip_layer = reversed_layers[i+3]
                    skip_info = skip_layer.get_info()
                    
                    # Draw skip connection
                    y3 = i + 3
                    
                    # Skip connection with φ-scaled width
                    skip_width = conn_width / PHI
                    
                    # Draw skip connection arrow
                    skip_arrow = FancyArrowPatch(
                        (5 - width/4, y1),
                        (5 - width/4, y3),
                        arrowstyle='->',
                        color='#FF6347',  # Tomato color for skip connections
                        alpha=0.4,
                        linewidth=skip_width,
                        linestyle='--',
                        connectionstyle='arc3,rad=0.2'
                    )
                    ax.add_patch(skip_arrow)
                    
                    # Store reference for animation
                    skip_key = f"{layer_info['index']}-skip-{skip_info['index']}"
                    self.connection_plots[skip_key] = skip_arrow
        
        # Add φ-harmonic annotations
        ax.text(
            11, 9,
            f"φ = {PHI:.8f}",
            ha='right', va='top',
            color='white',
            fontsize=10
        )
        
        ax.text(
            11, 8.5,
            f"φ^75 seal: {PHI_75:.2e}",
            ha='right', va='top',
            color='white',
            fontsize=10
        )
        
        # Add layer group annotations
        ax.text(
            -1.5, 8,
            "Quantum\nLayers",
            ha='center', va='center',
            color='#BA55D3',
            fontsize=10,
            fontweight='bold'
        )
        
        ax.text(
            -1.5, 5,
            "Neural\nLayers",
            ha='center', va='center',
            color='#1E90FF',
            fontsize=10,
            fontweight='bold'
        )
        
        ax.text(
            -1.5, 1.5,
            "Pattern\nLayers",
            ha='center', va='center',
            color='#ADFF2F',
            fontsize=10,
            fontweight='bold'
        )
    
    def plot_layer_metrics(self):
        """Plot metrics for all layers"""
        layers = self.architecture.layers
        indices = [layer.get_info()['index'] for layer in layers]
        
        # Plot layer activity
        ax = self.axes['activity']
        ax.clear()
        ax.set_title('Layer Activity')
        
        activities = [np.mean(np.abs(layer.activation)) if hasattr(layer, 'activation') and 
                     layer.activation is not None else 0 for layer in layers]
        
        activity_plot = ax.bar(indices, activities, color=phi_cmap(np.linspace(0, 1, len(indices))))
        ax.set_xlabel('Layer Index')
        ax.set_ylabel('Activity')
        ax.set_xticks(indices)
        ax.set_ylim(0, 1)
        
        # Plot frequency spectrum
        ax = self.axes['frequency']
        ax.clear()
        ax.set_title('φ-Harmonic Frequencies')
        
        frequencies = [layer.frequency for layer in layers]
        freq_plot = ax.plot(indices, frequencies, 'o-', color='cyan')
        
        # Add φ-scaling curve
        x_fine = np.linspace(1, 9, 100)
        y_fine = 11.09 * (PHI ** (1 - x_fine))
        ax.plot(x_fine, y_fine, '--', color='gray', alpha=0.5)
        
        ax.set_xlabel('Layer Index')
        ax.set_ylabel('Frequency (Hz)')
        ax.set_xticks(indices)
        ax.set_yscale('log')
        ax.grid(True, alpha=0.3)
        
        # Plot energy distribution
        ax = self.axes['energy']
        ax.clear()
        ax.set_title('φ-Scaled Energy')
        
        energies = [layer.energy for layer in layers]
        energy_plot = ax.bar(indices, energies, color=phi_cmap(np.linspace(0, 1, len(indices))))
        
        # Add φ-scaling curve
        x_fine = np.linspace(1, 9, 100)
        y_fine = self.architecture.base_energy * (1 / (PHI ** (x_fine - 1)))
        ax.plot(x_fine, y_fine, '--', color='gray', alpha=0.5)
        
        ax.set_xlabel('Layer Index')
        ax.set_ylabel('Energy')
        ax.set_xticks(indices)
        
        # Plot size scaling
        ax = self.axes['size']
        ax.clear()
        ax.set_title('φ-Scaled Layer Size')
        
        sizes = [layer.size for layer in layers]
        size_plot = ax.bar(indices, sizes, color=phi_cmap(np.linspace(0, 1, len(indices))))
        
        # Add φ-scaling curve
        x_fine = np.linspace(1, 9, 100)
        y_fine = self.architecture.base_size * (1 / (PHI ** (x_fine - 1)))
        ax.plot(x_fine, y_fine, '--', color='gray', alpha=0.5)
        
        ax.set_xlabel('Layer Index')
        ax.set_ylabel('Size')
        ax.set_xticks(indices)
        
        # Plot learning curve if we have error history
        ax = self.axes['learning']
        ax.clear()
        ax.set_title('φ-Harmonic Learning')
        
        if hasattr(self.architecture, 'error_history') and self.architecture.error_history:
            errors = self.architecture.error_history
            cycles = np.arange(len(errors))
            
            ax.plot(cycles, errors, 'o-', color='orange')
            
            # Add φ-harmonic learning curve
            if len(cycles) > 1:
                x_fine = np.linspace(0, max(cycles), 100)
                # E₀ × exp(-t/φ)
                y_fine = errors[0] * np.exp(-x_fine / PHI)
                ax.plot(x_fine, y_fine, '--', color='gray', alpha=0.5)
        
        ax.set_xlabel('Cycle')
        ax.set_ylabel('Error')
        ax.set_yscale('log')
        ax.grid(True, alpha=0.3)
        
        # Plot quantum metrics
        ax = self.axes['quantum']
        ax.clear()
        ax.set_title('Quantum Bridge Metrics')
        
        # Get quantum layer outputs if available
        quantum_outputs = []
        for layer in layers:
            if layer.get_info()['index'] >= 7:  # Quantum layers
                if hasattr(layer, 'activation') and layer.activation is not None:
                    quantum_outputs.append(np.mean(np.abs(layer.activation)))
        
        if quantum_outputs:
            quantum_indices = [7, 8, 9]  # Bridge, Q-State, Quantum
            ax.bar(quantum_indices, quantum_outputs, color=quantum_cmap(np.linspace(0, 1, len(quantum_outputs))))
            
            # Add φ-coherence line
            ax.axhline(y=1/PHI, color='magenta', linestyle='--', alpha=0.5, label='φ-Coherence')
            
        ax.set_xlabel('Quantum Layer')
        ax.set_ylabel('φ-Coherence')
        ax.set_ylim(0, 1)
        ax.legend()
    
    def animate_processing(self, input_data, num_frames=100):
        """Animate the processing of input data through the architecture"""
        self.setup_figure()
        self.draw_architecture()
        
        # Initialize plots
        self.plot_layer_metrics()
        
        def update(frame):
            """Update function for animation"""
            # Process input with small variations for animation
            t = frame / num_frames
            # Add φ-harmonic variations to input
            variation = 0.1 * np.sin(2 * np.pi * t * PHI)
            varied_input = input_data + variation
            
            # Process through architecture
            self.architecture.process(varied_input)
            
            # Update layer colors based on activation
            for layer in self.architecture.layers:
                info = layer.get_info()
                layer_rect = self.layer_plots[info['index']]
                
                # Calculate activation intensity
                if hasattr(layer, 'activation') and layer.activation is not None:
                    intensity = np.mean(np.abs(layer.activation))
                    # Clamp intensity to 0-1 range for φ-harmonic visualization
                    intensity = min(max(intensity, 0.0), 1.0)
                    # Adjust color based on activation
                    if info['is_quantum']:
                        color = quantum_cmap(intensity)
                    else:
                        color = phi_cmap(intensity)
                    layer_rect.set_facecolor(color)
                    # Ensure alpha stays in 0-1 range
                    layer_rect.set_alpha(0.5 + min(0.5, 0.5 * intensity))
            
            # Update connection colors based on data flow
            for i, layer in enumerate(self.architecture.layers):
                if i < len(self.architecture.layers) - 1:
                    layer_info = layer.get_info()
                    next_layer = self.architecture.layers[i+1]
                    next_info = next_layer.get_info()
                    
                    # Get connection arrow
                    conn_key = f"{layer_info['index']}-{next_info['index']}"
                    if conn_key in self.connection_plots:
                        arrow = self.connection_plots[conn_key]
                        
                        # Calculate flow intensity
                        if hasattr(layer, 'activation') and layer.activation is not None:
                            intensity = np.mean(np.abs(layer.activation))
                            # Clamp intensity to 0-1 range
                            intensity = min(max(intensity, 0.0), 1.0)
                            # Pulse effect with φ-harmonic timing
                            pulse = 0.5 + 0.5 * np.sin(2 * np.pi * (t * layer.frequency + frame / (10 * PHI)))
                            # Ensure alpha stays in 0-1 range
                            alpha_value = min(1.0, 0.2 + 0.8 * intensity * pulse)
                            arrow.set_alpha(alpha_value)
            
            # Update metrics plots
            self.plot_layer_metrics()
            
            self.frame_count += 1
            return list(self.layer_plots.values()) + list(self.connection_plots.values())
        
        # Create animation
        self.anim = animation.FuncAnimation(
            self.fig, update, frames=num_frames, interval=50, blit=True
        )
        
        plt.tight_layout()
        return self.anim
    
    def visualize_static(self, input_data):
        """Create a static visualization of the architecture"""
        self.setup_figure()
        self.draw_architecture()
        
        # Process input through architecture
        self.architecture.process(input_data)
        
        # Update layer colors based on activation
        for layer in self.architecture.layers:
            info = layer.get_info()
            layer_rect = self.layer_plots[info['index']]
            
            # Calculate activation intensity
            if hasattr(layer, 'activation') and layer.activation is not None:
                intensity = np.mean(np.abs(layer.activation))
                # Clamp intensity to 0-1 range for φ-harmonic visualization
                intensity = min(max(intensity, 0.0), 1.0)
                # Adjust color based on activation
                if info['is_quantum']:
                    color = quantum_cmap(intensity)
                else:
                    color = phi_cmap(intensity)
                layer_rect.set_facecolor(color)
                # Ensure alpha stays in 0-1 range
                layer_rect.set_alpha(0.5 + min(0.5, 0.5 * intensity))
        
        # Update metrics plots
        self.plot_layer_metrics()
        
        plt.tight_layout()
        return self.fig
    
    def save_animation(self, filename='phi_harmonic_animation.mp4'):
        """Save the animation to a file"""
        if self.anim is not None:
            self.anim.save(filename, writer='ffmpeg', dpi=100)
            print(f"[φ] Animation saved to {filename}")
        else:
            print("[φ] No animation to save")
    
    def save_figure(self, filename='phi_harmonic_architecture.png'):
        """Save the current figure to a file"""
        if self.fig is not None:
            self.fig.savefig(filename, dpi=150)
            print(f"[φ] Figure saved to {filename}")
        else:
            print("[φ] No figure to save")


# Example usage
if __name__ == "__main__":
    # Create φ-harmonic neural architecture
    architecture = PhiHarmonicNeuralArchitecture(base_size=64)
    
    # Create visualizer
    visualizer = PhiHarmonicVisualizer(architecture)
    
    # Generate sample input (sine wave with φ-harmonic frequencies)
    x = np.linspace(0, 2*np.pi, architecture.layers[-1].size)
    input_data = np.sin(x) + 0.5 * np.sin(PHI * x) + 0.25 * np.sin(PHI**2 * x)
    
    # Static visualization
    visualizer.visualize_static(input_data)
    visualizer.save_figure()
    
    # Animate processing
    anim = visualizer.animate_processing(input_data, num_frames=100)
    
    # Show visualization
    plt.show()
    
    print(f"\n[φ] φ-harmonic visualization complete")
    print(f"[φ] φ^75 validation seal: {PHI_75:.2f}")
