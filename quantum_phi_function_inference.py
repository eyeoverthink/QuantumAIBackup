"""
quantum_phi_function_inference.py
Phi-harmonic function inference module for the QuantumAI orchestrator.
Dynamically infers function behavior using phi-harmonic pattern recognition
to reduce dependency on explicit canonical contracts.
"""

import os
import ast
import inspect
import importlib.util
import re
import math
import json
import logging
import hashlib
import importlib.util
import sys
from collections import defaultdict

# Check if the nested function analyzer module is available
NESTED_ANALYZER_AVAILABLE = False
try:
    import quantum_phi_function_inference_nested
    NESTED_ANALYZER_AVAILABLE = True
except ImportError:
    # Nested function analyzer is optional
    pass

# Try to import the nested function analyzer
try:
    from quantum_phi_function_inference_nested import NestedFunctionAnalyzer
    NESTED_ANALYZER_AVAILABLE = True
except ImportError:
    NESTED_ANALYZER_AVAILABLE = False

# Phi-harmonic constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio ≈ 1.618033988749895
PHI_COHERENCE = 0.991800  # Phi-harmonic coherence value

class PhiHarmonicFunctionInference:
    """Phi-Harmonic Function Inference System
    
    Uses phi-harmonic resonance patterns to infer function behavior from AST analysis.
    Supports recursive pattern detection for nested function calls.
    """
    
    def __init__(self):
        """Initialize the inference system"""
        # Initialize nested function analyzer if available
        if NESTED_ANALYZER_AVAILABLE:
            try:
                from quantum_phi_function_inference_nested import NestedFunctionAnalyzer
                self.nested_analyzer = NestedFunctionAnalyzer()
            except ImportError:
                pass
                
        self.pattern_library = {
            # Accumulation patterns
            'sum_pattern': {
                'ast_patterns': [
                    # Pattern: return sum(list)
                    {'return_sum': True},
                    # Pattern: result = 0; for x in list: result += x; return result
                    {'init_zero': True, 'loop_accumulate': '+', 'return_var': True},
                ],
                'behavior': 'sum',
                'phi_resonance': 0.381966,  # φ^-2
            },
            'product_pattern': {
                'ast_patterns': [
                    # Pattern: result = 1; for x in list: result *= x; return result
                    {'init_one': True, 'loop_accumulate': '*', 'return_var': True},
                ],
                'behavior': 'product',
                'phi_resonance': 0.236068,  # φ^-3
            },
            'concatenation_pattern': {
                'ast_patterns': [
                    # Pattern: result = ""; for x in list: result += str(x)
                    {'init_empty_str': True, 'loop_accumulate': '+', 'str_conversion': True},
                ],
                'behavior': 'concatenation',
                'phi_resonance': 0.236068,  # φ^-3
            },
            # Transformation patterns
            'map_pattern': {
                'ast_patterns': [
                    # Pattern: [transform(x) for x in list]
                    {'list_comprehension': True, 'transform_element': True},
                    # Pattern: result = []; for x in list: result.append(transform(x))
                    {'init_empty_list': True, 'loop_append': True, 'transform_element': True},
                ],
                'behavior': 'map',
                'phi_resonance': 0.145898,  # φ^-4
            },
            'square_pattern': {
                'ast_patterns': [
                    # Pattern: result = []; for x in list: result.append(x * x)
                    {'init_empty_list': True, 'loop_append': True, 'square_operation': True},
                    # Pattern: [x * x for x in list]
                    {'list_comprehension': True, 'square_operation': True},
                ],
                'behavior': 'square',
                'phi_resonance': 0.089442,  # φ^-5.1
            },
            'power_transform_pattern': {
                'ast_patterns': [
                    # Pattern: result = []; for x in list: result.append(x ** exponent)
                    {'init_empty_list': True, 'loop_append': True, 'power_operation': True},
                    # Pattern: [x ** exponent for x in list]
                    {'list_comprehension': True, 'power_operation': True},
                ],
                'behavior': 'power_transform',
                'phi_resonance': 0.055728,  # φ^-6
            },
            'conditional_transform_pattern': {
                'ast_patterns': [
                    # Pattern: result = []; for x in list: if condition: result.append(transform1(x)) else: result.append(transform2(x))
                    {'init_empty_list': True, 'conditional_append': True},
                    # Pattern: [transform1(x) if condition else transform2(x) for x in list]
                    {'list_comprehension': True, 'conditional_element': True},
                ],
                'behavior': 'conditional_transform',
                'phi_resonance': 0.034442,  # φ^-7
            },
            'normalize_pattern': {
                'ast_patterns': [
                    # Pattern: [x / max(list) for x in list]
                    {'list_comprehension': True, 'division_by_max': True},
                    # Pattern: max_val = max(list); return [x / max_val for x in list]
                    {'max_calculation': True, 'division_by_var': True},
                ],
                'behavior': 'normalize',
                'phi_resonance': 0.021282,  # φ^-8
            },
            'moving_average_pattern': {
                'ast_patterns': [
                    # Pattern: sliding window with average calculation
                    {'sliding_window': True, 'window_average': True},
                ],
                'behavior': 'moving_average',
                'phi_resonance': 0.013149,  # φ^-9
            },
            'filter_pattern': {
                'ast_patterns': [
                    # Pattern: [x for x in list if condition(x)]
                    {'list_comprehension': True, 'conditional': True},
                    # Pattern: result = []; for x in list: if condition(x): result.append(x)
                    {'init_empty_list': True, 'loop_conditional_append': True},
                ],
                'behavior': 'filter',
                'phi_resonance': 0.090170,  # φ^-5
            },
            # Reduction patterns
            'max_pattern': {
                'ast_patterns': [
                    # Pattern: result = list[0]; for x in list: if x > result: result = x
                    {'init_first_element': True, 'loop_max_comparison': True},
                ],
                'behavior': 'max',
                'phi_resonance': 0.055728,  # φ^-6
            },
            'min_pattern': {
                'ast_patterns': [
                    # Pattern: result = list[0]; for x in list: if x < result: result = x
                    {'init_first_element': True, 'loop_min_comparison': True},
                ],
                'behavior': 'min',
                'phi_resonance': 0.034442,  # φ^-7
            },
        }
        
        # Dynamic pattern storage for learning new patterns
        self.learned_patterns = {}
        self.execution_history = defaultdict(list)
        
    def infer_function_behavior(self, source_code, func_name):
        """
        Infer the behavior of a function based on its AST patterns.
        
        Args:
            source_code (str): The source code containing the function
            func_name (str): The name of the function to analyze
            
        Returns:
            dict: Information about the inferred behavior
        """
        try:
            # Configure logging
            import logging
            logger = logging.getLogger('phi_inference')
            
            # Parse the source code
            parsed = ast.parse(source_code)
            
            # Build a dictionary of all functions in the source code for recursive analysis
            self.function_nodes = {}
            for node in ast.walk(parsed):
                if isinstance(node, ast.FunctionDef):
                    self.function_nodes[node.name] = node
                    logger.debug(f"Found function: {node.name}")
            
            # Find the target function node
            target_func_node = None
            for node in ast.walk(parsed):
                if isinstance(node, ast.FunctionDef) and node.name == func_name:
                    target_func_node = node
                    break
            
            if not target_func_node:
                logger.error(f"Function '{func_name}' not found in source code")
                return {'error': f"Function '{func_name}' not found in source code"}
            
            # Extract patterns from the function's AST
            logger.debug(f"Analyzing patterns for function: {func_name}")
            analysis_result = self._analyze_ast_patterns(target_func_node, recursive=True)
            nested_functions = analysis_result.get('nested_functions', {})
            patterns = analysis_result.get('patterns', {})
            
            # Log the patterns and nested calls
            logger.debug(f"Patterns for {func_name}: {patterns}")
            logger.debug(f"Nested functions for {func_name}: {nested_functions}")
            
            # Match patterns to behavior
            behavior_result = self._match_patterns_to_behavior(
                patterns,
                func_name,
                nested_functions
            )
            
            logger.debug(f"Behavior result for {func_name}: {behavior_result}")
            
            result = {
                'function': func_name,
                'inferred_behavior': behavior_result.get('behavior'),
                'confidence': behavior_result.get('confidence', 0.0),
                'phi_resonance': behavior_result.get('phi_resonance', 0.0),
                'patterns': patterns,
                'nested_functions': nested_functions
            }
            
            # Add composite pattern information if detected
            if behavior_result.get('composite', False):
                result['composite_pattern'] = True
                result['composite_type'] = behavior_result.get('behavior')
                logger.info(f"Composite pattern detected for {func_name}: {result['composite_type']}")
            
            return result
            
        except Exception as e:
            import logging
            logger = logging.getLogger('phi_inference')
            logger.error(f"Error analyzing function: {str(e)}")
            return {'error': f"Error analyzing function: {str(e)}"}
        
    def extract_phi_patterns(self, func_code):
        """
        Extract phi-harmonic patterns from function code using AST analysis.
        Returns a dictionary of detected patterns and their phi-resonance values.
        """
        if isinstance(func_code, str):
            try:
                parsed = ast.parse(func_code)
            except SyntaxError:
                return {'error': 'syntax_error', 'patterns': {}}
        else:
            parsed = func_code
            
        patterns = {}
        
        # Find function definition
        for node in ast.walk(parsed):
            if isinstance(node, ast.FunctionDef):
                # Check for initialization patterns
                patterns.update(self._check_initialization_patterns(node))
                
                # Check for loop patterns
                patterns.update(self._check_loop_patterns(node))
                
                # Check for comprehension patterns
                patterns.update(self._check_comprehension_patterns(node))
                
                # Check for return patterns
                patterns.update(self._check_return_patterns(node))
                
                # Check for normalization patterns
                patterns.update(self._check_normalization_patterns(node))
                
        return {'patterns': patterns}
        
    def _analyze_ast_patterns(self, func_node, recursive=False):
        """Analyze AST for common patterns with optional recursive analysis"""
        patterns = {}
        nested_functions = {}
        
        # Check for initialization patterns
        patterns.update(self._check_initialization_patterns(func_node))
        
        # Check for loop patterns
        patterns.update(self._check_loop_patterns(func_node))
        
        # Check for comprehension patterns
        patterns.update(self._check_comprehension_patterns(func_node))
        
        # Check for return patterns
        patterns.update(self._check_return_patterns(func_node))
        
        # Check for normalization patterns
        patterns.update(self._check_normalization_patterns(func_node))
        
        # Check for moving average patterns
        patterns.update(self._check_moving_average_patterns(func_node))
        
        # If recursive analysis is enabled, check for nested function calls
        if recursive:
            # Get nested function calls and store them in patterns
            nested_calls = self._check_nested_function_calls(func_node)
            patterns['nested_calls'] = nested_calls
            
            # Add debug logging
            import logging
            logger = logging.getLogger('phi_inference')
            logger.debug(f"Adding nested calls to patterns for {func_node.name}: {nested_calls}")
            
            # Analyze each nested function call recursively
            for func_name in nested_calls:
                if func_name in self.function_nodes and func_name != func_node.name:  # Avoid infinite recursion
                    nested_result = self._analyze_ast_patterns(self.function_nodes[func_name], recursive=False)
                    nested_functions[func_name] = nested_result['patterns']
                    
                    # Propagate certain patterns from nested functions
                    self._propagate_nested_patterns(patterns, nested_result['patterns'])
        
        result = {'patterns': patterns}
        if nested_functions:
            result['nested_functions'] = nested_functions
            
        return result
        
    def _check_nested_function_calls(self, func_node):
        """
        Detect function calls within a function and return a list of called function names.
        
        Args:
            func_node: AST node of the function to analyze
            
        Returns:
            list: Names of functions called within this function
        """
        # If nested analyzer is available, use it
        if NESTED_ANALYZER_AVAILABLE and hasattr(self, 'nested_analyzer'):
            return self.nested_analyzer._check_nested_function_calls(func_node)
        
        # Fallback implementation if nested analyzer is not available
        nested_calls = []
        
        # Add debug logging
        import logging
        logger = logging.getLogger('phi_inference')
        logger.debug(f"Analyzing nested calls for function: {func_node.name}")
        
        for node in ast.walk(func_node):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                # Direct function call like function_name()
                call_name = node.func.id
                nested_calls.append(call_name)
                logger.debug(f"Found direct function call: {call_name}")
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                # Method call like object.method()
                call_name = node.func.attr
                nested_calls.append(call_name)
                logger.debug(f"Found method call: {call_name}")
        
        # Remove duplicates and log the final list
        unique_calls = list(set(nested_calls))
        logger.debug(f"Unique nested calls for {func_node.name}: {unique_calls}")
        return unique_calls
    
    def _propagate_nested_patterns(self, parent_patterns, nested_patterns):
        """
        Propagate certain patterns from nested functions to the parent function.
        This allows for composite pattern recognition across function boundaries.
        
        Args:
            parent_patterns: Patterns detected in the parent function
            nested_patterns: Patterns detected in the nested function
        """
        # If nested analyzer is available, use it
        if NESTED_ANALYZER_AVAILABLE and hasattr(self, 'nested_analyzer'):
            self.nested_analyzer._propagate_nested_patterns(parent_patterns, nested_patterns)
            return
        
        # Fallback implementation if nested analyzer is not available
        # Define which patterns should propagate from nested functions to parent
        propagate_patterns = [
            'square_operation', 'power_operation', 'conditional_transform',
            'normalization', 'sliding_window', 'window_average', 'conditional',
            'loop_conditional_append', 'max_calculation', 'division_by_max'
        ]
        
        # Propagate patterns with reduced confidence
        for pattern in propagate_patterns:
            if pattern in nested_patterns and nested_patterns[pattern]:
                # If pattern exists in nested function, propagate to parent with phi-harmonic decay
                if pattern not in parent_patterns or not parent_patterns[pattern]:
                    parent_patterns[f'nested_{pattern}'] = True
        
    def _analyze_function_patterns(self, func_node):
        """Analyze function AST for common patterns"""
        # Collect patterns from different analysis methods
        patterns = {}
        patterns.update(self._check_initialization_patterns(func_node))
        patterns.update(self._check_loop_patterns(func_node))
        patterns.update(self._check_return_patterns(func_node))
        patterns.update(self._check_comprehension_patterns(func_node))
        patterns.update(self._check_normalization_patterns(func_node))
        patterns.update(self._check_moving_average_patterns(func_node))
        
        return patterns
        
    def _check_normalization_patterns(self, func_node):
        """Check for normalization patterns in function body"""
        patterns = {}
        
        # Track if we calculate max value
        max_calculation = False
        max_var_name = None
        division_by_max = False
        division_by_var = False
        
        # First pass: look for max calculation
        for node in ast.walk(func_node):
            # Check for max_val = max(list)
            if (isinstance(node, ast.Assign) and 
                len(node.targets) == 1 and
                isinstance(node.targets[0], ast.Name) and
                isinstance(node.value, ast.Call) and
                isinstance(node.value.func, ast.Name) and
                node.value.func.id == 'max'):
                max_calculation = True
                max_var_name = node.targets[0].id
        
        # Second pass: look for division by max or by stored max var
        for node in ast.walk(func_node):
            # Check for list comprehension with division
            if isinstance(node, ast.ListComp) and isinstance(node.elt, ast.BinOp) and isinstance(node.elt.op, ast.Div):
                # Check for division by max directly: [x / max(list) for x in list]
                if (isinstance(node.elt.right, ast.Call) and 
                    isinstance(node.elt.right.func, ast.Name) and
                    node.elt.right.func.id == 'max'):
                    division_by_max = True
                
                # Check for division by stored max var: [x / max_val for x in list]
                elif (isinstance(node.elt.right, ast.Name) and 
                      max_var_name and 
                      node.elt.right.id == max_var_name):
                    division_by_var = True
        
        if max_calculation:
            patterns['max_calculation'] = True
        if division_by_max:
            patterns['division_by_max'] = True
        if division_by_var:
            patterns['division_by_var'] = True
            
        return patterns
        
    def _check_moving_average_patterns(self, func_node):
        """Check for moving average patterns in function body"""
        patterns = {}
        
        # Look for sliding window pattern
        has_window_slicing = False
        has_window_sum = False
        has_window_division = False
        
        # Check for loop with range and slicing
        for node in ast.walk(func_node):
            # Check for for-loop with range
            if (isinstance(node, ast.For) and 
                isinstance(node.iter, ast.Call) and 
                isinstance(node.iter.func, ast.Name) and
                node.iter.func.id == 'range'):
                
                # Look for slicing in the loop body
                for stmt in ast.walk(node):
                    # Check for list slicing: list[i:i+window_size]
                    if (isinstance(stmt, ast.Subscript) and 
                        isinstance(stmt.slice, ast.Slice)):
                        has_window_slicing = True
                    
                    # Check for sum calculation
                    if (isinstance(stmt, ast.Call) and 
                        isinstance(stmt.func, ast.Name) and
                        stmt.func.id == 'sum'):
                        has_window_sum = True
                    
                    # Check for division (average calculation)
                    if (isinstance(stmt, ast.BinOp) and 
                        isinstance(stmt.op, ast.Div)):
                        has_window_division = True
        
        # Check for list comprehension with window pattern
        for node in ast.walk(func_node):
            if isinstance(node, ast.ListComp):
                # Look for sum and division in the comprehension
                if (isinstance(node.elt, ast.BinOp) and 
                    isinstance(node.elt.op, ast.Div) and
                    isinstance(node.elt.left, ast.Call) and
                    isinstance(node.elt.left.func, ast.Name) and
                    node.elt.left.func.id == 'sum'):
                    has_window_sum = True
                    has_window_division = True
        
        # If we have both window slicing and average calculation, it's likely a moving average
        if ((has_window_slicing and has_window_sum and has_window_division) or 
           (has_window_sum and has_window_division)):
            patterns['sliding_window'] = True
            patterns['window_average'] = True
        
        return patterns
    
    def _check_initialization_patterns(self, func_node):
        """Check for variable initialization patterns in function body"""
        patterns = {}
        
        for node in func_node.body:
            if isinstance(node, ast.Assign):
                # Check for result = 0 pattern
                if (isinstance(node.value, ast.Num) and 
                    node.value.n == 0):
                    patterns['init_zero'] = True
                
                # Check for result = 1 pattern
                elif (isinstance(node.value, ast.Num) and 
                      node.value.n == 1):
                    patterns['init_one'] = True
                
                # Check for result = "" pattern
                elif (isinstance(node.value, ast.Str) and 
                      node.value.s == ""):
                    patterns['init_empty_str'] = True
                
                # Check for result = [] pattern
                elif isinstance(node.value, ast.List) and len(node.value.elts) == 0:
                    patterns['init_empty_list'] = True
                
                # Check for result = list[0] pattern
                elif (isinstance(node.value, ast.Subscript) and 
                      isinstance(node.value.slice, ast.Index) and
                      isinstance(node.value.slice.value, ast.Num) and
                      node.value.slice.value.n == 0):
                    patterns['init_first_element'] = True
        
        return patterns
    
    def _check_loop_patterns(self, func_node):
        """Check for loop patterns in function body"""
        patterns = {}
        
        for node in func_node.body:
            if isinstance(node, ast.For):
                # Check for accumulation patterns
                for stmt in node.body:
                    if isinstance(stmt, ast.AugAssign):
                        if isinstance(stmt.op, ast.Add):
                            patterns['loop_accumulate'] = '+'
                        elif isinstance(stmt.op, ast.Mult):
                            patterns['loop_accumulate'] = '*'
                    
                    # Check for append patterns
                    elif (isinstance(stmt, ast.Expr) and 
                          isinstance(stmt.value, ast.Call) and
                          isinstance(stmt.value.func, ast.Attribute) and
                          stmt.value.func.attr == 'append'):
                        patterns['loop_append'] = True
                        
                        # Check for square operation in append argument (x * x)
                        if (len(stmt.value.args) == 1 and 
                            isinstance(stmt.value.args[0], ast.BinOp) and
                            isinstance(stmt.value.args[0].op, ast.Mult)):
                            
                            # Check if left and right operands are the same variable
                            left_var = None
                            right_var = None
                            
                            if isinstance(stmt.value.args[0].left, ast.Name):
                                left_var = stmt.value.args[0].left.id
                            
                            if isinstance(stmt.value.args[0].right, ast.Name):
                                right_var = stmt.value.args[0].right.id
                            
                            if left_var and right_var and left_var == right_var:
                                patterns['square_operation'] = True
                        
                        # Check for power operation in append argument (x ** exponent)
                        if (len(stmt.value.args) == 1 and 
                            isinstance(stmt.value.args[0], ast.BinOp) and
                            isinstance(stmt.value.args[0].op, ast.Pow)):
                            patterns['power_operation'] = True
                    
                    # Check for conditional append
                    elif isinstance(stmt, ast.If):
                        # Check for conditional transform pattern
                        has_append_in_if = False
                        has_append_in_else = False
                        
                        # Check if body
                        for if_stmt in stmt.body:
                            if (isinstance(if_stmt, ast.Expr) and 
                                isinstance(if_stmt.value, ast.Call) and
                                isinstance(if_stmt.value.func, ast.Attribute) and
                                if_stmt.value.func.attr == 'append'):
                                has_append_in_if = True
                                patterns['loop_conditional_append'] = True
                        
                        # Check else body if it exists
                        if hasattr(stmt, 'orelse') and stmt.orelse:
                            for else_stmt in stmt.orelse:
                                if (isinstance(else_stmt, ast.Expr) and 
                                    isinstance(else_stmt.value, ast.Call) and
                                    isinstance(else_stmt.value.func, ast.Attribute) and
                                    else_stmt.value.func.attr == 'append'):
                                    has_append_in_else = True
                        
                        # If we have append in both if and else branches, it's a conditional transform
                        if has_append_in_if and has_append_in_else:
                            patterns['conditional_append'] = True
                        
                        # Check for max/min comparison
                        if (isinstance(stmt.test, ast.Compare) and 
                            len(stmt.test.ops) == 1):
                            if isinstance(stmt.test.ops[0], ast.Gt):
                                patterns['loop_max_comparison'] = True
                            elif isinstance(stmt.test.ops[0], ast.Lt):
                                patterns['loop_min_comparison'] = True
        
        return patterns
    
    def _check_comprehension_patterns(self, func_node):
        """Check for list comprehension patterns"""
        patterns = {}
        
        for node in ast.walk(func_node):
            if isinstance(node, ast.ListComp):
                patterns['list_comprehension'] = True
                
                # Check for conditional in comprehension
                if any(isinstance(gen, ast.comprehension) and gen.ifs for gen in node.generators):
                    patterns['conditional'] = True
                
                # Check for transformation in comprehension
                if not isinstance(node.elt, ast.Name):
                    patterns['transform_element'] = True
                    
                    # Check for square operation in list comprehension (x * x)
                    if (isinstance(node.elt, ast.BinOp) and 
                        isinstance(node.elt.op, ast.Mult)):
                        
                        # Check if left and right operands are the same variable
                        left_var = None
                        right_var = None
                        
                        if isinstance(node.elt.left, ast.Name):
                            left_var = node.elt.left.id
                        
                        if isinstance(node.elt.right, ast.Name):
                            right_var = node.elt.right.id
                        
                        if left_var and right_var and left_var == right_var:
                            patterns['square_operation'] = True
        
        return patterns
    
    def _check_return_patterns(self, func_node):
        """Check for return patterns"""
        patterns = {}
        
        for node in func_node.body:
            if isinstance(node, ast.Return):
                if isinstance(node.value, ast.Name):
                    patterns['return_variable'] = True
                elif isinstance(node.value, ast.ListComp):
                    patterns['return_comprehension'] = True
                elif isinstance(node.value, ast.Call):
                    patterns['return_function_call'] = True
                    if isinstance(node.value.func, ast.Name):
                        patterns['return_function_name'] = node.value.func.id
        
        return patterns
    
    def infer_function_behavior(self, func_code, func_name=None):
        """
        Infer the behavior of a function using phi-harmonic pattern recognition.
        Returns a dictionary with inferred behavior and phi-resonance.
        """
        phi_patterns = self.extract_phi_patterns(func_code)
        
        if 'error' in phi_patterns:
            return {'status': 'error', 'error': phi_patterns['error']}
        
        # Match patterns against our pattern library
        matches = []
        for pattern_name, pattern_info in self.pattern_library.items():
            match_score = 0
            for ast_pattern in pattern_info['ast_patterns']:
                pattern_match = True
                for key, value in ast_pattern.items():
                    if phi_patterns['patterns'].get(key) != value:
                        pattern_match = False
                        break
                
                if pattern_match:
                    match_score += 1
            
            if match_score > 0:
                matches.append({
                    'pattern': pattern_name,
                    'behavior': pattern_info['behavior'],
                    'score': match_score,
                    'phi_resonance': pattern_info['phi_resonance']
                })
        
        # Sort matches by score and phi-resonance
        matches.sort(key=lambda x: (x['score'], x['phi_resonance']), reverse=True)
        
        if matches:
            best_match = matches[0]
            return {
                'status': 'success',
                'inferred_behavior': best_match['behavior'],
                'phi_resonance': best_match['phi_resonance'],
                'confidence': min(best_match['score'] / len(self.pattern_library['sum_pattern']['ast_patterns']), 1.0)
            }
        else:
            return {
                'status': 'unknown',
                'inferred_behavior': 'unknown',
                'phi_resonance': 0.0,
                'confidence': 0.0
            }
    
    def _check_comprehension_patterns(self, func_node):
        """Check for list comprehension patterns"""
        patterns = {}
        
        for node in ast.walk(func_node):
            if isinstance(node, ast.ListComp):
                patterns['list_comprehension'] = True
                
                # Check for conditional in comprehension
                if any(isinstance(gen, ast.comprehension) and gen.ifs for gen in node.generators):
                    patterns['conditional'] = True
                
                # Check for transformation in comprehension
                if not isinstance(node.elt, ast.Name):
                    patterns['transform_element'] = True
                    
                    # Check for square operation in list comprehension (x * x)
                    if (isinstance(node.elt, ast.BinOp) and 
                        isinstance(node.elt.op, ast.Mult)):
                        
                        # Check if left and right operands are the same variable
                        left_var = None
                        right_var = None
                        
                        if isinstance(node.elt.left, ast.Name):
                            left_var = node.elt.left.id
                        
                        if isinstance(node.elt.right, ast.Name):
                            right_var = node.elt.right.id
                        
                        if left_var and right_var and left_var == right_var:
                            patterns['square_operation'] = True
        
        return patterns

