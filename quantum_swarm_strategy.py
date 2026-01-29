#!/usr/bin/env python3
"""
Quantum Swarm Strategy
---------------------

This module implements a quantum swarm intelligence strategy for task distribution
in the QuantumAI nodular blockchain system. It combines quantum computing principles
with swarm intelligence to enable self-organizing task distribution.

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
import random
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
logger = logging.getLogger("QuantumSwarmStrategy")

class QuantumSwarmStrategy(DistributionStrategy):
    """Quantum swarm intelligence strategy for task distribution."""
    
    def __init__(self):
        """Initialize the quantum swarm strategy."""
        super().__init__("Quantum Swarm")
        self.swarm_size = 20
        self.max_iterations = 50
        self.phi_inertia = 0.7
        self.phi_cognitive = PHI - 1  # ≈ 0.618034
        self.phi_social = PHI  # ≈ 1.618034
        self.best_positions = {}
        logger.info(f"Initialized Quantum Swarm Strategy with ID: {self.strategy_id}")
    
    def distribute(self, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Distribute a task to nodes using quantum swarm intelligence.
        
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
        
        # Initialize swarm
        swarm = self._initialize_swarm(task, nodes)
        
        # Run swarm optimization
        best_solution = self._run_swarm_optimization(swarm, task, nodes)
        
        # Extract selected nodes from best solution
        selected_nodes = self._extract_selected_nodes(best_solution, nodes)
        
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
        """Calculate the coherence of a distribution result.
        
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
        
        if not selected_nodes or not all_nodes:
            return 0.0
        
        # Calculate coherence using the quantum coherence calculator
        coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
            task, all_nodes, selected_nodes
        )
        
        return coherence
    
    def optimize_distribution(self, distribution_result: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize a distribution result for maximum coherence.
        
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
        
        if not assigned_nodes or not all_nodes:
            return distribution_result
        
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
    
    def _initialize_swarm(self, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Initialize quantum swarm particles.
        
        Args:
            task: Task to distribute
            nodes: Available nodes
            
        Returns:
            Initialized swarm
        """
        n_nodes = len(nodes)
        swarm = []
        
        for i in range(self.swarm_size):
            # Initialize particle position (binary vector indicating selected nodes)
            position = np.zeros(n_nodes)
            
            # Randomly select nodes
            n_select = max(1, int(math.ceil(n_nodes * PHI / (PHI + 1))))
            selected_indices = random.sample(range(n_nodes), n_select)
            position[selected_indices] = 1
            
            # Initialize particle velocity
            velocity = np.random.uniform(-0.1, 0.1, n_nodes)
            
            # Initialize particle
            particle = {
                "position": position,
                "velocity": velocity,
                "fitness": 0.0,
                "best_position": position.copy(),
                "best_fitness": 0.0
            }
            
            # Evaluate particle fitness
            particle["fitness"] = self._evaluate_fitness(particle["position"], task, nodes)
            particle["best_fitness"] = particle["fitness"]
            
            swarm.append(particle)
        
        return swarm
    
    def _run_swarm_optimization(self, swarm: List[Dict[str, Any]], task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> np.ndarray:
        """Run quantum swarm optimization.
        
        Args:
            swarm: Initialized swarm
            task: Task to distribute
            nodes: Available nodes
            
        Returns:
            Best solution found
        """
        # Initialize global best
        global_best_position = None
        global_best_fitness = -float('inf')
        
        # Find initial global best
        for particle in swarm:
            if particle["fitness"] > global_best_fitness:
                global_best_fitness = particle["fitness"]
                global_best_position = particle["position"].copy()
        
        # Run optimization iterations
        for iteration in range(self.max_iterations):
            # Update each particle
            for particle in swarm:
                # Update velocity
                cognitive_component = self.phi_cognitive * np.random.random() * (particle["best_position"] - particle["position"])
                social_component = self.phi_social * np.random.random() * (global_best_position - particle["position"])
                particle["velocity"] = self.phi_inertia * particle["velocity"] + cognitive_component + social_component
                
                # Apply quantum effects
                self._apply_quantum_effects(particle)
                
                # Update position
                particle["position"] = particle["position"] + particle["velocity"]
                
                # Binarize position
                particle["position"] = self._binarize_position(particle["position"])
                
                # Evaluate fitness
                particle["fitness"] = self._evaluate_fitness(particle["position"], task, nodes)
                
                # Update particle best
                if particle["fitness"] > particle["best_fitness"]:
                    particle["best_fitness"] = particle["fitness"]
                    particle["best_position"] = particle["position"].copy()
                
                # Update global best
                if particle["fitness"] > global_best_fitness:
                    global_best_fitness = particle["fitness"]
                    global_best_position = particle["position"].copy()
            
            # Apply phi-harmonic swarm evolution
            if iteration % int(PHI * 10) == 0:
                self._phi_harmonic_swarm_evolution(swarm, global_best_position)
        
        # Store best position for this task
        task_id = task.get("task_id", str(uuid.uuid4()))
        self.best_positions[task_id] = global_best_position
        
        return global_best_position
    
    def _evaluate_fitness(self, position: np.ndarray, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> float:
        """Evaluate fitness of a particle position.
        
        Args:
            position: Particle position
            task: Task to distribute
            nodes: Available nodes
            
        Returns:
            Fitness value
        """
        # Get selected nodes
        selected_indices = np.where(position > 0.5)[0]
        
        if len(selected_indices) == 0:
            return 0.0
        
        selected_nodes = [nodes[i] for i in selected_indices]
        
        # Calculate task complexity
        task_complexity = self._calculate_task_complexity(task)
        
        # Calculate node capabilities
        node_capabilities = [
            self._calculate_node_capability(node)
            for node in selected_nodes
        ]
        
        # Calculate capability sum
        capability_sum = sum(node_capabilities)
        
        # Calculate coherence
        node_coherence_values = [
            node.get("capabilities", {}).get("coherence", TARGET_COHERENCE)
            for node in selected_nodes
        ]
        mean_coherence = sum(node_coherence_values) / len(node_coherence_values)
        
        # Calculate phi-harmonic distribution factor
        n_selected = len(selected_nodes)
        n_total = len(nodes)
        distribution_factor = 1.0 - abs((n_selected / n_total) - (1.0 / PHI))
        
        # Calculate fitness
        fitness = (
            capability_sum / task_complexity +
            mean_coherence / TARGET_COHERENCE +
            distribution_factor
        ) / 3.0
        
        return fitness
    
    def _apply_quantum_effects(self, particle: Dict[str, Any]):
        """Apply quantum effects to particle.
        
        Args:
            particle: Particle to update
        """
        # Quantum tunneling
        if random.random() < 0.1:
            # Randomly flip some bits
            n_flip = max(1, int(len(particle["position"]) / 10))
            flip_indices = random.sample(range(len(particle["position"])), n_flip)
            
            for idx in flip_indices:
                particle["position"][idx] = 1.0 - particle["position"][idx]
        
        # Quantum entanglement
        if random.random() < 0.05:
            # Entangle with best position
            entanglement_factor = random.random() * PHI
            particle["position"] = (
                (1.0 - entanglement_factor) * particle["position"] +
                entanglement_factor * particle["best_position"]
            )
    
    def _binarize_position(self, position: np.ndarray) -> np.ndarray:
        """Binarize particle position.
        
        Args:
            position: Particle position
            
        Returns:
            Binarized position
        """
        # Apply sigmoid function
        sigmoid = 1.0 / (1.0 + np.exp(-position))
        
        # Binarize
        binary = np.zeros_like(position)
        binary[sigmoid > 0.5] = 1.0
        
        # Ensure at least one node is selected
        if np.sum(binary) == 0:
            binary[np.argmax(sigmoid)] = 1.0
        
        return binary
    
    def _phi_harmonic_swarm_evolution(self, swarm: List[Dict[str, Any]], global_best_position: np.ndarray):
        """Apply phi-harmonic swarm evolution.
        
        Args:
            swarm: Swarm to evolve
            global_best_position: Global best position
        """
        # Sort particles by fitness
        swarm.sort(key=lambda p: p["fitness"], reverse=True)
        
        # Apply phi-harmonic evolution to bottom particles
        n_evolve = int(len(swarm) / PHI)
        
        for i in range(n_evolve):
            idx = len(swarm) - i - 1
            
            # Reset position with phi-harmonic influence
            swarm[idx]["position"] = (
                (1.0 / PHI) * global_best_position +
                (1.0 - 1.0 / PHI) * np.random.random(len(global_best_position))
            )
            
            # Binarize position
            swarm[idx]["position"] = self._binarize_position(swarm[idx]["position"])
            
            # Reset velocity
            swarm[idx]["velocity"] = np.random.uniform(-0.1, 0.1, len(global_best_position))
    
    def _extract_selected_nodes(self, position: np.ndarray, nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract selected nodes from position.
        
        Args:
            position: Binary position vector
            nodes: Available nodes
            
        Returns:
            Selected nodes
        """
        selected_indices = np.where(position > 0.5)[0]
        
        if len(selected_indices) == 0:
            # If no nodes selected, select the one with highest capability
            capabilities = [self._calculate_node_capability(node) for node in nodes]
            selected_indices = [np.argmax(capabilities)]
        
        selected_nodes = []
        for i in selected_indices:
            node = nodes[i].copy()
            node["selection_weight"] = float(position[i])
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
        
        # Calculate selection weights
        selection_weights = [node.get("selection_weight", 1.0) for node in selected_nodes]
        
        # Normalize weights
        total_weight = sum(selection_weights)
        if total_weight > 0:
            normalized_weights = [w / total_weight for w in selection_weights]
        else:
            normalized_weights = [1.0 / n_nodes] * n_nodes
        
        # Create task distribution
        task_distribution = []
        
        for i, node in enumerate(selected_nodes):
            # Calculate quantum subtask parameters
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
    
    def _quantum_annealing_optimization(self, nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Optimize node selection using quantum annealing.
        
        Args:
            nodes: Selected nodes
            
        Returns:
            Optimized nodes
        """
        # Sort nodes by coherence
        nodes.sort(
            key=lambda node: node.get("capabilities", {}).get("coherence", 0),
            reverse=True
        )
        
        # Calculate optimal weights using quantum annealing
        n_nodes = len(nodes)
        weights = np.zeros(n_nodes)
        
        # Initial temperature
        temperature = 1.0
        
        # Annealing iterations
        for i in range(100):
            # Calculate phi-harmonic weights
            for j in range(n_nodes):
                weights[j] = PHI ** (-(j+1))
            
            # Apply quantum fluctuations
            for j in range(n_nodes):
                if random.random() < temperature:
                    # Quantum flip
                    idx1 = j
                    idx2 = random.randint(0, n_nodes - 1)
                    weights[idx1], weights[idx2] = weights[idx2], weights[idx1]
            
            # Reduce temperature
            temperature *= 0.95
        
        # Normalize weights
        weights = weights / np.sum(weights)
        
        # Update nodes with optimized weights
        optimized_nodes = []
        for i, node in enumerate(nodes):
            node_copy = node.copy()
            node_copy["selection_weight"] = float(weights[i])
            optimized_nodes.append(node_copy)
        
        return optimized_nodes
    
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
    
    def _calculate_subtask_parameters(self, task: Dict[str, Any], allocation_factor: float, node_index: int, n_nodes: int) -> Dict[str, Any]:
        """Calculate quantum subtask parameters.
        
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


if __name__ == "__main__":
    # Simple test
    strategy = QuantumSwarmStrategy()
    
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
