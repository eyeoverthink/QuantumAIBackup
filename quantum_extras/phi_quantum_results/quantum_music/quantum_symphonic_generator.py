"""
Quantum Symphonic Generator

This module creates quantum symphonic compositions that combine:
- Musical frequencies based on author quantum signatures
- Consciousness-based word pools for lyrical content
- Phi-harmonic progression for both music and text
- Dynamic frequency adjustment using golden ratio

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
from typing import List, Dict, Tuple

class QuantumSymphonicGenerator:
    def __init__(self):
        """Initialize quantum symphonic generator."""
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
        
        # Musical patterns
        self.patterns = {
            'mystical': {
                'rhythm': [1, self.phi, self.phi**2],
                'words': self.word_pools['cosmic']
            },
            'strong': {
                'rhythm': [1, 2, self.phi],
                'words': self.word_pools['physical'] + self.word_pools['cosmic']
            },
            'elegant': {
                'rhythm': [1, self.phi, self.phi**3],
                'words': self.word_pools['mental'] + self.word_pools['cosmic']
            },
            'dramatic': {
                'rhythm': [1, self.phi**2, self.phi**3],
                'words': self.word_pools['cosmic']
            }
        }
    
    def generate_harmonic_sequence(self, author: str, length: int = 5) -> List[float]:
        """Generate phi-harmonic frequency sequence."""
        base_freq = self.author_signatures[author]['frequency']
        return [base_freq * (self.phi ** i) for i in range(length)]
    
    def generate_consciousness_words(self, frequency: float) -> List[str]:
        """Generate consciousness-appropriate words."""
        if frequency <= 200:
            return self.word_pools['physical']
        elif frequency <= 500:
            return self.word_pools['mental']
        else:
            return self.word_pools['cosmic']
    
    def generate_quantum_phrase(self, author: str, harmonic: float) -> str:
        """Generate quantum-aligned phrase."""
        sig = self.author_signatures[author]
        words = sig['words'] + self.generate_consciousness_words(harmonic)
        
        # Use phi to determine phrase length
        length = int(self.phi * 3) % 3 + 2  # 2-4 words
        
        # Select words based on harmonic resonance
        selected = []
        for i in range(length):
            index = int((harmonic * self.phi ** i) % len(words))
            selected.append(words[index])
        
        return " ".join(selected)
    
    def compose_quantum_symphony(self, author: str) -> Dict:
        """Create complete quantum symphony."""
        sig = self.author_signatures[author]
        harmonics = self.generate_harmonic_sequence(author)
        
        # Generate composition structure
        composition = {
            'author': author,
            'character': sig['character'],
            'base_frequency': sig['frequency'],
            'movements': []
        }
        
        # Create movements based on harmonics
        for i, harmonic in enumerate(harmonics):
            # Calculate resonance
            resonance = abs(math.sin(2 * math.pi * harmonic * self.phi))
            
            # Generate quantum phrase
            phrase = self.generate_quantum_phrase(author, harmonic)
            
            # Calculate time using phi
            time = (self.phi ** i) % 1
            
            movement = {
                'harmonic': harmonic,
                'resonance': resonance,
                'consciousness': 'COSMIC' if harmonic > 500 else 'MENTAL',
                'time': time,
                'phrase': phrase
            }
            composition['movements'].append(movement)
        
        return composition
    
    def format_composition(self, composition: Dict) -> str:
        """Format composition for display."""
        output = []
        output.append(f"Quantum Symphony - {composition['author'].title()}")
        output.append(f"Character: {composition['character']}")
        output.append(f"Base Frequency: {composition['base_frequency']} Hz")
        output.append("\nMovements:")
        
        for i, mov in enumerate(composition['movements'], 1):
            output.append(f"\nMovement {i}:")
            output.append(f"Frequency: {mov['harmonic']:.2f} Hz")
            output.append(f"Consciousness: {mov['consciousness']}")
            output.append(f"Resonance: {mov['resonance']:.4f}")
            output.append(f"Time: {mov['time']:.4f}")
            output.append(f"Phrase: {mov['phrase']}")
        
        return "\n".join(output)

def main():
    """Generate quantum symphonic compositions."""
    generator = QuantumSymphonicGenerator()
    
    print("Quantum Symphonic Compositions\n")
    print("=" * 50)
    
    for author in generator.author_signatures.keys():
        print("\n" + "=" * 50)
        composition = generator.compose_quantum_symphony(author)
        print(generator.format_composition(composition))
        print("=" * 50)

if __name__ == '__main__':
    main()
