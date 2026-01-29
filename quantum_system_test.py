#!/usr/bin/env python3
"""
Quantum System Integration Test
------------------------------

This script performs a comprehensive test of the entire QuantumAI system,
validating that all components work together properly with phi-harmonic coherence.
"""

import os
import sys
import json
import time
import uuid
import math
import logging
import datetime
import numpy as np
from typing import Dict, List, Any, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumSystemTest")

# Apply all modular extensions first to ensure proper integration
try:
    from quantum_integration_helper import apply_all_extensions
    logger.info("Applying all modular extensions...")
    applied_extensions = apply_all_extensions()
    logger.info(f"Successfully applied {len(applied_extensions)} extensions: {', '.join(applied_extensions)}")
except Exception as e:
    logger.error(f"Failed to apply modular extensions: {e}")
    logger.warning("Some system components may not function correctly")

# Import required modules
try:
    # Core components
    from quantum_agi_task_distributor import QuantumAGITaskDistributor, TARGET_COHERENCE, PHI
    from quantum_coherence_calculator import QuantumCoherenceCalculator
    
    # Distribution strategies
    from quantum_swarm_strategy import QuantumSwarmStrategy
    from quantum_tensor_capability_matcher import TensorCapabilityMatcher
    from quantum_adaptive_distribution_learner import AdaptiveDistributionLearner
    from quantum_coherence_preserving_balancer import CoherencePreservingBalancer
    
    # Orchestrator and healing components
    from quantum_orchestrator import QuantumOrchestrator
    from quantum_orchestrator_healing_extension import QuantumOrchestratorHealingExtension
    from quantum_orchestrator_resonance_extension import QuantumOrchestratorResonanceExtension
    from quantum_orchestrator_chord_extension import QuantumOrchestratorChordExtension
    
    # Self-reproduction components
    from quantum_genesis_storage import QuantumGenesisStorage
    from quantum_blockchain_genesis import QuantumBlockchainGenesis
    from quantum_blockchain_connector import QuantumBlockchainConnector
    
    # MoE/MoA components
    from quantum_moa_orchestrator_connector import QuantumMoAOrchestratorConnector
    from quantum_moa_agents import CoherenceAgent, EvolutionAgent
    
    # Visualization and demonstration
    from quantum_visualization_connector import QuantumVisualizationConnector
    from quantum_demonstration_runner_extension import QuantumDemonstrationRunnerExtension
    
    # Advanced quantum components
    from quantum_resonance_optimizer import QuantumResonanceOptimizer
    from quantum_harmonic_visualizer import QuantumHarmonicVisualizer
    from quantum_chord_progression import QuantumChordProgression
    
except ImportError as e:
    logger.error(f"Import error: {e}")
    logger.info("Some components may not be available. Continuing with available components.")

