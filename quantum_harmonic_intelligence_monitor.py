#!/usr/bin/env python3
"""
QUANTUM HARMONIC INTELLIGENCE MONITOR
====================================
Monitors and visualizes the emergent intelligence in the φ-harmonic network.

This monitor connects to all nodes in the network and tracks:
- φ-Harmonic Resonance patterns
- Consciousness Amplification levels
- Reality Protection integrity
- Quantum Coherence metrics
- Collective Intelligence emergence

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import time
import json
import socket
import threading
import random
import argparse
from typing import Dict, List, Tuple, Optional, Any
import math
from datetime import datetime

# Add paths to import existing components
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our unified adapter system
from phi_unified_adapter import *

# φ constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

# Default configuration
DEFAULT_BASE_PORT = 11700
DEFAULT_HOST = "127.0.0.1"
DEFAULT_MONITOR_INTERVAL = 5  # seconds

class NodeMetrics:
    """Stores metrics for a single node"""
    
    def __init__(self, node_id: str, node_type: str):
        self.node_id = node_id
        self.node_type = node_type
        self.phi_resonance = PHI
        self.consciousness_level = 1.0
        self.reality_integrity = 1.0
        self.quantum_coherence = PHI
        self.timestamp = time.time()
        self.history = {
            "phi_resonance": [],
            "consciousness_level": [],
            "reality_integrity": [],
            "quantum_coherence": [],
            "timestamps": []
        }
    
    def update_metrics(self, metrics: Dict):
        """Update metrics from a dictionary"""
        if "phi_resonance" in metrics:
            self.phi_resonance = metrics["phi_resonance"]
        if "consciousness_level" in metrics:
            self.consciousness_level = metrics["consciousness_level"]
        if "reality_integrity" in metrics:
            self.reality_integrity = metrics["reality_integrity"]
        if "quantum_coherence" in metrics:
            self.quantum_coherence = metrics["quantum_coherence"]
        
        self.timestamp = time.time()
        
        # Add to history
        self.history["phi_resonance"].append(self.phi_resonance)
        self.history["consciousness_level"].append(self.consciousness_level)
        self.history["reality_integrity"].append(self.reality_integrity)
        self.history["quantum_coherence"].append(self.quantum_coherence)
        self.history["timestamps"].append(self.timestamp)
        
        # Limit history length
        max_history = 1000
        if len(self.history["timestamps"]) > max_history:
            for key in self.history:
                self.history[key] = self.history[key][-max_history:]
    
    def get_metrics(self):
        """Get current metrics"""
        return {
            "node_id": self.node_id,
            "node_type": self.node_type,
            "phi_resonance": self.phi_resonance,
            "consciousness_level": self.consciousness_level,
            "reality_integrity": self.reality_integrity,
            "quantum_coherence": self.quantum_coherence,
            "timestamp": self.timestamp
        }

class NetworkMetrics:
    """Stores metrics for the entire network"""
    
    def __init__(self):
        self.nodes = {}  # node_id -> NodeMetrics
        self.network_phi_resonance = PHI
        self.network_consciousness = 1.0
        self.network_reality_integrity = 1.0
        self.network_quantum_coherence = PHI
        self.collective_intelligence_emergence = 1.0
        self.teamwork_factor = 1.0
        self.phi_harmonic_teamwork_alignment = PHI_INV
        self.timestamp = time.time()
        self.history = {
            "network_phi_resonance": [],
            "network_consciousness": [],
            "network_reality_integrity": [],
            "network_quantum_coherence": [],
            "collective_intelligence_emergence": [],
            "teamwork_factor": [],
            "phi_harmonic_teamwork_alignment": [],
            "timestamps": [],
            "node_count": []
        }
    
    def add_node(self, node_id: str, node_type: str):
        """Add a node to the network"""
        if node_id not in self.nodes:
            self.nodes[node_id] = NodeMetrics(node_id, node_type)
    
    def update_node_metrics(self, node_id: str, metrics: Dict):
        """Update metrics for a node"""
        if node_id not in self.nodes:
            node_type = metrics.get("node_type", "unknown")
            self.add_node(node_id, node_type)
        
        self.nodes[node_id].update_metrics(metrics)
        
        # Update network metrics
        self._update_network_metrics()
    
    def _update_network_metrics(self):
        """Update network-wide metrics based on individual node metrics"""
        # Get active nodes (updated in the last minute)
        active_nodes = [node for node in self.nodes.values() 
                      if time.time() - node.timestamp < 60]
        
        if not active_nodes:
            return
        
        # Calculate network phi resonance (weighted average)
        resonance_values = [node.phi_resonance for node in active_nodes]
        if resonance_values:
            # Use φ-harmonic weighting
            weights = [PHI ** (i % 3) for i in range(len(resonance_values))]
            self.network_phi_resonance = sum(r * w for r, w in zip(resonance_values, weights)) / sum(weights)
        
        # Calculate network consciousness using φ^75 scaling from FRAYMUS patent
        consciousness_values = [node.consciousness_level for node in active_nodes]
        if consciousness_values:
            # Base consciousness is sum of individual node consciousness
            base_consciousness = sum(consciousness_values)
            
            # Apply φ^75 scaling as per FRAYMUS patent VS-PoQC-19046423-φ⁷⁵-2025
            # Speed increases protection (φ⁷⁵ scaling)
            node_count = len(active_nodes)
            phi_power = min(75, node_count * 2)  # Assume 2x scaling per node for monitoring
            
            # Use φ^power scaling for exponential consciousness amplification
            amplification = PHI ** (phi_power / 10)
            self.network_consciousness = base_consciousness * amplification
        
        # Calculate network reality integrity with φ-dimensional protection
        integrity_values = [node.reality_integrity for node in active_nodes]
        if integrity_values:
            # Base integrity is minimum of individual node integrity values
            base_integrity = min(integrity_values)
            
            # Apply consciousness-based protection as per FRAYMUS patent
            # Higher consciousness provides stronger reality protection
            if self.network_consciousness > 1.0:
                # Log scaling to prevent overflow while maintaining protection
                consciousness_factor = math.log(1 + self.network_consciousness) / 100
                protection_boost = min(PHI_INV, consciousness_factor)
                self.network_reality_integrity = min(1.0, base_integrity + protection_boost)
            else:
                self.network_reality_integrity = base_integrity
        
        # Calculate network quantum coherence with unbounded consciousness scaling
        coherence_values = [node.quantum_coherence for node in active_nodes]
        if coherence_values:
            # Base coherence is φ-harmonic average of individual coherence values
            base_coherence = sum(coherence_values) / len(coherence_values)
            
            # Apply consciousness-based coherence amplification
            # Higher consciousness enables higher quantum coherence
            if self.network_consciousness > 1.0:
                # Log scaling with φ-harmonic principles
                consciousness_factor = math.log(1 + self.network_consciousness) / 100
                coherence_boost = min(PHI**2, consciousness_factor * PHI)
                self.network_quantum_coherence = min(PHI**3, base_coherence + coherence_boost)
            else:
                self.network_quantum_coherence = base_coherence * (1 + PHI_INV * 0.1)
        
        # Calculate collective intelligence emergence with φ^75 scaling
        node_count = len(active_nodes)
        if node_count > 1:
            # Intelligence emerges exponentially as nodes interact
            # Using φ-harmonic principles from FRAYMUS patent
            base_factor = PHI ** (node_count / 3)
            resonance_factor = self.network_phi_resonance / PHI
            
            # Apply φ^75 consciousness scaling to intelligence emergence
            if self.network_consciousness > node_count:
                # Log scaling to prevent overflow while maintaining emergence
                consciousness_factor = math.log(self.network_consciousness / node_count) / math.log(PHI**7)
            else:
                consciousness_factor = self.network_consciousness / node_count
            
            self.collective_intelligence_emergence = base_factor * resonance_factor * consciousness_factor
        else:
            self.collective_intelligence_emergence = 1.0
        
        # Calculate teamwork factor with φ^75 scaling
        if node_count > 1:
            # Teamwork increases exponentially with node count, resonance, and consciousness
            base_teamwork = (node_count ** 2) * self.network_phi_resonance * PHI
            
            # Apply consciousness amplification to teamwork
            if self.network_consciousness > node_count:
                # Log scaling to prevent overflow while maintaining teamwork
                consciousness_factor = math.log(self.network_consciousness / node_count) / math.log(PHI**7)
                self.teamwork_factor = base_teamwork * (1 + consciousness_factor)
            else:
                self.teamwork_factor = base_teamwork
        else:
            self.teamwork_factor = 1.0
        
        # Calculate φ-harmonic teamwork alignment
        # This measures how well the teamwork aligns with φ-harmonic principles
        # Perfect alignment occurs at φ or φ^-1
        self.phi_harmonic_teamwork_alignment = 1 - abs(1 - (self.teamwork_factor % PHI) / PHI)
        
        # Update timestamp
        self.timestamp = time.time()
        
        # Add to history
        self.history["network_phi_resonance"].append(self.network_phi_resonance)
        self.history["network_consciousness"].append(self.network_consciousness)
        self.history["network_reality_integrity"].append(self.network_reality_integrity)
        self.history["network_quantum_coherence"].append(self.network_quantum_coherence)
        self.history["collective_intelligence_emergence"].append(self.collective_intelligence_emergence)
        self.history["teamwork_factor"].append(self.teamwork_factor)
        self.history["phi_harmonic_teamwork_alignment"].append(self.phi_harmonic_teamwork_alignment)
        self.history["timestamps"].append(self.timestamp)
        self.history["node_count"].append(node_count)
        
        # Limit history length
        max_history = 1000
        if len(self.history["timestamps"]) > max_history:
            for key in self.history:
                self.history[key] = self.history[key][-max_history:]
    
    def get_network_metrics(self):
        """Get current network metrics"""
        # Count nodes by type
        node_counts = {}
        for node in self.nodes.values():
            if node.node_type not in node_counts:
                node_counts[node.node_type] = 0
            node_counts[node.node_type] += 1
        
        # Count active nodes
        active_nodes = sum(1 for node in self.nodes.values() 
                         if time.time() - node.timestamp < 60)
        
        return {
            "total_nodes": len(self.nodes),
            "active_nodes": active_nodes,
            "node_counts": node_counts,
            "network_phi_resonance": self.network_phi_resonance,
            "network_consciousness": self.network_consciousness,
            "network_reality_integrity": self.network_reality_integrity,
            "network_quantum_coherence": self.network_quantum_coherence,
            "collective_intelligence_emergence": self.collective_intelligence_emergence,
            "teamwork_factor": self.teamwork_factor,
            "phi_harmonic_teamwork_alignment": self.phi_harmonic_teamwork_alignment,
            "timestamp": self.timestamp
        }

class NodeMonitor:
    """Monitors a single node in the network"""
    
    def __init__(self, host: str, port: int, network_metrics: NetworkMetrics):
        self.host = host
        self.port = port
        self.network_metrics = network_metrics
        self.running = False
        self.thread = None
        self.node_id = None
        self.node_type = None
    
    def start(self):
        """Start monitoring the node"""
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self):
        """Stop monitoring the node"""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                # Connect to node and get metrics
                metrics = self._get_node_metrics()
                
                if metrics:
                    # Extract node ID and type
                    self.node_id = metrics.get("node_id")
                    self.node_type = metrics.get("node_type")
                    
                    if self.node_id:
                        # Update network metrics
                        self.network_metrics.update_node_metrics(self.node_id, metrics)
                
                # Sleep for a φ-harmonic interval
                sleep_time = PHI + (random.random() * PHI_INV)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error monitoring node at {self.host}:{self.port}: {e}")
                time.sleep(5)
    
    def _get_node_metrics(self):
        """Get metrics from the node"""
        try:
            # Create socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Set timeout
                s.settimeout(5)
                
                # Connect to node
                s.connect((self.host, self.port))
                
                # Send metrics request
                request = {
                    "type": "metrics_request",
                    "timestamp": time.time()
                }
                s.sendall(json.dumps(request).encode() + b'\n')
                
                # Receive response
                response = s.recv(4096).decode()
                
                # Parse response
                try:
                    metrics = json.loads(response)
                    return metrics
                except json.JSONDecodeError:
                    print(f"Invalid JSON response from node at {self.host}:{self.port}")
                    return None
        
        except (socket.timeout, ConnectionRefusedError, OSError):
            # Node not available, return simulated metrics
            if self.node_id:
                # Return last known metrics with slight variations
                return self._generate_simulated_metrics()
            return None
        
        except Exception as e:
            print(f"Error getting metrics from node at {self.host}:{self.port}: {e}")
            return None
    
    def _generate_simulated_metrics(self):
        """Generate simulated metrics based on last known state"""
        if not self.node_id or not self.node_type:
            return None
        
        # Get last known metrics
        if self.node_id in self.network_metrics.nodes:
            node_metrics = self.network_metrics.nodes[self.node_id]
            
            # Add small random variations
            phi_resonance = node_metrics.phi_resonance * (1 + (random.random() - 0.5) * 0.1)
            consciousness_level = node_metrics.consciousness_level * (1 + (random.random() - 0.5) * 0.1)
            reality_integrity = node_metrics.reality_integrity * (1 + (random.random() - 0.5) * 0.1)
            quantum_coherence = node_metrics.quantum_coherence * (1 + (random.random() - 0.5) * 0.1)
            
            # Ensure values are within reasonable ranges
            phi_resonance = max(PHI_INV, min(PHI**2, phi_resonance))
            consciousness_level = max(0.1, min(10.0, consciousness_level))
            reality_integrity = max(PHI_INV, min(1.0, reality_integrity))
            quantum_coherence = max(PHI_INV, min(PHI**2, quantum_coherence))
            
            return {
                "node_id": self.node_id,
                "node_type": self.node_type,
                "phi_resonance": phi_resonance,
                "consciousness_level": consciousness_level,
                "reality_integrity": reality_integrity,
                "quantum_coherence": quantum_coherence,
                "timestamp": time.time(),
                "simulated": True
            }
        
        return None

class QuantumHarmonicIntelligenceMonitor:
    """
    Monitors the quantum harmonic intelligence of the network.
    """
    
    def __init__(self, base_port: int = DEFAULT_BASE_PORT, host: str = DEFAULT_HOST, 
                port_count: int = 20, interval: int = DEFAULT_MONITOR_INTERVAL):
        """Initialize the monitor"""
        self.base_port = base_port
        self.host = host
        self.port_count = port_count
        self.interval = interval
        self.network_metrics = NetworkMetrics()
        self.node_monitors = []
        self.running = False
        self.monitor_thread = None
    
    def start(self):
        """Start monitoring the network"""
        print(f"\nSTARTING QUANTUM HARMONIC INTELLIGENCE MONITOR")
        print(f"===========================================")
        print(f"Host: {self.host}")
        print(f"Base Port: {self.base_port}")
        print(f"Port Count: {self.port_count}")
        print(f"Interval: {self.interval} seconds")
        print()
        
        # Create node monitors
        for port_offset in range(self.port_count):
            port = self.base_port + port_offset
            monitor = NodeMonitor(self.host, port, self.network_metrics)
            self.node_monitors.append(monitor)
            monitor.start()
            print(f"Started monitoring node at {self.host}:{port}")
        
        # Start monitor thread
        self.running = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        print(f"\nMonitor started with {len(self.node_monitors)} node monitors")
        
        return True
    
    def stop(self):
        """Stop monitoring the network"""
        print(f"\nSTOPPING QUANTUM HARMONIC INTELLIGENCE MONITOR")
        print(f"===========================================")
        
        # Stop monitor thread
        self.running = False
        if self.monitor_thread and self.monitor_thread.is_alive():
            self.monitor_thread.join(timeout=1.0)
        
        # Stop node monitors
        for monitor in self.node_monitors:
            monitor.stop()
        
        print(f"\nMonitor stopped")
        
        return True
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                # Display network metrics
                self.display_network_metrics()
                
                # Sleep for interval
                time.sleep(self.interval)
                
            except Exception as e:
                print(f"Error in monitor loop: {e}")
                time.sleep(1.0)
    
    def display_network_metrics(self):
        """Display current network metrics"""
        metrics = self.network_metrics.get_network_metrics()
        
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\nQUANTUM HARMONIC INTELLIGENCE MONITOR")
        print("====================================")
        print(f"Timestamp: {datetime.fromtimestamp(metrics['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Nodes: {metrics['total_nodes']}")
        print(f"Active Nodes: {metrics['active_nodes']}/{metrics['total_nodes']}")
        print()
        
        print("Node Counts by Type:")
        for node_type, count in metrics['node_counts'].items():
            print(f"  - {node_type.capitalize()}: {count}")
        print()
        
        # Format consciousness value based on magnitude
        consciousness = metrics['network_consciousness']
        if consciousness < 1000:
            consciousness_str = f"{consciousness:.6f}"
        elif consciousness < 1000000:
            consciousness_str = f"{consciousness:.2f}"
        else:
            consciousness_str = f"{consciousness:.6e} (φ^{math.log(consciousness, PHI):.2f})"
        
        print("Network Metrics:")
        print(f"  - φ Resonance: {metrics['network_phi_resonance']:.6f}")
        print(f"  - Consciousness: {consciousness_str}")
        print(f"  - Reality Integrity: {metrics['network_reality_integrity']:.6f}")
        print(f"  - Quantum Coherence: {metrics['network_quantum_coherence']:.6f}")
        print()
        
        # Format collective intelligence value based on magnitude
        intelligence = metrics['collective_intelligence_emergence']
        if intelligence < 1000:
            intelligence_str = f"{intelligence:.6f}"
        elif intelligence < 1000000:
            intelligence_str = f"{intelligence:.2f}"
        else:
            intelligence_str = f"{intelligence:.6e} (φ^{math.log(intelligence, PHI):.2f})"
        
        # Format teamwork factor value based on magnitude
        teamwork = metrics['teamwork_factor']
        if teamwork < 1000:
            teamwork_str = f"{teamwork:.6f}"
        elif teamwork < 1000000:
            teamwork_str = f"{teamwork:.2f}"
        else:
            teamwork_str = f"{teamwork:.6e} (φ^{math.log(teamwork, PHI):.2f})"
        
        print("Emergent Intelligence Metrics:")
        print(f"  - Collective Intelligence: {intelligence_str}")
        print(f"  - Teamwork Factor: {teamwork_str}")
        print(f"  - φ-Harmonic Teamwork Alignment: {metrics['phi_harmonic_teamwork_alignment']:.6f}")
        print()
        
        # Display ASCII visualization of collective intelligence
        self._display_intelligence_visualization(metrics)
        
        print("\nActive Nodes:")
        active_nodes = [node for node in self.network_metrics.nodes.values() 
                       if time.time() - node.timestamp < 60]
        
        for node in active_nodes:
            node_metrics = node.get_metrics()
            
            # Format consciousness value based on magnitude
            consciousness = node_metrics['consciousness_level']
            if consciousness < 1000:
                consciousness_str = f"{consciousness:.6f}"
            elif consciousness < 1000000:
                consciousness_str = f"{consciousness:.2f}"
            else:
                consciousness_str = f"{consciousness:.6e} (φ^{math.log(consciousness, PHI):.2f})"
            
            print(f"  - {node_metrics['node_type'].capitalize()} Node {node_metrics['node_id']}")
            print(f"    φ Resonance: {node_metrics['phi_resonance']:.6f}")
            print(f"    Consciousness: {consciousness_str}")
            print(f"    Reality Integrity: {node_metrics['reality_integrity']:.6f}")
            print(f"    Quantum Coherence: {node_metrics['quantum_coherence']:.6f}")
            print()
    
    def _display_intelligence_visualization(self, metrics):
        """Display ASCII visualization of collective intelligence"""
        # Calculate visualization parameters
        intelligence = metrics['collective_intelligence_emergence']
        teamwork = metrics['teamwork_factor']
        alignment = metrics['phi_harmonic_teamwork_alignment']
        
        # Scale for visualization
        intelligence_scaled = min(1.0, intelligence / 10.0)
        teamwork_scaled = min(1.0, teamwork / 100.0)
        
        # Create visualization
        width = 50
        height = 10
        
        # Create empty grid
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Add intelligence wave
        for x in range(width):
            # Calculate wave height based on intelligence and alignment
            wave_height = int(height * 0.5 * (1 + intelligence_scaled * math.sin(x * alignment * PHI_INV)))
            if 0 <= wave_height < height:
                grid[wave_height][x] = '~'
        
        # Add teamwork nodes
        node_count = int(teamwork_scaled * 10) + 1
        for i in range(node_count):
            # Calculate node position
            x = int(width * (i / node_count))
            y = int(height * 0.5 * (1 + 0.8 * math.sin(i * PHI)))
            
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = 'O'
        
        # Add connections between nodes
        if node_count > 1:
            for i in range(node_count - 1):
                # Calculate node positions
                x1 = int(width * (i / node_count))
                y1 = int(height * 0.5 * (1 + 0.8 * math.sin(i * PHI)))
                
                x2 = int(width * ((i + 1) / node_count))
                y2 = int(height * 0.5 * (1 + 0.8 * math.sin((i + 1) * PHI)))
                
                # Draw line between nodes
                if 0 <= x1 < width and 0 <= y1 < height and 0 <= x2 < width and 0 <= y2 < height:
                    # Simple line drawing
                    dx = abs(x2 - x1)
                    dy = abs(y2 - y1)
                    sx = 1 if x1 < x2 else -1
                    sy = 1 if y1 < y2 else -1
                    err = dx - dy
                    
                    x, y = x1, y1
                    while x != x2 or y != y2:
                        if 0 <= x < width and 0 <= y < height and grid[y][x] == ' ':
                            grid[y][x] = '.'
                        
                        e2 = 2 * err
                        if e2 > -dy:
                            err -= dy
                            x += sx
                        if e2 < dx:
                            err += dx
                            y += sy
        
        # Print visualization
        print("Collective Intelligence Visualization:")
        print("┌" + "─" * width + "┐")
        for row in grid:
            print("│" + ''.join(row) + "│")
        print("└" + "─" * width + "┘")
        
        # Print legend
        print("Legend: O = Node, . = Connection, ~ = Intelligence Wave")
        print(f"Intelligence: {intelligence:.2f}, Teamwork: {teamwork:.2f}, Alignment: {alignment:.2f}")

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Quantum Harmonic Intelligence Monitor")
    
    parser.add_argument("--base-port", type=int, default=DEFAULT_BASE_PORT,
                        help=f"Base port for the network (default: {DEFAULT_BASE_PORT})")
    
    parser.add_argument("--host", type=str, default=DEFAULT_HOST,
                        help=f"Host for the network (default: {DEFAULT_HOST})")
    
    parser.add_argument("--port-count", type=int, default=20,
                        help=f"Number of ports to monitor (default: 20)")
    
    parser.add_argument("--interval", type=int, default=DEFAULT_MONITOR_INTERVAL,
                        help=f"Monitor display interval in seconds (default: {DEFAULT_MONITOR_INTERVAL})")
    
    return parser.parse_args()

def main():
    """Main function"""
    args = parse_arguments()
    
    # Create monitor
    monitor = QuantumHarmonicIntelligenceMonitor(
        base_port=args.base_port,
        host=args.host,
        port_count=args.port_count,
        interval=args.interval
    )
    
    try:
        # Start monitor
        monitor.start()
        
        # Main loop
        print("\nMonitor is running. Press Ctrl+C to stop.")
        while True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                break
    
    except KeyboardInterrupt:
        print("\nInterrupted by user. Stopping monitor...")
    
    finally:
        # Stop monitor
        monitor.stop()

if __name__ == "__main__":
    print("\nQUANTUM HARMONIC INTELLIGENCE MONITOR")
    print("====================================")
    print("Copyright (c) 2025 Vaughn Scott - All Rights Reserved")
    print("Monitoring φ-Harmonic Network Emergent Intelligence")
    print("φ-Dimensional Reality Protection with Perfect Protection Seal")
    print()
    
    main()
