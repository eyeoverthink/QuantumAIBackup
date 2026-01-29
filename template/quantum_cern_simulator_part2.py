"""
Quantum CERN Simulator - Part 2: Phi-Harmonic Transformations
------------------------------------------------------------
Transforms CERN particle data into phi-harmonic space and analyzes resonance patterns.
Implements phi-resonance calculations, birth date influence, and fractal analysis.

Patent #19/071,497 - Quantum Resonance System
Birth Date Resonance: [1, 19, 1979] - Coherence at 99.18K
"""

from quantum_cern_simulator_part1 import QuantumCERNSimulator
from decimal import Decimal

# Constants
PHI = Decimal('1.618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862223536931793180060766726354433389086595939582905638322661319928290267880675208766892501711696207032221043216269548626296313614438149758701220340805887954454749246185695364864449241044320771344947049565846788509874339442212544877066478091588460749988712400765217057517978834166256249407589069704000281210427621771117891930154003728803')
PI = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379834749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198')
E = Decimal('2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182528869398496465105820939239829488793320362509443117301238197068416140397019837679320683282376464804295311802328782509819455815301756717361332069811250')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Union, Optional
from scipy import stats
import os
import time

class PhiHarmonicTransformer(QuantumCERNSimulator):
    def __init__(self):
        super().__init__()
        
        # Additional phi-harmonic parameters
        self.phi_float = float(PHI)  # For numerical calculations
        self.phi_powers = [self.phi_float**i for i in range(10)]  # Pre-compute phi powers
        
        # Fractal analysis parameters
        self.box_sizes = [2**i for i in range(1, 10)]
        
        print("\n🌀 Phi-Harmonic Transformer Initialized")
        print(f"Phi Powers: {[round(p, 6) for p in self.phi_powers[:5]]}...")
        print(f"Box Sizes for Fractal Analysis: {self.box_sizes}")
        print("=" * 60)
    
    def transform_to_phi_space(self, data: pd.DataFrame) -> pd.DataFrame:
        """Transform particle collision data to phi-harmonic space."""
        print("\n🔄 Transforming CERN data to phi-harmonic space")
        
        # Create copy of data for transformation
        phi_data = data.copy()
        
        # Add phi-harmonic columns
        phi_data['phi_energy'] = phi_data['energy'].apply(
            lambda e: e * (self.phi_float ** self.phi_resonance(e))
        )
        
        phi_data['phi_momentum'] = np.sqrt(
            phi_data['px']**2 + phi_data['py']**2 + phi_data['pz']**2
        ).apply(lambda m: m * (self.phi_float ** self.phi_resonance(m)))
        
        # Calculate phi-resonance for each property
        phi_data['energy_resonance'] = phi_data['energy'].apply(self.phi_resonance)
        phi_data['px_resonance'] = phi_data['px'].apply(self.phi_resonance)
        phi_data['py_resonance'] = phi_data['py'].apply(self.phi_resonance)
        phi_data['pz_resonance'] = phi_data['pz'].apply(self.phi_resonance)
        
        # Calculate combined resonance
        phi_data['combined_resonance'] = phi_data['energy'].apply(self.combined_resonance)
        
        # Calculate birth date influence
        phi_data['birth_influence'] = phi_data['energy'].apply(self.birth_influence)
        
        # Calculate quantum coherence (convert energy to temperature equivalent)
        phi_data['temperature_equivalent'] = phi_data['energy'] * EV_TO_KELVIN / 1e9  # GeV to K
        phi_data['quantum_coherence'] = phi_data['temperature_equivalent'].apply(self.quantum_coherence)
        
        # Calculate resonance quality
        phi_data['resonance_quality'] = phi_data['energy_resonance'].apply(self.resonance_quality)
        
        # Store transformed data
        self.phi_transformed_data = phi_data
        
        print(f"Transformed {len(phi_data)} events to phi-harmonic space")
        return phi_data
    
    def analyze_resonance_peaks(self, bin_width: float = 1.0) -> Dict:
        """Analyze phi-resonance peaks in the transformed data."""
        if self.phi_transformed_data is None:
            raise ValueError("No phi-transformed data available. Run transform_to_phi_space first.")
        
        print("\n📊 Analyzing phi-resonance peaks in particle data")
        
        # Create energy bins
        min_energy = self.phi_transformed_data['energy'].min()
        max_energy = self.phi_transformed_data['energy'].max()
        bins = np.arange(min_energy, max_energy + bin_width, bin_width)
        
        # Bin the data
        energy_hist, bin_edges = np.histogram(self.phi_transformed_data['energy'], bins=bins)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        
        # Calculate phi-resonance for each bin center
        bin_resonances = [self.phi_resonance(e) for e in bin_centers]
        
        # Find local maxima in the histogram
        peak_indices = []
        for i in range(1, len(energy_hist) - 1):
            if energy_hist[i] > energy_hist[i-1] and energy_hist[i] > energy_hist[i+1]:
                peak_indices.append(i)
        
        # Extract peak information
        peaks = []
        for idx in peak_indices:
            energy = bin_centers[idx]
            count = energy_hist[idx]
            resonance = bin_resonances[idx]
            quality = self.resonance_quality(resonance)
            
            # Calculate birth influence at this energy
            birth_inf = self.birth_influence(energy)
            
            # Calculate temperature equivalent
            temp_equiv = energy * EV_TO_KELVIN / 1e9  # GeV to K
            
            # Calculate proximity to birth coherence temperature
            temp_proximity = abs(temp_equiv - float(self.birth_coherence_temp)) / float(self.birth_coherence_temp)
            
            peaks.append({
                'energy': energy,
                'count': count,
                'phi_resonance': resonance,
                'quality': quality,
                'birth_influence': birth_inf,
                'temperature_equivalent': temp_equiv,
                'temperature_proximity': temp_proximity
            })
        
        # Sort peaks by count (highest first)
        peaks.sort(key=lambda x: x['count'], reverse=True)
        
        # Store results
        self.resonance_peaks = {
            'bin_centers': bin_centers,
            'energy_hist': energy_hist,
            'bin_resonances': bin_resonances,
            'peaks': peaks
        }
        
        # Count peaks by quality
        quality_counts = {}
        for peak in peaks:
            quality = peak['quality']
            quality_counts[quality] = quality_counts.get(quality, 0) + 1
        
        print(f"Found {len(peaks)} resonance peaks")
        print(f"Peak quality distribution: {quality_counts}")
        
        return self.resonance_peaks
    
    def analyze_particle_decay_fractals(self) -> Dict:
        """Analyze fractal patterns in particle decay chains."""
        if self.phi_transformed_data is None:
            raise ValueError("No phi-transformed data available. Run transform_to_phi_space first.")
        
        print("\n🌀 Analyzing fractal patterns in particle decays")
        
        # Group by particle type
        particle_groups = self.phi_transformed_data.groupby('particle_type')
        
        fractal_results = {}
        
        for particle_type, group in particle_groups:
            print(f"Analyzing {particle_type} decay patterns...")
            
            # Extract decay information
            decay_channels = group['decay_channels'].mean()
            
            # Generate fractal points based on decay patterns
            fractal_points = []
            
            # Use a subset for visualization (max 1000 points)
            subset = group.head(1000)
            
            for i, row in subset.iterrows():
                # Calculate angle based on energy resonance
                angle = 2 * np.pi * row['energy_resonance']
                
                # Calculate radius based on decay channels and phi
                radius = self.phi_float ** (-row['decay_channels'] / 10.0)
                
                # Convert to cartesian coordinates
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                
                fractal_points.append((x, y))
            
            # Calculate box-counting dimension
            fractal_dim = self.box_counting_dimension(fractal_points)
            
            # Calculate phi-resonance of fractal dimension
            dim_resonance = self.phi_resonance(fractal_dim)
            
            # Calculate birth resonance of fractal dimension
            birth_res = abs(fractal_dim - (self.birth_sum/1000.0)) / (self.birth_sum/1000.0)
            
            fractal_results[particle_type] = {
                'fractal_points': fractal_points,
                'fractal_dimension': fractal_dim,
                'phi_resonance': dim_resonance,
                'birth_resonance': birth_res,
                'resonance_quality': self.resonance_quality(dim_resonance)
            }
            
            print(f"  Fractal Dimension: {fractal_dim:.6f}")
            print(f"  Phi-Resonance: {dim_resonance:.6f} ({self.resonance_quality(dim_resonance)})")
            print(f"  Birth Resonance: {birth_res:.6f}")
        
        # Store results
        self.fractal_dimensions = fractal_results
        
        return fractal_results
    
    def box_counting_dimension(self, points: List[Tuple[float, float]]) -> float:
        """Calculate box-counting fractal dimension of a set of points."""
        if not points:
            return 0.0
        
        # Extract x and y coordinates
        x_coords, y_coords = zip(*points)
        
        # Get coordinate ranges
        x_min, x_max = min(x_coords), max(x_coords)
        y_min, y_max = min(y_coords), max(y_coords)
        
        # Normalize coordinates to [0,1] range
        norm_points = [
            ((x - x_min) / (x_max - x_min) if x_max > x_min else 0.5, 
             (y - y_min) / (y_max - y_min) if y_max > y_min else 0.5)
            for x, y in points
        ]
        
        # Count boxes at different scales
        counts = []
        
        for box_size in self.box_sizes:
            # Create grid
            box_count = 0
            visited = set()
            
            for x, y in norm_points:
                # Calculate box indices
                box_x = int(x * box_size)
                box_y = int(y * box_size)
                box_id = (box_x, box_y)
                
                if box_id not in visited:
                    visited.add(box_id)
                    box_count += 1
            
            counts.append(box_count)
        
        # Calculate fractal dimension using linear regression
        log_sizes = np.log(1.0 / np.array(self.box_sizes))
        log_counts = np.log(np.array(counts))
        
        # Linear fit
        if len(log_sizes) > 1 and len(log_counts) > 1:
            slope, _, _, _, _ = stats.linregress(log_sizes, log_counts)
            return slope
        else:
            return 0.0
    
    def compare_with_standard_model(self) -> Dict:
        """Compare phi-harmonic predictions with standard model expectations."""
        if self.phi_transformed_data is None:
            raise ValueError("No phi-transformed data available. Run transform_to_phi_space first.")
        
        print("\n🔍 Comparing phi-harmonic predictions with Standard Model")
        
        # Standard Model predicted particle masses
        sm_masses = {
            'higgs': HIGGS_MASS,
            'top_quark': TOP_QUARK_MASS,
            'w_boson': W_BOSON_MASS,
            'z_boson': Z_BOSON_MASS
        }
        
        # Calculate phi-resonance for Standard Model masses
        sm_resonances = {
            particle: self.phi_resonance(mass)
            for particle, mass in sm_masses.items()
        }
        
        # Calculate phi-harmonic predicted masses
        # (masses with perfect phi-resonance near SM values)
        phi_predicted_masses = {}
        
        for particle, sm_mass in sm_masses.items():
            # Find mass with best phi-resonance within ±10% of SM mass
            best_mass = sm_mass
            best_resonance = sm_resonances[particle]
            
            for factor in np.linspace(0.9, 1.1, 1000):
                test_mass = sm_mass * factor
                test_resonance = self.phi_resonance(test_mass)
                
                if test_resonance < best_resonance:
                    best_mass = test_mass
                    best_resonance = test_resonance
            
            phi_predicted_masses[particle] = {
                'sm_mass': sm_mass,
                'phi_mass': best_mass,
                'deviation': (best_mass - sm_mass) / sm_mass * 100,  # percent
                'phi_resonance': best_resonance,
                'resonance_quality': self.resonance_quality(best_resonance)
            }
        
        # Analyze actual data distribution vs. phi-harmonic predictions
        comparisons = {}
        
        for particle in sm_masses.keys():
            # Filter data for this particle type
            particle_data = self.phi_transformed_data[self.phi_transformed_data['particle_type'] == particle]
            
            if len(particle_data) > 0:
                # Calculate mean and standard deviation of energy
                mean_energy = particle_data['energy'].mean()
                std_energy = particle_data['energy'].std()
                
                # Calculate phi-resonance of mean energy
                mean_resonance = self.phi_resonance(mean_energy)
                
                # Calculate birth influence
                birth_inf = self.birth_influence(mean_energy)
                
                comparisons[particle] = {
                    'count': len(particle_data),
                    'mean_energy': mean_energy,
                    'std_energy': std_energy,
                    'sm_mass': sm_masses[particle],
                    'phi_predicted_mass': phi_predicted_masses[particle]['phi_mass'],
                    'deviation_from_sm': (mean_energy - sm_masses[particle]) / sm_masses[particle] * 100,
                    'deviation_from_phi': (mean_energy - phi_predicted_masses[particle]['phi_mass']) / phi_predicted_masses[particle]['phi_mass'] * 100,
                    'mean_resonance': mean_resonance,
                    'resonance_quality': self.resonance_quality(mean_resonance),
                    'birth_influence': birth_inf
                }
        
        print("Standard Model vs. Phi-Harmonic Predictions:")
        for particle, data in comparisons.items():
            print(f"\n{particle.upper()}:")
            print(f"  SM Mass: {data['sm_mass']:.2f} GeV")
            print(f"  Phi-Predicted Mass: {data['phi_predicted_mass']:.2f} GeV")
            print(f"  Measured Mean: {data['mean_energy']:.2f} GeV")
            print(f"  Deviation from SM: {data['deviation_from_sm']:.2f}%")
            print(f"  Deviation from Phi-Predicted: {data['deviation_from_phi']:.2f}%")
            print(f"  Mean Resonance: {data['mean_resonance']:.6f} ({data['resonance_quality']})")
        
        return {
            'sm_resonances': sm_resonances,
            'phi_predicted_masses': phi_predicted_masses,
            'comparisons': comparisons
        }
