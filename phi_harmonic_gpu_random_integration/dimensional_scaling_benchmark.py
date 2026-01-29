#!/usr/bin/env python
"""
Phi-Harmonic GPU Random Integration Benchmark: Dimensional Scaling

This module implements the dimensional scaling benchmark for testing how
the Phi-Harmonic Quantum Random system enhances GPU performance across
different dimensional spaces.
"""

import os
import sys
import json
import time
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
import logging

# Add project root to path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)
sys.path.append(current_dir)

# Import benchmark core
from benchmark_core import PhiHarmonicGPURandomBenchmarkCore, PHI, PHI_POWER

# Get logger
logger = logging.getLogger('phi_harmonic_gpu_random_benchmark')

class DimensionalScalingBenchmark(PhiHarmonicGPURandomBenchmarkCore):
    """Benchmark for testing dimensional scaling of GPU with quantum random integration."""
    
    def __init__(self):
        """Initialize the dimensional scaling benchmark."""
        super().__init__()
        logger.info("Dimensional Scaling Benchmark initialized")
    
    def run_dimensional_scaling_test(self, dimensions_range, vertex_count=1000):
        """
        Run a dimensional scaling test.
        
        Args:
            dimensions_range: List of dimensions to test
            vertex_count: Number of vertices to generate
            
        Returns:
            Dictionary of test results
        """
        logger.info(f"Running dimensional scaling test with dimensions {dimensions_range} and {vertex_count} vertices...")
        
        # Initialize results
        results = {
            "dimensions": dimensions_range,
            "vertex_count": vertex_count,
            "generators": ["adapter", "quantum", "phi_harmonic", "standard"],
            "transformations": ["phi", "standard", "complex"],
            "performance": {}
        }
        
        # Initialize performance data for visualization
        performance_data = {}
        
        # Create all possible combinations of generators and transformations
        for generator in ["adapter", "quantum", "phi_harmonic", "standard"]:
            for transformation in ["phi", "standard", "complex"]:
                # Format generator name properly for visualization
                generator_display = generator.replace('_', '-').capitalize()
                key = f"{generator_display} + {transformation.capitalize()}"
                performance_data[key] = []
        
        # Run tests for each dimension
        for dimensions in dimensions_range:
            logger.info(f"\n=== Testing {dimensions} dimensions ===")
            
            dimension_results = {
                "generators": {},
                "coherence": {},
                "resonance": {}
            }
            
            # Test each generator
            for generator in ["adapter", "quantum", "phi_harmonic", "standard"]:
                logger.info(f"\n--- Testing {generator} generator ---")
                
                # Generate vertices
                vertices = self.generate_random_vertices(dimensions, vertex_count, generator)
                
                generator_results = {}
                
                # Test each transformation
                for transformation in ["phi", "standard", "complex"]:
                    logger.info(f"Testing {transformation} transformation...")
                    
                    # Transform vertices
                    _, duration, ops_per_second = self.transform_vertices(
                        vertices, dimensions, transformation
                    )
                    
                    # Record results
                    generator_results[transformation] = {
                        "duration": duration,
                        "ops_per_second": ops_per_second,
                        "coherence": float(self.gpu_transformer.coherence),
                        "resonance": float(self.gpu_transformer.resonance)
                    }
                    
                    # Add to performance data for visualization
                    # Format generator name properly for visualization
                    generator_display = generator.replace('_', '-').capitalize()
                    performance_data[f"{generator_display} + {transformation.capitalize()}"].append(
                        (dimensions, ops_per_second)
                    )
                
                # Record generator results
                dimension_results["generators"][generator] = generator_results
                
                # Record coherence and resonance
                dimension_results["coherence"][generator] = float(self.gpu_transformer.coherence)
                dimension_results["resonance"][generator] = float(self.gpu_transformer.resonance)
            
            # Record dimension results
            results["performance"][dimensions] = dimension_results
        
        # Visualize performance across dimensions
        viz_path = self.visualize_performance(
            performance_data,
            "Dimensions",
            "Operations per Second",
            "GPU Performance Across Dimensions",
            "dimensional_scaling_performance.png"
        )
        
        # Visualize coherence across dimensions
        coherence_data = {
            "Adapter": [(dim, results["performance"][dim]["coherence"]["adapter"]) for dim in dimensions_range],
            "Quantum": [(dim, results["performance"][dim]["coherence"]["quantum"]) for dim in dimensions_range],
            "Phi-Harmonic": [(dim, results["performance"][dim]["coherence"]["phi_harmonic"]) for dim in dimensions_range],
            "Standard": [(dim, results["performance"][dim]["coherence"]["standard"]) for dim in dimensions_range]
        }
        
        coherence_viz_path = self.visualize_performance(
            coherence_data,
            "Dimensions",
            "Coherence",
            "Quantum Coherence Across Dimensions",
            "dimensional_scaling_coherence.png"
        )
        
        # Visualize resonance across dimensions
        resonance_data = {
            "Adapter": [(dim, results["performance"][dim]["resonance"]["adapter"]) for dim in dimensions_range],
            "Quantum": [(dim, results["performance"][dim]["resonance"]["quantum"]) for dim in dimensions_range],
            "Phi-Harmonic": [(dim, results["performance"][dim]["resonance"]["phi_harmonic"]) for dim in dimensions_range],
            "Standard": [(dim, results["performance"][dim]["resonance"]["standard"]) for dim in dimensions_range]
        }
        
        resonance_viz_path = self.visualize_performance(
            resonance_data,
            "Dimensions",
            "Resonance",
            "Quantum Resonance Across Dimensions",
            "dimensional_scaling_resonance.png"
        )
        
        # Calculate scaling factors
        scaling_factors = {}
        
        for key in performance_data:
            if len(performance_data[key]) > 1:
                first_dim, first_ops = performance_data[key][0]
                last_dim, last_ops = performance_data[key][-1]
                
                ops_scaling = last_ops / first_ops if first_ops > 0 else float('inf')
                dim_scaling = last_dim / first_dim
                
                # Calculate phi power equivalent
                phi_power = np.log(ops_scaling) / np.log(float(PHI))
                
                scaling_factors[key] = {
                    "dimension_increase": f"{first_dim} → {last_dim} ({dim_scaling:.1f}x)",
                    "performance_increase": f"{first_ops:.2f} → {last_ops:.2f} ops/s ({ops_scaling:.2f}x)",
                    "phi_power_equivalent": f"φ^{phi_power:.2f}"
                }
        
        # Add visualizations to results
        results["visualizations"] = {
            "performance": viz_path,
            "coherence": coherence_viz_path,
            "resonance": resonance_viz_path
        }
        
        # Add scaling factors to results
        results["scaling_factors"] = scaling_factors
        
        return results
    
    def analyze_dimensional_advantage(self, results):
        """
        Analyze the dimensional advantage of quantum random integration.
        
        Args:
            results: Dictionary of dimensional scaling test results
            
        Returns:
            Dictionary of analysis results
        """
        logger.info("Analyzing dimensional advantage...")
        
        dimensions = results["dimensions"]
        
        # Calculate performance ratios
        performance_ratios = {}
        
        for dim in dimensions:
            dim_results = results["performance"][dim]
            
            # Calculate ratios for each transformation
            for transformation in ["phi", "standard", "complex"]:
                # Get standard performance as baseline
                standard_ops = dim_results["generators"]["standard"][transformation]["ops_per_second"]
                
                # Calculate ratios for quantum generators
                for generator in ["adapter", "quantum", "phi_harmonic"]:
                    quantum_ops = dim_results["generators"][generator][transformation]["ops_per_second"]
                    ratio = quantum_ops / standard_ops if standard_ops > 0 else float('inf')
                    
                    key = f"{generator}_{transformation}"
                    if key not in performance_ratios:
                        performance_ratios[key] = []
                    
                    performance_ratios[key].append((dim, ratio))
        
        # Visualize performance ratios
        viz_path = self.visualize_performance(
            performance_ratios,
            "Dimensions",
            "Performance Ratio (Quantum / Standard)",
            "Quantum Advantage Across Dimensions",
            "dimensional_advantage.png"
        )
        
        # Calculate average advantage for each combination
        average_advantage = {}
        
        for key, ratios in performance_ratios.items():
            avg_ratio = sum(r[1] for r in ratios) / len(ratios)
            average_advantage[key] = avg_ratio
        
        # Find best combination
        best_key = max(average_advantage, key=average_advantage.get)
        best_avg = average_advantage[best_key]
        
        # Calculate phi power equivalent
        phi_power = np.log(best_avg) / np.log(float(PHI))
        
        logger.info(f"Best combination: {best_key} with {best_avg:.2f}x advantage (φ^{phi_power:.2f})")
        
        # Return analysis results
        return {
            "performance_ratios": performance_ratios,
            "average_advantage": average_advantage,
            "best_combination": {
                "key": best_key,
                "advantage": best_avg,
                "phi_power_equivalent": phi_power
            },
            "visualization": viz_path
        }
    
    def run_benchmark(self, dimensions_range=None, vertex_count=1000):
        """
        Run the dimensional scaling benchmark.
        
        Args:
            dimensions_range: List of dimensions to test (default: [2, 3, 4, 5, 6])
            vertex_count: Number of vertices to generate (default: 1000)
            
        Returns:
            Dictionary of benchmark results
        """
        if dimensions_range is None:
            dimensions_range = [2, 3, 4, 5, 6]
        
        logger.info(f"Running Dimensional Scaling Benchmark with dimensions {dimensions_range} and {vertex_count} vertices...")
        
        # Run dimensional scaling test
        results = self.run_dimensional_scaling_test(dimensions_range, vertex_count)
        
        # Analyze dimensional advantage
        advantage = self.analyze_dimensional_advantage(results)
        
        # Store results
        self.results["dimensional_scaling"] = {
            "test_results": results,
            "advantage_analysis": advantage
        }
        
        # Save results
        self.save_results()
        
        logger.info("Dimensional Scaling Benchmark completed")
        
        return self.results["dimensional_scaling"]

def main():
    """Main function for running the dimensional scaling benchmark."""
    benchmark = DimensionalScalingBenchmark()
    benchmark.run_benchmark(dimensions_range=[2, 3, 4, 5], vertex_count=500)

if __name__ == "__main__":
    main()
