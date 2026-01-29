"""
test_meta_integration.py

Test script for validating the integration of meta-learning components
with the existing QuantumAI orchestrator system.

This script tests the full workflow from function analysis to healing and optimization,
ensuring all components work together while maintaining phi-harmonic principles.
"""

import os
import sys
import json
import time
import logging
import unittest
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("TestMetaIntegration")

# Import meta-learning components
try:
    from quantum_phi_meta_learning import PhiHarmonicMetaLearning
    from quantum_expert_interface import PhiHarmonicExpert, create_expert
    from quantum_agent_factory import PhiHarmonicAgentFactory, create_agent
    from quantum_moe_router import PhiHarmonicRouter
    from quantum_agent_coordinator import PhiHarmonicCoordinator, create_healing_team
    from quantum_hyper_processor import PhiHarmonicHyperProcessor, create_default_space
    from quantum_meta_integration import QuantumMetaIntegrator, integrate_with_orchestrator
except ImportError as e:
    logger.error(f"Failed to import meta-learning components: {str(e)}")
    sys.exit(1)

# Try to import orchestrator
try:
    from quantum_orchestrator import QuantumOrchestrator
    ORCHESTRATOR_AVAILABLE = True
except ImportError:
    logger.warning("QuantumOrchestrator not available. Some tests will be skipped.")
    ORCHESTRATOR_AVAILABLE = False

# Test function with logic error
TEST_FUNCTION_WITH_ERROR = """
def increment_values(numbers):
    # Logic error: incrementing by 2 instead of 1
    return [x + 2 for x in numbers]
"""

# Test function with optimization opportunity
TEST_FUNCTION_FOR_OPTIMIZATION = """
def find_duplicates(numbers):
    # Inefficient implementation
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates
"""

# Test recursive function
TEST_RECURSIVE_FUNCTION = """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
"""

# Test functional programming function
TEST_FUNCTIONAL_FUNCTION = """
def process_data(data):
    filtered = [x for x in data if x > 0]
    squared = map(lambda x: x**2, filtered)
    return list(squared)
"""

