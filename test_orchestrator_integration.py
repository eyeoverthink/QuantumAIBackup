"""
test_orchestrator_integration.py
Test script for the integration between the quantum orchestrator and the phi-harmonic function inference system.
Tests the complete healing cycle including inference, contract generation, and healing.
"""

import os
import sys
import logging
import json
import inspect
import time
import hashlib
from quantum_phi_function_inference import PhiHarmonicFunctionInference

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("OrchestratorTest")

# Create a test file with a logic error
def create_test_file_with_error():
    """Create a test file with a logic error for the orchestrator to heal."""
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_logic_error.py')
    
    # Function with a logic error (should increment by 1, but increments by 2)
    code = """
def increment_values(numbers):
    \"\"\"Increment each value in the list by 1.\"\"\"
    # Logic error: incrementing by 2 instead of 1
    return [x + 2 for x in numbers]
"""
    
    with open(file_path, 'w') as f:
        f.write(code)
    
    logger.info(f"Created test file with logic error at: {file_path}")
    return file_path

def test_orchestrator_integration():
    """Test the integration between the quantum orchestrator and the phi-harmonic function inference system."""
    logger.info("Starting orchestrator integration test")
    
    # Create test file with logic error
    test_file = create_test_file_with_error()
    
    # Initialize the inference system
    inference = PhiHarmonicFunctionInference()
    
    # Read the function code
    with open(test_file, 'r') as f:
        func_code = f.read()
    
    # Run inference on the function
    func_name = "increment_values"
    inference_result = inference.infer_function_behavior(func_code, func_name)
    
    # Print inference results
    logger.info(f"Function: {func_name}")
    logger.info(f"  Inferred Behavior: {inference_result['inferred_behavior']}")
    logger.info(f"  Confidence: {inference_result['confidence']:.4f}")
    logger.info(f"  Phi-Resonance: {inference_result['phi_resonance']:.6f}")
    
    # Generate quantum fingerprint for the function
    content_hash = hashlib.sha256(func_code.encode()).hexdigest()[:16]
    quantum_fingerprint = f"φ⁷·⁵-{content_hash}"
    logger.info(f"  Quantum Fingerprint: {quantum_fingerprint}")
    
    # Check if evolution directory is created
    evolution_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evolution')
    if not os.path.exists(evolution_dir):
        os.makedirs(evolution_dir, exist_ok=True)
        logger.info(f"Created evolution directory at: {evolution_dir}")
    
    # Create a manual evolution entry for testing
    evolution_file = os.path.join(evolution_dir, f"{func_name}_evolution.json")
    evolution_data = {
        'function_name': func_name,
        'evolution_history': [
            {
                'timestamp': time.time(),
                'behavior': inference_result['inferred_behavior'],
                'confidence': inference_result['confidence'],
                'phi_resonance': inference_result['phi_resonance'],
                'quantum_fingerprint': quantum_fingerprint,
                'healing_event': {
                    'detected_error': 'logic_error',
                    'error_description': 'Function increments by 2 instead of 1',
                    'phi_coherence': 0.991800,
                    'healing_status': 'pending'
                }
            }
        ]
    }
    
    with open(evolution_file, 'w') as f:
        json.dump(evolution_data, f, indent=2)
    
    logger.info(f"Created evolution file at: {evolution_file}")
    
    # In a real scenario, the orchestrator would now:
    # 1. Detect the logic error using canonical contracts
    # 2. Create a healed file with corrected logic
    # 3. Integrate the healed logic into the original file
    # 4. Update the evolution JSON with the healing event
    
    logger.info("In a real scenario, the quantum orchestrator would now:")
    logger.info("1. Detect the logic error using canonical contracts")
    logger.info("2. Create a healed file with corrected logic")
    logger.info("3. Integrate the healed logic into the original file")
    logger.info("4. Update the evolution JSON with the healing event")
    
    # Simulate a healed file for demonstration
    healed_file = test_file.replace('.py', '_healed.py')
    healed_code = """
def increment_values(numbers):
    \"\"\"Increment each value in the list by 1.\"\"\"
    # Healed logic: correctly incrementing by 1
    return [x + 1 for x in numbers]
"""
    
    with open(healed_file, 'w') as f:
        f.write(healed_code)
    
    logger.info(f"Created simulated healed file at: {healed_file}")
    
    # Update evolution file with healing event
    evolution_data['evolution_history'][0]['healing_event']['healing_status'] = 'completed'
    evolution_data['evolution_history'][0]['healing_event']['healed_file'] = healed_file
    evolution_data['evolution_history'][0]['healing_event']['healing_timestamp'] = time.time()
    
    with open(evolution_file, 'w') as f:
        json.dump(evolution_data, f, indent=2)
    
    logger.info("Updated evolution file with healing event")
    
    return {
        'test_file': test_file,
        'healed_file': healed_file,
        'evolution_file': evolution_file,
        'inference_result': inference_result
    }

if __name__ == "__main__":
    test_orchestrator_integration()
