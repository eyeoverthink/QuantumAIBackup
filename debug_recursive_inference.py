#!/usr/bin/env python3
"""
debug_recursive_inference.py
Debug script for the recursive pattern detection in the phi-harmonic function inference system.
"""

import os
import json
import logging
import ast
from quantum_phi_function_inference import PhiHarmonicFunctionInference

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('debug_recursive_inference')

def read_file(file_path):
    """Read a file and return its contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def debug_nested_function_detection():
    """Debug the nested function detection."""
    logger.info("Debugging nested function detection...")
    
    # Initialize the phi-harmonic function inference system
    inference = PhiHarmonicFunctionInference()
    
    # Read the test file with nested functions
    file_path = os.path.join(os.path.dirname(__file__), 'nested_functions.py')
    source_code = read_file(file_path)
    
    # Parse the source code
    parsed = ast.parse(source_code)
    
    # Build a dictionary of all functions in the source code
    function_nodes = {}
    for node in ast.walk(parsed):
        if isinstance(node, ast.FunctionDef):
            function_nodes[node.name] = node
    
    logger.debug(f"Found functions: {list(function_nodes.keys())}")
    
    # Test process_data function
    process_data_node = function_nodes.get('process_data')
    if process_data_node:
        # Check for nested function calls
        nested_calls = inference._check_nested_function_calls(process_data_node)
        logger.debug(f"Nested calls in process_data: {nested_calls}")
        
        # Manually check for filter_positives, square_values, normalize_values in the AST
        for node in ast.walk(process_data_node):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                logger.debug(f"Found function call: {node.func.id}")
    
    # Test recursive_sum function
    recursive_sum_node = function_nodes.get('recursive_sum')
    if recursive_sum_node:
        # Check for nested function calls
        nested_calls = inference._check_nested_function_calls(recursive_sum_node)
        logger.debug(f"Nested calls in recursive_sum: {nested_calls}")
        
        # Manually check for recursive_sum in the AST
        for node in ast.walk(recursive_sum_node):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                logger.debug(f"Found function call: {node.func.id}")

def debug_pattern_matching():
    """Debug the pattern matching process."""
    logger.info("Debugging pattern matching...")
    
    # Initialize the phi-harmonic function inference system
    inference = PhiHarmonicFunctionInference()
    
    # Read the test file with nested functions
    file_path = os.path.join(os.path.dirname(__file__), 'nested_functions.py')
    source_code = read_file(file_path)
    
    # Test process_data function
    logger.debug("Analyzing process_data function...")
    result = inference.infer_function_behavior(source_code, 'process_data')
    
    # Debug the result
    logger.debug(f"Inferred behavior: {result.get('inferred_behavior')}")
    logger.debug(f"Confidence: {result.get('confidence')}")
    logger.debug(f"Phi-resonance: {result.get('phi_resonance')}")
    logger.debug(f"Patterns: {result.get('patterns')}")
    logger.debug(f"Nested functions: {result.get('nested_functions')}")
    
    # Test recursive_sum function
    logger.debug("Analyzing recursive_sum function...")
    result = inference.infer_function_behavior(source_code, 'recursive_sum')
    
    # Debug the result
    logger.debug(f"Inferred behavior: {result.get('inferred_behavior')}")
    logger.debug(f"Confidence: {result.get('confidence')}")
    logger.debug(f"Phi-resonance: {result.get('phi_resonance')}")
    logger.debug(f"Patterns: {result.get('patterns')}")
    logger.debug(f"Nested functions: {result.get('nested_functions')}")

def main():
    """Main function to run the debug script."""
    logger.info("Starting recursive pattern detection debugging...")
    
    # Debug nested function detection
    debug_nested_function_detection()
    
    # Debug pattern matching
    debug_pattern_matching()
    
    logger.info("Debugging completed.")

if __name__ == "__main__":
    main()
