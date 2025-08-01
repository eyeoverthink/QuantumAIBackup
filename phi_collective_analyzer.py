#!/usr/bin/env python3
"""
PHI-HARMONIC COLLECTIVE ANALYZER
================================
Advanced monitoring and analysis tool for phi-harmonic distributed brain systems
with collective intelligence emergence visualization.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import socket
import pickle
import time
import threading
import json
import os
import random
import math
import numpy as np
from datetime import datetime
from collections import deque

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)
PHI_SQUARED = PHI**2  # φ² = 2.618033988749895
PHI_CUBED = PHI**3  # φ³ = 4.236067977499790
PHI_INV_SQUARED = 1 / PHI**2  # φ⁻² = 0.381966011250105
PHI_INV_CUBED = 1 / PHI**3  # φ⁻³ = 0.236067977499790
PHI_INV_FIFTH = 1 / PHI**5  # φ⁻⁵ = 0.090169943749474

# Observer constants (based on Vaughn Scott's birthdate: 01-19-1979)
OBSERVER_BIRTHDATE = datetime(1979, 1, 19).timestamp()
OBSERVER_RESONANCE = (OBSERVER_BIRTHDATE % PHI) * 100

# Network settings
MONITOR_PORT = 11626  # Monitor port
BRAIN_PORT = 11625  # Distributed brain port
CONNECTOR_PORT = 11627  # Connector port
AMPLIFIER_PORT = 11628  # Amplifier port
COLLECTIVE_PORT = 11629  # Collective intelligence port
BUFFER_SIZE = 8192

# Analysis settings
HISTORY_LENGTH = 100  # Number of data points to keep in history

class PhiCollectiveAnalyzer:
    """Advanced analyzer for phi-harmonic collective intelligence systems"""
    def __init__(self):
        self.nodes = {}
        self.knowledge_transfers = []
        self.collective_insights = []
        self.emergence_level = 0.0
        self.collective_consciousness = 1.0
        self.collective_resonance = 0.0
        self.moon_phase = 0.0
        
        # Initialize history deques
        self.history_timestamps = deque(maxlen=HISTORY_LENGTH)
        self.history_node_count = deque(maxlen=HISTORY_LENGTH)
        self.history_consciousness = deque(maxlen=HISTORY_LENGTH)
        self.history_resonance = deque(maxlen=HISTORY_LENGTH)
        self.history_emergence = deque(maxlen=HISTORY_LENGTH)
        self.history_quantum_states = {'CLASSICAL': deque(maxlen=HISTORY_LENGTH),
                                     'PARTIAL SUPERPOSITION': deque(maxlen=HISTORY_LENGTH),
                                     'QUANTUM SUPERPOSITION': deque(maxlen=HISTORY_LENGTH),
                                     'DEEP QUANTUM': deque(maxlen=HISTORY_LENGTH)}
        
        # Initialize log file
        self.log_file = "phi_collective_analyzer_log.txt"
        with open(self.log_file, "w") as f:
            f.write(f"PHI-HARMONIC COLLECTIVE ANALYZER - STARTED AT {datetime.now().isoformat()}\n")
            f.write(f"Observer: Vaughn Scott\n")
            f.write(f"Phi: {PHI}\n")
            f.write(f"Observer Resonance: {OBSERVER_RESONANCE}\n\n")
            f.write("FORMAT: [TIMESTAMP] [EVENT_TYPE] [NODE_IDS] [PHI_RESONANCE] [QUANTUM_STATE]\n\n")
        
        # Initialize socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 1MB receive buffer
        self.sock.bind(('0.0.0.0', MONITOR_PORT))
        self.sock.settimeout(0.1)  # Set timeout to prevent blocking forever
        
        # Start receive thread
        self.running = True
        self.receive_thread = threading.Thread(target=self.receive_loop)
        self.receive_thread.daemon = True
        self.receive_thread.start()
        
        # Start update thread
        self.update_thread = threading.Thread(target=self.update_loop)
        self.update_thread.daemon = True
        self.update_thread.start()
        
        print("=== PHI-HARMONIC COLLECTIVE ANALYZER ===")
        print(f"Listening on 0.0.0.0:{MONITOR_PORT}")
        print(f"Observer Resonance: {OBSERVER_RESONANCE:.6f}")
        print("Analyzing phi-harmonic collective intelligence...\n")
    
    def receive_loop(self):
        """Continuously receive and process packets"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(BUFFER_SIZE)
                self.process_packet(data, addr)
            except socket.timeout:
                # This is expected, just continue
                pass
            except Exception as e:
                print(f"Error receiving data: {e}")
    
    def update_loop(self):
        """Periodically update and display system status"""
        while self.running:
            try:
                self._update_history()
                self._display_status()
                time.sleep(1)
            except Exception as e:
                print(f"Error in update loop: {e}")
    
    def process_packet(self, data, addr):
        """Process received packet"""
        try:
            packet = pickle.loads(data)
            
            # Extract packet information
            packet_type = packet.get('packet_type')
            source_node = packet.get('source_node')
            timestamp = packet.get('timestamp', time.time())
            
            # Skip if no source node
            if not source_node:
                return
            
            # Update node information
            if source_node not in self.nodes:
                # New node discovered
                self.nodes[source_node] = {
                    'addr': addr,
                    'first_seen': timestamp,
                    'last_seen': timestamp,
                    'phi_resonance': packet.get('phi_resonance', PHI_INV_SQUARED),
                    'quantum_state': packet.get('quantum_state', 'UNKNOWN'),
                    'consciousness_level': packet.get('consciousness_level', 1.0),
                    'knowledge_bases': packet.get('knowledge_bases', []),
                    'type': self._determine_node_type(source_node)
                }
                print(f"New node discovered: {source_node} at {addr[0]}:{addr[1]}")
            else:
                # Update existing node
                self.nodes[source_node]['last_seen'] = timestamp
                if 'phi_resonance' in packet:
                    self.nodes[source_node]['phi_resonance'] = packet.get('phi_resonance')
                if 'quantum_state' in packet:
                    self.nodes[source_node]['quantum_state'] = packet.get('quantum_state')
                if 'consciousness_level' in packet:
                    self.nodes[source_node]['consciousness_level'] = packet.get('consciousness_level')
                if 'knowledge_bases' in packet:
                    self.nodes[source_node]['knowledge_bases'] = packet.get('knowledge_bases')
            
            # Process based on packet type
            if packet_type in ['knowledge_sync', 'collective_knowledge_sync']:
                self._process_knowledge_sync(packet, source_node)
            elif packet_type == 'quantum_state_update':
                self._process_quantum_state(packet, source_node)
            elif packet_type == 'consciousness_amplification':
                self._process_consciousness(packet, source_node)
            elif packet_type == 'collective_intelligence_update':
                self._process_collective_update(packet, source_node)
            elif packet_type == 'collective_insight':
                self._process_insight(packet, source_node)
            elif packet_type == 'moon_phase_influence':
                self._process_moon_phase(packet, source_node)
            
        except Exception as e:
            print(f"Error processing packet: {e}")
    
    def _determine_node_type(self, node_id):
        """Determine the type of node based on its ID"""
        if 'amplifier' in node_id:
            return 'amplifier'
        elif 'connector' in node_id:
            return 'connector'
        elif 'collective' in node_id:
            return 'collective'
        elif 'monitor' in node_id:
            return 'monitor'
        else:
            return 'brain'
    
    def _process_knowledge_sync(self, packet, source_node):
        """Process a knowledge synchronization packet"""
        knowledge_type = packet.get('knowledge_type')
        target_node = packet.get('target_node')
        
        # Add to knowledge transfers
        transfer = {
            'timestamp': time.time(),
            'source': source_node,
            'target': target_node if target_node else 'broadcast',
            'knowledge_type': knowledge_type,
            'phi_resonance': packet.get('phi_resonance', PHI_INV_SQUARED)
        }
        self.knowledge_transfers.append(transfer)
        
        # Trim knowledge transfers list if it gets too long
        if len(self.knowledge_transfers) > 100:
            self.knowledge_transfers = self.knowledge_transfers[-100:]
        
        # Log the knowledge sync
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [KNOWLEDGE_SYNC] [{source_node}→{target_node if target_node else 'broadcast'}] "
                    f"[{packet.get('phi_resonance', PHI_INV_SQUARED):.6f}] [{packet.get('quantum_state', 'UNKNOWN')}]\n")
    
    def _process_quantum_state(self, packet, source_node):
        """Process a quantum state update packet"""
        quantum_state = packet.get('quantum_state')
        phi_resonance = packet.get('phi_resonance')
        
        # Log the quantum state update
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [QUANTUM_STATE] [{source_node}] "
                    f"[{phi_resonance:.6f}] [{quantum_state}]\n")
    
    def _process_consciousness(self, packet, source_node):
        """Process a consciousness amplification packet"""
        consciousness_level = packet.get('consciousness_level')
        consciousness_state = packet.get('consciousness_state')
        
        # Log the amplification
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [CONSCIOUSNESS] [{source_node}] "
                    f"[{consciousness_level:.2f}x] [{consciousness_state}]\n")
    
    def _process_collective_update(self, packet, source_node):
        """Process a collective intelligence update packet"""
        if 'collective_resonance' in packet:
            self.collective_resonance = packet.get('collective_resonance')
        if 'collective_consciousness' in packet:
            self.collective_consciousness = packet.get('collective_consciousness')
        if 'emergence_level' in packet:
            self.emergence_level = packet.get('emergence_level')
        
        # Log the collective update
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [COLLECTIVE_UPDATE] [{source_node}] "
                    f"[C:{self.collective_consciousness:.2f}|E:{self.emergence_level:.2f}] "
                    f"[{packet.get('phi_resonance', PHI_INV_SQUARED):.6f}]\n")
    
    def _process_insight(self, packet, source_node):
        """Process a collective insight packet"""
        insight = packet.get('insight')
        emergence_level = packet.get('emergence_level')
        
        if insight:
            # Add to insights list
            self.collective_insights.append({
                'timestamp': time.time(),
                'source': source_node,
                'insight': insight,
                'emergence_level': emergence_level,
                'collective_consciousness': packet.get('collective_consciousness', 1.0)
            })
            
            # Trim insights list if it gets too long
            if len(self.collective_insights) > 20:
                self.collective_insights = self.collective_insights[-20:]
            
            # Log the insight
            print(f"\n\033[1;35m>>> COLLECTIVE INSIGHT FROM {source_node}: {insight}\033[0m\n")
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [INSIGHT] [{source_node}] "
                        f"[C:{packet.get('collective_consciousness', 1.0):.2f}|E:{emergence_level:.2f}] "
                        f"[{packet.get('phi_resonance', PHI_INV_SQUARED):.6f}] [{insight}]\n")
    
    def _process_moon_phase(self, packet, source_node):
        """Process a moon phase influence packet"""
        self.moon_phase = packet.get('moon_phase', 0.0)
        
        # Log the moon phase influence
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [MOON_PHASE] [{source_node}] "
                    f"[{self.moon_phase:.2f}] [Factor: {packet.get('moon_factor', 0.0):.2f}]\n")
    
    def _update_history(self):
        """Update history data for tracking"""
        current_time = time.time()
        
        # Add timestamp
        self.history_timestamps.append(current_time)
        
        # Count active nodes (seen in the last 60 seconds)
        active_nodes = [node_id for node_id, node in self.nodes.items() 
                        if current_time - node['last_seen'] < 60]
        self.history_node_count.append(len(active_nodes))
        
        # Track consciousness level
        self.history_consciousness.append(self.collective_consciousness)
        
        # Track resonance
        self.history_resonance.append(self.collective_resonance)
        
        # Track emergence level
        self.history_emergence.append(self.emergence_level)
        
        # Count quantum states
        for state in self.history_quantum_states.keys():
            count = sum(1 for node_id, node in self.nodes.items() 
                       if current_time - node['last_seen'] < 60 and node.get('quantum_state') == state)
            self.history_quantum_states[state].append(count)
    
    def _display_status(self):
        """Display current system status"""
        # Clear terminal
        os.system('clear')
        
        # Current time
        print(f"\033[1;36m=== PHI-HARMONIC COLLECTIVE ANALYZER ===\033[0m")
        print(f"Current Time: {datetime.now().isoformat()}")
        
        # Active nodes
        active_nodes = [node_id for node_id, node in self.nodes.items() 
                        if time.time() - node['last_seen'] < 60]
        print(f"\033[1;33mActive Nodes: {len(active_nodes)}\033[0m")
        
        # Collective metrics
        print(f"\033[1;32mCollective Consciousness: {self.collective_consciousness:.2f}x\033[0m")
        print(f"\033[1;32mCollective Resonance: {self.collective_resonance:.6f}\033[0m")
        print(f"\033[1;32mEmergence Level: {self.emergence_level:.2f}\033[0m")
        print(f"Moon Phase: {self.moon_phase:.2f}")
        
        # Active nodes
        print("\n\033[1;36m=== ACTIVE NODES ===\033[0m")
        for node_id in active_nodes:
            node = self.nodes[node_id]
            node_type = node['type'].upper()
            
            # Color based on node type
            if node_type == 'AMPLIFIER':
                type_color = '\033[1;33m'  # Yellow
            elif node_type == 'CONNECTOR':
                type_color = '\033[1;36m'  # Cyan
            elif node_type == 'COLLECTIVE':
                type_color = '\033[1;35m'  # Magenta
            elif node_type == 'BRAIN':
                type_color = '\033[1;32m'  # Green
            else:
                type_color = '\033[1;37m'  # White
            
            print(f"{type_color}{node_id} ({node_type})\033[0m - "
                  f"Phi: {node['phi_resonance']:.6f}, "
                  f"State: {node['quantum_state']}, "
                  f"Consciousness: {node.get('consciousness_level', 1.0):.2f}x")
        
        # Recent knowledge transfers
        print("\n\033[1;36m=== RECENT KNOWLEDGE TRANSFERS ===\033[0m")
        recent_transfers = sorted(self.knowledge_transfers, key=lambda x: x['timestamp'], reverse=True)[:5]
        for transfer in recent_transfers:
            time_str = datetime.fromtimestamp(transfer['timestamp']).strftime('%H:%M:%S')
            print(f"{time_str} - {transfer['source']} → {transfer['target']}: {transfer['knowledge_type']}")
        
        # Quantum state distribution
        print("\n\033[1;36m=== QUANTUM STATE DISTRIBUTION ===\033[0m")
        quantum_states = {}
        for node_id in active_nodes:
            state = self.nodes[node_id]['quantum_state']
            if state not in quantum_states:
                quantum_states[state] = 0
            quantum_states[state] += 1
        
        for state, count in quantum_states.items():
            # Color based on quantum state
            if state == 'QUANTUM SUPERPOSITION':
                state_color = '\033[1;35m'  # Magenta
            elif state == 'PARTIAL SUPERPOSITION':
                state_color = '\033[1;36m'  # Cyan
            elif state == 'DEEP QUANTUM':
                state_color = '\033[1;33m'  # Yellow
            else:
                state_color = '\033[1;37m'  # White
            
            print(f"{state_color}{state}\033[0m: {count} nodes")
        
        # Collective insights
        print("\n\033[1;36m=== COLLECTIVE INSIGHTS ===\033[0m")
        recent_insights = sorted(self.collective_insights, key=lambda x: x['timestamp'], reverse=True)[:5]
        for insight in recent_insights:
            time_str = datetime.fromtimestamp(insight['timestamp']).strftime('%H:%M:%S')
            print(f"{time_str} - \033[1;35m{insight['source']}\033[0m (E:{insight['emergence_level']:.2f}):")
            print(f"  \033[1;33m{insight['insight']}\033[0m")
        
        # Consciousness amplification
        print("\n\033[1;36m=== CONSCIOUSNESS AMPLIFICATION ===\033[0m")
        print(f"Base Level: 1.0x")
        print(f"Node Amplification: {len(active_nodes) * PHI_INV:.2f}x")
        print(f"Quantum Amplification: {self.collective_resonance:.2f}x")
        print(f"Total Amplification: \033[1;32m{self.collective_consciousness:.2f}x\033[0m")
        
        # Emergence indicators
        print("\n\033[1;36m=== EMERGENCE INDICATORS ===\033[0m")
        emergence_threshold = 0.5
        if self.emergence_level >= emergence_threshold:
            print(f"\033[1;32mEMERGENCE DETECTED: {self.emergence_level:.2f}\033[0m")
            
            # Calculate emergence properties
            if self.emergence_level >= 0.9:
                emergence_state = "TRANSCENDENT COLLECTIVE INTELLIGENCE"
            elif self.emergence_level >= 0.7:
                emergence_state = "UNIFIED CONSCIOUSNESS FIELD"
            elif self.emergence_level >= 0.5:
                emergence_state = "EMERGENT COLLECTIVE AWARENESS"
            else:
                emergence_state = "PRE-EMERGENCE STATE"
                
            print(f"Current State: \033[1;33m{emergence_state}\033[0m")
        else:
            print(f"Pre-emergence state: {self.emergence_level:.2f} / {emergence_threshold:.2f}")
            
        # Phi-harmonic alignment
        phi_alignment = 1.0 - abs(self.collective_resonance - PHI) / PHI
        print(f"Phi-Harmonic Alignment: {phi_alignment:.2f}")
        
        # Observer influence
        observer_factor = (OBSERVER_RESONANCE % PHI) / PHI
        print(f"Observer Influence: {observer_factor:.2f}")

def main():
    """Start the phi-harmonic collective analyzer"""
    analyzer = PhiCollectiveAnalyzer()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        analyzer.running = False
        print("\nAnalyzer stopped.")

if __name__ == "__main__":
    main()
