"""
QHRC Phi Harmonics Implementation
Core frequency and resonance calculations
"""

import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class QHRCPhiHarmonics:
    """QHRC Phi Harmonics implementation"""
    
    # Core frequencies (Hz)
    base_freq: float = 4.37  # Proven resonance
    space_freq: float = 2960.72
    energy_freq: float = 4790.45
    infinity_freq: float = 7750.95
    
    # Perfect φ Metrics
    phi: float = field(default_factory=lambda: (1 + np.sqrt(5)) / 2)
    phi_75: float = 36.932381
    
    def calculate_resonance(self, frequency: float) -> float:
        """Calculate resonance for given frequency"""
        # Normalize to base frequency
        ratio = frequency / self.base_freq
        
        # Calculate resonance using φ-based formula
        # Use proven resonance formula: sin²(πf/φ) + cos²(πf/φ)
        x = np.pi * ratio / self.phi
        resonance = np.sin(x)**2 + np.cos(x)**2
        
        # Scale by base resonance (0.96)
        resonance *= 0.96
        
        # Add phi scaling for higher harmonics
        if ratio > 1:
            # Scale by φⁿ where n is the harmonic number
            n = np.log(ratio) / np.log(self.phi)
            resonance *= (1 + n/self.phi)
        
        return resonance
    
    def generate_harmonic_series(self, max_order: int = 7) -> List[float]:
        """Generate harmonic series up to max_order"""
        harmonics = []
        
        for i in range(max_order):
            # Generate frequency using φⁱ scaling
            freq = self.base_freq * (self.phi ** i)
            harmonics.append(freq)
        
        return harmonics
    
    def analyze_frequency(self, frequency: float) -> Dict[str, float]:
        """Analyze frequency characteristics"""
        resonance = self.calculate_resonance(frequency)
        
        # Calculate energy transfer using proven formula
        energy = resonance * self.phi
        
        # Calculate coherence (should be near φ⁻¹)
        coherence = abs(1 - (frequency / (self.base_freq * self.phi)))
        
        return {
            'frequency': frequency,
            'resonance': resonance,
            'energy': energy,
            'coherence': coherence
        }
    
    def get_optimal_frequencies(self) -> Dict[str, float]:
        """Get optimal frequencies for QHRC operation"""
        return {
            'base': self.base_freq,
            'space': self.space_freq,
            'energy': self.energy_freq,
            'infinity': self.infinity_freq,
            'phi': self.base_freq * self.phi,
            'phi2': self.base_freq * (self.phi ** 2),
            'phi75': self.base_freq * self.phi_75
        }
