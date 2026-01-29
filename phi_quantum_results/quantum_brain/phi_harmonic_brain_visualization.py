#!/usr/bin/env python3
"""
Phi-Harmonic Brain Visualization Module

A module for visualizing the Phi-Harmonic Brain system, including its quantum states,
layer activities, resonance patterns, and phi-harmonic interactions.

This module extends the brain system with visualization capabilities without modifying
core components, following the "lego" design philosophy.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import time
from typing import Dict, List, Tuple, Any, Optional, Union
import logging

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

# Import brain components
from phi_harmonic_brain_core import (
    PhiHarmonicBrain, PhiHarmonicLayer,
    PHI, PHI_INV, PHI_SQUARED, PHI_CUBED,
    EARTH_FREQUENCY, MOON_FREQUENCY, BRAIN_FREQUENCY
)
from phi_harmonic_brain_io import PhiHarmonicBrainIO
from phi_harmonic_brain_integration import PhiHarmonicBrainSystem

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('phi_brain_viz')

class PhiHarmonicBrainVisualizer:
    """
    Visualizes the Phi-Harmonic Brain system's quantum states and phi-harmonic patterns.
    """
    
    def __init__(self, brain_system: Union[PhiHarmonicBrain, PhiHarmonicBrainIO, PhiHarmonicBrainSystem] = None):
        """
        Initialize the brain visualizer.
        
        Args:
            brain_system: Brain system to visualize (Brain, BrainIO, or BrainSystem)
        """
        # Initialize brain component
        if brain_system is None:
            # Create default brain
            self.brain = PhiHarmonicBrain()
            self.brain_io = None
            self.brain_system = None
        elif isinstance(brain_system, PhiHarmonicBrain):
            # Use provided brain
            self.brain = brain_system
            self.brain_io = None
            self.brain_system = None
        elif isinstance(brain_system, PhiHarmonicBrainIO):
            # Use brain from IO system
            self.brain_io = brain_system
            self.brain = brain_system.brain
            self.brain_system = None
        elif isinstance(brain_system, PhiHarmonicBrainSystem):
            # Use brain from integrated system
            self.brain_system = brain_system
            self.brain = brain_system.brain
            self.brain_io = brain_system.brain_io
        else:
            # Default to new brain
            self.brain = PhiHarmonicBrain()
            self.brain_io = None
            self.brain_system = None
        
        # Initialize visualization state
        self.layer_activities = {}
        self.resonance_history = {
            "earth": [],
            "moon": [],
            "brain": []
        }
        self.energy_history = []
        self.coherence_history = []
        self.time_points = []
        
        # Animation components
        self.fig = None
        self.animation = None
        self.is_animating = False
        
        # Phi-harmonic color map
        self.phi_colors = self._generate_phi_colors()
        
        logger.info("PhiHarmonicBrainVisualizer initialized")
        logger.info(f"Connected to brain with fingerprint: {self.brain.quantum_fingerprint}")
    
    def _generate_phi_colors(self, n_colors: int = 9) -> List[Tuple[float, float, float]]:
        """Generate phi-harmonic color sequence."""
        colors = []
        
        for i in range(n_colors):
            # Use golden angle in HSV color space (phi-based)
            hue = (i * PHI) % 1.0
            
            # Phi-scaled saturation and value
            saturation = 0.5 + 0.5 * math.sin(i * PHI_INV * math.pi)
            value = 0.5 + 0.5 * math.cos(i * PHI_INV * math.pi)
            
            # Convert HSV to RGB
            h = hue * 6.0
            c = value * saturation
            x = c * (1 - abs(h % 2 - 1))
            m = value - c
            
            if h < 1:
                r, g, b = c, x, 0
            elif h < 2:
                r, g, b = x, c, 0
            elif h < 3:
                r, g, b = 0, c, x
            elif h < 4:
                r, g, b = 0, x, c
            elif h < 5:
                r, g, b = x, 0, c
            else:
                r, g, b = c, 0, x
            
            # Add offset
            r, g, b = r + m, g + m, b + m
            
            colors.append((r, g, b))
        
        return colors
    
    def _capture_brain_state(self) -> Dict[str, Any]:
        """Capture the current state of the brain for visualization."""
        # Get layer activities
        self.layer_activities = {}
        
        # Access layers directly from the list
        for i, layer in enumerate(self.brain.layers):
            layer_name = layer.name
            if hasattr(layer, 'last_output'):
                self.layer_activities[layer_name] = layer.last_output
        
        # Get resonances
        if self.brain_io:
            earth_res = self.brain_io.get_earth_resonance()
            moon_res = self.brain_io.get_moon_resonance()
            brain_res = self.brain_io.get_brain_resonance()
        elif self.brain_system:
            resonances = self.brain_system.get_earth_moon_brain_resonance()
            earth_res = resonances["earth"]
            moon_res = resonances["moon"]
            brain_res = resonances["brain"]
        else:
            freq_analysis = self.brain.frequency_analysis()
            earth_res = freq_analysis["earth_resonance"]
            moon_res = freq_analysis["moon_resonance"]
            brain_res = freq_analysis["brain_resonance"]
        
        # Get brain state
        brain_state = self.brain.get_state()
        energy = brain_state["energy"]
        coherence = brain_state["coherence"]
        
        # Update histories
        self.resonance_history["earth"].append(earth_res)
        self.resonance_history["moon"].append(moon_res)
        self.resonance_history["brain"].append(brain_res)
        self.energy_history.append(energy)
        self.coherence_history.append(coherence)
        self.time_points.append(time.time())
        
        # Limit history length
        max_history = 100
        if len(self.time_points) > max_history:
            self.time_points = self.time_points[-max_history:]
            self.energy_history = self.energy_history[-max_history:]
            self.coherence_history = self.coherence_history[-max_history:]
            self.resonance_history["earth"] = self.resonance_history["earth"][-max_history:]
            self.resonance_history["moon"] = self.resonance_history["moon"][-max_history:]
            self.resonance_history["brain"] = self.resonance_history["brain"][-max_history:]
        
        # Return current state
        return {
            "layer_activities": self.layer_activities,
            "resonances": {
                "earth": earth_res,
                "moon": moon_res,
                "brain": brain_res
            },
            "energy": energy,
            "coherence": coherence,
            "timestamp": time.time()
        }
    
    def visualize_brain_state(self) -> plt.Figure:
        """
        Create a static visualization of the current brain state.
        
        Returns:
            Matplotlib figure
        """
        # Capture brain state
        state = self._capture_brain_state()
        
        # Create figure with subplots
        fig = plt.figure(figsize=(15, 10))
        fig.suptitle(f"Phi-Harmonic Brain State: {self.brain.quantum_fingerprint}", fontsize=16)
        
        # Layer activities plot
        ax1 = fig.add_subplot(2, 2, 1)
        self._plot_layer_activities(ax1, state["layer_activities"])
        
        # Resonances plot
        ax2 = fig.add_subplot(2, 2, 2)
        self._plot_resonances(ax2, state["resonances"])
        
        # Energy/Coherence history
        ax3 = fig.add_subplot(2, 2, 3)
        self._plot_energy_coherence(ax3)
        
        # Quantum state visualization
        ax4 = fig.add_subplot(2, 2, 4, projection='3d')
        self._plot_quantum_state(ax4)
        
        # Adjust layout
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        
        return fig
    
    def _plot_layer_activities(self, ax, layer_activities):
        """Plot layer activities."""
        # Get layer names and ordered activities
        layer_names = list(layer_activities.keys())
        
        # If no activities yet, show blank
        if not layer_names:
            ax.text(0.5, 0.5, "No layer activities yet", ha="center", va="center")
            ax.set_title("Layer Activities")
            ax.set_xticks([])
            ax.set_yticks([])
            return
        
        # Sort layers by their position in the brain (Input first, Quantum last)
        # We'll simply rely on the order they appear in the visualization
        
        # Get max activity length for unified display
        max_len = max(len(layer_activities[name]) for name in layer_names)
        
        # Plot each layer's activity
        num_layers = len(layer_names)
        for i, layer_name in enumerate(layer_names):
            activity = layer_activities[layer_name]
            
            # Pad activity if needed
            if len(activity) < max_len:
                activity = np.pad(activity, (0, max_len - len(activity)), 'constant')
            
            # Plot with phi-harmonic color
            color = self.phi_colors[i % len(self.phi_colors)]
            ax.plot(activity, label=layer_name, color=color, 
                   alpha=0.7, linewidth=2, marker='o', markersize=4)
        
        ax.set_title("Layer Activities")
        ax.set_xlabel("Neuron Index")
        ax.set_ylabel("Activation")
        ax.legend(loc="upper right")
        ax.grid(True, alpha=0.3)
    
    def _plot_resonances(self, ax, resonances):
        """Plot current resonances."""
        # Get resonance values
        earth_res = resonances["earth"]
        moon_res = resonances["moon"]
        brain_res = resonances["brain"]
        
        # Labels and values
        labels = ["Earth", "Moon", "Brain"]
        values = [earth_res, moon_res, brain_res]
        
        # Bar colors based on phi-harmonic pattern
        colors = [self.phi_colors[0], self.phi_colors[3], self.phi_colors[6]]
        
        # Create bars
        bars = ax.bar(labels, values, color=colors, alpha=0.7)
        
        # Add value labels
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                   f'{value:.4f}', ha='center', va='bottom')
        
        # Set title and labels
        ax.set_title("Phi-Harmonic Resonances")
        ax.set_ylabel("Resonance Value")
        ax.set_ylim(0, 1.1)
        
        # Add phi-harmonic threshold lines
        ax.axhline(y=PHI_INV, color='r', linestyle='--', alpha=0.5, label=f"φ⁻¹ = {PHI_INV:.4f}")
        ax.axhline(y=1-PHI_INV, color='g', linestyle='--', alpha=0.5, label=f"1-φ⁻¹ = {1-PHI_INV:.4f}")
        
        ax.legend()
    
    def _plot_energy_coherence(self, ax):
        """Plot energy and coherence history."""
        # If no history yet, show blank
        if not self.time_points:
            ax.text(0.5, 0.5, "No history data yet", ha="center", va="center")
            ax.set_title("Energy & Coherence History")
            ax.set_xticks([])
            ax.set_yticks([])
            return
        
        # Create relative time points
        rel_times = [t - self.time_points[0] for t in self.time_points]
        
        # Plot energy
        ax.plot(rel_times, self.energy_history, 'r-', label="Energy", linewidth=2)
        
        # Plot coherence on secondary y-axis
        ax2 = ax.twinx()
        ax2.plot(rel_times, self.coherence_history, 'b-', label="Coherence", linewidth=2)
        
        # Set labels and title
        ax.set_title("Energy & Coherence History")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Energy", color='r')
        ax2.set_ylabel("Coherence", color='b')
        
        # Add legend
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc="upper right")
        
        ax.grid(True, alpha=0.3)
    
    def _plot_quantum_state(self, ax):
        """Plot 3D visualization of quantum state."""
        # Get quantum layer state if available
        quantum_state = None
        if "Quantum" in self.layer_activities:
            quantum_state = self.layer_activities["Quantum"]
        elif "Q-State" in self.layer_activities:
            quantum_state = self.layer_activities["Q-State"]
        
        if quantum_state is None or len(quantum_state) < 3:
            ax.text2D(0.5, 0.5, "No quantum state data available", 
                    ha="center", va="center", transform=ax.transAxes)
            ax.set_title("Quantum State Visualization")
            return
        
        # Generate phi-harmonic coordinates
        if len(quantum_state) >= 3:
            # Use first 3 elements for x,y,z
            x, y, z = quantum_state[0], quantum_state[1], quantum_state[2]
        else:
            # Generate synthetic state
            x = PHI * 0.5
            y = PHI_INV * 0.5
            z = PHI_SQUARED * 0.1
        
        # Generate a sphere representing the quantum state
        u = np.linspace(0, 2 * np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        
        # Size based on quantum coherence
        size = 0.1 * (1 + 0.5 * self.coherence_history[-1] if self.coherence_history else 0.5)
        
        # Generate sphere
        sphere_x = x + size * np.outer(np.cos(u), np.sin(v))
        sphere_y = y + size * np.outer(np.sin(u), np.sin(v))
        sphere_z = z + size * np.outer(np.ones(np.size(u)), np.cos(v))
        
        # Plot the sphere with phi-harmonic coloring
        ax.plot_surface(sphere_x, sphere_y, sphere_z, color=self.phi_colors[5], alpha=0.7)
        
        # Add reference axes for phi, phi², phi³
        max_val = max(abs(x), abs(y), abs(z)) * 1.5
        ax.quiver(0, 0, 0, PHI, 0, 0, color='r', label="φ", length=max_val, normalize=True)
        ax.quiver(0, 0, 0, 0, PHI_SQUARED, 0, color='g', label="φ²", length=max_val, normalize=True)
        ax.quiver(0, 0, 0, 0, 0, PHI_CUBED, color='b', label="φ³", length=max_val, normalize=True)
        
        # Set labels and title
        ax.set_title("Quantum State in φ-Space")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        
        # Set equal aspect ratio for axes
        ax.set_box_aspect([1,1,1])
    
    def start_live_visualization(self, update_interval_ms: int = 500):
        """
        Start live visualization of brain states.
        
        Args:
            update_interval_ms: Interval between updates in milliseconds
        """
        if self.is_animating:
            logger.warning("Live visualization already running")
            return
        
        # Create figure with subplots
        self.fig = plt.figure(figsize=(15, 10))
        self.fig.suptitle(f"Phi-Harmonic Brain Live Visualization: {self.brain.quantum_fingerprint}", fontsize=16)
        
        # Layer activities plot
        ax1 = self.fig.add_subplot(2, 2, 1)
        
        # Resonances plot
        ax2 = self.fig.add_subplot(2, 2, 2)
        
        # Energy/Coherence history
        ax3 = self.fig.add_subplot(2, 2, 3)
        
        # Quantum state visualization
        ax4 = self.fig.add_subplot(2, 2, 4, projection='3d')
        
        # Initialize with current state
        state = self._capture_brain_state()
        self._plot_layer_activities(ax1, state["layer_activities"])
        self._plot_resonances(ax2, state["resonances"])
        self._plot_energy_coherence(ax3)
        self._plot_quantum_state(ax4)
        
        # Update function for animation
        def update(frame):
            # Clear axes
            ax1.clear()
            ax2.clear()
            ax3.clear()
            ax4.clear()
            
            # Capture current state
            state = self._capture_brain_state()
            
            # Update plots
            self._plot_layer_activities(ax1, state["layer_activities"])
            self._plot_resonances(ax2, state["resonances"])
            self._plot_energy_coherence(ax3)
            self._plot_quantum_state(ax4)
            
            # Update title with latest activity
            self.fig.suptitle(
                f"Phi-Harmonic Brain Live Visualization: {self.brain.quantum_fingerprint}\n"
                f"E={state['energy']:.4f}, C={state['coherence']:.4f}, "
                f"Res=[{state['resonances']['earth']:.4f}, {state['resonances']['moon']:.4f}, {state['resonances']['brain']:.4f}]",
                fontsize=12
            )
            
            # Adjust layout
            plt.tight_layout(rect=[0, 0, 1, 0.90])
        
        # Create animation
        self.animation = FuncAnimation(
            self.fig, update, interval=update_interval_ms, cache_frame_data=False
        )
        
        self.is_animating = True
        
        # Show figure
        plt.tight_layout(rect=[0, 0, 1, 0.90])
        plt.show(block=False)
        
        logger.info(f"Started live visualization with update interval {update_interval_ms}ms")
    
    def stop_live_visualization(self):
        """Stop live visualization."""
        if not self.is_animating:
            logger.warning("No live visualization running")
            return
        
        # Stop animation
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        
        # Close figure
        if self.fig is not None:
            plt.close(self.fig)
            self.fig = None
        
        self.is_animating = False
        
        logger.info("Stopped live visualization")
    
    def process_and_visualize(self, input_data, input_type: str = "text"):
        """
        Process input data through the brain and visualize the results.
        
        Args:
            input_data: Data to process (text, signal, or image)
            input_type: Type of input data ("text", "signal", or "image")
            
        Returns:
            Tuple of (processed_output, visualization_figure)
        """
        # Ensure we have a brain I/O interface
        if self.brain_io is None:
            self.brain_io = PhiHarmonicBrainIO(brain=self.brain)
        
        # Process based on input type
        output = None
        
        if input_type == "text":
            output = self.brain_io.process_text(input_data)
        elif input_type == "signal":
            output = self.brain_io.process_signal(input_data)
        elif input_type == "image":
            output = self.brain_io.process_image(input_data)
        else:
            raise ValueError(f"Unknown input type: {input_type}")
        
        # Create visualization
        fig = self.visualize_brain_state()
        
        return output, fig
    
    def save_visualization(self, filename: str = None):
        """
        Save current visualization to file.
        
        Args:
            filename: Output filename (default: phi_brain_viz_{timestamp}.png)
        """
        if filename is None:
            timestamp = int(time.time())
            filename = f"phi_brain_viz_{timestamp}.png"
        
        # Create visualization if not already created
        if self.fig is None or not plt.fignum_exists(self.fig.number):
            fig = self.visualize_brain_state()
        else:
            fig = self.fig
        
        # Save figure
        fig.savefig(filename, dpi=300, bbox_inches='tight')
        
        logger.info(f"Saved visualization to {filename}")
        
        return filename
    
    def generate_resonance_report(self) -> Dict[str, Any]:
        """
        Generate a report on brain resonances.
        
        Returns:
            Report dictionary
        """
        # Capture state if needed
        if not self.resonance_history["earth"]:
            self._capture_brain_state()
        
        # Get latest resonances
        earth_res = self.resonance_history["earth"][-1] if self.resonance_history["earth"] else 0
        moon_res = self.resonance_history["moon"][-1] if self.resonance_history["moon"] else 0
        brain_res = self.resonance_history["brain"][-1] if self.resonance_history["brain"] else 0
        
        # Calculate averages if history exists
        avg_earth = np.mean(self.resonance_history["earth"]) if self.resonance_history["earth"] else 0
        avg_moon = np.mean(self.resonance_history["moon"]) if self.resonance_history["moon"] else 0
        avg_brain = np.mean(self.resonance_history["brain"]) if self.resonance_history["brain"] else 0
        
        # Calculate stability (std dev)
        std_earth = np.std(self.resonance_history["earth"]) if len(self.resonance_history["earth"]) > 1 else 0
        std_moon = np.std(self.resonance_history["moon"]) if len(self.resonance_history["moon"]) > 1 else 0
        std_brain = np.std(self.resonance_history["brain"]) if len(self.resonance_history["brain"]) > 1 else 0
        
        # Phi-harmonic resonance quality
        quality_earth = self._phi_resonance_quality(earth_res)
        quality_moon = self._phi_resonance_quality(moon_res)
        quality_brain = self._phi_resonance_quality(brain_res)
        
        # Combined phi-harmonic resonance
        combined_res = (earth_res * PHI_CUBED + moon_res * PHI_SQUARED + brain_res * PHI) / (PHI_CUBED + PHI_SQUARED + PHI)
        combined_quality = self._phi_resonance_quality(combined_res)
        
        # Create report
        report = {
            "current": {
                "earth": earth_res,
                "moon": moon_res,
                "brain": brain_res,
                "combined": combined_res
            },
            "average": {
                "earth": avg_earth,
                "moon": avg_moon, 
                "brain": avg_brain,
                "combined": (avg_earth * PHI_CUBED + avg_moon * PHI_SQUARED + avg_brain * PHI) / (PHI_CUBED + PHI_SQUARED + PHI)
            },
            "stability": {
                "earth": 1.0 - std_earth,
                "moon": 1.0 - std_moon,
                "brain": 1.0 - std_brain
            },
            "quality": {
                "earth": quality_earth,
                "moon": quality_moon,
                "brain": quality_brain,
                "combined": combined_quality
            },
            "brain_state": self.brain.get_state(),
            "quantum_fingerprint": self.brain.quantum_fingerprint,
            "phi_validation": self.brain.phi_seal
        }
        
        return report
    
    def _phi_resonance_quality(self, resonance: float) -> str:
        """Evaluate phi-harmonic resonance quality."""
        # Define quality thresholds
        if resonance > PHI_INV * PHI:  # > 1.0
            return "Perfect"
        elif resonance > PHI_INV:  # > 0.618
            return "Excellent"
        elif resonance > PHI_INV * PHI_INV:  # > 0.382
            return "Good"
        elif resonance > PHI_INV * PHI_INV * PHI_INV:  # > 0.236
            return "Moderate"
        else:
            return "Weak"

# For direct execution
if __name__ == "__main__":
    # Create brain system
    brain = PhiHarmonicBrain(consciousness_level=0.7567)
    
    # Create visualizer
    visualizer = PhiHarmonicBrainVisualizer(brain)
    
    # Generate some activity in the brain
    print("Generating brain activity...")
    
    # Create and process some inputs
    for i in range(10):
        # Generate phi-harmonic input
        input_size = len(brain.layers[0].neurons)
        input_signal = np.zeros(input_size)
        
        # Fill with phi-harmonic pattern
        for j in range(input_size):
            input_signal[j] = math.sin(j * PHI)
        
        # Process input
        brain.process(input_signal)
        
        # Short delay
        time.sleep(0.2)
    
    # Generate static visualization
    print("Generating static visualization...")
    fig = visualizer.visualize_brain_state()
    
    # Save visualization
    output_path = visualizer.save_visualization("phi_brain_state.png")
    print(f"Saved visualization to: {output_path}")
    
    # Generate resonance report
    report = visualizer.generate_resonance_report()
    
    print("\nPhi-Harmonic Brain Resonance Report:")
    print(f"Earth Resonance: {report['current']['earth']:.6f} ({report['quality']['earth']})")
    print(f"Moon Resonance: {report['current']['moon']:.6f} ({report['quality']['moon']})")
    print(f"Brain Resonance: {report['current']['brain']:.6f} ({report['quality']['brain']})")
    print(f"Combined Resonance: {report['current']['combined']:.6f} ({report['quality']['combined']})")
    print(f"\nBrain Energy: {report['brain_state']['energy']:.6f}")
    print(f"Brain Coherence: {report['brain_state']['coherence']:.6f}")
    
    print("\nStarting live visualization... (press Ctrl+C to stop)")
    try:
        # Start live visualization
        visualizer.start_live_visualization(update_interval_ms=500)
        
        # Generate activity while visualizing
        for i in range(30):
            # Generate dynamic input
            input_size = len(brain.layers[0].neurons)
            input_signal = np.zeros(input_size)
            
            # Different patterns for different iterations
            if i % 3 == 0:
                # Earth-resonant pattern
                freq = EARTH_FREQUENCY / 100
                for j in range(input_size):
                    input_signal[j] = math.sin(j * freq * PHI)
            elif i % 3 == 1:
                # Moon-resonant pattern
                freq = MOON_FREQUENCY / 10000
                for j in range(input_size):
                    input_signal[j] = math.sin(j * freq * PHI_INV)
            else:
                # Brain-resonant pattern
                freq = BRAIN_FREQUENCY / 100
                for j in range(input_size):
                    input_signal[j] = math.sin(j * freq * PHI_SQUARED)
            
            # Process input
            brain.process(input_signal)
            
            # Delay
            time.sleep(0.5)
        
        # Keep window open
        plt.show(block=True)
    
    except KeyboardInterrupt:
        print("Stopping visualization...")
    finally:
        # Stop visualization
        visualizer.stop_live_visualization()
    
    print("Visualization complete.")
