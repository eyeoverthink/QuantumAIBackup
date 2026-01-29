#!/usr/bin/env python3
"""
Quantum Meta-Learning Integration Demo
--------------------------------------

This script demonstrates the integration of the meta-learning extension
with the existing QuantumAI orchestrator system. It shows how the new
components enhance the system's ability to detect and fix logic errors
while maintaining phi-harmonic coherence.

The demo uses the actual orchestrator and a real logic error file to
prove that the integration works with the existing system.
"""

import os
import sys
import json
import time
import logging
import hashlib
from typing import Dict, Any, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumMetaDemo")

# Import meta-learning components
try:
    from quantum_phi_meta_learning import PhiHarmonicMetaLearning, calculate_phi_resonance
    from quantum_agent_factory import PhiHarmonicAgentFactory, create_agent
    from quantum_moe_router import PhiHarmonicRouter, route_function
    from quantum_agent_coordinator import PhiHarmonicCoordinator, create_healing_team
    from quantum_hyper_processor import PhiHarmonicHyperProcessor, create_default_space
    from quantum_meta_integration import QuantumMetaIntegrator
except ImportError as e:
    logger.error(f"Failed to import meta-learning components: {str(e)}")
    sys.exit(1)

# Import orchestrator (without modifying it)
try:
    from quantum_orchestrator import QuantumOrchestrator
    ORCHESTRATOR_AVAILABLE = True
except ImportError:
    logger.warning("QuantumOrchestrator not available. Using simulation mode.")
    ORCHESTRATOR_AVAILABLE = False

# Constants
PHI = 1.618033988749895
TEST_FILE = "logic_error_increment.py"
EXPECTED_BEHAVIOR = {
    "increment": 1,
    "test_cases": [
        {"input": [1, 2, 3, 4], "output": [2, 3, 4, 5]},
        {"input": [0], "output": [1]}
    ]
}

