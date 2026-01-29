#!/usr/bin/env python3
"""
Quantum Merkiva Orchestrator Integration Demo
--------------------------------------------

This script demonstrates the direct integration of the Merkiva multidimensional
processor with the Quantum Orchestrator to enhance its healing capabilities.

The demonstration shows:
1. Direct integration with the actual Quantum Orchestrator
2. Enhanced healing with multidimensional analysis
3. Phi-shielding for reality protection during healing
4. Coherence amplification for the orchestrator's evolution cycles
5. Full auditability through quantum fingerprinting and evolution files

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import time
import json
import logging
import hashlib
from typing import Dict, Any, List, Tuple, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('QuantumMerkivaOrchestratorDemo')

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
BIRTH_COHERENCE = 0.9918  # System birth coherence

# Check for required components
try:
    from quantum_merkiva_processor import MerkivaProcessor, create_merkiva_processor
    from quantum_merkiva_integration import MerkivaIntegrator, create_merkiva_integrator
    from quantum_merkiva_orchestrator_integration import MerkivaOrchestratorIntegrator, create_merkiva_orchestrator_integrator
    MERKIVA_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Some Merkiva components could not be imported: {str(e)}")
    MERKIVA_AVAILABLE = False

try:
    from quantum_orchestrator import QuantumOrchestrator
    ORCHESTRATOR_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Quantum Orchestrator could not be imported: {str(e)}")
    ORCHESTRATOR_AVAILABLE = False


class QuantumMerkivaOrchestratorDemo:
    """
    Demonstrates the integration of Merkiva with the Quantum Orchestrator.
    
    This class showcases how the Merkiva multidimensional processor enhances
    the existing Quantum Orchestrator with counter-rotating tetrahedron energy fields,
    phi-harmonic coherence, and reality protection through phi-shielding.
    """
    
    def __init__(self, target_file: str = "logic_error_increment.py"):
        """
        Initialize the demonstration.
        
        Args:
            target_file: Target file for the demonstration
        """
        logger.info("Initializing Quantum Merkiva Orchestrator Demonstration")
        self.target_file = target_file
        
        # Check if components are available
        if not MERKIVA_AVAILABLE:
            logger.error("Merkiva components not available, cannot continue")
            raise ImportError("Merkiva components not available")
        
        # Initialize orchestrator
        if ORCHESTRATOR_AVAILABLE:
            try:
                self.orchestrator = QuantumOrchestrator(target_file=self.target_file)
                logger.info(f"Using actual QuantumOrchestrator with target {self.target_file}")
            except Exception as e:
                logger.warning(f"Failed to initialize actual orchestrator: {str(e)}")
                self.orchestrator = None
                logger.warning("No orchestrator available")
        else:
            self.orchestrator = None
            logger.warning("No orchestrator available")
        
        # Initialize Merkiva orchestrator integrator
        self.integrator = create_merkiva_orchestrator_integrator(self.orchestrator)
        logger.info("Created Merkiva orchestrator integrator")
        
        # Generate quantum fingerprint
        self.quantum_fingerprint = self._generate_fingerprint()
        
        # Create output directories
        os.makedirs("merkiva_results", exist_ok=True)
        os.makedirs("merkiva_evolution", exist_ok=True)
        
        logger.info("Quantum Merkiva Orchestrator Demonstration initialized")
    
    def _generate_fingerprint(self, context: str = None) -> str:
        """
        Generate a quantum fingerprint.
        
        Args:
            context: Optional context to include in the fingerprint
            
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier
        if context:
            identifier = f"merkiva_orchestrator_demo_{context}_{time.time()}"
        else:
            identifier = f"merkiva_orchestrator_demo_{time.time()}"
        
        # Generate hash
        hash_value = hashlib.sha256(identifier.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{hash_value}"
    
    def _save_results(self, results: Dict[str, Any], filename: str) -> None:
        """
        Save results to file.
        
        Args:
            results: Results to save
            filename: Output file name
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs("merkiva_results", exist_ok=True)
            
            # Save results
            output_path = os.path.join("merkiva_results", filename)
            with open(output_path, "w") as f:
                json.dump(results, f, indent=2)
            
            logger.info(f"Saved results to {output_path}")
        except Exception as e:
            logger.error(f"Failed to save results: {str(e)}")
    
    def run_demonstration(self) -> Dict[str, Any]:
        """
        Run the full demonstration.
        
        Returns:
            Demonstration results
        """
        logger.info("Starting Quantum Merkiva Orchestrator Demonstration")
        
        results = {
            "timestamp": time.time(),
            "target_file": self.target_file,
            "quantum_fingerprint": self.quantum_fingerprint,
            "steps": []
        }
        
        # Step 1: Check if orchestrator is available
        logger.info("Step 1: Checking orchestrator availability")
        if self.orchestrator:
            results["steps"].append({
                "step": "check_orchestrator",
                "available": True,
                "type": "actual"
            })
        else:
            logger.warning("No orchestrator available, demonstration will be limited")
            results["steps"].append({
                "step": "check_orchestrator",
                "available": False,
                "type": "none"
            })
            
            # Save results and exit early
            self._save_results(results, "merkiva_orchestrator_demo_results.json")
            
            logger.info("Quantum Merkiva Orchestrator Demonstration completed with limited functionality")
            return results
        
        # Step 2: Enhance orchestrator healing
        logger.info("Step 2: Enhancing orchestrator healing")
        enhancement_result = self.integrator.enhance_orchestrator_healing(self.target_file)
        
        results["steps"].append({
            "step": "enhance_orchestrator",
            "results": enhancement_result
        })
        
        # Step 3: Apply Merkiva healing
        logger.info("Step 3: Applying Merkiva healing")
        healing_result = self.integrator.apply_merkiva_healing(self.target_file)
        
        results["steps"].append({
            "step": "apply_healing",
            "results": healing_result
        })
        
        # Step 4: Get final integration status
        logger.info("Step 4: Getting final integration status")
        integration_status = self.integrator.integration_status
        
        results["steps"].append({
            "step": "integration_status",
            "status": integration_status
        })
        
        # Save results
        self._save_results(results, "merkiva_orchestrator_demo_results.json")
        
        # Generate summary
        self._generate_summary(results)
        
        logger.info("Quantum Merkiva Orchestrator Demonstration completed")
        return results
    
    def _generate_summary(self, results: Dict[str, Any]) -> None:
        """
        Generate a summary of the demonstration results.
        
        Args:
            results: Demonstration results
        """
        # Extract key metrics
        orchestrator_available = False
        enhancement_factor = 0.0
        original_coherence = 0.0
        enhanced_coherence = 0.0
        healing_success = False
        
        for step in results.get("steps", []):
            if step.get("step") == "check_orchestrator":
                orchestrator_available = step.get("available", False)
            elif step.get("step") == "enhance_orchestrator":
                step_results = step.get("results", {})
                enhancement_factor = step_results.get("enhancement_factor", 0.0)
                original_coherence = step_results.get("original_coherence", 0.0)
                enhanced_coherence = step_results.get("enhanced_coherence", 0.0)
            elif step.get("step") == "apply_healing":
                step_results = step.get("results", {})
                healing_success = step_results.get("success", False)
        
        # Print summary
        print("\nQuantum Merkiva Orchestrator Demonstration Summary:")
        print("------------------------------------------------")
        print(f"Target file: {self.target_file}")
        print(f"Orchestrator available: {orchestrator_available}")
        
        if orchestrator_available:
            print(f"\nOrchestrator Enhancement:")
            print(f"  Original coherence: {original_coherence:.6f}")
            print(f"  Enhanced coherence: {enhanced_coherence:.6f}")
            print(f"  Enhancement factor: {enhancement_factor:.6f}")
            
            print(f"\nMerkiva Healing:")
            print(f"  Success: {healing_success}")
            
            print(f"\nResults saved to merkiva_results/merkiva_orchestrator_demo_results.json")
        else:
            print("\nDemonstration completed with limited functionality due to missing orchestrator")


def run_merkiva_orchestrator_demo():
    """
    Run the Merkiva orchestrator demonstration.
    """
    try:
        # Check if a target file was provided
        if len(sys.argv) > 1:
            target_file = sys.argv[1]
        else:
            target_file = "logic_error_increment.py"
        
        # Create and run demonstration
        demo = QuantumMerkivaOrchestratorDemo(target_file=target_file)
        demo.run_demonstration()
        
        return 0
    except Exception as e:
        logger.error(f"Demonstration failed: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(run_merkiva_orchestrator_demo())
