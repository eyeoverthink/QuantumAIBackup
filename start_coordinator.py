#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Nodular Network Coordinator Starter
==============================================

This script starts a coordinator node for the φ-Harmonic Nodular Network.
Run this script on the machine that will serve as the network coordinator.

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

def main():
    """Main function to start the coordinator node."""
    parser = argparse.ArgumentParser(description='Start a φ-Harmonic Nodular Network coordinator node.')
    parser.add_argument('--host', type=str, default=None, help='Host address to bind to. If not specified, uses the local IP.')
    parser.add_argument('--port', type=int, default=7272, help='Port to bind to.')
    
    args = parser.parse_args()
    
    # Use the local IP if host is not specified
    host = args.host if args.host else get_local_ip()
    port = args.port
    
    print(f"\n{'='*50}")
    print(f"φ-HARMONIC NODULAR NETWORK COORDINATOR")
    print(f"{'='*50}")
    
    print(f"\nStarting coordinator node at {host}:{port}...")
    
    # Create the visualizations directory if it doesn't exist
    os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    # Save the network information to a file
    with open("phi_harmonic_visualizations/network_info.txt", "w") as f:
        f.write(f"φ-HARMONIC NODULAR NETWORK INFORMATION\n")
        f.write(f"{'='*50}\n\n")
        f.write(f"Coordinator Address: {host}:{port}\n\n")
        f.write(f"To connect worker nodes to this coordinator, run on the other machine:\n")
        f.write(f"python start_worker.py --connect {host}:{port}\n")
    
    print(f"Network information saved to phi_harmonic_visualizations/network_info.txt")
    print(f"To connect worker nodes to this coordinator, run on the other machine:")
    print(f"python start_worker.py --connect {host}:{port}")
    
    # Start the coordinator using the built-in functionality
    supercomputer = PhiHarmonicQuantumSupercomputer(
        coordinator_host=host,
        coordinator_port=port
    )
    
    print(f"\nCoordinator node is running. Press Ctrl+C to stop.")
    
    # Keep the program running
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down coordinator node...")
        sys.exit(0)

if __name__ == "__main__":
    main()
