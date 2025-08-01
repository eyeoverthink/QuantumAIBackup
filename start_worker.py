#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Nodular Network Worker Starter
=========================================

This script starts a worker node for the φ-Harmonic Nodular Network.
Run this script on machines that will serve as worker nodes in the network.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import socket
import argparse

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNode
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

def main():
    """Main function to start the worker node."""
    parser = argparse.ArgumentParser(description='Start a φ-Harmonic Nodular Network worker node.')
    parser.add_argument('--connect', type=str, required=True, help='Coordinator address to connect to (format: host:port)')
    parser.add_argument('--host', type=str, default=None, help='Host address to bind to. If not specified, uses the local IP.')
    parser.add_argument('--port', type=int, default=7273, help='Port to bind to.')
    
    args = parser.parse_args()
    
    # Use the local IP if host is not specified
    worker_host = args.host if args.host else get_local_ip()
    worker_port = args.port
    
    # Parse the coordinator address
    coordinator_host, coordinator_port = args.connect.split(':')
    coordinator_port = int(coordinator_port)
    
    print(f"\n{'='*50}")
    print(f"φ-HARMONIC NODULAR NETWORK WORKER")
    print(f"{'='*50}")
    
    print(f"\nStarting worker node at {worker_host}:{worker_port}...")
    print(f"Connecting to coordinator at {coordinator_host}:{coordinator_port}...")
    
    # Initialize the computation engine
    phi_engine = PhiHarmonicComputation()
    
    # Initialize the worker node
    node = PhiHarmonicNode(host=worker_host, port=worker_port, is_coordinator=False)
    
    # Start the node
    node.start()
    
    # Connect to the coordinator
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
            f.write(f"Worker Node ID: {node.node_id[:8]}\n")
            f.write(f"Worker Address: {worker_host}:{worker_port}\n")
            f.write(f"Reality Integrity: {node.reality_integrity:.6f}\n")
            f.write(f"Initial Phase: {node.phase:.6f}\n\n")
            f.write(f"Connected to coordinator at: {coordinator_host}:{coordinator_port}\n")
        
        print(f"\nWorker information saved to phi_harmonic_visualizations/worker_info.txt")
        print(f"\nWorker node is running. Press Ctrl+C to stop.")
        
        # Keep the program running
        try:
            while True:
                import time
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down worker node...")
            sys.exit(0)
    else:
        print(f"\nFailed to connect to coordinator at {coordinator_host}:{coordinator_port}")
        print(f"Please ensure the coordinator is running and the address is correct.")
        sys.exit(1)

if __name__ == "__main__":
    main()