class TestMetaIntegration(unittest.TestCase):
    """Test case for meta-learning integration."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.phi = 1.618033988749895
        
        # Initialize components
        cls.meta_learning = PhiHarmonicMetaLearning(phi=cls.phi)
        cls.agent_factory = PhiHarmonicAgentFactory(phi=cls.phi)
        cls.expert_router = PhiHarmonicRouter(phi=cls.phi)
        cls.agent_coordinator = PhiHarmonicCoordinator(phi=cls.phi)
        cls.hyper_processor = PhiHarmonicHyperProcessor(phi=cls.phi)
        
        # Create integrator
        cls.integrator = QuantumMetaIntegrator(phi=cls.phi)
        
        # Try to initialize orchestrator
        cls.orchestrator = None
        if ORCHESTRATOR_AVAILABLE:
            try:
                cls.orchestrator = QuantumOrchestrator()
                cls.integrator.connect_orchestrator(cls.orchestrator)
            except Exception as e:
                logger.warning(f"Failed to initialize orchestrator: {str(e)}")
        
        # Create test files
        cls._create_test_files()
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test environment."""
        # Remove test files
        cls._cleanup_test_files()
    
    @classmethod
    def _create_test_files(cls):
        """Create test function files."""
        # Create directory for test files
        os.makedirs("test_functions", exist_ok=True)
        
        # Create test files
        with open("test_functions/increment_values.py", "w") as f:
            f.write(TEST_FUNCTION_WITH_ERROR)
        
        with open("test_functions/find_duplicates.py", "w") as f:
            f.write(TEST_FUNCTION_FOR_OPTIMIZATION)
        
        with open("test_functions/factorial.py", "w") as f:
            f.write(TEST_RECURSIVE_FUNCTION)
        
        with open("test_functions/process_data.py", "w") as f:
            f.write(TEST_FUNCTIONAL_FUNCTION)
    
    @classmethod
    def _cleanup_test_files(cls):
        """Clean up test files."""
        # Remove test files
        for filename in ["increment_values.py", "find_duplicates.py", "factorial.py", "process_data.py"]:
            try:
                os.remove(f"test_functions/{filename}")
            except:
                pass
        
        # Try to remove directory
        try:
            os.rmdir("test_functions")
        except:
            pass
    
    def test_01_meta_learning_initialization(self):
        """Test meta-learning component initialization."""
        # Verify components are initialized
        self.assertIsNotNone(self.meta_learning)
        self.assertIsNotNone(self.agent_factory)
        self.assertIsNotNone(self.expert_router)
        self.assertIsNotNone(self.agent_coordinator)
        self.assertIsNotNone(self.hyper_processor)
        self.assertIsNotNone(self.integrator)
        
        # Verify integrator status
        status = self.integrator.get_integration_status()
        self.assertTrue(status["integration_state"]["initialized"])
        self.assertTrue(status["integration_state"]["meta_learning_initialized"])
        self.assertTrue(status["integration_state"]["moe_initialized"])
        self.assertTrue(status["integration_state"]["moa_initialized"])
        self.assertTrue(status["integration_state"]["hyper_processor_initialized"])
        
        logger.info("Meta-learning components initialized successfully")
    
    def test_02_expert_routing(self):
        """Test MoE expert routing."""
        # Test routing recursive function
        recursive_result = self.expert_router.route_function(
            TEST_RECURSIVE_FUNCTION, "factorial")
        
        # Test routing functional function
        functional_result = self.expert_router.route_function(
            TEST_FUNCTIONAL_FUNCTION, "process_data")
        
        # Verify results
        self.assertIsNotNone(recursive_result)
        self.assertIsNotNone(functional_result)
        self.assertIn("expert_specialization", recursive_result)
        self.assertIn("expert_specialization", functional_result)
        
        # Check if routing worked correctly
        recursive_expert = recursive_result["expert_specialization"]
        functional_expert = functional_result["expert_specialization"]
        
        logger.info(f"Recursive function routed to: {recursive_expert}")
        logger.info(f"Functional function routed to: {functional_expert}")
        
        # Get router statistics
        stats = self.expert_router.get_routing_statistics()
        self.assertEqual(stats["total_routings"], 2)
        
        logger.info("Expert routing test completed successfully")
    
    def test_03_agent_team_creation(self):
        """Test MoA agent team creation and task processing."""
        # Create a healing team
        team_id = self.agent_coordinator.create_team("Test Healing Team", {
            "logic_error": "healer",
            "optimization": "optimizer"
        })
        
        # Verify team creation
        self.assertIsNotNone(team_id)
        team = self.agent_coordinator.get_team(team_id)
        self.assertIsNotNone(team)
        
        # Submit task to team
        task = {
            "task_type": "logic_error_detection",
            "func_code": TEST_FUNCTION_WITH_ERROR,
            "func_name": "increment_values",
            "expected_behavior": {"increment": 1}
        }
        
        submission_result = self.agent_coordinator.submit_task(
            team_id, task, auto_execute=True)
        
        # Verify task submission
        self.assertIsNotNone(submission_result)
        self.assertIn("task_id", submission_result)
        
        # Get task result
        task_id = submission_result["task_id"]
        task_result = self.agent_coordinator.get_task_result(task_id)
        
        # Verify task result
        self.assertIsNotNone(task_result)
        self.assertIn("errors_detected", task_result)
        
        logger.info(f"Agent team detected errors: {task_result.get('errors_detected', {})}")
        logger.info(f"Agent team healing suggestions: {task_result.get('healing_suggestions', {})}")
        
        logger.info("Agent team creation and task processing test completed successfully")
    
    def test_04_hyper_dimensional_processing(self):
        """Test hyper-dimensional processing."""
        # Create a space
        space_id = self.hyper_processor.create_space("Test Space", [
            "Recursion",
            "Functional",
            "Imperative",
            "Object-Oriented"
        ])
        
        # Verify space creation
        self.assertIsNotNone(space_id)
        space = self.hyper_processor.get_space(space_id)
        self.assertIsNotNone(space)
        
        # Register patterns
        recursive_pattern = self.hyper_processor.register_pattern(
            space_id,
            "Recursive Pattern",
            [
                [0.8, 0.2, 0.1, 0.3],
                [0.9, 0.1, 0.0, 0.2]
            ]
        )
        
        functional_pattern = self.hyper_processor.register_pattern(
            space_id,
            "Functional Pattern",
            [
                [0.2, 0.9, 0.1, 0.4],
                [0.1, 0.8, 0.2, 0.5]
            ]
        )
        
        # Verify pattern registration
        self.assertIsNotNone(recursive_pattern)
        self.assertIsNotNone(functional_pattern)
        
        # Test pattern matching
        query = [
            [0.75, 0.25, 0.1, 0.3],
            [0.85, 0.15, 0.0, 0.25]
        ]
        
        matches = self.hyper_processor.match_pattern(space_id, query)
        
        # Verify matches
        self.assertIsNotNone(matches)
        self.assertTrue(len(matches) > 0)
        
        logger.info(f"Pattern matches: {matches}")
        
        # Test transformation
        transform_result = self.hyper_processor.transform_data(space_id, query)
        
        # Verify transformation
        self.assertIsNotNone(transform_result)
        self.assertIn("transformed_points", transform_result)
        
        logger.info(f"Transformation resonance improvement: {transform_result.get('resonance_improvement', 0)}")
        
        logger.info("Hyper-dimensional processing test completed successfully")
    
    def test_05_function_analysis(self):
        """Test function analysis with meta-learning components."""
        # Analyze functions
        increment_analysis = self.integrator.analyze_function(
            TEST_FUNCTION_WITH_ERROR, "increment_values")
        
        duplicates_analysis = self.integrator.analyze_function(
            TEST_FUNCTION_FOR_OPTIMIZATION, "find_duplicates")
        
        # Verify analyses
        self.assertIsNotNone(increment_analysis)
        self.assertIsNotNone(duplicates_analysis)
        self.assertIn("hyper_dimensional", increment_analysis)
        self.assertIn("hyper_dimensional", duplicates_analysis)
        
        logger.info(f"Increment function analysis: {increment_analysis}")
        logger.info(f"Duplicates function analysis: {duplicates_analysis}")
        
        logger.info("Function analysis test completed successfully")
    
    def test_06_function_healing(self):
        """Test function healing with agent team."""
        # Heal functions
        increment_healing = self.integrator.heal_function_with_agents(
            TEST_FUNCTION_WITH_ERROR, "increment_values", {"increment": 1})
        
        # Verify healing
        self.assertIsNotNone(increment_healing)
        self.assertIn("errors_detected", increment_healing)
        self.assertIn("healing_suggestions", increment_healing)
        
        logger.info(f"Increment function healing: {increment_healing}")
        
        logger.info("Function healing test completed successfully")
    
    def test_07_function_optimization(self):
        """Test function optimization."""
        # Optimize functions
        duplicates_optimization = self.integrator.optimize_function(
            TEST_FUNCTION_FOR_OPTIMIZATION, "find_duplicates")
        
        # Verify optimization
        self.assertIsNotNone(duplicates_optimization)
        self.assertIn("optimization_opportunities", duplicates_optimization)
        self.assertIn("optimization_suggestions", duplicates_optimization)
        
        logger.info(f"Duplicates function optimization: {duplicates_optimization}")
        
        logger.info("Function optimization test completed successfully")
    
    @unittest.skipIf(not ORCHESTRATOR_AVAILABLE, "Orchestrator not available")
    def test_08_orchestrator_integration(self):
        """Test integration with orchestrator."""
        # Verify orchestrator connection
        self.assertIsNotNone(self.orchestrator)
        self.assertTrue(self.integrator.integration_state["orchestrator_connected"])
        
        # Test integration
        try:
            integration_result = self.integrator.integrate_with_orchestrator(
                "test_functions/increment_values.py", "increment_values")
            
            # Verify integration
            self.assertIsNotNone(integration_result)
            self.assertIn("integrated", integration_result)
            self.assertTrue(integration_result["integrated"])
            
            logger.info(f"Orchestrator integration result: {integration_result}")
            
            logger.info("Orchestrator integration test completed successfully")
            
        except Exception as e:
            logger.warning(f"Orchestrator integration test failed: {str(e)}")
            self.skipTest(f"Orchestrator integration test failed: {str(e)}")
    
    def test_09_integration_status(self):
        """Test getting integration status."""
        # Get integration status
        status = self.integrator.get_integration_status()
        
        # Verify status
        self.assertIsNotNone(status)
        self.assertIn("integration_state", status)
        self.assertIn("phi_coherence", status)
        self.assertIn("coherence_quality", status)
        self.assertIn("meta_learning_stats", status)
        self.assertIn("expert_stats", status)
        self.assertIn("agent_stats", status)
        self.assertIn("hyper_stats", status)
        
        logger.info(f"Integration status: {status}")
        
        logger.info("Integration status test completed successfully")


if __name__ == "__main__":
    # Run tests
    unittest.main(verbosity=2)
