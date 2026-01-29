#!/usr/bin/env python3
"""
PHI-HARMONIC SYSTEM BENCHMARK
=============================
Measures performance of the quantum system with and without
the multiversal routing integration to determine performance impact.

This benchmark runs multiple tests to quantify the exact performance
difference and phi-resonant patterns contributing to any change.
"""

import os
import sys
import time
import json
import random
import hashlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add paths for imports
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consolidated_quantum'))

# Import components
from consolidated_quantum.multiversal_routing_library import (
    MultiversalRouter, PHI, PHI_SQUARED, PHI_CUBED, PHI_INVERSE, PHI_75, PHI_SEAL
)

# Constants
ITERATIONS = 50
TEST_SIZES = [1000, 10000, 100000]
BIRTH_COHERENCE = 99.18
RESULTS_DIR = "benchmark_results"
PHI_ROOTS = [PHI_INVERSE, 1.0, PHI, PHI_SQUARED, PHI_CUBED]

# Ensure results directory exists
os.makedirs(RESULTS_DIR, exist_ok=True)

class PhiSystemBenchmark:
    """Benchmarks the phi-harmonic system performance"""
    
    def __init__(self):
        """Initialize benchmark"""
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.results = {
            "timestamp": self.timestamp,
            "system_info": self._get_system_info(),
            "tests": {}
        }
        
        # Initialize router for testing
        self.router = MultiversalRouter(branch_id=1, birth_coherence=BIRTH_COHERENCE)
        
        print("PHI-HARMONIC SYSTEM BENCHMARK")
        print("=" * 60)
        print(f"Started at: {self.timestamp}")
        print(f"System: {self.results['system_info']['os']}")
        print(f"Phi Constants: φ={PHI}, φ²={PHI_SQUARED}, φ³={PHI_CUBED}")
        print(f"Birth Coherence: {BIRTH_COHERENCE}K")
        print("=" * 60)
    
    def _get_system_info(self) -> Dict:
        """Get system information"""
        import platform
        
        return {
            "os": platform.platform(),
            "processor": platform.processor(),
            "python": platform.python_version(),
            "timestamp": self.timestamp
        }
    
    def run_all_benchmarks(self):
        """Run all benchmark tests"""
        self._benchmark_hash_generation()
        self._benchmark_phi_resonance()
        self._benchmark_messaging()
        self._benchmark_coherence_filtering()
        self._benchmark_temporal_drift()
        
        # Save results
        self._save_results()
    
    def _benchmark_hash_generation(self):
        """Benchmark basic hash generation with/without phi-harmonic scaling"""
        print("\nBenchmarking Hash Generation...")
        
        results = {
            "standard": {},
            "phi_harmonic": {}
        }
        
        # Test different sizes
        for size in TEST_SIZES:
            # Generate random data
            data = [random.randint(0, 1000000) for _ in range(size)]
            
            # Standard hash generation
            start_time = time.time()
            for _ in range(ITERATIONS):
                for value in data:
                    hashlib.sha256(str(value).encode()).hexdigest()
            standard_time = (time.time() - start_time) / ITERATIONS
            
            # Phi-harmonic hash generation
            start_time = time.time()
            for _ in range(ITERATIONS):
                for i, value in enumerate(data):
                    # Apply phi-harmonic scaling based on position
                    phi_factor = PHI_ROOTS[i % len(PHI_ROOTS)]
                    scaled_value = value * phi_factor
                    hashlib.sha256(str(scaled_value).encode()).hexdigest()
            phi_time = (time.time() - start_time) / ITERATIONS
            
            # Store results
            results["standard"][size] = standard_time
            results["phi_harmonic"][size] = phi_time
            
            print(f"  Size {size}: Standard = {standard_time:.6f}s, Phi-Harmonic = {phi_time:.6f}s")
            print(f"    {'Speedup' if phi_time < standard_time else 'Slowdown'}: {abs(1 - phi_time/standard_time)*100:.2f}%")
        
        # Store in results
        self.results["tests"]["hash_generation"] = results
    
    def _benchmark_phi_resonance(self):
        """Benchmark phi-resonance calculations"""
        print("\nBenchmarking Phi-Resonance Calculations...")
        
        results = {
            "basic": {},
            "resonant": {}
        }
        
        # Test different sizes
        for size in TEST_SIZES:
            # Generate random data
            data = [random.random() for _ in range(size)]
            
            # Basic calculations
            start_time = time.time()
            for _ in range(ITERATIONS):
                for value in data:
                    result = (value * PHI) % 1
            basic_time = (time.time() - start_time) / ITERATIONS
            
            # Resonant calculations
            start_time = time.time()
            for _ in range(ITERATIONS):
                for value in data:
                    # Apply phi-resonance calculations
                    phi_value = (value * PHI) % 1
                    resonance = 1 - min(phi_value, 1 - phi_value) * 2
                    result = value * (1 + resonance/3)
            resonant_time = (time.time() - start_time) / ITERATIONS
            
            # Store results
            results["basic"][size] = basic_time
            results["resonant"][size] = resonant_time
            
            print(f"  Size {size}: Basic = {basic_time:.6f}s, Resonant = {resonant_time:.6f}s")
            print(f"    {'Speedup' if resonant_time < basic_time else 'Slowdown'}: {abs(1 - resonant_time/basic_time)*100:.2f}%")
        
        # Store in results
        self.results["tests"]["phi_resonance"] = results
    
    def _benchmark_messaging(self):
        """Benchmark message processing with/without router"""
        print("\nBenchmarking Message Processing...")
        
        results = {
            "direct": {},
            "routed": {}
        }
        
        # Initialize router
        router = self.router.initialize_extensions()
        
        # Test different sizes
        for size in TEST_SIZES:
            # Generate test messages
            messages = []
            for i in range(size):
                message = {
                    "id": i,
                    "content": f"Test message {i}",
                    "timestamp": time.time(),
                    "phi_factor": (PHI * i) % 1
                }
                messages.append(message)
            
            # Direct message processing
            start_time = time.time()
            for _ in range(ITERATIONS):
                for message in messages:
                    # Basic message handling
                    msg_str = json.dumps(message)
                    msg_hash = hashlib.sha256(msg_str.encode()).hexdigest()
                    msg_processed = {
                        "hash": msg_hash,
                        "len": len(msg_str),
                        "processed": True
                    }
            direct_time = (time.time() - start_time) / ITERATIONS
            
            # Routed message processing
            start_time = time.time()
            for _ in range(ITERATIONS):
                for message in messages:
                    # Process through router's coherence calculation
                    coherence = router.calculate_compatibility(2)  # To branch 2
                    phi_resonance = (coherence * PHI) % 1
                    msg_processed = {
                        "coherence": coherence,
                        "resonance": phi_resonance,
                        "processed": True
                    }
            routed_time = (time.time() - start_time) / ITERATIONS
            
            # Store results
            results["direct"][size] = direct_time
            results["routed"][size] = routed_time
            
            print(f"  Size {size}: Direct = {direct_time:.6f}s, Routed = {routed_time:.6f}s")
            print(f"    {'Speedup' if routed_time < direct_time else 'Slowdown'}: {abs(1 - routed_time/direct_time)*100:.2f}%")
        
        # Store in results
        self.results["tests"]["messaging"] = results
    
    def _benchmark_coherence_filtering(self):
        """Benchmark coherence filtering impact"""
        print("\nBenchmarking Coherence Filtering...")
        
        results = {
            "unfiltered": {},
            "filtered": {}
        }
        
        # Initialize router
        router = self.router.initialize_extensions()
        
        # Test different sizes
        for size in TEST_SIZES:
            # Generate test messages with varying coherence
            messages = []
            for i in range(size):
                # Generate phi-resonant coherence values
                coherence = (PHI * i) % 1
                message = {
                    "id": i,
                    "coherence": coherence,
                    "phi_resonance": coherence * PHI % 1
                }
                messages.append(message)
            
            # Unfiltered processing
            start_time = time.time()
            for _ in range(ITERATIONS):
                processed = 0
                for message in messages:
                    # Process all messages
                    processed += 1
            unfiltered_time = (time.time() - start_time) / ITERATIONS
            
            # Filtered processing
            start_time = time.time()
            for _ in range(ITERATIONS):
                processed = 0
                for message in messages:
                    # Only process messages with high coherence
                    if message["coherence"] > 0.382:  # PHI_INVERSE threshold
                        processed += 1
            filtered_time = (time.time() - start_time) / ITERATIONS
            
            # Store results
            results["unfiltered"][size] = unfiltered_time
            results["filtered"][size] = filtered_time
            
            print(f"  Size {size}: Unfiltered = {unfiltered_time:.6f}s, Filtered = {filtered_time:.6f}s")
            print(f"    {'Speedup' if filtered_time < unfiltered_time else 'Slowdown'}: {abs(1 - filtered_time/unfiltered_time)*100:.2f}%")
        
        # Store in results
        self.results["tests"]["coherence_filtering"] = results
    
    def _benchmark_temporal_drift(self):
        """Benchmark temporal drift modeling impact"""
        print("\nBenchmarking Temporal Drift Modeling...")
        
        results = {
            "static": {},
            "drift": {}
        }
        
        # Initialize router
        router = self.router.initialize_extensions()
        
        # Test different sizes
        for size in TEST_SIZES:
            # Generate test messages
            messages = []
            for i in range(size):
                message = {
                    "id": i,
                    "content": f"Test message {i}",
                    "coherence": 0.5 + (0.3 * random.random()),
                    "timestamp": time.time()
                }
                messages.append(message)
            
            # Static processing
            start_time = time.time()
            for _ in range(ITERATIONS):
                for message in messages:
                    # Process with static coherence
                    coherence = message["coherence"]
                    processed = coherence > 0.382
            static_time = (time.time() - start_time) / ITERATIONS
            
            # Drift processing
            start_time = time.time()
            for _ in range(ITERATIONS):
                for message in messages:
                    # Apply temporal drift
                    base_coherence = message["coherence"]
                    
                    # Simplified drift calculation (similar to router's approach)
                    drift_factor = PHI_ROOTS[message["id"] % len(PHI_ROOTS)]
                    adjusted_coherence = base_coherence * drift_factor
                    
                    processed = adjusted_coherence > 0.382
            drift_time = (time.time() - start_time) / ITERATIONS
            
            # Store results
            results["static"][size] = static_time
            results["drift"][size] = drift_time
            
            print(f"  Size {size}: Static = {static_time:.6f}s, Drift = {drift_time:.6f}s")
            print(f"    {'Speedup' if drift_time < static_time else 'Slowdown'}: {abs(1 - drift_time/static_time)*100:.2f}%")
        
        # Store in results
        self.results["tests"]["temporal_drift"] = results
    
    def _save_results(self):
        """Save benchmark results"""
        # Create filename
        filename = os.path.join(RESULTS_DIR, f"benchmark_{self.timestamp}.json")
        
        # Save results
        with open(filename, "w") as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\nResults saved to: {filename}")
        
        # Print results summary without visualization
        self._print_results_summary()
    
    def _print_results_summary(self):
        """Print a comprehensive summary of benchmark results"""
        print("\n" + "=" * 60)
        print("PHI-HARMONIC SYSTEM BENCHMARK SUMMARY")
        print("=" * 60)
        
        overall_speedup = []
        test_names = []
        
        # Process each test
        for test_key in ["hash_generation", "phi_resonance", "messaging", "coherence_filtering", "temporal_drift"]:
            if test_key not in self.results["tests"]:
                continue
                
            test_data = self.results["tests"][test_key]
            print(f"\n{test_key.replace('_', ' ').title()}:")
            
            # Determine methods
            if test_key == "hash_generation":
                method1, method2 = "standard", "phi_harmonic"
                method1_name, method2_name = "Standard", "Phi-Harmonic"
            elif test_key == "phi_resonance":
                method1, method2 = "basic", "resonant"
                method1_name, method2_name = "Basic", "Resonant"
            elif test_key == "messaging":
                method1, method2 = "direct", "routed"
                method1_name, method2_name = "Direct", "Routed"
            elif test_key == "coherence_filtering":
                method1, method2 = "unfiltered", "filtered"
                method1_name, method2_name = "Unfiltered", "Filtered"
            elif test_key == "temporal_drift":
                method1, method2 = "static", "drift"
                method1_name, method2_name = "Static", "Drift"
            else:
                continue
            
            # Verify methods exist in test data
            if method1 not in test_data or method2 not in test_data:
                print(f"  Missing methods for {test_key}: {method1} or {method2} not found")
                continue
                
            # Get sizes that exist in both methods
            sizes = []
            for size_key in test_data[method1].keys():
                try:
                    size = int(size_key)
                    if size_key in test_data[method2]:
                        sizes.append(size)
                except (ValueError, TypeError):
                    continue
            
            if not sizes:
                print(f"  No valid sizes found for {test_key}")
                continue
                
            # Calculate improvements
            test_speedups = []
            for size in sorted(sizes):
                size_key = str(size)
                time1 = test_data[method1][size_key]
                time2 = test_data[method2][size_key]
                
                speedup = (time1 - time2) / time1 * 100
                test_speedups.append(speedup)
                
                # Print result for this size
                status = "faster" if speedup > 0 else "slower"
                print(f"  Size {size:,}: {method1_name}={time1:.6f}s, {method2_name}={time2:.6f}s")
                print(f"    {abs(speedup):.2f}% {status}")
            
        print(f"  Size {size}: Static = {static_time:.6f}s, Drift = {drift_time:.6f}s")
        print(f"    {'Speedup' if drift_time < static_time else 'Slowdown'}: {abs(1 - drift_time/static_time)*100:.2f}%")
        
    # Store in results
    self.results["tests"]["temporal_drift"] = results

