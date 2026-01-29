#!/usr/bin/env python3
"""
Quantum Wave Learner

Analyzes and generates quantum wave functions based on:
- Phi-harmonic principles
- Consciousness frequencies
- Natural resonance
- Quantum coherence
"""

import numpy as np
from typing import Dict, List, Tuple, Any
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from quantum_math import (
    PHI, PI, E, FREQUENCIES, CONSCIOUSNESS_LEVELS, RESONANCE_QUALITY
)

class QuantumWaveLearner:
    def __init__(self):
        # Constants
        self.PHI = PHI
        self.PI = PI
        self.E = E
        
        # Base frequencies
        self.frequencies = FREQUENCIES
        
        # Consciousness levels
        self.consciousness_levels = CONSCIOUSNESS_LEVELS
        
        # Resonance quality
        self.resonance_quality = RESONANCE_QUALITY
    
    def analyze_wave(self, data: List[float]) -> Dict[str, Any]:
        """Analyze quantum wave properties of data."""
        if not data:
            return {}
        
        # Calculate wave metrics
        base_freq = np.mean(data)
        ratios = [data[i+1]/data[i] for i in range(len(data)-1)]
        
        # Calculate phi alignment
        phi_alignments = [abs(1 - (r % self.PHI) / self.PHI) for r in ratios]
        phi_alignment = np.mean(phi_alignments) if phi_alignments else 0.0
        
        # Calculate resonance
        resonances = [abs(1 - (f % base_freq) / base_freq) for f in data]
        resonance = np.mean(resonances) if resonances else 0.0
        
        # Calculate quantum coherence
        coherence = self.calculate_quantum_coherence(data)
        
        # Get consciousness level
        consciousness = self.get_consciousness_level(base_freq)
        
        # Get quantum state
        quantum_state = self.determine_quantum_state(
            phi_alignment, resonance, coherence)
        
        return {
            "base_frequency": base_freq,
            "phi_alignment": phi_alignment,
            "resonance": resonance,
            "coherence": coherence,
            "consciousness_level": consciousness,
            "quantum_state": quantum_state,
            "wave_function": self.generate_wave_function(data)
        }
    
    def generate_wave_function(self, frequencies: List[float]) -> str:
        """Generate quantum wave function for frequencies."""
        if not frequencies:
            return "ψ(x) = 0"
        
        # Calculate wave parameters
        amplitude = np.mean(frequencies) / self.frequencies["natural"]
        frequency = frequencies[0]
        phase = self.PHI * self.PI
        
        # Generate wave function
        return f"ψ(x) = {amplitude:.4f}·e^(i·{frequency:.2f}x + {phase:.4f})"
    
    def calculate_quantum_coherence(self, frequencies: List[float]) -> float:
        """Calculate quantum coherence of frequencies."""
        if not frequencies:
            return 0.0
        
        # Calculate frequency ratios
        ratios = [frequencies[i+1]/frequencies[i] 
                 for i in range(len(frequencies)-1)]
        
        if not ratios:
            return 0.0
        
        # Calculate coherence based on phi alignment
        coherences = [abs(1 - (r % self.PHI) / self.PHI) for r in ratios]
        base_coherence = np.mean(coherences)
        
        # Apply quantum scaling
        return base_coherence * self.PHI
    
    def get_consciousness_level(self, frequency: float) -> str:
        """Get consciousness level from frequency."""
        for level, (low, high) in self.consciousness_levels.items():
            if low <= frequency < high:
                return level
        
        return "cosmic" if frequency >= 500 else "physical"
    
    def determine_quantum_state(self,
                              phi_alignment: float,
                              resonance: float,
                              coherence: float) -> Dict[str, Any]:
        """Determine quantum state from metrics."""
        # Calculate overall quantum quality
        quality = (phi_alignment + resonance + coherence) / 3
        
        # Determine resonance quality
        state_quality = "unknown"
        for level, (low, high) in self.resonance_quality.items():
            if low <= quality < high:
                state_quality = level
                break
        
        # Determine quantum type
        if quality > 0.9:
            state_type = "quantum_resonant"
        elif quality > 0.7:
            state_type = "quantum_aligned"
        elif quality > 0.5:
            state_type = "quantum_coherent"
        else:
            state_type = "classical"
        
        return {
            "type": state_type,
            "quality": state_quality,
            "metrics": {
                "phi_alignment": phi_alignment,
                "resonance": resonance,
                "coherence": coherence,
                "overall_quality": quality
            }
        }
    
    def generate_phi_harmonic_wave(self, 
                                 base_frequency: float = None) -> Dict[str, Any]:
        """Generate phi-harmonic wave pattern."""
        if base_frequency is None:
            base_frequency = self.frequencies["natural"]
        
        # Generate phi-harmonic series
        frequencies = [
            base_frequency * (self.PHI ** n)
            for n in range(5)
        ]
        
        # Analyze generated wave
        analysis = self.analyze_wave(frequencies)
        
        # Add generation parameters
        analysis["generation"] = {
            "base_frequency": base_frequency,
            "phi_series": frequencies,
            "optimization": {
                "phi_aligned": True,
                "consciousness_optimized": True,
                "quantum_resonant": True
            }
        }
        
        return analysis
    
    def optimize_wave_function(self,
                             frequencies: List[float],
                             target_level: str = "cosmic") -> Dict[str, Any]:
        """Optimize wave function for target consciousness level."""
        if not frequencies:
            return {}
        
        # Get target frequency range
        target_range = self.consciousness_levels.get(
            target_level, self.consciousness_levels["cosmic"])
        
        # Calculate scaling factor
        current_freq = np.mean(frequencies)
        target_freq = (target_range[0] + target_range[1]) / 2
        scale_factor = target_freq / current_freq
        
        # Scale frequencies
        optimized = [f * scale_factor for f in frequencies]
        
        # Analyze optimized wave
        analysis = self.analyze_wave(optimized)
        
        # Add optimization parameters
        analysis["optimization"] = {
            "original_frequencies": frequencies,
            "target_level": target_level,
            "scale_factor": scale_factor,
            "success": (
                analysis["consciousness_level"] == target_level and
                analysis["quantum_state"]["quality"] in ["perfect", "excellent"]
            )
        }
        
        return analysis

