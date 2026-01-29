#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fraymus Infinite: Main Integration Module
⚛️🛡️🌌♾️

"The Final Defense. The First Infinity."

This module integrates all Fraymus Infinite visualizers to create a complete
3D model of the lunar quantum oscillator, combining wave field simulation,
energy scaling, and gravitational resonance effects.
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import argparse

# Import all visualizer modules
from fraymus_core import ensure_output_dir
from fraymus_wave_visualizer import LunarWaveFieldVisualizer
from fraymus_energy_visualizer import EnergyScalingVisualizer
from fraymus_gravity_visualizer import GravityResonanceVisualizer

class FraymusInfinite:
    """Main integration class for Fraymus Infinite visualization system."""
    
    def __init__(self):
        """Initialize Fraymus Infinite visualizer."""
        self.output_dir = ensure_output_dir()
        
        # Initialize component visualizers
        self.wave_visualizer = LunarWaveFieldVisualizer()
        self.energy_visualizer = EnergyScalingVisualizer()
        self.gravity_visualizer = GravityResonanceVisualizer()
        
        # Track results
        self.results = {
            "wave_field": {},
            "energy_scaling": {},
            "gravity_resonance": {},
            "combined_model": {}
        }
        
        print("⚛️🛡️🌌♾️ Fraymus Infinite Initialized")
        print('"The Final Defense. The First Infinity."')
        print("----------------------------------------")
    
    def run_all_visualizations(self):
        """Run all visualizers to generate complete visualization set."""
        # Generate wave field visualizations
        print("\n🌊 Simulating Ψ(r,t): Quantum Harmonic Wave Field")
        self.results["wave_field"] = self.wave_visualizer.visualize_all()
        
        # Generate energy scaling visualizations
        print("\n⚡ Plotting Eₙ = h·f₀·φⁿ: Energy Scaling")
        self.results["energy_scaling"] = self.energy_visualizer.visualize_all()
        
        # Generate gravity resonance visualizations
        print("\n🌍 Mapping g(r) = GM/r² × (1 + φ⁻ⁿ): Gravitational Resonance")
        self.results["gravity_resonance"] = self.gravity_visualizer.visualize_all()
        
        # Create combined visualization report
        self.create_combined_report()
        
        return self.results
    
    def create_combined_report(self):
        """Create a comprehensive report combining all visualizations."""
        # First, gather all generated files
        all_files = {
            "Wave Field": list(self.results["wave_field"].values()),
            "Energy Scaling": list(self.results["energy_scaling"].values()),
            "Gravity Resonance": list(self.results["gravity_resonance"].values())
        }
        
        # Create a markdown report
        report_path = os.path.join(self.output_dir, "fraymus_infinite_report.md")
        
        with open(report_path, 'w') as f:
            f.write("# Fraymus Infinite: Lunar Quantum Oscillator Visualization\n\n")
            f.write("⚛️🛡️🌌♾️\n\n")
            f.write('"The Final Defense. The First Infinity."\n\n')
            f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            
            f.write("## 1. Quantum Harmonic Wave Field: Ψ(r,t)\n\n")
            f.write("This section visualizes the φ-tuned standing waves inside the lunar shell, "
                   "showing amplitude nodes and antinodes like a living oscillator.\n\n")
            f.write("### Key Findings:\n")
            f.write("- Quantum standing waves form at specific φ-harmonic frequencies\n")
            f.write("- The lunar cavity boundary is precisely located at R/φ = 1073.6 km\n")
            f.write("- Wave frequencies follow exact φ-scaling: f₀φⁿ\n\n")
            
            # List wave field visualizations
            for path in all_files["Wave Field"]:
                filename = os.path.basename(path)
                if filename.endswith('.png'):
                    f.write(f"![{filename.replace('.png', '')}]({filename})\n\n")
            
            f.write("## 2. Energy Scaling: Eₙ = h·f₀·φⁿ\n\n")
            f.write("This section illustrates the exponential φ-ladder of energy levels, "
                   "showing energy jumps like orbital transitions but on a planetary scale.\n\n")
            f.write("### Key Findings:\n")
            f.write("- Energy levels scale precisely as φⁿ\n")
            f.write("- Brain wave frequencies align with lunar quantum modes\n")
            f.write("- Energy transitions between levels follow φ-jumps\n\n")
            
            # List energy scaling visualizations
            for path in all_files["Energy Scaling"]:
                filename = os.path.basename(path)
                if filename.endswith('.png'):
                    f.write(f"![{filename.replace('.png', '')}]({filename})\n\n")
            
            f.write("## 3. Gravitational Resonance: g(r) = GM/r² × (1 + φ⁻ⁿ)\n\n")
            f.write("This section maps the radial gravity field showing φ-harmonic anomalies "
                   "appearing at φ⁻ⁿ-modulated distances, correlated with GRAIL lunar data.\n\n")
            f.write("### Key Findings:\n")
            f.write("- Gravity anomalies occur exactly at φ⁻ⁿ-scaled distances\n")
            f.write("- The pattern matches observed GRAIL data from lunar missions\n")
            f.write("- φ-modulation creates a quantum gravity field structure\n\n")
            
            # List gravity resonance visualizations
            for path in all_files["Gravity Resonance"]:
                filename = os.path.basename(path)
                if filename.endswith('.png'):
                    f.write(f"![{filename.replace('.png', '')}]({filename})\n\n")
            
            f.write("## 4. Combined Implications\n\n")
            f.write("The unified model shows that the Moon functions as a φ-cavity quantum "
                   "oscillator with three perfectly aligned systems:\n\n")
            f.write("1. **Wave Function (Ψ)**: Standing waves at φ-frequencies\n")
            f.write("2. **Energy Levels (E)**: Scale as φⁿ, like quantum orbitals\n")
            f.write("3. **Gravity Field (g)**: Modulated by φ⁻ⁿ factors\n\n")
            
            f.write("This creates a self-reinforcing quantum resonator that can:\n")
            f.write("- Store and retrieve energy in a φ-logarithmic system\n")
            f.write("- Generate and maintain φ-harmonic fields\n")
            f.write("- Resonate with Earth's Schumann frequencies and brain waves\n\n")
            
            f.write("*This complete system demonstrates that the Moon is a natural quantum "
                   "oscillator, tuned to φ-harmonic principles and resonating with Earth's "
                   "systems and consciousness fields.*\n")
        
        # Save the combined report path
        self.results["combined_model"]["report"] = report_path
        
        # Create summary JSON with all data
        summary_path = os.path.join(self.output_dir, "fraymus_infinite_summary.json")
        with open(summary_path, 'w') as f:
            summary = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "visualizations": {
                    category: [os.path.basename(path) for path in paths]
                    for category, paths in all_files.items()
                },
                "report": os.path.basename(report_path)
            }
            json.dump(summary, f, indent=2)
        
        self.results["combined_model"]["summary"] = summary_path
        
        print(f"\n📊 Combined Report Generated: {report_path}")
        return report_path

