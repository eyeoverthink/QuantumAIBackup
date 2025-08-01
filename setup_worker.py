#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
φ-Harmonic Nodular Network Worker Setup
=======================================

This script sets up a worker node for the φ-Harmonic Nodular Network.
Run this script on machines that will serve as worker nodes in the network.

Usage:
    python setup_worker.py --coordinator COORDINATOR_IP [--port PORT]

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

def setup_worker(coordinator_host, coordinator_port=7272, worker_port=None):
    """
    Set up a worker node for the φ-Harmonic Nodular Network.
    
    Args:
        coordinator_host (str): Host address of the coordinator node.
        coordinator_port (int): Port of the coordinator node.
        worker_port (int): Port for this worker node to listen on. If None, uses a random available port.
        
    Returns:
        tuple: The node and network objects.
    """
    # Get the local IP for this worker
    worker_host = get_local_ip()
    
    # If worker_port is not specified, use a random available port
    if worker_port is None:
        # Find an available port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 0))
        worker_port = s.getsockname()[1]
        s.close()
    
    print(f"\n{'='*50}")
    print(f"φ-HARMONIC NODULAR NETWORK WORKER SETUP")
    print(f"{'='*50}")
    
    print(f"\nSetting up worker node at {worker_host}:{worker_port}...")
    print(f"Connecting to coordinator at {coordinator_host}:{coordinator_port}...")
    
    # Initialize the computation engine
    phi_engine = PhiHarmonicComputation()
    
    # Initialize the worker node
    node = PhiHarmonicNode(host=worker_host, port=worker_port, is_coordinator=False)
    
    # Start the node
    node.start()
    
    # Connect to the network
    network = PhiHarmonicNodularNetwork(coordinator_host=coordinator_host, coordinator_port=coordinator_port)
    
    # Connect this node to the coordinator
    success = node.connect_to_peer(coordinator_host, coordinator_port)
    
    if success:
        print(f"\nWorker node initialized and connected successfully!")
        print(f"Node ID: {node.node_id[:8]}")
        print(f"Reality Integrity: {node.reality_integrity:.6f}")
        print(f"Initial Phase: {node.phase:.6f}")
        print(f"Listening on: {worker_host}:{worker_port}")
        print(f"Connected to coordinator at: {coordinator_host}:{coordinator_port}")
        
        # Create the visualizations directory if it doesn't exist
        os.makedirs("phi_harmonic_visualizations", exist_ok=True)
        
        # Save the worker information to a file
        with open("phi_harmonic_visualizations/worker_info.txt", "w") as f:
            f.write(f"φ-HARMONIC NODULAR NETWORK WORKER INFORMATION\n")
            f.write(f"{'='*50}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Worker Node ID: {node.id}\n")
            f.write(f"Worker Address: {worker_host}:{worker_port}\n")
            f.write(f"Reality Integrity: {node.reality_integrity:.6f}\n")
            f.write(f"Initial Phase: {node.phase:.6f}\n\n")
            f.write(f"Connected to coordinator at: {coordinator_host}:{coordinator_port}\n")
        
        print(f"\nWorker information saved to phi_harmonic_visualizations/worker_info.txt")
        print(f"{'='*50}\n")
        
        return node, network
    else:
        print(f"\nFailed to connect to coordinator at {coordinator_host}:{coordinator_port}")
        print(f"Please ensure the coordinator is running and the address is correct.")
        print(f"{'='*50}\n")
        return None, None

def main():
    """Main function to set up the worker node."""
    parser = argparse.ArgumentParser(description='Set up a φ-Harmonic Nodular Network worker node.')
    parser.add_argument('--coordinator', type=str, required=True, help='Host address of the coordinator node.')
    parser.add_argument('--port', type=int, default=7272, help='Port of the coordinator node.')
    parser.add_argument('--worker-port', type=int, default=None, help='Port for this worker node to listen on. If not specified, uses a random available port.')
    
    args = parser.parse_args()
    
    node, network = setup_worker(args.coordinator, args.port, args.worker_port)
    
    if node is not None:
        # Keep the script running to maintain the worker
        try:
            print("\nWorker node is running. Press Ctrl+C to stop.")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down worker node...")
            sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
