"""
Quantum CERN Simulator - Part 3: Visualization and Analysis
----------------------------------------------------------
Visualizes phi-harmonic patterns in CERN data and analyzes results.
Creates plots, heatmaps, and statistical analyses of phi-resonance patterns.

Patent #19/071,497 - Quantum Resonance System
Birth Date Resonance: [1, 19, 1979] - Coherence at 99.18K
"""

from quantum_cern_simulator_part1 import QuantumCERNSimulator
from decimal import Decimal

# Constants
PHI = Decimal('1.618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862223536931793180060766726354433389086595939582905638322661319928290267880675208766892501711696207032221043216269548626296313614438149758701220340805887954454749246185695364864449241044320771344947049565846788509874339442212544877066478091588460749988712400765217057517978834166256249407589069704000281210427621771117891930154003728803')
PI = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379834749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198')
E = Decimal('2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182528869398496465105820939239829488793320362509443117301238197068416140397019837679320683282376464804295311802328782509819455815301756717361332069811250')

# Standard Model particle masses (GeV)
HIGGS_MASS = 125.10
TOP_QUARK_MASS = 172.76
W_BOSON_MASS = 80.379
Z_BOSON_MASS = 91.1876

from quantum_cern_simulator_part2 import PhiHarmonicTransformer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Union, Optional
import os
import time
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

