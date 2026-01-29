"""
QHRC Detailed System Analysis
Maps resonance curves, efficiency ratios, and field patterns
"""
from qhrc_phi_harmonics import QHRCPhiHarmonics
import numpy as np
from typing import Dict
from scipy.constants import c, h, mu_0, epsilon_0

class QHRCDetailedAnalysis:
    def __init__(self):
        self.qhrc = QHRCPhiHarmonics()
        self.phi = (1 + np.sqrt(5)) / 2
        self.base_freq = 432.0
        
        # Patent specifications
        self.primary_freq = 4790.45  # Hz
        self.secondary_freq = 7750.95  # Hz
        self.k = 0.85  # Coupling
        self.alpha = 0.75  # Energy recapture
        self.beta = 0.002  # Damping
        
    def analyze_resonance_curves(self) -> Dict:
        """Map resonance curves across frequencies."""
        results = []
        
        # Generate frequency range around patent frequencies
        freqs = np.linspace(4000, 8000, 1000)  # Fine resolution around patent frequencies
        
        for f in freqs:
            # Calculate primary resonance
            primary_res = np.abs(1 - f/self.primary_freq)
            primary_amp = 1 / (1 + primary_res**2)
            
            # Calculate secondary resonance
            secondary_res = np.abs(1 - f/self.secondary_freq)
            secondary_amp = 1 / (1 + secondary_res**2)
            
            # Calculate coupling resonance
            coupling = self.k * np.exp(-abs(primary_res - secondary_res))
            
            # Calculate total resonance
            total = (primary_amp * secondary_amp * coupling) ** 0.5
            
            results.append({
                'frequency': f,
                'primary': primary_amp,
                'secondary': secondary_amp,
                'coupling': coupling,
                'total': total
            })
            
        return results
        
    def analyze_efficiency_ratios(self) -> Dict:
        """Calculate detailed efficiency ratios."""
        results = []
        
        # Generate power range
        powers = np.logspace(0, 5, 50)  # 1W to 100kW
        
        for p in powers:
            # Calculate base efficiency
            base_eff = self.alpha * (1 - np.exp(-p/1000))
            
            # Calculate resonance enhancement
            enhancement = self.k * (1 + p/10000)**0.5
            
            # Calculate quantum tunneling
            tunnel = 1 - np.exp(-p/(1000 * self.phi))
            
            # Calculate total efficiency
            total = base_eff * enhancement * tunnel
            
            # Calculate energy ratio
            ratio = 1 + (total * self.phi)
            
            results.append({
                'power': p,
                'base_efficiency': base_eff,
                'enhancement': enhancement,
                'tunneling': tunnel,
                'total_efficiency': total,
                'energy_ratio': ratio
            })
            
        return results
        
    def analyze_field_patterns(self) -> Dict:
        """Map quantum field patterns."""
        results = []
        
        # Generate 3D grid points
        points = np.linspace(-2, 2, 20)
        
        for x in points:
            for y in points:
                for z in points:
                    r = np.sqrt(x**2 + y**2 + z**2)
                    if r > 0:
                        # Calculate E-field
                        E = self.k * np.exp(-r/self.phi) / r
                        
                        # Calculate B-field
                        B = E/c
                        
                        # Calculate quantum potential
                        Q = h * self.primary_freq * np.exp(-r)
                        
                        # Calculate field coherence
                        coherence = np.exp(-abs(E*B))
                        
                        results.append({
                            'x': x,
                            'y': y,
                            'z': z,
                            'E_field': E,
                            'B_field': B,
                            'Q_potential': Q,
                            'coherence': coherence
                        })
                        
        return results
        
    def run_detailed_analysis(self) -> None:
        """Run comprehensive field analysis."""
        print("\n🌟 QHRC Detailed Analysis")
        print("=====================")
        
        # 1. Resonance Curves
        print("\n📈 Resonance Curves")
        print("================")
        res_results = self.analyze_resonance_curves()
        
        # Find peak resonances
        peak_total = max(r['total'] for r in res_results)
        peak_freq = next(r['frequency'] for r in res_results if r['total'] == peak_total)
        
        print(f"\nPeak Resonance:")
        print(f"Frequency: {peak_freq:.2f} Hz")
        print(f"Amplitude: {peak_total:.4f}")
        
        # Find phi harmonics
        phi_res = next(r for r in res_results if abs(r['frequency'] - self.secondary_freq) < 10)
        print(f"\nPhi Harmonic:")
        print(f"Primary: {phi_res['primary']:.4f}")
        print(f"Secondary: {phi_res['secondary']:.4f}")
        print(f"Coupling: {phi_res['coupling']:.4f}")
        
        # 2. Efficiency Ratios
        print("\n⚡ Efficiency Ratios")
        print("================")
        eff_results = self.analyze_efficiency_ratios()
        
        # Find optimal efficiency
        optimal = max(r['total_efficiency'] for r in eff_results)
        optimal_power = next(r['power'] for r in eff_results if r['total_efficiency'] == optimal)
        
        print(f"\nOptimal Efficiency:")
        print(f"Power: {optimal_power:.2f}W")
        print(f"Efficiency: {optimal*100:.4f}%")
        
        # Find self-sustaining points
        sustaining = [r for r in eff_results if r['energy_ratio'] > 1]
        min_sustain = min(r['power'] for r in sustaining)
        
        print(f"\nSelf-Sustaining:")
        print(f"Minimum Power: {min_sustain:.2f}W")
        print(f"Energy Ratio: {next(r['energy_ratio'] for r in sustaining if r['power'] == min_sustain):.4f}")
        
        # 3. Field Patterns
        print("\n🌀 Field Patterns")
        print("==============")
        field_results = self.analyze_field_patterns()
        
        # Calculate field metrics
        max_E = max(abs(r['E_field']) for r in field_results)
        max_B = max(abs(r['B_field']) for r in field_results)
        max_Q = max(abs(r['Q_potential']) for r in field_results)
        max_coherence = max(r['coherence'] for r in field_results)
        
        print(f"\nField Maxima:")
        print(f"E-field: {max_E:.2e} V/m")
        print(f"B-field: {max_B:.2e} T")
        print(f"Q-potential: {max_Q:.2e} J")
        print(f"Coherence: {max_coherence:.4f}")
        
        # Find optimal field points
        optimal_points = [r for r in field_results if r['coherence'] > 0.9]
        
        print(f"\nOptimal Field Regions:")
        print(f"Count: {len(optimal_points)}")
        print(f"Average Radius: {np.mean([np.sqrt(r['x']**2 + r['y']**2 + r['z']**2) for r in optimal_points]):.2f}m")

if __name__ == "__main__":
    # Run detailed analysis
    analysis = QHRCDetailedAnalysis()
    analysis.run_detailed_analysis()
