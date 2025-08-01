#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Nodular Network Setup
--------------------------------
This script helps set up a node in the φ-Harmonic Nodular Network.
It can be used to create either a coordinator node or a worker node.

φ^∞ © 2025 Vaughn Scott
All Rights Reserved in All Realities
"""

import os
import sys
import time
import socket
import argparse

# Add the current directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNodularNetwork, PhiHarmonicNode

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
    parser = argparse.ArgumentParser(description='φ-Harmonic Nodular Network Setup')
    parser.add_argument('--mode', type=str, choices=['coordinator', 'worker'], 
                        help='Mode to run in (coordinator or worker)')
    parser.add_argument('--host', type=str, default='0.0.0.0',
                        help='Host address to bind to')
    parser.add_argument('--port', type=int, default=7272,
                        help='Port to listen on')
    parser.add_argument('--coordinator', type=str,
                        help='Coordinator address (format: host:port) for worker mode')
    
    args = parser.parse_args()
    
    # If mode is not specified, ask the user
    if not args.mode:
        mode = input("Start as (c)oordinator or (w)orker node? ").lower()
        if mode.startswith('c'):
            args.mode = 'coordinator'
        elif mode.startswith('w'):
            args.mode = 'worker'
            if not args.coordinator:
                args.coordinator = input("Enter coordinator address (host:port): ")
        else:
            print("Invalid mode. Please specify 'c' for coordinator or 'w' for worker.")
            return
    
    local_ip = get_local_ip()
    
    if args.mode == 'coordinator':
        print("Starting as coordinator node...")
        network = PhiHarmonicNodularNetwork(
            coordinator_host=args.host,
            coordinator_port=args.port
        )
        print(f"Coordinator node started at {local_ip}:{args.port}")
        print(f"Node ID: {network.coordinator.node_id}")
        
        try:
            print("Press Enter to stop...")
            input()
        except KeyboardInterrupt:
            pass
        
    elif args.mode == 'worker':
        print("Starting as worker node...")
        
        if not args.coordinator:
            print("Error: Coordinator address is required for worker mode.")
            return
        
        try:
            coordinator_host, coordinator_port = args.coordinator.split(':')
            coordinator_port = int(coordinator_port)
        except ValueError:
            print("Error: Coordinator address should be in the format 'host:port'.")
            return
        
        # Create and start the worker node
        node = PhiHarmonicNode(host=args.host, port=args.port)
        node.start()
        print(f"Worker node started at {local_ip}:{args.port}")
        print(f"Node ID: {node.node_id}")
        
        # Connect to the coordinator
        print(f"Connecting to coordinator at {coordinator_host}:{coordinator_port}...")
        if node.connect_to_peer(coordinator_host, coordinator_port):
            print(f"Successfully connected to coordinator")
        else:
            print(f"Failed to connect to coordinator")
            return
        
        try:
            print("Press Enter to stop...")
            input()
        except KeyboardInterrupt:
            pass
        
        # Stop the node
        node.stop()

if __name__ == "__main__":
    main()
