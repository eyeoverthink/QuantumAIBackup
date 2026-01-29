"""
Quantum Orchestrator Factory

This module provides a factory function to create instances of the QuantumOrchestrator
without modifying the core orchestrator file, following the modular "lego" architecture.

Created: 2025-07-17
Coherence: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import logging
import tempfile
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('QuantumOrchestratorFactory')

def create_orchestrator(target_file: Optional[str] = None) -> 'QuantumOrchestrator':
    """
    Factory function to create a Quantum Orchestrator instance.
    
    If target_file is not provided, a temporary file will be created.
    
    Args:
        target_file: Optional path to the target file for the orchestrator
        
    Returns:
        QuantumOrchestrator instance
    """
    from quantum_orchestrator import QuantumOrchestrator
    
    # If no target file is provided, create a temporary one
    if target_file is None:
        # Create a temporary file with minimal valid Python content
        temp_fd, target_file = tempfile.mkstemp(suffix='.py')
        with os.fdopen(temp_fd, 'w') as f:
            f.write('# Temporary file for Quantum Orchestrator\n')
            f.write('def main():\n')
            f.write('    print("Quantum Orchestrator Temporary File")\n\n')
            f.write('if __name__ == "__main__":\n')
            f.write('    main()\n')
        
        logger.info(f"Created temporary target file: {target_file}")
    
    # Create and return the orchestrator
    orchestrator = QuantumOrchestrator(target_file)
    logger.info(f"Created Quantum Orchestrator for target: {target_file}")
    
    return orchestrator
