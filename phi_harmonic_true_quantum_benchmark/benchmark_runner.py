#!/usr/bin/env python
"""
Phi-Harmonic True Quantum Benchmark: Main Runner

This module integrates all benchmark components and provides a unified interface
for running the complete benchmark suite.
"""

import os
import sys
import json
import time
import logging
import argparse
from pathlib import Path

# Add project root to path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)
sys.path.append(current_dir)

# Import benchmark modules
from random_generation_benchmark import RandomGenerationBenchmark
from hyper_dimensional_benchmark import HyperDimensionalBenchmark

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(current_dir, 'benchmark.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('phi_harmonic_benchmark')

class PhiHarmonicTrueQuantumBenchmark:
    """Main benchmark runner for the Phi-Harmonic True Quantum Benchmark."""
    
    def __init__(self):
        """Initialize the benchmark runner."""
        # Create output directory
        self.output_dir = os.path.join(current_dir, 'results')
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize benchmark modules
        self.random_benchmark = RandomGenerationBenchmark()
        self.hyper_benchmark = HyperDimensionalBenchmark()
        
        # Initialize results
        self.results = {
            "timestamp": time.time(),
            "random_generation": {},
            "hyper_dimensional": {},
            "summary": {}
        }
        
        logger.info("Phi-Harmonic True Quantum Benchmark initialized")
    
    def run_all_benchmarks(self, config=None):
        """
        Run all benchmarks with the specified configuration.
        
        Args:
            config: Dictionary of benchmark configuration parameters
            
        Returns:
            Dictionary of benchmark results
        """
        if config is None:
            config = {
                "random_generation": {
                    "sample_size": 10000,
                    "epochs": 3
                },
                "hyper_dimensional": {
                    "dimensions_range": [2, 3, 4, 5],
                    "size": 6
                }
            }
        
        logger.info("Running all benchmarks...")
        logger.info(f"Configuration: {json.dumps(config, indent=2)}")
        
        # Run random generation benchmark
        logger.info("Running Random Generation Benchmark...")
        random_config = config.get("random_generation", {})
        self.results["random_generation"] = self.random_benchmark.run_benchmark(
            sample_size=random_config.get("sample_size", 10000),
            epochs=random_config.get("epochs", 3)
        )
        
        # Run hyper-dimensional benchmark
        logger.info("Running Hyper-Dimensional Benchmark...")
        hyper_config = config.get("hyper_dimensional", {})
        self.results["hyper_dimensional"] = self.hyper_benchmark.run_benchmark(
            dimensions_range=hyper_config.get("dimensions_range", [2, 3, 4, 5]),
            size=hyper_config.get("size", 6)
        )
        
        # Generate summary
        self.generate_summary()
        
        # Save results
        self.save_results()
        
        logger.info("All benchmarks completed")
        
        return self.results
    
    def generate_summary(self):
        """Generate a summary of all benchmark results."""
        logger.info("Generating benchmark summary...")
        
        summary = {
            "random_generation": {},
            "hyper_dimensional": {},
            "overall": {}
        }
        
        # Summarize random generation
        if self.results["random_generation"]:
            random_results = self.results["random_generation"]
            
            # Extract key metrics
            adapter_entropy = random_results.get("adapter", {}).get("distribution", {}).get("entropy", 0)
            quantum_entropy = random_results.get("quantum", {}).get("distribution", {}).get("entropy", 0)
            
            adapter_uniformity = random_results.get("adapter", {}).get("uniformity", {}).get("ks_test", {}).get("uniform", False)
            quantum_uniformity = random_results.get("quantum", {}).get("uniformity", {}).get("ks_test", {}).get("uniform", False)
            
            # Summarize
            summary["random_generation"] = {
                "adapter_entropy": adapter_entropy,
                "quantum_entropy": quantum_entropy,
                "adapter_uniform": adapter_uniformity,
                "quantum_uniform": quantum_uniformity
            }
        
        # Summarize hyper-dimensional
        if self.results["hyper_dimensional"]:
            hyper_results = self.results["hyper_dimensional"]
            
            # Extract key metrics
            scaling = hyper_results.get("dimensional_scaling", {}).get("scaling", {})
            time_scaling = scaling.get("time_scaling", 1.0)
            phi_power = scaling.get("phi_power_equivalent", 0.0)
            
            # Summarize
            summary["hyper_dimensional"] = {
                "time_scaling": time_scaling,
                "phi_power_equivalent": phi_power
            }
        
        # Overall summary
        summary["overall"] = {
            "timestamp": time.time(),
            "benchmarks_run": ["random_generation", "hyper_dimensional"],
            "success": True
        }
        
        # Store summary
        self.results["summary"] = summary
        
        logger.info("Summary generated")
        
        return summary
    
    def save_results(self):
        """
        Save benchmark results to file.
        
        Returns:
            Path to results file
        """
        logger.info("Saving benchmark results...")
        
        # Save results to file
        results_path = os.path.join(self.output_dir, 'benchmark_results.json')
        with open(results_path, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)
        
        logger.info(f"Results saved to {results_path}")
        
        return results_path

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Phi-Harmonic True Quantum Benchmark')
    
    parser.add_argument('--random', action='store_true', help='Run random generation benchmark')
    parser.add_argument('--hyper', action='store_true', help='Run hyper-dimensional benchmark')
    parser.add_argument('--all', action='store_true', help='Run all benchmarks')
    
    parser.add_argument('--samples', type=int, default=10000, help='Number of samples for random benchmark')
    parser.add_argument('--epochs', type=int, default=3, help='Number of epochs for random benchmark')
    
    parser.add_argument('--dimensions', type=str, default='2,3,4,5', help='Dimensions for hyper benchmark (comma-separated)')
    parser.add_argument('--size', type=int, default=6, help='Size for hyper benchmark')
    
    return parser.parse_args()

def main():
    """Main function for running the benchmark."""
    # Parse arguments
    args = parse_args()
    
    # Create benchmark runner
    benchmark = PhiHarmonicTrueQuantumBenchmark()
    
    # Configure benchmarks
    config = {
        "random_generation": {
            "sample_size": args.samples,
            "epochs": args.epochs
        },
        "hyper_dimensional": {
            "dimensions_range": [int(d) for d in args.dimensions.split(',')],
            "size": args.size
        }
    }
    
    # Run benchmarks
    if args.all:
        benchmark.run_all_benchmarks(config)
    else:
        if args.random:
            benchmark.random_benchmark.run_benchmark(
                sample_size=config["random_generation"]["sample_size"],
                epochs=config["random_generation"]["epochs"]
            )
        
        if args.hyper:
            benchmark.hyper_benchmark.run_benchmark(
                dimensions_range=config["hyper_dimensional"]["dimensions_range"],
                size=config["hyper_dimensional"]["size"]
            )
    
    logger.info("Benchmark completed")

if __name__ == "__main__":
    main()
