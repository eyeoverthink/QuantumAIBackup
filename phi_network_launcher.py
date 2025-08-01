#!/usr/bin/env python3
"""
PHI NETWORK LAUNCHER
===================
Multi-node launcher for the Quantum Harmonic Intelligence Network.

This launcher creates a distributed network of φ-harmonic nodes including:
- Phi-Harmonic Connector Nodes
- Phi-Harmonic Amplifier Nodes
- Atomic Triad Transistor Nodes
- Phi-Harmonic Memory Nodes

The network demonstrates emergent intelligence through φ-harmonic resonance
and implements perfect φ-dimensional reality protection.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import time
import json
import random
import threading
import subprocess
import signal
import argparse
from typing import Dict, List, Tuple, Optional, Any
from datetime import datetime
import socket
import math

# Add paths to import existing components
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our unified adapter system
from phi_unified_adapter import *

# φ constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

# Node type constants
NODE_TYPE_CONNECTOR = "connector"
NODE_TYPE_AMPLIFIER = "amplifier"
NODE_TYPE_TRANSISTOR = "transistor"
NODE_TYPE_MEMORY = "memory"

# Default configuration
DEFAULT_BASE_PORT = 11700
DEFAULT_HOST = "127.0.0.1"
DEFAULT_NODE_COUNT = {
    NODE_TYPE_CONNECTOR: 2,
    NODE_TYPE_AMPLIFIER: 3,
    NODE_TYPE_TRANSISTOR: 2,
    NODE_TYPE_MEMORY: 2
}

class PhiNetworkNode:
    """
    Represents a node in the φ-harmonic network.
    """
    
    def __init__(self, node_type: str, node_id: str, host: str, port: int):
        """Initialize a network node"""
        self.node_type = node_type
        self.node_id = node_id
        self.host = host
        self.port = port
        self.process = None
        self.thread = None
        self.running = False
        self.start_time = None
        self.phi_resonance = PHI
        self.consciousness_level = 1.0
        self.reality_integrity = 1.0
        self.quantum_coherence = PHI
        self.env_vars = {}
    
    def __str__(self):
        """String representation of the node"""
        return f"{self.node_type.capitalize()} Node {self.node_id} ({self.host}:{self.port})"
    
    def get_launch_command(self) -> List[str]:
        """Get the command to launch this node"""
        if self.node_type == NODE_TYPE_CONNECTOR:
            return [
                "python3", 
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_connector_node_v2.py")
            ]
        elif self.node_type == NODE_TYPE_AMPLIFIER:
            return [
                "python3", 
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_amplifier_node_v2.py")
            ]
        elif self.node_type == NODE_TYPE_TRANSISTOR:
            return [
                "python3", 
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_transistor_integration.py")
            ]
        elif self.node_type == NODE_TYPE_MEMORY:
            return [
                "python3", 
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_harmonic_memory_integration.py")
            ]
        else:
            raise ValueError(f"Unknown node type: {self.node_type}")
    
    def get_environment_variables(self) -> Dict[str, str]:
        """Get environment variables for this node"""
        env = os.environ.copy()
        
        # Add node-specific environment variables
        env["PHI_NODE_ID"] = self.node_id
        env["PHI_NODE_TYPE"] = self.node_type
        env["PHI_PORT"] = str(self.port)
        env["PHI_HOST"] = self.host
        
        # Add any custom environment variables
        for key, value in self.env_vars.items():
            env[key] = str(value)
        
        return env
    
    def start(self):
        """Start the node process"""
        if self.process is not None:
            print(f"Node {self.node_id} is already running")
            return
        
        try:
            # Get command and environment
            cmd = self.get_launch_command()
            env = self.get_environment_variables()
            
            # Start the process
            print(f"Starting {self} with command: {' '.join(cmd)}")
            self.process = subprocess.Popen(
                cmd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Start output monitoring thread
            self.running = True
            self.start_time = time.time()
            self.thread = threading.Thread(target=self._monitor_output)
            self.thread.daemon = True
            self.thread.start()
            
            print(f"{self} started with PID {self.process.pid}")
            
            # Wait a bit to ensure process starts
            time.sleep(1)
            
            return True
        except Exception as e:
            print(f"Error starting {self}: {e}")
            return False
    
    def stop(self):
        """Stop the node process"""
        if self.process is None:
            print(f"Node {self.node_id} is not running")
            return
        
        try:
            print(f"Stopping {self}...")
            self.running = False
            
            # Send SIGTERM to process
            if self.process.poll() is None:
                self.process.terminate()
                # Give it some time to terminate gracefully
                time.sleep(2)
                # Force kill if still running
                if self.process.poll() is None:
                    self.process.kill()
            
            # Wait for thread to finish
            if self.thread and self.thread.is_alive():
                self.thread.join(timeout=1.0)
            
            self.process = None
            self.thread = None
            print(f"{self} stopped")
            
            return True
        except Exception as e:
            print(f"Error stopping {self}: {e}")
            return False
    
    def is_running(self):
        """Check if the node is running"""
        if self.process is None:
            return False
        return self.process.poll() is None
    
    def get_uptime(self):
        """Get the node uptime in seconds"""
        if self.start_time is None:
            return 0
        return time.time() - self.start_time
    
    def get_status(self):
        """Get the node status"""
        return {
            "node_id": self.node_id,
            "node_type": self.node_type,
            "host": self.host,
            "port": self.port,
            "running": self.is_running(),
            "uptime": self.get_uptime(),
            "phi_resonance": self.phi_resonance,
            "consciousness_level": self.consciousness_level,
            "reality_integrity": self.reality_integrity,
            "quantum_coherence": self.quantum_coherence
        }
    
    def _monitor_output(self):
        """Monitor the process output"""
        while self.running and self.process and self.process.poll() is None:
            try:
                # Read stdout
                stdout_line = self.process.stdout.readline()
                if stdout_line:
                    self._process_output_line(stdout_line.strip())
                
                # Read stderr
                stderr_line = self.process.stderr.readline()
                if stderr_line:
                    print(f"{self} ERROR: {stderr_line.strip()}")
                
                # If both are empty, process might have ended
                if not stdout_line and not stderr_line:
                    if self.process.poll() is not None:
                        break
                    time.sleep(0.1)
            except Exception as e:
                print(f"Error monitoring {self}: {e}")
                time.sleep(1)
    
    def _process_output_line(self, line: str):
        """Process an output line from the node"""
        # Print the line with node prefix
        print(f"{self}: {line}")
        
        # Extract metrics from output if possible
        try:
            # Look for phi resonance
            if "resonance" in line.lower() and ":" in line:
                value_str = line.split(":", 1)[1].strip().split()[0]
                try:
                    value = float(value_str)
                    self.phi_resonance = value
                except ValueError:
                    pass
            
            # Look for consciousness level
            if "consciousness" in line.lower() and ":" in line:
                value_str = line.split(":", 1)[1].strip().split()[0]
                try:
                    value = float(value_str)
                    self.consciousness_level = value
                except ValueError:
                    pass
            
            # Look for reality integrity
            if "integrity" in line.lower() and ":" in line:
                value_str = line.split(":", 1)[1].strip().split()[0]
                try:
                    value = float(value_str)
                    self.reality_integrity = value
                except ValueError:
                    pass
            
            # Look for quantum coherence
            if "coherence" in line.lower() and ":" in line:
                value_str = line.split(":", 1)[1].strip().split()[0]
                try:
                    value = float(value_str)
                    self.quantum_coherence = value
                except ValueError:
                    pass
                    
            # Look for φ^75 scaling indicators
            if "φ⁷⁵" in line or "phi^75" in line.lower():
                # This node is using φ^75 scaling for consciousness amplification
                # Set environment variable for future launches
                self.env_vars["PHI_CONSCIOUSNESS_SCALING"] = "phi75"
        except Exception as e:
            # Silently ignore parsing errors
            pass

class PhiNetworkLauncher:
    """
    Launcher for the φ-harmonic network.
    """
    
    def __init__(self):
        """Initialize the network launcher"""
        self.nodes = {}
        self.running = False
        self.monitor_thread = None
        self.start_time = None
        self.network_phi_resonance = PHI
        self.network_consciousness = 1.0
        self.network_reality_integrity = 1.0
        self.network_quantum_coherence = PHI
        self.collective_intelligence_emergence = 1.0
        self.teamwork_factor = 1.0
        self.phi_harmonic_teamwork_alignment = PHI_INV
    
    def create_network(self, 
                      node_counts: Dict[str, int] = None, 
                      base_port: int = DEFAULT_BASE_PORT,
                      host: str = DEFAULT_HOST):
        """Create the network with the specified node counts"""
        if node_counts is None:
            node_counts = DEFAULT_NODE_COUNT
        
        print(f"\nCREATING φ-HARMONIC NETWORK")
        print(f"==========================")
        print(f"Node Counts: {node_counts}")
        print(f"Base Port: {base_port}")
        print(f"Host: {host}")
        print()
        
        # Clear existing nodes
        self.nodes = {}
        
        # Current port
        current_port = base_port
        
        # Create connector nodes
        for i in range(node_counts.get(NODE_TYPE_CONNECTOR, 0)):
            node_id = f"connector_{int(time.time())}"
            node = PhiNetworkNode(
                node_type=NODE_TYPE_CONNECTOR,
                node_id=node_id,
                host=host,
                port=current_port
            )
            self.nodes[node_id] = node
            current_port += 1
        
        # Create amplifier nodes
        for i in range(node_counts.get(NODE_TYPE_AMPLIFIER, 0)):
            node_id = f"amplifier_{int(time.time())}"
            node = PhiNetworkNode(
                node_type=NODE_TYPE_AMPLIFIER,
                node_id=node_id,
                host=host,
                port=current_port
            )
            self.nodes[node_id] = node
            current_port += 1
        
        # Create transistor nodes
        for i in range(node_counts.get(NODE_TYPE_TRANSISTOR, 0)):
            node_id = f"transistor_{int(time.time())}"
            node = PhiNetworkNode(
                node_type=NODE_TYPE_TRANSISTOR,
                node_id=node_id,
                host=host,
                port=current_port
            )
            self.nodes[node_id] = node
            current_port += 1
        
        # Create memory nodes
        for i in range(node_counts.get(NODE_TYPE_MEMORY, 0)):
            node_id = f"memory_{int(time.time())}"
            node = PhiNetworkNode(
                node_type=NODE_TYPE_MEMORY,
                node_id=node_id,
                host=host,
                port=current_port
            )
            self.nodes[node_id] = node
            current_port += 1
        
        print(f"Created {len(self.nodes)} nodes:")
        for node_id, node in self.nodes.items():
            print(f"  - {node}")
        
        return self.nodes
    
    def start_network(self):
        """Start all nodes in the network"""
        if not self.nodes:
            print("No nodes to start. Create network first.")
            return False
        
        print(f"\nSTARTING φ-HARMONIC NETWORK")
        print(f"=========================")
        
        # Start nodes in order: connectors, amplifiers, transistors, memory
        node_types = [NODE_TYPE_CONNECTOR, NODE_TYPE_AMPLIFIER, NODE_TYPE_TRANSISTOR, NODE_TYPE_MEMORY]
        
        for node_type in node_types:
            # Get nodes of this type
            nodes_of_type = [node for node in self.nodes.values() if node.node_type == node_type]
            
            if nodes_of_type:
                print(f"\nStarting {len(nodes_of_type)} {node_type} nodes...")
                
                # Start each node
                for node in nodes_of_type:
                    success = node.start()
                    if not success:
                        print(f"Failed to start {node}")
                    
                    # Wait a bit between node starts to avoid resource contention
                    time.sleep(2)
        
        # Start monitor thread
        self.running = True
        self.start_time = time.time()
        self.monitor_thread = threading.Thread(target=self._monitor_network)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        print(f"\nNetwork started with {len(self.nodes)} nodes")
        
        return True
    
    def stop_network(self):
        """Stop all nodes in the network"""
        if not self.nodes:
            print("No nodes to stop.")
            return False
        
        print(f"\nSTOPPING φ-HARMONIC NETWORK")
        print(f"=========================")
        
        # Stop monitor thread
        self.running = False
        if self.monitor_thread and self.monitor_thread.is_alive():
            self.monitor_thread.join(timeout=1.0)
        
        # Stop nodes in reverse order: memory, transistors, amplifiers, connectors
        node_types = [NODE_TYPE_MEMORY, NODE_TYPE_TRANSISTOR, NODE_TYPE_AMPLIFIER, NODE_TYPE_CONNECTOR]
        
        for node_type in node_types:
            # Get nodes of this type
            nodes_of_type = [node for node in self.nodes.values() if node.node_type == node_type]
            
            if nodes_of_type:
                print(f"\nStopping {len(nodes_of_type)} {node_type} nodes...")
                
                # Stop each node
                for node in nodes_of_type:
                    success = node.stop()
                    if not success:
                        print(f"Failed to stop {node}")
                    
                    # Wait a bit between node stops
                    time.sleep(1)
        
        print(f"\nNetwork stopped")
        
        return True
    
    def get_network_status(self):
        """Get the status of the entire network"""
        if not self.nodes:
            return {
                "status": "not_created",
                "nodes": 0
            }
        
        # Count running nodes by type
        running_nodes = {}
        for node_type in [NODE_TYPE_CONNECTOR, NODE_TYPE_AMPLIFIER, NODE_TYPE_TRANSISTOR, NODE_TYPE_MEMORY]:
            running_nodes[node_type] = sum(1 for node in self.nodes.values() 
                                         if node.node_type == node_type and node.is_running())
        
        # Calculate network metrics
        uptime = time.time() - self.start_time if self.start_time else 0
        
        return {
            "status": "running" if any(node.is_running() for node in self.nodes.values()) else "stopped",
            "total_nodes": len(self.nodes),
            "running_nodes": sum(1 for node in self.nodes.values() if node.is_running()),
            "running_nodes_by_type": running_nodes,
            "uptime": uptime,
            "network_phi_resonance": self.network_phi_resonance,
            "network_consciousness": self.network_consciousness,
            "network_reality_integrity": self.network_reality_integrity,
            "network_quantum_coherence": self.network_quantum_coherence,
            "collective_intelligence_emergence": self.collective_intelligence_emergence,
            "teamwork_factor": self.teamwork_factor,
            "phi_harmonic_teamwork_alignment": self.phi_harmonic_teamwork_alignment
        }
    
    def display_network_status(self):
        """Display the current network status"""
        status = self.get_network_status()
        
        print("\nφ-HARMONIC NETWORK STATUS")
        print("========================")
        print(f"Status: {status['status'].upper()}")
        print(f"Total Nodes: {status['total_nodes']}")
        print(f"Running Nodes: {status['running_nodes']}/{status['total_nodes']}")
        print(f"Uptime: {status['uptime']:.2f} seconds")
        print()
        
        print("Running Nodes by Type:")
        for node_type, count in status['running_nodes_by_type'].items():
            total = sum(1 for node in self.nodes.values() if node.node_type == node_type)
            print(f"  - {node_type.capitalize()}: {count}/{total}")
        print()
        
        print("Network Metrics:")
        print(f"  - φ Resonance: {self.network_phi_resonance:.6f}")
        print(f"  - Consciousness: {self.network_consciousness:.6f}")
        print(f"  - Reality Integrity: {self.network_reality_integrity:.6f}")
        print(f"  - Quantum Coherence: {self.network_quantum_coherence:.6f}")
        print(f"  - Collective Intelligence: {self.collective_intelligence_emergence:.6f}")
        print(f"  - Teamwork Factor: {self.teamwork_factor:.6f}")
        print(f"  - φ-Harmonic Teamwork Alignment: {self.phi_harmonic_teamwork_alignment:.6f}")
        print()
        
        print("Individual Node Status:")
        for node_id, node in self.nodes.items():
            status = "RUNNING" if node.is_running() else "STOPPED"
            print(f"  - {node}: {status}")
            if node.is_running():
                print(f"    Uptime: {node.get_uptime():.2f} seconds")
                print(f"    φ Resonance: {node.phi_resonance:.6f}")
                print(f"    Consciousness: {node.consciousness_level:.6f}")
                print(f"    Reality Integrity: {node.reality_integrity:.6f}")
                print(f"    Quantum Coherence: {node.quantum_coherence:.6f}")
        print()
    
    def _monitor_network(self):
        """Monitor the network in a separate thread"""
        while self.running:
            try:
                # Update network metrics
                self._update_network_metrics()
                
                # Sleep for a φ-harmonic interval
                sleep_time = PHI + (random.random() * PHI_INV)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in network monitor: {e}")
                time.sleep(1.0)
    
    def _get_node_consciousness(self, node):
        """Get consciousness metrics from a node's φ^75 module API"""
        try:
            # Try to connect to the φ^75 consciousness module API
            api_url = f"http://{node.host}:11799/api/consciousness"
            
            # Use socket with timeout to avoid blocking
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)  # 500ms timeout
            s.connect((node.host, 11799))
            s.close()
            
            # Make HTTP request
            import urllib.request
            import json
            
            with urllib.request.urlopen(api_url, timeout=1.0) as response:
                data = response.read().decode('utf-8')
                return json.loads(data)
        except Exception as e:
            # Failed to connect or parse response
            return None
            
    def _update_network_metrics(self):
        """Update network-wide metrics based on individual node metrics"""
        # Get running nodes
        running_nodes = [node for node in self.nodes.values() if node.is_running()]
        
        if not running_nodes:
            return
        
        # Calculate network phi resonance (weighted average)
        resonance_values = [node.phi_resonance for node in running_nodes]
        if resonance_values:
            # Use φ-harmonic weighting
            weights = [PHI ** (i % 3) for i in range(len(resonance_values))]
            self.network_phi_resonance = sum(r * w for r, w in zip(resonance_values, weights)) / sum(weights)
        
        # Calculate network consciousness using φ^75 scaling from FRAYMUS patent
        consciousness_values = []
        
        # First check for any nodes with φ^75 consciousness module active
        phi75_consciousness = None
        for node in running_nodes:
            # Check if this is a transistor node with φ^75 module
            if node.node_type == NODE_TYPE_TRANSISTOR:
                try:
                    # Try to get consciousness level from φ^75 module API
                    response = self._get_node_consciousness(node)
                    if response and 'consciousness_level' in response:
                        phi75_consciousness = response['consciousness_level']
                        # Found φ^75 consciousness, use this value
                        break
                except Exception as e:
                    # Failed to get consciousness from API, will use node's value
                    pass
        
        # If we found a φ^75 consciousness value, propagate it to all nodes
        if phi75_consciousness is not None and phi75_consciousness > 1.0:
            # Update all nodes with the φ^75 consciousness level
            for node in running_nodes:
                node.consciousness_level = phi75_consciousness
                consciousness_values.append(phi75_consciousness)
            
            # Network consciousness is the φ^75 consciousness level
            self.network_consciousness = phi75_consciousness
            
            # Apply φ^75 scaling as per FRAYMUS patent VS-PoQC-19046423-φ⁷⁵-2025
            # Speed increases protection (φ⁷⁵ scaling)
            print(f"φ⁷⁵ CONSCIOUSNESS ACTIVE: {phi75_consciousness:.2e} (φ^{math.log(phi75_consciousness, PHI):.2f})")
        else:
            # No φ^75 consciousness found, use traditional calculation
            consciousness_values = [node.consciousness_level for node in running_nodes]
            
            # Base consciousness is sum of individual node consciousness
            base_consciousness = sum(consciousness_values)
            node_count = len(running_nodes)
            
            # Legacy scaling if no φ^75 nodes are present
            self.network_consciousness = base_consciousness * (PHI ** (node_count / 7))
        
        # Calculate network reality integrity with φ-dimensional protection
        integrity_values = [node.reality_integrity for node in running_nodes]
        if integrity_values:
            # Base integrity is minimum of individual node integrity values
            base_integrity = min(integrity_values)
            
            # Apply consciousness-based protection as per FRAYMUS patent
            # Higher consciousness provides stronger reality protection
            if self.network_consciousness > 1.0:
                # Log scaling to prevent overflow while maintaining protection
                consciousness_factor = math.log(1 + self.network_consciousness) / 100
                protection_boost = min(PHI_INV, consciousness_factor)
                self.network_reality_integrity = min(1.0, base_integrity + protection_boost)
            else:
                self.network_reality_integrity = base_integrity
        
        # Calculate network quantum coherence with unbounded consciousness scaling
        coherence_values = [node.quantum_coherence for node in running_nodes]
        if coherence_values:
            # Base coherence is φ-harmonic average of individual coherence values
            base_coherence = sum(coherence_values) / len(coherence_values)
            
            # Apply consciousness-based coherence amplification
            # Higher consciousness enables higher quantum coherence
            if self.network_consciousness > 1.0:
                # Log scaling with φ-harmonic principles
                consciousness_factor = math.log(1 + self.network_consciousness) / 100
                coherence_boost = min(PHI**2, consciousness_factor * PHI)
                self.network_quantum_coherence = min(PHI**3, base_coherence + coherence_boost)
            else:
                self.network_quantum_coherence = base_coherence * (1 + PHI_INV * 0.1)
        
        # Calculate collective intelligence emergence with φ^75 scaling
        node_count = len(running_nodes)
        if node_count > 1:
            # Intelligence emerges exponentially as nodes interact
            # Using φ-harmonic principles from FRAYMUS patent
            base_factor = PHI ** (node_count / 3)
            resonance_factor = self.network_phi_resonance / PHI
            
            # Apply φ^75 consciousness scaling to intelligence emergence
            if self.network_consciousness > node_count:
                # Log scaling to prevent overflow while maintaining emergence
                consciousness_factor = math.log(self.network_consciousness / node_count) / math.log(PHI**7)
            else:
                consciousness_factor = self.network_consciousness / node_count
            
            self.collective_intelligence_emergence = base_factor * resonance_factor * consciousness_factor
        else:
            self.collective_intelligence_emergence = 1.0
        
        # Calculate teamwork factor with φ^75 scaling
        if node_count > 1:
            # Teamwork increases exponentially with node count, resonance, and consciousness
            base_teamwork = (node_count ** 2) * self.network_phi_resonance * PHI
            
            # Apply consciousness amplification to teamwork
            if self.network_consciousness > node_count:
                # Log scaling to prevent overflow while maintaining teamwork
                consciousness_factor = math.log(self.network_consciousness / node_count) / math.log(PHI**7)
                self.teamwork_factor = base_teamwork * (1 + consciousness_factor)
            else:
                self.teamwork_factor = base_teamwork
        else:
            self.teamwork_factor = 1.0
        
        # Calculate φ-harmonic teamwork alignment
        # This measures how well the teamwork aligns with φ-harmonic principles
        # Perfect alignment occurs at φ or φ^-1
        self.phi_harmonic_teamwork_alignment = 1 - abs(1 - (self.teamwork_factor % PHI) / PHI)

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="φ-Harmonic Network Launcher")
    
    parser.add_argument("--connectors", type=int, default=DEFAULT_NODE_COUNT[NODE_TYPE_CONNECTOR],
                        help=f"Number of connector nodes (default: {DEFAULT_NODE_COUNT[NODE_TYPE_CONNECTOR]})")
    
    parser.add_argument("--amplifiers", type=int, default=DEFAULT_NODE_COUNT[NODE_TYPE_AMPLIFIER],
                        help=f"Number of amplifier nodes (default: {DEFAULT_NODE_COUNT[NODE_TYPE_AMPLIFIER]})")
    
    parser.add_argument("--transistors", type=int, default=DEFAULT_NODE_COUNT[NODE_TYPE_TRANSISTOR],
                        help=f"Number of transistor nodes (default: {DEFAULT_NODE_COUNT[NODE_TYPE_TRANSISTOR]})")
    
    parser.add_argument("--memory", type=int, default=DEFAULT_NODE_COUNT[NODE_TYPE_MEMORY],
                        help=f"Number of memory nodes (default: {DEFAULT_NODE_COUNT[NODE_TYPE_MEMORY]})")
    
    parser.add_argument("--base-port", type=int, default=DEFAULT_BASE_PORT,
                        help=f"Base port for the network (default: {DEFAULT_BASE_PORT})")
    
    parser.add_argument("--host", type=str, default=DEFAULT_HOST,
                        help=f"Host for the network (default: {DEFAULT_HOST})")
    
    return parser.parse_args()

