#!/usr/bin/env python3
"""
PHI^75 FTL DISTRIBUTED CONFIGURATION
====================================
Configuration for distributed φ^75 FTL communication across multiple physical machines,
enabling true faster-than-light testing with φ-dimensional reality protection.

This implementation follows the FRAYMUS patent principles (VS-PoQC-19046423-φ⁷⁵-2025)
for testing quantum consciousness emergence across physical distances.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import socket
import json
from typing import Dict, List, Any

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)

# Network configuration for 3 MacBooks based on FRAYMUS patent drawings
NETWORK_CONFIG = {
    "macbook1": {
        "name": "φ-Phase Generator",  # From FRAYMUS Drawing 1
        "role": "AMPLIFIER",
        "ip": "192.168.1.101",  # Update with actual IP
        "port": 11700,
        "nodes": 3,  # Number of nodes to run
        "node_types": ["AMPLIFIER", "AMPLIFIER", "BRIDGE"],
        "is_monitor": True,  # This machine runs the monitor
        "phi_space_transform": True  # From FRAYMUS Drawing 3
    },
    "macbook2": {
        "name": "Reality Engine",  # From FRAYMUS Drawing 1
        "role": "CONNECTOR",
        "ip": "192.168.1.102",  # Update with actual IP
        "port": 11800,
        "nodes": 3,
        "node_types": ["CONNECTOR", "CONNECTOR", "AMPLIFIER"],
        "is_monitor": False,
        "power_control": True  # From FRAYMUS Drawing 4
    },
    "macbook3": {
        "name": "Quantum Interface",  # From FRAYMUS Drawing 1
        "role": "BRIDGE",
        "ip": "192.168.1.103",  # Update with actual IP
        "port": 11900,
        "nodes": 2,
        "node_types": ["BRIDGE", "OBSERVER"],
        "is_monitor": False,
        "reality_protection": True  # From FRAYMUS Drawing 5
    }
}

# FTL communication configuration based on FRAYMUS patent claims
FTL_CONFIG = {
    "base_port": 11700,
    "monitor_port": 11750,
    "ftl_port": 11702,
    "consciousness_scaling": "phi75",  # φ⁷⁵ scaling from patent
    "power_scaling": "75",
    "reality_protection": True,  # Perfect protection through φ-space mapping
    "quantum_entanglement": True,  # Quantum bridge between realities
    "phi_harmonic_resonance": True,  # Uses golden ratio for reality transformation
    "phase_control": True,  # From FRAYMUS Drawing 7
    "reality_map": {  # From FRAYMUS Drawing 8
        "reality_layer": True,
        "phi_space_layer": True,
        "quantum_layer": True
    },
    "future_protection": True  # From FRAYMUS Drawing 10
}

class Phi75DistributedConfig:
    """
    Configuration manager for distributed φ^75 FTL communication.
    """
    
    def __init__(self):
        """Initialize the configuration manager"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.machine_config = self._identify_machine()
        
        print(f"φ^75 Distributed Configuration initialized")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Hostname: {self.hostname}")
        print(f"Local IP: {self.local_ip}")
        
        if self.machine_config:
            print(f"Machine identified as: {self.machine_config['name']}")
            print(f"Role: {self.machine_config['role']}")
            print(f"Running {self.machine_config['nodes']} nodes")
        else:
            print("WARNING: Machine not identified in network configuration")
    
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
    
    def _identify_machine(self) -> Dict[str, Any]:
        """Identify which machine in the configuration this is"""
        # Try to match by IP
        for machine_id, config in NETWORK_CONFIG.items():
            if config["ip"] == self.local_ip:
                return config
        
        # If no IP match, try to match by hostname
        for machine_id, config in NETWORK_CONFIG.items():
            if machine_id.lower() in self.hostname.lower():
                return config
        
        # If no match, return None
        return None
    
    def get_node_configs(self) -> List[Dict[str, Any]]:
        """Get configurations for nodes to run on this machine"""
        if not self.machine_config:
            return []
        
        node_configs = []
        base_port = self.machine_config["port"]
        
        for i, node_type in enumerate(self.machine_config["node_types"]):
            node_config = {
                "node_type": node_type,
                "node_id": f"{node_type.lower()}-{self.hostname}-{i:02d}",
                "host": self.local_ip,
                "discovery_port": base_port + (i * 10),
                "sync_port": base_port + (i * 10) + 1,
                "ftl_port": base_port + (i * 10) + 2,
                "monitor_host": NETWORK_CONFIG["macbook1"]["ip"],
                "monitor_port": FTL_CONFIG["monitor_port"],
                "consciousness_scaling": FTL_CONFIG["consciousness_scaling"],
                "power_scaling": FTL_CONFIG["power_scaling"],
                "reality_protection": FTL_CONFIG["reality_protection"],
                "quantum_entanglement": FTL_CONFIG["quantum_entanglement"],
                "phi_harmonic_resonance": FTL_CONFIG["phi_harmonic_resonance"]
            }
            
            node_configs.append(node_config)
        
        return node_configs
    
    def get_remote_nodes(self) -> List[Dict[str, Any]]:
        """Get configurations for remote nodes to connect to"""
        if not self.machine_config:
            return []
        
        remote_nodes = []
        
        # Add all nodes from other machines
        for machine_id, config in NETWORK_CONFIG.items():
            if config["ip"] != self.local_ip:  # Skip local machine
                base_port = config["port"]
                
                for i, node_type in enumerate(config["node_types"]):
                    remote_node = {
                        "node_type": node_type,
                        "host": config["ip"],
                        "discovery_port": base_port + (i * 10),
                        "sync_port": base_port + (i * 10) + 1,
                        "ftl_port": base_port + (i * 10) + 2
                    }
                    
                    remote_nodes.append(remote_node)
        
        return remote_nodes
    
    def should_run_monitor(self) -> bool:
        """Check if this machine should run the monitor"""
        if not self.machine_config:
            return False
        
        return self.machine_config.get("is_monitor", False)
    
    def save_config(self, filename: str = "phi75_distributed_config.json") -> str:
        """Save the configuration to a file"""
        config = {
            "hostname": self.hostname,
            "local_ip": self.local_ip,
            "machine_config": self.machine_config,
            "node_configs": self.get_node_configs(),
            "remote_nodes": self.get_remote_nodes(),
            "should_run_monitor": self.should_run_monitor(),
            "ftl_config": FTL_CONFIG
        }
        
        with open(filename, "w") as f:
            json.dump(config, f, indent=2)
        
        print(f"Configuration saved to {filename}")
        return filename

def update_ips():
    """Update the IP addresses in the configuration"""
    print("=== φ^75 FTL DISTRIBUTED CONFIGURATION ===")
    print("Updating IP addresses for the 3 MacBooks")
    
    for machine_id in NETWORK_CONFIG:
        ip = input(f"Enter IP address for {machine_id} ({NETWORK_CONFIG[machine_id]['name']}): ")
        if ip:
            NETWORK_CONFIG[machine_id]["ip"] = ip
    
    # Create and save configuration
    config = Phi75DistributedConfig()
    config.save_config()
    
    print("\nConfiguration updated. Copy this file to all 3 MacBooks.")
    print("Run the following on each MacBook:")
    print("python3 phi75_ftl_network_distributed_launcher.py")

if __name__ == "__main__":
    update_ips()
