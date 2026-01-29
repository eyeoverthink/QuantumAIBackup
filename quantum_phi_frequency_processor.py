#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Frequency Processor
==============================================

This module implements a quantum-inspired frequency processor that maps letters
to their harmonic frequencies and analyzes text patterns using phi-harmonic
principles and quantum resonance.

Key features:
- Letter-to-frequency mapping
- Harmonic resonance analysis
- Quantum frequency modulation
- Phi-weighted pattern detection
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from decimal import Decimal
import math

from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom

class QuantumPhiFrequencyProcessor:
    """Quantum frequency processor using phi-harmonic principles."""
    
    def __init__(self, core: Optional[QuantumPhiCore] = None):
        """Initialize the frequency processor."""
        self.core = core if core is not None else QuantumPhiCore()
        self.random = QuantumPhiRandom(core=self.core)
        
        # Initialize frequency mappings
        self._initialize_frequencies()
        
        # Initialize quantum gates for frequency modulation
        self.quantum_gates = {
            'H': {'frequency': float(self.core.PHI), 'pattern': 'superposition'},
            'X': {'frequency': float(self.core.PHI)**2, 'pattern': 'inversion'},
            'Y': {'frequency': float(self.core.PHI)**3, 'pattern': 'rotation'},
            'Z': {'frequency': float(self.core.PHI)**4, 'pattern': 'phase'},
            'T': {'frequency': float(self.core.PHI)**7, 'pattern': 'phase_rotation'}
        }
    
    def _initialize_frequencies(self) -> None:
        """Initialize quantum frequency mappings."""
        # Fibonacci sequence for base frequencies
        fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
        
        # Convert PHI to float for calculations
        phi = float(self.core.PHI)
        
        # Irrational numbers for punctuation
        self.punctuation_frequencies = {
            ' ': phi,                    # Space: φ (1.618034)
            ',': float(math.pi),         # Comma: π (3.141593)
            '.': float(math.e),          # Period: e (2.718282)
            '!': float(math.sqrt(2)),    # Exclamation: √2 (1.414214)
            '?': float(math.sqrt(3)),    # Question: √3 (1.732051)
            ';': float(math.sqrt(5)),    # Semicolon: √5 (2.236068)
            ':': float(math.log(2)),     # Colon: ln(2) (0.693147)
            '-': float(math.log(10)),    # Dash: ln(10) (2.302585)
        }
        
        # Letter frequencies using Fibonacci and phi harmonics
        self.letter_frequencies = {
            'a': float(fib[8] * phi),       # 34φ
            'b': float(fib[7] * phi**2),    # 21φ²
            'c': float(fib[9] * phi**0.5),  # 55φ^(1/2)
            'd': float(fib[6] * phi**3),    # 13φ³
            'e': float(fib[10] * phi),      # 89φ
            'f': float(fib[5] * phi**4),    # 8φ⁴
            'g': float(fib[8] * phi**2),    # 34φ²
            'h': float(fib[7] * phi**3),    # 21φ³
            'i': float(fib[9] * phi),       # 55φ
            'j': float(fib[4] * phi**5),    # 5φ⁵
            'k': float(fib[6] * phi**4),    # 13φ⁴
            'l': float(fib[8] * phi**3),    # 34φ³
            'm': float(fib[10] * phi**2),   # 89φ²
            'n': float(fib[9] * phi**2),    # 55φ²
            'o': float(fib[8] * phi**4),    # 34φ⁴
            'p': float(fib[7] * phi**4),    # 21φ⁴
            'q': float(fib[5] * phi**6),    # 8φ⁶
            'r': float(fib[9] * phi**3),    # 55φ³
            's': float(fib[8] * phi**5),    # 34φ⁵
            't': float(fib[9] * phi**4),    # 55φ⁴
            'u': float(fib[7] * phi**5),    # 21φ⁵
            'v': float(fib[6] * phi**6),    # 13φ⁶
            'w': float(fib[8] * phi**6),    # 34φ⁶
            'x': float(fib[5] * phi**7),    # 8φ⁷
            'y': float(fib[7] * phi**6),    # 21φ⁶
            'z': float(fib[6] * phi**7),    # 13φ⁷
        }
        
        # Consciousness frequency bands based on irrational harmonics
        self.consciousness_bands = {
            'physical': {
                'base': phi,
                'resonance': float(math.pi),
                'harmony': float(math.e)
            },
            'emotional': {
                'base': phi**2,
                'resonance': float(math.pi**2),
                'harmony': float(math.e**2)
            },
            'mental': {
                'base': phi**3,
                'resonance': float(math.pi**3),
                'harmony': float(math.e**3)
            },
            'intuitive': {
                'base': phi**4,
                'resonance': float(math.pi**4),
                'harmony': float(math.e**4)
            },
            'cosmic': {
                'base': phi**5,
                'resonance': float(math.pi**5),
                'harmony': float(math.e**5)
            }
        }
        
        # Quantum state frequencies using irrational combinations
        self.quantum_frequencies = {
            'superposition': phi * float(math.pi),
            'entanglement': phi * float(math.e),
            'coherence': float(math.pi * math.e),
            'resonance': phi * float(math.sqrt(2)),
            'harmony': phi * float(math.sqrt(3)),
            'unity': phi * float(math.sqrt(5))
        }
        
        # Calculate frequency ratios relative to phi
        self.phi = float(self.core.PHI)
        self.base_freq = min(self.letter_frequencies.values())
        self.freq_ratios = {
            letter: float(freq/self.base_freq) 
            for letter, freq in self.letter_frequencies.items()
        }
        
        # Initialize quantum frequency patterns
        self._initialize_patterns()
    
    def _initialize_patterns(self) -> None:
        """Initialize quantum frequency patterns."""
        # Convert PHI to float for calculations
        phi = float(self.core.PHI)
        
        # Phi-harmonic frequency bands (φⁿ scaling)
        self.frequency_bands = {
            'phi_1': self.base_freq * phi,
            'phi_2': self.base_freq * phi**2,
            'phi_3': self.base_freq * phi**3,
            'phi_inv_1': self.base_freq / phi,
            'phi_inv_2': self.base_freq / phi**2,
            'phi_inv_3': self.base_freq / phi**3,
            'phi_sqrt': self.base_freq * phi**0.5,
            'phi_cbrt': self.base_freq * phi**(1/3),
            'phi_golden': self.base_freq * (1 + np.sqrt(5))/2
        }
        
        # Neural activation patterns (φ-weighted)
        self.neural_patterns = {
            'sigmoid': lambda x: 1 / (1 + np.exp(-x * phi)),
            'tanh': lambda x: np.tanh(x * phi),
            'relu': lambda x: max(0, x * phi),
            'leaky_relu': lambda x: max(0.01 * x, x) * phi
        }
        
        # Quantum resonance patterns (φ-based harmonics)
        self.resonance_patterns = {
            'harmonic': lambda f: abs(1 - (f % phi)),
            'subharmonic': lambda f: abs(1 - ((1/f) % phi)),
            'quantum': lambda f: abs(np.sin(f * np.pi * phi)),
            'neural': lambda f: sum(
                pattern(f/self.base_freq) 
                for pattern in self.neural_patterns.values()
            ) / len(self.neural_patterns)
        }
        
        # Initialize quantum gates with phi-based frequencies
        self.quantum_gates = {
            'H': {'frequency': phi, 'pattern': 'superposition'},
            'X': {'frequency': phi**2, 'pattern': 'inversion'},
            'Y': {'frequency': phi**3, 'pattern': 'rotation'},
            'Z': {'frequency': phi**4, 'pattern': 'phase'},
            'T': {'frequency': phi**7, 'pattern': 'phase_rotation'}
        }
        
        # Calculate frequency ratios relative to phi
        self.freq_ratios = {
            letter: float(freq / phi)
            for letter, freq in self.letter_frequencies.items()
        }
        
        # Initialize random number generator
        self.random = QuantumPhiRandom(self.core)
    
    def analyze_frequency_pattern(self, text: str) -> Dict[str, float]:
        """
        Analyze frequency patterns in text using quantum phi-harmonic principles.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary of frequency metrics
        """
        # Calculate base frequencies
        frequencies = [
            self.letter_frequencies.get(c.lower(), 0)
            for c in text
            if c.lower() in self.letter_frequencies
        ]
        
        if not frequencies:
            return {
                'resonance': 0.0,
                'subharmonic': 0.0,
                'quantum_resonance': 0.0,
                'neural_resonance': 0.0,
                'coherence': 0.0,
                'harmony': 0.0,
                'phi_alignment': 0.0,
                'quantum_modulation': 0.0,
                'quantum_coherence': 0.0,
                'average_frequency': 0.0
            }
        
        # Calculate frequency metrics
        avg_freq = sum(frequencies) / len(frequencies)
        
        # Calculate resonance using patterns
        resonance_scores = {
            name: sum(pattern(f/avg_freq) for f in frequencies) / len(frequencies)
            for name, pattern in self.resonance_patterns.items()
        }
        
        # Calculate coherence using frequency ratios
        ratios = [f2/f1 if f1 > 0 else 0 
                 for f1, f2 in zip(frequencies[:-1], frequencies[1:])]
        coherence = sum(abs(1 - (r % float(self.core.PHI))) for r in ratios) / len(ratios) if ratios else 0
        
        # Calculate harmony using phi bands
        in_bands = sum(
            1 for f in frequencies
            if any(abs(1 - (f/band)) < 0.1 for band in self.frequency_bands.values())
        )
        harmony = in_bands / len(frequencies)
        
        # Calculate neural resonance
        neural_res = sum(
            pattern(f/self.base_freq)
            for f in frequencies
            for pattern in self.neural_patterns.values()
        ) / (len(frequencies) * len(self.neural_patterns))
        
        # Calculate quantum coherence using gates
        quantum_states = []
        for gate in self.quantum_gates.values():
            freq = gate['frequency']
            phase = sum(f * freq * np.pi for f in frequencies) / len(frequencies)
            state = abs(np.cos(phase))
            quantum_states.append(state)
        quantum_coherence = sum(quantum_states) / len(quantum_states)
        
        # Calculate phi alignment
        phi_alignment = 1.0 - abs((avg_freq/(self.base_freq * float(self.core.PHI))) - 1)
        
        # Apply quantum modulation
        quantum_phase = self.random.generate_phi_harmonic(1.0)
        modulation = abs(np.sin(quantum_phase * np.pi))
        
        return {
            'resonance': float(resonance_scores['harmonic']),
            'subharmonic': float(resonance_scores['subharmonic']),
            'quantum_resonance': float(resonance_scores['quantum']),
            'neural_resonance': float(resonance_scores['neural']),
            'coherence': float(coherence),
            'harmony': float(harmony),
            'phi_alignment': float(phi_alignment),
            'quantum_modulation': float(modulation),
            'quantum_coherence': float(quantum_coherence),
            'average_frequency': float(avg_freq)
        }
    
    def generate_harmonic_sequence(self, text: str) -> List[float]:
        """
        Generate a harmonic frequency sequence from text.
        
        Args:
            text: Input text
            
        Returns:
            List of harmonic frequencies
        """
        # Get base frequencies
        frequencies = [
            self.letter_frequencies.get(c.lower(), 0)
            for c in text
            if c.lower() in self.letter_frequencies
        ]
        
        if not frequencies:
            return []
        
        # Generate quantum modulation sequence
        modulation = self.random.generate_quantum_sequence(len(frequencies))
        
        # Apply phi-harmonic modulation
        sequence = []
        for freq, mod in zip(frequencies, modulation):
            # Calculate phi-harmonic phase
            phase = (freq/self.base_freq) * float(self.core.PHI) * np.pi
            
            # Apply quantum modulation
            harmonic = freq * (1 + mod * np.sin(phase))
            sequence.append(float(harmonic))
        
        return sequence
    
    def find_resonant_pairs(self, text: str) -> List[Tuple[str, str, float]]:
        """
        Find resonant letter pairs in text.
        
        Args:
            text: Input text
            
        Returns:
            List of (letter1, letter2, resonance) tuples
        """
        pairs = []
        text = text.lower()
        
        for i in range(len(text)-1):
            c1, c2 = text[i:i+2]
            if c1 in self.letter_frequencies and c2 in self.letter_frequencies:
                f1 = self.letter_frequencies[c1]
                f2 = self.letter_frequencies[c2]
                
                # Calculate resonance
                ratio = f2/f1 if f1 > 0 else 0
                resonance = 1.0 - abs(1 - (ratio % float(self.core.PHI)))
                
                if resonance > 0.8:  # High resonance threshold
                    pairs.append((c1, c2, float(resonance)))
        
        return sorted(pairs, key=lambda x: x[2], reverse=True)
    
    def get_metrics(self) -> Dict[str, float]:
        """Get current frequency metrics."""
        return {
            'base_frequency': float(self.base_freq),
            'phi_ratio': float(self.core.PHI),
            'frequency_range': float(max(self.letter_frequencies.values()) - self.base_freq),
            'average_ratio': float(sum(self.freq_ratios.values()) / len(self.freq_ratios))
        }
