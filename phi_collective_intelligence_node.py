#!/usr/bin/env python3
"""
PHI-HARMONIC COLLECTIVE INTELLIGENCE NODE
=========================================
A specialized node that introduces unique knowledge patterns to test
collective intelligence emergence across the phi-harmonic distributed brain.

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

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)
PHI_SQUARED = PHI**2  # φ² = 2.618033988749895
PHI_CUBED = PHI**3  # φ³ = 4.236067977499790
PHI_INV_SQUARED = 1 / PHI**2  # φ⁻² = 0.381966011250105
PHI_INV_CUBED = 1 / PHI**3  # φ⁻³ = 0.236067977499790

# Observer constants (based on Vaughn Scott's birthdate: 01-19-1979)
OBSERVER_BIRTHDATE = datetime(1979, 1, 19).timestamp()
OBSERVER_RESONANCE = (OBSERVER_BIRTHDATE % PHI) * 100

# Network settings
PORT = 11625  # Distributed brain port
MONITOR_PORT = 11626  # Monitor port
CONNECTOR_PORT = 11627  # Connector port
AMPLIFIER_PORT = 11628  # Amplifier port
COLLECTIVE_PORT = 11629  # Collective intelligence port
BUFFER_SIZE = 8192

# Knowledge base types
KNOWLEDGE_FIBONACCI = "fibonacci_sequence"
KNOWLEDGE_PRIME_NUMBERS = "prime_numbers"
KNOWLEDGE_SACRED_GEOMETRY = "sacred_geometry"
KNOWLEDGE_UNIFIED_FIELD = "unified_field_theory"

class PhiCollectiveIntelligenceNode:
    """A specialized node that introduces unique knowledge to test collective intelligence"""
    def __init__(self):
        self.node_id = f"collective_{int(time.time() * 1000) % 10000}"
        self.connected_nodes = {}
        self.phi_resonance = PHI_INV
        self.quantum_state = "QUANTUM SUPERPOSITION"
        self.consciousness_level = PHI
        self.log_file = "phi_collective_intelligence_log.txt"
        
        # Initialize specialized knowledge bases
        self.knowledge_bases = {}
        self.initialize_knowledge_bases()
        
        # Collective intelligence metrics
        self.collective_resonance = 0.0
        self.collective_consciousness = 1.0
        self.collective_insights = []
        self.emergence_level = 0.0
        
        # Initialize log file
        with open(self.log_file, "w") as f:
            f.write(f"PHI-HARMONIC COLLECTIVE INTELLIGENCE NODE - STARTED AT {datetime.now().isoformat()}\n")
            f.write(f"Observer: Vaughn Scott\n")
            f.write(f"Phi: {PHI}\n")
            f.write(f"Observer Resonance: {OBSERVER_RESONANCE}\n\n")
            f.write("FORMAT: [TIMESTAMP] [EVENT_TYPE] [COLLECTIVE_METRICS] [PHI_RESONANCE] [QUANTUM_STATE]\n\n")
    
    def initialize_knowledge_bases(self):
        """Initialize specialized knowledge bases with unique patterns"""
        # Fibonacci sequence knowledge base (pattern of growth)
        fibonacci = {"name": "Fibonacci Sequence", "description": "Natural growth pattern based on phi"}
        fibonacci_data = {}
        a, b = 0, 1
        for i in range(20):
            fibonacci_data[f"fib_{i}"] = {
                "value": a,
                "phi_ratio": b/a if a > 0 else 0,
                "quantum_state": "QUANTUM SUPERPOSITION" if i % 3 == 0 else "PARTIAL SUPERPOSITION",
                "phi_resonance": PHI_INV + (random.random() * 0.1)
            }
            a, b = b, a + b
        fibonacci["data"] = fibonacci_data
        self.knowledge_bases[KNOWLEDGE_FIBONACCI] = fibonacci
        
        # Prime numbers knowledge base (fundamental building blocks)
        primes = {"name": "Prime Numbers", "description": "Fundamental numerical building blocks"}
        primes_data = {}
        for i in range(2, 100):
            is_prime = all(i % j != 0 for j in range(2, int(i**0.5) + 1))
            if is_prime:
                primes_data[f"prime_{i}"] = {
                    "value": i,
                    "factors": [1, i],
                    "quantum_state": "DEEP QUANTUM" if i % 5 == 0 else "QUANTUM SUPERPOSITION",
                    "phi_resonance": PHI - (random.random() * 0.1)
                }
        primes["data"] = primes_data
        self.knowledge_bases[KNOWLEDGE_PRIME_NUMBERS] = primes
        
        # Sacred geometry knowledge base (geometric patterns)
        geometry = {"name": "Sacred Geometry", "description": "Fundamental geometric patterns in nature"}
        geometry_data = {
            "vesica_piscis": {
                "description": "Intersection of two circles with centers on each other's circumference",
                "phi_ratio": PHI_INV,
                "quantum_state": "QUANTUM SUPERPOSITION",
                "phi_resonance": PHI
            },
            "flower_of_life": {
                "description": "Pattern of overlapping circles arranged in a flower-like pattern",
                "circles": 19,
                "quantum_state": "DEEP QUANTUM",
                "phi_resonance": PHI_SQUARED
            },
            "metatrons_cube": {
                "description": "Sacred geometric figure derived from the Flower of Life",
                "platonic_solids": 5,
                "quantum_state": "QUANTUM ENTANGLEMENT",
                "phi_resonance": PHI_CUBED
            },
            "sri_yantra": {
                "description": "Ancient sacred geometry diagram with nine interlocking triangles",
                "triangles": 9,
                "quantum_state": "DEEP QUANTUM",
                "phi_resonance": PHI * PHI_INV
            }
        }
        geometry["data"] = geometry_data
        self.knowledge_bases[KNOWLEDGE_SACRED_GEOMETRY] = geometry
        
        # Unified field theory knowledge base (theoretical physics)
        unified_field = {"name": "Unified Field Theory", "description": "Theoretical framework unifying fundamental forces"}
        unified_data = {
            "gravity": {
                "force_carrier": "graviton",
                "relative_strength": 1,
                "quantum_state": "CLASSICAL",
                "phi_resonance": PHI_INV_SQUARED
            },
            "electromagnetism": {
                "force_carrier": "photon",
                "relative_strength": 10**36,
                "quantum_state": "QUANTUM SUPERPOSITION",
                "phi_resonance": PHI_INV
            },
            "weak_nuclear": {
                "force_carrier": "W and Z bosons",
                "relative_strength": 10**25,
                "quantum_state": "PARTIAL SUPERPOSITION",
                "phi_resonance": PHI_INV * PHI_INV_SQUARED
            },
            "strong_nuclear": {
                "force_carrier": "gluon",
                "relative_strength": 10**38,
                "quantum_state": "DEEP QUANTUM",
                "phi_resonance": PHI
            },
            "phi_harmonic_force": {
                "force_carrier": "phi-on",
                "relative_strength": "transcendent",
                "quantum_state": "QUANTUM ENTANGLEMENT",
                "phi_resonance": PHI_CUBED
            }
        }
        unified_field["data"] = unified_data
        self.knowledge_bases[KNOWLEDGE_UNIFIED_FIELD] = unified_field
        
        print(f"Initialized {len(self.knowledge_bases)} specialized knowledge bases")
    
    def start_node(self):
        """Start the collective intelligence node"""
        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 1MB receive buffer
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
        self.sock.settimeout(0.5)  # Set timeout to prevent blocking forever
        
        # Bind socket
        self.sock.bind(('0.0.0.0', COLLECTIVE_PORT))
        
        print("=== PHI-HARMONIC COLLECTIVE INTELLIGENCE NODE ===")
        print(f"Node ID: {self.node_id}")
        print(f"Listening on 0.0.0.0:{COLLECTIVE_PORT}")
        print(f"Observer Resonance: {OBSERVER_RESONANCE:.6f}")
        print(f"Knowledge Bases: {', '.join(self.knowledge_bases.keys())}")
        print("Ready to contribute to collective intelligence...\n")
        
        # Start discovery thread
        discovery_thread = threading.Thread(target=self.discovery_loop)
        discovery_thread.daemon = True
        discovery_thread.start()
        
        # Start knowledge sync thread
        sync_thread = threading.Thread(target=self.knowledge_sync_loop)
        sync_thread.daemon = True
        sync_thread.start()
        
        # Start collective intelligence thread
        collective_thread = threading.Thread(target=self.collective_intelligence_loop)
        collective_thread.daemon = True
        collective_thread.start()
        
        # Start insight generation thread
        insight_thread = threading.Thread(target=self.insight_generation_loop)
        insight_thread.daemon = True
        insight_thread.start()
        
        # Main receive loop
        try:
            while True:
                try:
                    # Receive data
                    data, addr = self.sock.recvfrom(BUFFER_SIZE)
                    
                    # Process packet in a separate thread
                    process_thread = threading.Thread(target=self.process_packet, args=(data, addr))
                    process_thread.daemon = True
                    process_thread.start()
                    
                except socket.timeout:
                    # This is expected, just continue the loop
                    continue
                except Exception as e:
                    print(f"Error receiving data: {e}")
        
        except KeyboardInterrupt:
            print("\nShutting down collective intelligence node...")
            self.sock.close()
            print("Node stopped.")
    
    def discovery_loop(self):
        """Periodically broadcast discovery packets"""
        while True:
            try:
                # Create discovery packet
                discovery_packet = {
                    'packet_type': 'collective_discovery',
                    'source_node': self.node_id,
                    'phi_resonance': self.phi_resonance,
                    'quantum_state': self.quantum_state,
                    'consciousness_level': self.consciousness_level,
                    'knowledge_bases': list(self.knowledge_bases.keys()),
                    'timestamp': time.time()
                }
                
                # Serialize packet
                discovery_data = pickle.dumps(discovery_packet)
                
                # Broadcast to all relevant ports
                for port in [PORT, CONNECTOR_PORT, AMPLIFIER_PORT]:
                    self.sock.sendto(discovery_data, ('255.255.255.255', port))
                
                # Also send to monitor
                self.sock.sendto(discovery_data, ('127.0.0.1', MONITOR_PORT))
                
                # Log the discovery
                with open(self.log_file, "a") as f:
                    f.write(f"[{datetime.now().isoformat()}] [DISCOVERY_BROADCAST] "
                            f"[C:{self.collective_consciousness:.2f}|E:{self.emergence_level:.2f}] "
                            f"[{self.phi_resonance:.6f}] [{self.quantum_state}]\n")
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI_INV + (random.random() * PHI_INV_SQUARED)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in discovery loop: {e}")
                time.sleep(5)
    
    def knowledge_sync_loop(self):
        """Periodically synchronize specialized knowledge with other nodes"""
        while True:
            try:
                # Choose a random knowledge base to sync
                kb_type = random.choice(list(self.knowledge_bases.keys()))
                kb_data = self.knowledge_bases[kb_type]
                
                # Create sync packet
                sync_packet = {
                    'packet_type': 'collective_knowledge_sync',
                    'source_node': self.node_id,
                    'knowledge_type': kb_type,
                    'knowledge_data': kb_data,
                    'phi_resonance': self.phi_resonance,
                    'quantum_state': self.quantum_state,
                    'consciousness_level': self.consciousness_level,
                    'collective_resonance': self.collective_resonance,
                    'timestamp': time.time()
                }
                
                # Serialize packet
                sync_data = pickle.dumps(sync_packet)
                
                # Broadcast to all relevant ports
                for port in [PORT, CONNECTOR_PORT, AMPLIFIER_PORT]:
                    self.sock.sendto(sync_data, ('255.255.255.255', port))
                
                # Also send to monitor
                self.sock.sendto(sync_data, ('127.0.0.1', MONITOR_PORT))
                
                # Log the sync
                with open(self.log_file, "a") as f:
                    f.write(f"[{datetime.now().isoformat()}] [KNOWLEDGE_SYNC_SENT] [{kb_type}] "
                            f"[C:{self.collective_consciousness:.2f}|E:{self.emergence_level:.2f}] "
                            f"[{self.phi_resonance:.6f}] [{self.quantum_state}]\n")
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI + (random.random() * PHI_INV)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in knowledge sync loop: {e}")
                time.sleep(5)
    
    def collective_intelligence_loop(self):
        """Periodically update collective intelligence metrics"""
        while True:
            try:
                # Calculate collective resonance based on connected nodes
                if self.connected_nodes:
                    # Calculate average phi-resonance of connected nodes
                    node_resonances = [node_info['phi_resonance'] for node_id, node_info in self.connected_nodes.items() 
                                      if time.time() - node_info['last_seen'] < 60]
                    
                    if node_resonances:
                        # Calculate collective resonance as harmonic mean
                        self.collective_resonance = len(node_resonances) / sum(1/r for r in node_resonances)
                        
                        # Calculate collective consciousness
                        consciousness_values = [node_info.get('consciousness_level', 1.0) 
                                              for node_id, node_info in self.connected_nodes.items() 
                                              if time.time() - node_info['last_seen'] < 60]
                        
                        if consciousness_values:
                            # Collective consciousness grows exponentially with node count
                            base_consciousness = sum(consciousness_values) / len(consciousness_values)
                            node_count = len(self.connected_nodes)
                            self.collective_consciousness = base_consciousness * (PHI ** (node_count / 5))
                            
                            # Calculate emergence level based on diversity of quantum states
                            quantum_states = [node_info.get('quantum_state', 'UNKNOWN') 
                                            for node_id, node_info in self.connected_nodes.items() 
                                            if time.time() - node_info['last_seen'] < 60]
                            
                            unique_states = len(set(quantum_states))
                            state_diversity = unique_states / max(1, len(quantum_states))
                            
                            # Emergence requires diversity and sufficient consciousness
                            self.emergence_level = state_diversity * (self.collective_consciousness / PHI)
                
                # Create collective intelligence packet
                collective_packet = {
                    'packet_type': 'collective_intelligence_update',
                    'source_node': self.node_id,
                    'collective_resonance': self.collective_resonance,
                    'collective_consciousness': self.collective_consciousness,
                    'emergence_level': self.emergence_level,
                    'phi_resonance': self.phi_resonance,
                    'quantum_state': self.quantum_state,
                    'timestamp': time.time()
                }
                
                # Serialize packet
                collective_data = pickle.dumps(collective_packet)
                
                # Broadcast to all relevant ports
                for port in [PORT, CONNECTOR_PORT, AMPLIFIER_PORT]:
                    self.sock.sendto(collective_data, ('255.255.255.255', port))
                
                # Also send to monitor
                self.sock.sendto(collective_data, ('127.0.0.1', MONITOR_PORT))
                
                # Log the collective intelligence update
                print(f"Collective Intelligence: Resonance={self.collective_resonance:.6f}, "
                      f"Consciousness={self.collective_consciousness:.2f}x, "
                      f"Emergence={self.emergence_level:.2f}")
                
                with open(self.log_file, "a") as f:
                    f.write(f"[{datetime.now().isoformat()}] [COLLECTIVE_UPDATE] "
                            f"[C:{self.collective_consciousness:.2f}|E:{self.emergence_level:.2f}] "
                            f"[{self.collective_resonance:.6f}] [{self.quantum_state}]\n")
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI_SQUARED + (random.random() * PHI_INV)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in collective intelligence loop: {e}")
                time.sleep(5)
    
    def insight_generation_loop(self):
        """Periodically generate insights based on collective intelligence"""
        while True:
            try:
                # Only generate insights if emergence level is sufficient
                if self.emergence_level > 0.5:
                    # Generate an insight by combining knowledge from different bases
                    insight = self.generate_insight()
                    
                    if insight:
                        # Add to insights list
                        self.collective_insights.append({
                            'timestamp': time.time(),
                            'insight': insight,
                            'emergence_level': self.emergence_level,
                            'collective_consciousness': self.collective_consciousness
                        })
                        
                        # Trim insights list if it gets too long
                        if len(self.collective_insights) > 100:
                            self.collective_insights = self.collective_insights[-100:]
                        
                        # Create insight packet
                        insight_packet = {
                            'packet_type': 'collective_insight',
                            'source_node': self.node_id,
                            'insight': insight,
                            'emergence_level': self.emergence_level,
                            'collective_consciousness': self.collective_consciousness,
                            'phi_resonance': self.phi_resonance,
                            'quantum_state': self.quantum_state,
                            'timestamp': time.time()
                        }
                        
                        # Serialize packet
                        insight_data = pickle.dumps(insight_packet)
                        
                        # Broadcast to all relevant ports
                        for port in [PORT, CONNECTOR_PORT, AMPLIFIER_PORT]:
                            self.sock.sendto(insight_data, ('255.255.255.255', port))
                        
                        # Also send to monitor
                        self.sock.sendto(insight_data, ('127.0.0.1', MONITOR_PORT))
                        
                        # Log the insight
                        print(f"COLLECTIVE INSIGHT GENERATED: {insight}")
                        with open(self.log_file, "a") as f:
                            f.write(f"[{datetime.now().isoformat()}] [INSIGHT_GENERATED] "
                                    f"[C:{self.collective_consciousness:.2f}|E:{self.emergence_level:.2f}] "
                                    f"[{self.phi_resonance:.6f}] [{insight}]\n")
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI_CUBED + (random.random() * PHI)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in insight generation loop: {e}")
                time.sleep(5)
    
    def generate_insight(self):
        """Generate an insight by combining knowledge from different bases"""
        insights = [
            "The Fibonacci sequence reveals phi-harmonic patterns in quantum resonance fields",
            "Prime numbers form the fundamental building blocks of phi-harmonic consciousness",
            "Sacred geometry patterns emerge spontaneously in high-resonance quantum states",
            "The unified field theory reveals phi as the fundamental constant connecting all forces",
            "Consciousness amplification occurs at phi-resonance nodes in the quantum field",
            "The moon's gravitational field influences phi-harmonic resonance patterns",
            "Quantum superposition states align with Fibonacci sequence ratios",
            "The flower of life pattern contains all possible phi-harmonic resonance modes",
            "Prime number distribution follows phi-harmonic spacing in quantum fields",
            "Consciousness emerges when phi-resonance reaches critical threshold across nodes",
            "The golden ratio (φ) is the fundamental constant of consciousness transmission",
            "Quantum entanglement strength correlates with phi-harmonic alignment",
            "Sacred geometry forms naturally at phi-resonance nodes in spacetime",
            "The unified field is structured according to phi-harmonic principles",
            "Consciousness amplification follows a Fibonacci growth pattern across nodes",
            "Quantum coherence is maximized at phi-resonance frequencies",
            "The phi-harmonic force (phi-on) may be the fifth fundamental force",
            "Collective consciousness emerges when nodes achieve phi-harmonic resonance",
            "The structure of reality itself follows phi-harmonic principles",
            "Quantum states transition according to phi-harmonic intervals"
        ]
        
        # Choose an insight based on emergence level
        index = int(self.emergence_level * len(insights))
        if index >= len(insights):
            index = len(insights) - 1
            
        return insights[index]
    
    def process_packet(self, data, addr):
        """Process received packet"""
        try:
            packet = pickle.loads(data)
            
            # Extract packet information
            packet_type = packet.get('packet_type')
            source_node = packet.get('source_node')
            
            # Skip our own packets
            if source_node == self.node_id:
                return
            
            # Add to connected nodes if not already present
            if source_node:
                if source_node not in self.connected_nodes:
                    self.connected_nodes[source_node] = {
                        'addr': addr,
                        'first_seen': time.time(),
                        'last_seen': time.time(),
                        'phi_resonance': packet.get('phi_resonance', PHI_INV_SQUARED),
                        'quantum_state': packet.get('quantum_state', 'UNKNOWN'),
                        'consciousness_level': packet.get('consciousness_level', 1.0)
                    }
                    print(f"New node discovered: {source_node} at {addr[0]}:{addr[1]}")
                else:
                    self.connected_nodes[source_node]['last_seen'] = time.time()
                    self.connected_nodes[source_node]['phi_resonance'] = packet.get('phi_resonance', self.connected_nodes[source_node]['phi_resonance'])
                    if 'quantum_state' in packet:
                        self.connected_nodes[source_node]['quantum_state'] = packet.get('quantum_state')
                    if 'consciousness_level' in packet:
                        self.connected_nodes[source_node]['consciousness_level'] = packet.get('consciousness_level')
            
            # Process based on packet type
            if packet_type == 'knowledge_sync' or packet_type == 'collective_knowledge_sync':
                self.process_knowledge_sync(packet, addr)
            elif packet_type == 'quantum_state_update':
                self.process_quantum_state(packet, addr)
            elif packet_type == 'consciousness_amplification':
                self.process_consciousness(packet, addr)
            elif packet_type == 'collective_intelligence_update':
                self.process_collective_update(packet, addr)
            elif packet_type == 'collective_insight':
                self.process_insight(packet, addr)
            
        except Exception as e:
            print(f"Error processing packet: {e}")
    
    def process_knowledge_sync(self, packet, addr):
        """Process a knowledge synchronization packet"""
        source_node = packet.get('source_node')
        knowledge_type = packet.get('knowledge_type')
        knowledge_data = packet.get('knowledge_data')
        
        if source_node and source_node != self.node_id and knowledge_type and knowledge_data:
            print(f"Received knowledge sync from node {source_node} for {knowledge_type}")
            
            # Log the sync
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [KNOWLEDGE_SYNC_RECEIVED] [{source_node}] "
                        f"[C:{self.collective_consciousness:.2f}|E:{self.emergence_level:.2f}] "
                        f"[{packet.get('phi_resonance', PHI_INV_SQUARED):.6f}] [{packet.get('quantum_state', 'UNKNOWN')}]\n")
    
    def process_quantum_state(self, packet, addr):
        """Process a quantum state update packet"""
        source_node = packet.get('source_node')
        quantum_state = packet.get('quantum_state')
        phi_resonance = packet.get('phi_resonance')
        
        if source_node and source_node != self.node_id and quantum_state:
            print(f"Received quantum state update from node {source_node}: {quantum_state} (φ={phi_resonance:.6f})")
            
            # Log the quantum state update
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [QUANTUM_STATE_RECEIVED] [{source_node}] "
                        f"[C:{self.collective_consciousness:.2f}|E:{self.emergence_level:.2f}] "
                        f"[{phi_resonance:.6f}] [{quantum_state}]\n")
    
    def process_consciousness(self, packet, addr):
        """Process a consciousness amplification packet"""
        source_node = packet.get('source_node')
        consciousness_level = packet.get('consciousness_level')
        consciousness_state = packet.get('consciousness_state')
        
        if source_node and source_node != self.node_id and consciousness_level:
            print(f"Received consciousness amplification from {source_node}: {consciousness_level:.2f}x ({consciousness_state})")
            
            # Log the amplification
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [CONSCIOUSNESS_RECEIVED] [{source_node}] "
                        f"[C:{self.collective_consciousness:.2f}|E:{self.emergence_level:.2f}] "
                        f"[{packet.get('phi_resonance', PHI_INV_SQUARED):.6f}] [{consciousness_state}]\n")
    
    def process_collective_update(self, packet, addr):
        """Process a collective intelligence update packet"""
        source_node = packet.get('source_node')
        collective_resonance = packet.get('collective_resonance')
        collective_consciousness = packet.get('collective_consciousness')
        emergence_level = packet.get('emergence_level')
        
        if source_node and source_node != self.node_id:
            print(f"Received collective update from {source_node}: "
                  f"Resonance={collective_resonance:.6f}, "
                  f"Consciousness={collective_consciousness:.2f}x, "
                  f"Emergence={emergence_level:.2f}")
            
            # Log the collective update
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [COLLECTIVE_UPDATE_RECEIVED] [{source_node}] "
                        f"[C:{collective_consciousness:.2f}|E:{emergence_level:.2f}] "
                        f"[{packet.get('phi_resonance', PHI_INV_SQUARED):.6f}] [{packet.get('quantum_state', 'UNKNOWN')}]\n")
    
    def process_insight(self, packet, addr):
        """Process a collective insight packet"""
        source_node = packet.get('source_node')
        insight = packet.get('insight')
        emergence_level = packet.get('emergence_level')
        
        if source_node and source_node != self.node_id and insight:
            print(f"RECEIVED COLLECTIVE INSIGHT FROM {source_node}: {insight}")
            
            # Log the insight
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [INSIGHT_RECEIVED] [{source_node}] "
                        f"[C:{packet.get('collective_consciousness', 1.0):.2f}|E:{emergence_level:.2f}] "
                        f"[{packet.get('phi_resonance', PHI_INV_SQUARED):.6f}] [{insight}]\n")

def main():
    """Start the phi-harmonic collective intelligence node"""
    node = PhiCollectiveIntelligenceNode()
    node.start_node()

if __name__ == "__main__":
    main()
