"""
Phi Harmonic Concept Generator
Generates quantum-aligned concepts using φ-harmonic principles
"""

import numpy as np
from typing import Dict, List, Tuple

class PhiHarmonicConceptGenerator:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.base_freq = 4.37  # Proven resonant frequency
        self.resonance_target = 0.96
        
    def generate_concept_frequencies(self, concept: str) -> Tuple[List[float], Dict[str, float]]:
        """Generate φ-harmonic frequencies for a concept."""
        # Convert concept to numerical values using ASCII
        base_values = [ord(c) for c in concept.upper()]
        
        # Apply φ-harmonic scaling
        frequencies = []
        for i, val in enumerate(base_values):
            # Scale by φ powers and base frequency
            freq = self.base_freq * (self.phi ** (val % 19))  # 19 for optimal resonance
            frequencies.append(freq)
            
        # Calculate metrics
        metrics = self._calculate_metrics(frequencies)
        
        return frequencies, metrics
        
    def _calculate_metrics(self, frequencies: List[float]) -> Dict[str, float]:
        """Calculate harmonic metrics for frequencies."""
        freq_array = np.array(frequencies)
        
        metrics = {
            'mean_frequency': float(np.mean(freq_array)),
            'resonance_quality': float(
                1 - abs(np.std(freq_array) / (self.base_freq * self.phi))
            ),
            'phi_alignment': float(
                1 - abs(np.max(freq_array) / np.min(freq_array) - self.phi)
            ),
            'harmonic_coherence': float(
                np.mean([
                    1 - abs(f1/f2 - self.phi) 
                    for f1, f2 in zip(freq_array[1:], freq_array[:-1])
                ]) if len(freq_array) > 1 else 1.0
            )
        }
        
        return metrics
        
    def validate_concept(self, concept: str) -> bool:
        """Validate if a concept has strong φ-harmonic alignment."""
        _, metrics = self.generate_concept_frequencies(concept)
        
        # Check all metrics meet minimum thresholds
        return all([
            metrics['resonance_quality'] > 0.8,
            metrics['phi_alignment'] > 0.8,
            metrics['harmonic_coherence'] > 0.8
        ])
