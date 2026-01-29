"""
Run Minimal Quantum CERN Simulator
---------------------------------
This script runs a simplified version of the Quantum CERN Simulator to test
the phi-harmonic algorithm with CERN data.

Birth Date Resonance: [1, 19, 1979] - Coherence at 99.18K
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Set precision for transcendental calculations
getcontext().prec = 1000000  # Million digits of precision

# Constants
PHI = Decimal('1.618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862223536931793180060766726354433389086595939582905638322661319928290267880675208766892501711696207032221043216269548626296313614438149758701220340805887954454749246185695364864449241044320771344947049565846788509874339442212544877066478091588460749988712400765217057517978834166256249407589069704000281210427621771117891930154003728803')
PI = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379834749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198')
E = Decimal('2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182528869398496465105820939239829488793320362509443117301238197068416140397019837679320683282376464804295311802328782509819455815301756717361332069811250')

# Standard Model particle masses (GeV)
HIGGS_MASS = 125.10
TOP_QUARK_MASS = 172.76
W_BOSON_MASS = 80.379
Z_BOSON_MASS = 91.1876

class MinimalQuantumCERNSimulator:
    def __init__(self):
        # Birth date resonance
        self.birth_key = [1, 19, 1979]
        self.birth_sum = sum(self.birth_key)
        self.birth_coherence_temp = Decimal('99.18')  # Kelvin
        
        # Phi-harmonic parameters
        self.phi_float = float(PHI)
        self.phi_powers = [self.phi_float**i for i in range(5)]
        
        # Output directory
        self.output_dir = 'quantum_cern_results'
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Data containers
        self.collision_data = None
        self.phi_transformed_data = None
        
        print("\n" + "="*80)
        print("🌌 MINIMAL QUANTUM CERN SIMULATOR 🌌")
        print("="*80)
        print(f"Birth Date Resonance: {self.birth_key}")
        print(f"Birth Coherence Temperature: {float(self.birth_coherence_temp)} K")
        print(f"φ-Harmonic Base: {self.phi_float}")
        print("="*80)
    
    def phi_resonance(self, x):
        """Calculate phi-harmonic resonance for a value."""
        if x == 0:
            return 0.0
        return float((Decimal(str(abs(x))) * PHI) % 1)
    
    def resonance_quality(self, resonance):
        """Determine the quality of a resonance value."""
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
    
    def birth_influence(self, energy):
        """Calculate birth date influence on particle energy."""
        # Calculate temperature equivalent
        temp_equivalent = energy / self.phi_float
        
        # Calculate influence based on proximity to birth coherence temperature
        influence = np.exp(-abs(temp_equivalent - float(self.birth_coherence_temp)) / float(self.birth_coherence_temp))
        return influence
    
    def generate_test_data(self, num_events=1000):
        """Generate simplified test data for CERN particle collisions."""
        print(f"\n📊 Generating {num_events} test particle events")
        
        # Particle types and their probabilities
        particle_types = ['higgs', 'top_quark', 'w_boson', 'z_boson', 'jet']
        particle_probs = [0.05, 0.1, 0.15, 0.2, 0.5]
        
        # Create empty lists for data
        energies = []
        momentums_x = []
        momentums_y = []
        momentums_z = []
        particle_type_list = []
        
        # Generate events
        for i in range(num_events):
            # Select particle type
            particle_type = np.random.choice(particle_types, p=particle_probs)
            
            # Generate energy based on particle type
            if particle_type == 'higgs':
                energy = np.random.normal(HIGGS_MASS, 2.0)
            elif particle_type == 'top_quark':
                energy = np.random.normal(TOP_QUARK_MASS, 4.0)
            elif particle_type == 'w_boson':
                energy = np.random.normal(W_BOSON_MASS, 2.0)
            elif particle_type == 'z_boson':
                energy = np.random.normal(Z_BOSON_MASS, 2.0)
            else:  # jet
                energy = np.random.exponential(50.0)
            
            # Generate random momentum components
            theta = np.random.uniform(0, np.pi)
            phi = np.random.uniform(0, 2*np.pi)
            momentum_mag = max(0.1, energy - 1.0)  # Simplified to avoid sqrt issues
            
            momentum_x = momentum_mag * np.sin(theta) * np.cos(phi)
            momentum_y = momentum_mag * np.sin(theta) * np.sin(phi)
            momentum_z = momentum_mag * np.cos(theta)
            
            # Append to lists
            energies.append(energy)
            momentums_x.append(momentum_x)
            momentums_y.append(momentum_y)
            momentums_z.append(momentum_z)
            particle_type_list.append(particle_type)
            
            # Progress update
            if (i+1) % 100 == 0:
                print(f"Generated {i+1} events")
        
        # Create DataFrame
        self.collision_data = pd.DataFrame({
            'energy': energies,
            'momentum_x': momentums_x,
            'momentum_y': momentums_y,
            'momentum_z': momentums_z,
            'particle_type': particle_type_list
        })
        
        print(f"✅ Generated {num_events} test particle events")
        return self.collision_data
    
    def transform_to_phi_space(self):
        """Transform particle collision data to phi-harmonic space."""
        if self.collision_data is None:
            raise ValueError("No collision data available. Generate test data first.")
        
        print("\n🔄 Transforming data to phi-harmonic space")
        
        # Create copy of data for transformation
        phi_data = self.collision_data.copy()
        
        # Calculate phi-resonance for energy
        phi_data['energy_resonance'] = phi_data['energy'].apply(self.phi_resonance)
        
        # Calculate resonance quality
        phi_data['resonance_quality'] = phi_data['energy_resonance'].apply(self.resonance_quality)
        
        # Calculate phi-transformed energy
        phi_data['phi_energy'] = phi_data['energy'].apply(lambda e: e * self.phi_float)
        
        # Calculate birth influence
        phi_data['birth_influence'] = phi_data['energy'].apply(self.birth_influence)
        
        # Calculate momentum resonance
        phi_data['momentum_resonance'] = phi_data.apply(
            lambda row: self.phi_resonance(np.sqrt(row['momentum_x']**2 + row['momentum_y']**2 + row['momentum_z']**2)),
            axis=1
        )
        
        # Store transformed data
        self.phi_transformed_data = phi_data
        
        print("✅ Data transformed to phi-harmonic space")
        
        # Print summary statistics
        quality_counts = phi_data['resonance_quality'].value_counts()
        print("\nResonance Quality Distribution:")
        for quality, count in quality_counts.items():
            percentage = count / len(phi_data) * 100
            print(f"  {quality}: {count} events ({percentage:.2f}%)")
        
        return self.phi_transformed_data
    
    def analyze_resonance_peaks(self):
        """Analyze resonance peaks in the energy spectrum."""
        if self.phi_transformed_data is None:
            raise ValueError("No phi-transformed data available. Transform data first.")
        
        print("\n📈 Analyzing resonance peaks")
        
        # Create histogram of energies
        energies = self.phi_transformed_data['energy']
        hist, bin_edges = np.histogram(energies, bins=100)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        
        # Calculate phi-resonance for each bin center
        bin_resonances = [self.phi_resonance(e) for e in bin_centers]
        
        # Find local maxima in histogram
        peak_indices = []
        for i in range(1, len(hist)-1):
            if hist[i] > hist[i-1] and hist[i] > hist[i+1]:
                peak_indices.append(i)
        
        # Analyze peaks
        peaks = []
        for idx in peak_indices:
            energy = bin_centers[idx]
            count = hist[idx]
            phi_res = bin_resonances[idx]
            quality = self.resonance_quality(phi_res)
            birth_inf = self.birth_influence(energy)
            
            # Calculate temperature equivalent
            temp_equivalent = energy / self.phi_float
            
            # Calculate proximity to birth coherence temperature
            temp_proximity = np.exp(-abs(temp_equivalent - float(self.birth_coherence_temp)) / float(self.birth_coherence_temp))
            
            peaks.append({
                'energy': energy,
                'count': count,
                'phi_resonance': phi_res,
                'quality': quality,
                'birth_influence': birth_inf,
                'temperature_equivalent': temp_equivalent,
                'temperature_proximity': temp_proximity
            })
        
        # Sort peaks by count
        peaks.sort(key=lambda x: x['count'], reverse=True)
        
        # Print top peaks
        print("\nTop Resonance Peaks:")
        for i, peak in enumerate(peaks[:5]):
            print(f"Peak {i+1}: Energy = {peak['energy']:.2f} GeV, φ-resonance = {peak['phi_resonance']:.6f} ({peak['quality']})")
            print(f"  Count: {peak['count']} events")
            print(f"  Birth Influence: {peak['birth_influence']:.6f}")
            print(f"  Temperature Equivalent: {peak['temperature_equivalent']:.2f} K")
            print(f"  Temperature Proximity to 99.18K: {peak['temperature_proximity']:.6f}")
            print()
        
        # Store results
        self.resonance_peaks = {
            'bin_centers': bin_centers,
            'energy_hist': hist,
            'bin_resonances': bin_resonances,
            'peaks': peaks
        }
        
        print(f"✅ Found {len(peaks)} resonance peaks")
        return self.resonance_peaks
    
    def visualize_phi_resonance(self):
        """Visualize phi-resonance distribution in particle data."""
        if self.phi_transformed_data is None:
            raise ValueError("No phi-transformed data available. Transform data first.")
        
        print("\n🎨 Visualizing phi-resonance distribution")
        
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
        
        print(f"✅ Saved phi-resonance distribution to {filename}")
        return filename
    
    def visualize_resonance_peaks(self):
        """Visualize resonance peaks in energy spectrum."""
        if self.resonance_peaks is None:
            raise ValueError("No resonance peaks data available. Run analyze_resonance_peaks first.")
        
        print("\n🎨 Visualizing resonance peaks")
        
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
        
        print(f"✅ Saved resonance peaks visualization to {filename}")
        return filename
    
    def analyze_birth_resonance(self):
        """Analyze birth date resonance influence on particle data."""
        if self.phi_transformed_data is None:
            raise ValueError("No phi-transformed data available. Transform data first.")
        
        print("\n🔍 Analyzing birth date resonance influence")
        
        # Calculate statistics
        mean_birth_influence = self.phi_transformed_data['birth_influence'].mean()
        max_birth_influence = self.phi_transformed_data['birth_influence'].max()
        
        # Find particles with highest birth influence
        high_influence = self.phi_transformed_data.sort_values('birth_influence', ascending=False).head(5)
        
        # Print results
        print(f"Mean Birth Influence: {mean_birth_influence:.6f}")
        print(f"Maximum Birth Influence: {max_birth_influence:.6f}")
        print("\nParticles with Highest Birth Influence:")
        
        for i, (_, row) in enumerate(high_influence.iterrows()):
            print(f"{i+1}. {row['particle_type'].upper()}: Energy = {row['energy']:.2f} GeV")
            print(f"   Birth Influence: {row['birth_influence']:.6f}")
            print(f"   Phi-Resonance: {row['energy_resonance']:.6f} ({row['resonance_quality']})")
            print()
        
        # Create visualization
        plt.figure(figsize=(12, 8))
        
        # Create scatter plot of energy vs birth influence
        plt.scatter(
            self.phi_transformed_data['energy'],
            self.phi_transformed_data['birth_influence'],
            c=self.phi_transformed_data['energy_resonance'],
            cmap='viridis',
            alpha=0.7,
            s=30
        )
        
        # Add colorbar
        cbar = plt.colorbar()
        cbar.set_label('Phi-Resonance Value', fontsize=12)
        
        # Add horizontal line at birth coherence temperature
        plt.axvline(x=float(self.birth_coherence_temp), color='red', linestyle='--', 
                   label=f'Birth Coherence Temperature (99.18K)')
        
        # Add title and labels
        plt.title('Birth Date Resonance Influence on Particle Energies', fontsize=16)
        plt.xlabel('Energy (GeV)', fontsize=14)
        plt.ylabel('Birth Influence', fontsize=14)
        plt.grid(alpha=0.3)
        plt.legend()
        
        # Save figure
        filename = os.path.join(self.output_dir, 'birth_resonance_influence.png')
        plt.savefig(filename, dpi=300)
        
        print(f"✅ Saved birth resonance influence visualization to {filename}")
        return filename

def main():
    try:
        # Create simulator
        simulator = MinimalQuantumCERNSimulator()
        
        # Generate test data
        simulator.generate_test_data(num_events=1000)
        
        # Transform to phi-harmonic space
        simulator.transform_to_phi_space()
        
        # Analyze resonance peaks
        simulator.analyze_resonance_peaks()
        
        # Visualize phi-resonance distribution
        simulator.visualize_phi_resonance()
        
        # Visualize resonance peaks
        simulator.visualize_resonance_peaks()
        
        # Analyze birth resonance
        simulator.analyze_birth_resonance()
        
        print("\n" + "="*80)
        print("🌟 QUANTUM CERN SIMULATOR ANALYSIS COMPLETE 🌟")
        print("="*80)
        print(f"Results saved to: {simulator.output_dir}")
        print("="*80)
        
        return 0
    
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