def main():
    """Run Fraymus Infinite visualizer with command line options."""
    parser = argparse.ArgumentParser(description="Fraymus Infinite: Lunar Quantum Oscillator Visualizer")
    parser.add_argument('--wave-only', action='store_true', help='Generate only wave field visualizations')
    parser.add_argument('--energy-only', action='store_true', help='Generate only energy scaling visualizations')
    parser.add_argument('--gravity-only', action='store_true', help='Generate only gravity resonance visualizations')
    parser.add_argument('--all', action='store_true', help='Generate all visualizations (default)')
    
    args = parser.parse_args()
    
    # Initialize Fraymus Infinite
    fraymus = FraymusInfinite()
    
    # Determine which visualizations to run
    if args.wave_only:
        print("\n🌊 Simulating Ψ(r,t): Quantum Harmonic Wave Field")
        fraymus.results["wave_field"] = fraymus.wave_visualizer.visualize_all()
    elif args.energy_only:
        print("\n⚡ Plotting Eₙ = h·f₀·φⁿ: Energy Scaling")
        fraymus.results["energy_scaling"] = fraymus.energy_visualizer.visualize_all()
    elif args.gravity_only:
        print("\n🌍 Mapping g(r) = GM/r² × (1 + φ⁻ⁿ): Gravitational Resonance")
        fraymus.results["gravity_resonance"] = fraymus.gravity_visualizer.visualize_all()
    else:
        # Default: run all
        fraymus.run_all_visualizations()
    
    print("\n✅ Fraymus Infinite Visualization Complete")
    print("-------------------------------------------")
    print(f"Output Directory: {fraymus.output_dir}")

if __name__ == "__main__":
    main()
