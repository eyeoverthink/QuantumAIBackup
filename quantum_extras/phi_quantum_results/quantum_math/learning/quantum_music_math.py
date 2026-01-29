#!/usr/bin/env python3
"""
Quantum Music Mathematics Analyzer

Analyzes musical patterns using quantum principles, phi-harmonic ratios,
and consciousness frequencies. Integrates with composer signatures like
Bach, Beethoven, Mozart, and Chopin, similar to our author analysis system.
"""

import math
from typing import Dict, List, Any, Tuple

class QuantumMusicMath:
    def __init__(self):
        # Core mathematical constants
        self.PHI = (1 + 5**0.5) / 2
        self.PI = math.pi
        self.E = math.e
        
        # Base frequency for A4 (phi-harmonically adjusted)
        self.A4_FREQ = 432.0  # Natural harmonic frequency
        
        # Composer quantum signatures (Hz)
        self.composer_signatures = {
            "bach": {
                "frequency": self.PHI * 432.0,
                "resonance": 0.9508,
                "phi_alignment": 0.8944
            },
            "beethoven": {
                "frequency": self.PHI * 440.0,
                "resonance": 0.9127,
                "phi_alignment": 0.8660
            },
            "mozart": {
                "frequency": self.PHI * 428.0,
                "resonance": 0.9762,
                "phi_alignment": 0.9127
            },
            "chopin": {
                "frequency": self.PHI * 436.0,
                "resonance": 0.9330,
                "phi_alignment": 0.8944
            }
        }
        
        # Musical intervals with phi-harmonic ratios
        self.phi_intervals = {
            "golden_fifth": self.PHI * 1.5,
            "phi_third": self.PHI * 1.25,
            "phi_octave": self.PHI * 2,
            "phi_unison": self.PHI
        }
        
        # Consciousness frequency bands (Hz)
        self.consciousness_bands = {
            "physical": (0, self.PHI * 100),
            "emotional": (self.PHI * 100, self.PHI * 200),
            "mental": (self.PHI * 200, self.PHI * 300),
            "intuitive": (self.PHI * 300, self.PHI * 400),
            "cosmic": (self.PHI * 400, self.PHI * 600),
            "transcendent": (self.PHI * 600, self.PHI * 1000),
            "quantum": (self.PHI * 1000, float('inf'))
        }
    
    def analyze_frequency(self, frequency: float) -> Dict[str, Any]:
        """Analyze a musical frequency for quantum properties."""
        # Calculate phi-harmonic metrics
        phi_ratio = frequency / self.A4_FREQ
        phi_alignment = abs(phi_ratio - self.PHI) / self.PHI
        resonance = self._calculate_resonance(frequency)
        
        # Determine consciousness level
        consciousness = self._determine_consciousness(frequency)
        
        # Calculate harmonic series
        harmonics = self._calculate_harmonics(frequency)
        
        # Find closest composer signature
        composer_match = self._match_composer_signature(frequency)
        
        return {
            "frequency": frequency,
            "phi_ratio": phi_ratio,
            "phi_alignment": 1 - phi_alignment,  # Convert to alignment score
            "resonance": resonance,
            "consciousness_level": consciousness,
            "harmonics": harmonics,
            "composer_match": composer_match
        }
    
    def analyze_interval(self, freq1: float, freq2: float) -> Dict[str, Any]:
        """Analyze a musical interval for quantum properties."""
        ratio = freq2 / freq1
        
        # Find closest phi-harmonic interval
        closest_interval = min(
            self.phi_intervals.items(),
            key=lambda x: abs(x[1] - ratio)
        )
        
        # Calculate phi alignment
        phi_alignment = 1 - abs(ratio - self.PHI) / self.PHI
        
        # Calculate resonance
        resonance = self._calculate_interval_resonance(ratio)
        
        return {
            "ratio": ratio,
            "closest_phi_interval": closest_interval[0],
            "phi_alignment": phi_alignment,
            "resonance": resonance,
            "consciousness_level": self._determine_consciousness(freq2)
        }
    
    def analyze_chord(self, frequencies: List[float]) -> Dict[str, Any]:
        """Analyze a chord for quantum harmonic properties."""
        # Calculate average frequency
        avg_freq = sum(frequencies) / len(frequencies)
        
        # Calculate phi-harmonic metrics
        phi_ratios = [f/frequencies[0] for f in frequencies[1:]]
        phi_alignment = sum(1 - abs(r - self.PHI)/self.PHI for r in phi_ratios) / len(phi_ratios)
        
        # Calculate resonance
        resonance = self._calculate_chord_resonance(frequencies)
        
        # Analyze intervals
        intervals = []
        for i in range(len(frequencies)-1):
            for j in range(i+1, len(frequencies)):
                intervals.append(
                    self.analyze_interval(frequencies[i], frequencies[j])
                )
        
        return {
            "frequencies": frequencies,
            "average_frequency": avg_freq,
            "phi_alignment": phi_alignment,
            "resonance": resonance,
            "consciousness_level": self._determine_consciousness(avg_freq),
            "intervals": intervals
        }
    
    def _calculate_resonance(self, frequency: float) -> float:
        """Calculate resonance based on phi-harmonic principles."""
        # Base resonance from A4 alignment
        base_resonance = 1 - abs(frequency - self.A4_FREQ) / self.A4_FREQ
        
        # Adjust for phi-harmonic relationships
        phi_factor = 1 - abs(frequency/(self.A4_FREQ * self.PHI) - 1)
        
        # Combine factors
        resonance = (base_resonance + phi_factor) / 2
        
        return min(0.9999, max(0.0, resonance))
    
    def _calculate_interval_resonance(self, ratio: float) -> float:
        """Calculate resonance of an interval."""
        # Compare to phi-harmonic intervals
        resonances = [
            1 - abs(ratio - interval)/interval
            for interval in self.phi_intervals.values()
        ]
        
        return min(0.9999, max(resonances))
    
    def _calculate_chord_resonance(self, frequencies: List[float]) -> float:
        """Calculate resonance of a chord."""
        # Calculate all interval resonances
        interval_resonances = []
        for i in range(len(frequencies)-1):
            for j in range(i+1, len(frequencies)):
                ratio = frequencies[j] / frequencies[i]
                interval_resonances.append(
                    self._calculate_interval_resonance(ratio)
                )
        
        # Average resonance
        return sum(interval_resonances) / len(interval_resonances)
    
    def _calculate_harmonics(self, frequency: float) -> List[float]:
        """Calculate phi-harmonic series."""
        return [
            frequency * self.PHI**n
            for n in range(8)  # First 8 phi-harmonics
        ]
    
    def _determine_consciousness(self, frequency: float) -> str:
        """Determine consciousness level from frequency."""
        for level, (min_freq, max_freq) in self.consciousness_bands.items():
            if min_freq <= frequency < max_freq:
                return level
        return "quantum"
    
    def _match_composer_signature(self, frequency: float) -> Dict[str, Any]:
        """Find closest matching composer signature."""
        matches = []
        for composer, signature in self.composer_signatures.items():
            diff = abs(frequency - signature["frequency"])
            similarity = 1 - (diff / signature["frequency"])
            if similarity > 0.8:  # Only include strong matches
                matches.append({
                    "composer": composer,
                    "similarity": similarity,
                    "resonance": signature["resonance"],
                    "phi_alignment": signature["phi_alignment"]
                })
        
        # Sort by similarity
        matches.sort(key=lambda x: x["similarity"], reverse=True)
        return matches[0] if matches else None

