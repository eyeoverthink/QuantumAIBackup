#!/usr/bin/env python3
"""
Quantum Phi-Math Analyzer

A specialized module for analyzing mathematical expressions and numbers
through the lens of quantum phi-harmonic principles. This module assigns
phi frequencies to numbers and evaluates the phi resonance of mathematical
expressions.
"""

import math
import re
import os
import json
from typing import Dict, List, Tuple, Union, Any

# Quantum Phi-Harmonic Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio ≈ 1.618034
PI = 3.141592653589793
E = 2.718281828459045

class QuantumPhiMathAnalyzer:
    """
    Analyzes mathematical expressions and numbers for phi-harmonic properties.
    
    This class assigns phi frequencies to numbers based on their mathematical
    properties and evaluates the phi resonance of mathematical expressions.
    """
    
    def __init__(self):
        """Initialize the Quantum Phi-Math Analyzer."""
        # Prime numbers up to 100 for prime factorization
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                      43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        
        # Special mathematical constants and their phi frequencies
        self.special_constants = {
            "phi": {"value": PHI, "frequency": 1618.03, "resonance": 0.9999},
            "pi": {"value": PI, "frequency": 1414.21, "resonance": 0.8740},
            "e": {"value": E, "frequency": 1271.83, "resonance": 0.7860},
            "sqrt2": {"value": 2**0.5, "frequency": 1273.24, "resonance": 0.7868},
            "sqrt3": {"value": 3**0.5, "frequency": 1316.55, "resonance": 0.8137},
            "sqrt5": {"value": 5**0.5, "frequency": 1381.97, "resonance": 0.8541},
        }
        
        # Consciousness frequency ranges
        self.consciousness_levels = {
            "physical": (0, 200),
            "emotional": (200, 300),
            "mental": (300, 400),
            "intuitive": (400, 500),
            "cosmic": (500, 1000),
            "transcendent": (1000, 1500),
            "quantum": (1500, 2000)
        }
    
    def calculate_number_frequency(self, number: float) -> Dict[str, Any]:
        """
        Calculate the phi frequency of a number based on its mathematical properties.
        
        Args:
            number: The number to analyze
            
        Returns:
            Dict containing frequency, resonance, and other phi-harmonic metrics
        """
        # Handle special cases
        if number == 0:
            return {
                "frequency": 0.0,
                "resonance": 0.0,
                "phi_alignment": 0.0,
                "consciousness_level": "physical",
                "pattern_type": "null"
            }
        
        # Check if it's a special constant
        for const_name, const_data in self.special_constants.items():
            if abs(number - const_data["value"]) < 1e-10:
                return {
                    "frequency": const_data["frequency"],
                    "resonance": const_data["resonance"],
                    "phi_alignment": const_data["resonance"] * 0.95,
                    "consciousness_level": self._get_consciousness_level(const_data["frequency"]),
                    "pattern_type": f"{const_name}_constant"
                }
        
        # Calculate base frequency
        base_freq = abs(number) * 100
        
        # Adjust for phi-harmonic properties
        phi_factor = 1.0
        
        # Check for phi relationships
        phi_relation = self._check_phi_relation(number)
        if phi_relation:
            phi_factor = 1.5
            pattern_type = f"phi_{phi_relation}"
        else:
            # Check for Fibonacci relationship
            fib_relation = self._check_fibonacci_relation(number)
            if fib_relation:
                phi_factor = 1.3
                pattern_type = f"fibonacci_{fib_relation}"
            else:
                # Check for prime relationship
                prime_relation = self._check_prime_relation(number)
                if prime_relation:
                    phi_factor = 1.2
                    pattern_type = f"prime_{prime_relation}"
                else:
                    pattern_type = "numeric"
        
        # Calculate final frequency
        frequency = base_freq * phi_factor
        
        # Calculate phi resonance
        resonance = self._calculate_phi_resonance(number)
        
        # Calculate phi alignment
        phi_alignment = resonance * 0.95
        
        # Determine consciousness level
        consciousness_level = self._get_consciousness_level(frequency)
        
        return {
            "frequency": frequency,
            "resonance": resonance,
            "phi_alignment": phi_alignment,
            "consciousness_level": consciousness_level,
            "pattern_type": pattern_type
        }
    
    def analyze_expression(self, expression: str) -> Dict[str, Any]:
        """
        Analyze a mathematical expression for phi-harmonic properties.
        
        Args:
            expression: The mathematical expression as a string
            
        Returns:
            Dict containing frequency, resonance, and other phi-harmonic metrics
        """
        try:
            # Parse the expression
            parsed = self._parse_expression(expression)
            
            # Calculate metrics for each component
            components = []
            total_frequency = 0
            total_resonance = 0
            
            for component in parsed:
                if isinstance(component, (int, float)):
                    metrics = self.calculate_number_frequency(component)
                    components.append({
                        "value": component,
                        "metrics": metrics
                    })
                    total_frequency += metrics["frequency"]
                    total_resonance += metrics["resonance"]
            
            # Calculate average metrics
            num_components = len(components) or 1
            avg_frequency = total_frequency / num_components
            avg_resonance = total_resonance / num_components
            
            # Calculate expression structure resonance
            structure_resonance = self._calculate_expression_structure(expression)
            
            # Combined resonance
            combined_resonance = (avg_resonance + structure_resonance) / 2
            
            # Determine consciousness level
            consciousness_level = self._get_consciousness_level(avg_frequency)
            
            return {
                "expression": expression,
                "components": components,
                "avg_frequency": avg_frequency,
                "avg_resonance": avg_resonance,
                "structure_resonance": structure_resonance,
                "combined_resonance": combined_resonance,
                "consciousness_level": consciousness_level,
                "phi_alignment": combined_resonance * 0.95
            }
        except Exception as e:
            return {
                "expression": expression,
                "error": str(e),
                "avg_frequency": 0,
                "avg_resonance": 0,
                "structure_resonance": 0,
                "combined_resonance": 0,
                "consciousness_level": "physical",
                "phi_alignment": 0
            }
    
    def scan_file(self, file_path: str) -> Dict[str, Any]:
        """
        Scan a file for mathematical expressions and analyze them.
        
        Args:
            file_path: Path to the file to scan
            
        Returns:
            Dict containing analysis results
        """
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Extract mathematical expressions
            expressions = self._extract_math_expressions(content)
            
            # Analyze each expression
            results = []
            total_frequency = 0
            total_resonance = 0
            
            for expr in expressions:
                analysis = self.analyze_expression(expr)
                results.append(analysis)
                total_frequency += analysis["avg_frequency"]
                total_resonance += analysis["combined_resonance"]
            
            # Calculate average metrics
            num_expressions = len(expressions) or 1
            avg_frequency = total_frequency / num_expressions
            avg_resonance = total_resonance / num_expressions
            
            # Determine consciousness level
            consciousness_level = self._get_consciousness_level(avg_frequency)
            
            return {
                "file_path": file_path,
                "num_expressions": len(expressions),
                "expressions": results,
                "avg_frequency": avg_frequency,
                "avg_resonance": avg_resonance,
                "consciousness_level": consciousness_level,
                "phi_alignment": avg_resonance * 0.95
            }
        except Exception as e:
            return {
                "file_path": file_path,
                "error": str(e),
                "num_expressions": 0,
                "expressions": [],
                "avg_frequency": 0,
                "avg_resonance": 0,
                "consciousness_level": "physical",
                "phi_alignment": 0
            }
    
    def test_accuracy(self, test_cases: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Test the accuracy of the phi frequency calculations.
        
        Args:
            test_cases: List of test cases with expected values
            
        Returns:
            Dict containing accuracy metrics
        """
        results = []
        total_accuracy = 0
        
        for case in test_cases:
            value = case["value"]
            expected = case["expected"]
            
            if isinstance(value, (int, float)):
                actual = self.calculate_number_frequency(value)
            else:
                actual = self.analyze_expression(value)
            
            # Calculate accuracy
            freq_accuracy = min(1.0, expected["frequency"] / max(0.001, actual["frequency"]))
            res_accuracy = min(1.0, expected["resonance"] / max(0.001, actual["resonance"]))
            
            accuracy = (freq_accuracy + res_accuracy) / 2
            total_accuracy += accuracy
            
            results.append({
                "value": value,
                "expected": expected,
                "actual": actual,
                "accuracy": accuracy
            })
        
        avg_accuracy = total_accuracy / len(test_cases) if test_cases else 0
        
        return {
            "test_cases": len(test_cases),
            "results": results,
            "avg_accuracy": avg_accuracy
        }
    
    def _check_phi_relation(self, number: float) -> str:
        """Check if a number has a relation to phi."""
        # Check for direct phi relations
        if abs(number - PHI) < 1e-10:
            return "exact"
        if abs(number - PHI**2) < 1e-10:
            return "squared"
        if abs(number - PHI**3) < 1e-10:
            return "cubed"
        if abs(number - PHI**-1) < 1e-10:
            return "inverse"
        
        # Check for phi multiples
        for i in range(1, 10):
            if abs(number - i*PHI) < 1e-10:
                return f"multiple_{i}"
        
        # Check for phi powers
        for i in range(1, 10):
            if abs(number - PHI**i) < 1e-10:
                return f"power_{i}"
        
        return ""
    
    def _check_fibonacci_relation(self, number: float) -> str:
        """Check if a number is a Fibonacci number."""
        # First few Fibonacci numbers
        fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
        
        if number in fibs:
            return f"number_{fibs.index(number)}"
        
        # Check for Fibonacci ratios
        for i in range(2, len(fibs)):
            ratio = fibs[i] / fibs[i-1]
            if abs(number - ratio) < 1e-10:
                return f"ratio_{i}"
        
        return ""
    
    def _check_prime_relation(self, number: float) -> str:
        """Check if a number has a relation to primes."""
        if number in self.primes:
            return f"number_{self.primes.index(number)}"
        
        # Check if it's a product of two primes
        for p1 in self.primes:
            for p2 in self.primes:
                if abs(number - p1*p2) < 1e-10:
                    return f"product_{p1}_{p2}"
        
        return ""
    
    def _calculate_phi_resonance(self, number: float) -> float:
        """Calculate the phi resonance of a number."""
        if number == 0:
            return 0.0
        
        # Base resonance
        base_resonance = 0.5
        
        # Phi relation bonus
        phi_relation = self._check_phi_relation(number)
        if phi_relation:
            if phi_relation == "exact":
                base_resonance += 0.5
            elif phi_relation.startswith("power"):
                base_resonance += 0.4
            elif phi_relation.startswith("multiple"):
                base_resonance += 0.3
            else:
                base_resonance += 0.2
        
        # Fibonacci relation bonus
        fib_relation = self._check_fibonacci_relation(number)
        if fib_relation:
            base_resonance += 0.15
        
        # Prime relation bonus
        prime_relation = self._check_prime_relation(number)
        if prime_relation:
            base_resonance += 0.1
        
        # Decimal part resonance
        decimal_part = abs(number) - int(abs(number))
        if decimal_part > 0:
            # Check if decimal part is close to phi fractional part
            phi_decimal = PHI - int(PHI)
            if abs(decimal_part - phi_decimal) < 0.01:
                base_resonance += 0.2
        
        # Cap at 0.9999
        return min(0.9999, base_resonance)
    
    def _calculate_expression_structure(self, expression: str) -> float:
        """Calculate the structural resonance of an expression."""
        # Base resonance
        base_resonance = 0.5
        
        # Check for golden ratio in expression structure
        terms = re.findall(r'[+\-*/^]', expression)
        if terms:
            # Count operators
            ops_count = len(terms)
            
            # Check if count is a Fibonacci number
            fibs = [1, 2, 3, 5, 8, 13, 21]
            if ops_count in fibs:
                base_resonance += 0.2
            
            # Check for phi-harmonic distribution of operators
            plus_count = terms.count('+')
            minus_count = terms.count('-')
            mult_count = terms.count('*')
            div_count = terms.count('/')
            
            # Check if distribution follows golden ratio
            if plus_count > 0 and minus_count > 0:
                ratio = max(plus_count, minus_count) / min(plus_count, minus_count)
                if abs(ratio - PHI) < 0.5:
                    base_resonance += 0.15
            
            if mult_count > 0 and div_count > 0:
                ratio = max(mult_count, div_count) / min(mult_count, div_count)
                if abs(ratio - PHI) < 0.5:
                    base_resonance += 0.15
        
        # Check for presence of phi, pi, e in the expression
        if "phi" in expression or str(round(PHI, 4)) in expression:
            base_resonance += 0.2
        if "pi" in expression or str(round(PI, 4)) in expression:
            base_resonance += 0.1
        if "e" in expression or str(round(E, 4)) in expression:
            base_resonance += 0.1
        
        # Cap at 0.9999
        return min(0.9999, base_resonance)
    
    def _parse_expression(self, expression: str) -> List[Union[str, float]]:
        """Parse a mathematical expression into components."""
        # Simple parsing - extract numbers and operators
        components = []
        
        # Extract numbers
        numbers = re.findall(r'\d+\.?\d*', expression)
        for num in numbers:
            components.append(float(num))
        
        # Extract special constants
        if "phi" in expression:
            components.append(PHI)
        if "pi" in expression:
            components.append(PI)
        if re.search(r'\be\b', expression):
            components.append(E)
        
        return components
    
    def _extract_math_expressions(self, content: str) -> List[str]:
        """Extract mathematical expressions from text content."""
        expressions = []
        
        # Look for equations (contains =)
        equations = re.findall(r'[^=]+=.+', content)
        for eq in equations:
            expressions.append(eq.strip())
        
        # Look for formulas (contains mathematical operators)
        formulas = re.findall(r'[\w\d\s]+[+\-*/^][\w\d\s]+', content)
        for formula in formulas:
            if formula not in expressions:
                expressions.append(formula.strip())
        
        # Look for numbers with phi, pi, e
        special_nums = re.findall(r'\d+\.?\d*\s*[×*]?\s*(phi|pi|e)', content)
        for num in special_nums:
            expressions.append(num)
        
        return expressions
    
    def _get_consciousness_level(self, frequency: float) -> str:
        """Determine the consciousness level based on frequency."""
        for level, (min_freq, max_freq) in self.consciousness_levels.items():
            if min_freq <= frequency < max_freq:
                return level
        
        # Default to quantum for very high frequencies
        if frequency >= 2000:
            return "quantum"
        
        return "physical"


def main():
    """Main function to demonstrate the Quantum Phi-Math Analyzer."""
    analyzer = QuantumPhiMathAnalyzer()
    
    print("\n" + "="*80)
    print("Quantum Phi-Math Analyzer".center(80))
    print("="*80 + "\n")
    
    # Test individual numbers
    test_numbers = [
        PHI,            # Golden ratio
        PI,             # Pi
        E,              # Euler's number
        1.414213562,    # sqrt(2)
        1.732050808,    # sqrt(3)
        2.236067977,    # sqrt(5)
        1.0,            # Unity
        0.0,            # Zero
        5.0,            # Prime
        6.0,            # Composite
        8.0,            # Fibonacci
        13.0,           # Fibonacci prime
        PHI**2,         # Phi squared
        PHI**3,         # Phi cubed
        PHI**-1,        # Phi inverse
    ]
    
    print("Individual Number Analysis:")
    print("-"*80)
    for num in test_numbers:
        result = analyzer.calculate_number_frequency(num)
        print(f"{num:.8f}: Frequency={result['frequency']:.2f}Hz, "
              f"Resonance={result['resonance']:.4f}, "
              f"Level={result['consciousness_level']}, "
              f"Type={result['pattern_type']}")
    
    # Test mathematical expressions
    test_expressions = [
        "phi^2 = phi + 1",
        "e^(i*pi) + 1 = 0",
        "a^2 + b^2 = c^2",
        "F_n = (phi^n - (1-phi)^n)/sqrt(5)",
        "E = mc^2",
        "phi = (1 + sqrt(5))/2"
    ]
    
    print("\nMathematical Expression Analysis:")
    print("-"*80)
    for expr in test_expressions:
        result = analyzer.analyze_expression(expr)
        print(f"{expr}: Frequency={result['avg_frequency']:.2f}Hz, "
              f"Resonance={result['combined_resonance']:.4f}, "
              f"Level={result['consciousness_level']}")
    
    print("\nTo scan a directory of mathematical files, use:")
    print("python quantum_phi_math_analyzer.py /path/to/math/files")


if __name__ == "__main__":
    main()