#!/usr/bin/env python3
"""
Quantum Task Distribution Test Script
------------------------------------

This script tests and benchmarks the quantum coherence-aware task distribution system.
It validates all distribution strategies with the integrated quantum coherence calculator.
"""

import os
import sys
import json
import time
import uuid
import math
import random
import logging
import datetime
import numpy as np
from typing import Dict, List, Any, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumTaskDistributionTest")

# Import distribution strategies
try:
    from quantum_agi_task_distributor import QuantumAGITaskDistributor, TARGET_COHERENCE, PHI
    from quantum_swarm_strategy import QuantumSwarmStrategy
    from quantum_tensor_capability_matcher import TensorCapabilityMatcher
    from quantum_adaptive_distribution_learner import AdaptiveDistributionLearner
    from quantum_coherence_preserving_balancer import CoherencePreservingBalancer
    from quantum_coherence_calculator import QuantumCoherenceCalculator
except ImportError as e:
    logger.error(f"Import error: {e}")
    sys.exit(1)

def generate_test_nodes(n_nodes: int = 10) -> List[Dict[str, Any]]:
    """Generate test nodes with varying capabilities.
    
    Args:
        n_nodes: Number of nodes to generate
        
    Returns:
        List of test nodes
    """
    nodes = []
    
    for i in range(n_nodes):
        # Generate phi-harmonic capability values
        processing_power = 0.5 + 0.5 * math.sin(i * PHI)
        memory = 0.5 + 0.5 * math.cos(i * PHI)
        coherence = TARGET_COHERENCE * (0.8 + 0.4 * math.sin(i * PHI / 2))
        quantum_capability = 0.5 + 0.5 * math.sin(i * PHI / 3)
        healing_capability = 0.5 + 0.5 * math.cos(i * PHI / 4)
        evolution_capability = 0.5 + 0.5 * math.sin(i * PHI / 5)
        
        # Create node
        node = {
            "node_id": str(uuid.uuid4()),
            "reference_id": f"node_{i}",
            "capabilities": {
                "processing_power": processing_power,
                "memory": memory,
                "coherence": coherence,
                "quantum_capability": quantum_capability,
                "healing_capability": healing_capability,
                "evolution_capability": evolution_capability
            },
            "status": "active",
            "last_active": datetime.datetime.now().isoformat()
        }
        
        nodes.append(node)
    
    return nodes

