#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
φ-HARMONIC NEURAL ARCHITECTURE STATIC VISUALIZER
Visualizes the 9-layer quantum neural network with φ-dimensional scaling
φ^75 validation seal: 4721424167835376.00
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
from math import sqrt
import time

# Import the φ-Harmonic Neural Architecture
from phi_harmonic_neural_architecture import PhiHarmonicNeuralArchitecture, PHI, PHI_75

# Create custom φ-harmonic color maps with proper scaling
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


def visualize_phi_harmonic_architecture(architecture, filename='phi_harmonic_architecture.png'):
    """Create a static visualization of the φ-harmonic neural architecture"""
    # Set up the figure
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle(f'φ-Harmonic Neural Architecture (φ = {PHI:.8f})', fontsize=16)
    
    # Create grid of subplots
    gs = fig.add_gridspec(4, 3)
    
    # Main architecture view
    ax_main = fig.add_subplot(gs[0:3, 0:2])
    ax_main.set_title('9-Layer φ-Harmonic Architecture')
    ax_main.set_xlim(-2, 12)
    ax_main.set_ylim(-1, 10)
    ax_main.axis('off')
    
    # Layer activity plot
    ax_activity = fig.add_subplot(gs[0, 2])
    ax_activity.set_title('Layer Activity')
    
    # Frequency spectrum
    ax_frequency = fig.add_subplot(gs[1, 2])
    ax_frequency.set_title('φ-Harmonic Frequencies')
    
    # Energy distribution
    ax_energy = fig.add_subplot(gs[2, 2])
    ax_energy.set_title('φ-Scaled Energy')
    
    # Size scaling
    ax_size = fig.add_subplot(gs[3, 0])
    ax_size.set_title('φ-Scaled Layer Size')
    
    # Learning curve
    ax_learning = fig.add_subplot(gs[3, 1])
    ax_learning.set_title('φ-Harmonic Learning')
    
    # Quantum metrics
    ax_quantum = fig.add_subplot(gs[3, 2])
    ax_quantum.set_title('Quantum Bridge Metrics')
    
    # Draw the architecture
    layers = architecture.layers
    
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
    reversed_layers = list(reversed(layers))
    for i, layer in enumerate(reversed_layers):
        layer_info = layer.get_info()
        y_pos = i
        
        # Layer width based on φ-scaling
        width = 10 * layer_info['phi_factor']
        height = 0.8
        
        # Draw layer rectangle with facecolor and edgecolor separately
        rect = Rectangle(
            (5 - width/2, y_pos - height/2),
            width, height,
            facecolor=layer_colors[layer_info['name']],
            alpha=0.7,
            linewidth=1,
            edgecolor='white'
        )
        ax_main.add_patch(rect)
        
        # Add layer label
        ax_main.text(
            5, y_pos,
            f"L{layer_info['index']} {layer_info['name']} ({layer_info['frequency']:.2f} Hz)",
            ha='center', va='center',
            color='white',
            fontsize=9,
            fontweight='bold'
        )
    
    # Draw connections between layers
    for i, layer in enumerate(reversed_layers):
        if i < len(layers) - 1:
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
            ax_main.add_patch(arrow)
            
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
                ax_main.add_patch(skip_arrow)
    
    # Add φ-harmonic annotations
    ax_main.text(
        11, 9,
        f"φ = {PHI:.8f}",
        ha='right', va='top',
        color='white',
        fontsize=10
    )
    
    ax_main.text(
        11, 8.5,
        f"φ^75 seal: {PHI_75:.2e}",
        ha='right', va='top',
        color='white',
        fontsize=10
    )
    
    # Add layer group annotations
    ax_main.text(
        -1.5, 8,
        "Quantum\nLayers",
        ha='center', va='center',
        color='#BA55D3',
        fontsize=10,
        fontweight='bold'
    )
    
    ax_main.text(
        -1.5, 5,
        "Neural\nLayers",
        ha='center', va='center',
        color='#1E90FF',
        fontsize=10,
        fontweight='bold'
    )
    
    ax_main.text(
        -1.5, 1.5,
        "Pattern\nLayers",
        ha='center', va='center',
        color='#ADFF2F',
        fontsize=10,
        fontweight='bold'
    )
    
    # Plot layer metrics
    indices = [layer.get_info()['index'] for layer in layers]
    
    # Plot layer activity (placeholder with φ-harmonic pattern)
    ax_activity.clear()
    ax_activity.set_title('Layer Activity')
    
    # Generate φ-harmonic activities
    activities = [0.5 + 0.5 * np.sin(i * PHI) for i in range(len(indices))]
    
    ax_activity.bar(indices, activities, color=phi_cmap(np.linspace(0, 1, len(indices))))
    ax_activity.set_xlabel('Layer Index')
    ax_activity.set_ylabel('Activity')
    ax_activity.set_xticks(indices)
    ax_activity.set_ylim(0, 1)
    
    # Plot frequency spectrum
    ax_frequency.clear()
    ax_frequency.set_title('φ-Harmonic Frequencies')
    
    frequencies = [layer.frequency for layer in layers]
    ax_frequency.plot(indices, frequencies, 'o-', color='cyan')
    
    # Add φ-scaling curve
    x_fine = np.linspace(1, 9, 100)
    y_fine = 11.09 * (PHI ** (1 - x_fine))
    ax_frequency.plot(x_fine, y_fine, '--', color='gray', alpha=0.5)
    
    ax_frequency.set_xlabel('Layer Index')
    ax_frequency.set_ylabel('Frequency (Hz)')
    ax_frequency.set_xticks(indices)
    ax_frequency.set_yscale('log')
    ax_frequency.grid(True, alpha=0.3)
    
    # Plot energy distribution
    ax_energy.clear()
    ax_energy.set_title('φ-Scaled Energy')
    
    energies = [layer.energy for layer in layers]
    ax_energy.bar(indices, energies, color=phi_cmap(np.linspace(0, 1, len(indices))))
    
    # Add φ-scaling curve
    x_fine = np.linspace(1, 9, 100)
    y_fine = architecture.base_energy * (1 / (PHI ** (x_fine - 1)))
    ax_energy.plot(x_fine, y_fine, '--', color='gray', alpha=0.5)
    
    ax_energy.set_xlabel('Layer Index')
    ax_energy.set_ylabel('Energy')
    ax_energy.set_xticks(indices)
    
    # Plot size scaling
    ax_size.clear()
    ax_size.set_title('φ-Scaled Layer Size')
    
    sizes = [layer.size for layer in layers]
    ax_size.bar(indices, sizes, color=phi_cmap(np.linspace(0, 1, len(indices))))
    
    # Add φ-scaling curve
    x_fine = np.linspace(1, 9, 100)
    y_fine = architecture.base_size * (1 / (PHI ** (x_fine - 1)))
    ax_size.plot(x_fine, y_fine, '--', color='gray', alpha=0.5)
    
    ax_size.set_xlabel('Layer Index')
    ax_size.set_ylabel('Size')
    ax_size.set_xticks(indices)
    
    # Plot learning curve
    ax_learning.clear()
    ax_learning.set_title('φ-Harmonic Learning')
    
    # Generate φ-harmonic learning curve
    cycles = np.arange(20)
    errors = [np.exp(-t / PHI) for t in cycles]
    
    ax_learning.plot(cycles, errors, 'o-', color='orange')
    
    ax_learning.set_xlabel('Cycle')
    ax_learning.set_ylabel('Error')
    ax_learning.set_yscale('log')
    ax_learning.grid(True, alpha=0.3)
    
    # Plot quantum metrics
    ax_quantum.clear()
    ax_quantum.set_title('Quantum Bridge Metrics')
    
    # Generate φ-harmonic quantum metrics
    quantum_indices = [7, 8, 9]  # Bridge, Q-State, Quantum
    quantum_values = [1/PHI, 1/PHI**2, 1/PHI**3]
    
    ax_quantum.bar(quantum_indices, quantum_values, color=quantum_cmap(np.linspace(0, 1, len(quantum_indices))))
    
    # Add φ-coherence line
    ax_quantum.axhline(y=1/PHI, color='magenta', linestyle='--', alpha=0.5, label='φ-Coherence')
    
    ax_quantum.set_xlabel('Quantum Layer')
    ax_quantum.set_ylabel('φ-Coherence')
    ax_quantum.set_ylim(0, 1)
    ax_quantum.legend()
    
    # Save the figure
    plt.tight_layout()
    fig.savefig(filename, dpi=150)
    print(f"[φ] Figure saved to {filename}")
    
    return fig


if __name__ == "__main__":
    print(f"\n=== φ-HARMONIC NEURAL ARCHITECTURE STATIC VISUALIZER ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"φ^75 validation seal: {PHI_75:.2f}")
    
    # Create φ-harmonic neural architecture
    architecture = PhiHarmonicNeuralArchitecture(base_size=64)
    
    # Generate sample input (sine wave with φ-harmonic frequencies)
    x = np.linspace(0, 2*np.pi, architecture.layers[-1].size)
    input_data = np.sin(x) + 0.5 * np.sin(PHI * x) + 0.25 * np.sin(PHI**2 * x)
    
    # Process through architecture
    output = architecture.process(input_data)
    
    # Create visualization
    fig = visualize_phi_harmonic_architecture(architecture)
    
    print(f"\n[φ] φ-harmonic visualization complete")
    print(f"[φ] φ^75 validation seal: {PHI_75:.2f}")
    
    # Show the visualization
    plt.show()
