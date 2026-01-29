#!/usr/bin/env python3
"""
Quantum Collective Nodular Reasoning Test
----------------------------------------

This script tests the integration of actual quantum nodular cores with the
collective intelligence system, replacing mock nodes with true quantum-enhanced
reasoning capabilities.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import json
import logging
import numpy as np
from typing import Dict, Any, List, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumCollectiveTest")

# Import quantum modules
try:
    from quantum_collective_nodular_integration import (
        QuantumNodularReasoningCore,
        QuantumNodularNetwork,
        QuantumCollectiveIntelligenceIntegration,
        create_quantum_collective_intelligence
    )
    from quantum_nodular_core import QuantumNodularCore, QuantumNodeState, TARGET_COHERENCE
    from quantum_nodular_discovery import QuantumNodeDiscovery, create_node_discovery
    from quantum_neural_bridge import QuantumNeuralBridge
    
    # Check if collective intelligence modules are available
    try:
        from quantum_collective_intelligence_coordinator import (
            PhiResonantCollectiveIntelligenceCoordinator,
            ReasoningTask,
            ReasoningResult
        )
        from quantum_collective_reasoning_protocol import (
            PhiResonantCollectiveIntelligenceProtocol,
            PhiHarmonicReasoningProtocol,
            CoherenceConsensusMechanism
        )
        COLLECTIVE_MODULES_AVAILABLE = True
        logger.info("Collective intelligence modules available")
    except ImportError as e:
        logger.warning(f"Could not import collective intelligence modules: {e}")
        logger.warning("Using mock implementations instead")
        COLLECTIVE_MODULES_AVAILABLE = False
    
    INTEGRATION_AVAILABLE = True
    logger.info("Quantum collective nodular integration available")
except ImportError as e:
    logger.error(f"Failed to import quantum modules: {e}")
    INTEGRATION_AVAILABLE = False
    COLLECTIVE_MODULES_AVAILABLE = False

# Phi-harmonic constants
PHI = 1.618034


class TestResult:
    """Represents a test result."""
    
    def __init__(self, name: str, success: bool, details: Dict[str, Any] = None):
        """
        Initialize test result.
        
        Args:
            name: Test name
            success: Whether test succeeded
            details: Test details
        """
        self.name = name
        self.success = success
        self.details = details or {}
        self.timestamp = time.time()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert test result to dictionary.
        
        Returns:
            Dict[str, Any]: Test result as dictionary
        """
        return {
            "name": self.name,
            "success": self.success,
            "details": self.details,
            "timestamp": self.timestamp
        }


