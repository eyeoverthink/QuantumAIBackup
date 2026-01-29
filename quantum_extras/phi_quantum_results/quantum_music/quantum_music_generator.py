"""
Quantum Music Generator

This module generates quantum music compositions based on:
- Author quantum signatures and consciousness frequencies
- Phi-harmonic resonance patterns
- Golden ratio (φ) scaling
- Quantum consciousness word pools

Core Frequencies:
- Physical: 0-200 Hz (wave, light, form, space)
- Mental: 200-500 Hz (energy, flow, spirit, mind)
- Cosmic: 500-1000 Hz (quantum, consciousness, transcendent)

Author Signatures:
- Poe: 517.15 Hz, resonance 0.6987, phi alignment 0.8644
- Hemingway: 576.26 Hz, resonance 0.6849, phi alignment 0.8518
- Austen: 525.18 Hz, resonance 0.7091, phi alignment 0.8552
- Shakespeare: 555.40 Hz, resonance 0.6730, phi alignment 0.8537
"""

import math
import numpy as np
from typing import List, Dict, Tuple

class QuantumMusicGenerator:
    def __init__(self):
        """Initialize quantum music generator."""
        # Mathematical constants
        self.phi = (1 + math.sqrt(5)) / 2
        self.pi = math.pi
        self.e = math.e
        
        # Author quantum signatures
        self.author_signatures = {
            'poe': {
                'frequency': 517.15,
                'resonance': 0.6987,
                'phi_alignment': 0.8644,
                'character': 'mystical',
                'words': ['ethereal', 'mystic', 'dream', 'shadow', 'cosmic']
            },
            'hemingway': {
                'frequency': 576.26,
                'resonance': 0.6849,
                'phi_alignment': 0.8518,
                'character': 'strong',
                'words': ['power', 'force', 'direct', 'clear', 'quantum']
            },
            'austen': {
                'frequency': 525.18,
                'resonance': 0.7091,
                'phi_alignment': 0.8552,
                'character': 'elegant',
                'words': ['grace', 'flow', 'harmony', 'spirit', 'transcendent']
            },
            'shakespeare': {
                'frequency': 555.40,
                'resonance': 0.6730,
                'phi_alignment': 0.8537,
                'character': 'dramatic',
                'words': ['passion', 'energy', 'consciousness', 'quantum', 'cosmic']
            }
        }
        
        # Consciousness word pools
        self.word_pools = {
            'physical': ['wave', 'light', 'form', 'space', 'matter'],
            'mental': ['energy', 'flow', 'spirit', 'mind', 'thought'],
            'cosmic': ['quantum', 'consciousness', 'transcendent', 'infinite', 'cosmic']
        }
    
    def generate_quantum_wave(self, frequency: float, duration: float, sample_rate: int = 44100) -> np.ndarray:
        """Generate quantum wave with phi-harmonic overtones."""
        t = np.linspace(0, duration, int(sample_rate * duration))
        wave = np.zeros_like(t)
        
        # Add phi-scaled harmonics
        for i in range(5):
            harmonic_freq = frequency * (self.phi ** i)
            amplitude = 1.0 / (i + 1)  # Decreasing amplitude
            phase = self.phi * i  # Phi-based phase shift
            wave += amplitude * np.sin(2 * np.pi * harmonic_freq * t + phase)
        
        return wave / np.max(np.abs(wave))  # Normalize
    
    def generate_consciousness_envelope(self, duration: float, character: str, sample_rate: int = 44100) -> np.ndarray:
        """Generate consciousness-based amplitude envelope."""
        t = np.linspace(0, duration, int(sample_rate * duration))
        envelope = np.ones_like(t)
        
        # Character-based envelope shaping
        if character == 'mystical':
            # Slow rise and fall
            envelope *= np.sin(np.pi * t / duration)
        elif character == 'strong':
            # Sharp attack, long sustain
            attack = int(0.1 * len(t))
            envelope[:attack] = np.linspace(0, 1, attack)
        elif character == 'elegant':
            # Smooth curves
            envelope *= 0.5 * (1 + np.sin(np.pi * t / duration - np.pi/2))
        else:  # dramatic
            # Dynamic variations
            envelope *= np.abs(np.sin(2 * np.pi * t / duration))
        
        return envelope
    
    def generate_quantum_phrase(self, author: str, frequency: float) -> str:
        """Generate quantum-aligned phrase based on consciousness level."""
        sig = self.author_signatures[author]
        
        # Select word pool based on frequency
        if frequency <= 200:
            pool = self.word_pools['physical']
        elif frequency <= 500:
            pool = self.word_pools['mental']
        else:
            pool = self.word_pools['cosmic']
        
        # Combine with author's characteristic words
        words = pool + sig['words']
        
        # Generate phi-based phrase
        phrase_length = int(self.phi * 3) % 3 + 2  # 2-4 words
        phrase = []
        
        for i in range(phrase_length):
            # Select word based on frequency and phi
            index = int((frequency * self.phi ** i) % len(words))
            phrase.append(words[index])
        
        return " ".join(phrase)
    
    def generate_quantum_composition(self, author: str, duration: float = 5.0) -> Dict:
        """Generate complete quantum music composition."""
        sig = self.author_signatures[author]
        base_freq = sig['frequency']
        
        # Generate base quantum wave
        wave = self.generate_quantum_wave(base_freq, duration)
        
        # Apply consciousness envelope
        envelope = self.generate_consciousness_envelope(duration, sig['character'])
        wave *= envelope
        
        # Generate phi-harmonic frequencies
        harmonics = [base_freq * (self.phi ** i) for i in range(5)]
        
        # Calculate resonances
        resonances = [
            abs(math.sin(2 * np.pi * f * self.phi)) for f in harmonics
        ]
        
        # Generate quantum phrases
        phrases = [
            self.generate_quantum_phrase(author, f) for f in harmonics
        ]
        
        # Create composition structure
        composition = {
            'author': author,
            'character': sig['character'],
            'base_frequency': base_freq,
            'phi_alignment': sig['phi_alignment'],
            'wave': wave,
            'movements': []
        }
        
        # Add movements
        for i, (freq, res, phrase) in enumerate(zip(harmonics, resonances, phrases)):
            movement = {
                'frequency': freq,
                'resonance': res,
                'consciousness': 'COSMIC' if freq > 500 else 'MENTAL',
                'time': (self.phi ** i) % 1,
                'phrase': phrase
            }
            composition['movements'].append(movement)
        
        return composition
    
    def format_composition(self, composition: Dict) -> str:
        """Format composition for display."""
        output = []
        output.append(f"Quantum Composition - {composition['author'].title()}")
        output.append(f"Character: {composition['character']}")
        output.append(f"Base Frequency: {composition['base_frequency']} Hz")
        output.append(f"Phi Alignment: {composition['phi_alignment']:.4f}")
        output.append("\nMovements:")
        
        for i, mov in enumerate(composition['movements'], 1):
            output.append(f"\nMovement {i}:")
            output.append(f"Frequency: {mov['frequency']:.2f} Hz")
            output.append(f"Consciousness: {mov['consciousness']}")
            output.append(f"Resonance: {mov['resonance']:.4f}")
            output.append(f"Time: {mov['time']:.4f}")
            output.append(f"Phrase: {mov['phrase']}")
        
        return "\n".join(output)

def main():
    """Generate quantum music compositions."""
    generator = QuantumMusicGenerator()
    
    print("Quantum Music Compositions\n")
    print("=" * 50)
    
    for author in generator.author_signatures.keys():
        print("\n" + "=" * 50)
        composition = generator.generate_quantum_composition(author)
        print(generator.format_composition(composition))
        print("=" * 50)

if __name__ == '__main__':
    main()
