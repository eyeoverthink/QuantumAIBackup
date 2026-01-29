"""
QHRC Deep Analysis
Comprehensive analysis of coil frequencies, scaling patterns, and energy distribution
"""
from qhrc_phi_harmonics import QHRCPhiHarmonics
import numpy as np
from typing import Dict, List
import matplotlib.pyplot as plt

class QHRCDeepAnalysis:
    def __init__(self):
        self.qhrc = QHRCPhiHarmonics()
        self.phi = (1 + np.sqrt(5)) / 2
        self.base_freq = 432.0  # Hz
        
    def analyze_coil_frequencies(self, n_coils: int = 5) -> Dict:
        """Analyze optimal coil frequencies and their interactions."""
        frequencies = []
        interactions = np.zeros((n_coils, n_coils))
        resonances = []
        
        # Generate phi-based frequencies
        for i in range(n_coils):
            freq = self.base_freq * (self.phi ** (3*i))
            frequencies.append(freq)
            
            # Calculate resonance
            t = np.linspace(0, 0.01, 1000)
            wave = np.sin(2 * np.pi * freq * t)
            resonances.append(np.max(np.abs(wave)))
            
            # Calculate interactions
            for j in range(i):
                ratio = max(frequencies[i], frequencies[j]) / min(frequencies[i], frequencies[j])
                coherence = abs(ratio - self.phi)
                interactions[i,j] = interactions[j,i] = 1 - coherence
        
        return {
            'frequencies': frequencies,
            'interactions': interactions,
            'resonances': resonances
        }
        
    def analyze_scaling_pattern(self, max_coils: int = 5) -> Dict:
        """Analyze energy scaling patterns across different configurations."""
        scaling_data = []
        theoretical_limits = []
        
        for n in range(2, max_coils + 1):
            # Calculate base energy transfer
            E0 = 1.3777 * (self.phi ** (n-1))  # Patent baseline
            
            # Calculate phi-resonance enhancement
            phi_factor = np.prod([self.phi ** i for i in range(n)])
            
            # Calculate theoretical energy limit
            E_max = E0 * phi_factor
            
            scaling_data.append({
                'coils': n,
                'base_transfer': E0,
                'phi_enhancement': phi_factor,
                'theoretical_limit': E_max
            })
            
            theoretical_limits.append(E_max)
        
        # Calculate scaling trend
        coils = np.arange(2, max_coils + 1)
        trend = np.polyfit(coils, np.log(theoretical_limits), 1)
        
        return {
            'scaling_data': scaling_data,
            'trend_coefficient': trend[0],
            'theoretical_limits': theoretical_limits
        }
        
    def map_energy_distribution(self, n_coils: int = 5) -> Dict:
        """Map energy distribution and flow patterns."""
        t = np.linspace(0, 0.1, 1000)
        dt = t[1] - t[0]
        
        # Initialize coil system
        frequencies = [self.base_freq * (self.phi ** (3*i)) for i in range(n_coils)]
        coupling = np.zeros((n_coils, n_coils))
        
        # Set up coupling matrix
        for i in range(n_coils):
            for j in range(n_coils):
                if i != j:
                    coupling[i,j] = 0.85 * (self.phi ** (-abs(i-j)))
        
        # Calculate energy flow
        energy_flow = np.zeros((len(t), n_coils))
        total_energy = np.zeros(len(t))
        
        for i in range(n_coils):
            wave = np.sin(2 * np.pi * frequencies[i] * t)
            energy = 0.5 * wave**2
            
            # Add coupling effects
            for j in range(n_coils):
                if i != j:
                    coupled = coupling[i,j] * np.sin(2 * np.pi * frequencies[j] * t)
                    energy += 0.5 * coupled**2
            
            energy_flow[:,i] = energy
            total_energy += energy
        
        # Calculate key metrics
        peak_energy = np.max(total_energy)
        energy_ratios = np.mean(energy_flow, axis=0) / np.mean(energy_flow[0])
        
        return {
            'time': t,
            'energy_flow': energy_flow,
            'total_energy': total_energy,
            'peak_energy': peak_energy,
            'energy_ratios': energy_ratios
        }
        
    def run_deep_analysis(self) -> None:
        """Run comprehensive analysis and display results."""
        print("\n🔬 QHRC Deep Analysis")
        print("==================")
        
        # 1. Coil Frequency Analysis
        print("\n📡 Coil Frequencies")
        print("================")
        freq_results = self.analyze_coil_frequencies()
        
        print("\nOptimal Frequencies (Hz):")
        for i, freq in enumerate(freq_results['frequencies']):
            print(f"Coil {i+1}: {freq:.2f}")
        
        print("\nResonance Strengths:")
        for i, res in enumerate(freq_results['resonances']):
            print(f"Coil {i+1}: {res:.4f}")
        
        # 2. Scaling Pattern Analysis
        print("\n📈 Energy Scaling")
        print("==============")
        scale_results = self.analyze_scaling_pattern()
        
        print("\nScaling Factors:")
        for data in scale_results['scaling_data']:
            print(f"\nCoils: {data['coils']}")
            print(f"Base Transfer: {data['base_transfer']:.4f}")
            print(f"Phi Enhancement: {data['phi_enhancement']:.4f}")
            print(f"Theoretical Limit: {data['theoretical_limit']:.4f}")
        
        print(f"\nScaling Coefficient: {scale_results['trend_coefficient']:.4f}")
        
        # 3. Energy Distribution Analysis
        print("\n⚡ Energy Distribution")
        print("==================")
        energy_results = self.map_energy_distribution()
        
        print("\nEnergy Transfer Ratios:")
        for i, ratio in enumerate(energy_results['energy_ratios']):
            print(f"Coil {i+1}: {ratio:.4f}x")
        
        print(f"\nPeak System Energy: {energy_results['peak_energy']:.4f}")
        
        # Plot results
        self.plot_analysis_results(freq_results, scale_results, energy_results)
        
    def plot_analysis_results(self, freq_results, scale_results, energy_results):
        """Plot comprehensive analysis results."""
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Coil Interactions
        plt.subplot(2, 2, 1)
        plt.imshow(freq_results['interactions'], cmap='viridis')
        plt.colorbar(label='Coupling Strength')
        plt.title('Coil Interactions')
        plt.xlabel('Coil Number')
        plt.ylabel('Coil Number')
        
        # Plot 2: Energy Scaling
        plt.subplot(2, 2, 2)
        coils = range(2, len(scale_results['theoretical_limits'])+2)
        plt.semilogy(coils, scale_results['theoretical_limits'], 'bo-')
        plt.title('Energy Scaling Pattern')
        plt.xlabel('Number of Coils')
        plt.ylabel('Theoretical Energy Limit')
        plt.grid(True)
        
        # Plot 3: Energy Flow
        plt.subplot(2, 2, 3)
        t = energy_results['time']
        for i in range(energy_results['energy_flow'].shape[1]):
            plt.plot(t, energy_results['energy_flow'][:,i], 
                    label=f'Coil {i+1}')
        plt.title('Energy Flow by Coil')
        plt.xlabel('Time (s)')
        plt.ylabel('Energy')
        plt.legend()
        
        # Plot 4: Total System Energy
        plt.subplot(2, 2, 4)
        plt.plot(t, energy_results['total_energy'])
        plt.title('Total System Energy')
        plt.xlabel('Time (s)')
        plt.ylabel('Energy')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Run deep analysis
    analysis = QHRCDeepAnalysis()
    analysis.run_deep_analysis()
