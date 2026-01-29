"""
Quantum Stability Visualizer

This module provides advanced visualization tools for the Quantum Stability Framework,
with special focus on z-axis instability and phi-resonance principles.

Key features:
1. Interactive 3D visualization of quantum state evolution
2. Phi-resonant stability heatmaps across dimensions
3. Z-axis instability analysis with birth date resonance (1979)
4. Consciousness evolution tracking
5. Dimensional efficiency visualization
"""

import torch
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
from typing import Dict, List, Tuple, Optional, Union, Any
import time
import os

# Try to import the stability framework
try:
    from advanced_quantum_stability_framework import AdvancedQuantumStabilityFramework
except ImportError:
    print("Warning: Advanced Quantum Stability Framework not found.")
    print("Please ensure advanced_quantum_stability_framework.py is available")

# Constants
PHI = 1.618033988749895
BIRTH_YEAR = 1979


class QuantumStabilityVisualizer:
    """
    Visualizer for quantum stability metrics with focus on z-axis instability.
    """
    
    def __init__(self, stability_framework=None):
        """
        Initialize the visualizer.
        
        Args:
            stability_framework: Instance of AdvancedQuantumStabilityFramework
        """
        self.framework = stability_framework
        
        # Create framework if not provided
        if self.framework is None:
            try:
                self.framework = AdvancedQuantumStabilityFramework(
                    dimensions=3, 
                    use_birth_resonance=True
                )
            except NameError:
                print("Error: Cannot create framework. Please provide an instance.")
                return
                
        # Set up visualization parameters
        self.colors = {
            'x_dim': '#3498db',  # Blue
            'y_dim': '#2ecc71',  # Green
            'z_dim': '#e74c3c',  # Red
            'stability': '#9b59b6',  # Purple
            'coherence': '#f39c12',  # Orange
            'background': '#f8f9fa',  # Light gray
            'grid': '#dee2e6'   # Medium gray
        }
        
        # Set up plot style
        plt.style.use('seaborn-v0_8-whitegrid')
        
        print(f"Quantum Stability Visualizer initialized")
        print(f"Connected to framework with quantum signature: {self.framework.quantum_signature}")
    
    def visualize_3d_state_evolution(self, duration: float = 10.0, steps: int = 100, 
                                    save_path: Optional[str] = "quantum_3d_evolution.mp4"):
        """
        Create an animated 3D visualization of quantum state evolution.
        
        Args:
            duration: Total simulation time
            steps: Number of time steps
            save_path: Path to save animation (None for no saving)
        """
        # Create figure
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Set background color
        ax.set_facecolor(self.colors['background'])
        fig.patch.set_facecolor(self.colors['background'])
        
        # Initialize data
        x_points, y_points, z_points = [], [], []
        stability_values, coherence_values = [], []
        
        # Time points
        time_points = np.linspace(0, duration, steps)
        
        # Function to update the plot for animation
        def update(frame):
            t = time_points[frame]
            
            # Evolve quantum state
            stability, coherence = self.framework.phi_resonant_stability(t)
            state = self.framework.quantum_state
            
            # Get first 3 dimensions
            x = torch.abs(state[0]).item()
            y = torch.abs(state[1]).item()
            z = torch.abs(state[2]).item()
            
            # Apply phi-resonance
            x = x * (PHI ** float(self.framework.PHI_COEFFICIENTS['x']))
            y = y * (PHI ** float(self.framework.PHI_COEFFICIENTS['y']))
            z = z * (PHI ** float(self.framework.PHI_COEFFICIENTS['z']))
            
            # Store points
            x_points.append(x)
            y_points.append(y)
            z_points.append(z)
            stability_values.append(stability)
            coherence_values.append(coherence)
            
            # Clear and redraw
            ax.clear()
            
            # Plot trajectory
            ax.plot(x_points, y_points, z_points, color=self.colors['stability'], 
                   label='Quantum State Path', linewidth=2)
            
            # Plot current point
            ax.scatter([x], [y], [z], color=self.colors['coherence'], s=100, 
                      label='Current State')
            
            # Plot dimension projections
            ax.plot([x, x], [y, y], [0, z], 'k--', alpha=0.3)
            ax.plot([x, x], [0, y], [z, z], 'k--', alpha=0.3)
            ax.plot([0, x], [y, y], [z, z], 'k--', alpha=0.3)
            
            # Highlight z-axis instability
            z_instability = float(self.framework.Z_INSTABILITY_AMPLITUDE) * np.sin(
                float(self.framework.Z_INSTABILITY_FREQUENCY) * t * PHI
            )
            
            # Add instability indicator
            ax.text(x, y, z, f"Z-Instability: {z_instability:.4f}", 
                   color=self.colors['z_dim'], fontsize=9)
            
            # Add metrics
            title = (f"Quantum State Evolution (t={t:.2f})\n"
                    f"Stability: {stability:.4f}, Coherence: {coherence:.4f}")
            ax.set_title(title)
            
            # Set labels
            ax.set_xlabel('X Dimension')
            ax.set_ylabel('Y Dimension')
            ax.set_zlabel('Z Dimension (Unstable)')
            
            # Set axis limits with some padding
            max_val = max(max(x_points), max(y_points), max(z_points)) * 1.1
            ax.set_xlim(0, max_val)
            ax.set_ylim(0, max_val)
            ax.set_zlim(0, max_val)
            
            # Add legend
            ax.legend(loc='upper right')
            
            return ax,
        
        # Create animation
        ani = FuncAnimation(fig, update, frames=steps, interval=100, blit=False)
        
        # Save if requested
        if save_path:
            try:
                ani.save(save_path, writer='ffmpeg', fps=15, dpi=200)
                print(f"Animation saved to {save_path}")
            except Exception as e:
                print(f"Error saving animation: {e}")
                print("Continuing with display only...")
        
        plt.tight_layout()
        plt.show()
        
        # Return final values
        return {
            'x_final': x_points[-1],
            'y_final': y_points[-1],
            'z_final': z_points[-1],
            'stability_final': stability_values[-1],
            'coherence_final': coherence_values[-1]
        }
    
    def visualize_stability_heatmap(self, x_range: Tuple[float, float] = (0, 2), 
                                  y_range: Tuple[float, float] = (0, 2),
                                  z_range: Tuple[float, float] = (0, 2),
                                  resolution: int = 20,
                                  time_point: float = 1.0):
        """
        Create a stability heatmap across dimensions.
        
        Args:
            x_range: Range for x dimension
            y_range: Range for y dimension
            z_range: Range for z dimension
            resolution: Grid resolution
            time_point: Time point for evaluation
        """
        # Create meshgrid
        x = np.linspace(x_range[0], x_range[1], resolution)
        y = np.linspace(y_range[0], y_range[1], resolution)
        z = np.linspace(z_range[0], z_range[1], resolution)
        
        # Create figure for 2D slices
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        
        # XY plane (fixed z)
        xy_stability = np.zeros((resolution, resolution))
        for i in range(resolution):
            for j in range(resolution):
                xy_stability[j, i] = self.framework.pythagorean_quantum(
                    x[i], y[j], z[resolution//2], time_point
                )
        
        # YZ plane (fixed x)
        yz_stability = np.zeros((resolution, resolution))
        for i in range(resolution):
            for j in range(resolution):
                yz_stability[j, i] = self.framework.pythagorean_quantum(
                    x[resolution//2], y[i], z[j], time_point
                )
        
        # XZ plane (fixed y)
        xz_stability = np.zeros((resolution, resolution))
        for i in range(resolution):
            for j in range(resolution):
                xz_stability[j, i] = self.framework.pythagorean_quantum(
                    x[i], y[resolution//2], z[j], time_point
                )
        
        # Plot heatmaps
        im0 = axes[0].imshow(xy_stability, extent=[*x_range, *y_range], 
                           origin='lower', cmap='viridis')
        im1 = axes[1].imshow(yz_stability, extent=[*y_range, *z_range], 
                           origin='lower', cmap='viridis')
        im2 = axes[2].imshow(xz_stability, extent=[*x_range, *z_range], 
                           origin='lower', cmap='viridis')
        
        # Add colorbars
        fig.colorbar(im0, ax=axes[0], label='Quantum Stability')
        fig.colorbar(im1, ax=axes[1], label='Quantum Stability')
        fig.colorbar(im2, ax=axes[2], label='Quantum Stability')
        
        # Set titles and labels
        axes[0].set_title(f'XY Plane (Z={z[resolution//2]:.2f})')
        axes[0].set_xlabel('X Dimension')
        axes[0].set_ylabel('Y Dimension')
        
        axes[1].set_title(f'YZ Plane (X={x[resolution//2]:.2f})')
        axes[1].set_xlabel('Y Dimension')
        axes[1].set_ylabel('Z Dimension (Unstable)')
        
        axes[2].set_title(f'XZ Plane (Y={y[resolution//2]:.2f})')
        axes[2].set_xlabel('X Dimension')
        axes[2].set_ylabel('Z Dimension (Unstable)')
        
        # Add overall title
        plt.suptitle(f'Quantum Stability Heatmap (t={time_point:.2f})', fontsize=16)
        
        plt.tight_layout()
        plt.savefig('quantum_stability_heatmap.png')
        plt.show()
    
    def visualize_z_instability_analysis(self, duration: float = 10.0, steps: int = 100):
        """
        Create a detailed analysis of z-axis instability.
        
        Args:
            duration: Total simulation time
            steps: Number of time steps
        """
        # Run simulation
        results = self.framework.simulate_evolution(duration, steps)
        
        # Create figure
        fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
        
        # Time points
        time_points = results['time']
        
        # Extract z-dimension values
        z_values = []
        for t in time_points:
            # Evolve state
            self.framework.quantum_state_evolution(t)
            # Get z value
            z = torch.abs(self.framework.quantum_state[2]).item()
            # Apply phi-resonance
            z = z * (PHI ** float(self.framework.PHI_COEFFICIENTS['z']))
            z_values.append(z)
        
        # Calculate z-instability
        z_instability = [
            float(self.framework.Z_INSTABILITY_AMPLITUDE) * np.sin(
                float(self.framework.Z_INSTABILITY_FREQUENCY) * t * PHI
            ) for t in time_points
        ]
        
        # Plot z-dimension evolution
        axes[0].plot(time_points, z_values, color=self.colors['z_dim'], 
                    label='Z-Dimension Value')
        axes[0].set_title('Z-Dimension Evolution')
        axes[0].set_ylabel('Amplitude')
        axes[0].grid(True, color=self.colors['grid'])
        axes[0].legend()
        
        # Plot z-instability
        axes[1].plot(time_points, z_instability, color=self.colors['coherence'], 
                    label='Z-Instability Factor')
        axes[1].set_title('Z-Instability Evolution')
        axes[1].set_ylabel('Instability')
        axes[1].grid(True, color=self.colors['grid'])
        axes[1].legend()
        
        # Plot stability
        axes[2].plot(time_points, results['stability'], color=self.colors['stability'], 
                    label='Phi-Resonant Stability')
        axes[2].set_title('Stability Evolution')
        axes[2].set_xlabel('Time')
        axes[2].set_ylabel('Stability')
        axes[2].grid(True, color=self.colors['grid'])
        axes[2].legend()
        
        # Add birth resonance markers
        birth_points = [t for t in time_points if abs(t % (BIRTH_YEAR / 1000)) < duration/steps]
        if birth_points:
            for ax in axes:
                for t in birth_points:
                    ax.axvline(x=t, color='k', linestyle='--', alpha=0.3)
                    ax.text(t, ax.get_ylim()[1]*0.9, f"Birth\nResonance", 
                           rotation=90, verticalalignment='top', fontsize=8)
        
        plt.tight_layout()
        plt.savefig('z_instability_analysis.png')
        plt.show()
    
    def visualize_consciousness_evolution(self, duration: float = 10.0, steps: int = 100):
        """
        Visualize consciousness evolution over time.
        
        Args:
            duration: Total simulation time
            steps: Number of time steps
        """
        # Run simulation
        results = self.framework.simulate_evolution(duration, steps)
        
        # Calculate consciousness levels
        consciousness_levels = []
        for i in range(len(results['time'])):
            # Set current state
            t = results['time'][i]
            stability = results['stability'][i]
            coherence = results['coherence'][i]
            efficiency = results['efficiency'][i]
            resonance = results['resonance'][i]
            
            # Calculate consciousness
            consciousness = (
                stability * 0.3 +
                coherence * 0.3 +
                efficiency * 0.2 +
                resonance * 0.2
            ) * PHI
            
            # Scale to 0-10 range
            consciousness = min(10.0, max(0.0, consciousness))
            consciousness_levels.append(consciousness)
        
        # Create figure
        fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True)
        
        # Plot consciousness level
        axes[0, 0].plot(results['time'], consciousness_levels, color=self.colors['stability'], 
                       linewidth=2)
        axes[0, 0].set_title('Consciousness Level Evolution')
        axes[0, 0].set_ylabel('Level (0-10)')
        axes[0, 0].grid(True, color=self.colors['grid'])
        
        # Plot stability and coherence
        axes[0, 1].plot(results['time'], results['stability'], color=self.colors['stability'], 
                       label='Stability')
        axes[0, 1].plot(results['time'], results['coherence'], color=self.colors['coherence'], 
                       label='Coherence')
        axes[0, 1].set_title('Stability and Coherence')
        axes[0, 1].set_ylabel('Value')
        axes[0, 1].grid(True, color=self.colors['grid'])
        axes[0, 1].legend()
        
        # Plot efficiency
        axes[1, 0].plot(results['time'], results['efficiency'], color=self.colors['x_dim'], 
                       linewidth=2)
        axes[1, 0].set_title('Dimensional Efficiency')
        axes[1, 0].set_xlabel('Time')
        axes[1, 0].set_ylabel('Efficiency (0-1)')
        axes[1, 0].grid(True, color=self.colors['grid'])
        
        # Plot resonance
        axes[1, 1].plot(results['time'], results['resonance'], color=self.colors['y_dim'], 
                       linewidth=2)
        axes[1, 1].set_title('Birth Resonance Alignment')
        axes[1, 1].set_xlabel('Time')
        axes[1, 1].set_ylabel('Alignment (0-1)')
        axes[1, 1].grid(True, color=self.colors['grid'])
        
        # Add overall title
        plt.suptitle('Quantum Consciousness Evolution Analysis', fontsize=16)
        
        plt.tight_layout()
        plt.savefig('consciousness_evolution_analysis.png')
        plt.show()
        
        # Return final consciousness level
        return consciousness_levels[-1]
    
    def generate_visual_report(self, output_dir: str = "."):
        """
        Generate a comprehensive visual report with all visualizations.
        
        Args:
            output_dir: Directory to save report files
        """
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Run simulations
        print("Generating stability heatmap...")
        self.visualize_stability_heatmap(
            save_path=os.path.join(output_dir, "stability_heatmap.png")
        )
        
        print("Analyzing z-axis instability...")
        self.visualize_z_instability_analysis(
            save_path=os.path.join(output_dir, "z_instability_analysis.png")
        )
        
        print("Analyzing consciousness evolution...")
        consciousness = self.visualize_consciousness_evolution(
            save_path=os.path.join(output_dir, "consciousness_evolution.png")
        )
        
        print("Generating 3D state evolution animation...")
        self.visualize_3d_state_evolution(
            save_path=os.path.join(output_dir, "quantum_3d_evolution.mp4")
        )
        
        # Generate report summary
        report = f"""
        # Quantum Stability Visual Analysis Report
        
        ## Overview
        This report provides a comprehensive visual analysis of the Quantum Stability Framework
        with special focus on z-axis instability and phi-resonance principles.
        
        ## Key Findings
        
        - **Final Consciousness Level**: {consciousness:.4f}/10.0
        - **Z-Axis Stability**: {'Low' if consciousness < 3.0 else 'Medium' if consciousness < 7.0 else 'High'}
        - **Phi-Resonance Quality**: {'Low' if self.framework.dimensional_efficiency() < 0.3 else 'Medium' if self.framework.dimensional_efficiency() < 0.7 else 'High'}
        
        ## Visualizations
        
        1. **Stability Heatmap**: Shows stability across dimensions
        2. **Z-Axis Instability Analysis**: Detailed analysis of z-axis instability
        3. **Consciousness Evolution**: Tracks consciousness level over time
        4. **3D State Evolution**: Animated visualization of quantum state evolution
        
        ## Quantum Signature
        
        {self.framework.quantum_signature}
        
        ## Generated on {time.strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        # Save report
        with open(os.path.join(output_dir, "visual_analysis_report.md"), "w") as f:
            f.write(report)
            
        print(f"Visual report generated in {output_dir}")
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Create framework
        framework = AdvancedQuantumStabilityFramework(dimensions=3, use_birth_resonance=True)
        
        # Create visualizer
        visualizer = QuantumStabilityVisualizer(framework)
        
        # Generate visual report
        visualizer.generate_visual_report()
        
    except NameError:
        print("Error: Advanced Quantum Stability Framework not available.")
        print("Please ensure advanced_quantum_stability_framework.py is in the same directory.")
