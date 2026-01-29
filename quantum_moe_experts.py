#!/usr/bin/env python3
"""
Quantum MoE Experts
------------------

This module implements specialized experts for the Mixture of Experts (MoE)
architecture in the QuantumAI system. Each expert focuses on a specific domain
of expertise while maintaining phi-harmonic coherence.

The experts follow the modular "lego" approach, allowing them to be combined
and extended while maintaining quantum principles and phi-harmonic resonance.
"""

import os
import re
import ast
import time
import json
import logging
import hashlib
from typing import Dict, Any, List, Optional, Tuple, Set, Union

# Import interfaces
from quantum_moe_interfaces import (
    QuantumExpertInterface, 
    PHI, 
    PHI_POWERS,
    calculate_phi_resonance,
    generate_quantum_id
)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumMoEExperts")

class LogicErrorExpert(QuantumExpertInterface):
    """
    Expert specialized in detecting and analyzing logic errors in code.
    """
    
    def __init__(self, phi: float = PHI):
        """Initialize the logic error expert."""
        super().__init__(phi)
        self.specialization = "LogicErrorExpert"
        self.resonance_level = PHI_POWERS["φ⁷·⁵"] / 10
        self.error_patterns = {
            "off_by_one": re.compile(r'([-+]=?\s*1|[-+]\s*1)'),
            "condition_inversion": re.compile(r'(==|!=|>|<|>=|<=)'),
            "infinite_loop": re.compile(r'while\s+.*:'),
            "variable_misuse": re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*='),
        }
        logger.info(f"Initialized {self.specialization} with ID: {self.expert_id}")
    
    def analyze(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze code for logic errors.
        
        Args:
            input_data: Dictionary with 'code' and optional 'expected_behavior'
            
        Returns:
            Analysis results
        """
        if 'code' not in input_data:
            return {"error": "No code provided for analysis"}
        
        code = input_data['code']
        expected_behavior = input_data.get('expected_behavior', {})
        
        # Analyze the code
        analysis = {
            "expert_id": self.expert_id,
            "expert_specialization": self.specialization,
            "timestamp": time.time(),
            "code_hash": hashlib.sha256(code.encode()).hexdigest()[:16],
            "potential_issues": [],
            "confidence": 0.0,
            "phi_resonance": 0.0
        }
        
        # Check for syntax errors first
        try:
            ast.parse(code)
        except SyntaxError as e:
            analysis["potential_issues"].append({
                "type": "syntax_error",
                "description": f"Syntax error: {str(e)}",
                "line": e.lineno,
                "confidence": 0.99
            })
            analysis["confidence"] = 0.99
            return analysis
        
        # Check for logic error patterns
        for error_type, pattern in self.error_patterns.items():
            matches = pattern.findall(code)
            if matches:
                for match in matches:
                    analysis["potential_issues"].append({
                        "type": error_type,
                        "pattern": match,
                        "description": f"Potential {error_type} issue",
                        "confidence": 0.7
                    })
        
        # Advanced logic analysis using AST
        try:
            tree = ast.parse(code)
            visitor = LogicErrorVisitor()
            visitor.visit(tree)
            
            for issue in visitor.issues:
                analysis["potential_issues"].append({
                    "type": issue["type"],
                    "description": issue["description"],
                    "line": issue.get("line", 0),
                    "confidence": issue.get("confidence", 0.8)
                })
        except Exception as e:
            logger.warning(f"Error during AST analysis: {str(e)}")
        
        # Calculate overall confidence based on issues found
        if analysis["potential_issues"]:
            confidences = [issue.get("confidence", 0.5) for issue in analysis["potential_issues"]]
            analysis["confidence"] = sum(confidences) / len(confidences)
        else:
            analysis["confidence"] = 0.1  # Low confidence if no issues found
        
        # Calculate phi-harmonic resonance
        resonance_value = sum(ord(c) for c in code) * self.phi
        analysis["phi_resonance"] = calculate_phi_resonance(resonance_value)
        
        return analysis
    
    def get_confidence(self, input_data: Any) -> float:
        """
        Calculate confidence in handling the given input.
        
        Args:
            input_data: The data to evaluate
            
        Returns:
            Confidence score between 0 and 1
        """
        if not isinstance(input_data, dict) or 'code' not in input_data:
            return 0.1
        
        code = input_data['code']
        
        # Quick check for code that likely has logic errors
        confidence = 0.5  # Base confidence
        
        # Check for error patterns
        for pattern in self.error_patterns.values():
            if pattern.search(code):
                confidence += 0.1  # Increase confidence for each pattern match
        
        # Check for conditionals and loops (common sources of logic errors)
        if 'if ' in code or 'for ' in code or 'while ' in code:
            confidence += 0.2
            
        # Check for arithmetic operations
        if re.search(r'[-+*/]', code):
            confidence += 0.1
            
        return min(confidence, 0.95)  # Cap at 0.95

class OptimizationExpert(QuantumExpertInterface):
    """
    Expert specialized in optimizing code for performance and efficiency.
    """
    
    def __init__(self, phi: float = PHI):
        """Initialize the optimization expert."""
        super().__init__(phi)
        self.specialization = "OptimizationExpert"
        self.resonance_level = PHI_POWERS["φ⁶"] / 10
        self.optimization_patterns = {
            "nested_loops": re.compile(r'for.*:.*\n.*for.*:'),
            "repeated_calls": re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\(.*\).*\1\('),
            "large_allocations": re.compile(r'(list|dict|set)\(.*\)'),
            "string_concatenation": re.compile(r'".*"\s*\+\s*".*"'),
        }
        logger.info(f"Initialized {self.specialization} with ID: {self.expert_id}")
    
    def analyze(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze code for optimization opportunities.
        
        Args:
            input_data: Dictionary with 'code' and optional 'performance_metrics'
            
        Returns:
            Analysis results
        """
        if 'code' not in input_data:
            return {"error": "No code provided for analysis"}
        
        code = input_data['code']
        performance_metrics = input_data.get('performance_metrics', {})
        
        # Analyze the code
        analysis = {
            "expert_id": self.expert_id,
            "expert_specialization": self.specialization,
            "timestamp": time.time(),
            "code_hash": hashlib.sha256(code.encode()).hexdigest()[:16],
            "optimization_opportunities": [],
            "confidence": 0.0,
            "phi_resonance": 0.0
        }
        
        # Check for optimization patterns
        for opt_type, pattern in self.optimization_patterns.items():
            matches = pattern.findall(code)
            if matches:
                for match in matches:
                    analysis["optimization_opportunities"].append({
                        "type": opt_type,
                        "pattern": match if isinstance(match, str) else match[0],
                        "description": f"Potential {opt_type} optimization",
                        "confidence": 0.7
                    })
        
        # Advanced optimization analysis using AST
        try:
            tree = ast.parse(code)
            visitor = OptimizationVisitor()
            visitor.visit(tree)
            
            for opportunity in visitor.opportunities:
                analysis["optimization_opportunities"].append({
                    "type": opportunity["type"],
                    "description": opportunity["description"],
                    "line": opportunity.get("line", 0),
                    "confidence": opportunity.get("confidence", 0.8)
                })
        except Exception as e:
            logger.warning(f"Error during AST analysis: {str(e)}")
        
        # Calculate overall confidence based on opportunities found
        if analysis["optimization_opportunities"]:
            confidences = [opp.get("confidence", 0.5) for opp in analysis["optimization_opportunities"]]
            analysis["confidence"] = sum(confidences) / len(confidences)
        else:
            analysis["confidence"] = 0.1  # Low confidence if no opportunities found
        
        # Calculate phi-harmonic resonance
        resonance_value = sum(ord(c) for c in code) * self.phi
        analysis["phi_resonance"] = calculate_phi_resonance(resonance_value)
        
        return analysis
    
    def get_confidence(self, input_data: Any) -> float:
        """
        Calculate confidence in handling the given input.
        
        Args:
            input_data: The data to evaluate
            
        Returns:
            Confidence score between 0 and 1
        """
        if not isinstance(input_data, dict) or 'code' not in input_data:
            return 0.1
        
        code = input_data['code']
        
        # Quick check for code that likely has optimization opportunities
        confidence = 0.4  # Base confidence
        
        # Check for optimization patterns
        for pattern in self.optimization_patterns.values():
            if pattern.search(code):
                confidence += 0.1  # Increase confidence for each pattern match
        
        # Check for loops and data structures (common optimization targets)
        if 'for ' in code or 'while ' in code:
            confidence += 0.15
            
        # Check for large functions or methods
        if len(code.split('\n')) > 20:
            confidence += 0.1
            
        return min(confidence, 0.9)  # Cap at 0.9

class CoherenceExpert(QuantumExpertInterface):
    """
    Expert specialized in maintaining phi-harmonic coherence in code.
    """
    
    def __init__(self, phi: float = PHI):
        """Initialize the coherence expert."""
        super().__init__(phi)
        self.specialization = "CoherenceExpert"
        self.resonance_level = PHI_POWERS["φ⁷·⁵"] / 10
        self.phi_patterns = {
            "phi_constants": re.compile(r'(1\.618|phi|PHI|golden_ratio)'),
            "fibonacci_sequence": re.compile(r'(fibonacci|fib\(|Fibonacci)'),
            "recursive_patterns": re.compile(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\(.*\).*\1\('),
        }
        logger.info(f"Initialized {self.specialization} with ID: {self.expert_id}")
    
    def analyze(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze code for phi-harmonic coherence.
        
        Args:
            input_data: Dictionary with 'code' and optional 'coherence_target'
            
        Returns:
            Analysis results
        """
        if 'code' not in input_data:
            return {"error": "No code provided for analysis"}
        
        code = input_data['code']
        coherence_target = input_data.get('coherence_target', PHI_POWERS["φ⁷·⁵"])
        
        # Analyze the code
        analysis = {
            "expert_id": self.expert_id,
            "expert_specialization": self.specialization,
            "timestamp": time.time(),
            "code_hash": hashlib.sha256(code.encode()).hexdigest()[:16],
            "coherence_metrics": {},
            "coherence_patterns": [],
            "confidence": 0.0,
            "phi_resonance": 0.0
        }
        
        # Calculate basic coherence metrics
        code_length = len(code)
        lines = code.split('\n')
        line_count = len(lines)
        
        # Character frequency analysis
        char_freq = {}
        for char in code:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Calculate entropy
        entropy = 0
        for char, freq in char_freq.items():
            prob = freq / code_length
            entropy -= prob * (prob ** (1/self.phi))
        
        # Calculate phi-harmonic metrics
        length_phi_ratio = code_length / (line_count * self.phi)
        entropy_phi_product = entropy * self.phi
        
        analysis["coherence_metrics"] = {
            "code_length": code_length,
            "line_count": line_count,
            "length_phi_ratio": length_phi_ratio,
            "entropy": entropy,
            "entropy_phi_product": entropy_phi_product,
            "character_diversity": len(char_freq) / (code_length ** (1/self.phi)),
            "phi_resonance_score": calculate_phi_resonance(code_length * entropy, coherence_target)
        }
        
        # Check for phi-harmonic patterns
        for pattern_type, pattern in self.phi_patterns.items():
            matches = pattern.findall(code)
            if matches:
                analysis["coherence_patterns"].append({
                    "type": pattern_type,
                    "count": len(matches),
                    "examples": matches[:3]  # Limit examples to 3
                })
        
        # Calculate overall confidence
        phi_resonance = analysis["coherence_metrics"]["phi_resonance_score"]
        pattern_bonus = 0.1 * len(analysis["coherence_patterns"])
        analysis["confidence"] = max(0.3, min(0.9, (1 - phi_resonance) + pattern_bonus))
        
        # Set phi resonance
        analysis["phi_resonance"] = phi_resonance
        
        return analysis
    
    def get_confidence(self, input_data: Any) -> float:
        """
        Calculate confidence in handling the given input.
        
        Args:
            input_data: The data to evaluate
            
        Returns:
            Confidence score between 0 and 1
        """
        if not isinstance(input_data, dict) or 'code' not in input_data:
            return 0.1
        
        code = input_data['code']
        
        # Base confidence for coherence expert
        confidence = 0.6  # Always somewhat confident about coherence analysis
        
        # Check for phi-related patterns
        for pattern in self.phi_patterns.values():
            if pattern.search(code):
                confidence += 0.1  # Increase confidence for each pattern match
        
        # Higher confidence for longer code (more patterns to analyze)
        if len(code) > 500:
            confidence += 0.1
            
        # Higher confidence for recursive or mathematical code
        if 'def ' in code and 'return ' in code:
            confidence += 0.1
            
        return min(confidence, 0.95)  # Cap at 0.95

class EvolutionExpert(QuantumExpertInterface):
    """
    Expert specialized in evolutionary patterns and self-improvement in code.
    """
    
    def __init__(self, phi: float = PHI):
        """Initialize the evolution expert."""
        super().__init__(phi)
        self.specialization = "EvolutionExpert"
        self.resonance_level = PHI_POWERS["φ⁷"] / 10
        self.evolution_patterns = {
            "version_tracking": re.compile(r'(version|v\d+\.\d+|rev\.\s*\d+)'),
            "self_modification": re.compile(r'(self\..*\s*=|setattr\(|update_)'),
            "learning_patterns": re.compile(r'(learn|train|adapt|evolve)'),
        }
        logger.info(f"Initialized {self.specialization} with ID: {self.expert_id}")
    
    def analyze(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze code for evolutionary patterns and self-improvement capabilities.
        
        Args:
            input_data: Dictionary with 'code' and optional 'evolution_history'
            
        Returns:
            Analysis results
        """
        if 'code' not in input_data:
            return {"error": "No code provided for analysis"}
        
        code = input_data['code']
        evolution_history = input_data.get('evolution_history', [])
        
        # Analyze the code
        analysis = {
            "expert_id": self.expert_id,
            "expert_specialization": self.specialization,
            "timestamp": time.time(),
            "code_hash": hashlib.sha256(code.encode()).hexdigest()[:16],
            "evolution_capabilities": [],
            "evolution_metrics": {},
            "confidence": 0.0,
            "phi_resonance": 0.0
        }
        
        # Check for evolution patterns
        for pattern_type, pattern in self.evolution_patterns.items():
            matches = pattern.findall(code)
            if matches:
                analysis["evolution_capabilities"].append({
                    "type": pattern_type,
                    "count": len(matches),
                    "examples": matches[:3]  # Limit examples to 3
                })
        
        # Advanced evolution analysis using AST
        try:
            tree = ast.parse(code)
            visitor = EvolutionVisitor()
            visitor.visit(tree)
            
            for capability in visitor.capabilities:
                analysis["evolution_capabilities"].append({
                    "type": capability["type"],
                    "description": capability["description"],
                    "line": capability.get("line", 0),
                    "confidence": capability.get("confidence", 0.7)
                })
        except Exception as e:
            logger.warning(f"Error during AST analysis: {str(e)}")
        
        # Calculate evolution metrics
        if evolution_history:
            # Analyze evolution history
            versions = len(evolution_history)
            changes = sum(h.get("changes", 0) for h in evolution_history)
            improvements = sum(1 for h in evolution_history if h.get("improved", False))
            
            analysis["evolution_metrics"] = {
                "versions": versions,
                "total_changes": changes,
                "improvements": improvements,
                "improvement_ratio": improvements / max(1, versions),
                "change_frequency": changes / max(1, versions),
                "phi_evolution_score": calculate_phi_resonance(versions * self.phi)
            }
        
        # Calculate overall confidence
        capability_count = len(analysis["evolution_capabilities"])
        history_bonus = 0.2 if evolution_history else 0
        analysis["confidence"] = min(0.9, 0.4 + (0.1 * capability_count) + history_bonus)
        
        # Calculate phi-harmonic resonance
        resonance_value = (sum(ord(c) for c in code) * self.phi) + (len(evolution_history) * self.phi**2)
        analysis["phi_resonance"] = calculate_phi_resonance(resonance_value)
        
        return analysis
    
    def get_confidence(self, input_data: Any) -> float:
        """
        Calculate confidence in handling the given input.
        
        Args:
            input_data: The data to evaluate
            
        Returns:
            Confidence score between 0 and 1
        """
        if not isinstance(input_data, dict) or 'code' not in input_data:
            return 0.1
        
        code = input_data['code']
        evolution_history = input_data.get('evolution_history', [])
        
        # Base confidence
        confidence = 0.3
        
        # Check for evolution patterns
        for pattern in self.evolution_patterns.values():
            if pattern.search(code):
                confidence += 0.1  # Increase confidence for each pattern match
        
        # Higher confidence if evolution history is provided
        if evolution_history:
            confidence += 0.2 + (0.05 * min(10, len(evolution_history)))
            
        # Higher confidence for class definitions (more likely to have evolution patterns)
        if 'class ' in code:
            confidence += 0.1
            
        return min(confidence, 0.9)  # Cap at 0.9

# AST Visitors for advanced analysis

class LogicErrorVisitor(ast.NodeVisitor):
    """AST visitor to detect potential logic errors."""
    
    def __init__(self):
        self.issues = []
        self.variables = set()
        self.defined_variables = set()
    
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.defined_variables.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            self.variables.add(node.id)
        self.generic_visit(node)
    
    def visit_Compare(self, node):
        # Check for potential off-by-one errors in comparisons
        if isinstance(node.ops[0], (ast.Lt, ast.LtE, ast.Gt, ast.GtE)):
            if isinstance(node.left, ast.Num) and node.left.n in (0, 1):
                self.issues.append({
                    "type": "potential_off_by_one",
                    "description": "Comparison with 0 or 1 might indicate an off-by-one error",
                    "line": node.lineno,
                    "confidence": 0.6
                })
        self.generic_visit(node)
    
    def visit_While(self, node):
        # Check for potential infinite loops
        if isinstance(node.test, ast.Constant) and node.test.value is True:
            self.issues.append({
                "type": "infinite_loop",
                "description": "While loop with constant True condition",
                "line": node.lineno,
                "confidence": 0.9
            })
        self.generic_visit(node)

class OptimizationVisitor(ast.NodeVisitor):
    """AST visitor to detect optimization opportunities."""
    
    def __init__(self):
        self.opportunities = []
        self.function_calls = {}
    
    def visit_Call(self, node):
        # Track function calls
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            self.function_calls[func_name] = self.function_calls.get(func_name, 0) + 1
            
            # Check for repeated expensive function calls
            if self.function_calls[func_name] > 2:
                self.opportunities.append({
                    "type": "repeated_function_call",
                    "description": f"Function '{func_name}' called multiple times, consider caching result",
                    "line": getattr(node, 'lineno', 0),
                    "confidence": 0.7
                })
        self.generic_visit(node)
    
    def visit_For(self, node):
        # Check for nested loops
        for child in ast.walk(node.body):
            if isinstance(child, ast.For):
                self.opportunities.append({
                    "type": "nested_loop",
                    "description": "Nested loop detected, potential O(n²) complexity",
                    "line": node.lineno,
                    "confidence": 0.8
                })
                break
        self.generic_visit(node)

class EvolutionVisitor(ast.NodeVisitor):
    """AST visitor to detect evolutionary capabilities."""
    
    def __init__(self):
        self.capabilities = []
    
    def visit_ClassDef(self, node):
        # Check for classes with evolutionary capabilities
        for base in node.bases:
            if isinstance(base, ast.Name) and any(pattern in base.id.lower() for pattern in 
                                                ["evol", "adapt", "learn", "improv"]):
                self.capabilities.append({
                    "type": "evolutionary_inheritance",
                    "description": f"Class '{node.name}' inherits from evolutionary base class",
                    "line": node.lineno,
                    "confidence": 0.8
                })
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        # Check for methods related to evolution
        if any(pattern in node.name.lower() for pattern in 
              ["evolve", "adapt", "learn", "improve", "mutate", "update", "optimize"]):
            self.capabilities.append({
                "type": "evolutionary_method",
                "description": f"Method '{node.name}' appears to have evolutionary purpose",
                "line": node.lineno,
                "confidence": 0.7
            })
        self.generic_visit(node)

# Factory function to create experts
def create_expert(expert_type: str, phi: float = PHI) -> QuantumExpertInterface:
    """
    Create an expert of the specified type.
    
    Args:
        expert_type: Type of expert to create
        phi: The golden ratio value to use
        
    Returns:
        An initialized expert
    """
    expert_classes = {
        "logic": LogicErrorExpert,
        "optimization": OptimizationExpert,
        "coherence": CoherenceExpert,
        "evolution": EvolutionExpert
    }
    
    if expert_type.lower() not in expert_classes:
        logger.warning(f"Unknown expert type: {expert_type}")
        return None
    
    expert_class = expert_classes[expert_type.lower()]
    return expert_class(phi)

# Create a full expert team
def create_expert_team(phi: float = PHI) -> List[QuantumExpertInterface]:
    """
    Create a complete team of experts.
    
    Args:
        phi: The golden ratio value to use
        
    Returns:
        List of initialized experts
    """
    experts = [
        LogicErrorExpert(phi),
        OptimizationExpert(phi),
        CoherenceExpert(phi),
        EvolutionExpert(phi)
    ]
    
    logger.info(f"Created expert team with {len(experts)} experts")
    return experts

# Export key components
__all__ = [
    'LogicErrorExpert',
    'OptimizationExpert',
    'CoherenceExpert',
    'EvolutionExpert',
    'create_expert',
    'create_expert_team'
]
