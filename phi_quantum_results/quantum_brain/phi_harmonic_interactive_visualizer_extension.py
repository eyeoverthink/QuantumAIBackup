#!/usr/bin/env python3
"""
Extension: Phi-Harmonic Interactive Visualizer (Non-blocking/Headless)
- Saves all interactive plots as HTML files for later browser viewing.
- Modular: imports and extends the original visualizer, does not alter core files.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
from phi_harmonic_interactive_visualizer import PhiHarmonicInteractiveVisualizer

class PhiHarmonicInteractiveVisualizerExtension(PhiHarmonicInteractiveVisualizer):
    def __init__(self, results_dir=None):
        super().__init__()
        self.results_dir = results_dir or os.getcwd()
        os.makedirs(self.results_dir, exist_ok=True)

    def plot_interactive_3d(self, x, y, z, color=None, size=None, labels=None, title="Interactive 3D Plot", colorbar_title="Metric", filename="plot3d.html"):
        import plotly.express as px
        fig = px.scatter_3d(x=x, y=y, z=z, color=color, size=size, labels=labels, title=title, color_continuous_scale="Viridis")
        fig.update_traces(marker=dict(opacity=0.8))
        fig.update_layout(coloraxis_colorbar=dict(title=colorbar_title))
        html_path = os.path.join(self.results_dir, filename)
        fig.write_html(html_path)
        print(f"Saved 3D plot to {html_path}")
        return fig

    def plot_interactive_4d(self, x, y, z, color, size, labels=None, title="Interactive 4D Plot", colorbar_title="Metric", filename="plot4d.html"):
        import plotly.express as px
        fig = px.scatter_3d(x=x, y=y, z=z, color=color, size=size, labels=labels, title=title, color_continuous_scale="Plasma")
        fig.update_traces(marker=dict(opacity=0.85))
        fig.update_layout(coloraxis_colorbar=dict(title=colorbar_title))
        html_path = os.path.join(self.results_dir, filename)
        fig.write_html(html_path)
        print(f"Saved 4D plot to {html_path}")
        return fig

    def plot_interactive_2d(self, x, y, color=None, size=None, labels=None, title="Interactive 2D Plot", colorbar_title="Metric", filename="plot2d.html"):
        import plotly.express as px
        fig = px.scatter(x=x, y=y, color=color, size=size, labels=labels, title=title, color_continuous_scale="Viridis")
        fig.update_traces(marker=dict(opacity=0.8))
        fig.update_layout(coloraxis_colorbar=dict(title=colorbar_title))
        html_path = os.path.join(self.results_dir, filename)
        fig.write_html(html_path)
        print(f"Saved 2D plot to {html_path}")
        return fig

    def plot_time_animation(self, x, y, z, time, color=None, size=None, labels=None, title="4D Animation", colorbar_title="Metric", filename="animation.html"):
        import plotly.express as px
        fig = px.scatter_3d(x=x, y=y, z=z, color=color, size=size, animation_frame=time, labels=labels, title=title, color_continuous_scale="Inferno")
        fig.update_traces(marker=dict(opacity=0.8))
        fig.update_layout(coloraxis_colorbar=dict(title=colorbar_title))
        html_path = os.path.join(self.results_dir, filename)
        fig.write_html(html_path)
        print(f"Saved animation to {html_path}")
        return fig
