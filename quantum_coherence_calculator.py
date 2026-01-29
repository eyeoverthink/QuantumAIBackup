#!/usr/bin/env python3
"""
Quantum Coherence Calculator
---------------------------

Module for calculating phi-harmonic coherence in quantum task distribution.
This module implements advanced coherence calculation algorithms based on
phi-harmonic principles and quantum resonance patterns.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import math
import numpy as np
from typing import Dict, List, Any, Optional, Tuple, Union

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


class QuantumCoherenceCalculator:
    """Calculator for quantum phi-harmonic coherence."""
    
    @staticmethod
    def calculate_phi_resonance(value: float) -> float:
        """Calculate phi resonance of a value.
        
        Args:
            value: Input value
            
        Returns:
            Phi resonance value between 0 and 1
        """
        # Calculate resonance as proximity to a multiple of phi
        resonance = abs((value / PHI) % 1)
        if resonance > 0.5:
            resonance = 1 - resonance
        
        # Scale to 0-1 range
        resonance = 1 - (resonance * 2)
        return resonance
    
    @staticmethod
    def calculate_distribution_coherence(
        task: Dict[str, Any],
        nodes: List[Dict[str, Any]],
        assigned_nodes: List[Dict[str, Any]]
    ) -> float:
        """Calculate coherence of a task distribution.
        
        Args:
            task: Task being distributed
            nodes: All available nodes
            assigned_nodes: Nodes assigned to the task
            
        Returns:
            Coherence value
        """
        if not assigned_nodes:
            return 0.0
        
        # Calculate base coherence from node capabilities
        capability_coherence = QuantumCoherenceCalculator._calculate_capability_coherence(
            task, assigned_nodes
        )
        
        # Calculate distribution pattern coherence
        pattern_coherence = QuantumCoherenceCalculator._calculate_pattern_coherence(
            assigned_nodes, nodes
        )
        
        # Calculate quantum resonance coherence
        resonance_coherence = QuantumCoherenceCalculator._calculate_resonance_coherence(
            task, assigned_nodes
        )
        
        # Calculate phi-harmonic balance
        phi_balance = QuantumCoherenceCalculator._calculate_phi_balance(
            assigned_nodes
        )
        
        # Combine coherence components with phi-weighted average
        coherence = (
            capability_coherence * PHI_POWERS["φ"] +
            pattern_coherence * PHI_POWERS["φ²"] / 10 +
            resonance_coherence * PHI_POWERS["φ³"] / 100 +
            phi_balance * PHI_POWERS["φ⁴"] / 1000
        ) / (
            PHI_POWERS["φ"] +
            PHI_POWERS["φ²"] / 10 +
            PHI_POWERS["φ³"] / 100 +
            PHI_POWERS["φ⁴"] / 1000
        )
        
        return coherence
    
    @staticmethod
    def _calculate_capability_coherence(
        task: Dict[str, Any],
        assigned_nodes: List[Dict[str, Any]]
    ) -> float:
        """Calculate coherence based on node capabilities.
        
        Args:
            task: Task being distributed
            assigned_nodes: Nodes assigned to the task
            
        Returns:
            Capability coherence value
        """
        if not assigned_nodes:
            return 0.0
        
        # Extract task requirements
        task_requirements = task.get("requirements", {})
        if not task_requirements:
            # Default requirements if not specified
            task_requirements = {
                "processing_power": 0.5,
                "memory": 0.5,
                "quantum_capability": 0.5,
                "healing_capability": 0.5,
                "evolution_capability": 0.5
            }
        
        # Calculate capability match for each node
        capability_matches = []
        for node in assigned_nodes:
            node_capabilities = node.get("capabilities", {})
            if not node_capabilities:
                continue
            
            # Calculate match for each requirement
            requirement_matches = []
            for req_name, req_value in task_requirements.items():
                if req_name in node_capabilities:
                    # Calculate match as 1 - normalized difference
                    match = 1 - abs(node_capabilities[req_name] - req_value)
                    requirement_matches.append(match)
            
            if requirement_matches:
                # Calculate phi-weighted average of requirement matches
                weights = [PHI ** (-(i+1)) for i in range(len(requirement_matches))]
                weight_sum = sum(weights)
                capability_match = sum(m * w for m, w in zip(requirement_matches, weights)) / weight_sum
                capability_matches.append(capability_match)
        
        if not capability_matches:
            return 0.0
        
        # Calculate phi-weighted average of capability matches
        weights = [PHI ** (-(i+1)) for i in range(len(capability_matches))]
        weight_sum = sum(weights)
        capability_coherence = sum(m * w for m, w in zip(capability_matches, weights)) / weight_sum
        
        # Scale to target coherence
        capability_coherence *= TARGET_COHERENCE
        
        return capability_coherence
    
    @staticmethod
    def _calculate_pattern_coherence(
        assigned_nodes: List[Dict[str, Any]],
        all_nodes: List[Dict[str, Any]]
    ) -> float:
        """Calculate coherence based on distribution pattern.
        
        Args:
            assigned_nodes: Nodes assigned to the task
            all_nodes: All available nodes
            
        Returns:
            Pattern coherence value
        """
        if not assigned_nodes or not all_nodes:
            return 0.0
        
        # Calculate distribution ratio
        distribution_ratio = len(assigned_nodes) / len(all_nodes)
        
        # Calculate phi resonance of distribution ratio
        resonance = QuantumCoherenceCalculator.calculate_phi_resonance(distribution_ratio)
        
        # Calculate node selection pattern coherence
        node_indices = [all_nodes.index(node) for node in assigned_nodes if node in all_nodes]
        if not node_indices:
            return resonance * TARGET_COHERENCE
        
        # Calculate differences between consecutive indices
        diffs = [node_indices[i+1] - node_indices[i] for i in range(len(node_indices)-1)]
        if not diffs:
            return resonance * TARGET_COHERENCE
        
        # Calculate phi resonance of differences
        diff_resonances = [QuantumCoherenceCalculator.calculate_phi_resonance(diff) for diff in diffs]
        avg_diff_resonance = sum(diff_resonances) / len(diff_resonances)
        
        # Combine resonances
        pattern_coherence = (resonance + avg_diff_resonance) / 2
        
        # Scale to target coherence
        pattern_coherence *= TARGET_COHERENCE
        
        return pattern_coherence
    
    @staticmethod
    def _calculate_resonance_coherence(
        task: Dict[str, Any],
        assigned_nodes: List[Dict[str, Any]]
    ) -> float:
        """Calculate coherence based on quantum resonance.
        
        Args:
            task: Task being distributed
            assigned_nodes: Nodes assigned to the task
            
        Returns:
            Resonance coherence value
        """
        if not assigned_nodes:
            return 0.0
        
        # Extract task ID
        task_id = task.get("task_id", "")
        if not task_id:
            return 0.0
        
        # Calculate task ID hash value
        task_hash = sum(ord(c) for c in task_id)
        
        # Calculate node ID hash values
        node_hashes = []
        for node in assigned_nodes:
            node_id = node.get("node_id", "")
            if node_id:
                node_hash = sum(ord(c) for c in node_id)
                node_hashes.append(node_hash)
        
        if not node_hashes:
            return 0.0
        
        # Calculate resonance between task and nodes
        resonances = []
        for node_hash in node_hashes:
            # Calculate resonance as phi-modulated XOR
            xor_value = task_hash ^ node_hash
            resonance = QuantumCoherenceCalculator.calculate_phi_resonance(xor_value)
            resonances.append(resonance)
        
        # Calculate average resonance
        avg_resonance = sum(resonances) / len(resonances)
        
        # Scale to target coherence
        resonance_coherence = avg_resonance * TARGET_COHERENCE
        
        return resonance_coherence
    
    @staticmethod
    def _calculate_phi_balance(assigned_nodes: List[Dict[str, Any]]) -> float:
        """Calculate coherence based on phi-harmonic balance.
        
        Args:
            assigned_nodes: Nodes assigned to the task
            
        Returns:
            Phi balance coherence value
        """
        if not assigned_nodes:
            return 0.0
        
        # Check if number of nodes is a Fibonacci number
        def is_fibonacci(n):
            phi = PHI
            a = phi * n
            return n == 0 or abs(round(a) - a) < 1e-10
        
        # Calculate base balance based on number of nodes
        n_nodes = len(assigned_nodes)
        if is_fibonacci(n_nodes):
            base_balance = 1.0
        else:
            # Find closest Fibonacci numbers
            fib_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
            closest_fib = min(fib_seq, key=lambda x: abs(x - n_nodes))
            base_balance = 1.0 - abs(n_nodes - closest_fib) / max(n_nodes, closest_fib)
        
        # Calculate coherence values of nodes
        node_coherences = []
        for node in assigned_nodes:
            node_coherence = node.get("capabilities", {}).get("coherence", 0.0)
            node_coherences.append(node_coherence)
        
        if not node_coherences:
            return base_balance * TARGET_COHERENCE
        
        # Calculate standard deviation of coherence values
        std_dev = np.std(node_coherences) if len(node_coherences) > 1 else 0.0
        
        # Calculate balance as inverse of normalized standard deviation
        if sum(node_coherences) > 0:
            normalized_std_dev = std_dev / (sum(node_coherences) / len(node_coherences))
            coherence_balance = 1.0 / (1.0 + normalized_std_dev)
        else:
            coherence_balance = 0.0
        
        # Combine base balance and coherence balance
        phi_balance = (base_balance + coherence_balance) / 2
        
        # Scale to target coherence
        phi_balance *= TARGET_COHERENCE
        
        return phi_balance
    
    @staticmethod
    def optimize_node_selection(
        task: Dict[str, Any],
        nodes: List[Dict[str, Any]],
        initial_selection: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Optimize node selection for maximum coherence.
        
        Args:
            task: Task being distributed
            nodes: All available nodes
            initial_selection: Initial node selection
            
        Returns:
            Optimized node selection
        """
        if not nodes:
            return []
        
        # Start with initial selection
        best_selection = initial_selection.copy()
        best_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
            task, nodes, best_selection
        )
        
        # Try to improve coherence by swapping nodes
        for _ in range(min(10, len(nodes))):  # Limit iterations for performance
            improved = False
            
            # Try adding a node
            if len(best_selection) < len(nodes):
                for node in nodes:
                    if node not in best_selection:
                        new_selection = best_selection + [node]
                        new_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
                            task, nodes, new_selection
                        )
                        
                        if new_coherence > best_coherence:
                            best_selection = new_selection
                            best_coherence = new_coherence
                            improved = True
                            break
            
            # Try removing a node
            if len(best_selection) > 1 and not improved:
                for i in range(len(best_selection)):
                    new_selection = best_selection[:i] + best_selection[i+1:]
                    new_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
                        task, nodes, new_selection
                    )
                    
                    if new_coherence > best_coherence:
                        best_selection = new_selection
                        best_coherence = new_coherence
                        improved = True
                        break
            
            # Try swapping a node
            if not improved:
                for i in range(len(best_selection)):
                    for node in nodes:
                        if node not in best_selection:
                            new_selection = best_selection.copy()
                            new_selection[i] = node
                            new_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
                                task, nodes, new_selection
                            )
                            
                            if new_coherence > best_coherence:
                                best_selection = new_selection
                                best_coherence = new_coherence
                                improved = True
                                break
                    
                    if improved:
                        break
            
            # Stop if no improvement
            if not improved:
                break
        
        return best_selection


# Simple test
if __name__ == "__main__":
    # Create test task
    task = {
        "task_id": "test-task-1",
        "action": "process_file",
        "requirements": {
            "processing_power": 0.8,
            "memory": 0.7,
            "quantum_capability": 0.9,
            "healing_capability": 0.5,
            "evolution_capability": 0.6
        }
    }
    
    # Create test nodes
    nodes = [
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
        for i in range(10)
    ]
    
    # Calculate coherence for different node selections
    initial_selection = nodes[:3]
    initial_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
        task, nodes, initial_selection
    )
    print(f"Initial coherence: {initial_coherence:.6f}")
    
    # Optimize node selection
    optimized_selection = QuantumCoherenceCalculator.optimize_node_selection(
        task, nodes, initial_selection
    )
    optimized_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
        task, nodes, optimized_selection
    )
    print(f"Optimized coherence: {optimized_coherence:.6f}")
    print(f"Target coherence: {TARGET_COHERENCE:.6f}")
    
    # Calculate phi resonance
    resonance = QuantumCoherenceCalculator.calculate_phi_resonance(optimized_coherence)
    print(f"Phi resonance: {resonance:.6f}")