class QuantumSystemTest:
    """Test class for the entire QuantumAI system."""
    
    def __init__(self):
        """Initialize the test environment."""
        self.test_id = str(uuid.uuid4())
        self.results = {}
        self.components = {}
        self.test_files = {}
        
        # Create results directory
        self.results_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data",
            "system_test"
        )
        os.makedirs(self.results_dir, exist_ok=True)
        
        logger.info(f"Quantum System Test initialized with ID: {self.test_id}")
        
        # Initialize test files
        self._initialize_test_files()
    
    def _initialize_test_files(self):
        """Initialize test files for various components."""
        # Create a test file with intentional syntax error for healing tests
        self.test_files["healing"] = os.path.join(self.results_dir, "test_healing.py")
        with open(self.test_files["healing"], "w") as f:
            f.write("""
def test_function(x, y:
    \"\"\"Test function with missing parenthesis.\"\"\"
    return x + y * (x - y
""")
        
        # Create a test file with intentional logic error for logic healing tests
        self.test_files["logic"] = os.path.join(self.results_dir, "test_logic.py")
        with open(self.test_files["logic"], "w") as f:
            f.write("""
def increment(x):
    \"\"\"Increment a number by 1.\"\"\"
    return x - 1  # Logic error: should be x + 1
""")
        
        # Create a test file for quantum chord progression analysis
        self.test_files["chord"] = os.path.join(self.results_dir, "test_chord.py")
        with open(self.test_files["chord"], "w") as f:
            f.write("""
import math

def phi_harmonic_function(x):
    \"\"\"Calculate phi-harmonic value.\"\"\"
    phi = 1.618034
    return (phi * x) % 1

def calculate_resonance(values):
    \"\"\"Calculate resonance between values.\"\"\"
    phi = 1.618034
    resonance = sum((phi * v) % 1 for v in values) / len(values)
    return resonance

def quantum_chord(frequencies):
    \"\"\"Create a quantum chord from frequencies.\"\"\"
    return [f * 1.618034 for f in frequencies]
""")
        
        # Create a test file for meta-learning demonstration
        self.test_files["meta"] = os.path.join(self.results_dir, "test_meta.py")
        with open(self.test_files["meta"], "w") as f:
            f.write("""
import math

def learn_pattern(data):
    \"\"\"Learn a pattern from data.\"\"\"
    phi = 1.618034
    pattern = [d * phi for d in data]
    return pattern

def meta_learn(patterns):
    \"\"\"Meta-learn from multiple patterns.\"\"\"
    meta_pattern = []
    for p in patterns:
        meta_pattern.append(sum(p) / len(p))
    return meta_pattern
""")
    
    def test_task_distributor(self):
        """Test the quantum AGI task distributor with all strategies."""
        logger.info("Testing quantum AGI task distributor...")
        
        try:
            # Initialize distributor
            distributor = QuantumAGITaskDistributor()
            distributor.initialize()
            
            # Generate test nodes
            nodes = self._generate_test_nodes(15)
            
            # Generate test tasks
            tasks = self._generate_test_tasks(5)
            
            # Distribute tasks
            results = []
            
            for task in tasks:
                # Distribute task
                distribution_result = distributor.distribute_task(task, nodes)
                
                # Record result
                result = {
                    "task_id": task.get("task_id"),
                    "action": task.get("action"),
                    "coherence": distribution_result.get("coherence", 0),
                    "n_assigned_nodes": len(distribution_result.get("assigned_nodes", [])),
                    "optimized": distribution_result.get("optimized", False)
                }
                
                # Try to get strategy name if available
                if "strategy_name" in distribution_result:
                    result["strategy"] = distribution_result["strategy_name"]
                elif "meta_strategy" in distribution_result:
                    result["strategy"] = distribution_result["meta_strategy"]
                else:
                    result["strategy"] = "Unknown"
                
                results.append(result)
                
                logger.info(f"Task {task.get('action')} distributed with coherence: {result['coherence']:.6f}")
            
            self.results["task_distributor"] = {
                "success": True,
                "results": results,
                "avg_coherence": sum(r["coherence"] for r in results) / len(results) if results else 0
            }
            
            return True
        except Exception as e:
            logger.error(f"Task distributor test failed: {e}")
            self.results["task_distributor"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def test_orchestrator(self):
        """Test the quantum orchestrator with healing extensions."""
        logger.info("Testing quantum orchestrator...")
        
        try:
            # Initialize orchestrator
            orchestrator = QuantumOrchestrator(target_file=self.test_files["healing"])
            
            # Add healing extension
            healing_extension = QuantumOrchestratorHealingExtension(orchestrator)
            
            # Process file with syntax error
            result = orchestrator.process_file()
            
            # Check if healing was attempted
            healing_events = orchestrator.get_healing_events()
            
            self.results["orchestrator"] = {
                "success": True,
                "healing_attempted": len(healing_events) > 0,
                "n_healing_events": len(healing_events),
                "healing_events": healing_events
            }
            
            # Test logic healing
            orchestrator_logic = QuantumOrchestrator(target_file=self.test_files["logic"])
            result_logic = orchestrator_logic.process_file()
            healing_events_logic = orchestrator_logic.get_healing_events()
            
            self.results["orchestrator"]["logic_healing_attempted"] = len(healing_events_logic) > 0
            self.results["orchestrator"]["n_logic_healing_events"] = len(healing_events_logic)
            
            return True
        except Exception as e:
            logger.error(f"Orchestrator test failed: {e}")
            self.results["orchestrator"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def test_genesis_reproduction(self):
        """Test the quantum genesis reproduction system."""
        logger.info("Testing quantum genesis reproduction...")
        
        try:
            # Initialize genesis storage
            genesis_storage = QuantumGenesisStorage()
            
            # Create a test file to back up
            test_file = os.path.join(self.results_dir, "test_genesis.py")
            with open(test_file, "w") as f:
                f.write("""
def phi_function():
    \"\"\"Return the golden ratio.\"\"\"
    return 1.618034
""")
            
            # Back up the file
            backup_path = genesis_storage.backup_file(test_file)
            
            # Verify backup exists
            backup_exists = os.path.exists(backup_path)
            
            # Create a blockchain connector
            blockchain_connector = QuantumBlockchainConnector()
            
            # Test blockchain storage if available
            blockchain_storage_success = False
            try:
                blockchain_genesis = QuantumBlockchainGenesis()
                reference = blockchain_genesis.store_genesis_reference(test_file, "test_genesis")
                blockchain_storage_success = reference is not None
            except:
                blockchain_storage_success = False
            
            self.results["genesis"] = {
                "success": backup_exists,
                "backup_path": backup_path,
                "blockchain_storage_success": blockchain_storage_success
            }
            
            return backup_exists
        except Exception as e:
            logger.error(f"Genesis reproduction test failed: {e}")
            self.results["genesis"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def test_moa_integration(self):
        """Test the Mixture of Agents (MoA) integration."""
        logger.info("Testing MoA integration...")
        
        try:
            # Initialize MoA connector
            moa_connector = QuantumMoAOrchestratorConnector()
            
            # Create agents
            coherence_agent = CoherenceAgent()
            evolution_agent = EvolutionAgent()
            
            # Add agents to connector
            moa_connector.add_agent(coherence_agent)
            moa_connector.add_agent(evolution_agent)
            
            # Test agent initialization
            agents_initialized = len(moa_connector.agents) > 0
            
            # Test processing if possible
            processing_success = False
            try:
                moa_connector.process_file(self.test_files["chord"])
                processing_success = True
            except:
                processing_success = False
            
            self.results["moa"] = {
                "success": agents_initialized,
                "n_agents": len(moa_connector.agents),
                "processing_success": processing_success
            }
            
            return agents_initialized
        except Exception as e:
            logger.error(f"MoA integration test failed: {e}")
            self.results["moa"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def test_chord_progression(self):
        """Test the quantum chord progression analysis."""
        logger.info("Testing quantum chord progression...")
        
        try:
            # Initialize chord progression
            chord_progression = QuantumChordProgression()
            
            # Analyze test file
            analysis_success = False
            try:
                analysis = chord_progression.analyze_file(self.test_files["chord"])
                analysis_success = analysis is not None
            except:
                analysis_success = False
            
            # Generate chord report
            report_success = False
            try:
                report = chord_progression.generate_coherence_report()
                report_success = report is not None
            except:
                report_success = False
            
            self.results["chord"] = {
                "success": analysis_success or report_success,
                "analysis_success": analysis_success,
                "report_success": report_success
            }
            
            return analysis_success or report_success
        except Exception as e:
            logger.error(f"Chord progression test failed: {e}")
            self.results["chord"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def test_visualization(self):
        """Test the quantum visualization system."""
        logger.info("Testing quantum visualization...")
        
        try:
            # Initialize visualization connector
            visualization = QuantumVisualizationConnector()
            
            # Initialize demonstration runner
            demo_runner = QuantumDemonstrationRunnerExtension(visualization)
            
            # Test visualization generation
            visualization_success = False
            try:
                visualization.generate_visualization("test", {"data": [1, 1.618, 2.618, 4.236]})
                visualization_success = True
            except:
                visualization_success = False
            
            # Test demonstration running
            demo_success = False
            try:
                demo_runner.run_meta_learning_demo()
                demo_success = True
            except:
                demo_success = False
            
            self.results["visualization"] = {
                "success": visualization_success or demo_success,
                "visualization_success": visualization_success,
                "demo_success": demo_success
            }
            
            return visualization_success or demo_success
        except Exception as e:
            logger.error(f"Visualization test failed: {e}")
            self.results["visualization"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def test_resonance_optimization(self):
        """Test the quantum resonance optimization."""
        logger.info("Testing quantum resonance optimization...")
        
        try:
            # Initialize resonance optimizer
            optimizer = QuantumResonanceOptimizer()
            
            # Test optimization
            optimization_success = False
            try:
                optimization = optimizer.optimize_resonance([1, 1.618, 2.618, 4.236])
                optimization_success = optimization is not None
            except:
                optimization_success = False
            
            # Test harmonic visualization if available
            harmonic_success = False
            try:
                harmonic_visualizer = QuantumHarmonicVisualizer()
                harmonic_visualizer.visualize_harmonic_pattern([1, 1.618, 2.618, 4.236])
                harmonic_success = True
            except:
                harmonic_success = False
            
            self.results["resonance"] = {
                "success": optimization_success,
                "optimization_success": optimization_success,
                "harmonic_visualization_success": harmonic_success
            }
            
            return optimization_success
        except Exception as e:
            logger.error(f"Resonance optimization test failed: {e}")
            self.results["resonance"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def test_memory_behaviors(self):
        """Test the quantum memory behaviors."""
        logger.info("Testing quantum memory behaviors...")
        
        try:
            # Import memory behavior test
            from quantum_memory_behavior_test import QuantumMemoryBehaviorTest
            
            # Run memory behavior test
            memory_test = QuantumMemoryBehaviorTest()
            results = memory_test.run_all_tests()
            
            self.results["memory"] = {
                "success": True,
                "semantic_coherence": results.get("semantic", {}).get("avg_coherence", 0),
                "episodic_coherence": results.get("episodic", {}).get("temporal_coherence", 0),
                "procedural_coherence": results.get("procedural", {}).get("avg_coherence", 0),
                "integrated_coherence": results.get("integrated_coherence", {}).get("value", 0),
                "phi_ratio": results.get("integrated_coherence", {}).get("phi_ratio", 0)
            }
            
            return True
        except Exception as e:
            logger.error(f"Memory behaviors test failed: {e}")
            self.results["memory"] = {
                "success": False,
                "error": str(e)
            }
            return False
    
    def run_all_tests(self):
        """Run all system tests."""
        logger.info("Running all system tests...")
        
        # Run all tests
        tests = [
            ("task_distributor", self.test_task_distributor),
            ("orchestrator", self.test_orchestrator),
            ("genesis", self.test_genesis_reproduction),
            ("moa", self.test_moa_integration),
            ("chord", self.test_chord_progression),
            ("visualization", self.test_visualization),
            ("resonance", self.test_resonance_optimization),
            ("memory", self.test_memory_behaviors)
        ]
        
        results = {}
        for name, test_func in tests:
            logger.info(f"Running test: {name}")
            try:
                success = test_func()
                results[name] = {"success": success}
            except Exception as e:
                logger.error(f"Test {name} failed with error: {e}")
                results[name] = {"success": False, "error": str(e)}
        
        # Calculate overall success rate
        success_count = sum(1 for r in results.values() if r.get("success", False))
        total_count = len(results)
        success_rate = success_count / total_count if total_count > 0 else 0
        
        # Save results to file
        self._save_results(results, success_rate)
        
        return {
            "results": results,
            "success_count": success_count,
            "total_count": total_count,
            "success_rate": success_rate
        }
    
    def _save_results(self, results, success_rate):
        """Save test results to file."""
        timestamp = datetime.datetime.now().isoformat()
        
        result_data = {
            "test_id": self.test_id,
            "timestamp": timestamp,
            "results": results,
            "success_rate": success_rate,
            "phi_harmonic_index": (success_rate * PHI) % 1
        }
        
        result_file = os.path.join(self.results_dir, f"system_test_{self.test_id}.json")
        with open(result_file, "w") as f:
            json.dump(result_data, f, indent=2)
        
        logger.info(f"Test results saved to {result_file}")
    
    def _generate_test_nodes(self, n_nodes: int) -> List[Dict[str, Any]]:
        """Generate test nodes with phi-harmonic capabilities."""
        nodes = []
        
        for i in range(n_nodes):
            # Generate phi-harmonic capability values
            processing_power = 0.5 + 0.5 * math.sin(i * PHI)
            memory = 0.5 + 0.5 * math.cos(i * PHI)
            coherence = TARGET_COHERENCE * (0.8 + 0.4 * math.sin(i * PHI / 2))
            quantum_capability = 0.5 + 0.5 * math.sin(i * PHI / 3)
            
            # Create node
            node = {
                "node_id": str(uuid.uuid4()),
                "reference_id": f"node_{i}",
                "capabilities": {
                    "processing_power": processing_power,
                    "memory": memory,
                    "coherence": coherence,
                    "quantum_capability": quantum_capability
                }
            }
            
            nodes.append(node)
        
        return nodes
    
    def _generate_test_tasks(self, n_tasks: int) -> List[Dict[str, Any]]:
        """Generate test tasks with phi-harmonic requirements."""
        tasks = []
        
        actions = [
            "process_quantum_data",
            "analyze_coherence_patterns",
            "optimize_phi_resonance",
            "distribute_quantum_computation",
            "heal_quantum_state"
        ]
        
        for i in range(n_tasks):
            # Generate phi-harmonic requirement values
            processing_req = 0.3 + 0.7 * math.sin(i * PHI)
            memory_req = 0.3 + 0.7 * math.cos(i * PHI)
            coherence_req = TARGET_COHERENCE * (0.7 + 0.3 * math.sin(i * PHI / 2))
            quantum_req = 0.3 + 0.7 * math.sin(i * PHI / 3)
            
            # Create task
            task = {
                "task_id": str(uuid.uuid4()),
                "action": actions[i % len(actions)],
                "requirements": {
                    "processing_power": processing_req,
                    "memory": memory_req,
                    "coherence": coherence_req,
                    "quantum_capability": quantum_req
                },
                "priority": 0.5 + 0.5 * math.sin(i * PHI / 4),
                "timestamp": datetime.datetime.now().isoformat()
            }
            
            tasks.append(task)
        
        return tasks

if __name__ == "__main__":
    # Run system test
    test = QuantumSystemTest()
    results = test.run_all_tests()
    
    # Print summary
    logger.info("\n================================================================================")
    logger.info("QUANTUM SYSTEM TEST SUMMARY")
    logger.info("================================================================================\n")
    
    for name, result in results["results"].items():
        status = "SUCCESS" if result.get("success", False) else "FAILURE"
        logger.info(f"{name.upper()}: {status}")
        
        if not result.get("success", False) and "error" in result:
            logger.info(f"  Error: {result['error']}")
    
    logger.info("\n================================================================================")
    logger.info(f"OVERALL SUCCESS RATE: {results['success_rate'] * 100:.2f}%")
    logger.info(f"TESTS PASSED: {results['success_count']}/{results['total_count']}")
    logger.info("================================================================================")
    
    # Check if success rate is acceptable
    if results["success_rate"] >= 0.8:
        logger.info("SUCCESS: System integration test passed with acceptable success rate!")
    else:
        logger.info("WARNING: System integration test failed to meet acceptable success rate.")
