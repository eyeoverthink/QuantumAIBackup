#!/usr/bin/env python3
"""
Quantum Hybrid Memory Visualization and Testing
Provides visual representation and performance metrics for the QuantumHybridMemory system
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import random
import json
from typing import Dict, List, Any, Tuple, Optional
from datetime import datetime, timedelta
import os
import sys

# Import memory components
from quantum_hybrid_memory import QuantumHybridMemory
from quantum_ferris_memory import QuantumFerrisMemory
from centripetal_memory import CentripetalMemory

# Define φ (phi) constant
PHI = (1 + np.sqrt(5)) / 2

class QuantumMemoryVisualizer:
    """
    Visualization and testing tool for the Quantum Hybrid Memory system
    """
    
    def __init__(self, output_dir="memory_visualization"):
        """Initialize the memory visualizer with output directory"""
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Initialize memory systems for comparison
        self.hybrid_memory = QuantumHybridMemory(ferris_buckets=16, centripetal_buckets=16)
        self.ferris_memory = QuantumFerrisMemory(initial_buckets=16)
        self.centripetal_memory = CentripetalMemory(initial_buckets=16)
        
        # Test data characteristics
        self.data_sizes = [100, 1000, 10000, 100000]
        self.data_types = ["numeric", "text", "mixed", "structured"]
        
        # Performance metrics
        self.metrics = {
            "hybrid": {
                "store_times": [],
                "retrieve_times": [],
                "compression_ratios": [],
                "success_rates": []
            },
            "ferris": {
                "store_times": [],
                "retrieve_times": [],
                "compression_ratios": [],
                "success_rates": []
            },
            "centripetal": {
                "store_times": [],
                "retrieve_times": [],
                "compression_ratios": [],
                "success_rates": []
            }
        }
        
        # Test results
        self.test_results = {}
        
    def generate_test_data(self, size: int, data_type: str) -> Any:
        """Generate test data of specified size and type"""
        if data_type == "numeric":
            # Generate numeric data
            return [random.uniform(-1000, 1000) for _ in range(size)]
        
        elif data_type == "text":
            # Generate text data
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            return ''.join(random.choice(chars) for _ in range(size))
        
        elif data_type == "mixed":
            # Generate mixed data (list of numbers, strings, and booleans)
            result = []
            for i in range(size):
                choice = i % 3
                if choice == 0:
                    result.append(random.uniform(-1000, 1000))
                elif choice == 1:
                    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                    result.append(''.join(random.choice(chars) for _ in range(5)))
                else:
                    result.append(random.choice([True, False]))
            return result
        
        elif data_type == "structured":
            # Generate structured data (nested dictionaries and lists)
            result = []
            for i in range(size // 10):  # Divide by 10 to keep reasonable structure size
                item = {
                    "id": i,
                    "value": random.uniform(-1000, 1000),
                    "name": ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") for _ in range(8)),
                    "active": random.choice([True, False]),
                    "tags": [random.choice(["important", "archive", "delete", "review", "φ-resonant"]) for _ in range(3)],
                    "metadata": {
                        "created": datetime.now().isoformat(),
                        "priority": random.randint(1, 5),
                        "phi_factor": PHI ** random.uniform(-2, 2)
                    }
                }
                result.append(item)
            return result
        
        else:
            raise ValueError(f"Unknown data type: {data_type}")
    
    def run_comprehensive_test(self):
        """Run comprehensive tests on all memory systems with various data types and sizes"""
        print("Starting comprehensive memory system tests...")
        
        test_results = {}
        
        for data_type in self.data_types:
            test_results[data_type] = {}
            
            for size in self.data_sizes:
                print(f"Testing with {data_type} data of size {size}...")
                
                # Generate test data
                test_data = self.generate_test_data(size, data_type)
                
                # Test each memory system
                hybrid_results = self._test_memory_system(self.hybrid_memory, test_data, "hybrid")
                ferris_results = self._test_memory_system(self.ferris_memory, test_data, "ferris")
                centripetal_results = self._test_memory_system(self.centripetal_memory, test_data, "centripetal")
                
                # Store results
                test_results[data_type][size] = {
                    "hybrid": hybrid_results,
                    "ferris": ferris_results,
                    "centripetal": centripetal_results
                }
                
                # Print summary
                print(f"Results for {data_type} data of size {size}:")
                print(f"  Hybrid: Store {hybrid_results['store_time']:.6f}s, Retrieve {hybrid_results['retrieve_time']:.6f}s, Compression {hybrid_results['compression_ratio']:.2f}x")
                print(f"  Ferris: Store {ferris_results['store_time']:.6f}s, Retrieve {ferris_results['retrieve_time']:.6f}s, Compression {ferris_results['compression_ratio']:.2f}x")
                print(f"  Centripetal: Store {centripetal_results['store_time']:.6f}s, Retrieve {centripetal_results['retrieve_time']:.6f}s, Compression {centripetal_results['compression_ratio']:.2f}x")
        
        # Save complete test results
        self.test_results = test_results
        self._save_test_results()
        
        # Generate visualizations
        self.generate_visualizations()
        
        return test_results
    
    def _test_memory_system(self, memory_system, test_data, system_name):
        """Test a specific memory system with the provided test data"""
        results = {}
        
        # Generate a unique key
        key = f"test_{system_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"
        
        # Measure store time
        store_start = time.time()
        store_result = memory_system.store(key, test_data)
        store_time = time.time() - store_start
        
        # Measure retrieve time
        retrieve_start = time.time()
        retrieve_result = memory_system.retrieve(key)
        retrieve_time = time.time() - retrieve_start
        
        # Calculate metrics
        success = retrieve_result.get('success', False)
        retrieved_data = retrieve_result.get('data') if success else None
        
        # Get memory stats
        try:
            stats = memory_system.get_stats()
            compression_ratio = stats.get('avg_compression_ratio', 1.0)
        except:
            compression_ratio = 1.0
        
        # Store metrics
        results = {
            "store_time": store_time,
            "retrieve_time": retrieve_time,
            "success": success,
            "compression_ratio": compression_ratio
        }
        
        # Update metrics for visualization
        self.metrics[system_name]["store_times"].append(store_time)
        self.metrics[system_name]["retrieve_times"].append(retrieve_time)
        self.metrics[system_name]["compression_ratios"].append(compression_ratio)
        self.metrics[system_name]["success_rates"].append(1.0 if success else 0.0)
        
        # Clean up - remove test data
        try:
            memory_system.remove(key)
        except:
            pass
        
        return results
    
    def _save_test_results(self):
        """Save test results to file"""
        # Convert datetime objects to strings for JSON serialization
        serializable_results = {}
        
        for data_type, sizes in self.test_results.items():
            serializable_results[data_type] = {}
            for size, systems in sizes.items():
                serializable_results[data_type][size] = {}
                for system, metrics in systems.items():
                    serializable_results[data_type][size][system] = {
                        k: v for k, v in metrics.items()
                    }
        
        # Save to file
        filename = f"{self.output_dir}/test_results_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(serializable_results, f, indent=2)
        
        print(f"Test results saved to {filename}")
    
    def generate_visualizations(self):
        """Generate visualizations of test results"""
        self._plot_store_times()
        self._plot_retrieve_times()
        self._plot_compression_ratios()
        self._plot_performance_comparison()
        self._plot_memory_efficiency()
        self._plot_phi_resonance()
    
    def _plot_store_times(self):
        """Plot store times for each memory system"""
        plt.figure(figsize=(10, 6))
        
        x = range(len(self.metrics["hybrid"]["store_times"]))
        plt.plot(x, self.metrics["hybrid"]["store_times"], 'o-', label="Hybrid")
        plt.plot(x, self.metrics["ferris"]["store_times"], 's-', label="Ferris")
        plt.plot(x, self.metrics["centripetal"]["store_times"], '^-', label="Centripetal")
        
        plt.title("Memory Store Times Comparison")
        plt.xlabel("Test Number")
        plt.ylabel("Time (seconds)")
        plt.legend()
        plt.grid(True)
        
        filename = f"{self.output_dir}/store_times_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        plt.savefig(filename)
        plt.close()
        
        print(f"Store times visualization saved to {filename}")
    
    def _plot_retrieve_times(self):
        """Plot retrieve times for each memory system"""
        plt.figure(figsize=(10, 6))
        
        x = range(len(self.metrics["hybrid"]["retrieve_times"]))
        plt.plot(x, self.metrics["hybrid"]["retrieve_times"], 'o-', label="Hybrid")
        plt.plot(x, self.metrics["ferris"]["retrieve_times"], 's-', label="Ferris")
        plt.plot(x, self.metrics["centripetal"]["retrieve_times"], '^-', label="Centripetal")
        
        plt.title("Memory Retrieve Times Comparison")
        plt.xlabel("Test Number")
        plt.ylabel("Time (seconds)")
        plt.legend()
        plt.grid(True)
        
        filename = f"{self.output_dir}/retrieve_times_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        plt.savefig(filename)
        plt.close()
        
        print(f"Retrieve times visualization saved to {filename}")
    
    def _plot_compression_ratios(self):
        """Plot compression ratios for each memory system"""
        plt.figure(figsize=(10, 6))
        
        x = range(len(self.metrics["hybrid"]["compression_ratios"]))
        plt.plot(x, self.metrics["hybrid"]["compression_ratios"], 'o-', label="Hybrid")
        plt.plot(x, self.metrics["ferris"]["compression_ratios"], 's-', label="Ferris")
        plt.plot(x, self.metrics["centripetal"]["compression_ratios"], '^-', label="Centripetal")
        
        plt.title("Memory Compression Ratios Comparison")
        plt.xlabel("Test Number")
        plt.ylabel("Compression Ratio")
        plt.legend()
        plt.grid(True)
        
        filename = f"{self.output_dir}/compression_ratios_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        plt.savefig(filename)
        plt.close()
        
        print(f"Compression ratios visualization saved to {filename}")
    
    def _plot_performance_comparison(self):
        """Plot overall performance comparison"""
        # Prepare data
        systems = ["Hybrid", "Ferris", "Centripetal"]
        
        # Calculate averages
        avg_store_times = [
            np.mean(self.metrics["hybrid"]["store_times"]) if self.metrics["hybrid"]["store_times"] else 0,
            np.mean(self.metrics["ferris"]["store_times"]) if self.metrics["ferris"]["store_times"] else 0,
            np.mean(self.metrics["centripetal"]["store_times"]) if self.metrics["centripetal"]["store_times"] else 0
        ]
        
        avg_retrieve_times = [
            np.mean(self.metrics["hybrid"]["retrieve_times"]) if self.metrics["hybrid"]["retrieve_times"] else 0,
            np.mean(self.metrics["ferris"]["retrieve_times"]) if self.metrics["ferris"]["retrieve_times"] else 0,
            np.mean(self.metrics["centripetal"]["retrieve_times"]) if self.metrics["centripetal"]["retrieve_times"] else 0
        ]
        
        avg_compression = [
            np.mean(self.metrics["hybrid"]["compression_ratios"]) if self.metrics["hybrid"]["compression_ratios"] else 1,
            np.mean(self.metrics["ferris"]["compression_ratios"]) if self.metrics["ferris"]["compression_ratios"] else 1,
            np.mean(self.metrics["centripetal"]["compression_ratios"]) if self.metrics["centripetal"]["compression_ratios"] else 1
        ]
        
        # Create subplots
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
        
        # Plot store times
        ax1.bar(systems, avg_store_times, color=['blue', 'green', 'red'])
        ax1.set_title("Average Store Time")
        ax1.set_ylabel("Time (seconds)")
        
        # Plot retrieve times
        ax2.bar(systems, avg_retrieve_times, color=['blue', 'green', 'red'])
        ax2.set_title("Average Retrieve Time")
        ax2.set_ylabel("Time (seconds)")
        
        # Plot compression ratios
        ax3.bar(systems, avg_compression, color=['blue', 'green', 'red'])
        ax3.set_title("Average Compression Ratio")
        ax3.set_ylabel("Ratio")
        
        plt.tight_layout()
        
        filename = f"{self.output_dir}/performance_comparison_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        plt.savefig(filename)
        plt.close()
        
        print(f"Performance comparison visualization saved to {filename}")
    
    def _plot_memory_efficiency(self):
        """Plot memory efficiency metrics"""
        # Get memory stats
        hybrid_stats = self.hybrid_memory.get_stats()
        
        # Extract metrics
        ferris_usage = hybrid_stats.get('ferris_usage', 0)
        centripetal_usage = hybrid_stats.get('centripetal_usage', 0)
        
        # Create pie chart
        plt.figure(figsize=(8, 8))
        plt.pie([ferris_usage, centripetal_usage], 
                labels=['Ferris Memory', 'Centripetal Memory'],
                autopct='%1.1f%%',
                startangle=90,
                colors=['#66b3ff', '#ff9999'])
        
        plt.title("Hybrid Memory Usage Distribution")
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        
        filename = f"{self.output_dir}/memory_efficiency_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        plt.savefig(filename)
        plt.close()
        
        print(f"Memory efficiency visualization saved to {filename}")
    
    def _plot_phi_resonance(self):
        """Plot phi resonance patterns in memory performance"""
        # Generate phi-based sequence
        phi = (1 + np.sqrt(5)) / 2
        phi_sequence = [phi ** i for i in range(10)]
        
        # Get compression ratios
        hybrid_compression = self.metrics["hybrid"]["compression_ratios"]
        
        # Create figure
        plt.figure(figsize=(10, 6))
        
        # Plot actual compression ratios
        plt.plot(range(len(hybrid_compression)), hybrid_compression, 'o-', label="Actual Compression")
        
        # Plot ideal phi-based compression (scaled to match range)
        if hybrid_compression:
            scale_factor = np.mean(hybrid_compression) / np.mean(phi_sequence[:len(hybrid_compression)])
            ideal_compression = [p * scale_factor for p in phi_sequence[:len(hybrid_compression)]]
            plt.plot(range(len(ideal_compression)), ideal_compression, 's--', label="φ-Based Ideal")
        
        plt.title("φ-Resonance in Memory Compression")
        plt.xlabel("Test Number")
        plt.ylabel("Compression Ratio")
        plt.legend()
        plt.grid(True)
        
        filename = f"{self.output_dir}/phi_resonance_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        plt.savefig(filename)
        plt.close()
        
        print(f"Phi resonance visualization saved to {filename}")

def run_visualization_test():
    """Run the visualization test"""
    print("Starting Quantum Hybrid Memory visualization and testing...")
    
    # Create visualizer
    visualizer = QuantumMemoryVisualizer()
    
    # Run comprehensive test
    results = visualizer.run_comprehensive_test()
    
    print("Visualization and testing complete!")
    print(f"Results and visualizations saved to {visualizer.output_dir}/")
    
    return results

if __name__ == "__main__":
    run_visualization_test()