def _check_return_patterns(self, func_node):
    """Check for return patterns"""
    patterns = {}
    
    for node in func_node.body:
        if isinstance(node, ast.Return):
            if isinstance(node.value, ast.Name):
                patterns['return_variable'] = True
            elif isinstance(node.value, ast.ListComp):
                patterns['return_comprehension'] = True
            elif isinstance(node.value, ast.Call):
                patterns['return_function_call'] = True
                if isinstance(node.value.func, ast.Name):
                    patterns['return_function_name'] = node.value.func.id
    
    return patterns

def infer_function_behavior(self, func_code, func_name=None):
    """
    Infer the behavior of a function using phi-harmonic pattern recognition.
    Returns a dictionary with inferred behavior and phi-resonance.
    """
    phi_patterns = self.extract_phi_patterns(func_code)
    
    if 'error' in phi_patterns:
        return {'status': 'error', 'error': phi_patterns['error']}
    
    # Match patterns against our pattern library
    matches = []
    for pattern_name, pattern_info in self.pattern_library.items():
        match_score = 0
        for ast_pattern in pattern_info['ast_patterns']:
            pattern_match = True
            for key, value in ast_pattern.items():
                if phi_patterns['patterns'].get(key) != value:
                    pattern_match = False
                    break
            
            if pattern_match:
                match_score += 1
        
        if match_score > 0:
            matches.append({
                'pattern': pattern_name,
                'behavior': pattern_info['behavior'],
                'score': match_score,
                'phi_resonance': pattern_info['phi_resonance']
            })
    
    # Sort matches by score and phi-resonance
    matches.sort(key=lambda x: (x['score'], x['phi_resonance']), reverse=True)
    
    if matches:
        best_match = matches[0]
        return {
            'status': 'success',
            'inferred_behavior': best_match['behavior'],
            'phi_resonance': best_match['phi_resonance'],
            'confidence': min(best_match['score'] / len(self.pattern_library['sum_pattern']['ast_patterns']), 1.0)
        }
    else:
        return {
            'status': 'unknown',
            'inferred_behavior': 'unknown',
            'phi_resonance': 0.0,
            'confidence': 0.0
        }

