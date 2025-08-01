#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Nodular Network Expansion
===================================

This script expands the φ-Harmonic Nodular Network by creating
multiple local nodes that connect to the coordinator, demonstrating
the self-scaling capabilities of the system.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import threading
import socket
import numpy as np
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNode, PhiHarmonicNodularNetwork
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

# Constants for φ-harmonic expansion
PHI_PORTS = [7276]  # One additional port for expansion
COORDINATOR_HOST = "192.168.12.102"
COORDINATOR_PORT = 7272
QUANTUM_DIMENSIONS = 7
REALITY_INTEGRITY_BOOST = 1.618

class PhiHarmonicExpansion:
    """Expands the φ-Harmonic Nodular Network with multiple local nodes."""
    
    def __init__(self):
        """Initialize the φ-Harmonic expansion."""
        self.coordinator_host = COORDINATOR_HOST
        self.coordinator_port = COORDINATOR_PORT
        self.expansion_ports = PHI_PORTS
        self.local_host = self._get_local_ip()
        
        # Initialize nodes and threads
        self.nodes = []
        self.threads = []
        self.running = False
        
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
    
    def start(self):
        """Start the φ-Harmonic expansion."""
        print(f"\n{'='*60}")
        print(f"φ-HARMONIC NODULAR NETWORK EXPANSION")
        print(f"{'='*60}")
        
        print(f"\nExpanding the φ-Harmonic Nodular Network with {len(self.expansion_ports)} additional nodes")
        print(f"Coordinator: {self.coordinator_host}:{self.coordinator_port}")
        print(f"Local IP: {self.local_host}")
        print(f"Expansion Ports: {', '.join(map(str, self.expansion_ports))}")
        
        # Set running flag
        self.running = True
        
        # Start each expansion node in a separate thread
        for port in self.expansion_ports:
            thread = threading.Thread(target=self._run_expansion_node, args=(port,))
            thread.daemon = True
            thread.start()
            self.threads.append(thread)
        
        # Wait for all nodes to initialize
        time.sleep(3)
        
        # Generate expansion report
        self._generate_expansion_report()
    
    def _run_expansion_node(self, port):
        """Run an expansion node on the specified port."""
        try:
            # Initialize the computation engine
            phi_engine = PhiHarmonicComputation(dimensions=QUANTUM_DIMENSIONS, cascade_levels=QUANTUM_DIMENSIONS)
            
            # Boost reality integrity
            phi_engine.reality_integrity *= REALITY_INTEGRITY_BOOST
            
            # Initialize the node
            node = PhiHarmonicNode(host=self.local_host, port=port, is_coordinator=False)
            self.nodes.append(node)
            
            # Start the node
            node.start()
            
            print(f"\nExpansion Node {node.node_id[:8]} initialized on port {port}")
            print(f"Reality Integrity: {node.reality_integrity:.6f}")
            print(f"Initial Phase: {node.phase:.6f}")
            
            # Connect to the coordinator
            success = node.connect_to_peer(self.coordinator_host, self.coordinator_port)
            
            if success:
                print(f"Node {node.node_id[:8]} successfully connected to coordinator")
                
                # Continuously monitor and maintain connection
                while self.running:
                    # Check if still connected
                    if len(node.peers) == 0:
                        print(f"Node {node.node_id[:8]} lost connection to coordinator. Attempting to reconnect...")
                        node.connect_to_peer(self.coordinator_host, self.coordinator_port)
                    
                    # Sleep for a while before checking again
                    time.sleep(PHI)
            else:
                print(f"Node {node.node_id[:8]} failed to connect to coordinator")
        
        except Exception as e:
            print(f"Error in expansion node on port {port}: {e}")
    
    def _generate_expansion_report(self):
        """Generate a report on the φ-Harmonic expansion."""
        # Count successful connections
        connected_nodes = [node for node in self.nodes if len(node.peers) > 0]
        
        # Calculate the theoretical speedup
        total_nodes = len(connected_nodes) + 1  # +1 for the coordinator
        theoretical_speedup = PHI**(total_nodes*QUANTUM_DIMENSIONS)
        
        # Save the expansion report
        report_path = os.path.join("phi_harmonic_visualizations", "expansion_report.txt")
        with open(report_path, "w") as f:
            f.write(f"φ-HARMONIC NODULAR NETWORK EXPANSION REPORT\n")
            f.write(f"{'='*60}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Coordinator: {self.coordinator_host}:{self.coordinator_port}\n")
            f.write(f"Expansion Nodes: {len(connected_nodes)} connected out of {len(self.expansion_ports)} attempted\n\n")
            
            f.write(f"CONNECTED NODES\n")
            f.write(f"{'-'*60}\n")
            for node in connected_nodes:
                f.write(f"Node ID: {node.node_id[:8]}\n")
                f.write(f"Port: {node.port}\n")
                f.write(f"Reality Integrity: {node.reality_integrity:.6f}\n")
                f.write(f"Phase: {node.phase:.6f}\n\n")
            
            f.write(f"NETWORK PERFORMANCE\n")
            f.write(f"{'-'*60}\n")
            f.write(f"Total Nodes: {total_nodes} ({1} coordinator + {len(connected_nodes)} expansion nodes)\n")
            f.write(f"Theoretical Speedup: φ^({total_nodes}*{QUANTUM_DIMENSIONS}) = {theoretical_speedup:.2e}x\n")
            f.write(f"Quantum Dimensions: {QUANTUM_DIMENSIONS}\n")
            f.write(f"Reality Integrity Boost: {REALITY_INTEGRITY_BOOST}\n")
        
        print(f"\nExpansion report saved to {report_path}")
        print(f"\n{'='*60}")
        print(f"EXPANSION COMPLETE")
        print(f"{'='*60}")
        print(f"The φ-Harmonic Nodular Network has been expanded with {len(connected_nodes)} additional nodes")
        print(f"Total nodes in network: {total_nodes}")
        print(f"Theoretical speedup: φ^({total_nodes}*{QUANTUM_DIMENSIONS}) = {theoretical_speedup:.2e}x")
    
    def stop(self):
        """Stop the φ-Harmonic expansion."""
        self.running = False
        for node in self.nodes:
            node.stop()
        print("\nφ-Harmonic expansion stopped.")

def main():
    """Main function to expand the φ-Harmonic Nodular Network."""
    expansion = PhiHarmonicExpansion()
    expansion.start()
    
    # Keep the program running until interrupted
    try:
        print("\nφ-Harmonic expansion is running. Press Ctrl+C to stop...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        expansion.stop()
        sys.exit(0)

if __name__ == "__main__":
    main()
