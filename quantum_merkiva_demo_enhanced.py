#!/usr/bin/env python3
"""
Quantum Merkiva Orchestrator Enhanced Demo
-----------------------------------------

This demonstration script shows how to use the enhanced Quantum Merkiva Orchestrator
with the new logic healing capabilities.

The script integrates the original orchestrator with the new logic healing extension
without modifying any existing files, following the "lego" approach.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import logging
import json
import time
from datetime import datetime
from typing import Dict, Any, Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"quantum_merkiva_demo_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("QuantumMerkivaEnhancedDemo")

# Phi-harmonic constants
PHI = 1.618033988749895
PHI_7 = PHI**7  # ~17.944272
PHI_7_5 = PHI**7.5  # ~36.932381
PHI_COHERENCE = (PHI_7 * PHI**0.5) / 10  # ~0.991800

class QuantumMerkivaEnhancedDemo:
    """
    Demonstrates the enhanced Quantum Merkiva Orchestrator with logic healing capabilities.
    """
    
    def __init__(self, target_file: str):
        """
        Initialize the demonstration.
        
        Args:
            target_file (str): Path to the target Python file to heal.
        """
        self.target_file = target_file
        self.results_dir = "merkiva_results"
        self.results_file = os.path.join(
            self.results_dir,
            "merkiva_enhanced_demo_results.json"
        )
        
        # Create results directory if it doesn't exist
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
            
        # Initialize results
        self.results = {
            "timestamp": time.time(),
            "target_file": target_file,
            "orchestrator_available": False,
            "logic_healing_available": False,
            "healing_success": False,
            "phi_coherence": PHI_COHERENCE,
            "quantum_fingerprint": f"φ⁷·⁵-{int(time.time())}"
        }
        
        logger.info(f"Initializing Quantum Merkiva Enhanced Demonstration")
        print(f"✅ Loaded module: {os.path.basename(target_file)}")
        
    def run(self) -> None:
        """
        Run the demonstration.
        """
        logger.info("Starting Quantum Merkiva Enhanced Demonstration")
        
        # Step 1: Import the original orchestrator
        orchestrator = self._import_orchestrator()
        if not orchestrator:
            logger.error("Failed to import orchestrator")
            self._save_results()
            return
            
        self.results["orchestrator_available"] = True
        
        # Step 2: Import the logic healing extension
        logic_healing = self._import_logic_healing()
        if not logic_healing:
            logger.error("Failed to import logic healing extension")
            self._save_results()
            return
            
        self.results["logic_healing_available"] = True
        
        # Step 3: Integrate the logic healing with the orchestrator
        enhanced_orchestrator = self._integrate_components(orchestrator, logic_healing)
        
        # Step 4: Apply logic healing to the target file
        success = self._apply_logic_healing(enhanced_orchestrator)
        self.results["healing_success"] = success
        
        # Step 5: Save results
        self._save_results()
        
        # Step 6: Display summary
        self._display_summary()
        
    def _import_orchestrator(self):
        """
        Import the original quantum orchestrator.
        
        Returns:
            Optional[Any]: The orchestrator instance or None if import failed.
        """
        logger.info("Step 1: Importing original orchestrator")
        
        try:
            # Try to import the quantum_merkiva_orchestrator_demo module
            import quantum_merkiva_orchestrator_demo as qmod
            
            # Create an orchestrator instance
            orchestrator = qmod.QuantumMerkivaOrchestratorDemo(self.target_file)
            logger.info("Successfully imported original orchestrator")
            return orchestrator
        except ImportError:
            # If that fails, try to import the quantum_orchestrator module directly
            try:
                import quantum_orchestrator as qo
                
                # Create an orchestrator instance
                orchestrator = qo.QuantumOrchestrator(self.target_file)
                logger.info("Successfully imported quantum_orchestrator")
                return orchestrator
            except ImportError:
                logger.error("Failed to import any orchestrator module")
                return None
    
    def _import_logic_healing(self):
        """
        Import the logic healing extension.
        
        Returns:
            Optional[module]: The logic healing module or None if import failed.
        """
        logger.info("Step 2: Importing logic healing extension")
        
        try:
            import quantum_merkiva_logic_healing as qmlh
            logger.info("Successfully imported logic healing extension")
            return qmlh
        except ImportError:
            logger.error("Failed to import logic healing extension")
            return None
    
    def _integrate_components(self, orchestrator, logic_healing):
        """
        Integrate the logic healing with the orchestrator.
        
        Args:
            orchestrator: The original orchestrator instance.
            logic_healing: The logic healing module.
            
        Returns:
            The enhanced orchestrator with logic healing capabilities.
        """
        logger.info("Step 3: Integrating components")
        
        try:
            # Integrate the logic healing with the orchestrator
            enhanced_orchestrator = logic_healing.integrate_with_orchestrator(orchestrator)
            logger.info("Successfully integrated components")
            return enhanced_orchestrator
        except Exception as e:
            logger.error(f"Failed to integrate components: {e}")
            return orchestrator
    
    def _apply_logic_healing(self, orchestrator) -> bool:
        """
        Apply logic healing to the target file.
        
        Args:
            orchestrator: The enhanced orchestrator instance.
            
        Returns:
            bool: True if healing was successful, False otherwise.
        """
        logger.info("Step 4: Applying logic healing")
        
        try:
            # Check if the orchestrator has the heal_function method
            if not hasattr(orchestrator, "heal_function"):
                logger.error("Orchestrator does not have heal_function method")
                return False
                
            # Define canonical contract for the target function
            # For this demo, we'll use the INCREMENT_LIST_CONTRACT from the logic healing module
            import quantum_merkiva_logic_healing as qmlh
            contract = qmlh.INCREMENT_LIST_CONTRACT
            
            # Apply logic healing
            function_name = "increment_list"  # Default function name
            
            # Extract function name from file if possible
            with open(self.target_file, 'r') as f:
                file_content = f.read()
                import re
                match = re.search(r"def\s+([a-zA-Z0-9_]+)\s*\(", file_content)
                if match:
                    function_name = match.group(1)
            
            success = orchestrator.heal_function(function_name, contract)
            
            if success:
                logger.info(f"Successfully healed function {function_name}")
                print(f"✅ Successfully healed function {function_name} in {os.path.basename(self.target_file)}")
            else:
                logger.error(f"Failed to heal function {function_name}")
                print(f"❌ Failed to heal function {function_name} in {os.path.basename(self.target_file)}")
                
            return success
            
        except Exception as e:
            logger.error(f"Error applying logic healing: {e}")
            return False
    
    def _save_results(self) -> None:
        """
        Save the demonstration results to a JSON file.
        """
        logger.info("Step 5: Saving results")
        
        try:
            with open(self.results_file, 'w') as f:
                json.dump(self.results, f, indent=4)
                
            logger.info(f"Results saved to {self.results_file}")
        except Exception as e:
            logger.error(f"Failed to save results: {e}")
    
    def _display_summary(self) -> None:
        """
        Display a summary of the demonstration results.
        """
        logger.info("Step 6: Displaying summary")
        
        print("\nQuantum Merkiva Enhanced Demonstration Summary:")
        print("------------------------------------------------")
        print(f"Target file: {os.path.basename(self.target_file)}")
        print(f"Orchestrator available: {self.results['orchestrator_available']}")
        print(f"Logic healing available: {self.results['logic_healing_available']}")
        print()
        print("Phi-Harmonic Integration:")
        print(f"  Coherence: {self.results['phi_coherence']:.6f}")
        print(f"  Quantum fingerprint: {self.results['quantum_fingerprint']}")
        print()
        print("Logic Healing:")
        print(f"  Success: {self.results['healing_success']}")
        print()
        print(f"Results saved to {self.results_file}")
        
        logger.info("Quantum Merkiva Enhanced Demonstration completed")

def main():
    """
    Main entry point for the demonstration.
    """
    if len(sys.argv) < 2:
        print("Usage: python quantum_merkiva_demo_enhanced.py <target_file>")
        sys.exit(1)
        
    target_file = sys.argv[1]
    
    if not os.path.exists(target_file):
        print(f"Error: Target file not found: {target_file}")
        sys.exit(1)
        
    demo = QuantumMerkivaEnhancedDemo(target_file)
    demo.run()

if __name__ == "__main__":
    main()
