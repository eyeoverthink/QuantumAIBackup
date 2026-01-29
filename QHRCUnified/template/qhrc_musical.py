"""
QHRC Musical Harmonics
Implements the core musical resonance features of the QHRC system
"""
import numpy as np
from scipy import signal
from typing import Dict, List

class QHRCMusical:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.base_freq = 432.0  # Universal A note
        
        # Patent-validated configuration 
        # Patent-validated configuration (1.3777 resonance)
        self.config = {
            'primary_coil': {
                'turns': 4500,
                'frequency': 4790.45,  # φ⁵
                'coupling': 0.999,  # Increased coupling
                'energy_recapture': 0.999  # Energy stabilization
            },
            'secondary_coil': {
                'turns': 6200,
                'frequency': 7750.95,  # φ⁸
                'damping': 0.0005  # Reduced damping
            },
            'phi_decay': 1/self.phi  # Golden ratio decay
        }
        
        # Initialize harmonics
        self.harmonics = self._generate_harmonics()
        
    def _generate_harmonics(self) -> Dict[str, float]:
        """Generate phi-based musical harmonics."""
        harmonics = {
            'root': self.base_freq,  # 432 Hz
            'phi1': self.base_freq * self.phi,  # 698.99 Hz
            'phi2': self.base_freq * self.phi**2,  # 1130.99 Hz
            'phi3': self.base_freq * self.phi**3,  # 1829.98 Hz
            'phi5': self.base_freq * self.phi**5,  # 4790.95 Hz (primary)
            'phi8': self.base_freq * self.phi**8,  # 20294.80 Hz (secondary)
            'phi13': self.base_freq * self.phi**13  # 225072.83 Hz
        }
        return harmonics
        
    def analyze_432hz_carrier(self, duration: float = 1.0) -> Dict:
        """Analyze 432 Hz carrier wave with harmonics."""
        # Time points
        t = np.linspace(0, duration, 1000)
        
        # Generate carrier wave
        carrier = np.sin(2 * np.pi * self.base_freq * t)
        
        # Generate phi harmonics
        harmonics = {
            name: np.sin(2 * np.pi * freq * t)
            for name, freq in self.harmonics.items()
        }
        
        # Calculate resonance
        resonance = np.zeros_like(t)
        for wave in harmonics.values():
            resonance += carrier * wave
        
        # Calculate energy
        energy = np.cumsum(resonance**2) * (t[1] - t[0])
        
        return {
            'time': t,
            'carrier': carrier,
            'harmonics': harmonics,
            'resonance': resonance,
            'energy': energy,
            'frequencies': self.harmonics
        }
        
    def analyze_standing_waves(self, duration: float = 1.0) -> Dict:
        """Analyze standing wave patterns."""
        t = np.linspace(0, duration, 1000)
        dt = t[1] - t[0]
        
        # Primary and secondary frequencies
        f1 = self.config['primary_coil']['frequency']
        f2 = self.config['secondary_coil']['frequency']
        
        # Generate waves
        wave1 = np.sin(2 * np.pi * f1 * t)
        wave2 = np.sin(2 * np.pi * f2 * t)
        
        # Calculate standing wave
        standing = wave1 * wave2
        
        # Find nodes (zeros) and antinodes (peaks)
        nodes = []
        antinodes = []
        
        for i in range(1, len(t)-1):
            if abs(standing[i]) < 0.01:
                nodes.append(t[i])
            elif abs(abs(standing[i]) - np.max(abs(standing))) < 0.01:
                antinodes.append(t[i])
                
        return {
            'time': t,
            'standing_wave': standing,
            'nodes': nodes,
            'antinodes': antinodes,
            'frequency_ratio': f2/f1
        }
        
    def simulate_resonance(self, duration: float = 2.0) -> Dict:
        """Simulate QHRC resonance with musical harmonics."""
        # Time points
        t = np.linspace(0, duration, 2000)
        dt = t[1] - t[0]
        
        # System parameters from patent
        f1 = self.config['primary_coil']['frequency']   # 4790.45 Hz
        f2 = self.config['secondary_coil']['frequency'] # 7750.95 Hz
        k = self.config['primary_coil']['coupling']     # 0.999
        d = self.config['secondary_coil']['damping']    # 0.0005
        e = self.config['primary_coil']['energy_recapture'] # 0.999
        phi_decay = self.config['phi_decay']            # 1/φ
        
        # Initial conditions (normalized)
        y0 = [0.1, 0, 0.1, 0]  # [i1, di1/dt, i2, di2/dt]
        
        def system_dynamics(y, t):
            i1, di1dt, i2, di2dt = y
            
            # Add phi-harmonic feedback
            phi5 = np.sin(2 * np.pi * self.harmonics['phi5'] * t)
            phi8 = np.sin(2 * np.pi * self.harmonics['phi8'] * t)
            phi13 = np.sin(2 * np.pi * self.harmonics['phi13'] * t)
            
            # Primary coil with energy recapture
            d2i1dt2 = (
                k * f1 * i2 * (1 + e * phi5) -
                d * di1dt * phi_decay -
                f1**2 * i1
            )
            
            # Secondary coil with harmonic resonance
            d2i2dt2 = (
                k * f2 * i1 * (1 + e * phi8) -
                d * di2dt * phi_decay -
                f2**2 * i2 +
                0.1 * phi13
            )
            
            return [di1dt, d2i1dt2, di2dt, d2i2dt2]
        
        # Solve system
        from scipy.integrate import odeint
        solution = odeint(system_dynamics, y0, t)
        
        # Calculate energies
        E1 = 0.5 * (solution[:, 0]**2 + solution[:, 1]**2)
        E2 = 0.5 * (solution[:, 2]**2 + solution[:, 3]**2)
        
        # Calculate metrics
        resonance_ratio = np.max(E2) / np.max(E1)
        energy_transfer = np.mean(E2) / np.mean(E1)
        
        return {
            'time': t,
            'primary_current': solution[:, 0],
            'secondary_current': solution[:, 2],
            'primary_energy': E1,
            'secondary_energy': E2,
            'resonance_ratio': resonance_ratio,
            'energy_transfer': energy_transfer
        }
