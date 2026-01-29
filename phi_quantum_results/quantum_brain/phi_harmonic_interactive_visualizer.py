#!/usr/bin/env python3
"""
Phi-Harmonic Interactive & 4D+ Visualizer

Provides interactive 2D/3D/4D+ visualizations for phi-harmonic, quantum, and field metrics.
- Modular: Extends the genomics visualizer, does not modify core files.
- Features: Plotly-based interactive plots, 4D encoding (color, size, animation).
- Accepts arbitrary phi-harmonic/quantum/field data for hyperdimensional exploration.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from typing import List, Optional, Dict, Any

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

class PhiHarmonicInteractiveVisualizer:
    """
    Interactive visualizer for phi-harmonic, quantum, and field metrics in 2D/3D/4D+.
    """
    def __init__(self):
        pass

    def plot_interactive_3d(self, x, y, z, color=None, size=None, labels=None, title="Interactive 3D Plot", colorbar_title="Metric"):
        fig = px.scatter_3d(x=x, y=y, z=z, color=color, size=size, labels=labels, title=title, color_continuous_scale="Viridis")
        fig.update_traces(marker=dict(opacity=0.8))
        fig.update_layout(coloraxis_colorbar=dict(title=colorbar_title))
        fig.show()

    def plot_interactive_4d(self, x, y, z, color, size, labels=None, title="Interactive 4D Plot", colorbar_title="Metric"):
        fig = px.scatter_3d(x=x, y=y, z=z, color=color, size=size, labels=labels, title=title, color_continuous_scale="Plasma")
        fig.update_traces(marker=dict(opacity=0.85))
        fig.update_layout(coloraxis_colorbar=dict(title=colorbar_title))
        fig.show()

    def plot_interactive_2d(self, x, y, color=None, size=None, labels=None, title="Interactive 2D Plot", colorbar_title="Metric"):
        fig = px.scatter(x=x, y=y, color=color, size=size, labels=labels, title=title, color_continuous_scale="Viridis")
        fig.update_traces(marker=dict(opacity=0.8))
        fig.update_layout(coloraxis_colorbar=dict(title=colorbar_title))
        fig.show()

    def plot_time_animation(self, x, y, z, time, color=None, size=None, labels=None, title="4D Animation", colorbar_title="Metric"):
        fig = px.scatter_3d(x=x, y=y, z=z, color=color, size=size, animation_frame=time, labels=labels, title=title, color_continuous_scale="Inferno")
        fig.update_traces(marker=dict(opacity=0.8))
        fig.update_layout(coloraxis_colorbar=dict(title=colorbar_title))
        fig.show()

# Example usage with quantum/field metrics
def demo():
    # Simulate quantum/field metrics (from your documentation)
    n = 100
    np.random.seed(42)
    quantum_turns = np.random.normal(5000, 1000, n)
    frequency = np.random.normal(6000, 1500, n)
    resonance = np.random.uniform(1.2, 2.0, n)
    coherence = np.random.uniform(0.5, 0.8, n)
    stability = np.random.uniform(3.5, 4.5, n)
    alignment = np.random.uniform(2.0, 3.0, n)
    # 3D: turns, frequency, resonance; color by coherence, size by stability
    visualizer = PhiHarmonicInteractiveVisualizer()
    visualizer.plot_interactive_3d(
        x=quantum_turns, y=frequency, z=resonance,
        color=coherence, size=stability,
        labels={"x": "Quantum Turns", "y": "Frequency (Hz)", "z": "Resonance"},
        title="Quantum Field Interactive 3D", colorbar_title="Coherence"
    )
    # 4D: add alignment as color, resonance as size
    visualizer.plot_interactive_4d(
        x=quantum_turns, y=frequency, z=coherence,
        color=alignment, size=resonance*10,
        labels={"x": "Quantum Turns", "y": "Frequency (Hz)", "z": "Coherence"},
        title="Quantum Field Interactive 4D", colorbar_title="Alignment"
    )
    # 2D: frequency vs. resonance, color by stability
    visualizer.plot_interactive_2d(
        x=frequency, y=resonance, color=stability,
        labels={"x": "Frequency (Hz)", "y": "Resonance"},
        title="Field 2D Interactive", colorbar_title="Stability"
    )

if __name__ == "__main__":
    demo()