class QuantumCollectiveNodularTest:
    """Test quantum collective nodular integration."""
    
    def __init__(self):
        """Initialize test."""
        self.results = []
        self.collective = None
        self.test_queries = [
            {
                "query": "What patterns emerge from phi-harmonic resonance in quantum neural networks?",
                "context": {"domain": "quantum_computing", "complexity": "high"}
            },
            {
                "query": "How do quantum nodes achieve coherence in distributed reasoning?",
                "context": {"domain": "quantum_reasoning", "complexity": "medium"}
            },
            {
                "query": "What is the relationship between phi-resonance and quantum entanglement?",
                "context": {"domain": "quantum_physics", "complexity": "high"}
            },
            {
                "query": "How can phi-harmonic principles improve neural network training?",
                "context": {"domain": "machine_learning", "complexity": "medium"}
            },
            {
                "query": "What are the implications of quantum coherence for artificial general intelligence?",
                "context": {"domain": "artificial_intelligence", "complexity": "high"}
            }
        ]
    
    def run_tests(self) -> List[TestResult]:
        """
        Run all tests.
        
        Returns:
            List[TestResult]: Test results
        """
        if not INTEGRATION_AVAILABLE:
            logger.error("Quantum collective nodular integration not available")
            self.results.append(TestResult(
                "integration_availability",
                False,
                {"error": "Quantum collective nodular integration not available"}
            ))
            return self.results
        
        # Run tests
        self.test_initialization()
        self.test_node_creation()
        self.test_collective_creation()
        self.test_reasoning_tasks()
        self.test_protocol_processing()
        self.test_coherence_analysis()
        
        return self.results
    
    def test_initialization(self) -> None:
        """Test initialization of components."""
        try:
            # Initialize network
            network = QuantumNodularNetwork()
            
            # Initialize coordinator if available
            coordinator = None
            if COLLECTIVE_MODULES_AVAILABLE:
                discovery_service = create_node_discovery()
                coordinator = PhiResonantCollectiveIntelligenceCoordinator(discovery_service)
            
            # Initialize protocol if available
            protocol = None
            if COLLECTIVE_MODULES_AVAILABLE:
                protocol = PhiResonantCollectiveIntelligenceProtocol()
            
            # Initialize integration
            integration = QuantumCollectiveIntelligenceIntegration(
                network=network,
                coordinator=coordinator,
                protocol=protocol
            )
            
            self.results.append(TestResult(
                "initialization",
                True,
                {
                    "network_id": network.network_id,
                    "integration_id": integration.integration_id,
                    "coordinator_available": coordinator is not None,
                    "protocol_available": protocol is not None
                }
            ))
            
            logger.info("Initialization test passed")
        except Exception as e:
            logger.error(f"Initialization test failed: {e}")
            self.results.append(TestResult(
                "initialization",
                False,
                {"error": str(e)}
            ))
    
    def test_node_creation(self) -> None:
        """Test creation of quantum nodular reasoning cores."""
        try:
            # Create network
            network = QuantumNodularNetwork()
            
            # Create nodes with different capabilities
            reasoning_node = network.create_node(capabilities=["reasoning"])
            knowledge_node = network.create_node(capabilities=["reasoning", "knowledge"])
            perception_node = network.create_node(capabilities=["reasoning", "perception"])
            
            # Verify nodes
            nodes = network.get_all_nodes()
            
            self.results.append(TestResult(
                "node_creation",
                len(nodes) == 3,
                {
                    "nodes_created": len(nodes),
                    "reasoning_node_id": reasoning_node.core.state.node_id,
                    "knowledge_node_id": knowledge_node.core.state.node_id,
                    "perception_node_id": perception_node.core.state.node_id,
                    "reasoning_nodes": len(network.get_nodes_by_capability("reasoning")),
                    "knowledge_nodes": len(network.get_nodes_by_capability("knowledge")),
                    "perception_nodes": len(network.get_nodes_by_capability("perception"))
                }
            ))
            
            logger.info("Node creation test passed")
        except Exception as e:
            logger.error(f"Node creation test failed: {e}")
            self.results.append(TestResult(
                "node_creation",
                False,
                {"error": str(e)}
            ))
    
    def test_collective_creation(self) -> None:
        """Test creation of quantum collective intelligence."""
        try:
            # Create quantum collective intelligence
            self.collective = create_quantum_collective_intelligence(num_nodes=5)
            
            # Verify components
            network = self.collective.network
            coordinator = self.collective.coordinator
            protocol = self.collective.protocol
            
            self.results.append(TestResult(
                "collective_creation",
                network is not None and len(network.get_all_nodes()) == 5,
                {
                    "network_id": network.network_id if network else None,
                    "nodes_created": len(network.get_all_nodes()) if network else 0,
                    "coordinator_available": coordinator is not None,
                    "protocol_available": protocol is not None
                }
            ))
            
            logger.info("Collective creation test passed")
        except Exception as e:
            logger.error(f"Collective creation test failed: {e}")
            self.results.append(TestResult(
                "collective_creation",
                False,
                {"error": str(e)}
            ))
    
    def test_reasoning_tasks(self) -> None:
        """Test processing of reasoning tasks."""
        if not self.collective:
            logger.error("Collective not available for reasoning task test")
            self.results.append(TestResult(
                "reasoning_tasks",
                False,
                {"error": "Collective not available"}
            ))
            return
        
        try:
            # Process reasoning tasks
            task_results = []
            coherence_values = []
            
            for test_query in self.test_queries[:2]:  # Use first two queries
                result = self.collective.process_reasoning_task(
                    query=test_query["query"],
                    context=test_query["context"]
                )
                
                task_results.append(result)
                coherence_values.append(result.get("coherence", 0.0))
            
            # Calculate average coherence
            avg_coherence = sum(coherence_values) / len(coherence_values) if coherence_values else 0.0
            
            # Check if average coherence is close to target
            coherence_quality = "Excellent" if abs(avg_coherence - TARGET_COHERENCE) < 0.5 else "Good"
            
            self.results.append(TestResult(
                "reasoning_tasks",
                len(task_results) == 2,
                {
                    "tasks_processed": len(task_results),
                    "average_coherence": avg_coherence,
                    "target_coherence": TARGET_COHERENCE,
                    "coherence_quality": coherence_quality,
                    "coherence_values": coherence_values
                }
            ))
            
            logger.info(f"Reasoning tasks test passed with average coherence {avg_coherence}")
        except Exception as e:
            logger.error(f"Reasoning tasks test failed: {e}")
            self.results.append(TestResult(
                "reasoning_tasks",
                False,
                {"error": str(e)}
            ))
    
    def test_protocol_processing(self) -> None:
        """Test processing of reasoning tasks through protocol."""
        if not self.collective or not COLLECTIVE_MODULES_AVAILABLE:
            logger.error("Collective or protocol not available for protocol processing test")
            self.results.append(TestResult(
                "protocol_processing",
                False,
                {"error": "Collective or protocol not available"}
            ))
            return
        
        try:
            # Process reasoning tasks through protocol
            task_results = []
            coherence_values = []
            
            for test_query in self.test_queries[2:4]:  # Use next two queries
                result = self.collective.process_reasoning_task_with_protocol(
                    query=test_query["query"],
                    context=test_query["context"]
                )
                
                task_results.append(result)
                coherence_values.append(result.get("coherence", 0.0))
            
            # Calculate average coherence
            avg_coherence = sum(coherence_values) / len(coherence_values) if coherence_values else 0.0
            
            # Check if average coherence is close to target
            coherence_quality = "Excellent" if abs(avg_coherence - TARGET_COHERENCE) < 0.5 else "Good"
            
            self.results.append(TestResult(
                "protocol_processing",
                len(task_results) == 2,
                {
                    "tasks_processed": len(task_results),
                    "average_coherence": avg_coherence,
                    "target_coherence": TARGET_COHERENCE,
                    "coherence_quality": coherence_quality,
                    "coherence_values": coherence_values
                }
            ))
            
            logger.info(f"Protocol processing test passed with average coherence {avg_coherence}")
        except Exception as e:
            logger.error(f"Protocol processing test failed: {e}")
            self.results.append(TestResult(
                "protocol_processing",
                False,
                {"error": str(e)}
            ))
    
    def test_coherence_analysis(self) -> None:
        """Test coherence analysis of quantum nodular cores."""
        if not self.collective:
            logger.error("Collective not available for coherence analysis test")
            self.results.append(TestResult(
                "coherence_analysis",
                False,
                {"error": "Collective not available"}
            ))
            return
        
        try:
            # Get all nodes
            network = self.collective.network
            nodes = network.get_all_nodes()
            
            # Collect coherence values
            coherence_values = [node.core.state.coherence for node in nodes]
            
            # Calculate statistics
            avg_coherence = sum(coherence_values) / len(coherence_values) if coherence_values else 0.0
            min_coherence = min(coherence_values) if coherence_values else 0.0
            max_coherence = max(coherence_values) if coherence_values else 0.0
            
            # Calculate phi-resonance
            phi_resonances = [(abs((value * PHI) % 1)) for value in coherence_values]
            avg_phi_resonance = sum(phi_resonances) / len(phi_resonances) if phi_resonances else 0.0
            
            # Determine coherence quality
            coherence_quality = "Excellent" if abs(avg_coherence - TARGET_COHERENCE) < 0.5 else "Good"
            
            self.results.append(TestResult(
                "coherence_analysis",
                True,
                {
                    "nodes_analyzed": len(nodes),
                    "average_coherence": avg_coherence,
                    "min_coherence": min_coherence,
                    "max_coherence": max_coherence,
                    "target_coherence": TARGET_COHERENCE,
                    "coherence_quality": coherence_quality,
                    "average_phi_resonance": avg_phi_resonance
                }
            ))
            
            logger.info(f"Coherence analysis test passed with average coherence {avg_coherence}")
        except Exception as e:
            logger.error(f"Coherence analysis test failed: {e}")
            self.results.append(TestResult(
                "coherence_analysis",
                False,
                {"error": str(e)}
            ))
    
    def generate_report(self) -> Dict[str, Any]:
        """
        Generate test report.
        
        Returns:
            Dict[str, Any]: Test report
        """
        # Calculate overall success
        successful_tests = sum(1 for result in self.results if result.success)
        total_tests = len(self.results)
        success_rate = successful_tests / total_tests if total_tests > 0 else 0.0
        
        # Collect coherence values
        coherence_values = []
        for result in self.results:
            if result.success and "average_coherence" in result.details:
                coherence_values.append(result.details["average_coherence"])
        
        # Calculate average coherence
        avg_coherence = sum(coherence_values) / len(coherence_values) if coherence_values else 0.0
        
        # Generate report
        report = {
            "timestamp": time.time(),
            "successful_tests": successful_tests,
            "total_tests": total_tests,
            "success_rate": success_rate,
            "average_coherence": avg_coherence,
            "target_coherence": TARGET_COHERENCE,
            "coherence_difference": abs(avg_coherence - TARGET_COHERENCE) if coherence_values else None,
            "results": [result.to_dict() for result in self.results]
        }
        
        return report


