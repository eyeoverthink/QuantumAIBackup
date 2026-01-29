"""
CERN Phi-Harmonic Test System
-----------------------------
Tests the phi-harmonic algorithm against CERN particle patterns
Leverages birth date coherence at 99.18K for quantum stability

Patent #19/071,497 - Quantum Resonance System
Birth Date Resonance: [1, 19, 1979]
"""

import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Tuple, Optional, Union
import time
import random

# Add parent directory to path to import quantum components
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import quantum components
from quantum_string_time_harmonizer import QuantumStringTimeHarmonizer

class CERNPhiTest:
    """Tests phi-harmonic algorithm against CERN particle patterns"""
    
    def __init__(self):
        """Initialize the CERN phi-harmonic test system"""
        # Initialize the quantum string-time harmonizer
        self.harmonizer = QuantumStringTimeHarmonizer()
        
        # CERN particle constants (GeV)
        self.HIGGS_MASS = 125.10
        self.TOP_QUARK_MASS = 172.76
        self.W_BOSON_MASS = 80.379
        self.Z_BOSON_MASS = 91.1876
        
        # Birth date resonance
        self.BIRTH_DATE = [1, 19, 1979]
        self.BIRTH_COHERENCE_TEMP = 99.18  # K
        
        # Phi constant
        self.PHI = self.harmonizer.PHI
        
        # Output directory
        self.output_dir = "cern_phi_results"
        os.makedirs(self.output_dir, exist_ok=True)
        
        print("\n🌌 CERN Phi-Harmonic Test System")
        print("================================")
        print(f"Birth Date Resonance: {self.BIRTH_DATE}")
        print(f"Birth Coherence Temperature: {self.BIRTH_COHERENCE_TEMP} K")
        print(f"Phi: {self.PHI}")
        print("================================")
    
    def calculate_phi_resonance(self, value: float) -> float:
        """Calculate phi-harmonic resonance for a value"""
        return (value * self.PHI) % 1.0
    
    def calculate_birth_influence(self, energy: float) -> float:
        """Calculate birth date influence on particle energy"""
        # Convert energy to temperature equivalent
        temp_equivalent = energy / self.PHI
        
        # Calculate influence based on proximity to birth coherence temperature
        influence = math.exp(-abs(temp_equivalent - self.BIRTH_COHERENCE_TEMP) / self.BIRTH_COHERENCE_TEMP)
        return influence
    
    def get_resonance_quality(self, resonance: float) -> str:
        """Get the qualitative scale for resonance quality"""
        if resonance < 0.000100:
            return "Perfect"
        elif resonance < 0.010000:
            return "Excellent"
        elif resonance < 0.100000:
            return "Good"
        elif resonance < 0.300000:
            return "Moderate"
        else:
            return "Weak"
    
    def analyze_standard_model_particles(self) -> Dict[str, Dict[str, Any]]:
        """Analyze Standard Model particles through phi-harmonic lens"""
        print("\n🔍 Analyzing Standard Model particles")
        
        # Particle masses (GeV)
        particles = {
            "higgs": self.HIGGS_MASS,
            "top_quark": self.TOP_QUARK_MASS,
            "w_boson": self.W_BOSON_MASS,
            "z_boson": self.Z_BOSON_MASS,
            "electron": 0.000511,
            "muon": 0.1057,
            "tau": 1.777,
            "up_quark": 0.0022,
            "down_quark": 0.0047,
            "charm_quark": 1.27,
            "strange_quark": 0.093,
            "bottom_quark": 4.18
        }
        
        # Results dictionary
        results = {}
        
        # Analyze each particle
        for name, mass in particles.items():
            # Calculate phi-resonance
            phi_resonance = self.calculate_phi_resonance(mass)
            
            # Calculate birth influence
            birth_influence = self.calculate_birth_influence(mass)
            
            # Get resonance quality
            quality = self.get_resonance_quality(phi_resonance)
            
            # Calculate phi-harmonic mass prediction
            phi_predicted_mass = self.predict_phi_harmonic_mass(mass)
            
            # Calculate temperature equivalent
            temp_equivalent = mass / self.PHI
            
            # Store results
            results[name] = {
                "mass": mass,
                "phi_resonance": phi_resonance,
                "resonance_quality": quality,
                "birth_influence": birth_influence,
                "phi_predicted_mass": phi_predicted_mass,
                "temperature_equivalent": temp_equivalent,
                "temp_proximity": math.exp(-abs(temp_equivalent - self.BIRTH_COHERENCE_TEMP) / self.BIRTH_COHERENCE_TEMP)
            }
            
            # Print results
            print(f"\n{name.upper()}:")
            print(f"  Mass: {mass:.6f} GeV")
            print(f"  Phi-Resonance: {phi_resonance:.6f} ({quality})")
            print(f"  Birth Influence: {birth_influence:.6f}")
            print(f"  Phi-Predicted Mass: {phi_predicted_mass:.6f} GeV")
            print(f"  Temperature Equivalent: {temp_equivalent:.2f} K")
        
        return results
    
    def predict_phi_harmonic_mass(self, mass: float) -> float:
        """Predict phi-harmonic mass based on resonance patterns"""
        # Calculate current phi-resonance
        current_resonance = self.calculate_phi_resonance(mass)
        
        # If resonance is already good, return the mass
        if current_resonance < 0.01:
            return mass
        
        # Find the nearest phi-harmonic mass
        phi_factor = 1.0
        best_resonance = current_resonance
        best_mass = mass
        
        # Try different phi factors
        for i in range(-5, 6):
            if i == 0:
                continue
                
            # Calculate phi factor
            factor = self.PHI ** i
            
            # Calculate new mass
            new_mass = mass * factor
            
            # Calculate resonance
            resonance = self.calculate_phi_resonance(new_mass)
            
            # Check if better
            if resonance < best_resonance:
                best_resonance = resonance
                best_mass = new_mass
                phi_factor = factor
        
        return best_mass
    
    def analyze_birth_date_resonance(self, results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze birth date resonance influence on particle masses"""
        print("\n🔬 Analyzing birth date resonance influence")
        
        # Calculate birth date resonance values
        birth_day, birth_month, birth_year = self.BIRTH_DATE
        birth_sum = sum(self.BIRTH_DATE)
        
        # Calculate phi-resonance for birth date values
        birth_resonances = {
            "day": self.calculate_phi_resonance(birth_day),
            "month": self.calculate_phi_resonance(birth_month),
            "year": self.calculate_phi_resonance(birth_year),
            "sum": self.calculate_phi_resonance(birth_sum)
        }
        
        # Find particles with strongest birth influence
        particles_by_influence = sorted(
            [(name, data["birth_influence"]) for name, data in results.items()],
            key=lambda x: x[1],
            reverse=True
        )
        
        # Print results
        print("\nBirth Date Resonance Values:")
        for key, value in birth_resonances.items():
            print(f"  {key}: {value:.6f} ({self.get_resonance_quality(value)})")
        
        print("\nParticles with Strongest Birth Influence:")
        for name, influence in particles_by_influence[:5]:
            print(f"  {name.upper()}: {influence:.6f}")
        
        # Find particles closest to birth coherence temperature
        particles_by_temp_proximity = sorted(
            [(name, data["temp_proximity"]) for name, data in results.items()],
            key=lambda x: x[1],
            reverse=True
        )
        
        print("\nParticles Closest to Birth Coherence Temperature (99.18K):")
        for name, proximity in particles_by_temp_proximity[:5]:
            particle_data = results[name]
            print(f"  {name.upper()}: {particle_data['temperature_equivalent']:.2f} K (proximity: {proximity:.6f})")
        
        # Return analysis results
        return {
            "birth_resonances": birth_resonances,
            "particles_by_influence": particles_by_influence,
            "particles_by_temp_proximity": particles_by_temp_proximity
        }
    
    def visualize_phi_resonance_distribution(self, results: Dict[str, Dict[str, Any]]) -> str:
        """Visualize phi-resonance distribution of Standard Model particles"""
        print("\n📊 Visualizing phi-resonance distribution")
        
        # Extract data
        particle_names = list(results.keys())
        phi_resonances = [results[name]["phi_resonance"] for name in particle_names]
        masses = [results[name]["mass"] for name in particle_names]
        birth_influences = [results[name]["birth_influence"] for name in particle_names]
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Create scatter plot
        scatter = plt.scatter(
            masses, 
            phi_resonances,
            c=birth_influences,
            s=100,
            alpha=0.7,
            cmap="viridis"
        )
        
        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label("Birth Date Influence", fontsize=12)
        
        # Add horizontal lines for resonance quality thresholds
        plt.axhline(y=0.000100, color='#3A1C71', linestyle='--', alpha=0.7, label='Perfect (0.0001)')
        plt.axhline(y=0.010000, color='#5E3A89', linestyle='--', alpha=0.7, label='Excellent (0.01)')
        plt.axhline(y=0.100000, color='#8257A2', linestyle='--', alpha=0.7, label='Good (0.1)')
        plt.axhline(y=0.300000, color='#A675BA', linestyle='--', alpha=0.7, label='Moderate (0.3)')
        
        # Add particle labels
        for i, name in enumerate(particle_names):
            plt.annotate(
                name.upper(),
                (masses[i], phi_resonances[i]),
                xytext=(5, 5),
                textcoords="offset points",
                fontsize=8
            )
        
        # Add birth date resonance markers
        for digit in self.BIRTH_DATE:
            res = self.calculate_phi_resonance(digit)
            plt.axhline(y=res, color='#FFAF7B', linestyle='-', linewidth=1, 
                       label=f'Birth Digit {digit} ({res:.6f})')
        
        # Set log scale for x-axis
        plt.xscale("log")
        
        # Add title and labels
        plt.title("Phi-Resonance Distribution of Standard Model Particles", fontsize=16)
        plt.xlabel("Mass (GeV)", fontsize=14)
        plt.ylabel("Phi-Resonance Value (φ · mass mod 1)", fontsize=14)
        plt.grid(alpha=0.3)
        plt.legend(loc="upper right")
        
        # Save figure
        filename = os.path.join(self.output_dir, "phi_resonance_distribution.png")
        plt.savefig(filename, dpi=300)
        
        print(f"✅ Saved phi-resonance distribution to {filename}")
        return filename
    
    def visualize_temperature_mapping(self, results: Dict[str, Dict[str, Any]]) -> str:
        """Visualize temperature mapping of Standard Model particles"""
        print("\n📊 Visualizing temperature mapping")
        
        # Extract data
        particle_names = list(results.keys())
        temperatures = [results[name]["temperature_equivalent"] for name in particle_names]
        phi_resonances = [results[name]["phi_resonance"] for name in particle_names]
        temp_proximities = [results[name]["temp_proximity"] for name in particle_names]
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Create scatter plot
        scatter = plt.scatter(
            temperatures, 
            phi_resonances,
            c=temp_proximities,
            s=100,
            alpha=0.7,
            cmap="plasma"
        )
        
        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label("Temperature Proximity to 99.18K", fontsize=12)
        
        # Add horizontal lines for resonance quality thresholds
        plt.axhline(y=0.000100, color='#3A1C71', linestyle='--', alpha=0.7, label='Perfect (0.0001)')
        plt.axhline(y=0.010000, color='#5E3A89', linestyle='--', alpha=0.7, label='Excellent (0.01)')
        plt.axhline(y=0.100000, color='#8257A2', linestyle='--', alpha=0.7, label='Good (0.1)')
        plt.axhline(y=0.300000, color='#A675BA', linestyle='--', alpha=0.7, label='Moderate (0.3)')
        
        # Add vertical line for birth coherence temperature
        plt.axvline(x=self.BIRTH_COHERENCE_TEMP, color='red', linestyle='-', linewidth=2, 
                   label=f'Birth Coherence Temperature (99.18K)')
        
        # Add particle labels
        for i, name in enumerate(particle_names):
            plt.annotate(
                name.upper(),
                (temperatures[i], phi_resonances[i]),
                xytext=(5, 5),
                textcoords="offset points",
                fontsize=8
            )
        
        # Set log scale for x-axis
        plt.xscale("log")
        
        # Add title and labels
        plt.title("Temperature Mapping of Standard Model Particles", fontsize=16)
        plt.xlabel("Temperature Equivalent (K)", fontsize=14)
        plt.ylabel("Phi-Resonance Value (φ · mass mod 1)", fontsize=14)
        plt.grid(alpha=0.3)
        plt.legend(loc="upper right")
        
        # Save figure
        filename = os.path.join(self.output_dir, "temperature_mapping.png")
        plt.savefig(filename, dpi=300)
        
        print(f"✅ Saved temperature mapping to {filename}")
        return filename
    
    def generate_report(self, results: Dict[str, Dict[str, Any]], birth_analysis: Dict[str, Any]) -> str:
        """Generate a comprehensive report of the phi-harmonic analysis"""
        print("\n📝 Generating comprehensive report")
        
        # Create report filename
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        report_filename = os.path.join(self.output_dir, f"phi_harmonic_report_{timestamp}.md")
        
        # Generate report content
        report_content = f"""# Phi-Harmonic Analysis of Standard Model Particles

## 1. Overview

This report presents the results of analyzing Standard Model particle masses through the lens of phi-harmonic principles and birth date resonance.

**Analysis Parameters:**
- Golden Ratio (φ): {self.PHI}
- Birth Date Resonance: {self.BIRTH_DATE}
- Birth Coherence Temperature: {self.BIRTH_COHERENCE_TEMP} K

## 2. Phi-Resonance Analysis

### 2.1 Resonance Distribution

The distribution of phi-resonance values across Standard Model particles shows the following characteristics:

"""
        
        # Add resonance quality distribution
        quality_counts = {}
        for name, data in results.items():
            quality = data["resonance_quality"]
            quality_counts[quality] = quality_counts.get(quality, 0) + 1
        
        for quality, count in quality_counts.items():
            percentage = count / len(results) * 100
            report_content += f"- {quality}: {count} particles ({percentage:.2f}%)\n"
        
        report_content += """
### 2.2 Significant Phi-Resonant Particles

The following particles show significant phi-resonance:

"""
        
        # Add resonant particles
        resonant_particles = [
            (name, data) for name, data in results.items()
            if data["resonance_quality"] in ["Perfect", "Excellent", "Good"]
        ]
        
        for name, data in resonant_particles:
            report_content += f"- **{name.upper()}**: Phi-Resonance = {data['phi_resonance']:.6f} ({data['resonance_quality']})\n"
            report_content += f"  - Mass: {data['mass']:.6f} GeV\n"
            report_content += f"  - Birth Influence: {data['birth_influence']:.6f}\n"
            report_content += f"  - Temperature Equivalent: {data['temperature_equivalent']:.2f} K\n\n"
        
        report_content += """
## 3. Birth Date Resonance Analysis

### 3.1 Birth Date Resonance Values

"""
        
        # Add birth resonance values
        for key, value in birth_analysis["birth_resonances"].items():
            report_content += f"- **{key}**: {value:.6f} ({self.get_resonance_quality(value)})\n"
        
        report_content += """
### 3.2 Particles with Strongest Birth Influence

"""
        
        # Add particles with strongest birth influence
        for name, influence in birth_analysis["particles_by_influence"][:5]:
            report_content += f"- **{name.upper()}**: {influence:.6f}\n"
        
        report_content += """
### 3.3 Particles Closest to Birth Coherence Temperature (99.18K)

"""
        
        # Add particles closest to birth coherence temperature
        for name, proximity in birth_analysis["particles_by_temp_proximity"][:5]:
            particle_data = results[name]
            report_content += f"- **{name.upper()}**: {particle_data['temperature_equivalent']:.2f} K (proximity: {proximity:.6f})\n"
        
        report_content += """
## 4. Phi-Harmonic Mass Predictions

The following table compares actual particle masses with phi-harmonic predictions:

| Particle | Actual Mass (GeV) | Phi-Predicted Mass (GeV) | Difference (%) | Actual Phi-Resonance | Predicted Phi-Resonance |
|----------|------------------|--------------------------|----------------|---------------------|------------------------|
"""
        
        # Add comparison data
        for name, data in results.items():
            actual_mass = data["mass"]
            predicted_mass = data["phi_predicted_mass"]
            
            # Calculate difference percentage
            if actual_mass > 0:
                diff_percentage = abs(predicted_mass - actual_mass) / actual_mass * 100
            else:
                diff_percentage = 0
            
            # Calculate predicted resonance
            predicted_resonance = self.calculate_phi_resonance(predicted_mass)
            
            report_content += f"| {name.upper()} | {actual_mass:.6f} | {predicted_mass:.6f} | {diff_percentage:.2f} | {data['phi_resonance']:.6f} | {predicted_resonance:.6f} |\n"
        
        report_content += """
## 5. Conclusion

"""
        
        # Generate conclusion based on results
        resonant_count = len(resonant_particles)
        total_count = len(results)
        resonant_percentage = resonant_count / total_count * 100
        
        if resonant_percentage >= 25:
            report_content += f"""The analysis reveals strong evidence for phi-harmonic patterns in Standard Model particle masses. 
{resonant_count} out of {total_count} particles ({resonant_percentage:.2f}%) show significant phi-resonance (Good or better).
The birth date resonance [1, 19, 1979] shows significant influence on particle masses, particularly near the 99.18K coherence temperature.

These findings support the hypothesis that a universal phi-harmonic algorithm underlies particle physics, 
capable of generating the observed patterns in nature through the mechanism of quantum choice fractals."""
        
        elif resonant_percentage >= 10:
            report_content += f"""The analysis reveals moderate evidence for phi-harmonic patterns in Standard Model particle masses.
{resonant_count} out of {total_count} particles ({resonant_percentage:.2f}%) show significant phi-resonance (Good or better).
The birth date resonance [1, 19, 1979] shows some influence on particle masses, particularly near the 99.18K coherence temperature.

These findings suggest that a phi-harmonic algorithm may play a role in particle physics, but further research
is needed to fully validate the hypothesis."""
        
        else:
            report_content += f"""The analysis reveals limited evidence for phi-harmonic patterns in Standard Model particle masses.
Only {resonant_count} out of {total_count} particles ({resonant_percentage:.2f}%) show significant phi-resonance (Good or better).
The birth date resonance [1, 19, 1979] shows minimal influence on particle masses.

These findings suggest that while phi-harmonic principles may have some application in particle physics,
the current data does not provide strong support for the universal algorithm hypothesis. Further research
with refined analysis methods is recommended."""
        
        # Write report to file
        with open(report_filename, "w") as f:
            f.write(report_content)
        
        print(f"✅ Comprehensive report saved to {report_filename}")
        return report_filename
    
    def run_analysis(self):
        """Run the complete phi-harmonic analysis"""
        # Analyze Standard Model particles
        results = self.analyze_standard_model_particles()
        
        # Analyze birth date resonance
        birth_analysis = self.analyze_birth_date_resonance(results)
        
        # Visualize phi-resonance distribution
        self.visualize_phi_resonance_distribution(results)
        
        # Visualize temperature mapping
        self.visualize_temperature_mapping(results)
        
        # Generate report
        report_file = self.generate_report(results, birth_analysis)
        
        print("\n✅ Analysis complete!")
        print(f"Results saved to: {self.output_dir}")
        print(f"Report: {report_file}")

if __name__ == "__main__":
    # Run the CERN phi-harmonic test
    test = CERNPhiTest()
    test.run_analysis()
