#!/usr/bin/env python3
"""
Quantum Healing Runner
---------------------

This script combines the QuantumOrchestrator with the UniversalHealer extension
to heal and evolve Python files with advanced quantum concepts.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: 0.991800 (φ⁷·⁵/10)
"""

import os
import sys
import logging
import traceback
from datetime import datetime

# Import the orchestrator and healing extension
from quantum_orchestrator import QuantumOrchestrator
from quantum_orchestrator_healing_extension import UniversalHealer

# Import MoA connector if available
try:
    from quantum_moa_orchestrator_connector import QuantumMoAOrchestratorConnector
    MOA_ENABLED = True
except ImportError:
    MOA_ENABLED = False

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumHealingRunner")

def run_healing_and_evolution(target_file):
    """
    Run the healing and evolution process on the target file.
    
    Args:
        target_file: Path to the Python file to heal and evolve
    """
    logger.info(f"Starting healing and evolution process for {target_file}")
    
    # Step 1: Initialize the orchestrator
    try:
        orchestrator = QuantumOrchestrator(target_file)
        logger.info("Orchestrator initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize orchestrator: {e}")
        return False
    
    # Step 2: Try to run the file directly first
    try:
        logger.info("Attempting to run the file directly")
        result = os.system(f"python {target_file}")
        if result == 0:
            logger.info("File ran successfully, no healing needed")
            return True
    except Exception as e:
        logger.info(f"File execution failed: {e}")
    
    # Step 3: Initialize the universal healer
    healer = UniversalHealer(target_file)
    logger.info("Universal healer initialized")
    
    # Step 4: Attempt to heal any syntax errors
    try:
        # Run the file and capture any errors
        logger.info("Running file to capture errors")
        import subprocess
        result = subprocess.run(
            [sys.executable, target_file],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            error_output = result.stderr
            logger.info(f"Captured error: {error_output}")
            
            # Attempt healing with the universal healer
            healed = healer.heal(error_output)
            logger.info(f"Healing attempt result: {'Success' if healed else 'Failed'}")
            
            if healed:
                # Try running the file again
                result = os.system(f"python {target_file}")
                if result == 0:
                    logger.info("File ran successfully after healing")
                else:
                    logger.warning("File still has errors after healing")
            else:
                logger.warning("Healing failed")
        else:
            logger.info("File ran successfully, no healing needed")
    except Exception as e:
        logger.error(f"Error during healing process: {e}")
        traceback.print_exc()
    
    # Step 5: If MoA is available, use it for advanced analysis
    if MOA_ENABLED:
        try:
            logger.info("Initializing MoA connector for advanced analysis")
            moa_connector = QuantumMoAOrchestratorConnector(orchestrator=orchestrator)
            
            # Process the file with MoA agents
            logger.info("Processing file with MoA agents")
            moa_connector.process_file(target_file)
            
            # Get the results
            results = moa_connector.get_action_history()
            logger.info(f"MoA processing results: {len(results)} actions performed")
            
            # Print a summary of the actions
            for action in results:
                logger.info(f"MoA action: {action.get('type', 'unknown')} - {action.get('description', 'no description')}")
        except Exception as e:
            logger.error(f"Error during MoA processing: {e}")
            traceback.print_exc()
    
    logger.info("Healing and evolution process completed")
    return True

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python run_quantum_healing.py <target_file>")
        return
    
    target_file = sys.argv[1]
    if not os.path.exists(target_file):
        print(f"Error: File {target_file} not found")
        return
    
    run_healing_and_evolution(target_file)

if __name__ == "__main__":
    main()
