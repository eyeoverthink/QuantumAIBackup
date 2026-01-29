#!/usr/bin/env python3
"""
Quantum Orchestrator Healing Adapter
-----------------------------------

This module provides a non-invasive adapter for the QuantumAI orchestrator's healing protocols
to ensure compatibility between different method signatures and enable proper integration
with extensions like chord progression analysis.

The adapter follows the modular "lego" architecture principle by providing
a wrapper around the orchestrator's healing methods without modifying the core files.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 0.991800
"""

import os
import sys
import logging
import functools
import types
from typing import Dict, Callable, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumOrchestratorHealingAdapter")

class QuantumOrchestratorHealingAdapter:
    """
    Adapter for the QuantumAI orchestrator's healing protocols to ensure
    compatibility between different method signatures.
    """
    
    def __init__(self, orchestrator):
        """
        Initialize the adapter with a reference to the orchestrator.
        
        Args:
            orchestrator: The QuantumOrchestrator instance to adapt
        """
        self.orchestrator = orchestrator
        self._patch_healing_protocols()
        logger.info("QuantumOrchestratorHealingAdapter initialized")
    
    def _patch_healing_protocols(self):
        """
        Patch the orchestrator's healing protocols to handle different method signatures.
        """
        # Save original healing_protocols dictionary
        original_protocols = self.orchestrator.healing_protocols.copy()
        
        # Create adapted versions of all healing protocols
        for key, heal_func in original_protocols.items():
            # Create an adapter function that can handle being called with or without error_str
            adapted_func = self._create_healing_adapter(heal_func, key)
            
            # Replace the original function with the adapted one
            self.orchestrator.healing_protocols[key] = adapted_func
            
        logger.info(f"Patched {len(original_protocols)} healing protocols")
    
    def _create_healing_adapter(self, original_func, protocol_key):
        """
        Create an adapter function for a healing protocol that can handle
        being called with or without an error_str parameter.
        
        Args:
            original_func: The original healing function
            protocol_key: The key for this healing protocol
            
        Returns:
            A wrapped function that can handle different call signatures
        """
        # Store a reference to self for use in the closure
        adapter_self = self
        
        # Create a new method that will replace the original in the healing_protocols dict
        def adapted_healing_func(error_str=None):
            """
            Adapted healing function that can be called with or without error_str.
            
            Args:
                error_str: Optional error string from run_and_heal
                
            Returns:
                bool: True if healing was successful, False otherwise
            """
            try:
                # Get the bound method directly from the orchestrator instance
                # This ensures we're calling the method on the orchestrator instance
                # rather than trying to call the unbound method and passing self
                bound_method = getattr(adapter_self.orchestrator, original_func.__name__)
                
                # Check if the method takes an error_str parameter
                import inspect
                sig = inspect.signature(bound_method)
                param_count = len(sig.parameters)
                
                # Call the bound method with appropriate arguments
                if param_count == 0:  # No parameters (already bound to self)
                    logger.info(f"Calling {protocol_key} without error_str")
                    return bound_method()
                else:  # Takes at least one parameter
                    logger.info(f"Calling {protocol_key} with error_str")
                    return bound_method(error_str)
            except Exception as e:
                logger.error(f"Error in adapted healing function for {protocol_key}: {e}")
                # Fall back to calling without parameters as a last resort
                try:
                    bound_method = getattr(adapter_self.orchestrator, original_func.__name__)
                    return bound_method()
                except Exception as e2:
                    logger.error(f"Fallback also failed for {protocol_key}: {e2}")
                    return False
        
        return adapted_healing_func

# Example usage
if __name__ == "__main__":
    # This is just an example - in practice, you would import the orchestrator
    class MockOrchestrator:
        def __init__(self):
            self.target_file = "example.py"
            self.healing_protocols = {
                "error1": self._heal_func1,
                "error2": self._heal_func2
            }
        
        def _heal_func1(self):
            print("Healing func1 called without params")
            return True
        
        def _heal_func2(self, error_str):
            print(f"Healing func2 called with: {error_str}")
            return True
    
    # Create adapter
    orchestrator = MockOrchestrator()
    adapter = QuantumOrchestratorHealingAdapter(orchestrator)
    
    # Test adapted protocols
    orchestrator.healing_protocols["error1"]("test error")  # Should work despite signature mismatch
    orchestrator.healing_protocols["error2"]("test error")  # Should work normally
