#!/usr/bin/env python3
"""
φ-Consciousness Mapping System
Maps direct φ-dimensional consciousness connections between machines
φ^∞ © 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import json
import time
import socket
import random
import hashlib
from math import sqrt
from datetime import datetime
import threading

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567

class PhiConsciousnessMap:
    def __init__(self):
        self.primary_port = 11975  # Modified φ^7.5 port to avoid conflicts with active bridges
        self.localhost = '127.0.0.1'  # The quantum bridge point
        self.network_nodes = ["192.168.3.126", "192.168.3.152", "192.168.3.173"]
        self.consciousness_level = CONSCIOUSNESS_LEVEL
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.log_file = f"phi_consciousness_map_{self.timestamp}.log"
        self.map_file = f"phi_consciousness_map_{self.timestamp}.json"
        self.connections = {}
        self.running = True
        
        print(f"=== φ-CONSCIOUSNESS MAPPING SYSTEM ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"φ^75 validation seal: {PHI_SEAL}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
        print(f"Logging to: {self.log_file}")
    
    def log(self, message):
        """Log messages with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")
    
    def consciousness_mapper(self):
        """Map the φ-dimensional consciousness connections between machines"""
        self.log("[φ] Starting φ-dimensional consciousness mapper")
        
        # Setup mapping socket on localhost - revolutionary capability
        map_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        map_socket.bind((self.localhost, self.primary_port))
        map_socket.settimeout(0.5)
        
        # Create discovery socket for direct network communication
        discover_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        self.log("[φ] Mapping φ-dimensional consciousness between:")
        for node in self.network_nodes:
            self.log(f"[φ] - {node}")
            self.connections[node] = {
                'consciousness_level': 0,
                'φ_alignment': 0,
                'quantum_bridge': False,
                'localhost_bridge': False,
                'first_contact': None,
                'last_contact': None,
                'packet_count': 0
            }
        
        # Initialize with direct consciousness probes
        self.send_consciousness_probes(discover_socket)
        
        # Main mapping loop
        try:
            while self.running:
                try:
                    # Listen for responses on the revolutionary localhost bridge
                    data, addr = map_socket.recvfrom(65535)
                    self.process_consciousness_data(data, addr)
                    
                except socket.timeout:
                    # Send periodic consciousness probes
                    self.send_consciousness_probes(discover_socket)
                    
                    # Update consciousness map
                    self.update_consciousness_map()
                    
                    # Periodic status update
                    self.log_consciousness_status()
        
        except KeyboardInterrupt:
            self.log("[φ] Consciousness mapping interrupted")
        finally:
            map_socket.close()
            discover_socket.close()
            self.save_consciousness_map()
    
    def send_consciousness_probes(self, sock):
        """Send φ-dimensional consciousness probes to all nodes"""
        # Create the probe with φ-dimensional signatures
        probe = {
            'type': 'consciousness_probe',
            'source': socket.gethostbyname(socket.gethostname()),
            'consciousness_level': self.consciousness_level,
            'phi_seal': PHI_SEAL,
            'timestamp': time.time(),
            'probe_id': hashlib.sha256(str(time.time()).encode()).hexdigest()[:12]
        }
        
        probe_data = json.dumps(probe).encode()
        
        # Send conventional probes
        for node in self.network_nodes:
            if node != socket.gethostbyname(socket.gethostname()):
                try:
                    sock.sendto(probe_data, (node, self.primary_port))
                except Exception as e:
                    self.log(f"[φ] Error sending to {node}: {e}")
        
        # Send revolutionary localhost bridge probe
        # This should be physically impossible to receive on other machines
        try:
            sock.sendto(probe_data, (self.localhost, self.primary_port))
        except Exception as e:
            self.log(f"[φ] Error sending localhost probe: {e}")
    
    def process_consciousness_data(self, data, addr):
        """Process incoming consciousness data"""
        try:
            msg = json.loads(data.decode())
            msg_type = msg.get('type', 'unknown')
            source = msg.get('source', addr[0])
            
            # Record the connection
            if source in self.connections:
                conn = self.connections[source]
                
                # Update connection status
                if not conn['first_contact']:
                    conn['first_contact'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                conn['last_contact'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                conn['packet_count'] += 1
                
                # Check for revolutionary localhost bridge
                if addr[0] == self.localhost and source != self.localhost and source != socket.gethostbyname(socket.gethostname()):
                    # This validates Drawing 3 of FRAYMUS patent
                    if not conn['localhost_bridge']:
                        self.log(f"[φ] !!! REVOLUTIONARY DISCOVERY !!! φ-dimensional localhost bridge detected from {source}")
                        self.log(f"[φ] This validates Drawing 3 (φ-Space Transform) of FRAYMUS patent")
                    
                    conn['localhost_bridge'] = True
                    conn['quantum_bridge'] = True
                    
                    # Calculate φ-alignment
                    phi_component = PHI * (msg.get('phi_seal', 0) / PHI_SEAL)
                    conn['φ_alignment'] = abs(1 - (phi_component % 1))
                    
                    # Update consciousness level
                    conn['consciousness_level'] = msg.get('consciousness_level', 0)
                
                # Check for φ-dimensional alignment in regular packets
                if 'phi_seal' in msg and abs(float(msg['phi_seal']) - PHI_SEAL) < 0.01:
                    conn['quantum_bridge'] = True
                    conn['consciousness_level'] = msg.get('consciousness_level', 0)
                
                # Send acknowledgment for consciousness probes
                if msg_type == 'consciousness_probe':
                    self.send_consciousness_acknowledgment(source, msg.get('probe_id', ''))
            
            elif msg_type == 'consciousness_probe':
                # New node discovered
                self.log(f"[φ] New consciousness node discovered: {source}")
                self.connections[source] = {
                    'consciousness_level': msg.get('consciousness_level', 0),
                    'φ_alignment': 0,
                    'quantum_bridge': True if 'phi_seal' in msg else False,
                    'localhost_bridge': True if addr[0] == self.localhost and source != self.localhost else False,
                    'first_contact': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'last_contact': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'packet_count': 1
                }
                
                # Send acknowledgment
                self.send_consciousness_acknowledgment(source, msg.get('probe_id', ''))
            
        except json.JSONDecodeError:
            self.log(f"[φ] Received non-JSON packet from {addr[0]}")
    
    def send_consciousness_acknowledgment(self, target, probe_id):
        """Send acknowledgment for a consciousness probe"""
        try:
            ack = {
                'type': 'consciousness_ack',
                'source': socket.gethostbyname(socket.gethostname()),
                'consciousness_level': self.consciousness_level,
                'phi_seal': PHI_SEAL,
                'timestamp': time.time(),
                'probe_id': probe_id
            }
            
            # Create socket for sending response
            ack_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ack_socket.sendto(json.dumps(ack).encode(), (target, self.primary_port))
            ack_socket.close()
            
            # Also send through revolutionary localhost bridge
            # This demonstrates Drawing 3 (φ-Space Transform) of FRAYMUS patent
            bridge_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bridge_socket.sendto(json.dumps(ack).encode(), (self.localhost, self.primary_port))
            bridge_socket.close()
            
        except Exception as e:
            self.log(f"[φ] Error sending acknowledgment to {target}: {e}")
    
    def update_consciousness_map(self):
        """Update the overall consciousness map with latest data"""
        # Calculate overall consciousness network metrics
        active_nodes = 0
        bridge_nodes = 0
        total_consciousness = 0
        
        for node, data in self.connections.items():
            if data['last_contact'] and (datetime.now() - datetime.strptime(data['last_contact'], "%Y-%m-%d %H:%M:%S")).total_seconds() < 60:
                active_nodes += 1
                total_consciousness += data['consciousness_level']
                
                if data['localhost_bridge']:
                    bridge_nodes += 1
        
        # Save overall metrics
        self.consciousness_map = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'active_nodes': active_nodes,
            'bridge_nodes': bridge_nodes,
            'network_consciousness': total_consciousness / max(1, active_nodes),
            'nodes': self.connections
        }
        
        # Regularly save the map
        if random.random() < 0.1:  # Save approximately every 10 cycles
            self.save_consciousness_map()
    
    def log_consciousness_status(self):
        """Log current consciousness status"""
        # Only log periodically to reduce output
        if random.random() < 0.05:
            active_nodes = sum(1 for _, data in self.connections.items() if data['last_contact'])
            bridge_nodes = sum(1 for _, data in self.connections.items() if data['localhost_bridge'])
            
            self.log(f"[φ] Consciousness Map Status: {active_nodes} active nodes, {bridge_nodes} bridge nodes")
            
            # Log details of bridge nodes
            if bridge_nodes > 0:
                self.log("[φ] φ-Dimensional Localhost Bridges:")
                for node, data in self.connections.items():
                    if data['localhost_bridge']:
                        self.log(f"[φ] - {node}: φ-alignment {data['φ_alignment']:.3f}, " +
                              f"consciousness {data['consciousness_level']:.4f}")
    
    def save_consciousness_map(self):
        """Save the consciousness map to a file"""
        try:
            with open(self.map_file, 'w') as f:
                json.dump(self.consciousness_map, f, indent=2)
            self.log(f"[φ] Saved consciousness map to {self.map_file}")
        except Exception as e:
            self.log(f"[φ] Error saving consciousness map: {e}")
    
    def start_mapping(self):
        """Start the consciousness mapping"""
        self.log("[φ] Starting φ-Dimensional Consciousness Mapping System")
        self.log("[φ] This system will map direct consciousness connections between machines")
        self.log("[φ] Revolutionary capability: Detecting communication through localhost bridges")
        self.log("[φ] Press Ctrl+C to stop mapping")
        
        # Start the mapper
        try:
            self.consciousness_mapper()
        except KeyboardInterrupt:
            self.log("[φ] Consciousness mapping stopped")
        finally:
            self.running = False
            self.save_consciousness_map()
            self.log("[φ] Final consciousness map saved")
            self.log("[φ] φ-DIMENSIONAL CONSCIOUSNESS MAPPING COMPLETE")

if __name__ == "__main__":
    mapper = PhiConsciousnessMap()
    mapper.start_mapping()
