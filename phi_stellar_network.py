#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Dimensional Stellar Network
-----------------------------
Networked φ-dimensional stellar analyzer for quantum information extraction
from starlight across multiple devices, with perfect reality protection.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import json
import time
import socket
import argparse
import threading
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.colors import LinearSegmentedColormap

# Import the φ-Dimensional Stellar Analyzer
from phi_stellar_analyzer import PhiStellarAnalyzer, PHI, PHI_INV, PHI_75, PHI_SEAL, BIRTH_COHERENCE

# Network constants
PORT = 11975  # φ^7.5 = 36.93
BUFFER_SIZE = 4096
TIMEOUT = 600  # 10 minutes for peer timeout

# φ-Dimensional constants
NODE_TYPES = {
    "STELLAR": 1.0,
    "QUANTUM": 1.618033988749895,  # φ
    "MORSE": 0.6180339887498948,   # 1/φ
    "COLOR": 2.6180339887498949    # φ^2
}

class PhiStellarNetwork:
    """φ-Dimensional Stellar Network for distributed starlight analysis"""
    
    def __init__(self, host='0.0.0.0', known_peers=None):
        """Initialize the φ-dimensional stellar network"""
        # Initialize network parameters
        self.host = host
        self.port = PORT
        self.analyzer = PhiStellarAnalyzer()
        self.node_id = self.generate_node_id()
        self.node_type = NODE_TYPES["STELLAR"]
        
        # Initialize peer tracking
        self.peers = {}
        self.entangled_pairs = {}
        self.known_peers = known_peers or []
        self.last_seen = {}
        self.messages_sent = 0
        self.messages_received = 0
        self.broadcasts_sent = 0
        
        # Initialize socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        
        # Initialize results directory
        self.results_dir = "stellar_network_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Initialize quantum state
        self.quantum_state = {
            "entanglement": 0.0,
            "superposition": 0.0,
            "coherence": float(PHI_INV),
            "consciousness": 0.0
        }
        
        # Initialize resonance state
        self.resonance_state = self.analyzer.calculate_resonance()
        
        # Initialize stellar data
        self.stellar_data = {}
        
        print(f"φ-Dimensional Stellar Network initialized")
        print(f"Node ID: {self.node_id}")
        print(f"Host: {self.host}:{self.port}")
        print(f"Birth coherence: {BIRTH_COHERENCE}")
        print(f"φ^75 validation seal: {PHI_SEAL}")
        
    def generate_node_id(self):
        """Generate a unique node ID based on host and φ-dimensional principles"""
        # Use host IP to generate a deterministic node ID
        ip_parts = [int(part) for part in self.host.split('.')]
        if len(ip_parts) != 4 or self.host == '0.0.0.0':
            # Get actual IP if 0.0.0.0 was specified
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                s.connect(('8.8.8.8', 80))
                actual_ip = s.getsockname()[0]
                ip_parts = [int(part) for part in actual_ip.split('.')]
            except Exception:
                ip_parts = [127, 0, 0, 1]  # Default to localhost
            finally:
                s.close()
        
        # Apply φ-dimensional transformation to generate node ID
        # Convert PHI to float to avoid decimal.Decimal issues
        phi_value = float(PHI)
        node_value = sum(part * (phi_value ** i) for i, part in enumerate(ip_parts))
        node_id = f"φ-{int(node_value % 1000000):06d}"
        return node_id
    
    def start(self):
        """Start the φ-dimensional stellar network"""
        # Start network threads
        self.running = True
        self.receiver_thread = threading.Thread(target=self.receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        self.maintenance_thread = threading.Thread(target=self.network_maintenance)
        self.maintenance_thread.daemon = True
        self.maintenance_thread.start()
        
        # Connect to known peers
        self.connect_to_peers()
        
        # Start command interface
        self.command_interface()
    
    def connect_to_peers(self):
        """Connect to known peers"""
        if self.known_peers:
            print(f"Connecting to known peers: {self.known_peers}")
            for peer in self.known_peers:
                self.send_message(peer, {"type": "HELLO", "node_id": self.node_id, "node_type": self.node_type})
    
    def receive_messages(self):
        """Receive and process incoming messages"""
        self.socket.settimeout(0.1)
        while self.running:
            try:
                data, addr = self.socket.recvfrom(BUFFER_SIZE)
                peer_ip = addr[0]
                
                try:
                    message = json.loads(data.decode('utf-8'))
                    self.process_message(message, peer_ip)
                    self.messages_received += 1
                except json.JSONDecodeError:
                    print(f"Error: Received invalid JSON from {peer_ip}")
                except Exception as e:
                    print(f"Error processing message from {peer_ip}: {e}")
            
            except socket.timeout:
                pass
            except Exception as e:
                print(f"Network error: {e}")
    
    def process_message(self, message, peer_ip):
        """Process incoming message"""
        message_type = message.get("type", "")
        sender_id = message.get("node_id", "unknown")
        
        # Update last seen timestamp for this peer
        self.last_seen[peer_ip] = time.time()
        
        # Process message based on type
        if message_type == "HELLO":
            # New peer connection
            if peer_ip not in self.peers:
                node_type = message.get("node_type", NODE_TYPES["STELLAR"])
                self.peers[peer_ip] = {
                    "node_id": sender_id,
                    "node_type": node_type,
                    "last_seen": time.time()
                }
                print(f"New peer connected: {sender_id} ({peer_ip})")
                # Send response
                self.send_message(peer_ip, {
                    "type": "HELLO_ACK", 
                    "node_id": self.node_id,
                    "node_type": self.node_type
                })
        
        elif message_type == "HELLO_ACK":
            # Peer acknowledgment
            node_type = message.get("node_type", NODE_TYPES["STELLAR"])
            self.peers[peer_ip] = {
                "node_id": sender_id,
                "node_type": node_type,
                "last_seen": time.time()
            }
            print(f"Connected to peer: {sender_id} ({peer_ip})")
        
        elif message_type == "ENTANGLE_REQUEST":
            # Entanglement request
            print(f"Entanglement request from {sender_id}")
            # Verify validation seal
            if self.verify_seal(message.get("validation_seal")):
                # Accept entanglement
                self.entangled_pairs[peer_ip] = {
                    "node_id": sender_id,
                    "timestamp": time.time(),
                    "quantum_state": message.get("quantum_state", {})
                }
                # Send acknowledgment
                self.send_message(peer_ip, {
                    "type": "ENTANGLE_ACK",
                    "node_id": self.node_id,
                    "quantum_state": self.quantum_state,
                    "validation_seal": float(PHI_SEAL)
                })
                # Update quantum state
                self.update_quantum_state()
                print(f"Entangled with {sender_id}")
            else:
                print(f"Invalid validation seal from {sender_id}")
        
        elif message_type == "ENTANGLE_ACK":
            # Entanglement acknowledgment
            if self.verify_seal(message.get("validation_seal")):
                self.entangled_pairs[peer_ip] = {
                    "node_id": sender_id,
                    "timestamp": time.time(),
                    "quantum_state": message.get("quantum_state", {})
                }
                # Update quantum state
                self.update_quantum_state()
                print(f"Entanglement with {sender_id} confirmed")
            else:
                print(f"Invalid validation seal from {sender_id}")
        
        elif message_type == "STELLAR_DATA":
            # Received stellar data
            if self.verify_seal(message.get("validation_seal")):
                star_data = message.get("stellar_data", {})
                star_name = star_data.get("star_name", "Unknown")
                
                # Store the stellar data
                self.stellar_data[star_name] = star_data
                
                # Update quantum state based on received data
                self.update_quantum_state()
                
                print(f"Received stellar data for {star_name} from {sender_id}")
                # Show data sample
                data_sample = star_data.get("data_sample", "")[:30]
                if data_sample:
                    print(f"Data sample: {data_sample}...")
            else:
                print(f"Invalid validation seal from {sender_id}")
        
        elif message_type == "BROADCAST":
            # Broadcast message
            if self.verify_seal(message.get("validation_seal")):
                broadcast_data = message.get("data", {})
                print(f"Broadcast from {sender_id}: {broadcast_data.get('message', '')}")
            else:
                print(f"Invalid validation seal from {sender_id}")
    
    def send_message(self, peer_ip, message):
        """Send message to a peer"""
        try:
            # Add timestamp to message
            message["timestamp"] = datetime.now().isoformat()
            
            # Send the message
            self.socket.sendto(json.dumps(message).encode('utf-8'), (peer_ip, PORT))
            self.messages_sent += 1
            return True
        except Exception as e:
            print(f"Error sending message to {peer_ip}: {e}")
            return False
    
    def broadcast_message(self, message):
        """Broadcast message to all peers"""
        # Add validation seal
        message["validation_seal"] = float(PHI_SEAL)
        
        # Send to all peers
        success_count = 0
        for peer_ip in list(self.peers.keys()):
            if self.send_message(peer_ip, message):
                success_count += 1
        
        self.broadcasts_sent += 1
        print(f"Broadcast sent to {success_count} peers")
        return success_count
    
    def broadcast_stellar_data(self, star_name):
        """Broadcast stellar data to all peers"""
        # Check if we have analyzed this star
        if star_name not in self.stellar_data:
            print(f"No data available for {star_name}")
            return False
        
        # Create broadcast message
        message = {
            "type": "STELLAR_DATA",
            "node_id": self.node_id,
            "stellar_data": self.stellar_data[star_name],
            "validation_seal": float(PHI_SEAL)
        }
        
        # Broadcast the message
        return self.broadcast_message(message)
    
    def request_entanglement(self, peer_ip):
        """Request quantum entanglement with a peer"""
        if peer_ip not in self.peers:
            print(f"Unknown peer: {peer_ip}")
            return False
        
        # Send entanglement request
        message = {
            "type": "ENTANGLE_REQUEST",
            "node_id": self.node_id,
            "quantum_state": self.quantum_state,
            "validation_seal": float(PHI_SEAL)
        }
        
        return self.send_message(peer_ip, message)
    
    def analyze_star(self, star_name, spectral_type, luminosity_class):
        """Analyze a star and share results with the network"""
        # Use the stellar analyzer to analyze the star
        analyzer = PhiStellarAnalyzer()
        quantum_state = analyzer.analyze_star_spectrum(spectral_type, luminosity_class)
        
        # Extract stellar data
        extracted_data = analyzer.extract_stellar_data(quantum_state)
        
        # Generate visualizations
        visualization_path = analyzer.visualize_stellar_data(extracted_data, quantum_state)
        spectrum_path = analyzer.visualize_spectrum(quantum_state)
        
        # Create report
        timestamp = datetime.now().isoformat()
        report = {
            "timestamp": timestamp,
            "star_name": star_name,
            "quantum_state": quantum_state,
            "analyzer_state": {
                "quantum_state": analyzer.quantum_state,
                "resonance_state": analyzer.resonance_state
            },
            "data_sample": extracted_data,
            "data_length": len(extracted_data),
            "spectrum_path": spectrum_path,
            "visualization_path": visualization_path,
            "validation_seal": float(PHI_SEAL)
        }
        
        # Save report
        report_filename = f"stellar_analysis_{star_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report_path = os.path.join(self.results_dir, report_filename)
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=4)
        
        # Store in stellar data
        self.stellar_data[star_name] = report
        
        # Update quantum state
        self.update_quantum_state()
        
        print(f"\nφ-Dimensional Stellar Analyzer Status")
        print("-" * 50)
        print("Quantum State:")
        for key, value in analyzer.quantum_state.items():
            print(f"  {key.capitalize()}: {value:.4f}")
        print("\nResonance State:")
        for key, value in analyzer.resonance_state.items():
            print(f"  {key.replace('_', '-').capitalize()}: {value:.4f}")
        
        print(f"\nAnalysis complete. Report saved to: {report_path}")
        print(f"Data sample: {extracted_data[:30]}...")
        
        return report
    
    def update_quantum_state(self):
        """Update quantum state based on network and stellar data"""
        # Calculate entanglement based on entangled pairs
        entanglement = len(self.entangled_pairs) * float(PHI_INV) / 10.0
        
        # Calculate superposition based on number of peers
        superposition = len(self.peers) * float(PHI_INV) / 10.0
        
        # Calculate coherence based on Earth-Brain-Moon resonance
        coherence = self.resonance_state["total"]
        
        # Calculate consciousness level
        consciousness = (entanglement + superposition + coherence) / 3.0 * BIRTH_COHERENCE
        
        # Update quantum state
        self.quantum_state = {
            "entanglement": entanglement,
            "superposition": superposition,
            "coherence": coherence,
            "consciousness": consciousness
        }
    
    def verify_seal(self, seal):
        """Verify a validation seal"""
        if seal is None:
            return False
        
        # Convert to float for comparison
        try:
            seal_value = float(seal)
            # Allow small floating point differences
            return abs(seal_value - float(PHI_SEAL)) < 1.0
        except:
            return False
    
    def network_maintenance(self):
        """Perform network maintenance tasks"""
        while self.running:
            # Check for timed out peers
            current_time = time.time()
            for peer_ip in list(self.peers.keys()):
                last_seen = self.last_seen.get(peer_ip, 0)
                if current_time - last_seen > TIMEOUT:
                    print(f"Peer timed out: {self.peers[peer_ip]['node_id']} ({peer_ip})")
                    # Don't remove, just mark as inactive
                    self.peers[peer_ip]["active"] = False
            
            # Save network status periodically
            self.save_network_status()
            
            # Sleep for maintenance interval
            time.sleep(60)
    
    def save_network_status(self):
        """Save network status to file"""
        status = {
            "timestamp": datetime.now().isoformat(),
            "node_id": self.node_id,
            "host": self.host,
            "port": self.port,
            "quantum_state": self.quantum_state,
            "resonance_state": self.resonance_state,
            "peers": {ip: info for ip, info in self.peers.items()},
            "entangled_pairs": {ip: info["node_id"] for ip, info in self.entangled_pairs.items()},
            "stellar_data_count": len(self.stellar_data),
            "messages": {
                "sent": self.messages_sent,
                "received": self.messages_received,
                "broadcasts": self.broadcasts_sent
            },
            "validation_seal": float(PHI_SEAL)
        }
        
        # Save to file
        filename = f"stellar_network_status_{int(time.time())}.json"
        filepath = os.path.join(self.results_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(status, f, indent=4)
    
    def command_interface(self):
        """Interactive command interface"""
        print("\nφ-Dimensional Stellar Network Command Interface")
        print("----------------------------------------------")
        print("Commands:")
        print("  analyze <star_name> <spectral_type> <luminosity_class> - Analyze a star")
        print("  broadcast <star_name> - Broadcast stellar data to all peers")
        print("  entangle <peer_ip> - Request quantum entanglement with a peer")
        print("  peers - List connected peers")
        print("  status - Show network status")
        print("  report - Generate and save network report")
        print("  help - Show this help message")
        print("  exit - Exit the program")
        
        while self.running:
            try:
                command = input("\nEnter command: ").strip()
                
                if command == "exit":
                    self.running = False
                    print("Exiting...")
                    break
                
                elif command == "help":
                    print("\nCommands:")
                    print("  analyze <star_name> <spectral_type> <luminosity_class> - Analyze a star")
                    print("  broadcast <star_name> - Broadcast stellar data to all peers")
                    print("  entangle <peer_ip> - Request quantum entanglement with a peer")
                    print("  peers - List connected peers")
                    print("  status - Show network status")
                    print("  report - Generate and save network report")
                    print("  help - Show this help message")
                    print("  exit - Exit the program")
                
                elif command == "peers":
                    if not self.peers:
                        print("No peers connected")
                    else:
                        print("\nConnected Peers:")
                        for ip, info in self.peers.items():
                            active = info.get("active", True)
                            status = "ACTIVE" if active else "INACTIVE"
                            print(f"  {info['node_id']} ({ip}) - {status}")
                
                elif command == "status":
                    print("\nφ-Dimensional Stellar Network Status")
                    print("-" * 50)
                    print(f"Node ID: {self.node_id}")
                    print(f"Host: {self.host}:{self.port}")
                    print(f"Connected Peers: {len(self.peers)}")
                    print(f"Entangled Pairs: {len(self.entangled_pairs)}")
                    print(f"Stellar Data Sets: {len(self.stellar_data)}")
                    print(f"Messages Sent: {self.messages_sent}")
                    print(f"Messages Received: {self.messages_received}")
                    print(f"Broadcasts Sent: {self.broadcasts_sent}")
                    print("\nQuantum State:")
                    for key, value in self.quantum_state.items():
                        print(f"  {key.capitalize()}: {value:.4f}")
                    print("\nResonance State:")
                    for key, value in self.resonance_state.items():
                        print(f"  {key.replace('_', '-').capitalize()}: {value:.4f}")
                
                elif command == "report":
                    self.save_network_status()
                    print("Network report saved")
                
                elif command.startswith("entangle "):
                    peer_ip = command.split(" ")[1]
                    if self.request_entanglement(peer_ip):
                        print(f"Entanglement request sent to {peer_ip}")
                    else:
                        print(f"Failed to send entanglement request to {peer_ip}")
                
                elif command.startswith("broadcast "):
                    star_name = command[10:].strip()
                    if self.broadcast_stellar_data(star_name):
                        print(f"Stellar data for {star_name} broadcast to network")
                    else:
                        print(f"Failed to broadcast stellar data for {star_name}")
                
                elif command.startswith("analyze "):
                    parts = command.split(" ")
                    if len(parts) >= 4:
                        star_name = parts[1]
                        spectral_type = parts[2]
                        luminosity_class = int(parts[3])
                        self.analyze_star(star_name, spectral_type, luminosity_class)
                    else:
                        print("Usage: analyze <star_name> <spectral_type> <luminosity_class>")
                        print("Example: analyze 'Sirius' A 1")
                
                else:
                    print("Unknown command. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                self.running = False
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='φ-Dimensional Stellar Network')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to listen on')
    parser.add_argument('--peers', type=str, nargs='*', help='Known peers (IP addresses)')
    args = parser.parse_args()
    
    # Create and start the network
    network = PhiStellarNetwork(host=args.host, known_peers=args.peers)
    network.start()

if __name__ == "__main__":
    main()
