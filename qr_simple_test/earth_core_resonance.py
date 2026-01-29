"""
Earth Core Quantum Resonance Analysis
Studies Fe-Ni core interactions with quantum fields
"""
import numpy as np
from scipy.constants import mu_0, epsilon_0, c, e, m_e, h, k, hbar

class EarthCoreResonance:
    def __init__(self):
        # Earth core parameters
        self.core_radius = 1.22e6  # Inner core radius (m)
        self.temp_core = 5400  # Core temperature (K)
        self.pressure = 3.3e11  # Core pressure (Pa)
        
        # Composition ratios
        self.fe_ratio = 0.85  # Iron ratio
        self.ni_ratio = 0.05  # Nickel ratio
        
        # Magnetic properties
        self.B_field = 25e-6  # Earth's magnetic field (T)
        self.schumann = 7.83  # Schumann resonance (Hz)
        
        # Quantum parameters
        self.phi = (1 + np.sqrt(5)) / 2
        self.larmor_fe = 2.0678e7  # Iron Larmor frequency
        self.larmor_ni = 2.2e7     # Nickel Larmor frequency
        
    def core_frequencies(self):
        """Calculate core resonant frequencies"""
        # Natural frequencies
        f_plasma = np.sqrt(self.fe_ratio * e**2 / (m_e * epsilon_0))
        f_cyclotron = e * self.B_field / (2 * np.pi * m_e)
        f_larmor = (self.fe_ratio * self.larmor_fe + 
                   self.ni_ratio * self.larmor_ni)
        
        return {
            'plasma': f_plasma,
            'cyclotron': f_cyclotron,
            'larmor': f_larmor,
            'schumann': self.schumann
        }
    
    def quantum_resonance(self):
        """Calculate quantum resonance conditions"""
        # De Broglie wavelength at core temperature
        lambda_db = h * np.sqrt(2 / (m_e * k * self.temp_core))
        
        # Core quantum numbers
        n_quantum = self.core_radius / lambda_db
        n_phi = int(n_quantum / self.phi)
        
        # Resonance energies
        E_n = h**2 * n_phi**2 / (8 * m_e * self.core_radius**2)
        
        return {
            'wavelength': lambda_db,
            'quantum_number': n_phi,
            'energy': E_n
        }
    
    def magnetic_coupling(self):
        """Calculate Fe-Ni magnetic coupling"""
        # Exchange energy
        J_fe_ni = 2e-21  # Fe-Ni exchange constant (J)
        
        # Spin alignment
        S_fe = 2  # Iron spin
        S_ni = 1  # Nickel spin
        
        # Coupling energy
        E_coupling = -J_fe_ni * S_fe * S_ni
        
        # Resonance frequency
        f_res = abs(E_coupling) / h
        
        return {
            'coupling_energy': E_coupling,
            'resonance_freq': f_res
        }
    
    def analyze_core(self):
        """Complete core analysis"""
        freqs = self.core_frequencies()
        quantum = self.quantum_resonance()
        coupling = self.magnetic_coupling()
        
        # Check for resonance matching
        schumann_ratio = freqs['schumann'] / self.phi
        larmor_ratio = freqs['larmor'] / (2 * np.pi * self.schumann)
        
        return {
            'frequencies': freqs,
            'quantum_state': quantum,
            'coupling': coupling,
            'schumann_phi_ratio': schumann_ratio,
            'larmor_schumann_ratio': larmor_ratio
        }

def main():
    core = EarthCoreResonance()
    results = core.analyze_core()
    
    print("\n🌍 Earth Core Quantum Analysis")
    print("=" * 50)
    
    print("\n📊 Core Frequencies")
    for name, freq in results['frequencies'].items():
        print(f"{name.title()}: {freq:.2e} Hz")
    
    print("\n🌊 Quantum State")
    state = results['quantum_state']
    print(f"De Broglie λ: {state['wavelength']:.2e} m")
    print(f"Quantum n: {state['quantum_number']:.2e}")
    print(f"Energy: {state['energy']:.2e} J")
    
    print("\n🧲 Fe-Ni Coupling")
    coupling = results['coupling']
    print(f"Energy: {coupling['coupling_energy']:.2e} J")
    print(f"Frequency: {coupling['resonance_freq']:.2e} Hz")
    
    print("\n🎯 Resonance Ratios")
    print(f"Schumann/φ: {results['schumann_phi_ratio']:.6f}")
    print(f"Larmor/Schumann: {results['larmor_schumann_ratio']:.6f}")

if __name__ == "__main__":
    main()
