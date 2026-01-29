#!/usr/bin/env python3
"""
Quantum Adaptive Distribution Learner
-----------------------------------

This module implements an adaptive learning system for task distribution
in the QuantumAI nodular blockchain system. It learns from past distribution
results to improve future task allocation decisions.

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
logger = logging.getLogger("AdaptiveDistributionLearner")

class AdaptiveDistributionLearner(DistributionStrategy):
    """Adaptive learning system for task distribution."""
    
    def __init__(self, history_file: str = None):
        """Initialize the adaptive distribution learner.
        
        Args:
            history_file: Path to distribution history file
        """
        super().__init__("Adaptive Learner")
        self.history_file = history_file or os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data",
            "distribution_history.json"
        )
        self.history = self._load_history()
        self.feature_extractors = self._initialize_feature_extractors()
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 0.2
        self.weights = self._initialize_weights()
        self.recent_distributions = []
        self.max_recent_distributions = int(PHI * 10)  # ≈ 16
        logger.info(f"Initialized Adaptive Distribution Learner with ID: {self.strategy_id}")
    
    def distribute(self, task: Dict[str, Any], nodes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Distribute a task to nodes using adaptive learning and quantum coherence.
        
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
        
        # Extract features
        task_features = self._extract_task_features(task)
        node_features = [self._extract_node_features(node) for node in nodes]
        
        # Decide whether to explore or exploit
        if random.random() < self.exploration_rate:
            # Exploration: try a random distribution
            selected_nodes = self._explore_distribution(nodes)
        else:
            # Exploitation: use learned weights
            selected_nodes = self._exploit_distribution(task_features, node_features, nodes)
        
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
            "timestamp": datetime.datetime.now().isoformat(),
            "task_features": task_features,
            "exploration": random.random() < self.exploration_rate
        }
        
        # Store distribution for learning
        self._store_distribution(distribution_result)
        
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
        base_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
            task, all_nodes, selected_nodes
        )
        
        # Apply adaptive learning factor
        learning_factor = 1.0 + self.learning_rate * math.log(1 + len(self.history))
        
        # Calculate final coherence with learning factor
        adaptive_coherence = base_coherence * learning_factor
        
        return adaptive_coherence
    
    def optimize_distribution(self, distribution_result: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize a distribution result based on learned patterns and quantum coherence.
        
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
        
        # First apply learned optimizations
        task_features = distribution_result.get("task_features") or self._extract_task_features(task)
        node_features = [self._extract_node_features(node) for node in assigned_nodes]
        learned_optimized_nodes = self._apply_learned_optimizations(task_features, node_features, assigned_nodes)
        
        # Then use quantum coherence calculator for further optimization
        optimized_nodes = QuantumCoherenceCalculator.optimize_node_selection(
            task, all_nodes, learned_optimized_nodes
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
    
    def learn_from_feedback(self, distribution_result: Dict[str, Any], feedback: Dict[str, Any]) -> None:
        """Learn from feedback on a distribution result.
        
        Args:
            distribution_result: Distribution result
            feedback: Feedback on the distribution
        """
        if not distribution_result.get("success"):
            return
        
        # Extract reward from feedback
        reward = feedback.get("reward", 0.0)
        
        # Update weights based on reward
        self._update_weights(distribution_result, reward)
        
        # Update history
        distribution_entry = {
            "task_id": distribution_result.get("task_id"),
            "timestamp": datetime.datetime.now().isoformat(),
            "coherence": distribution_result.get("coherence", 0.0),
            "reward": reward,
            "feedback": feedback
        }
        
        self.history.append(distribution_entry)
        
        # Save history
        self._save_history()
        
        # Update exploration rate
        self._update_exploration_rate()
        
        logger.info(f"Learned from feedback for task {distribution_result.get('task_id')}, reward: {reward}")
    
    def _initialize_feature_extractors(self) -> Dict[str, Callable]:
        """Initialize feature extractors.
        
        Returns:
            Dictionary of feature extractors
        """
        return {
            "task_complexity": lambda task: self._calculate_task_complexity(task),
            "task_memory": lambda task: task.get("parameters", {}).get("memory_requirement", 0.5),
            "task_coherence": lambda task: task.get("parameters", {}).get("coherence_requirement", TARGET_COHERENCE) / TARGET_COHERENCE,
            "task_quantum": lambda task: task.get("parameters", {}).get("quantum_requirement", 0.5),
            "task_healing": lambda task: 1.0 if task.get("action") == "heal_code" else 0.0,
            "task_evolution": lambda task: 1.0 if task.get("action") == "evolve_code" else 0.0,
            "node_processing": lambda node: node.get("capabilities", {}).get("processing_power", 0.5),
            "node_memory": lambda node: node.get("capabilities", {}).get("memory", 0.5),
            "node_coherence": lambda node: node.get("capabilities", {}).get("coherence", TARGET_COHERENCE) / TARGET_COHERENCE,
            "node_quantum": lambda node: node.get("capabilities", {}).get("quantum_capability", 0.5),
            "node_healing": lambda node: node.get("capabilities", {}).get("healing_capability", 0.5),
            "node_evolution": lambda node: node.get("capabilities", {}).get("evolution_capability", 0.5)
        }
    
    def _initialize_weights(self) -> Dict[str, float]:
        """Initialize weights for features.
        
        Returns:
            Dictionary of weights
        """
        weights = {}
        
        # Task-node feature weights
        for task_feature in ["task_complexity", "task_memory", "task_coherence", "task_quantum", "task_healing", "task_evolution"]:
            for node_feature in ["node_processing", "node_memory", "node_coherence", "node_quantum", "node_healing", "node_evolution"]:
                key = f"{task_feature}_{node_feature}"
                
                # Initialize with phi-harmonic values
                if task_feature.replace("task_", "") == node_feature.replace("node_", ""):
                    # Matching features get higher weight
                    weights[key] = PHI
                else:
                    # Non-matching features get lower weight
                    weights[key] = 1.0 / PHI
        
        # Node selection weights
        weights["node_count"] = 1.0 / PHI
        weights["node_diversity"] = PHI - 1.0
        
        return weights
    
    def _extract_task_features(self, task: Dict[str, Any]) -> Dict[str, float]:
        """Extract features from a task.
        
        Args:
            task: Task to analyze
            
        Returns:
            Task features
        """
        features = {}
        
        for name, extractor in self.feature_extractors.items():
            if name.startswith("task_"):
                try:
                    features[name] = extractor(task)
                except:
                    features[name] = 0.0
        
        return features
    
    def _extract_node_features(self, node: Dict[str, Any]) -> Dict[str, float]:
        """Extract features from a node.
        
        Args:
            node: Node to analyze
            
        Returns:
            Node features
        """
        features = {}
        
        for name, extractor in self.feature_extractors.items():
            if name.startswith("node_"):
                try:
                    features[name] = extractor(node)
                except:
                    features[name] = 0.0
        
        return features
    
    def _explore_distribution(self, nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Explore a random distribution.
        
        Args:
            nodes: Available nodes
            
        Returns:
            Selected nodes
        """
        n_nodes = len(nodes)
        
        # Select a random number of nodes
        n_select = max(1, int(random.uniform(1, n_nodes / PHI)))
        
        # Select random nodes
        selected_indices = random.sample(range(n_nodes), n_select)
        
        # Create selected nodes list
        selected_nodes = []
        for i in selected_indices:
            node = nodes[i].copy()
            node["selection_weight"] = random.uniform(0.5, 1.0)
            selected_nodes.append(node)
        
        return selected_nodes
    
    def _exploit_distribution(self, task_features: Dict[str, float], node_features: List[Dict[str, float]], nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Exploit learned weights for distribution.
        
        Args:
            task_features: Task features
            node_features: Node features
            nodes: Available nodes
            
        Returns:
            Selected nodes
        """
        n_nodes = len(nodes)
        
        # Calculate node scores
        node_scores = []
        
        for i, node_feature in enumerate(node_features):
            score = 0.0
            
            # Calculate weighted feature match
            for task_name, task_value in task_features.items():
                for node_name, node_value in node_feature.items():
                    weight_key = f"{task_name}_{node_name}"
                    if weight_key in self.weights:
                        score += self.weights[weight_key] * task_value * node_value
            
            node_scores.append(score)
        
        # Normalize scores
        max_score = max(node_scores) if node_scores else 1.0
        if max_score > 0:
            normalized_scores = [score / max_score for score in node_scores]
        else:
            normalized_scores = [1.0 / n_nodes] * n_nodes
        
        # Calculate number of nodes to select
        n_select = max(1, int(math.ceil(n_nodes / (PHI * (1 + self.weights["node_count"])))))
        
        # Select top nodes
        top_indices = np.argsort(normalized_scores)[-n_select:]
        
        # Create selected nodes list
        selected_nodes = []
        for i in top_indices:
            node = nodes[i].copy()
            node["selection_weight"] = normalized_scores[i]
            selected_nodes.append(node)
        
        return selected_nodes
    
    def _apply_learned_optimizations(self, task_features: Dict[str, float], node_features: List[Dict[str, float]], nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply learned optimizations to node selection.
        
        Args:
            task_features: Task features
            node_features: Node features
            nodes: Selected nodes
            
        Returns:
            Optimized nodes
        """
        n_nodes = len(nodes)
        
        if n_nodes == 0:
            return []
        
        # Find similar historical distributions
        similar_distributions = self._find_similar_distributions(task_features)
        
        if not similar_distributions:
            # No similar distributions found, return original nodes
            return nodes
        
        # Calculate optimal weights based on similar distributions
        weights = np.zeros(n_nodes)
        
        for i, node_feature in enumerate(node_features):
            weight = 0.0
            
            # Calculate feature-based weight
            for task_name, task_value in task_features.items():
                for node_name, node_value in node_feature.items():
                    weight_key = f"{task_name}_{node_name}"
                    if weight_key in self.weights:
                        weight += self.weights[weight_key] * task_value * node_value
            
            weights[i] = weight
        
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
            node_copy["selection_weight"] = float(phi_weights[i])
            optimized_nodes.append(node_copy)
        
        return optimized_nodes
    
    def _find_similar_distributions(self, task_features: Dict[str, float]) -> List[Dict[str, Any]]:
        """Find similar historical distributions.
        
        Args:
            task_features: Task features
            
        Returns:
            Similar distributions
        """
        similar_distributions = []
        
        for entry in self.history:
            if "task_features" not in entry:
                continue
            
            # Calculate similarity
            similarity = 0.0
            count = 0
            
            for name, value in task_features.items():
                if name in entry["task_features"]:
                    similarity += 1.0 - abs(value - entry["task_features"][name])
                    count += 1
            
            if count > 0:
                similarity /= count
                
                # Add if similar enough
                if similarity > 0.8:
                    entry["similarity"] = similarity
                    similar_distributions.append(entry)
        
        # Sort by similarity
        similar_distributions.sort(key=lambda x: x.get("similarity", 0.0), reverse=True)
        
        # Return top similar distributions
        return similar_distributions[:int(PHI * 5)]
    
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
            # Calculate adaptive subtask parameters
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
    
    def _calculate_subtask_parameters(self, task: Dict[str, Any], allocation_factor: float, node_index: int, n_nodes: int) -> Dict[str, Any]:
        """Calculate adaptive subtask parameters.
        
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
    
    def _store_distribution(self, distribution_result: Dict[str, Any]) -> None:
        """Store a distribution result for learning.
        
        Args:
            distribution_result: Distribution result
        """
        # Add to recent distributions
        self.recent_distributions.append(distribution_result)
        
        # Limit recent distributions
        if len(self.recent_distributions) > self.max_recent_distributions:
            self.recent_distributions.pop(0)
    
    def _update_weights(self, distribution_result: Dict[str, Any], reward: float) -> None:
        """Update weights based on reward.
        
        Args:
            distribution_result: Distribution result
            reward: Reward value
        """
        # Skip if no task features
        if "task_features" not in distribution_result:
            return
        
        task_features = distribution_result["task_features"]
        
        # Extract node features
        node_features = []
        for node in distribution_result.get("assigned_nodes", []):
            node_features.append(self._extract_node_features(node))
        
        # Update weights
        for task_name, task_value in task_features.items():
            for node_feature in node_features:
                for node_name, node_value in node_feature.items():
                    weight_key = f"{task_name}_{node_name}"
                    
                    if weight_key in self.weights:
                        # Calculate weight update
                        update = self.learning_rate * reward * task_value * node_value
                        
                        # Apply update
                        self.weights[weight_key] += update
        
        # Update node count weight
        n_nodes = len(distribution_result.get("assigned_nodes", []))
        n_total = distribution_result.get("n_total_nodes", n_nodes)
        
        if n_total > 0:
            node_ratio = n_nodes / n_total
            optimal_ratio = 1.0 / PHI
            
            # Update node count weight
            update = self.learning_rate * reward * (1.0 - abs(node_ratio - optimal_ratio))
            self.weights["node_count"] += update
        
        # Update node diversity weight
        if n_nodes > 1:
            # Calculate diversity
            diversity = 0.0
            count = 0
            
            for i in range(len(node_features)):
                for j in range(i + 1, len(node_features)):
                    # Calculate feature distance
                    distance = 0.0
                    feature_count = 0
                    
                    for name in node_features[i]:
                        if name in node_features[j]:
                            distance += abs(node_features[i][name] - node_features[j][name])
                            feature_count += 1
                    
                    if feature_count > 0:
                        diversity += distance / feature_count
                        count += 1
            
            if count > 0:
                diversity /= count
                
                # Update diversity weight
                update = self.learning_rate * reward * diversity
                self.weights["node_diversity"] += update
    
    def _update_exploration_rate(self) -> None:
        """Update exploration rate based on learning progress."""
        # Calculate average reward
        rewards = [entry.get("reward", 0.0) for entry in self.history[-100:]]
        
        if rewards:
            avg_reward = sum(rewards) / len(rewards)
            
            # Adjust exploration rate
            if avg_reward > 0.8:
                # Good performance, reduce exploration
                self.exploration_rate = max(0.05, self.exploration_rate * 0.95)
            elif avg_reward < 0.3:
                # Poor performance, increase exploration
                self.exploration_rate = min(0.5, self.exploration_rate * 1.05)
    
    def _load_history(self) -> List[Dict[str, Any]]:
        """Load distribution history.
        
        Returns:
            Distribution history
        """
        if not os.path.exists(self.history_file):
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
            return []
        
        try:
            with open(self.history_file, "r") as f:
                return json.load(f)
        except:
            return []
    
    def _save_history(self) -> None:
        """Save distribution history."""
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        
        try:
            with open(self.history_file, "w") as f:
                json.dump(self.history, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save history: {e}")


if __name__ == "__main__":
    # Simple test
    learner = AdaptiveDistributionLearner()
    
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
    
    # First distribution
    result = learner.distribute(test_task, test_nodes)
    print(json.dumps(result, indent=2))
    
    # Provide feedback
    learner.learn_from_feedback(result, {"reward": 0.8, "message": "Good distribution"})
    
    # Second distribution
    result2 = learner.distribute(test_task, test_nodes)
    print(json.dumps(result2, indent=2))
    
    # Optimize distribution
    optimized_result = learner.optimize_distribution(result2)
    print(json.dumps(optimized_result, indent=2))