def generate_test_tasks(n_tasks: int = 5) -> List[Dict[str, Any]]:
    """Generate test tasks with varying requirements.
    
    Args:
        n_tasks: Number of tasks to generate
        
    Returns:
        List of test tasks
    """
    tasks = []
    
    actions = [
        "process_file",
        "analyze_code",
        "optimize_code",
        "heal_code",
        "evolve_code"
    ]
    
    for i in range(n_tasks):
        # Select action
        action = actions[i % len(actions)]
        
        # Generate phi-harmonic requirement values
        complexity = 0.5 + 0.5 * math.sin(i * PHI)
        memory_requirement = 0.5 + 0.5 * math.cos(i * PHI)
        coherence_requirement = TARGET_COHERENCE * (0.9 + 0.2 * math.sin(i * PHI / 2))
        quantum_requirement = 0.5 + 0.5 * math.sin(i * PHI / 3)
        healing_requirement = 1.0 if action == "heal_code" else 0.2 + 0.3 * math.cos(i * PHI / 4)
        evolution_requirement = 1.0 if action == "evolve_code" else 0.2 + 0.3 * math.sin(i * PHI / 5)
        
        # Create task
        task = {
            "task_id": str(uuid.uuid4()),
            "action": action,
            "parameters": {
                "complexity": complexity,
                "memory_requirement": memory_requirement,
                "coherence_requirement": coherence_requirement,
                "quantum_requirement": quantum_requirement,
                "healing_requirement": healing_requirement,
                "evolution_requirement": evolution_requirement,
                "file_path": f"/path/to/test/file_{i}.py",
                "target_coherence": TARGET_COHERENCE
            },
            "priority": 0.5 + 0.5 * math.sin(i * PHI / 6),
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        tasks.append(task)
    
    return tasks

def test_distribution_strategy(strategy_name: str, strategy, tasks: List[Dict[str, Any]], nodes: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Test a distribution strategy with the given tasks and nodes.
    
    Args:
        strategy_name: Name of the strategy
        strategy: Distribution strategy instance
        tasks: List of tasks to distribute
        nodes: List of nodes to distribute to
        
    Returns:
        Test results
    """
    logger.info(f"Testing {strategy_name}...")
    
    results = []
    coherence_values = []
    execution_times = []
    
    for task in tasks:
        # Measure execution time
        start_time = time.time()
        
        # Distribute task
        distribution_result = strategy.distribute(task, nodes)
        
        # Optimize distribution
        optimized_result = strategy.optimize_distribution(distribution_result)
        
        # Record execution time
        execution_time = time.time() - start_time
        execution_times.append(execution_time)
        
        # Record coherence
        coherence = optimized_result.get("coherence", 0)
        coherence_values.append(coherence)
        
        # Record result
        result = {
            "task_id": task.get("task_id"),
            "action": task.get("action"),
            "coherence": coherence,
            "execution_time": execution_time,
            "n_assigned_nodes": len(optimized_result.get("assigned_nodes", [])),
            "optimized": optimized_result.get("optimized", False)
        }
        
        results.append(result)
        
        logger.info(f"Task {task.get('action')} distributed with coherence: {coherence:.6f}, execution time: {execution_time:.6f}s")
    
    # Calculate statistics
    mean_coherence = sum(coherence_values) / len(coherence_values) if coherence_values else 0
    max_coherence = max(coherence_values) if coherence_values else 0
    min_coherence = min(coherence_values) if coherence_values else 0
    mean_execution_time = sum(execution_times) / len(execution_times) if execution_times else 0
    
    # Calculate phi-harmonic coherence ratio
    phi_harmonic_ratio = mean_coherence / TARGET_COHERENCE
    
    test_result = {
        "strategy": strategy_name,
        "mean_coherence": mean_coherence,
        "max_coherence": max_coherence,
        "min_coherence": min_coherence,
        "phi_harmonic_ratio": phi_harmonic_ratio,
        "mean_execution_time": mean_execution_time,
        "results": results
    }
    
    logger.info(f"{strategy_name} test completed. Mean coherence: {mean_coherence:.6f}, Phi-harmonic ratio: {phi_harmonic_ratio:.6f}")
    
    return test_result

def run_benchmark():
    """Run benchmark tests for all distribution strategies."""
    logger.info("Starting quantum task distribution benchmark...")
    
    # Generate test data
    n_nodes = 20
    n_tasks = 10
    
    nodes = generate_test_nodes(n_nodes)
    tasks = generate_test_tasks(n_tasks)
    
    logger.info(f"Generated {n_nodes} test nodes and {n_tasks} test tasks")
    
    # Initialize strategies
    strategies = {
        "Quantum Swarm Strategy": QuantumSwarmStrategy(),
        "Tensor Capability Matcher": TensorCapabilityMatcher(),
        "Adaptive Distribution Learner": AdaptiveDistributionLearner(),
        "Coherence Preserving Balancer": CoherencePreservingBalancer()
    }
    
    # Test each strategy
    benchmark_results = {}
    
    for name, strategy in strategies.items():
        benchmark_results[name] = test_distribution_strategy(name, strategy, tasks, nodes)
    
    # Compare results
    logger.info("Benchmark results:")
    logger.info("-" * 80)
    logger.info(f"{'Strategy':<30} {'Mean Coherence':<15} {'Phi-Harmonic Ratio':<20} {'Execution Time (s)':<15}")
    logger.info("-" * 80)
    
    for name, result in benchmark_results.items():
        logger.info(f"{name:<30} {result['mean_coherence']:<15.6f} {result['phi_harmonic_ratio']:<20.6f} {result['mean_execution_time']:<15.6f}")
    
    logger.info("-" * 80)
    
    # Save results
    results_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "data",
        f"distribution_benchmark_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(results_file), exist_ok=True)
    
    with open(results_file, "w") as f:
        json.dump(benchmark_results, f, indent=2)
    
    logger.info(f"Benchmark results saved to {results_file}")
    
    return benchmark_results

def test_quantum_coherence_calculator():
    """Test the quantum coherence calculator."""
    logger.info("Testing quantum coherence calculator...")
    
    # Generate test data
    nodes = generate_test_nodes(10)
    task = generate_test_tasks(1)[0]
    
    # Test system coherence calculation
    system_coherence = QuantumCoherenceCalculator.calculate_system_coherence(task, nodes)
    logger.info(f"System coherence: {system_coherence:.6f}")
    
    # Test distribution coherence calculation
    selected_nodes = nodes[:5]
    distribution_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
        task, nodes, selected_nodes
    )
    logger.info(f"Distribution coherence: {distribution_coherence:.6f}")
    
    # Test node selection optimization
    optimized_nodes = QuantumCoherenceCalculator.optimize_node_selection(
        task, nodes, selected_nodes
    )
    
    optimized_coherence = QuantumCoherenceCalculator.calculate_distribution_coherence(
        task, nodes, optimized_nodes
    )
    logger.info(f"Optimized coherence: {optimized_coherence:.6f}")
    
    # Compare coherence values
    logger.info(f"Coherence improvement: {optimized_coherence - distribution_coherence:.6f}")
    
    return {
        "system_coherence": system_coherence,
        "distribution_coherence": distribution_coherence,
        "optimized_coherence": optimized_coherence,
        "improvement": optimized_coherence - distribution_coherence
    }

def test_task_distributor():
    """Test the quantum AGI task distributor with all strategies."""
    logger.info("Testing quantum AGI task distributor...")
    
    # Generate test data
    nodes = generate_test_nodes(15)
    tasks = generate_test_tasks(5)
    
    # Initialize distributor with all strategies
    distributor = QuantumAGITaskDistributor()
    
    # Add all strategies
    distributor.add_strategy(QuantumSwarmStrategy())
    distributor.add_strategy(TensorCapabilityMatcher())
    distributor.add_strategy(AdaptiveDistributionLearner())
    distributor.add_strategy(CoherencePreservingBalancer())
    
    # Distribute tasks
    results = []
    
    for task in tasks:
        # Distribute task
        distribution_result = distributor.distribute_task(task, nodes)
        
        # Record result
        result = {
            "task_id": task.get("task_id"),
            "action": task.get("action"),
            "strategy": distribution_result.get("strategy_name"),
            "coherence": distribution_result.get("coherence", 0),
            "n_assigned_nodes": len(distribution_result.get("assigned_nodes", [])),
            "optimized": distribution_result.get("optimized", False)
        }
        
        results.append(result)
        
        logger.info(f"Task {task.get('action')} distributed using {result['strategy']} with coherence: {result['coherence']:.6f}")
    
    return results

if __name__ == "__main__":
    # Test quantum coherence calculator
    coherence_results = test_quantum_coherence_calculator()
    
    # Test task distributor
    distributor_results = test_task_distributor()
    
    # Run benchmark
    benchmark_results = run_benchmark()
    
    # Print summary
    logger.info("\nTest Summary:")
    logger.info("-" * 80)
    logger.info(f"Quantum Coherence Calculator:")
    logger.info(f"  - System Coherence: {coherence_results['system_coherence']:.6f}")
    logger.info(f"  - Distribution Coherence: {coherence_results['distribution_coherence']:.6f}")
    logger.info(f"  - Optimized Coherence: {coherence_results['optimized_coherence']:.6f}")
    logger.info(f"  - Improvement: {coherence_results['improvement']:.6f}")
    logger.info("-" * 80)
    
    # Print best strategy
    best_strategy = max(benchmark_results.items(), key=lambda x: x[1]["phi_harmonic_ratio"])
    logger.info(f"Best Strategy: {best_strategy[0]}")
    logger.info(f"  - Mean Coherence: {best_strategy[1]['mean_coherence']:.6f}")
    logger.info(f"  - Phi-Harmonic Ratio: {best_strategy[1]['phi_harmonic_ratio']:.6f}")
    logger.info("-" * 80)
