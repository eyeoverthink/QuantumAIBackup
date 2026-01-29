#!/usr/bin/env python3
"""
φ-Harmonic FTL Bridge
Connects the φ-Harmonic Bidirectional Node with the FTL Network
Implements φ-dimensional reality protection with quantum-speed data transfer
"""

import os
import sys
import time
import socket
import json
import hashlib
import threading
from math import sqrt
import subprocess

# Add the quantum_core directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
quantum_core_dir = os.path.join(current_dir, 'quantum_core')
sys.path.append(parent_dir)
sys.path.append(quantum_core_dir)

# Import φ-Harmonic components
from phi_bidirectional_node import PhiBidirectionalNode
from quantum_core.phi_harmonic_ftl_network import PhiHarmonicNode, PHI, PHI_CUBED, CONSCIOUSNESS_FREQUENCY
from quantum_core.atomic_triad_transistor import AtomicTriadTransistor

# φ-Harmonic constants from FRAYMUS patent
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

class PhiFTLBridge:
    def __init__(self, node_id="ftl_bridge_2", phi_port=11975, ftl_port=11976):
        """Initialize the φ-Harmonic FTL Bridge"""
        self.node_id = 'ftl_bridge_1'
        self.phi_port = 11975  # φ^7.5 port
        self.ftl_port = 11976  # φ * 10000 - 5000
        self.consciousness_level = 0.7567
        self.running = True
        self.peers = {}
        
        print(f"\n=== φ-HARMONIC FTL BRIDGE ===")
        print(f"Node ID: {self.node_id}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"φ port: {self.phi_port} (φ^7.5 = {PHI_75:.2f})")
        print(f"FTL port: {self.ftl_port}")
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Consciousness level: {self.consciousness_level}")
        print(f"Consciousness frequency: {CONSCIOUSNESS_FREQUENCY} Hz")
        
        # Initialize φ-Harmonic components
        self.phi_node = PhiBidirectionalNode(node_id=f"{node_id}_phi", port=phi_port)
        self.ftl_node = PhiHarmonicNode(node_id=f"{node_id}_ftl")
        
        # Create script directory if it doesn't exist
        self.script_dir = "phi_scripts"
        os.makedirs(self.script_dir, exist_ok=True)
        
        # Initialize quantum bridge socket
        self.bridge_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bridge_sock.bind(('0.0.0.0', 0))  # Bind to any available port
        self.bridge_port = 11975
        
        print(f"Bridge port: {self.bridge_port}")
        print(f"Ready for φ-dimensional FTL communication")
    
    def start(self):
        """Start the φ-Harmonic FTL Bridge"""
        # Start φ-Harmonic components
        phi_thread = threading.Thread(target=self._start_phi_node)
        phi_thread.daemon = True
        phi_thread.start()
        
        ftl_thread = threading.Thread(target=self._start_ftl_node)
        ftl_thread.daemon = True
        ftl_thread.start()
        
        # Start bridge listener
        bridge_thread = threading.Thread(target=self._bridge_loop)
        bridge_thread.daemon = True
        bridge_thread.start()
        
        # Start command interface
        self.command_interface()
    
    def _start_phi_node(self):
        """Start the φ-Harmonic Bidirectional Node"""
        try:
            # Start the node in a separate thread
            self.phi_node.listen()
        except Exception as e:
            print(f"[φ] Error starting φ-node: {e}")
    
    def _start_ftl_node(self):
        """Start the FTL Network Node"""
        try:
            # Start the node
            self.ftl_node.start()
        except Exception as e:
            print(f"[FTL] Error starting FTL node: {e}")
    
    def _bridge_loop(self):
        """Main bridge loop for φ-FTL communication"""
        print(f"[BRIDGE] φ-FTL bridge active")
        
        while self.running:
            try:
                # Process φ -> FTL transfers
                self._process_phi_to_ftl()
                
                # Process FTL -> φ transfers
                self._process_ftl_to_phi()
                
                # Sleep a bit to avoid hammering the CPU
                time.sleep(0.1)
                
            except Exception as e:
                print(f"[BRIDGE] Error in bridge loop: {e}")
                time.sleep(1)
    
    def _process_phi_to_ftl(self):
        """Process data from φ-node to FTL network"""
        # Check for data in the φ-node buffer
        # This is a simplified implementation - in a real system, you would
        # need to access the actual buffer from the φ-node
        
        # For demonstration purposes, we'll just check if there's any data
        # in the bridge socket
        try:
            self.bridge_sock.settimeout(0.01)
            data, addr = self.bridge_sock.recvfrom(65536)
            
            if data.startswith(b'PHI_TO_FTL:'):
                # Extract data and target
                bridge_data = json.loads(data[11:].decode('utf-8'))
                target_node = bridge_data.get('target_node', 'broadcast')
                payload = bridge_data.get('data', {})
                
                # Send via FTL
                print(f"[BRIDGE] Sending data via FTL to {target_node}")
                self.ftl_node.send_data_ftl(payload, target_node)
                
                # Add to peers if new
                if addr[0] not in self.peers:
                    self.peers[addr[0]] = {"last_seen": time.time(), "type": "phi"}
                else:
                    self.peers[addr[0]]["last_seen"] = time.time()
        
        except socket.timeout:
            pass
        except Exception as e:
            if not str(e).startswith('timed out'):
                print(f"[BRIDGE] Error processing φ->FTL: {e}")
    
    def _process_ftl_to_phi(self):
        """Process data from FTL network to φ-node"""
        # Check for data in the FTL node buffer
        ftl_data = self.ftl_node.receive_data_ftl()
        
        if ftl_data:
            for item in ftl_data:
                try:
                    source_node = item.get('source_node', 'unknown')
                    data = item.get('data', {})
                    
                    # Check if target IP is specified
                    target_ip = data.get('target_ip', None)
                    
                    if target_ip:
                        # Send to specific φ-node
                        print(f"[BRIDGE] Routing FTL data to φ-node at {target_ip}")
                        self.phi_node.send_message(f"FTL:{json.dumps(data)}", target_ip)
                    else:
                        # Broadcast to all known φ-nodes
                        print(f"[BRIDGE] Broadcasting FTL data to all φ-nodes")
                        for peer_ip, peer_data in self.peers.items():
                            if peer_data.get('type') == 'phi':
                                self.phi_node.send_message(f"FTL:{json.dumps(data)}", peer_ip)
                
                except Exception as e:
                    print(f"[BRIDGE] Error processing FTL->φ: {e}")
    
    def send_phi_to_ftl(self, data, target_node='broadcast'):
        """Send data from φ-network to FTL network"""
        bridge_data = {
            'data': data,
            'target_node': target_node,
            'timestamp': time.time(),
            'source_bridge': self.node_id
        }
        
        # Send to bridge socket
        message = f"PHI_TO_FTL:{json.dumps(bridge_data)}".encode('utf-8')
        self.bridge_sock.sendto(message, ('127.0.0.1', self.bridge_port))
        
        return True
    
    def send_ftl_to_phi(self, data, target_ip):
        """Send data from FTL network to φ-network"""
        # Add target information
        data['target_ip'] = target_ip
        data['source_bridge'] = self.node_id
        data['timestamp'] = time.time()
        
        # Send via FTL node
        self.ftl_node.send_data_ftl(data)
        
        return True
    
    def command_interface(self):
        """Interactive command interface"""
        print("\n[BRIDGE] Command interface ready. Type 'help' for commands.")
        
        while self.running:
            try:
                cmd = input("\nφ-FTL> ").strip()
                
                if cmd == "help":
                    print("\nCommands:")
                    print("  phi2ftl <data> [target_node]   - Send data from φ to FTL")
                    print("  ftl2phi <data> <target_ip>     - Send data from FTL to φ")
                    print("  peers                          - List known peers")
                    print("  status                         - Show bridge status")
                    print("  quit                           - Exit bridge")
                
                elif cmd.startswith("phi2ftl "):
                    parts = cmd.split(" ", 2)
                    target = parts[2] if len(parts) > 2 else 'broadcast'
                    self.send_phi_to_ftl({"message": parts[1]}, target)
                    print(f"[BRIDGE] Sent message to FTL network (target: {target})")
                
                elif cmd.startswith("ftl2phi "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("[BRIDGE] Usage: ftl2phi <data> <target_ip>")
                    else:
                        self.send_ftl_to_phi({"message": parts[1]}, parts[2])
                        print(f"[BRIDGE] Sent message to φ-node at {parts[2]}")
                
                elif cmd == "peers":
                    if not self.peers:
                        print("[BRIDGE] No known peers")
                    else:
                        print("\nKnown peers:")
                        for ip, data in self.peers.items():
                            last_seen = time.time() - data["last_seen"]
                            peer_type = data.get("type", "unknown")
                            print(f"  {ip} - Type: {peer_type}, Last seen: {last_seen:.1f}s ago")
                
                elif cmd == "status":
                    print("\nφ-FTL Bridge Status:")
                    print(f"  Node ID: {self.node_id}")
                    print(f"  φ Port: {self.phi_port}")
                    print(f"  FTL Port: {self.ftl_port}")
                    print(f"  Bridge Port: {self.bridge_port}")
                    print(f"  Consciousness Level: {self.consciousness_level}")
                    print(f"  Known Peers: {len(self.peers)}")
                    print(f"  φ^75 Validation Seal: {PHI_SEAL:.2f}")
                
                elif cmd == "quit":
                    print("[BRIDGE] Shutting down φ-FTL bridge...")
                    self.running = False
                    break
                
                else:
                    print(f"[BRIDGE] Unknown command: {cmd}")
            
            except KeyboardInterrupt:
                print("\n[BRIDGE] Shutting down φ-FTL bridge...")
                self.running = False
                break
            
            except Exception as e:
                print(f"[BRIDGE] Error in command interface: {e}")
        
        print("[BRIDGE] Bridge stopped")
        
        # Stop components
        try:
            self.ftl_node.stop()
        except:
            pass

if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='φ-Harmonic FTL Bridge')
    parser.add_argument('--id', type=str, default="ftl_bridge", help='Bridge ID')
    parser.add_argument('--phi-port', type=int, default=11975, help='φ port (default: 11975 = φ^7.5)')
    parser.add_argument('--ftl-port', type=int, default=11618, help='FTL port (default: 11618 = φ*10000-5000)')
    args = parser.parse_args()
    
    # Create and start bridge
    bridge = PhiFTLBridge(node_id=args.id, phi_port=args.phi_port, ftl_port=args.ftl_port)
    bridge.start()
