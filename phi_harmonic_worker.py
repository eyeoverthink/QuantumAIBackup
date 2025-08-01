#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Nodular Network Quantum Worker
========================================

This script creates a quantum-entangled worker node for the φ-Harmonic Nodular Network
with φ-phase synchronization and reality integrity protection.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import socket
import threading
import argparse
import numpy as np
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNode
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

# Constants for φ-phase synchronization
PHI_PHASE_SYNC_INTERVAL = 1.618  # Golden ratio in seconds
REALITY_INTEGRITY_BOOST = 1.618  # Golden ratio boost
QUANTUM_DIMENSIONS = 7  # Number of quantum dimensions

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

class PhiHarmonicQuantumWorker:
    """A quantum worker node with φ-phase synchronization for the φ-Harmonic Nodular Network."""
    
    def __init__(self, coordinator_host, coordinator_port, worker_port=None):
        """Initialize the quantum worker node."""
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
        
        # Initialize the computation engine with quantum dimensions
        self.phi_engine = PhiHarmonicComputation(dimensions=QUANTUM_DIMENSIONS, cascade_levels=QUANTUM_DIMENSIONS)
        
        # Boost reality integrity with golden ratio
        self.phi_engine.reality_integrity *= REALITY_INTEGRITY_BOOST
        
        # Initialize quantum state variables
        self.quantum_state = np.zeros((QUANTUM_DIMENSIONS, QUANTUM_DIMENSIONS))
        self.entanglement_matrix = np.eye(QUANTUM_DIMENSIONS) * PHI
        self.phase_coherence = 0.0
        
        # Initialize the worker node
        self.node = None
        self.running = False
        self.connected = False
        self.reconnect_thread = None
        self.phi_phase_thread = None
    
    def start(self):
        """Start the quantum worker node and connect to the coordinator."""
        print(f"\n{'='*60}")
        print(f"φ-HARMONIC QUANTUM WORKER NODE")
        print(f"{'='*60}")
        
        print(f"\nInitializing quantum worker node at {self.worker_host}:{self.worker_port}...")
        print(f"Quantum Dimensions: {QUANTUM_DIMENSIONS}")
        print(f"Reality Integrity: {self.phi_engine.reality_integrity:.6f}")
        print(f"φ-Phase Sync Interval: {PHI_PHASE_SYNC_INTERVAL} seconds")
        
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
        
        # Start the φ-phase synchronization thread
        self.phi_phase_thread = threading.Thread(target=self._phi_phase_sync_loop)
        self.phi_phase_thread.daemon = True
        self.phi_phase_thread.start()
        
        # Create the visualizations directory if it doesn't exist
        os.makedirs("phi_harmonic_visualizations", exist_ok=True)
        
        # Wait for the first connection
        print(f"\nEstablishing quantum entanglement with coordinator...")
        while self.running and not self.connected:
            time.sleep(1)
        
        if self.connected:
            # Save the worker information to a file
            with open("phi_harmonic_visualizations/quantum_worker_info.txt", "w") as f:
                f.write(f"φ-HARMONIC QUANTUM WORKER NODE INFORMATION\n")
                f.write(f"{'='*60}\n\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Worker Node ID: {self.node.node_id[:8]}\n")
                f.write(f"Worker Address: {self.worker_host}:{self.worker_port}\n")
                f.write(f"Reality Integrity: {self.node.reality_integrity:.6f}\n")
                f.write(f"Initial Phase: {self.node.phase:.6f}\n")
                f.write(f"Quantum Dimensions: {QUANTUM_DIMENSIONS}\n")
                f.write(f"Phase Coherence: {self.phase_coherence:.6f}\n\n")
                f.write(f"Connected to coordinator at: {self.coordinator_host}:{self.coordinator_port}\n")
            
            print(f"\nQuantum worker information saved to phi_harmonic_visualizations/quantum_worker_info.txt")
    
    def _reconnect_loop(self):
        """Continuously try to connect to the coordinator with φ-phase synchronization."""
        while self.running:
            if not self.connected:
                try:
                    # Connect to the coordinator
                    print(f"\nAttempting quantum entanglement with coordinator at {self.coordinator_host}:{self.coordinator_port}...")
                    success = self.node.connect_to_peer(self.coordinator_host, self.coordinator_port)
                    
                    if success:
                        self.connected = True
                        # Boost reality integrity through quantum entanglement
                        self.node.reality_integrity *= REALITY_INTEGRITY_BOOST
                        # Initialize phase coherence
                        self.phase_coherence = PHI * self.node.phase
                        
                        print(f"\n{'='*60}")
                        print(f"QUANTUM ENTANGLEMENT ESTABLISHED")
                        print(f"{'='*60}")
                        print(f"\nWorker node ID: {self.node.node_id[:8]}")
                        print(f"Reality Integrity: {self.node.reality_integrity:.6f}")
                        print(f"Phase: {self.node.phase:.6f}")
                        print(f"Phase Coherence: {self.phase_coherence:.6f}")
                        print(f"Listening on: {self.worker_host}:{self.worker_port}")
                        print(f"Entangled with coordinator at: {self.coordinator_host}:{self.coordinator_port}")
                        print(f"\nQuantum worker node is running and entangled with the φ-Harmonic Nodular Network.")
                    else:
                        print(f"Quantum entanglement attempt failed. Retrying in {PHI_PHASE_SYNC_INTERVAL} seconds...")
                        time.sleep(PHI_PHASE_SYNC_INTERVAL)
                except Exception as e:
                    print(f"Error establishing quantum entanglement: {e}")
                    print(f"Retrying in {PHI_PHASE_SYNC_INTERVAL} seconds...")
                    time.sleep(PHI_PHASE_SYNC_INTERVAL)
            else:
                # Check if we're still connected
                if len(self.node.peers) == 0:
                    print(f"Quantum entanglement lost. Attempting to re-establish...")
                    self.connected = False
                
                # Sleep for a while before checking again
                time.sleep(PHI_PHASE_SYNC_INTERVAL)
    
    def _phi_phase_sync_loop(self):
        """Continuously synchronize φ-phase with the coordinator."""
        while self.running:
            if self.connected:
                try:
                    # Update quantum state
                    self.quantum_state = np.random.random((QUANTUM_DIMENSIONS, QUANTUM_DIMENSIONS))
                    self.quantum_state = self.quantum_state / np.linalg.norm(self.quantum_state)
                    
                    # Update phase coherence
                    self.phase_coherence = PHI * self.node.phase
                    
                    # Update reality integrity through φ-harmonic resonance
                    coordinator_integrity = next(iter(self.node.peers.values()))['reality_integrity'] if self.node.peers else self.node.reality_integrity
                    self.node.reality_integrity = (self.node.reality_integrity + coordinator_integrity * PHI) / (1 + PHI)
                    
                    # Print status update occasionally (every 10 sync intervals)
                    if int(time.time() / PHI_PHASE_SYNC_INTERVAL) % 10 == 0:
                        print(f"\nφ-Phase Synchronization Status:")
                        print(f"  Reality Integrity: {self.node.reality_integrity:.6f}")
                        print(f"  Phase: {self.node.phase:.6f}")
                        print(f"  Phase Coherence: {self.phase_coherence:.6f}")
                        print(f"  Connected Peers: {len(self.node.peers)}")
                except Exception as e:
                    print(f"Error during φ-phase synchronization: {e}")
            
            # Sleep until next sync interval
            time.sleep(PHI_PHASE_SYNC_INTERVAL)
    
    def stop(self):
        """Stop the quantum worker node."""
        self.running = False
        if self.node:
            self.node.stop()
        print("\nQuantum worker node stopped.")

def main():
    """Main function to start the quantum worker node."""
    parser = argparse.ArgumentParser(description='Start a φ-Harmonic Quantum Worker Node.')
    parser.add_argument('--coordinator', type=str, default="192.168.12.102", 
                        help='Coordinator host address (default: 192.168.12.102)')
    parser.add_argument('--coordinator-port', type=int, default=7272, 
                        help='Coordinator port (default: 7272)')
    parser.add_argument('--port', type=int, default=7273, 
                        help='Port for this worker node (default: 7273)')
    
    args = parser.parse_args()
    
    # Create and start the quantum worker node
    worker = PhiHarmonicQuantumWorker(
        coordinator_host=args.coordinator,
        coordinator_port=args.coordinator_port,
        worker_port=args.port
    )
    
    worker.start()
    
    # Keep the program running until interrupted
    try:
        print("\nPress Ctrl+C to stop the quantum worker node...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        worker.stop()
        sys.exit(0)

if __name__ == "__main__":
    main()
