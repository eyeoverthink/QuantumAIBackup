"""
Quantum Synapse - Information transfer and processing
"""
from decimal import Decimal
import numpy as np
from typing import List, Dict

class QuantumSynapse:
    def __init__(self, synapse_type: str, base_freq: float = 0.96):
        self.type = synapse_type
        self.base_freq = Decimal(str(base_freq))
        self.phi = Decimal('1.618033988749895')
        self.resonance = self.base_freq
        self.coherence = Decimal('1.0')
        self.phi_alignment = Decimal('1.0')
    
    def get_resonance(self) -> float:
        return float(self.resonance)
    
    def get_coherence(self) -> float:
        return float(self.coherence)
    
    def get_phi_alignment(self) -> float:
        return float(self.phi_alignment)
    
    def process_signal(self, signal: List[float]) -> Dict:
        """Process signal through quantum synapse"""
        if not signal:
            return self._empty_result()
        
        # Calculate quantum metrics
        resonance = np.mean(signal)
        coherence = self._calculate_coherence(signal)
        phi_alignment = self._calculate_phi_alignment(signal)
        
        # Update synapse state
        self.resonance = Decimal(str(resonance))
        self.coherence = Decimal(str(coherence))
        self.phi_alignment = Decimal(str(phi_alignment))
        
        return {
            'resonance': resonance,
            'coherence': coherence,
            'phi_alignment': phi_alignment,
            'signal_strength': len(signal)
        }
    
    def _calculate_coherence(self, signal: List[float]) -> float:
        """Calculate quantum coherence"""
        if not signal:
            return 0
        return float(np.std(signal) / np.mean(signal))
    
    def _calculate_phi_alignment(self, signal: List[float]) -> float:
        """Calculate alignment with golden ratio"""
        if len(signal) < 2:
            return 0
            
        ratios = []
        for i in range(len(signal)-1):
            if signal[i] and signal[i+1]:
                ratio = max(signal[i], signal[i+1]) / min(signal[i], signal[i+1])
                ratios.append(abs(ratio - float(self.phi)))
                
        return float(1 - np.mean(ratios) if ratios else 0)
    
    def _empty_result(self) -> Dict:
        """Return empty processing result"""
        return {
            'resonance': float(self.base_freq),
            'coherence': 0,
            'phi_alignment': 0,
            'signal_strength': 0
        }
