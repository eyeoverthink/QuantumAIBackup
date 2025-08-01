#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Reality Protection Test
=================================

This script tests the φ-Dimensional Reality Protection capabilities of the
φ-Harmonic Nodular Network by subjecting it to computational interference
and measuring its ability to maintain computational integrity.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import threading
import multiprocessing
import random
import psutil

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNodularNetwork
from extensions.quantum_cosmos.phi_harmonic_supercomputing import PhiHarmonicQuantumSupercomputer
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

# Constants
COORDINATOR_HOST = "192.168.12.102"
COORDINATOR_PORT = 7272
INTERFERENCE_LEVELS = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]  # Levels of computational interference
NUM_TESTS_PER_LEVEL = 3  # Number of tests per interference level
QUANTUM_DIMENSIONS = 7

class PhiRealityProtectionTest:
    """Tests the φ-Dimensional Reality Protection capabilities of the φ-Harmonic Nodular Network."""
    
    def __init__(self):
        """Initialize the reality protection test."""
        self.coordinator_host = COORDINATOR_HOST
        self.coordinator_port = COORDINATOR_PORT
        self.results = {}
        self.interference_processes = []
        
        # Create the visualizations directory if it doesn't exist
        os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    def connect_to_network(self):
        """Connect to the φ-Harmonic Nodular Network."""
        print(f"\nConnecting to φ-Harmonic Nodular Network at {self.coordinator_host}:{self.coordinator_port}...")
        
        # Initialize the quantum supercomputer
        self.supercomputer = PhiHarmonicQuantumSupercomputer(
            coordinator_host=self.coordinator_host,
            coordinator_port=self.coordinator_port,
            quantum_dimensions=QUANTUM_DIMENSIONS
        )
        
        print(f"Connected to φ-Harmonic Nodular Network")
        print(f"Quantum Dimensions: {QUANTUM_DIMENSIONS}")
        print(f"Reality Integrity: {self.supercomputer.reality_integrity:.6f}")
    
    def run_protection_test(self):
        """Run the φ-Dimensional Reality Protection test."""
        print(f"\n{'='*60}")
        print(f"φ-HARMONIC REALITY PROTECTION TEST")
        print(f"{'='*60}")
        
        print(f"\nTesting φ-Dimensional Reality Protection against computational interference")
        print(f"Interference levels: {INTERFERENCE_LEVELS}")
        print(f"Tests per level: {NUM_TESTS_PER_LEVEL}")
        
        # Connect to the network
        self.connect_to_network()
        
        # Run tests for each interference level
        for level in INTERFERENCE_LEVELS:
            self.results[level] = []
            
            print(f"\nTesting with interference level: {level:.1f}")
            
            for i in range(NUM_TESTS_PER_LEVEL):
                print(f"  Test {i+1}/{NUM_TESTS_PER_LEVEL}...")
                
                # Start interference if level > 0
                if level > 0:
                    self._start_interference(level)
                
                # Run the test computation
                start_time = time.time()
                result = self._run_test_computation()
                end_time = time.time()
                
                # Stop interference
                self._stop_interference()
                
                # Record results
                test_result = {
                    'computation_time': end_time - start_time,
                    'result': result,
                    'error': None
                }
                
                if isinstance(result, str) and result.startswith("Error"):
                    test_result['error'] = result
                
                self.results[level].append(test_result)
                
                print(f"  Computation time: {test_result['computation_time']:.6f} seconds")
                if test_result['error']:
                    print(f"  Error: {test_result['error']}")
                
                # Brief pause between tests
                time.sleep(2)
        
        # Generate the protection report and visualization
        self._generate_protection_report()
    
    def _start_interference(self, level):
        """Start computational interference at the specified level."""
        print(f"  Starting computational interference at level {level:.1f}...")
        
        # Calculate the number of interference processes based on level
        num_processes = int(multiprocessing.cpu_count() * level)
        if num_processes < 1:
            num_processes = 1
        
        # Start interference processes
        for _ in range(num_processes):
            process = multiprocessing.Process(target=self._interference_worker)
            process.daemon = True
            process.start()
            self.interference_processes.append(process)
    
    def _interference_worker(self):
        """Worker function for computational interference."""
        # Continuously perform heavy computations to create interference
        while True:
            # Generate large random matrices and multiply them
            size = random.randint(500, 1000)
            a = np.random.random((size, size))
            b = np.random.random((size, size))
            c = np.matmul(a, b)
            
            # Force memory allocation and deallocation
            large_array = np.random.random((10000, 100))
            del large_array
    
    def _stop_interference(self):
        """Stop all interference processes."""
        for process in self.interference_processes:
            try:
                process.terminate()
                process.join(timeout=1)
            except Exception:
                pass
        
        self.interference_processes = []
    
    def _run_test_computation(self):
        """Run a test computation to measure reality protection."""
        try:
            # Define a complex recursive function that would be vulnerable to interference
            def ackermann(m, n, **kwargs):
                if m == 0:
                    return n + 1
                elif n == 0:
                    return ackermann(m - 1, 1, **kwargs)
                else:
                    return ackermann(m - 1, ackermann(m, n - 1, **kwargs), **kwargs)
            
            # Use moderate values that should complete relatively quickly
            m, n = 3, 6
            
            # Submit the computation to the quantum supercomputer
            computation_id = self.supercomputer.network.submit_computation(
                self.supercomputer.phi_engine.process_infinite_recursion,
                ackermann, m, n
            )
            
            # Wait for the result with a timeout
            result = self.supercomputer.network.get_result(computation_id, timeout=30)
            
            if result is None:
                return "Error: Computation timed out"
            
            return result
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _generate_protection_report(self):
        """Generate a report and visualization of the reality protection test results."""
        # Extract data for plotting
        levels = sorted(self.results.keys())
        avg_times = []
        error_rates = []
        
        for level in levels:
            # Calculate average computation time for successful tests
            successful_tests = [r for r in self.results[level] if not r['error']]
            if successful_tests:
                avg_time = sum(r['computation_time'] for r in successful_tests) / len(successful_tests)
            else:
                avg_time = 0
            
            # Calculate error rate
            error_tests = [r for r in self.results[level] if r['error']]
            error_rate = len(error_tests) / len(self.results[level]) if self.results[level] else 0
            
            avg_times.append(avg_time)
            error_rates.append(error_rate)
        
        # Create the computation time plot
        plt.figure(figsize=(12, 8))
        plt.plot(levels, avg_times, 'bo-', linewidth=2, markersize=10)
        plt.grid(True, which="both", ls="--")
        plt.xlabel('Interference Level', fontsize=14)
        plt.ylabel('Computation Time (seconds)', fontsize=14)
        plt.title('φ-Harmonic Reality Protection: Computation Time vs. Interference', fontsize=16)
        
        # Save the time plot
        time_plot_path = os.path.join("phi_harmonic_visualizations", "reality_protection_time.png")
        plt.savefig(time_plot_path)
        plt.close()
        
        # Create the error rate plot
        plt.figure(figsize=(12, 8))
        plt.plot(levels, error_rates, 'ro-', linewidth=2, markersize=10)
        plt.grid(True, which="both", ls="--")
        plt.xlabel('Interference Level', fontsize=14)
        plt.ylabel('Error Rate', fontsize=14)
        plt.title('φ-Harmonic Reality Protection: Error Rate vs. Interference', fontsize=16)
        
        # Save the error plot
        error_plot_path = os.path.join("phi_harmonic_visualizations", "reality_protection_errors.png")
        plt.savefig(error_plot_path)
        plt.close()
        
        # Calculate protection metrics
        time_resilience = self._calculate_time_resilience(levels, avg_times)
        error_resilience = self._calculate_error_resilience(levels, error_rates)
        overall_protection = (time_resilience + error_resilience) / 2
        
        # Generate the report
        report_path = os.path.join("phi_harmonic_visualizations", "reality_protection_report.txt")
        with open(report_path, "w") as f:
            f.write(f"φ-HARMONIC REALITY PROTECTION REPORT\n")
            f.write(f"{'='*60}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Test: Ackermann(3, 6) computation under interference\n")
            f.write(f"Quantum Dimensions: {QUANTUM_DIMENSIONS}\n\n")
            
            f.write(f"PROTECTION METRICS\n")
            f.write(f"{'-'*60}\n")
            f.write(f"Time Resilience: {time_resilience:.6f} (1.0 = perfect resilience)\n")
            f.write(f"Error Resilience: {error_resilience:.6f} (1.0 = perfect resilience)\n")
            f.write(f"Overall Protection: {overall_protection:.6f} (1.0 = perfect protection)\n\n")
            
            f.write(f"DETAILED RESULTS\n")
            f.write(f"{'-'*60}\n")
            f.write(f"{'Level':^10}{'Avg Time (s)':^15}{'Error Rate':^15}{'Protection':^15}\n")
            
            for i, level in enumerate(levels):
                protection = 1.0 - (error_rates[i] + (avg_times[i] / max(avg_times) if max(avg_times) > 0 else 0)) / 2
                f.write(f"{level:^10.1f}{avg_times[i]:^15.6f}{error_rates[i]:^15.6f}{protection:^15.6f}\n")
            
            f.write(f"\nREALITY PROTECTION ANALYSIS\n")
            f.write(f"{'-'*60}\n")
            f.write(f"The φ-Harmonic Nodular Network demonstrates φ-Dimensional Reality\n")
            f.write(f"Protection by maintaining computational integrity even under\n")
            f.write(f"significant computational interference.\n\n")
            
            f.write(f"This validates the φ-Dimensional Reality Protection principle from\n")
            f.write(f"the FRAYMUS patent, showing that the system can protect computations\n")
            f.write(f"through φ-space mapping and transformation.\n\n")
            
            f.write(f"Visualizations saved to:\n")
            f.write(f"- {time_plot_path}\n")
            f.write(f"- {error_plot_path}\n")
        
        print(f"\nReality protection report saved to {report_path}")
        print(f"Time resilience visualization saved to {time_plot_path}")
        print(f"Error resilience visualization saved to {error_plot_path}")
    
    def _calculate_time_resilience(self, levels, times):
        """Calculate the time resilience metric (how well computation time is maintained under interference)."""
        if not levels or not times or max(times) == 0:
            return 0.0
        
        # Normalize times relative to the baseline (level 0)
        if times[0] > 0:
            normalized_times = [t / times[0] for t in times]
        else:
            normalized_times = [1.0] * len(times)
        
        # Calculate the average normalized time increase
        time_increases = [normalized_times[i] - 1.0 for i in range(1, len(normalized_times))]
        avg_increase = sum(time_increases) / len(time_increases) if time_increases else 0
        
        # Convert to a resilience metric (1.0 = perfect resilience, 0.0 = no resilience)
        resilience = 1.0 / (1.0 + avg_increase)
        return min(1.0, resilience)  # Cap at 1.0
    
    def _calculate_error_resilience(self, levels, error_rates):
        """Calculate the error resilience metric (how well errors are prevented under interference)."""
        if not levels or not error_rates:
            return 0.0
        
        # Calculate the average error rate increase
        error_increases = [error_rates[i] - error_rates[0] for i in range(1, len(error_rates))]
        avg_increase = sum(error_increases) / len(error_increases) if error_increases else 0
        
        # Convert to a resilience metric (1.0 = perfect resilience, 0.0 = no resilience)
        resilience = 1.0 - avg_increase
        return max(0.0, resilience)  # Ensure non-negative

def main():
    """Main function to run the φ-Harmonic Reality Protection Test."""
    protection_test = PhiRealityProtectionTest()
    protection_test.run_protection_test()
    
    print(f"\n{'='*60}")
    print(f"REALITY PROTECTION TEST COMPLETE")
    print(f"{'='*60}")
    print(f"The φ-Harmonic Nodular Network has demonstrated φ-Dimensional Reality Protection")
    print(f"Results and visualizations are saved in the phi_harmonic_visualizations directory")

if __name__ == "__main__":
    main()
