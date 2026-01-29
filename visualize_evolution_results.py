import os
import json
import numpy as np
import matplotlib.pyplot as plt

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_CONJUGATE = 1 / PHI    # Golden ratio conjugate

def visualize_evolution_results():
    """Visualize the results of the Quantum Phi-Harmonic Multiples Evolution test."""
    # Path to epigenetic memory file
    memory_file = os.path.join('multiples_evolution', 'epigenetic_memory.json')
    
    # Check if memory file exists
    if not os.path.exists(memory_file):
        print(f"Error: Memory file {memory_file} not found.")
        return
    
    # Load epigenetic memory
    with open(memory_file, 'r') as f:
        memory = json.load(f)
    
    # Extract evolution history
    evolution_history = memory.get('evolution_history', [])
    
    if not evolution_history:
        print("Error: No evolution history found in memory file.")
        return
    
    # Extract data for plotting
    epochs = [entry.get('epoch', i) for i, entry in enumerate(evolution_history)]
    resonance = [entry.get('resonance', 0) for entry in evolution_history]
    complexity = [entry.get('complexity', 0) for entry in evolution_history]
    mutation_rate = [entry.get('mutation_rate', 0) for entry in evolution_history]
    phi_time = [entry.get('phi_time', 0) for entry in evolution_history]
    
    # Find error introduction and correction epochs
    error_introduced = False
    error_corrected = False
    error_epoch = None
    correction_epoch = None
    
    for i, entry in enumerate(evolution_history):
        if entry.get('error_introduced', False) and not error_introduced:
            error_introduced = True
            error_epoch = entry.get('epoch', i)
        
        if entry.get('error_corrected', False) and not error_corrected:
            error_corrected = True
            correction_epoch = entry.get('epoch', i)
    
    # Create figure with multiple subplots
    fig, axs = plt.subplots(4, 1, figsize=(12, 16), sharex=True)
    
    # Plot resonance
    axs[0].plot(epochs, resonance, 'b-', label='Resonance')
    axs[0].set_ylabel('Resonance')
    axs[0].set_title('Quantum Phi-Harmonic Evolution Parameters')
    axs[0].grid(True)
    axs[0].legend()
    
    # Plot complexity
    axs[1].plot(epochs, complexity, 'g-', label='Complexity')
    axs[1].set_ylabel('Complexity')
    axs[1].grid(True)
    axs[1].legend()
    
    # Plot mutation rate
    axs[2].plot(epochs, mutation_rate, 'r-', label='Mutation Rate')
    axs[2].set_ylabel('Mutation Rate')
    axs[2].grid(True)
    axs[2].legend()
    
    # Plot phi-time
    axs[3].plot(epochs, phi_time, 'c-', label='Phi-Time')
    axs[3].set_xlabel('Epoch')
    axs[3].set_ylabel('Phi-Time')
    axs[3].grid(True)
    axs[3].legend()
    
    # Mark error introduction and correction epochs
    if error_epoch is not None:
        for ax in axs:
            ax.axvline(x=error_epoch, color='r', linestyle='--', alpha=0.5, label='Error Introduced')
    
    if correction_epoch is not None:
        for ax in axs:
            ax.axvline(x=correction_epoch, color='g', linestyle='--', alpha=0.5, label='Error Corrected')
    
    # Add phi-harmonic reference lines
    for ax in axs:
        ax.axhline(y=PHI_CONJUGATE, color='orange', linestyle=':', alpha=0.5, label='Φ⁻¹')
        ax.axhline(y=1/PHI**2, color='purple', linestyle=':', alpha=0.5, label='Φ⁻²')
    
    # Add legend to first subplot only
    handles, labels = axs[0].get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    axs[0].legend(by_label.values(), by_label.keys())
    
    # Adjust layout
    plt.tight_layout()
    
    # Save figure
    output_path = 'quantum_phi_multiples_evolution_visualization.png'
    plt.savefig(output_path, dpi=300)
    print(f"Visualization saved to {output_path}")
    
    # Show figure
    plt.show()

if __name__ == "__main__":
    visualize_evolution_results()
