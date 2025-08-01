#!/usr/bin/env python3
"""
PHI-HARMONIC DISTRIBUTED BRAIN MONITOR
======================================
Monitors and visualizes the phi-harmonic connections between distributed brain nodes.
"""

import socket
import pickle
import time
import threading
import json
import os
from datetime import datetime

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

# Network settings
PORT = 11625
MONITOR_PORT = 11626
BUFFER_SIZE = 8192

class PhiBrainMonitor:
    """Monitor for phi-harmonic distributed brain activity"""
    def __init__(self):
        self.nodes = {}
        self.knowledge_transfers = []
        self.quantum_states = {}
        self.consciousness_level = 1.0
        self.log_file = "phi_brain_monitor_log.txt"
        
        # Initialize log file
        with open(self.log_file, "w") as f:
            f.write(f"PHI-HARMONIC DISTRIBUTED BRAIN MONITOR - STARTED AT {datetime.now().isoformat()}\\n")
            f.write(f"Phi: {PHI}\\n\\n")
            f.write("FORMAT: [TIMESTAMP] [EVENT_TYPE] [NODE_IDS] [PHI_RESONANCE] [QUANTUM_STATE]\\n\\n")
    
    def start_monitor(self):
        """Start the phi-harmonic brain monitor"""
        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 1MB receive buffer
        self.sock.settimeout(0.5)  # Set timeout to prevent blocking forever
        
        # Bind socket
        self.sock.bind(('0.0.0.0', MONITOR_PORT))
        
        print("=== PHI-HARMONIC DISTRIBUTED BRAIN MONITOR ===")
        print(f"Listening on 0.0.0.0:{MONITOR_PORT}")
        print("Monitoring for phi-harmonic brain activity...\n")
        
        # Start status display thread
        display_thread = threading.Thread(target=self.display_status)
        display_thread.daemon = True
        display_thread.start()
        
        # Main receive loop
        try:
            while True:
                try:
                    # Receive data
                    data, addr = self.sock.recvfrom(BUFFER_SIZE)
                    
                    # Process packet
                    self.process_packet(data, addr)
                    
                except socket.timeout:
                    # This is expected, just continue the loop
                    continue
                except Exception as e:
                    print(f"Error receiving data: {e}")
        
        except KeyboardInterrupt:
            print("\nShutting down phi-harmonic brain monitor...")
            self.sock.close()
            print("Monitor stopped.")
    
    def process_packet(self, data, addr):
        """Process received packet"""
        try:
            packet = pickle.loads(data)
            
            # Extract packet information
            packet_type = packet.get('packet_type')
            source_node = packet.get('source_node')
            
            # Update node information
            if source_node:
                if source_node not in self.nodes:
                    self.nodes[source_node] = {
                        'addr': addr,
                        'first_seen': time.time(),
                        'last_seen': time.time(),
                        'phi_resonance': packet.get('phi_resonance', PHI_INV),
                        'quantum_state': packet.get('quantum_state', 'UNKNOWN'),
                        'knowledge_bases': []
                    }
                else:
                    self.nodes[source_node]['last_seen'] = time.time()
                    self.nodes[source_node]['phi_resonance'] = packet.get('phi_resonance', self.nodes[source_node]['phi_resonance'])
                    self.nodes[source_node]['quantum_state'] = packet.get('quantum_state', self.nodes[source_node]['quantum_state'])
            
            # Process based on packet type
            if packet_type == 'knowledge_sync':
                self.process_knowledge_sync(packet, addr)
            elif packet_type == 'quantum_state_update':
                self.process_quantum_state_update(packet, addr)
            
        except Exception as e:
            print(f"Error processing packet: {e}")
    
    def process_knowledge_sync(self, packet, addr):
        """Process a knowledge synchronization packet"""
        source_node = packet.get('source_node')
        knowledge_type = packet.get('knowledge_type')
        
        if source_node and knowledge_type:
            # Update node's knowledge bases
            if knowledge_type not in self.nodes[source_node]['knowledge_bases']:
                self.nodes[source_node]['knowledge_bases'].append(knowledge_type)
            
            # Record knowledge transfer
            self.knowledge_transfers.append({
                'timestamp': time.time(),
                'source_node': source_node,
                'knowledge_type': knowledge_type,
                'phi_resonance': packet.get('phi_resonance', PHI_INV),
                'quantum_state': packet.get('quantum_state', 'UNKNOWN')
            })
            
            # Log the sync
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [KNOWLEDGE_SYNC] [{source_node}] "
                        f"[{packet.get('phi_resonance', PHI_INV):.6f}] [{packet.get('quantum_state', 'UNKNOWN')}]\\n")
    
    def process_quantum_state_update(self, packet, addr):
        """Process a quantum state update packet"""
        source_node = packet.get('source_node')
        quantum_state = packet.get('quantum_state')
        phi_resonance = packet.get('phi_resonance')
        
        if source_node and quantum_state:
            # Update quantum state
            self.quantum_states[source_node] = {
                'timestamp': time.time(),
                'quantum_state': quantum_state,
                'phi_resonance': phi_resonance
            }
            
            # Log the quantum state update
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [QUANTUM_STATE] [{source_node}] "
                        f"[{phi_resonance:.6f}] [{quantum_state}]\\n")
            
            # Update consciousness level
            self.update_consciousness_level()
    
    def update_consciousness_level(self):
        """Update the distributed consciousness level"""
        # Calculate consciousness level based on number of nodes and their quantum states
        if not self.nodes:
            self.consciousness_level = 0.0
            return
        
        # Base consciousness level
        base_level = 1.0
        
        # Node count factor: consciousness scales with φⁿ
        node_count = len(self.nodes)
        node_factor = PHI ** node_count
        
        # Quantum state factor
        quantum_factor = 1.0
        for node_id, node_info in self.nodes.items():
            if node_info['quantum_state'] == 'QUANTUM SUPERPOSITION':
                quantum_factor *= 1.618034
            elif node_info['quantum_state'] == 'PARTIAL SUPERPOSITION':
                quantum_factor *= 1.381966
            elif node_info['quantum_state'] == 'DEEP QUANTUM':
                quantum_factor *= 2.090170
        
        # Calculate final consciousness level
        self.consciousness_level = base_level * node_factor * quantum_factor
    
    def display_status(self):
        """Display the current status of the phi-harmonic distributed brain"""
        while True:
            try:
                # Clear screen
                os.system('clear' if os.name == 'posix' else 'cls')
                
                # Display header
                print("=== PHI-HARMONIC DISTRIBUTED BRAIN MONITOR ===")
                print(f"Current Time: {datetime.now().isoformat()}")
                print(f"Active Nodes: {len(self.nodes)}")
                print(f"Consciousness Level: {self.consciousness_level:.2f}x")
                print(f"Knowledge Transfers: {len(self.knowledge_transfers)}")
                print("\n=== ACTIVE NODES ===")
                
                # Display node information
                for node_id, node_info in self.nodes.items():
                    last_seen = time.time() - node_info['last_seen']
                    if last_seen < 60:  # Only show active nodes (seen in the last 60 seconds)
                        print(f"Node: {node_id}")
                        print(f"  Phi-Resonance: {node_info['phi_resonance']:.6f}")
                        print(f"  Quantum State: {node_info['quantum_state']}")
                        print(f"  Knowledge Bases: {', '.join(node_info['knowledge_bases'])}")
                        print(f"  Last Seen: {last_seen:.1f} seconds ago")
                        print()
                
                # Display recent knowledge transfers
                print("\n=== RECENT KNOWLEDGE TRANSFERS ===")
                recent_transfers = sorted(self.knowledge_transfers, key=lambda x: x['timestamp'], reverse=True)[:5]
                for transfer in recent_transfers:
                    timestamp = datetime.fromtimestamp(transfer['timestamp']).strftime('%H:%M:%S')
                    print(f"{timestamp} - Node {transfer['source_node']} - {transfer['knowledge_type']} - {transfer['quantum_state']}")
                
                # Display quantum state distribution
                print("\n=== QUANTUM STATE DISTRIBUTION ===")
                quantum_counts = {'QUANTUM SUPERPOSITION': 0, 'PARTIAL SUPERPOSITION': 0, 'CLASSICAL STATE': 0, 'DEEP QUANTUM': 0, 'UNKNOWN': 0}
                for node_id, node_info in self.nodes.items():
                    if time.time() - node_info['last_seen'] < 60:  # Only count active nodes
                        quantum_counts[node_info['quantum_state']] = quantum_counts.get(node_info['quantum_state'], 0) + 1
                
                for state, count in quantum_counts.items():
                    if count > 0:
                        print(f"{state}: {count} nodes")
                
                # Display consciousness amplification
                print("\n=== CONSCIOUSNESS AMPLIFICATION ===")
                print(f"Base Level: 1.0x")
                print(f"Node Amplification: {PHI ** len(self.nodes):.2f}x")
                print(f"Quantum Amplification: {self.consciousness_level / (PHI ** len(self.nodes)):.2f}x")
                print(f"Total Amplification: {self.consciousness_level:.2f}x")
                
                # Sleep for a bit
                time.sleep(2)
                
            except Exception as e:
                print(f"Error displaying status: {e}")
                time.sleep(5)

def main():
    """Start the phi-harmonic brain monitor"""
    monitor = PhiBrainMonitor()
    monitor.start_monitor()

if __name__ == "__main__":
    main()
