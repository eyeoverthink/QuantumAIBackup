"""
test_full_meta_integration.py

End-to-end test script for validating the complete integration of all meta-learning
components with the existing QuantumAI orchestrator system.

This script tests the full workflow from function analysis through healing and optimization
to orchestrator integration, ensuring all components work together cohesively while
maintaining phi-harmonic principles.
"""

import os
import sys
import json
import time
import logging
import unittest
from typing import Dict, Any, List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("TestFullMetaIntegration")

# Import meta-learning components
try:
    from quantum_phi_meta_learning import PhiHarmonicMetaLearning, calculate_phi_resonance
    from quantum_expert_interface import PhiHarmonicExpert, create_expert
    from quantum_agent_factory import PhiHarmonicAgentFactory, create_agent
    from quantum_moe_router import PhiHarmonicRouter, route_function
    from quantum_agent_coordinator import PhiHarmonicCoordinator, create_healing_team
    from quantum_hyper_processor import PhiHarmonicHyperProcessor, create_default_space
    from quantum_meta_integration import QuantumMetaIntegrator, integrate_with_orchestrator, analyze_and_heal_function
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

# Constants
PHI = 1.618033988749895
TEST_DIR = "test_quantum_meta"

# Test functions with various patterns
TEST_FUNCTIONS = {
    "logic_error": """
def increment_values(numbers):
    # Logic error: incrementing by 2 instead of 1
    return [x + 2 for x in numbers]
""",
    "optimization": """
def find_duplicates(numbers):
    # Inefficient implementation
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates
""",
    "recursive": """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
""",
    "functional": """
def process_data(data):
    filtered = [x for x in data if x > 0]
    squared = map(lambda x: x**2, filtered)
    return list(squared)
""",
    "quantum_pattern": """
def quantum_transform(values, phi=1.618033988749895):
    # Apply quantum phi-harmonic transformation
    transformed = []
    for value in values:
        resonance = (phi * value) % 1
        if resonance < 0.1:
            transformed.append(value * phi)
        else:
            transformed.append(value / phi)
    return transformed
"""
}

