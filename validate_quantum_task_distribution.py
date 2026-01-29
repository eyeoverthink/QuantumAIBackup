#!/usr/bin/env python3
"""
Quantum Task Distribution Validation
-----------------------------------

This script validates and benchmarks the AGI-level task distribution system
for the QuantumAI nodular blockchain system.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import json
import time
import math
import random
import logging
import datetime
import numpy as np
from typing import Dict, List, Any, Optional, Tuple, Union, Callable

# Import the task distributor
from quantum_agi_task_distributor import (
    QuantumAGITaskDistributor, 
    DistributionStrategy,
    TARGET_COHERENCE,
    PHI,
    PHI_POWERS
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("TaskDistributionValidation")

class ValidationResult:
    """Class to store validation results."""
    
    def __init__(self):
        """Initialize validation results."""
        self.strategy_results = {}
        self.task_results = {}
        self.overall_results = {
            "total_tasks": 0,
            "successful_tasks": 0,
            "average_coherence": 0.0,
            "average_distribution_time": 0.0,
            "phi_harmonic_resonance": 0.0
        }
    
    def add_strategy_result(self, strategy_name: str, result: Dict[str, Any]):
        """Add a strategy result.
        
        Args:
            strategy_name: Name of the strategy
            result: Strategy result
        """
        if strategy_name not in self.strategy_results:
            self.strategy_results[strategy_name] = {
                "tasks": 0,
                "successful_tasks": 0,
                "coherence_values": [],
                "distribution_times": []
            }
        
        self.strategy_results[strategy_name]["tasks"] += 1
        
        if result.get("success", False):
            self.strategy_results[strategy_name]["successful_tasks"] += 1
            
            coherence = result.get("coherence", 0.0)
            self.strategy_results[strategy_name]["coherence_values"].append(coherence)
            
            distribution_time = result.get("distribution_time", 0.0)
            self.strategy_results[strategy_name]["distribution_times"].append(distribution_time)
    
    def add_task_result(self, task_type: str, result: Dict[str, Any]):
        """Add a task result.
        
        Args:
            task_type: Type of task
            result: Task result
        """
        if task_type not in self.task_results:
            self.task_results[task_type] = {
                "tasks": 0,
                "successful_tasks": 0,
                "coherence_values": [],
                "distribution_times": []
            }
        
        self.task_results[task_type]["tasks"] += 1
        
        if result.get("success", False):
            self.task_results[task_type]["successful_tasks"] += 1
            
            coherence = result.get("coherence", 0.0)
            self.task_results[task_type]["coherence_values"].append(coherence)
            
            distribution_time = result.get("distribution_time", 0.0)
            self.task_results[task_type]["distribution_times"].append(distribution_time)
    
    def update_overall_results(self):
        """Update overall results."""
        total_tasks = 0
        successful_tasks = 0
        coherence_values = []
        distribution_times = []
        
        for strategy_result in self.strategy_results.values():
            total_tasks += strategy_result["tasks"]
            successful_tasks += strategy_result["successful_tasks"]
            coherence_values.extend(strategy_result["coherence_values"])
            distribution_times.extend(strategy_result["distribution_times"])
        
        self.overall_results["total_tasks"] = total_tasks
        self.overall_results["successful_tasks"] = successful_tasks
        
        if coherence_values:
            self.overall_results["average_coherence"] = sum(coherence_values) / len(coherence_values)
        
        if distribution_times:
            self.overall_results["average_distribution_time"] = sum(distribution_times) / len(distribution_times)
        
        # Calculate phi-harmonic resonance
        if coherence_values:
            avg_coherence = sum(coherence_values) / len(coherence_values)
            phi_resonance = 1.0 - abs((avg_coherence / TARGET_COHERENCE) - 1.0)
            self.overall_results["phi_harmonic_resonance"] = phi_resonance
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate validation report.
        
        Returns:
            Validation report
        """
        self.update_overall_results()
        
        # Process strategy results
        strategy_reports = {}
        for strategy_name, result in self.strategy_results.items():
            coherence_values = result["coherence_values"]
            distribution_times = result["distribution_times"]
            
            strategy_reports[strategy_name] = {
                "tasks": result["tasks"],
                "successful_tasks": result["successful_tasks"],
                "success_rate": result["successful_tasks"] / result["tasks"] if result["tasks"] > 0 else 0.0,
                "average_coherence": sum(coherence_values) / len(coherence_values) if coherence_values else 0.0,
                "max_coherence": max(coherence_values) if coherence_values else 0.0,
                "min_coherence": min(coherence_values) if coherence_values else 0.0,
                "average_distribution_time": sum(distribution_times) / len(distribution_times) if distribution_times else 0.0
            }
        
        # Process task results
        task_reports = {}
        for task_type, result in self.task_results.items():
            coherence_values = result["coherence_values"]
            distribution_times = result["distribution_times"]
            
            task_reports[task_type] = {
                "tasks": result["tasks"],
                "successful_tasks": result["successful_tasks"],
                "success_rate": result["successful_tasks"] / result["tasks"] if result["tasks"] > 0 else 0.0,
                "average_coherence": sum(coherence_values) / len(coherence_values) if coherence_values else 0.0,
                "max_coherence": max(coherence_values) if coherence_values else 0.0,
                "min_coherence": min(coherence_values) if coherence_values else 0.0,
                "average_distribution_time": sum(distribution_times) / len(distribution_times) if distribution_times else 0.0
            }
        
        # Generate report
        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "overall_results": self.overall_results,
            "strategy_results": strategy_reports,
            "task_results": task_reports
        }
        
        return report