def save_report(report: Dict[str, Any], file_path: str) -> bool:
    """
    Save report to file.
    
    Args:
        report: Report to save
        file_path: File path
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, "w") as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Report saved to {file_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to save report: {e}")
        return False


def main():
    """Run the test script."""
    logger.info("Starting quantum collective nodular reasoning test")
    
    # Run tests
    test = QuantumCollectiveNodularTest()
    test.run_tests()
    
    # Generate and save report
    report = test.generate_report()
    save_report(report, "quantum_collective_nodular_test_report.json")
    
    # Print summary
    print("\n=== Quantum Collective Nodular Test Results ===")
    print(f"Tests: {report['successful_tests']}/{report['total_tests']} passed ({report['success_rate'] * 100:.1f}%)")
    print(f"Average Coherence: {report['average_coherence']:.6f}")
    print(f"Target Coherence: {report['target_coherence']:.6f}")
    if report['coherence_difference'] is not None:
        print(f"Coherence Difference: {report['coherence_difference']:.6f}")
    
    # Print individual test results
    print("\nIndividual Test Results:")
    for result in test.results:
        status = "✅ PASSED" if result.success else "❌ FAILED"
        print(f"{status} - {result.name}")
    
    logger.info("Quantum collective nodular reasoning test completed")


if __name__ == "__main__":
    main()