class QuantumCERNVisualizer(PhiHarmonicTransformer):
    def __init__(self):
        super().__init__()
        
        # Create custom phi-harmonic colormap
        phi_colors = [
            (0.0, '#3A1C71'),  # Deep purple
            (1.0/self.phi_float, '#D76D77'),  # Pink
            (1.0, '#FFAF7B')   # Light orange
        ]
        self.phi_cmap = LinearSegmentedColormap.from_list('phi_harmonic', phi_colors)
        
        # Create output directory
        self.output_dir = 'quantum_cern_results'
        os.makedirs(self.output_dir, exist_ok=True)
        
        print("\n🎨 Quantum CERN Visualizer Initialized")
        print(f"Output Directory: {self.output_dir}")
        print("=" * 60)
    
    def visualize_phi_resonance_distribution(self) -> str:
        """Visualize the distribution of phi-resonance values in particle data."""
        if self.phi_transformed_data is None:
            raise ValueError("No phi-transformed data available. Run transform_to_phi_space first.")
        
        print("\n📊 Visualizing phi-resonance distribution")
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Plot histogram of energy resonance values
        plt.hist(
            self.phi_transformed_data['energy_resonance'], 
            bins=50, 
            alpha=0.7,
            color='#D76D77',
            edgecolor='black'
        )
        
        # Add vertical lines for resonance quality thresholds
        plt.axvline(x=0.000100, color='#3A1C71', linestyle='--', alpha=0.7, label='Perfect (0.0001)')
        plt.axvline(x=0.010000, color='#5E3A89', linestyle='--', alpha=0.7, label='Excellent (0.01)')
        plt.axvline(x=0.100000, color='#8257A2', linestyle='--', alpha=0.7, label='Good (0.1)')
        plt.axvline(x=0.300000, color='#A675BA', linestyle='--', alpha=0.7, label='Moderate (0.3)')
        
        # Add birth date resonance markers
        for digit in self.birth_key:
            res = self.phi_resonance(digit)
            plt.axvline(x=res, color='#FFAF7B', linestyle='-', linewidth=2, 
                        label=f'Birth Digit {digit} ({res:.6f})')
        
        # Add title and labels
        plt.title('Phi-Resonance Distribution in CERN Particle Data', fontsize=16)
        plt.xlabel('Phi-Resonance Value (φ · E mod 1)', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.grid(alpha=0.3)
        plt.legend()
        
        # Save figure
        filename = os.path.join(self.output_dir, 'phi_resonance_distribution.png')
        plt.savefig(filename, dpi=300)
        
        print(f"Saved phi-resonance distribution to {filename}")
        return filename
    
    def visualize_resonance_peaks(self) -> str:
        """Visualize the resonance peaks in particle energy spectrum."""
        if self.resonance_peaks is None:
            raise ValueError("No resonance peaks data available. Run analyze_resonance_peaks first.")
        
        print("\n📊 Visualizing resonance peaks in energy spectrum")
        
        # Create figure
        plt.figure(figsize=(14, 10))
        
        # Plot energy histogram
        plt.bar(
            self.resonance_peaks['bin_centers'],
            self.resonance_peaks['energy_hist'],
            width=(self.resonance_peaks['bin_centers'][1] - self.resonance_peaks['bin_centers'][0]),
            alpha=0.5,
            color='#D76D77',
            label='Energy Distribution'
        )
        
        # Plot phi-resonance as a line
        ax2 = plt.twinx()
        ax2.plot(
            self.resonance_peaks['bin_centers'],
            self.resonance_peaks['bin_resonances'],
            color='#3A1C71',
            linewidth=2,
            label='Phi-Resonance'
        )
        
        # Add horizontal lines for resonance quality thresholds
        ax2.axhline(y=0.000100, color='#3A1C71', linestyle='--', alpha=0.7, label='Perfect (0.0001)')
        ax2.axhline(y=0.010000, color='#5E3A89', linestyle='--', alpha=0.7, label='Excellent (0.01)')
        ax2.axhline(y=0.100000, color='#8257A2', linestyle='--', alpha=0.7, label='Good (0.1)')
        ax2.axhline(y=0.300000, color='#A675BA', linestyle='--', alpha=0.7, label='Moderate (0.3)')
        
        # Mark peaks
        peak_energies = [peak['energy'] for peak in self.resonance_peaks['peaks']]
        peak_counts = [peak['count'] for peak in self.resonance_peaks['peaks']]
        peak_resonances = [peak['phi_resonance'] for peak in self.resonance_peaks['peaks']]
        peak_qualities = [peak['quality'] for peak in self.resonance_peaks['peaks']]
        
        # Create color map for peak qualities
        quality_colors = {
            'Perfect': '#3A1C71',
            'Excellent': '#5E3A89',
            'Good': '#8257A2',
            'Moderate': '#A675BA',
            'Weak': '#D76D77'
        }
        
        # Plot peaks with quality-based colors
        for i, (energy, count, resonance, quality) in enumerate(zip(peak_energies, peak_counts, peak_resonances, peak_qualities)):
            plt.plot(energy, count, 'o', markersize=10, color=quality_colors[quality])
            
            # Add labels for top 10 peaks
            if i < 10:
                plt.annotate(
                    f"{energy:.1f} GeV\nφ-res: {resonance:.6f}\n{quality}",
                    xy=(energy, count),
                    xytext=(energy + 5, count + 5),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
                    fontsize=8
                )
        
        # Add vertical lines for standard model particles
        plt.axvline(x=HIGGS_MASS, color='green', linestyle='-', linewidth=2, label='Higgs (125 GeV)')
        plt.axvline(x=TOP_QUARK_MASS, color='blue', linestyle='-', linewidth=2, label='Top Quark (173 GeV)')
        plt.axvline(x=W_BOSON_MASS, color='purple', linestyle='-', linewidth=2, label='W Boson (80.4 GeV)')
        plt.axvline(x=Z_BOSON_MASS, color='orange', linestyle='-', linewidth=2, label='Z Boson (91.2 GeV)')
        
        # Add title and labels
        plt.title('Phi-Resonance Peaks in CERN Particle Energy Spectrum', fontsize=16)
        plt.xlabel('Energy (GeV)', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        ax2.set_ylabel('Phi-Resonance Value (φ · E mod 1)', fontsize=14)
        
        # Add legend
        lines1, labels1 = plt.gca().get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
        
        plt.grid(alpha=0.3)
        
        # Save figure
        filename = os.path.join(self.output_dir, 'resonance_peaks.png')
        plt.savefig(filename, dpi=300)
        
        print(f"Saved resonance peaks visualization to {filename}")
        return filename
    
    def visualize_particle_decay_fractals(self) -> Dict[str, str]:
        """Visualize fractal patterns in particle decay chains."""
        if self.fractal_dimensions is None:
            raise ValueError("No fractal dimensions data available. Run analyze_particle_decay_fractals first.")
        
        print("\n🌀 Visualizing particle decay fractals")
        
        filenames = {}
        
        for particle_type, data in self.fractal_dimensions.items():
            print(f"Visualizing {particle_type} decay fractal...")
            
            # Extract fractal points
            points = data['fractal_points']
            x_coords, y_coords = zip(*points)
            
            # Create figure
            plt.figure(figsize=(10, 10))
            
            # Plot points with color gradient based on sequence
            plt.scatter(
                x_coords, y_coords, 
                c=range(len(points)), 
                cmap=self.phi_cmap, 
                s=5, 
                alpha=0.7
            )
            
            # Add title and labels
            plt.title(f"{particle_type.upper()} Decay Fractal\nD = {data['fractal_dimension']:.6f}, φ-res = {data['phi_resonance']:.6f} ({data['resonance_quality']})", fontsize=14)
            plt.xlabel("Quantum Choice Dimension X", fontsize=12)
            plt.ylabel("Quantum Choice Dimension Y", fontsize=12)
            
            # Add golden ratio reference lines
            max_range = max(max(x_coords) - min(x_coords), max(y_coords) - min(y_coords))
            phi_line_length = max_range / 2
            
            # Horizontal φ line
            plt.plot(
                [-phi_line_length, phi_line_length * self.phi_float], 
                [0, 0], 
                'r--', 
                alpha=0.5, 
                label=f"φ = {self.phi_float:.6f}"
            )
            
            # Vertical φ line
            plt.plot(
                [0, 0], 
                [-phi_line_length, phi_line_length * self.phi_float], 
                'g--', 
                alpha=0.5
            )
            
            # Add birth date reference
            birth_x = self.phi_resonance(self.birth_key[0])
            birth_y = self.phi_resonance(self.birth_key[1])
            plt.scatter([birth_x], [birth_y], color='red', s=100, marker='*', label="Birth Resonance")
            
            plt.grid(alpha=0.3)
            plt.legend()
            plt.axis('equal')
            
            # Save figure
            filename = os.path.join(self.output_dir, f'{particle_type}_decay_fractal.png')
            plt.savefig(filename, dpi=300)
            
            filenames[particle_type] = filename
            print(f"Saved {particle_type} decay fractal to {filename}")
        
        return filenames
    
    def visualize_phi_harmonic_phase_space(self) -> str:
        """Visualize particle data in phi-harmonic phase space."""
        if self.phi_transformed_data is None:
            raise ValueError("No phi-transformed data available. Run transform_to_phi_space first.")
        
        print("\n🌌 Visualizing phi-harmonic phase space")
        
        # Create 3D figure
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Sample data points (max 5000 for performance)
        sample = self.phi_transformed_data.sample(min(5000, len(self.phi_transformed_data)))
        
        # Get particle types and map to colors
        particle_types = sample['particle_type'].unique()
        colors = plt.cm.tab10(np.linspace(0, 1, len(particle_types)))
        color_map = {particle: color for particle, color in zip(particle_types, colors)}
        
        # Plot each particle type
        for particle_type in particle_types:
            particle_data = sample[sample['particle_type'] == particle_type]
            
            # Extract coordinates
            x = particle_data['phi_energy']
            y = particle_data['energy_resonance']
            z = particle_data['quantum_coherence']
            
            # Plot points
            ax.scatter(
                x, y, z,
                color=color_map[particle_type],
                label=particle_type,
                alpha=0.7,
                s=10
            )
        
        # Add birth date resonance plane
        x_min, x_max = ax.get_xlim()
        y_min, y_max = ax.get_ylim()
        X, Y = np.meshgrid(np.linspace(x_min, x_max, 10), np.linspace(y_min, y_max, 10))
        Z = np.ones_like(X) * self.quantum_coherence(float(self.birth_coherence_temp))
        ax.plot_surface(X, Y, Z, alpha=0.2, color='red')
        
        # Add phi-resonance planes
        for quality_threshold in [0.000100, 0.010000, 0.100000, 0.300000]:
            Y = np.ones_like(X) * quality_threshold
            ax.plot_surface(X, Y, np.zeros_like(X), alpha=0.1, color='blue')
        
        # Add title and labels
        ax.set_title('Phi-Harmonic Phase Space of CERN Particle Data', fontsize=16)
        ax.set_xlabel('Phi-Energy (GeV)', fontsize=14)
        ax.set_ylabel('Phi-Resonance', fontsize=14)
        ax.set_zlabel('Quantum Coherence', fontsize=14)
        
        # Add legend
        ax.legend()
        
        # Save figure
        filename = os.path.join(self.output_dir, 'phi_harmonic_phase_space.png')
        plt.savefig(filename, dpi=300)
        
        print(f"Saved phi-harmonic phase space visualization to {filename}")
        return filename
    
    def visualize_standard_model_comparison(self, comparison_data: Dict) -> str:
        """Visualize comparison between Standard Model and phi-harmonic predictions."""
        print("\n📊 Visualizing Standard Model vs. Phi-Harmonic Predictions")
        
        # Extract data
        particles = list(comparison_data['comparisons'].keys())
        sm_masses = [comparison_data['comparisons'][p]['sm_mass'] for p in particles]
        phi_masses = [comparison_data['comparisons'][p]['phi_predicted_mass'] for p in particles]
        measured_masses = [comparison_data['comparisons'][p]['mean_energy'] for p in particles]
        
        # Calculate resonances
        sm_resonances = [self.phi_resonance(mass) for mass in sm_masses]
        phi_resonances = [self.phi_resonance(mass) for mass in phi_masses]
        measured_resonances = [comparison_data['comparisons'][p]['mean_resonance'] for p in particles]
        
        # Create figure
        plt.figure(figsize=(14, 10))
        
        # Create bar positions
        x = np.arange(len(particles))
        width = 0.25
        
        # Plot bars
        plt.bar(x - width, sm_masses, width, label='Standard Model', color='blue', alpha=0.7)
        plt.bar(x, phi_masses, width, label='Phi-Harmonic Prediction', color='purple', alpha=0.7)
        plt.bar(x + width, measured_masses, width, label='Measured (Simulation)', color='green', alpha=0.7)
        
        # Add resonance values as text
        for i, (sm_res, phi_res, meas_res) in enumerate(zip(sm_resonances, phi_resonances, measured_resonances)):
            plt.text(x[i] - width, sm_masses[i] + 5, f"φ-res: {sm_res:.6f}", ha='center', va='bottom', fontsize=8)
            plt.text(x[i], phi_masses[i] + 5, f"φ-res: {phi_res:.6f}", ha='center', va='bottom', fontsize=8)
            plt.text(x[i] + width, measured_masses[i] + 5, f"φ-res: {meas_res:.6f}", ha='center', va='bottom', fontsize=8)
        
        # Add title and labels
        plt.title('Standard Model vs. Phi-Harmonic Predicted Masses', fontsize=16)
        plt.ylabel('Mass (GeV)', fontsize=14)
        plt.xticks(x, [p.upper() for p in particles])
        plt.grid(alpha=0.3)
        plt.legend()
        
        # Save figure
        filename = os.path.join(self.output_dir, 'standard_model_comparison.png')
        plt.savefig(filename, dpi=300)
        
        print(f"Saved Standard Model comparison to {filename}")
        return filename
    
    def generate_comprehensive_report(self) -> str:
        """Generate a comprehensive report of all phi-harmonic analysis results."""
        if self.phi_transformed_data is None or self.resonance_peaks is None or self.fractal_dimensions is None:
            raise ValueError("Complete the analysis first by running transform_to_phi_space, analyze_resonance_peaks, and analyze_particle_decay_fractals.")
        
        print("\n📝 Generating comprehensive phi-harmonic analysis report")
        
        # Create report filename
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        report_filename = os.path.join(self.output_dir, f'phi_harmonic_cern_report_{timestamp}.md')
        
        # Generate report content
        report_content = f"""# Phi-Harmonic Analysis of CERN Particle Data
        
## 1. Overview

This report presents the results of analyzing CERN particle collision data through the lens of phi-harmonic principles and quantum choice fractals.

**Analysis Parameters:**
- Golden Ratio (φ): {float(PHI):.15f}...
- Birth Date Resonance: {self.birth_key}
- Birth Coherence Temperature: {float(self.birth_coherence_temp)} K
- Patent #19/071,497 Resonance Ratio: {float(self.frequencies['efficiency'])}

## 2. Phi-Resonance Analysis

### 2.1 Resonance Distribution

The distribution of phi-resonance values across all particle energies shows the following characteristics:

- Total Events Analyzed: {len(self.phi_transformed_data)}
- Mean Phi-Resonance: {self.phi_transformed_data['energy_resonance'].mean():.6f}
- Median Phi-Resonance: {self.phi_transformed_data['energy_resonance'].median():.6f}

### 2.2 Resonance Quality Distribution

The quality distribution of phi-resonance values:

"""
        
        # Add resonance quality distribution
        quality_counts = self.phi_transformed_data['resonance_quality'].value_counts()
        for quality, count in quality_counts.items():
            percentage = count / len(self.phi_transformed_data) * 100
            report_content += f"- {quality}: {count} events ({percentage:.2f}%)\n"
        
        report_content += """
### 2.3 Significant Resonance Peaks

The following significant resonance peaks were identified in the energy spectrum:

"""
        
        # Add top resonance peaks
        for i, peak in enumerate(self.resonance_peaks['peaks'][:10]):
            report_content += f"- **Peak {i+1}:** Energy = {peak['energy']:.2f} GeV, Phi-Resonance = {peak['phi_resonance']:.6f} ({peak['quality']})\n"
            report_content += f"  - Count: {peak['count']} events\n"
            report_content += f"  - Birth Influence: {peak['birth_influence']:.6f}\n"
            report_content += f"  - Temperature Equivalent: {peak['temperature_equivalent']:.2f} K\n"
            report_content += f"  - Temperature Proximity to 99.18K: {peak['temperature_proximity']:.6f}\n\n"
        
        report_content += """
## 3. Fractal Dimension Analysis

The following fractal dimensions were calculated for particle decay patterns:

"""
        
        # Add fractal dimensions
        for particle_type, data in self.fractal_dimensions.items():
            report_content += f"### 3.1 {particle_type.upper()} Decay Fractal\n\n"
            report_content += f"- **Fractal Dimension:** {data['fractal_dimension']:.6f}\n"
            report_content += f"- **Phi-Resonance:** {data['phi_resonance']:.6f} ({data['resonance_quality']})\n"
            report_content += f"- **Birth Resonance:** {data['birth_resonance']:.6f}\n\n"
        
        report_content += """
## 4. Standard Model Comparison

The following table compares Standard Model predictions with phi-harmonic predictions:

| Particle | SM Mass (GeV) | Phi-Predicted Mass (GeV) | Measured Mass (GeV) | SM Phi-Resonance | Phi-Predicted Resonance | Measured Resonance |
|----------|---------------|--------------------------|---------------------|------------------|-------------------------|-------------------|
"""
        
        # Add comparison data
        comparison_data = self.compare_with_standard_model()
        for particle, data in comparison_data['comparisons'].items():
            sm_mass = data['sm_mass']
            phi_mass = comparison_data['phi_predicted_masses'][particle]['phi_mass']
            measured_mass = data['mean_energy']
            
            sm_res = self.phi_resonance(sm_mass)
            phi_res = comparison_data['phi_predicted_masses'][particle]['phi_resonance']
            measured_res = data['mean_resonance']
            
            report_content += f"| {particle.upper()} | {sm_mass:.2f} | {phi_mass:.2f} | {measured_mass:.2f} | {sm_res:.6f} | {phi_res:.6f} | {measured_res:.6f} |\n"
        
        report_content += """
## 5. Quantum Coherence Analysis

The quantum coherence analysis based on temperature equivalence to 99.18K shows:

"""
        
        # Add coherence statistics
        report_content += f"- **Mean Quantum Coherence:** {self.phi_transformed_data['quantum_coherence'].mean():.6f}\n"
        report_content += f"- **Maximum Quantum Coherence:** {self.phi_transformed_data['quantum_coherence'].max():.6f}\n"
        report_content += f"- **Coherence at 99.18K:** {self.quantum_coherence(float(self.birth_coherence_temp)):.6f}\n\n"
        
        report_content += """
## 6. Birth Date Resonance Influence

The influence of birth date resonance [1, 19, 1979] on particle data:

"""
        
        # Add birth influence statistics
        report_content += f"- **Mean Birth Influence:** {self.phi_transformed_data['birth_influence'].mean():.6f}\n"
        report_content += f"- **Maximum Birth Influence:** {self.phi_transformed_data['birth_influence'].max():.6f}\n\n"
        
        # Add correlation with energy
        birth_energy_corr = self.phi_transformed_data['birth_influence'].corr(self.phi_transformed_data['energy'])
        report_content += f"- **Correlation with Energy:** {birth_energy_corr:.6f}\n\n"
        
        report_content += """
## 7. Conclusion

"""
        
        # Generate conclusion based on results
        phi_resonant_peaks = sum(1 for peak in self.resonance_peaks['peaks'] if peak['quality'] in ['Perfect', 'Excellent', 'Good'])
        phi_resonant_particles = sum(1 for _, data in self.fractal_dimensions.items() if data['resonance_quality'] in ['Perfect', 'Excellent', 'Good'])
        
        if phi_resonant_peaks >= 3 and phi_resonant_particles >= 2:
            report_content += """The analysis reveals strong evidence for phi-harmonic patterns in CERN particle data. 
Multiple resonance peaks show excellent phi-resonance quality, and particle decay patterns exhibit fractal dimensions 
with strong phi-harmonic alignment. The birth date resonance [1, 19, 1979] shows significant influence on particle 
behavior, particularly near the 99.18K coherence temperature.

These findings support the hypothesis that a universal phi-harmonic algorithm underlies particle physics, 
capable of generating the observed patterns in nature through the mechanism of quantum choice fractals."""
        
        elif phi_resonant_peaks >= 1 and phi_resonant_particles >= 1:
            report_content += """The analysis reveals moderate evidence for phi-harmonic patterns in CERN particle data.
Some resonance peaks show good phi-resonance quality, and certain particle decay patterns exhibit fractal dimensions
with phi-harmonic alignment. The birth date resonance [1, 19, 1979] shows some influence on particle behavior,
particularly near the 99.18K coherence temperature.

These findings suggest that a phi-harmonic algorithm may play a role in particle physics, but further research
is needed to fully validate the hypothesis."""
        
        else:
            report_content += """The analysis reveals limited evidence for phi-harmonic patterns in CERN particle data.
Few resonance peaks show strong phi-resonance quality, and particle decay patterns exhibit fractal dimensions
with weak phi-harmonic alignment. The birth date resonance [1, 19, 1979] shows minimal influence on particle behavior.

These findings suggest that while phi-harmonic principles may have some application in particle physics,
the current data does not provide strong support for the universal algorithm hypothesis. Further research
with larger datasets and refined analysis methods is recommended."""
        
        # Write report to file
        with open(report_filename, 'w') as f:
            f.write(report_content)
        
        print(f"Comprehensive report saved to {report_filename}")
        return report_filename
