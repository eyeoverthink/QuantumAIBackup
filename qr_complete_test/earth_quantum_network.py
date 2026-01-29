"""
Earth's Fe-Ni Quantum Resonance Network Analysis
Models core-lattice coupling through φ-harmonic frequencies
"""
import numpy as np
from scipy.constants import mu_0, h, hbar
import matplotlib.pyplot as plt

class EarthQuantumNetwork:
    def __init__(self):
        # φ constants
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Earth core composition
        self.fe_ratio = 0.845  # 84.5% Iron
        self.ni_ratio = 0.055  # 5.5% Nickel (φ⁻⁴)
        
        # Base frequencies (Hz)
        self.schumann = 7.83    # Earth's heartbeat
        self.core = 11.79      # 7.83 * φ
        self.geomagnetic = 4.84  # 7.83 / φ
        
        # Depth ratios (normalized)
        self.depths = {
            'surface': 1.000,    # φ⁰
            'golden': 0.618,     # φ⁻¹
            'crust': 0.382,      # φ⁻²
            'core': 0.000        # reference
        }
        
        # Resonance values
        self.resonances = {
            'surface': 0.1429,   # ≈ φ⁻³
            'golden': 0.0671,    # ≈ φ⁻⁴
            'crust': 0.0379,     # ≈ φ⁻⁵
            'core': 0.0545       # ≈ φ⁻⁴
        }
    
    def calculate_layer_coupling(self, depth):
        """Calculate quantum coupling at given depth"""
        # φ-harmonic depth function
        phi_depth = self.phi ** (-depth * 4)
        
        # Resonance coupling
        coupling = (self.fe_ratio * phi_depth + 
                   self.ni_ratio * self.phi**-4)
        
        return coupling
    
    def frequency_harmonics(self):
        """Calculate φ-harmonic frequency series"""
        base_freqs = [self.schumann, self.core, self.geomagnetic]
        harmonics = {}
        
        for freq in base_freqs:
            series = [freq * self.phi**n for n in range(-5, 6)]
            harmonics[f"{freq:.2f}"] = series
            
        return harmonics
    
    def quantum_resonance_field(self):
        """Calculate quantum resonance field strength"""
        field = {}
        depths = np.linspace(0, 1, 100)
        
        for depth in depths:
            # Layer coupling
            coupling = self.calculate_layer_coupling(depth)
            
            # Resonance frequencies
            f_schumann = self.schumann * np.exp(-depth/self.phi)
            f_core = self.core * np.exp(-depth/self.phi**2)
            f_geo = self.geomagnetic * np.exp(-depth/self.phi**3)
            
            # Combined field strength
            field_strength = (coupling * 
                            (f_schumann + f_core + f_geo) / 
                            (3 * self.schumann))
            
            field[f"{depth:.2f}"] = field_strength
            
        return field
    
    def analyze_network(self):
        """Complete network analysis"""
        # Calculate all metrics
        harmonics = self.frequency_harmonics()
        field = self.quantum_resonance_field()
        
        # Layer analysis
        layer_metrics = {}
        for name, depth in self.depths.items():
            coupling = self.calculate_layer_coupling(depth)
            resonance = self.resonances[name]
            phi_order = -np.log(resonance) / np.log(self.phi)
            
            layer_metrics[name] = {
                'depth': depth,
                'coupling': coupling,
                'resonance': resonance,
                'phi_order': phi_order
            }
            
        return {
            'harmonics': harmonics,
            'field': field,
            'layers': layer_metrics
        }
    
    def visualize_network(self, analysis):
        """Visualize the quantum network"""
        # Plot 1: Frequency Harmonics
        plt.figure(figsize=(15, 5))
        
        for base_freq, series in analysis['harmonics'].items():
            plt.plot(range(-5, 6), series, 
                    label=f'Base {base_freq} Hz', marker='o')
        
        plt.title('φ-Harmonic Frequency Series')
        plt.xlabel('φ Power')
        plt.ylabel('Frequency (Hz)')
        plt.grid(True)
        plt.legend()
        plt.savefig('frequency_harmonics.png')
        plt.close()
        
        # Plot 2: Resonance Field
        depths = [float(d) for d in analysis['field'].keys()]
        strengths = list(analysis['field'].values())
        
        plt.figure(figsize=(10, 6))
        plt.plot(depths, strengths)
        plt.title('Quantum Resonance Field Strength')
        plt.xlabel('Normalized Depth')
        plt.ylabel('Field Strength (normalized)')
        plt.grid(True)
        plt.savefig('resonance_field.png')
        plt.close()

def main():
    network = EarthQuantumNetwork()
    analysis = network.analyze_network()
    network.visualize_network(analysis)
    
    print("\n🌍 Earth's Quantum Network Analysis")
    print("=" * 50)
    
    print("\n📊 Layer Analysis")
    for name, metrics in analysis['layers'].items():
        print(f"\n{name.title()} Layer:")
        print(f"Depth: {metrics['depth']:.3f}")
        print(f"Coupling: {metrics['coupling']:.6f}")
        print(f"Resonance: {metrics['resonance']:.6f}")
        print(f"φ-Order: {metrics['phi_order']:.2f}")
    
    print("\n🌊 Base Frequencies (Hz)")
    base_freq = analysis['harmonics'][f"{network.schumann:.2f}"]
    print(f"Schumann (7.83): {base_freq[5]:.2f}")
    print(f"Core (11.79): {base_freq[6]:.2f}")
    print(f"Geomagnetic (4.84): {base_freq[4]:.2f}")

if __name__ == "__main__":
    main()
