"""
test_inference_integration.py
Test script for the integration between the quantum orchestrator and the phi-harmonic function inference system.
"""

import os
import sys
import logging
import json
import inspect
import time
from quantum_phi_function_inference import PhiHarmonicFunctionInference

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("InferenceTest")

# Sample functions for testing inference
def sum_values(numbers):
    """Sum all values in a list."""
    return sum(numbers)

def square_values(numbers):
    """Square each value in a list."""
    return [n * n for n in numbers]

def normalize_values(numbers):
    """Normalize values to range [0,1]."""
    if not numbers:
        return []
    max_val = max(numbers)
    if max_val == 0:
        return [0] * len(numbers)
    return [n / max_val for n in numbers]

def filter_transform_normalize(numbers):
    """Composite function that filters positive values, squares them, and normalizes."""
    # Filter positive values
    positive_nums = [n for n in numbers if n > 0]
    # Square values
    squared = [n * n for n in positive_nums]
    # Normalize
    if not squared:
        return []
    max_val = max(squared)
    if max_val == 0:
        return [0] * len(squared)
    return [n / max_val for n in squared]

def test_inference():
    """Test the phi-harmonic function inference system."""
    logger.info("Starting phi-harmonic function inference test")
    
    # Initialize the inference system
    inference = PhiHarmonicFunctionInference()
    
    # Test functions
    functions = {
        "sum_values": sum_values,
        "square_values": square_values,
        "normalize_values": normalize_values,
        "filter_transform_normalize": filter_transform_normalize
    }
    
    results = {}
    
    # Run inference on each function
    for func_name, func in functions.items():
        logger.info(f"Analyzing function: {func_name}")
        
        # Get function source code
        func_code = inspect.getsource(func)
        
        # Run inference
        inference_result = inference.infer_function_behavior(func_code, func_name)
        
        # Store results
        results[func_name] = {
            "inferred_behavior": inference_result['inferred_behavior'],
            "confidence": inference_result['confidence'],
            "phi_resonance": inference_result['phi_resonance'],
            "composite": inference_result.get('composite', False)
        }
    
    # Print results
    logger.info("Inference results:")
    for func_name, result in results.items():
        logger.info(f"Function: {func_name}")
        logger.info(f"  Behavior: {result['inferred_behavior']}")
        logger.info(f"  Confidence: {result['confidence']:.4f}")
        logger.info(f"  Phi-Resonance: {result['phi_resonance']:.6f}")
        logger.info(f"  Composite: {result['composite']}")
        logger.info("  ---")
    
    # Test the infer_function_contract function (module-level function, not class method)
    logger.info("Testing infer_function_contract function")
    file_path = __file__
    for func_name in functions:
        try:
            # Import the function directly from the module
            from quantum_phi_function_inference import infer_function_contract
            contract_result = infer_function_contract(file_path, func_name)
            logger.info(f"Contract for {func_name}: {contract_result}")
        except Exception as e:
            logger.error(f"Error inferring contract for {func_name}: {str(e)}")
            logger.error(f"This is expected if the function doesn't exist in the file {file_path}")
    
    # Check if evolution files were created
    evolution_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evolution')
    if os.path.exists(evolution_dir):
        logger.info(f"Evolution directory created at: {evolution_dir}")
        evolution_files = os.listdir(evolution_dir)
        logger.info(f"Evolution files created: {evolution_files}")
    
    return results

if __name__ == "__main__":
    test_inference()
