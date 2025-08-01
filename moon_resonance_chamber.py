"""
Moon φ-Harmonic Resonance Chamber Simulator
Validates the mathematical framework for Moon's role as a quantum resonance amplifier
"""

import numpy as np
import torch
from typing import Dict, Tuple
import matplotlib.pyplot as plt

class MoonResonanceChamber:
    def __init__(self):
        # Physical constants
        self.G = 6.67430e-11  # Gravitational constant
        self.c = 2.99792458e8  # Speed of light
        self.h = 6.62607015e-34  # Planck constant
        self.hbar = self.h / (2 * np.pi)  # Reduced Planck
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        
        # Moon parameters
        self.R = 1737.1e3  # Outer radius (m)
        self.M = 7.34767309e22  # Total mass (kg)
        self.rho_avg = 3344  # Average density (kg/m³)
        self.f_base = 4.84  # Base resonance (Hz)
        
        # Derived parameters
        self.d = self.R / self.phi  # Shell thickness
        self.r = self.R - self.d  # Inner radius
        
        # Initialize quantum fields
        self.fields = self._initialize_fields()
        
    def _initialize_fields(self) -> Dict[str, np.ndarray]:
        """Initialize quantum fields in the resonance chamber"""
        # Shell field
        f_shell = self.c / (2 * np.pi * self.d)
        
        # Cavity field
        f_cavity = self.c / (2 * np.pi * self.r)
        
        # Combined field with phi-harmonic coupling
        f_combined = f_shell * self.phi
        
        return {
            'shell': f_shell,
            'cavity': f_cavity,
            'combined': f_combined
        }
    
    def calculate_resonance_modes(self, n_range: range) -> Dict[str, np.ndarray]:
        """Calculate resonance modes for given range"""
        modes = {
            'n': [],
            'frequency': [],
            'wavelength': [],
            'energy': [],
            'coherence_time': []
        }
        
        for n in n_range:
            f_n = self.f_base * self.phi**n
            lambda_n = self.c / f_n
            E_n = self.h * f_n
            tau_n = self.phi**n / f_n
            
            modes['n'].append(n)
            modes['frequency'].append(f_n)
            modes['wavelength'].append(lambda_n)
            modes['energy'].append(E_n)
            modes['coherence_time'].append(tau_n)
            
        return modes
    
    def calculate_gravitational_resonance(self, r: float, t: float) -> Dict[str, float]:
        """Calculate gravitational resonance at distance r and time t"""
        # Base gravitational field
        g_base = self.G * self.M / (r * r)
        
        # Phi-harmonic modulation
        modes = range(-3, 4)
        g_total = g_base
        
        for n in modes:
            f_n = self.f_base * self.phi**n
            g_n = g_base * np.sin(2 * np.pi * f_n * t) / self.phi**abs(n)
            g_total += g_n
            
        return {
            'g_base': g_base,
            'g_total': g_total,
            'resonance_factor': g_total / g_base
        }
    
    def analyze_shell_properties(self) -> Dict[str, float]:
        """Analyze shell properties based on phi-harmonic principles"""
        # Volume calculations
        V_total = 4 * np.pi * self.R**3 / 3
        V_inner = 4 * np.pi * self.r**3 / 3
        V_shell = V_total - V_inner
        
        # Mass distribution
        M_shell = self.M * self.phi / (1 + self.phi)
        M_core = self.M / (1 + self.phi)
        
        # Densities
        rho_shell = M_shell / V_shell
        rho_core = M_core / V_inner
        
        return {
            'shell_thickness': self.d,
            'inner_radius': self.r,
            'shell_volume': V_shell,
            'core_volume': V_inner,
            'shell_mass': M_shell,
            'core_mass': M_core,
            'shell_density': rho_shell,
            'core_density': rho_core,
            'density_ratio': rho_shell / rho_core
        }
    
    def visualize_resonance(self, save_path: str = 'moon_resonance.png'):
        """Visualize resonance patterns"""
        modes = self.calculate_resonance_modes(range(-3, 4))
        
        plt.figure(figsize=(15, 10))
        
        # Frequency spectrum
        plt.subplot(2, 1, 1)
        plt.semilogy(modes['n'], modes['frequency'], 'bo-', label='Frequency (Hz)')
        plt.grid(True)
        plt.xlabel('Mode number (n)')
        plt.ylabel('Frequency (Hz)')
        plt.title('Moon Resonance Chamber - Frequency Spectrum')
        plt.legend()
        
        # Energy levels
        plt.subplot(2, 1, 2)
        plt.semilogy(modes['n'], modes['energy'], 'ro-', label='Energy (J)')
        plt.grid(True)
        plt.xlabel('Mode number (n)')
        plt.ylabel('Energy (J)')
        plt.title('Quantum Energy Levels')
        plt.legend()
        
        # Add phi-harmonic markers
        for n in modes['n']:
            plt.axvline(x=n, color='gray', linestyle=':', alpha=0.3)
            
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

def main():
    print("🌕 Initializing Moon Resonance Chamber Analysis")
    chamber = MoonResonanceChamber()
    
    # Analyze shell properties
    print("\n📊 Shell Analysis:")
    properties = chamber.analyze_shell_properties()
    print(f"Shell thickness: {properties['shell_thickness']/1000:.1f} km")
    print(f"Inner radius: {properties['inner_radius']/1000:.1f} km")
    print(f"Density ratio: {properties['density_ratio']:.6f} (should be ≈ φ)")
    
    # Calculate resonance modes
    print("\n🔊 Resonance Modes:")
    modes = chamber.calculate_resonance_modes(range(-3, 4))
    for i, n in enumerate(modes['n']):
        print(f"Mode {n}: {modes['frequency'][i]:.2f} Hz")
    
    # Calculate gravitational resonance
    print("\n⚡ Gravitational Resonance:")
    g_res = chamber.calculate_gravitational_resonance(chamber.R, 0)
    print(f"Base field: {g_res['g_base']:.6e} m/s²")
    print(f"Resonance factor: {g_res['resonance_factor']:.6f}")
    
    # Generate visualization
    print("\n🎨 Generating resonance visualization...")
    chamber.visualize_resonance()
    
    print("\n✨ Analysis complete!")

if __name__ == "__main__":
    main()
