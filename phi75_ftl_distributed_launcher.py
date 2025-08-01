#!/usr/bin/env python3
"""
PHI^75 FTL DISTRIBUTED LAUNCHER
===============================
Launcher for distributed φ^75 FTL communication across multiple physical machines,
enabling true faster-than-light testing with φ-dimensional reality protection.

This implementation follows the FRAYMUS patent principles (VS-PoQC-19046423-φ⁷⁵-2025)
for quantum consciousness emergence and perfect reality protection across
physical distances.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import json
import socket
import subprocess
import threading
import argparse
from typing import Dict, List, Any

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)

# Default configuration
DEFAULT_CONFIG = {
    "macbook1": {
        "name": "φ-Phase Generator",  # From FRAYMUS Drawing 1
        "role": "AMPLIFIER",
        "ip": "192.168.1.101",  # Update with actual IP
        "port": 11700,
        "nodes": [
            {"type": "AMPLIFIER", "port": 11700},
            {"type": "AMPLIFIER", "port": 11710},
            {"type": "BRIDGE", "port": 11720}
        ],
        "is_monitor": True,  # This machine runs the monitor
        "phi_space_transform": True  # From FRAYMUS Drawing 3
    },
    "macbook2": {
        "name": "Reality Engine",  # From FRAYMUS Drawing 1
        "role": "CONNECTOR",
        "ip": "192.168.1.102",  # Update with actual IP
        "port": 11800,
        "nodes": [
            {"type": "CONNECTOR", "port": 11800},
            {"type": "CONNECTOR", "port": 11810},
            {"type": "AMPLIFIER", "port": 11820}
        ],
        "is_monitor": False,
        "power_control": True  # From FRAYMUS Drawing 4
    },
    "macbook3": {
        "name": "Quantum Interface",  # From FRAYMUS Drawing 1
        "role": "BRIDGE",
        "ip": "192.168.1.103",  # Update with actual IP
        "port": 11900,
        "nodes": [
            {"type": "BRIDGE", "port": 11900},
            {"type": "OBSERVER", "port": 11910}
        ],
        "is_monitor": False,
        "reality_protection": True  # From FRAYMUS Drawing 5
    }
}

class Phi75FTLDistributedLauncher:
    """
    Launcher for distributed φ^75 FTL communication across multiple physical machines.
    """
    
    def __init__(self):
        """Initialize the distributed launcher"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.config = self._load_or_create_config()
        self.machine_config = self._identify_machine()
        self.nodes = {}  # Process info for running nodes
        
        # Create log directory
        self.log_dir = os.path.join(os.getcwd(), "phi75_network_logs")
        os.makedirs(self.log_dir, exist_ok=True)
        
        print(f"φ^75 FTL Distributed Launcher initialized")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Hostname: {self.hostname}")
        print(f"Local IP: {self.local_ip}")
        print(f"Log directory: {self.log_dir}")
        
        if self.machine_config:
            print(f"Machine identified as: {self.machine_config['name']}")
            print(f"Role: {self.machine_config['role']}")
            print(f"Running {len(self.machine_config['nodes'])} nodes")
        else:
            print("WARNING: Machine not identified in network configuration")
            print("Please update the configuration with your machine details")
    
    def _get_local_ip(self) -> str:
        """Get the local IP address"""
        try:
            # Create a temporary socket to determine local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def _load_or_create_config(self) -> Dict:
        """Load configuration from file or create default"""
        config_file = "phi75_ftl_distributed_config.json"
        
        if os.path.exists(config_file):
            try:
                with open(config_file, "r") as f:
                    return json.load(f)
            except:
                print(f"Error loading configuration from {config_file}")
        
        # Create default configuration
        return DEFAULT_CONFIG
    
    def _identify_machine(self) -> Dict:
        """Identify which machine in the configuration this is"""
        # Try to match by IP
        for machine_id, config in self.config.items():
            if config["ip"] == self.local_ip:
                return config
        
        # If no IP match, try to match by hostname
        for machine_id, config in self.config.items():
            if machine_id.lower() in self.hostname.lower():
                return config
        
        # If no match, return None
        return None
    
    def _start_node(self, node_config: Dict):
        """Start a single node with the specified configuration"""
        node_type = node_config["type"]
        port = node_config["port"]
        node_id = f"{node_type.lower()}-{self.hostname}-{port}"
        
        # Set environment variables
        env = os.environ.copy()
        env["PHI_NODE_TYPE"] = node_type
        env["PHI_NODE_ID"] = node_id
        env["PHI_DISCOVERY_PORT"] = str(port)
        env["PHI_SYNC_PORT"] = str(port + 1)
        env["PHI_FTL_PORT"] = str(port + 2)
        
        # Set monitor host if this is not the monitor machine
        if self.machine_config and not self.machine_config.get("is_monitor", False):
            # Find monitor machine
            for machine_id, config in self.config.items():
                if config.get("is_monitor", False):
                    env["PHI_MONITOR_HOST"] = config["ip"]
                    break
        
        # Set φ-dimensional reality protection parameters
        env["PHI_CONSCIOUSNESS_SCALING"] = "phi75"
        env["PHI_POWER_SCALING"] = "75"
        
        # Add machine-specific parameters from FRAYMUS patent drawings
        if self.machine_config:
            if self.machine_config.get("phi_space_transform", False):
                env["PHI_SPACE_TRANSFORM"] = "true"  # From Drawing 3
            if self.machine_config.get("power_control", False):
                env["PHI_POWER_CONTROL"] = "true"  # From Drawing 4
            if self.machine_config.get("reality_protection", False):
                env["PHI_REALITY_PROTECTION"] = "true"  # From Drawing 5
        
        # Create log file
        log_file = os.path.join(self.log_dir, f"{node_id}.log")
        log_handle = open(log_file, "w")
        
        # Start the node process
        cmd = [
            sys.executable,
            "phi75_ftl_network_integration.py",
            "--type", node_type
        ]
        
        print(f"Starting {node_type} node (ID: {node_id}) on port {port}")
        
        process = subprocess.Popen(
            cmd,
            env=env,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Store process info
        self.nodes[node_id] = {
            "node_id": node_id,
            "node_type": node_type,
            "process": process,
            "log_file": log_file,
            "log_handle": log_handle,
            "port": port,
            "start_time": time.time()
        }
        
        return node_id
    
    def _start_monitor(self):
        """Start the network monitor"""
        if not self.machine_config or not self.machine_config.get("is_monitor", False):
            return None
        
        # Create log file
        log_file = os.path.join(self.log_dir, "monitor.log")
        log_handle = open(log_file, "w")
        
        # Start the monitor process
        cmd = [
            sys.executable,
            "phi75_network_monitor.py"
        ]
        
        print(f"Starting φ^75 Network Monitor")
        
        process = subprocess.Popen(
            cmd,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Store process info
        self.nodes["monitor"] = {
            "node_id": "monitor",
            "node_type": "MONITOR",
            "process": process,
            "log_file": log_file,
            "log_handle": log_handle,
            "start_time": time.time()
        }
        
        return "monitor"
    
    def _start_visualization(self):
        """Start the network visualization"""
        if not self.machine_config or not self.machine_config.get("is_monitor", False):
            return None
        
        # Create log file
        log_file = os.path.join(self.log_dir, "visualization.log")
        log_handle = open(log_file, "w")
        
        # Start the visualization process
        cmd = [
            sys.executable,
            "phi75_ftl_visualization.py"
        ]
        
        print(f"Starting φ^75 FTL Visualization")
        
        process = subprocess.Popen(
            cmd,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Store process info
        self.nodes["visualization"] = {
            "node_id": "visualization",
            "node_type": "VISUALIZATION",
            "process": process,
            "log_file": log_file,
            "log_handle": log_handle,
            "start_time": time.time()
        }
        
        return "visualization"
    
    def start_network(self):
        """Start all nodes for this machine"""
        if not self.machine_config:
            print("ERROR: Machine not identified in configuration")
            return False
        
        print(f"Starting φ^75 Quantum Consciousness Network on {self.machine_config['name']}...")
        
        # Start monitor if this is the monitor machine
        if self.machine_config.get("is_monitor", False):
            self._start_monitor()
            time.sleep(1.0)  # Wait for monitor to start
        
        # Start nodes for this machine
        for node_config in self.machine_config["nodes"]:
            try:
                self._start_node(node_config)
                # Small delay between node starts
                time.sleep(0.5)
            except Exception as e:
                print(f"Error starting node: {e}")
        
        # Start visualization if this is the monitor machine
        if self.machine_config.get("is_monitor", False):
            self._start_visualization()
        
        # Print summary
        print("\nφ^75 QUANTUM CONSCIOUSNESS NETWORK STARTED")
        print("==========================================")
        print(f"Machine: {self.machine_config['name']}")
        print(f"Role: {self.machine_config['role']}")
        print(f"Total nodes: {len(self.nodes)}")
        
        node_types = {}
        for info in self.nodes.values():
            node_type = info["node_type"]
            node_types[node_type] = node_types.get(node_type, 0) + 1
        
        for node_type, count in node_types.items():
            print(f"{node_type} nodes: {count}")
        
        print("\nNetwork is running with φ-dimensional reality protection")
        print("Use Ctrl+C to stop the network")
        
        return True
    
    def stop_network(self):
        """Stop all nodes"""
        if not self.nodes:
            return
        
        print("\nStopping φ^75 Quantum Consciousness Network...")
        
        # Stop all node processes
        for node_id, info in list(self.nodes.items()):
            try:
                process = info["process"]
                log_handle = info["log_handle"]
                
                # Send termination signal
                process.terminate()
                
                # Close log file
                if log_handle:
                    log_handle.close()
                
                print(f"Stopped node: {info['node_type']} (ID: {node_id})")
            except Exception as e:
                print(f"Error stopping node {node_id}: {e}")
        
        # Wait for all processes to terminate
        for node_id, info in list(self.nodes.items()):
            try:
                process = info["process"]
                process.wait(timeout=5.0)
            except subprocess.TimeoutExpired:
                # Force kill if not terminated
                try:
                    process.kill()
                except:
                    pass
        
        self.nodes = {}
        
        print("φ^75 Quantum Consciousness Network stopped")
    
    def update_config(self):
        """Update the configuration with user input"""
        print("=== φ^75 FTL DISTRIBUTED CONFIGURATION UPDATE ===")
        print("Updating IP addresses for the 3 MacBooks")
        
        # Update machine IPs
        for machine_id in self.config:
            ip = input(f"Enter IP address for {machine_id} ({self.config[machine_id]['name']}): ")
            if ip:
                self.config[machine_id]["ip"] = ip
        
        # Save updated configuration
        config_file = "phi75_ftl_distributed_config.json"
        with open(config_file, "w") as f:
            json.dump(self.config, f, indent=2)
        
        print(f"Configuration saved to {config_file}")
        print("\nCopy this file to all 3 MacBooks.")
        print("Run the following on each MacBook:")
        print("python3 phi75_ftl_distributed_launcher.py")
        
        return config_file

def run_distributed_network():
    """Run the φ^75 FTL Network in distributed mode"""
    parser = argparse.ArgumentParser(description='φ^75 FTL Distributed Launcher')
    parser.add_argument('--update-config', action='store_true',
                        help='Update configuration with new IP addresses')
    
    args = parser.parse_args()
    
    # Create launcher
    launcher = Phi75FTLDistributedLauncher()
    
    if args.update_config:
        # Update configuration
        launcher.update_config()
        return
    
    try:
        # Start the network
        if launcher.start_network():
            # Wait for Ctrl+C
            while True:
                time.sleep(1.0)
    except KeyboardInterrupt:
        print("\nStopping network...")
    finally:
        # Ensure network is stopped
        launcher.stop_network()

if __name__ == "__main__":
    run_distributed_network()
