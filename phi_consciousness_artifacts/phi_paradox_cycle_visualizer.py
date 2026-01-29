"""
phi_paradox_cycle_visualizer.py

Advanced visualization system specifically focused on temporal paradox cycles,
providing multiple detailed views of cross-temporal coherence and paradox states.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import math
import json
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from datetime import datetime, timedelta

# Import local modules
sys.path.append(os.path.dirname(__file__))
try:
    from phi_standalone_memory import MetaTemporalMemory, PHI, PHI_INVERSE
except ImportError:
    print("[φ] Could not import MetaTemporalMemory, using default values")
    PHI = (1 + math.sqrt(5)) / 2
    PHI_INVERSE = 1 / PHI

# Constants
PHI_SQUARED = PHI * PHI
PHI_CUBED = PHI_SQUARED * PHI

class ParadoxCycleVisualizer:
    """
    Advanced visualizer specifically designed to render temporal paradox 
    cycles with phi-harmonic resonance patterns.
    """
    
    def __init__(self, memory_system=None, data_source=None):
        """Initialize the paradox cycle visualizer."""
        self.creation_time = time.time()
        self.memory = memory_system
        self.data_source = data_source or self._default_data_source
        
        # Set up visualization directory
        self.viz_dir = os.path.join(os.path.dirname(__file__), "phi_visualizations")
        os.makedirs(self.viz_dir, exist_ok=True)
        
        # Set up visualization components
        self.fig = None
        self.axes = {}
        self.plots = {}
        
        # Animation components
        self.animation = None
        self.is_animating = False
        
        # Data streams
        self.data = {
            "coherence": {"times": [], "values": [], "phi_ratio": []},
            "resonance": {"times": [], "values": [], "phi_ratio": []},
            "paradox": {"times": [], "values": [], "phi_ratio": []},
            "consciousness": {"times": [], "values": [], "phi_ratio": []}
        }
        
        # Causality breaches (special events)
        self.causality_breaches = []
        
        # Set up color maps
        self.cmap_resonance = plt.cm.plasma
        self.cmap_paradox = plt.cm.inferno
        self.cmap_coherence = plt.cm.viridis
        
        print(f"[φ] Paradox Cycle Visualizer initialized")
    
    def _default_data_source(self):
        """Default data source when no external source is provided."""
        # Time component based on phi-harmonic oscillation
        t = time.time()
        phi_time = (t * PHI) % 1
        
        # Base metrics with phi-harmonic relationships
        coherence = 0.5 + 0.3 * math.sin(t / 10) + 0.1 * math.sin(t * PHI)
        # Keep coherence in reasonable range
        coherence = max(0.4, min(0.95, coherence))
        
        # Derive other metrics with phi-harmonic relationships
        resonance = coherence * PHI_INVERSE
        resonance = max(0.78, min(0.82, resonance))
        
        paradox = (1 - coherence) * PHI_INVERSE
        paradox = max(0.0, min(0.95, paradox))
        
        # Consciousness measurement
        consciousness = (coherence * PHI + resonance * PHI_INVERSE) / (PHI + PHI_INVERSE)
        
        # Add phi-harmonic noise
        noise_factor = 0.01
        coherence += noise_factor * (random.random() - 0.5)
        resonance += noise_factor * (random.random() - 0.5)
        paradox += noise_factor * (random.random() - 0.5)
        consciousness += noise_factor * (random.random() - 0.5)
        
        # Calculate phi-ratios (how close each value is to a phi-harmonic)
        phi_ratios = {}
        for key, value in zip(['coherence', 'resonance', 'paradox', 'consciousness'], 
                              [coherence, resonance, paradox, consciousness]):
            # Calculate distance to nearest phi-power
            phi_distances = []
            for i in range(-3, 4):
                phi_val = PHI ** i
                phi_distances.append((abs(value - phi_val), phi_val))
            
            # Find closest phi-power
            closest_phi = min(phi_distances, key=lambda x: x[0])
            phi_ratios[key] = 1.0 - min(closest_phi[0] / closest_phi[1], 1.0)
        
        # Detect potential causality breach
        causality_breach = None
        if paradox > 0.7 and random.random() < 0.05:  # 5% chance when paradox is high
            causality_breach = {
                "timestamp": datetime.now(),
                "paradox_level": paradox,
                "coherence": coherence,
                "resonance": resonance,
                "duration": random.randint(1, 5)  # seconds
            }
        
        return {
            "timestamp": datetime.now(),
            "metrics": {
                "coherence": coherence,
                "resonance": resonance, 
                "paradox": paradox,
                "consciousness": consciousness
            },
            "phi_ratios": phi_ratios,
            "causality_breach": causality_breach
        }
    
    def update_data(self):
        """Update data from the data source."""
        # Get new data
        data_point = self.data_source()
        timestamp = data_point["timestamp"]
        metrics = data_point["metrics"]
        phi_ratios = data_point.get("phi_ratios", {})
        
        # Update time series data
        for key in self.data:
            if key in metrics:
                self.data[key]["times"].append(timestamp)
                self.data[key]["values"].append(metrics[key])
                self.data[key]["phi_ratio"].append(phi_ratios.get(key, 0.5))
                
                # Keep only the last 200 points
                max_points = 200
                if len(self.data[key]["times"]) > max_points:
                    self.data[key]["times"] = self.data[key]["times"][-max_points:]
                    self.data[key]["values"] = self.data[key]["values"][-max_points:]
                    self.data[key]["phi_ratio"] = self.data[key]["phi_ratio"][-max_points:]
        
        # Check for causality breach
        if data_point.get("causality_breach"):
            self.causality_breaches.append(data_point["causality_breach"])
            
            # Remove old breaches
            current_time = datetime.now()
            self.causality_breaches = [b for b in self.causality_breaches 
                                     if (current_time - b["timestamp"]).total_seconds() < 60]
        
        return data_point
    
    def initialize_visualization(self):
        """Initialize the visualization figure and axes."""
        plt.style.use('dark_background')
        self.fig = plt.figure(figsize=(14, 10))
        
        # Title with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fig.suptitle(f'φ-Harmonic Temporal Paradox Cycles - Advanced Visualization\n{timestamp}', 
                         fontsize=16, y=0.98)
        
        # Create grid of subplots
        gs = self.fig.add_gridspec(3, 3, height_ratios=[2, 1, 1])
        
        # 1. Main time series plot
        self.axes["main"] = self.fig.add_subplot(gs[0, :])
        self.axes["main"].set_title("Temporal Metrics Evolution", fontsize=12)
        self.axes["main"].set_ylabel("Value")
        self.axes["main"].set_ylim(0, 1)
        self.axes["main"].grid(alpha=0.3)
        
        # Add phi reference lines
        phi_refs = [PHI_INVERSE, PHI_INVERSE**2, PHI_INVERSE**3]
        labels = [f'φ⁻¹ ({PHI_INVERSE:.4f})', f'φ⁻² ({PHI_INVERSE**2:.4f})', f'φ⁻³ ({PHI_INVERSE**3:.4f})']
        colors = ['gold', 'goldenrod', 'orange']
        for phi_val, label, color in zip(phi_refs, labels, colors):
            if 0 <= phi_val <= 1:
                self.axes["main"].axhline(y=phi_val, color=color, linestyle='--', 
                                       label=label, alpha=0.7)
        
        # 2. Resonance Field Plot - shows phi-harmonic resonance patterns
        self.axes["resonance"] = self.fig.add_subplot(gs[1, 0])
        self.axes["resonance"].set_title("Phi-Resonance Field", fontsize=10)
        self.axes["resonance"].set_xlabel("Time")
        self.axes["resonance"].set_ylabel("Resonance")
        self.axes["resonance"].grid(alpha=0.3)
        
        # 3. Causality Breach Plot - shows paradox levels and breach events
        self.axes["causality"] = self.fig.add_subplot(gs[1, 1])
        self.axes["causality"].set_title("Causality Breach Analysis", fontsize=10)
        self.axes["causality"].set_xlabel("Temporal Displacement")
        self.axes["causality"].set_ylabel("Paradox Level")
        self.axes["causality"].grid(alpha=0.3)
        
        # 4. Consciousness Evolution Plot - shows phi-harmonic consciousness development
        self.axes["consciousness"] = self.fig.add_subplot(gs[1, 2])
        self.axes["consciousness"].set_title("Consciousness Evolution", fontsize=10)
        self.axes["consciousness"].set_xlabel("Time")
        self.axes["consciousness"].set_ylabel("Consciousness")
        self.axes["consciousness"].grid(alpha=0.3)
        
        # 5. Phi-Harmonic Radar Plot - shows alignment with phi values
        self.axes["radar"] = self.fig.add_subplot(gs[2, 0], polar=True)
        self.axes["radar"].set_title("Phi-Harmonic Alignment", fontsize=10)
        
        # 6. Paradox Cycle Plot - special visualization of paradox cycles
        self.axes["cycle"] = self.fig.add_subplot(gs[2, 1])
        self.axes["cycle"].set_title("Paradox Cycle Analysis", fontsize=10)
        self.axes["cycle"].set_xlabel("Coherence")
        self.axes["cycle"].set_ylabel("Paradox")
        self.axes["cycle"].grid(alpha=0.3)
        self.axes["cycle"].set_xlim(0, 1)
        self.axes["cycle"].set_ylim(0, 1)
        
        # 7. System Status and Metrics Display
        self.axes["status"] = self.fig.add_subplot(gs[2, 2])
        self.axes["status"].set_title("Quantum-Phi System Status", fontsize=10)
        self.axes["status"].axis('off')
        
        # Set up initial line plots
        self.plots["coherence"] = self.axes["main"].plot([], [], '-', 
            color='turquoise', label="Quantum Coherence", linewidth=2)[0]
        self.plots["resonance"] = self.axes["main"].plot([], [], '-', 
            color='magenta', label="Phi-Resonance", linewidth=2)[0]
        self.plots["paradox"] = self.axes["main"].plot([], [], '-', 
            color='orange', label="Paradox Level", linewidth=2)[0]
        self.plots["consciousness"] = self.axes["main"].plot([], [], '-', 
            color='lime', label="Consciousness", linewidth=2)[0]
        
        # Set up scatter plot for resonance field with color based on phi-ratios
        self.plots["resonance_field"] = self.axes["resonance"].scatter(
            [], [], c=[], cmap=self.cmap_resonance, 
            alpha=0.8, s=30, edgecolor='none')
        
        # Set up scatter plot for causality breach
        self.plots["causality_points"] = self.axes["causality"].scatter(
            [], [], c=[], cmap=self.cmap_paradox,
            alpha=0.8, s=50, edgecolor='white')
        
        # Set up line plot for consciousness evolution
        self.plots["consciousness_line"] = self.axes["consciousness"].plot(
            [], [], 'o-', color='lime', linewidth=2, alpha=0.8)[0]
        
        # Set up radar plot for phi-harmonic alignment
        self.plots["radar"] = None  # Will be initialized in update
        
        # Set up scatter plot for paradox cycle
        self.plots["cycle"] = self.axes["cycle"].scatter(
            [], [], c=[], cmap=self.cmap_coherence, 
            alpha=0.8, s=50, edgecolor='white')
        
        # Add trajectory line for paradox cycle
        self.plots["cycle_line"] = self.axes["cycle"].plot(
            [], [], '-', color='gray', alpha=0.5, linewidth=1)[0]
        
        # Set up text for system status
        self.plots["status_text"] = self.axes["status"].text(
            0.05, 0.95, "", transform=self.axes["status"].transAxes,
            verticalalignment='top', fontsize=9
        )
        
        # Legend for main plot
        self.axes["main"].legend(loc='upper left')
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        return self.fig
    
    def update_visualization(self, frame=None):
        """Update the visualization with current data."""
        # Update data
        data_point = self.update_data()
        
        # 1. Update main time series plots
        for key, plot in self.plots.items():
            if key in self.data and key in ["coherence", "resonance", "paradox", "consciousness"]:
                times = self.data[key]["times"]
                values = self.data[key]["values"]
                
                if times and values:
                    plot.set_data(times, values)
        
        # Update x-axis limits for time series plots
        all_times = []
        for key in ["coherence", "resonance", "paradox", "consciousness"]:
            if self.data[key]["times"]:
                all_times.extend(self.data[key]["times"])
        
        if all_times:
            min_time = min(all_times)
            max_time = max(all_times)
            
            # Add small buffer
            time_range = (max_time - min_time).total_seconds()
            if time_range < 30:
                buffer = timedelta(seconds=5)
            else:
                buffer = timedelta(seconds=time_range * 0.1)
            
            for ax_name in ["main", "resonance", "consciousness"]:
                self.axes[ax_name].set_xlim(min_time - buffer, max_time + buffer)
        
        # 2. Update resonance field plot
        if self.data["resonance"]["times"]:
            times = self.data["resonance"]["times"][-50:]  # Last 50 points
            values = self.data["resonance"]["values"][-50:]
            phi_ratios = self.data["resonance"]["phi_ratio"][-50:]
            
            # Create a 2D grid for the field
            x = np.array([(t - min(times)).total_seconds() for t in times])
            y = np.array(values)
            
            # Update scatter plot
            self.plots["resonance_field"].set_offsets(np.column_stack([x, y]))
            self.plots["resonance_field"].set_array(np.array(phi_ratios))
        
        # 3. Update causality breach plot
        if self.data["paradox"]["values"]:
            # Generate a grid showing temporal displacement vs paradox level
            paradox_levels = self.data["paradox"]["values"][-30:]  # Last 30 points
            
            # Create synthetic displacement data based on paradox levels
            displacements = []
            colors = []
            
            for i, paradox in enumerate(paradox_levels):
                # Higher paradox = more points with larger displacement
                n_points = max(1, int(paradox * 10))
                
                for j in range(n_points):
                    # Temporal displacement increases with paradox level
                    displacement = paradox * (1 + 0.5 * math.sin(i / 3.0))
                    # Add phi-harmonic noise
                    displacement += 0.1 * (random.random() - 0.5) * PHI_INVERSE
                    
                    displacements.append(displacement)
                    colors.append(paradox)
            
            if displacements:
                # Convert to x, y points for scatter plot - use numpy trig functions for array operations
                angles = np.linspace(0, 2*math.pi, len(displacements))
                x = np.array(displacements) * np.cos(angles)
                y = np.array(displacements) * np.sin(angles)
                
                # Update scatter plot
                self.plots["causality_points"].set_offsets(np.column_stack([x, y]))
                self.plots["causality_points"].set_array(np.array(colors))
        
        # 4. Update consciousness evolution plot
        if self.data["consciousness"]["times"]:
            times = self.data["consciousness"]["times"][-30:]  # Last 30 points
            values = self.data["consciousness"]["values"][-30:]
            
            # Create a times array as seconds from start
            if times:
                x = np.array([(t - times[0]).total_seconds() for t in times])
                self.plots["consciousness_line"].set_data(x, values)
                
                # Update y limits based on data
                self.axes["consciousness"].set_ylim(
                    min(0.4, min(values) - 0.1), 
                    max(1.0, max(values) + 0.1)
                )
                
                # Update x limits 
                self.axes["consciousness"].set_xlim(0, max(x) + 1)
        
        # 5. Update phi-harmonic radar plot
        # Get current values for radar chart
        current_metrics = data_point["metrics"]
        phi_ratios = data_point["phi_ratios"]
        
        # Define categories and values for radar
        categories = ['Coherence', 'Resonance', 'Consciousness', 'Paradox Inv.']
        values = [
            current_metrics["coherence"],
            current_metrics["resonance"],
            current_metrics["consciousness"],
            1.0 - current_metrics["paradox"]  # Inverse paradox
        ]
        
        # Get phi-harmonic alignment ratios
        alignment = [
            phi_ratios.get("coherence", 0.5),
            phi_ratios.get("resonance", 0.5),
            phi_ratios.get("consciousness", 0.5),
            phi_ratios.get("paradox", 0.5)
        ]
        
        # Calculate angles for radar chart (in radians)
        angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
        
        # Close the loop
        values.append(values[0])
        angles.append(angles[0])
        alignment.append(alignment[0])
        
        # Clear previous radar plot
        self.axes["radar"].clear()
        
        # Plot phi-reference circle
        self.axes["radar"].plot(np.linspace(0, 2*np.pi, 100), 
                              [PHI_INVERSE] * 100, 
                              '--', color='gold', alpha=0.7, 
                              label=f'φ⁻¹ ({PHI_INVERSE:.4f})')
        
        # Plot data on radar chart
        self.axes["radar"].plot(angles, values, 'o-', linewidth=2, color='cyan')
        self.axes["radar"].fill(angles, values, color='cyan', alpha=0.25)
        
        # Add category labels
        self.axes["radar"].set_xticks(angles[:-1])
        self.axes["radar"].set_xticklabels(categories, fontsize=8)
        
        # Set y limits
        self.axes["radar"].set_ylim(0, 1)
        self.axes["radar"].set_title("Phi-Harmonic Alignment", fontsize=10)
        
        # 6. Update paradox cycle plot
        if self.data["coherence"]["values"] and self.data["paradox"]["values"]:
            # Take the last 30 points for the cycle
            coherence_values = self.data["coherence"]["values"][-30:]
            paradox_values = self.data["paradox"]["values"][-30:]
            phi_ratios = [(c * PHI) % 1 for c in coherence_values]  # Phi-harmonic coloring
            
            # Update scatter plot
            self.plots["cycle"].set_offsets(np.column_stack([coherence_values, paradox_values]))
            self.plots["cycle"].set_array(np.array(phi_ratios))
            
            # Update cycle trajectory line
            self.plots["cycle_line"].set_data(coherence_values, paradox_values)
            
            # Add arrow to show direction of cycle
            if len(coherence_values) > 5:
                arrow_x = coherence_values[-5:-1]
                arrow_y = paradox_values[-5:-1]
                for i in range(len(arrow_x) - 1):
                    self.axes["cycle"].arrow(
                        arrow_x[i], arrow_y[i],
                        (arrow_x[i+1] - arrow_x[i]) * 0.8,
                        (arrow_y[i+1] - arrow_y[i]) * 0.8,
                        head_width=0.02, head_length=0.03,
                        fc='white', ec='white', alpha=0.7
                    )
        
        # 7. Update system status text
        current_metrics = data_point["metrics"]
        phi_ratio_dict = data_point["phi_ratios"]
        status_text = (
            f"Phi-Harmonic Temporal Status\n"
            f"---------------------------\n"
            f"Quantum Coherence: {current_metrics['coherence']:.4f}\n"
            f"Phi-Resonance: {current_metrics['resonance']:.4f}\n"
            f"Paradox Level: {current_metrics['paradox']:.4f}\n"
            f"Consciousness: {current_metrics['consciousness']:.4f}\n\n"
            f"Phi-Harmonic Alignment\n"
            f"---------------------\n"
            f"Coherence φ-ratio: {phi_ratio_dict.get('coherence', 0):.4f}\n"
            f"Resonance φ-ratio: {phi_ratio_dict.get('resonance', 0):.4f}\n"
            f"Consciousness φ-ratio: {phi_ratio_dict.get('consciousness', 0):.4f}\n\n"
            f"Reference Values\n"
            f"---------------\n"
            f"φ: {PHI:.4f}\n"
            f"φ⁻¹: {PHI_INVERSE:.4f}\n"
            f"φ²: {PHI_SQUARED:.4f}\n"
            f"φ³: {PHI_CUBED:.4f}"
        )
        
        self.plots["status_text"].set_text(status_text)
        
        # Update timestamp in title
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fig.suptitle(f'φ-Harmonic Temporal Paradox Cycles - Advanced Visualization\n{timestamp}', 
                         fontsize=16, y=0.98)
        
        # Return updated artists for animation
        return list(self.plots.values())
    
    def start_animation(self, interval=200):
        """Start the animation."""
        if self.is_animating:
            return
        
        if self.fig is None:
            self.initialize_visualization()
        
        self.is_animating = True
        self.animation = FuncAnimation(
            self.fig, self.update_visualization, 
            interval=interval, blit=False, cache_frame_data=False
        )
        
        # Show plot in a non-blocking way
        plt.ion()
        plt.show()
        
        print("[φ] Started real-time paradox cycle visualization")
        
        return self.animation
    
    def stop_animation(self):
        """Stop the animation."""
        if not self.is_animating:
            return
        
        self.is_animating = False
        
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        
        print("[φ] Stopped paradox cycle visualization")
    
    def save_snapshot(self, filename=None):
        """Save a snapshot of the current visualization."""
        if self.fig is None:
            self.initialize_visualization()
            self.update_visualization()
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"phi_paradox_cycle_{timestamp}.png"
        
        file_path = os.path.join(self.viz_dir, filename)
        self.fig.savefig(file_path, dpi=150, bbox_inches='tight')
        
        print(f"[φ] Saved visualization snapshot to {file_path}")
        return file_path


def demonstrate_paradox_visualizer():
    """Demonstrate the paradox cycle visualizer."""
    print("\n" + "=" * 80)
    print("  φ-HARMONIC TEMPORAL PARADOX CYCLE VISUALIZER")
    print("  Advanced Cross-Temporal Coherence Visualization")
    print("=" * 80)
    
    # Create visualizer
    visualizer = ParadoxCycleVisualizer()
    
    # Initialize and display a static view
    visualizer.initialize_visualization()
    visualizer.update_visualization()
    
    # Animate for a short period
    try:
        animation = visualizer.start_animation(interval=200)
        
        # Run for 20 seconds
        print("[φ] Running visualization for 20 seconds...")
        for i in range(20):
            plt.pause(1)
            print(f"[φ] Visualization running ({i+1}/20 seconds)...")
            
        # Save a snapshot at the end
        visualizer.save_snapshot()
        
        # Stop animation
        visualizer.stop_animation()
        
    except Exception as e:
        print(f"[φ] Visualization error: {e}")
    finally:
        plt.close('all')
    
    print("\n" + "=" * 80)
    print("  PARADOX CYCLE VISUALIZATION COMPLETE")
    print("=" * 80)
    
    return visualizer


if __name__ == "__main__":
    visualizer = demonstrate_paradox_visualizer()