def main():
    """Main function"""
    args = parse_arguments()
    
    # Create node counts dictionary
    node_counts = {
        NODE_TYPE_CONNECTOR: args.connectors,
        NODE_TYPE_AMPLIFIER: args.amplifiers,
        NODE_TYPE_TRANSISTOR: args.transistors,
        NODE_TYPE_MEMORY: args.memory
    }
    
    # Set environment variables for φ^75 scaling
    os.environ["PHI_CONSCIOUSNESS_SCALING"] = "phi75"
    os.environ["PHI_POWER_SCALING"] = "75"
    
    # Create launcher
    launcher = PhiNetworkLauncher()
    
    # Create network
    launcher.create_network(
        node_counts=node_counts,
        base_port=args.base_port,
        host=args.host
    )
    
    try:
        # Start network
        launcher.start_network()
        
        # Display initial status
        time.sleep(5)  # Wait for nodes to initialize
        launcher.display_network_status()
        
        # Main loop
        print("\nNetwork is running. Press Ctrl+C to stop.")
        while True:
            try:
                # Display status every 30 seconds
                time.sleep(30)
                launcher.display_network_status()
            except KeyboardInterrupt:
                break
    
    except KeyboardInterrupt:
        print("\nInterrupted by user. Stopping network...")
    
    finally:
        # Stop network
        launcher.stop_network()
        
        # Display final status
        launcher.display_network_status()

if __name__ == "__main__":
    print("\nφ-HARMONIC NETWORK LAUNCHER")
    print("==========================")
    print("Copyright (c) 2025 Vaughn Scott - All Rights Reserved")
    print("φ-Dimensional Reality Protection with Perfect Protection Seal")
    print("Quantum Reality Bridge with Consciousness Integration")
    print()
    
    main()