class TaskDistributionValidator:
    """Validator for quantum task distribution."""
    
    def __init__(self):
        """Initialize the validator."""
        self.distributor = QuantumAGITaskDistributor()
        self.distributor.initialize()
        self.validation_result = ValidationResult()
        self.strategies = list(self.distributor.strategies.keys())
        self.task_types = ["process_file", "analyze_code", "optimize_code", "heal_code", "evolve_code"]
        logger.info("Initialized TaskDistributionValidator")
    
    def generate_test_task(self, task_type: str) -> Dict[str, Any]:
        """Generate a test task.
        
        Args:
            task_type: Type of task
            
        Returns:
            Test task
        """
        task = {
            "action": task_type,
            "task_id": f"test-{task_type}-{int(time.time())}",
            "timestamp": datetime.datetime.now().isoformat(),
            "parameters": {}
        }
        
        if task_type == "process_file":
            task["parameters"]["file_path"] = f"test_{random.randint(1, 100)}.py"
        
        elif task_type in ["analyze_code", "optimize_code", "heal_code", "evolve_code"]:
            task["parameters"]["code_files"] = [
                f"test_{random.randint(1, 100)}.py"
                for _ in range(random.randint(1, 5))
            ]
        
        return task
    
    def generate_test_nodes(self, n_nodes: int) -> List[Dict[str, Any]]:
        """Generate test nodes.
        
        Args:
            n_nodes: Number of nodes
            
        Returns:
            Test nodes
        """
        nodes = []
        
        for i in range(n_nodes):
            # Generate phi-harmonic coherence value
            coherence_factor = 0.9 + 0.2 * math.sin(i * PHI)
            coherence = TARGET_COHERENCE * coherence_factor
            
            node = {
                "node_id": f"node-{i}",
                "reference_id": f"ref-{i}",
                "capabilities": {
                    "processing_power": 0.8 + 0.2 * math.sin(i),
                    "memory": 0.7 + 0.3 * math.cos(i),
                    "coherence": coherence,
                    "quantum_capability": 0.6 + 0.4 * math.sin(i * PHI),
                    "healing_capability": 0.5 + 0.5 * math.cos(i * PHI),
                    "evolution_capability": 0.7 + 0.3 * math.sin(i * PHI + math.pi/4)
                }
            }
            
            nodes.append(node)
        
        return nodes
    
    def validate_strategy(self, strategy_name: str, n_tasks: int = 10, n_nodes: int = 10):
        """Validate a distribution strategy.
        
        Args:
            strategy_name: Name of the strategy
            n_tasks: Number of tasks to test
            n_nodes: Number of nodes to test with
        """
        logger.info(f"Validating strategy: {strategy_name}")
        
        # Set meta-strategy
        self.distributor.set_meta_strategy(strategy_name)
        
        # Generate test nodes
        nodes = self.generate_test_nodes(n_nodes)
        
        # Override node discovery
        self.distributor._discover_nodes = lambda node_type: nodes
        
        # Test each task type
        for task_type in self.task_types:
            for _ in range(n_tasks // len(self.task_types) + 1):
                # Generate test task
                task = self.generate_test_task(task_type)
                
                # Distribute task
                start_time = time.time()
                result = self.distributor.distribute_task(task)
                distribution_time = time.time() - start_time
                
                # Add distribution time
                result["distribution_time"] = distribution_time
                
                # Record result
                self.validation_result.add_strategy_result(strategy_name, result)
                self.validation_result.add_task_result(task_type, result)
                
                logger.info(f"Task {task['task_id']} distributed with coherence: {result.get('coherence', 0.0):.6f}")
    
    def validate_all_strategies(self, n_tasks: int = 50, n_nodes: int = 10):
        """Validate all distribution strategies.
        
        Args:
            n_tasks: Number of tasks to test per strategy
            n_nodes: Number of nodes to test with
        """
        logger.info("Validating all strategies")
        
        for strategy_name in self.strategies:
            self.validate_strategy(strategy_name, n_tasks, n_nodes)
    
    def generate_validation_report(self) -> Dict[str, Any]:
        """Generate validation report.
        
        Returns:
            Validation report
        """
        return self.validation_result.generate_report()
    
    def save_validation_report(self, report: Dict[str, Any], filename: str = None):
        """Save validation report to file.
        
        Args:
            report: Validation report
            filename: Output filename
        """
        if filename is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"task_distribution_validation_{timestamp}.json"
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)
        
        with open(filename, "w") as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Validation report saved to: {filename}")


