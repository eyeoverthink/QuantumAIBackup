#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Allocation Strategy
---------------------------------------

This module implements a phi-harmonic task allocation strategy for the QuantumAI
nodular blockchain system. It uses golden ratio principles to optimally distribute
tasks while maintaining phi-harmonic coherence across the network.

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
logger = logging.getLogger("PhiHarmonicAllocation")

class PhiHarmonicAllocationStrategy(DistributionStrategy):
    """Phi-harmonic task allocation strategy based on golden ratio principles."""
    
    def __init__(self):
        """Initialize the phi-harmonic allocation strategy."""
        super().__init__("Phi-Harmonic Allocation")
        self.phi_sequence = self._generate_phi_sequence(10)
        self.phi_matrix = self._generate_phi_matrix(5, 5)
        logger.info(f"Initialized Phi-Harmonic Allocation Strategy with ID: {self.strategy_id}")
    
    def distribute(self, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Distribute a task to nodes using phi-harmonic allocation.
        
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
        
        # Calculate phi-harmonic task complexity
        task_complexity = self._calculate_task_complexity(task)
        
        # Calculate phi-harmonic node capabilities
        node_capabilities = self._calculate_node_capabilities(nodes)
        
        # Calculate phi-harmonic allocation matrix
        allocation_matrix = self._calculate_allocation_matrix(task_complexity, node_capabilities)
        
        # Select nodes based on allocation matrix
        selected_nodes = self._select_nodes(nodes, allocation_matrix)
        
        # Calculate task distribution
        task_distribution = self._calculate_task_distribution(task, selected_nodes)
        
        # Calculate coherence
        coherence = self.calculate_coherence({
            "task": task,
            "selected_nodes": selected_nodes,
            "task_distribution": task_distribution
        })
        
        distribution_result = {
            "success": True,
            "task_id": task.get("task_id", str(uuid.uuid4())),
            "assigned_nodes": selected_nodes,
            "task_distribution": task_distribution,
            "coherence": coherence,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        return distribution_result
    
    def calculate_coherence(self, distribution_result: Dict[str, Any]) -> float:
        """Calculate the coherence of a distribution result.
        
        Args:
            distribution_result: Result of task distribution
            
        Returns:
            Coherence value
        """
        if not distribution_result.get("selected_nodes"):
            return 0
        
        # Extract node coherence values
        node_coherence_values = []
        for node in distribution_result.get("selected_nodes", []):
            if "capabilities" in node and "coherence" in node["capabilities"]:
                node_coherence_values.append(node["capabilities"]["coherence"])
        
        if not node_coherence_values:
            return 0
        
        # Calculate phi-weighted coherence
        phi_weights = [PHI ** (-(i+1)) for i in range(len(node_coherence_values))]
        weighted_sum = sum(w * c for w, c in zip(phi_weights, node_coherence_values))
        phi_weighted_coherence = weighted_sum / sum(phi_weights)
        
        # Apply phi-harmonic scaling
        phi_harmonic_factor = PHI * (1 - math.exp(-len(node_coherence_values) / PHI))
        scaled_coherence = phi_weighted_coherence * phi_harmonic_factor
        
        # Normalize to target coherence
        normalized_coherence = scaled_coherence / TARGET_COHERENCE
        final_coherence = normalized_coherence * TARGET_COHERENCE
        
        return min(final_coherence, TARGET_COHERENCE * PHI)
    
    def optimize_distribution(self, distribution_result: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize a distribution result for maximum coherence.
        
        Args:
            distribution_result: Initial distribution result
            
        Returns:
            Optimized distribution result
        """
        if not distribution_result.get("success"):
            return distribution_result
        
        task = distribution_result.get("task", {})
        assigned_nodes = distribution_result.get("assigned_nodes", [])
        
        if not assigned_nodes:
            return distribution_result
        
        # Sort nodes by coherence
        assigned_nodes.sort(
            key=lambda node: node.get("capabilities", {}).get("coherence", 0),
            reverse=True
        )
        
        # Calculate optimal task distribution
        task_distribution = self._calculate_optimal_task_distribution(task, assigned_nodes)
        
        # Calculate coherence
        coherence = self.calculate_coherence({
            "task": task,
            "selected_nodes": assigned_nodes,
            "task_distribution": task_distribution
        })
        
        optimized_result = {
            "success": True,
            "task_id": distribution_result.get("task_id"),
            "assigned_nodes": assigned_nodes,
            "task_distribution": task_distribution,
            "coherence": coherence,
            "timestamp": datetime.datetime.now().isoformat(),
            "optimized": True
        }
        
        return optimized_result
    
    def _calculate_task_complexity(self, task: Dict[str, Any]) -> float:
        """Calculate phi-harmonic task complexity.
        
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
        
        # Calculate phi-harmonic complexity
        complexity = base_complexity * action_complexity + param_complexity
        phi_harmonic_complexity = complexity * (PHI ** (complexity / 10))
        
        return phi_harmonic_complexity
    
    def _calculate_node_capabilities(self, nodes: List[Dict[str, Any]]) -> List[float]:
        """Calculate phi-harmonic node capabilities.
        
        Args:
            nodes: Available nodes
            
        Returns:
            Node capabilities
        """
        capabilities = []
        
        for node in nodes:
            node_capabilities = node.get("capabilities", {})
            
            # Extract capability values
            processing_power = node_capabilities.get("processing_power", 0.5)
            memory = node_capabilities.get("memory", 0.5)
            coherence = node_capabilities.get("coherence", TARGET_COHERENCE)
            
            # Calculate phi-harmonic capability
            capability = (processing_power * PHI + memory + coherence / TARGET_COHERENCE) / (PHI + 2)
            capabilities.append(capability)
        
        return capabilities
    
    def _calculate_allocation_matrix(self, task_complexity: float, node_capabilities: List[float]) -> np.ndarray:
        """Calculate phi-harmonic allocation matrix.
        
        Args:
            task_complexity: Task complexity
            node_capabilities: Node capabilities
            
        Returns:
            Allocation matrix
        """
        n_nodes = len(node_capabilities)
        
        # Create allocation matrix
        allocation_matrix = np.zeros(n_nodes)
        
        # Calculate phi-harmonic allocation
        for i in range(n_nodes):
            # Phi-harmonic allocation factor
            phi_factor = PHI ** (-(i+1))
            
            # Node capability factor
            capability_factor = node_capabilities[i]
            
            # Task complexity factor
            complexity_factor = 1.0 / (1.0 + math.exp(-(task_complexity - 5.0) / 2.0))
            
            # Combined allocation factor
            allocation_factor = phi_factor * capability_factor * complexity_factor
            
            allocation_matrix[i] = allocation_factor
        
        # Normalize allocation matrix
        if np.sum(allocation_matrix) > 0:
            allocation_matrix = allocation_matrix / np.sum(allocation_matrix)
        
        return allocation_matrix
    
    def _select_nodes(self, nodes: List[Dict[str, Any]], allocation_matrix: np.ndarray) -> List[Dict[str, Any]]:
        """Select nodes based on allocation matrix.
        
        Args:
            nodes: Available nodes
            allocation_matrix: Allocation matrix
            
        Returns:
            Selected nodes
        """
        n_nodes = len(nodes)
        
        # Calculate number of nodes to select
        n_select = max(1, int(math.ceil(n_nodes * PHI / (PHI + 1))))
        
        # Get indices of top allocation values
        top_indices = np.argsort(allocation_matrix)[-n_select:]
        
        # Select nodes
        selected_nodes = []
        for i in top_indices:
            node = nodes[i].copy()
            node["allocation_factor"] = float(allocation_matrix[i])
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
        
        # Calculate allocation factors
        allocation_factors = [node.get("allocation_factor", 1.0 / n_nodes) for node in selected_nodes]
        
        # Normalize allocation factors
        total_allocation = sum(allocation_factors)
        if total_allocation > 0:
            allocation_factors = [f / total_allocation for f in allocation_factors]
        else:
            allocation_factors = [1.0 / n_nodes] * n_nodes
        
        # Create task distribution
        task_distribution = []
        
        for i, node in enumerate(selected_nodes):
            # Calculate phi-harmonic subtask parameters
            subtask_params = self._calculate_subtask_parameters(task, allocation_factors[i], i, n_nodes)
            
            # Create subtask
            subtask = {
                "node_id": node.get("node_id"),
                "reference_id": node.get("reference_id"),
                "allocation_factor": allocation_factors[i],
                "subtask_params": subtask_params
            }
            
            task_distribution.append(subtask)
        
        return task_distribution
    
    def _calculate_optimal_task_distribution(self, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Calculate optimal task distribution for maximum coherence.
        
        Args:
            task: Task to distribute
            nodes: Available nodes
            
        Returns:
            Optimal task distribution
        """
        n_nodes = len(nodes)
        
        if n_nodes == 0:
            return []
        
        # Calculate phi-harmonic allocation factors
        phi_factors = [PHI ** (-(i+1)) for i in range(n_nodes)]
        
        # Extract node coherence values
        node_coherence = [
            node.get("capabilities", {}).get("coherence", TARGET_COHERENCE)
            for node in nodes
        ]
        
        # Calculate coherence-weighted allocation factors
        coherence_weights = [c / TARGET_COHERENCE for c in node_coherence]
        weighted_factors = [p * c for p, c in zip(phi_factors, coherence_weights)]
        
        # Normalize allocation factors
        total_allocation = sum(weighted_factors)
        if total_allocation > 0:
            allocation_factors = [f / total_allocation for f in weighted_factors]
        else:
            allocation_factors = [1.0 / n_nodes] * n_nodes
        
        # Create task distribution
        task_distribution = []
        
        for i, node in enumerate(nodes):
            # Calculate phi-harmonic subtask parameters
            subtask_params = self._calculate_subtask_parameters(task, allocation_factors[i], i, n_nodes)
            
            # Create subtask
            subtask = {
                "node_id": node.get("node_id"),
                "reference_id": node.get("reference_id"),
                "allocation_factor": allocation_factors[i],
                "subtask_params": subtask_params
            }
            
            task_distribution.append(subtask)
        
        return task_distribution
    
    def _calculate_subtask_parameters(self, task: Dict[str, Any], allocation_factor: float, node_index: int, n_nodes: int) -> Dict[str, Any]:
        """Calculate phi-harmonic subtask parameters.
        
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
                    segment_size = 1.0 / n_nodes
                    start = node_index * segment_size
                    end = (node_index + 1) * segment_size
                    
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
                files_per_node = max(1, n_files // n_nodes)
                
                start_idx = node_index * files_per_node
                end_idx = min(n_files, (node_index + 1) * files_per_node)
                
                if node_index == n_nodes - 1:
                    end_idx = n_files
                
                subtask_params["code_files"] = code_files[start_idx:end_idx]
        
        # Add all other parameters
        for key, value in parameters.items():
            if key not in subtask_params:
                subtask_params[key] = value
        
        return subtask_params
    
    def _generate_phi_sequence(self, n: int) -> List[float]:
        """Generate a phi-harmonic sequence.
        
        Args:
            n: Length of sequence
            
        Returns:
            Phi-harmonic sequence
        """
        sequence = [1.0, PHI]
        
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
        
        return sequence
    
    def _generate_phi_matrix(self, rows: int, cols: int) -> np.ndarray:
        """Generate a phi-harmonic matrix.
        
        Args:
            rows: Number of rows
            cols: Number of columns
            
        Returns:
            Phi-harmonic matrix
        """
        matrix = np.zeros((rows, cols))
        
        for i in range(rows):
            for j in range(cols):
                matrix[i, j] = PHI ** ((i + j) / (rows + cols))
        
        return matrix


if __name__ == "__main__":
    # Simple test
    strategy = PhiHarmonicAllocationStrategy()
    
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
    
    result = strategy.distribute(test_task, test_nodes)
    print(json.dumps(result, indent=2))
    
    optimized_result = strategy.optimize_distribution(result)
    print(json.dumps(optimized_result, indent=2))