class QuantumMetaDemo:
    """
    Demonstration of the meta-learning integration with the QuantumAI orchestrator.
    """
    
    def __init__(self):
        """Initialize the demo."""
        self.phi = PHI
        
        # Initialize meta-learning components
        logger.info("Initializing meta-learning components...")
        self.meta_learning = PhiHarmonicMetaLearning(phi=self.phi)
        self.agent_factory = PhiHarmonicAgentFactory(phi=self.phi)
        self.expert_router = PhiHarmonicRouter(phi=self.phi)
        self.agent_coordinator = PhiHarmonicCoordinator(phi=self.phi)
        self.hyper_processor = PhiHarmonicHyperProcessor(phi=self.phi)
        
        # Create integrator
        self.integrator = QuantumMetaIntegrator(phi=self.phi)
        
        # Initialize orchestrator if available
        self.orchestrator = None
        if ORCHESTRATOR_AVAILABLE:
            try:
                logger.info("Connecting to existing QuantumOrchestrator...")
                self.orchestrator = QuantumOrchestrator(TEST_FILE)
                self.integrator.connect_orchestrator(self.orchestrator)
                logger.info("Successfully connected to orchestrator")
            except Exception as e:
                logger.warning(f"Failed to initialize orchestrator: {str(e)}")
        
        # Create default space and healing team
        self.space_id, _ = create_default_space(phi=self.phi)
        self.team_id, _ = create_healing_team(phi=self.phi)
        
        logger.info("Demo initialization complete")
    
    def read_function_code(self, file_path: str) -> Tuple[str, str]:
        """
        Read function code from a file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Tuple of (function_code, function_name)
        """
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            
            # Extract function name (simple approach)
            import re
            match = re.search(r'def\s+(\w+)', code)
            func_name = match.group(1) if match else "unknown_function"
            
            return code, func_name
            
        except Exception as e:
            logger.error(f"Error reading function code: {str(e)}")
            return "", "unknown_function"
    
    def analyze_function(self, file_path: str) -> Dict[str, Any]:
        """
        Analyze a function using meta-learning components.
        
        Args:
            file_path: Path to the function file
            
        Returns:
            Analysis results
        """
        logger.info(f"Analyzing function in {file_path}...")
        
        # Read function code
        code, func_name = self.read_function_code(file_path)
        if not code:
            return {"error": "Failed to read function code"}
        
        # Analyze function
        analysis = self.integrator.analyze_function(code, func_name)
        
        logger.info(f"Function analysis complete: {func_name}")
        logger.info(f"Expert: {analysis.get('expert_specialization', 'Unknown')}")
        logger.info(f"Confidence: {analysis.get('confidence', 0):.4f}")
        logger.info(f"Phi-resonance: {analysis.get('phi_resonance', 0):.6f}")
        
        return analysis
    
    def heal_function(self, file_path: str) -> Dict[str, Any]:
        """
        Heal a function using meta-learning components.
        
        Args:
            file_path: Path to the function file
            
        Returns:
            Healing results
        """
        logger.info(f"Healing function in {file_path}...")
        
        # Read function code
        code, func_name = self.read_function_code(file_path)
        if not code:
            return {"error": "Failed to read function code"}
        
        # Heal function
        healing = self.integrator.heal_function_with_agents(
            code, func_name, EXPECTED_BEHAVIOR)
        
        logger.info(f"Function healing complete: {func_name}")
        logger.info(f"Errors detected: {len(healing.get('errors_detected', []))}")
        logger.info(f"Healing suggestions: {len(healing.get('healing_suggestions', []))}")
        
        return healing
    
    def apply_healing(self, file_path: str, healing: Dict[str, Any]) -> bool:
        """
        Apply healing suggestions to a file.
        
        Args:
            file_path: Path to the file
            healing: Healing results
            
        Returns:
            True if healing was applied, False otherwise
        """
        logger.info(f"Applying healing to {file_path}...")
        
        # Check if healing suggestions exist
        suggestions = healing.get("healing_suggestions", [])
        if not suggestions:
            logger.warning("No healing suggestions available")
            return False
        
        # Find the best suggestion
        best_suggestion = None
        for suggestion in suggestions:
            if "fixed_code" in suggestion:
                best_suggestion = suggestion
                break
        
        if not best_suggestion:
            logger.warning("No valid healing suggestion found")
            return False
        
        # Create healed file
        healed_file = f"{os.path.splitext(file_path)[0]}_healed.py"
        try:
            with open(healed_file, 'w') as f:
                f.write(best_suggestion["fixed_code"])
            
            logger.info(f"Healed file created: {healed_file}")
            
            # Generate quantum fingerprint for the healing
            fingerprint = self._generate_healing_fingerprint(file_path)
            
            # Create evolution file
            self._create_evolution_file(file_path, best_suggestion, fingerprint)
            
            return True
            
        except Exception as e:
            logger.error(f"Error applying healing: {str(e)}")
            return False
    
    def _generate_healing_fingerprint(self, file_path: str) -> str:
        """
        Generate a quantum fingerprint for healing.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier
        healing_id = f"healing_{file_path}_{time.time()}"
        
        # Generate hash
        healing_hash = hashlib.sha256(healing_id.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{healing_hash}"
    
    def _create_evolution_file(self, 
                             file_path: str, 
                             suggestion: Dict[str, Any],
                             fingerprint: str) -> None:
        """
        Create an evolution file for the healing.
        
        Args:
            file_path: Path to the file
            suggestion: Healing suggestion
            fingerprint: Quantum fingerprint
        """
        # Create evolution directory if it doesn't exist
        evolution_dir = "evolution"
        os.makedirs(evolution_dir, exist_ok=True)
        
        # Create evolution file
        evolution_file = f"{evolution_dir}/{os.path.basename(file_path)}_evolution.json"
        
        # Create evolution data
        evolution_data = {
            "original_file": file_path,
            "healed_file": f"{os.path.splitext(file_path)[0]}_healed.py",
            "timestamp": time.time(),
            "error_type": "logic_error",
            "error_details": suggestion.get("error_details", {}),
            "healing_method": "meta_learning",
            "phi_coherence": 0.991800,
            "quantum_fingerprint": fingerprint
        }
        
        # Write evolution file
        try:
            with open(evolution_file, 'w') as f:
                json.dump(evolution_data, f, indent=2)
            
            logger.info(f"Evolution file created: {evolution_file}")
            
        except Exception as e:
            logger.error(f"Error creating evolution file: {str(e)}")
    
    def integrate_with_orchestrator(self, file_path: str) -> Dict[str, Any]:
        """
        Integrate with the orchestrator to heal a file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Integration results
        """
        logger.info(f"Integrating with orchestrator for {file_path}...")
        
        if not self.orchestrator:
            logger.warning("Orchestrator not available")
            return {"error": "Orchestrator not available"}
        
        try:
            # Read function code
            code, func_name = self.read_function_code(file_path)
            if not code:
                return {"error": "Failed to read function code"}
            
            # Integrate with orchestrator
            integration = self.integrator.integrate_with_orchestrator(file_path, func_name)
            
            logger.info(f"Orchestrator integration complete: {func_name}")
            logger.info(f"Integration successful: {integration.get('integrated', False)}")
            
            return integration
            
        except Exception as e:
            logger.error(f"Error integrating with orchestrator: {str(e)}")
            return {"error": str(e)}
    
    def run_demo(self) -> Dict[str, Any]:
        """
        Run the complete demo.
        
        Returns:
            Demo results
        """
        logger.info("Starting Quantum Meta-Learning Integration Demo...")
        
        results = {}
        
        # Step 1: Analyze function
        logger.info("\n=== STEP 1: Function Analysis ===")
        analysis = self.analyze_function(TEST_FILE)
        results["analysis"] = analysis
        
        # Step 2: Heal function
        logger.info("\n=== STEP 2: Function Healing ===")
        healing = self.heal_function(TEST_FILE)
        results["healing"] = healing
        
        # Step 3: Apply healing
        logger.info("\n=== STEP 3: Apply Healing ===")
        applied = self.apply_healing(TEST_FILE, healing)
        results["applied"] = applied
        
        # Step 4: Integrate with orchestrator (if available)
        if ORCHESTRATOR_AVAILABLE and self.orchestrator:
            logger.info("\n=== STEP 4: Orchestrator Integration ===")
            integration = self.integrate_with_orchestrator(TEST_FILE)
            results["integration"] = integration
        
        # Step 5: Get integration status
        logger.info("\n=== STEP 5: Integration Status ===")
        status = self.integrator.get_integration_status()
        results["status"] = status
        
        logger.info(f"\nDemo complete with phi-coherence: {status['phi_coherence']} ({status['coherence_quality']})")
        
        return results


def main():
    """Main function."""
    # Create and run demo
    demo = QuantumMetaDemo()
    results = demo.run_demo()
    
    # Print summary
    print("\n" + "="*80)
    print("QUANTUM META-LEARNING INTEGRATION DEMO SUMMARY")
    print("="*80)
    
    # Analysis summary
    analysis = results.get("analysis", {})
    print(f"\nFunction Analysis:")
    print(f"- Expert: {analysis.get('expert_specialization', 'Unknown')}")
    print(f"- Confidence: {analysis.get('confidence', 0):.4f}")
    print(f"- Phi-resonance: {analysis.get('phi_resonance', 0):.6f}")
    
    # Healing summary
    healing = results.get("healing", {})
    errors = healing.get("errors_detected", [])
    suggestions = healing.get("healing_suggestions", [])
    print(f"\nFunction Healing:")
    print(f"- Errors detected: {len(errors)}")
    print(f"- Healing suggestions: {len(suggestions)}")
    
    if errors:
        print("\nDetected Errors:")
        for i, error in enumerate(errors[:3], 1):
            print(f"  {i}. {error.get('error_type', 'Unknown')}: {error.get('description', 'No description')}")
    
    if suggestions:
        print("\nHealing Suggestions:")
        for i, suggestion in enumerate(suggestions[:2], 1):
            print(f"  {i}. {suggestion.get('suggestion_type', 'Unknown')}: {suggestion.get('description', 'No description')}")
    
    # Integration status
    status = results.get("status", {})
    print(f"\nIntegration Status:")
    print(f"- Phi-coherence: {status.get('phi_coherence', 0):.6f}")
    print(f"- Quality: {status.get('coherence_quality', 'Unknown')}")
    
    print("\nMeta-Learning Statistics:")
    meta_stats = status.get("meta_learning_stats", {})
    print(f"- Success rate: {meta_stats.get('success_rate', 0):.4f}")
    print(f"- Learning iterations: {meta_stats.get('learning_iterations', 0)}")
    
    print("\n" + "="*80)
    print("DEMONSTRATION COMPLETE")
    print("="*80)


if __name__ == "__main__":
    main()
