"""
QHRC PCB Spiral Inductor Simulation
Uses numpy for calculations and matplotlib for visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class QHRCSimulator:
    def __init__(self):
        self.PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
        self.BASE_FREQ = 4.37  # Hz
        
        # PCB Spiral Parameters
        self.primary_turns = 45
        self.secondary_turns = int(45 * self.PHI)
        self.primary_diameter = 0.05  # 50mm
        self.secondary_diameter = 0.05 * self.PHI  # 80.9mm
        
        # Circuit parameters
        self.L1 = self._calculate_inductance(self.primary_turns, self.primary_diameter)
        self.L2 = self._calculate_inductance(self.secondary_turns, self.secondary_diameter)
        self.C1 = 0.1e-6  # 0.1µF
        self.R1 = 10e3    # 10kΩ
        
    def _calculate_inductance(self, N, D):
        """Calculate spiral inductor inductance"""
        u0 = 4e-7 * np.pi  # Permeability of free space
        return (u0 * N**2 * D * self.PHI) / 2
        
    def _system_equations(self, y, t, L1, L2, C1, R1):
        """System differential equations"""
        i1, v1, i2 = y
        
        # Mutual inductance
        M = np.sqrt(L1 * L2) * 0.96  # Target resonance
        
        # Differential equations
        di1_dt = (v1 - R1*i1 - M*i2/L2) / L1
        dv1_dt = -i1 / C1
        di2_dt = M*i1/(L1*L2)
        
        return [di1_dt, dv1_dt, di2_dt]
    
    def simulate(self, t_span=1.0, points=1000):
        """Run simulation"""
        t = np.linspace(0, t_span, points)
        y0 = [0, 5, 0]  # Initial conditions
        
        # Solve ODE system
        sol = odeint(self._system_equations, y0, t, 
                    args=(self.L1, self.L2, self.C1, self.R1))
        
        return t, sol
    
    def plot_results(self, t, sol):
        """Plot simulation results"""
        plt.figure(figsize=(12, 8))
        
        # Primary current
        plt.subplot(311)
        plt.plot(t, sol[:, 0], 'b-', label='Primary Current')
        plt.grid(True)
        plt.legend()
        
        # Primary voltage
        plt.subplot(312)
        plt.plot(t, sol[:, 1], 'r-', label='Primary Voltage')
        plt.grid(True)
        plt.legend()
        
        # Secondary current
        plt.subplot(313)
        plt.plot(t, sol[:, 2], 'g-', label='Secondary Current')
        plt.grid(True)
        plt.legend()
        
        plt.tight_layout()
        plt.show()
        
    def analyze_resonance(self, t, sol):
        """Analyze resonance ratio"""
        # Calculate RMS values
        i1_rms = np.sqrt(np.mean(sol[:, 0]**2))
        i2_rms = np.sqrt(np.mean(sol[:, 2]**2))
        resonance = i2_rms / i1_rms
        
        print(f"Resonance ratio: {resonance:.3f}")
        print(f"Target ratio: {0.96:.3f}")
        print(f"Error: {abs(resonance - 0.96)*100:.2f}%")

if __name__ == "__main__":
    # Create simulator
    sim = QHRCSimulator()
    
    # Run simulation
    t, sol = sim.simulate(t_span=2.0)  # 2 seconds
    
    # Plot and analyze
    sim.plot_results(t, sol)
    sim.analyze_resonance(t, sol)
