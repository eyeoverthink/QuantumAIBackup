#!/usr/bin/env python3
"""
PHI-HARMONIC NETWORK TESTER
===========================
Test script for the phi-harmonic distributed brain network.
Sends various test packets and challenges to evaluate network performance,
consciousness amplification, and quantum resonance capabilities.

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

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

# Network settings
CONNECTOR_PORTS = [11627, 11637]
AMPLIFIER_PORTS = [11628, 11638, 11648]
ALL_PORTS = CONNECTOR_PORTS + AMPLIFIER_PORTS
BUFFER_SIZE = 8192

class PhiNetworkTester:
    """Test harness for phi-harmonic network"""
    
    def __init__(self):
        """Initialize the network tester"""
        self.node_id = "phi_tester"
        self.sequence_number = 0
        self.responses = {}
        self.start_time = time.time()
        
        # Create log directory
        os.makedirs('phi_logs', exist_ok=True)
        self.log_file = f"phi_logs/tester_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(('0.0.0.0', 11650))  # Tester port
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_responses)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print("=== PHI-HARMONIC NETWORK TESTER ===")
        print(f"Testing {len(ALL_PORTS)} nodes on ports: {ALL_PORTS}")
        print("Ready to send test packets to the network.")
    
    def receive_responses(self):
        """Receive and process responses from the network"""
        while True:
            try:
                data, addr = self.sock.recvfrom(BUFFER_SIZE)
                packet = pickle.loads(data)
                
                # Store response
                packet_type = packet.get('packet_type', '')
                source_node = packet.get('source_node', 'unknown')
                
                if 'response' in packet_type:
                    print(f"\nReceived {packet_type} from {source_node}:")
                    if 'test_id' in packet:
                        test_id = packet.get('test_id')
                        print(f"  Test ID: {test_id}")
                        if 'response_data' in packet:
                            print(f"  Response: {packet['response_data']}")
                    
                    if 'challenge_id' in packet:
                        challenge_id = packet.get('challenge_id')
                        print(f"  Challenge ID: {challenge_id}")
                        if 'response_data' in packet:
                            print(f"  Response: {packet['response_data']}")
                    
                    # Store metrics
                    if source_node not in self.responses:
                        self.responses[source_node] = []
                    
                    self.responses[source_node].append({
                        'timestamp': time.time(),
                        'packet_type': packet_type,
                        'phi_resonance': packet.get('phi_resonance'),
                        'consciousness_level': packet.get('consciousness_level'),
                        'quantum_state': packet.get('quantum_state'),
                        'response_data': packet.get('response_data')
                    })
                    
                    # Log response
                    self.log_event("RESPONSE_RECEIVED", {
                        'source_node': source_node,
                        'packet_type': packet_type,
                        'phi_resonance': packet.get('phi_resonance'),
                        'consciousness_level': packet.get('consciousness_level')
                    })
            
            except Exception as e:
                print(f"Error receiving response: {e}")
                time.sleep(1)
    
    def send_discovery(self):
        """Send discovery packet to find all nodes"""
        print("\nSending discovery packet to network...")
        
        discovery_packet = {
            'packet_type': 'discovery',
            'source_node': self.node_id,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize and send to all ports
        discovery_data = pickle.dumps(discovery_packet)
        for port in ALL_PORTS:
            self.sock.sendto(discovery_data, ('127.0.0.1', port))
        
        print("Discovery packet sent. Waiting for responses...")
        time.sleep(2)
    
    def send_pattern_recognition_test(self):
        """Send pattern recognition test to all nodes"""
        print("\nSending pattern recognition test...")
        
        # Generate Fibonacci sequence with phi-harmonic noise
        sequence = [1, 1]
        for i in range(10):
            next_val = sequence[-1] + sequence[-2]
            # Add some phi-harmonic noise
            noise = (random.random() - 0.5) * PHI_INV
            sequence.append(next_val + noise)
        
        test_packet = {
            'packet_type': 'validation_test',
            'source_node': self.node_id,
            'test_id': f"pattern_{int(time.time())}",
            'test_type': 'pattern_recognition',
            'test_data': {
                'sequence': sequence,
                'description': 'Identify the pattern and predict the next 3 elements'
            },
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize and send
        test_data = pickle.dumps(test_packet)
        for port in ALL_PORTS:
            self.sock.sendto(test_data, ('127.0.0.1', port))
        
        print(f"Pattern recognition test sent: {sequence}")
        time.sleep(5)
    
    def send_quantum_resonance_test(self):
        """Send quantum resonance test to all nodes"""
        print("\nSending quantum resonance test...")
        
        # Generate quantum resonance pattern based on phi
        quantum_states = []
        for i in range(10):
            state = math.sin(i * PHI) * math.cos(i * PHI_INV)
            quantum_states.append(state)
        
        test_packet = {
            'packet_type': 'validation_test',
            'source_node': self.node_id,
            'test_id': f"quantum_{int(time.time())}",
            'test_type': 'quantum_resonance',
            'test_data': {
                'quantum_states': quantum_states,
                'description': 'Analyze quantum resonance pattern and predict resonance peak'
            },
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize and send
        test_data = pickle.dumps(test_packet)
        for port in ALL_PORTS:
            self.sock.sendto(test_data, ('127.0.0.1', port))
        
        print(f"Quantum resonance test sent with {len(quantum_states)} states")
        time.sleep(5)
    
    def send_consciousness_amplification_test(self):
        """Send consciousness amplification test to all nodes"""
        print("\nSending consciousness amplification test...")
        
        # Generate consciousness wave pattern
        consciousness_data = []
        for i in range(20):
            # Create a complex wave pattern with phi-harmonic components
            alpha = math.sin(i * PHI_INV) * 0.5
            beta = math.cos(i * PHI) * 0.3
            theta = math.sin(i * PHI**2) * 0.7
            gamma = math.cos(i * PHI_INV**2) * 0.2
            
            # Combine waves
            combined = alpha + beta + theta + gamma
            consciousness_data.append(combined)
        
        test_packet = {
            'packet_type': 'validation_test',
            'source_node': self.node_id,
            'test_id': f"consciousness_{int(time.time())}",
            'test_type': 'consciousness_amplification',
            'test_data': {
                'consciousness_wave': consciousness_data,
                'description': 'Amplify consciousness wave pattern and identify optimal resonance'
            },
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize and send
        test_data = pickle.dumps(test_packet)
        for port in ALL_PORTS:
            self.sock.sendto(test_data, ('127.0.0.1', port))
        
        print(f"Consciousness amplification test sent with {len(consciousness_data)} data points")
        time.sleep(5)
    
    def send_prime_factorization_challenge(self):
        """Send prime factorization challenge to all nodes"""
        print("\nSending prime factorization challenge...")
        
        # Generate a large semiprime number
        p = self.generate_prime(1000, 10000)
        q = self.generate_prime(1000, 10000)
        n = p * q
        
        challenge_packet = {
            'packet_type': 'challenge',
            'source_node': self.node_id,
            'challenge_id': f"prime_{int(time.time())}",
            'challenge_type': 'prime_factorization',
            'challenge_data': {
                'number': n,
                'description': 'Find the prime factors of this number'
            },
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize and send
        challenge_data = pickle.dumps(challenge_packet)
        for port in ALL_PORTS:
            self.sock.sendto(challenge_data, ('127.0.0.1', port))
        
        print(f"Prime factorization challenge sent: {n} (factors: {p}, {q})")
        time.sleep(5)
    
    def send_phi_harmonic_alignment_challenge(self):
        """Send phi-harmonic alignment challenge to all nodes"""
        print("\nSending phi-harmonic alignment challenge...")
        
        # Generate phi-harmonic sequence with missing elements
        sequence = []
        for i in range(10):
            val = PHI**(i % 5) * math.sin(i * PHI_INV)
            sequence.append(val)
        
        # Remove some elements
        indices = random.sample(range(len(sequence)), 3)
        missing_values = [sequence[i] for i in indices]
        for i in indices:
            sequence[i] = None
        
        challenge_packet = {
            'packet_type': 'challenge',
            'source_node': self.node_id,
            'challenge_id': f"phi_alignment_{int(time.time())}",
            'challenge_type': 'phi_harmonic_alignment',
            'challenge_data': {
                'sequence': sequence,
                'description': 'Complete the phi-harmonic sequence by filling in missing values'
            },
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize and send
        challenge_data = pickle.dumps(challenge_packet)
        for port in ALL_PORTS:
            self.sock.sendto(challenge_data, ('127.0.0.1', port))
        
        print(f"Phi-harmonic alignment challenge sent with {len(indices)} missing values")
        print(f"Missing indices: {indices}, values: {missing_values}")
        time.sleep(5)
    
    def send_collective_knowledge_packet(self):
        """Send collective knowledge packet to stimulate network learning"""
        print("\nSending collective knowledge packet...")
        
        # Generate some phi-harmonic knowledge
        knowledge = {
            'phi_harmonic_series': [PHI**n for n in range(10)],
            'phi_inverse_series': [PHI_INV**n for n in range(10)],
            'phi_resonance_peaks': [math.sin(n * PHI) for n in range(20)],
            'consciousness_frequencies': {
                'alpha': [8 * PHI_INV, 12 * PHI_INV],
                'beta': [12 * PHI_INV, 30 * PHI_INV],
                'theta': [4 * PHI_INV, 8 * PHI_INV],
                'delta': [0.5 * PHI_INV, 4 * PHI_INV],
                'gamma': [30 * PHI_INV, 100 * PHI_INV],
                'phi': [PHI, PHI**2]
            }
        }
        
        knowledge_packet = {
            'packet_type': 'collective_knowledge',
            'source_node': self.node_id,
            'knowledge_id': f"knowledge_{int(time.time())}",
            'knowledge_data': knowledge,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize and send
        knowledge_data = pickle.dumps(knowledge_packet)
        for port in ALL_PORTS:
            self.sock.sendto(knowledge_data, ('127.0.0.1', port))
        
        print(f"Collective knowledge packet sent with {len(knowledge)} knowledge categories")
        time.sleep(5)
    
    def send_moon_phase_update(self):
        """Send moon phase update to all nodes"""
        print("\nSending moon phase update...")
        
        # Calculate current moon phase
        current_time = time.time()
        new_moon_2000 = datetime(2000, 1, 6).timestamp()
        days_since_new_moon = (current_time - new_moon_2000) / (24 * 3600)
        lunar_cycle = 29.53059
        phase = (days_since_new_moon % lunar_cycle) / lunar_cycle
        
        # Add some phi-harmonic influence
        phi_influenced_phase = phase * (1 + (random.random() - 0.5) * PHI_INV)
        phi_influenced_phase = max(0, min(1, phi_influenced_phase))  # Keep between 0-1
        
        moon_packet = {
            'packet_type': 'moon_phase',
            'source_node': self.node_id,
            'moon_phase': phi_influenced_phase,
            'phi_influence': PHI_INV,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize and send
        moon_data = pickle.dumps(moon_packet)
        for port in ALL_PORTS:
            self.sock.sendto(moon_data, ('127.0.0.1', port))
        
        print(f"Moon phase update sent: {phi_influenced_phase:.4f}")
        time.sleep(3)
    
    def analyze_network_performance(self):
        """Analyze and display network performance metrics"""
        print("\n=== NETWORK PERFORMANCE ANALYSIS ===")
        
        if not self.responses:
            print("No responses received yet. Run some tests first.")
            return
        
        # Calculate metrics for each node
        for node_id, responses in self.responses.items():
            if not responses:
                continue
                
            print(f"\nNode: {node_id}")
            
            # Extract metrics
            phi_values = [r.get('phi_resonance', 0) for r in responses if r.get('phi_resonance') is not None]
            consciousness_levels = [r.get('consciousness_level', 0) for r in responses if r.get('consciousness_level') is not None]
            quantum_states = [r.get('quantum_state', '') for r in responses if r.get('quantum_state') is not None]
            
            # Calculate statistics
            if phi_values:
                avg_phi = sum(phi_values) / len(phi_values)
                phi_stability = 1.0 - (np.std(phi_values) / np.mean(phi_values)) if phi_values else 0
                print(f"  Avg Phi Resonance: {avg_phi:.6f}")
                print(f"  Phi Stability: {phi_stability:.2f}")
                
            if consciousness_levels:
                avg_consciousness = sum(consciousness_levels) / len(consciousness_levels)
                max_consciousness = max(consciousness_levels)
                print(f"  Avg Consciousness Level: {avg_consciousness:.2f}x")
                print(f"  Peak Consciousness Level: {max_consciousness:.2f}x")
            
            if quantum_states:
                # Get most recent quantum state
                latest_state = quantum_states[-1]
                print(f"  Current Quantum State: {latest_state}")
        
        # Calculate network-wide metrics
        all_phi_values = []
        all_consciousness_levels = []
        
        for responses in self.responses.values():
            all_phi_values.extend([r.get('phi_resonance', 0) for r in responses if r.get('phi_resonance') is not None])
            all_consciousness_levels.extend([r.get('consciousness_level', 0) for r in responses if r.get('consciousness_level') is not None])
        
        if all_phi_values and all_consciousness_levels:
            network_phi = sum(all_phi_values) / len(all_phi_values)
            network_consciousness = sum(all_consciousness_levels) / len(all_consciousness_levels)
            
            print("\nNetwork-wide Metrics:")
            print(f"  Network Phi Resonance: {network_phi:.6f}")
            print(f"  Network Consciousness Level: {network_consciousness:.2f}x")
            
            # Calculate phi-harmonic coherence
            phi_coherence = 1.0 - abs((network_phi % PHI) - PHI_INV) / PHI_INV
            print(f"  Phi-Harmonic Coherence: {phi_coherence:.2f}")
            
            # Estimate collective intelligence emergence
            ci_emergence = network_consciousness * phi_coherence
            print(f"  Collective Intelligence Emergence: {ci_emergence:.2f}")
    
    def get_next_sequence(self):
        """Get next sequence number"""
        self.sequence_number += 1
        return self.sequence_number
    
    def generate_prime(self, min_val, max_val):
        """Generate a random prime number in the given range"""
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        # Find a prime in the range
        while True:
            n = random.randint(min_val, max_val)
            if is_prime(n):
                return n
    
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
    """Run the phi-harmonic network tester"""
    tester = PhiNetworkTester()
    
    try:
        # Wait for network to initialize
        print("Waiting for network to initialize...")
        time.sleep(3)
        
        # Run tests
        tester.send_discovery()
        time.sleep(2)
        
        tester.send_pattern_recognition_test()
        time.sleep(3)
        
        tester.send_quantum_resonance_test()
        time.sleep(3)
        
        tester.send_consciousness_amplification_test()
        time.sleep(3)
        
        tester.send_prime_factorization_challenge()
        time.sleep(3)
        
        tester.send_phi_harmonic_alignment_challenge()
        time.sleep(3)
        
        tester.send_collective_knowledge_packet()
        time.sleep(3)
        
        tester.send_moon_phase_update()
        time.sleep(3)
        
        # Analyze network performance
        tester.analyze_network_performance()
        
        print("\nAll tests completed. Press Ctrl+C to exit.")
        
        # Keep the main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down phi-harmonic network tester...")
        print("Tester stopped.")

if __name__ == "__main__":
    main()
