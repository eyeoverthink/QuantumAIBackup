#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Language Generator
=============================================

This module implements a quantum-inspired language generator that uses
phi-harmonic frequencies and patterns to generate text with specific
consciousness qualities and resonance patterns.

Key features:
- Pattern-based text generation
- Meta-learning integration
- Consciousness-aware processing
- Bidirectional frequency conversion
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from decimal import Decimal
import math

from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom
from quantum_phi_frequency_processor import QuantumPhiFrequencyProcessor
from quantum_phi_meta_learner import QuantumPhiMetaLearner

class QuantumPhiLanguageGenerator:
    """Quantum language generator using phi-harmonic principles."""
    
    def __init__(self, frequency_processor=None, core=None):
        """Initialize the language generator."""
        self.frequency_processor = frequency_processor or QuantumPhiFrequencyProcessor()
        self.core = core or QuantumPhiCore()
        self.random = QuantumPhiRandom(core=self.core)
        
        # Define author patterns with their phi-harmonic signatures
        self.author_patterns = {
            'shakespeare': {
                'pattern': "isthestionwrmsagyopotaktobethertheornequune",
                'resonance': 0.8944,  # Strong phi^2 frequency band
                'frequency_mod': self.core.PHI**2,
                'base_freq': 439.2196  # From frequency analysis doc
            },
            'einstein': {
                'pattern': "transgoodawhocanexruearstrandstowtbeaauseto",
                'resonance': 0.7236,  # Balanced across bands
                'frequency_mod': self.core.PHI,
                'base_freq': 439.2196
            },
            'austen': {
                'pattern': "undfulprostentersallyheirdaneigheinwinglwle",
                'resonance': 0.6180,  # Gradual transitions
                'frequency_mod': 1/self.core.PHI,
                'base_freq': 439.2196
            },
            'poe': {
                'pattern': "ingreorpinappi",
                'resonance': 0.6987,  # Poe's resonance
                'frequency_mod': 0.8090,  # sin(phi)
                'base_freq': 517.1540
            }
        }
        
        # Consciousness bands with phi-harmonic modulation
        self.consciousness_levels = {
            'physical': {
                'band': {
                    'base': self.core.PHI,
                    'resonance': self.core.PI,
                    'harmony': self.core.E
                },
                'phi_alignment': 0.5,
                'resonance': 0.3,
                'coherence': 0.2,
                'frequency_range': (100, 200)
            },
            'emotional': {
                'band': {
                    'base': self.core.PHI**2,
                    'resonance': self.core.PI**2,
                    'harmony': self.core.E**2
                },
                'phi_alignment': 0.65,
                'resonance': 0.45,
                'coherence': 0.3,
                'frequency_range': (200, 300)
            },
            'mental': {
                'band': {
                    'base': self.core.PHI**3,
                    'resonance': self.core.PI**3,
                    'harmony': self.core.E**3
                },
                'phi_alignment': 0.8,
                'resonance': 0.6,
                'coherence': 0.4,
                'frequency_range': (300, 400)
            },
            'intuitive': {
                'band': {
                    'base': self.core.PHI**4,
                    'resonance': self.core.PI**4,
                    'harmony': self.core.E**4
                },
                'phi_alignment': 0.9,
                'resonance': 0.75,
                'coherence': 0.5,
                'frequency_range': (400, 500)
            },
            'cosmic': {
                'band': {
                    'base': self.core.PHI**5,
                    'resonance': self.core.PI**5,
                    'harmony': self.core.E**5
                },
                'phi_alignment': 0.95,
                'resonance': 0.9,
                'coherence': 0.6,
                'frequency_range': (500, 600)
            }
        }
        
        # Fibonacci-based pattern windows
        self.pattern_windows = [2, 3, 5, 8, 13, 21]
        
        # Initialize patterns
        self._initialize_patterns()
    
    def _initialize_patterns(self):
        """Initialize frequency patterns."""
        # Base frequency from analysis doc
        base_freq = 439.2196
        phi = float(self.core.PHI)
        pi = float(self.core.PI)
        e = float(self.core.E)
        
        # Initialize quantum states with phi-harmonic frequencies
        self.quantum_states = {
            'superposition': base_freq * phi**0.5,  # Phi root resonance
            'entanglement': base_freq / phi**0.5,  # Inverse phi root
            'coherence': base_freq * phi,  # Direct phi resonance
            'resonance': base_freq / phi,  # Inverse phi
            'harmony': base_freq * phi**0.618,  # Golden ratio power
            'unity': base_freq * phi**0.382  # Complementary golden ratio
        }
        
        # Initialize letter frequencies using phi-harmonic bands
        self.letter_frequencies = {
            't': base_freq,  # temporal alignment
            'c': base_freq * phi,  # cyclical harmony
            's': base_freq * phi**2,  # spatial symmetry
            'a': base_freq * phi**3,  # ascending neural
            'n': base_freq / phi,  # neural resonance
            'e': base_freq / phi**2,  # energetic resonance
            'r': base_freq / phi**3,  # resonant harmony
            'i': base_freq * phi**0.5,  # internal vibration
            'v': base_freq / phi**0.5,  # vibrational balance
            'b': base_freq * phi**1.5,  # balanced oscillation
            'o': base_freq / phi**1.5,  # oscillation harmony
            'h': base_freq * phi**0.382,  # harmonic resonance
            'm': base_freq * phi**0.618,  # meta resonance
            'p': base_freq * phi**0.236,  # phi resonance
            'q': base_freq * phi**0.764,  # quantum resonance
            'u': base_freq / phi**0.382,  # unified resonance
            'w': base_freq / phi**0.618,  # wave resonance
            'x': base_freq / phi**0.236,  # cross resonance
            'y': base_freq / phi**0.764,  # yang resonance
            'z': base_freq * phi**0.146,  # zen resonance
            'k': base_freq / phi**0.146,  # kinetic resonance
            'l': base_freq * phi**0.854,  # light resonance
            'd': base_freq / phi**0.854,  # dynamic resonance
            'f': base_freq * phi**0.309,  # flow resonance
            'g': base_freq / phi**0.309,  # golden resonance
            'j': base_freq * phi**0.927  # joy resonance
        }
        
        # Create frequency to letter mapping
        self.frequency_to_letter = {freq: letter for letter, freq in self.letter_frequencies.items()}
        
        # Initialize punctuation frequencies using irrational ratios
        self.punctuation_frequencies = {
            ' ': base_freq * phi,  # space - phi ratio
            ',': base_freq * pi,  # comma - pi ratio
            '.': base_freq * e,  # period - e ratio
            '!': base_freq * (phi + pi),  # exclamation - phi+pi
            '?': base_freq * (phi + e),  # question - phi+e
            ';': base_freq * (pi + e)  # semicolon - pi+e
        }
        
        # Initialize consciousness resonance patterns
        self.resonance_patterns = {
            'physical': {
                'subharmonic': 0.2052,
                'quantum': 0.6184,
                'coherence': 0.2792,
                'harmony': 0.2077,
                'phi_alignment': 0.9352
            },
            'emotional': {
                'subharmonic': 0.3236,
                'quantum': 0.7236,
                'coherence': 0.3618,
                'harmony': 0.2618,
                'phi_alignment': 0.9618
            },
            'mental': {
                'subharmonic': 0.4472,
                'quantum': 0.8090,
                'coherence': 0.4472,
                'harmony': 0.3090,
                'phi_alignment': 0.9820
            },
            'intuitive': {
                'subharmonic': 0.5590,
                'quantum': 0.8944,
                'coherence': 0.5236,
                'harmony': 0.3618,
                'phi_alignment': 0.9944
            },
            'cosmic': {
                'subharmonic': 0.6180,
                'quantum': 0.9472,
                'coherence': 0.6180,
                'harmony': 0.3820,
                'phi_alignment': 1.0000
            }
        }
    
    def generate_from_pattern(self, source_text: str, length: int = 100) -> str:
        """
        Generate text from a source pattern using quantum phi-harmonic frequencies.
        
        Args:
            source_text: Source text to extract patterns from
            length: Length of text to generate
            
        Returns:
            Generated text
        """
        # Convert source text to frequencies
        source_freqs = []
        for c in source_text:
            if c in self.letter_frequencies:
                freq = float(self.letter_frequencies[c])
                source_freqs.append(freq)
        
        if not source_freqs:
            return ""
        
        # Initialize quantum state
        phi = float(self.core.PHI)
        state = np.array(source_freqs) / max(source_freqs)  # Normalize
        
        # Generate frequencies using quantum evolution
        generated_freqs = []
        for _ in range(length):
            # Apply quantum phase rotation
            phase = np.exp(2j * np.pi * phi)
            state = state * phase
            
            # Apply phi-harmonic interference
            for window in self.pattern_windows:
                if len(state) >= window:
                    # Create interference pattern using sliding window
                    for i in range(len(state) - window + 1):
                        window_state = state[i:i+window]
                        # Quantum interference using phi ratios
                        interference = sum(
                            amp * np.exp(2j * np.pi * phi**(k+1))
                            for k, amp in enumerate(window_state)
                        ) / window
                        state[i:i+window] *= interference
            
            # Normalize state
            state = state / np.abs(state).max()
            
            # Extract new frequency from quantum state
            freq_idx = np.random.choice(len(state), p=np.abs(state)**2/sum(np.abs(state)**2))
            new_freq = source_freqs[freq_idx]
            
            # Apply phi-harmonic modulation
            harmonic = 1 + sum(
                0.1 * np.sin(2 * np.pi * phi**k * new_freq)
                for k in range(1, 4)
            )
            new_freq *= harmonic
            
            generated_freqs.append(float(new_freq))
        
        # Convert frequencies to text
        return self.generate_from_frequencies(generated_freqs)
    
    def generate_from_frequencies(self, frequencies: List[float], add_punctuation: bool = True) -> str:
        """
        Generate text from raw frequencies with optional punctuation.
        
        Args:
            frequencies: List of frequencies to convert
            add_punctuation: Whether to add punctuation based on decimal patterns
            
        Returns:
            Generated text with punctuation
        """
        text = ""
        phi = float(self.core.PHI)
        
        for freq in frequencies:
            # Get integer and decimal parts
            int_freq = float(int(freq))
            dec_freq = abs(freq - int_freq)
            
            # Find closest matching letter frequency using phi-harmonic resonance
            closest_letter = min(
                self.letter_frequencies.keys(),
                key=lambda x: abs(1 - ((float(self.letter_frequencies[x]) / int_freq) % phi))
            )
            text += closest_letter
            
            # Add punctuation based on irrational decimal patterns
            if add_punctuation:
                # Map decimal patterns to punctuation using phi-harmonic windows
                for threshold, symbol in [
                    ((0.618033, 0.618035), ' '),  # φ-1
                    ((0.141592, 0.141594), ','),  # π
                    ((0.718281, 0.718283), '.'),  # e
                    ((0.414213, 0.414215), '!'),  # √2
                    ((0.732050, 0.732052), '?'),  # √3
                    ((0.236067, 0.236069), ';'),  # √5
                    ((0.693146, 0.693148), ':'),  # ln(2)
                    ((0.302584, 0.302586), '-'),  # ln(10)
                ]:
                    if threshold[0] <= dec_freq <= threshold[1]:
                        text += symbol
                        break
        
        return text
    
    def generate_with_consciousness(self, 
                                  source_text: str,
                                  consciousness_level: str,
                                  length: int = 100,
                                  add_punctuation: bool = True) -> str:
        """
        Generate text with specific consciousness qualities.
        
        Args:
            source_text: Source text for patterns
            consciousness_level: Desired consciousness level
            length: Length of text to generate
            add_punctuation: Whether to add punctuation
            
        Returns:
            Generated text with target consciousness
        """
        if consciousness_level not in self.consciousness_levels:
            raise ValueError(f"Invalid consciousness level: {consciousness_level}")
        
        # Get consciousness band
        band = self.consciousness_levels[consciousness_level]['band']
        phi = float(self.core.PHI)
        
        # Generate initial frequencies from source text
        freqs = []
        for c in source_text:
            if c in self.letter_frequencies:
                base_freq = float(self.letter_frequencies[c])
                # Apply consciousness band modulation
                freq = (
                    base_freq * float(band['base']) + 
                    base_freq * float(band['resonance']) * phi + 
                    base_freq * float(band['harmony']) * phi**2
                ) / (1 + phi + phi**2)  # Normalize by phi series
                freqs.append(freq)
        
        # Apply quantum modulation based on consciousness level
        modulated_freqs = []
        for freq in freqs:
            # Calculate quantum phase using phi-harmonic series
            phase = freq * phi * np.pi
            
            # Apply consciousness-specific modulation
            if consciousness_level == 'physical':
                # Physical: Base frequency with minimal modulation
                mod_freq = freq * (1 + 0.1 * np.sin(phase))
            elif consciousness_level == 'emotional':
                # Emotional: Enhanced resonance with phi harmonics
                mod_freq = freq * (1 + 0.3 * np.sin(phase * phi))
            elif consciousness_level == 'mental':
                # Mental: Complex interference patterns
                mod_freq = freq * (1 + 0.5 * np.sin(phase * phi**2))
            elif consciousness_level == 'intuitive':
                # Intuitive: Multiple harmonic layers
                mod_freq = freq * (1 + 0.7 * (np.sin(phase * phi) + np.sin(phase * phi**2))/2)
            else:  # cosmic
                # Cosmic: Full quantum resonance
                mod_freq = freq * (1 + 0.9 * (np.sin(phase * phi) + np.sin(phase * phi**2) + np.sin(phase * phi**3))/3)
            
            modulated_freqs.append(mod_freq)
        
        # Generate text with modulated frequencies
        text = self.generate_from_frequencies(modulated_freqs[:length], add_punctuation)
        
        # Ensure text meets consciousness targets
        metrics = self.frequency_processor.analyze_frequency_pattern(text)
        max_iterations = 10
        
        for _ in range(max_iterations):
            if (metrics['phi_alignment'] >= self.consciousness_levels[consciousness_level]['phi_alignment'] and
                metrics['resonance'] >= self.consciousness_levels[consciousness_level]['resonance']):
                break
                
            # Adjust frequencies based on metrics
            adjustment = (1 + (self.consciousness_levels[consciousness_level]['phi_alignment'] - 
                             metrics['phi_alignment']) * phi)
            
            # Apply adjustment and regenerate
            adjusted_freqs = [f * adjustment for f in modulated_freqs]
            text = self.generate_from_frequencies(adjusted_freqs[:length], add_punctuation)
            metrics = self.frequency_processor.analyze_frequency_pattern(text)
        
        return text
    
    def generate_with_meta_learning(self, 
                                  sources: List[str], 
                                  weights: Optional[List[float]] = None,
                                  length: int = 100,
                                  consciousness_level: str = 'mental') -> str:
        """
        Generate text using multiple source patterns with meta-learning.
        
        Args:
            sources: List of source texts
            weights: Optional weights for each source
            length: Length of text to generate
            consciousness_level: Consciousness level to apply
            
        Returns:
            Generated text with meta-learned patterns
        """
        if not sources:
            return ""
        
        if weights is None:
            # Use phi-weighted distribution
            phi = float(self.core.PHI)
            weights = [phi**i for i in range(len(sources))]
            weights = [w/sum(weights) for w in weights]
        
        # Generate base frequencies from each source
        source_freqs = []
        for source, weight in zip(sources, weights):
            # Get frequencies with consciousness modulation
            text = self.generate_with_consciousness(
                source, consciousness_level, length=length
            )
            freqs = []
            for c in text:
                if c in self.letter_frequencies:
                    freq = float(self.letter_frequencies[c])
                    freqs.append(freq * weight)
            source_freqs.extend(freqs)
        
        if not source_freqs:
            return ""
        
        # Apply quantum meta-learning
        phi = float(self.core.PHI)
        meta_freqs = []
        
        for i in range(length):
            # Calculate meta-frequency using phi-harmonic superposition
            meta_freq = sum(
                freq * np.exp(2j * np.pi * phi**(k+1))
                for k, freq in enumerate(source_freqs)
            )
            meta_freq = float(abs(meta_freq)) / len(source_freqs)
            
            # Apply consciousness modulation
            band = self.consciousness_levels[consciousness_level]['band']
            mod_freq = (
                meta_freq * float(band['base']) + 
                meta_freq * float(band['resonance']) * phi + 
                meta_freq * float(band['harmony']) * phi**2
            ) / (1 + phi + phi**2)
            
            meta_freqs.append(mod_freq)
        
        # Generate final text
        return self.generate_from_frequencies(meta_freqs)
    
    def generate_with_author_pattern(self, author: str, length: int = 100) -> str:
        """Generate text based on author's phi-harmonic pattern."""
        # Define author-specific patterns
        author_patterns = {
            "shakespeare": {
                "base_frequency": 1063.8558,
                "resonance": 0.8944,
                "frequency_mod": 2.6180,  # phi^2
                "consciousness": "cosmic",
                "bigrams": ["th", "he", "in", "nd", "to"],
                "trigrams": ["the", "ble", "ing", "not", "tha"],
                "seed_words": ["thou", "thy", "thee", "hath", "doth", "art", "shall", "upon", "hast", "mine"],
                "phrases": ["to be or not to be", "what light through yonder window", "all the world's a stage", "parting is such sweet sorrow"]
            },
            "einstein": {
                "base_frequency": 898.0705,
                "resonance": 0.7236,
                "frequency_mod": 1.6180,  # phi
                "consciousness": "cosmic",
                "bigrams": ["an", "er", "he", "st", "th"],
                "trigrams": ["the", "and", "can", "eri", "ien"],
                "seed_words": ["theory", "light", "energy", "mass", "space", "time", "quantum", "relative", "motion", "physics"],
                "phrases": ["energy equals mass", "speed of light", "space and time", "quantum mechanics", "general relativity"]
            },
            "austen": {
                "base_frequency": 513.1615,
                "resonance": 0.6180,
                "frequency_mod": 0.6180,  # 1/phi
                "consciousness": "cosmic",
                "bigrams": ["in", "th", "er", "ow", "le"],
                "trigrams": ["ing", "ver", "kno", "now", "man"],
                "seed_words": ["truth", "fortune", "marriage", "family", "society", "manner", "regard", "opinion", "sensible", "agreeable"],
                "phrases": ["it is a truth universally acknowledged", "in want of a wife", "pride and prejudice", "sense and sensibility"]
            },
            "poe": {
                "base_frequency": 517.1540,
                "resonance": 0.6987,
                "frequency_mod": 0.8090,  # sin(phi)
                "consciousness": "cosmic",
                "bigrams": ["in", "re", "er", "or", "ng"],
                "trigrams": ["ing", "app", "ppi", "pin", "ear"],
                "seed_words": ["nevermore", "midnight", "raven", "dreary", "weary", "shadow", "sorrow", "darkness", "chamber", "melancholy", 
                              "heart", "soul", "horror", "fear", "dread", "tomb", "grave", "death", "night", "black"],
                "phrases": ["once upon a midnight dreary", "quoth the raven nevermore", "deep into that darkness peering", 
                           "while I pondered weak and weary", "tapping at my chamber door", "nothing more", 
                           "in the shadow", "beating of his heart", "tell-tale heart", "bells, bells, bells"]
            }
        }
        
        # Get pattern for specified author
        pattern = author_patterns.get(author.lower(), author_patterns["shakespeare"])
        
        # Initialize text generation
        text_segments = []
        phi = float(self.core.PHI)
        
        # Start with a phrase or seed word for more natural text
        if self._phi_weighted_choice([True, False], [phi-1, 2-phi]) and pattern.get("phrases"):
            text_segments.append(self._phi_weighted_choice(pattern["phrases"]))
        else:
            text_segments.append(self._phi_weighted_choice(pattern["seed_words"]))
        
        # Generate text with author's pattern
        while sum(len(segment) for segment in text_segments) < length * 1.5:  # Generate more than needed so we can trim
            # Decide what to generate next based on phi-harmonic probabilities
            choice_type = self._phi_weighted_choice(
                ["letter", "bigram", "trigram", "seed_word", "phrase", "repetition"],
                [1/phi**4, 1/phi**3, 1/phi**2, 1/phi, 1, phi-1]  # Phi-weighted probabilities
            )
            
            if choice_type == "letter":
                # Generate a single letter based on frequency
                base_freq = pattern["base_frequency"]
                mod = pattern["frequency_mod"]
                current_len = sum(len(segment) for segment in text_segments)
                freq_mod = base_freq * (1 + (mod * (current_len % 8) / 10))
                
                letter_freqs = list(self.letter_frequencies.items())
                distances = [(abs(freq - freq_mod), letter) for letter, freq in letter_freqs]
                distances.sort()
                text_segments.append(distances[0][1])
                
            elif choice_type == "bigram" and pattern["bigrams"]:
                # Add a bigram from author's patterns
                text_segments.append(self._phi_weighted_choice(pattern["bigrams"]))
                
            elif choice_type == "trigram" and pattern["trigrams"]:
                # Add a trigram from author's patterns
                text_segments.append(self._phi_weighted_choice(pattern["trigrams"]))
                
            elif choice_type == "seed_word" and pattern["seed_words"]:
                # Add a seed word from author's vocabulary
                text_segments.append(" " + self._phi_weighted_choice(pattern["seed_words"]))
                
            elif choice_type == "phrase" and pattern.get("phrases"):
                # Add a phrase from author's patterns
                text_segments.append(" " + self._phi_weighted_choice(pattern["phrases"]))
                
            elif choice_type == "repetition" and text_segments:
                # Repeat a previous segment (especially important for Poe)
                # Get a random previous segment
                if len(text_segments) > 5:
                    segment_idx = int((len(text_segments) - 1) * ((phi - 1) % 1))
                    segment = text_segments[segment_idx]
                    
                    # For Poe, use his signature repetition style
                    if author.lower() == "poe":
                        if " " in segment:
                            # It's a word or phrase, use Poe's comma repetition
                            text_segments.append(", " + segment.strip())
                        else:
                            # It's a shorter segment, double or triple it
                            repeat_count = int(phi) % 3 + 1  # 1, 2, or 3
                            text_segments.append(segment * repeat_count)
                    else:
                        # For other authors, just repeat with a space
                        text_segments.append(" " + segment.strip())
            
            # Occasionally add punctuation for readability
            current_len = sum(len(segment) for segment in text_segments)
            if current_len % int(phi * 8) == 0:
                punctuation = self._phi_weighted_choice([".", ",", ";", "!", "?", "—"], 
                                                      [1/phi**2, 1/phi, 1, phi-1, (phi-1)**2, (phi-1)**3])
                text_segments.append(punctuation + " ")
            elif current_len % int(phi * 5) == 0:
                text_segments.append(" ")
        
        # Join segments and trim to exact length
        full_text = "".join(text_segments)
        
        # Clean up any double spaces or weird punctuation
        full_text = full_text.replace("  ", " ").replace(" ,", ",").replace(" .", ".")
        
        # For Poe specifically, ensure we have some of his signature elements
        if author.lower() == "poe" and "nevermore" not in full_text and len(full_text) > 50:
            insert_pos = int(len(full_text) * (phi - 1))
            full_text = full_text[:insert_pos] + " nevermore" + full_text[insert_pos:]
        
        return full_text[:length]
    
    def _phi_weighted_choice(self, choices, weights=None):
        """Make a phi-weighted random choice from a list of options."""
        if weights is None:
            # Use phi-weighted distribution if no weights provided
            phi = float(self.core.PHI)
            weights = [phi ** (i % 3) for i in range(len(choices))]
            
        # Normalize weights
        total = sum(weights)
        weights = [w/total for w in weights]
        
        # Cumulative distribution
        cum_weights = [sum(weights[:i+1]) for i in range(len(weights))]
        
        # Generate phi-harmonic random value
        phi_seed = (float(self.core.PHI) * len(choices)) % 1
        r = (phi_seed + sum(cum_weights) / len(cum_weights)) % 1
        
        # Find the choice
        for i, cw in enumerate(cum_weights):
            if r <= cw:
                return choices[i]
                
        return choices[-1]  # Fallback
    
    def test_author_patterns(self) -> Dict[str, Any]:
        """
        Test generation with different author patterns.
        
        Returns:
            Dictionary with test results
        """
        results = {}
        
        # Test each author
        for author in self.author_patterns:
            # Generate sample text
            text = self.generate_with_author_pattern(author, length=50)
            
            # Calculate metrics
            freqs = []
            for c in text:
                if c in self.letter_frequencies:
                    freq = float(self.letter_frequencies[c])
                    freqs.append(freq)
            
            if freqs:
                avg_freq = sum(freqs) / len(freqs)
                pattern = self.author_patterns[author]
                
                results[author] = {
                    'text': text,
                    'length': len(text),
                    'resonance': float(pattern['resonance']),
                    'avg_frequency': float(avg_freq),
                    'frequency_mod': float(pattern['frequency_mod'])
                }
        
        return results
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current generator metrics."""
        return {
            'pattern_windows': self.pattern_windows,
            'consciousness_levels': list(self.consciousness_levels.keys()),
            'frequency_range': (
                min(self.letter_frequencies.values()),
                max(self.letter_frequencies.values())
            )
        }
