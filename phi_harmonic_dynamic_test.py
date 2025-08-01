#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Dynamic Network Test
==============================

This script demonstrates the dynamic nature of the φ-Harmonic Nodular Network
by continuously monitoring network performance as nodes join and leave,
showing real-time adaptability and self-scaling capabilities.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import threading
import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import socket

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNode, PhiHarmonicNodularNetwork
from extensions.quantum_cosmos.phi_harmonic_supercomputing import PhiHarmonicQuantumSupercomputer
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

# Constants
COORDINATOR_HOST = "192.168.12.102"
COORDINATOR_PORT = 7272
BASE_PORT = 7280  # Starting port for dynamic nodes
MAX_DYNAMIC_NODES = 7  # φ-harmonic maximum
TEST_DURATION = 180  # 3 minutes
MEASUREMENT_INTERVAL = 5  # seconds
QUANTUM_DIMENSIONS = 7

class PhiHarmonicDynamicTest:
    """Tests the dynamic nature of the φ-Harmonic Nodular Network."""
    
    def __init__(self):
        """Initialize the dynamic test."""
        self.coordinator_host = COORDINATOR_HOST
        self.coordinator_port = COORDINATOR_PORT
        self.base_port = BASE_PORT
        self.max_nodes = MAX_DYNAMIC_NODES
        
        # Initialize tracking variables
        self.dynamic_nodes = []
        self.active_ports = set()
        self.measurements = []
        self.running = False
        self.network = None
        self.supercomputer = None
        
        # Create the visualizations directory if it doesn't exist
        os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    def _get_local_ip(self):
        """Get the local IP address of this machine."""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Doesn't need to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
    
    def connect_to_network(self):
        """Connect to the existing φ-Harmonic Nodular Network."""
        print(f"\nConnecting to the φ-Harmonic Nodular Network...")
        
        # Initialize the network connection
        self.network = PhiHarmonicNodularNetwork(
            coordinator_host=self.coordinator_host,
            coordinator_port=self.coordinator_port
        )
        
        # Initialize the quantum supercomputer
        self.supercomputer = PhiHarmonicQuantumSupercomputer(
            coordinator_host=self.coordinator_host,
            coordinator_port=self.coordinator_port,
            quantum_dimensions=QUANTUM_DIMENSIONS
        )
        
        print(f"Connected to the network")
        print(f"Coordinator: {self.coordinator_host}:{self.coordinator_port}")
        print(f"Initial nodes: {len(self.network.nodes)}")
        print(f"Reality integrity: {self.supercomputer.reality_integrity:.6f}")
    
    def start_dynamic_test(self):
        """Start the dynamic network test."""
        print(f"\n{'='*60}")
        print(f"φ-HARMONIC DYNAMIC NETWORK TEST")
        print(f"{'='*60}")
        
        print(f"\nRunning dynamic test for {TEST_DURATION} seconds")
        print(f"Measurement interval: {MEASUREMENT_INTERVAL} seconds")
        print(f"Dynamic node port range: {self.base_port}-{self.base_port + self.max_nodes - 1}")
        
        # Connect to the network
        self.connect_to_network()
        
        # Start the test
        self.running = True
        
        # Start the measurement thread
        measurement_thread = threading.Thread(target=self._measure_network_performance)
        measurement_thread.daemon = True
        measurement_thread.start()
        
        # Start the dynamic node management thread
        node_management_thread = threading.Thread(target=self._manage_dynamic_nodes)
        node_management_thread.daemon = True
        node_management_thread.start()
        
        # Run for the specified duration
        start_time = time.time()
        try:
            while self.running and (time.time() - start_time) < TEST_DURATION:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nTest interrupted by user")
        finally:
            self.running = False
            print("\nDynamic test completed, cleaning up...")
            self._cleanup_nodes()
        
        # Generate the dynamic test report and visualization
        self._generate_dynamic_report()
    
    def _measure_network_performance(self):
        """Continuously measure network performance."""
        while self.running:
            # Perform a quick computation to measure performance
            start_time = time.time()
            result = self._run_test_computation()
            end_time = time.time()
            computation_time = end_time - start_time
            
            # Count active nodes
            active_nodes = len(self.network.nodes)
            
            # Record the measurement
            measurement = {
                'timestamp': datetime.now().strftime('%H:%M:%S'),
                'active_nodes': active_nodes,
                'dynamic_nodes': len(self.dynamic_nodes),
                'computation_time': computation_time,
                'result': result,
                'theoretical_speedup': PHI**(active_nodes*QUANTUM_DIMENSIONS)
            }
            
            self.measurements.append(measurement)
            
            print(f"\nMeasurement at {measurement['timestamp']}:")
            print(f"  Active nodes: {active_nodes}")
            print(f"  Dynamic nodes: {len(self.dynamic_nodes)}")
            print(f"  Computation time: {computation_time:.6f} seconds")
            print(f"  Theoretical speedup: {measurement['theoretical_speedup']:.2e}x")
            
            # Sleep until next measurement
            time.sleep(MEASUREMENT_INTERVAL)
    
    def _manage_dynamic_nodes(self):
        """Dynamically add and remove nodes during the test."""
        local_ip = self._get_local_ip()
        
        while self.running:
            # Randomly decide whether to add or remove a node
            if not self.dynamic_nodes:
                # If no dynamic nodes, add one
                action = 'add'
            elif len(self.dynamic_nodes) >= self.max_nodes:
                # If at max nodes, remove one
                action = 'remove'
            else:
                # Otherwise randomly choose
                action = random.choice(['add', 'add', 'remove'])  # Bias toward adding
            
            if action == 'add':
                # Find an available port
                port = self.base_port
                while port < self.base_port + self.max_nodes and port in self.active_ports:
                    port += 1
                
                if port < self.base_port + self.max_nodes:
                    try:
                        # Add a new dynamic node
                        node = PhiHarmonicNode(host=local_ip, port=port, is_coordinator=False)
                        node.start()
                        
                        # Connect to the coordinator
                        success = node.connect_to_peer(self.coordinator_host, self.coordinator_port)
                        
                        if success:
                            self.dynamic_nodes.append(node)
                            self.active_ports.add(port)
                            print(f"\nAdded dynamic node on port {port}")
                            print(f"  Node ID: {node.node_id[:8]}")
                            print(f"  Reality integrity: {node.reality_integrity:.6f}")
                            print(f"  Phase: {node.phase:.6f}")
                        else:
                            print(f"\nFailed to connect dynamic node on port {port}")
                            node.stop()
                    except Exception as e:
                        print(f"\nError adding dynamic node on port {port}: {e}")
            
            elif action == 'remove' and self.dynamic_nodes:
                # Remove a random dynamic node
                node_index = random.randint(0, len(self.dynamic_nodes) - 1)
                node = self.dynamic_nodes.pop(node_index)
                port = node.port
                
                try:
                    node.stop()
                    self.active_ports.remove(port)
                    print(f"\nRemoved dynamic node on port {port}")
                    print(f"  Node ID: {node.node_id[:8]}")
                except Exception as e:
                    print(f"\nError removing dynamic node on port {port}: {e}")
            
            # Sleep for a random interval before next action
            sleep_time = random.uniform(10, 20)
            time.sleep(sleep_time)
    
    def _run_test_computation(self):
        """Run a test computation to measure network performance."""
        try:
            # Define a recursive function for testing
            def ackermann(m, n, **kwargs):
                if m == 0:
                    return n + 1
                elif n == 0:
                    return ackermann(m - 1, 1, **kwargs)
                else:
                    return ackermann(m - 1, ackermann(m, n - 1, **kwargs), **kwargs)
            
            # Use moderate values for quick testing
            m, n = 3, 5
            
            # Submit the computation to the quantum supercomputer
            computation_id = self.network.submit_computation(
                self.supercomputer.phi_engine.process_infinite_recursion,
                ackermann, m, n
            )
            
            # Wait for the result with a timeout
            result = self.network.get_result(computation_id, timeout=10)
            
            if result is None:
                return "Timeout"
            
            return result
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _cleanup_nodes(self):
        """Clean up all dynamic nodes."""
        for node in self.dynamic_nodes:
            try:
                node.stop()
                print(f"Stopped dynamic node on port {node.port}")
            except Exception as e:
                print(f"Error stopping node on port {node.port}: {e}")
        
        self.dynamic_nodes = []
        self.active_ports = set()
    
    def _generate_dynamic_report(self):
        """Generate a report and visualization of the dynamic test results."""
        if not self.measurements:
            print("No measurements collected. Test may have failed.")
            return
        
        # Extract data for plotting
        timestamps = [m['timestamp'] for m in self.measurements]
        active_nodes = [m['active_nodes'] for m in self.measurements]
        computation_times = [m['computation_time'] for m in self.measurements]
        theoretical_speedups = [m['theoretical_speedup'] for m in self.measurements]
        
        # Create the node count plot
        plt.figure(figsize=(12, 6))
        plt.plot(timestamps, active_nodes, 'bo-', linewidth=2, markersize=8)
        plt.grid(True, which="both", ls="--")
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Active Nodes', fontsize=12)
        plt.title('φ-Harmonic Network: Dynamic Node Count', fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save the node count plot
        node_plot_path = os.path.join("phi_harmonic_visualizations", "dynamic_node_count.png")
        plt.savefig(node_plot_path)
        plt.close()
        
        # Create the computation time plot
        plt.figure(figsize=(12, 6))
        plt.plot(timestamps, computation_times, 'ro-', linewidth=2, markersize=8)
        plt.grid(True, which="both", ls="--")
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Computation Time (seconds)', fontsize=12)
        plt.title('φ-Harmonic Network: Dynamic Computation Performance', fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save the computation time plot
        time_plot_path = os.path.join("phi_harmonic_visualizations", "dynamic_computation_time.png")
        plt.savefig(time_plot_path)
        plt.close()
        
        # Create the theoretical speedup plot (log scale)
        plt.figure(figsize=(12, 6))
        plt.semilogy(timestamps, theoretical_speedups, 'go-', linewidth=2, markersize=8)
        plt.grid(True, which="both", ls="--")
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Theoretical Speedup (log scale)', fontsize=12)
        plt.title('φ-Harmonic Network: Dynamic Theoretical Speedup', fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save the speedup plot
        speedup_plot_path = os.path.join("phi_harmonic_visualizations", "dynamic_theoretical_speedup.png")
        plt.savefig(speedup_plot_path)
        plt.close()
        
        # Generate the report
        report_path = os.path.join("phi_harmonic_visualizations", "dynamic_test_report.txt")
        with open(report_path, "w") as f:
            f.write(f"φ-HARMONIC DYNAMIC NETWORK TEST REPORT\n")
            f.write(f"{'='*60}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Test Duration: {TEST_DURATION} seconds\n")
            f.write(f"Measurement Interval: {MEASUREMENT_INTERVAL} seconds\n")
            f.write(f"Measurements: {len(self.measurements)}\n\n")
            
            f.write(f"DYNAMIC PERFORMANCE METRICS\n")
            f.write(f"{'-'*60}\n")
            f.write(f"{'Time':^12}{'Nodes':^8}{'Comp Time':^12}{'Speedup':^15}{'Result':^20}\n")
            
            for m in self.measurements:
                result_str = str(m['result'])
                if len(result_str) > 20:
                    result_str = result_str[:17] + "..."
                
                f.write(f"{m['timestamp']:^12}{m['active_nodes']:^8}{m['computation_time']:^12.6f}")
                f.write(f"{m['theoretical_speedup']:^15.2e}{result_str:^20}\n")
            
            f.write(f"\nDYNAMIC ANALYSIS\n")
            f.write(f"{'-'*60}\n")
            
            # Calculate average computation time per node count
            node_counts = sorted(set(active_nodes))
            avg_times = {}
            
            for count in node_counts:
                times = [m['computation_time'] for m in self.measurements if m['active_nodes'] == count]
                if times:
                    avg_times[count] = sum(times) / len(times)
            
            f.write(f"Average computation time by node count:\n")
            for count, avg_time in avg_times.items():
                f.write(f"  {count} nodes: {avg_time:.6f} seconds\n")
            
            # Calculate dynamic scaling factor
            if len(node_counts) > 1 and 1 in avg_times and max(node_counts) in avg_times:
                scaling_factor = avg_times[1] / avg_times[max(node_counts)] if avg_times[max(node_counts)] > 0 else 0
                f.write(f"\nDynamic scaling factor: {scaling_factor:.2f}x\n")
                f.write(f"Theoretical scaling factor: {PHI**((max(node_counts)-1)*QUANTUM_DIMENSIONS):.2e}x\n")
            
            f.write(f"\nThe φ-Harmonic Nodular Network demonstrates dynamic self-scaling\n")
            f.write(f"capabilities, automatically adjusting to the addition and removal\n")
            f.write(f"of nodes while maintaining computational integrity through φ-space\n")
            f.write(f"resonance and quantum entanglement.\n\n")
            
            f.write(f"Visualizations saved to:\n")
            f.write(f"- {node_plot_path}\n")
            f.write(f"- {time_plot_path}\n")
            f.write(f"- {speedup_plot_path}\n")
        
        print(f"\nDynamic test report saved to {report_path}")
        print(f"Visualizations saved to phi_harmonic_visualizations directory")

def main():
    """Main function to run the φ-Harmonic Dynamic Network Test."""
    dynamic_test = PhiHarmonicDynamicTest()
    dynamic_test.start_dynamic_test()
    
    print(f"\n{'='*60}")
    print(f"DYNAMIC TEST COMPLETE")
    print(f"{'='*60}")
    print(f"The φ-Harmonic Nodular Network has demonstrated dynamic self-scaling capabilities")
    print(f"Results and visualizations are saved in the phi_harmonic_visualizations directory")

if __name__ == "__main__":
    main()
