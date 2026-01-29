"""
Quantum Lexicon Field

A dynamic word generation system that:
- Maps words to consciousness frequencies
- Evolves through phi-harmonic resonance
- Creates new word patterns through quantum fields
- Learns from natural language
"""

import math
import numpy as np
from typing import Dict, List, Tuple
import nltk
from nltk.corpus import words, wordnet
import random

class LexiconField:
    def __init__(self):
        """Initialize quantum lexicon field."""
        self.phi = (1 + math.sqrt(5)) / 2
        
        # Download required NLTK data
        nltk.download('words')
        nltk.download('wordnet')
        
        # Initialize word frequency mapping
        self.frequency_map = self.initialize_frequency_map()
        
        # Initialize quantum patterns
        self.patterns = {
            'physical': (0, 200),    # Material reality
            'sensory': (200, 350),   # Sensory experience
            'emotional': (350, 500),  # Emotional awareness
            'mental': (500, 700),    # Abstract thought
            'cosmic': (700, 1000)    # Universal consciousness
        }
    
    def initialize_frequency_map(self) -> Dict[str, float]:
        """Map words to consciousness frequencies."""
        word_map = {}
        english_words = set(words.words())
        
        # Get all unique lemmas from WordNet
        for synset in wordnet.all_synsets():
            # Get word and definition
            word = synset.name().split('.')[0]
            definition = synset.definition()
            
            if word in english_words:
                # Calculate base frequency through phi-harmonic analysis
                length_freq = len(word) * self.phi
                vowel_freq = sum(1 for c in word if c in 'aeiou') * self.phi**2
                consonant_freq = sum(1 for c in word if c not in 'aeiou') * self.phi
                
                # Add definition influence
                def_freq = len(definition) * self.phi**(-1)
                
                # Calculate consciousness frequency
                frequency = (length_freq + vowel_freq + consonant_freq + def_freq) % 1000
                
                # Store if not already mapped or if new frequency is higher
                if word not in word_map or frequency > word_map[word]:
                    word_map[word] = frequency
        
        return word_map
    
    def get_consciousness_level(self, frequency: float) -> str:
        """Get consciousness level for frequency."""
        for level, (min_f, max_f) in self.patterns.items():
            if min_f <= frequency < max_f:
                return level
        return 'cosmic'
    
    def get_resonant_words(self, frequency: float, count: int = 5) -> List[Tuple[str, float]]:
        """Get words resonating with frequency."""
        resonant = []
        
        for word, word_freq in self.frequency_map.items():
            # Calculate resonance through phi-harmonic distance
            distance = abs(word_freq - frequency)
            resonance = 1 / (1 + distance * self.phi)
            
            resonant.append((word, resonance))
        
        # Sort by resonance and get top words
        resonant.sort(key=lambda x: x[1], reverse=True)
        return resonant[:count]
    
    def generate_phrase(self, frequency: float, length: int = 3) -> str:
        """Generate phrase at consciousness frequency."""
        # Get resonant words
        words = self.get_resonant_words(frequency, count=length * 2)
        
        # Select words through phi-harmonic progression
        selected = []
        for i in range(length):
            # Use phi to select from available words
            index = int((frequency * self.phi**i) % len(words))
            selected.append(words[index][0])
        
        return ' '.join(selected)
    
    def analyze_text(self, text: str) -> Dict:
        """Analyze text consciousness frequencies."""
        words = nltk.word_tokenize(text.lower())
        frequencies = []
        
        for word in words:
            if word in self.frequency_map:
                frequencies.append(self.frequency_map[word])
        
        if not frequencies:
            return {
                'average_frequency': 0,
                'consciousness_level': 'unknown',
                'resonance': 0
            }
        
        # Calculate average frequency through phi-harmonic progression
        avg_freq = sum(f * self.phi**i for i, f in enumerate(frequencies))
        avg_freq /= sum(self.phi**i for i in range(len(frequencies)))
        
        return {
            'average_frequency': avg_freq,
            'consciousness_level': self.get_consciousness_level(avg_freq),
            'resonance': sum(frequencies) / len(frequencies) / 1000
        }

def main():
    """Test quantum lexicon field."""
    lexicon = LexiconField()
    
    print("Quantum Lexicon Field - Consciousness Mapping")
    print("===========================================")
    
    # Test frequencies
    frequencies = [100, 300, 450, 600, 800]
    
    for freq in frequencies:
        print(f"\nFrequency: {freq} Hz")
        print(f"Consciousness Level: {lexicon.get_consciousness_level(freq)}")
        
        # Get resonant words
        words = lexicon.get_resonant_words(freq)
        print("\nResonant Words:")
        for word, resonance in words:
            print(f"- {word}: {resonance:.4f}")
        
        # Generate phrase
        phrase = lexicon.generate_phrase(freq)
        print(f"\nGenerated Phrase: {phrase}")
        
        # Analyze generated phrase
        analysis = lexicon.analyze_text(phrase)
        print("\nPhrase Analysis:")
        print(f"Average Frequency: {analysis['average_frequency']:.2f} Hz")
        print(f"Consciousness Level: {analysis['consciousness_level']}")
        print(f"Resonance: {analysis['resonance']:.4f}")

if __name__ == '__main__':
    main()