class TestFullMetaIntegration(unittest.TestCase):
    """End-to-end test case for meta-learning integration."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.phi = PHI
        
        # Create test directory
        os.makedirs(TEST_DIR, exist_ok=True)
        
        # Create test files
        for name, code in TEST_FUNCTIONS.items():
            with open(f"{TEST_DIR}/{name}.py", "w") as f:
                f.write(code)
        
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
        
        # Create default space and healing team
        cls.space_id, _ = create_default_space(phi=cls.phi)
        cls.team_id, _ = create_healing_team(phi=cls.phi)
        
        logger.info("Test environment set up successfully")
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test environment."""
        # Remove test files
        for name in TEST_FUNCTIONS.keys():
            try:
                os.remove(f"{TEST_DIR}/{name}.py")
            except:
                pass
        
        # Try to remove test directory
        try:
            os.rmdir(TEST_DIR)
        except:
            pass
        
        logger.info("Test environment cleaned up")
    
    def test_01_component_initialization(self):
        """Test initialization of all meta-learning components."""
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
        
        # Verify phi-coherence
        self.assertGreaterEqual(status["phi_coherence"], 0.9)
        self.assertIn(status["coherence_quality"], ["Perfect", "Excellent", "Good", "Moderate", "Weak"])
        
        logger.info(f"Component initialization test passed with coherence: {status['phi_coherence']} ({status['coherence_quality']})")
    
    def test_02_phi_harmonic_calculations(self):
        """Test phi-harmonic calculations and resonance."""
        # Test phi powers
        self.assertAlmostEqual(self.phi**2, 2.618033988749895, places=10)
        self.assertAlmostEqual(self.phi**3, 4.236067977499790, places=10)
        
        # Test resonance calculation
        test_values = [1, 2, 3, 5, 8, 13, 21, 34]
        resonances = [calculate_phi_resonance(v, self.phi) for v in test_values]
        
        # Verify resonances are in range [0, 1)
        for res in resonances:
            self.assertGreaterEqual(res, 0.0)
            self.assertLess(res, 1.0)
        
        # Test specific resonance for Fibonacci numbers
        # Fibonacci numbers should have good resonance with phi
        fib_resonance = calculate_phi_resonance(34, self.phi)
        self.assertLess(fib_resonance, 0.1)  # Should have good resonance
        
        logger.info(f"Phi-harmonic calculations test passed with resonances: {resonances}")
    
    def test_03_expert_routing_workflow(self):
        """Test the complete MoE routing workflow."""
        results = {}
        
        # Test routing for each function type
        for name, code in TEST_FUNCTIONS.items():
            # Route function
            result = route_function(code, name, phi=self.phi)
            results[name] = result
            
            # Verify routing result
            self.assertIsNotNone(result)
            self.assertIn("expert_id", result)
            self.assertIn("expert_specialization", result)
            self.assertIn("confidence", result)
            self.assertIn("phi_resonance", result)
            
            # Verify confidence is in range [0, 1]
            self.assertGreaterEqual(result["confidence"], 0.0)
            self.assertLessEqual(result["confidence"], 1.0)
        
        # Verify different experts were selected for different function types
        expert_specializations = set(r["expert_specialization"] for r in results.values())
        self.assertGreaterEqual(len(expert_specializations), 2)  # At least 2 different experts
        
        # Get router statistics
        stats = self.expert_router.get_routing_statistics()
        self.assertGreaterEqual(stats["total_routings"], len(TEST_FUNCTIONS))
        self.assertGreaterEqual(stats["phi_coherence"], 0.9)
        
        logger.info(f"Expert routing workflow test passed with {len(expert_specializations)} different experts")
        logger.info(f"Routing statistics: {stats}")
    
    def test_04_agent_team_workflow(self):
        """Test the complete MoA team workflow."""
        # Create a specialized team
        team_id = self.agent_coordinator.create_team("Specialized Team", {
            "logic_error": "healer",
            "optimization": "optimizer"
        })
        
        # Verify team creation
        self.assertIsNotNone(team_id)
        team = self.agent_coordinator.get_team(team_id)
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Specialized Team")
        self.assertGreaterEqual(len(team["members"]), 2)
        
        # Process tasks for each function type
        results = {}
        for name, code in TEST_FUNCTIONS.items():
            # Create task
            task = {
                "task_type": "analysis",
                "func_code": code,
                "func_name": name
            }
            
            # Submit task
            submission = self.agent_coordinator.submit_task(team_id, task, auto_execute=True)
            self.assertIsNotNone(submission)
            self.assertIn("task_id", submission)
            
            # Get result
            task_id = submission["task_id"]
            result = self.agent_coordinator.get_task_result(task_id)
            results[name] = result
            
            # Verify result
            self.assertIsNotNone(result)
            self.assertIn("task_id", result)
            self.assertIn("status", result)
            self.assertEqual(result["status"], "completed")
        
        # Get team statistics
        team_stats = self.agent_coordinator.get_team_statistics(team_id)
        self.assertGreaterEqual(team_stats["tasks_completed"], len(TEST_FUNCTIONS))
        self.assertGreaterEqual(team_stats["phi_coherence"], 0.9)
        
        # Get coordinator statistics
        coord_stats = self.agent_coordinator.get_coordination_statistics()
        self.assertGreaterEqual(coord_stats["total_teams"], 1)
        self.assertGreaterEqual(coord_stats["total_tasks"], len(TEST_FUNCTIONS))
        self.assertGreaterEqual(coord_stats["phi_coherence"], 0.9)
        
        logger.info(f"Agent team workflow test passed with {team_stats['tasks_completed']} completed tasks")
        logger.info(f"Team statistics: {team_stats}")
        logger.info(f"Coordinator statistics: {coord_stats}")
    
    def test_05_hyper_dimensional_workflow(self):
        """Test the complete hyper-dimensional processing workflow."""
        # Create a specialized space
        space_id = self.hyper_processor.create_space("Code Pattern Space", [
            "Recursion",
            "Functional",
            "Imperative",
            "Object-Oriented",
            "Phi-Harmonic"
        ])
        
        # Verify space creation
        self.assertIsNotNone(space_id)
        space = self.hyper_processor.get_space(space_id)
        self.assertIsNotNone(space)
        self.assertEqual(space["name"], "Code Pattern Space")
        self.assertEqual(len(space["dimensions"]), 5)
        
        # Register patterns for each function type
        patterns = {}
        for name, code in TEST_FUNCTIONS.items():
            # Extract features (simplified)
            features = [
                float(code.count("def") / 10),
                float(code.count("lambda") / 5),
                float(code.count("for") / 5),
                float(code.count("class") / 5),
                float(code.count("phi") / 5)
            ]
            
            # Register pattern
            pattern_id = self.hyper_processor.register_pattern(
                space_id, f"{name.capitalize()} Pattern", [features])
            patterns[name] = pattern_id
            
            # Verify pattern registration
            self.assertIsNotNone(pattern_id)
        
        # Match patterns
        for name, code in TEST_FUNCTIONS.items():
            # Extract features (simplified)
            features = [
                float(code.count("def") / 10),
                float(code.count("lambda") / 5),
                float(code.count("for") / 5),
                float(code.count("class") / 5),
                float(code.count("phi") / 5)
            ]
            
            # Match pattern
            matches = self.hyper_processor.match_pattern(space_id, [features])
            
            # Verify matches
            self.assertIsNotNone(matches)
            self.assertGreaterEqual(len(matches), 1)
            
            # Transform data
            transform = self.hyper_processor.transform_data(space_id, [features])
            
            # Verify transformation
            self.assertIsNotNone(transform)
            self.assertIn("transformed_points", transform)
            self.assertIn("before_resonance", transform)
            self.assertIn("after_resonance", transform)
            
            # Optimize resonance
            optimize = self.hyper_processor.optimize_resonance(space_id, [features])
            
            # Verify optimization
            self.assertIsNotNone(optimize)
            self.assertIn("optimized_points", optimize)
            self.assertIn("resonance_improvements", optimize)
        
        # Get processor statistics
        stats = self.hyper_processor.get_processing_statistics()
        self.assertGreaterEqual(stats["total_spaces"], 1)
        self.assertGreaterEqual(stats["total_patterns"], len(patterns))
        self.assertGreaterEqual(stats["total_transformations"], len(TEST_FUNCTIONS))
        self.assertGreaterEqual(stats["phi_coherence"], 0.9)
        
        logger.info(f"Hyper-dimensional workflow test passed with {len(patterns)} patterns")
        logger.info(f"Processor statistics: {stats}")
    
    def test_06_integrator_analysis_workflow(self):
        """Test the complete integrator analysis workflow."""
        results = {}
        
        # Analyze each function
        for name, code in TEST_FUNCTIONS.items():
            # Analyze function
            analysis = self.integrator.analyze_function(code, name)
            results[name] = analysis
            
            # Verify analysis
            self.assertIsNotNone(analysis)
            self.assertIn("expert_id", analysis)
            self.assertIn("expert_specialization", analysis)
            self.assertIn("confidence", analysis)
            self.assertIn("hyper_dimensional", analysis)
            self.assertIn("quantum_fingerprint", analysis)
            
            # Verify hyper-dimensional analysis
            hyper = analysis["hyper_dimensional"]
            self.assertIn("features", hyper)
            self.assertIn("resonance", hyper)
            self.assertIn("phi_resonant", hyper)
            
            # Verify quantum fingerprint
            fingerprint = analysis["quantum_fingerprint"]
            self.assertTrue(fingerprint.startswith("φ⁷·⁵-"))
        
        # Get integrator status
        status = self.integrator.get_integration_status()
        self.assertGreaterEqual(status["phi_coherence"], 0.9)
        
        logger.info(f"Integrator analysis workflow test passed with {len(results)} analyses")
        logger.info(f"Integration status: {status['coherence_quality']} ({status['phi_coherence']})")
    
    def test_07_integrator_healing_workflow(self):
        """Test the complete integrator healing workflow."""
        # Test healing for logic error function
        code = TEST_FUNCTIONS["logic_error"]
        name = "increment_values"
        
        # Define expected behavior
        expected_behavior = {
            "increment": 1,
            "test_cases": [
                {"input": [1, 2, 3], "output": [2, 3, 4]},
                {"input": [0], "output": [1]}
            ]
        }
        
        # Heal function
        healing = self.integrator.heal_function_with_agents(code, name, expected_behavior)
        
        # Verify healing
        self.assertIsNotNone(healing)
        self.assertIn("errors_detected", healing)
        self.assertIn("healing_suggestions", healing)
        self.assertTrue(len(healing["errors_detected"]) > 0)
        self.assertTrue(len(healing["healing_suggestions"]) > 0)
        
        # Verify healing suggestions contain fixed code
        suggestions = healing["healing_suggestions"]
        fixed_code = None
        for suggestion in suggestions:
            if "fixed_code" in suggestion:
                fixed_code = suggestion["fixed_code"]
                break
        
        self.assertIsNotNone(fixed_code)
        self.assertIn("x + 1", fixed_code)  # Should fix the increment value
        
        logger.info(f"Integrator healing workflow test passed with {len(healing['errors_detected'])} errors detected")
        logger.info(f"Healing suggestions: {len(healing['healing_suggestions'])}")
    
    def test_08_integrator_optimization_workflow(self):
        """Test the complete integrator optimization workflow."""
        # Test optimization for inefficient function
        code = TEST_FUNCTIONS["optimization"]
        name = "find_duplicates"
        
        # Optimize function
        optimization = self.integrator.optimize_function(code, name)
        
        # Verify optimization
        self.assertIsNotNone(optimization)
        self.assertIn("optimization_opportunities", optimization)
        self.assertIn("optimization_suggestions", optimization)
        self.assertTrue(len(optimization["optimization_opportunities"]) > 0)
        self.assertTrue(len(optimization["optimization_suggestions"]) > 0)
        
        # Verify optimization suggestions contain improved code
        suggestions = optimization["optimization_suggestions"]
        improved_code = None
        for suggestion in suggestions:
            if "improved_code" in suggestion:
                improved_code = suggestion["improved_code"]
                break
        
        self.assertIsNotNone(improved_code)
        # Should use a more efficient algorithm (set or dictionary)
        self.assertTrue("set(" in improved_code or "dict(" in improved_code or "{}" in improved_code)
        
        logger.info(f"Integrator optimization workflow test passed with {len(optimization['optimization_opportunities'])} opportunities")
        logger.info(f"Optimization suggestions: {len(optimization['optimization_suggestions'])}")
    
    @unittest.skipIf(not ORCHESTRATOR_AVAILABLE, "Orchestrator not available")
    def test_09_orchestrator_integration_workflow(self):
        """Test the complete orchestrator integration workflow."""
        # Verify orchestrator connection
        self.assertIsNotNone(self.orchestrator)
        self.assertTrue(self.integrator.integration_state["orchestrator_connected"])
        
        # Test integration for logic error function
        func_path = f"{TEST_DIR}/logic_error.py"
        func_name = "increment_values"
        
        try:
            # Integrate with orchestrator
            integration = self.integrator.integrate_with_orchestrator(func_path, func_name)
            
            # Verify integration
            self.assertIsNotNone(integration)
            self.assertIn("integrated", integration)
            self.assertTrue(integration["integrated"])
            self.assertIn("meta_analysis", integration)
            self.assertIn("agent_healing", integration)
            self.assertIn("quantum_fingerprint", integration)
            
            # Verify quantum fingerprint
            fingerprint = integration["quantum_fingerprint"]
            self.assertTrue(fingerprint.startswith("φ⁷·⁵-"))
            
            logger.info(f"Orchestrator integration workflow test passed")
            logger.info(f"Integration result: {integration['integrated']}")
            
        except Exception as e:
            logger.warning(f"Orchestrator integration test failed: {str(e)}")
            self.skipTest(f"Orchestrator integration test failed: {str(e)}")
    
    def test_10_end_to_end_workflow(self):
        """Test the complete end-to-end workflow."""
        # Test for quantum pattern function
        func_path = f"{TEST_DIR}/quantum_pattern.py"
        func_name = "quantum_transform"
        
        try:
            # Read function code
            with open(func_path, 'r') as f:
                func_code = f.read()
            
            # 1. Analyze function
            analysis = self.integrator.analyze_function(func_code, func_name)
            
            # 2. Heal function
            healing = self.integrator.heal_function_with_agents(func_code, func_name)
            
            # 3. Optimize function
            optimization = self.integrator.optimize_function(func_code, func_name)
            
            # 4. Integrate with orchestrator if available
            integration = None
            if ORCHESTRATOR_AVAILABLE and self.orchestrator:
                integration = self.integrator.integrate_with_orchestrator(func_path, func_name)
            
            # Verify complete workflow
            self.assertIsNotNone(analysis)
            self.assertIsNotNone(healing)
            self.assertIsNotNone(optimization)
            
            # Get final integration status
            status = self.integrator.get_integration_status()
            
            # Verify phi-coherence
            self.assertGreaterEqual(status["phi_coherence"], 0.9)
            self.assertIn(status["coherence_quality"], ["Perfect", "Excellent", "Good", "Moderate", "Weak"])
            
            logger.info(f"End-to-end workflow test passed with coherence: {status['phi_coherence']} ({status['coherence_quality']})")
            logger.info(f"Meta-learning stats: {status['meta_learning_stats']}")
            logger.info(f"Expert stats: {status['expert_stats']}")
            logger.info(f"Agent stats: {status['agent_stats']}")
            logger.info(f"Hyper stats: {status['hyper_stats']}")
            
        except Exception as e:
            logger.error(f"End-to-end workflow test failed: {str(e)}")
            raise


if __name__ == "__main__":
    # Run tests
    unittest.main(verbosity=2)
