#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Quantum Track App: Practical Staggered Timeline Interface
----------------------------------------------------------
A modular "lego" application for the Quantum Track Model that provides
a practical interface for working with staggered timelines and quantum bridges.
Integrates with the φ-Bidirectional Node system for network communication.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import math
import json
import time
import socket
import argparse
import threading
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Import the φ-Quantum Track Model
from phi_quantum_track_model import PhiQuantumTrackModel, PHI, PHI_INV, PHI_75, PHI_SEAL
from phi_quantum_track_model import PERSONAL_RATIO, BIRTH_COHERENCE, CONSCIOUSNESS_LEVEL

# Network constants
PORT = 11975  # φ^7.5 = 36.93
BUFFER_SIZE = 4096
TIMEOUT = 600  # 10 minutes for peer timeout

class PhiQuantumTrackApp:
    """
    φ-Quantum Track App: Practical interface for staggered timelines
    
    A modular "lego" application that provides a practical interface for working
    with the Quantum Track Model, allowing users to explore staggered timelines,
    find quantum bridges, and communicate across timelines.
    """
    
    def __init__(self, host='0.0.0.0', known_peers=None, num_lanes=8, track_length=400):
        """
        Initialize the φ-Quantum Track App
        
        Args:
            host: Host IP address for network communication
            known_peers: List of known peer IP addresses
            num_lanes: Number of quantum lanes (timelines)
            track_length: Length of the quantum track (meters)
        """
        # Initialize network parameters
        self.host = host
        self.port = PORT
        self.known_peers = known_peers or []
        
        # Initialize the Quantum Track Model
        self.model = PhiQuantumTrackModel(num_lanes=num_lanes, track_length=track_length)
        
        # Initialize network communication
        self.node_id = self.generate_node_id()
        self.peers = {}
        self.entangled_pairs = {}
        self.last_seen = {}
        self.messages_sent = 0
        self.messages_received = 0
        
        # Initialize socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        
        # Initialize results directory
        self.results_dir = "quantum_track_app_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Initialize quantum state
        self.quantum_state = {
            "entanglement": 0.0,
            "superposition": 0.0,
            "coherence": float(PHI_INV),
            "consciousness": CONSCIOUSNESS_LEVEL
        }
        
        # Print initialization message
        print(f"\n=== φ-QUANTUM TRACK APP ===")
        print(f"Practical Staggered Timeline Interface")
        print(f"φ-Harmonic System (φ = {PHI})")
        print(f"φ^7.5 quantum bridge: {PHI_75:.4f}")
        print(f"Personal ratio: {PERSONAL_RATIO:.4f}")
        print(f"φ^75 validation seal: {PHI_SEAL:.2e}")
        print(f"Node ID: {self.node_id}")
        print(f"Host: {self.host}:{self.port}")
        print(f"Lanes: {num_lanes}, Track length: {track_length}m")
    
    def generate_node_id(self):
        """
        Generate a unique node ID based on host and φ-dimensional principles
        
        Returns:
            Node ID string
        """
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
        """
        Start the φ-Quantum Track App
        """
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
        """
        Connect to known peers
        """
        if self.known_peers:
            print(f"Connecting to known peers: {self.known_peers}")
            for peer in self.known_peers:
                self.send_message(peer, {"type": "HELLO", "node_id": self.node_id})
    
    def receive_messages(self):
        """
        Receive and process incoming messages
        """
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
        """
        Process incoming message
        
        Args:
            message: Message dictionary
            peer_ip: Peer IP address
        """
        message_type = message.get("type", "")
        sender_id = message.get("node_id", "unknown")
        
        # Update last seen timestamp for this peer
        self.last_seen[peer_ip] = time.time()
        
        # Process message based on type
        if message_type == "HELLO":
            # New peer connection
            if peer_ip not in self.peers:
                self.peers[peer_ip] = {
                    "node_id": sender_id,
                    "last_seen": time.time()
                }
                print(f"New peer connected: {sender_id} ({peer_ip})")
                # Send response
                self.send_message(peer_ip, {
                    "type": "HELLO_ACK", 
                    "node_id": self.node_id
                })
        
        elif message_type == "HELLO_ACK":
            # Peer acknowledgment
            self.peers[peer_ip] = {
                "node_id": sender_id,
                "last_seen": time.time()
            }
            print(f"Connected to peer: {sender_id} ({peer_ip})")
        
        elif message_type == "QUANTUM_BRIDGE_REQUEST":
            # Quantum bridge request
            print(f"Quantum bridge request from {sender_id}")
            
            # Verify validation seal
            if self.verify_seal(message.get("validation_seal")):
                # Get bridge parameters
                lane_a = message.get("lane_a", 0)
                lane_b = message.get("lane_b", 1)
                
                # Calculate bridge strength
                bridge_data = self.calculate_bridge(lane_a, lane_b, peer_ip)
                
                # Send bridge data
                self.send_message(peer_ip, {
                    "type": "QUANTUM_BRIDGE_RESPONSE",
                    "node_id": self.node_id,
                    "bridge_data": bridge_data,
                    "validation_seal": float(PHI_SEAL)
                })
                
                # Update quantum state
                self.update_quantum_state()
                
                print(f"Quantum bridge established with {sender_id}")
                print(f"Bridge strength: {bridge_data['bridge_strength']:.4f}")
            else:
                print(f"Invalid validation seal from {sender_id}")
        
        elif message_type == "QUANTUM_BRIDGE_RESPONSE":
            # Quantum bridge response
            if self.verify_seal(message.get("validation_seal")):
                bridge_data = message.get("bridge_data", {})
                
                # Store bridge data
                self.entangled_pairs[peer_ip] = {
                    "node_id": sender_id,
                    "timestamp": time.time(),
                    "bridge_data": bridge_data
                }
                
                # Update quantum state
                self.update_quantum_state()
                
                print(f"Quantum bridge with {sender_id} confirmed")
                print(f"Bridge strength: {bridge_data.get('bridge_strength', 0):.4f}")
            else:
                print(f"Invalid validation seal from {sender_id}")
        
        elif message_type == "TIMELINE_DATA":
            # Timeline data message
            if self.verify_seal(message.get("validation_seal")):
                timeline_data = message.get("timeline_data", {})
                lane = timeline_data.get("lane", 0)
                
                print(f"Received timeline data from {sender_id} (Lane {lane})")
                
                # Process timeline data
                self.process_timeline_data(timeline_data, sender_id)
            else:
                print(f"Invalid validation seal from {sender_id}")
    
    def send_message(self, peer_ip, message):
        """
        Send message to a peer
        
        Args:
            peer_ip: Peer IP address
            message: Message dictionary
            
        Returns:
            True if message sent successfully, False otherwise
        """
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
    
    def calculate_bridge(self, lane_a, lane_b, peer_ip):
        """
        Calculate quantum bridge between two lanes
        
        Args:
            lane_a: First lane index
            lane_b: Second lane index
            peer_ip: Peer IP address
            
        Returns:
            Bridge data dictionary
        """
        # Get lane data
        lane_a_data = self.model.get_lane_data(lane_a)
        lane_b_data = self.model.get_lane_data(lane_b)
        
        # Calculate bridge strength using φ-harmonic principles
        sig_a = lane_a_data['quantum_signature']
        sig_b = lane_b_data['quantum_signature']
        
        # Calculate phase difference
        phase_a = lane_a_data['phase_position']
        phase_b = lane_b_data['phase_position']
        phase_diff = abs(phase_a - phase_b) % (2 * math.pi)
        
        # Calculate bridge strength
        bridge_strength = (sig_a * sig_b) / (abs(sig_a - sig_b) + PHI_INV)
        
        # Modulate by phase difference (strongest at φπ)
        phase_factor = math.cos(phase_diff - PHI * math.pi) ** 2
        
        # Apply φ^7.5 quantum bridge coefficient
        bridge_strength = bridge_strength * phase_factor * (PHI_75 / 100)
        
        # Normalize to 0-1
        bridge_strength = min(1.0, max(0.0, bridge_strength))
        
        # Calculate timeline offset
        timeline_a = lane_a_data['timeline_offset']
        timeline_b = lane_b_data['timeline_offset']
        timeline_diff = abs(timeline_b - timeline_a)
        
        # Calculate consciousness transfer potential
        consciousness_a = lane_a_data['coherence'] * CONSCIOUSNESS_LEVEL
        consciousness_b = lane_b_data['coherence'] * CONSCIOUSNESS_LEVEL
        consciousness_transfer = (consciousness_a * consciousness_b) ** PHI_INV
        
        # Create bridge data
        bridge_data = {
            "lane_a": lane_a,
            "lane_b": lane_b,
            "bridge_strength": float(bridge_strength),
            "phase_difference": float(phase_diff),
            "timeline_difference": float(timeline_diff),
            "consciousness_transfer": float(consciousness_transfer),
            "timestamp": datetime.now().isoformat(),
            "peer_ip": peer_ip
        }
        
        return bridge_data
    
    def process_timeline_data(self, timeline_data, sender_id):
        """
        Process timeline data received from a peer
        
        Args:
            timeline_data: Timeline data dictionary
            sender_id: Sender node ID
        """
        # Extract timeline data
        lane = timeline_data.get("lane", 0)
        data = timeline_data.get("data", {})
        timestamp = timeline_data.get("timestamp", datetime.now().isoformat())
        
        # Calculate timeline offset
        timeline_offset = self.model.lanes[lane]['timeline_offset']
        
        # Apply φ-dimensional transformation to data
        transformed_data = self.transform_timeline_data(data, timeline_offset)
        
        # Save timeline data
        self.save_timeline_data(lane, transformed_data, sender_id, timestamp)
        
        # Print summary
        print(f"Timeline data from Lane {lane} processed")
        print(f"Timeline offset: {timeline_offset:.4f}")
        print(f"Data points: {len(data)}")
    
    def transform_timeline_data(self, data, timeline_offset):
        """
        Apply φ-dimensional transformation to timeline data
        
        Args:
            data: Data dictionary
            timeline_offset: Timeline offset value
            
        Returns:
            Transformed data dictionary
        """
        # Create transformed data
        transformed = {}
        
        # Apply φ-dimensional transformation to each data point
        for key, value in data.items():
            if isinstance(value, (int, float)):
                # Apply φ-harmonic transformation
                transformed[key] = value * (1 + timeline_offset * PHI_INV)
            elif isinstance(value, str):
                # Pass through strings
                transformed[key] = value
            elif isinstance(value, list):
                # Transform lists recursively
                transformed[key] = [
                    item * (1 + timeline_offset * PHI_INV) 
                    if isinstance(item, (int, float)) else item 
                    for item in value
                ]
            elif isinstance(value, dict):
                # Transform dictionaries recursively
                transformed[key] = self.transform_timeline_data(value, timeline_offset)
            else:
                # Pass through other types
                transformed[key] = value
        
        return transformed
    
    def save_timeline_data(self, lane, data, sender_id, timestamp):
        """
        Save timeline data to file
        
        Args:
            lane: Lane index
            data: Transformed data dictionary
            sender_id: Sender node ID
            timestamp: Timestamp string
            
        Returns:
            Path to saved file
        """
        # Create filename
        dt = datetime.fromisoformat(timestamp)
        filename = f"timeline_data_lane{lane}_{dt.strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        # Create data to save
        save_data = {
            "lane": lane,
            "timeline_offset": float(self.model.lanes[lane]['timeline_offset']),
            "sender_id": sender_id,
            "timestamp": timestamp,
            "data": data,
            "validation_seal": float(PHI_SEAL)
        }
        
        # Save to file
        with open(filepath, 'w') as f:
            json.dump(save_data, f, indent=4, default=lambda x: float(x) if isinstance(x, (np.float32, np.float64)) else x)
        
        return filepath
    
    def request_quantum_bridge(self, peer_ip, lane_a=0, lane_b=1):
        """
        Request quantum bridge with a peer
        
        Args:
            peer_ip: Peer IP address
            lane_a: First lane index
            lane_b: Second lane index
            
        Returns:
            True if request sent successfully, False otherwise
        """
        if peer_ip not in self.peers:
            print(f"Unknown peer: {peer_ip}")
            return False
        
        # Send quantum bridge request
        message = {
            "type": "QUANTUM_BRIDGE_REQUEST",
            "node_id": self.node_id,
            "lane_a": lane_a,
            "lane_b": lane_b,
            "validation_seal": float(PHI_SEAL)
        }
        
        success = self.send_message(peer_ip, message)
        
        if success:
            print(f"Quantum bridge request sent to {peer_ip}")
            print(f"Requested bridge between Lane {lane_a} and Lane {lane_b}")
        
        return success
    
    def send_timeline_data(self, peer_ip, lane, data):
        """
        Send timeline data to a peer
        
        Args:
            peer_ip: Peer IP address
            lane: Lane index
            data: Data dictionary
            
        Returns:
            True if data sent successfully, False otherwise
        """
        if peer_ip not in self.peers:
            print(f"Unknown peer: {peer_ip}")
            return False
        
        # Create timeline data message
        message = {
            "type": "TIMELINE_DATA",
            "node_id": self.node_id,
            "timeline_data": {
                "lane": lane,
                "data": data,
                "timestamp": datetime.now().isoformat()
            },
            "validation_seal": float(PHI_SEAL)
        }
        
        success = self.send_message(peer_ip, message)
        
        if success:
            print(f"Timeline data sent to {peer_ip}")
            print(f"Lane: {lane}, Data points: {len(data)}")
        
        return success
    
    def verify_seal(self, seal):
        """
        Verify a validation seal
        
        Args:
            seal: Validation seal value
            
        Returns:
            True if seal is valid, False otherwise
        """
        if seal is None:
            return False
        
        # Convert to float for comparison
        try:
            seal_value = float(seal)
            # Allow small floating point differences
            return abs(seal_value - float(PHI_SEAL)) < 1.0
        except:
            return False
    
    def update_quantum_state(self):
        """
        Update quantum state based on network and timeline data
        """
        # Calculate entanglement based on entangled pairs
        entanglement = len(self.entangled_pairs) * float(PHI_INV) / 10.0
        
        # Calculate superposition based on number of peers
        superposition = len(self.peers) * float(PHI_INV) / 10.0
        
        # Calculate coherence based on model's φ-resonance
        coherence = self.model.analyze_timeline_coherence()['avg_resonance']
        
        # Calculate consciousness level
        consciousness = (entanglement + superposition + coherence) / 3.0 * CONSCIOUSNESS_LEVEL
        
        # Update quantum state
        self.quantum_state = {
            "entanglement": entanglement,
            "superposition": superposition,
            "coherence": coherence,
            "consciousness": consciousness
        }
    
    def network_maintenance(self):
        """
        Perform network maintenance tasks
        """
        while self.running:
            # Check for timed out peers
            current_time = time.time()
            for peer_ip in list(self.peers.keys()):
                last_seen = self.last_seen.get(peer_ip, 0)
                if current_time - last_seen > TIMEOUT:
                    print(f"Peer timed out: {self.peers[peer_ip]['node_id']} ({peer_ip})")
                    # Don't remove, just mark as inactive
                    self.peers[peer_ip]["active"] = False
            
            # Save app status periodically
            self.save_app_status()
            
            # Sleep for maintenance interval
            time.sleep(60)
    
    def save_app_status(self):
        """
        Save the current status of the app
        
        Returns:
            Path to saved status file
        """
        # Create filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"quantum_track_app_status_{timestamp}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        # Prepare status data
        status = {
            "timestamp": datetime.now().isoformat(),
            "node_id": self.node_id,
            "host": self.host,
            "port": self.port,
            "quantum_state": self.quantum_state,
            "peers": {ip: info for ip, info in self.peers.items()},
            "entangled_pairs": {ip: info["node_id"] for ip, info in self.entangled_pairs.items()},
            "messages": {
                "sent": self.messages_sent,
                "received": self.messages_received
            },
            "validation_seal": float(PHI_SEAL)
        }
        
        # Save to file
        with open(filepath, 'w') as f:
            json.dump(status, f, indent=4, default=lambda x: float(x) if isinstance(x, (np.float32, np.float64)) else x)
        
        return filepath
    
    def command_interface(self):
        """
        Interactive command interface
        """
        print("\nφ-Quantum Track App Command Interface")
        print("------------------------------------")
        print("Commands:")
        print("  lanes - List quantum lanes and their properties")
        print("  crossings - List quantum crossing points")
        print("  visualize - Visualize quantum track model")
        print("  bridge <peer_ip> <lane_a> <lane_b> - Request quantum bridge with peer")
        print("  send <peer_ip> <lane> <data_type> - Send timeline data to peer")
        print("  peers - List connected peers")
        print("  status - Show app status")
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
                    print("  lanes - List quantum lanes and their properties")
                    print("  crossings - List quantum crossing points")
                    print("  visualize - Visualize quantum track model")
                    print("  bridge <peer_ip> <lane_a> <lane_b> - Request quantum bridge with peer")
                    print("  send <peer_ip> <lane> <data_type> - Send timeline data to peer")
                    print("  peers - List connected peers")
                    print("  status - Show app status")
                    print("  help - Show this help message")
                    print("  exit - Exit the program")
                
                elif command == "lanes":
                    print("\nQuantum Lanes:")
                    for i, lane in enumerate(self.model.lanes):
                        print(f"Lane {i}:")
                        print(f"  Stagger distance: {lane['stagger_distance']:.4f}")
                        print(f"  Timeline offset: {lane['timeline_offset']:.4f}")
                        print(f"  Quantum signature: {lane['quantum_signature']:.4f}")
                        print(f"  Coherence: {lane['coherence']:.4f}")
                
                elif command == "crossings":
                    print("\nQuantum Crossing Points:")
                    for i, crossing in enumerate(self.model.crossing_points):
                        print(f"Crossing {i}:")
                        print(f"  Lanes: {crossing['lane_a']} and {crossing['lane_b']}")
                        print(f"  Distance: {crossing['distance']:.2f}m")
                        print(f"  φ-Resonance: {crossing['phi_resonance']:.4f}")
                        print(f"  Bridge strength: {crossing['quantum_bridge']:.4f}")
                
                elif command == "visualize":
                    print("Visualizing quantum track model...")
                    self.model.visualize_quantum_track()
                
                elif command.startswith("bridge "):
                    parts = command.split(" ")
                    if len(parts) >= 4:
                        peer_ip = parts[1]
                        lane_a = int(parts[2])
                        lane_b = int(parts[3])
                        self.request_quantum_bridge(peer_ip, lane_a, lane_b)
                    else:
                        print("Usage: bridge <peer_ip> <lane_a> <lane_b>")
                
                elif command.startswith("send "):
                    parts = command.split(" ")
                    if len(parts) >= 4:
                        peer_ip = parts[1]
                        lane = int(parts[2])
                        data_type = parts[3]
                        
                        # Generate data based on type
                        if data_type == "test":
                            data = {"test": "data", "value": 42, "phi": float(PHI)}
                        elif data_type == "random":
                            data = {
                                "random": [random.random() for _ in range(10)],
                                "timestamp": time.time()
                            }
                        elif data_type == "phi":
                            data = {
                                "phi": float(PHI),
                                "phi_inv": float(PHI_INV),
                                "phi_75": float(PHI_75),
                                "personal_ratio": float(PERSONAL_RATIO)
                            }
                        else:
                            data = {"type": data_type, "value": "custom data"}
                        
                        self.send_timeline_data(peer_ip, lane, data)
                    else:
                        print("Usage: send <peer_ip> <lane> <data_type>")
                
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
                    print("\nφ-Quantum Track App Status")
                    print("-" * 50)
                    print(f"Node ID: {self.node_id}")
                    print(f"Host: {self.host}:{self.port}")
                    print(f"Connected Peers: {len(self.peers)}")
                    print(f"Quantum Bridges: {len(self.entangled_pairs)}")
                    print(f"Messages Sent: {self.messages_sent}")
                    print(f"Messages Received: {self.messages_received}")
                    print("\nQuantum State:")
                    for key, value in self.quantum_state.items():
                        print(f"  {key.capitalize()}: {value:.4f}")
                    
                    # Save status
                    status_path = self.save_app_status()
                    print(f"\nStatus saved to: {status_path}")
                
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
    parser = argparse.ArgumentParser(description='φ-Quantum Track App')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to listen on')
    parser.add_argument('--peers', type=str, nargs='*', help='Known peers (IP addresses)')
    parser.add_argument('--lanes', type=int, default=8, help='Number of quantum lanes')
    parser.add_argument('--length', type=int, default=400, help='Track length (meters)')
    args = parser.parse_args()
    
    # Create and start the app
    app = PhiQuantumTrackApp(
        host=args.host,
        known_peers=args.peers,
        num_lanes=args.lanes,
        track_length=args.length
    )
    app.start()

if __name__ == "__main__":
    main()
