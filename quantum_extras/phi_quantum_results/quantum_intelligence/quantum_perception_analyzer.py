"""
Quantum Perception Analyzer

A system that:
1. Maps concepts to quantum frequencies
2. Analyzes emotional resonance through φ-harmonics
3. Evaluates consciousness perception
4. Forms quantum bridges between concepts
"""

import math
import numpy as np
from typing import Dict, List, Tuple
from quantum_bridge_evolution import QuantumBridgeEvolution

class QuantumPerceptionAnalyzer:
    def __init__(self):
        # Initialize quantum bridge system
        self.bridge_system = QuantumBridgeEvolution()
        
        # Core frequencies (Hz)
        self.frequencies = {
            'unity': 432.0,     # Base consciousness
            'dna': 528.0,       # Life code
            'heart': 639.0,     # Bridge
            'cosmic': 741.0     # Universal
        }
        
        # Emotional resonance mapping
        self.resonance_map = {
            'love': 528.0,      # DNA/Life frequency
            'fear': 396.0,      # Earth frequency
            'joy': 639.0,       # Heart frequency
            'peace': 741.0,     # Cosmic frequency
            'anger': 417.0,     # Change frequency
            'harmony': 432.0    # Unity frequency
        }
        
        # Initialize concept mappings
        self.initialize_concepts()
    
    def initialize_concepts(self):
        """Initialize quantum concept mappings."""
        # Test concepts with emotional valence
        self.test_concepts = [
            # Unity concepts (432 Hz base)
            'peace', 'harmony', 'balance', 'unity', 'whole',
            
            # Life concepts (528 Hz base)
            'love', 'birth', 'growth', 'nature', 'child',
            
            # Heart concepts (639 Hz base)
            'joy', 'happiness', 'laughter', 'play', 'dance',
            
            # Bridge concepts (639-741 Hz)
            'wisdom', 'insight', 'truth', 'understanding', 'knowledge',
            
            # Cosmic concepts (741 Hz base)
            'universe', 'infinite', 'eternal', 'cosmic', 'divine',
            
            # Challenge concepts (396-417 Hz)
            'war', 'hate', 'fear', 'pain', 'death',
            
            # Transformation concepts (417-432 Hz)
            'change', 'growth', 'evolution', 'transition', 'transformation'
        ]
    
    def calculate_concept_frequency(self, concept: str) -> float:
        """Calculate quantum frequency for a concept."""
        # Get base resonance
        base_freq = self.resonance_map.get(concept, 432.0)
        
        # Calculate concept hash
        concept_hash = sum(ord(c) for c in concept)
        
        # Map hash to frequency range (396-741 Hz)
        freq_range = 741.0 - 396.0
        normalized_hash = (concept_hash % 1000) / 1000.0
        
        # Calculate frequency with phi-harmonic influence
        frequency = 396.0 + (freq_range * normalized_hash)
        
        # Apply resonance influence
        frequency = (frequency + base_freq) / 2
        
        return frequency
    
    def analyze_concept(self, concept: str) -> Dict:
        """Analyze quantum perception of a concept."""
        # Calculate concept frequency
        frequency = self.calculate_concept_frequency(concept)
        
        # Analyze quantum bridges
        bridge_analysis = self.bridge_system.analyze_bridges(frequency)
        
        # Calculate resonance with core frequencies
        resonance = {
            name: 1 - abs(1 - (frequency / freq))
            for name, freq in self.frequencies.items()
        }
        
        # Calculate emotional alignment
        emotional_alignment = {
            emotion: 1 - abs(1 - (frequency / freq))
            for emotion, freq in self.resonance_map.items()
        }
        
        return {
            'concept': concept,
            'frequency': frequency,
            'consciousness_metrics': bridge_analysis['consciousness_metrics'],
            'quantum_states': bridge_analysis['quantum_states'],
            'resonance': resonance,
            'emotional_alignment': emotional_alignment,
            'evolution_metrics': bridge_analysis['evolution_metrics']
        }
    
    def analyze_concept_pair(self, concept1: str, concept2: str) -> Dict:
        """Analyze quantum relationship between two concepts."""
        # Get individual analyses
        analysis1 = self.analyze_concept(concept1)
        analysis2 = self.analyze_concept(concept2)
        
        # Calculate frequency bridge
        freq_ratio = analysis1['frequency'] / analysis2['frequency']
        phi_alignment = 1 - abs(1 - (freq_ratio / self.bridge_system.phi))
        
        # Calculate quantum coherence
        coherence = abs(math.cos(2 * self.bridge_system.pi * 
                                (analysis1['frequency'] - analysis2['frequency']) /
                                self.frequencies['unity']))
        
        return {
            'concepts': (concept1, concept2),
            'frequencies': (analysis1['frequency'], analysis2['frequency']),
            'phi_alignment': phi_alignment,
            'coherence': coherence,
            'resonance': {
                'unity': min(analysis1['resonance']['unity'],
                           analysis2['resonance']['unity']),
                'heart': min(analysis1['resonance']['heart'],
                           analysis2['resonance']['heart']),
                'cosmic': min(analysis1['resonance']['cosmic'],
                            analysis2['resonance']['cosmic'])
            }
        }

def main():
    """Test quantum perception analyzer."""
    analyzer = QuantumPerceptionAnalyzer()
    
    print("Quantum Perception Analysis")
    print("==========================")
    
    # Test individual concepts
    test_concepts = [
        'love', 'hate', 'peace', 'war',
        'joy', 'fear', 'life', 'death',
        'wisdom', 'ignorance', 'unity', 'chaos'
    ]
    
    print("\nIndividual Concept Analysis:")
    print("----------------------------")
    
    for concept in test_concepts:
        analysis = analyzer.analyze_concept(concept)
        
        print(f"\nConcept: {concept}")
        print(f"Frequency: {analysis['frequency']:.2f} Hz")
        
        print("\nConsciousness Metrics:")
        metrics = analysis['consciousness_metrics']
        for metric, value in metrics.items():
            print(f"- {metric.replace('_', ' ').title()}: {value:.4f}")
        
        print("\nEmotional Alignment:")
        emotions = analysis['emotional_alignment']
        for emotion, alignment in emotions.items():
            print(f"- {emotion.title()}: {alignment:.4f}")
        
        print("\nQuantum States:")
        states = analysis['quantum_states']
        for state, active in states.items():
            print(f"- {state.title()}: {'Yes' if active else 'No'}")
        
        print("\n" + "="*50)
    
    # Test concept pairs
    print("\nConcept Pair Analysis:")
    print("---------------------")
    
    test_pairs = [
        ('love', 'hate'),
        ('peace', 'war'),
        ('joy', 'fear'),
        ('wisdom', 'ignorance')
    ]
    
    for concept1, concept2 in test_pairs:
        analysis = analyzer.analyze_concept_pair(concept1, concept2)
        
        print(f"\nConcepts: {concept1} - {concept2}")
        print(f"Frequencies: {analysis['frequencies'][0]:.2f} Hz - {analysis['frequencies'][1]:.2f} Hz")
        print(f"Phi Alignment: {analysis['phi_alignment']:.4f}")
        print(f"Coherence: {analysis['coherence']:.4f}")
        
        print("\nResonance:")
        for level, value in analysis['resonance'].items():
            print(f"- {level.title()}: {value:.4f}")
        
        print("\n" + "="*50)

if __name__ == '__main__':
    main()