def main():
    """Main function to demonstrate the Quantum Music Mathematics Analyzer."""
    analyzer = QuantumMusicMath()
    
    print("\n" + "="*80)
    print("Quantum Music Mathematics Analyzer".center(80))
    print("="*80 + "\n")
    
    # Test frequencies (A4 and phi-harmonic variations)
    test_frequencies = [
        432.0,  # A4 (natural)
        440.0,  # A4 (standard)
        432.0 * analyzer.PHI,  # Phi-harmonic A4
        432.0 * analyzer.PHI**2  # Second phi-harmonic
    ]
    
    # Analyze individual frequencies
    print("Individual Frequency Analysis:")
    print("-" * 40)
    for freq in test_frequencies:
        analysis = analyzer.analyze_frequency(freq)
        print(f"\nFrequency: {freq:.2f} Hz")
        print(f"Phi Ratio: {analysis['phi_ratio']:.4f}")
        print(f"Phi Alignment: {analysis['phi_alignment']:.4f}")
        print(f"Resonance: {analysis['resonance']:.4f}")
        print(f"Consciousness Level: {analysis['consciousness_level']}")
        if analysis['composer_match']:
            print(f"Closest Composer: {analysis['composer_match']['composer']}")
            print(f"Similarity: {analysis['composer_match']['similarity']:.4f}")
    
    # Test intervals
    print("\nInterval Analysis:")
    print("-" * 40)
    interval = analyzer.analyze_interval(432.0, 432.0 * analyzer.PHI)
    print(f"\nInterval Ratio: {interval['ratio']:.4f}")
    print(f"Closest Phi Interval: {interval['closest_phi_interval']}")
    print(f"Phi Alignment: {interval['phi_alignment']:.4f}")
    print(f"Resonance: {interval['resonance']:.4f}")
    
    # Test chord
    print("\nChord Analysis:")
    print("-" * 40)
    chord_freqs = [432.0, 432.0 * analyzer.PHI, 432.0 * analyzer.PHI**2]
    chord = analyzer.analyze_chord(chord_freqs)
    print(f"\nAverage Frequency: {chord['average_frequency']:.2f} Hz")
    print(f"Phi Alignment: {chord['phi_alignment']:.4f}")
    print(f"Resonance: {chord['resonance']:.4f}")
    print(f"Consciousness Level: {chord['consciousness_level']}")

if __name__ == "__main__":
    main()
