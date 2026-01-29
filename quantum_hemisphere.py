"""
Quantum Hemispheres - Left and right brain processing
"""
from decimal import Decimal
import numpy as np
from typing import Dict, List
from quantum_cortex import QuantumCortex

class Hemisphere:
    def __init__(self, side: str):
        self.side = side
        self.phi = Decimal('1.618033988749895')
        self.resonance = Decimal('1.0')
        self.coherence = Decimal('1.0')
        self.phi_alignment = Decimal('1.0')
    
    def get_resonance(self) -> float:
        return float(self.resonance)
    
    def get_coherence(self) -> float:
        return float(self.coherence)
    
    def get_phi_alignment(self) -> float:
        return float(self.phi_alignment)
    
    def process_sequence(self, sequence: str, cortex: QuantumCortex, 
                        aa_resonance: Dict[str, Decimal]) -> Dict:
        """Process sequence through hemisphere"""
        if not sequence:
            return self._empty_result()
        
        # Calculate resonance pattern
        pattern = []
        bridges = []
        
        for i, aa in enumerate(sequence):
            if aa not in aa_resonance:
                continue
                
            res = float(aa_resonance[aa])
            pattern.append(res)
            
            if i > 0 and sequence[i-1] in aa_resonance:
                prev_res = float(aa_resonance[sequence[i-1]])
                ratio = max(res, prev_res) / min(res, prev_res)
                phi_proximity = abs(ratio - float(self.phi))
                
                if phi_proximity < 0.3:
                    bridges.append({
                        'position': i,
                        'residues': f'{sequence[i-1]}-{aa}',
                        'ratio': ratio,
                        'phi_proximity': phi_proximity,
                        'resonance': abs(1 - phi_proximity)
                    })
        
        # Update hemisphere state
        analysis = cortex.analyze_pattern(pattern)
        self.resonance = Decimal(str(analysis['resonance']))
        self.coherence = Decimal(str(analysis['coherence']))
        self.phi_alignment = Decimal(str(analysis['phi_alignment']))
        
        return {
            'resonance_pattern': pattern,
            'bridges': bridges,
            'metrics': analysis
        }
    
    def predict_structure(self, sequence: str, fold_metrics: Dict) -> List:
        """Predict structure elements"""
        if not sequence or len(sequence) < 4:
            return []
            
        elements = []
        for i in range(len(sequence)-3):
            window = sequence[i:i+4]
            coherence = self._calculate_window_coherence(window)
            
            if coherence > 2.0:
                if fold_metrics['alpha_helix_probability'] > 0.6:
                    elements.append(('H', i, i+4))
                elif fold_metrics['beta_sheet_probability'] > 0.6:
                    elements.append(('E', i, i+4))
                else:
                    elements.append(('C', i, i+4))
                    
        return elements
    
    def _calculate_window_coherence(self, window: str) -> float:
        """Calculate coherence for a sequence window"""
        if not window:
            return 0
        values = [ord(c) for c in window]
        return float(np.std(values) / np.mean(values))
    
    def _empty_result(self) -> Dict:
        """Return empty processing result"""
        return {
            'resonance_pattern': [],
            'bridges': [],
            'metrics': {
                'resonance': 0,
                'coherence': 0,
                'phi_alignment': 0
            }
        }

class LeftHemisphere(Hemisphere):
    def __init__(self):
        super().__init__('left')
        self.specialization = 'analytical'

class RightHemisphere(Hemisphere):
    def __init__(self):
        super().__init__('right')
        self.specialization = 'holistic'
