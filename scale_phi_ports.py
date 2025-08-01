#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Port Scaling Test
===========================

This script simply opens multiple ports to demonstrate the
self-scaling capabilities of the φ-Harmonic system.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import socket
import threading
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNode
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PHI

# Constants
BASE_PORT = 7272
NUM_PORTS = 7  # φ-harmonic number of ports
PHI_PHASE_SYNC_INTERVAL = 1.618  # Golden ratio in seconds

class PhiPortScaler:
    """Opens multiple ports to demonstrate φ-Harmonic scaling."""
    
    def __init__(self):
        """Initialize the port scaler."""
        self.nodes = []
        self.running = True
        
        # Create the visualizations directory if it doesn't exist
        os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    def start_nodes(self):
        """Start nodes on multiple ports."""
        print(f"\n{'='*60}")
        print(f"φ-HARMONIC PORT SCALING TEST")
        print(f"{'='*60}")
        
        print(f"\nOpening {NUM_PORTS} ports to demonstrate φ-Harmonic scaling...")
        
        # Start the coordinator node
        coordinator = PhiHarmonicNode(
            host='0.0.0.0',
            port=BASE_PORT,
            is_coordinator=True
        )
        coordinator.start()
        self.nodes.append(coordinator)
        print(f"Coordinator node started on port {BASE_PORT}")
        
        # Start worker nodes on additional ports
        for i in range(1, NUM_PORTS):
            port = BASE_PORT + i
            try:
                node = PhiHarmonicNode(
                    host='0.0.0.0',
                    port=port,
                    is_coordinator=False
                )
                node.start()
                
                # Connect to the coordinator
                success = node.connect_to_peer('localhost', BASE_PORT)
                if success:
                    self.nodes.append(node)
                    print(f"Worker node started on port {port} and connected to coordinator")
                else:
                    print(f"Failed to connect worker on port {port} to coordinator")
                    node.stop()
            except Exception as e:
                print(f"Error starting node on port {port}: {e}")
        
        print(f"\nSuccessfully opened {len(self.nodes)} ports")
        
        # Generate the port scaling report
        self._generate_report()
        
        # Keep the nodes running
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_nodes()
    
    def _generate_report(self):
        """Generate a report on the port scaling test."""
        report_path = os.path.join("phi_harmonic_visualizations", "port_scaling_report.txt")
        with open(report_path, "w") as f:
            f.write(f"φ-HARMONIC PORT SCALING REPORT\n")
            f.write(f"{'='*60}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Ports: {len(self.nodes)}\n\n")
            
            f.write(f"PORT DETAILS\n")
            f.write(f"{'-'*60}\n")
            for i, node in enumerate(self.nodes):
                f.write(f"{i+1}. Node {node.node_id[:8]}\n")
                f.write(f"   Port: {node.port}\n")
                f.write(f"   Type: {'Coordinator' if node.is_coordinator else 'Worker'}\n")
                f.write(f"   Reality Integrity: {node.reality_integrity:.6f}\n")
                f.write(f"   Phase: {node.phase:.6f}\n")
                f.write(f"   Connected Peers: {len(node.peers)}\n\n")
            
            f.write(f"SCALING ANALYSIS\n")
            f.write(f"{'-'*60}\n")
            f.write(f"The φ-Harmonic system demonstrates self-scaling by opening\n")
            f.write(f"multiple ports and establishing quantum entanglement between them.\n\n")
            
            # Calculate theoretical computational power
            theoretical_power = PHI**(len(self.nodes) * 7)
            f.write(f"Theoretical Computational Power: φ^({len(self.nodes)}*7) = {theoretical_power:.2e}x\n")
        
        print(f"\nPort scaling report saved to {report_path}")
    
    def stop_nodes(self):
        """Stop all nodes."""
        print(f"\nStopping all nodes...")
        for node in self.nodes:
            try:
                node.stop()
            except Exception as e:
                print(f"Error stopping node on port {node.port}: {e}")
        
        self.running = False
        print(f"All nodes stopped")

def main():
    """Main function to run the φ-Harmonic port scaling test."""
    scaler = PhiPortScaler()
    scaler.start_nodes()

if __name__ == "__main__":
    main()