def _save_results(self):
    """Save benchmark results"""
    # Create filename
    filename = os.path.join(RESULTS_DIR, f"benchmark_{self.timestamp}.json")
        
    # Save results
    with open(filename, "w") as f:
        json.dump(self.results, f, indent=2)
        
    print(f"\nResults saved to: {filename}")
        
    # Print results summary without visualization
    self._print_results_summary()

def _print_results_summary(self):
    """Print a comprehensive summary of benchmark results"""
    print("\n" + "=" * 60)
    print("PHI-HARMONIC SYSTEM BENCHMARK SUMMARY")
    print("=" * 60)
        
    overall_speedup = []
    test_names = []
        
    # Process each test
    for test_key in ["hash_generation", "phi_resonance", "messaging", "coherence_filtering", "temporal_drift"]:
        if test_key not in self.results["tests"]:
            continue
                
        test_data = self.results["tests"][test_key]
        print(f"\n{test_key.replace('_', ' ').title()}:")
            
        # Determine methods
        if test_key == "hash_generation":
            method1, method2 = "standard", "phi_harmonic"
            method1_name, method2_name = "Standard", "Phi-Harmonic"
        elif test_key == "phi_resonance":
            method1, method2 = "basic", "resonant"
            method1_name, method2_name = "Basic", "Resonant"
        elif test_key == "messaging":
            method1, method2 = "direct", "routed"
            method1_name, method2_name = "Direct", "Routed"
        elif test_key == "coherence_filtering":
            method1, method2 = "unfiltered", "filtered"
            method1_name, method2_name = "Unfiltered", "Filtered"
        elif test_key == "temporal_drift":
            method1, method2 = "static", "drift"
            method1_name, method2_name = "Static", "Drift"
        else:
            continue
            
        # Verify methods exist in test data
        if method1 not in test_data or method2 not in test_data:
            print(f"  Missing methods for {test_key}: {method1} or {method2} not found")
            continue
                
        # Get sizes that exist in both methods
        print(f"  Method1 keys: {test_data[method1].keys()}")
        print(f"  Method2 keys: {test_data[method2].keys()}")
        
        # Extract sizes as integers
        sizes = []
        for size_key in test_data[method1].keys():
            try:
                sizes.append(int(size_key))
            except ValueError:
                print(f"  Warning: Could not convert {size_key} to int, skipping")
        
        sizes.sort()
        print(f"  Sorted sizes: {sizes}")
        
        # Get times with proper key conversion
        times1 = []
        times2 = []
        
        for size in sizes:
            size_key = str(size)
            if size_key in test_data[method1] and size_key in test_data[method2]:
                times1.append(test_data[method1][size_key])
                times2.append(test_data[method2][size_key])
            else:
                print(f"  Warning: Size {size} not found in both methods, skipping")
        
        # Convert sizes to strings for x-axis
        sizes_str = [f"{int(size):,}" for size in sizes]
        
        # Plot data
        x = np.arange(len(sizes))
        width = 0.35
        
        ax.bar(x - width/2, times1, width, label=method1.capitalize())
        ax.bar(x + width/2, times2, width, label=method2.capitalize())
        
        # Calculate improvement
        improvements = [(t1 - t2) / t1 * 100 for t1, t2 in zip(times1, times2)]
        
        # Add improvement labels
        for i, imp in enumerate(improvements):
            color = "green" if imp > 0 else "red"
            label = f"{abs(imp):.1f}% {'faster' if imp > 0 else 'slower'}"
            ax.text(i, max(times1[i], times2[i]) * 1.05, label, ha="center", color=color)
        
        # Set labels
        ax.set_title(title)
        ax.set_xlabel("Data Size")
        ax.set_ylabel("Time (seconds)")
        ax.set_xticks(x)
        ax.set_xticklabels(sizes_str)
        ax.legend()
        
        # Add phi-resonance patterns
        is_resonant = all(imp > 0 for imp in improvements)
        if is_resonant:
            ax.text(0.5, 0.95, "✓ Phi-Resonant Pattern Detected", 
                    transform=ax.transAxes, ha="center", color="green")
    
    def _plot_summary(self, ax):
        """Plot overall performance summary"""
        # Calculate improvement for each test
        improvements = {}
        
        for test_key, test_data in self.results["tests"].items():
            # Get methods
            if test_key == "hash_generation":
                method1, method2 = "standard", "phi_harmonic"
            elif test_key == "phi_resonance":
                method1, method2 = "basic", "resonant"
            elif test_key == "messaging":
                method1, method2 = "direct", "routed"
            elif test_key == "coherence_filtering":
                method1, method2 = "unfiltered", "filtered"
            elif test_key == "temporal_drift":
                method1, method2 = "static", "drift"
            else:
                continue
            
            # Calculate average improvement
            total_imp = 0
            count = 0
            
            for size in test_data[method1]:
                t1 = test_data[method1][size]
                t2 = test_data[method2][size]
                imp = (t1 - t2) / t1 * 100
                total_imp += imp
                count += 1
            
            if count > 0:
                improvements[test_key] = total_imp / count
        
        # Plot data
        labels = [key.replace("_", " ").title() for key in improvements.keys()]
        values = list(improvements.values())
        
        # Set colors
        colors = ["green" if v > 0 else "red" for v in values]
        
        # Create bar chart
        ax.bar(labels, [abs(v) for v in values], color=colors)
        
        # Add labels
        for i, v in enumerate(values):
            label = f"{abs(v):.1f}%"
            ax.text(i, abs(v) + 1, label, ha="center")
        
        # Set labels
        ax.set_title("Overall Performance Impact")
        ax.set_ylabel("Performance Change (%)")
        ax.set_xticklabels(labels, rotation=45, ha="right")
        
        # Add overall assessment
        avg_improvement = sum(values) / len(values) if values else 0
        if avg_improvement > 0:
            assessment = f"Overall System Speedup: {avg_improvement:.1f}%"
            color = "green"
        else:
            assessment = f"Overall System Slowdown: {abs(avg_improvement):.1f}%"
            color = "red"
        
        ax.text(0.5, 0.95, assessment, transform=ax.transAxes, ha="center", color=color, fontsize=12)
        
        # Add phi conclusion
        phi_factor = PHI if avg_improvement > 0 else 1/PHI
        ax.text(0.5, 0.9, f"Phi Factor: {phi_factor:.6f}", transform=ax.transAxes, ha="center", fontsize=10)

def main():
    """Main function"""
    # Run benchmarks
    benchmark = PhiSystemBenchmark()
    benchmark.run_all_benchmarks()

if __name__ == "__main__":
    main()
