#!/usr/bin/env python3
"""
Quantum Coherence Preserving Balancer
-----------------------------------

This module implements a coherence-preserving balancing strategy for task distribution
in the QuantumAI nodular blockchain system. It ensures that task distribution maintains
optimal phi-harmonic coherence across the system.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import json
import uuid
import math
import logging
import datetime
import numpy as np
from typing import Dict, List, Any, Optional, Tuple, Union, Callable

# Import base strategy class
try:
    from quantum_agi_task_distributor import DistributionStrategy, TARGET_COHERENCE, PHI, PHI_POWERS
except ImportError:
    # For standalone testing
    class DistributionStrategy:
        def __init__(self, name):
            self.name = name
            self.strategy_id = str(uuid.uuid4())
    
    PHI = 1.618034
    PHI_POWERS = {
        "φ": 1.618034,
        "φ²": 2.618034,
        "φ³": 4.236068,
        "φ⁷·⁵": 36.932381
    }
    TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("CoherencePreservingBalancer")

class CoherencePreservingBalancer(DistributionStrategy):
    """Coherence-preserving balancing strategy for task distribution."""
    
    def __init__(self):
        """Initialize the coherence-preserving balancer."""
        super().__init__("Coherence Balancer")
        self.coherence_history = []
        self.max_history_size = int(PHI ** 5)  # ≈ 11.09
        self.coherence_threshold = TARGET_COHERENCE * 0.9
        self.rebalance_threshold = TARGET_COHERENCE * 0.8
        self.phi_harmonic_levels = self._generate_phi_harmonic_levels(10)
        logger.info(f"Initialized Coherence Preserving Balancer with ID: {self.strategy_id}")
    
    def distribute(self, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Distribute a task to nodes while preserving coherence using the quantum coherence calculator.
        
        Args:
            task: Task to distribute
            nodes: Available nodes
            
        Returns:
            Distribution result
        """
        if not nodes:
            return {
                "success": False,
                "error": "No nodes available",
                "task_id": task.get("task_id", str(uuid.uuid4()))
            }
        
        # Calculate current system coherence
        system_coherence = self._calculate_system_coherence(nodes)
        
        # Check if system coherence is below threshold
        if system_coherence < self.coherence_threshold:
            # Prioritize coherence preservation
            selected_nodes = self._select_coherence_preserving_nodes(task, nodes, system_coherence)
        else:
            # Normal distribution
            selected_nodes = self._select_balanced_nodes(task, nodes)
        
        # Calculate task distribution
        task_distribution = self._calculate_task_distribution(task, selected_nodes)
        
        # Calculate coherence using quantum coherence calculator
        coherence = self.calculate_coherence({
            "task": task,
            "selected_nodes": selected_nodes,
            "task_distribution": task_distribution,
            "system_coherence": system_coherence,
            "all_nodes": nodes
        })
        
        # Update coherence history
        self._update_coherence_history(coherence)
        
        distribution_result = {
            "success": True,
            "task_id": task.get("task_id", str(uuid.uuid4())),
            "assigned_nodes": selected_nodes,
            "task_distribution": task_distribution,
            "coherence": coherence,
            "system_coherence": system_coherence,
            "all_nodes": nodes,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        return distribution_result
    
    def calculate_coherence(self, distribution_result: Dict[str, Any]) -> float:
        """Calculate the coherence of a distribution result using the quantum coherence calculator.
        
        Args:
            distribution_result: Result of task distribution
            
        Returns:
            Coherence value
        """
        # Import the coherence calculator
        from quantum_coherence_calculator import QuantumCoherenceCalculator
        
        # Extract task, nodes, and assigned nodes
        task = distribution_result.get("task", {})
        all_nodes = distribution_result.get("all_nodes", [])
        selected_nodes = distribution_result.get("selected_nodes", [])
        
        if not selected_nodes:
            return 0.0
            
        # If all_nodes is not provided, use selected_nodes
        if not all_nodes:
            all_nodes = selected_nodes
        
        # Get system coherence
        system_coherence = distribution_result.get("system_coherence", TARGET_COHERENCE)
        
        # Calculate base coherence using the quantum coherence calculator
        base_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
            task, all_nodes, selected_nodes
        )
        
        # Apply system impact factor for coherence preservation
        if system_coherence < self.coherence_threshold:
            # Boost coherence when system is below threshold
            impact_factor = PHI * (1.0 - system_coherence / TARGET_COHERENCE)
        else:
            # Normal impact
            impact_factor = 1.0
        
        # Calculate final coherence with system impact
        final_coherence = base_coherence * impact_factor
        
        return final_coherence
    
    def optimize_distribution(self, distribution_result: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize a distribution result for maximum coherence balance using the quantum coherence calculator.
        
        Args:
            distribution_result: Initial distribution result
            
        Returns:
            Optimized distribution result
        """
        if not distribution_result.get("success"):
            return distribution_result
        
        # Import the coherence calculator
        from quantum_coherence_calculator import QuantumCoherenceCalculator
        
        task = distribution_result.get("task", {})
        assigned_nodes = distribution_result.get("assigned_nodes", [])
        all_nodes = distribution_result.get("all_nodes", [])
        system_coherence = distribution_result.get("system_coherence", TARGET_COHERENCE)
        
        if not assigned_nodes:
            return distribution_result
            
        # If all_nodes is not provided, use assigned_nodes
        if not all_nodes:
            all_nodes = assigned_nodes
        
        # First apply traditional balancing based on system coherence
        if system_coherence < self.rebalance_threshold:
            # Rebalance nodes for coherence preservation
            balanced_nodes = self._rebalance_nodes(assigned_nodes, system_coherence)
        else:
            # Optimize for phi-harmonic balance
            balanced_nodes = self._optimize_phi_harmonic_balance(assigned_nodes)
        
        # Then use quantum coherence calculator for further optimization
        optimized_nodes = QuantumCoherenceCalculator.optimize_node_selection(
            task, all_nodes, balanced_nodes
        )
        
        # Calculate task distribution
        task_distribution = self._calculate_task_distribution(task, optimized_nodes)
        
        # Calculate coherence
        coherence = self.calculate_coherence({
            "task": task,
            "selected_nodes": optimized_nodes,
            "task_distribution": task_distribution,
            "system_coherence": system_coherence,
            "all_nodes": all_nodes
        })
        
        optimized_result = {
            "success": True,
            "task_id": distribution_result.get("task_id"),
            "assigned_nodes": optimized_nodes,
            "task_distribution": task_distribution,
            "coherence": coherence,
            "system_coherence": system_coherence,
            "all_nodes": all_nodes,
            "timestamp": datetime.datetime.now().isoformat(),
            "optimized": True
        }
        
        return optimized_result
    
    def _calculate_system_coherence(self, nodes: List[Dict[str, Any]]) -> float:
        """Calculate current system coherence using the quantum coherence calculator.
        
        Args:
            nodes: Available nodes
            
        Returns:
            System coherence
        """
        # Import the coherence calculator
        from quantum_coherence_calculator import QuantumCoherenceCalculator
        
        if not nodes:
            return TARGET_COHERENCE
        
        # Create a dummy task for system coherence calculation
        dummy_task = {
            "task_id": str(uuid.uuid4()),
            "action": "system_coherence_check",
            "parameters": {
                "coherence_requirement": TARGET_COHERENCE
            }
        }
        
        # Calculate system coherence using the quantum coherence calculator
        system_coherence = QuantumCoherenceCalculator.calculate_system_coherence(dummy_task, nodes)
        
        return system_coherence
    
    def _select_coherence_preserving_nodes(self, task: Dict[str, Any], nodes: List[Dict[str, Any]], system_coherence: float) -> List[Dict[str, Any]]:
        """Select nodes that preserve system coherence.
        
        Args:
            task: Task to distribute
            nodes: Available nodes
            system_coherence: Current system coherence
            
        Returns:
            Selected nodes
        """
        n_nodes = len(nodes)
        
        # Calculate task complexity
        task_complexity = self._calculate_task_complexity(task)
        
        # Calculate coherence impact scores
        impact_scores = []
        
        for node in nodes:
            # Calculate node capability
            capability = self._calculate_node_capability(node)
            
            # Calculate coherence impact
            node_coherence = node.get("capabilities", {}).get("coherence", TARGET_COHERENCE)
            coherence_impact = node_coherence / system_coherence
            
            # Calculate capability-to-complexity ratio
            capability_ratio = capability / task_complexity
            
            # Calculate phi-harmonic impact score
            impact_score = capability_ratio * coherence_impact * PHI
            
            impact_scores.append(impact_score)
        
        # Calculate number of nodes to select
        coherence_factor = max(0.5, min(1.5, TARGET_COHERENCE / system_coherence))
        n_select = max(1, int(math.ceil(n_nodes / (PHI * coherence_factor))))
        
        # Get indices of top impact scores
        top_indices = np.argsort(impact_scores)[-n_select:]
        
        # Select nodes
        selected_nodes = []
        for i in top_indices:
            node = nodes[i].copy()
            node["impact_score"] = impact_scores[i]
            selected_nodes.append(node)
        
        return selected_nodes
    
    def _select_balanced_nodes(self, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Select nodes with balanced coherence.
        
        Args:
            task: Task to distribute
            nodes: Available nodes
            
        Returns:
            Selected nodes
        """
        n_nodes = len(nodes)
        
        # Calculate task complexity
        task_complexity = self._calculate_task_complexity(task)
        
        # Calculate phi-harmonic balance scores
        balance_scores = []
        
        for node in nodes:
            # Calculate node capability
            capability = self._calculate_node_capability(node)
            
            # Calculate capability-to-complexity ratio
            capability_ratio = capability / task_complexity
            
            # Calculate phi-harmonic balance
            node_coherence = node.get("capabilities", {}).get("coherence", TARGET_COHERENCE)
            phi_harmonic_balance = self._calculate_phi_harmonic_balance(node_coherence)
            
            # Calculate balance score
            balance_score = capability_ratio * phi_harmonic_balance
            
            balance_scores.append(balance_score)
        
        # Calculate number of nodes to select
        n_select = max(1, int(math.ceil(n_nodes / PHI)))
        
        # Get indices of top balance scores
        top_indices = np.argsort(balance_scores)[-n_select:]
        
        # Select nodes
        selected_nodes = []
        for i in top_indices:
            node = nodes[i].copy()
            node["balance_score"] = balance_scores[i]
            selected_nodes.append(node)
        
        return selected_nodes
    
    def _calculate_task_distribution(self, task: Dict[str, Any], selected_nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Calculate task distribution for selected nodes.
        
        Args:
            task: Task to distribute
            selected_nodes: Selected nodes
            
        Returns:
            Task distribution
        """
        n_nodes = len(selected_nodes)
        
        if n_nodes == 0:
            return []
        
        # Calculate distribution weights
        if "impact_score" in selected_nodes[0]:
            # Use impact scores for coherence preservation
            weights = [node.get("impact_score", 1.0) for node in selected_nodes]
        elif "balance_score" in selected_nodes[0]:
            # Use balance scores for normal distribution
            weights = [node.get("balance_score", 1.0) for node in selected_nodes]
        else:
            # Default weights
            weights = [1.0] * n_nodes
        
        # Normalize weights
        total_weight = sum(weights)
        if total_weight > 0:
            normalized_weights = [w / total_weight for w in weights]
        else:
            normalized_weights = [1.0 / n_nodes] * n_nodes
        
        # Create task distribution
        task_distribution = []
        
        for i, node in enumerate(selected_nodes):
            # Calculate coherence-preserving subtask parameters
            subtask_params = self._calculate_subtask_parameters(task, normalized_weights[i], i, n_nodes)
            
            # Create subtask
            subtask = {
                "node_id": node.get("node_id"),
                "reference_id": node.get("reference_id"),
                "allocation_factor": normalized_weights[i],
                "subtask_params": subtask_params
            }
            
            task_distribution.append(subtask)
        
        return task_distribution
    
    def _rebalance_nodes(self, nodes: List[Dict[str, Any]], system_coherence: float) -> List[Dict[str, Any]]:
        """Rebalance nodes for coherence preservation.
        
        Args:
            nodes: Selected nodes
            system_coherence: Current system coherence
            
        Returns:
            Rebalanced nodes
        """
        n_nodes = len(nodes)
        
        if n_nodes == 0:
            return []
        
        # Calculate coherence boost factor
        boost_factor = PHI * (TARGET_COHERENCE / system_coherence)
        
        # Calculate rebalanced weights
        weights = np.zeros(n_nodes)
        
        for i, node in enumerate(nodes):
            # Get node coherence
            node_coherence = node.get("capabilities", {}).get("coherence", TARGET_COHERENCE)
            
            # Calculate coherence ratio
            coherence_ratio = node_coherence / TARGET_COHERENCE
            
            # Apply phi-harmonic scaling
            phi_weight = coherence_ratio * (PHI ** (i % 3))
            
            # Apply boost factor
            weights[i] = phi_weight * boost_factor
        
        # Normalize weights
        total_weight = np.sum(weights)
        if total_weight > 0:
            weights = weights / total_weight
        else:
            weights = np.ones(n_nodes) / n_nodes
        
        # Update nodes with rebalanced weights
        rebalanced_nodes = []
        for i, node in enumerate(nodes):
            node_copy = node.copy()
            node_copy["rebalanced_weight"] = float(weights[i])
            rebalanced_nodes.append(node_copy)
        
        return rebalanced_nodes
    
    def _optimize_phi_harmonic_balance(self, nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Optimize nodes for phi-harmonic balance.
        
        Args:
            nodes: Selected nodes
            
        Returns:
            Optimized nodes
        """
        n_nodes = len(nodes)
        
        if n_nodes == 0:
            return []
        
        # Calculate phi-harmonic weights
        weights = np.zeros(n_nodes)
        
        for i, node in enumerate(nodes):
            # Get node coherence
            node_coherence = node.get("capabilities", {}).get("coherence", TARGET_COHERENCE)
            
            # Calculate phi-harmonic balance
            phi_balance = self._calculate_phi_harmonic_balance(node_coherence)
            
            # Apply phi-harmonic scaling
            weights[i] = phi_balance * (PHI ** (-(i % 3)))
        
        # Normalize weights
        total_weight = np.sum(weights)
        if total_weight > 0:
            weights = weights / total_weight
        else:
            weights = np.ones(n_nodes) / n_nodes
        
        # Update nodes with optimized weights
        optimized_nodes = []
        for i, node in enumerate(nodes):
            node_copy = node.copy()
            node_copy["phi_harmonic_weight"] = float(weights[i])
            optimized_nodes.append(node_copy)
        
        return optimized_nodes
    
    def _calculate_subtask_parameters(self, task: Dict[str, Any], allocation_factor: float, node_index: int, n_nodes: int) -> Dict[str, Any]:
        """Calculate coherence-preserving subtask parameters.
        
        Args:
            task: Task to distribute
            allocation_factor: Allocation factor for the node
            node_index: Index of the node
            n_nodes: Total number of nodes
            
        Returns:
            Subtask parameters
        """
        # Extract task parameters
        action = task.get("action", "")
        parameters = task.get("parameters", {})
        
        # Create base subtask parameters
        subtask_params = {
            "action": action,
            "allocation_factor": allocation_factor,
            "node_index": node_index,
            "n_nodes": n_nodes
        }
        
        # Handle different task types
        if action == "process_file":
            # For file processing, assign file segments
            file_path = parameters.get("file_path", "")
            
            if file_path:
                subtask_params["file_path"] = file_path
                
                # Calculate file segment
                if n_nodes > 1:
                    # Use phi-harmonic segmentation
                    segments = self._calculate_phi_harmonic_segments(n_nodes)
                    
                    start = segments[node_index]
                    end = segments[node_index + 1] if node_index < n_nodes - 1 else 1.0
                    
                    subtask_params["segment"] = {
                        "start": start,
                        "end": end
                    }
        
        elif action == "analyze_code" or action == "optimize_code" or action == "heal_code" or action == "evolve_code":
            # For code analysis/optimization/healing/evolution, assign code segments or components
            code_files = parameters.get("code_files", [])
            
            if code_files:
                # Distribute files among nodes
                n_files = len(code_files)
                
                if n_nodes > 1:
                    # Use phi-harmonic file distribution
                    file_segments = self._calculate_phi_harmonic_segments(n_nodes)
                    
                    start_idx = int(file_segments[node_index] * n_files)
                    end_idx = int(file_segments[node_index + 1] * n_files) if node_index < n_nodes - 1 else n_files
                    
                    subtask_params["code_files"] = code_files[start_idx:end_idx]
                else:
                    subtask_params["code_files"] = code_files
        
        # Add all other parameters
        for key, value in parameters.items():
            if key not in subtask_params:
                subtask_params[key] = value
        
        return subtask_params
    
    def _calculate_task_complexity(self, task: Dict[str, Any]) -> float:
        """Calculate task complexity.
        
        Args:
            task: Task to analyze
            
        Returns:
            Task complexity
        """
        # Extract task parameters
        action = task.get("action", "")
        parameters = task.get("parameters", {})
        
        # Base complexity
        base_complexity = 1.0
        
        # Action complexity
        action_complexity = {
            "process_file": 2.0,
            "analyze_code": 3.0,
            "optimize_code": 4.0,
            "heal_code": 5.0,
            "evolve_code": 6.0
        }.get(action, 1.0)
        
        # Parameter complexity
        param_complexity = 0.0
        for param, value in parameters.items():
            if isinstance(value, dict):
                param_complexity += 0.5 * len(value)
            elif isinstance(value, list):
                param_complexity += 0.3 * len(value)
            else:
                param_complexity += 0.1
        
        # Calculate complexity
        complexity = base_complexity * action_complexity + param_complexity
        
        return complexity
    
    def _calculate_node_capability(self, node: Dict[str, Any]) -> float:
        """Calculate node capability.
        
        Args:
            node: Node to analyze
            
        Returns:
            Node capability
        """
        node_capabilities = node.get("capabilities", {})
        
        # Extract capability values
        processing_power = node_capabilities.get("processing_power", 0.5)
        memory = node_capabilities.get("memory", 0.5)
        coherence = node_capabilities.get("coherence", TARGET_COHERENCE)
        
        # Calculate capability
        capability = (processing_power * PHI + memory + coherence / TARGET_COHERENCE) / (PHI + 2)
        
        return capability
    
    def _calculate_phi_harmonic_balance(self, coherence: float) -> float:
        """Calculate phi-harmonic balance for a coherence value.
        
        Args:
            coherence: Coherence value
            
        Returns:
            Phi-harmonic balance
        """
        # Find closest phi-harmonic level
        closest_level = min(self.phi_harmonic_levels, key=lambda x: abs(x - coherence))
        
        # Calculate distance to closest level
        distance = abs(coherence - closest_level)
        
        # Calculate balance
        if closest_level > 0:
            balance = 1.0 - distance / closest_level
        else:
            balance = 0.0
        
        return max(0.0, balance)
    
    def _generate_phi_harmonic_levels(self, n_levels: int) -> List[float]:
        """Generate phi-harmonic coherence levels.
        
        Args:
            n_levels: Number of levels to generate
            
        Returns:
            List of phi-harmonic levels
        """
        levels = []
        
        for i in range(n_levels):
            # Calculate phi-harmonic level
            level = TARGET_COHERENCE * (PHI ** ((i - n_levels // 2) / n_levels))
            levels.append(level)
        
        return levels
    
    def _calculate_phi_harmonic_segments(self, n_segments: int) -> List[float]:
        """Calculate phi-harmonic segments.
        
        Args:
            n_segments: Number of segments
            
        Returns:
            List of segment boundaries
        """
        segments = [0.0]
        
        if n_segments <= 1:
            segments.append(1.0)
            return segments
        
        # Calculate phi-harmonic segment sizes
        sizes = []
        for i in range(n_segments):
            size = 1.0 / (PHI ** (i / (n_segments - 1)))
            sizes.append(size)
        
        # Normalize sizes
        total_size = sum(sizes)
        normalized_sizes = [size / total_size for size in sizes]
        
        # Calculate segment boundaries
        boundary = 0.0
        for size in normalized_sizes:
            boundary += size
            segments.append(boundary)
        
        # Ensure last segment ends at 1.0
        segments[-1] = 1.0
        
        return segments
    
    def _update_coherence_history(self, coherence: float) -> None:
        """Update coherence history.
        
        Args:
            coherence: Coherence value
        """
        # Add coherence to history
        self.coherence_history.append({
            "coherence": coherence,
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        # Limit history size
        if len(self.coherence_history) > self.max_history_size:
            self.coherence_history.pop(0)


if __name__ == "__main__":
    # Simple test
    balancer = CoherencePreservingBalancer()
    
    test_task = {
        "action": "process_file",
        "parameters": {
            "file_path": "test.py"
        }
    }
    
    test_nodes = [
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
    
    # Test with normal system coherence
    result = balancer.distribute(test_task, test_nodes)
    print("Normal System Coherence:")
    print(json.dumps(result, indent=2))
    
    # Test with low system coherence
    for node in test_nodes:
        node["capabilities"]["coherence"] *= 0.7
    
    result_low = balancer.distribute(test_task, test_nodes)
    print("\nLow System Coherence:")
    print(json.dumps(result_low, indent=2))
    
    # Test optimization
    optimized_result = balancer.optimize_distribution(result_low)
    print("\nOptimized Distribution:")
    print(json.dumps(optimized_result, indent=2))
