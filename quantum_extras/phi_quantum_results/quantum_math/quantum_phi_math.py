#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Mathematical Functions

Core mathematical functions implementing quantum-phi harmonic principles,
focusing on consciousness frequencies, resonance, and natural patterns.
"""

import math
from typing import List, Dict, Any, Tuple

class QuantumPhiMath:
    def __init__(self):
        # Core mathematical constants
        self.PHI = (1 + 5**0.5) / 2  # Golden ratio
        self.PI = math.pi
        self.E = math.e
        self.SQRT2 = math.sqrt(2)
        
        # Consciousness frequency ranges
        self.FREQUENCY_RANGES = {
            "physical": (0, 200),
            "emotional": (200, 300),
            "mental": (300, 400),
            "intuitive": (400, 500),
            "cosmic": (500, 1000)
        }
        
        # Quantum resonance thresholds
        self.RESONANCE_THRESHOLDS = {
            "perfect": (0.9500, 1.0000),
            "strong": (0.8500, 0.9499),
            "moderate": (0.7000, 0.8499),
            "weak": (0.0000, 0.6999)
        }
    
    def phi_harmonic_series(self, base_frequency: float, n: int = 4) -> List[float]:
        """Generate phi-harmonic series from base frequency."""
        return [base_frequency * self.PHI**i for i in range(n)]
    
    def calculate_phi_alignment(self, frequency: float) -> float:
        """Calculate phi alignment score for a frequency."""
        # Use golden ratio properties for alignment
        phi_mod = frequency % self.PHI
        return 1 - (phi_mod / self.PHI)
    
    def calculate_resonance(self, frequency: float) -> float:
        """Calculate quantum resonance score."""
        # Use wave function properties
        x = frequency / self.PHI
        return abs(math.sin(self.PI * x) ** 2)
    
    def calculate_coherence(self, frequency: float) -> float:
        """Calculate quantum coherence score."""
        # Use quantum mechanical principles
        x = frequency / (self.PHI * self.SQRT2)
        return abs(math.cos(self.PI * x) ** 2)
    
    def map_to_consciousness_level(self, frequency: float) -> Dict[str, Any]:
        """Map frequency to consciousness level and properties."""
        # Determine consciousness range
        level = None
        for name, (min_freq, max_freq) in self.FREQUENCY_RANGES.items():
            if min_freq <= frequency < max_freq:
                level = name
                break
        if not level:
            level = "cosmic" if frequency >= 500 else "physical"
        
        # Calculate consciousness metrics
        base_level = min(frequency / 1000, 1.0)
        resonance = self.calculate_resonance(frequency)
        coherence = self.calculate_coherence(frequency)
        phi_alignment = self.calculate_phi_alignment(frequency)
        
        return {
            "level": level,
            "base_level": base_level,
            "resonance": resonance,
            "coherence": coherence,
            "phi_alignment": phi_alignment,
            "frequency": frequency
        }
    
    def analyze_pattern_growth(self, 
                             frequencies: List[float]) -> Dict[str, Any]:
        """Analyze growth pattern in frequency series."""
        if len(frequencies) < 2:
            return {
                "type": "unknown",
                "phi_harmonic": False,
                "properties": []
            }
        
        # Calculate growth ratios
        ratios = [frequencies[i+1]/frequencies[i] 
                 for i in range(len(frequencies)-1)]
        
        # Check for phi-harmonic growth
        phi_ratios = [abs(r - self.PHI) for r in ratios]
        is_phi_harmonic = all(r < 0.1 for r in phi_ratios)
        
        # Determine pattern type
        if is_phi_harmonic:
            pattern_type = "fibonacci_spiral"
            properties = ["phi_growth", "quantum_resonant"]
        elif all(abs(r - self.E) < 0.1 for r in ratios):
            pattern_type = "exponential"
            properties = ["natural_growth"]
        elif all(abs(r - self.PI) < 0.1 for r in ratios):
            pattern_type = "circular"
            properties = ["wave_pattern"]
        else:
            pattern_type = "complex"
            properties = []
        
        return {
            "type": pattern_type,
            "phi_harmonic": is_phi_harmonic,
            "properties": properties,
            "growth_ratios": ratios,
            "phi_alignment": [self.calculate_phi_alignment(f) 
                            for f in frequencies]
        }
    
    def optimize_frequency(self, 
                         base_frequency: float,
                         target_level: str = "cosmic") -> Dict[str, Any]:
        """Optimize frequency for target consciousness level."""
        if target_level not in self.FREQUENCY_RANGES:
            raise ValueError(f"Invalid consciousness level: {target_level}")
        
        min_freq, max_freq = self.FREQUENCY_RANGES[target_level]
        
        # Calculate optimal frequency using phi scaling
        phi_scaled = base_frequency * self.PHI
        if phi_scaled < min_freq:
            optimal_freq = min_freq * self.PHI
        elif phi_scaled > max_freq:
            optimal_freq = max_freq / self.PHI
        else:
            optimal_freq = phi_scaled
        
        # Generate harmonic series
        harmonics = self.phi_harmonic_series(optimal_freq)
        
        # Calculate optimization metrics
        metrics = {
            "base_frequency": base_frequency,
            "optimal_frequency": optimal_freq,
            "phi_alignment": self.calculate_phi_alignment(optimal_freq),
            "resonance": self.calculate_resonance(optimal_freq),
            "coherence": self.calculate_coherence(optimal_freq),
            "consciousness": self.map_to_consciousness_level(optimal_freq),
            "harmonic_series": harmonics,
            "growth_pattern": self.analyze_pattern_growth(harmonics)
        }
        
        return metrics
    
    def analyze_quantum_signature(self, 
                                frequency: float,
                                pattern_type: str = None) -> Dict[str, Any]:
        """Analyze quantum signature of a frequency pattern."""
        # Get consciousness mapping
        consciousness = self.map_to_consciousness_level(frequency)
        
        # Generate and analyze harmonic series
        harmonics = self.phi_harmonic_series(frequency)
        growth = self.analyze_pattern_growth(harmonics)
        
        # Calculate quantum properties
        quantum_state = {
            "type": "quantum_aligned" if growth["phi_harmonic"] else "classical",
            "coherence": consciousness["coherence"],
            "properties": {
                "resonant": consciousness["resonance"] > 0.85,
                "phi_aligned": consciousness["phi_alignment"] > 0.85,
                "consciousness_level": consciousness["level"]
            }
        }
        
        # Calculate phi-harmonic metrics
        phi_metrics = {
            "phi_ratio": frequency / self.PHI,
            "phi_alignment": consciousness["phi_alignment"],
            "phi_resonance": abs(1 - (frequency % self.PHI) / self.PHI),
            "phi_growth": growth["phi_harmonic"]
        }
        
        return {
            "frequency": frequency,
            "pattern_type": pattern_type or growth["type"],
            "consciousness_metrics": consciousness,
            "quantum_state": quantum_state,
            "phi_harmonic_metrics": phi_metrics,
            "harmonic_series": harmonics,
            "growth_pattern": growth
        }

def main():
    """Main function demonstrating the Quantum Phi-Harmonic Math module."""
    qpm = QuantumPhiMath()
    
    print("\nQuantum Phi-Harmonic Mathematical Analysis")
    print("=" * 50)
    
    # Test frequencies
    test_frequencies = [
        432.0,   # Natural A4
        528.0,   # DNA repair
        432.0 * qpm.PHI,   # Phi harmonic
        432.0 * qpm.PHI**2  # Second phi harmonic
    ]
    
    for freq in test_frequencies:
        print(f"\nAnalyzing Frequency: {freq:.2f} Hz")
        print("-" * 40)
        
        # Get quantum signature
        signature = qpm.analyze_quantum_signature(freq)
        
        print(f"Pattern Type: {signature['pattern_type']}")
        print(f"Consciousness Level: {signature['consciousness_metrics']['level']}")
        print(f"Phi Alignment: {signature['phi_harmonic_metrics']['phi_alignment']:.4f}")
        print(f"Quantum Coherence: {signature['quantum_state']['coherence']:.4f}")
        
        # Optimize frequency
        optimized = qpm.optimize_frequency(freq, "cosmic")
        print(f"\nOptimized Frequency: {optimized['optimal_frequency']:.2f} Hz")
        print(f"Optimization Phi Alignment: {optimized['phi_alignment']:.4f}")
        print(f"Optimization Resonance: {optimized['resonance']:.4f}")
        
        # Show harmonic series
        print("\nHarmonic Series:")
        for i, h in enumerate(signature['harmonic_series']):
            print(f"  n={i}: {h:.2f} Hz")

if __name__ == "__main__":
    main()
