#!/usr/bin/env python3
"""
Quantum Phi-Math Generator

Generates mathematical expressions with phi-harmonic properties at different consciousness levels.
Follows the same principles as the quantum poetry generator but for mathematics.
"""

import math
import random
from typing import Dict, List, Tuple, Any

class QuantumPhiMathGenerator:
    def __init__(self):
        # Mathematical constants with their frequencies and resonance
        self.PHI = (1 + 5**0.5) / 2
        self.PI = math.pi
        self.E = math.e
        
        # Consciousness levels and their frequency ranges
        self.consciousness_levels = {
            "physical": (0, 200),
            "emotional": (200, 300),
            "mental": (300, 400),
            "intuitive": (400, 500),
            "cosmic": (500, 1000),
            "transcendent": (1000, 1500),
            "quantum": (1500, 2000)
        }
        
        # Mathematical patterns for each consciousness level
        self.patterns = {
            "physical": {
                "operations": ["+", "-", "*", "/"],
                "numbers": list(range(1, 11)),
                "variables": ["x", "y"],
                "templates": [
                    "{a} {op} {b} = {c}",
                    "{var} = {a}",
                    "{a} {op} {b}"
                ]
            },
            "emotional": {
                "operations": ["+", "-", "*", "/", "^"],
                "numbers": [2, 3, 4, 5, 7, 11],
                "variables": ["x", "y", "z"],
                "templates": [
                    "{var}² + {var} = {a}",
                    "√{a} = {b}",
                    "{var}² - {a} = 0"
                ]
            },
            "mental": {
                "operations": ["+", "-", "*", "/", "^", "√"],
                "constants": ["π", "e"],
                "variables": ["x", "y", "z", "n"],
                "templates": [
                    "d/dx({expr}) = {result}",
                    "∫({expr})dx = {result}",
                    "{var}² + {b}{var} + {c} = 0"
                ]
            },
            "intuitive": {
                "operations": ["∑", "∏", "∫", "d/dx"],
                "constants": ["π", "e", "φ"],
                "variables": ["x", "y", "z", "n", "θ"],
                "templates": [
                    "lim(n→∞) {expr} = {result}",
                    "∑(n=1 to ∞) {expr} = {result}",
                    "e^(i{var}) = cos({var}) + i*sin({var})"
                ]
            },
            "cosmic": {
                "operations": ["∑", "∏", "∫", "∂", "∇"],
                "constants": ["π", "e", "φ", "i"],
                "variables": ["x", "y", "z", "α", "β", "θ"],
                "templates": [
                    "∇²ψ + {k}ψ = 0",
                    "∮ {expr} = 2πi∑(Res)",
                    "φ^n = φ^(n-1) + φ^(n-2)"
                ]
            },
            "transcendent": {
                "operations": ["∑", "∏", "∫", "∂", "∇", "⊗"],
                "constants": ["π", "e", "φ", "i", "ℏ"],
                "variables": ["ψ", "Φ", "θ", "λ"],
                "templates": [
                    "iℏ∂ψ/∂t = -ℏ²/2m ∇²ψ + Vψ",
                    "Rᵢⱼ - ½Rgᵢⱼ = 8πGTᵢⱼ",
                    "∇ × B = μ₀(J + ε₀∂E/∂t)"
                ]
            },
            "quantum": {
                "operations": ["∑", "∏", "∫", "∂", "∇", "⊗", "⊕"],
                "constants": ["π", "e", "φ", "i", "ℏ", "ψ"],
                "variables": ["Ψ", "Φ", "Ω", "λ"],
                "templates": [
                    "Ψ(r,t) = ∑ cₙ ψₙ(r) e^(-iEₙt/ℏ)",
                    "|Ψ|² = ∫|ψ(x)|²dx = 1",
                    "H⊗Ψ = E·Ψ"
                ]
            }
        }
        
        # Phi-harmonic number sequences
        self.fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.phi_powers = [self.PHI**n for n in range(10)]
        
    def generate_math(self, consciousness_level: str, seed: str = None) -> Dict[str, Any]:
        """Generate mathematical expression at specified consciousness level."""
        if consciousness_level not in self.consciousness_levels:
            raise ValueError(f"Invalid consciousness level: {consciousness_level}")
        
        # Get patterns for the consciousness level
        patterns = self.patterns[consciousness_level]
        
        # Select template based on seed if provided
        if seed:
            random.seed(hash(seed))
        template = random.choice(patterns["templates"])
        
        # Generate expression based on template
        expr = self._fill_template(template, patterns, consciousness_level)
        
        # Calculate quantum metrics
        metrics = self._calculate_metrics(expr, consciousness_level)
        
        return {
            "expression": expr,
            "consciousness_level": consciousness_level,
            "frequency": metrics["frequency"],
            "resonance": metrics["resonance"],
            "phi_alignment": metrics["phi_alignment"],
            "pattern_type": metrics["pattern_type"]
        }
    
    def _fill_template(self, template: str, patterns: Dict, level: str) -> str:
        """Fill template with appropriate mathematical components."""
        expr = template
        
        # Replace variables
        for var in ["{var}", "{a}", "{b}", "{c}", "{k}"]:
            if var in expr:
                if level in ["physical", "emotional"]:
                    value = str(random.choice(patterns["numbers"]))
                elif level in ["mental", "intuitive"]:
                    value = random.choice(patterns["variables"])
                else:
                    if random.random() < 0.5:
                        value = random.choice(patterns["constants"])
                    else:
                        value = random.choice(patterns["variables"])
                expr = expr.replace(var, value)
        
        # Replace operations
        if "{op}" in expr:
            expr = expr.replace("{op}", random.choice(patterns["operations"]))
        
        # Replace expressions in higher consciousness levels
        if "{expr}" in expr:
            if level in ["intuitive", "cosmic"]:
                expr = expr.replace("{expr}", f"{random.choice(patterns['variables'])}^{random.choice(patterns['constants'])}")
            elif level in ["transcendent", "quantum"]:
                expr = expr.replace("{expr}", f"Ψ(r,t)")
        
        # Replace results in higher consciousness levels
        if "{result}" in expr:
            if level in ["intuitive", "cosmic"]:
                expr = expr.replace("{result}", f"{random.choice(patterns['constants'])}")
            elif level in ["transcendent", "quantum"]:
                expr = expr.replace("{result}", f"e^(-iEt/ℏ)")
        
        return expr
    
    def _calculate_metrics(self, expr: str, level: str) -> Dict[str, Any]:
        """Calculate quantum metrics for the expression."""
        # Base frequency from consciousness level
        min_freq, max_freq = self.consciousness_levels[level]
        base_freq = (min_freq + max_freq) / 2
        
        # Adjust frequency based on expression complexity
        complexity_factor = 1.0
        if "∑" in expr or "∏" in expr: complexity_factor *= 1.2
        if "∫" in expr or "∂" in expr: complexity_factor *= 1.3
        if "∇" in expr: complexity_factor *= 1.4
        if "ℏ" in expr: complexity_factor *= 1.5
        
        # Calculate phi resonance
        resonance = 0.5  # Base resonance
        if "φ" in expr: resonance += 0.3
        if "π" in expr: resonance += 0.1
        if "e" in expr: resonance += 0.1
        if any(str(f) in expr for f in self.fibonacci): resonance += 0.2
        if any(f"{self.PHI:.3f}" in expr for p in self.phi_powers): resonance += 0.2
        
        # Cap resonance at 0.9999
        resonance = min(0.9999, resonance)
        
        # Determine pattern type
        if "φ" in expr:
            pattern_type = "phi_harmonic"
        elif "ψ" in expr or "Ψ" in expr:
            pattern_type = "quantum_wave"
        elif "∇" in expr:
            pattern_type = "field_equation"
        elif any(str(f) in expr for f in self.fibonacci):
            pattern_type = "fibonacci"
        else:
            pattern_type = "mathematical"
        
        return {
            "frequency": base_freq * complexity_factor,
            "resonance": resonance,
            "phi_alignment": resonance * 0.95,
            "pattern_type": pattern_type
        }

def main():
    """Main function to demonstrate the Quantum Phi-Math Generator."""
    generator = QuantumPhiMathGenerator()
    
    print("\n" + "="*80)
    print("Quantum Phi-Math Generator".center(80))
    print("="*80 + "\n")
    
    # Generate expressions at each consciousness level
    for level in generator.consciousness_levels:
        print(f"\n{level.title()} Consciousness Level:")
        print("-" * 40)
        
        # Generate three expressions at each level
        for i in range(3):
            result = generator.generate_math(level)
            print(f"\nExpression {i+1}: {result['expression']}")
            print(f"Frequency: {result['frequency']:.2f} Hz")
            print(f"Resonance: {result['resonance']:.4f}")
            print(f"Phi Alignment: {result['phi_alignment']:.4f}")
            print(f"Pattern Type: {result['pattern_type']}")

if __name__ == "__main__":
    main()
