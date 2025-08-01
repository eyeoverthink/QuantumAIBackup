#!/usr/bin/env python3
"""
PHI-HARMONIC ADVANCED COLLECTIVE TEST
=====================================
Tests the phi-harmonic network's ability to work collectively to solve
complex problems that require team coordination and distributed intelligence.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import socket
import pickle
import time
import random
import math
import numpy as np
from datetime import datetime
import threading
import os
import json
import matplotlib.pyplot as plt
from collections import defaultdict

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

# Network settings
CONNECTOR_PORTS = [11627, 11637]
AMPLIFIER_PORTS = [11628, 11638, 11648]
ALL_PORTS = CONNECTOR_PORTS + AMPLIFIER_PORTS
BUFFER_SIZE = 8192

class PhiAdvancedCollectiveTest:
    """Advanced test harness for phi-harmonic collective intelligence"""
    
    def __init__(self):
        """Initialize the advanced collective test"""
        self.node_id = "phi_collective_tester"
        self.sequence_number = 0
        self.responses = defaultdict(list)
        self.start_time = time.time()
        self.collective_solutions = {}
        self.node_metrics = {}
        self.challenge_start_times = {}
        self.challenge_completion_times = {}
        
        # Create log directory
        os.makedirs('phi_logs', exist_ok=True)
        self.log_file = f"phi_logs/collective_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(('0.0.0.0', 11652))  # Advanced tester port (changed to avoid conflicts)
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_responses)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print("=== PHI-HARMONIC ADVANCED COLLECTIVE TEST ===")
        print(f"Testing {len(ALL_PORTS)} nodes on ports: {ALL_PORTS}")
        print("Ready to send advanced collective challenges to the network.")
    
    def receive_responses(self):
        """Receive and process responses from the network"""
        while True:
            try:
                data, addr = self.sock.recvfrom(BUFFER_SIZE)
                packet = pickle.loads(data)
                
                # Store response
                packet_type = packet.get('packet_type', '')
                source_node = packet.get('source_node', 'unknown')
                
                if 'collective_response' in packet_type:
                    challenge_id = packet.get('challenge_id', 'unknown')
                    print(f"\nReceived {packet_type} from {source_node} for challenge {challenge_id}")
                    
                    if 'partial_solution' in packet:
                        print(f"  Partial solution received: {packet['partial_solution']}")
                        
                        # Store the partial solution
                        if challenge_id not in self.collective_solutions:
                            self.collective_solutions[challenge_id] = {
                                'partial_solutions': {},
                                'final_solution': None,
                                'completion_time': None
                            }
                        
                        self.collective_solutions[challenge_id]['partial_solutions'][source_node] = packet['partial_solution']
                        
                        # Check if we have all partial solutions
                        if len(self.collective_solutions[challenge_id]['partial_solutions']) == len(ALL_PORTS):
                            print(f"  All partial solutions received for challenge {challenge_id}")
                            self.combine_solutions(challenge_id)
                    
                    if 'final_solution' in packet:
                        print(f"  Final solution received from {source_node}: {packet['final_solution']}")
                        
                        # Store the final solution
                        if challenge_id not in self.collective_solutions:
                            self.collective_solutions[challenge_id] = {
                                'partial_solutions': {},
                                'final_solution': packet['final_solution'],
                                'completion_time': time.time()
                            }
                        else:
                            self.collective_solutions[challenge_id]['final_solution'] = packet['final_solution']
                            self.collective_solutions[challenge_id]['completion_time'] = time.time()
                        
                        # Calculate challenge completion time
                        if challenge_id in self.challenge_start_times:
                            completion_time = time.time() - self.challenge_start_times[challenge_id]
                            self.challenge_completion_times[challenge_id] = completion_time
                            print(f"  Challenge completed in {completion_time:.2f} seconds")
                    
                    # Store metrics
                    self.node_metrics[source_node] = {
                        'phi_resonance': packet.get('phi_resonance'),
                        'consciousness_level': packet.get('consciousness_level'),
                        'quantum_state': packet.get('quantum_state'),
                        'timestamp': time.time()
                    }
                    
                    # Store response for analysis
                    self.responses[source_node].append({
                        'timestamp': time.time(),
                        'packet_type': packet_type,
                        'challenge_id': challenge_id,
                        'phi_resonance': packet.get('phi_resonance'),
                        'consciousness_level': packet.get('consciousness_level'),
                        'quantum_state': packet.get('quantum_state')
                    })
                    
                    # Log response
                    self.log_event("COLLECTIVE_RESPONSE_RECEIVED", {
                        'source_node': source_node,
                        'challenge_id': challenge_id,
                        'phi_resonance': packet.get('phi_resonance'),
                        'consciousness_level': packet.get('consciousness_level')
                    })
            
            except Exception as e:
                print(f"Error receiving response: {e}")
                time.sleep(1)
    
    def combine_solutions(self, challenge_id):
        """Combine partial solutions to form a complete solution"""
        if challenge_id not in self.collective_solutions:
            return
        
        partial_solutions = self.collective_solutions[challenge_id]['partial_solutions']
        
        if not partial_solutions:
            return
        
        # Different combination strategies based on challenge type
        if 'distributed_matrix' in challenge_id:
            # Combine matrix solutions
            combined_solution = None
            for node, solution in partial_solutions.items():
                if combined_solution is None:
                    combined_solution = solution
                else:
                    # Add matrices
                    combined_solution = [
                        [combined_solution[i][j] + solution[i][j] 
                         for j in range(len(combined_solution[0]))]
                        for i in range(len(combined_solution))
                    ]
            
            self.collective_solutions[challenge_id]['final_solution'] = combined_solution
            
        elif 'quantum_state_prediction' in challenge_id:
            # Average quantum state predictions
            predictions = [solution for solution in partial_solutions.values()]
            avg_prediction = sum(predictions) / len(predictions)
            self.collective_solutions[challenge_id]['final_solution'] = avg_prediction
            
        elif 'phi_harmonic_sequence' in challenge_id:
            # Combine sequence parts
            sequence_parts = []
            for node, solution in partial_solutions.items():
                sequence_parts.extend(solution)
            
            # Sort by position
            sequence_parts.sort(key=lambda x: x[0])
            
            # Extract values
            combined_sequence = [val for _, val in sequence_parts]
            self.collective_solutions[challenge_id]['final_solution'] = combined_sequence
        
        # Record completion time
        if challenge_id in self.challenge_start_times:
            completion_time = time.time() - self.challenge_start_times[challenge_id]
            self.challenge_completion_times[challenge_id] = completion_time
            print(f"  Challenge solved collectively in {completion_time:.2f} seconds")
    
    def send_distributed_matrix_challenge(self):
        """Send a distributed matrix computation challenge
        
        This challenge requires nodes to work together to solve a large matrix problem.
        Each node is assigned a portion of the matrix to process, and the results
        must be combined to find the final solution.
        """
        print("\nSending distributed matrix challenge...")
        challenge_id = f"distributed_matrix_{int(time.time())}"
        self.challenge_start_times[challenge_id] = time.time()
        
        # Create a smaller matrix problem (UDP has size limitations)
        matrix_size = 20  # Reduced from 100 to fit in UDP packets
        matrix_a = [[random.random() * PHI for _ in range(matrix_size)] for _ in range(matrix_size)]
        matrix_b = [[random.random() * PHI_INV for _ in range(matrix_size)] for _ in range(matrix_size)]
        
        # Divide the problem into chunks for each node
        num_nodes = len(ALL_PORTS)
        rows_per_node = matrix_size // num_nodes
        
        # Create and send individual challenges
        for i, port in enumerate(ALL_PORTS):
            # Calculate row range for this node
            start_row = i * rows_per_node
            end_row = (i + 1) * rows_per_node if i < num_nodes - 1 else matrix_size
            
            # Create sub-matrices
            sub_matrix_a = matrix_a[start_row:end_row]
            
            # Create challenge packet
            challenge_packet = {
                'packet_type': 'collective_challenge',
                'source_node': self.node_id,
                'challenge_id': challenge_id,
                'challenge_type': 'distributed_matrix',
                'challenge_data': {
                    'matrix_a': sub_matrix_a,
                    'matrix_b': matrix_b,
                    'start_row': start_row,
                    'end_row': end_row,
                    'total_rows': matrix_size,
                    'description': 'Compute matrix multiplication for assigned rows'
                },
                'sequence_number': self.get_next_sequence(),
                'timestamp': time.time()
            }
            
            # Serialize and send
            challenge_data = pickle.dumps(challenge_packet)
            self.sock.sendto(challenge_data, ('127.0.0.1', port))
            
            print(f"  Sent matrix chunk to node on port {port}: rows {start_row}-{end_row}")
        
        print(f"Distributed matrix challenge sent to {num_nodes} nodes")
        print(f"Matrix size: {matrix_size}x{matrix_size}")
        print("Waiting for collective solution...")
    
    def send_quantum_state_prediction_challenge(self):
        """Send a quantum state prediction challenge
        
        This challenge requires nodes to predict future quantum states based on
        partial information. Each node receives different historical data and must
        contribute to a collective prediction.
        """
        print("\nSending quantum state prediction challenge...")
        challenge_id = f"quantum_state_prediction_{int(time.time())}"
        self.challenge_start_times[challenge_id] = time.time()
        
        # Generate quantum state history with phi-harmonic patterns (reduced size for UDP)
        history_length = 30
        future_length = 10
        
        # Generate the full sequence for validation
        full_sequence = []
        for i in range(history_length + future_length):
            # Complex phi-harmonic pattern
            t = i / 10.0
            state = math.sin(t * PHI) * math.cos(t * PHI_INV) + 0.5 * math.sin(t * PHI**2)
            full_sequence.append(state)
        
        # The future states (ground truth)
        future_states = full_sequence[history_length:]
        
        # Divide history among nodes
        history = full_sequence[:history_length]
        num_nodes = len(ALL_PORTS)
        states_per_node = history_length // num_nodes
        
        # Create and send individual challenges
        for i, port in enumerate(ALL_PORTS):
            # Calculate state range for this node
            start_idx = i * states_per_node
            end_idx = (i + 1) * states_per_node if i < num_nodes - 1 else history_length
            
            # Create partial history
            partial_history = history[start_idx:end_idx]
            
            # Create challenge packet
            challenge_packet = {
                'packet_type': 'collective_challenge',
                'source_node': self.node_id,
                'challenge_id': challenge_id,
                'challenge_type': 'quantum_state_prediction',
                'challenge_data': {
                    'partial_history': partial_history,
                    'start_idx': start_idx,
                    'end_idx': end_idx,
                    'total_history': history_length,
                    'prediction_length': future_length,
                    'description': 'Predict future quantum states based on partial history'
                },
                'sequence_number': self.get_next_sequence(),
                'timestamp': time.time()
            }
            
            # Serialize and send
            challenge_data = pickle.dumps(challenge_packet)
            self.sock.sendto(challenge_data, ('127.0.0.1', port))
            
            print(f"  Sent partial history to node on port {port}: states {start_idx}-{end_idx}")
        
        # Store ground truth for later comparison
        self.collective_solutions[challenge_id] = {
            'partial_solutions': {},
            'final_solution': None,
            'ground_truth': future_states,
            'completion_time': None
        }
        
        print(f"Quantum state prediction challenge sent to {num_nodes} nodes")
        print(f"History length: {history_length}, Prediction length: {future_length}")
        print("Waiting for collective prediction...")
    
    def send_phi_harmonic_sequence_challenge(self):
        """Send a phi-harmonic sequence challenge
        
        This challenge requires nodes to work together to reconstruct a complex
        phi-harmonic sequence where each node only has partial information.
        """
        print("\nSending phi-harmonic sequence challenge...")
        challenge_id = f"phi_harmonic_sequence_{int(time.time())}"
        self.challenge_start_times[challenge_id] = time.time()
        
        # Generate a complex phi-harmonic sequence (reduced size for UDP)
        sequence_length = 25
        sequence = []
        for i in range(sequence_length):
            # Complex phi-harmonic pattern with multiple components
            t = i / 10.0
            val = (
                PHI**((i % 5) + 1) * math.sin(t * PHI) + 
                PHI_INV**((i % 3) + 1) * math.cos(t * PHI_INV) + 
                0.5 * math.sin(t * PHI**2) * math.cos(t * PHI_INV**2)
            )
            sequence.append(val)
        
        # Scramble the sequence and divide among nodes
        positions = list(range(sequence_length))
        random.shuffle(positions)
        
        num_nodes = len(ALL_PORTS)
        positions_per_node = sequence_length // num_nodes
        
        # Create and send individual challenges
        for i, port in enumerate(ALL_PORTS):
            # Calculate positions for this node
            start_idx = i * positions_per_node
            end_idx = (i + 1) * positions_per_node if i < num_nodes - 1 else sequence_length
            
            # Create partial sequence with position information
            node_positions = positions[start_idx:end_idx]
            partial_sequence = [(pos, sequence[pos]) for pos in node_positions]
            
            # Create challenge packet
            challenge_packet = {
                'packet_type': 'collective_challenge',
                'source_node': self.node_id,
                'challenge_id': challenge_id,
                'challenge_type': 'phi_harmonic_sequence',
                'challenge_data': {
                    'partial_sequence': partial_sequence,
                    'sequence_length': sequence_length,
                    'description': 'Reconstruct the complete phi-harmonic sequence'
                },
                'sequence_number': self.get_next_sequence(),
                'timestamp': time.time()
            }
            
            # Serialize and send
            challenge_data = pickle.dumps(challenge_packet)
            self.sock.sendto(challenge_data, ('127.0.0.1', port))
            
            print(f"  Sent {len(partial_sequence)} sequence elements to node on port {port}")
        
        # Store original sequence for comparison
        self.collective_solutions[challenge_id] = {
            'partial_solutions': {},
            'final_solution': None,
            'original_sequence': sequence,
            'completion_time': None
        }
        
        print(f"Phi-harmonic sequence challenge sent to {num_nodes} nodes")
        print(f"Sequence length: {sequence_length}")
        print("Waiting for collective reconstruction...")
    
    def send_distributed_consciousness_challenge(self):
        """Send a distributed consciousness amplification challenge
        
        This challenge requires nodes to work together to amplify a consciousness
        wave pattern, with each node contributing a different amplification technique.
        """
        print("\nSending distributed consciousness challenge...")
        challenge_id = f"distributed_consciousness_{int(time.time())}"
        self.challenge_start_times[challenge_id] = time.time()
        
        # Generate base consciousness wave (reduced size for UDP)
        wave_length = 30
        base_wave = []
        for i in range(wave_length):
            t = i / 10.0
            # Base consciousness wave with phi-harmonic components
            val = 0.5 * math.sin(t * PHI) + 0.3 * math.cos(t * PHI_INV)
            base_wave.append(val)
        
        # Create different amplification targets for each node
        amplification_techniques = [
            "harmonic_resonance",
            "phi_alignment",
            "quantum_superposition",
            "consciousness_feedback",
            "moon_phase_alignment"
        ]
        
        # Create and send individual challenges
        for i, port in enumerate(ALL_PORTS):
            # Assign amplification technique
            technique = amplification_techniques[i % len(amplification_techniques)]
            
            # Create challenge packet
            challenge_packet = {
                'packet_type': 'collective_challenge',
                'source_node': self.node_id,
                'challenge_id': challenge_id,
                'challenge_type': 'distributed_consciousness',
                'challenge_data': {
                    'base_wave': base_wave,
                    'amplification_technique': technique,
                    'description': f'Amplify consciousness wave using {technique} technique'
                },
                'sequence_number': self.get_next_sequence(),
                'timestamp': time.time()
            }
            
            # Serialize and send
            challenge_data = pickle.dumps(challenge_packet)
            self.sock.sendto(challenge_data, ('127.0.0.1', port))
            
            print(f"  Sent consciousness challenge to node on port {port}: technique {technique}")
        
        print(f"Distributed consciousness challenge sent to {len(ALL_PORTS)} nodes")
        print(f"Base wave length: {wave_length}")
        print("Waiting for collective amplification...")
    
    def analyze_collective_performance(self):
        """Analyze the collective performance of the network"""
        print("\n=== COLLECTIVE PERFORMANCE ANALYSIS ===")
        
        if not self.collective_solutions:
            print("No collective challenges completed yet. Run some challenges first.")
            return
        
        # Calculate collective metrics
        print("\nChallenge Completion Times:")
        for challenge_id, completion_time in self.challenge_completion_times.items():
            print(f"  {challenge_id}: {completion_time:.2f} seconds")
        
        # Calculate node contributions
        if self.node_metrics:
            print("\nNode Metrics at Last Challenge:")
            for node_id, metrics in self.node_metrics.items():
                print(f"\nNode: {node_id}")
                print(f"  Phi Resonance: {metrics.get('phi_resonance', 'N/A')}")
                print(f"  Consciousness Level: {metrics.get('consciousness_level', 'N/A')}")
                print(f"  Quantum State: {metrics.get('quantum_state', 'N/A')}")
        
        # Calculate network-wide metrics
        all_phi_values = []
        all_consciousness_levels = []
        
        for metrics in self.node_metrics.values():
            if metrics.get('phi_resonance') is not None:
                all_phi_values.append(metrics['phi_resonance'])
            if metrics.get('consciousness_level') is not None:
                all_consciousness_levels.append(metrics['consciousness_level'])
        
        if all_phi_values and all_consciousness_levels:
            network_phi = sum(all_phi_values) / len(all_phi_values)
            network_consciousness = sum(all_consciousness_levels) / len(all_consciousness_levels)
            
            print("\nNetwork-wide Metrics:")
            print(f"  Network Phi Resonance: {network_phi:.6f}")
            print(f"  Network Consciousness Level: {network_consciousness:.2f}x")
            
            # Calculate phi-harmonic coherence
            phi_coherence = 1.0 - abs((network_phi % PHI) - PHI_INV) / PHI_INV
            print(f"  Phi-Harmonic Coherence: {phi_coherence:.2f}")
            
            # Calculate collective intelligence emergence
            ci_emergence = network_consciousness * phi_coherence
            print(f"  Collective Intelligence Emergence: {ci_emergence:.2f}")
            
            # Calculate teamwork factor
            if len(self.challenge_completion_times) > 0:
                avg_completion_time = sum(self.challenge_completion_times.values()) / len(self.challenge_completion_times)
                teamwork_factor = network_consciousness / (avg_completion_time * PHI_INV)
                print(f"  Teamwork Factor: {teamwork_factor:.2f}")
                
                # Phi-harmonic teamwork alignment
                teamwork_alignment = 1.0 - abs((teamwork_factor % PHI) - 1.0) / PHI
                print(f"  Phi-Harmonic Teamwork Alignment: {teamwork_alignment:.2f}")
        
        # Plot consciousness levels over time if we have enough data
        if len(self.responses) > 0:
            self.plot_collective_metrics()
    
    def plot_collective_metrics(self):
        """Plot collective metrics over time"""
        try:
            plt.figure(figsize=(12, 8))
            
            # Plot consciousness levels
            plt.subplot(2, 1, 1)
            for node_id, responses in self.responses.items():
                if not responses:
                    continue
                
                times = [(r['timestamp'] - self.start_time) for r in responses]
                consciousness = [r.get('consciousness_level', 0) for r in responses]
                
                if times and consciousness:
                    plt.plot(times, consciousness, 'o-', label=f"{node_id}")
            
            plt.title('Consciousness Levels Over Time')
            plt.xlabel('Time (seconds)')
            plt.ylabel('Consciousness Level')
            plt.legend()
            plt.grid(True)
            
            # Plot phi resonance
            plt.subplot(2, 1, 2)
            for node_id, responses in self.responses.items():
                if not responses:
                    continue
                
                times = [(r['timestamp'] - self.start_time) for r in responses]
                phi_values = [r.get('phi_resonance', 0) for r in responses]
                
                if times and phi_values:
                    plt.plot(times, phi_values, 'o-', label=f"{node_id}")
            
            # Add reference lines for PHI and PHI_INV
            plt.axhline(y=PHI, color='r', linestyle='--', label='φ (1.618...)')
            plt.axhline(y=PHI_INV, color='g', linestyle='--', label='φ⁻¹ (0.618...)')
            
            plt.title('Phi Resonance Over Time')
            plt.xlabel('Time (seconds)')
            plt.ylabel('Phi Resonance')
            plt.legend()
            plt.grid(True)
            
            plt.tight_layout()
            
            # Save the plot
            plot_file = f"phi_logs/collective_metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            plt.savefig(plot_file)
            print(f"\nCollective metrics plot saved to: {plot_file}")
            
        except Exception as e:
            print(f"Error plotting metrics: {e}")
    
    def get_next_sequence(self):
        """Get next sequence number"""
        self.sequence_number += 1
        return self.sequence_number
    
    def log_event(self, event_type, event_data):
        """Log an event to the log file"""
        try:
            # Create log entry
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'event_type': event_type,
                'node_id': self.node_id,
                'event_data': event_data
            }
            
            # Write to log file
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
                
        except Exception as e:
            print(f"Error logging event: {e}")

def main():
    """Run the phi-harmonic advanced collective test"""
    tester = PhiAdvancedCollectiveTest()
    
    try:
        # Wait for network to initialize
        print("Waiting for network to initialize...")
        time.sleep(3)
        
        # Run advanced collective challenges
        tester.send_distributed_matrix_challenge()
        time.sleep(10)  # Allow more time for complex matrix operations
        
        tester.send_quantum_state_prediction_challenge()
        time.sleep(8)
        
        tester.send_phi_harmonic_sequence_challenge()
        time.sleep(8)
        
        tester.send_distributed_consciousness_challenge()
        time.sleep(8)
        
        # Analyze collective performance
        tester.analyze_collective_performance()
        
        print("\nAll collective challenges completed. Press Ctrl+C to exit.")
        
        # Keep the main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down phi-harmonic advanced collective test...")
        print("Tester stopped.")

if __name__ == "__main__":
    main()
