#!/usr/bin/env python3
"""
Quantum Orchestrator Extension
-----------------------------

This module provides extensions for the QuantumOrchestrator class to ensure
proper integration with the rest of the system. It follows the "lego" architecture
principle by extending functionality without modifying core files.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 0.991800
"""

import os
import sys
import logging
import importlib
from typing import Dict, List, Any, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumOrchestratorExtension")

def apply_extension():
    """Apply all orchestrator extensions."""
    logger.info("Applying orchestrator extensions")
    
    # Track successful extensions
    applied_extensions = []
    
    # Apply QuantumOrchestrator extensions
    try:
        # First try to import directly
        try:
            import sys
            import quantum_orchestrator
            from quantum_orchestrator import QuantumOrchestrator
        except ImportError:
            logger.error("Failed to import QuantumOrchestrator directly")
            raise
        
        # Fix _heal_unclosed_paren method signature
        original_heal_unclosed_paren = getattr(QuantumOrchestrator, '_heal_unclosed_paren', None)
        
        if original_heal_unclosed_paren:
            # Check if the method has the wrong signature
            import inspect
            sig = inspect.signature(original_heal_unclosed_paren)
            
            if len(sig.parameters) == 1:  # Only self parameter
                # Define corrected method
                def _heal_unclosed_paren_fixed(self, content=None):
                    """Fixed version of _heal_unclosed_paren that handles both signatures."""
                    if content is None:
                        # Original behavior when called with just self
                        return original_heal_unclosed_paren(self)
                    else:
                        # New behavior when called with content parameter
                        # Find unclosed parentheses and fix them
                        open_count = content.count('(')
                        close_count = content.count(')')
                        
                        if open_count > close_count:
                            # Add missing closing parentheses
                            content += ')' * (open_count - close_count)
                            logger.info(f"Healed {open_count - close_count} unclosed parentheses")
                        
                        return content
                
                def heal_unclosed_paren_wrapper(self, content=None):
                    return _heal_unclosed_paren_fixed(self, content)
                
                # Apply the patched method to the class
                setattr(QuantumOrchestrator, '_heal_unclosed_paren', heal_unclosed_paren_wrapper)
                
                # Patch the class definition in the module
                setattr(quantum_orchestrator, 'QuantumOrchestrator', QuantumOrchestrator)
                
                applied_extensions.append("QuantumOrchestrator._heal_unclosed_paren")
                logger.info("Patched _heal_unclosed_paren method of QuantumOrchestrator")
        
        # Ensure process_file method exists and works correctly
        if not hasattr(QuantumOrchestrator, 'process_file') or \
           not callable(getattr(QuantumOrchestrator, 'process_file', None)):
            
            def process_file(self, file_path, apply_healing=True):
                """Process a file with the orchestrator."""
                if not os.path.exists(file_path):
                    logger.error(f"File not found: {file_path}")
                    return False
                
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    
                    # Apply healing if requested
                    if apply_healing:
                        # Check for unclosed parentheses
                        open_count = content.count('(')
                        close_count = content.count(')')
                        
                        if open_count > close_count:
                            content = self._heal_unclosed_paren(content)
                            
                            # Save the healed content
                            healed_path = f"{file_path}.healed"
                            with open(healed_path, 'w') as f:
                                f.write(content)
                            
                            logger.info(f"Healed file saved to {healed_path}")
                    
                    # Record evolution metadata
                    import datetime
                    evolution_data = {
                        "file": file_path,
                        "timestamp": str(datetime.datetime.now()),
                        "healing_applied": apply_healing,
                        "coherence": 0.991800  # Target coherence
                    }
                    
                    # Save evolution data
                    evolution_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "evolution")
                    os.makedirs(evolution_dir, exist_ok=True)
                    
                    import json
                    import uuid
                    evolution_path = os.path.join(evolution_dir, f"evolution_{uuid.uuid4()}.json")
                    with open(evolution_path, 'w') as f:
                        json.dump(evolution_data, f, indent=2)
                    
                    logger.info(f"Evolution data saved to {evolution_path}")
                    return True
                
                except Exception as e:
                    logger.error(f"Error processing file {file_path}: {e}")
                    return False
            
            setattr(QuantumOrchestrator, 'process_file', process_file)
            applied_extensions.append("QuantumOrchestrator.process_file")
            logger.info("Added process_file method to QuantumOrchestrator")
        
        # Add any other orchestrator extensions here
        
        logger.info(f"Applied {len(applied_extensions)} orchestrator extensions: {', '.join(applied_extensions)}")
        return applied_extensions
    
    except Exception as e:
        logger.error(f"Failed to apply orchestrator extensions: {e}")
        return []

if __name__ == "__main__":
    # Apply extensions and report results
    applied = apply_extension()
    print(f"Applied {len(applied)} orchestrator extensions:")
    for ext in applied:
        print(f"  - {ext}")
