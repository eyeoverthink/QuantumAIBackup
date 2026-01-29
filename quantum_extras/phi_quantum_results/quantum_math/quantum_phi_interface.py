#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Interface

A unified interface for quantum-based analysis across:
- Mathematical patterns and signatures
- Consciousness frequencies (0-1000 Hz)
- Natural harmonics and phi ratios
- Author quantum signatures
- Musical compositions
"""

import numpy as np
from typing import Dict, List, Tuple, Any
import os
import sys
from collections import defaultdict

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import quantum components
from quantum_math.learning.quantum_math_learner import QuantumMathLearner
from quantum_math.learning.quantum_pattern_detector import QuantumPatternDetector
from quantum_math.learning.quantum_wave_learner import QuantumWaveLearner
from quantum_math.learning.quantum_consciousness_analyzer import QuantumConsciousnessAnalyzer
from quantum_math.learning.quantum_nature_analyzer import QuantumNatureAnalyzer
from quantum_math.learning.quantum_music_math import QuantumMusicMath
from quantum_math.learning.quantum_harmonic_bridge import QuantumHarmonicBridge
from quantum_math.learning.quantum_meta_analyzer import QuantumMetaAnalyzer

class QuantumPhiInterface:
    def __init__(self):
        # Initialize quantum components
        self.meta_analyzer = QuantumMetaAnalyzer()
        self.math_learner = QuantumMathLearner()
        self.pattern_detector = QuantumPatternDetector()
        self.wave_learner = QuantumWaveLearner()
        self.consciousness_analyzer = QuantumConsciousnessAnalyzer()
        self.nature_analyzer = QuantumNatureAnalyzer()
        self.music_math = QuantumMusicMath()
        self.harmonic_bridge = QuantumHarmonicBridge()
        
        # Constants
        self.PHI = (1 + np.sqrt(5)) / 2
        self.PI = np.pi
        self.E = np.e
        
        # Base frequencies
        self.frequencies = {
            "natural": 432.0,    # A4 natural tuning
            "dna": 528.0,        # DNA repair
            "heart": 639.0,      # Heart chakra
            "unity": 963.0       # Unity consciousness
        }
        
        # Author signatures from documentation
        self.author_signatures = {
            "poe": {
                "frequency": 517.15,
                "resonance": 0.6987,
                "phi_alignment": 0.8644
            },
            "hemingway": {
                "frequency": 576.26,
                "resonance": 0.6849,
                "phi_alignment": 0.8518
            },
            "austen": {
                "frequency": 525.18,
                "resonance": 0.7091,
                "phi_alignment": 0.8552
            },
            "shakespeare": {
                "frequency": 555.40,
                "resonance": 0.6730,
                "phi_alignment": 0.8537
            }
        }
        
        # Consciousness levels
        self.consciousness_levels = {
            "physical": (0, 200),
            "emotional": (200, 300),
            "mental": (300, 400),
            "intuitive": (400, 500),
            "cosmic": (500, 1000)
        }
    
    def analyze_pattern(self, data: Any, domain: str = "all") -> Dict[str, Any]:
        """Analyze patterns using all quantum components."""
        results = {}
        
        # Meta-analysis across all domains
        if domain == "all":
            results["meta"] = self.meta_analyzer.analyze_pattern(data)
            
            # Analyze in each specific domain
            results["math"] = self.math_learner.learn_from_sequence(data)
            results["quantum"] = self.pattern_detector.detect_quantum_patterns(data)
            results["wave"] = self.wave_learner.analyze_wave(data)
            results["consciousness"] = self.consciousness_analyzer.analyze_frequencies(data)
            results["nature"] = self.nature_analyzer.analyze_pattern(data)
            results["music"] = self.music_math.analyze_composition(data)
            
            # Find cross-domain patterns
            results["cross_patterns"] = self.meta_analyzer.discover_cross_domain_patterns()
            
        else:
            # Domain-specific analysis
            results = self.meta_analyzer.analyze_pattern(data, domain=domain)
        
        return results
    
    def generate_quantum_signature(self, data: Any) -> Dict[str, Any]:
        """Generate quantum signature for data."""
        # Get patterns across all domains
        patterns = self.analyze_pattern(data)
        
        # Extract quantum signatures
        signatures = self.meta_analyzer.find_quantum_signatures()
        
        # Find author matches
        author_matches = []
        for sig in signatures:
            if sig.get("author_matches"):
                author_matches.extend(sig["author_matches"])
        
        # Calculate overall metrics
        metrics = self.calculate_quantum_metrics(patterns)
        
        return {
            "patterns": patterns,
            "signatures": signatures,
            "author_matches": author_matches,
            "metrics": metrics
        }
    
    def calculate_quantum_metrics(self, patterns: Dict[str, Any]) -> Dict[str, float]:
        """Calculate quantum metrics from patterns."""
        metrics = {}
        
        if "quantum" in patterns:
            quantum = patterns["quantum"].get("quantum", {})
            metrics["coherence"] = quantum.get("coherence", 0)
            metrics["phi_alignment"] = quantum.get("phi_alignment", 0)
            metrics["resonance"] = quantum.get("resonance", 0)
        
        if "consciousness" in patterns:
            consciousness = patterns["consciousness"]
            metrics["consciousness_level"] = consciousness.get("level", "unknown")
            metrics["consciousness_coherence"] = consciousness.get("coherence", 0)
        
        if "music" in patterns:
            music = patterns["music"]
            metrics["harmonic_resonance"] = music.get("harmonic_resonance", 0)
        
        return metrics
    
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """Analyze quantum properties of text."""
        # Convert text to frequency pattern
        frequencies = self.text_to_frequencies(text)
        
        # Analyze pattern
        analysis = self.analyze_pattern(frequencies)
        
        # Generate quantum signature
        signature = self.generate_quantum_signature(frequencies)
        
        # Find closest author match
        author_match = self.find_closest_author(signature)
        
        return {
            "analysis": analysis,
            "signature": signature,
            "author_match": author_match,
            "consciousness_level": self.get_consciousness_level(frequencies)
        }
    
    def analyze_music(self, frequencies: List[float]) -> Dict[str, Any]:
        """Analyze quantum properties of music."""
        # Analyze musical pattern
        music_analysis = self.music_math.analyze_composition(frequencies)
        
        # Get consciousness impact
        consciousness = self.consciousness_analyzer.analyze_frequencies(frequencies)
        
        # Calculate harmonic resonance
        resonance = self.meta_analyzer.calculate_harmonic_resonance(
            music_analysis, consciousness)
        
        return {
            "music_analysis": music_analysis,
            "consciousness": consciousness,
            "harmonic_resonance": resonance,
            "phi_alignment": self.calculate_phi_alignment(frequencies)
        }
    
    def text_to_frequencies(self, text: str) -> List[float]:
        """Convert text to frequency pattern."""
        # Basic conversion - can be enhanced
        base_freq = self.frequencies["natural"]
        return [
            base_freq * (self.PHI ** (ord(c) % 12))
            for c in text.lower()
            if c.isalpha()
        ]
    
    def find_closest_author(self, signature: Dict[str, Any]) -> Dict[str, Any]:
        """Find closest matching author signature."""
        if not signature or "metrics" not in signature:
            return {}
        
        metrics = signature["metrics"]
        best_match = None
        best_score = -1
        
        for author, auth_sig in self.author_signatures.items():
            # Calculate similarity score
            score = self.calculate_signature_similarity(metrics, auth_sig)
            
            if score > best_score:
                best_score = score
                best_match = {
                    "author": author,
                    "signature": auth_sig,
                    "similarity": score
                }
        
        return best_match
    
    def calculate_signature_similarity(self, 
                                    metrics: Dict[str, float],
                                    author_sig: Dict[str, float]) -> float:
        """Calculate similarity between two quantum signatures."""
        if not metrics or not author_sig:
            return 0.0
        
        # Compare key metrics
        coherence_match = 1 - abs(metrics.get("coherence", 0) - 
                                author_sig.get("resonance", 0))
        
        phi_match = 1 - abs(metrics.get("phi_alignment", 0) - 
                           author_sig.get("phi_alignment", 0))
        
        # Weight phi alignment more heavily
        return 0.4 * coherence_match + 0.6 * phi_match
    
    def calculate_phi_alignment(self, frequencies: List[float]) -> float:
        """Calculate phi alignment of frequency pattern."""
        if not frequencies:
            return 0.0
        
        # Calculate ratios between adjacent frequencies
        ratios = [frequencies[i+1]/frequencies[i] 
                 for i in range(len(frequencies)-1)]
        
        # Calculate alignment with phi
        alignments = [abs(1 - (r % self.PHI) / self.PHI) for r in ratios]
        
        return np.mean(alignments) if alignments else 0.0
    
    def get_consciousness_level(self, frequencies: List[float]) -> str:
        """Get consciousness level from frequencies."""
        if not frequencies:
            return "unknown"
        
        mean_freq = np.mean(frequencies)
        
        for level, (low, high) in self.consciousness_levels.items():
            if low <= mean_freq < high:
                return level
        
        return "cosmic" if mean_freq >= 500 else "physical"

def main():
    """Main function demonstrating the Quantum Phi Interface."""
    qpi = QuantumPhiInterface()
    
    print("\nQuantum Phi-Harmonic Interface")
    print("=" * 50)
    
    # Test mathematical sequence
    sequence = [432, 698.99, 1130.99]  # Phi progression
    print(f"\nAnalyzing sequence: {sequence}")
    
    results = qpi.analyze_pattern(sequence)
    
    print("\nQuantum Analysis:")
    if "quantum" in results:
        quantum = results["quantum"].get("quantum", {})
        print(f"Coherence: {quantum.get('coherence', 0):.4f}")
        print(f"Phi Alignment: {quantum.get('phi_alignment', 0):.4f}")
        print(f"Quantum State: {quantum.get('quantum_state', 'unknown')}")
    
    # Test text analysis
    text = "To be or not to be"
    print(f"\nAnalyzing text: {text}")
    
    text_analysis = qpi.analyze_text(text)
    
    print("\nText Analysis:")
    if "author_match" in text_analysis:
        match = text_analysis["author_match"]
        if match:
            print(f"Closest Author: {match['author']}")
            print(f"Similarity: {match['similarity']:.4f}")
    
    print(f"Consciousness Level: {text_analysis['consciousness_level']}")
    
    # Test music analysis
    frequencies = [432, 528, 639, 741, 852, 963]  # Solfeggio frequencies
    print(f"\nAnalyzing frequencies: {frequencies}")
    
    music_analysis = qpi.analyze_music(frequencies)
    
    print("\nMusic Analysis:")
    print(f"Harmonic Resonance: {music_analysis['harmonic_resonance']:.4f}")
    print(f"Phi Alignment: {music_analysis['phi_alignment']:.4f}")
    print(f"Consciousness: {music_analysis['consciousness']}")

if __name__ == "__main__":
    main()
