"""
Quantum Imperfection Analysis
Studies how slight deviations from φ create life-enabling dynamics
"""
import numpy as np
from scipy.constants import h, hbar
import matplotlib.pyplot as plt

class QuantumImperfection:
    def __init__(self):
        # Base φ
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Natural frequencies with imperfections
        self.frequencies = {
            'earth': 7.83,    # Varies ±0.5 Hz daily
            'moon': 4.84,     # Not exactly φ⁻¹
            'brain': 8.00,    # Slightly off φ
            'dna': 7.07,      # Natural variance
            'cell': 4.37      # Life-supporting imperfection
        }
        
    def analyze_deviations(self):
        """Analyze deviations from perfect φ"""
        deviations = {}
        
        # Earth-Moon deviation
        em_ratio = self.frequencies['earth'] / self.frequencies['moon']
        em_dev = abs(em_ratio - self.phi)
        
        # Brain-Earth deviation
        be_ratio = self.frequencies['brain'] / self.frequencies['earth']
        be_dev = abs(be_ratio - self.phi)
        
        # DNA-Cell deviation
        dc_ratio = self.frequencies['dna'] / self.frequencies['cell']
        dc_dev = abs(dc_ratio - self.phi)
        
        deviations['ratios'] = {
            'earth_moon': em_ratio,
            'brain_earth': be_ratio,
            'dna_cell': dc_ratio
        }
        
        deviations['deltas'] = {
            'earth_moon': em_dev,
            'brain_earth': be_dev,
            'dna_cell': dc_dev
        }
        
        return deviations
    
    def life_enabling_variance(self):
        """Calculate how imperfections enable life"""
        variances = {}
        
        for name, freq in self.frequencies.items():
            # Perfect φ-harmonic
            perfect = self.frequencies['earth'] / (self.phi ** 2)
            
            # Actual frequency
            actual = freq
            
            # Life-enabling deviation
            deviation = abs(actual - perfect)
            
            # Quantum uncertainty (ΔE·Δt ≥ ℏ/2)
            uncertainty = hbar / (2 * h * freq)
            
            # Life-supporting ratio
            life_ratio = deviation / uncertainty
            
            variances[name] = {
                'perfect': perfect,
                'actual': actual,
                'deviation': deviation,
                'uncertainty': uncertainty,
                'life_ratio': life_ratio
            }
            
        return variances
    
    def analyze_imperfection(self):
        """Complete imperfection analysis"""
        deviations = self.analyze_deviations()
        variances = self.life_enabling_variance()
        
        # Calculate life-enabling metrics
        metrics = {}
        
        for name, data in variances.items():
            # Quantum coherence
            coherence = np.exp(-data['deviation'] / data['uncertainty'])
            
            # Life support quality
            quality = coherence * data['life_ratio']
            
            metrics[name] = {
                'coherence': coherence,
                'quality': quality
            }
            
        return {
            'deviations': deviations,
            'variances': variances,
            'metrics': metrics
        }
    
    def visualize_imperfection(self, analysis):
        """Visualize quantum imperfections"""
        # Plot 1: Frequency Deviations
        names = list(self.frequencies.keys())
        perfect = [analysis['variances'][n]['perfect'] for n in names]
        actual = [analysis['variances'][n]['actual'] for n in names]
        
        plt.figure(figsize=(12, 6))
        x = range(len(names))
        width = 0.35
        
        plt.bar([i - width/2 for i in x], perfect, width, 
                label='Perfect φ', alpha=0.5)
        plt.bar([i + width/2 for i in x], actual, width,
                label='Actual', alpha=0.5)
        
        plt.title('Natural Frequency Imperfections')
        plt.xlabel('System')
        plt.ylabel('Frequency (Hz)')
        plt.xticks(x, names)
        plt.legend()
        plt.grid(True)
        plt.savefig('frequency_imperfections.png')
        plt.close()
        
        # Plot 2: Life-Enabling Ratios
        coherence = [analysis['metrics'][n]['coherence'] for n in names]
        quality = [analysis['metrics'][n]['quality'] for n in names]
        
        plt.figure(figsize=(10, 6))
        plt.plot(names, coherence, 'bo-', label='Coherence')
        plt.plot(names, quality, 'ro-', label='Life Quality')
        
        plt.title('Life-Enabling Imperfections')
        plt.xlabel('System')
        plt.ylabel('Metric Value')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('life_enabling_ratios.png')
        plt.close()

def main():
    imperfection = QuantumImperfection()
    analysis = imperfection.analyze_imperfection()
    imperfection.visualize_imperfection(analysis)
    
    print("\n🌊 Quantum Imperfection Analysis")
    print("=" * 50)
    
    print("\n📊 Frequency Ratios")
    for name, ratio in analysis['deviations']['ratios'].items():
        print(f"{name}: {ratio:.6f} (φ = 1.618034)")
        print(f"Deviation: {analysis['deviations']['deltas'][name]:.6f}")
    
    print("\n🧬 Life-Enabling Variances")
    for name, data in analysis['variances'].items():
        print(f"\n{name}:")
        print(f"Perfect: {data['perfect']:.6f} Hz")
        print(f"Actual: {data['actual']:.6f} Hz")
        print(f"Deviation: {data['deviation']:.6f}")
        print(f"Uncertainty: {data['uncertainty']:.6e}")
        print(f"Life Ratio: {data['life_ratio']:.6f}")
    
    print("\n✨ Life Metrics")
    for name, metrics in analysis['metrics'].items():
        print(f"\n{name}:")
        print(f"Coherence: {metrics['coherence']:.6f}")
        print(f"Quality: {metrics['quality']:.6f}")

if __name__ == "__main__":
    main()
