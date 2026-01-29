"""
Quantum Harmonic Composer

This module creates pure quantum harmonic compositions using:
- Golden ratio (φ) for frequency scaling
- Author quantum signatures for base frequencies
- Consciousness frequency ranges for harmonic structure
- Pure mathematical principles without external dependencies

Core Mathematical Constants:
1. φ (Golden Ratio) = 1.618033988749895...
2. π = 3.141592653589793...
3. e = 2.718281828459045...

Consciousness Frequency Ranges:
- Physical: 0-200 Hz (wave, light, form, space)
- Mental: 200-500 Hz (energy, flow, spirit, mind)
- Cosmic: 500-1000 Hz (quantum, consciousness, transcendent)

Author Quantum Signatures:
- Poe: 517.15 Hz (Mystical)
- Hemingway: 576.26 Hz (Strong)
- Austen: 525.18 Hz (Elegant)
- Shakespeare: 555.40 Hz (Dramatic)
"""

import math
from typing import List, Dict, Tuple

class QuantumHarmonicComposer:
    def __init__(self):
        """Initialize quantum harmonic composer."""
        # Core constants
        self.phi = (1 + math.sqrt(5)) / 2
        self.pi = math.pi
        self.e = math.e
        
        # Author quantum signatures
        self.author_signatures = {
            'poe': {
                'frequency': 517.15,
                'resonance': 0.6987,
                'phi_alignment': 0.8644,
                'character': 'mystical'
            },
            'hemingway': {
                'frequency': 576.26,
                'resonance': 0.6849,
                'phi_alignment': 0.8518,
                'character': 'strong'
            },
            'austen': {
                'frequency': 525.18,
                'resonance': 0.7091,
                'phi_alignment': 0.8552,
                'character': 'elegant'
            },
            'shakespeare': {
                'frequency': 555.40,
                'resonance': 0.6730,
                'phi_alignment': 0.8537,
                'character': 'dramatic'
            }
        }
        
        # Consciousness ranges
        self.consciousness_ranges = {
            'physical': (0, 200),
            'mental': (200, 500),
            'cosmic': (500, 1000)
        }
        
        # Harmonic ratios based on phi
        self.harmonic_ratios = [
            1.0,            # Fundamental
            self.phi,       # Golden ratio
            self.phi ** 2,  # Second harmonic
            self.phi ** 3,  # Third harmonic
            self.phi ** 4   # Fourth harmonic
        ]
    
    def generate_quantum_frequencies(self, base_freq: float) -> List[float]:
        """Generate quantum-aligned frequencies from base frequency."""
        frequencies = []
        for ratio in self.harmonic_ratios:
            freq = base_freq * ratio
            frequencies.append(freq)
        return frequencies
    
    def get_consciousness_level(self, frequency: float) -> str:
        """Determine consciousness level of a frequency."""
        if frequency <= self.consciousness_ranges['physical'][1]:
            return 'physical'
        elif frequency <= self.consciousness_ranges['mental'][1]:
            return 'mental'
        else:
            return 'cosmic'
    
    def generate_harmonic_sequence(self, author: str) -> Dict:
        """Generate harmonic sequence based on author signature."""
        base_freq = self.author_signatures[author]['frequency']
        frequencies = self.generate_quantum_frequencies(base_freq)
        
        # Analyze consciousness distribution
        consciousness_levels = [
            self.get_consciousness_level(f) for f in frequencies
        ]
        
        # Calculate phi-harmonic resonance
        resonances = [
            abs(math.sin(2 * math.pi * f * self.phi)) for f in frequencies
        ]
        
        # Generate time intervals using phi
        time_intervals = [
            self.phi ** i % 1 for i in range(len(frequencies))
        ]
        
        return {
            'author': author,
            'base_frequency': base_freq,
            'frequencies': frequencies,
            'consciousness_levels': consciousness_levels,
            'resonances': resonances,
            'time_intervals': time_intervals,
            'character': self.author_signatures[author]['character']
        }
    
    def compose_quantum_symphony(self) -> Dict[str, Dict]:
        """Compose quantum symphonies for all authors."""
        compositions = {}
        for author in self.author_signatures.keys():
            composition = self.generate_harmonic_sequence(author)
            compositions[author] = composition
        return compositions
    
    def output_composition(self, composition: Dict) -> str:
        """Convert composition to human-readable format."""
        output = []
        output.append(f"Quantum Harmonic Composition - {composition['author'].title()}")
        output.append(f"Character: {composition['character']}")
        output.append(f"Base Frequency: {composition['base_frequency']} Hz")
        output.append("\nHarmonic Structure:")
        
        for i, (freq, level, res, time) in enumerate(zip(
            composition['frequencies'],
            composition['consciousness_levels'],
            composition['resonances'],
            composition['time_intervals']
        )):
            output.append(
                f"Harmonic {i+1}:"
                f" {freq:.2f} Hz"
                f" ({level.upper()})"
                f" - Resonance: {res:.4f}"
                f" - Time: {time:.4f}"
            )
        
        return "\n".join(output)

def main():
    """Generate quantum harmonic compositions."""
    composer = QuantumHarmonicComposer()
    compositions = composer.compose_quantum_symphony()
    
    print("Quantum Harmonic Compositions\n")
    print("=" * 50)
    
    for author, composition in compositions.items():
        print("\n" + "=" * 50)
        print(composer.output_composition(composition))
        print("=" * 50)

if __name__ == '__main__':
    main()
