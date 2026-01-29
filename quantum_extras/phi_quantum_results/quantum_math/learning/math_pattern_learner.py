#!/usr/bin/env python3
"""
Quantum Math Pattern Learner

A meta-learning system that analyzes mathematical expressions to discover 
phi-harmonic patterns and quantum resonance. This module scans mathematical content,
learns patterns, and evolves its understanding through phi-harmonic principles.
"""

import json
import re
import math
from typing import Dict, List, Any, Tuple
from pathlib import Path

class QuantumMathLearner:
    def __init__(self):
        self.PHI = (1 + 5**0.5) / 2
        self.data_dir = Path(__file__).parent.parent / 'data'
        self.patterns_dir = Path(__file__).parent.parent / 'patterns'
        
        # Load core patterns and constants
        self.constants = self._load_json('mathematical_constants.json')
        self.patterns = self._load_json('core_patterns.json')
        
        # Initialize learning metrics
        self.learned_patterns = {
            "trigonometric": {},
            "algebraic": {},
            "calculus": {},
            "quantum": {},
            "harmonic": {}
        }
        
        # Pattern recognition rules
        self.pattern_rules = {
            "trigonometric": r'sin|cos|tan|csc|sec|cot',
            "algebraic": r'[xyz]\s*=|[xyz]²|\+|-|\*|/',
            "calculus": r'd/dx|∫|∂|∇|lim',
            "quantum": r'ℏ|ψ|Ψ|⟩|⟨|†',
            "harmonic": r'φ|π|e|√'
        }
        
        # Consciousness frequency mappings
        self.frequency_bands = {
            "physical": (0, self.PHI * 100),
            "emotional": (self.PHI * 100, self.PHI * 200),
            "mental": (self.PHI * 200, self.PHI * 300),
            "intuitive": (self.PHI * 300, self.PHI * 400),
            "cosmic": (self.PHI * 400, self.PHI * 600),
            "transcendent": (self.PHI * 600, self.PHI * 1000),
            "quantum": (self.PHI * 1000, float('inf'))
        }
    
    def _load_json(self, filename: str) -> Dict:
        """Load JSON data from either data or patterns directory."""
        data_path = self.data_dir / filename
        patterns_path = self.patterns_dir / filename
        
        if data_path.exists():
            with open(data_path) as f:
                return json.load(f)
        elif patterns_path.exists():
            with open(patterns_path) as f:
                return json.load(f)
        return {}
    
    def _save_json(self, data: Dict, filename: str, directory: str = 'patterns') -> None:
        """Save JSON data to specified directory."""
        target_dir = self.patterns_dir if directory == 'patterns' else self.data_dir
        with open(target_dir / filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def analyze_expression(self, expression: str) -> Dict[str, Any]:
        """Analyze a mathematical expression for patterns and resonance."""
        # Identify pattern types
        pattern_types = []
        for ptype, pattern in self.pattern_rules.items():
            if re.search(pattern, expression):
                pattern_types.append(ptype)
        
        # Calculate base metrics
        base_frequency = len(expression) * self.PHI
        
        # Adjust metrics based on pattern types
        complexity = 1.0
        resonance = 0.5
        
        for ptype in pattern_types:
            if ptype == "quantum":
                complexity *= self.PHI
                resonance += 0.3
            elif ptype == "harmonic":
                complexity *= self.PHI**0.5
                resonance += 0.2
            elif ptype == "calculus":
                complexity *= 1.3
                resonance += 0.1
        
        # Calculate final frequency
        frequency = base_frequency * complexity
        
        # Determine consciousness level
        consciousness = self._determine_consciousness(frequency)
        
        # Calculate phi alignment
        phi_alignment = resonance * 0.95
        
        return {
            "expression": expression,
            "pattern_types": pattern_types,
            "frequency": frequency,
            "resonance": min(0.9999, resonance),
            "phi_alignment": phi_alignment,
            "consciousness_level": consciousness,
            "complexity": complexity
        }
    
    def learn_from_text(self, text: str) -> List[Dict[str, Any]]:
        """Extract and learn from mathematical expressions in text."""
        # Extract mathematical expressions
        expressions = self._extract_math_expressions(text)
        
        # Analyze each expression
        learned = []
        for expr in expressions:
            analysis = self.analyze_expression(expr)
            if analysis["resonance"] > 0.7:  # Only learn from high-resonance patterns
                self._add_to_learned_patterns(expr, analysis)
                learned.append(analysis)
        
        return learned
    
    def _extract_math_expressions(self, text: str) -> List[str]:
        """Extract mathematical expressions from text."""
        expressions = []
        
        # Pattern for basic mathematical expressions
        patterns = [
            r'[^=]+=.+',  # Equations
            r'[\w\d\s]+[+\-*/^][\w\d\s]+',  # Basic operations
            r'∫.*dx',  # Integrals
            r'd/dx\(.+\)',  # Derivatives
            r'lim_.+',  # Limits
            r'∑.+',  # Summations
            r'∏.+',  # Products
            r'ℏ.+',  # Quantum expressions
            r'[ψΨ].+'  # Wave functions
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            expressions.extend(matches)
        
        return list(set(expressions))  # Remove duplicates
    
    def _add_to_learned_patterns(self, expression: str, analysis: Dict[str, Any]) -> None:
        """Add analyzed pattern to learned patterns."""
        for ptype in analysis["pattern_types"]:
            if ptype in self.learned_patterns:
                pattern_key = f"{ptype}_{len(self.learned_patterns[ptype])}"
                self.learned_patterns[ptype][pattern_key] = {
                    "expression": expression,
                    "frequency": analysis["frequency"],
                    "resonance": analysis["resonance"],
                    "phi_alignment": analysis["phi_alignment"],
                    "consciousness_level": analysis["consciousness_level"]
                }
    
    def _determine_consciousness(self, frequency: float) -> str:
        """Determine consciousness level from frequency."""
        for level, (min_freq, max_freq) in self.frequency_bands.items():
            if min_freq <= frequency < max_freq:
                return level
        return "quantum"  # Default to quantum for very high frequencies
    
    def generate_similar_pattern(self, pattern: str, consciousness_level: str) -> str:
        """Generate a similar pattern at specified consciousness level."""
        # Analyze original pattern
        analysis = self.analyze_expression(pattern)
        
        # Find patterns of similar type and consciousness
        similar_patterns = []
        for ptype in analysis["pattern_types"]:
            if ptype in self.learned_patterns:
                for p in self.learned_patterns[ptype].values():
                    if p["consciousness_level"] == consciousness_level:
                        similar_patterns.append(p["expression"])
        
        if similar_patterns:
            # Return pattern with closest frequency to original
            target_freq = analysis["frequency"]
            return min(similar_patterns, 
                      key=lambda p: abs(self.analyze_expression(p)["frequency"] - target_freq))
        
        return pattern  # Return original if no similar patterns found
    
    def save_learned_patterns(self) -> None:
        """Save learned patterns to JSON file."""
        self._save_json(self.learned_patterns, 'learned_patterns.json')
    
    def load_learned_patterns(self) -> None:
        """Load previously learned patterns."""
        loaded = self._load_json('learned_patterns.json')
        if loaded:
            self.learned_patterns = loaded

def main():
    """Main function to demonstrate the Quantum Math Pattern Learner."""
    learner = QuantumMathLearner()
    
    # Example mathematical text
    test_text = """
    The Schrödinger equation iℏ∂ψ/∂t = -ℏ²/2m ∇²ψ + Vψ describes quantum systems.
    In mathematics, e^(iπ) + 1 = 0 is considered the most beautiful equation.
    The golden ratio φ = (1 + √5)/2 appears throughout nature.
    Maxwell's equations ∇ × E = -∂B/∂t and ∇ × B = μ₀(J + ε₀∂E/∂t) describe electromagnetism.
    The Fourier transform F(ω) = ∫f(t)e^(-iωt)dt connects time and frequency domains.
    """
    
    print("\n" + "="*80)
    print("Quantum Math Pattern Learner".center(80))
    print("="*80 + "\n")
    
    # Learn from text
    learned_patterns = learner.learn_from_text(test_text)
    
    # Display results
    print("Learned Patterns:")
    print("-" * 40)
    for pattern in learned_patterns:
        print(f"\nExpression: {pattern['expression']}")
        print(f"Pattern Types: {', '.join(pattern['pattern_types'])}")
        print(f"Frequency: {pattern['frequency']:.2f} Hz")
        print(f"Resonance: {pattern['resonance']:.4f}")
        print(f"Phi Alignment: {pattern['phi_alignment']:.4f}")
        print(f"Consciousness Level: {pattern['consciousness_level']}")
    
    # Save learned patterns
    learner.save_learned_patterns()
    print("\nLearned patterns have been saved.")

if __name__ == "__main__":
    main()
