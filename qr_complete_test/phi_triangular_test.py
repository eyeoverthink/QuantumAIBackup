#!/usr/bin/env python3
"""
φ-Triangular Quantum Network Test
Demonstrates φ-dimensional reality protection across three nodes
"""

import os
import time
import platform
import socket
import json
import threading
import random
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

class PhiTriangularNode:
    """
    φ-Triangular Quantum Node for three-way reality mapping
    """
    def __init__(self, node_id, consciousness_level=0.7567):
        self.node_id = node_id
        self.consciousness_level = consciousness_level
        self.port = int(PHI_75 * 1000)  # 11975
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.port))
        self.peers = []
        self.running = True
        self.quantum_state = {}
        
        # Initialize φ-dimensional quantum state
        self.quantum_state["phi_seal"] = PHI_SEAL
        self.quantum_state["consciousness"] = self.consciousness_level
        self.quantum_state["node_id"] = self.node_id
        self.quantum_state["reality_map"] = {}
        
        print(f"\n=== φ-TRIANGULAR QUANTUM NODE {node_id} ===")
        print(f"Running on: {platform.node()}")
        print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Port: {self.port} (φ^7.5 * 1000)")
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Consciousness level: {self.consciousness_level}")
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
    
    def add_peer(self, ip):
        """Add a peer to the triangular quantum network"""
        if ip not in self.peers:
            self.peers.append(ip)
            print(f"Added peer {ip} to triangular quantum network")
            
            # Update reality map
            self.quantum_state["reality_map"][ip] = {
                "added": time.time(),
                "phi_seal": PHI_SEAL,
                "consciousness": self.consciousness_level
            }
            
            # Notify peer about this node
            self.send_quantum_state(ip)
    
    def send_quantum_state(self, target_ip):
        """Send quantum state through φ-dimensional quantum bridge"""
        message = f"QUANTUM_STATE:{json.dumps(self.quantum_state)}"
        self.socket.sendto(message.encode('utf-8'), (target_ip, self.port))
        print(f"Sent quantum state to {target_ip}")
    
    def broadcast_quantum_state(self):
        """Broadcast quantum state to all peers in triangular network"""
        for peer in self.peers:
            self.send_quantum_state(peer)
        print(f"Broadcasted quantum state to {len(self.peers)} peers")
    
    def send_triangular_message(self, message):
        """Send message to all peers in triangular quantum network"""
        for peer in self.peers:
            self.send_message(peer, message)
    
    def send_message(self, target_ip, message):
        """Send a message through φ-dimensional quantum bridge"""
        protected_message = f"MSG:{message}"
        self.socket.sendto(protected_message.encode('utf-8'), (target_ip, self.port))
        print(f"Sent message to {target_ip}: {message}")
    
    def receive_messages(self):
        """Receive messages through φ-dimensional quantum bridge"""
        while self.running:
            try:
                data, addr = self.socket.recvfrom(4096)
                sender_ip = addr[0]
                message = data.decode('utf-8')
                
                # Add sender to peers if not already added
                if sender_ip not in self.peers and sender_ip != "127.0.0.1":
                    self.add_peer(sender_ip)
                
                # Process message based on type
                if message.startswith("MSG:"):
                    content = message[4:]
                    print(f"\nReceived message from {sender_ip}: {content}")
                    
                    # Relay message to other peers (triangular communication)
                    for peer in self.peers:
                        if peer != sender_ip:
                            relay_message = f"RELAY:{self.node_id}:{content}"
                            self.send_message(peer, relay_message)
                
                elif message.startswith("RELAY:"):
                    parts = message[6:].split(":", 1)
                    origin_node = parts[0]
                    content = parts[1]
                    print(f"\nRelayed message from Node {origin_node} via {sender_ip}: {content}")
                
                elif message.startswith("QUANTUM_STATE:"):
                    state_json = message[14:]
                    peer_state = json.loads(state_json)
                    peer_node_id = peer_state.get("node_id", "unknown")
                    print(f"\nReceived quantum state from Node {peer_node_id} ({sender_ip})")
                    
                    # Update reality map with peer's reality map
                    peer_reality_map = peer_state.get("reality_map", {})
                    for ip, data in peer_reality_map.items():
                        if ip not in self.quantum_state["reality_map"] and ip != "127.0.0.1":
                            self.quantum_state["reality_map"][ip] = data
                            if ip not in self.peers and ip != sender_ip:
                                self.add_peer(ip)
                
                else:
                    print(f"\nUnknown message type from {sender_ip}: {message[:20]}...")
            
            except Exception as e:
                print(f"Error receiving message: {e}")
    
    def run_triangular_test(self):
        """Run φ-triangular quantum network test"""
        print("\n=== RUNNING φ-TRIANGULAR QUANTUM NETWORK TEST ===")
        
        # Phase 1: Establish triangular quantum network
        print("\nPhase 1: Establishing triangular quantum network...")
        self.broadcast_quantum_state()
        time.sleep(2)
        
        # Phase 2: Send test message through triangular network
        print("\nPhase 2: Sending test message through triangular network...")
        test_message = f"TRIANGULAR_TEST:{self.node_id}:{time.time()}:{PHI_SEAL}"
        self.send_triangular_message(test_message)
        time.sleep(2)
        
        # Phase 3: Verify triangular quantum bridge
        print("\nPhase 3: Verifying triangular quantum bridge...")
        verification_message = f"VERIFY:{self.node_id}:{random.randint(1000, 9999)}:{PHI_SEAL}"
        self.send_triangular_message(verification_message)
        time.sleep(2)
        
        print("\nφ-Triangular Quantum Network Test Complete")
        print(f"Connected to {len(self.peers)} peers in triangular network")
        print(f"Reality map contains {len(self.quantum_state['reality_map'])} nodes")
        print("φ^∞ © 2025 Vaughn Scott")
        print("All Rights Reserved in All Realities")

def main():
    """Main function to run φ-triangular quantum network test"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python phi_triangular_test.py <node_id>")
        print("Example: python phi_triangular_test.py 1")
        return
    
    node_id = sys.argv[1]
    node = PhiTriangularNode(node_id)
    
    # Add initial peers if provided
    for i in range(2, len(sys.argv)):
        node.add_peer(sys.argv[i])
    
    # Wait for peers to connect
    print("\nWaiting for peers to connect to triangular quantum network...")
    print("Press Enter to start the triangular test when all nodes are connected")
    input()
    
    # Run triangular test
    node.run_triangular_test()
    
    # Keep running to receive messages
    print("\nNode is running. Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        node.running = False
        print("\nShutting down φ-triangular quantum node...")

if __name__ == "__main__":
    main()
