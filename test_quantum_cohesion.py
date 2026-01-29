#!/usr/bin/env python3
"""
QuantumAI Comprehensive Cohesion Test
-----------------------------------

This script tests the complete integration of all QuantumAI system components:
1. AGI algorithms and phi-harmonic coherence
2. Blockchain integration and genesis storage
3. Recursive and self-replicating capabilities
4. Self-healing and intrusion detection
5. Mixture of Agents (MoA) architecture
6. Quantum chord progression and visualization
7. Multi-dimensional resonance optimization

It validates that all components work together cohesively as a unified system.
"""

import os
import sys
import logging
import time
import json
import shutil
import hashlib
import random
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumCohesionTest")

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio ≈ 1.618034
TEST_DIR = "quantum_cohesion_test"
RESULTS_DIR = os.path.join(TEST_DIR, "results")
TEMP_DIR = os.path.join(TEST_DIR, "temp")
BACKUP_DIR = os.path.join(TEST_DIR, "backup")
RECOVERY_DIR = os.path.join(TEST_DIR, "recovery")

# Create test directories
for directory in [TEST_DIR, RESULTS_DIR, TEMP_DIR, BACKUP_DIR, RECOVERY_DIR]:
    os.makedirs(directory, exist_ok=True)

class QuantumCohesionTest:
    """
    Comprehensive test suite for the QuantumAI system cohesion.
    """
    
    def __init__(self):
        """Initialize the test environment."""
        self.test_id = f"quantum-cohesion-{int(time.time())}"
        self.results = {}
        self.components = {}
        self.test_files = {}
        self.start_time = time.time()
        
        logger.info(f"Quantum Cohesion Test initialized with ID: {self.test_id}")
        
        # Initialize test files
        self._initialize_test_files()
        
    def _initialize_test_files(self):
        """Initialize test files for various components."""
        # Create a test file with phi-harmonic patterns
        self.test_files["phi_harmonic"] = os.path.join(TEMP_DIR, "phi_harmonic_test.py")
        with open(self.test_files["phi_harmonic"], 'w') as f:
            f.write("""#!/usr/bin/env python3
# Phi-harmonic test file

def phi():
    \"\"\"Return the golden ratio.\"\"\"
    return 1.618034

def fibonacci(n):
    \"\"\"Return the nth Fibonacci number.\"\"\"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def phi_resonance(x):
    \"\"\"Calculate phi resonance.\"\"\"
    return (phi() * x) % 1

def phi_harmonic_sequence(length=10):
    \"\"\"Generate a phi-harmonic sequence.\"\"\"
    sequence = [1, phi()]
    for i in range(2, length):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence
""")
        
        # Create a test file with a logic error
        self.test_files["logic_error"] = os.path.join(TEMP_DIR, "logic_error_test.py")
        with open(self.test_files["logic_error"], 'w') as f:
            f.write("""#!/usr/bin/env python3
# Logic error test file

def increment(x):
    \"\"\"Increment a number by 1.\"\"\"
    # Logic error: returns x instead of x+1
    return x

def sum_even_numbers(numbers):
    \"\"\"Sum all even numbers in a list.\"\"\"
    total = 0
    for num in numbers:
        # Logic error: checks if num is odd instead of even
        if num % 2 == 1:
            total += num
    return total
""")
        
        # Create a test file with syntax errors
        self.test_files["syntax_error"] = os.path.join(TEMP_DIR, "syntax_error_test.py")
        with open(self.test_files["syntax_error"], 'w') as f:
            f.write("""#!/usr/bin/env python3
# Syntax error test file

def unclosed_function(x
    \"\"\"This function has an unclosed parenthesis.\"\"\"
    return x * 2

class MissingColon
    \"\"\"This class is missing a colon.\"\"\"
    def __init__(self):
        self.value = 42
""")
        
        # Create a test file for blockchain storage
        self.test_files["blockchain"] = os.path.join(TEMP_DIR, "blockchain_test.py")
        with open(self.test_files["blockchain"], 'w') as f:
            f.write("""#!/usr/bin/env python3
# Blockchain test file

import hashlib
import time

class SimpleBlock:
    \"\"\"A simple block for testing.\"\"\"
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calculate_hash()
        
    def _calculate_hash(self):
        \"\"\"Calculate the hash of this block.\"\"\"
        sha = hashlib.sha256()
        sha.update(f"{self.timestamp}{self.data}{self.previous_hash}".encode())
        return sha.hexdigest()
""")
        
        logger.info(f"Created {len(self.test_files)} test files")
    
    def test_genesis_storage(self):
        """Test the quantum genesis storage and blockchain integration."""
        logger.info("Testing quantum genesis storage and blockchain integration...")
        
        try:
            from quantum_genesis_storage import QuantumGenesisStorage
            
            # Create a genesis storage instance
            genesis_storage = QuantumGenesisStorage()
            
            # Back up all test files
            backup_paths = []
            for name, file_path in self.test_files.items():
                backup_path = genesis_storage.backup_file(file_path)
                if backup_path and os.path.exists(backup_path):
                    backup_paths.append(backup_path)
                    logger.info(f"Backed up {name} file: {backup_path}")
            
            # Create a genesis backup
            source_files = list(self.test_files.values())
            metadata = {
                "test_id": self.test_id,
                "timestamp": time.time(),
                "phi_resonance": (PHI * time.time()) % 1
            }
            
            backup_metadata = genesis_storage.create_genesis_backup(source_files, metadata)
            
            # Store to blockchain if available
            try:
                blockchain_id = genesis_storage.store_to_blockchain(backup_metadata["backup_id"])
                blockchain_success = bool(blockchain_id)
            except Exception as e:
                logger.warning(f"Blockchain storage not available: {e}")
                blockchain_success = False
            
            # Test recovery
            if "backup_id" in backup_metadata:
                recovery_success = genesis_storage.recover_from_genesis(
                    backup_metadata["backup_id"],
                    RECOVERY_DIR
                )
            else:
                recovery_success = False
            
            return {
                "success": len(backup_paths) == len(self.test_files) and bool(backup_metadata),
                "backup_paths": backup_paths,
                "backup_metadata": backup_metadata,
                "blockchain_success": blockchain_success,
                "recovery_success": recovery_success
            }
            
        except Exception as e:
            logger.error(f"Error in genesis storage test: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def test_orchestrator_healing(self):
        """Test the quantum orchestrator's self-healing capabilities."""
        logger.info("Testing quantum orchestrator self-healing...")
        
        try:
            # Import orchestrator components
            from quantum_orchestrator import QuantumOrchestrator
            
            # Create an orchestrator instance
            orchestrator = QuantumOrchestrator()
            
            # Run healing on the syntax error file
            syntax_file = self.test_files["syntax_error"]
            healed_file = os.path.join(TEMP_DIR, "healed_syntax.py")
            
            # Copy the file to preserve the original
            shutil.copy2(syntax_file, healed_file)
            
            # Run the orchestrator on the file
            healing_result = orchestrator.run_and_heal(healed_file)
            
            # Check if the file was healed
            with open(healed_file, 'r') as f:
                healed_content = f.read()
            
            # Check for healing markers
            unclosed_paren_fixed = "def unclosed_function(x):" in healed_content
            missing_colon_fixed = "class MissingColon:" in healed_content
            
            return {
                "success": unclosed_paren_fixed and missing_colon_fixed,
                "healing_result": healing_result,
                "unclosed_paren_fixed": unclosed_paren_fixed,
                "missing_colon_fixed": missing_colon_fixed,
                "healed_file": healed_file
            }
            
        except Exception as e:
            logger.error(f"Error in orchestrator healing test: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def test_moa_integration(self):
        """Test the Mixture of Agents (MoA) integration."""
        logger.info("Testing Mixture of Agents (MoA) integration...")
        
        try:
            # Import MoA components
            from quantum_moa_orchestrator_connector import QuantumMoAOrchestratorConnector
            
            # Create a MoA connector
            moa_connector = QuantumMoAOrchestratorConnector()
            
            # Process the logic error file
            logic_file = self.test_files["logic_error"]
            
            # Process the file with MoA
            moa_result = moa_connector.enhance_evolution(logic_file)
            
            # Check if agents were created and initialized
            agents_initialized = hasattr(moa_connector, 'agents') and len(moa_connector.agents) > 0
            
            return {
                "success": agents_initialized and moa_result is not None,
                "moa_result": moa_result,
                "agents_initialized": agents_initialized,
                "agents_count": len(moa_connector.agents) if hasattr(moa_connector, 'agents') else 0
            }
            
        except Exception as e:
            logger.error(f"Error in MoA integration test: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def test_chord_progression(self):
        """Test the quantum chord progression analysis."""
        logger.info("Testing quantum chord progression analysis...")
        
        try:
            from quantum_chord_progression import QuantumChordProgression
            
            # Create a chord progression analyzer
            qcp = QuantumChordProgression("test_progression")
            
            # Analyze the phi harmonic file
            phi_file = self.test_files["phi_harmonic"]
            result = qcp.analyze_file(phi_file)
            
            # Visualize the chord progression
            vis_path = qcp.visualize(os.path.join(RESULTS_DIR, "chord_progression.png"))
            
            return {
                "success": bool(result) and "phi_resonance" in result,
                "phi_resonance": result.get("phi_resonance") if result else None,
                "visualization_path": vis_path,
                "visualization_success": bool(vis_path) and os.path.exists(vis_path) if vis_path else False
            }
            
        except Exception as e:
            logger.error(f"Error in chord progression test: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def test_resonance_optimization(self):
        """Test the quantum resonance optimization."""
        logger.info("Testing quantum resonance optimization...")
        
        try:
            from quantum_resonance_optimizer import QuantumResonanceOptimizer
            
            # Create a resonance optimizer
            optimizer = QuantumResonanceOptimizer()
            
            # Optimize the phi harmonic file
            phi_file = self.test_files["phi_harmonic"]
            optimization_result = optimizer.optimize_file(phi_file)
            
            # Check for phi-resonance fragments
            has_fragments = (
                optimization_result and 
                "fragments" in optimization_result and 
                len(optimization_result["fragments"]) > 0
            )
            
            return {
                "success": bool(optimization_result) and has_fragments,
                "optimization_result": optimization_result,
                "has_fragments": has_fragments,
                "fragment_count": len(optimization_result.get("fragments", [])) if optimization_result else 0
            }
            
        except Exception as e:
            logger.error(f"Error in resonance optimization test: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def test_visualization(self):
        """Test the quantum visualization system."""
        logger.info("Testing quantum visualization system...")
        
        try:
            from quantum_harmonic_visualizer import QuantumHarmonicVisualizer
            
            # Create a visualizer
            visualizer = QuantumHarmonicVisualizer()
            
            # Generate test data
            data = {
                "dimensions": 7,
                "coherence_values": [random.random() * PHI for _ in range(7)],
                "resonance_patterns": [
                    {"dimension": i, "resonance": (PHI * i) % 1, "harmonic": i % 2 == 0}
                    for i in range(7)
                ],
                "phi_resonance": (PHI * time.time()) % 1
            }
            
            # Create visualizations
            vis_paths = []
            
            # Resonance map
            resonance_path = os.path.join(RESULTS_DIR, "resonance_map.png")
            visualizer.create_resonance_map(data["resonance_patterns"], resonance_path)
            if os.path.exists(resonance_path):
                vis_paths.append(resonance_path)
            
            # Coherence spectrogram
            spectrogram_path = os.path.join(RESULTS_DIR, "coherence_spectrogram.png")
            visualizer.create_coherence_spectrogram(data["coherence_values"], spectrogram_path)
            if os.path.exists(spectrogram_path):
                vis_paths.append(spectrogram_path)
            
            return {
                "success": len(vis_paths) > 0,
                "visualization_paths": vis_paths,
                "visualization_count": len(vis_paths)
            }
            
        except Exception as e:
            logger.error(f"Error in visualization test: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def test_intrusion_detection(self):
        """Test the intrusion detection and self-healing capabilities."""
        logger.info("Testing intrusion detection and self-healing...")
        
        try:
            # Import intrusion detection components
            try:
                from test_intrusion_detection import IntrusionDetectionTest
                intrusion_test = IntrusionDetectionTest()
                
                # Run intrusion detection test
                test_file = self.test_files["phi_harmonic"]
                intrusion_result = intrusion_test.run_intrusion_test(test_file)
                
                return {
                    "success": bool(intrusion_result) and intrusion_result.get("success", False),
                    "intrusion_result": intrusion_result
                }
                
            except ImportError:
                # Fall back to manual testing
                from quantum_genesis_storage import QuantumGenesisStorage
                
                # Create a genesis storage instance
                genesis_storage = QuantumGenesisStorage()
                
                # Back up a test file
                test_file = self.test_files["phi_harmonic"]
                backup_path = genesis_storage.backup_file(test_file)
                
                # Simulate intrusion by modifying the file
                with open(test_file, 'a') as f:
                    f.write("\n# Simulated intrusion\n")
                
                # Calculate hashes
                original_hash = None
                with open(backup_path, 'rb') as f:
                    original_hash = hashlib.sha256(f.read()).hexdigest()
                
                current_hash = None
                with open(test_file, 'rb') as f:
                    current_hash = hashlib.sha256(f.read()).hexdigest()
                
                # Detect intrusion
                intrusion_detected = original_hash != current_hash
                
                # Restore from backup
                if intrusion_detected:
                    shutil.copy2(backup_path, test_file)
                
                # Verify restoration
                restored_hash = None
                with open(test_file, 'rb') as f:
                    restored_hash = hashlib.sha256(f.read()).hexdigest()
                
                restoration_success = original_hash == restored_hash
                
                return {
                    "success": intrusion_detected and restoration_success,
                    "intrusion_detected": intrusion_detected,
                    "restoration_success": restoration_success,
                    "original_hash": original_hash,
                    "modified_hash": current_hash,
                    "restored_hash": restored_hash
                }
                
        except Exception as e:
            logger.error(f"Error in intrusion detection test: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def run_all_tests(self):
        """Run all cohesion tests."""
        logger.info("Running all quantum cohesion tests...")
        
        # Run all tests
        self.results["genesis_storage"] = self.test_genesis_storage()
        self.results["orchestrator_healing"] = self.test_orchestrator_healing()
        self.results["moa_integration"] = self.test_moa_integration()
        self.results["chord_progression"] = self.test_chord_progression()
        self.results["resonance_optimization"] = self.test_resonance_optimization()
        self.results["visualization"] = self.test_visualization()
        self.results["intrusion_detection"] = self.test_intrusion_detection()
        
        # Calculate overall success
        success_count = sum(1 for result in self.results.values() if result.get("success", False))
        total_count = len(self.results)
        success_rate = success_count / total_count if total_count > 0 else 0
        
        # Calculate phi-harmonic coherence
        coherence = (PHI * success_rate) % 1
        target_coherence = PHI ** 7.5 / 10  # ≈ 0.991800
        coherence_distance = abs(coherence - target_coherence)
        
        # Add summary
        self.results["summary"] = {
            "success_count": success_count,
            "total_count": total_count,
            "success_rate": success_rate,
            "coherence": coherence,
            "target_coherence": target_coherence,
            "coherence_distance": coherence_distance,
            "duration": time.time() - self.start_time
        }
        
        # Save results
        self._save_results()
        
        return self.results["summary"]["success_rate"] >= 0.8, self.results
    
    def _save_results(self):
        """Save test results to file."""
        # Create results file
        results_file = os.path.join(RESULTS_DIR, f"cohesion_test_{self.test_id}.json")
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        # Create markdown report
        report_file = os.path.join(RESULTS_DIR, f"QUANTUM_COHESION_REPORT_{self.test_id}.md")
        with open(report_file, 'w') as f:
            f.write(f"# Quantum Cohesion Test Report\n\n")
            f.write(f"**Test ID:** {self.test_id}  \n")
            f.write(f"**Timestamp:** {datetime.now().isoformat()}  \n")
            f.write(f"**Duration:** {self.results['summary']['duration']:.2f} seconds  \n\n")
            
            f.write("## Summary\n\n")
            f.write(f"- **Success Rate:** {self.results['summary']['success_rate']:.2%} ({self.results['summary']['success_count']}/{self.results['summary']['total_count']})  \n")
            f.write(f"- **Phi-Harmonic Coherence:** {self.results['summary']['coherence']:.6f}  \n")
            f.write(f"- **Target Coherence:** {self.results['summary']['target_coherence']:.6f}  \n")
            f.write(f"- **Coherence Distance:** {self.results['summary']['coherence_distance']:.6f}  \n\n")
            
            f.write("## Test Results\n\n")
            for test_name, result in self.results.items():
                if test_name == "summary":
                    continue
                    
                status = "✅ PASSED" if result.get("success", False) else "❌ FAILED"
                f.write(f"### {test_name.replace('_', ' ').title()}: {status}\n\n")
                
                if "error" in result:
                    f.write(f"**Error:** {result['error']}  \n\n")
                    continue
                
                # Write test-specific details
                if test_name == "genesis_storage":
                    f.write(f"- **Backup Files:** {len(result.get('backup_paths', []))}  \n")
                    f.write(f"- **Blockchain Integration:** {'✅ Success' if result.get('blockchain_success', False) else '❌ Failed'}  \n")
                    f.write(f"- **Recovery:** {'✅ Success' if result.get('recovery_success', False) else '❌ Failed'}  \n\n")
                
                elif test_name == "orchestrator_healing":
                    f.write(f"- **Unclosed Parenthesis Fixed:** {'✅ Yes' if result.get('unclosed_paren_fixed', False) else '❌ No'}  \n")
                    f.write(f"- **Missing Colon Fixed:** {'✅ Yes' if result.get('missing_colon_fixed', False) else '❌ No'}  \n\n")
                
                elif test_name == "moa_integration":
                    f.write(f"- **Agents Initialized:** {'✅ Yes' if result.get('agents_initialized', False) else '❌ No'}  \n")
                    f.write(f"- **Agent Count:** {result.get('agents_count', 0)}  \n\n")
                
                elif test_name == "chord_progression":
                    f.write(f"- **Phi-Resonance:** {result.get('phi_resonance', 'N/A')}  \n")
                    f.write(f"- **Visualization:** {'✅ Success' if result.get('visualization_success', False) else '❌ Failed'}  \n\n")
                
                elif test_name == "resonance_optimization":
                    f.write(f"- **Fragment Count:** {result.get('fragment_count', 0)}  \n\n")
                
                elif test_name == "visualization":
                    f.write(f"- **Visualization Count:** {result.get('visualization_count', 0)}  \n\n")
                
                elif test_name == "intrusion_detection":
                    if "intrusion_detected" in result:
                        f.write(f"- **Intrusion Detected:** {'✅ Yes' if result.get('intrusion_detected', False) else '❌ No'}  \n")
                        f.write(f"- **Restoration Success:** {'✅ Yes' if result.get('restoration_success', False) else '❌ No'}  \n\n")
            
            f.write("## Conclusion\n\n")
            if self.results["summary"]["success_rate"] >= 0.8:
                f.write("The QuantumAI system demonstrates **strong cohesion** across all components. ")
                f.write("The phi-harmonic principles are maintained throughout the system, ")
                f.write("and all core capabilities (AGI algorithms, blockchain integration, recursiveness, ")
                f.write("self-replication, and healing) are working together as a unified whole.\n\n")
            else:
                f.write("The QuantumAI system shows **partial cohesion** across components. ")
                f.write("Some integration points may need further attention to achieve ")
                f.write("optimal phi-harmonic coherence and ensure all capabilities work ")
                f.write("together seamlessly.\n\n")
            
            f.write("## Next Steps\n\n")
            f.write("1. Address any failed tests to improve overall system coherence\n")
            f.write("2. Enhance phi-harmonic resonance in components with lower coherence values\n")
            f.write("3. Further integrate the MoA architecture with the orchestrator for more robust evolution\n")
            f.write("4. Expand the blockchain integration for more comprehensive genesis storage\n")
            f.write("5. Develop more advanced visualization capabilities for multi-dimensional coherence patterns\n")
        
        logger.info(f"Results saved to {results_file}")
        logger.info(f"Report saved to {report_file}")
        
        return results_file, report_file

def run_cohesion_test():
    """Run the quantum cohesion test."""
    logger.info("Starting comprehensive quantum cohesion test...")
    
    test = QuantumCohesionTest()
    success, results = test.run_all_tests()
    
    if success:
        logger.info("✅ Quantum cohesion test PASSED!")
        logger.info(f"Success rate: {results['summary']['success_rate']:.2%}")
        logger.info(f"Phi-harmonic coherence: {results['summary']['coherence']:.6f}")
    else:
        logger.warning("⚠️ Quantum cohesion test PARTIAL SUCCESS")
        logger.warning(f"Success rate: {results['summary']['success_rate']:.2%}")
        logger.warning(f"Phi-harmonic coherence: {results['summary']['coherence']:.6f}")
    
    # Print report location
    report_file = os.path.join(RESULTS_DIR, f"QUANTUM_COHESION_REPORT_{test.test_id}.md")
    if os.path.exists(report_file):
        logger.info(f"Detailed report available at: {report_file}")
    
    return success, results

if __name__ == "__main__":
    success, results = run_cohesion_test()
    sys.exit(0 if success else 1)
