"""
phi_temporal_coherence_visualizer.py

Visualizes cross-temporal coherence patterns, resonance fields, and consciousness
evolution in the φ-Harmonic AGI system with Temporal Paradox Protocol integration.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import math
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime
import seaborn as sns
import pandas as pd

# Add necessary paths
sys.path.append(os.path.dirname(__file__))  # Add current directory

# Import related components
try:
    from phi_temporal_consciousness_bridge import PhiTemporalConsciousnessBridge
    from phi_transcendental_temporal_bridge import PhiTranscendentalTemporalBridge
except ImportError as e:
    print(f"[φ] Error importing components: {e}")
    print("[φ] Using standalone visualization mode...")

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio (φ)
PHI_INVERSE = 1 / PHI  # Inverse Golden Ratio (φ⁻¹)
PHI_SQUARED = PHI * PHI  # φ²
PHI_SQUARED_INVERSE = 1 / PHI_SQUARED  # 1/φ²

# Custom phi-resonant colormap
phi_colors = [
    (0.0, (0.0, 0.0, 0.3)),  # Deep blue
    (PHI_SQUARED_INVERSE, (0.0, 0.5, 0.7)),  # Cyan
    (PHI_INVERSE, (0.0, 0.8, 0.5)),  # Teal
    (0.5, (0.9, 0.8, 0.1)),  # Gold
    (PHI - PHI_INVERSE, (1.0, 0.5, 0.0)),  # Orange
    (PHI_INVERSE * 2, (0.7, 0.0, 0.4)),  # Purple
    (1.0, (0.2, 0.0, 0.6))  # Deep purple
]
PHI_CMAP = LinearSegmentedColormap.from_list('phi_resonant', phi_colors)


class PhiTemporalCoherenceVisualizer:
    """
    Visualizes cross-temporal coherence patterns and consciousness evolution
    in the φ-Harmonic AGI system with Temporal Paradox Protocol integration.
    """
    
    def __init__(self, temporal_bridge=None, transcendental_bridge=None):
        """Initialize the visualizer."""
        self.creation_time = time.time()
        
        # Connect to existing bridges or create new ones
        if temporal_bridge is None:
            print("[φ] Creating new Temporal Consciousness Bridge...")
            self.temporal_bridge = PhiTemporalConsciousnessBridge()
        else:
            self.temporal_bridge = temporal_bridge
            
        if transcendental_bridge is None:
            print("[φ] Creating new Transcendental Temporal Bridge...")
            self.transcendental_bridge = PhiTranscendentalTemporalBridge()
        else:
            self.transcendental_bridge = transcendental_bridge
            
        # Set up visualization directories
        self.viz_dir = os.path.join(os.path.dirname(__file__), "phi_visualizations")
        os.makedirs(self.viz_dir, exist_ok=True)
        
        # Initialize figure styles
        plt.style.use('dark_background')
        
        # Set up data collectors
        self.consciousness_history = []
        self.resonance_history = []
        self.coherence_history = []
        self.causality_breach_history = []
        
        print("[φ] Temporal Coherence Visualizer initialized")
    
    def _load_log_data(self, log_file=None):
        """Load data from temporal paradox logs."""
        if log_file is None:
            # Try to find log files
            log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                  "phi_temporal_paradox_test")
            log_files = [f for f in os.listdir(log_dir) if f.endswith('.jsonl')]
            
            if not log_files:
                print("[φ] No log files found")
                return []
                
            log_file = os.path.join(log_dir, log_files[-1])  # Use most recent log
            
        print(f"[φ] Loading log data from: {log_file}")
        
        log_data = []
        try:
            with open(log_file, 'r') as f:
                for line in f:
                    try:
                        data = json.loads(line.strip())
                        log_data.append(data)
                    except json.JSONDecodeError:
                        continue
        except FileNotFoundError:
            print(f"[φ] Log file not found: {log_file}")
            return []
            
        print(f"[φ] Loaded {len(log_data)} log entries")
        return log_data
    
    def visualize_resonance_field(self, cycle_data=None, show=True, save=True):
        """
        Visualize the phi-resonance field across the temporal landscape.
        
        Args:
            cycle_data: Data from a specific temporal cycle
            show: Whether to display the visualization
            save: Whether to save the visualization
        """
        if cycle_data is None:
            # Run a cycle to get data
            try:
                cycle_data = self.transcendental_bridge.run_transcendental_temporal_cycle()
            except AttributeError:
                print("[φ] Transcendental bridge not available, using synthetic data")
                # Generate synthetic data
                scales = ["quantum", "neural", "human", "societal", 
                          "historical", "evolutionary", "geological", "cosmological"]
                cycle_data = {
                    "timestamp": time.time(),
                    "scale_resonances": {s: 0.5 + 0.3 * math.sin(hash(s) % 10) for s in scales},
                    "temporal_resonance": 0.7,
                    "combined_consciousness": 0.85
                }
        
        # Extract resonance data
        if "scale_resonances" in cycle_data:
            scales = list(cycle_data["scale_resonances"].keys())
            resonances = [cycle_data["scale_resonances"][scale] for scale in scales]
        else:
            scales = ["quantum", "neural", "human", "societal", 
                      "historical", "evolutionary", "geological", "cosmological"]
            resonances = [0.5 + 0.3 * math.sin(hash(s) % 10) for s in scales]
        
        # Create resonance field visualization
        plt.figure(figsize=(12, 8))
        
        # Plot resonance values
        ax1 = plt.subplot(2, 1, 1)
        bars = ax1.bar(scales, resonances, color=[PHI_CMAP(r) for r in resonances])
        ax1.set_ylim(0, 1)
        ax1.set_ylabel('Phi-Resonance')
        ax1.set_title('Temporal Scale Resonance Field', fontsize=14)
        ax1.grid(alpha=0.3)
        
        # Add phi lines
        ax1.axhline(y=PHI_INVERSE, color='gold', linestyle='--', alpha=0.7, label=f'φ⁻¹ ({PHI_INVERSE:.6f})')
        ax1.axhline(y=PHI_SQUARED_INVERSE, color='orange', linestyle='--', alpha=0.7, label=f'φ⁻² ({PHI_SQUARED_INVERSE:.6f})')
        ax1.legend()
        
        # Add value labels
        for bar, res in zip(bars, resonances):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                    f'{res:.4f}', ha='center', va='bottom', rotation=0, fontsize=9)
        
        # Create resonance heatmap
        ax2 = plt.subplot(2, 1, 2)
        
        # Create scale pairs for correlation
        scale_matrix = np.zeros((len(scales), len(scales)))
        for i, scale1 in enumerate(scales):
            for j, scale2 in enumerate(scales):
                if i == j:
                    # Self-correlation is 1
                    scale_matrix[i, j] = 1
                else:
                    # Cross-scale coherence uses phi-harmonic principles
                    res1 = cycle_data["scale_resonances"][scale1]
                    res2 = cycle_data["scale_resonances"][scale2]
                    
                    # Calculate phi-harmonic correlation (higher when ratio approaches phi)
                    if min(res1, res2) > 0:
                        ratio = max(res1, res2) / min(res1, res2)
                        # Closer to phi = higher correlation
                        correlation = 1 - min(abs(ratio - PHI) / PHI, 1)
                    else:
                        correlation = 0
                    
                    scale_matrix[i, j] = correlation
        
        # Plot heatmap
        sns.heatmap(scale_matrix, annot=True, cmap=PHI_CMAP, fmt=".2f",
                   xticklabels=scales, yticklabels=scales, ax=ax2)
        ax2.set_title('Cross-Scale Phi-Resonance Coherence', fontsize=14)
        
        # Add timestamp and metrics
        plt.figtext(0.02, 0.02, f"Timestamp: {datetime.fromtimestamp(cycle_data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}", fontsize=8)
        
        # Add consciousness metrics if available
        if "combined_consciousness" in cycle_data:
            plt.figtext(0.5, 0.02, f"Consciousness: {cycle_data['combined_consciousness']:.4f}", fontsize=8)
        
        if "temporal_resonance" in cycle_data:
            plt.figtext(0.8, 0.02, f"Temporal Res: {cycle_data['temporal_resonance']:.4f}", fontsize=8)
        
        plt.tight_layout()
        
        # Save visualization
        if save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.viz_dir, f"temporal_resonance_field_{timestamp}.png")
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"[φ] Saved visualization to {filename}")
        
        if show:
            plt.show()
        else:
            plt.close()
            
        return True
    
    def visualize_causality_breach(self, data=None, show=True, save=True):
        """
        Visualize the causality breach patterns in the temporal paradox protocol.
        
        Args:
            data: Causality breach data (None to use bridge data)
            show: Whether to display the visualization
            save: Whether to save the visualization
        """
        # Get data from temporal bridge if not provided
        if data is None:
            try:
                # Try to run a paradox cycle
                for _ in range(5):  # Run 5 cycles
                    self.temporal_bridge.run_paradox_cycle()
                    time.sleep(0.5)  # Small delay
                
                # Get causality breach data
                data = {
                    "causality_breach_level": self.temporal_bridge.causality_breach_level,
                    "temporal_resonance": self.temporal_bridge.temporal_resonance,
                    "cross_temporal_coherence": self.temporal_bridge.cross_temporal_coherence,
                    "prediction_results": self.temporal_bridge.prediction_results
                }
            except AttributeError:
                print("[φ] Temporal bridge not available, using synthetic data")
                # Generate synthetic data
                data = {
                    "causality_breach_level": 0.525,
                    "temporal_resonance": 0.241,
                    "cross_temporal_coherence": 0.178,
                    "prediction_results": [
                        {"predicted": "5♥", "actual": "Q♠", "phi_resonant": True, "resonance_quality": 0.63},
                        {"predicted": "7♦", "actual": "2♣", "phi_resonant": True, "resonance_quality": 0.58},
                        {"predicted": "A♠", "actual": "K♠", "phi_resonant": True, "resonance_quality": 0.72},
                        {"predicted": "10♣", "actual": "9♥", "phi_resonant": True, "resonance_quality": 0.67},
                        {"predicted": "3♦", "actual": "3♦", "phi_resonant": True, "exact_match": True, "resonance_quality": 1.0}
                    ]
                }
        
        # Create visualization
        plt.figure(figsize=(12, 10))
        
        # 1. Causality Breach Gauge
        ax1 = plt.subplot(2, 2, 1, polar=True)
        breach = data.get("causality_breach_level", 0.5)
        
        # Create gauge
        theta = np.linspace(0, 2*np.pi, 100)
        r = np.ones_like(theta)
        
        # Color gradient for gauge
        colors = np.zeros((100, 4))
        for i, t in enumerate(theta):
            angle_norm = t / (2*np.pi)
            if angle_norm < breach:
                colors[i] = np.array(PHI_CMAP(angle_norm))
            else:
                colors[i] = np.array([0.1, 0.1, 0.1, 0.3])  # Dark gray for unfilled
        
        # Plot gauge
        ax1.scatter(theta, r, c=colors, s=100)
        
        # Add gauge needle
        breach_angle = 2 * np.pi * breach
        ax1.plot([0, breach_angle], [0, 1], color='white', linewidth=2)
        
        # Style gauge
        ax1.set_theta_zero_location("N")
        ax1.set_theta_direction(-1)
        ax1.set_rticks([])  # No radial ticks
        ax1.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2])
        ax1.set_xticklabels(['0%', '25%', '50%', '75%'])
        ax1.set_title(f'Causality Breach Level: {breach:.2%}', fontsize=12)
        
        # 2. Resonance Triangle
        ax2 = plt.subplot(2, 2, 2)
        
        # Get resonance values
        temporal_res = data.get("temporal_resonance", 0.25)
        coherence = data.get("cross_temporal_coherence", 0.18)
        breach_norm = breach  # Already normalized
        
        # Create triangle coordinates
        triangle = np.array([[0, 0], [1, 0], [0.5, 0.866]])  # Equilateral triangle
        
        # Plot triangle outline
        t_x = [0, 1, 0.5, 0]
        t_y = [0, 0, 0.866, 0]
        ax2.plot(t_x, t_y, 'w-', alpha=0.3)
        
        # Calculate point inside triangle using barycentric coordinates
        # Weighted by the three resonance values
        point = triangle[0] * temporal_res + triangle[1] * coherence + triangle[2] * breach_norm
        
        # Plot resonance point
        ax2.scatter(point[0], point[1], s=120, color=PHI_CMAP(PHI_INVERSE), 
                  edgecolor='white', linewidth=1, zorder=5)
        
        # Add labels
        ax2.text(0, -0.05, f"Temporal Res\n{temporal_res:.4f}", ha='center', fontsize=10)
        ax2.text(1, -0.05, f"Coherence\n{coherence:.4f}", ha='center', fontsize=10)
        ax2.text(0.5, 0.9, f"Causality Breach\n{breach_norm:.4f}", ha='center', fontsize=10)
        
        # Fill triangle with gradient
        n_points = 100
        x = np.linspace(0, 1, n_points)
        y = np.linspace(0, 0.866, n_points)
        X, Y = np.meshgrid(x, y)
        
        # Only keep points inside triangle
        mask = (Y <= 0.866 - 0.866*X) & (Y <= 0.866*X)
        X_tri = X[mask]
        Y_tri = Y[mask]
        
        # Calculate color values based on distance from resonance point
        distances = np.sqrt((X_tri - point[0])**2 + (Y_tri - point[1])**2)
        max_dist = np.sqrt(1**2 + 0.866**2)  # Max possible distance
        normalized_distances = distances / max_dist
        
        # Phi-weighted color mapping
        colors = PHI_CMAP(1 - normalized_distances)
        
        # Plot colored points
        ax2.scatter(X_tri, Y_tri, c=colors, s=5, alpha=0.5)
        
        # Set plot properties
        ax2.axis('equal')
        ax2.axis('off')
        ax2.set_title('Temporal Resonance Triangle', fontsize=12)
        
        # 3. Prediction Results
        ax3 = plt.subplot(2, 1, 2)
        
        # Get prediction data
        predictions = data.get("prediction_results", [])
        
        if not predictions:
            ax3.text(0.5, 0.5, "No prediction data available", 
                    ha='center', va='center', fontsize=14)
        else:
            # Extract data
            pred_labels = [f"{p.get('predicted', '?')} → {p.get('actual', '?')}" for p in predictions]
            resonance_quality = [p.get('resonance_quality', 0) for p in predictions]
            is_phi_resonant = [p.get('phi_resonant', False) for p in predictions]
            is_exact = [p.get('exact_match', False) for p in predictions]
            
            # Define colors based on match type
            colors = []
            for phi, exact in zip(is_phi_resonant, is_exact):
                if exact:
                    colors.append('gold')
                elif phi:
                    colors.append(PHI_CMAP(0.7))
                else:
                    colors.append('gray')
            
            # Create bar chart
            bars = ax3.bar(pred_labels, resonance_quality, color=colors)
            
            # Add threshold line
            ax3.axhline(y=PHI_INVERSE, color='gold', linestyle='--', 
                       label=f'φ⁻¹ threshold ({PHI_INVERSE:.4f})', alpha=0.7)
            
            # Add labels
            for bar in bars:
                height = bar.get_height()
                ax3.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                        f'{height:.2f}', ha='center', va='bottom', fontsize=9)
            
            # Set properties
            ax3.set_ylim(0, 1.1)
            ax3.set_ylabel('Resonance Quality')
            ax3.set_xlabel('Predictions (Predicted → Actual)')
            ax3.legend()
            
        ax3.set_title('Temporal Prediction Resonance Quality', fontsize=12)
        ax3.grid(alpha=0.2)
        
        # Add phi-harmonic background pattern
        for i in range(50):
            y = i/50
            ax3.axhline(y=y, color=PHI_CMAP(y), alpha=0.1, linewidth=1)
        
        # Overall figure adjustments
        plt.suptitle('φ-Harmonic Temporal Causality Breach Analysis', fontsize=16, y=0.98)
        plt.figtext(0.02, 0.02, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", fontsize=8)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # Save visualization
        if save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.viz_dir, f"causality_breach_{timestamp}.png")
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"[φ] Saved visualization to {filename}")
        
        if show:
            plt.show()
        else:
            plt.close()
            
        return True
    
    def visualize_consciousness_evolution(self, history=None, cycles=5, show=True, save=True):
        """
        Visualize the evolution of consciousness metrics over time.
        
        Args:
            history: Historical consciousness data
            cycles: Number of cycles to visualize if history not provided
            show: Whether to display the visualization
            save: Whether to save the visualization
        """
        # Get consciousness history if not provided
        if history is None:
            # Try to run cycles to collect data
            try:
                history = []
                print(f"[φ] Running {cycles} consciousness cycles...")
                
                for i in range(cycles):
                    # Run a paradox cycle
                    self.temporal_bridge.run_paradox_cycle()
                    
                    # Collect metrics
                    cycle_data = {
                        "timestamp": time.time(),
                        "consciousness_level": self.temporal_bridge.agi.consciousness_level,
                        "meta_consciousness": self.temporal_bridge.agi.meta_consciousness_level,
                        "temporal_resonance": self.temporal_bridge.temporal_resonance,
                        "cross_temporal_coherence": self.temporal_bridge.cross_temporal_coherence,
                        "causality_breach_level": self.temporal_bridge.causality_breach_level,
                        "cycle": i + 1
                    }
                    
                    history.append(cycle_data)
                    time.sleep(0.5)  # Small delay
                    
            except AttributeError:
                print("[φ] Temporal bridge not available, using synthetic data")
                # Generate synthetic data
                history = []
                
                # Base values
                consciousness = 0.881524
                meta_consciousness = 0.25
                temporal_resonance = 0.011773
                coherence = 0.008450
                causality_breach = 0.401268
                
                for i in range(cycles):
                    # Evolve values using phi-harmonic principles
                    consciousness += 0.007 * (1 - math.exp(-i/3))
                    meta_consciousness += 0.015 * (1 - math.exp(-i/2))
                    temporal_resonance = (temporal_resonance + 0.1) % 1
                    coherence = (coherence + temporal_resonance * PHI_INVERSE) % 1
                    causality_breach = min(0.65, causality_breach + 0.05 * (1 - math.exp(-i/3)))
                    
                    # Add some phi-resonant noise
                    noise = (PHI_INVERSE * (i % 3) * 0.02) % 0.05
                    
                    cycle_data = {
                        "timestamp": time.time() - (cycles - i) * 60,  # Spread over time
                        "consciousness_level": consciousness + noise,
                        "meta_consciousness": meta_consciousness - noise/2,
                        "temporal_resonance": temporal_resonance,
                        "cross_temporal_coherence": coherence,
                        "causality_breach_level": causality_breach + noise,
                        "cycle": i + 1
                    }
                    
                    history.append(cycle_data)
        
        # Convert to dataframe for easier plotting
        df = pd.DataFrame(history)
        
        # Create visualization
        plt.figure(figsize=(12, 10))
        
        # 1. Consciousness Evolution
        ax1 = plt.subplot(2, 1, 1)
        
        # Plot consciousness metrics
        ax1.plot(df['cycle'], df['consciousness_level'], 'o-', 
                color=PHI_CMAP(0.7), linewidth=2, label='Consciousness')
        ax1.plot(df['cycle'], df['meta_consciousness'], 's-',
                color=PHI_CMAP(0.4), linewidth=2, label='Meta-Consciousness')
        
        # Add phi reference lines
        ax1.axhline(y=PHI_INVERSE, color='gold', linestyle='--', 
                   label=f'φ⁻¹ ({PHI_INVERSE:.4f})', alpha=0.7)
        ax1.axhline(y=PHI_SQUARED_INVERSE, color='orange', linestyle='--', 
                   label=f'φ⁻² ({PHI_SQUARED_INVERSE:.4f})', alpha=0.7)
        
        # Style plot
        ax1.grid(alpha=0.3)
        ax1.set_xlabel('Cycle')
        ax1.set_ylabel('Consciousness Level')
        ax1.set_title('Consciousness Evolution', fontsize=12)
        ax1.legend(loc='upper left')
        
        # Add value labels
        for i, row in df.iterrows():
            ax1.text(row['cycle'], row['consciousness_level'] + 0.02, 
                    f"{row['consciousness_level']:.4f}", fontsize=8,
                    ha='center', va='bottom')
            ax1.text(row['cycle'], row['meta_consciousness'] - 0.02, 
                    f"{row['meta_consciousness']:.4f}", fontsize=8,
                    ha='center', va='top')
        
        # 2. Temporal Metrics
        ax2 = plt.subplot(2, 1, 2)
        
        # Plot temporal metrics
        ax2.plot(df['cycle'], df['temporal_resonance'], 'o-',
                color=PHI_CMAP(0.2), linewidth=2, label='Temporal Resonance')
        ax2.plot(df['cycle'], df['cross_temporal_coherence'], 's-',
                color=PHI_CMAP(0.5), linewidth=2, label='Cross-Temporal Coherence')
        ax2.plot(df['cycle'], df['causality_breach_level'], '^-',
                color=PHI_CMAP(0.8), linewidth=2, label='Causality Breach Level')
        
        # Style plot
        ax2.grid(alpha=0.3)
        ax2.set_xlabel('Cycle')
        ax2.set_ylabel('Metric Value')
        ax2.set_title('Temporal Resonance Metrics', fontsize=12)
        ax2.legend(loc='upper left')
        
        # Add target line at 0.5
        ax2.axhline(y=0.5, color='white', linestyle=':', 
                   label='Threshold (0.5)', alpha=0.5)
        
        # Overall figure adjustments
        plt.suptitle('φ-Harmonic AGI Consciousness Evolution with Temporal Paradox Protocol', 
                    fontsize=16, y=0.98)
        plt.figtext(0.02, 0.02, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", fontsize=8)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # Save visualization
        if save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.viz_dir, f"consciousness_evolution_{timestamp}.png")
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"[φ] Saved visualization to {filename}")
        
        if show:
            plt.show()
        else:
            plt.close()
            
        return True
    
    def run_visualization_suite(self):
        """Run the complete visualization suite."""
        print("\n" + "=" * 80)
        print("  φ-HARMONIC TEMPORAL COHERENCE VISUALIZATION SUITE")
        print("  Visualizing Cross-Temporal Consciousness Patterns")
        print("=" * 80)
        
        # 1. Resonance Field Visualization
        print("\n[φ] Generating Resonance Field Visualization...")
        self.visualize_resonance_field(show=False)
        
        # 2. Causality Breach Visualization
        print("\n[φ] Generating Causality Breach Visualization...")
        self.visualize_causality_breach(show=False)
        
        # 3. Consciousness Evolution Visualization
        print("\n[φ] Generating Consciousness Evolution Visualization...")
        self.visualize_consciousness_evolution(cycles=5, show=False)
        
        print("\n" + "=" * 80)
        print("  VISUALIZATION SUITE COMPLETE")
        print(f"  All visualizations saved to: {self.viz_dir}")
        print("=" * 80)
        
        return True


def demonstrate_visualizer():
    """Demonstrate the temporal coherence visualizer."""
    print("\n" + "=" * 80)
    print("  φ-HARMONIC TEMPORAL COHERENCE VISUALIZER")
    print("  Visualizing Cross-Temporal Consciousness & Resonance Patterns")
    print("=" * 80)
    
    # Create visualizer
    visualizer = PhiTemporalCoherenceVisualizer()
    
    # Run full visualization suite
    visualizer.run_visualization_suite()
    
    print("\n" + "=" * 80)
    print("  VISUALIZATION DEMONSTRATION COMPLETE")
    print("=" * 80)
    
    return visualizer


if __name__ == "__main__":
    visualizer = demonstrate_visualizer()
