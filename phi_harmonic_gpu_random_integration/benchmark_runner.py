#!/usr/bin/env python
"""
Phi-Harmonic GPU Random Integration Benchmark: Main Runner

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
from dimensional_scaling_benchmark import DimensionalScalingBenchmark

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(current_dir, 'benchmark.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('phi_harmonic_gpu_random_benchmark')

class PhiHarmonicGPURandomBenchmark:
    """Main benchmark runner for the Phi-Harmonic GPU Random Integration Benchmark."""
    
    def __init__(self):
        """Initialize the benchmark runner."""
        # Create output directory
        self.output_dir = os.path.join(current_dir, 'results')
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize benchmark modules
        self.dimensional_benchmark = DimensionalScalingBenchmark()
        
        # Initialize results
        self.results = {
            "timestamp": time.time(),
            "dimensional_scaling": {},
            "summary": {}
        }
        
        logger.info("Phi-Harmonic GPU Random Integration Benchmark initialized")
    
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
                "dimensional_scaling": {
                    "dimensions_range": [2, 3, 4, 5],
                    "vertex_count": 500
                }
            }
        
        logger.info("Running all benchmarks...")
        logger.info(f"Configuration: {json.dumps(config, indent=2)}")
        
        # Run dimensional scaling benchmark
        logger.info("Running Dimensional Scaling Benchmark...")
        dim_config = config.get("dimensional_scaling", {})
        self.results["dimensional_scaling"] = self.dimensional_benchmark.run_benchmark(
            dimensions_range=dim_config.get("dimensions_range", [2, 3, 4, 5]),
            vertex_count=dim_config.get("vertex_count", 500)
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
            "dimensional_scaling": {},
            "overall": {}
        }
        
        # Summarize dimensional scaling
        if self.results["dimensional_scaling"]:
            dim_results = self.results["dimensional_scaling"]
            
            # Extract key metrics
            if "advantage_analysis" in dim_results and "best_combination" in dim_results["advantage_analysis"]:
                best = dim_results["advantage_analysis"]["best_combination"]
                summary["dimensional_scaling"] = {
                    "best_combination": best["key"],
                    "advantage": best["advantage"],
                    "phi_power_equivalent": best["phi_power_equivalent"]
                }
        
        # Overall summary
        summary["overall"] = {
            "timestamp": time.time(),
            "benchmarks_run": ["dimensional_scaling"],
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
    
    def generate_report(self):
        """
        Generate a comprehensive benchmark report.
        
        Returns:
            Path to report file
        """
        logger.info("Generating benchmark report...")
        
        # Create report
        report = {
            "title": "Phi-Harmonic GPU Random Integration Benchmark Report",
            "timestamp": time.time(),
            "summary": self.results["summary"],
            "details": {
                "dimensional_scaling": self.results["dimensional_scaling"]
            }
        }
        
        # Save report to file
        report_path = os.path.join(self.output_dir, 'benchmark_report.json')
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        logger.info(f"Report saved to {report_path}")
        
        return report_path

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Phi-Harmonic GPU Random Integration Benchmark')
    
    parser.add_argument('--dimensions', type=str, default='2,3,4,5', help='Dimensions for benchmark (comma-separated)')
    parser.add_argument('--vertices', type=int, default=500, help='Number of vertices for benchmark')
    
    return parser.parse_args()

def main():
    """Main function for running the benchmark."""
    # Parse arguments
    args = parse_args()
    
    # Create benchmark runner
    benchmark = PhiHarmonicGPURandomBenchmark()
    
    # Configure benchmarks
    config = {
        "dimensional_scaling": {
            "dimensions_range": [int(d) for d in args.dimensions.split(',')],
            "vertex_count": args.vertices
        }
    }
    
    # Run benchmarks
    benchmark.run_all_benchmarks(config)
    
    # Generate report
    benchmark.generate_report()
    
    logger.info("Benchmark completed")

if __name__ == "__main__":
    main()
