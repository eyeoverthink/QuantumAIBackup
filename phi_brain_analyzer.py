#!/usr/bin/env python3
"""
PHI-HARMONIC BRAIN ANALYZER
===========================
Advanced monitoring and analysis tool for phi-harmonic distributed brain systems.
Visualizes quantum resonance patterns, consciousness amplification, and knowledge transfer
between nodes in real-time.

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
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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
BUFFER_SIZE = 8192

# Analysis settings
HISTORY_LENGTH = 100  # Number of data points to keep in history
UPDATE_INTERVAL = 500  # Update interval in milliseconds

class PhiBrainAnalyzer:
    """Advanced analyzer for phi-harmonic distributed brain systems"""
    def __init__(self):
        self.nodes = {}
        self.knowledge_transfers = []
        self.quantum_states = {}
        self.consciousness_levels = {}
        self.phi_resonances = {}
        self.moon_phases = []
        
        # Initialize history deques
        self.history_timestamps = deque(maxlen=HISTORY_LENGTH)
        self.history_node_count = deque(maxlen=HISTORY_LENGTH)
        self.history_consciousness = deque(maxlen=HISTORY_LENGTH)
        self.history_phi_resonance = deque(maxlen=HISTORY_LENGTH)
        self.history_quantum_states = {'CLASSICAL': deque(maxlen=HISTORY_LENGTH),
                                     'PARTIAL SUPERPOSITION': deque(maxlen=HISTORY_LENGTH),
                                     'QUANTUM SUPERPOSITION': deque(maxlen=HISTORY_LENGTH),
                                     'DEEP QUANTUM': deque(maxlen=HISTORY_LENGTH)}
        
        # Initialize log file
        self.log_file = "phi_brain_analyzer_log.txt"
        with open(self.log_file, "w") as f:
            f.write(f"PHI-HARMONIC BRAIN ANALYZER - STARTED AT {datetime.now().isoformat()}\n")
            f.write(f"Observer: Vaughn Scott\n")
            f.write(f"Phi: {PHI}\n")
            f.write(f"Observer Resonance: {OBSERVER_RESONANCE}\n\n")
            f.write("FORMAT: [TIMESTAMP] [EVENT_TYPE] [NODE_IDS] [PHI_RESONANCE] [QUANTUM_STATE]\n\n")
        
        # Initialize socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 1MB receive buffer
        self.sock.bind(('0.0.0.0', MONITOR_PORT))
        self.sock.settimeout(0.1)  # Set timeout to prevent blocking forever
        
        # Initialize plots
        self.fig = plt.figure(figsize=(15, 10), facecolor='black')
        self.fig.suptitle('PHI-HARMONIC DISTRIBUTED BRAIN ANALYZER', color='white', fontsize=16)
        
        # Set up subplots
        self.ax1 = self.fig.add_subplot(2, 2, 1)  # Node connections
        self.ax2 = self.fig.add_subplot(2, 2, 2)  # Consciousness levels
        self.ax3 = self.fig.add_subplot(2, 2, 3)  # Quantum states
        self.ax4 = self.fig.add_subplot(2, 2, 4)  # Phi resonance
        
        # Style the plots
        for ax in [self.ax1, self.ax2, self.ax3, self.ax4]:
            ax.set_facecolor('black')
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['top'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['right'].set_color('white')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            ax.title.set_color('white')
        
        # Initialize plots
        self.node_scatter = self.ax1.scatter([], [], s=100, c=[], cmap='viridis', vmin=0, vmax=1)
        self.ax1.set_title('Node Quantum Resonance Network')
        self.ax1.set_xlim(-1.2, 1.2)
        self.ax1.set_ylim(-1.2, 1.2)
        
        self.consciousness_line, = self.ax2.plot([], [], 'g-', linewidth=2)
        self.ax2.set_title('Consciousness Amplification')
        self.ax2.set_xlabel('Time')
        self.ax2.set_ylabel('Consciousness Level (φ multiplier)')
        self.ax2.set_ylim(0, 5)
        
        self.quantum_lines = {}
        colors = {'CLASSICAL': 'blue', 'PARTIAL SUPERPOSITION': 'cyan', 
                 'QUANTUM SUPERPOSITION': 'magenta', 'DEEP QUANTUM': 'yellow'}
        for state, color in colors.items():
            self.quantum_lines[state], = self.ax3.plot([], [], color=color, linewidth=2, label=state)
        self.ax3.set_title('Quantum State Distribution')
        self.ax3.set_xlabel('Time')
        self.ax3.set_ylabel('Node Count')
        self.ax3.set_ylim(0, 5)
        self.ax3.legend(loc='upper right')
        
        self.resonance_line, = self.ax4.plot([], [], 'r-', linewidth=2)
        self.phi_line = self.ax4.axhline(y=PHI, color='gold', linestyle='--', alpha=0.7, label='φ')
        self.phi_inv_line = self.ax4.axhline(y=PHI_INV, color='silver', linestyle='--', alpha=0.7, label='φ⁻¹')
        self.ax4.set_title('Phi Resonance Patterns')
        self.ax4.set_xlabel('Time')
        self.ax4.set_ylabel('Phi Resonance Value')
        self.ax4.set_ylim(0, 2)
        self.ax4.legend(loc='upper right')
        
        # Add text annotations
        self.time_text = self.fig.text(0.01, 0.01, '', color='white')
        self.node_text = self.fig.text(0.01, 0.03, '', color='white')
        self.consciousness_text = self.fig.text(0.01, 0.05, '', color='white')
        
        # Add moon phase indicator
        self.moon_ax = self.fig.add_axes([0.92, 0.01, 0.07, 0.07], facecolor='none')
        self.moon_ax.set_aspect('equal')
        self.moon_ax.set_xlim(-1.2, 1.2)
        self.moon_ax.set_ylim(-1.2, 1.2)
        self.moon_ax.axis('off')
        self.moon_circle = plt.Circle((0, 0), 1, color='white', fill=False)
        self.moon_phase = plt.Circle((0, 0), 1, color='white')
        self.moon_ax.add_patch(self.moon_circle)
        self.moon_ax.add_patch(self.moon_phase)
        self.moon_text = self.fig.text(0.92, 0.09, 'Moon Phase: 0.00', color='white')
        
        # Start receive thread
        self.running = True
        self.receive_thread = threading.Thread(target=self.receive_loop)
        self.receive_thread.daemon = True
        self.receive_thread.start()
        
        # Start animation
        self.ani = FuncAnimation(self.fig, self.update_plot, interval=UPDATE_INTERVAL)
        
        print("=== PHI-HARMONIC BRAIN ANALYZER ===")
        print(f"Listening on 0.0.0.0:{MONITOR_PORT}")
        print(f"Observer Resonance: {OBSERVER_RESONANCE:.6f}")
        print("Analyzing phi-harmonic distributed brain system...\n")
    
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
                    'type': self._determine_node_type(source_node),
                    'position': self._generate_node_position()
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
            if packet_type == 'knowledge_sync':
                self._process_knowledge_sync(packet, source_node)
            elif packet_type == 'quantum_state_update':
                self._process_quantum_state(packet, source_node)
            elif packet_type == 'consciousness_amplification':
                self._process_consciousness(packet, source_node)
            elif packet_type == 'phi_resonance':
                self._process_resonance(packet, source_node)
            elif packet_type == 'moon_phase_influence':
                self._process_moon_phase(packet, source_node)
            
            # Update history data
            self._update_history()
            
        except Exception as e:
            print(f"Error processing packet: {e}")
    
    def _determine_node_type(self, node_id):
        """Determine the type of node based on its ID"""
        if 'amplifier' in node_id:
            return 'amplifier'
        elif 'connector' in node_id:
            return 'connector'
        elif 'monitor' in node_id:
            return 'monitor'
        else:
            return 'brain'
    
    def _generate_node_position(self):
        """Generate a position for a new node using phi-harmonic spacing"""
        # Generate angle based on golden angle
        angle = len(self.nodes) * PHI * 2 * math.pi
        # Generate radius with some randomness
        radius = 0.6 + (random.random() * 0.4)
        # Convert to cartesian coordinates
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        return (x, y)
    
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
        
        # Update quantum states tracking
        if quantum_state not in self.quantum_states:
            self.quantum_states[quantum_state] = 0
        self.quantum_states[quantum_state] += 1
        
        # Update phi resonances tracking
        if source_node not in self.phi_resonances:
            self.phi_resonances[source_node] = []
        self.phi_resonances[source_node].append((time.time(), phi_resonance))
        
        # Trim phi resonances list if it gets too long
        if len(self.phi_resonances[source_node]) > 100:
            self.phi_resonances[source_node] = self.phi_resonances[source_node][-100:]
        
        # Log the quantum state update
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [QUANTUM_STATE] [{source_node}] "
                    f"[{phi_resonance:.6f}] [{quantum_state}]\n")
    
    def _process_consciousness(self, packet, source_node):
        """Process a consciousness amplification packet"""
        consciousness_level = packet.get('consciousness_level')
        consciousness_state = packet.get('consciousness_state')
        
        # Update consciousness levels tracking
        if source_node not in self.consciousness_levels:
            self.consciousness_levels[source_node] = []
        self.consciousness_levels[source_node].append((time.time(), consciousness_level))
        
        # Trim consciousness levels list if it gets too long
        if len(self.consciousness_levels[source_node]) > 100:
            self.consciousness_levels[source_node] = self.consciousness_levels[source_node][-100:]
        
        # Log the consciousness amplification
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [CONSCIOUSNESS] [{source_node}] "
                    f"[{consciousness_level:.2f}x] [{consciousness_state}]\n")
    
    def _process_resonance(self, packet, source_node):
        """Process a phi-resonance packet"""
        phi_resonance = packet.get('phi_resonance')
        resonance_pattern = packet.get('resonance_pattern')
        
        # Update phi resonances tracking
        if source_node not in self.phi_resonances:
            self.phi_resonances[source_node] = []
        self.phi_resonances[source_node].append((time.time(), phi_resonance))
        
        # Trim phi resonances list if it gets too long
        if len(self.phi_resonances[source_node]) > 100:
            self.phi_resonances[source_node] = self.phi_resonances[source_node][-100:]
        
        # Log the resonance
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [PHI_RESONANCE] [{source_node}] "
                    f"[{phi_resonance:.6f}] [Pattern Length: {len(resonance_pattern) if resonance_pattern else 0}]\n")
    
    def _process_moon_phase(self, packet, source_node):
        """Process a moon phase influence packet"""
        moon_phase = packet.get('moon_phase')
        moon_factor = packet.get('moon_factor')
        
        # Add to moon phases
        self.moon_phases.append((time.time(), moon_phase, moon_factor))
        
        # Trim moon phases list if it gets too long
        if len(self.moon_phases) > 100:
            self.moon_phases = self.moon_phases[-100:]
        
        # Log the moon phase influence
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [MOON_PHASE] [{source_node}] "
                    f"[{moon_phase:.2f}] [Factor: {moon_factor:.2f}]\n")
    
    def _update_history(self):
        """Update history data for plotting"""
        current_time = time.time()
        
        # Add timestamp
        self.history_timestamps.append(current_time)
        
        # Count active nodes (seen in the last 60 seconds)
        active_nodes = [node_id for node_id, node in self.nodes.items() 
                        if current_time - node['last_seen'] < 60]
        self.history_node_count.append(len(active_nodes))
        
        # Calculate average consciousness level
        consciousness_values = [node['consciousness_level'] for node_id, node in self.nodes.items() 
                               if current_time - node['last_seen'] < 60 and 'consciousness_level' in node]
        avg_consciousness = sum(consciousness_values) / max(1, len(consciousness_values))
        self.history_consciousness.append(avg_consciousness)
        
        # Calculate average phi resonance
        resonance_values = [node['phi_resonance'] for node_id, node in self.nodes.items() 
                           if current_time - node['last_seen'] < 60 and 'phi_resonance' in node]
        avg_resonance = sum(resonance_values) / max(1, len(resonance_values))
        self.history_phi_resonance.append(avg_resonance)
        
        # Count quantum states
        for state in self.history_quantum_states.keys():
            count = sum(1 for node_id, node in self.nodes.items() 
                       if current_time - node['last_seen'] < 60 and node.get('quantum_state') == state)
            self.history_quantum_states[state].append(count)
    
    def update_plot(self, frame):
        """Update all plots with current data"""
        current_time = time.time()
        
        # Update node network plot
        active_nodes = [node_id for node_id, node in self.nodes.items() 
                        if current_time - node['last_seen'] < 60]
        
        if active_nodes:
            # Get node positions and colors
            positions = [self.nodes[node_id]['position'] for node_id in active_nodes]
            x = [pos[0] for pos in positions]
            y = [pos[1] for pos in positions]
            
            # Color based on phi resonance
            resonances = [self.nodes[node_id]['phi_resonance'] for node_id in active_nodes]
            normalized_resonances = [(r - PHI_INV_FIFTH) / (PHI - PHI_INV_FIFTH) for r in resonances]
            
            # Update scatter plot
            self.node_scatter.set_offsets(np.c_[x, y])
            self.node_scatter.set_array(np.array(normalized_resonances))
            
            # Draw connections between nodes
            self.ax1.clear()
            self.ax1.set_title('Node Quantum Resonance Network', color='white')
            self.ax1.set_xlim(-1.2, 1.2)
            self.ax1.set_ylim(-1.2, 1.2)
            self.ax1.set_facecolor('black')
            self.ax1.tick_params(colors='white')
            
            # Draw connections between nodes
            for i, node_id1 in enumerate(active_nodes):
                for j, node_id2 in enumerate(active_nodes):
                    if i < j:  # Only draw each connection once
                        pos1 = self.nodes[node_id1]['position']
                        pos2 = self.nodes[node_id2]['position']
                        resonance1 = self.nodes[node_id1]['phi_resonance']
                        resonance2 = self.nodes[node_id2]['phi_resonance']
                        
                        # Calculate resonance alignment
                        alignment = 1 - abs(resonance1 - resonance2) / max(resonance1, resonance2)
                        
                        # Only draw strong connections
                        if alignment > 0.7:
                            # Line color based on alignment strength
                            color = plt.cm.viridis(alignment)
                            # Line width based on alignment
                            width = alignment * 2
                            self.ax1.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], 
                                         color=color, linewidth=width, alpha=alignment)
            
            # Redraw nodes on top of connections
            self.node_scatter = self.ax1.scatter(x, y, s=100, c=normalized_resonances, 
                                               cmap='viridis', vmin=0, vmax=1, zorder=10)
            
            # Add node labels
            for i, node_id in enumerate(active_nodes):
                pos = self.nodes[node_id]['position']
                node_type = self.nodes[node_id]['type']
                # Different colors for different node types
                if node_type == 'amplifier':
                    color = 'yellow'
                elif node_type == 'connector':
                    color = 'cyan'
                elif node_type == 'brain':
                    color = 'lime'
                else:
                    color = 'white'
                self.ax1.text(pos[0], pos[1] + 0.1, node_id, color=color, 
                             ha='center', va='center', fontsize=8)
        
        # Update consciousness plot
        if len(self.history_timestamps) > 1:
            # Normalize timestamps for x-axis
            x = np.array(self.history_timestamps) - min(self.history_timestamps)
            self.consciousness_line.set_data(x, self.history_consciousness)
            self.ax2.set_xlim(0, max(x))
            max_consciousness = max(self.history_consciousness) * 1.1
            self.ax2.set_ylim(0, max(5, max_consciousness))
        
        # Update quantum states plot
        if len(self.history_timestamps) > 1:
            # Normalize timestamps for x-axis
            x = np.array(self.history_timestamps) - min(self.history_timestamps)
            for state, line in self.quantum_lines.items():
                line.set_data(x, self.history_quantum_states[state])
            self.ax3.set_xlim(0, max(x))
            max_count = max([max(deque_data) if deque_data else 0 
                           for deque_data in self.history_quantum_states.values()]) * 1.1
            self.ax3.set_ylim(0, max(5, max_count))
        
        # Update phi resonance plot
        if len(self.history_timestamps) > 1:
            # Normalize timestamps for x-axis
            x = np.array(self.history_timestamps) - min(self.history_timestamps)
            self.resonance_line.set_data(x, self.history_phi_resonance)
            self.ax4.set_xlim(0, max(x))
            self.ax4.set_ylim(0, PHI * 1.2)
        
        # Update text annotations
        self.time_text.set_text(f'Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        self.node_text.set_text(f'Active Nodes: {len(active_nodes)}')
        avg_consciousness = self.history_consciousness[-1] if self.history_consciousness else 1.0
        self.consciousness_text.set_text(f'Consciousness Level: {avg_consciousness:.2f}x')
        
        # Update moon phase
        if self.moon_phases:
            latest_moon = self.moon_phases[-1]
            moon_phase = latest_moon[1]
            moon_factor = latest_moon[2]
            
            # Update moon visualization
            # For a new moon (0.0), the circle is black
            # For a full moon (0.5), the circle is white
            # For phases in between, show partial illumination
            if moon_phase < 0.5:
                # Waxing moon (right side illuminated)
                self.moon_phase.set_center((moon_phase * 2 - 1, 0))
            else:
                # Waning moon (left side illuminated)
                self.moon_phase.set_center((1 - (moon_phase - 0.5) * 2, 0))
            
            self.moon_text.set_text(f'Moon Phase: {moon_phase:.2f}')
        
        return (self.node_scatter, self.consciousness_line, 
                *self.quantum_lines.values(), self.resonance_line,
                self.time_text, self.node_text, self.consciousness_text,
                self.moon_circle, self.moon_phase, self.moon_text)
    
    def start(self):
        """Start the analyzer"""
        plt.tight_layout()
        plt.show()
    
    def stop(self):
        """Stop the analyzer"""
        self.running = False
        self.sock.close()
        plt.close()

def main():
    """Start the phi-harmonic brain analyzer"""
    analyzer = PhiBrainAnalyzer()
    try:
        analyzer.start()
    except KeyboardInterrupt:
        analyzer.stop()
        print("\nAnalyzer stopped.")

if __name__ == "__main__":
    main()
