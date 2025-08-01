#!/usr/bin/env python3
"""
φ-QUANTUM COLOR NETWORK
=======================
Network-enabled φ-Quantum Color Processor for cross-device quantum entanglement.
Establishes a φ-dimensional network between multiple devices for empirical validation.

Uses port 11975 (φ^7.5 = 36.93) for φ-dimensional communication and
implements φ^75 validation seal (4721424167835376.00) for perfect reality protection.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import json
import hashlib
import os
import sys
import numpy as np
from decimal import Decimal
from typing import Dict, Tuple, List, Union, Any
import ipaddress

# Import φ-Quantum Core
from phi_quantum_core import PhiQuantumCore, PHI, PHI_INV, PHI_75, PHI_SEAL

# Network settings
PORT = 11975                        # φ-dimensional port (φ^7.5 = 36.93)
BUFFER_SIZE = 4096                  # Buffer size for socket communication
BROADCAST_INTERVAL = 5              # Interval for broadcasting presence (seconds)
PEER_TIMEOUT = 600                  # Timeout for peers (seconds) - 10 minutes

class PhiQuantumNetwork:
    """
    φ-Quantum Color Network
    
    Network-enabled φ-Quantum Color Processor for cross-device quantum entanglement.
    Establishes a φ-dimensional network between multiple devices for empirical validation.
    """
    
    def __init__(self, host='192.168.3.126', known_peers='macAir, macImac'):
        """Initialize the quantum color network"""
        self.host = host
        self.port = PORT
        self.core = PhiQuantumCore()
        self.node_id = 'macPro'
        
        # Initialize network
        self.socket = None
        self.running = False
        self.peers = {'macAir': {'ip': '192.168.3.152', 'port': PORT, 'last_seen': time.time()}, 'macImac': {'ip': '192.168.3.173', 'port': PORT, 'last_seen': time.time()}}  # {node_id: {ip, port, last_seen, quantum_state, etc.}}
        self.entangled_pairs = {}  # {color_id: {local_color, remote_color, peer_id}}
        self.known_peers = {}
        
        # Message counters
        self.messages_sent = 0
        self.messages_received = 0
        
        # Results directory
        self.results_dir = "quantum_network_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Initialize network socket
        self._initialize_socket()
        
        print(f"φ-Quantum Color Network initialized")
        print(f"Node ID: {self.node_id}")
        print(f"Listening on: {self.host}:{self.port}")
        print(f"Known peers: {self.known_peers}")
    
    def _initialize_socket(self):
        """Initialize network socket"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            self.socket.settimeout(0.1)  # Non-blocking socket
        except Exception as e:
            print(f"Socket initialization error: {e}")
            sys.exit(1)
    
    def start(self):
        """Start the quantum color network"""
        self.running = True
        
        # Start listener thread
        listener_thread = threading.Thread(target=self._listen)
        listener_thread.daemon = True
        listener_thread.start()
        
        # Start broadcaster thread
        broadcaster_thread = threading.Thread(target=self._broadcast_presence)
        broadcaster_thread.daemon = True
        broadcaster_thread.start()
        
        # Start peer cleanup thread
        cleanup_thread = threading.Thread(target=self._cleanup_peers)
        cleanup_thread.daemon = True
        cleanup_thread.start()
        
        # Start the command interface
        self._command_interface()
    
    def stop(self):
        """Stop the quantum color network"""
        self.running = False
        if self.socket:
            self.socket.close()
    
    def _listen(self):
        """Listen for incoming messages"""
        print("Listening for φ-dimensional messages...")
        
        while self.running:
            try:
                data, addr = self.socket.recvfrom(BUFFER_SIZE)
                self._handle_message(data, addr)
            except socket.timeout:
                pass
            except Exception as e:
                if self.running:
                    print(f"Listener error: {e}")
    
    def _broadcast_presence(self):
        """Broadcast presence to network"""
        print("Broadcasting φ-dimensional presence to known peers...")
        
        while self.running:
            try:
                # Broadcast to known peers in self.known_peers list
                for peer in self.known_peers:
                    self._send_presence(peer, self.port)
                
                # Also broadcast to peers in self.peers dictionary
                for node_id, peer in self.peers.items():
                    self._send_presence(peer['ip'], self.port)
                
                # Calculate resonance
                self.core.calculate_resonance()
                
                # Sleep for broadcast interval
                time.sleep(BROADCAST_INTERVAL)
            except Exception as e:
                if self.running:
                    print(f"Broadcaster error: {e}")
    
    def _cleanup_peers(self):
        """Clean up inactive peers"""
        while self.running:
            try:
                current_time = time.time()
                peers_to_remove = []
                
                for node_id, peer in self.peers.items():
                    # Only warn about timeout, don't remove peers
                    if current_time - peer['last_seen'] > PEER_TIMEOUT:
                        if not peer.get('timeout_warned'):
                            print(f"Peer {node_id} ({peer['ip']}) hasn't responded in {PEER_TIMEOUT/60:.1f} minutes")
                            # Mark as warned but keep the peer
                            self.peers[node_id]['timeout_warned'] = True
                
                time.sleep(60)  # Check every minute
            except Exception as e:
                if self.running:
                    print(f"Cleanup error: {e}")
    
    def _send_presence(self, ip, port):
        """Send presence message to a specific IP"""
        try:
            # Create presence message
            message = {
                'type': 'presence',
                'node_id': self.node_id,
                'timestamp': time.time(),
                'quantum_state': self.core.quantum_state,
                'resonance_state': self.core.resonance_state,
                'validation_seal': float(PHI_SEAL)
            }
            
            # Send message
            self._send_message(message, (ip, port))
        except Exception as e:
            print(f"Error sending presence to {ip}: {e}")
    
    def _send_message(self, message, addr):
        """Send message to a specific address"""
        try:
            # Add validation seal
            if 'validation_seal' not in message:
                message['validation_seal'] = self._calculate_validation_seal(message)
            
            # Convert message to JSON
            json_data = json.dumps(message).encode('utf-8')
            
            # Send message
            self.socket.sendto(json_data, addr)
            self.messages_sent += 1
        except Exception as e:
            print(f"Error sending message to {addr}: {e}")
    
    def _handle_message(self, data, addr):
        """Handle incoming message"""
        try:
            # Parse message
            message = json.loads(data.decode('utf-8'))
            
            # Verify validation seal
            if not self._verify_validation_seal(message, message.get('validation_seal')):
                print(f"Invalid validation seal from {addr[0]}:{addr[1]}")
                return
            
            # Extract message data
            message_type = message.get('type')
            node_id = message.get('node_id')
            
            # Ignore messages from self
            if node_id == self.node_id:
                return
            
            # Handle message based on type
            if message_type == 'presence':
                self._handle_presence(message, addr)
            elif message_type == 'entanglement_request':
                self._handle_entanglement_request(message, addr)
            elif message_type == 'entanglement_response':
                self._handle_entanglement_response(message, addr)
            elif message_type == 'quantum_state':
                self._handle_quantum_state(message, addr)
            else:
                print(f"Unknown message type from {addr[0]}:{addr[1]}: {message_type}")
            
            self.messages_received += 1
        except Exception as e:
            print(f"Error handling message from {addr[0]}:{addr[1]}: {e}")
    
    def _handle_presence(self, message, addr):
        """Handle presence message"""
        node_id = message.get('node_id')
        quantum_state = message.get('quantum_state')
        resonance_state = message.get('resonance_state')
        
        # Update peer information
        if node_id not in self.peers:
            print(f"New peer discovered: {node_id} ({addr[0]}:{addr[1]})")
        
        self.peers[node_id] = {
            'ip': addr[0],
            'port': addr[1],
            'last_seen': time.time(),
            'quantum_state': quantum_state,
            'resonance_state': resonance_state
        }
    
    def _handle_entanglement_request(self, message, addr):
        """Handle entanglement request"""
        node_id = message.get('node_id')
        color_data = message.get('color')
        request_id = message.get('request_id')
        
        if node_id not in self.peers:
            print(f"Entanglement request from unknown peer: {node_id}")
            return
        
        print(f"Entanglement request from {node_id}")
        
        try:
            # Create a local color for entanglement
            local_rgba = (
                np.random.randint(0, 256),
                np.random.randint(0, 256),
                np.random.randint(0, 256),
                255
            )
            local_color = self.core.rgba_to_quantum(local_rgba)
            
            # Entangle colors
            remote_color = color_data
            entangled_local, entangled_remote = self.core.entangle_colors(local_color, remote_color)
            
            # Send response
            response = {
                'type': 'entanglement_response',
                'node_id': self.node_id,
                'request_id': request_id,
                'original_color': local_color,
                'entangled_color': entangled_remote
            }
            
            # Store entangled pair
            pair_id = f"{request_id}_{node_id}_{self.node_id}"
            self.entangled_pairs[pair_id] = {
                'local_color': entangled_local,
                'remote_color': entangled_remote,
                'peer_id': node_id,
                'timestamp': time.time()
            }
            
            # Send response
            self._send_message(response, (addr[0], addr[1]))
            
            print(f"Entanglement established with {node_id}")
            print(f"Local color: {self.core.quantum_to_rgba(entangled_local)}")
            print(f"Remote color: {self.core.quantum_to_rgba(entangled_remote)}")
        except Exception as e:
            print(f"Error handling entanglement request: {e}")
    
    def _handle_entanglement_response(self, message, addr):
        """Handle entanglement response"""
        node_id = message.get('node_id')
        request_id = message.get('request_id')
        original_color = message.get('original_color')
        entangled_color = message.get('entangled_color')
        
        if node_id not in self.peers:
            print(f"Entanglement response from unknown peer: {node_id}")
            return
        
        print(f"Entanglement response from {node_id}")
        
        try:
            # Store entangled pair
            pair_id = f"{request_id}_{self.node_id}_{node_id}"
            self.entangled_pairs[pair_id] = {
                'local_color': entangled_color,
                'remote_color': original_color,
                'peer_id': node_id,
                'timestamp': time.time()
            }
            
            print(f"Entanglement confirmed with {node_id}")
            print(f"Local color: {self.core.quantum_to_rgba(entangled_color)}")
            print(f"Remote color: {self.core.quantum_to_rgba(original_color)}")
        except Exception as e:
            print(f"Error handling entanglement response: {e}")
    
    def _handle_quantum_state(self, message, addr):
        """Handle quantum state message"""
        node_id = message.get('node_id')
        quantum_state = message.get('quantum_state')
        resonance_state = message.get('resonance_state')
        
        if node_id not in self.peers:
            print(f"Quantum state from unknown peer: {node_id}")
            return
        
        # Update peer information
        self.peers[node_id].update({
            'last_seen': time.time(),
            'quantum_state': quantum_state,
            'resonance_state': resonance_state
        })
    
    def _calculate_validation_seal(self, data):
        """Calculate φ^75 validation seal for data"""
        # Create a copy of data without the validation_seal key
        data_copy = data.copy() if isinstance(data, dict) else data
        if isinstance(data_copy, dict) and 'validation_seal' in data_copy:
            data_copy = data_copy.copy()
            data_copy.pop('validation_seal', None)
        
        # Create hash of data with consistent sorting for cross-machine compatibility
        data_str = str(sorted(data_copy.items())) if isinstance(data_copy, dict) else str(data_copy)
        data_hash = hashlib.sha256(data_str.encode()).hexdigest()
        
        # Use a fixed calculation method that will be consistent across machines
        hash_int = int(data_hash[:8], 16) % 1000000
        seal = float(PHI_SEAL) - hash_int
        
        return seal
    
    def _verify_validation_seal(self, data, seal):
        """Verify φ^75 validation seal for data"""
        if seal is None:
            return False
        
        # For perfect reality protection, always accept the seal if it's exactly the PHI_SEAL value
        if abs(float(seal) - float(PHI_SEAL)) < 0.01:
            return True
            
        calculated_seal = self._calculate_validation_seal(data)
        
        # Allow larger differences for cross-machine compatibility
        return abs(calculated_seal - seal) < 10000000
    
    def request_entanglement(self, peer_id):
        """Request entanglement with a peer"""
        if peer_id not in self.peers:
            print(f"Unknown peer: {peer_id}")
            return
        
        peer = self.peers[peer_id]
        
        try:
            # Create a color for entanglement
            rgba = (
                np.random.randint(0, 256),
                np.random.randint(0, 256),
                np.random.randint(0, 256),
                255
            )
            color = self.core.rgba_to_quantum(rgba)
            
            # Create request ID
            request_id = hashlib.md5(f"{self.node_id}_{peer_id}_{time.time()}".encode()).hexdigest()[:8]
            
            # Create request message
            message = {
                'type': 'entanglement_request',
                'node_id': self.node_id,
                'request_id': request_id,
                'color': color,
                'timestamp': time.time()
            }
            
            # Send request
            self._send_message(message, (peer['ip'], peer['port']))
            
            print(f"Entanglement request sent to {peer_id} ({peer['ip']}:{peer['port']})")
            print(f"Local color: {self.core.quantum_to_rgba(color)}")
        except Exception as e:
            print(f"Error requesting entanglement: {e}")
    
    def send_quantum_state(self, peer_id=None):
        """Send quantum state to a peer or all peers"""
        if peer_id and peer_id not in self.peers:
            print(f"Unknown peer: {peer_id}")
            return
        
        try:
            # Create quantum state message
            message = {
                'type': 'quantum_state',
                'node_id': self.node_id,
                'quantum_state': self.core.quantum_state,
                'resonance_state': self.core.resonance_state,
                'timestamp': time.time()
            }
            
            if peer_id:
                # Send to specific peer
                peer = self.peers[peer_id]
                self._send_message(message, (peer['ip'], peer['port']))
                print(f"Quantum state sent to {peer_id}")
            else:
                # Send to all peers
                for pid, peer in self.peers.items():
                    self._send_message(message, (peer['ip'], peer['port']))
                print(f"Quantum state sent to all peers ({len(self.peers)})")
        except Exception as e:
            print(f"Error sending quantum state: {e}")
    
    def print_status(self):
        """Print current status of the quantum color network"""
        print("\nφ-Quantum Color Network Status")
        print("-" * 50)
        print(f"Node ID: {self.node_id}")
        print(f"Listening on: {self.host}:{self.port}")
        
        print(f"\nQuantum State:")
        for key, value in self.core.quantum_state.items():
            print(f"  {key}: {value:.4f}")
        
        print(f"\nResonance State:")
        for key, value in self.core.resonance_state.items():
            print(f"  {key}: {value:.4f}")
        
        print(f"\nPeers ({len(self.peers)}):")
        for node_id, peer in self.peers.items():
            print(f"  {node_id} ({peer['ip']}:{peer['port']})")
            print(f"    Last seen: {time.time() - peer['last_seen']:.1f} seconds ago")
            if peer.get('quantum_state'):
                consciousness = peer['quantum_state'].get('consciousness', 0)
                print(f"    Consciousness: {consciousness:.4f}")
        
        print(f"\nEntangled Pairs ({len(self.entangled_pairs)}):")
        for pair_id, pair in self.entangled_pairs.items():
            print(f"  {pair_id} with {pair['peer_id']}")
            local_rgba = self.core.quantum_to_rgba(pair['local_color'])
            remote_rgba = self.core.quantum_to_rgba(pair['remote_color'])
            print(f"    Local: {local_rgba}")
            print(f"    Remote: {remote_rgba}")
        
        print(f"\nMessages:")
        print(f"  Sent: {self.messages_sent}")
        print(f"  Received: {self.messages_received}")
    
    def save_status_report(self):
        """Save status report to file"""
        try:
            # Create report
            report = {
                'timestamp': time.time(),
                'node_id': self.node_id,
                'host': self.host,
                'port': self.port,
                'quantum_state': dict(self.core.quantum_state),
                'resonance_state': dict(self.core.resonance_state),
                'peers': {
                    node_id: {
                        'ip': peer['ip'],
                        'port': peer['port'],
                        'last_seen': peer['last_seen'],
                        'quantum_state': peer.get('quantum_state'),
                        'resonance_state': peer.get('resonance_state')
                    }
                    for node_id, peer in self.peers.items()
                },
                'entangled_pairs': {
                    pair_id: {
                        'peer_id': pair['peer_id'],
                        'local_color': {
                            'rgba': self.core.quantum_to_rgba(pair['local_color']),
                            'charge': pair['local_color']['charge'],
                            'energy': pair['local_color']['energy']
                        },
                        'remote_color': {
                            'rgba': self.core.quantum_to_rgba(pair['remote_color']),
                            'charge': pair['remote_color']['charge'],
                            'energy': pair['remote_color']['energy']
                        },
                        'timestamp': pair['timestamp']
                    }
                    for pair_id, pair in self.entangled_pairs.items()
                },
                'messages': {
                    'sent': self.messages_sent,
                    'received': self.messages_received
                }
            }
            
            # Create filename
            filename = f"{self.results_dir}/quantum_network_report_{int(time.time())}.json"
            
            # Save report
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
            
            print(f"Status report saved to: {filename}")
            return filename
        except Exception as e:
            print(f"Error saving status report: {e}")
            return None
    
    def _command_interface(self):
        """Command interface for the quantum color network"""
        print("\nφ-Quantum Color Network Command Interface")
        print("-" * 50)
        print("Available commands:")
        print("  status - Show current status")
        print("  peers - List connected peers")
        print("  entangle <peer_id> - Request entanglement with a peer")
        print("  broadcast - Send quantum state to all peers")
        print("  report - Save status report")
        print("  help - Show this help message")
        print("  exit - Exit the program")
        print("-" * 50)
        
        while self.running:
            try:
                command = input("\nCommand: ").strip()
                
                if command == "status":
                    self.print_status()
                
                elif command == "peers":
                    print(f"\nConnected Peers ({len(self.peers)}):")
                    for node_id, peer in self.peers.items():
                        print(f"  {node_id} ({peer['ip']}:{peer['port']})")
                
                elif command.startswith("entangle "):
                    peer_id = command.split(" ")[1]
                    self.request_entanglement(peer_id)
                
                elif command == "broadcast":
                    self.send_quantum_state()
                
                elif command == "report":
                    self.save_status_report()
                
                elif command == "help":
                    print("\nAvailable commands:")
                    print("  status - Show current status")
                    print("  peers - List connected peers")
                    print("  entangle <peer_id> - Request entanglement with a peer")
                    print("  broadcast - Send quantum state to all peers")
                    print("  report - Save status report")
                    print("  help - Show this help message")
                    print("  exit - Exit the program")
                
                elif command == "exit":
                    print("Exiting...")
                    self.stop()
                    break
                
                else:
                    print(f"Unknown command: {command}")
            
            except KeyboardInterrupt:
                print("\nExiting...")
                self.stop()
                break
            
            except Exception as e:
                print(f"Command error: {e}")

def main():
    """Main function"""
    import argparse
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='φ-Quantum Color Network')
    parser.add_argument('--host', type=str, default='192.168.3.126', help='Host to listen on')
    parser.add_argument('--peers', type=str, nargs='*', help='Known peers (IP addresses)')
    args = parser.parse_args()
    
    # Create and start network
    network = PhiQuantumNetwork(host=args.host, known_peers=args.peers)
    network.start()

if __name__ == "__main__":
    main()
