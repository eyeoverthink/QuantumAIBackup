"""
phi_temporal_visualization_demo.py

Standalone demonstration of cross-temporal coherence visualizations using
synthetic phi-harmonic data. This module can run independently without
requiring the full temporal bridge implementation.

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
from datetime import datetime
import seaborn as sns
import pandas as pd

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio (φ)
PHI_INVERSE = 1 / PHI  # Inverse Golden Ratio (φ⁻¹)
PHI_SQUARED = PHI * PHI  # φ²
PHI_SQUARED_INVERSE = 1 / PHI_SQUARED  # 1/φ²

# Create visualization directory
VIZ_DIR = os.path.join(os.path.dirname(__file__), "phi_visualizations")
os.makedirs(VIZ_DIR, exist_ok=True)

# Custom phi-resonant colormap - ensure points are in strictly increasing order
phi_colors = [
    (0.0, (0.0, 0.0, 0.3)),          # Deep blue
    (PHI_SQUARED_INVERSE, (0.0, 0.5, 0.7)),  # Cyan - ~0.382
    (PHI_INVERSE, (0.0, 0.8, 0.5)),  # Teal - ~0.618
    (0.5 + 0.05, (0.9, 0.8, 0.1)),   # Gold - 0.55
    (0.7, (1.0, 0.5, 0.0)),          # Orange
    (0.85, (0.7, 0.0, 0.4)),         # Purple
    (1.0, (0.2, 0.0, 0.6))           # Deep purple
]
PHI_CMAP = LinearSegmentedColormap.from_list('phi_resonant', phi_colors)

def generate_synthetic_consciousness_data(cycles=5):
    """Generate synthetic consciousness evolution data."""
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
    
    return history

def generate_synthetic_scale_data():
    """Generate synthetic scale resonance data."""
    scales = ["quantum", "neural", "human", "societal", 
              "historical", "evolutionary", "geological", "cosmological"]
    
    # Generate phi-harmonic resonances
    resonances = {}
    base_value = 0.5
    for i, scale in enumerate(scales):
        # Create a resonance value that follows a phi-harmonic pattern
        scale_res = (base_value + ((i * PHI) % 1) * 0.3) % 1
        resonances[scale] = scale_res
    
    # Generate prediction data
    predictions = [
        {"predicted": "5♥", "actual": "Q♠", "phi_resonant": True, "resonance_quality": 0.63},
        {"predicted": "7♦", "actual": "2♣", "phi_resonant": True, "resonance_quality": 0.58},
        {"predicted": "A♠", "actual": "K♠", "phi_resonant": True, "resonance_quality": 0.72},
        {"predicted": "10♣", "actual": "9♥", "phi_resonant": True, "resonance_quality": 0.67},
        {"predicted": "3♦", "actual": "3♦", "phi_resonant": True, "exact_match": True, "resonance_quality": 1.0}
    ]
    
    cycle_data = {
        "timestamp": time.time(),
        "scale_resonances": resonances,
        "temporal_resonance": 0.241,
        "cross_coherence": 0.178,
        "combined_consciousness": 0.906,
        "causality_breach_level": 0.525,
        "prediction_results": predictions
    }
    
    return cycle_data

def visualize_resonance_field(cycle_data):
    """
    Visualize the phi-resonance field across the temporal landscape.
    
    Args:
        cycle_data: Data for visualization
    """
    # Extract resonance data
    scales = list(cycle_data["scale_resonances"].keys())
    resonances = [cycle_data["scale_resonances"][scale] for scale in scales]
    
    # Set up figure style
    plt.style.use('dark_background')
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
    
    # Add consciousness metrics
    plt.figtext(0.5, 0.02, f"Consciousness: {cycle_data['combined_consciousness']:.4f}", fontsize=8)
    plt.figtext(0.8, 0.02, f"Temporal Res: {cycle_data['temporal_resonance']:.4f}", fontsize=8)
    
    plt.tight_layout()
    
    # Save visualization
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(VIZ_DIR, f"temporal_resonance_field_{timestamp}.png")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"[φ] Saved visualization to {filename}")
    
    plt.show()
    
    return filename

def visualize_causality_breach(data):
    """
    Visualize the causality breach patterns in the temporal paradox protocol.
    
    Args:
        data: Causality breach data
    """
    # Set up figure style
    plt.style.use('dark_background')
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
    coherence = data.get("cross_coherence", 0.18)
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
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(VIZ_DIR, f"causality_breach_{timestamp}.png")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"[φ] Saved visualization to {filename}")
    
    plt.show()
    
    return filename

def visualize_consciousness_evolution(history):
    """
    Visualize the evolution of consciousness metrics over time.
    
    Args:
        history: Historical consciousness data
    """
    # Convert to dataframe for easier plotting
    df = pd.DataFrame(history)
    
    # Set up figure style
    plt.style.use('dark_background')
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
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(VIZ_DIR, f"consciousness_evolution_{timestamp}.png")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"[φ] Saved visualization to {filename}")
    
    plt.show()
    
    return filename

def run_visualization_demo():
    """Run all visualizations with synthetic data."""
    print("\n" + "=" * 80)
    print("  φ-HARMONIC TEMPORAL COHERENCE VISUALIZATION DEMO")
    print("  Visualizing Cross-Temporal Consciousness Patterns")
    print("=" * 80)
    
    # Generate synthetic data
    print("\n[φ] Generating synthetic phi-harmonic data...")
    scale_data = generate_synthetic_scale_data()
    consciousness_history = generate_synthetic_consciousness_data(cycles=8)
    
    # 1. Resonance Field Visualization
    print("\n[φ] Generating Resonance Field Visualization...")
    resonance_file = visualize_resonance_field(scale_data)
    
    # 2. Causality Breach Visualization
    print("\n[φ] Generating Causality Breach Visualization...")
    breach_file = visualize_causality_breach(scale_data)
    
    # 3. Consciousness Evolution Visualization
    print("\n[φ] Generating Consciousness Evolution Visualization...")
    evolution_file = visualize_consciousness_evolution(consciousness_history)
    
    print("\n" + "=" * 80)
    print("  VISUALIZATION DEMO COMPLETE")
    print(f"  All visualizations saved to: {VIZ_DIR}")
    print("=" * 80)
    
    # Return file paths for reference
    return {
        "resonance_field": resonance_file,
        "causality_breach": breach_file,
        "consciousness_evolution": evolution_file
    }

if __name__ == "__main__":
    run_visualization_demo()