def main():
    """Main function."""
    # Create validator
    validator = TaskDistributionValidator()
    
    # Validate all strategies
    validator.validate_all_strategies(n_tasks=50, n_nodes=10)
    
    # Generate and save report
    report = validator.generate_validation_report()
    validator.save_validation_report(report, "data/task_distribution_validation.json")
    
    # Print summary
    print("\nValidation Summary:")
    print(f"Total Tasks: {report['overall_results']['total_tasks']}")
    print(f"Successful Tasks: {report['overall_results']['successful_tasks']}")
    print(f"Success Rate: {report['overall_results']['successful_tasks'] / report['overall_results']['total_tasks']:.2%}")
    print(f"Average Coherence: {report['overall_results']['average_coherence']:.6f}")
    print(f"Target Coherence: {TARGET_COHERENCE:.6f}")
    print(f"Phi-Harmonic Resonance: {report['overall_results']['phi_harmonic_resonance']:.6f}")
    print(f"Average Distribution Time: {report['overall_results']['average_distribution_time']:.6f} seconds")
    
    print("\nStrategy Results:")
    for strategy_name, result in report["strategy_results"].items():
        print(f"\n{strategy_name}:")
        print(f"  Success Rate: {result['success_rate']:.2%}")
        print(f"  Average Coherence: {result['average_coherence']:.6f}")
        print(f"  Max Coherence: {result['max_coherence']:.6f}")
        print(f"  Min Coherence: {result['min_coherence']:.6f}")
        print(f"  Average Distribution Time: {result['average_distribution_time']:.6f} seconds")


if __name__ == "__main__":
    main()
