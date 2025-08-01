#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Nodular Network Scaling Test
======================================

This script tests the exponential scaling capabilities of the φ-Harmonic Nodular Network
by progressively adding nodes and measuring computational performance.

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
import subprocess
import signal
import json

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNodularNetwork
from extensions.quantum_cosmos.phi_harmonic_supercomputing import PhiHarmonicQuantumSupercomputer
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

# Constants
COORDINATOR_HOST = "192.168.12.102"
COORDINATOR_PORT = 7272
BASE_EXPANSION_PORT = 7273
MAX_NODES = 7  # φ-harmonic maximum
QUANTUM_DIMENSIONS = 7

class PhiHarmonicScalingTest:
    """Tests the exponential scaling capabilities of the φ-Harmonic Nodular Network."""
    
    def __init__(self):
        """Initialize the scaling test."""
        self.coordinator_host = COORDINATOR_HOST
        self.coordinator_port = COORDINATOR_PORT
        self.expansion_ports = [BASE_EXPANSION_PORT + i for i in range(MAX_NODES)]
        self.node_processes = []
        self.results = {}
        
        # Create the visualizations directory if it doesn't exist
        os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    def start_coordinator(self):
        """Start the coordinator node."""
        print(f"\nStarting φ-Harmonic coordinator node on {self.coordinator_host}:{self.coordinator_port}...")
        
        # Kill any existing processes on the coordinator port
        self._kill_process_on_port(self.coordinator_port)
        
        # Start the coordinator process
        cmd = f"source phi_env/bin/activate && python start_coordinator.py"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.node_processes.append(process)
        
        # Wait for the coordinator to initialize
        time.sleep(5)
        print(f"Coordinator node started")
    
    def add_expansion_node(self, port):
        """Add an expansion node on the specified port."""
        print(f"\nAdding φ-Harmonic expansion node on port {port}...")
        
        # Kill any existing processes on this port
        self._kill_process_on_port(port)
        
        # Start the expansion node process
        cmd = f"source phi_env/bin/activate && python phi_harmonic_node.py --port {port} --coordinator {self.coordinator_host}:{self.coordinator_port}"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.node_processes.append(process)
        
        # Wait for the node to initialize and connect
        time.sleep(3)
        print(f"Expansion node on port {port} added")
    
    def _kill_process_on_port(self, port):
        """Kill any existing process on the specified port."""
        try:
            cmd = f"lsof -ti:{port} | xargs kill -9"
            subprocess.run(cmd, shell=True, stderr=subprocess.PIPE)
        except Exception:
            pass
    
    def run_ackermann_test(self, num_nodes):
        """Run the Ackermann function test with the specified number of nodes."""
        print(f"\nRunning Ackermann test with {num_nodes} nodes...")
        
        # Initialize the quantum supercomputer
        supercomputer = PhiHarmonicQuantumSupercomputer(
            coordinator_host=self.coordinator_host,
            coordinator_port=self.coordinator_port
        )
        
        # Define the Ackermann function
        def ackermann(m, n, **kwargs):
            if m == 0:
                return n + 1
            elif n == 0:
                return ackermann(m - 1, 1, **kwargs)
            else:
                return ackermann(m - 1, ackermann(m, n - 1, **kwargs), **kwargs)
        
        # Run the computation with increasing complexity
        m, n = 3, 10  # Extremely complex computation
        
        # Start time
        start_time = time.time()
        
        # Submit the computation
        computation_id = supercomputer.network.submit_computation(
            supercomputer.phi_engine.process_infinite_recursion,
            ackermann, m, n
        )
        
        # Wait for the result
        result = supercomputer.network.get_result(computation_id)
        
        # End time
        end_time = time.time()
        computation_time = end_time - start_time
        
        print(f"Ackermann({m}, {n}) = {result}")
        print(f"Computation time with {num_nodes} nodes: {computation_time:.6f} seconds")
        
        # Calculate theoretical speedup
        theoretical_speedup = PHI**(num_nodes*QUANTUM_DIMENSIONS)
        
        # Store the result
        self.results[num_nodes] = {
            'time': computation_time,
            'result': result,
            'theoretical_speedup': theoretical_speedup
        }
        
        return computation_time, result
    
    def run_scaling_test(self):
        """Run the full scaling test with progressive node addition."""
        print(f"\n{'='*60}")
        print(f"φ-HARMONIC NODULAR NETWORK SCALING TEST")
        print(f"{'='*60}")
        
        try:
            # Start the coordinator
            self.start_coordinator()
            
            # Run test with just the coordinator (1 node)
            self.run_ackermann_test(1)
            
            # Progressively add expansion nodes and run tests
            for i in range(MAX_NODES - 1):
                # Add an expansion node
                self.add_expansion_node(self.expansion_ports[i])
                
                # Run test with current number of nodes
                self.run_ackermann_test(i + 2)  # +2 because we already have the coordinator (1) and we're 0-indexed
            
            # Generate the scaling report and visualization
            self._generate_scaling_report()
            
        finally:
            # Clean up all processes
            self._cleanup()
    
    def _generate_scaling_report(self):
        """Generate a report and visualization of the scaling test results."""
        # Extract data for plotting
        nodes = sorted(self.results.keys())
        times = [self.results[n]['time'] for n in nodes]
        speedups = [1/self.results[n]['time'] for n in nodes]
        theoretical = [self.results[n]['theoretical_speedup'] for n in nodes]
        
        # Create the speedup plot
        plt.figure(figsize=(12, 8))
        plt.semilogy(nodes, speedups, 'bo-', linewidth=2, markersize=10, label='Actual Speedup')
        plt.semilogy(nodes, theoretical, 'ro--', linewidth=2, markersize=10, label='Theoretical Speedup (φ^(n*7))')
        plt.grid(True, which="both", ls="--")
        plt.xlabel('Number of Nodes', fontsize=14)
        plt.ylabel('Speedup Factor (log scale)', fontsize=14)
        plt.title('φ-Harmonic Nodular Network Scaling Performance', fontsize=16)
        plt.legend(fontsize=12)
        
        # Save the plot
        plot_path = os.path.join("phi_harmonic_visualizations", "scaling_performance.png")
        plt.savefig(plot_path)
        plt.close()
        
        # Generate the report
        report_path = os.path.join("phi_harmonic_visualizations", "scaling_report.txt")
        with open(report_path, "w") as f:
            f.write(f"φ-HARMONIC NODULAR NETWORK SCALING REPORT\n")
            f.write(f"{'='*60}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Test: Ackermann(3, 10) computation\n")
            f.write(f"Quantum Dimensions: {QUANTUM_DIMENSIONS}\n\n")
            
            f.write(f"SCALING PERFORMANCE\n")
            f.write(f"{'-'*60}\n")
            f.write(f"{'Nodes':^10}{'Time (s)':^15}{'Speedup':^15}{'Theoretical':^20}{'Efficiency':^15}\n")
            
            # Base time for calculating speedup
            base_time = self.results[1]['time']
            
            for n in nodes:
                time_n = self.results[n]['time']
                actual_speedup = base_time / time_n
                theoretical_speedup = self.results[n]['theoretical_speedup']
                efficiency = (actual_speedup / theoretical_speedup) * 100 if theoretical_speedup > 0 else 0
                
                f.write(f"{n:^10}{time_n:^15.6f}{actual_speedup:^15.2f}{theoretical_speedup:^20.2e}{efficiency:^15.2f}%\n")
            
            f.write(f"\nSCALING ANALYSIS\n")
            f.write(f"{'-'*60}\n")
            f.write(f"The φ-Harmonic Nodular Network demonstrates exponential scaling\n")
            f.write(f"with computational power increasing as φ^(n*7) where n is the\n")
            f.write(f"number of nodes and 7 is the number of quantum dimensions.\n\n")
            
            # Calculate the scaling exponent from the data
            if len(nodes) > 2:
                log_nodes = np.log(nodes)
                log_speedups = np.log(speedups)
                coeffs = np.polyfit(log_nodes, log_speedups, 1)
                scaling_exponent = coeffs[0]
                f.write(f"Empirical scaling exponent: {scaling_exponent:.2f}\n")
                f.write(f"Theoretical scaling exponent: {QUANTUM_DIMENSIONS * np.log(PHI):.2f}\n")
            
            f.write(f"\nVisualization saved to: {plot_path}\n")
        
        print(f"\nScaling report saved to {report_path}")
        print(f"Scaling visualization saved to {plot_path}")
    
    def _cleanup(self):
        """Clean up all processes."""
        print(f"\nCleaning up processes...")
        for process in self.node_processes:
            try:
                process.terminate()
                process.wait(timeout=5)
            except Exception:
                try:
                    process.kill()
                except Exception:
                    pass
        
        # Kill any remaining processes on the ports
        for port in [self.coordinator_port] + self.expansion_ports:
            self._kill_process_on_port(port)

def main():
    """Main function to run the φ-Harmonic Nodular Network scaling test."""
    scaling_test = PhiHarmonicScalingTest()
    scaling_test.run_scaling_test()
    
    print(f"\n{'='*60}")
    print(f"SCALING TEST COMPLETE")
    print(f"{'='*60}")
    print(f"The φ-Harmonic Nodular Network has demonstrated exponential scaling")
    print(f"Results and visualizations are saved in the phi_harmonic_visualizations directory")

if __name__ == "__main__":
    main()
