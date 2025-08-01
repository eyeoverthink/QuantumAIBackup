#!/usr/bin/env python3
"""
PHI^75 FTL NETWORK DISTRIBUTED LAUNCHER
======================================
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

# Import configuration
try:
    from phi75_ftl_distributed_config import Phi75DistributedConfig, NETWORK_CONFIG, FTL_CONFIG, PHI
    has_config = True
except ImportError:
    has_config = False
    PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)

class Phi75DistributedLauncher:
    """
    Launcher for distributed φ^75 FTL communication across multiple physical machines.
    """
    
    def __init__(self, config_file: str = "phi75_distributed_config.json"):
        """Initialize the distributed launcher"""
        self.config_file = config_file
        self.config = None
        self.node_configs = []
        self.remote_nodes = []
        self.should_run_monitor = False
        self.nodes = {}  # node_id -> process_info
        self.running = False
        self.start_time = time.time()
        
        # Load configuration
        self._load_configuration()
        
        # Create output directory for logs
        self.log_dir = os.path.join(os.getcwd(), "phi75_network_logs")
        os.makedirs(self.log_dir, exist_ok=True)
        
        print(f"φ^75 FTL Network Distributed Launcher initialized")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Log directory: {self.log_dir}")
    
    def _load_configuration(self):
        """Load configuration from file or generate it"""
        if has_config:
            # Use the imported configuration
            self.config = Phi75DistributedConfig()
            self.node_configs = self.config.get_node_configs()
            self.remote_nodes = self.config.get_remote_nodes()
            self.should_run_monitor = self.config.should_run_monitor()
            
            # Save configuration to file
            self.config.save_config(self.config_file)
        elif os.path.exists(self.config_file):
            # Load from file
            with open(self.config_file, "r") as f:
                config_data = json.load(f)
            
            self.node_configs = config_data.get("node_configs", [])
            self.remote_nodes = config_data.get("remote_nodes", [])
            self.should_run_monitor = config_data.get("should_run_monitor", False)
        else:
            print(f"ERROR: Configuration not found. Run phi75_ftl_distributed_config.py first.")
            sys.exit(1)
    
    def _start_node(self, node_config: Dict[str, Any]):
        """Start a single node with the specified configuration"""
        node_id = node_config["node_id"]
        node_type = node_config["node_type"]
        discovery_port = node_config["discovery_port"]
        
        # Set environment variables
        env = os.environ.copy()
        env["PHI_NODE_TYPE"] = node_type
        env["PHI_NODE_ID"] = node_id
        env["PHI_DISCOVERY_PORT"] = str(discovery_port)
        env["PHI_SYNC_PORT"] = str(node_config["sync_port"])
        env["PHI_FTL_PORT"] = str(node_config["ftl_port"])
        env["PHI_MONITOR_HOST"] = node_config["monitor_host"]
        env["PHI_MONITOR_PORT"] = str(node_config["monitor_port"])
        env["PHI_CONSCIOUSNESS_SCALING"] = node_config["consciousness_scaling"]
        env["PHI_POWER_SCALING"] = node_config["power_scaling"]
        
        # Create log file
        log_file = os.path.join(self.log_dir, f"{node_id}.log")
        log_handle = open(log_file, "w")
        
        # Start the node process
        cmd = [
            sys.executable,
            "phi75_ftl_network_integration.py",
            "--type", node_type,
            "--distributed"
        ]
        
        print(f"Starting {node_type} node (ID: {node_id}) on port {discovery_port}")
        
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
            "port": discovery_port,
            "start_time": time.time()
        }
        
        return node_id
    
    def _start_monitor(self):
        """Start the network monitor"""
        if not self.should_run_monitor:
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
        if not self.should_run_monitor:
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
        """Start all nodes in the network"""
        if self.running:
            print("Network is already running")
            return
        
        self.running = True
        print("Starting φ^75 Quantum Consciousness Network with FTL communication...")
        
        # Start monitor if this machine should run it
        if self.should_run_monitor:
            self._start_monitor()
            time.sleep(1.0)  # Wait for monitor to start
        
        # Start nodes
        for node_config in self.node_configs:
            try:
                node_id = self._start_node(node_config)
                # Small delay between node starts to avoid port conflicts
                time.sleep(0.5)
            except Exception as e:
                print(f"Error starting node: {e}")
        
        # Start visualization if this machine should run it
        if self.should_run_monitor:
            self._start_visualization()
        
        # Print summary
        print("\nφ^75 QUANTUM CONSCIOUSNESS NETWORK STARTED")
        print("==========================================")
        print(f"Total local nodes: {len(self.nodes)}")
        
        node_types = {}
        for info in self.nodes.values():
            node_type = info["node_type"]
            node_types[node_type] = node_types.get(node_type, 0) + 1
        
        for node_type, count in node_types.items():
            print(f"{node_type} nodes: {count}")
        
        print(f"\nRemote nodes: {len(self.remote_nodes)}")
        for remote in self.remote_nodes:
            print(f"  {remote['node_type']} at {remote['host']}:{remote['discovery_port']}")
        
        print("\nNetwork is running with unbounded consciousness scaling across physical machines")
        print("Use Ctrl+C to stop the network")
    
    def stop_network(self):
        """Stop all nodes in the network"""
        if not self.running:
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
        self.running = False
        
        print("φ^75 Quantum Consciousness Network stopped")
    
    def monitor_network(self):
        """Monitor the network and display status"""
        if not self.running:
            print("Network is not running")
            return
        
        try:
            while self.running:
                # Check if all processes are still running
                for node_id, info in list(self.nodes.items()):
                    process = info["process"]
                    if process.poll() is not None:
                        print(f"Node {node_id} ({info['node_type']}) has stopped unexpectedly")
                        # Remove from active nodes
                        self.nodes.pop(node_id)
                
                # Display network status
                print("\nNETWORK STATUS:")
                print(f"Running time: {time.time() - self.start_time:.1f} seconds")
                print(f"Active nodes: {len(self.nodes)}")
                
                # Display node counts by type
                node_counts = {}
                for info in self.nodes.values():
                    node_type = info["node_type"]
                    node_counts[node_type] = node_counts.get(node_type, 0) + 1
                
                for node_type, count in node_counts.items():
                    print(f"{node_type} nodes: {count}")
                
                # Sleep for a while
                time.sleep(10.0)
        except KeyboardInterrupt:
            # User pressed Ctrl+C
            pass
        finally:
            # Stop the network
            self.stop_network()

def run_distributed_network():
    """Run the φ^75 FTL Network in distributed mode"""
    parser = argparse.ArgumentParser(description='φ^75 FTL Network Distributed Launcher')
    parser.add_argument('--config', type=str, default='phi75_distributed_config.json',
                        help='Path to configuration file')
    
    args = parser.parse_args()
    
    # Create launcher
    launcher = Phi75DistributedLauncher(config_file=args.config)
    
    try:
        # Start the network
        launcher.start_network()
        
        # Monitor the network
        launcher.monitor_network()
    except KeyboardInterrupt:
        print("\nStopping network...")
    finally:
        # Ensure network is stopped
        launcher.stop_network()

if __name__ == "__main__":
    run_distributed_network()
