#!/usr/bin/env python3
# Quantum Anti-AI Lie Loop Visualizer
# This script provides visualization tools for the Quantum Anti-AI Lie Loop system
# to help understand trust metrics and phi-harmonic resonance patterns

import os
import sys
import json
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from typing import Dict, List, Any, Optional, Union

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio
PHI_CONJUGATE = 1 / PHI  # Golden ratio conjugate

class QuantumAntiAILieLoopVisualizer:
    """Visualizes trust metrics and phi-harmonic resonance patterns from verification reports."""
    
    def __init__(self, report_file=None, report_data=None):
        """Initialize the visualizer with report data."""
        self.report_data = None
        
        if report_file and os.path.isfile(report_file):
            with open(report_file, 'r') as f:
                self.report_data = json.load(f)
        elif report_data:
            self.report_data = report_data
        
        # Initialize visualization parameters
        self.phi_colors = {
            "primary": "#1a5fb4",     # Phi-aligned blue
            "secondary": "#c01c28",  # Phi-complementary red
            "tertiary": "#26a269",   # Phi-resonant green
            "background": "#f6f5f4", # Light background
            "text": "#241f31"        # Dark text
        }
        
        # Create phi-harmonic color map
        self.phi_cmap = self._create_phi_cmap()
    
    def _create_phi_cmap(self):
        """Create a phi-harmonic color map based on golden ratio."""
        # Define colors at phi-harmonic points
        colors = [
            (0.0, self.phi_colors["primary"]),           # Start with primary
            (PHI_CONJUGATE, self.phi_colors["secondary"]), # At phi conjugate point
            (1.0, self.phi_colors["tertiary"])           # End with tertiary
        ]
        
        # Create the colormap
        cmap_name = 'phi_harmonic'
        cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=256)
        
        return cm
    
    def visualize_trust_metrics(self, output_file="trust_metrics_visualization.png"):
        """Visualize trust metrics from verification reports."""
        if not self.report_data:
            print("No report data available for visualization")
            return
        
        # Extract trust metrics
        if "results" in self.report_data:
            # Multiple verification results
            trust_metrics = [r.get("trust_metric", 0) for r in self.report_data["results"] if "trust_metric" in r]
            labels = [r.get("file_path", r.get("snippet_id", f"Code {i+1}")) 
                     for i, r in enumerate(self.report_data["results"])]
        elif "trust_metric" in self.report_data:
            # Single verification result
            trust_metrics = [self.report_data["trust_metric"]]
            labels = ["Code"]
        else:
            print("No trust metrics found in report data")
            return
        
        # Create figure
        plt.figure(figsize=(12, 8))
        plt.style.use('seaborn-v0_8-whitegrid')
        
        # Plot trust metrics
        bars = plt.bar(labels, trust_metrics, color=[self.phi_cmap(tm) for tm in trust_metrics])
        
        # Add phi-harmonic reference lines
        plt.axhline(y=PHI_CONJUGATE, color=self.phi_colors["secondary"], linestyle='--', 
                   alpha=0.7, label=f"φ Conjugate ({PHI_CONJUGATE:.6f})")
        plt.axhline(y=1/PHI**2, color=self.phi_colors["tertiary"], linestyle=':', 
                   alpha=0.7, label=f"φ⁻² ({1/PHI**2:.6f})")
        
        # Add labels and title
        plt.ylabel('Trust Metric')
        plt.title('Quantum Anti-AI Lie Loop Trust Metrics', fontsize=14, fontweight='bold')
        plt.ylim(0, 1.1)  # Trust metrics are between 0 and 1
        
        # Add trust level annotations
        for i, v in enumerate(trust_metrics):
            plt.text(i, v + 0.02, f"{v:.4f}", ha='center', fontweight='bold')
        
        # Add legend
        plt.legend()
        
        # Rotate x-axis labels if there are many
        if len(labels) > 5:
            plt.xticks(rotation=45, ha='right')
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300)
        plt.close()
        
        print(f"Trust metrics visualization saved to: {output_file}")
        return output_file
    
    def visualize_phi_resonance(self, output_file="phi_resonance_visualization.png"):
        """Visualize phi-harmonic resonance patterns from verification reports."""
        if not self.report_data:
            print("No report data available for visualization")
            return
        
        # Extract phi resonance data
        resonance_data = []
        labels = []
        
        if "results" in self.report_data:
            # Multiple verification results
            for i, r in enumerate(self.report_data["results"]):
                if "verification_phi_resonance" in r:
                    resonance_data.append(r["verification_phi_resonance"])
                    labels.append(r.get("file_path", r.get("snippet_id", f"Code {i+1}")))
        elif "verification_phi_resonance" in self.report_data:
            # Single verification result
            resonance_data = [self.report_data["verification_phi_resonance"]]
            labels = ["Code"]
        
        if not resonance_data:
            print("No phi resonance data found in report")
            return
        
        # Create figure
        plt.figure(figsize=(12, 8))
        plt.style.use('seaborn-v0_8-whitegrid')
        
        # Create a circular plot (polar coordinates)
        ax = plt.subplot(111, projection='polar')
        
        # Convert resonance values to angles (0 to 2π)
        theta = [2 * math.pi * r for r in resonance_data]
        
        # Use radius 1 for all points
        r = [1] * len(resonance_data)
        
        # Plot resonance points
        ax.scatter(theta, r, c=theta, s=200, cmap=self.phi_cmap, alpha=0.7)
        
        # Add labels to points
        for i, (angle, radius, label) in enumerate(zip(theta, r, labels)):
            # Adjust text position slightly outside the point
            text_radius = radius * 1.1
            ha = 'left' if -math.pi/2 <= angle % (2*math.pi) <= math.pi/2 else 'right'
            plt.annotate(label, xy=(angle, text_radius), xytext=(angle, text_radius),
                        ha=ha, va='center', fontsize=8)
        
        # Add phi-harmonic reference lines
        phi_angle = 2 * math.pi * PHI_CONJUGATE
        ax.plot([phi_angle, phi_angle], [0, 1.2], color=self.phi_colors["secondary"], 
                linestyle='--', alpha=0.7, label=f"φ Conjugate ({PHI_CONJUGATE:.6f})")
        
        # Remove radial ticks and labels
        ax.set_rticks([])
        
        # Set custom theta ticks and labels
        ax.set_xticks([0, math.pi/2, math.pi, 3*math.pi/2])
        ax.set_xticklabels(['0.0', '0.25', '0.5', '0.75'])
        
        # Add title
        plt.title('Phi-Harmonic Resonance Pattern', fontsize=14, fontweight='bold', y=1.1)
        
        # Add legend
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300)
        plt.close()
        
        print(f"Phi resonance visualization saved to: {output_file}")
        return output_file
    
    def visualize_contradictions(self, output_file="contradictions_visualization.png"):
        """Visualize contradictions found in verification reports."""
        if not self.report_data:
            print("No report data available for visualization")
            return
        
        # Extract contradiction data
        contradictions = []
        
        if "contradictions" in self.report_data:
            # Single verification result
            contradictions = self.report_data["contradictions"]
        
        if not contradictions:
            print("No contradiction data found in report")
            return
        
        # Group contradictions by type
        contradiction_types = {}
        for c in contradictions:
            c_type = c.get("type", "Unknown")
            if c_type not in contradiction_types:
                contradiction_types[c_type] = []
            contradiction_types[c_type].append(c)
        
        # Create figure
        plt.figure(figsize=(12, 8))
        plt.style.use('seaborn-v0_8-whitegrid')
        
        # Plot contradiction counts by type
        types = list(contradiction_types.keys())
        counts = [len(contradiction_types[t]) for t in types]
        
        # Calculate severity for each type
        severities = [sum(c["severity"] for c in contradiction_types[t]) / len(contradiction_types[t]) 
                     for t in types]
        
        # Create bar chart with severity-based colors
        bars = plt.bar(types, counts, color=[self.phi_cmap(s) for s in severities])
        
        # Add labels and title
        plt.ylabel('Number of Contradictions')
        plt.title('Contradictions by Type', fontsize=14, fontweight='bold')
        
        # Add count annotations
        for i, v in enumerate(counts):
            plt.text(i, v + 0.1, str(v), ha='center')
        
        # Add severity annotations
        for i, (bar, severity) in enumerate(zip(bars, severities)):
            plt.text(bar.get_x() + bar.get_width()/2, 0.3, 
                    f"Severity: {severity:.2f}", ha='center', color='white',
                    fontweight='bold', fontsize=8)
        
        # Rotate x-axis labels if there are many
        if len(types) > 3:
            plt.xticks(rotation=30, ha='right')
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300)
        plt.close()
        
        print(f"Contradictions visualization saved to: {output_file}")
        return output_file
    
    def visualize_all(self, output_dir="."):
        """Generate all visualizations and return paths to the output files."""
        os.makedirs(output_dir, exist_ok=True)
        
        outputs = {}
        
        # Generate trust metrics visualization
        trust_file = os.path.join(output_dir, "trust_metrics_visualization.png")
        outputs["trust_metrics"] = self.visualize_trust_metrics(trust_file)
        
        # Generate phi resonance visualization
        resonance_file = os.path.join(output_dir, "phi_resonance_visualization.png")
        outputs["phi_resonance"] = self.visualize_phi_resonance(resonance_file)
        
        # Generate contradictions visualization if contradictions exist
        if "contradictions" in self.report_data:
            contradictions_file = os.path.join(output_dir, "contradictions_visualization.png")
            outputs["contradictions"] = self.visualize_contradictions(contradictions_file)
        
        return outputs

def main():
    """Main function to run the visualizer."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Quantum Anti-AI Lie Loop Visualizer")
    parser.add_argument("--report", "-r", type=str, required=True, 
                        help="Path to verification report JSON file")
    parser.add_argument("--output", "-o", type=str, default=".", 
                        help="Output directory for visualizations")
    parser.add_argument("--type", "-t", type=str, choices=["all", "trust", "resonance", "contradictions"], 
                        default="all", help="Type of visualization to generate")
    
    args = parser.parse_args()
    
    if not os.path.isfile(args.report):
        print(f"Error: Report file not found: {args.report}")
        return 1
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)
    
    # Initialize visualizer
    visualizer = QuantumAntiAILieLoopVisualizer(report_file=args.report)
    
    # Generate visualizations based on type
    if args.type == "all":
        visualizer.visualize_all(args.output)
    elif args.type == "trust":
        visualizer.visualize_trust_metrics(os.path.join(args.output, "trust_metrics_visualization.png"))
    elif args.type == "resonance":
        visualizer.visualize_phi_resonance(os.path.join(args.output, "phi_resonance_visualization.png"))
    elif args.type == "contradictions":
        visualizer.visualize_contradictions(os.path.join(args.output, "contradictions_visualization.png"))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
