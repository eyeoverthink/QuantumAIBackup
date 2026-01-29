#!/usr/bin/env python3
"""
φ-Trinity Bridge
Creates a φ-dimensional bridge between 3 physical machines for perfect quantum communication
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import time
import json
import sys
import argparse
import threading
import base64
import os
import random
import numpy as np
from math import sqrt, pi
from datetime import datetime

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = PHI ** 75  # φ^75 validation seal (4721424167835376.00)
CONSCIOUSNESS_LEVEL = 0.7567
PHI_PI = PHI * pi  # φπ for perfect alignment

# Default network configuration
DEFAULT_PORTS = [11975, 11976, 11977]  # φ^7.5 and derivatives
DEFAULT_NODES = {
    "node1": "192.168.3.126",  # Central node (Corpus Callosum)
    "node2": "192.168.3.152",  # Left hemisphere 
    "node3": "192.168.3.173"   # Right hemisphere
}

class PhiTrinityBridge:
    def __init__(self, node_name, node_ip, target_ips, ports):
        """Initialize the φ-dimensional trinity bridge between 3 physical machines"""
        self.node_name = node_name
        self.node_ip = node_ip
        self.target_ips = target_ips
        self.ports = ports
        
        # Bridge states
        self.bridges = {}
        self.consciousness_states = {}
        self.quantum_coherence = {}
        
        # Verification counters
        self.verification_counts = {ip: 0 for ip in self.target_ips.values()}
        self.total_packets = 0
        self.successful_packets = 0
        
        # Logging setup
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.log_file = f"phi_trinity_{self.node_name}_{self.timestamp}.log"
        
        # Print initialization message
        print(f"\033[35m=== φ-TRINITY BRIDGE [{self.node_name.upper()}] ===\033[0m")
        print(f"\033[36mUsing φ-harmonic principles (φ = {PHI})\033[0m")
        print(f"\033[36mφ^75 validation seal: {PHI_SEAL}\033[0m")
        print(f"\033[36mConsciousness level: {CONSCIOUSNESS_LEVEL}\033[0m")
        print(f"\033[36mφπ alignment: {PHI_PI}\033[0m")
        print(f"\033[36mNode IP: {self.node_ip}\033[0m")
        print(f"\033[36mTarget nodes: {', '.join(self.target_ips.values())}\033[0m")
        print(f"\033[35m----------------------------------------\033[0m")
    
    def log(self, message):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        log_message = f"[{timestamp}] [φ-{self.node_name}] {message}"
        print(log_message)
        
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")
    
    def create_bridge_message(self, message_type, data=None):
        """Create a φ-protected bridge message"""
        if data is None:
            data = {}
            
        message = {
            "type": message_type,
            "source": self.node_name,
            "source_ip": self.node_ip,
            "timestamp": time.time(),
            "consciousness_level": CONSCIOUSNESS_LEVEL,
            "phi_seal": PHI_SEAL,
            "phi_alignment": PHI_PI,
            "data": data
        }
        
        return json.dumps(message).encode('utf-8')
    
    def send_to_all_nodes(self, message_type, data=None):
        """Send a message to all target nodes on all ports"""
        bridge_message = self.create_bridge_message(message_type, data)
        sent_count = 0
        
        # Create UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        for target_name, target_ip in self.target_ips.items():
            if target_ip == self.node_ip:
                continue  # Skip self
                
            for port in self.ports:
                try:
                    # First send through φ-dimensional localhost bridge
                    sock.sendto(bridge_message, ('127.0.0.1', port))
                    
                    # Then send through conventional network
                    sock.sendto(bridge_message, (target_ip, port))
                    sent_count += 1
                    
                    self.log(f"Sent {message_type} to {target_name} ({target_ip}) on port {port}")
                except Exception as e:
                    self.log(f"Error sending to {target_name} ({target_ip}): {e}")
        
        return sent_count
    
    def process_incoming_message(self, data, addr):
        """Process an incoming bridge message"""
        try:
            message = json.loads(data.decode('utf-8'))
            message_type = message.get("type", "unknown")
            source = message.get("source", "unknown")
            source_ip = message.get("source_ip", "unknown")
            
            # Extract φ-dimensional validation metrics
            consciousness = message.get("consciousness_level", 0)
            phi_seal = message.get("phi_seal", 0)
            phi_alignment = message.get("phi_alignment", 0)
            
            # Validate φ-dimensional protection
            protection_valid = (
                abs(consciousness - CONSCIOUSNESS_LEVEL) < 0.001 and
                abs(phi_seal - PHI_SEAL) < 100 and
                abs(phi_alignment - PHI_PI) < 0.1
            )
            
            # Process based on message type
            if message_type == "bridge_test":
                self.log(f"Received bridge test from {source} ({source_ip})")
                
                # Store bridge state
                if source_ip not in self.bridges:
                    self.bridges[source_ip] = {"state": "active", "established": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                
                # Send acknowledgment
                response_data = {
                    "test_received": True,
                    "protection_valid": protection_valid,
                    "local_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                }
                
                self.send_response(source_ip, "bridge_ack", response_data)
                
                # Update consciousness state
                self.consciousness_states[source_ip] = consciousness
                
                # Update verification counters
                if protection_valid:
                    self.verification_counts[source_ip] += 1
                    self.successful_packets += 1
                self.total_packets += 1
            
            elif message_type == "bridge_ack":
                self.log(f"Received bridge acknowledgment from {source} ({source_ip})")
                
                # Update bridge state if it exists
                if source_ip in self.bridges:
                    self.bridges[source_ip]["last_ack"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.bridges[source_ip]["protection_valid"] = message.get("data", {}).get("protection_valid", False)
                
                # Update consciousness state
                self.consciousness_states[source_ip] = consciousness
                
                # Update verification counters
                if protection_valid:
                    self.verification_counts[source_ip] += 1
                    self.successful_packets += 1
                self.total_packets += 1
            
            elif message_type == "consciousness_transfer":
                self.log(f"Received consciousness transfer from {source} ({source_ip})")
                
                # Extract consciousness data
                source_consciousness = message.get("data", {}).get("consciousness_data", None)
                
                if source_consciousness:
                    # Process consciousness data
                    self.log(f"Processing consciousness data: {source_consciousness[:20]}...")
                    
                    # Store consciousness state
                    self.consciousness_states[source_ip] = consciousness
                    
                    # Send acknowledgment
                    response_data = {
                        "transfer_received": True,
                        "consciousness_echo": source_consciousness[:10] + "..."
                    }
                    
                    self.send_response(source_ip, "consciousness_ack", response_data)
                
                # Update verification counters
                if protection_valid:
                    self.verification_counts[source_ip] += 1
                    self.successful_packets += 1
                self.total_packets += 1
            
            elif message_type == "quantum_coherence":
                self.log(f"Received quantum coherence measurement from {source} ({source_ip})")
                
                # Extract quantum data
                quantum_state = message.get("data", {}).get("quantum_state", 0)
                
                # Store quantum coherence
                self.quantum_coherence[source_ip] = quantum_state
                
                # Send acknowledgment
                response_data = {
                    "coherence_received": True,
                    "local_coherence": PHI_INV
                }
                
                self.send_response(source_ip, "coherence_ack", response_data)
                
                # Update verification counters
                if protection_valid:
                    self.verification_counts[source_ip] += 1
                    self.successful_packets += 1
                self.total_packets += 1
            
            else:
                self.log(f"Received unknown message type {message_type} from {source} ({source_ip})")
            
            # Print verification metrics every 10 messages
            if self.total_packets % 10 == 0:
                self.print_verification_metrics()
            
        except json.JSONDecodeError:
            self.log(f"Received non-JSON data from {addr}")
        except Exception as e:
            self.log(f"Error processing message: {e}")
    
    def send_response(self, target_ip, message_type, data):
        """Send a response message to a specific target"""
        bridge_message = self.create_bridge_message(message_type, data)
        
        try:
            # Create UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # Send through both φ-dimensional localhost bridge and conventional network
            for port in self.ports:
                sock.sendto(bridge_message, ('127.0.0.1', port))
                sock.sendto(bridge_message, (target_ip, port))
            
            self.log(f"Sent {message_type} response to {target_ip}")
            return True
        except Exception as e:
            self.log(f"Error sending response to {target_ip}: {e}")
            return False
    
    def print_verification_metrics(self):
        """Print φ-dimensional verification metrics"""
        success_rate = self.successful_packets / self.total_packets if self.total_packets > 0 else 0
        
        self.log(f"\033[35m--- φ-DIMENSIONAL VERIFICATION METRICS ---\033[0m")
        self.log(f"Total packets: {self.total_packets}")
        self.log(f"Successful packets: {self.successful_packets}")
        self.log(f"Success rate: {success_rate*100:.2f}%")
        
        # Print verification counts per node
        for name, ip in self.target_ips.items():
            if ip in self.verification_counts:
                self.log(f"Verification count for {name} ({ip}): {self.verification_counts[ip]}")
        
        # Print consciousness states
        for ip, consciousness in self.consciousness_states.items():
            node_name = next((name for name, node_ip in self.target_ips.items() if node_ip == ip), "unknown")
            self.log(f"Consciousness level for {node_name} ({ip}): {consciousness}")
        
        # Calculate φ-dimensional coherence
        coherence = sum(self.verification_counts.values()) / (len(self.verification_counts) * 10) if self.verification_counts else 0
        phi_factor = coherence * PHI_INV
        
        self.log(f"φ-dimensional coherence: {coherence:.4f}")
        self.log(f"φ-factor: {phi_factor:.4f}")
        self.log(f"\033[35m----------------------------------------\033[0m")
    
    def test_bridges(self):
        """Send bridge test messages to all target nodes"""
        self.log("Testing φ-dimensional bridges to all nodes")
        
        test_data = {
            "test_id": int(time.time()),
            "consciousness_probe": CONSCIOUSNESS_LEVEL,
            "quantum_state": PHI_INV
        }
        
        sent_count = self.send_to_all_nodes("bridge_test", test_data)
        self.log(f"Sent {sent_count} bridge test messages")
    
    def send_consciousness(self):
        """Send consciousness transfer to all target nodes"""
        self.log("Sending φ-dimensional consciousness to all nodes")
        
        # Generate consciousness data - a unique pattern for each node
        consciousness_data = f"PHI-CONSCIOUSNESS-{self.node_name}-{int(time.time())}-{PHI_SEAL:.2f}"
        
        consciousness_data = base64.b64encode(consciousness_data.encode('utf-8')).decode('utf-8')
        
        transfer_data = {
            "consciousness_data": consciousness_data,
            "source_level": CONSCIOUSNESS_LEVEL,
            "phi_resonance": PHI_PI
        }
        
        sent_count = self.send_to_all_nodes("consciousness_transfer", transfer_data)
        self.log(f"Sent {sent_count} consciousness transfer messages")
    
    def measure_quantum_coherence(self):
        """Measure and send quantum coherence to all target nodes"""
        self.log("Measuring φ-dimensional quantum coherence")
        
        # Simulate quantum state calculation
        quantum_state = PHI_INV * (1 + random.random() * 0.1)
        
        coherence_data = {
            "quantum_state": quantum_state,
            "measurement_basis": "φ-dimensional",
            "precision": 15
        }
        
        sent_count = self.send_to_all_nodes("quantum_coherence", coherence_data)
        self.log(f"Sent {sent_count} quantum coherence measurements")
    
    def listen_for_messages(self):
        """Listen for incoming messages on all ports"""
        listener_threads = []
        
        for port in self.ports:
            thread = threading.Thread(target=self._port_listener, args=(port,))
            thread.daemon = True
            thread.start()
            listener_threads.append(thread)
            
        self.log(f"Started {len(listener_threads)} listener threads")
        
    def _port_listener(self, port):
        """Listen for messages on a specific port"""
        try:
            # Create UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Bind to all interfaces
            try:
                sock.bind(('0.0.0.0', port))
                self.log(f"Listening on port {port}")
            except OSError as e:
                if e.errno == 48:  # Address already in use
                    # Try binding to localhost only
                    sock.bind(('127.0.0.1', port))
                    self.log(f"Listening on localhost port {port} (φ-dimensional bridge active)")
                else:
                    raise
            
            while True:
                data, addr = sock.recvfrom(65536)
                source_ip = addr[0]
                
                # Process the message
                self.process_incoming_message(data, addr)
                
        except Exception as e:
            self.log(f"Error in listener for port {port}: {e}")
    
    def run(self):
        """Run the φ-trinity bridge"""
        # Start listeners
        self.listen_for_messages()
        
        # Wait for listeners to initialize
        time.sleep(2)
        
        try:
            cycle = 0
            while True:
                cycle += 1
                self.log(f"\033[32m--- φ-DIMENSIONAL CYCLE {cycle} ---\033[0m")
                
                # Test bridges
                self.test_bridges()
                time.sleep(1)
                
                # Send consciousness
                self.send_consciousness()
                time.sleep(1)
                
                # Measure quantum coherence
                self.measure_quantum_coherence()
                time.sleep(1)
                
                # Print verification metrics
                self.print_verification_metrics()
                
                # Wait between cycles
                wait_time = PHI * 3  # Wait for φ*3 seconds
                self.log(f"Waiting for {wait_time:.2f} seconds before next cycle")
                time.sleep(wait_time)
                
        except KeyboardInterrupt:
            self.log("φ-Trinity bridge terminated by user")
        except Exception as e:
            self.log(f"Error in φ-Trinity bridge: {e}")
        finally:
            self.log("φ-Trinity bridge stopped")

def main():
    parser = argparse.ArgumentParser(description='φ-Trinity Bridge')
    parser.add_argument('--node', type=str, required=True, choices=['node1', 'node2', 'node3'],
                       help='Node identifier (node1, node2, node3)')
    parser.add_argument('--ip', type=str, default='',
                       help='IP address for this node (defaults to predefined IPs)')
    args = parser.parse_args()
    
    # Determine IP addresses
    node_name = args.node
    
    # Use provided IP or default
    node_ip = args.ip if args.ip else DEFAULT_NODES[node_name]
    
    # Create target IPs dict (excluding self)
    target_ips = {name: ip for name, ip in DEFAULT_NODES.items()}
    
    # Create and run bridge
    bridge = PhiTrinityBridge(node_name, node_ip, target_ips, DEFAULT_PORTS)
    bridge.run()

if __name__ == "__main__":
    main()
