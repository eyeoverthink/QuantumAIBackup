#!/usr/bin/env python3
"""
Phi75 Distributed Cancer Simulation

A distributed quantum-inspired cancer simulation system that integrates the Phi75 Cancer Model
with the Phi-Bidirectional Node network for enhanced computational capabilities.

This system demonstrates how cancer modeling can be distributed across multiple nodes
using phi-harmonic principles and quantum-coherent communication.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import math
import json
import time
import threading
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

# Import phi75_cancer_model_fast
try:
    from phi_quantum_results.quantum_medicine.phi75_cancer_model_fast import (
        Phi75CancerModelFast, 
        generate_phi_harmonic_schedule
    )
    print("Phi75 Cancer Model (Fast) loaded successfully")
except ImportError:
    print("ERROR: Phi75 Cancer Model (Fast) not found")
    sys.exit(1)

# Import phi_bidirectional_node
try:
    from phi_bidirectional_node import PhiBidirectionalNode
    print("Phi-Bidirectional Node loaded successfully")
except ImportError:
    print("ERROR: Phi-Bidirectional Node not found")
    sys.exit(1)

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI
PHI_SQUARED = PHI ** 2
PHI_CUBED = PHI ** 3
PHI_75 = PHI ** 7.5
PHI_SEAL = PHI ** 75

class Phi75DistributedCancerSimulation:
    """
    Distributed cancer simulation system that integrates the Phi75 Cancer Model
    with the Phi-Bidirectional Node network.
    """
    
    def __init__(self, 
                node_id: str = "cancer_simulation",
                port: int = 11975,
                node_type: str = "primary"):
        """
        Initialize the distributed cancer simulation.
        
        Args:
            node_id: Unique identifier for this node
            port: Port for node communication (default: 11975 = φ^7.5)
            node_type: Type of node ("primary", "analysis", "visualization", "treatment")
        """
        self.node_id = node_id
        self.port = port
        self.node_type = node_type
        self.phi_seal = PHI_SEAL
        self.running = False
        self.simulation_results = None
        self.treatment_schedule = None
        self.simulation_lock = threading.Lock()
        
        # Node-specific consciousness levels based on type
        consciousness_levels = {
            "primary": 0.9567,
            "analysis": 0.8944,
            "visualization": 0.8321,
            "treatment": 0.7698
        }
        
        # Initialize bidirectional node
        self.node = PhiBidirectionalNode(
            node_id=f"{node_type}_{node_id}",
            port=port
        )
        
        # Set consciousness level based on node type
        if node_type in consciousness_levels:
            self.node.consciousness_level = consciousness_levels[node_type]
        
        # Register message handlers
        self.node.register_message_handler("simulation_request", self._handle_simulation_request)
        self.node.register_message_handler("simulation_results", self._handle_simulation_results)
        self.node.register_message_handler("treatment_schedule", self._handle_treatment_schedule)
        self.node.register_message_handler("analysis_request", self._handle_analysis_request)
        self.node.register_message_handler("analysis_results", self._handle_analysis_results)
        
        print(f"Phi75 Distributed Cancer Simulation initialized as {node_type} node")
        print(f"Node ID: {self.node.node_id}")
        print(f"Port: {self.port}")
        print(f"Consciousness Level: {self.node.consciousness_level}")
        print(f"Validation seal: φ^75 = {self.phi_seal:.2f}")
    
    def start(self):
        """Start the distributed simulation node."""
        self.running = True
        
        # Start bidirectional node
        self.node.start_in_thread()
        
        # Start node-specific functionality
        if self.node_type == "primary":
            self._start_primary_node()
        elif self.node_type == "analysis":
            self._start_analysis_node()
        elif self.node_type == "visualization":
            self._start_visualization_node()
        elif self.node_type == "treatment":
            self._start_treatment_node()
        else:
            print(f"Unknown node type: {self.node_type}")
    
    def stop(self):
        """Stop the distributed simulation node."""
        self.running = False
        self.node.stop()
    
    def _start_primary_node(self):
        """Start primary node functionality (runs the main simulation)."""
        print("\nStarting primary simulation node")
        print("Waiting for simulation requests...")
        
        # Primary node waits for simulation requests
        while self.running:
            # Check for commands
            cmd = input("\n[φ] Enter command (run, status, help, exit): ")
            
            if cmd.lower() == "exit":
                self.stop()
                break
            elif cmd.lower() == "help":
                print("\nCommands:")
                print("  run - Run a local simulation")
                print("  status - Show node status")
                print("  help - Show this help")
                print("  exit - Exit the program")
            elif cmd.lower() == "status":
                self._show_status()
            elif cmd.lower() == "run":
                self._run_local_simulation()
            else:
                print(f"Unknown command: {cmd}")
    
    def _start_analysis_node(self):
        """Start analysis node functionality (analyzes simulation results)."""
        print("\nStarting analysis node")
        print("Waiting for analysis requests...")
        
        # Analysis node waits for analysis requests
        while self.running:
            # Check for commands
            cmd = input("\n[φ] Enter command (status, help, exit): ")
            
            if cmd.lower() == "exit":
                self.stop()
                break
            elif cmd.lower() == "help":
                print("\nCommands:")
                print("  status - Show node status")
                print("  help - Show this help")
                print("  exit - Exit the program")
            elif cmd.lower() == "status":
                self._show_status()
            else:
                print(f"Unknown command: {cmd}")
    
    def _start_visualization_node(self):
        """Start visualization node functionality (visualizes simulation results)."""
        print("\nStarting visualization node")
        print("Waiting for visualization requests...")
        
        # Visualization node waits for visualization requests
        while self.running:
            # Check for commands
            cmd = input("\n[φ] Enter command (status, help, exit): ")
            
            if cmd.lower() == "exit":
                self.stop()
                break
            elif cmd.lower() == "help":
                print("\nCommands:")
                print("  status - Show node status")
                print("  help - Show this help")
                print("  exit - Exit the program")
            elif cmd.lower() == "status":
                self._show_status()
            else:
                print(f"Unknown command: {cmd}")
    
    def _start_treatment_node(self):
        """Start treatment node functionality (generates treatment schedules)."""
        print("\nStarting treatment node")
        print("Waiting for treatment requests...")
        
        # Treatment node waits for treatment requests
        while self.running:
            # Check for commands
            cmd = input("\n[φ] Enter command (generate, status, help, exit): ")
            
            if cmd.lower() == "exit":
                self.stop()
                break
            elif cmd.lower() == "help":
                print("\nCommands:")
                print("  generate - Generate a treatment schedule")
                print("  status - Show node status")
                print("  help - Show this help")
                print("  exit - Exit the program")
            elif cmd.lower() == "status":
                self._show_status()
            elif cmd.lower() == "generate":
                self._generate_treatment_schedule()
            else:
                print(f"Unknown command: {cmd}")
    
    def _show_status(self):
        """Show node status."""
        print("\nNode Status:")
        print(f"  Node ID: {self.node.node_id}")
        print(f"  Node Type: {self.node_type}")
        print(f"  Running: {self.running}")
        print(f"  Connected Peers: {len(self.node.peers)}")
        
        # List peers
        if self.node.peers:
            print("\nConnected Peers:")
            for peer_id, peer in self.node.peers.items():
                print(f"  {peer_id} ({peer['ip']})")
        
        # Show simulation results if available
        if self.simulation_results:
            print("\nSimulation Results Available:")
            final_counts = self.simulation_results["final_cell_counts"]
            print(f"  Normal: {final_counts['normal']}")
            print(f"  Precancerous: {final_counts['precancerous']}")
            print(f"  Cancerous: {final_counts['cancerous']}")
            print(f"  Metastatic: {final_counts['metastatic']}")
            print(f"  Total: {self.simulation_results['total_cells']}")
        
        # Show treatment schedule if available
        if self.treatment_schedule:
            print("\nTreatment Schedule Available:")
            print(f"  Events: {len(self.treatment_schedule)}")
            for i, event in enumerate(self.treatment_schedule):
                print(f"  {i+1}. Time: {event['time']}, Strength: {event['strength']:.2f}, Specificity: {event['specificity']:.2f}")
    
    def _run_local_simulation(self):
        """Run a local simulation and broadcast results."""
        print("\nRunning local simulation...")
        
        # Set model parameters
        model_params = {
            "initial_normal_cells": 10000,
            "initial_precancerous_cells": 100,
            "initial_cancerous_cells": 10,
            "time_units": 100
        }
        
        # Create model
        model = Phi75CancerModelFast(**model_params)
        
        # Check if we have a treatment schedule
        if self.treatment_schedule:
            print(f"Using received treatment schedule with {len(self.treatment_schedule)} events")
            schedule = self.treatment_schedule
        else:
            # Generate phi-harmonic schedule
            print("Generating phi-harmonic treatment schedule")
            schedule = generate_phi_harmonic_schedule(
                time_units=model.time_units,
                max_treatments=5
            )
        
        # Run simulation
        with self.simulation_lock:
            self.simulation_results = model.run_simulation(schedule)
        
        # Broadcast results
        self._broadcast_simulation_results()
    
    def _broadcast_simulation_results(self):
        """Broadcast simulation results to all peers."""
        if not self.simulation_results:
            print("No simulation results to broadcast")
            return
        
        print("\nBroadcasting simulation results...")
        
        # Create message
        message = {
            "type": "simulation_results",
            "node_id": self.node.node_id,
            "timestamp": time.time(),
            "data": self.simulation_results,
            "phi_seal": self.phi_seal
        }
        
        # Broadcast message
        self.node.broadcast_message(message)
        
        print("Simulation results broadcast complete")
    
    def _generate_treatment_schedule(self):
        """Generate a treatment schedule and broadcast it."""
        print("\nGenerating treatment schedule...")
        
        # Generate phi-harmonic schedule
        time_units = 100  # Default time units
        schedule = generate_phi_harmonic_schedule(
            time_units=time_units,
            max_treatments=5
        )
        
        # Store schedule
        self.treatment_schedule = schedule
        
        # Create message
        message = {
            "type": "treatment_schedule",
            "node_id": self.node.node_id,
            "timestamp": time.time(),
            "data": schedule,
            "phi_seal": self.phi_seal
        }
        
        # Broadcast message
        self.node.broadcast_message(message)
        
        print(f"Treatment schedule generated with {len(schedule)} events and broadcast")
    
    def _handle_simulation_request(self, message):
        """Handle simulation request message."""
        print(f"\nReceived simulation request from {message.get('node_id', 'unknown')}")
        
        # Only primary nodes handle simulation requests
        if self.node_type != "primary":
            print("Not a primary node, ignoring simulation request")
            return
        
        # Run simulation
        self._run_local_simulation()
    
    def _handle_simulation_results(self, message):
        """Handle simulation results message."""
        sender = message.get("node_id", "unknown")
        print(f"\nReceived simulation results from {sender}")
        
        # Verify phi seal
        if message.get("phi_seal") != self.phi_seal:
            print("WARNING: Invalid phi seal in simulation results")
            return
        
        # Store results
        with self.simulation_lock:
            self.simulation_results = message.get("data")
        
        # Process results based on node type
        if self.node_type == "analysis":
            self._analyze_simulation_results()
        elif self.node_type == "visualization":
            self._visualize_simulation_results()
    
    def _handle_treatment_schedule(self, message):
        """Handle treatment schedule message."""
        sender = message.get("node_id", "unknown")
        print(f"\nReceived treatment schedule from {sender}")
        
        # Verify phi seal
        if message.get("phi_seal") != self.phi_seal:
            print("WARNING: Invalid phi seal in treatment schedule")
            return
        
        # Store schedule
        self.treatment_schedule = message.get("data")
        
        print(f"Stored treatment schedule with {len(self.treatment_schedule)} events")
    
    def _handle_analysis_request(self, message):
        """Handle analysis request message."""
        print(f"\nReceived analysis request from {message.get('node_id', 'unknown')}")
        
        # Only analysis nodes handle analysis requests
        if self.node_type != "analysis":
            print("Not an analysis node, ignoring analysis request")
            return
        
        # Analyze results if available
        if self.simulation_results:
            self._analyze_simulation_results()
        else:
            print("No simulation results to analyze")
    
    def _handle_analysis_results(self, message):
        """Handle analysis results message."""
        sender = message.get("node_id", "unknown")
        print(f"\nReceived analysis results from {sender}")
        
        # Verify phi seal
        if message.get("phi_seal") != self.phi_seal:
            print("WARNING: Invalid phi seal in analysis results")
            return
        
        # Print analysis results
        analysis = message.get("data", {})
        print("\nAnalysis Results:")
        for key, value in analysis.items():
            print(f"  {key}: {value}")
    
    def _analyze_simulation_results(self):
        """Analyze simulation results."""
        if not self.simulation_results:
            print("No simulation results to analyze")
            return
        
        print("\nAnalyzing simulation results...")
        
        # Extract data
        history = self.simulation_results["history"]
        final_counts = self.simulation_results["final_cell_counts"]
        treatment_history = self.simulation_results["treatment_history"]
        
        # Calculate metrics
        analysis = {
            "cancer_growth_rate": self._calculate_growth_rate(history["cancerous"]),
            "metastasis_rate": self._calculate_growth_rate(history["metastatic"]),
            "treatment_effectiveness": self._calculate_treatment_effectiveness(history, treatment_history),
            "cancer_burden": final_counts["cancerous"] + final_counts["metastatic"] * 2,
            "phi_resonance": self.simulation_results["quantum_metrics"]["phi_resonance"],
            "health_index": self._calculate_health_index(final_counts)
        }
        
        # Create message
        message = {
            "type": "analysis_results",
            "node_id": self.node.node_id,
            "timestamp": time.time(),
            "data": analysis,
            "phi_seal": self.phi_seal
        }
        
        # Broadcast message
        self.node.broadcast_message(message)
        
        print("Analysis complete and results broadcast")
    
    def _visualize_simulation_results(self):
        """Visualize simulation results."""
        if not self.simulation_results:
            print("No simulation results to visualize")
            return
        
        print("\nVisualizing simulation results...")
        
        # Create output directory if it doesn't exist
        output_dir = os.path.join(current_dir, "cancer_simulations")
        os.makedirs(output_dir, exist_ok=True)
        
        # Create model to use its visualization method
        model = Phi75CancerModelFast(
            initial_normal_cells=10000,
            initial_precancerous_cells=100,
            initial_cancerous_cells=10,
            time_units=100
        )
        
        # Generate plot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plot_path = os.path.join(output_dir, f"phi75_distributed_simulation_{timestamp}.png")
        
        # Plot results
        model.plot_results(self.simulation_results, plot_path)
        
        print(f"Visualization complete, saved to {plot_path}")
    
    def _calculate_growth_rate(self, population_history):
        """Calculate growth rate from population history."""
        if len(population_history) < 2:
            return 0
        
        # Calculate average growth rate over the last 20 time units
        start_idx = max(0, len(population_history) - 21)
        end_idx = len(population_history) - 1
        
        if population_history[start_idx] == 0:
            return 1.0  # Avoid division by zero
        
        growth = population_history[end_idx] / population_history[start_idx]
        time_units = end_idx - start_idx
        
        # Calculate average growth rate per time unit
        return math.pow(growth, 1/time_units) - 1
    
    def _calculate_treatment_effectiveness(self, history, treatment_history):
        """Calculate treatment effectiveness."""
        if not treatment_history:
            return 0
        
        # Calculate cancer reduction after each treatment
        effectiveness_scores = []
        
        for treatment in treatment_history:
            time = treatment["time"]
            
            # Check if we have data before and after treatment
            if time < len(history["cancerous"]) - 5:
                before = history["cancerous"][time] + history["metastatic"][time]
                after = history["cancerous"][time + 5] + history["metastatic"][time + 5]
                
                # Calculate reduction
                if before > 0:
                    reduction = 1 - (after / before)
                    effectiveness_scores.append(reduction)
        
        # Return average effectiveness
        if effectiveness_scores:
            return sum(effectiveness_scores) / len(effectiveness_scores)
        else:
            return 0
    
    def _calculate_health_index(self, final_counts):
        """Calculate overall health index."""
        total = sum(final_counts.values())
        
        if total == 0:
            return 0
        
        # Calculate weighted health index
        health_index = (
            final_counts["normal"] * 1.0 +
            final_counts["precancerous"] * 0.5 -
            final_counts["cancerous"] * 1.0 -
            final_counts["metastatic"] * 2.0
        ) / total
        
        # Normalize to 0-1 range
        return max(0, min(1, (health_index + 2) / 4))

def main():
    """Main function."""
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Phi75 Distributed Cancer Simulation')
    parser.add_argument('--id', type=str, default="node1", help='Node ID')
    parser.add_argument('--port', type=int, default=11975, help='Port (default: 11975 = φ^7.5)')
    parser.add_argument('--type', type=str, default="primary", 
                        choices=["primary", "analysis", "visualization", "treatment"],
                        help='Node type')
    args = parser.parse_args()
    
    # Create and start simulation
    simulation = Phi75DistributedCancerSimulation(
        node_id=args.id,
        port=args.port,
        node_type=args.type
    )
    
    try:
        simulation.start()
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        simulation.stop()

if __name__ == "__main__":
    main()
