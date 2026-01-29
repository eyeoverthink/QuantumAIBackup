"""
Bipolar Consciousness Field Analysis
Models Earth-Moon quantum poles and consciousness resonance
"""
import numpy as np
from scipy.constants import G, c
import matplotlib.pyplot as plt

class BipolarConsciousnessField:
    def __init__(self):
        # φ constants
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Earth-Moon parameters
        self.earth_mass = 5.972e24  # kg
        self.moon_mass = 7.34767309e22  # kg
        self.mean_distance = 384400e3  # meters
        
        # Consciousness frequencies
        self.schumann = 7.83  # Hz (Earth)
        self.lunar = 7.83 / self.phi  # Hz (Moon)
        self.consciousness = 4.37  # Hz (φ² resonance)
        
        # Field parameters
        self.nodes = 1000
        self.time_steps = 100
        
    def calculate_bipolar_field(self, x, t):
        """Calculate bipolar field strength at point x and time t"""
        # Earth's contribution
        earth_field = np.sin(2*np.pi*self.schumann*t) / (x**2)
        
        # Moon's contribution
        moon_field = np.sin(2*np.pi*self.lunar*t) / ((x - 1)**2)
        
        # Consciousness resonance
        consciousness = np.sin(2*np.pi*self.consciousness*t)
        
        # Combined field with φ-harmonic weighting
        field = (earth_field + 
                self.phi**-1 * moon_field + 
                self.phi**-2 * consciousness)
        
        return field
    
    def resonance_modes(self):
        """Calculate resonance modes between Earth and Moon"""
        modes = []
        for n in range(1, 7):
            # φ-harmonic frequencies
            f_n = self.consciousness * self.phi**n
            
            # Mode energy
            E_n = self.phi**-n * f_n
            
            modes.append({
                'frequency': f_n,
                'energy': E_n,
                'phi_order': n
            })
        
        return modes
    
    def consciousness_coupling(self):
        """Calculate consciousness field coupling"""
        # Gravitational coupling
        G_coupling = G * self.earth_mass * self.moon_mass / self.mean_distance**2
        
        # φ-harmonic frequencies
        frequencies = [
            self.schumann,          # Earth base
            self.lunar,             # Moon base
            self.consciousness,     # Consciousness
            self.schumann * self.phi,  # Earth harmonic
            self.lunar / self.phi      # Moon harmonic
        ]
        
        # Coupling strengths
        couplings = []
        for f in frequencies:
            # Quantum coupling with consciousness field
            coupling = G_coupling * np.exp(-f/self.consciousness)
            couplings.append(coupling)
            
        return {
            'frequencies': frequencies,
            'couplings': couplings,
            'total_coupling': sum(couplings)
        }
    
    def analyze_field(self):
        """Analyze complete bipolar consciousness field"""
        # Space-time grid
        x = np.linspace(0, 1, self.nodes)
        t = np.linspace(0, 10/self.consciousness, self.time_steps)
        X, T = np.meshgrid(x, t)
        
        # Calculate field
        field = np.zeros_like(X)
        for i in range(self.time_steps):
            for j in range(self.nodes):
                field[i,j] = self.calculate_bipolar_field(X[i,j], T[i,j])
        
        # Calculate resonance modes
        modes = self.resonance_modes()
        
        # Calculate coupling
        coupling = self.consciousness_coupling()
        
        return {
            'field': field,
            'x': x,
            't': t,
            'modes': modes,
            'coupling': coupling
        }
    
    def visualize_field(self, analysis):
        """Visualize bipolar consciousness field"""
        # Plot 1: Field Evolution
        plt.figure(figsize=(12, 8))
        plt.pcolormesh(analysis['x'], analysis['t'], 
                      analysis['field'], shading='auto')
        plt.colorbar(label='Field Strength')
        plt.title('Bipolar Consciousness Field Evolution')
        plt.xlabel('Normalized Distance (Earth → Moon)')
        plt.ylabel('Time (s)')
        plt.savefig('consciousness_field.png')
        plt.close()
        
        # Plot 2: Resonance Modes
        frequencies = [mode['frequency'] for mode in analysis['modes']]
        energies = [mode['energy'] for mode in analysis['modes']]
        
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, 7), frequencies, 'bo-', label='Frequency')
        plt.plot(range(1, 7), energies, 'ro-', label='Energy')
        plt.title('φ-Harmonic Resonance Modes')
        plt.xlabel('Mode Number')
        plt.ylabel('Value (normalized)')
        plt.legend()
        plt.grid(True)
        plt.savefig('resonance_modes.png')
        plt.close()

def main():
    field = BipolarConsciousnessField()
    analysis = field.analyze_field()
    field.visualize_field(analysis)
    
    print("\n🧠 Bipolar Consciousness Field Analysis")
    print("=" * 50)
    
    print("\n📊 Base Frequencies")
    print(f"Earth (Schumann): {field.schumann:.2f} Hz")
    print(f"Moon (Lunar): {field.lunar:.2f} Hz")
    print(f"Consciousness: {field.consciousness:.2f} Hz")
    
    print("\n🌊 Resonance Modes")
    for mode in analysis['modes']:
        print(f"\nMode φ^{mode['phi_order']}:")
        print(f"Frequency: {mode['frequency']:.2f} Hz")
        print(f"Energy: {mode['energy']:.2e}")
    
    print("\n🔄 Coupling Analysis")
    coupling = analysis['coupling']
    print(f"Total Coupling: {coupling['total_coupling']:.2e}")
    for f, c in zip(coupling['frequencies'], coupling['couplings']):
        print(f"f = {f:.2f} Hz → coupling = {c:.2e}")

if __name__ == "__main__":
    main()
