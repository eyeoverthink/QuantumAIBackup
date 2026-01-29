#!/usr/bin/env python3
"""
debug_recursive_detection.py
Debug script for the recursive pattern detection in the phi-harmonic function inference system.
"""

import os
import json
import logging
import sys
from quantum_phi_function_inference import PhiHarmonicFunctionInference

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('recursive_debug.log')
    ]
)

logger = logging.getLogger('phi_inference')
logger.setLevel(logging.DEBUG)

def read_file(file_path):
    """Read a file and return its contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def debug_nested_function_detection():
    """Debug the nested function detection logic."""
    logger.info("Starting nested function detection debugging...")
    
    # Initialize the phi-harmonic function inference system
    inference = PhiHarmonicFunctionInference()
    
    # Read the test file with nested functions
    file_path = os.path.join(os.path.dirname(__file__), 'nested_functions.py')
    source_code = read_file(file_path)
    
    # Test functions with nested calls
    functions_to_test = [
        'process_data',  # Composite pattern (filter -> square -> normalize)
        'recursive_sum'  # Recursive pattern
    ]
    
    for func_name in functions_to_test:
        logger.info(f"=== Debugging function: {func_name} ===")
        
        # Parse the source code to get the AST
        import ast
        parsed = ast.parse(source_code)
        
        # Build a dictionary of all functions in the source code
        function_nodes = {}
        for node in ast.walk(parsed):
            if isinstance(node, ast.FunctionDef):
                function_nodes[node.name] = node
                logger.debug(f"Found function: {node.name}")
        
        # Get the target function node
        target_func_node = function_nodes.get(func_name)
        if not target_func_node:
            logger.error(f"Function {func_name} not found in source code")
            continue
        
        # Extract nested function calls
        inference.function_nodes = function_nodes  # Set the function nodes dictionary
        nested_calls = inference._check_nested_function_calls(target_func_node)
        logger.info(f"Nested calls for {func_name}: {nested_calls}")
        
        # Check for composite patterns
        if func_name == 'process_data':
            filter_transform_normalize = ['filter_positives', 'square_values', 'normalize_values']
            if all(func in nested_calls for func in filter_transform_normalize):
                logger.info(f"Filter-transform-normalize pattern detected in {func_name}")
            else:
                logger.warning(f"Filter-transform-normalize pattern NOT detected in {func_name}")
                logger.warning(f"Missing functions: {[f for f in filter_transform_normalize if f not in nested_calls]}")
        
        if func_name == 'recursive_sum':
            if func_name in nested_calls:
                logger.info(f"Recursive pattern detected in {func_name}")
            else:
                logger.warning(f"Recursive pattern NOT detected in {func_name}")
        
        # Run the full inference
        logger.info(f"Running full inference on {func_name}...")
        result = inference.infer_function_behavior(source_code, func_name)
        
        # Log the detailed results
        logger.info(f"Inferred behavior: {result.get('inferred_behavior')}")
        logger.info(f"Confidence: {result.get('confidence', 0.0):.4f}")
        logger.info(f"Phi-resonance: {result.get('phi_resonance', 0.0):.6f}")
        logger.info(f"Composite pattern: {result.get('composite_pattern', False)}")
        logger.info(f"Composite type: {result.get('composite_type')}")
        logger.info(f"Patterns: {result.get('patterns', {})}")
        logger.info(f"Nested functions: {result.get('nested_functions', {})}")
        
        # Save the detailed result to a JSON file
        with open(f"{func_name}_debug_result.json", 'w') as f:
            json.dump(result, f, indent=2, default=str)
        logger.info(f"Detailed results saved to {func_name}_debug_result.json")
        
        logger.info(f"=== End debugging for {func_name} ===\n")

if __name__ == "__main__":
    debug_nested_function_detection()
