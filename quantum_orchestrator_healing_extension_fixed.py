#!/usr/bin/env python3
"""
Quantum Orchestrator Healing Extension (Fixed)
-----------------------------------

This module provides a fixed extension for the quantum orchestrator's healing protocol,
particularly addressing the method signature mismatch in _heal_unclosed_paren().

This follows the 'lego' modular philosophy by extending functionality without
modifying core files.
"""

import logging
import inspect
from typing import Union, Optional, Callable, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumOrchestratorHealingExt")

def patch_heal_unclosed_paren(original_instance: Any, content: Optional[str] = None) -> str:
    """
    A wrapper for the _heal_unclosed_paren method that handles both 1 and 2 argument versions.
    
    This function adapts to both:
    - _heal_unclosed_paren(self)
    - _heal_unclosed_paren(self, content)
    
    Args:
        original_instance: The instance of QuantumOrchestrator
        content: Optional content to heal
        
    Returns:
        str: Healed content
    """
    logger.info("Using compatible _heal_unclosed_paren wrapper")
    
    # Get the original method
    original_method = getattr(original_instance.__class__, '_heal_unclosed_paren', None)
    
    if not original_method:
        logger.error("Original _heal_unclosed_paren method not found")
        return content or ""
    
    # Check the signature of the original method
    sig = inspect.signature(original_method)
    param_count = len(sig.parameters)
    
    try:
        if param_count == 1:  # Only self
            logger.info("Calling single-argument _heal_unclosed_paren")
            # The original method doesn't take content, it must access it from self
            return original_method(original_instance)
        else:  # self and content
            logger.info("Calling two-argument _heal_unclosed_paren")
            # The original method takes content as an argument
            return original_method(original_instance, content)
    except Exception as e:
        logger.error(f"Error in _heal_unclosed_paren wrapper: {e}")
        # Return the original content if healing fails
        return content or ""

def apply_healing_patches(orchestrator_instance: Any) -> None:
    """
    Apply all healing patches to the orchestrator instance.
    
    Args:
        orchestrator_instance: The instance of QuantumOrchestrator to patch
    """
    logger.info("Applying orchestrator healing patches")
    
    # Store the original method
    original_method = getattr(orchestrator_instance.__class__, '_heal_unclosed_paren', None)
    
    if original_method:
        # Create a bound method that will properly handle 'self'
        def patched_method(self, content=None):
            return patch_heal_unclosed_paren(self, content)
        
        # Apply the patch to the class
        setattr(orchestrator_instance.__class__, '_heal_unclosed_paren', patched_method)
        logger.info("Successfully patched _heal_unclosed_paren method")
    else:
        logger.warning("Could not find _heal_unclosed_paren method to patch")

# Example usage
if __name__ == "__main__":
    # This would be used in a real scenario where you have an orchestrator instance
    class MockOrchestrator:
        def _heal_unclosed_paren(self):
            return "Healed content"
    
    mock = MockOrchestrator()
    apply_healing_patches(mock)
    
    # Now the mock should have the patched method
    result = mock._heal_unclosed_paren("Test content")
    print(f"Result: {result}")
