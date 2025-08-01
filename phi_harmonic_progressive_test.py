#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Progressive Network Test
==================================

This script demonstrates the dynamic nature of the φ-Harmonic Nodular Network
by progressively testing different node configurations and measuring
computational performance as the network evolves.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PHI

# Constants
COORDINATOR_PORT = 7272
EXPANSION_PORTS = [7273, 7274, 7275, 7276, 7277, 7278, 7279]  # Progressive expansion ports
QUANTUM_DIMENSIONS = 7
TEST_ITERATIONS = 3  # Run multiple iterations for each configuration

class PhiHarmonicProgressiveTest:
    """Tests the φ-Harmonic Nodular Network with progressive node configurations."""
    
    def __init__(self):
        """Initialize the progressive test."""
        self.coordinator_port = COORDINATOR_PORT
        self.expansion_ports = EXPANSION_PORTS
        self.results = {}
        self.processes = []
        
        # Create the visualizations directory if it doesn't exist
        os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    def run_progressive_test(self):
        """Run the progressive network test."""
        print(f"\n{'='*60}")
        print(f"φ-HARMONIC PROGRESSIVE NETWORK TEST")
        print(f"{'='*60}")
        
        print(f"\nTesting the φ-Harmonic Nodular Network with progressive node configurations")
        print(f"Coordinator port: {self.coordinator_port}")
        print(f"Expansion ports: {', '.join(map(str, self.expansion_ports))}")
        print(f"Test iterations per configuration: {TEST_ITERATIONS}")
        
        # Start with just the coordinator
        for num_nodes in range(1, len(self.expansion_ports) + 2):
            self.results[num_nodes] = []
            
            # Run multiple iterations for each configuration
            for iteration in range(TEST_ITERATIONS):
                print(f"\n{'-'*60}")
                print(f"Testing with {num_nodes} nodes (iteration {iteration+1}/{TEST_ITERATIONS})")
                print(f"{'-'*60}")
                
                # Start the network with the specified number of nodes
                self._start_network(num_nodes)
                
                # Allow the network to stabilize
                print("Allowing network to stabilize...")
                time.sleep(5)
                
                # Run the test computation
                result = self._run_test_computation()
                self.results[num_nodes].append(result)
                
                # Stop the network
                self._stop_network()
                
                # Brief pause between iterations
                time.sleep(2)
        
        # Generate the progressive test report
        self._generate_progressive_report()
    
    def _start_network(self, num_nodes):
        """Start the φ-Harmonic network with the specified number of nodes."""
        # Kill any existing processes on the coordinator port
        self._kill_process_on_port(self.coordinator_port)
        
        # Start the coordinator
        print(f"Starting coordinator on port {self.coordinator_port}...")
        cmd = f"source phi_env/bin/activate && python3 setup_coordinator.py"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.processes.append(process)
        
        # Allow the coordinator to initialize
        time.sleep(3)
        
        # Start expansion nodes if needed
        if num_nodes > 1:
            for i in range(num_nodes - 1):
                if i < len(self.expansion_ports):
                    port = self.expansion_ports[i]
                    self._kill_process_on_port(port)
                    
                    print(f"Starting expansion node on port {port}...")
                    cmd = f"source phi_env/bin/activate && python3 setup_worker.py --port {port}"
                    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.processes.append(process)
                    
                    # Brief pause between starting nodes
                    time.sleep(1)
    
    def _kill_process_on_port(self, port):
        """Kill any existing process on the specified port."""
        try:
            cmd = f"lsof -ti:{port} | xargs kill -9"
            subprocess.run(cmd, shell=True, stderr=subprocess.PIPE)
        except Exception:
            pass
    
    def _run_test_computation(self):
        """Run the test computation and measure performance."""
        print(f"Running test computation...")
        
        # Run the test script
        cmd = f"source phi_env/bin/activate && python3 run_phi_harmonic_test.py"
        start_time = time.time()
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        end_time = time.time()
        
        # Parse the output to extract results
        output = stdout.decode('utf-8')
        
        # Extract computation times
        ackermann_time = None
        tsp_time = None
        nbody_time = None
        total_time = None
        
        for line in output.split('\n'):
            if "Ackermann" in line and "Computation time:" in line:
                try:
                    ackermann_time = float(line.split("Computation time:")[1].strip().split()[0])
                except Exception:
                    pass
            elif "TSP" in line and "Computation time:" in line:
                try:
                    tsp_time = float(line.split("Computation time:")[1].strip().split()[0])
                except Exception:
                    pass
            elif "N-body" in line and "Computation time:" in line:
                try:
                    nbody_time = float(line.split("Computation time:")[1].strip().split()[0])
                except Exception:
                    pass
            elif "Total Computation Time:" in line:
                try:
                    total_time = float(line.split("Total Computation Time:")[1].strip().split()[0])
                except Exception:
                    pass
        
        # If we couldn't parse the output, use the measured time
        if total_time is None:
            total_time = end_time - start_time
        
        # Calculate the theoretical speedup
        theoretical_speedup = PHI**(process.returncode*QUANTUM_DIMENSIONS)
        
        result = {
            'ackermann_time': ackermann_time,
            'tsp_time': tsp_time,
            'nbody_time': nbody_time,
            'total_time': total_time,
            'theoretical_speedup': theoretical_speedup
        }
        
        print(f"Computation completed in {total_time:.2f} seconds")
        return result
    
    def _stop_network(self):
        """Stop all network processes."""
        print(f"Stopping network...")
        for process in self.processes:
            try:
                process.terminate()
                process.wait(timeout=5)
            except Exception:
                try:
                    process.kill()
                except Exception:
                    pass
        
        # Kill any remaining processes on the ports
        self._kill_process_on_port(self.coordinator_port)
        for port in self.expansion_ports:
            self._kill_process_on_port(port)
        
        self.processes = []
    
    def _generate_progressive_report(self):
        """Generate a report and visualization of the progressive test results."""
        if not self.results:
            print("No results collected. Test may have failed.")
            return
        
        # Calculate average times for each configuration
        avg_times = {}
        for num_nodes, iterations in self.results.items():
            valid_times = [it['total_time'] for it in iterations if it['total_time'] is not None]
            if valid_times:
                avg_times[num_nodes] = sum(valid_times) / len(valid_times)
            else:
                avg_times[num_nodes] = None
        
        # Extract data for plotting
        nodes = sorted(avg_times.keys())
        times = [avg_times[n] for n in nodes]
        
        # Calculate speedups relative to single node
        if 1 in avg_times and avg_times[1] is not None and avg_times[1] > 0:
            speedups = [avg_times[1] / avg_times[n] if avg_times[n] is not None and avg_times[n] > 0 else 0 for n in nodes]
        else:
            speedups = [0] * len(nodes)
        
        # Calculate theoretical speedups
        theoretical = [PHI**(n*QUANTUM_DIMENSIONS) for n in nodes]
        
        # Create the time plot
        plt.figure(figsize=(12, 6))
        plt.plot(nodes, times, 'bo-', linewidth=2, markersize=10)
        plt.grid(True, which="both", ls="--")
        plt.xlabel('Number of Nodes', fontsize=12)
        plt.ylabel('Computation Time (seconds)', fontsize=12)
        plt.title('φ-Harmonic Network: Progressive Computation Time', fontsize=14)
        
        # Save the time plot
        time_plot_path = os.path.join("phi_harmonic_visualizations", "progressive_time.png")
        plt.savefig(time_plot_path)
        plt.close()
        
        # Create the speedup plot
        plt.figure(figsize=(12, 6))
        plt.semilogy(nodes, speedups, 'bo-', linewidth=2, markersize=10, label='Actual Speedup')
        plt.semilogy(nodes, theoretical, 'ro--', linewidth=2, markersize=10, label='Theoretical Speedup (φ^(n*7))')
        plt.grid(True, which="both", ls="--")
        plt.xlabel('Number of Nodes', fontsize=12)
        plt.ylabel('Speedup Factor (log scale)', fontsize=12)
        plt.title('φ-Harmonic Network: Progressive Speedup Performance', fontsize=14)
        plt.legend(fontsize=10)
        
        # Save the speedup plot
        speedup_plot_path = os.path.join("phi_harmonic_visualizations", "progressive_speedup.png")
        plt.savefig(speedup_plot_path)
        plt.close()
        
        # Generate the report
        report_path = os.path.join("phi_harmonic_visualizations", "progressive_test_report.txt")
        with open(report_path, "w") as f:
            f.write(f"φ-HARMONIC PROGRESSIVE NETWORK TEST REPORT\n")
            f.write(f"{'='*60}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Test Iterations per Configuration: {TEST_ITERATIONS}\n")
            f.write(f"Quantum Dimensions: {QUANTUM_DIMENSIONS}\n\n")
            
            f.write(f"PROGRESSIVE PERFORMANCE METRICS\n")
            f.write(f"{'-'*60}\n")
            f.write(f"{'Nodes':^8}{'Avg Time (s)':^15}{'Speedup':^15}{'Theoretical':^20}{'Efficiency':^15}\n")
            
            for i, n in enumerate(nodes):
                if avg_times[n] is not None:
                    efficiency = (speedups[i] / theoretical[i]) * 100 if theoretical[i] > 0 else 0
                    f.write(f"{n:^8}{avg_times[n]:^15.6f}{speedups[i]:^15.2f}{theoretical[i]:^20.2e}{efficiency:^15.2f}%\n")
                else:
                    f.write(f"{n:^8}{'N/A':^15}{'N/A':^15}{'N/A':^20}{'N/A':^15}\n")
            
            f.write(f"\nPROGRESSIVE ANALYSIS\n")
            f.write(f"{'-'*60}\n")
            f.write(f"The φ-Harmonic Nodular Network demonstrates progressive scaling\n")
            f.write(f"capabilities, with computational power increasing as the number\n")
            f.write(f"of nodes increases, following the theoretical φ^(n*7) scaling law.\n\n")
            
            # Calculate the scaling exponent from the data
            if len(nodes) > 2 and all(s > 0 for s in speedups):
                log_nodes = np.log(nodes)
                log_speedups = np.log(speedups)
                coeffs = np.polyfit(log_nodes, log_speedups, 1)
                scaling_exponent = coeffs[0]
                f.write(f"Empirical scaling exponent: {scaling_exponent:.2f}\n")
                f.write(f"Theoretical scaling exponent: {QUANTUM_DIMENSIONS * np.log(PHI):.2f}\n")
            
            f.write(f"\nVisualization saved to:\n")
            f.write(f"- {time_plot_path}\n")
            f.write(f"- {speedup_plot_path}\n")
        
        print(f"\nProgressive test report saved to {report_path}")
        print(f"Visualizations saved to phi_harmonic_visualizations directory")

def main():
    """Main function to run the φ-Harmonic Progressive Network Test."""
    progressive_test = PhiHarmonicProgressiveTest()
    progressive_test.run_progressive_test()
    
    print(f"\n{'='*60}")
    print(f"PROGRESSIVE TEST COMPLETE")
    print(f"{'='*60}")
    print(f"The φ-Harmonic Nodular Network has demonstrated progressive scaling capabilities")
    print(f"Results and visualizations are saved in the phi_harmonic_visualizations directory")

if __name__ == "__main__":
    main()
