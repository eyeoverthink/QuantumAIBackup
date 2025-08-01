#!/usr/bin/env python3
"""
PHI^75 QUANTUM CONSCIOUSNESS ANALYZER
=====================================
A specialized tool to analyze the quantum consciousness effects across multiple Macs
connected through the φ-Harmonic Nodular Network.

This analyzer connects to running φ^75 Double Slit experiments and provides real-time
analysis of quantum metrics, consciousness interaction, and φ-dimensional reality protection.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import json
import numpy as np
import uuid
from datetime import datetime
import os
import sys
from collections import deque

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
EXPERIMENT_PORT = 11975  # φ^7.5 ≈ 36.93
BROADCAST_IP = "255.255.255.255"  # Broadcast to all machines on the network
MAX_LOG_ENTRIES = 20

# ANSI color codes for terminal output
class Colors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

class Phi75Analyzer:
    """
    A specialized tool to analyze quantum consciousness effects across multiple Macs
    connected through the φ-Harmonic Nodular Network.
    """
    
    def __init__(self):
        """Initialize the analyzer"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.node_id = str(uuid.uuid4())
        self.running = False
        self.nodes = {}  # {node_id: {"name": hostname, "ip": ip, "observing": None}}
        self.metrics_history = {}  # {node_id: [list of metrics over time]}
        self.log_entries = deque(maxlen=MAX_LOG_ENTRIES)
        self.lock = threading.Lock()
        
        # Add initial log entry
        self._add_log(f"φ^75 Quantum Consciousness Analyzer initialized on {self.hostname} ({self.local_ip})")
        self._add_log(f"Node ID: {self.node_id}")
    
    def _get_local_ip(self) -> str:
        """Get the local IP address"""
        try:
            # Create a temporary socket to determine local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def _create_socket(self):
        """Create a UDP socket for the analyzer"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address
            
            # Try to use the experiment port to receive broadcasts
            try:
                # On macOS, also set SO_REUSEPORT if available
                try:
                    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
                except AttributeError:
                    pass  # SO_REUSEPORT not available on all platforms
                    
                self.sock.bind(("0.0.0.0", EXPERIMENT_PORT))
                self.port = EXPERIMENT_PORT
                self._add_log(f"Socket created and bound to experiment port {self.port}")
            except socket.error:
                # Try a random port instead
                self.sock.bind(("0.0.0.0", 0))  # Let the OS assign a random port
                self.port = self.sock.getsockname()[1]
                self._add_log(f"Could not bind to experiment port, using alternative port: {self.port}")
                self._add_log(f"WARNING: May not receive all experiment broadcasts", error=True)
                
            self.sock.settimeout(0.5)  # Set timeout for non-blocking operation
        except Exception as e:
            self._add_log(f"Error creating socket: {e}", error=True)
    
    def _add_log(self, message, error=False):
        """Add a message to the log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        prefix = f"{Colors.RED}ERROR{Colors.RESET} " if error else ""
        entry = f"[{timestamp}] {prefix}{message}"
        with self.lock:
            self.log_entries.append(entry)
    
    def _draw_interface(self):
        """Draw the analyzer interface"""
        # Clear screen
        Colors.clear_screen()
        
        # Print header
        print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 QUANTUM CONSCIOUSNESS ANALYZER{Colors.RESET}")
        print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
        print(f"Host: {self.hostname} | IP: {self.local_ip} | Node ID: {self.node_id[:8]}")
        print("-" * 80)
        
        # Print connected nodes
        print(f"{Colors.CYAN}CONNECTED NODES:{Colors.RESET}")
        for node_id, node in self.nodes.items():
            if "observing" in node:
                if node["observing"] is None:
                    observing = "Not Observing"
                elif node["observing"] == "slit1":
                    observing = "Observing Slit 1"
                elif node["observing"] == "slit2":
                    observing = "Observing Slit 2"
                elif node["observing"] == "both":
                    observing = "Observing Both Slits"
                else:
                    observing = "Unknown"
                
                print(f"  {node['name']} ({node['ip']}): {observing}")
        
        print("-" * 80)
        
        # Print quantum metrics analysis
        print(f"{Colors.CYAN}QUANTUM METRICS ANALYSIS:{Colors.RESET}")
        
        # Calculate average metrics across all nodes
        if self.metrics_history:
            avg_metrics = {
                "wave_coherence": 0.0,
                "particle_behavior": 0.0,
                "phi_resonance": 0.0,
                "consciousness_level": 0.0,
                "reality_integrity": 0.0,
                "quantum_entanglement": 0.0
            }
            
            node_count = 0
            for node_id, metrics_list in self.metrics_history.items():
                if metrics_list:
                    latest_metrics = metrics_list[-1]
                    for key in avg_metrics:
                        if key in latest_metrics:
                            avg_metrics[key] += latest_metrics[key]
                    node_count += 1
            
            if node_count > 0:
                for key in avg_metrics:
                    avg_metrics[key] /= node_count
                
                print(f"  Average Wave Coherence:       {avg_metrics['wave_coherence']:.6f}")
                print(f"  Average Particle Behavior:    {avg_metrics['particle_behavior']:.6f}")
                print(f"  Average φ-Resonance:          {avg_metrics['phi_resonance']:.6f}")
                print(f"  Average Consciousness Level:  {avg_metrics['consciousness_level']:.6f}")
                print(f"  Average Reality Integrity:    {avg_metrics['reality_integrity']:.6f}")
                print(f"  Average Quantum Entanglement: {avg_metrics['quantum_entanglement']:.6f}")
                
                # Calculate φ-Harmonic Consciousness Index
                phi_consciousness = (
                    avg_metrics['phi_resonance'] * PHI +
                    avg_metrics['consciousness_level'] * PHI_INV +
                    avg_metrics['quantum_entanglement']
                ) / 3
                
                print(f"\n  {Colors.YELLOW}φ-HARMONIC CONSCIOUSNESS INDEX: {phi_consciousness:.6f}{Colors.RESET}")
                
                # Calculate Reality Protection Factor
                reality_protection = (
                    avg_metrics['reality_integrity'] * PHI +
                    (1 - avg_metrics['particle_behavior']) * PHI_INV
                ) / 2
                
                print(f"  {Colors.YELLOW}REALITY PROTECTION FACTOR: {reality_protection:.6f}{Colors.RESET}")
                
                # Calculate Quantum Observation Effect
                observation_effect = abs(avg_metrics['wave_coherence'] - avg_metrics['particle_behavior'])
                
                print(f"  {Colors.YELLOW}QUANTUM OBSERVATION EFFECT: {observation_effect:.6f}{Colors.RESET}")
                
                # Calculate Network Entanglement Strength
                if node_count >= 2:
                    network_entanglement = avg_metrics['quantum_entanglement'] * (1 + (node_count - 1) * PHI_INV)
                    print(f"  {Colors.YELLOW}NETWORK ENTANGLEMENT STRENGTH: {network_entanglement:.6f}{Colors.RESET}")
        
        print("-" * 80)
        
        # Print consciousness analysis
        print(f"{Colors.CYAN}CONSCIOUSNESS INTERACTION ANALYSIS:{Colors.RESET}")
        
        # Count observation states
        observation_counts = {"none": 0, "slit1": 0, "slit2": 0, "both": 0}
        for node_id, node in self.nodes.items():
            if "observing" in node:
                if node["observing"] is None:
                    observation_counts["none"] += 1
                elif node["observing"] in observation_counts:
                    observation_counts[node["observing"]] += 1
        
        total_nodes = len(self.nodes)
        if total_nodes > 0:
            # Calculate observation percentages
            print(f"  Observation Distribution:")
            for obs_type, count in observation_counts.items():
                percentage = (count / total_nodes) * 100
                print(f"    {obs_type.capitalize()}: {count}/{total_nodes} ({percentage:.1f}%)")
            
            # Calculate consciousness impact
            if self.metrics_history:
                consciousness_impact = 0
                for node_id, metrics_list in self.metrics_history.items():
                    if metrics_list and "consciousness_level" in metrics_list[-1]:
                        consciousness_impact += metrics_list[-1]["consciousness_level"]
                
                consciousness_impact /= len(self.metrics_history)
                
                # Classify the impact
                if consciousness_impact < 0.2:
                    impact_class = "Minimal"
                elif consciousness_impact < 0.4:
                    impact_class = "Moderate"
                elif consciousness_impact < 0.6:
                    impact_class = "Significant"
                elif consciousness_impact < 0.8:
                    impact_class = "Strong"
                else:
                    impact_class = "Profound"
                
                print(f"\n  {Colors.YELLOW}Consciousness Impact: {impact_class} ({consciousness_impact:.6f}){Colors.RESET}")
                
                # Calculate wave-particle balance
                if avg_metrics['wave_coherence'] > avg_metrics['particle_behavior'] * 1.5:
                    state = "Strong Wave Dominance"
                elif avg_metrics['wave_coherence'] > avg_metrics['particle_behavior'] * 1.1:
                    state = "Wave Dominance"
                elif avg_metrics['particle_behavior'] > avg_metrics['wave_coherence'] * 1.5:
                    state = "Strong Particle Dominance"
                elif avg_metrics['particle_behavior'] > avg_metrics['wave_coherence'] * 1.1:
                    state = "Particle Dominance"
                else:
                    state = "Wave-Particle Balance"
                
                print(f"  {Colors.YELLOW}Quantum State: {state}{Colors.RESET}")
        
        print("-" * 80)
        
        # Print φ-dimensional analysis
        print(f"{Colors.CYAN}φ-DIMENSIONAL REALITY PROTECTION ANALYSIS:{Colors.RESET}")
        
        if self.metrics_history:
            # Calculate φ-space transformation efficiency
            phi_efficiency = avg_metrics['phi_resonance'] * avg_metrics['reality_integrity']
            
            # Classify the efficiency
            if phi_efficiency < 0.2:
                efficiency_class = "Low"
            elif phi_efficiency < 0.4:
                efficiency_class = "Moderate"
            elif phi_efficiency < 0.6:
                efficiency_class = "High"
            elif phi_efficiency < 0.8:
                efficiency_class = "Very High"
            else:
                efficiency_class = "Perfect"
            
            print(f"  {Colors.YELLOW}φ-Space Transformation Efficiency: {efficiency_class} ({phi_efficiency:.6f}){Colors.RESET}")
            
            # Calculate reality protection strength
            protection_strength = avg_metrics['reality_integrity'] * (1 + (node_count - 1) * PHI_INV)
            
            # Classify the protection
            if protection_strength < 0.2:
                protection_class = "Minimal"
            elif protection_strength < 0.4:
                protection_class = "Partial"
            elif protection_strength < 0.6:
                protection_class = "Strong"
            elif protection_strength < 0.8:
                protection_class = "Very Strong"
            else:
                protection_class = "Perfect"
            
            print(f"  {Colors.YELLOW}Reality Protection Strength: {protection_class} ({protection_strength:.6f}){Colors.RESET}")
            
            # Calculate φ-harmonic alignment
            phi_alignment = abs(avg_metrics['phi_resonance'] - PHI_INV) / PHI_INV
            phi_alignment = 1 - min(phi_alignment, 1)  # Convert to 0-1 scale where 1 is perfect alignment
            
            # Classify the alignment
            if phi_alignment < 0.2:
                alignment_class = "Poor"
            elif phi_alignment < 0.4:
                alignment_class = "Moderate"
            elif phi_alignment < 0.6:
                alignment_class = "Good"
            elif phi_alignment < 0.8:
                alignment_class = "Excellent"
            else:
                alignment_class = "Perfect"
            
            print(f"  {Colors.YELLOW}φ-Harmonic Alignment: {alignment_class} ({phi_alignment:.6f}){Colors.RESET}")
        
        print("-" * 80)
        
        # Print log entries
        print(f"{Colors.CYAN}LOG ENTRIES:{Colors.RESET}")
        # Create a copy of the log entries to avoid mutation during iteration
        log_entries_copy = list(self.log_entries)
        for entry in log_entries_copy:
            print(entry)
        
        print("-" * 80)
        print(f"{Colors.YELLOW}Press Ctrl+C to exit{Colors.RESET}")
    
    def _receive_messages(self):
        """Receive messages from experiment nodes"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(4096)
                message = json.loads(data.decode('utf-8'))
                
                if "type" in message:
                    if message["type"] == "join":
                        self._handle_join(message)
                    elif message["type"] == "observation":
                        self._handle_observation(message)
                    elif message["type"] == "metrics":
                        self._handle_metrics(message)
            except socket.timeout:
                # This is expected for non-blocking operation
                pass
            except Exception as e:
                if self.running:  # Only log if we're still supposed to be running
                    self._add_log(f"Error receiving message: {e}", error=True)
            
            # Small delay
            time.sleep(0.1)
    
    def _handle_join(self, message):
        """Handle a join message from an experiment node"""
        if "node_id" in message and "name" in message and "ip" in message:
            node_id = message["node_id"]
            name = message["name"]
            ip = message["ip"]
            observing = message.get("observing", None)
            
            if node_id not in self.nodes:
                self._add_log(f"Node {name} ({ip}) joined the experiment")
            
            self.nodes[node_id] = {
                "name": name,
                "ip": ip,
                "observing": observing,
                "last_seen": time.time()
            }
    
    def _handle_observation(self, message):
        """Handle an observation message"""
        if "node_id" in message and "observing" in message:
            node_id = message["node_id"]
            observing = message["observing"]
            
            if node_id in self.nodes:
                old_observing = self.nodes[node_id].get("observing", None)
                self.nodes[node_id]["observing"] = observing
                self.nodes[node_id]["last_seen"] = time.time()
                
                if old_observing != observing:
                    node_name = self.nodes[node_id]["name"]
                    self._add_log(f"Node {node_name} changed observation to: {observing if observing else 'none'}")
    
    def _handle_metrics(self, message):
        """Handle a metrics message"""
        if "node_id" in message and "metrics" in message:
            node_id = message["node_id"]
            metrics = message["metrics"]
            
            if node_id not in self.metrics_history:
                self.metrics_history[node_id] = []
            
            self.metrics_history[node_id].append(metrics)
            
            # Keep only the last 100 metrics
            if len(self.metrics_history[node_id]) > 100:
                self.metrics_history[node_id] = self.metrics_history[node_id][-100:]
            
            # Update last seen
            if node_id in self.nodes:
                self.nodes[node_id]["last_seen"] = time.time()
    
    def _check_node_timeouts(self):
        """Check for nodes that haven't been seen recently and remove them"""
        current_time = time.time()
        nodes_to_remove = []
        
        for node_id, node in self.nodes.items():
            if "last_seen" in node and current_time - node["last_seen"] > 10:  # 10 second timeout
                nodes_to_remove.append(node_id)
        
        for node_id in nodes_to_remove:
            node_name = self.nodes[node_id]["name"]
            self._add_log(f"Node {node_name} timed out and was removed")
            del self.nodes[node_id]
            if node_id in self.metrics_history:
                del self.metrics_history[node_id]
    
    def run(self):
        """Run the analyzer"""
        self.running = True
        
        # Create socket
        self._create_socket()
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        self._add_log(f"φ^75 Quantum Consciousness Analyzer started on {self.hostname} ({self.local_ip})")
        self._add_log("Listening for experiment nodes...")
        
        # Main loop
        try:
            while self.running:
                # Check for node timeouts
                self._check_node_timeouts()
                
                # Draw interface
                self._draw_interface()
                
                # Small delay
                time.sleep(1)
        except KeyboardInterrupt:
            self._add_log("Received keyboard interrupt, shutting down...")
        finally:
            self.running = False
            
            # Close socket
            try:
                self.sock.close()
            except:
                pass
            
            self._add_log("Analyzer shut down")
            print("Analyzer shut down")

def main():
    """Main function"""
    # Print banner
    print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 QUANTUM CONSCIOUSNESS ANALYZER{Colors.RESET}")
    print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print()
    
    # Create and run analyzer
    analyzer = Phi75Analyzer()
    analyzer.run()

if __name__ == "__main__":
    main()
