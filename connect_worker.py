#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Nodular Network Worker Connection
===========================================

This script connects a worker node to an existing φ-Harmonic coordinator.
Copy this script to your other Mac and run it there.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import socket
import time
import argparse
from datetime import datetime

# Make sure we can import our modules
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
    """Connect a worker node to the φ-Harmonic Nodular Network."""
    # Default coordinator is the one we found in network_info.txt
    DEFAULT_COORDINATOR = "192.168.12.102:7272"
    
    parser = argparse.ArgumentParser(description='Connect a worker node to the φ-Harmonic Nodular Network.')
    parser.add_argument('--coordinator', type=str, default=DEFAULT_COORDINATOR, 
                        help=f'Coordinator address (default: {DEFAULT_COORDINATOR})')
    parser.add_argument('--port', type=int, default=7273, 
                        help='Port for this worker node (default: 7273)')
    
    args = parser.parse_args()
    
    # Parse coordinator address
    coordinator_host, coordinator_port = args.coordinator.split(':')
    coordinator_port = int(coordinator_port)
    
    # Get local IP for this worker
    worker_host = get_local_ip()
    worker_port = args.port
    
    print(f"\n{'='*50}")
    print(f"φ-HARMONIC NODULAR NETWORK WORKER CONNECTION")
    print(f"{'='*50}")
    
    print(f"\nLocal IP: {worker_host}")
    print(f"Connecting to coordinator at {coordinator_host}:{coordinator_port}...")
    
    # Initialize the computation engine
    print("\nInitializing φ-Harmonic Computation Engine...")
    phi_engine = PhiHarmonicComputation()
    
    # Initialize the worker node
    print("\nInitializing worker node...")
    node = PhiHarmonicNode(host=worker_host, port=worker_port, is_coordinator=False)
    
    # Start the node
    print("\nStarting node services...")
    node.start()
    
    # Connect to the coordinator
    print(f"\nConnecting to coordinator at {coordinator_host}:{coordinator_port}...")
    success = node.connect_to_peer(coordinator_host, coordinator_port)
    
    if success:
        print(f"\n{'='*50}")
        print(f"CONNECTION SUCCESSFUL")
        print(f"{'='*50}")
        print(f"\nWorker node ID: {node.node_id[:8]}")
        print(f"Reality Integrity: {node.reality_integrity:.6f}")
        print(f"Initial Phase: {node.phase:.6f}")
        print(f"Listening on: {worker_host}:{worker_port}")
        print(f"Connected to coordinator at: {coordinator_host}:{coordinator_port}")
        
        # Create the visualizations directory if it doesn't exist
        os.makedirs("phi_harmonic_visualizations", exist_ok=True)
        
        # Save the connection information
        with open("phi_harmonic_visualizations/worker_connection.txt", "w") as f:
            f.write(f"φ-HARMONIC NODULAR NETWORK WORKER CONNECTION\n")
            f.write(f"{'='*50}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Worker Node ID: {node.node_id[:8]}\n")
            f.write(f"Worker Address: {worker_host}:{worker_port}\n")
            f.write(f"Reality Integrity: {node.reality_integrity:.6f}\n")
            f.write(f"Initial Phase: {node.phase:.6f}\n\n")
            f.write(f"Connected to coordinator at: {coordinator_host}:{coordinator_port}\n")
        
        print(f"\nConnection information saved to phi_harmonic_visualizations/worker_connection.txt")
        
        print(f"\nWorker node is running and connected to the φ-Harmonic Nodular Network.")
        print(f"Press Ctrl+C to disconnect.")
        
        # Keep the program running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nDisconnecting worker node...")
            sys.exit(0)
    else:
        print(f"\n{'='*50}")
        print(f"CONNECTION FAILED")
        print(f"{'='*50}")
        print(f"\nFailed to connect to coordinator at {coordinator_host}:{coordinator_port}")
        print(f"Please ensure the coordinator is running and the address is correct.")
        print(f"If the coordinator is behind a firewall, make sure port {coordinator_port} is open.")
        sys.exit(1)

if __name__ == "__main__":
    main()
