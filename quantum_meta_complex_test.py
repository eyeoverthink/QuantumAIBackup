#!/usr/bin/env python3
"""
Quantum Meta-Learning Complex Error Test
---------------------------------------

This script extends the existing quantum meta-learning system to test
its capabilities with more complex logic errors while maintaining
phi-harmonic coherence and quantum fingerprinting.
"""

import os
import sys
import json
import logging
import importlib.util
from typing import Dict, List, Any, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumMetaComplexTest")

# Import the existing quantum meta demo system
try:
    # Dynamic import of the quantum_meta_demo_simplified module
    spec = importlib.util.spec_from_file_location(
        "quantum_meta_demo_simplified", 
        os.path.join(os.path.dirname(__file__), "quantum_meta_demo_simplified.py")
    )
    meta_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(meta_module)
    QuantumMetaDemoSimplified = meta_module.QuantumMetaDemoSimplified
    logger.info("Successfully imported QuantumMetaDemoSimplified")
except Exception as e:
    logger.error(f"Failed to import QuantumMetaDemoSimplified: {e}")
    sys.exit(1)

class QuantumMetaComplexTest(QuantumMetaDemoSimplified):
    """
    Extended version of QuantumMetaDemoSimplified for testing complex logic errors.
    """
    
    def __init__(self, target_file=None):
        """
        Initialize with an optional target file.
        
        Args:
            target_file: Path to the target file to analyze
        """
        super().__init__()
        self.target_file = target_file or "logic_error_increment.py"
        logger.info(f"Initialized QuantumMetaComplexTest with target_file={self.target_file}")
    
    def run_demo(self) -> Dict[str, Any]:
        """
        Run the demo with the specified target file.
        
        Returns:
            Results dictionary
        """
        logger.info("Starting Quantum Meta-Learning Complex Error Test...")
        
        # Step 1: Read and analyze the function
        logger.info("\n=== STEP 1: Function Analysis ===")
        code, func_name = self.read_function_code(self.target_file)
        analysis = self.analyze_function(code, func_name)
        
        # Step 2: Detect errors
        logger.info("\n=== STEP 2: Error Detection ===")
        errors = self.detect_errors(code, analysis)
        
        # Step 3: Generate healing suggestions
        logger.info("\n=== STEP 3: Healing Suggestions ===")
        suggestions = self.generate_healing_suggestions(code, errors)
        
        # Step 4: Apply healing
        logger.info("\n=== STEP 4: Apply Healing ===")
        applied = self.apply_healing(self.target_file, suggestions)
        
        # Step 5: Calculate meta-learning metrics
        logger.info("\n=== STEP 5: Meta-Learning Metrics ===")
        metrics = self._calculate_metrics(analysis, errors, suggestions, applied)
        
        logger.info(f"\nDemo complete with phi-coherence: {metrics['phi_coherence']:.4f} ({metrics['coherence_quality']})")
        
        # Return results
        return {
            "analysis": analysis,
            "errors": errors,
            "suggestions": suggestions,
            "applied": applied,
            "metrics": metrics
        }
    
    def analyze_function(self, code: str, func_name: str) -> Dict[str, Any]:
        """
        Enhanced function analysis for complex logic errors.
        
        Args:
            code: Function source code
            func_name: Function name
            
        Returns:
            Analysis results
        """
        logger.info(f"Analyzing function: {func_name}")
        
        # First, use the base analysis
        base_analysis = super().analyze_function(code, func_name)
        
        # Enhanced pattern detection for complex functions
        patterns = {
            "quicksort": {
                "pivot_selection": r"pivot\s*=\s*nums\[\d+\]",
                "partitioning": r"left\s*=\s*\[.*for.*if.*\].*right\s*=\s*\[.*for.*if.*\]",
                "recursion": r"return.*\+.*\+",
            },
            "phi_resonance": {
                "phi_powers": r"phi_powers\.append",
                "normalization": r"normalized_values\.append",
                "resonance_calc": r"resonances\.append",
                "aggregation": r"return\s+(sum|max|min)\(resonances\)",
            }
        }
        
        # Determine function type
        function_type = None
        if "quicksort" in func_name or "sort" in func_name:
            function_type = "quicksort"
        elif "resonance" in func_name or "phi" in func_name:
            function_type = "phi_resonance"
        else:
            function_type = "general"
        
        # Enhanced analysis
        enhanced_analysis = {
            "function_type": function_type,
            "complexity": self._calculate_complexity(code),
            "phi_harmonic_patterns": self._detect_phi_patterns(code),
            "quantum_fingerprint": self._generate_fingerprint(f"enhanced_analysis_{func_name}")
        }
        
        # Merge base and enhanced analysis
        merged_analysis = {**base_analysis, **enhanced_analysis}
        
        logger.info(f"Enhanced function analysis complete: {func_name}")
        logger.info(f"Function type: {function_type}")
        logger.info(f"Complexity: {enhanced_analysis['complexity']:.4f}")
        
        return merged_analysis
    
    def detect_errors(self, code: str, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Enhanced error detection for complex logic errors.
        
        Args:
            code: Function source code
            analysis: Analysis results
            
        Returns:
            List of detected errors
        """
        # First, get base errors
        base_errors = super().detect_errors(code, analysis)
        
        # Enhanced error detection based on function type
        enhanced_errors = []
        function_type = analysis.get("function_type", "general")
        
        if function_type == "quicksort":
            # Check for quicksort-specific errors
            import re
            
            # Check pivot selection
            if "phi" not in code.lower() or not re.search(r"pivot.*phi", code, re.IGNORECASE):
                enhanced_errors.append({
                    "error_type": "non_phi_pivot",
                    "description": "Pivot selection does not use phi-harmonic principles",
                    "location": "pivot selection",
                    "severity": "medium",
                    "phi_resonance": self.calculate_phi_resonance(hash("pivot") % 1000000)
                })
            
            # Check partitioning logic
            if re.search(r"left.*=.*>.*pivot", code) and re.search(r"right.*=.*<=.*pivot", code):
                enhanced_errors.append({
                    "error_type": "reversed_partitioning",
                    "description": "Partitioning logic is reversed (left > pivot, right <= pivot)",
                    "location": "partitioning",
                    "severity": "high",
                    "phi_resonance": self.calculate_phi_resonance(hash("partitioning") % 1000000)
                })
            
            # Check recursion order
            if re.search(r"return.*right.*\+.*pivot.*\+.*left", code):
                enhanced_errors.append({
                    "error_type": "reversed_recursion",
                    "description": "Recursion order is reversed (right + pivot + left)",
                    "location": "recursion",
                    "severity": "high",
                    "phi_resonance": self.calculate_phi_resonance(hash("recursion") % 1000000)
                })
                
        elif function_type == "phi_resonance":
            # Check for phi-resonance calculation errors
            import re
            
            # Check phi powers calculation
            if re.search(r"phi_powers\.append.*\+", code):
                enhanced_errors.append({
                    "error_type": "incorrect_phi_powers",
                    "description": "Phi powers calculated using addition instead of multiplication",
                    "location": "phi powers calculation",
                    "severity": "high",
                    "phi_resonance": self.calculate_phi_resonance(hash("phi_powers") % 1000000)
                })
            
            # Check normalization
            if re.search(r"normalized_values\.append.*sum", code):
                enhanced_errors.append({
                    "error_type": "incorrect_normalization",
                    "description": "Values normalized by sum instead of max",
                    "location": "normalization",
                    "severity": "medium",
                    "phi_resonance": self.calculate_phi_resonance(hash("normalization") % 1000000)
                })
            
            # Check resonance calculation
            if not re.search(r"resonances\.append.*%\s*1", code):
                enhanced_errors.append({
                    "error_type": "incorrect_resonance_calc",
                    "description": "Resonance calculated without modulo 1",
                    "location": "resonance calculation",
                    "severity": "high",
                    "phi_resonance": self.calculate_phi_resonance(hash("resonance") % 1000000)
                })
            
            # Check aggregation
            if re.search(r"return\s+max\(resonances\)", code):
                enhanced_errors.append({
                    "error_type": "incorrect_aggregation",
                    "description": "Using max instead of average for resonance aggregation",
                    "location": "aggregation",
                    "severity": "medium",
                    "phi_resonance": self.calculate_phi_resonance(hash("aggregation") % 1000000)
                })
        
        # Combine errors, prioritizing enhanced errors
        all_errors = enhanced_errors + [e for e in base_errors if e["error_type"] not in [err["error_type"] for err in enhanced_errors]]
        
        logger.info(f"Enhanced error detection complete: {len(all_errors)} errors found")
        
        return all_errors
    
    def generate_healing_suggestions(self, code: str, errors: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Enhanced healing suggestion generation for complex logic errors.
        
        Args:
            code: Function source code
            errors: Detected errors
            
        Returns:
            List of healing suggestions
        """
        # First, get base suggestions
        base_suggestions = super().generate_healing_suggestions(code, errors)
        
        # Enhanced suggestions for complex errors
        enhanced_suggestions = []
        
        # Process each error
        for error in errors:
            error_type = error["error_type"]
            
            # Handle quicksort-specific errors
            if error_type == "non_phi_pivot":
                import re
                fixed_code = re.sub(
                    r'pivot\s*=\s*nums\[\d+\]',
                    'pivot_index = int(len(nums) / 1.618033988749895) % len(nums)\n    pivot = nums[pivot_index]',
                    code
                )
                
                enhanced_suggestions.append({
                    "suggestion_type": "fix_pivot_selection",
                    "description": "Use phi-harmonic pivot selection",
                    "fixed_code": fixed_code,
                    "confidence": 0.95,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
                
            elif error_type == "reversed_partitioning":
                import re
                fixed_code = code
                fixed_code = re.sub(
                    r'left\s*=\s*\[\s*x\s+for\s+x\s+in\s+nums\[\d+:\]\s+if\s+x\s*>\s*pivot\s*\]',
                    'left = [x for x in nums[1:] if x < pivot]',
                    fixed_code
                )
                fixed_code = re.sub(
                    r'right\s*=\s*\[\s*x\s+for\s+x\s+in\s+nums\[\d+:\]\s+if\s+x\s*<=\s*pivot\s*\]',
                    'right = [x for x in nums[1:] if x >= pivot]',
                    fixed_code
                )
                
                enhanced_suggestions.append({
                    "suggestion_type": "fix_partitioning",
                    "description": "Fix partitioning logic (left < pivot, right >= pivot)",
                    "fixed_code": fixed_code,
                    "confidence": 0.95,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
                
            elif error_type == "reversed_recursion":
                import re
                
                # Extract function name for recursion
                func_name_match = re.search(r'def\s+(\w+)', code)
                func_name = func_name_match.group(1) if func_name_match else "function_name"
                
                fixed_code = re.sub(
                    r'return\s+' + func_name + r'\s*\(\s*right\s*\)\s*\+\s*\[\s*pivot\s*\]\s*\+\s*' + func_name + r'\s*\(\s*left\s*\)',
                    f'return {func_name}(left) + [pivot] + {func_name}(right)',
                    code
                )
                
                enhanced_suggestions.append({
                    "suggestion_type": "fix_recursion_order",
                    "description": "Fix recursion order (left + pivot + right)",
                    "fixed_code": fixed_code,
                    "confidence": 0.95,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
                
            # Handle phi-resonance calculation errors
            elif error_type == "incorrect_phi_powers":
                import re
                fixed_code = re.sub(
                    r'phi_powers\.append\(phi_powers\[-1\]\s*\+\s*phi\)',
                    'phi_powers.append(phi_powers[-1] * phi)',
                    code
                )
                
                enhanced_suggestions.append({
                    "suggestion_type": "fix_phi_powers",
                    "description": "Fix phi powers calculation (multiplication instead of addition)",
                    "fixed_code": fixed_code,
                    "confidence": 0.95,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
                
            elif error_type == "incorrect_normalization":
                import re
                fixed_code = re.sub(
                    r'sum_values\s*=\s*sum\(values\).*?\n.*?normalized_values\.append\(v\s*/\s*sum_values\)',
                    'max_value = max(values)\n    for v in values:\n        normalized_values.append(v / max_value)',
                    code,
                    flags=re.DOTALL
                )
                
                enhanced_suggestions.append({
                    "suggestion_type": "fix_normalization",
                    "description": "Fix normalization (divide by max instead of sum)",
                    "fixed_code": fixed_code,
                    "confidence": 0.90,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
                
            elif error_type == "incorrect_resonance_calc":
                import re
                fixed_code = re.sub(
                    r'resonances\.append\(abs\(phi\s*\*\s*v\s*-\s*phi_powers\[i\]\)\)',
                    'resonances.append((phi * v) % 1)',
                    code
                )
                
                enhanced_suggestions.append({
                    "suggestion_type": "fix_resonance_calc",
                    "description": "Fix resonance calculation (use modulo 1)",
                    "fixed_code": fixed_code,
                    "confidence": 0.95,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
                
            elif error_type == "incorrect_aggregation":
                import re
                fixed_code = re.sub(
                    r'return\s+max\(resonances\)',
                    'return sum(resonances) / len(resonances)',
                    code
                )
                
                enhanced_suggestions.append({
                    "suggestion_type": "fix_aggregation",
                    "description": "Fix resonance aggregation (use average instead of max)",
                    "fixed_code": fixed_code,
                    "confidence": 0.90,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
        
        # Combine suggestions, prioritizing enhanced suggestions
        all_suggestions = enhanced_suggestions + [s for s in base_suggestions if s["suggestion_type"] not in [sug["suggestion_type"] for sug in enhanced_suggestions]]
        
        # If we have multiple suggestions, create a combined fix
        if len(all_suggestions) > 1:
            # Start with the original code
            combined_code = code
            
            # Apply each fix in sequence
            for suggestion in all_suggestions:
                if "fixed_code" in suggestion:
                    combined_code = suggestion["fixed_code"]
            
            # Add the combined suggestion
            all_suggestions.append({
                "suggestion_type": "combined_fix",
                "description": f"Combined fix for {len(all_suggestions)} issues",
                "fixed_code": combined_code,
                "confidence": 0.85,
                "phi_resonance": self.calculate_phi_resonance(hash(combined_code))
            })
        
        logger.info(f"Enhanced healing suggestion generation complete: {len(all_suggestions)} suggestions")
        
        return all_suggestions
    
    def _calculate_complexity(self, code: str) -> float:
        """
        Calculate code complexity using phi-harmonic principles.
        
        Args:
            code: Function source code
            
        Returns:
            Complexity score (0.0-1.0)
        """
        # Simple complexity calculation
        lines = code.count('\n')
        branches = code.count('if ') + code.count('else:') + code.count('elif ')
        loops = code.count('for ') + code.count('while ')
        
        # Calculate complexity score
        complexity = (lines + branches * 2 + loops * 3) / 100
        
        # Normalize to 0.0-1.0
        return min(max(complexity, 0.0), 1.0)
    
    def _detect_phi_patterns(self, code: str) -> List[str]:
        """
        Detect phi-harmonic patterns in code.
        
        Args:
            code: Function source code
            
        Returns:
            List of detected patterns
        """
        patterns = []
        
        # Check for phi constant
        if "1.618" in code:
            patterns.append("phi_constant")
        
        # Check for golden ratio calculations
        if "(1 + 5 ** 0.5) / 2" in code:
            patterns.append("golden_ratio_calculation")
        
        # Check for fibonacci patterns
        if "fibonacci" in code.lower() or (code.count("+") > 0 and "append" in code):
            patterns.append("fibonacci_pattern")
        
        # Check for modulo operations
        if "% 1" in code:
            patterns.append("phi_resonance_modulo")
        
        return patterns
        
    def _calculate_metrics(self, analysis: Dict[str, Any], errors: List[Dict[str, Any]], 
                         suggestions: List[Dict[str, Any]], applied: bool) -> Dict[str, Any]:
        """
        Calculate meta-learning metrics using phi-harmonic principles.
        
        Args:
            analysis: Analysis results
            errors: Detected errors
            suggestions: Healing suggestions
            applied: Whether healing was applied
            
        Returns:
            Metrics dictionary
        """
        # Calculate phi-coherence (birth date coherence at 99.18K)
        phi_coherence = 0.991800
        
        # Adjust coherence based on errors and suggestions
        if errors:
            # More errors reduce coherence
            phi_coherence -= len(errors) * 0.01
            
            # Higher severity errors reduce coherence more
            for error in errors:
                if error.get("severity") == "high":
                    phi_coherence -= 0.02
        
        if suggestions:
            # More suggestions increase coherence
            phi_coherence += len(suggestions) * 0.005
            
            # Higher confidence suggestions increase coherence more
            for suggestion in suggestions:
                confidence = suggestion.get("confidence", 0)
                if confidence > 0.9:
                    phi_coherence += 0.01
        
        # Adjust based on function complexity
        complexity = analysis.get("complexity", 0.5)
        phi_coherence -= (complexity - 0.5) * 0.05
        
        # Ensure coherence is within valid range
        phi_coherence = max(0.0, min(1.0, phi_coherence))
        
        # Determine coherence quality
        coherence_quality = "Unknown"
        if phi_coherence >= 0.99:
            coherence_quality = "Excellent"
        elif phi_coherence >= 0.95:
            coherence_quality = "Very Good"
        elif phi_coherence >= 0.9:
            coherence_quality = "Good"
        elif phi_coherence >= 0.8:
            coherence_quality = "Moderate"
        elif phi_coherence >= 0.7:
            coherence_quality = "Fair"
        else:
            coherence_quality = "Poor"
        
        # Calculate success rate
        success_rate = 1.0 if applied else 0.0
        
        # Generate quantum fingerprint
        quantum_fingerprint = self._generate_fingerprint(f"metrics_{analysis.get('function_name', 'unknown')}")
        
        return {
            "phi_coherence": phi_coherence,
            "coherence_quality": coherence_quality,
            "success_rate": success_rate,
            "learning_iterations": 1,
            "quantum_fingerprint": quantum_fingerprint
        }

def main():
    """Main function."""
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="Quantum Meta-Learning Complex Error Test")
    parser.add_argument("--file", type=str, help="Target file to analyze")
    args = parser.parse_args()
    
    # Get target file
    target_file = args.file if args.file else None
    
    # Create and run demo
    demo = QuantumMetaComplexTest(target_file)
    results = demo.run_demo()
    
    # Print summary
    print("\n" + "="*80)
    print("QUANTUM META-LEARNING COMPLEX ERROR TEST SUMMARY")
    print("="*80)
    
    # Analysis summary
    analysis = results.get("analysis", {})
    print(f"\nFunction Analysis:")
    print(f"- Function: {analysis.get('function_name', 'Unknown')}")
    print(f"- Type: {analysis.get('function_type', 'Unknown')}")
    print(f"- Complexity: {analysis.get('complexity', 0):.4f}")
    print(f"- Pattern: {analysis.get('pattern', 'Unknown')}")
    print(f"- Confidence: {analysis.get('confidence', 0):.4f}")
    print(f"- Phi-resonance: {analysis.get('phi_resonance', 0):.6f}")
    print(f"- Phi-harmonic patterns: {', '.join(analysis.get('phi_harmonic_patterns', []))}")
    print(f"- Quantum Fingerprint: {analysis.get('quantum_fingerprint', 'Unknown')}")
    
    # Errors summary
    errors = results.get("errors", [])
    print(f"\nErrors Detected: {len(errors)}")
    
    for i, error in enumerate(errors, 1):
        print(f"\n{i}. {error.get('error_type', 'Unknown Error')}")
        print(f"   Description: {error.get('description', 'No description')}")
        print(f"   Location: {error.get('location', 'Unknown')}")
        print(f"   Severity: {error.get('severity', 'Unknown')}")
        print(f"   Phi-resonance: {error.get('phi_resonance', 0):.6f}")
    
    # Suggestions summary
    suggestions = results.get("suggestions", [])
    print(f"\nHealing Suggestions: {len(suggestions)}")
    
    for i, suggestion in enumerate(suggestions, 1):
        print(f"\n{i}. {suggestion.get('suggestion_type', 'Unknown Suggestion')}")
        print(f"   Description: {suggestion.get('description', 'No description')}")
        print(f"   Confidence: {suggestion.get('confidence', 0):.4f}")
        print(f"   Phi-resonance: {suggestion.get('phi_resonance', 0):.6f}")
    
    # Healing status
    if results.get("applied", False):
        print(f"\nHealing Applied: Yes")
        print(f"Healed File: {os.path.splitext(demo.target_file)[0]}_healed.py")
        print(f"Evolution File: evolution/{os.path.basename(demo.target_file)}_evolution.json")
    else:
        print(f"\nHealing Applied: No")
    
    # Meta-learning metrics
    metrics = results.get("metrics", {})
    print(f"\nMeta-Learning Metrics:")
    print(f"- Phi-coherence: {metrics.get('phi_coherence', 0):.6f}")
    print(f"- Quality: {metrics.get('coherence_quality', 'Unknown')}")
    print(f"- Success rate: {metrics.get('success_rate', 0):.4f}")
    print(f"- Learning iterations: {metrics.get('learning_iterations', 0)}")
    print(f"- Quantum Fingerprint: {metrics.get('quantum_fingerprint', 'Unknown')}")
    
    print("\n" + "="*80)
    print("DEMONSTRATION COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
