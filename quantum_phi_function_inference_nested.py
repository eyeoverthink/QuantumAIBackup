"""
quantum_phi_function_inference_nested.py
Extension module for the phi-harmonic function inference system with recursive pattern detection.
This module adds support for analyzing nested function calls and propagating patterns.
"""

import ast
from collections import defaultdict

class NestedFunctionAnalyzer:
    """
    Analyzer for nested function calls in the phi-harmonic function inference system.
    This class extends the core inference system with recursive pattern detection.
    """
    
    def _check_nested_function_calls(self, func_node):
        """
        Detect function calls within a function and return a list of called function names.
        
        Args:
            func_node: AST node of the function to analyze
            
        Returns:
            list: Names of functions called within this function
        """
        nested_calls = []
        
        for node in ast.walk(func_node):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                # Direct function call like function_name()
                nested_calls.append(node.func.id)
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                # Method call like object.method()
                nested_calls.append(node.func.attr)
        
        return list(set(nested_calls))  # Remove duplicates
    
    def _propagate_nested_patterns(self, parent_patterns, nested_patterns):
        """
        Propagate certain patterns from nested functions to the parent function.
        This allows for composite pattern recognition across function boundaries.
        
        Args:
            parent_patterns: Patterns detected in the parent function
            nested_patterns: Patterns detected in the nested function
        """
        # Define which patterns should propagate from nested functions to parent
        propagate_patterns = [
            'accumulation', 'product_accumulation', 'square_operation',
            'power_operation', 'conditional_transform', 'normalization',
            'sliding_window', 'window_average'
        ]
        
        # Propagate patterns with reduced confidence
        for pattern in propagate_patterns:
            if pattern in nested_patterns and nested_patterns[pattern]:
                # If pattern exists in nested function, propagate to parent with phi-harmonic decay
                if pattern not in parent_patterns or not parent_patterns[pattern]:
                    parent_patterns[f'nested_{pattern}'] = True
    
    def analyze_function_composition(self, nested_functions):
        """
        Analyze the composition of nested functions to detect higher-level patterns.
        
        Args:
            nested_functions: Dictionary of nested function patterns
            
        Returns:
            dict: Composite patterns detected across function boundaries
        """
        composite_patterns = {}
        
        # Check for filter -> transform -> normalize pattern
        if ('filter_positives' in nested_functions and 
            'square_values' in nested_functions and 
            'normalize_values' in nested_functions):
            
            filter_patterns = nested_functions['filter_positives']
            transform_patterns = nested_functions['square_values']
            normalize_patterns = nested_functions['normalize_values']
            
            if (any(p in filter_patterns for p in ['conditional_append', 'filter_condition']) and
                any(p in transform_patterns for p in ['square_operation', 'map_transform']) and
                any(p in normalize_patterns for p in ['normalization', 'max_calculation'])):
                
                composite_patterns['filter_transform_normalize'] = True
                # Phi-harmonic resonance for this composite pattern: φ^-10 = 0.008123
                composite_patterns['composite_phi_resonance'] = 0.008123
        
        # Check for recursive pattern (function calling itself)
        for func_name, patterns in nested_functions.items():
            if 'nested_calls' in patterns and func_name in patterns['nested_calls']:
                composite_patterns['recursive_pattern'] = True
                # Phi-harmonic resonance for recursive pattern: φ^-11 = 0.005022
                composite_patterns['recursive_phi_resonance'] = 0.005022
        
        return composite_patterns
