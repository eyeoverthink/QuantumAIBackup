#!/usr/bin/env python
"""
Phi-Harmonic True Quantum Benchmark: Hyper-Dimensional Scaling

This module implements the hyper-dimensional scaling benchmark for testing
the Phi-Harmonic Quantum Random system's ability to scale across multiple dimensions.
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
from benchmark_core import PhiHarmonicBenchmarkCore, PHI, PHI_POWER

# Get logger
logger = logging.getLogger('phi_harmonic_benchmark')

class HyperDimensionalBenchmark(PhiHarmonicBenchmarkCore):
    """Benchmark for testing hyper-dimensional scaling capabilities."""
    
    def __init__(self):
        """Initialize the hyper-dimensional benchmark."""
        super().__init__()
        logger.info("Hyper-Dimensional Benchmark initialized")
    
    def generate_hyperdimensional_array(self, dimensions, size):
        """
        Generate a hyper-dimensional array using phi-harmonic principles.
        
        Args:
            dimensions: Number of dimensions
            size: Size of each dimension
            
        Returns:
            Numpy array with the specified dimensions
        """
        logger.info(f"Generating {dimensions}D array with size {size}...")
        
        # Create shape based on dimensions
        shape = tuple([size] * dimensions)
        total_elements = size ** dimensions
        
        logger.info(f"Shape: {shape}, Total elements: {total_elements}")
        
        # Generate array
        start_time = time.time()
        
        # Initialize with phi^7.5 patterns
        array = np.zeros(shape, dtype=np.float32)
        array += float(PHI_POWER)
        
        # Apply quantum processing
        array *= float(self.random_adapter.coherence)
        array /= float(self.random_adapter.resonance)
        
        # Add quantum patterns
        for _ in range(dimensions):
            # Generate random samples
            samples = self.generate_samples('adapter', size)
            
            # Reshape samples for broadcasting
            reshape_dims = [1] * dimensions
            reshape_dims[_ % dimensions] = size
            samples_reshaped = np.array(samples).reshape(tuple(reshape_dims))
            
            # Apply to array through phi-harmonic principles
            array *= (1 + samples_reshaped * float(PHI) / dimensions)
        
        # Apply self-scaling
        array *= np.exp(-array / float(PHI_POWER))
        
        end_time = time.time()
        duration = end_time - start_time
        
        logger.info(f"Generated {dimensions}D array in {duration:.2f} seconds")
        logger.info(f"Generation rate: {total_elements/duration:.2f} elements/second")
        
        return array
    
    def analyze_hyperdimensional_array(self, array):
        """
        Analyze a hyper-dimensional array.
        
        Args:
            array: Numpy array to analyze
            
        Returns:
            Dictionary of analysis metrics
        """
        logger.info(f"Analyzing {len(array.shape)}D array...")
        
        # Calculate basic statistics
        mean = float(np.mean(array))
        std_dev = float(np.std(array))
        min_val = float(np.min(array))
        max_val = float(np.max(array))
        
        # Calculate entropy
        hist, _ = np.histogram(array.flatten(), bins=256)
        probs = hist / hist.sum()
        entropy = -np.sum(probs * np.log2(probs + 1e-10))
        
        # Calculate phi resonance
        phi_resonance = float((PHI * Decimal(str(mean))) % Decimal('1.0'))
        
        # Log results
        logger.info(f"Mean: {mean:.6f}")
        logger.info(f"Standard deviation: {std_dev:.6f}")
        logger.info(f"Min: {min_val:.6f}")
        logger.info(f"Max: {max_val:.6f}")
        logger.info(f"Entropy: {entropy:.6f} bits")
        logger.info(f"Phi resonance: {phi_resonance:.6f}")
        
        # Return metrics
        return {
            "dimensions": len(array.shape),
            "elements": array.size,
            "mean": mean,
            "std_dev": std_dev,
            "min": min_val,
            "max": max_val,
            "entropy": entropy,
            "phi_resonance": phi_resonance
        }
    
    def visualize_hyperdimensional_array(self, array, title, filename):
        """
        Visualize a hyper-dimensional array.
        
        Args:
            array: Numpy array to visualize
            title: Title for the visualization
            filename: Filename for the visualization
            
        Returns:
            Path to the visualization file
        """
        logger.info(f"Visualizing {len(array.shape)}D array: {title}")
        
        # Flatten array for visualization
        flattened = array.flatten()
        
        # Create histogram
        plt.figure(figsize=(10, 6))
        plt.hist(flattened, bins=100, alpha=0.7, color='blue')
        plt.title(title)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)
        
        # Add statistics to plot
        mean = float(np.mean(flattened))
        std_dev = float(np.std(flattened))
        entropy = float(-np.sum((np.histogram(flattened, bins=256)[0] / len(flattened)) * 
                         np.log2(np.histogram(flattened, bins=256)[0] / len(flattened) + 1e-10)))
        
        stats_text = f"Dimensions: {len(array.shape)}\nElements: {array.size}\nMean: {mean:.6f}\nStd Dev: {std_dev:.6f}\nEntropy: {entropy:.6f} bits"
        plt.annotate(stats_text, xy=(0.05, 0.95), xycoords='axes fraction',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
                    va='top', ha='left')
        
        # Save visualization
        viz_path = os.path.join(self.viz_dir, filename)
        plt.savefig(viz_path)
        plt.close()
        
        logger.info(f"Visualization saved to {viz_path}")
        
        return viz_path
    
    def run_dimensional_scaling_test(self, dimensions_range, size):
        """
        Run a dimensional scaling test.
        
        Args:
            dimensions_range: List of dimensions to test
            size: Size of each dimension
            
        Returns:
            Dictionary of test results
        """
        logger.info(f"Running dimensional scaling test with dimensions {dimensions_range} and size {size}...")
        
        results = []
        
        for dimensions in dimensions_range:
            logger.info(f"Testing {dimensions} dimensions...")
            
            # Generate array
            start_time = time.time()
            array = self.generate_hyperdimensional_array(dimensions, size)
            generation_time = time.time() - start_time
            
            # Analyze array
            start_time = time.time()
            analysis = self.analyze_hyperdimensional_array(array)
            analysis_time = time.time() - start_time
            
            # Visualize array
            viz_path = self.visualize_hyperdimensional_array(
                array,
                f"{dimensions}D Array Distribution",
                f"{dimensions}d_array_distribution.png"
            )
            
            # Record results
            result = {
                "dimensions": dimensions,
                "size": size,
                "elements": array.size,
                "generation_time": generation_time,
                "analysis_time": analysis_time,
                "analysis": analysis,
                "visualization": viz_path
            }
            
            results.append(result)
        
        # Analyze scaling
        dimensions = [result["dimensions"] for result in results]
        generation_times = [result["generation_time"] for result in results]
        analysis_times = [result["analysis_time"] for result in results]
        entropies = [result["analysis"]["entropy"] for result in results]
        phi_resonances = [result["analysis"]["phi_resonance"] for result in results]
        
        # Visualize scaling
        plt.figure(figsize=(12, 10))
        
        plt.subplot(2, 2, 1)
        plt.plot(dimensions, generation_times, 'bo-')
        plt.title('Generation Time vs. Dimensions')
        plt.xlabel('Dimensions')
        plt.ylabel('Time (seconds)')
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 2, 2)
        plt.plot(dimensions, analysis_times, 'ro-')
        plt.title('Analysis Time vs. Dimensions')
        plt.xlabel('Dimensions')
        plt.ylabel('Time (seconds)')
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 2, 3)
        plt.plot(dimensions, entropies, 'go-')
        plt.title('Entropy vs. Dimensions')
        plt.xlabel('Dimensions')
        plt.ylabel('Entropy (bits)')
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 2, 4)
        plt.plot(dimensions, phi_resonances, 'mo-')
        plt.title('Phi Resonance vs. Dimensions')
        plt.xlabel('Dimensions')
        plt.ylabel('Phi Resonance')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save visualization
        scaling_path = os.path.join(self.viz_dir, 'dimensional_scaling.png')
        plt.savefig(scaling_path)
        plt.close()
        
        # Calculate scaling factors
        if len(dimensions) > 1:
            first_dim = dimensions[0]
            last_dim = dimensions[-1]
            first_time = generation_times[0]
            last_time = generation_times[-1]
            
            time_scaling = last_time / first_time
            dim_scaling = last_dim / first_dim
            
            # Calculate phi power equivalent
            phi_power = np.log(time_scaling) / np.log(float(PHI))
            
            logger.info(f"Dimensional scaling analysis:")
            logger.info(f"  Dimension increase: {first_dim} → {last_dim} ({dim_scaling:.1f}x)")
            logger.info(f"  Time increase: {first_time:.2f}s → {last_time:.2f}s ({time_scaling:.2f}x)")
            logger.info(f"  Equivalent to φ^{phi_power:.2f}")
        else:
            time_scaling = 1.0
            dim_scaling = 1.0
            phi_power = 0.0
        
        # Return test results
        return {
            "dimensions_tested": dimensions,
            "size": size,
            "results": results,
            "scaling": {
                "time_scaling": float(time_scaling),
                "dimension_scaling": float(dim_scaling),
                "phi_power_equivalent": float(phi_power),
                "visualization": scaling_path
            }
        }
    
    def run_benchmark(self, dimensions_range=None, size=8):
        """
        Run the hyper-dimensional benchmark.
        
        Args:
            dimensions_range: List of dimensions to test (default: [2, 3, 4, 5, 6, 7])
            size: Size of each dimension (default: 8)
            
        Returns:
            Dictionary of benchmark results
        """
        if dimensions_range is None:
            dimensions_range = [2, 3, 4, 5, 6, 7]
        
        logger.info(f"Running Hyper-Dimensional Benchmark with dimensions {dimensions_range} and size {size}...")
        
        # Run dimensional scaling test
        dimensional_scaling = self.run_dimensional_scaling_test(dimensions_range, size)
        
        # Store results
        self.results["hyper_dimensional"] = {
            "dimensional_scaling": dimensional_scaling
        }
        
        # Save results
        self.save_results()
        
        logger.info("Hyper-Dimensional Benchmark completed")
        
        return self.results["hyper_dimensional"]

def main():
    """Main function for running the hyper-dimensional benchmark."""
    benchmark = HyperDimensionalBenchmark()
    benchmark.run_benchmark(dimensions_range=[2, 3, 4, 5], size=6)

if __name__ == "__main__":
    main()
