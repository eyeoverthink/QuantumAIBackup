"""
Quantum Phi-Harmonic Thesaurus: Dynamic word relationships based on quantum resonance
"""

import numpy as np
from typing import Dict, List, Set, Tuple
import json
from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom

class QuantumPhiThesaurus:
    def __init__(self, core: QuantumPhiCore, random_gen: QuantumPhiRandom):
        self.core = core
        self.random = random_gen
        self.phi = float(core.PHI)
        
        # Initialize quantum word networks
        self._init_quantum_networks()
        
    def _init_quantum_networks(self):
        """Initialize quantum-entangled word networks."""
        # Base frequencies for word categories
        self.frequency_map = {
            'nouns': {
                'consciousness': 439.219556,  # φ-root base
                'quantum': 710.67,  # H-gate
                'resonance': 1149.89,  # X-gate
                'harmony': 1860.56,  # Y-gate
                'energy': 3010.46,  # Z-gate
                'light': 4870.02,  # φ⁵
                'wave': 7880.48,  # φ⁶
                'particle': 12752.49,  # T-gate
                # New quantum nouns
                'quark': 271.45,  # Neuron resonance
                'lepton': 439.22,  # φ-root
                'boson': 710.67,  # H-gate
                'fermion': 1149.89,  # X-gate
                'neuron': 1860.56,  # Y-gate
                'proton': 3010.46,  # Z-gate
                'electron': 4870.02,  # φ⁵
                'photon': 7880.48  # φ⁶
            },
            'verbs': {
                'flow': self.phi ** 2,
                'dance': self.phi ** 3,
                'shine': self.phi ** 4,
                'resonate': self.phi ** 5,
                'transform': self.phi ** 6,
                'evolve': self.phi ** 7,
                'harmonize': self.phi ** 8,
                'quantum_leap': self.phi ** 9,
                # New quantum verbs
                'spin': self.phi ** 2,
                'oscillate': self.phi ** 3,
                'vibrate': self.phi ** 4,
                'pulse': self.phi ** 5,
                'entangle': self.phi ** 6,
                'superpose': self.phi ** 7,
                'interfere': self.phi ** 8,
                'collapse': self.phi ** 9
            },
            'adjectives': {
                'cosmic': 1/self.phi,
                'quantum': 1/self.phi ** 2,
                'harmonic': 1/self.phi ** 3,
                'resonant': 1/self.phi ** 4,
                'sacred': 1/self.phi ** 5,
                'divine': 1/self.phi ** 6,
                'eternal': 1/self.phi ** 7,
                'infinite': 1/self.phi ** 8,
                # New quantum adjectives
                'entangled': 1/self.phi,
                'coherent': 1/self.phi ** 2,
                'superposed': 1/self.phi ** 3,
                'quantum_pure': 1/self.phi ** 4,
                'phi_aligned': 1/self.phi ** 5,
                'resonant': 1/self.phi ** 6,
                'transcendent': 1/self.phi ** 7,
                'unified': 1/self.phi ** 8
            }
        }
        
        # Quantum word relationships with resonance weights
        self.quantum_relationships = {
            # Consciousness levels
            'physical': {
                'words': ['earth', 'body', 'matter', 'form', 'structure', 'quark', 'proton', 'neutron'],
                'frequency': 271.45,  # Neuron resonance
                'coherence': 0.618  # φ⁻¹
            },
            'emotional': {
                'words': ['heart', 'feel', 'flow', 'energy', 'passion', 'pulse', 'wave', 'vibration'],
                'frequency': 439.22,  # φ-root
                'coherence': 0.786
            },
            'mental': {
                'words': ['mind', 'think', 'analyze', 'understand', 'know', 'electron', 'pattern', 'logic'],
                'frequency': 710.67,  # H-gate
                'coherence': 0.854
            },
            'intuitive': {
                'words': ['vision', 'see', 'perceive', 'insight', 'wisdom', 'photon', 'light', 'clarity'],
                'frequency': 1149.89,  # X-gate
                'coherence': 0.944
            },
            'cosmic': {
                'words': ['universe', 'infinite', 'eternal', 'divine', 'one', 'unified', 'transcendent', 'absolute'],
                'frequency': 1860.56,  # Y-gate
                'coherence': 1.0
            }
        }
        
        # Dynamic resonance patterns
        self.resonance_patterns = {
            'harmony': {
                'root': ['ground', 'earth', 'stable', 'solid', 'crystal', 'foundation'],
                'heart': ['love', 'feel', 'pulse', 'rhythm', 'resonance', 'harmony'],
                'mind': ['think', 'clear', 'bright', 'sharp', 'quantum', 'coherent'],
                'crown': ['light', 'pure', 'divine', 'cosmic', 'transcendent', 'unified']
            },
            'quantum': {
                'wave': ['flow', 'ripple', 'vibrate', 'oscillate', 'pulse', 'resonate'],
                'particle': ['point', 'seed', 'core', 'center', 'quark', 'nucleus'],
                'field': ['space', 'matrix', 'grid', 'web', 'network', 'fabric'],
                'force': ['power', 'drive', 'push', 'pull', 'attract', 'repel']
            },
            'consciousness': {
                'awareness': ['wake', 'alert', 'alive', 'present', 'aware', 'conscious'],
                'expansion': ['grow', 'rise', 'expand', 'evolve', 'transform', 'transcend'],
                'integration': ['merge', 'blend', 'unite', 'combine', 'harmonize', 'synthesize'],
                'transcendence': ['lift', 'soar', 'ascend', 'transform', 'enlighten', 'illuminate']
            },
            # New quantum patterns
            'particle': {
                'quarks': ['up', 'down', 'charm', 'strange', 'top', 'bottom'],
                'leptons': ['electron', 'muon', 'tau', 'neutrino'],
                'bosons': ['photon', 'gluon', 'graviton', 'higgs'],
                'hadrons': ['proton', 'neutron', 'meson', 'baryon']
            },
            'frequency': {
                'phi': ['golden', 'divine', 'perfect', 'harmonic', 'resonant'],
                'neural': ['brain', 'synapse', 'neuron', 'dendrite', 'axon'],
                'cosmic': ['star', 'galaxy', 'universe', 'cosmos', 'infinite'],
                'quantum': ['superposition', 'entanglement', 'coherence', 'collapse']
            },
            'gate': {
                'hadamard': ['superpose', 'transform', 'combine', 'mix'],
                'pauli_x': ['flip', 'invert', 'mirror', 'reflect'],
                'pauli_y': ['rotate', 'spin', 'phase', 'shift'],
                'pauli_z': ['phase', 'polarize', 'orient', 'align']
            }
        }
        
    def get_quantum_synonyms(self, word: str, resonance_type: str = 'harmony') -> List[str]:
        """Get quantum-entangled synonyms based on resonance type."""
        # Calculate quantum resonance
        word_freq = self._get_word_frequency(word)
        resonance = self._calculate_resonance(word_freq)
        
        # Get base synonyms
        base_synonyms = self._get_base_synonyms(word)
        
        # Apply quantum transformation
        quantum_synonyms = []
        for synonym in base_synonyms:
            syn_freq = self._get_word_frequency(synonym)
            syn_resonance = self._calculate_resonance(syn_freq)
            
            # Check resonance compatibility
            if abs(resonance - syn_resonance) < self.phi ** -3:
                quantum_synonyms.append(synonym)
        
        return quantum_synonyms
    
    def get_resonant_words(self, frequency: float, count: int = 5) -> List[str]:
        """Get words that resonate at a specific frequency."""
        resonant_words = []
        resonance_threshold = self.phi ** -4
        
        for category, words in self.frequency_map.items():
            for word, word_freq in words.items():
                if abs(frequency - word_freq) < resonance_threshold:
                    resonant_words.append(word)
        
        # Sort by resonance strength
        resonant_words.sort(key=lambda w: abs(frequency - self._get_word_frequency(w)))
        return resonant_words[:count]
    
    def generate_quantum_phrase(self, seed_word: str, length: int = 4) -> List[str]:
        """Generate a quantum-entangled phrase from a seed word."""
        phrase = [seed_word]
        seed_freq = self._get_word_frequency(seed_word)
        
        for _ in range(length - 1):
            # Get current resonance
            current_freq = self._get_word_frequency(phrase[-1])
            
            # Calculate target frequency using phi-harmonic progression
            target_freq = current_freq * self.phi
            
            # Get resonant words
            next_words = self.get_resonant_words(target_freq)
            
            # Choose next word
            if next_words:
                phrase.append(next_words[0])
        
        return phrase
    
    def _get_word_frequency(self, word: str) -> float:
        """Get the quantum frequency of a word."""
        # Check all categories
        for category in self.frequency_map.values():
            if word in category:
                return category[word]
        
        # Calculate based on letters if not found
        freq = 0
        for i, char in enumerate(word.lower()):
            freq += ord(char) * self.phi ** (i / len(word))
        return freq % (self.phi ** 10)
    
    def _calculate_resonance(self, frequency: float) -> float:
        """Calculate quantum resonance of a frequency."""
        return (frequency * self.phi) % 1
    
    def _get_base_synonyms(self, word: str) -> List[str]:
        """Get base synonyms from quantum relationships."""
        synonyms = set()
        
        # Check all relationship categories
        for category in self.quantum_relationships.values():
            if word in category['words']:
                synonyms.update(category['words'])
        
        # Check resonance patterns
        for pattern in self.resonance_patterns.values():
            for group in pattern.values():
                if word in group:
                    synonyms.update(group)
        
        # Remove the original word
        synonyms.discard(word)
        return list(synonyms)

def main():
    """Test the quantum thesaurus."""
    core = QuantumPhiCore()
    random_gen = QuantumPhiRandom(core)
    thesaurus = QuantumPhiThesaurus(core, random_gen)
    
    # Test words
    test_words = ['quantum', 'light', 'consciousness', 'harmony']
    
    for word in test_words:
        print(f"\nQuantum analysis for '{word}':")
        print("=" * 40)
        
        # Get frequency and resonance
        freq = thesaurus._get_word_frequency(word)
        res = thesaurus._calculate_resonance(freq)
        print(f"Frequency: {freq:.2f} Hz")
        print(f"Resonance: {res:.4f}")
        
        # Get quantum synonyms
        synonyms = thesaurus.get_quantum_synonyms(word)
        print("\nQuantum Synonyms:")
        print(", ".join(synonyms))
        
        # Generate quantum phrase
        phrase = thesaurus.generate_quantum_phrase(word)
        print("\nQuantum Phrase:")
        print(" ".join(phrase))
        print()

if __name__ == "__main__":
    main()
