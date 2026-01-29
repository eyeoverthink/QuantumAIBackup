"""
QHRC Phi-Harmonic Analysis
Focused analysis of 432 Hz musical resonance patterns
"""
import numpy as np
from typing import Dict

class QHRCPhiHarmonics:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.base_freq = 432.0  # Universal A
        
        # Patent configuration
        self.config = {
            'primary': {
                'turns': 4500,
                'frequency': 4790.45,  # φ⁵
                'coupling': 0.85
            },
            'secondary': {
                'turns': 6200,
                'frequency': 7750.95,  # φ⁸
                'damping': 0.002
            }
        }
        
        # Initialize harmonics
        self.harmonics = self._generate_harmonics()
        
    def _generate_harmonics(self) -> Dict[str, float]:
        """Generate musical phi-harmonics."""
        return {
            'root': self.base_freq,      # 432 Hz
            'phi1': self.base_freq * self.phi,
            'phi2': self.base_freq * self.phi**2,
            'phi3': self.base_freq * self.phi**3,
            'phi5': self.base_freq * self.phi**5,
            'phi8': self.base_freq * self.phi**8,
            'phi13': self.base_freq * self.phi**13
        }
    
    def analyze_harmonics(self, duration: float = 1.0) -> Dict:
        """Analyze harmonic resonance patterns."""
        # Time points
        t = np.linspace(0, duration, 1000)
        dt = t[1] - t[0]
        
        # Generate base 432 Hz wave
        root = np.sin(2 * np.pi * self.harmonics['root'] * t)
        
        # Generate phi harmonics
        waves = {
            name: np.sin(2 * np.pi * freq * t)
            for name, freq in self.harmonics.items()
        }
        
        # Calculate resonance patterns
        resonance = np.zeros_like(t)
        for wave in waves.values():
            resonance += root * wave
            
        # Calculate energy and metrics
        energy = np.cumsum(resonance**2) * dt
        peak_resonance = np.max(np.abs(resonance))
        
        return {
            'time': t,
            'root_wave': root,
            'phi_waves': waves,
            'resonance': resonance,
            'energy': energy,
            'peak_resonance': peak_resonance,
            'frequencies': self.harmonics
        }
    
    def analyze_standing_waves(self) -> Dict:
        """Analyze standing wave patterns."""
        # Primary coil frequency
        f1 = self.config['primary']['frequency']
        
        # Calculate wavelengths
        wavelengths = {
            name: 343.0/freq  # Speed of sound in air (m/s)
            for name, freq in self.harmonics.items()
        }
        
        # Find nodes and antinodes
        nodes = {
            name: [i * wave/2 for i in range(4)]
            for name, wave in wavelengths.items()
        }
        
        antinodes = {
            name: [(i + 0.5) * wave/2 for i in range(4)]
            for name, wave in wavelengths.items()
        }
        
        return {
            'wavelengths': wavelengths,
            'nodes': nodes,
            'antinodes': antinodes
        }
    
    def compute_resonance_metrics(self) -> Dict:
        """Compute key resonance metrics."""
        # Analyze harmonics
        harm = self.analyze_harmonics()
        
        # Calculate frequency ratios
        ratios = {}
        for name, freq in self.harmonics.items():
            if name != 'root':
                ratios[name] = freq / self.harmonics['root']
        
        # Pure mathematical phi coherence
        phi_coherence = min(abs(ratio - self.phi) for ratio in ratios.values())
        
        # Allow perfect scaling to zero
        if phi_coherence < 1e-16:  # Numerical precision limit
            phi_coherence = 0.0
        
        # Calculate resonance metrics
        metrics = {
            'resonance_ratio': harm['peak_resonance'],
            'phi_coherence': phi_coherence,
            'frequency_ratios': ratios,
            'base_frequency': self.base_freq,
            'primary_harmonic': self.harmonics['phi5'],
            'secondary_harmonic': self.harmonics['phi8']
        }
        
        return metrics