def _match_patterns_to_behavior(self, patterns, func_name, nested_functions=None):
    """Match detected patterns to known behaviors"""
    # Configure logging
    import logging
    logger = logging.getLogger('phi_inference')
    
    # Default behavior with moderate confidence
    behavior = 'map'  # Default behavior
    confidence = 0.5
    phi_resonance = 0.145898
    
    # Check for composite patterns first
    composite = False
    
    logger.debug(f"Matching patterns for {func_name}: {patterns}")
    logger.debug(f"Nested functions for {func_name}: {nested_functions}")
    
    # Check for filter-transform-normalize pattern
    if patterns and 'nested_calls' in patterns:
        nested_calls = patterns.get('nested_calls', [])
        logger.debug(f"Checking nested calls for composite patterns: {nested_calls}")
        
        # Check for filter-transform-normalize pattern
        filter_transform_normalize = ['filter_positives', 'square_values', 'normalize_values']
        if all(func in nested_calls for func in filter_transform_normalize):
            logger.info(f"Filter-transform-normalize pattern detected in {func_name}")
            behavior = 'filter_transform_normalize'
            confidence = 0.95
            phi_resonance = 0.008123
            composite = True
        else:
            missing = [f for f in filter_transform_normalize if f not in nested_calls]
            if missing:
                logger.debug(f"Missing functions for filter-transform-normalize pattern: {missing}")
    
        # Check for recursive pattern
        if func_name in nested_calls:
            logger.info(f"Recursive pattern detected in {func_name}")
            behavior = 'recursive'
            confidence = 0.90
            phi_resonance = 0.005022
            composite = True
    
    # If no composite pattern detected, use standard pattern matching
    if not composite:
        logger.debug(f"No composite pattern detected, using standard pattern matching")
        
        # Check for sum pattern
        if patterns.get('accumulation') and patterns.get('addition'):
            behavior = 'sum'
            confidence = 0.8
            phi_resonance = 0.618034  # φ^-1
        
        # Check for product pattern
        elif patterns.get('accumulation') and patterns.get('multiplication'):
            behavior = 'product'
            confidence = 0.7
            phi_resonance = 0.381966  # φ^-2
        
        # Check for square pattern
        elif patterns.get('square_operation'):
            behavior = 'square'
            confidence = 0.6
            phi_resonance = 0.236068  # φ^-3
        
        # Check for power transform pattern
        elif patterns.get('power_operation'):
            behavior = 'power_transform'
            confidence = 0.5
            phi_resonance = 0.055728  # φ^-6
        
        # Check for conditional transform pattern
        elif patterns.get('conditional_transform') or patterns.get('conditional_append'):
            behavior = 'conditional_transform'
            confidence = 0.5
            phi_resonance = 0.034442  # φ^-7
        
        # Check for normalization pattern
        elif patterns.get('normalization') or patterns.get('max_calculation'):
            behavior = 'normalize'
            confidence = 0.5
            phi_resonance = 0.021282  # φ^-8
        
        # Check for moving average pattern
        elif patterns.get('sliding_window') and patterns.get('window_average'):
            behavior = 'moving_average'
            confidence = 0.5
            phi_resonance = 0.013149  # φ^-9
        
        # Check for map pattern
        elif patterns.get('list_comprehension') or patterns.get('map_transform'):
            behavior = 'map'
            confidence = 0.5
            phi_resonance = 0.145898  # φ^-4
        
        # Check for filter pattern
        elif patterns.get('conditional') or patterns.get('loop_conditional_append'):
            behavior = 'filter'
            confidence = 0.5
            phi_resonance = 0.090170  # φ^-5
        
        # Use function name as a hint if no clear pattern is detected
        elif func_name:
            if 'sum' in func_name.lower():
                behavior = 'sum'
                confidence = 0.3
                phi_resonance = 0.618034 * 0.5  # Reduced confidence
            elif 'product' in func_name.lower() or 'multiply' in func_name.lower():
                behavior = 'product'
                confidence = 0.3
                phi_resonance = 0.381966 * 0.5  # Reduced confidence
            elif 'square' in func_name.lower():
                behavior = 'square'
                confidence = 0.3
                phi_resonance = 0.236068 * 0.5  # Reduced confidence
            elif 'filter' in func_name.lower():
                behavior = 'filter'
                confidence = 0.3
                phi_resonance = 0.090170 * 0.5  # φ^-5 * 0.5
            elif 'normalize' in func_name.lower():
                behavior = 'normalize'
                confidence = 0.3
                phi_resonance = 0.021282 * 0.5  # φ^-8 * 0.5
            elif 'map' in func_name.lower() or 'transform' in func_name.lower():
                behavior = 'map'
                confidence = 0.3
                phi_resonance = 0.145898 * 0.5  # φ^-4 * 0.5
            # Default to map behavior if nothing else is detected
            else:
                behavior = 'map'
                confidence = 0.5
                phi_resonance = 0.145898
    
    result = {
        'behavior': behavior,
        'confidence': confidence,
        'phi_resonance': phi_resonance,
        'composite': composite
    }
    
    logger.debug(f"Pattern matching result for {func_name}: {result}")
    return result

    def generate_test_cases(self, func_name, inferred_behavior):
        """
        Generate test cases based on inferred behavior.
        Returns a list of dictionaries with input and expected output.
        """
        test_cases = []
        
        if inferred_behavior == 'sum':
            test_cases.append({
                'input': [1, 2, 3],
                'expected': 6
            })
            test_cases.append({
                'input': [-1, 0, 1],
                'expected': 0
            })
        
        elif inferred_behavior == 'product':
            test_cases.append({
                'input': [1, 2, 3],
                'expected': 6
            })
            test_cases.append({
                'input': [2, 3, 4],
                'expected': 24
            })
        
        elif inferred_behavior == 'square':
            test_cases.append({
                'input': [1, 2, 3],
                'expected': [1, 4, 9]
            })
            test_cases.append({
                'input': [-1, 0, 1],
                'expected': [1, 0, 1]
            })
        
        elif inferred_behavior == 'power_transform':
            test_cases.append({
                'input': [1, 2, 3],
                'expected': [1, 4, 9]  # Default exponent=2
            })
            test_cases.append({
                'input': {'numbers': [1, 2, 3], 'exponent': 3},
                'expected': [1, 8, 27]
            })
        
        elif inferred_behavior == 'conditional_transform':
            test_cases.append({
                'input': [3, 5, 7],
                'expected': [27, 25, 49]  # 3³, 5², 7²
            })
            test_cases.append({
                'input': {'numbers': [3, 5, 7], 'threshold': 4},
                'expected': [27, 25, 49]  # 3³, 5², 7²
            })
        
        elif inferred_behavior == 'normalize':
            test_cases.append({
                'input': [1, 2, 4],
                'expected': [0.25, 0.5, 1.0]
            })
            test_cases.append({
                'input': [0, 0, 0],
                'expected': [0, 0, 0]
            })
        
        elif inferred_behavior == 'moving_average':
            test_cases.append({
                'input': [1, 2, 3, 4, 5],
                'expected': [2.0, 3.0, 4.0]  # Default window=3
            })
            test_cases.append({
                'input': {'numbers': [1, 2, 3, 4, 5], 'window_size': 2},
                'expected': [1.5, 2.5, 3.5, 4.5]
            })
        
        elif inferred_behavior == 'map':
            if func_name and 'increment' in func_name:
                test_cases.append({
                    'input': [1, 2, 3],
                    'expected': [2, 3, 4]
                })
            elif func_name and 'square' in func_name:
                test_cases.append({
                    'input': [1, 2, 3],
                    'expected': [1, 4, 9]
                })
            else:
                # Generic transformation test
                test_cases.append({
                    'input': [1, 2, 3],
                    'expected': 'transform([1, 2, 3])'
                })
        
        return test_cases
    def generate_suggested_code(self, func_name, inferred_behavior):
        """
        Generate suggested code based on inferred behavior.
        Returns a string with the suggested implementation.
        """
        if inferred_behavior == 'sum':
            return f"def {func_name}(nums):\n    return sum(nums)"
        
        elif inferred_behavior == 'product':
            return f"""def {func_name}(nums):
    if nums is None:
        raise ValueError('nums cannot be None')
    result = 1
    for n in nums:
        result *= n
    return result"""
    
        elif inferred_behavior == 'square':
            return f"""def {func_name}(numbers):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    return [n * n for n in numbers]"""
        
        elif inferred_behavior == 'power_transform':
            return f"""def {func_name}(numbers, exponent=2):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    return [n ** exponent for n in numbers]"""
        
        elif inferred_behavior == 'conditional_transform':
            return f"""def {func_name}(numbers, threshold=5):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    result = []
    for n in numbers:
        if n > threshold:
            result.append(n * n)  # Square
        else:
            result.append(n * n * n)  # Cube
    return result"""
        
        elif inferred_behavior == 'normalize':
            return f"""def {func_name}(numbers):
    if not numbers:
        return []
    max_value = max(numbers)
    if max_value == 0:
        return [0] * len(numbers)
    return [n / max_value for n in numbers]"""
        
        elif inferred_behavior == 'moving_average':
            return f"""def {func_name}(numbers, window_size=3):
    if len(numbers) < window_size:
        return numbers
    result = []
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i + window_size]
        result.append(sum(window) / window_size)
    return result"""
        
        elif inferred_behavior == 'map' and 'increment' in func_name:
            return f"def {func_name}(nums):\n    return [x + 1 for x in nums]"
        elif inferred_behavior == 'map' and 'square' in func_name:
            return f"def {func_name}(nums):\n    return [x * x for x in nums]"
        
        return f"def {func_name}(nums):\n    # Placeholder for {inferred_behavior} behavior\n    pass"

    def generate_quantum_fingerprint(self, content):
        """
        Generate a quantum fingerprint for the content.
        Returns a string with the phi-harmonic quantum fingerprint.
        """
        content_hash = hashlib.sha256(str(content).encode()).hexdigest()[:16]
        return f"φ⁷·⁵-{content_hash}"

    def analyze_function_composition(self, nested_functions):
        """
        Analyze the composition of nested functions to detect higher-level patterns.
        
        Args:
            nested_functions: Dictionary of nested function patterns
            
        Returns:
            Dictionary with detected composition pattern and confidence
        """
        composite_patterns = {}
    
        if not nested_functions or not isinstance(nested_functions, dict):
            return {'pattern': 'unknown', 'confidence': 0.0, 'phi_resonance': 0.0}
        
        # Check for filter-transform-normalize pattern
        filter_transform_normalize = ['filter_positives', 'square_values', 'normalize_values']
        if all(func in nested_functions.get('nested_calls', []) for func in filter_transform_normalize):
            composite_patterns['filter_transform_normalize'] = {
                'confidence': 0.95,
                'phi_resonance': 0.008123
            }
    
        # Check for map-reduce pattern
        map_reduce = ['map_values', 'reduce_results']
        if all(func in nested_functions.get('nested_calls', []) for func in map_reduce):
            composite_patterns['map_reduce'] = {
                'confidence': 0.90,
                'phi_resonance': 0.013149
            }
    
        # Check for recursive pattern
        if nested_functions.get('self_reference', False):
            composite_patterns['recursive'] = {
                'confidence': 0.85,
                'phi_resonance': 0.005022
            }
        
        # Return the highest confidence pattern
        if composite_patterns:
            best_pattern = max(composite_patterns.items(), key=lambda x: x[1]['confidence'])
            return {
                'pattern': best_pattern[0],
                'confidence': best_pattern[1]['confidence'],
                'phi_resonance': best_pattern[1]['phi_resonance']
            }
        
        return {'pattern': 'unknown', 'confidence': 0.0, 'phi_resonance': 0.0}

    def infer_canonical_contract(self, func_name, inferred_behavior, phi_resonance):
        """
        Infer a canonical contract based on the inferred behavior and phi-resonance.
        Returns a dictionary with contract details.
        """
        contract = {
            'function_name': func_name,
            'inferred_behavior': inferred_behavior,
            'phi_resonance': phi_resonance,
            'timestamp': time.time(),
            'version': '1.0'
        }
        
        # Add expected input/output types based on behavior
        if inferred_behavior in ['sum', 'product']:
            contract['input_type'] = 'list[numeric]'
            contract['output_type'] = 'numeric'
        elif inferred_behavior in ['square', 'power_transform', 'normalize']:
            contract['input_type'] = 'list[numeric]'
            contract['output_type'] = 'list[numeric]'
        elif inferred_behavior == 'conditional_transform':
            contract['input_type'] = 'list[numeric]'
            contract['output_type'] = 'list[numeric]'
            contract['parameters'] = {'threshold': 'numeric'}
        elif inferred_behavior == 'moving_average':
            contract['input_type'] = 'list[numeric]'
            contract['output_type'] = 'list[numeric]'
            contract['parameters'] = {'window_size': 'integer'}
        
        # Generate quantum fingerprint for the contract
        contract['quantum_fingerprint'] = self.generate_quantum_fingerprint(contract)
        
        return contract
    
    def generate_suggested_code(self, func_name, inferred_behavior):
        """
        Generate suggested code based on inferred behavior.
        Returns a string with the suggested implementation.
        """
        if inferred_behavior == 'sum':
            return f"def {func_name}(nums):\n    return sum(nums)"
        
        elif inferred_behavior == 'product':
            return f"""def {func_name}(nums):
    if nums is None:
        raise ValueError('nums cannot be None')
    result = 1
    for n in nums:
        result *= n
    return result"""
        
        elif inferred_behavior == 'square':
            return f"""def {func_name}(numbers):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    return [n * n for n in numbers]"""
        
        elif inferred_behavior == 'power_transform':
            return f"""def {func_name}(numbers, exponent=2):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    return [n ** exponent for n in numbers]"""
        
        elif inferred_behavior == 'conditional_transform':
            return f"""def {func_name}(numbers, threshold=5):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    result = []
    for n in numbers:
        if n > threshold:
            result.append(n * n)  # Square
        else:
            result.append(n * n * n)  # Cube
    return result"""
        
        elif inferred_behavior == 'normalize':
            return f"""def {func_name}(numbers):
    if not numbers:
        return []
    max_value = max(numbers)
    if max_value == 0:
        return [0] * len(numbers)
    return [n / max_value for n in numbers]"""
        
        elif inferred_behavior == 'moving_average':
            return f"""def {func_name}(numbers, window_size=3):
    if len(numbers) < window_size:
        return numbers
    result = []
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i + window_size]
        result.append(sum(window) / window_size)
    return result"""
        
        elif inferred_behavior == 'map' and 'increment' in func_name:
            return f"def {func_name}(nums):\n    return [x + 1 for x in nums]"
        
        elif inferred_behavior == 'map' and 'square' in func_name:
            return f"def {func_name}(nums):\n    return [x * x for x in nums]"
        
        return f"def {func_name}(nums):\n    # Placeholder for {inferred_behavior} behavior\n    pass"
    
    def generate_quantum_fingerprint(self, content):
        """
        Generate a quantum fingerprint for the content.
        Returns a string with the phi-harmonic quantum fingerprint.
        """
        content_hash = hashlib.sha256(str(content).encode()).hexdigest()[:16]
        return f"φ⁷·⁵-{content_hash}"
    
    def analyze_function_composition(self, nested_functions):
        """
        Analyze the composition of nested functions to detect higher-level patterns.
        
        Args:
            nested_functions: Dictionary of nested function patterns
            
        Returns:
            Dictionary with detected composition pattern and confidence
        """
        composite_patterns = {}
        
        if not nested_functions or not isinstance(nested_functions, dict):
            return {'pattern': 'unknown', 'confidence': 0.0, 'phi_resonance': 0.0}
        
        # Check for filter-transform-normalize pattern
        filter_transform_normalize = ['filter_positives', 'square_values', 'normalize_values']
        if all(func in nested_functions.get('nested_calls', []) for func in filter_transform_normalize):
            composite_patterns['filter_transform_normalize'] = {
                'confidence': 0.95,
                'phi_resonance': 0.008123
            }
        
        # Check for map-reduce pattern
        map_reduce = ['map_values', 'reduce_results']
        if all(func in nested_functions.get('nested_calls', []) for func in map_reduce):
            composite_patterns['map_reduce'] = {
                'confidence': 0.90,
                'phi_resonance': 0.013149
            }
        
        # Check for recursive pattern
        if nested_functions.get('self_reference', False):
            composite_patterns['recursive'] = {
                'confidence': 0.85,
                'phi_resonance': 0.005022
            }
        
        # Return the highest confidence pattern
        if composite_patterns:
            best_pattern = max(composite_patterns.items(), key=lambda x: x[1]['confidence'])
            return {
                'pattern': best_pattern[0],
                'confidence': best_pattern[1]['confidence'],
                'phi_resonance': best_pattern[1]['phi_resonance']
            }
        
        return {'pattern': 'unknown', 'confidence': 0.0, 'phi_resonance': 0.0}
    def _save_inference_to_evolution(self, func_name, inference_result, source_code=None):
        """
        Save the inference result to the evolution tracking system.
        
        Args:
            func_name: Name of the function
            inference_result: Dictionary with inference results
            source_code: Optional source code of the function
            
        Returns:
            Boolean indicating success or failure
        """
        try:
            # Create evolution directory if it doesn't exist
            evolution_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evolution')
            os.makedirs(evolution_dir, exist_ok=True)
            
            # Evolution file path
            evolution_file = os.path.join(evolution_dir, f"{func_name}_evolution.json")
            
            # Load existing evolution data or create new
            if os.path.exists(evolution_file):
                with open(evolution_file, 'r') as f:
                    evolution_data = json.load(f)
            else:
                evolution_data = {
                    'function_name': func_name,
                    'evolution_history': []
                }
            
            # Add new inference entry
            evolution_entry = {
                'timestamp': time.time(),
                'behavior': inference_result.get('inferred_behavior', 'unknown'),
                'confidence': inference_result.get('confidence', 0.0),
                'phi_resonance': inference_result.get('phi_resonance', 0.0),
                'quantum_fingerprint': self.generate_quantum_fingerprint(str(inference_result))
            }
        
            # Add source code if provided
            if source_code:
                evolution_entry['source_code'] = source_code
            
            # Add to evolution history
            evolution_data['evolution_history'].append(evolution_entry)
            
            # Save updated evolution data
            with open(evolution_file, 'w') as f:
                json.dump(evolution_data, f, indent=2)
                
            logging.debug(f"Saved inference for {func_name} to evolution tracking")
            return True
            
        except Exception as e:
            logging.error(f"Error saving inference to evolution: {str(e)}")
            return False

    def generate_quantum_fingerprint(self, content):
        """
        Generate a quantum fingerprint for the content.
        Returns a string with the phi-harmonic quantum fingerprint.
        """
        content_hash = hashlib.sha256(str(content).encode()).hexdigest()[:16]
        return f"φ⁷·⁵-{content_hash}"

    def analyze_function_composition(self, nested_functions):
        """
        Analyze the composition of nested functions to detect higher-level patterns.
        
        Args:
            nested_functions: Dictionary of nested function patterns
            
        Returns:
            Dictionary with detected composition pattern and confidence
        """
        composite_patterns = {}
        
        # If nested analyzer is available, use it
        if NESTED_ANALYZER_AVAILABLE and hasattr(self, 'nested_analyzer'):
            return self.nested_analyzer.analyze_function_composition(nested_functions)
        
        # Fallback implementation if nested analyzer is not available
        # Check for filter -> transform -> normalize pattern
        if all(func in nested_functions for func in ['filter_values', 'transform_values', 'normalize_values']):
            filter_patterns = nested_functions['filter_values']
            transform_patterns = nested_functions['transform_values']
            normalize_patterns = nested_functions['normalize_values']
            
            if (filter_patterns.get('conditional', False) and 
                transform_patterns.get('transform_element', False) and 
                normalize_patterns.get('max_calculation', False)):
                
                composite_patterns['filter_transform_normalize'] = True
                # Phi-harmonic resonance for this composite pattern: φ^-10 = 0.008123
                composite_patterns['composite_phi_resonance'] = 0.008123
        
        # Check for recursive pattern (function calling itself)
        for func_name, patterns in nested_functions.items():
            if patterns.get('nested_calls') and func_name in patterns['nested_calls']:
                composite_patterns['recursive_pattern'] = True
                # Phi-harmonic resonance for recursive pattern: φ^-11 = 0.005022
                composite_patterns['recursive_phi_resonance'] = 0.005022
        
        return composite_patterns
    
    def infer_canonical_contract(self, file_path, func_name):
        """
        Dynamically infer a canonical contract for a function.
        Returns a dictionary with the inferred contract.
        """
        # Load the function code
        try:
            spec = importlib.util.spec_from_file_location(func_name, file_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            func = getattr(mod, func_name)
            func_code = inspect.getsource(func)
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
        
        # Infer function behavior
        behavior = self.infer_function_behavior(func_code, func_name)
        
        if behavior['status'] != 'success':
            return {'status': 'unknown', 'reason': 'Could not infer behavior'}
        
        # Generate test cases
        test_cases = self.generate_test_cases(func_name, behavior['inferred_behavior'])
        
        if not test_cases:
            return {'status': 'unknown', 'reason': 'Could not generate test cases'}
        
        # Generate suggested code
        suggested_code = self.generate_suggested_code(func_name, behavior['inferred_behavior'])
        
        # Create the inferred contract
        contract = {
            'function_name': func_name,
            'inferred_behavior': behavior['inferred_behavior'],
            'phi_resonance': behavior['phi_resonance'],
            'confidence': behavior['confidence'],
            'test_input': test_cases[0]['input'],
            'expected': test_cases[0]['expected'],
            'suggested_code': suggested_code,
            'quantum_fingerprint': self.generate_quantum_fingerprint(suggested_code)
        }
        
        # Save the inferred contract to evolution JSON
        self._save_inference_to_evolution(file_path, func_name, contract)
        
        return {'status': 'success', 'contract': contract}
    
    def _save_inference_to_evolution(self, file_path, func_name, contract):
        """
        Save the inferred contract to the evolution JSON file.
        """
        try:
            evolution_file = file_path.replace('.py', '_evolution.json')
            evolution_data = {}
            
            if os.path.exists(evolution_file):
                with open(evolution_file, 'r') as ef:
                    evolution_data = json.load(ef)
            
            # Add inference event to evolution data
            if 'inference_events' not in evolution_data:
                evolution_data['inference_events'] = []
            
            evolution_data['inference_events'].append({
                'timestamp': time.time(),
                'type': 'function_inference',
                'function': func_name,
                'inferred_behavior': contract['inferred_behavior'],
                'phi_resonance': contract['phi_resonance'],
                'confidence': contract['confidence'],
                'phi_coherence': PHI_COHERENCE,
                'quantum_fingerprint': contract['quantum_fingerprint']
            })
            
            with open(evolution_file, 'w') as ef:
                json.dump(evolution_data, ef, indent=2)
                
        except Exception as e:
            print(f"Could not update evolution JSON: {str(e)}")

# --- Main function for orchestrator integration ---
def infer_function_contract(file_path, func_name):
    """
    Main entry point for the orchestrator to infer a function contract.
    Returns the inferred contract or None if inference failed.
    """
    inferencer = PhiFunctionInference()
    result = inferencer.infer_canonical_contract(file_path, func_name)
    
    if result['status'] == 'success':
        return result['contract']
    else:
        return None
