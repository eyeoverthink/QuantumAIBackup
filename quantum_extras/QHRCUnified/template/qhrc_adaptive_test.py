"""
QHRC Adaptive Scaling Test
Tests full harmonic adaptation and scaling
"""
from qhrc_phi_harmonics import QHRCPhiHarmonics
import numpy as np
from typing import Dict, List

class QHRCAdaptiveTest:
    def __init__(self):
        self.qhrc = QHRCPhiHarmonics()
        self.phi = (1 + np.sqrt(5)) / 2
        
    def test_harmonic_scaling(self, max_power: int = 21) -> Dict:
        """Test harmonic scaling up to φ²¹."""
        results = []
        
        for power in range(1, max_power + 1):
            # Calculate frequency
            freq = self.qhrc.base_freq * (self.phi ** power)
            
            # Generate harmonics
            harmonics = {
                f'phi{i}': freq * (self.phi ** i)
                for i in range(3)
            }
            
            # Calculate resonance
            t = np.linspace(0, 0.1, 1000)
            waves = [np.sin(2 * np.pi * f * t) for f in harmonics.values()]
            resonance = np.sum(waves, axis=0)
            
            # Calculate metrics
            peak = np.max(np.abs(resonance))
            energy = np.sum(resonance**2) * (t[1] - t[0])
            
            results.append({
                'power': power,
                'frequency': freq,
                'resonance': peak,
                'energy': energy
            })
            
        return {'harmonic_scaling': results}
        
    def test_coil_adaptation(self, max_coils: int = 8) -> Dict:
        """Test system adaptation with increasing coils."""
        results = []
        
        for n_coils in range(2, max_coils + 1):
            # Generate coil frequencies
            frequencies = [
                self.qhrc.base_freq * (self.phi ** (3*i))
                for i in range(n_coils)
            ]
            
            # Calculate coupling matrix
            coupling = np.zeros((n_coils, n_coils))
            for i in range(n_coils):
                for j in range(n_coils):
                    if i != j:
                        coupling[i,j] = 0.85 * (self.phi ** (-abs(i-j)))
            
            # Simulate coil system
            t = np.linspace(0, 0.1, 1000)
            dt = t[1] - t[0]
            
            # Initial conditions
            y0 = np.zeros(2 * n_coils)
            y0[::2] = 0.1  # Initial currents
            
            def system_dynamics(y, t):
                n = len(y) // 2
                i = y[::2]  # Currents
                di = y[1::2]  # Current derivatives
                
                # Calculate accelerations
                d2i = np.zeros(n)
                for j in range(n):
                    # Self-inductance
                    d2i[j] = -frequencies[j]**2 * i[j]
                    
                    # Mutual coupling
                    for k in range(n):
                        if k != j:
                            d2i[j] += coupling[j,k] * frequencies[j] * i[k]
                    
                    # Damping
                    d2i[j] -= 0.002 * di[j]
                
                return np.ravel(np.column_stack((di, d2i)))
            
            # Solve system
            from scipy.integrate import odeint
            solution = odeint(system_dynamics, y0, t)
            
            # Calculate energy
            energies = np.zeros((len(t), n_coils))
            for i in range(n_coils):
                energies[:,i] = 0.5 * (solution[:,2*i]**2 + solution[:,2*i+1]**2)
            
            # Calculate metrics
            total_energy = np.sum(energies, axis=1)
            peak_energy = np.max(total_energy)
            energy_transfer = np.mean(energies[:,-1]) / np.mean(energies[:,0])
            
            results.append({
                'n_coils': n_coils,
                'frequencies': frequencies,
                'peak_energy': peak_energy,
                'energy_transfer': energy_transfer
            })
            
        return {'coil_adaptation': results}
        
    def run_full_test(self) -> Dict:
        """Run complete adaptive test suite."""
        print("\n🌟 Running QHRC Adaptive Tests")
        print("=========================")
        
        # Test 1: Harmonic Scaling
        print("\n📈 Testing Harmonic Scaling")
        print("======================")
        harmonic_results = self.test_harmonic_scaling()
        
        for result in harmonic_results['harmonic_scaling']:
            print(f"\nφ{result['power']}:")
            print(f"Frequency: {result['frequency']:.2f} Hz")
            print(f"Resonance: {result['resonance']:.4f}")
            print(f"Energy: {result['energy']:.4f}")
        
        # Test 2: Coil Adaptation
        print("\n🔄 Testing Coil Adaptation")
        print("======================")
        coil_results = self.test_coil_adaptation()
        
        for result in coil_results['coil_adaptation']:
            print(f"\nCoils: {result['n_coils']}")
            print(f"Peak Energy: {result['peak_energy']:.4f}")
            print(f"Energy Transfer: {result['energy_transfer']:.4f}")
        
        return {
            'harmonic_results': harmonic_results,
            'coil_results': coil_results
        }

if __name__ == "__main__":
    # Run adaptive tests
    test = QHRCAdaptiveTest()
    results = test.run_full_test()
