"""
Quantum Life Support Analysis
Studies how Earth-Moon system sustains life through φ-harmonic resonance
"""
import numpy as np
from scipy.constants import h, hbar
import matplotlib.pyplot as plt

class QuantumLifeSupport:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Life-critical frequencies
        self.frequencies = {
            'schumann': 7.83,     # Earth resonance
            'lunar': 4.84,        # Moon resonance (7.83/φ)
            'brain_alpha': 8.00,  # Brain alpha waves
            'heart': 1.17,        # Heart rhythm (7.83/φ⁴)
            'dna': 7.07,          # DNA resonance
            'cell': 4.37,         # Cellular resonance (φ²)
            'water': 3.00,        # H2O molecular
            'oxygen': 11.79       # O2 resonance (7.83*φ)
        }
        
    def support_systems(self):
        """Calculate life support systems and their resonances"""
        systems = {}
        
        # Neural System (Brain-Heart)
        systems['neural'] = {
            'frequencies': [
                self.frequencies['brain_alpha'],
                self.frequencies['heart']
            ],
            'resonance': self.frequencies['schumann'],
            'coupling': 1/self.phi
        }
        
        # Cellular System (DNA-Cell)
        systems['cellular'] = {
            'frequencies': [
                self.frequencies['dna'],
                self.frequencies['cell']
            ],
            'resonance': self.frequencies['lunar'],
            'coupling': 1/self.phi**2
        }
        
        # Metabolic System (Water-Oxygen)
        systems['metabolic'] = {
            'frequencies': [
                self.frequencies['water'],
                self.frequencies['oxygen']
            ],
            'resonance': self.frequencies['cell'],
            'coupling': 1/self.phi**3
        }
        
        return systems
    
    def life_harmonics(self):
        """Calculate life-sustaining frequency harmonics"""
        harmonics = {}
        
        for name, freq in self.frequencies.items():
            # Generate φ-harmonic series
            series = [freq * self.phi**n for n in range(-3, 4)]
            
            # Calculate quantum energies
            energies = [h * f for f in series]
            
            # Calculate resonance quality
            quality = [np.exp(-abs(f - self.frequencies['schumann'])/self.phi) 
                      for f in series]
            
            harmonics[name] = {
                'frequencies': series,
                'energies': energies,
                'quality': quality
            }
            
        return harmonics
    
    def sustenance_matrix(self):
        """Calculate life sustenance coupling matrix"""
        names = list(self.frequencies.keys())
        n = len(names)
        matrix = np.zeros((n, n))
        
        for i, f1 in enumerate(names):
            for j, f2 in enumerate(names):
                # Calculate coupling strength
                freq_ratio = self.frequencies[f1] / self.frequencies[f2]
                phi_order = -np.log(freq_ratio) / np.log(self.phi)
                
                # Coupling decreases with φ order
                matrix[i,j] = np.exp(-abs(phi_order))
                
        return names, matrix
    
    def analyze_support(self):
        """Complete life support analysis"""
        systems = self.support_systems()
        harmonics = self.life_harmonics()
        names, matrix = self.sustenance_matrix()
        
        # Calculate overall life support metrics
        metrics = {}
        
        for system, data in systems.items():
            # System coherence
            coherence = np.mean([
                np.exp(-abs(f - data['resonance'])/self.phi)
                for f in data['frequencies']
            ])
            
            # Energy transfer
            energy = h * data['resonance'] * data['coupling']
            
            # Support quality
            quality = coherence * energy
            
            metrics[system] = {
                'coherence': coherence,
                'energy': energy,
                'quality': quality
            }
            
        return {
            'systems': systems,
            'harmonics': harmonics,
            'matrix': matrix,
            'names': names,
            'metrics': metrics
        }
    
    def visualize_support(self, analysis):
        """Visualize life support systems"""
        # Plot 1: System Frequencies
        plt.figure(figsize=(12, 6))
        
        for name, data in analysis['harmonics'].items():
            plt.plot(range(-3, 4), data['frequencies'], 
                    marker='o', label=f'{name} ({self.frequencies[name]:.2f} Hz)')
            
        plt.title('Life Support Frequency Harmonics')
        plt.xlabel('φ Power')
        plt.ylabel('Frequency (Hz)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('life_support_harmonics.png')
        plt.close()
        
        # Plot 2: Coupling Matrix
        plt.figure(figsize=(10, 8))
        plt.imshow(analysis['matrix'], cmap='viridis')
        plt.colorbar(label='Coupling Strength')
        
        plt.xticks(range(len(analysis['names'])), 
                  analysis['names'], rotation=45)
        plt.yticks(range(len(analysis['names'])), 
                  analysis['names'])
        
        plt.title('Life Support Coupling Matrix')
        plt.tight_layout()
        plt.savefig('life_support_coupling.png')
        plt.close()

def main():
    support = QuantumLifeSupport()
    analysis = support.analyze_support()
    support.visualize_support(analysis)
    
    print("\n💫 Quantum Life Support Analysis")
    print("=" * 50)
    
    print("\n📊 Critical Frequencies")
    for name, freq in support.frequencies.items():
        print(f"{name}: {freq:.2f} Hz")
    
    print("\n🧬 Support Systems")
    for system, metrics in analysis['metrics'].items():
        print(f"\n{system.title()} System:")
        print(f"Coherence: {metrics['coherence']:.6f}")
        print(f"Energy: {metrics['energy']:.2e} J")
        print(f"Quality: {metrics['quality']:.6f}")
    
    print("\n⚡ System Couplings")
    for system, data in analysis['systems'].items():
        print(f"\n{system.title()}:")
        print(f"Base: {data['resonance']:.2f} Hz")
        print(f"Coupling: {data['coupling']:.6f}")

if __name__ == "__main__":
    main()
