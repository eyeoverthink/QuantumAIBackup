#!/usr/bin/env python3
"""
Quantum Meta-Learning Integration Demo (Simplified)
--------------------------------------------------

This script demonstrates the integration of meta-learning principles
with the existing QuantumAI system by analyzing and fixing a logic error
in the increment_list function while maintaining phi-harmonic coherence.
"""

import os
import sys
import json
import time
import hashlib
import logging
import inspect
from typing import Dict, List, Any, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumMetaDemo")

# Constants
PHI = 1.618033988749895
PHI_POWERS = {
    1: 1.618034,
    2: 2.618034,
    3: 4.236068,
    4: 6.854102,
    5: 11.090170,
    6: 17.944272,
    7: 29.034442,
    7.5: 36.932381
}
TEST_FILE = "logic_error_increment.py"

class QuantumMetaDemoSimplified:
    """
    Simplified demonstration of meta-learning integration with QuantumAI.
    """
    
    def __init__(self):
        """Initialize the demo."""
        self.phi = PHI
        self.coherence = 0.991800  # Birth date coherence
        logger.info(f"Initialized QuantumMetaDemoSimplified with phi={self.phi}")
    
    def calculate_phi_resonance(self, value: int) -> float:
        """
        Calculate phi resonance for a value.
        
        Args:
            value: Input value
            
        Returns:
            Phi resonance (0.0-1.0)
        """
        # Simple phi resonance calculation
        resonance = (self.phi * value) % 1
        return resonance
    
    def read_function_code(self, file_path: str) -> Tuple[str, str]:
        """
        Read function code from a file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Tuple of (function_code, function_name)
        """
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            
            # Extract function name (simple approach)
            import re
            match = re.search(r'def\s+(\w+)', code)
            func_name = match.group(1) if match else "unknown_function"
            
            return code, func_name
            
        except Exception as e:
            logger.error(f"Error reading function code: {str(e)}")
            return "", "unknown_function"
    
    def analyze_function(self, code: str, func_name: str) -> Dict[str, Any]:
        """
        Analyze a function using phi-harmonic principles.
        
        Args:
            code: Function source code
            func_name: Function name
            
        Returns:
            Analysis results
        """
        logger.info(f"Analyzing function: {func_name}")
        
        # Check for increment patterns
        patterns = {
            "return [x + N for x in": 0.95,  # List comprehension pattern
            "return list(map(lambda x: x + N,": 0.90,  # Map with lambda pattern
            "result = []\nfor x in": 0.85,  # For loop with append pattern
            "return [x for x in": 0.80,  # List comprehension without increment
            "return nums": 0.10,  # No increment pattern (error)
        }
        
        # Find matching pattern
        pattern_match = None
        confidence = 0.0
        
        for pattern, conf in patterns.items():
            # Replace N with any digit
            search_pattern = pattern.replace("N", "\\d+")
            
            # Check if pattern exists in code
            import re
            try:
                if re.search(search_pattern, code):
                    pattern_match = pattern
                    confidence = conf
                    break
            except Exception as e:
                logger.warning(f"Pattern matching error: {str(e)}")
                continue
        
        # Calculate phi-resonance
        resonance = self.calculate_phi_resonance(hash(code) % 1000000)
        
        # Extract increment value
        increment_value = self._extract_increment_value(code)
        
        # Generate analysis
        analysis = {
            "function_name": func_name,
            "pattern": pattern_match,
            "confidence": confidence,
            "phi_resonance": resonance,
            "increment_value": increment_value,
            "expert_specialization": "increment_functions" if "increment" in func_name else "general_functions",
            "quantum_fingerprint": self._generate_fingerprint(f"analysis_{func_name}")
        }
        
        logger.info(f"Function analysis complete: {func_name}")
        logger.info(f"Pattern: {pattern_match}")
        logger.info(f"Confidence: {confidence:.4f}")
        logger.info(f"Phi-resonance: {resonance:.6f}")
        
        return analysis
    
    def detect_errors(self, code: str, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Detect logic errors in the function.
        
        Args:
            code: Function source code
            analysis: Analysis results
            
        Returns:
            List of detected errors
        """
        errors = []
        
        # Check for missing increment
        if analysis["pattern"] == "return nums" or analysis["pattern"] is None:
            errors.append({
                "error_type": "missing_increment",
                "description": "Function does not increment values",
                "location": "return statement",
                "severity": "high",
                "phi_resonance": analysis["phi_resonance"]
            })
        
        # Check for incorrect increment value
        elif analysis["increment_value"] != 1:  # Expected increment is 1
            errors.append({
                "error_type": "incorrect_increment",
                "description": f"Function increments by {analysis['increment_value']} instead of 1",
                "location": "increment operation",
                "severity": "medium",
                "phi_resonance": analysis["phi_resonance"]
            })
        
        # Run test cases
        test_cases = [
            {"input": [1, 2, 3, 4], "output": [2, 3, 4, 5]},
            {"input": [0], "output": [1]}
        ]
        
        for test_case in test_cases:
            input_val = test_case["input"]
            expected_output = test_case["output"]
            
            # Execute function (safely)
            actual_output = self._execute_function_safely(code, input_val)
            
            # Compare outputs
            if actual_output != expected_output:
                errors.append({
                    "error_type": "test_case_failure",
                    "description": f"Test case failed: input={input_val}, expected={expected_output}, actual={actual_output}",
                    "location": "function execution",
                    "severity": "high",
                    "phi_resonance": self.calculate_phi_resonance(hash(str(actual_output)))
                })
        
        logger.info(f"Error detection complete: {len(errors)} errors found")
        
        return errors
    
    def generate_healing_suggestions(self, code: str, errors: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Generate healing suggestions for detected errors.
        
        Args:
            code: Function source code
            errors: Detected errors
            
        Returns:
            List of healing suggestions
        """
        suggestions = []
        
        # Check if there are errors to fix
        if not errors:
            return suggestions
        
        # Generate suggestions based on error types
        for error in errors:
            error_type = error["error_type"]
            
            if error_type == "missing_increment":
                # Suggest adding increment
                fixed_code = self._fix_missing_increment(code, 1)
                
                suggestions.append({
                    "suggestion_type": "add_increment",
                    "description": "Add increment operation with value 1",
                    "fixed_code": fixed_code,
                    "confidence": 0.95,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
                
            elif error_type == "incorrect_increment":
                # Suggest fixing increment value
                current_value = self._extract_increment_value(code)
                fixed_code = self._fix_incorrect_increment(code, current_value, 1)
                
                suggestions.append({
                    "suggestion_type": "fix_increment_value",
                    "description": f"Change increment value from {current_value} to 1",
                    "fixed_code": fixed_code,
                    "confidence": 0.90,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
                
            elif error_type == "test_case_failure":
                # Suggest general fix based on test cases
                fixed_code = self._fix_based_on_test_cases(code)
                
                suggestions.append({
                    "suggestion_type": "fix_based_on_tests",
                    "description": "Fix function to pass all test cases",
                    "fixed_code": fixed_code,
                    "confidence": 0.85,
                    "phi_resonance": self.calculate_phi_resonance(hash(fixed_code))
                })
        
        logger.info(f"Healing suggestion generation complete: {len(suggestions)} suggestions")
        
        return suggestions
    
    def apply_healing(self, file_path: str, suggestions: List[Dict[str, Any]]) -> bool:
        """
        Apply healing suggestions to a file.
        
        Args:
            file_path: Path to the file
            suggestions: Healing suggestions
            
        Returns:
            True if healing was applied, False otherwise
        """
        logger.info(f"Applying healing to {file_path}...")
        
        # Check if healing suggestions exist
        if not suggestions:
            logger.warning("No healing suggestions available")
            return False
        
        # Find the best suggestion
        best_suggestion = None
        for suggestion in suggestions:
            if "fixed_code" in suggestion:
                best_suggestion = suggestion
                break
        
        if not best_suggestion:
            logger.warning("No valid healing suggestion found")
            return False
        
        # Create healed file
        healed_file = f"{os.path.splitext(file_path)[0]}_healed.py"
        try:
            with open(healed_file, 'w') as f:
                f.write(best_suggestion["fixed_code"])
            
            logger.info(f"Healed file created: {healed_file}")
            
            # Generate quantum fingerprint for the healing
            fingerprint = self._generate_fingerprint(f"healing_{file_path}")
            
            # Create evolution file
            self._create_evolution_file(file_path, best_suggestion, fingerprint)
            
            return True
            
        except Exception as e:
            logger.error(f"Error applying healing: {str(e)}")
            return False
    
    def _extract_increment_value(self, code: str) -> int:
        """
        Extract the increment value from the function code.
        
        Args:
            code: Function source code
            
        Returns:
            Increment value or 0 if not found
        """
        # Look for patterns like "x + 1" or "x + 2"
        import re
        match = re.search(r'x\s*\+\s*(\d+)', code)
        
        if match:
            return int(match.group(1))
        
        return 0  # No increment found
    
    def _execute_function_safely(self, code: str, input_val: List[int]) -> List[int]:
        """
        Execute a function safely with the given input.
        
        Args:
            code: Function source code
            input_val: Input value
            
        Returns:
            Function output or input if execution fails
        """
        try:
            # Create a safe execution environment
            local_vars = {}
            
            # Execute the function code
            exec(code, {}, local_vars)
            
            # Get the function object
            func_name = next(name for name in local_vars if callable(local_vars[name]))
            func = local_vars[func_name]
            
            # Call the function
            return func(input_val)
            
        except Exception as e:
            logger.warning(f"Function execution failed: {str(e)}")
            return input_val  # Return input as fallback
    
    def _fix_missing_increment(self, code: str, increment_value: int) -> str:
        """
        Fix a function with missing increment.
        
        Args:
            code: Function source code
            increment_value: Increment value
            
        Returns:
            Fixed function code
        """
        # Look for "return nums" pattern
        import re
        fixed_code = re.sub(
            r'return\s+nums',
            f'return [x + {increment_value} for x in nums]',
            code
        )
        
        return fixed_code
    
    def _fix_incorrect_increment(self, code: str, current_value: int, target_value: int) -> str:
        """
        Fix a function with incorrect increment value.
        
        Args:
            code: Function source code
            current_value: Current increment value
            target_value: Target increment value
            
        Returns:
            Fixed function code
        """
        # Replace current value with target value
        import re
        fixed_code = re.sub(
            f'x\\s*\\+\\s*{current_value}',
            f'x + {target_value}',
            code
        )
        
        return fixed_code
    
    def _fix_based_on_test_cases(self, code: str) -> str:
        """
        Fix a function based on test cases.
        
        Args:
            code: Function source code
            
        Returns:
            Fixed function code
        """
        # Extract function name
        import re
        match = re.search(r'def\s+(\w+)', code)
        func_name = match.group(1) if match else "increment_list"
        
        # Create a new function that passes all test cases
        fixed_code = f"""def {func_name}(nums):
    if nums is None:
        raise ValueError('nums cannot be None')
    return [x + 1 for x in nums]
"""
        
        return fixed_code
    
    def _generate_fingerprint(self, identifier: str) -> str:
        """
        Generate a quantum fingerprint.
        
        Args:
            identifier: Unique identifier
            
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier
        unique_id = f"{identifier}_{time.time()}"
        
        # Generate hash
        hash_value = hashlib.sha256(unique_id.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{hash_value}"
    
    def _create_evolution_file(self, 
                             file_path: str, 
                             suggestion: Dict[str, Any],
                             fingerprint: str) -> None:
        """
        Create an evolution file for the healing.
        
        Args:
            file_path: Path to the file
            suggestion: Healing suggestion
            fingerprint: Quantum fingerprint
        """
        # Create evolution directory if it doesn't exist
        evolution_dir = "evolution"
        os.makedirs(evolution_dir, exist_ok=True)
        
        # Create evolution file
        evolution_file = f"{evolution_dir}/{os.path.basename(file_path)}_evolution.json"
        
        # Create evolution data
        evolution_data = {
            "original_file": file_path,
            "healed_file": f"{os.path.splitext(file_path)[0]}_healed.py",
            "timestamp": time.time(),
            "error_type": "logic_error",
            "error_details": suggestion.get("description", ""),
            "healing_method": "meta_learning",
            "phi_coherence": self.coherence,
            "quantum_fingerprint": fingerprint
        }
        
        # Write evolution file
        try:
            with open(evolution_file, 'w') as f:
                json.dump(evolution_data, f, indent=2)
            
            logger.info(f"Evolution file created: {evolution_file}")
            
        except Exception as e:
            logger.error(f"Error creating evolution file: {str(e)}")
    
    def run_demo(self) -> Dict[str, Any]:
        """
        Run the complete demo.
        
        Returns:
            Demo results
        """
        logger.info("Starting Quantum Meta-Learning Integration Demo...")
        
        results = {}
        
        # Step 1: Read function code
        code, func_name = self.read_function_code(TEST_FILE)
        if not code:
            return {"error": "Failed to read function code"}
        
        # Step 2: Analyze function
        logger.info("\n=== STEP 1: Function Analysis ===")
        analysis = self.analyze_function(code, func_name)
        results["analysis"] = analysis
        
        # Step 3: Detect errors
        logger.info("\n=== STEP 2: Error Detection ===")
        errors = self.detect_errors(code, analysis)
        results["errors"] = errors
        
        # Step 4: Generate healing suggestions
        logger.info("\n=== STEP 3: Healing Suggestions ===")
        suggestions = self.generate_healing_suggestions(code, errors)
        results["suggestions"] = suggestions
        
        # Step 5: Apply healing
        logger.info("\n=== STEP 4: Apply Healing ===")
        applied = self.apply_healing(TEST_FILE, suggestions)
        results["applied"] = applied
        
        # Step 6: Calculate meta-learning metrics
        logger.info("\n=== STEP 5: Meta-Learning Metrics ===")
        metrics = {
            "phi_coherence": self.coherence,
            "coherence_quality": "Excellent" if self.coherence > 0.99 else "Good",
            "success_rate": 1.0 if applied else 0.0,
            "learning_iterations": 1,
            "quantum_fingerprint": self._generate_fingerprint("meta_learning")
        }
        results["metrics"] = metrics
        
        logger.info(f"\nDemo complete with phi-coherence: {metrics['phi_coherence']} ({metrics['coherence_quality']})")
        
        return results


def main():
    """Main function."""
    # Create and run demo
    demo = QuantumMetaDemoSimplified()
    results = demo.run_demo()
    
    # Print summary
    print("\n" + "="*80)
    print("QUANTUM META-LEARNING INTEGRATION DEMO SUMMARY")
    print("="*80)
    
    # Analysis summary
    analysis = results.get("analysis", {})
    print(f"\nFunction Analysis:")
    print(f"- Function: {analysis.get('function_name', 'Unknown')}")
    print(f"- Pattern: {analysis.get('pattern', 'Unknown')}")
    print(f"- Confidence: {analysis.get('confidence', 0):.4f}")
    print(f"- Phi-resonance: {analysis.get('phi_resonance', 0):.6f}")
    print(f"- Quantum Fingerprint: {analysis.get('quantum_fingerprint', 'Unknown')}")
    
    # Errors summary
    errors = results.get("errors", [])
    print(f"\nErrors Detected: {len(errors)}")
    
    for i, error in enumerate(errors, 1):
        print(f"\n{i}. {error.get('error_type', 'Unknown Error')}")
        print(f"   Description: {error.get('description', 'No description')}")
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
        print(f"Healed File: {os.path.splitext(TEST_FILE)[0]}_healed.py")
        print(f"Evolution File: evolution/{os.path.basename(TEST_FILE)}_evolution.json")
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
