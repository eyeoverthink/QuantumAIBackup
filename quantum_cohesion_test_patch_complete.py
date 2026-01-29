#!/usr/bin/env python3
"""
Quantum Cohesion Test Patch (Complete)
-------------------------

This module provides runtime patches for the quantum cohesion test to ensure
it uses the final versions of all extended components without modifying the original
test file.

This follows the 'lego' modular philosophy by extending functionality without
modifying core files.
"""

import sys
import logging
import importlib.util
from types import ModuleType

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumCohesionTestPatch")

class ModulePatches:
    """Manages runtime patches for modules."""
    
    @staticmethod
    def patch_module(module_name, patches):
        """
        Patch a module with new attributes.
        
        Args:
            module_name (str): Name of the module to patch
            patches (dict): Dictionary of attribute names to patch values
        """
        if module_name in sys.modules:
            for attr_name, attr_value in patches.items():
                setattr(sys.modules[module_name], attr_name, attr_value)
                logger.info(f"Patched {module_name}.{attr_name}")
        else:
            logger.warning(f"Module {module_name} not loaded, cannot patch")

    @staticmethod
    def create_module_proxy(real_module_name, proxy_name=None):
        """
        Create a proxy module that will be imported instead of the real module.
        
        Args:
            real_module_name (str): Name of the real module to proxy
            proxy_name (str, optional): Name for the proxy module. If None, uses real_module_name
            
        Returns:
            ModuleType: The proxy module
        """
        if proxy_name is None:
            proxy_name = real_module_name
            
        # Create a new module
        proxy_module = ModuleType(proxy_name)
        
        # Add it to sys.modules
        sys.modules[proxy_name] = proxy_module
        
        # Import the real module
        real_module = importlib.import_module(real_module_name)
        
        # Copy all attributes from the real module to the proxy
        for attr_name in dir(real_module):
            if not attr_name.startswith('__'):
                setattr(proxy_module, attr_name, getattr(real_module, attr_name))
                
        logger.info(f"Created proxy module {proxy_name} for {real_module_name}")
        return proxy_module

def apply_quantum_patches():
    """Apply all quantum component patches."""
    logger.info("Applying quantum cohesion test patches...")
    
    # 1. Patch quantum_orchestrator module
    try:
        from quantum_orchestrator_adapter import QuantumOrchestratorAdapter
        
        def patched_orchestrator_import():
            """Patch the QuantumOrchestrator import in the test."""
            # Original import: from quantum_orchestrator import QuantumOrchestrator
            import quantum_orchestrator
            quantum_orchestrator.QuantumOrchestrator = QuantumOrchestratorAdapter
            logger.info("Patched quantum_orchestrator.QuantumOrchestrator with QuantumOrchestratorAdapter")
            
        patched_orchestrator_import()
    except Exception as e:
        logger.error(f"Failed to patch QuantumOrchestrator: {e}")
    
    # 2. Patch quantum_resonance_optimizer module with FINAL extension
    try:
        from quantum_resonance_optimizer_extension_final import QuantumResonanceOptimizerExtension
        
        def patched_optimizer_import():
            """Patch the QuantumResonanceOptimizer import in the test."""
            # Original import: from quantum_resonance_optimizer import QuantumResonanceOptimizer
            import quantum_resonance_optimizer
            quantum_resonance_optimizer.QuantumResonanceOptimizer = QuantumResonanceOptimizerExtension
            logger.info("Patched quantum_resonance_optimizer.QuantumResonanceOptimizer with QuantumResonanceOptimizerExtension (FINAL)")
            
        patched_optimizer_import()
    except Exception as e:
        logger.error(f"Failed to patch QuantumResonanceOptimizer: {e}")
    
    # 3. Patch quantum_harmonic_visualizer module with FIXED extension
    try:
        from quantum_harmonic_visualizer_extension_fixed import QuantumHarmonicVisualizerExtension
        
        def patched_visualizer_import():
            """Patch the QuantumHarmonicVisualizer import in the test."""
            # Original import: from quantum_harmonic_visualizer import QuantumHarmonicVisualizer
            import quantum_harmonic_visualizer
            quantum_harmonic_visualizer.QuantumHarmonicVisualizer = QuantumHarmonicVisualizerExtension
            logger.info("Patched quantum_harmonic_visualizer.QuantumHarmonicVisualizer with QuantumHarmonicVisualizerExtension (FIXED)")
            
        patched_visualizer_import()
    except Exception as e:
        logger.error(f"Failed to patch QuantumHarmonicVisualizer: {e}")
    
    # 4. Patch quantum_orchestrator_healing_extension for unclosed parenthesis fix
    try:
        from quantum_orchestrator_healing_extension_final import apply_healing_patches
        
        def apply_fixed_healing_patch():
            """Apply the final healing patches for orchestrator."""
            import quantum_orchestrator
            from quantum_orchestrator import QuantumOrchestrator
            
            # Get an instance to patch the class
            dummy_instance = QuantumOrchestrator("dummy.py")
            
            # Apply all healing patches
            apply_healing_patches(dummy_instance)
            
            # Update the class with the patched methods
            for attr_name in dir(dummy_instance):
                if attr_name.startswith('_heal_') or attr_name == 'run_and_heal':
                    setattr(QuantumOrchestrator, attr_name, getattr(dummy_instance, attr_name))
            
            logger.info("Applied all healing patches to QuantumOrchestrator class")
                
        apply_fixed_healing_patch()
    except Exception as e:
        logger.error(f"Failed to apply healing patches: {e}")
    
    # 5. Fix JSON serialization in test results
    try:
        import json
        import numpy as np
        
        # Create a custom JSON encoder for NumPy types
        class NumpyJSONEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, np.integer):
                    return int(obj)
                elif isinstance(obj, np.floating):
                    return float(obj)
                elif isinstance(obj, np.ndarray):
                    return obj.tolist()
                elif isinstance(obj, np.bool_):
                    return bool(obj)
                return super().default(obj)
        
        # Patch the json module
        json._original_dump = json.dump
        json._original_dumps = json.dumps
        
        def patched_dump(obj, fp, *args, **kwargs):
            return json._original_dump(obj, fp, cls=NumpyJSONEncoder, *args, **kwargs)
        
        def patched_dumps(obj, *args, **kwargs):
            return json._original_dumps(obj, cls=NumpyJSONEncoder, *args, **kwargs)
        
        json.dump = patched_dump
        json.dumps = patched_dumps
        
        logger.info("Patched json module with NumPy-compatible encoder")
    except Exception as e:
        logger.error(f"Failed to patch json module: {e}")
    
    logger.info("All quantum patches applied")

if __name__ == "__main__":
    apply_quantum_patches()
    
    # Run the original test
    import test_quantum_cohesion
    test_quantum_cohesion.run_cohesion_test()
