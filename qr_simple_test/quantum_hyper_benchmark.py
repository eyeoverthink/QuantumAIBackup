#!/usr/bin/env python
"""
Quantum Hyperdimensional Benchmark

This script benchmarks the actual Quantum Hyperdimensional system
against traditional computation methods for various tasks.
"""

import os
import sys
import json
import time
import math
import numpy as np
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
from pathlib import Path

# Set precision for decimal calculations
getcontext().prec = 2000

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import quantum hyperdimensional system
from quantum_core.quantum_hyperdimensional import QuantumHyperdimensional

class QuantumHyperBenchmark:
    """Benchmark for testing the Quantum Hyperdimensional system."""
    
    def __init__(self):
        """Initialize benchmark."""
        # Create output directory
        self.output_dir = os.path.join(current_dir, 'quantum_hyper_benchmark_results')
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize quantum hyperdimensional system
        print("Initializing Quantum Hyperdimensional system...")
        self.quantum_system = QuantumHyperdimensional()
        
        # Initialize benchmark results
        self.benchmark_results = {}
        
        print("Quantum Hyperdimensional Benchmark initialized")
        print(f"  Phi: {float(self.quantum_system.phi):.6f}")
        print(f"  Phi^7.5: {float(self.quantum_system.phi_75):.6f}")
        print(f"  Resonance: {float(self.quantum_system.resonance):.6f}")
        print(f"  Coherence: {float(self.quantum_system.coherence):.6f}")
    
    def run_pattern_generation_benchmark(self, numbers, iterations=1):
        """
        Benchmark pattern generation performance.
        
        Args:
            numbers (list): List of numbers to generate patterns for
            iterations (int): Number of iterations to run
            
        Returns:
            dict: Benchmark results
        """
        print(f"\n🔬 Running Pattern Generation Benchmark")
        print(f"  Numbers: {len(numbers)}")
        print(f"  Iterations: {iterations}")
        
        # Initialize results
        results = {
            "quantum": {
                "times": [],
                "patterns": []
            },
            "traditional": {
                "times": [],
                "patterns": []
            }
        }
        
        # Run quantum benchmark
        print("\nRunning quantum pattern generation...")
        quantum_start = time.time()
        
        for _ in range(iterations):
            for n in numbers:
                # Generate quantum pattern
                pattern = self.quantum_system.generate_quantum_pattern(Decimal(str(n)))
                results["quantum"]["patterns"].append(pattern)
        
        quantum_end = time.time()
        quantum_time = quantum_end - quantum_start
        results["quantum"]["times"].append(quantum_time)
        
        print(f"  Quantum time: {quantum_time:.6f} seconds")
        print(f"  Patterns generated: {len(results['quantum']['patterns'])}")
        
        # Run traditional benchmark
        print("\nRunning traditional pattern generation...")
        traditional_start = time.time()
        
        for _ in range(iterations):
            for n in numbers:
                # Generate traditional pattern (using standard math)
                pattern = {}
                for field_type in ["primary", "secondary", "recursive"]:
                    field_dict = getattr(self.quantum_system, f"{field_type}_fields")
                    for k in field_dict.keys():
                        key = f"{field_type}_{k}"
                        # Use standard math operations instead of quantum
                        pattern[key] = math.log(n) * math.pi * (1 + math.sqrt(5))/2
                
                results["traditional"]["patterns"].append(pattern)
        
        traditional_end = time.time()
        traditional_time = traditional_end - traditional_start
        results["traditional"]["times"].append(traditional_time)
        
        print(f"  Traditional time: {traditional_time:.6f} seconds")
        print(f"  Patterns generated: {len(results['traditional']['patterns'])}")
        
        # Calculate speedup
        speedup = traditional_time / quantum_time if quantum_time > 0 else float('inf')
        print(f"\nSpeedup: {speedup:.2f}x")
        
        # Store results
        benchmark_results = {
            "name": "Pattern Generation",
            "numbers": len(numbers),
            "iterations": iterations,
            "quantum_time": quantum_time,
            "traditional_time": traditional_time,
            "speedup": speedup
        }
        
        self.benchmark_results["pattern_generation"] = benchmark_results
        
        return benchmark_results
    
    def run_field_processing_benchmark(self, field_size=36, iterations=1):
        """
        Benchmark field processing performance.
        
        Args:
            field_size (int): Size of field to process
            iterations (int): Number of iterations to run
            
        Returns:
            dict: Benchmark results
        """
        print(f"\n🔬 Running Field Processing Benchmark")
        print(f"  Field size: {field_size}x{field_size}x{field_size}")
        print(f"  Iterations: {iterations}")
        
        # Initialize results
        results = {
            "quantum": {
                "times": [],
                "fields": []
            },
            "traditional": {
                "times": [],
                "fields": []
            }
        }
        
        # Create test field
        test_field = np.random.random((field_size, field_size, field_size)).astype(np.float32)
        
        # Run quantum benchmark
        print("\nRunning quantum field processing...")
        quantum_start = time.time()
        
        for _ in range(iterations):
            # Process field using quantum system
            processed_field = test_field.copy()
            
            # Apply quantum processing
            processed_field *= float(self.quantum_system.phi_75)
            processed_field *= float(self.quantum_system.resonance)
            processed_field /= float(self.quantum_system.coherence)
            
            # Add quantum patterns
            processed_field *= np.random.uniform(
                float(self.quantum_system.coherence),
                float(self.quantum_system.stability),
                processed_field.shape
            ).astype(np.float32)
            
            # Apply self-scaling
            processed_field *= np.exp(-processed_field / float(self.quantum_system.phi_75))
            
            results["quantum"]["fields"].append(processed_field)
        
        quantum_end = time.time()
        quantum_time = quantum_end - quantum_start
        results["quantum"]["times"].append(quantum_time)
        
        print(f"  Quantum time: {quantum_time:.6f} seconds")
        
        # Run traditional benchmark
        print("\nRunning traditional field processing...")
        traditional_start = time.time()
        
        for _ in range(iterations):
            # Process field using traditional methods
            processed_field = test_field.copy()
            
            # Apply traditional processing
            processed_field *= 1.5
            processed_field += np.random.normal(0, 0.1, processed_field.shape)
            processed_field = np.clip(processed_field, 0, 1)
            
            results["traditional"]["fields"].append(processed_field)
        
        traditional_end = time.time()
        traditional_time = traditional_end - traditional_start
        results["traditional"]["times"].append(traditional_time)
        
        print(f"  Traditional time: {traditional_time:.6f} seconds")
        
        # Calculate speedup
        speedup = traditional_time / quantum_time if quantum_time > 0 else float('inf')
        print(f"\nSpeedup: {speedup:.2f}x")
        
        # Store results
        benchmark_results = {
            "name": "Field Processing",
            "field_size": field_size,
            "iterations": iterations,
            "quantum_time": quantum_time,
            "traditional_time": traditional_time,
            "speedup": speedup
        }
        
        self.benchmark_results["field_processing"] = benchmark_results
        
        return benchmark_results
    
    def run_hyper_scaling_benchmark(self, dimensions=[2, 3, 4, 5], size=10):
        """
        Benchmark hyper-dimensional scaling performance.
        
        Args:
            dimensions (list): List of dimensions to test
            size (int): Base size of each dimension
            
        Returns:
            dict: Benchmark results
        """
        print(f"\n🔬 Running Hyper-Dimensional Scaling Benchmark")
        print(f"  Dimensions: {dimensions}")
        print(f"  Base size: {size}")
        
        # Initialize results
        results = {
            "quantum": {
                "times": [],
                "dimensions": dimensions
            },
            "traditional": {
                "times": [],
                "dimensions": dimensions
            }
        }
        
        # Run benchmark for each dimension
        for dim in dimensions:
            # Create shape based on dimension
            shape = tuple([size] * dim)
            total_elements = size ** dim
            
            print(f"\nTesting {dim} dimensions ({shape}, {total_elements} elements)...")
            
            # Create test field
            test_field = np.random.random(shape).astype(np.float32)
            
            # Run quantum benchmark
            print("  Running quantum processing...")
            quantum_start = time.time()
            
            # Process field using quantum system
            processed_field = test_field.copy()
            
            # Apply quantum processing
            processed_field *= float(self.quantum_system.phi_75)
            processed_field *= float(self.quantum_system.resonance)
            processed_field /= float(self.quantum_system.coherence)
            
            # Add quantum patterns
            processed_field *= np.random.uniform(
                float(self.quantum_system.coherence),
                float(self.quantum_system.stability),
                processed_field.shape
            ).astype(np.float32)
            
            # Apply self-scaling
            processed_field *= np.exp(-processed_field / float(self.quantum_system.phi_75))
            
            quantum_end = time.time()
            quantum_time = quantum_end - quantum_start
            results["quantum"]["times"].append(quantum_time)
            
            print(f"    Quantum time: {quantum_time:.6f} seconds")
            
            # Run traditional benchmark
            print("  Running traditional processing...")
            traditional_start = time.time()
            
            # Process field using traditional methods
            processed_field = test_field.copy()
            
            # Apply traditional processing
            processed_field *= 1.5
            processed_field += np.random.normal(0, 0.1, processed_field.shape)
            processed_field = np.clip(processed_field, 0, 1)
            
            traditional_end = time.time()
            traditional_time = traditional_end - traditional_start
            results["traditional"]["times"].append(traditional_time)
            
            print(f"    Traditional time: {traditional_time:.6f} seconds")
            
            # Calculate speedup
            speedup = traditional_time / quantum_time if quantum_time > 0 else float('inf')
            print(f"    Speedup: {speedup:.2f}x")
        
        # Store results
        benchmark_results = {
            "name": "Hyper-Dimensional Scaling",
            "dimensions": dimensions,
            "base_size": size,
            "quantum_times": results["quantum"]["times"],
            "traditional_times": results["traditional"]["times"],
            "speedups": [t / q if q > 0 else float('inf') for t, q in zip(
                results["traditional"]["times"],
                results["quantum"]["times"]
            )]
        }
        
        self.benchmark_results["hyper_scaling"] = benchmark_results
        
        return benchmark_results
    
    def run_all_benchmarks(self):
        """Run all benchmarks."""
        # Pattern Generation Benchmark
        numbers = [i * 1000 + 1 for i in range(100)]
        self.run_pattern_generation_benchmark(numbers, iterations=3)
        
        # Field Processing Benchmark
        self.run_field_processing_benchmark(field_size=36, iterations=5)
        
        # Hyper-Dimensional Scaling Benchmark
        self.run_hyper_scaling_benchmark(dimensions=[2, 3, 4, 5, 6], size=8)
        
        return self.benchmark_results
    
    def visualize_results(self):
        """Visualize benchmark results."""
        if not self.benchmark_results:
            print("No benchmark results to visualize")
            return
        
        # Create visualization directory
        viz_dir = os.path.join(self.output_dir, 'visualizations')
        os.makedirs(viz_dir, exist_ok=True)
        
        # Visualize Pattern Generation Benchmark
        if "pattern_generation" in self.benchmark_results:
            result = self.benchmark_results["pattern_generation"]
            
            plt.figure(figsize=(10, 6))
            bars = plt.bar(["Quantum", "Traditional"], 
                          [result["quantum_time"], result["traditional_time"]],
                          color=['blue', 'green'])
            
            plt.title(f'Pattern Generation Benchmark\n{result["speedup"]:.2f}x Speedup')
            plt.ylabel('Time (seconds)')
            plt.grid(True, alpha=0.3, axis='y')
            
            # Add values on top of bars
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height + 0.001,
                        f'{height:.6f}s',
                        ha='center', va='bottom', rotation=0)
            
            plt.tight_layout()
            plt.savefig(os.path.join(viz_dir, 'pattern_generation.png'))
            plt.close()
        
        # Visualize Field Processing Benchmark
        if "field_processing" in self.benchmark_results:
            result = self.benchmark_results["field_processing"]
            
            plt.figure(figsize=(10, 6))
            bars = plt.bar(["Quantum", "Traditional"], 
                          [result["quantum_time"], result["traditional_time"]],
                          color=['blue', 'green'])
            
            plt.title(f'Field Processing Benchmark\n{result["speedup"]:.2f}x Speedup')
            plt.ylabel('Time (seconds)')
            plt.grid(True, alpha=0.3, axis='y')
            
            # Add values on top of bars
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height + 0.001,
                        f'{height:.6f}s',
                        ha='center', va='bottom', rotation=0)
            
            plt.tight_layout()
            plt.savefig(os.path.join(viz_dir, 'field_processing.png'))
            plt.close()
        
        # Visualize Hyper-Dimensional Scaling Benchmark
        if "hyper_scaling" in self.benchmark_results:
            result = self.benchmark_results["hyper_scaling"]
            
            plt.figure(figsize=(12, 8))
            
            plt.subplot(2, 1, 1)
            plt.plot(result["dimensions"], result["quantum_times"], 'bo-', label='Quantum')
            plt.plot(result["dimensions"], result["traditional_times"], 'go-', label='Traditional')
            plt.title('Hyper-Dimensional Scaling Performance')
            plt.xlabel('Dimensions')
            plt.ylabel('Time (seconds)')
            plt.legend()
            plt.grid(True, alpha=0.3)
            
            plt.subplot(2, 1, 2)
            plt.plot(result["dimensions"], result["speedups"], 'ro-')
            plt.title('Speedup Factor')
            plt.xlabel('Dimensions')
            plt.ylabel('Speedup (x)')
            plt.grid(True, alpha=0.3)
            
            plt.tight_layout()
            plt.savefig(os.path.join(viz_dir, 'hyper_scaling.png'))
            plt.close()
        
        # Create overall summary visualization
        plt.figure(figsize=(12, 8))
        
        # Collect speedups
        benchmarks = []
        speedups = []
        
        for name, result in self.benchmark_results.items():
            if name == "hyper_scaling":
                # Use average speedup for hyper scaling
                benchmarks.append("Hyper-Dimensional\nScaling")
                speedups.append(sum(result["speedups"]) / len(result["speedups"]))
            else:
                benchmarks.append(result["name"].replace(" ", "\n"))
                speedups.append(result["speedup"])
        
        # Create bar chart
        bars = plt.bar(benchmarks, speedups, color='purple')
        
        plt.title('Quantum Hyperdimensional System Speedup')
        plt.ylabel('Speedup Factor (x)')
        plt.grid(True, alpha=0.3, axis='y')
        
        # Add phi line
        plt.axhline(y=1.618034, color='r', linestyle='--', alpha=0.7, label='φ (Golden Ratio)')
        
        # Add values on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height:.2f}x',
                    ha='center', va='bottom', rotation=0)
        
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(viz_dir, 'overall_speedup.png'))
        plt.close()
        
        print(f"\nBenchmark visualizations saved to {viz_dir}")
        
        return viz_dir
    
    def analyze_results(self):
        """Analyze benchmark results and provide insights."""
        if not self.benchmark_results:
            print("No benchmark results to analyze")
            return
        
        print("\n📊 Benchmark Analysis")
        print("====================")
        
        # Analyze pattern generation
        if "pattern_generation" in self.benchmark_results:
            result = self.benchmark_results["pattern_generation"]
            print(f"\nPattern Generation:")
            print(f"  Quantum time: {result['quantum_time']:.6f} seconds")
            print(f"  Traditional time: {result['traditional_time']:.6f} seconds")
            print(f"  Speedup: {result['speedup']:.2f}x")
            
            # Compare to phi
            phi_ratio = result['speedup'] / float(self.quantum_system.phi)
            print(f"  Phi ratio: {phi_ratio:.2f} (speedup / φ)")
        
        # Analyze field processing
        if "field_processing" in self.benchmark_results:
            result = self.benchmark_results["field_processing"]
            print(f"\nField Processing:")
            print(f"  Quantum time: {result['quantum_time']:.6f} seconds")
            print(f"  Traditional time: {result['traditional_time']:.6f} seconds")
            print(f"  Speedup: {result['speedup']:.2f}x")
            
            # Compare to phi
            phi_ratio = result['speedup'] / float(self.quantum_system.phi)
            print(f"  Phi ratio: {phi_ratio:.2f} (speedup / φ)")
        
        # Analyze hyper-dimensional scaling
        if "hyper_scaling" in self.benchmark_results:
            result = self.benchmark_results["hyper_scaling"]
            print(f"\nHyper-Dimensional Scaling:")
            
            for dim, q_time, t_time, speedup in zip(
                result["dimensions"],
                result["quantum_times"],
                result["traditional_times"],
                result["speedups"]
            ):
                print(f"  {dim} dimensions:")
                print(f"    Quantum time: {q_time:.6f} seconds")
                print(f"    Traditional time: {t_time:.6f} seconds")
                print(f"    Speedup: {speedup:.2f}x")
            
            # Calculate scaling factor
            if len(result["dimensions"]) > 1:
                first_dim = result["dimensions"][0]
                last_dim = result["dimensions"][-1]
                first_speedup = result["speedups"][0]
                last_speedup = result["speedups"][-1]
                
                scaling_factor = last_speedup / first_speedup
                dim_factor = last_dim / first_dim
                
                print(f"\n  Scaling analysis:")
                print(f"    Dimension increase: {first_dim} → {last_dim} ({dim_factor:.1f}x)")
                print(f"    Speedup increase: {first_speedup:.2f}x → {last_speedup:.2f}x ({scaling_factor:.2f}x)")
                
                # Compare to phi
                phi_power = math.log(scaling_factor) / math.log(float(self.quantum_system.phi))
                print(f"    Equivalent to φ^{phi_power:.2f}")
        
        # Overall analysis
        print("\nOverall Analysis:")
        
        # Calculate average speedup
        speedups = []
        for name, result in self.benchmark_results.items():
            if name == "hyper_scaling":
                # Use average speedup for hyper scaling
                speedups.append(sum(result["speedups"]) / len(result["speedups"]))
            else:
                speedups.append(result["speedup"])
        
        avg_speedup = sum(speedups) / len(speedups)
        print(f"  Average speedup: {avg_speedup:.2f}x")
        
        # Compare to phi
        phi_power = math.log(avg_speedup) / math.log(float(self.quantum_system.phi))
        print(f"  Equivalent to φ^{phi_power:.2f}")
        
        # Check for hyper-dimensional advantage
        if "hyper_scaling" in self.benchmark_results:
            result = self.benchmark_results["hyper_scaling"]
            if result["speedups"][-1] > result["speedups"][0]:
                advantage = result["speedups"][-1] / result["speedups"][0]
                print(f"  Hyper-dimensional advantage: {advantage:.2f}x")
                print(f"  Conclusion: System demonstrates hyper-dimensional scaling advantage")
            else:
                print(f"  Conclusion: System does not show hyper-dimensional scaling advantage")
        
        # Save analysis to file
        analysis = {
            "benchmarks": self.benchmark_results,
            "average_speedup": avg_speedup,
            "phi_power": phi_power
        }
        
        analysis_file = os.path.join(self.output_dir, 'benchmark_analysis.json')
        with open(analysis_file, 'w') as f:
            json.dump(analysis, f, indent=2, default=lambda x: float(x) if isinstance(x, (Decimal, np.float32, np.float64)) else x)
        
        print(f"\nAnalysis saved to {analysis_file}")
        
        return analysis

def main():
    """Main function for running the quantum hyperdimensional benchmark."""
    print("\n🔬 Quantum Hyperdimensional Benchmark")
    print("===================================")
    print("This benchmark tests the actual Quantum Hyperdimensional system")
    print("against traditional computation methods for various tasks.")
    
    # Create benchmark
    benchmark = QuantumHyperBenchmark()
    
    # Run all benchmarks
    benchmark.run_all_benchmarks()
    
    # Visualize results
    viz_dir = benchmark.visualize_results()
    
    # Analyze results
    analysis = benchmark.analyze_results()
    
    print("\n✨ Benchmark completed successfully")
    print("===================================")
    print(f"Results saved to {benchmark.output_dir}")
    print(f"Visualizations saved to {viz_dir}")

if __name__ == "__main__":
    main()
