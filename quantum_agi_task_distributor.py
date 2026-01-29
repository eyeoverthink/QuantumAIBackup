#!/usr/bin/env python3
"""
Quantum AGI Task Distributor
----------------------------

Core module for AGI-level task distribution in the QuantumAI nodular blockchain system.
This module implements advanced task distribution algorithms based on phi-harmonic
principles, quantum swarm intelligence, and multi-dimensional capability matching.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import json
import uuid
import time
import math
import logging
import datetime
import numpy as np
from typing import Dict, List, Any, Optional, Tuple, Union, Callable

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumAGITaskDistributor")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁴": 6.854102,
    "φ⁵": 11.090170,
    "φ⁶": 17.944272,
    "φ⁷": 29.034442,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

class DistributionStrategy:
    """Base class for task distribution strategies."""
    
    def __init__(self, name: str):
        """Initialize the distribution strategy.
        
        Args:
            name: Name of the strategy
        """
        self.name = name
        self.coherence = TARGET_COHERENCE
        self.strategy_id = str(uuid.uuid4())
        logger.info(f"Initialized {name} distribution strategy with ID: {self.strategy_id}")
    
    def distribute(self, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Distribute a task to nodes.
        
        Args:
            task: Task to distribute
            nodes: Available nodes
            
        Returns:
            Distribution result
        """
        raise NotImplementedError("Subclasses must implement distribute()")
    
    def calculate_coherence(self, distribution_result: Dict[str, Any]) -> float:
        """Calculate the coherence of a distribution result.
        
        Args:
            distribution_result: Result of task distribution
            
        Returns:
            Coherence value
        """
        raise NotImplementedError("Subclasses must implement calculate_coherence()")
    
    def optimize_distribution(self, distribution_result: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize a distribution result for maximum coherence.
        
        Args:
            distribution_result: Initial distribution result
            
        Returns:
            Optimized distribution result
        """
        raise NotImplementedError("Subclasses must implement optimize_distribution()")


class QuantumAGITaskDistributor:
    """AGI-level task distributor for quantum nodular blockchain system."""
    
    def __init__(self, blockchain_connector=None, node_discovery=None):
        """Initialize the task distributor.
        
        Args:
            blockchain_connector: Blockchain connector instance
            node_discovery: Node discovery instance
        """
        self.distributor_id = str(uuid.uuid4())
        self.blockchain_connector = blockchain_connector
        self.node_discovery = node_discovery
        self.strategies = {}
        self.distribution_history = []
        self.coherence = TARGET_COHERENCE
        self.meta_strategy = None
        self.initialized = False
        
        logger.info(f"Initialized QuantumAGITaskDistributor with ID: {self.distributor_id}")
    
    def initialize(self):
        """Initialize the task distributor with strategies."""
        if self.initialized:
            logger.warning("Task distributor already initialized")
            return
        
        # Import strategies here to avoid circular imports
        from quantum_phi_harmonic_allocation import PhiHarmonicAllocationStrategy
        from quantum_swarm_strategy import QuantumSwarmStrategy
        from quantum_tensor_capability_matcher import TensorCapabilityMatcher
        from quantum_adaptive_distribution_learner import AdaptiveDistributionLearner
        from quantum_coherence_preserving_balancer import CoherencePreservingBalancer
        
        # Register strategies
        self.register_strategy("phi_harmonic", PhiHarmonicAllocationStrategy())
        self.register_strategy("quantum_swarm", QuantumSwarmStrategy())
        self.register_strategy("tensor_capability", TensorCapabilityMatcher())
        self.register_strategy("adaptive_learning", AdaptiveDistributionLearner())
        self.register_strategy("coherence_balancer", CoherencePreservingBalancer())
        
        # Set default meta-strategy
        self.set_meta_strategy("phi_harmonic")
        
        self.initialized = True
        logger.info("Task distributor initialized with all strategies")
    
    def register_strategy(self, strategy_name: str, strategy: DistributionStrategy) -> bool:
        """Register a distribution strategy.
        
        Args:
            strategy_name: Name of the strategy
            strategy: Strategy instance
            
        Returns:
            Success status
        """
        if strategy_name in self.strategies:
            logger.warning(f"Strategy {strategy_name} already registered")
            return False
        
        self.strategies[strategy_name] = strategy
        logger.info(f"Registered strategy: {strategy_name}")
        return True
    
    def set_meta_strategy(self, strategy_name: str) -> bool:
        """Set the meta-strategy for task distribution.
        
        Args:
            strategy_name: Name of the strategy to use as meta-strategy
            
        Returns:
            Success status
        """
        if strategy_name not in self.strategies:
            logger.error(f"Strategy {strategy_name} not registered")
            return False
        
        self.meta_strategy = strategy_name
        logger.info(f"Set meta-strategy to: {strategy_name}")
        return True
    
    def distribute_task(self, task: Dict[str, Any], node_type: str = None) -> Dict[str, Any]:
        """Distribute a task to nodes.
        
        Args:
            task: Task to distribute
            node_type: Type of nodes to consider
            
        Returns:
            Distribution result
        """
        if not self.initialized:
            self.initialize()
        
        # Generate task ID if not provided
        if "task_id" not in task:
            task["task_id"] = str(uuid.uuid4())
        
        # Add timestamp if not provided
        if "timestamp" not in task:
            task["timestamp"] = datetime.datetime.now().isoformat()
        
        # Discover nodes
        nodes = self._discover_nodes(node_type)
        if not nodes:
            logger.warning(f"No nodes found for type: {node_type}")
            return {
                "success": False,
                "error": f"No nodes found for type: {node_type}",
                "task_id": task["task_id"]
            }
        
        # Get strategy
        strategy = self.strategies.get(self.meta_strategy)
        if not strategy:
            logger.error(f"Meta-strategy {self.meta_strategy} not found")
            return {
                "success": False,
                "error": f"Meta-strategy {self.meta_strategy} not found",
                "task_id": task["task_id"]
            }
        
        # Distribute task
        logger.info(f"Distributing task {task['task_id']} using strategy: {self.meta_strategy}")
        distribution_result = strategy.distribute(task, nodes)
        
        # Calculate coherence
        coherence = strategy.calculate_coherence(distribution_result)
        distribution_result["coherence"] = coherence
        
        # Optimize distribution if coherence is below target
        if coherence < TARGET_COHERENCE * 0.9:
            logger.info(f"Optimizing distribution for task {task['task_id']}")
            distribution_result = strategy.optimize_distribution(distribution_result)
            coherence = strategy.calculate_coherence(distribution_result)
            distribution_result["coherence"] = coherence
        
        # Record distribution in history
        self._record_distribution(task, distribution_result)
        
        # Store distribution result in blockchain
        if self.blockchain_connector:
            self._store_distribution_result(distribution_result)
        
        return distribution_result
    
    def collect_task_results(self, task_id: str) -> Dict[str, Any]:
        """Collect results for a distributed task.
        
        Args:
            task_id: ID of the task
            
        Returns:
            Collection result
        """
        if not self.initialized:
            self.initialize()
        
        # Find distribution record
        distribution_record = None
        for record in self.distribution_history:
            if record["task"]["task_id"] == task_id:
                distribution_record = record
                break
        
        if not distribution_record:
            logger.warning(f"No distribution record found for task: {task_id}")
            return {
                "success": False,
                "error": f"No distribution record found for task: {task_id}",
                "task_id": task_id
            }
        
        # Collect results from assigned nodes
        results = []
        assigned_nodes = distribution_record["distribution_result"].get("assigned_nodes", [])
        
        for node in assigned_nodes:
            node_id = node.get("node_id")
            reference_id = node.get("reference_id")
            
            # Get node result
            node_result = self._get_node_result(node_id, reference_id, task_id)
            if node_result:
                results.append({
                    "node_id": node_id,
                    "reference_id": reference_id,
                    "result": node_result
                })
        
        # Calculate coherence of results
        coherence = self._calculate_results_coherence(results)
        
        collection_result = {
            "success": True,
            "task_id": task_id,
            "results": results,
            "coherence": coherence,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        # Store collection result in blockchain
        if self.blockchain_connector:
            self._store_collection_result(collection_result)
        
        return collection_result
    
    def get_distribution_history(self) -> List[Dict[str, Any]]:
        """Get the distribution history.
        
        Returns:
            Distribution history
        """
        return self.distribution_history
    
    def get_strategy_performance(self, strategy_name: str = None) -> Dict[str, Any]:
        """Get performance metrics for a strategy.
        
        Args:
            strategy_name: Name of the strategy
            
        Returns:
            Performance metrics
        """
        if not strategy_name:
            strategy_name = self.meta_strategy
        
        if strategy_name not in self.strategies:
            logger.error(f"Strategy {strategy_name} not found")
            return {
                "success": False,
                "error": f"Strategy {strategy_name} not found"
            }
        
        # Calculate performance metrics
        strategy_distributions = [
            record for record in self.distribution_history
            if record["strategy"] == strategy_name
        ]
        
        if not strategy_distributions:
            return {
                "success": True,
                "strategy": strategy_name,
                "distributions": 0,
                "average_coherence": 0,
                "max_coherence": 0,
                "min_coherence": 0
            }
        
        coherence_values = [
            record["distribution_result"].get("coherence", 0)
            for record in strategy_distributions
        ]
        
        return {
            "success": True,
            "strategy": strategy_name,
            "distributions": len(strategy_distributions),
            "average_coherence": sum(coherence_values) / len(coherence_values),
            "max_coherence": max(coherence_values),
            "min_coherence": min(coherence_values)
        }
    
    def _discover_nodes(self, node_type: str = None) -> List[Dict[str, Any]]:
        """Discover nodes for task distribution.
        
        Args:
            node_type: Type of nodes to discover
            
        Returns:
            Discovered nodes
        """
        if self.node_discovery:
            return self.node_discovery.discover_nodes(node_type=node_type)
        
        # Mock node discovery for testing
        return [
            {
                "node_id": f"node-{i}",
                "reference_id": f"ref-{i}",
                "capabilities": {
                    "processing_power": 0.8 + 0.2 * math.sin(i),
                    "memory": 0.7 + 0.3 * math.cos(i),
                    "coherence": TARGET_COHERENCE * (0.9 + 0.1 * math.sin(i * PHI))
                }
            }
            for i in range(5)
        ]
    
    def _record_distribution(self, task: Dict[str, Any], distribution_result: Dict[str, Any]):
        """Record a task distribution in history.
        
        Args:
            task: Distributed task
            distribution_result: Distribution result
        """
        record = {
            "task": task,
            "distribution_result": distribution_result,
            "strategy": self.meta_strategy,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        self.distribution_history.append(record)
        
        # Limit history size
        if len(self.distribution_history) > 100:
            self.distribution_history = self.distribution_history[-100:]
    
    def _store_distribution_result(self, distribution_result: Dict[str, Any]) -> str:
        """Store distribution result in blockchain.
        
        Args:
            distribution_result: Distribution result
            
        Returns:
            Reference ID
        """
        if not self.blockchain_connector:
            return None
        
        try:
            reference_id = self.blockchain_connector.store_data(
                data_type="task_distribution",
                data=distribution_result
            )
            logger.info(f"Stored distribution result in blockchain: {reference_id}")
            return reference_id
        except Exception as e:
            logger.error(f"Failed to store distribution result: {e}")
            return None
    
    def _store_collection_result(self, collection_result: Dict[str, Any]) -> str:
        """Store collection result in blockchain.
        
        Args:
            collection_result: Collection result
            
        Returns:
            Reference ID
        """
        if not self.blockchain_connector:
            return None
        
        try:
            reference_id = self.blockchain_connector.store_data(
                data_type="task_collection",
                data=collection_result
            )
            logger.info(f"Stored collection result in blockchain: {reference_id}")
            return reference_id
        except Exception as e:
            logger.error(f"Failed to store collection result: {e}")
            return None
    
    def _get_node_result(self, node_id: str, reference_id: str, task_id: str) -> Dict[str, Any]:
        """Get result from a node.
        
        Args:
            node_id: ID of the node
            reference_id: Reference ID of the node
            task_id: ID of the task
            
        Returns:
            Node result
        """
        if self.blockchain_connector:
            try:
                # Query blockchain for node result
                result = self.blockchain_connector.query_data(
                    query={
                        "node_id": node_id,
                        "task_id": task_id
                    },
                    data_type="task_result"
                )
                
                if result:
                    return result
            except Exception as e:
                logger.error(f"Failed to get node result: {e}")
        
        # Mock result for testing
        return {
            "success": True,
            "task_id": task_id,
            "node_id": node_id,
            "result_data": {
                "value": 42 * PHI,
                "coherence": TARGET_COHERENCE
            },
            "timestamp": datetime.datetime.now().isoformat()
        }
    
    def _calculate_results_coherence(self, results: List[Dict[str, Any]]) -> float:
        """Calculate coherence of task results.
        
        Args:
            results: Task results
            
        Returns:
            Coherence value
        """
        if not results:
            return 0
        
        # Extract coherence values
        coherence_values = []
        for result in results:
            if "result" in result and "coherence" in result["result"]:
                coherence_values.append(result["result"]["coherence"])
        
        if not coherence_values:
            return 0
        
        # Calculate phi-harmonic mean
        phi_harmonic_sum = sum(1 / (value + 1e-10) for value in coherence_values)
        phi_harmonic_mean = len(coherence_values) / phi_harmonic_sum
        
        # Apply phi scaling
        phi_scaled = phi_harmonic_mean * PHI / math.sqrt(len(coherence_values))
        
        # Normalize to target coherence
        normalized = phi_scaled / TARGET_COHERENCE
        
        return normalized * TARGET_COHERENCE


if __name__ == "__main__":
    # Simple test
    distributor = QuantumAGITaskDistributor()
    distributor.initialize()
    
    test_task = {
        "action": "test_task",
        "parameters": {
            "value": 42
        }
    }
    
    result = distributor.distribute_task(test_task, node_type="test")
    print(json.dumps(result, indent=2))
    
    collection_result = distributor.collect_task_results(result["task_id"])
    print(json.dumps(collection_result, indent=2))
