#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
φ-Harmonic Nodular Network Coordinator Setup
===========================================

This script sets up a coordinator node for the φ-Harmonic Nodular Network.
Run this script on the machine that will serve as the network coordinator.

Usage:
    python setup_coordinator.py [--host HOST] [--port PORT]

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import argparse
import os
import sys
import time
import socket
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNode, PhiHarmonicNodularNetwork
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation
from extensions.quantum_cosmos.phi_harmonic_supercomputing import PhiHarmonicQuantumSupercomputer

def get_local_ip():
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

def setup_coordinator(host=None, port=7272):
    """
    Set up a coordinator node for the φ-Harmonic Nodular Network.
    
    Args:
        host (str): Host address to bind to. If None, uses the local IP.
        port (int): Port to bind to.
        
    Returns:
        tuple: The node and network objects.
    """
    # Use the local IP if host is not specified
    if host is None:
        host = get_local_ip()
    
    print(f"\n{'='*50}")
    print(f"φ-HARMONIC NODULAR NETWORK COORDINATOR SETUP")
    print(f"{'='*50}")
    
    print(f"\nSetting up coordinator node at {host}:{port}...")
    
    # Initialize the computation engine
    phi_engine = PhiHarmonicComputation()
    
    # Initialize the node as coordinator
    node = PhiHarmonicNode(host=host, port=port, is_coordinator=True)
    
    # Initialize the network with this node as coordinator
    network = PhiHarmonicNodularNetwork(coordinator_host=host, coordinator_port=port)
    
    # Start the node
    node.start()
    
    # Initialize the quantum supercomputer
    supercomputer = PhiHarmonicQuantumSupercomputer(network)
    
    print(f"\nCoordinator node initialized successfully!")
    print(f"Node ID: {node.node_id[:8]}")
    print(f"Reality Integrity: {node.reality_integrity:.6f}")
    print(f"Initial Phase: {node.phase:.6f}")
    print(f"Listening on: {host}:{port}")
    
    print(f"\n{'='*50}")
    print(f"NETWORK INFORMATION")
    print(f"{'='*50}")
    print(f"To connect worker nodes to this coordinator, run:")
    print(f"python setup_worker.py --coordinator {host} --port {port}")
    print(f"\nThe network is now ready to accept connections.")
    print(f"{'='*50}\n")
    
    # Create the visualizations directory if it doesn't exist
    os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    # Save the network information to a file
    with open("phi_harmonic_visualizations/network_info.txt", "w") as f:
        f.write(f"φ-HARMONIC NODULAR NETWORK INFORMATION\n")
        f.write(f"{'='*50}\n\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Coordinator Node ID: {node.node_id[:8]}\n")
        f.write(f"Coordinator Address: {host}:{port}\n")
        f.write(f"Reality Integrity: {node.reality_integrity:.6f}\n")
        f.write(f"Initial Phase: {node.phase:.6f}\n\n")
        f.write(f"To connect worker nodes to this coordinator, run:\n")
        f.write(f"python setup_worker.py --coordinator {host} --port {port}\n")
    
    print(f"Network information saved to phi_harmonic_visualizations/network_info.txt")
    
    return node, network, supercomputer

def main():
    """Main function to set up the coordinator node."""
    parser = argparse.ArgumentParser(description='Set up a φ-Harmonic Nodular Network coordinator node.')
    parser.add_argument('--host', type=str, default=None, help='Host address to bind to. If not specified, uses the local IP.')
    parser.add_argument('--port', type=int, default=7272, help='Port to bind to.')
    
    args = parser.parse_args()
    
    node, network, supercomputer = setup_coordinator(args.host, args.port)
    
    # Keep the script running to maintain the coordinator
    try:
        print("\nCoordinator node is running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down coordinator node...")
        sys.exit(0)

if __name__ == "__main__":
    main()
