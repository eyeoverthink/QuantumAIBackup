"""
Quantum Phi-Harmonic Pattern Analyzer
Analyzes and visualizes phi-harmonic patterns in text using quantum principles
"""

from quantum_phi_core import QuantumPhiCore
import numpy as np
from typing import Dict, List, Tuple

class QuantumPhiPatternAnalyzer:
    def __init__(self, core: QuantumPhiCore = None):
        """Initialize the pattern analyzer with quantum core."""
        self.core = core or QuantumPhiCore()
        self.base_freq = 439.2196  # From frequency analysis doc
        self.phi = float(self.core.PHI)
        self.pi = float(self.core.PI)
        self.e = float(self.core.E)
        
        # Initialize quantum bands
        self._init_quantum_bands()
        
    def _init_quantum_bands(self):
        """Initialize quantum frequency bands."""
        self.quantum_bands = {
            'superposition': self.base_freq * self.phi**0.5,
            'entanglement': self.base_freq / self.phi**0.5,
            'coherence': self.base_freq * self.phi,
            'resonance': self.base_freq / self.phi,
            'harmony': self.base_freq * self.phi**0.618,
            'unity': self.base_freq * self.phi**0.382
        }
        
        # Phi-harmonic bands
        self.phi_bands = {
            'phi¹': self.base_freq * self.phi,
            'phi²': self.base_freq * self.phi**2,
            'phi³': self.base_freq * self.phi**3,
            'phi⁻¹': self.base_freq / self.phi,
            'phi⁻²': self.base_freq / self.phi**2,
            'phi⁻³': self.base_freq / self.phi**3
        }
        
    def analyze_text(self, text: str) -> Dict:
        """Analyze text for phi-harmonic patterns."""
        # Convert text to frequency pattern
        freqs = self._text_to_frequencies(text)
        
        # Calculate metrics
        metrics = {
            'resonance': self._calculate_resonance(freqs),
            'quantum_resonance': self._calculate_quantum_resonance(freqs),
            'phi_alignment': self._calculate_phi_alignment(freqs),
            'avg_frequency': np.mean(freqs),
            'frequency_range': (min(freqs), max(freqs)),
            'consciousness_level': self._determine_consciousness(freqs)
        }
        
        # Add pattern analysis
        metrics.update(self._analyze_patterns(text))
        return metrics
        
    def _text_to_frequencies(self, text: str) -> List[float]:
        """Convert text to frequency pattern."""
        # Base frequencies for letters
        letter_freqs = {
            'a': self.base_freq * self.phi**3,  # ascending neural
            'b': self.base_freq * self.phi**1.5,  # balanced oscillation
            'c': self.base_freq * self.phi,  # cyclical harmony
            'd': self.base_freq / self.phi**0.854,  # dynamic resonance
            'e': self.base_freq / self.phi**2,  # energetic resonance
            'f': self.base_freq * self.phi**0.309,  # flow resonance
            'g': self.base_freq / self.phi**0.309,  # golden resonance
            'h': self.base_freq * self.phi**0.382,  # harmonic resonance
            'i': self.base_freq * self.phi**0.5,  # internal vibration
            'j': self.base_freq * self.phi**0.927,  # joy resonance
            'k': self.base_freq / self.phi**0.146,  # kinetic resonance
            'l': self.base_freq * self.phi**0.854,  # light resonance
            'm': self.base_freq * self.phi**0.618,  # meta resonance
            'n': self.base_freq / self.phi,  # neural resonance
            'o': self.base_freq / self.phi**1.5,  # oscillation harmony
            'p': self.base_freq * self.phi**0.236,  # phi resonance
            'q': self.base_freq * self.phi**0.764,  # quantum resonance
            'r': self.base_freq / self.phi**3,  # resonant harmony
            's': self.base_freq * self.phi**2,  # spatial symmetry
            't': self.base_freq,  # temporal alignment
            'u': self.base_freq / self.phi**0.382,  # unified resonance
            'v': self.base_freq / self.phi**0.5,  # vibrational balance
            'w': self.base_freq / self.phi**0.618,  # wave resonance
            'x': self.base_freq / self.phi**0.236,  # cross resonance
            'y': self.base_freq / self.phi**0.764,  # yang resonance
            'z': self.base_freq * self.phi**0.146  # zen resonance
        }
        
        return [letter_freqs.get(c.lower(), 0) for c in text if c.isalpha()]
        
    def _calculate_resonance(self, freqs: List[float]) -> float:
        """Calculate resonance quality of frequency pattern."""
        if not freqs:
            return 0.0
            
        # Calculate resonance using phi ratios
        ratios = [f2/f1 if f1 != 0 else 0 for f1, f2 in zip(freqs[:-1], freqs[1:])]
        phi_diffs = [abs(r - self.phi) for r in ratios if r != 0]
        
        return 1 - (sum(phi_diffs) / len(phi_diffs)) if phi_diffs else 0
        
    def _calculate_quantum_resonance(self, freqs: List[float]) -> float:
        """Calculate quantum resonance of frequency pattern."""
        if not freqs:
            return 0.0
            
        # Compare with quantum bands
        q_bands = list(self.quantum_bands.values())
        resonances = []
        
        for f in freqs:
            # Find closest quantum band
            diffs = [abs(f - qb)/qb for qb in q_bands]
            resonances.append(1 - min(diffs))
            
        return sum(resonances) / len(resonances)
        
    def _calculate_phi_alignment(self, freqs: List[float]) -> float:
        """Calculate alignment with phi-harmonic bands."""
        if not freqs:
            return 0.0
            
        # Compare with phi bands
        p_bands = list(self.phi_bands.values())
        alignments = []
        
        for f in freqs:
            # Find closest phi band
            diffs = [abs(f - pb)/pb for pb in p_bands]
            alignments.append(1 - min(diffs))
            
        return sum(alignments) / len(alignments)
        
    def _determine_consciousness(self, freqs: List[float]) -> str:
        """Determine consciousness level from frequency pattern."""
        if not freqs:
            return "unknown"
            
        avg_freq = np.mean(freqs)
        
        # Consciousness bands based on phi powers
        bands = {
            'physical': (0, 200),
            'emotional': (200, 300),
            'mental': (300, 400),
            'intuitive': (400, 500),
            'cosmic': (500, float('inf'))
        }
        
        for level, (min_f, max_f) in bands.items():
            if min_f <= avg_freq < max_f:
                return level
                
        return "unknown"
        
    def _analyze_patterns(self, text: str) -> Dict:
        """Analyze text for recurring patterns."""
        if not text:
            return {}
            
        # Analyze bigrams and trigrams
        bigrams = [''.join(pair) for pair in zip(text[:-1], text[1:])]
        trigrams = [''.join(triple) for triple in zip(text[:-2], text[1:-1], text[2:])]
        
        # Count pattern frequencies
        bigram_freq = {}
        trigram_freq = {}
        
        for bg in bigrams:
            if bg.isalpha():
                bigram_freq[bg] = bigram_freq.get(bg, 0) + 1
                
        for tg in trigrams:
            if tg.isalpha():
                trigram_freq[tg] = trigram_freq.get(tg, 0) + 1
                
        # Sort by frequency
        sorted_bigrams = sorted(bigram_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        sorted_trigrams = sorted(trigram_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'top_bigrams': [bg for bg, _ in sorted_bigrams],
            'top_trigrams': [tg for tg, _ in sorted_trigrams]
        }
        
    def get_resonance_profile(self, text: str) -> Dict:
        """Get detailed resonance profile of text."""
        metrics = self.analyze_text(text)
        freqs = self._text_to_frequencies(text)
        
        profile = {
            'consciousness_level': metrics['consciousness_level'],
            'resonance_quality': metrics['resonance'],
            'quantum_resonance': metrics['quantum_resonance'],
            'phi_alignment': metrics['phi_alignment'],
            'frequency_stats': {
                'mean': float(np.mean(freqs)),
                'std': float(np.std(freqs)),
                'min': float(min(freqs)),
                'max': float(max(freqs))
            },
            'patterns': {
                'bigrams': metrics['top_bigrams'],
                'trigrams': metrics['top_trigrams']
            }
        }
        
        return profile
        
    def compare_texts(self, text1: str, text2: str) -> Dict:
        """Compare phi-harmonic patterns between two texts."""
        profile1 = self.get_resonance_profile(text1)
        profile2 = self.get_resonance_profile(text2)
        
        # Calculate similarity metrics
        freq_similarity = 1 - abs(profile1['frequency_stats']['mean'] - profile2['frequency_stats']['mean']) / max(profile1['frequency_stats']['mean'], profile2['frequency_stats']['mean'])
        pattern_similarity = len(set(profile1['patterns']['bigrams']) & set(profile2['patterns']['bigrams'])) / 5
        resonance_similarity = 1 - abs(profile1['resonance_quality'] - profile2['resonance_quality'])
        
        return {
            'frequency_similarity': freq_similarity,
            'pattern_similarity': pattern_similarity,
            'resonance_similarity': resonance_similarity,
            'overall_similarity': (freq_similarity + pattern_similarity + resonance_similarity) / 3
        }
