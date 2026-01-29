#!/usr/bin/env python3
"""
Quantum Tensor Capability Matcher
--------------------------------

This module implements a multi-dimensional tensor-based capability matching strategy
for task distribution in the QuantumAI nodular blockchain system. It uses tensor
representations of node capabilities and task requirements for optimal matching.

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
logger = logging.getLogger("TensorCapabilityMatcher")

class TensorCapabilityMatcher(DistributionStrategy):
    """Multi-dimensional tensor-based capability matching strategy."""
    
    def __init__(self):
        """Initialize the tensor capability matcher."""
        super().__init__("Tensor Capability Matcher")
        self.capability_dimensions = [
            "processing_power",
            "memory",
            "coherence",
            "quantum_capability",
            "healing_capability",
            "evolution_capability"
        ]
        self.task_dimensions = [
            "complexity",
            "memory_requirement",
            "coherence_requirement",
            "quantum_requirement",
            "healing_requirement",
            "evolution_requirement"
        ]
        self.dimension_weights = {
            "processing_power": PHI,
            "memory": 1.0,
            "coherence": PHI ** 2,
            "quantum_capability": PHI / 2,
            "healing_capability": 1.0,
            "evolution_capability": 1.0
        }
        self.phi_tensor = self._generate_phi_tensor([3, 3, 3])
        logger.info(f"Initialized Tensor Capability Matcher with ID: {self.strategy_id}")
    
    def distribute(self, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Distribute a task to nodes using tensor capability matching.
        
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
        
        # Extract task tensor
        task_tensor = self._extract_task_tensor(task)
        
        # Extract node tensors
        node_tensors = [self._extract_node_tensor(node) for node in nodes]
        
        # Calculate matching scores
        matching_scores = [
            self._calculate_tensor_match(task_tensor, node_tensor)
            for node_tensor in node_tensors
        ]
        
        # Select nodes based on matching scores
        selected_nodes = self._select_nodes(nodes, matching_scores)
        
        # Calculate task distribution
        task_distribution = self._calculate_task_distribution(task, selected_nodes)
        
        # Calculate coherence using quantum coherence calculator
        coherence = self.calculate_coherence({
            "task": task,
            "selected_nodes": selected_nodes,
            "task_distribution": task_distribution,
            "all_nodes": nodes
        })
        
        distribution_result = {
            "success": True,
            "task_id": task.get("task_id", str(uuid.uuid4())),
            "assigned_nodes": selected_nodes,
            "task_distribution": task_distribution,
            "coherence": coherence,
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
        
        # Calculate coherence using the quantum coherence calculator
        coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
            task, all_nodes, selected_nodes
        )
        
        return coherence
    
    def optimize_distribution(self, distribution_result: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize a distribution result for maximum coherence using the quantum coherence calculator.
        
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
        
        if not assigned_nodes:
            return distribution_result
            
        # If all_nodes is not provided, use assigned_nodes
        if not all_nodes:
            all_nodes = assigned_nodes
        
        # Use quantum coherence calculator to optimize node selection
        optimized_nodes = QuantumCoherenceCalculator.optimize_node_selection(
            task, all_nodes, assigned_nodes
        )
        
        # Calculate task distribution
        task_distribution = self._calculate_task_distribution(task, optimized_nodes)
        
        # Calculate coherence
        coherence = self.calculate_coherence({
            "task": task,
            "selected_nodes": optimized_nodes,
            "task_distribution": task_distribution,
            "all_nodes": all_nodes
        })
        
        optimized_result = {
            "success": True,
            "task_id": distribution_result.get("task_id"),
            "assigned_nodes": optimized_nodes,
            "task_distribution": task_distribution,
            "coherence": coherence,
            "all_nodes": all_nodes,
            "timestamp": datetime.datetime.now().isoformat(),
            "optimized": True
        }
        
        return optimized_result
    
    def _extract_task_tensor(self, task: Dict[str, Any]) -> np.ndarray:
        """Extract tensor representation of a task.
        
        Args:
            task: Task to analyze
            
        Returns:
            Task tensor
        """
        # Extract task parameters
        action = task.get("action", "")
        parameters = task.get("parameters", {})
        
        # Initialize tensor
        tensor = np.zeros(len(self.task_dimensions))
        
        # Set complexity
        complexity = self._calculate_task_complexity(task)
        tensor[0] = complexity
        
        # Set memory requirement
        memory_requirement = 0.5  # Default
        if "memory_requirement" in parameters:
            memory_requirement = parameters["memory_requirement"]
        elif action in ["process_file", "analyze_code", "optimize_code"]:
            # Estimate memory requirement based on action
            memory_requirement = {
                "process_file": 0.7,
                "analyze_code": 0.8,
                "optimize_code": 0.9,
                "heal_code": 0.8,
                "evolve_code": 0.9
            }.get(action, 0.5)
        tensor[1] = memory_requirement
        
        # Set coherence requirement
        coherence_requirement = TARGET_COHERENCE  # Default
        if "coherence_requirement" in parameters:
            coherence_requirement = parameters["coherence_requirement"]
        elif action in ["heal_code", "evolve_code"]:
            # Higher coherence for healing and evolution
            coherence_requirement = TARGET_COHERENCE * 1.1
        tensor[2] = coherence_requirement
        
        # Set quantum requirement
        quantum_requirement = 0.5  # Default
        if "quantum_requirement" in parameters:
            quantum_requirement = parameters["quantum_requirement"]
        elif action in ["optimize_code", "evolve_code"]:
            # Higher quantum requirement for optimization and evolution
            quantum_requirement = 0.8
        tensor[3] = quantum_requirement
        
        # Set healing requirement
        healing_requirement = 0.0  # Default
        if "healing_requirement" in parameters:
            healing_requirement = parameters["healing_requirement"]
        elif action == "heal_code":
            healing_requirement = 1.0
        tensor[4] = healing_requirement
        
        # Set evolution requirement
        evolution_requirement = 0.0  # Default
        if "evolution_requirement" in parameters:
            evolution_requirement = parameters["evolution_requirement"]
        elif action == "evolve_code":
            evolution_requirement = 1.0
        tensor[5] = evolution_requirement
        
        return tensor
    
    def _extract_node_tensor(self, node: Dict[str, Any]) -> np.ndarray:
        """Extract tensor representation of a node.
        
        Args:
            node: Node to analyze
            
        Returns:
            Node tensor
        """
        # Extract node capabilities
        capabilities = node.get("capabilities", {})
        
        # Initialize tensor
        tensor = np.zeros(len(self.capability_dimensions))
        
        # Set processing power
        tensor[0] = capabilities.get("processing_power", 0.5)
        
        # Set memory
        tensor[1] = capabilities.get("memory", 0.5)
        
        # Set coherence
        tensor[2] = capabilities.get("coherence", TARGET_COHERENCE) / TARGET_COHERENCE
        
        # Set quantum capability
        tensor[3] = capabilities.get("quantum_capability", 0.5)
        
        # Set healing capability
        tensor[4] = capabilities.get("healing_capability", 0.5)
        
        # Set evolution capability
        tensor[5] = capabilities.get("evolution_capability", 0.5)
        
        return tensor
    
    def _calculate_tensor_match(self, task_tensor: np.ndarray, node_tensor: np.ndarray) -> float:
        """Calculate matching score between task and node tensors.
        
        Args:
            task_tensor: Task tensor
            node_tensor: Node tensor
            
        Returns:
            Matching score
        """
        # Apply dimension weights
        weighted_task_tensor = np.zeros_like(task_tensor)
        weighted_node_tensor = np.zeros_like(node_tensor)
        
        for i, dim in enumerate(self.task_dimensions):
            weight = self.dimension_weights.get(self.capability_dimensions[i], 1.0)
            weighted_task_tensor[i] = task_tensor[i] * weight
            weighted_node_tensor[i] = node_tensor[i] * weight
        
        # Calculate cosine similarity
        dot_product = np.sum(weighted_task_tensor * weighted_node_tensor)
        task_norm = np.sqrt(np.sum(weighted_task_tensor ** 2))
        node_norm = np.sqrt(np.sum(weighted_node_tensor ** 2))
        
        if task_norm == 0 or node_norm == 0:
            return 0
        
        cosine_similarity = dot_product / (task_norm * node_norm)
        
        # Calculate capability satisfaction
        capability_satisfaction = np.mean(np.maximum(0, weighted_node_tensor - weighted_task_tensor))
        
        # Calculate phi-harmonic match score
        match_score = (cosine_similarity + capability_satisfaction) / 2
        
        # Apply phi-harmonic scaling
        phi_scaled_score = match_score * (1 + (PHI - 1) * (match_score ** 2))
        
        return phi_scaled_score
    
    def _select_nodes(self, nodes: List[Dict[str, Any]], matching_scores: List[float]) -> List[Dict[str, Any]]:
        """Select nodes based on matching scores.
        
        Args:
            nodes: Available nodes
            matching_scores: Matching scores
            
        Returns:
            Selected nodes
        """
        n_nodes = len(nodes)
        
        # Calculate number of nodes to select
        n_select = max(1, int(math.ceil(n_nodes / PHI)))
        
        # Get indices of top matching scores
        top_indices = np.argsort(matching_scores)[-n_select:]
        
        # Select nodes
        selected_nodes = []
        for i in top_indices:
            node = nodes[i].copy()
            node["matching_score"] = matching_scores[i]
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
        
        # Calculate matching scores
        matching_scores = [node.get("matching_score", 0.5) for node in selected_nodes]
        
        # Normalize matching scores
        total_score = sum(matching_scores)
        if total_score > 0:
            normalized_scores = [score / total_score for score in matching_scores]
        else:
            normalized_scores = [1.0 / n_nodes] * n_nodes
        
        # Create task distribution
        task_distribution = []
        
        for i, node in enumerate(selected_nodes):
            # Calculate tensor subtask parameters
            subtask_params = self._calculate_subtask_parameters(task, normalized_scores[i], i, n_nodes)
            
            # Create subtask
            subtask = {
                "node_id": node.get("node_id"),
                "reference_id": node.get("reference_id"),
                "allocation_factor": normalized_scores[i],
                "subtask_params": subtask_params
            }
            
            task_distribution.append(subtask)
        
        return task_distribution
    
    def _optimize_tensor_matching(self, task_tensor: np.ndarray, node_tensors: List[np.ndarray], nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Optimize tensor matching for maximum coherence.
        
        Args:
            task_tensor: Task tensor
            node_tensors: Node tensors
            nodes: Selected nodes
            
        Returns:
            Optimized nodes
        """
        n_nodes = len(nodes)
        
        if n_nodes == 0:
            return []
        
        # Calculate optimal weights using tensor decomposition
        weights = np.zeros(n_nodes)
        
        # Create task-node tensor
        task_node_tensor = np.zeros((n_nodes, len(task_tensor)))
        for i, node_tensor in enumerate(node_tensors):
            task_node_tensor[i] = node_tensor
        
        # Calculate tensor decomposition
        try:
            # Use SVD for tensor decomposition
            U, S, Vt = np.linalg.svd(task_node_tensor, full_matrices=False)
            
            # Project task tensor onto principal components
            task_projection = task_tensor @ Vt.T
            
            # Calculate weights based on projection
            for i in range(n_nodes):
                node_projection = U[i] * S
                weights[i] = np.sum(node_projection * task_projection) / np.sum(node_projection ** 2)
        except:
            # Fallback to simple matching
            for i, node_tensor in enumerate(node_tensors):
                weights[i] = self._calculate_tensor_match(task_tensor, node_tensor)
        
        # Apply phi-harmonic scaling
        phi_weights = np.zeros(n_nodes)
        for i in range(n_nodes):
            phi_weights[i] = weights[i] * (PHI ** (-(i % 3)))
        
        # Normalize weights
        total_weight = np.sum(phi_weights)
        if total_weight > 0:
            phi_weights = phi_weights / total_weight
        else:
            phi_weights = np.ones(n_nodes) / n_nodes
        
        # Update nodes with optimized weights
        optimized_nodes = []
        for i, node in enumerate(nodes):
            node_copy = node.copy()
            node_copy["matching_score"] = float(phi_weights[i])
            optimized_nodes.append(node_copy)
        
        return optimized_nodes
    
    def _calculate_subtask_parameters(self, task: Dict[str, Any], allocation_factor: float, node_index: int, n_nodes: int) -> Dict[str, Any]:
        """Calculate tensor subtask parameters.
        
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
    
    def _generate_phi_tensor(self, shape: List[int]) -> np.ndarray:
        """Generate a phi-harmonic tensor.
        
        Args:
            shape: Tensor shape
            
        Returns:
            Phi-harmonic tensor
        """
        # Create tensor
        tensor = np.zeros(shape)
        
        # Fill tensor with phi-harmonic values
        indices = np.indices(shape)
        sum_indices = np.sum(indices, axis=0)
        
        for idx in np.ndindex(*shape):
            tensor[idx] = PHI ** (sum_indices[idx] / np.sum(shape))
        
        return tensor


if __name__ == "__main__":
    # Simple test
    strategy = TensorCapabilityMatcher()
    
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
                "coherence": TARGET_COHERENCE * (0.9 + 0.1 * math.sin(i * PHI)),
                "quantum_capability": 0.6 + 0.4 * math.sin(i * PHI),
                "healing_capability": 0.5 + 0.5 * math.cos(i * PHI),
                "evolution_capability": 0.7 + 0.3 * math.sin(i * PHI + math.pi/4)
            }
        }
        for i in range(5)
    ]
    
    result = strategy.distribute(test_task, test_nodes)
    print(json.dumps(result, indent=2))
    
    optimized_result = strategy.optimize_distribution(result)
    print(json.dumps(optimized_result, indent=2))
