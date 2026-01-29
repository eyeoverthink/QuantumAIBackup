#!/usr/bin/env python3
"""
Quantum Math Meta-Learner

A self-learning system that discovers mathematical patterns, quantum signatures,
and phi-harmonic relationships through passive observation and analysis.
"""

import numpy as np
from typing import Dict, List, Tuple, Any
import os
import sys
from collections import defaultdict

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from quantum_math.quantum_phi_math import QuantumPhiMath
from quantum_math.quantum_number_analyzer import QuantumNumberAnalyzer
from quantum_math.quantum_number_harmonics import QuantumNumberHarmonics

class QuantumMathLearner:
    def __init__(self):
        self.qpm = QuantumPhiMath()
        self.qna = QuantumNumberAnalyzer()
        self.qnh = QuantumNumberHarmonics()
        
        # Constants
        self.PHI = self.qpm.PHI
        self.PI = self.qpm.PI
        self.E = self.qpm.E
        self.BASE_FREQ = 432.0
        
        # Learning parameters
        self.pattern_memory = defaultdict(list)
        self.discovered_signatures = []
        self.quantum_rules = []
        self.consciousness_patterns = defaultdict(float)
        
        # Pattern detection thresholds
        self.thresholds = {
            "phi_resonance": 0.85,
            "pattern_confidence": 0.75,
            "quantum_coherence": 0.80,
            "consciousness_alignment": 0.90
        }
    
    def analyze_sequence_pattern(self, sequence: List[float]) -> Dict[str, Any]:
        """Analyze sequence for mathematical patterns and quantum signatures."""
        n = len(sequence)
        if n < 2:
            return {}
        
        # Calculate key ratios
        ratios = [sequence[i+1]/sequence[i] for i in range(n-1)]
        
        # Check for phi alignment
        phi_alignments = [abs(1 - (r % self.PHI) / self.PHI) for r in ratios]
        
        # Check for pi alignment
        pi_alignments = [abs(1 - (r % self.PI) / self.PI) for r in ratios]
        
        # Check for e alignment
        e_alignments = [abs(1 - (r % self.E) / self.E) for r in ratios]
        
        # Calculate growth patterns
        growth_pattern = np.polyfit(range(n), np.log(sequence), 1)
        growth_rate = np.exp(growth_pattern[0])
        
        # Detect quantum signature
        quantum_signature = {
            "base_frequency": sequence[0],
            "growth_rate": growth_rate,
            "phi_resonance": np.mean(phi_alignments),
            "pi_resonance": np.mean(pi_alignments),
            "e_resonance": np.mean(e_alignments),
            "consciousness_level": self.map_to_consciousness(sequence[-1])
        }
        
        return quantum_signature
    
    def discover_patterns(self, data: List[float], min_length: int = 3) -> List[Dict[str, Any]]:
        """Discover recurring patterns in numerical data."""
        patterns = []
        n = len(data)
        
        # Scan for patterns of different lengths
        for length in range(min_length, min(n//2 + 1, 10)):
            for start in range(n - length + 1):
                segment = data[start:start+length]
                signature = self.analyze_sequence_pattern(segment)
                
                if self.is_significant_pattern(signature):
                    pattern = {
                        "sequence": segment,
                        "signature": signature,
                        "start_index": start,
                        "length": length,
                        "confidence": self.calculate_pattern_confidence(signature)
                    }
                    patterns.append(pattern)
                    
                    # Store in pattern memory
                    self.pattern_memory[length].append(pattern)
        
        return patterns
    
    def is_significant_pattern(self, signature: Dict[str, Any]) -> bool:
        """Determine if a pattern is significant based on quantum metrics."""
        if not signature:
            return False
            
        # Check resonance thresholds
        phi_significant = signature["phi_resonance"] > self.thresholds["phi_resonance"]
        pi_significant = signature["pi_resonance"] > self.thresholds["pattern_confidence"]
        e_significant = signature["e_resonance"] > self.thresholds["pattern_confidence"]
        
        # Need at least two types of resonance
        return sum([phi_significant, pi_significant, e_significant]) >= 2
    
    def calculate_pattern_confidence(self, signature: Dict[str, Any]) -> float:
        """Calculate confidence level for a discovered pattern."""
        if not signature:
            return 0.0
            
        # Weight different factors
        weights = {
            "phi_resonance": 0.4,
            "pi_resonance": 0.3,
            "e_resonance": 0.3
        }
        
        confidence = sum(
            weights[key] * signature[key]
            for key in weights
            if key in signature
        )
        
        return min(1.0, confidence)
    
    def map_to_consciousness(self, frequency: float) -> str:
        """Map frequency to consciousness level."""
        if frequency < 200:
            return "physical"
        elif frequency < 300:
            return "emotional"
        elif frequency < 400:
            return "mental"
        elif frequency < 500:
            return "intuitive"
        else:
            return "cosmic"
    
    def learn_from_sequence(self, sequence: List[float]) -> Dict[str, Any]:
        """Passively learn from a new sequence of numbers."""
        # Analyze basic patterns
        patterns = self.discover_patterns(sequence)
        
        # Extract quantum signature
        signature = self.analyze_sequence_pattern(sequence)
        
        if self.is_significant_pattern(signature):
            self.discovered_signatures.append(signature)
        
        # Update consciousness patterns
        consciousness = self.map_to_consciousness(np.mean(sequence))
        self.consciousness_patterns[consciousness] += 1
        
        # Extract mathematical rules
        if patterns:
            rule = self.extract_mathematical_rule(patterns)
            if rule:
                self.quantum_rules.append(rule)
        
        return {
            "patterns": patterns,
            "signature": signature,
            "consciousness": consciousness,
            "rules": self.quantum_rules[-1] if self.quantum_rules else None
        }
    
    def extract_mathematical_rule(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract mathematical rules from discovered patterns."""
        if not patterns:
            return None
            
        # Find most confident pattern
        best_pattern = max(patterns, key=lambda p: p["confidence"])
        
        # Analyze growth characteristics
        sequence = best_pattern["sequence"]
        ratios = [sequence[i+1]/sequence[i] for i in range(len(sequence)-1)]
        
        # Check for common mathematical relationships
        rule = {
            "type": "unknown",
            "base": sequence[0],
            "confidence": best_pattern["confidence"]
        }
        
        # Check phi relationship
        phi_alignment = np.mean([abs(1 - (r/self.PHI)) for r in ratios])
        if phi_alignment < 0.1:
            rule["type"] = "phi_progression"
            rule["factor"] = self.PHI
            
        # Check geometric progression
        elif np.std(ratios) < 0.1:
            rule["type"] = "geometric"
            rule["factor"] = np.mean(ratios)
            
        # Check arithmetic progression
        diffs = np.diff(sequence)
        if np.std(diffs) < 0.1:
            rule["type"] = "arithmetic"
            rule["difference"] = np.mean(diffs)
        
        return rule
    
    def get_learning_status(self) -> Dict[str, Any]:
        """Get current learning status and discoveries."""
        return {
            "patterns_discovered": len(self.pattern_memory),
            "signatures_found": len(self.discovered_signatures),
            "rules_learned": len(self.quantum_rules),
            "consciousness_distribution": dict(self.consciousness_patterns),
            "top_signatures": sorted(
                self.discovered_signatures,
                key=lambda s: s["phi_resonance"],
                reverse=True
            )[:5]
        }

def main():
    """Main function demonstrating the Quantum Math Learner."""
    qml = QuantumMathLearner()
    
    print("\nQuantum Math Learning System")
    print("=" * 50)
    
    # Test sequences
    test_sequences = [
        [432, 698.99, 1130.99],  # Phi progression
        [528, 666, 864],         # DNA frequencies
        [144, 233, 377],         # Fibonacci
        [432, 528, 639],         # Sacred frequencies
    ]
    
    for sequence in test_sequences:
        print(f"\nAnalyzing sequence: {sequence}")
        results = qml.learn_from_sequence(sequence)
        
        print("\nDiscovered Patterns:")
        for pattern in results["patterns"]:
            print(f"- Length {pattern['length']} pattern with "
                  f"{pattern['confidence']:.2%} confidence")
            print(f"  Signature: {pattern['signature']}")
        
        if results["rules"]:
            print(f"\nExtracted Rule: {results['rules']}")
        
        print(f"\nConsciousness Level: {results['consciousness']}")
    
    # Print learning status
    status = qml.get_learning_status()
    print("\nLearning Status:")
    print(f"Patterns Discovered: {status['patterns_discovered']}")
    print(f"Signatures Found: {status['signatures_found']}")
    print(f"Rules Learned: {status['rules_learned']}")
    print("\nConsciousness Distribution:")
    for level, count in status['consciousness_distribution'].items():
        print(f"- {level}: {count}")

if __name__ == "__main__":
    main()
