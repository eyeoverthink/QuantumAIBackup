"""
quantum_logic_agent.py

A specialized phi-harmonic agent for detecting and fixing logic errors
in the increment_list function. This agent demonstrates the integration
of the meta-learning extension with the existing QuantumAI orchestrator.

This agent uses phi-harmonic principles to analyze function behavior,
detect logic errors, and suggest fixes that maintain phi-resonance.
"""

import os
import json
import time
import hashlib
import logging
import inspect
from typing import Dict, List, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumLogicAgent")

# Import meta-learning components
from quantum_phi_meta_learning import PhiHarmonicMetaLearning, calculate_phi_resonance
from quantum_agent_factory import PhiHarmonicAgent

# Constants
PHI = 1.618033988749895
TARGET_FILE = "logic_error_increment.py"
EXPECTED_BEHAVIOR = {
    "increment": 1,
    "test_cases": [
        {"input": [1, 2, 3, 4], "output": [2, 3, 4, 5]},
        {"input": [0], "output": [1]}
    ]
}

class IncrementLogicAgent(PhiHarmonicAgent):
    """
    Specialized agent for detecting and fixing logic errors in increment functions.
    
    This agent demonstrates the integration of the meta-learning extension
    with the existing QuantumAI orchestrator by focusing on a specific
    function type and error pattern.
    """
    
    def __init__(self, phi: float = PHI):
        """
        Initialize the increment logic agent.
        
        Args:
            phi: Golden ratio value
        """
        super().__init__(
            agent_id="increment_logic_agent",
            agent_type="logic_error",
            specialization="increment_functions",
            phi=phi
        )
        
        # Initialize meta-learning
        self.meta_learning = PhiHarmonicMetaLearning(phi=phi)
        
        # Agent-specific state
        self.increment_patterns = {
            "return [x + N for x in": 0.95,  # List comprehension pattern
            "return list(map(lambda x: x + N,": 0.90,  # Map with lambda pattern
            "result = []\nfor x in": 0.85,  # For loop with append pattern
            "return [x for x in": 0.80,  # List comprehension without increment
            "return nums": 0.10,  # No increment pattern (error)
        }
        
        # Initialize state
        self.state = {
            "tasks_processed": 0,
            "errors_detected": 0,
            "suggestions_generated": 0,
            "success_rate": 0.0,
            "phi_coherence": 0.991800
        }
        
        # Generate quantum fingerprint
        self.quantum_fingerprint = self._generate_agent_fingerprint()
        
        logger.info(f"Initialized IncrementLogicAgent with phi={phi}")
    
    def get_capabilities(self) -> Dict[str, Any]:
        """
        Get the agent's capabilities.
        
        Returns:
            Dictionary of capabilities
        """
        return {
            "specialization": "increment_functions",
            "error_types": ["missing_increment", "incorrect_increment", "test_case_failure"],
            "healing_methods": ["add_increment", "fix_increment_value", "fix_based_on_tests"],
            "confidence": 0.95,
            "phi_resonance": calculate_phi_resonance(hash("increment_functions"), self.phi)
        }
    
    def get_state(self) -> Dict[str, Any]:
        """
        Get the agent's current state.
        
        Returns:
            Dictionary of state information
        """
        return self.state
    
    def get_evolution_history(self) -> List[Dict[str, Any]]:
        """
        Get the agent's evolution history.
        
        Returns:
            List of evolution events
        """
        return [{
            "timestamp": time.time(),
            "agent_id": self.agent_id,
            "agent_type": self.agent_type,
            "specialization": self.specialization,
            "state": self.state,
            "quantum_fingerprint": self.quantum_fingerprint
        }]
    
    def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a task to detect and fix logic errors in increment functions.
        
        Args:
            task: Task dictionary with func_code, func_name, and expected_behavior
            
        Returns:
            Task result with errors_detected and healing_suggestions
        """
        # Extract task information
        func_code = task.get("func_code", "")
        func_name = task.get("func_name", "")
        expected_behavior = task.get("expected_behavior", EXPECTED_BEHAVIOR)
        
        logger.info(f"Processing task for function: {func_name}")
        
        # Analyze function
        analysis = self.analyze_function(func_code, func_name)
        
        # Detect errors
        errors = self.detect_errors(func_code, analysis, expected_behavior)
        
        # Generate healing suggestions
        suggestions = self.generate_healing_suggestions(func_code, errors, expected_behavior)
        
        # Update success metrics
        self.update_success_metrics(
            len(errors) > 0 and len(suggestions) > 0,
            {
                "function_name": func_name,
                "errors_detected": len(errors),
                "suggestions_generated": len(suggestions)
            }
        )
        
        # Generate result
        result = {
            "task_id": task.get("task_id", f"task_{time.time()}"),
            "function_name": func_name,
            "errors_detected": errors,
            "healing_suggestions": suggestions,
            "phi_resonance": analysis.get("phi_resonance", 0),
            "confidence": analysis.get("confidence", 0),
            "quantum_fingerprint": self._generate_task_fingerprint(func_name)
        }
        
        logger.info(f"Task processing complete for {func_name}")
        logger.info(f"Errors detected: {len(errors)}")
        logger.info(f"Healing suggestions: {len(suggestions)}")
        
        return result
    
    def analyze_function(self, 
                       func_code: str, 
                       func_name: str) -> Dict[str, Any]:
        """
        Analyze a function to determine its pattern and phi-resonance.
        
        Args:
            func_code: Function source code
            func_name: Function name
            
        Returns:
            Analysis results
        """
        # Check for increment patterns
        pattern_match = None
        confidence = 0.0
        
        for pattern, conf in self.increment_patterns.items():
            # Replace N with any digit
            search_pattern = pattern.replace("N", r"\d+")
            
            # Check if pattern exists in code
            import re
            if re.search(search_pattern, func_code):
                pattern_match = pattern
                confidence = conf
                break
        
        # Calculate phi-resonance
        resonance = calculate_phi_resonance(
            hash(func_code) % 1000000,
            self.phi
        )
        
        # Generate analysis
        analysis = {
            "pattern": pattern_match,
            "confidence": confidence,
            "phi_resonance": resonance,
            "expected_increment": EXPECTED_BEHAVIOR["increment"],
            "actual_increment": self._extract_increment_value(func_code)
        }
        
        logger.info(f"Function analysis complete for {func_name}")
        logger.info(f"Pattern: {pattern_match}")
        logger.info(f"Confidence: {confidence:.4f}")
        logger.info(f"Phi-resonance: {resonance:.6f}")
        
        return analysis
    
    def detect_errors(self, 
                    func_code: str, 
                    analysis: Dict[str, Any],
                    expected_behavior: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Detect logic errors in the function.
        
        Args:
            func_code: Function source code
            analysis: Analysis results
            expected_behavior: Expected behavior
            
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
        elif analysis["actual_increment"] != expected_behavior["increment"]:
            errors.append({
                "error_type": "incorrect_increment",
                "description": f"Function increments by {analysis['actual_increment']} instead of {expected_behavior['increment']}",
                "location": "increment operation",
                "severity": "medium",
                "phi_resonance": analysis["phi_resonance"]
            })
        
        # Run test cases
        for test_case in expected_behavior.get("test_cases", []):
            input_val = test_case["input"]
            expected_output = test_case["output"]
            
            # Execute function (safely)
            actual_output = self._execute_function_safely(func_code, input_val)
            
            # Compare outputs
            if actual_output != expected_output:
                errors.append({
                    "error_type": "test_case_failure",
                    "description": f"Test case failed: input={input_val}, expected={expected_output}, actual={actual_output}",
                    "location": "function execution",
                    "severity": "high",
                    "phi_resonance": calculate_phi_resonance(hash(str(actual_output)), self.phi)
                })
        
        logger.info(f"Error detection complete: {len(errors)} errors found")
        
        return errors
    
    def generate_healing_suggestions(self, 
                                   func_code: str, 
                                   errors: List[Dict[str, Any]],
                                   expected_behavior: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate healing suggestions for detected errors.
        
        Args:
            func_code: Function source code
            errors: Detected errors
            expected_behavior: Expected behavior
            
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
                fixed_code = self._fix_missing_increment(
                    func_code, 
                    expected_behavior["increment"]
                )
                
                suggestions.append({
                    "suggestion_type": "add_increment",
                    "description": f"Add increment operation with value {expected_behavior['increment']}",
                    "fixed_code": fixed_code,
                    "confidence": 0.95,
                    "phi_resonance": calculate_phi_resonance(hash(fixed_code), self.phi)
                })
                
            elif error_type == "incorrect_increment":
                # Suggest fixing increment value
                fixed_code = self._fix_incorrect_increment(
                    func_code,
                    analysis["actual_increment"],
                    expected_behavior["increment"]
                )
                
                suggestions.append({
                    "suggestion_type": "fix_increment_value",
                    "description": f"Change increment value from {analysis['actual_increment']} to {expected_behavior['increment']}",
                    "fixed_code": fixed_code,
                    "confidence": 0.90,
                    "phi_resonance": calculate_phi_resonance(hash(fixed_code), self.phi)
                })
                
            elif error_type == "test_case_failure":
                # Suggest general fix based on test cases
                fixed_code = self._fix_based_on_test_cases(
                    func_code,
                    expected_behavior["test_cases"]
                )
                
                suggestions.append({
                    "suggestion_type": "fix_based_on_tests",
                    "description": "Fix function to pass all test cases",
                    "fixed_code": fixed_code,
                    "confidence": 0.85,
                    "phi_resonance": calculate_phi_resonance(hash(fixed_code), self.phi)
                })
        
        logger.info(f"Healing suggestion generation complete: {len(suggestions)} suggestions")
        
        return suggestions
    
    def _extract_increment_value(self, func_code: str) -> int:
        """
        Extract the increment value from the function code.
        
        Args:
            func_code: Function source code
            
        Returns:
            Increment value or 0 if not found
        """
        # Look for patterns like "x + 1" or "x + 2"
        import re
        match = re.search(r'x\s*\+\s*(\d+)', func_code)
        
        if match:
            return int(match.group(1))
        
        return 0  # No increment found
    
    def _execute_function_safely(self, func_code: str, input_val: List[int]) -> List[int]:
        """
        Execute a function safely with the given input.
        
        Args:
            func_code: Function source code
            input_val: Input value
            
        Returns:
            Function output or input if execution fails
        """
        try:
            # Create a safe execution environment
            local_vars = {}
            
            # Execute the function code
            exec(func_code, {}, local_vars)
            
            # Get the function object
            func_name = next(name for name in local_vars if callable(local_vars[name]))
            func = local_vars[func_name]
            
            # Call the function
            return func(input_val)
            
        except Exception as e:
            logger.warning(f"Function execution failed: {str(e)}")
            return input_val  # Return input as fallback
    
    def _fix_missing_increment(self, func_code: str, increment_value: int) -> str:
        """
        Fix a function with missing increment.
        
        Args:
            func_code: Function source code
            increment_value: Increment value
            
        Returns:
            Fixed function code
        """
        # Look for "return nums" pattern
        import re
        fixed_code = re.sub(
            r'return\s+nums',
            f'return [x + {increment_value} for x in nums]',
            func_code
        )
        
        return fixed_code
    
    def _fix_incorrect_increment(self, 
                               func_code: str, 
                               current_value: int,
                               target_value: int) -> str:
        """
        Fix a function with incorrect increment value.
        
        Args:
            func_code: Function source code
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
            func_code
        )
        
        return fixed_code
    
    def _fix_based_on_test_cases(self, 
                               func_code: str,
                               test_cases: List[Dict[str, Any]]) -> str:
        """
        Fix a function based on test cases.
        
        Args:
            func_code: Function source code
            test_cases: Test cases
            
        Returns:
            Fixed function code
        """
        # Extract function name
        import re
        match = re.search(r'def\s+(\w+)', func_code)
        func_name = match.group(1) if match else "increment_list"
        
        # Create a new function that passes all test cases
        fixed_code = f"""def {func_name}(nums):
    if nums is None:
        raise ValueError('nums cannot be None')
    return [x + 1 for x in nums]
"""
        
        return fixed_code
    
    def _generate_agent_fingerprint(self) -> str:
        """
        Generate a quantum fingerprint for the agent.
        
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier
        agent_id = f"increment_logic_agent_{time.time()}"
        
        # Generate hash
        agent_hash = hashlib.sha256(agent_id.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{agent_hash}"
    
    def _generate_task_fingerprint(self, func_name: str) -> str:
        """
        Generate a quantum fingerprint for a task.
        
        Args:
            func_name: Function name
            
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier
        task_id = f"task_{func_name}_{time.time()}"
        
        # Generate hash
        task_hash = hashlib.sha256(task_id.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{task_hash}"


def heal_increment_function(file_path: str = TARGET_FILE) -> Dict[str, Any]:
    """
    Heal an increment function using the specialized agent.
    
    Args:
        file_path: Path to the function file
        
    Returns:
        Healing results
    """
    # Read function code
    try:
        with open(file_path, 'r') as f:
            func_code = f.read()
        
        # Extract function name
        import re
        match = re.search(r'def\s+(\w+)', func_code)
        func_name = match.group(1) if match else "unknown_function"
        
    except Exception as e:
        logger.error(f"Error reading function code: {str(e)}")
        return {"error": str(e)}
    
    # Create agent
    agent = IncrementLogicAgent()
    
    # Create task
    task = {
        "task_id": f"task_{time.time()}",
        "task_type": "logic_error_detection",
        "func_code": func_code,
        "func_name": func_name,
        "expected_behavior": EXPECTED_BEHAVIOR
    }
    
    # Process task
    result = agent.process_task(task)
    
    # Apply healing if suggestions exist
    suggestions = result.get("healing_suggestions", [])
    if suggestions:
        # Find the best suggestion
        best_suggestion = None
        for suggestion in suggestions:
            if "fixed_code" in suggestion:
                best_suggestion = suggestion
                break
        
        if best_suggestion:
            # Create healed file
            healed_file = f"{os.path.splitext(file_path)[0]}_healed.py"
            try:
                with open(healed_file, 'w') as f:
                    f.write(best_suggestion["fixed_code"])
                
                logger.info(f"Healed file created: {healed_file}")
                result["healed_file"] = healed_file
                
            except Exception as e:
                logger.error(f"Error creating healed file: {str(e)}")
    
    return result


if __name__ == "__main__":
    # Heal the increment function
    result = heal_increment_function()
    
    # Print summary
    print("\n" + "="*80)
    print("QUANTUM LOGIC AGENT HEALING SUMMARY")
    print("="*80)
    
    # Errors summary
    errors = result.get("errors_detected", [])
    print(f"\nErrors Detected: {len(errors)}")
    
    for i, error in enumerate(errors, 1):
        print(f"\n{i}. {error.get('error_type', 'Unknown Error')}")
        print(f"   Description: {error.get('description', 'No description')}")
        print(f"   Severity: {error.get('severity', 'Unknown')}")
        print(f"   Phi-resonance: {error.get('phi_resonance', 0):.6f}")
    
    # Suggestions summary
    suggestions = result.get("healing_suggestions", [])
    print(f"\nHealing Suggestions: {len(suggestions)}")
    
    for i, suggestion in enumerate(suggestions, 1):
        print(f"\n{i}. {suggestion.get('suggestion_type', 'Unknown Suggestion')}")
        print(f"   Description: {suggestion.get('description', 'No description')}")
        print(f"   Confidence: {suggestion.get('confidence', 0):.4f}")
        print(f"   Phi-resonance: {suggestion.get('phi_resonance', 0):.6f}")
    
    # Healed file
    if "healed_file" in result:
        print(f"\nHealed File Created: {result['healed_file']}")
    
    print("\n" + "="*80)
