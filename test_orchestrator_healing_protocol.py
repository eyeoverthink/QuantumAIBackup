#!/usr/bin/env python3
"""
Test script for validating the orchestrator healing protocol fix.

This script:
1. Creates a test file with an unclosed parenthesis
2. Applies the healing patches to the orchestrator
3. Runs the orchestrator on the test file
4. Validates that the healing was successful

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import logging
import shutil
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("OrchestratorHealingTest")

# Import the healing extension
try:
    from quantum_orchestrator_healing_extension import apply_healing_patches
    HEALING_EXTENSION_AVAILABLE = True
except ImportError:
    logger.error("Quantum orchestrator healing extension not found")
    HEALING_EXTENSION_AVAILABLE = False
    sys.exit(1)

def create_test_file_with_error():
    """Create a test file with an unclosed parenthesis error"""
    test_file_path = "test_files/test_unclosed_paren.py"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
    
    # Create test file with error
    with open(test_file_path, "w") as f:
        f.write("""#!/usr/bin/env python3
\"\"\"
Test file with unclosed parenthesis for orchestrator healing protocol validation.
\"\"\"

def main():
    print("Testing orchestrator healing protocol"
    
    # This function has an unclosed parenthesis above
    result = calculate_phi_resonance(1.618034)
    print(f"Phi resonance: {result}")
    
    return 0

def calculate_phi_resonance(x):
    \"\"\"Calculate phi resonance for a value\"\"\"
    phi = 1.618034
    return (phi * x) % 1

if __name__ == "__main__":
    sys.exit(main())
""")
    
    logger.info(f"Created test file with unclosed parenthesis: {test_file_path}")
    return test_file_path

def validate_healing(test_file_path):
    """Validate that the file was healed correctly"""
    try:
        with open(test_file_path, "r") as f:
            content = f.read()
        
        # Check if the parenthesis was closed
        if 'print("Testing orchestrator healing protocol")' in content:
            logger.info("✅ Healing successful: Parenthesis was properly closed")
            return True
        else:
            logger.error("❌ Healing failed: Parenthesis was not properly closed")
            return False
    except Exception as e:
        logger.error(f"Error validating healing: {e}")
        return False

def main():
    """Main test function"""
    logger.info("Starting orchestrator healing protocol test")
    
    # Step 1: Create test file with error
    test_file_path = create_test_file_with_error()
    
    # Step 2: Apply healing patches
    if not HEALING_EXTENSION_AVAILABLE:
        logger.error("Healing extension not available")
        return 1
    
    logger.info("Applying healing patches to orchestrator")
    if not apply_healing_patches():
        logger.error("Failed to apply healing patches")
        return 1
    
    # Step 3: Run orchestrator on test file
    logger.info("Running orchestrator on test file")
    try:
        from quantum_orchestrator import QuantumOrchestrator
        orchestrator = QuantumOrchestrator(test_file_path)
        # The orchestrator should automatically run and heal the file
        logger.info("Orchestrator execution completed")
    except Exception as e:
        logger.error(f"Error running orchestrator: {e}")
        return 1
    
    # Step 4: Validate healing
    if validate_healing(test_file_path):
        logger.info("✅ Orchestrator healing protocol test PASSED")
        return 0
    else:
        logger.error("❌ Orchestrator healing protocol test FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