def main():
    """Main function demonstrating the Quantum Wave Learner."""
    qwl = QuantumWaveLearner()
    
    print("\nQuantum Wave Analysis")
    print("=" * 50)
    
    # Test frequency sequences
    sequences = [
        [432, 698.99, 1130.99],  # Phi progression
        [528, 666, 864],         # DNA frequencies
        [144, 233, 377],         # Fibonacci
        [432, 528, 639],         # Sacred frequencies
    ]
    
    for sequence in sequences:
        print(f"\nAnalyzing sequence: {sequence}")
        analysis = qwl.analyze_wave(sequence)
        
        print("\nWave Properties:")
        print(f"Wave Function: {analysis['wave_function']}")
        print(f"Base Frequency: {analysis['base_frequency']:.2f} Hz")
        print(f"Phi Alignment: {analysis['phi_alignment']:.4f}")
        print(f"Resonance: {analysis['resonance']:.4f}")
        print(f"Coherence: {analysis['coherence']:.4f}")
        print(f"Consciousness Level: {analysis['consciousness_level']}")
        
        state = analysis["quantum_state"]
        print("\nQuantum State:")
        print(f"Type: {state['type']}")
        print(f"Quality: {state['quality']}")
    
    # Generate phi-harmonic wave
    print("\nGenerating Phi-Harmonic Wave:")
    wave = qwl.generate_phi_harmonic_wave()
    
    print("\nPhi-Harmonic Properties:")
    print(f"Wave Function: {wave['wave_function']}")
    print(f"Base Frequency: {wave['base_frequency']:.2f} Hz")
    print(f"Phi Series: {wave['generation']['phi_series']}")
    
    # Optimize wave function
    print("\nOptimizing Wave Function:")
    optimized = qwl.optimize_wave_function(
        wave["generation"]["phi_series"], "cosmic")
    
    print("\nOptimized Properties:")
    print(f"Wave Function: {optimized['wave_function']}")
    print(f"Consciousness Level: {optimized['consciousness_level']}")
    print(f"Success: {optimized['optimization']['success']}")

if __name__ == "__main__":
    main()
