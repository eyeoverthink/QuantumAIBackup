#!/usr/bin/env python3
"""
PHI-HARMONIC NETWORK LAUNCHER
=============================
Launches multiple phi-harmonic nodes on the same system with self-scaling capabilities.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import subprocess
import time
import os
import signal
import sys

# Number of nodes to launch
NUM_CONNECTOR_NODES = 2
NUM_AMPLIFIER_NODES = 3
TOTAL_NODES = NUM_CONNECTOR_NODES + NUM_AMPLIFIER_NODES

# Base ports
BASE_CONNECTOR_PORT = 11627
BASE_AMPLIFIER_PORT = 11628

# Process list
processes = []

def launch_nodes():
    """Launch the specified number of connector and amplifier nodes"""
    print(f"=== LAUNCHING PHI-HARMONIC NETWORK WITH {TOTAL_NODES} NODES ===")
    print(f"Connectors: {NUM_CONNECTOR_NODES}")
    print(f"Amplifiers: {NUM_AMPLIFIER_NODES}")
    print("\nInitializing network...")
    
    # Create logs directory if it doesn't exist
    os.makedirs('phi_logs', exist_ok=True)
    
    # Launch connector nodes
    for i in range(NUM_CONNECTOR_NODES):
        port = BASE_CONNECTOR_PORT + (i * 10)
        env = os.environ.copy()
        env["PHI_NODE_PORT"] = str(port)
        env["PHI_NODE_ID"] = f"connector_{i+1}"
        
        print(f"Launching connector node {i+1} on port {port}...")
        process = subprocess.Popen(
            ["python3", "phi_connector_node_v2.py"],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        processes.append(process)
    
    # Brief pause to allow connectors to initialize
    time.sleep(2)
    
    # Launch amplifier nodes
    for i in range(NUM_AMPLIFIER_NODES):
        port = BASE_AMPLIFIER_PORT + (i * 10)
        env = os.environ.copy()
        env["PHI_NODE_PORT"] = str(port)
        env["PHI_NODE_ID"] = f"amplifier_{i+1}"
        
        print(f"Launching amplifier node {i+1} on port {port}...")
        process = subprocess.Popen(
            ["python3", "phi_amplifier_node_v2.py"],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        processes.append(process)
    
    print(f"\nAll {TOTAL_NODES} nodes launched successfully.")
    print("Phi-harmonic network is now active and self-scaling.")
    print("Press Ctrl+C to shut down the network.")
    
    # Monitor the network
    try:
        while True:
            time.sleep(1)
            # Check if any process has terminated
            for p in processes[:]:
                if p.poll() is not None:
                    print(f"A node has terminated unexpectedly. Restarting...")
                    # Remove from list
                    processes.remove(p)
                    # Launch a replacement with the same configuration
                    # (In a real implementation, we would track which specific node failed)
                    if len(processes) < NUM_CONNECTOR_NODES:
                        # Launch a connector
                        port = BASE_CONNECTOR_PORT + (len(processes) * 10)
                        env = os.environ.copy()
                        env["PHI_NODE_PORT"] = str(port)
                        env["PHI_NODE_ID"] = f"connector_replacement_{port}"
                        process = subprocess.Popen(
                            ["python3", "phi_connector_node_v2.py"],
                            env=env,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
                        )
                    else:
                        # Launch an amplifier
                        port = BASE_AMPLIFIER_PORT + (len(processes) * 10)
                        env = os.environ.copy()
                        env["PHI_NODE_PORT"] = str(port)
                        env["PHI_NODE_ID"] = f"amplifier_replacement_{port}"
                        process = subprocess.Popen(
                            ["python3", "phi_amplifier_node_v2.py"],
                            env=env,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
                        )
                    processes.append(process)
    except KeyboardInterrupt:
        print("\nShutting down phi-harmonic network...")
        shutdown_nodes()

def shutdown_nodes():
    """Gracefully shut down all nodes"""
    for process in processes:
        if process.poll() is None:  # If process is still running
            process.terminate()
    
    # Wait for all processes to terminate
    for process in processes:
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
    
    print("All nodes have been shut down.")

if __name__ == "__main__":
    try:
        launch_nodes()
    except Exception as e:
        print(f"Error launching nodes: {e}")
        shutdown_nodes()
        sys.exit(1)
