#!/usr/bin/env python3
"""
test_recursive_inference.py
Test script for the recursive pattern detection in the phi-harmonic function inference system.
"""

import os
import json
import logging
from quantum_phi_function_inference import PhiHarmonicFunctionInference

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('recursive_inference_test')

def read_file(file_path):
    """Read a file and return its contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def save_results(results, output_file):
    """Save inference results to a JSON file."""
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    logger.info(f"Results saved to {output_file}")

def test_nested_functions():
    """Test recursive pattern detection on nested functions."""
    logger.info("Testing recursive pattern detection on nested functions...")
    
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
    
    results = {}
    
    for func_name in functions_to_test:
        logger.info(f"Analyzing function: {func_name}")
        result = inference.infer_function_behavior(source_code, func_name)
        
        # Log the results
        logger.info(f"Inferred behavior: {result['inferred_behavior']}")
        logger.info(f"Confidence: {result['confidence']:.4f}")
        logger.info(f"Phi-resonance: {result['phi_resonance']:.6f}")
        
        if 'composite_pattern' in result:
            logger.info(f"Composite pattern detected: {result['composite_type']}")
        
        # Store the results
        results[func_name] = {
            'inferred_behavior': result.get('inferred_behavior'),
            'confidence': result.get('confidence', 0.0),
            'phi_resonance': result.get('phi_resonance', 0.0),
            'patterns': result.get('patterns', {}),
            'nested_functions': {k: v for k, v in result.get('nested_functions', {}).items()},
            'composite_pattern': result.get('composite_pattern', False),
            'composite_type': result.get('composite_type', None)
        }
    
    # Save the results
    output_file = os.path.join(os.path.dirname(__file__), 'recursive_inference_results.json')
    save_results(results, output_file)
    
    return results

def test_individual_functions():
    """Test individual functions in the nested functions file."""
    logger.info("Testing individual functions...")
    
    # Initialize the phi-harmonic function inference system
    inference = PhiHarmonicFunctionInference()
    
    # Read the test file with nested functions
    file_path = os.path.join(os.path.dirname(__file__), 'nested_functions.py')
    source_code = read_file(file_path)
    
    # Test individual functions
    functions_to_test = [
        'filter_positives',
        'square_values',
        'normalize_values'
    ]
    
    results = {}
    
    for func_name in functions_to_test:
        logger.info(f"Analyzing function: {func_name}")
        result = inference.infer_function_behavior(source_code, func_name)
        
        # Log the results
        logger.info(f"Inferred behavior: {result['inferred_behavior']}")
        logger.info(f"Confidence: {result['confidence']:.4f}")
        logger.info(f"Phi-resonance: {result['phi_resonance']:.6f}")
        
        # Store the results
        results[func_name] = {
            'inferred_behavior': result.get('inferred_behavior'),
            'confidence': result.get('confidence', 0.0),
            'phi_resonance': result.get('phi_resonance', 0.0),
            'patterns': result.get('patterns', {})
        }
    
    # Save the results
    output_file = os.path.join(os.path.dirname(__file__), 'individual_inference_results.json')
    save_results(results, output_file)
    
    return results

def main():
    """Main function to run the tests."""
    logger.info("Starting recursive pattern detection tests...")
    
    # Test nested functions
    nested_results = test_nested_functions()
    
    # Test individual functions
    individual_results = test_individual_functions()
    
    logger.info("All tests completed successfully.")
    
    # Print summary
    print("\n=== Recursive Pattern Detection Test Results ===")
    print("\nComposite Functions:")
    for func, result in nested_results.items():
        composite = "Yes" if result.get('composite_pattern') else "No"
        print(f"  {func}: {result['inferred_behavior']} (Confidence: {result['confidence']:.4f}, Composite: {composite})")
    
    print("\nIndividual Functions:")
    for func, result in individual_results.items():
        print(f"  {func}: {result['inferred_behavior']} (Confidence: {result['confidence']:.4f})")

if __name__ == "__main__":
    main()
