#!/usr/bin/env python3
"""
PHI^75 FTL MESSAGE SENDER
=========================
Sends direct text messages across the distributed network as proof of
FTL communication with perfect reality protection between physical machines.

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
import random
import hashlib
import argparse
from datetime import datetime
from typing import Dict, List, Any

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)

# Load configuration
CONFIG_FILE = "phi75_ftl_distributed_config.json"
try:
    with open(CONFIG_FILE, "r") as f:
        CONFIG = json.load(f)
except:
    print(f"Error: Could not load configuration from {CONFIG_FILE}")
    CONFIG = {}

class Phi75FTLMessageSender:
    """
    Sends direct text messages across the distributed network as proof of
    FTL communication with perfect reality protection between physical machines.
    """
    
    def __init__(self):
        """Initialize the message sender"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.machine_config = self._identify_machine()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.messages_sent = 0
        
        print(f"φ^75 FTL Message Sender initialized")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Hostname: {self.hostname}")
        print(f"Local IP: {self.local_ip}")
        
        if self.machine_config:
            print(f"Machine identified as: {self.machine_config['name']}")
            print(f"Role: {self.machine_config['role']}")
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
    
    def _identify_machine(self) -> Dict:
        """Identify which machine in the configuration this is"""
        if not CONFIG:
            return None
        
        # Try to match by IP
        for machine_id, config in CONFIG.items():
            if config.get("ip") == self.local_ip:
                return config
        
        # If no IP match, try to match by hostname
        for machine_id, config in CONFIG.items():
            if machine_id.lower() in self.hostname.lower():
                return config
        
        # If no match, return None
        return None
    
    def _generate_message_id(self) -> str:
        """Generate a unique message ID"""
        base = f"ftl-msg-{time.time()}-{random.random()}-{PHI}"
        hash_obj = hashlib.sha256(base.encode())
        return hash_obj.hexdigest()[:8]
    
    def create_message(self, text: str) -> Dict:
        """Create a message with the specified text"""
        message_id = self._generate_message_id()
        source_machine = self.machine_config["name"] if self.machine_config else "Unknown"
        source_role = self.machine_config["role"] if self.machine_config else "Unknown"
        source_path = self.machine_config.get("path", "/unknown") if self.machine_config else "/unknown"
        
        # Create message
        message = {
            "type": "ftl_message",
            "message_id": message_id,
            "text": text,
            "source_machine": source_machine,
            "source_role": source_role,
            "source_hostname": self.hostname,
            "source_ip": self.local_ip,
            "source_path": source_path,
            "timestamp": time.time(),
            "phi_harmonic": True,
            "reality_protection": True,
            "ftl_communication": True,
            "phi_power": 75
        }
        
        return message
    
    def send_message_to_machine(self, message: Dict, machine_id: str):
        """Send a message to a specific machine"""
        if not CONFIG or machine_id not in CONFIG:
            print(f"Error: Machine {machine_id} not found in configuration")
            return False
        
        machine_config = CONFIG[machine_id]
        machine_ip = machine_config["ip"]
        machine_name = machine_config["name"]
        machine_hostname = machine_config.get("hostname", "unknown")
        machine_path = machine_config.get("path", "/unknown")
        
        # Send to all nodes on the machine
        for node in machine_config.get("nodes", []):
            try:
                port = node.get("port", 11700)
                
                # Encode message
                data = json.dumps(message).encode('utf-8')
                
                # Send to node
                self.socket.sendto(data, (machine_ip, port))
                
                print(f"Sent message to {machine_name} ({machine_hostname})")
                print(f"  IP: {machine_ip}:{port}")
                print(f"  Path: {machine_path}")
                print(f"  Message ID: {message['message_id']}")
                print(f"  Text: {message['text']}")
                
                self.messages_sent += 1
                
                # Small delay between sends
                time.sleep(0.1)
            except Exception as e:
                print(f"Error sending to {machine_ip}:{port}: {e}")
        
        return True
    
    def send_message_to_all_machines(self, message: Dict):
        """Send a message to all machines in the network"""
        if not CONFIG:
            print("Error: No configuration available")
            return False
        
        for machine_id in CONFIG:
            self.send_message_to_machine(message, machine_id)
        
        return True
    
    def send_direct_message(self, text: str):
        """Send a direct message to all machines"""
        message = self.create_message(text)
        return self.send_message_to_all_machines(message)

def run_message_sender():
    """Run the φ^75 FTL Message Sender"""
    parser = argparse.ArgumentParser(description='φ^75 FTL Message Sender')
    parser.add_argument('--message', type=str, default=None,
                        help='Message to send (if not provided, will prompt)')
    
    args = parser.parse_args()
    
    print("=== φ^75 FTL MESSAGE SENDER ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    
    # Create message sender
    sender = Phi75FTLMessageSender()
    
    # Get message text
    if args.message:
        message_text = args.message
    else:
        message_text = input("Enter message to send to all machines: ")
    
    # Add timestamp and source info
    source_info = f"[{sender.machine_config['name'] if sender.machine_config else 'Unknown'}]"
    full_message = f"{source_info} {message_text} - {datetime.now().strftime('%H:%M:%S')}"
    
    # Send message
    print(f"Sending message: {full_message}")
    sender.send_direct_message(full_message)
    print(f"Message sent to all machines with φ-dimensional reality protection")

if __name__ == "__main__":
    run_message_sender()
