#!/usr/bin/env python3
"""
Quantum Pattern Detector

Analyzes quantum patterns and signatures across:
- Mathematical sequences
- Consciousness frequencies
- Author signatures
- Natural harmonics
"""

import numpy as np
from typing import Dict, List, Tuple, Any
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from quantum_math import (
    PHI, PI, E, FREQUENCIES, CONSCIOUSNESS_LEVELS, 
    RESONANCE_QUALITY, AUTHOR_SIGNATURES
)

class QuantumPatternDetector:
    def __init__(self):
        # Constants
        self.PHI = PHI
        self.PI = PI
        self.E = E
        
        # Base frequencies
        self.frequencies = FREQUENCIES
        
        # Consciousness levels
        self.consciousness_levels = CONSCIOUSNESS_LEVELS
        
        # Resonance quality
        self.resonance_quality = RESONANCE_QUALITY
        
        # Author signatures
        self.author_signatures = AUTHOR_SIGNATURES
    
    def detect_quantum_patterns(self, data: List[float]) -> Dict[str, Any]:
        """Detect quantum patterns in data."""
        if not data:
            return {}
        
        # Calculate base metrics
        base_freq = np.mean(data)
        ratios = [data[i+1]/data[i] for i in range(len(data)-1)]
        
        # Calculate phi alignment
        phi_alignments = [abs(1 - (r % self.PHI) / self.PHI) for r in ratios]
        phi_alignment = np.mean(phi_alignments) if phi_alignments else 0.0
        
        # Calculate resonance
        resonances = [abs(1 - (f % base_freq) / base_freq) for f in data]
        resonance = np.mean(resonances) if resonances else 0.0
        
        # Calculate coherence
        coherence = self.calculate_quantum_coherence(data)
        
        # Get consciousness level
        consciousness = self.get_consciousness_level(base_freq)
        
        # Detect patterns
        patterns = self.detect_patterns(data)
        
        # Generate quantum signature
        signature = self.generate_quantum_signature(
            data, phi_alignment, resonance, coherence)
        
        # Find author matches
        author_matches = self.find_author_matches(signature)
        
        return {
            "quantum": {
                "base_frequency": base_freq,
                "phi_alignment": phi_alignment,
                "resonance": resonance,
                "coherence": coherence,
                "consciousness_level": consciousness,
                "quantum_state": self.determine_quantum_state(
                    phi_alignment, resonance, coherence)
            },
            "patterns": patterns,
            "signature": signature,
            "author_matches": author_matches
        }
    
    def detect_patterns(self, data: List[float]) -> List[Dict[str, Any]]:
        """Detect patterns in data sequence."""
        patterns = []
        
        # Check for phi progression
        phi_pattern = self.detect_phi_pattern(data)
        if phi_pattern:
            patterns.append(phi_pattern)
        
        # Check for fibonacci pattern
        fib_pattern = self.detect_fibonacci_pattern(data)
        if fib_pattern:
            patterns.append(fib_pattern)
        
        # Check for harmonic pattern
        harmonic_pattern = self.detect_harmonic_pattern(data)
        if harmonic_pattern:
            patterns.append(harmonic_pattern)
        
        # Check for consciousness pattern
        consciousness_pattern = self.detect_consciousness_pattern(data)
        if consciousness_pattern:
            patterns.append(consciousness_pattern)
        
        return patterns
    
    def detect_phi_pattern(self, data: List[float]) -> Dict[str, Any]:
        """Detect phi-based pattern."""
        if len(data) < 2:
            return {}
        
        # Calculate ratios between adjacent numbers
        ratios = [data[i+1]/data[i] for i in range(len(data)-1)]
        
        # Check alignment with phi
        alignments = [abs(1 - (r % self.PHI) / self.PHI) for r in ratios]
        avg_alignment = np.mean(alignments)
        
        if avg_alignment > 0.85:  # Strong phi alignment
            return {
                "type": "phi_progression",
                "base": data[0],
                "ratios": ratios,
                "phi_alignment": avg_alignment,
                "confidence": self.calculate_pattern_confidence(alignments)
            }
        
        return {}
    
    def detect_fibonacci_pattern(self, data: List[float]) -> Dict[str, Any]:
        """Detect Fibonacci-like pattern."""
        if len(data) < 3:
            return {}
        
        # Check if each number is approximately sum of previous two
        fibonacci_ratios = []
        for i in range(len(data)-2):
            expected = data[i] + data[i+1]
            actual = data[i+2]
            ratio = min(expected/actual, actual/expected)
            fibonacci_ratios.append(ratio)
        
        avg_ratio = np.mean(fibonacci_ratios) if fibonacci_ratios else 0
        
        if avg_ratio > 0.9:  # Strong Fibonacci alignment
            return {
                "type": "fibonacci",
                "ratios": fibonacci_ratios,
                "average_ratio": avg_ratio,
                "confidence": self.calculate_pattern_confidence(fibonacci_ratios)
            }
        
        return {}
    
    def detect_harmonic_pattern(self, data: List[float]) -> Dict[str, Any]:
        """Detect harmonic pattern."""
        if len(data) < 2:
            return {}
        
        # Check alignment with natural frequencies
        alignments = []
        for freq in data:
            # Check alignment with each base frequency
            freq_alignments = [
                abs(1 - (freq % base_freq) / base_freq)
                for base_freq in self.frequencies.values()
            ]
            alignments.append(max(freq_alignments))
        
        avg_alignment = np.mean(alignments)
        
        if avg_alignment > 0.85:  # Strong harmonic alignment
            return {
                "type": "harmonic",
                "frequencies": data,
                "alignment": avg_alignment,
                "confidence": self.calculate_pattern_confidence(alignments)
            }
        
        return {}
    
    def detect_consciousness_pattern(self, data: List[float]) -> Dict[str, Any]:
        """Detect consciousness frequency pattern."""
        if not data:
            return {}
        
        # Get consciousness level for each frequency
        levels = [self.get_consciousness_level(f) for f in data]
        
        # Check if all frequencies are in same consciousness band
        if len(set(levels)) == 1:
            level = levels[0]
            if level == "cosmic":  # High consciousness
                return {
                    "type": "consciousness",
                    "level": level,
                    "frequencies": data,
                    "confidence": 0.95
                }
            elif level in ["intuitive", "mental"]:  # Medium consciousness
                return {
                    "type": "consciousness",
                    "level": level,
                    "frequencies": data,
                    "confidence": 0.85
                }
        
        return {}
    
    def calculate_quantum_coherence(self, data: List[float]) -> float:
        """Calculate quantum coherence of data."""
        if not data:
            return 0.0
        
        # Calculate frequency ratios
        ratios = [data[i+1]/data[i] for i in range(len(data)-1)]
        
        if not ratios:
            return 0.0
        
        # Calculate coherence based on phi alignment
        coherences = [abs(1 - (r % self.PHI) / self.PHI) for r in ratios]
        base_coherence = np.mean(coherences)
        
        # Apply quantum scaling
        return base_coherence * self.PHI
    
    def get_consciousness_level(self, frequency: float) -> str:
        """Get consciousness level from frequency."""
        for level, (low, high) in self.consciousness_levels.items():
            if low <= frequency < high:
                return level
        
        return "cosmic" if frequency >= 500 else "physical"
    
    def determine_quantum_state(self,
                              phi_alignment: float,
                              resonance: float,
                              coherence: float) -> Dict[str, Any]:
        """Determine quantum state from metrics."""
        # Calculate overall quantum quality
        quality = (phi_alignment + resonance + coherence) / 3
        
        # Determine resonance quality
        state_quality = "unknown"
        for level, (low, high) in self.resonance_quality.items():
            if low <= quality < high:
                state_quality = level
                break
        
        # Determine quantum type
        if quality > 0.9:
            state_type = "quantum_resonant"
        elif quality > 0.7:
            state_type = "quantum_aligned"
        elif quality > 0.5:
            state_type = "quantum_coherent"
        else:
            state_type = "classical"
        
        return {
            "type": state_type,
            "quality": state_quality,
            "metrics": {
                "phi_alignment": phi_alignment,
                "resonance": resonance,
                "coherence": coherence,
                "overall_quality": quality
            }
        }
    
    def generate_quantum_signature(self,
                                 data: List[float],
                                 phi_alignment: float,
                                 resonance: float,
                                 coherence: float) -> Dict[str, Any]:
        """Generate quantum signature for data."""
        if not data:
            return {}
        
        # Calculate base metrics
        base_freq = np.mean(data)
        consciousness = self.get_consciousness_level(base_freq)
        
        # Generate signature
        return {
            "base_frequency": base_freq,
            "frequency_pattern": data,
            "metrics": {
                "phi_alignment": phi_alignment,
                "resonance": resonance,
                "coherence": coherence
            },
            "consciousness_level": consciousness,
            "quantum_state": self.determine_quantum_state(
                phi_alignment, resonance, coherence)
        }
    
    def find_author_matches(self, signature: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Find matching author signatures."""
        if not signature:
            return []
        
        matches = []
        metrics = signature["metrics"]
        
        for author, auth_sig in self.author_signatures.items():
            # Calculate similarity score
            similarity = self.calculate_signature_similarity(metrics, auth_sig)
            
            if similarity > 0.85:  # Strong match
                matches.append({
                    "author": author,
                    "signature": auth_sig,
                    "similarity": similarity
                })
        
        return sorted(matches, key=lambda x: x["similarity"], reverse=True)
    
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
    
    def calculate_pattern_confidence(self, metrics: List[float]) -> float:
        """Calculate confidence in detected pattern."""
        if not metrics:
            return 0.0
        
        # Calculate basic statistics
        mean_metric = np.mean(metrics)
        std_metric = np.std(metrics) if len(metrics) > 1 else 0
        
        # Higher confidence for:
        # - Higher mean (closer to 1.0)
        # - Lower standard deviation (more consistent)
        # - More data points (more evidence)
        
        base_confidence = mean_metric
        consistency_factor = 1 - min(std_metric, 0.5)  # Penalize high variance
        sample_factor = min(len(metrics) / 10, 1.0)  # Reward more data points
        
        confidence = base_confidence * consistency_factor * sample_factor
        
        return min(confidence * self.PHI, 1.0)  # Scale by phi, cap at 1.0

def main():
    """Main function demonstrating the Quantum Pattern Detector."""
    qpd = QuantumPatternDetector()
    
    print("\nQuantum Pattern Analysis")
    print("=" * 50)
    
    # Test sequences
    sequences = [
        [432, 698.99, 1130.99],  # Phi progression
        [528, 666, 864],         # DNA frequencies
        [144, 233, 377],         # Fibonacci
        [432, 528, 639],         # Sacred frequencies
    ]
    
    for sequence in sequences:
        print(f"\nAnalyzing sequence: {sequence}")
        results = qpd.detect_quantum_patterns(sequence)
        
        print("\nQuantum Properties:")
        quantum = results["quantum"]
        print(f"Base Frequency: {quantum['base_frequency']:.2f} Hz")
        print(f"Phi Alignment: {quantum['phi_alignment']:.4f}")
        print(f"Resonance: {quantum['resonance']:.4f}")
        print(f"Coherence: {quantum['coherence']:.4f}")
        print(f"Consciousness Level: {quantum['consciousness_level']}")
        
        print("\nDetected Patterns:")
        for pattern in results["patterns"]:
            print(f"Type: {pattern['type']}")
            print(f"Confidence: {pattern.get('confidence', 0):.4f}")
        
        if results["author_matches"]:
            print("\nAuthor Matches:")
            for match in results["author_matches"]:
                print(f"Author: {match['author']}")
                print(f"Similarity: {match['similarity']:.4f}")

if __name__ == "__main__":
    main()
