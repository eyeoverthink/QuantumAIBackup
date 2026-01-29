"""
Moon φ-Harmonic Resonance Chamber Analysis
Studies Moon as a natural quantum resonator
"""
import numpy as np
from scipy.constants import G, c, h
import matplotlib.pyplot as plt

class MoonResonanceChamber:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Moon parameters
        self.radius = 1737.1e3  # meters
        self.mass = 7.34767309e22  # kg
        self.shell_thickness = self.radius / self.phi  # φ-ratio shell
        
        # Resonance frequencies
        self.frequencies = {
            'base': 4.84,          # Moon base (7.83/φ)
            'shell': 7.83/self.phi**2,  # Shell resonance
            'cavity': 4.37,        # Inner cavity (φ²)
            'orbital': 1.17        # Orbital frequency
        }
        
    def chamber_modes(self):
        """Calculate resonance chamber modes"""
        modes = {}
        
        # Shell modes (standing waves)
        r = self.radius - self.shell_thickness  # Inner radius
        
        for n in range(1, 8):
            # Radial modes
            f_r = c / (2 * np.pi * r) * n
            
            # Angular modes
            f_a = c / (2 * np.pi * r) * n * self.phi
            
            # Combined mode
            f_mode = (f_r + f_a) / 2
            
            # Mode energy
            E_mode = h * f_mode
            
            modes[f'mode_{n}'] = {
                'frequency': f_mode,
                'energy': E_mode,
                'radius': r,
                'order': n
            }
            
        return modes
    
    def cavity_resonance(self):
        """Calculate cavity quantum resonance"""
        # Cavity volume
        V = 4/3 * np.pi * (self.radius - self.shell_thickness)**3
        
        # Cavity frequencies
        frequencies = []
        energies = []
        
        for n in range(1, 6):
            # φ-harmonic frequencies
            f_n = self.frequencies['cavity'] * self.phi**n
            
            # Mode energy
            E_n = h * f_n
            
            # Quantum amplitude
            A_n = np.sqrt(2 * E_n / (self.mass * (2*np.pi*f_n)**2))
            
            frequencies.append(f_n)
            energies.append(E_n)
            
        return {
            'volume': V,
            'frequencies': frequencies,
            'energies': energies
        }
    
    def shell_harmonics(self):
        """Calculate shell φ-harmonic structure"""
        harmonics = {}
        
        # Shell layers
        layers = np.linspace(0, self.shell_thickness, 7)
        
        for i, r in enumerate(layers):
            # Layer radius
            radius = self.radius - r
            
            # Layer frequency
            f = self.frequencies['shell'] * self.phi**(-i)
            
            # Layer energy
            E = h * f
            
            # Resonance quality
            Q = np.exp(-i/self.phi)
            
            harmonics[f'layer_{i}'] = {
                'radius': radius,
                'frequency': f,
                'energy': E,
                'quality': Q
            }
            
        return harmonics
    
    def analyze_chamber(self):
        """Complete resonance chamber analysis"""
        modes = self.chamber_modes()
        cavity = self.cavity_resonance()
        harmonics = self.shell_harmonics()
        
        # Calculate resonance metrics
        metrics = {}
        
        # Standing wave patterns
        for name, f in self.frequencies.items():
            # Wavelength
            lambda_n = c / f
            
            # Mode number
            n = self.radius / lambda_n
            
            # Resonance quality
            Q = 2 * np.pi * f * self.mass / (self.radius * G)
            
            metrics[name] = {
                'wavelength': lambda_n,
                'mode_number': n,
                'quality': Q
            }
            
        return {
            'modes': modes,
            'cavity': cavity,
            'harmonics': harmonics,
            'metrics': metrics
        }
    
    def visualize_chamber(self, analysis):
        """Visualize resonance chamber"""
        # Plot 1: Chamber Modes
        mode_freqs = [m['frequency'] for m in analysis['modes'].values()]
        mode_energies = [m['energy'] for m in analysis['modes'].values()]
        
        plt.figure(figsize=(12, 6))
        plt.plot(range(1, 8), mode_freqs, 'bo-', label='Frequency')
        plt.plot(range(1, 8), mode_energies, 'ro-', label='Energy')
        
        plt.title('Moon Chamber Modes')
        plt.xlabel('Mode Number')
        plt.ylabel('Value')
        plt.yscale('log')
        plt.legend()
        plt.grid(True)
        plt.savefig('moon_modes.png')
        plt.close()
        
        # Plot 2: Shell Structure
        radii = [h['radius'] for h in analysis['harmonics'].values()]
        freqs = [h['frequency'] for h in analysis['harmonics'].values()]
        quality = [h['quality'] for h in analysis['harmonics'].values()]
        
        plt.figure(figsize=(10, 8))
        plt.scatter(radii, freqs, c=quality, s=100, cmap='viridis')
        
        plt.title('Moon Shell Harmonics')
        plt.xlabel('Radius (m)')
        plt.ylabel('Frequency (Hz)')
        plt.colorbar(label='Resonance Quality')
        plt.grid(True)
        plt.savefig('moon_shell.png')
        plt.close()

def main():
    chamber = MoonResonanceChamber()
    analysis = chamber.analyze_chamber()
    chamber.visualize_chamber(analysis)
    
    print("\n🌙 Moon Resonance Chamber Analysis")
    print("=" * 50)
    
    print("\n📊 Chamber Dimensions")
    print(f"Outer Radius: {chamber.radius/1000:.1f} km")
    print(f"Shell Thickness: {chamber.shell_thickness/1000:.1f} km")
    print(f"Cavity Volume: {analysis['cavity']['volume']/1e9:.2e} km³")
    
    print("\n🌊 Base Frequencies")
    for name, freq in chamber.frequencies.items():
        print(f"{name}: {freq:.2f} Hz")
    
    print("\n💫 Chamber Modes")
    for name, mode in analysis['modes'].items():
        print(f"\n{name}:")
        print(f"Frequency: {mode['frequency']:.2e} Hz")
        print(f"Energy: {mode['energy']:.2e} J")
        print(f"Order: {mode['order']}")
    
    print("\n✨ Shell Harmonics")
    for name, layer in analysis['harmonics'].items():
        print(f"\n{name}:")
        print(f"Radius: {layer['radius']/1000:.1f} km")
        print(f"Frequency: {layer['frequency']:.2f} Hz")
        print(f"Quality: {layer['quality']:.6f}")

if __name__ == "__main__":
    main()
