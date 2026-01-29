#!/usr/bin/env python3
"""
debug_recursive_patterns.py
Detailed debugging for the recursive pattern detection in the phi-harmonic function inference system.
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
logger = logging.getLogger('debug_recursive_patterns')

def read_file(file_path):
    """Read a file and return its contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def debug_process_data_function():
    """Debug the process_data function analysis in detail."""
    logger.info("Debugging process_data function analysis...")
    
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
    
    # Set the function_nodes attribute on the inference object
    inference.function_nodes = function_nodes
    
    # Get the process_data function node
    process_data_node = function_nodes.get('process_data')
    if not process_data_node:
        logger.error("process_data function not found")
        return
    
    # Analyze the AST patterns with recursive detection
    logger.debug("Analyzing AST patterns for process_data...")
    analysis_result = inference._analyze_ast_patterns(process_data_node, recursive=True)
    
    # Log the analysis result
    logger.debug(f"Analysis result patterns: {analysis_result.get('patterns')}")
    logger.debug(f"Analysis result nested functions: {analysis_result.get('nested_functions')}")
    
    # Check if nested_calls is in the patterns
    nested_calls = analysis_result.get('patterns', {}).get('nested_calls', [])
    logger.debug(f"Nested calls: {nested_calls}")
    
    # Check if the required functions are in nested_calls
    required_functions = ['filter_positives', 'square_values', 'normalize_values']
    logger.debug(f"All required functions in nested_calls: {all(func in nested_calls for func in required_functions)}")
    logger.debug(f"All required functions in function_nodes: {all(func in function_nodes for func in required_functions)}")
    
    # Match patterns to behaviors
    logger.debug("Matching patterns to behaviors...")
    nested_functions = analysis_result.get('nested_functions', {})
    behavior_result = inference._match_patterns_to_behavior(
        analysis_result.get('patterns', {}),
        'process_data',
        nested_functions
    )
    
    # Log the behavior result
    logger.debug(f"Behavior result: {behavior_result}")
    
    # Check the composite pattern detection logic
    logger.debug("Checking composite pattern detection logic...")
    patterns = analysis_result.get('patterns', {})
    nested_calls = patterns.get('nested_calls', [])
    
    logger.debug(f"Checking filter-transform-normalize pattern:")
    logger.debug(f"  Required functions: {required_functions}")
    logger.debug(f"  Nested calls: {nested_calls}")
    logger.debug(f"  All required in nested_calls: {all(func in nested_calls for func in required_functions)}")
    logger.debug(f"  All required in function_nodes: {all(func in function_nodes for func in required_functions)}")
    
    # Check the condition that should trigger the filter-transform-normalize pattern
    condition_met = (
        all(func in nested_calls for func in required_functions) and
        all(func in function_nodes for func in required_functions)
    )
    logger.debug(f"Condition for filter-transform-normalize pattern met: {condition_met}")

def debug_recursive_sum_function():
    """Debug the recursive_sum function analysis in detail."""
    logger.info("Debugging recursive_sum function analysis...")
    
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
    
    # Set the function_nodes attribute on the inference object
    inference.function_nodes = function_nodes
    
    # Get the recursive_sum function node
    recursive_sum_node = function_nodes.get('recursive_sum')
    if not recursive_sum_node:
        logger.error("recursive_sum function not found")
        return
    
    # Analyze the AST patterns with recursive detection
    logger.debug("Analyzing AST patterns for recursive_sum...")
    analysis_result = inference._analyze_ast_patterns(recursive_sum_node, recursive=True)
    
    # Log the analysis result
    logger.debug(f"Analysis result patterns: {analysis_result.get('patterns')}")
    logger.debug(f"Analysis result nested functions: {analysis_result.get('nested_functions')}")
    
    # Check if nested_calls is in the patterns
    nested_calls = analysis_result.get('patterns', {}).get('nested_calls', [])
    logger.debug(f"Nested calls: {nested_calls}")
    
    # Check if recursive_sum is in nested_calls (recursive pattern)
    logger.debug(f"recursive_sum in nested_calls: {'recursive_sum' in nested_calls}")
    
    # Match patterns to behaviors
    logger.debug("Matching patterns to behaviors...")
    nested_functions = analysis_result.get('nested_functions', {})
    behavior_result = inference._match_patterns_to_behavior(
        analysis_result.get('patterns', {}),
        'recursive_sum',
        nested_functions
    )
    
    # Log the behavior result
    logger.debug(f"Behavior result: {behavior_result}")
    
    # Check the recursive pattern detection logic
    logger.debug("Checking recursive pattern detection logic...")
    patterns = analysis_result.get('patterns', {})
    nested_calls = patterns.get('nested_calls', [])
    
    logger.debug(f"Checking recursive pattern:")
    logger.debug(f"  Function name: recursive_sum")
    logger.debug(f"  Nested calls: {nested_calls}")
    logger.debug(f"  Function calls itself: {'recursive_sum' in nested_calls}")
    
    # Check the condition that should trigger the recursive pattern
    condition_met = 'recursive_sum' in nested_calls
    logger.debug(f"Condition for recursive pattern met: {condition_met}")

def main():
    """Main function to run the debug script."""
    logger.info("Starting detailed recursive pattern detection debugging...")
    
    # Debug process_data function
    debug_process_data_function()
    
    # Debug recursive_sum function
    debug_recursive_sum_function()
    
    logger.info("Detailed debugging completed.")

if __name__ == "__main__":
    main()
