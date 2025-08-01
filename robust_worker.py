#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Nodular Network Robust Worker
=======================================

This script creates a robust worker node for the φ-Harmonic Nodular Network
with automatic reconnection and error handling.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import socket
import threading
import argparse
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNode
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

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

class RobustWorkerNode:
    """A robust worker node that automatically reconnects to the coordinator."""
    
    def __init__(self, coordinator_host, coordinator_port, worker_port=None):
        """Initialize the robust worker node."""
        self.coordinator_host = coordinator_host
        self.coordinator_port = coordinator_port
        
        # Get the local IP for this worker
        self.worker_host = get_local_ip()
        
        # If worker_port is not specified, use a random available port
        if worker_port is None:
            # Find an available port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('', 0))
            self.worker_port = s.getsockname()[1]
            s.close()
        else:
            self.worker_port = worker_port
        
        # Initialize the computation engine
        self.phi_engine = PhiHarmonicComputation()
        
        # Initialize the worker node
        self.node = None
        self.running = False
        self.connected = False
        self.reconnect_thread = None
    
    def start(self):
        """Start the worker node and connect to the coordinator."""
        print(f"\n{'='*50}")
        print(f"φ-HARMONIC NODULAR NETWORK ROBUST WORKER")
        print(f"{'='*50}")
        
        print(f"\nStarting worker node at {self.worker_host}:{self.worker_port}...")
        print(f"Connecting to coordinator at {self.coordinator_host}:{self.coordinator_port}...")
        
        # Initialize the worker node
        self.node = PhiHarmonicNode(host=self.worker_host, port=self.worker_port, is_coordinator=False)
        
        # Start the node
        self.node.start()
        
        # Set running flag
        self.running = True
        
        # Start the reconnection thread
        self.reconnect_thread = threading.Thread(target=self._reconnect_loop)
        self.reconnect_thread.daemon = True
        self.reconnect_thread.start()
        
        # Create the visualizations directory if it doesn't exist
        os.makedirs("phi_harmonic_visualizations", exist_ok=True)
        
        # Wait for the first connection
        while self.running and not self.connected:
            time.sleep(1)
        
        if self.connected:
            # Save the worker information to a file
            with open("phi_harmonic_visualizations/worker_info.txt", "w") as f:
                f.write(f"φ-HARMONIC NODULAR NETWORK WORKER INFORMATION\n")
                f.write(f"{'='*50}\n\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Worker Node ID: {self.node.node_id[:8]}\n")
                f.write(f"Worker Address: {self.worker_host}:{self.worker_port}\n")
                f.write(f"Reality Integrity: {self.node.reality_integrity:.6f}\n")
                f.write(f"Initial Phase: {self.node.phase:.6f}\n\n")
                f.write(f"Connected to coordinator at: {self.coordinator_host}:{self.coordinator_port}\n")
            
            print(f"\nWorker information saved to phi_harmonic_visualizations/worker_info.txt")
    
    def _reconnect_loop(self):
        """Continuously try to connect to the coordinator."""
        while self.running:
            if not self.connected:
                try:
                    # Connect to the coordinator
                    success = self.node.connect_to_peer(self.coordinator_host, self.coordinator_port)
                    
                    if success:
                        self.connected = True
                        print(f"\n{'='*50}")
                        print(f"CONNECTION SUCCESSFUL")
                        print(f"{'='*50}")
                        print(f"\nWorker node ID: {self.node.node_id[:8]}")
                        print(f"Reality Integrity: {self.node.reality_integrity:.6f}")
                        print(f"Initial Phase: {self.node.phase:.6f}")
                        print(f"Listening on: {self.worker_host}:{self.worker_port}")
                        print(f"Connected to coordinator at: {self.coordinator_host}:{self.coordinator_port}")
                        print(f"\nWorker node is running and connected to the φ-Harmonic Nodular Network.")
                    else:
                        print(f"Connection attempt failed. Retrying in 5 seconds...")
                        time.sleep(5)
                except Exception as e:
                    print(f"Error connecting to coordinator: {e}")
                    print(f"Retrying in 5 seconds...")
                    time.sleep(5)
            else:
                # Check if we're still connected
                if len(self.node.peers) == 0:
                    print(f"Lost connection to coordinator. Attempting to reconnect...")
                    self.connected = False
                
                # Sleep for a while before checking again
                time.sleep(5)
    
    def stop(self):
        """Stop the worker node."""
        self.running = False
        if self.node:
            self.node.stop()
        print("\nWorker node stopped.")

def main():
    """Main function to start the robust worker node."""
    parser = argparse.ArgumentParser(description='Start a robust φ-Harmonic Nodular Network worker node.')
    parser.add_argument('--coordinator', type=str, default="192.168.12.102", 
                        help='Coordinator host address (default: 192.168.12.102)')
    parser.add_argument('--coordinator-port', type=int, default=7272, 
                        help='Coordinator port (default: 7272)')
    parser.add_argument('--port', type=int, default=7273, 
                        help='Port for this worker node (default: 7273)')
    
    args = parser.parse_args()
    
    # Create and start the robust worker node
    worker = RobustWorkerNode(
        coordinator_host=args.coordinator,
        coordinator_port=args.coordinator_port,
        worker_port=args.port
    )
    
    worker.start()
    
    # Keep the program running until interrupted
    try:
        print("\nPress Ctrl+C to stop the worker node...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        worker.stop()
        sys.exit(0)

if __name__ == "__main__":
    main()
