"""
debug_nested_calls.py
Debug script to analyze nested function calls in the process_data function.
"""

import ast
import json
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('debug_nested_calls')

def extract_nested_calls(source_code, func_name):
    """Extract nested function calls from a function."""
    try:
        # Parse the source code
        parsed = ast.parse(source_code)
        
        # Find the target function node
        target_func_node = None
        for node in ast.walk(parsed):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                target_func_node = node
                break
        
        if not target_func_node:
            logger.error(f"Function '{func_name}' not found in source code")
            return None
        
        # Extract nested function calls
        nested_calls = []
        for node in ast.walk(target_func_node):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                nested_calls.append(node.func.id)
        
        return nested_calls
    
    except Exception as e:
        logger.error(f"Error extracting nested calls: {str(e)}")
        return None

def main():
    logger.info("Starting nested calls debug...")
    
    # Read the source code
    try:
        with open('nested_functions.py', 'r') as f:
            source_code = f.read()
    except Exception as e:
        logger.error(f"Error reading source file: {str(e)}")
        return
    
    # Extract nested calls from process_data
    process_data_calls = extract_nested_calls(source_code, 'process_data')
    logger.info(f"Nested calls in process_data: {process_data_calls}")
    
    # Extract nested calls from recursive_sum
    recursive_sum_calls = extract_nested_calls(source_code, 'recursive_sum')
    logger.info(f"Nested calls in recursive_sum: {recursive_sum_calls}")
    
    # Extract nested calls from other functions
    filter_calls = extract_nested_calls(source_code, 'filter_positives')
    logger.info(f"Nested calls in filter_positives: {filter_calls}")
    
    square_calls = extract_nested_calls(source_code, 'square_values')
    logger.info(f"Nested calls in square_values: {square_calls}")
    
    normalize_calls = extract_nested_calls(source_code, 'normalize_values')
    logger.info(f"Nested calls in normalize_values: {normalize_calls}")
    
    logger.info("Nested calls debug completed.")

if __name__ == '__main__':
    main()
