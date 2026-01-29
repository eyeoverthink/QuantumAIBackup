#!/usr/bin/env python3
"""
Quantum Phi-Harmonic CLI Interface
Interactive command-line interface for the Quantum Phi-Harmonic System
"""

import sys
import cmd
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import tempfile
import os
from typing import List, Dict, Any, Tuple, Optional

# Import the core system
from phi_core import QuantumPhiCore

class QuantumPhiCLI(cmd.Cmd):
    """Interactive CLI for Quantum Phi-Harmonic System"""
    
    intro = """
╔═══════════════════════════════════════════════════════════╗
║         QUANTUM PHI-HARMONIC COMPUTATIONAL SYSTEM         ║
║                     CLI Interface v3.14.15                 ║
╚═══════════════════════════════════════════════════════════╝

Core mathematical functionality based on phi-harmonic principles.
Type 'help' or '?' to list commands.
Type 'exit' or 'quit' to exit.
    """
    prompt = "\nφ> "
    
    def __init__(self):
        super().__init__()
        self.system = QuantumPhiCore()
        self.last_pattern = None
        self.last_tensor = None
        self.temp_dir = tempfile.mkdtemp(prefix="quantum_phi_")
        
    def do_status(self, arg):
        """Show current system status and parameters"""
        print("\n=== SYSTEM STATUS ===")
        print(f"Quantum Coherence: {self.system.quantum_coherence:.4f}")
        print(f"Phi Resonance:     {self.system.phi_resonance:.4f}")
        print(f"Phi Stability:     {self.system.phi_stability:.4f}")
        print(f"Active Dimensions: {self.system.active_dimensions}")
        print(f"Golden Ratio (φ):  {QuantumPhiCore.PHI:.10f}")
        print(f"1/φ:               {QuantumPhiCore.PHI_INVERSE:.10f}")
        
    def do_query(self, arg):
        """Process natural language query and adjust system parameters
        Usage: query <text>"""
        if not arg:
            print("Error: Query text required. Usage: query <text>")
            return
            
        response = self.system.process_query(arg)
        
        print("\n=== QUERY RESPONSE ===")
        print(f"{response['text']}")
        
        if any(change != 0 for change in response["changes"].values()):
            print("\n=== PARAMETER CHANGES ===")
            for param, change in response["changes"].items():
                if change != 0:
                    print(f"{param}: {change:+.4f}")
    
    def do_fractal(self, arg):
        """Generate fractal pattern with specified parameters
        Usage: fractal [depth=5] [density=1.0]"""
        args = arg.split()
        depth = 5
        density = 1.0
        
        if len(args) >= 1:
            try:
                depth = int(args[0])
            except ValueError:
                print("Error: Depth must be an integer")
                return
                
        if len(args) >= 2:
            try:
                density = float(args[1])
            except ValueError:
                print("Error: Density must be a number")
                return
        
        print(f"Generating fractal pattern with depth={depth}, density={density}...")
        self.last_pattern = self.system.generate_fractal_pattern(depth, density)
        
        print("\n=== FRACTAL PATTERN GENERATED ===")
        print(f"Nodes: {len(self.last_pattern['nodes'])}")
        print(f"Connections: {len(self.last_pattern['connections'])}")
        
        print("\n=== PATTERN METRICS ===")
        print(f"Phi Resonance:     {self.last_pattern['metrics']['phi_resonance']:.4f}")
        print(f"Quantum Coherence: {self.last_pattern['metrics']['quantum_coherence']:.4f}")
        print(f"Phi Stability:     {self.last_pattern['metrics']['phi_stability']:.4f}")
        
        # Save fractal data
        filename = os.path.join(self.temp_dir, "fractal_pattern.json")
        with open(filename, "w") as f:
            json.dump(self.last_pattern, f, indent=2)
        print(f"\nPattern saved to {filename}")
        
        print("\nUse 'plot fractal' to visualize the pattern")
        
    def do_tensor(self, arg):
        """Generate phi-harmonic tensor with specified dimensions
        Usage: tensor <dim1> [dim2] [dim3] ..."""
        args = arg.split()
        
        if not args:
            print("Error: At least one dimension required. Usage: tensor <dim1> [dim2] [dim3] ...")
            return
            
        dims = []
        for dim_str in args:
            try:
                dim = int(dim_str)
                if dim <= 0:
                    print(f"Error: Dimensions must be positive integers, got {dim}")
                    return
                dims.append(dim)
            except ValueError:
                print(f"Error: Dimensions must be integers, got {dim_str}")
                return
        
        print(f"Generating phi-harmonic tensor with dimensions {dims}...")
        self.last_tensor = self.system.generate_phi_harmonic_tensor(dims)
        
        print("\n=== TENSOR GENERATED ===")
        print(f"Shape: {self.last_tensor.shape}")
        print(f"Elements: {self.last_tensor.size}")
        
        # Analyze dimensions
        analysis = self.system.analyze_dimensions(self.last_tensor)
        
        print("\n=== DIMENSIONAL ANALYSIS ===")
        print(f"Quantum Coherence:       {analysis['quantum_coherence']:.4f}")
        print(f"Phi-Dimensional Harmony: {analysis['phi_dimensional_harmony']:.4f}")
        
        print("\n=== DIMENSION RESONANCE ===")
        for dim, resonance in analysis['dimension_resonance']:
            print(f"Dimension {dim}: {resonance:.4f}")
        
        # Save tensor
        filename = os.path.join(self.temp_dir, "phi_tensor.npy")
        np.save(filename, self.last_tensor)
        print(f"\nTensor saved to {filename}")
        
        print("\nUse 'plot tensor' to visualize the tensor")
    
    def do_analyze(self, arg):
        """Analyze sequence of numbers for phi-harmonic patterns
        Usage: analyze <num1> <num2> <num3> ..."""
        args = arg.split()
        
        if not args:
            print("Error: Sequence required. Usage: analyze <num1> <num2> <num3> ...")
            return
            
        values = []
        for val_str in args:
            try:
                val = float(val_str)
                values.append(val)
            except ValueError:
                print(f"Error: Values must be numbers, got {val_str}")
                return
        
        if len(values) < 2:
            print("Error: At least two values required for analysis")
            return
            
        print(f"Analyzing sequence: {values}")
        result = self.system.calculate_phi_pattern(values)
        
        print("\n=== SEQUENCE ANALYSIS ===")
        print(f"Phi Resonance:       {result['phi_resonance']:.4f}")
        print(f"Fibonacci Similarity: {result['fibonacci_similarity']:.4f}")
        
        if result['phi_ratios']:
            print("\n=== PHI RATIO LOCATIONS ===")
            for idx, ratio in result['phi_ratios']:
                print(f"Between positions {idx} and {idx+1}: {ratio:.4f}")
        
        if result['fibonacci_indices']:
            print("\n=== FIBONACCI-LIKE SEQUENCES ===")
            for idx in result['fibonacci_indices']:
                print(f"Positions {idx}, {idx+1}, {idx+2}: " +
                      f"{values[idx]} + {values[idx+1]} ≈ {values[idx+2]}")
            
        # Find optimal partition
        partition, resonance = self.system.find_optimal_phi_partition(values)
        
        print("\n=== OPTIMAL PHI PARTITION ===")
        if resonance > 0.5:
            print(f"Optimal partition at position {partition}")
            print(f"Left segment:  {values[:partition]} (sum: {sum(values[:partition]):.2f})")
            print(f"Right segment: {values[partition:]} (sum: {sum(values[partition:]):.2f})")
            print(f"Phi resonance: {resonance:.4f}")
        else:
            print("No strong phi resonance found in partitions")
    
    def do_plot(self, arg):
        """Visualize generated patterns or tensors
        Usage: plot <fractal|tensor|sequence> [output_file]"""
        args = arg.split()
        
        if not args:
            print("Error: Plot type required. Usage: plot <fractal|tensor|sequence> [output_file]")
            return
            
        plot_type = args[0].lower()
        
        if plot_type == "fractal":
            self._plot_fractal(args[1] if len(args) > 1 else None)
        elif plot_type == "tensor":
            self._plot_tensor(args[1] if len(args) > 1 else None)
        else:
            print(f"Error: Unknown plot type '{plot_type}'. Use fractal or tensor")
    
    def _plot_fractal(self, filename=None):
        """Plot fractal pattern"""
        if not self.last_pattern:
            print("Error: No fractal pattern available. Generate one with 'fractal' command first")
            return
            
        # Create figure
        fig, ax = plt.figure(figsize=(10, 10)), plt.gca()
        ax.set_aspect('equal')
        ax.set_title('Quantum Phi-Harmonic Fractal Pattern')
        ax.set_xlim(-200, 200)
        ax.set_ylim(-200, 200)
        ax.axis('off')
        
        # Set background color
        fig.patch.set_facecolor('#050510')
        ax.set_facecolor('#050510')
        
        # Plot connections
        for conn in self.last_pattern['connections']:
            src = self.last_pattern['nodes'][conn['source']]
            tgt = self.last_pattern['nodes'][conn['target']]
            ax.plot([src['x'], tgt['x']], [src['y'], tgt['y']], 
                   color=(0, 1, 1, conn['strength']), linewidth=0.8, zorder=1)
        
        # Plot nodes
        for node in self.last_pattern['nodes']:
            size = node['size'] * 20
            color = plt.cm.cool(1 - node['level'] / 5)
            ax.scatter(node['x'], node['y'], s=size, color=color, 
                      alpha=0.7, edgecolor='none', zorder=2)
        
        # Add phi symbol and metrics
        metrics_text = (
            f"φ Resonance: {self.last_pattern['metrics']['phi_resonance']:.2f}\n"
            f"Q Coherence: {self.last_pattern['metrics']['quantum_coherence']:.2f}\n"
            f"φ Stability:  {self.last_pattern['metrics']['phi_stability']:.2f}"
        )
        ax.text(0.02, 0.98, metrics_text, transform=ax.transAxes, 
               color='#00FFFF', fontsize=12, va='top', family='monospace')
        
        # Add phi symbol
        ax.text(0.5, 0.5, "Φ", transform=ax.transAxes, color='#FFBF00', 
               fontsize=100, va='center', ha='center', alpha=0.2, family='serif')
        
        # Save or show
        if filename:
            plt.savefig(filename, dpi=150, bbox_inches='tight')
            print(f"Plot saved to {filename}")
        else:
            temp_file = os.path.join(self.temp_dir, "fractal_plot.png")
            plt.savefig(temp_file, dpi=150, bbox_inches='tight')
            plt.close()
            print(f"Plot saved to {temp_file}")
    
    def _plot_tensor(self, filename=None):
        """Plot tensor visualization"""
        if self.last_tensor is None:
            print("Error: No tensor available. Generate one with 'tensor' command first")
            return
            
        # Check tensor dimensions
        dims = self.last_tensor.shape
        
        if len(dims) == 1:
            # 1D tensor visualization
            fig, ax = plt.subplots(figsize=(10, 6))
            x = np.arange(dims[0])
            ax.plot(x, self.last_tensor, 'o-', color='#00AAFF', linewidth=2, markersize=5)
            ax.set_title('Phi-Harmonic 1D Tensor')
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            ax.grid(alpha=0.3)
            
            # Calculate phi-pattern
            result = self.system.calculate_phi_pattern(self.last_tensor)
            
            # Add phi ratios
            for idx, ratio in result['phi_ratios']:
                ax.plot([idx, idx+1], [self.last_tensor[idx], self.last_tensor[idx+1]], 
                       'o-', color='#FFBF00', linewidth=3, markersize=7)
            
            # Add metrics
            metrics_text = (
                f"φ Resonance: {result['phi_resonance']:.2f}\n"
                f"Fibonacci:   {result['fibonacci_similarity']:.2f}"
            )
            ax.text(0.02, 0.98, metrics_text, transform=ax.transAxes, 
                   color='#00FFFF', fontsize=12, va='top', family='monospace')
            
        elif len(dims) == 2:
            # 2D tensor visualization
            fig, ax = plt.subplots(figsize=(10, 8))
            
            # Create custom colormap (teal to amber)
            colors = [(0, 0.5, 0.5), (1, 0.75, 0)]  # Teal to amber
            cmap = LinearSegmentedColormap.from_list('phi_cmap', colors, N=100)
            
            im = ax.imshow(self.last_tensor, cmap=cmap, interpolation='nearest')
            ax.set_title('Phi-Harmonic 2D Tensor')
            fig.colorbar(im, ax=ax, label='Value')
            
            # Add phi symbol
            ax.text(dims[1]/2, dims[0]/2, "Φ", color='white', 
                   fontsize=min(dims)/2, va='center', ha='center', alpha=0.3, family='serif')
            
            # Add dimensional analysis
            analysis = self.system.analyze_dimensions(self.last_tensor)
            metrics_text = (
                f"Q Coherence:   {analysis['quantum_coherence']:.2f}\n"
                f"φ Dim Harmony: {analysis['phi_dimensional_harmony']:.2f}"
            )
            ax.text(0.02, 0.98, metrics_text, transform=ax.transAxes, 
                   color='white', fontsize=12, va='top', family='monospace', 
                   bbox=dict(facecolor='black', alpha=0.7, boxstyle='round'))
            
        else:
            # 3D+ tensor visualization (slice through the first 2 dimensions)
            fig, axs = plt.subplots(1, min(3, dims[2]), figsize=(15, 5))
            if min(3, dims[2]) == 1:
                axs = [axs]
                
            # Create custom colormap
            colors = [(0, 0.5, 0.5), (1, 0.75, 0)]  # Teal to amber
            cmap = LinearSegmentedColormap.from_list('phi_cmap', colors, N=100)
            
            for i, ax in enumerate(axs):
                if i < dims[2]:
                    im = ax.imshow(self.last_tensor[:,:,i], cmap=cmap, interpolation='nearest')
                    ax.set_title(f'Slice {i}')
                    fig.colorbar(im, ax=ax)
                
            plt.suptitle(f'Phi-Harmonic {len(dims)}D Tensor (First {len(axs)} Slices)')
            
            # Add dimensional analysis
            analysis = self.system.analyze_dimensions(self.last_tensor)
            metrics_text = (
                f"Tensor Shape: {dims}\n"
                f"Q Coherence: {analysis['quantum_coherence']:.2f}\n"
                f"φ Dim Harmony: {analysis['phi_dimensional_harmony']:.2f}"
            )
            axs[0].text(-0.1, 1.1, metrics_text, transform=axs[0].transAxes, 
                       color='black', fontsize=12, va='top', family='monospace')
        
        # Set background color
        fig.patch.set_facecolor('#F8F8F8')
        
        # Save or show
        if filename:
            plt.savefig(filename, dpi=150, bbox_inches='tight')
            print(f"Plot saved to {filename}")
        else:
            temp_file = os.path.join(self.temp_dir, "tensor_plot.png")
            plt.savefig(temp_file, dpi=150, bbox_inches='tight')
            plt.close()
            print(f"Plot saved to {temp_file}")
    
    def do_save(self, arg):
        """Save current system state, pattern or tensor
        Usage: save <state|pattern|tensor> <filename>"""
        args = arg.split()
        
        if len(args) < 2:
            print("Error: Both type and filename required. Usage: save <state|pattern|tensor> <filename>")
            return
            
        save_type = args[0].lower()
        filename = args[1]
        
        if save_type == "state":
            state = {
                "quantum_coherence": self.system.quantum_coherence,
                "phi_resonance": self.system.phi_resonance,
                "phi_stability": self.system.phi_stability,
                "active_dimensions": self.system.active_dimensions
            }
            
            with open(filename, "w") as f:
                json.dump(state, f, indent=2)
                
            print(f"System state saved to {filename}")
            
        elif save_type == "pattern":
            if not self.last_pattern:
                print("Error: No pattern available. Generate one with 'fractal' command first")
                return
                
            with open(filename, "w") as f:
                json.dump(self.last_pattern, f, indent=2)
                
            print(f"Fractal pattern saved to {filename}")
            
        elif save_type == "tensor":
            if self.last_tensor is None:
                print("Error: No tensor available. Generate one with 'tensor' command first")
                return
                
            np.save(filename, self.last_tensor)
            print(f"Tensor saved to {filename}")
            
        else:
            print(f"Error: Unknown save type '{save_type}'. Use state, pattern, or tensor")
    
    def do_load(self, arg):
        """Load system state from file
        Usage: load <filename>"""
        if not arg:
            print("Error: Filename required. Usage: load <filename>")
            return
            
        try:
            with open(arg, "r") as f:
                state = json.load(f)
                
            if isinstance(state, dict):
                if "quantum_coherence" in state:
                    self.system.quantum_coherence = state["quantum_coherence"]
                if "phi_resonance" in state:
                    self.system.phi_resonance = state["phi_resonance"]
                if "phi_stability" in state:
                    self.system.phi_stability = state["phi_stability"]
                if "active_dimensions" in state:
                    self.system.active_dimensions = state["active_dimensions"]
                    
                print(f"System state loaded from {arg}")
                self.do_status("")
            else:
                print("Error: Invalid state file format")
                
        except Exception as e:
            print(f"Error loading state: {e}")
    
    def do_exit(self, arg):
        """Exit the program"""
        print("\nExiting Quantum Phi-Harmonic System. Phi guide you!")
        return True
        
    def do_quit(self, arg):
        """Exit the program"""
        return self.do_exit(arg)
        
    def do_EOF(self, arg):
        """Exit on Ctrl-D"""
        print("")
        return self.do_exit(arg)
        
    def default(self, line):
        """Handle unknown commands"""
        if line.strip():
            print(f"Unknown command: {line}")
            print("Type 'help' or '?' to list available commands")


if __name__ == "__main__":
    QuantumPhiCLI().cmdloop()