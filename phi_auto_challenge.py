#!/usr/bin/env python3
"""
PHI-HARMONIC AUTO CHALLENGE
===========================
Automatically tests the parallel thinking capabilities of the phi-harmonic distributed brain
by presenting complex problems and collecting responses without user interaction.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import socket
import pickle
import time
import threading
import random
import math
import numpy as np
from datetime import datetime

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

# Network settings
BRAIN_PORT = 11625
MONITOR_PORT = 11626
CONNECTOR_PORT = 11627
AMPLIFIER_PORT = 11628
COLLECTIVE_PORT = 11629
CHALLENGE_PORT = 11630
BUFFER_SIZE = 8192

class PhiAutoChallenge:
    """Automatic challenge system for testing collective intelligence capabilities"""
    
    def __init__(self):
        """Initialize the challenge system"""
        self.node_id = f"auto_challenge_{int(time.time() * 1000) % 10000}"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.responses = {}
        self.challenge_results = {}
        self.current_challenge = None
        self.challenge_start_time = None
        self.log_file = "phi_challenge_results.log"
        
        # Initialize log file
        with open(self.log_file, "w") as f:
            f.write(f"PHI-HARMONIC AUTO CHALLENGE - STARTED AT {datetime.now().isoformat()}\n")
            f.write("FORMAT: [TIMESTAMP] [CHALLENGE_TYPE] [RESULT] [DETAILS]\n\n")
        
        # Create receiver socket
        self.receiver_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.receiver_sock.bind(('0.0.0.0', CHALLENGE_PORT))
            print(f"Listening on port: {CHALLENGE_PORT}")
        except OSError:
            # Try a different port
            alt_port = CHALLENGE_PORT + 1
            self.receiver_sock.bind(('0.0.0.0', alt_port))
            print(f"Port {CHALLENGE_PORT} in use, listening on port: {alt_port}")
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_responses)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print("=== PHI-HARMONIC AUTO CHALLENGE ===")
        print(f"Challenge Node: {self.node_id}")
        print("Automatically testing collective intelligence capabilities...")
    
    def receive_responses(self):
        """Receive and process responses from the distributed brain nodes"""
        while True:
            try:
                data, addr = self.receiver_sock.recvfrom(BUFFER_SIZE)
                self.process_response(data, addr)
            except Exception as e:
                print(f"Error receiving response: {e}")
                time.sleep(1)
    
    def process_response(self, data, addr):
        """Process a response from a distributed brain node"""
        try:
            packet = pickle.loads(data)
            
            # Check if this is a response to our challenge
            if packet.get('packet_type') == 'challenge_response' and self.current_challenge:
                source_node = packet.get('source_node', 'unknown')
                response_data = packet.get('response_data', {})
                response_time = packet.get('timestamp', time.time())
                
                # Calculate response time
                if self.challenge_start_time:
                    time_to_respond = response_time - self.challenge_start_time
                else:
                    time_to_respond = 0
                
                # Store the response
                if source_node not in self.responses:
                    self.responses[source_node] = []
                
                self.responses[source_node].append({
                    'challenge_id': self.current_challenge.get('challenge_id'),
                    'response_data': response_data,
                    'time_to_respond': time_to_respond,
                    'timestamp': response_time
                })
                
                print(f"\nResponse received from {source_node}:")
                print(f"Time to respond: {time_to_respond:.2f} seconds")
                print(f"Response data: {response_data}")
                
                # Check if this completes the challenge
                self.check_challenge_completion()
            
            # Also look for any phi-harmonic packets that might contain insights
            elif 'phi_resonance' in packet:
                print(f"\nDetected phi-harmonic packet from {addr}:")
                print(f"Packet type: {packet.get('packet_type')}")
                print(f"Phi resonance: {packet.get('phi_resonance')}")
                if 'knowledge_data' in packet:
                    print(f"Knowledge data: {packet.get('knowledge_data')}")
                if 'insight' in packet:
                    print(f"Insight: {packet.get('insight')}")
        
        except Exception as e:
            # Try to analyze raw data
            try:
                data_str = str(data)
                if 'phi' in data_str.lower() or 'quantum' in data_str.lower() or 'resonance' in data_str.lower():
                    print(f"\nDetected potential phi-harmonic raw data from {addr}")
            except:
                pass
            print(f"Error processing response: {e}")
    
    def check_challenge_completion(self):
        """Check if the current challenge has been completed"""
        if not self.current_challenge:
            return
        
        # Get all responses for the current challenge
        challenge_responses = {}
        for node, responses in self.responses.items():
            for response in responses:
                if response['challenge_id'] == self.current_challenge.get('challenge_id'):
                    challenge_responses[node] = response
        
        # Check if we have responses or if timeout has occurred
        timeout = 30  # 30 seconds timeout
        if len(challenge_responses) > 0 or (time.time() - self.challenge_start_time > timeout):
            self.evaluate_challenge(challenge_responses)
    
    def evaluate_challenge(self, responses):
        """Evaluate the responses to the current challenge"""
        if not self.current_challenge:
            return
        
        challenge_id = self.current_challenge.get('challenge_id')
        challenge_type = self.current_challenge.get('challenge_type')
        
        print("\n=== CHALLENGE EVALUATION ===")
        print(f"Challenge ID: {challenge_id}")
        print(f"Challenge Type: {challenge_type}")
        print(f"Number of Responses: {len(responses)}")
        
        # Evaluate based on challenge type
        if challenge_type == 'prime_factorization':
            result = self.evaluate_prime_factorization(responses)
        elif challenge_type == 'pattern_recognition':
            result = self.evaluate_pattern_recognition(responses)
        elif challenge_type == 'quantum_state_prediction':
            result = self.evaluate_quantum_state_prediction(responses)
        elif challenge_type == 'consciousness_amplification':
            result = self.evaluate_consciousness_amplification(responses)
        elif challenge_type == 'phi_harmonic_alignment':
            result = self.evaluate_phi_harmonic_alignment(responses)
        else:
            result = {"success": False, "message": "Unknown challenge type"}
        
        # Log the result
        with open(self.log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [{challenge_type}] "
                   f"[{'SUCCESS' if result.get('success') else 'FAILURE'}] "
                   f"[{result.get('message')}]\n")
        
        # Store challenge results
        self.challenge_results[challenge_id] = {
            'challenge': self.current_challenge,
            'responses': responses,
            'completion_time': time.time() - self.challenge_start_time,
            'result': result
        }
        
        # Clear current challenge
        self.current_challenge = None
        self.challenge_start_time = None
        
        # Schedule next challenge
        threading.Timer(5.0, self.run_next_challenge).start()
    
    def evaluate_prime_factorization(self, responses):
        """Evaluate prime factorization challenge responses"""
        target_number = self.current_challenge.get('target_number')
        expected_factors = self.current_challenge.get('expected_factors')
        
        print(f"Target Number: {target_number}")
        print(f"Expected Factors: {expected_factors}")
        
        # Check each response
        correct_responses = 0
        fastest_node = None
        fastest_time = float('inf')
        
        for node, response in responses.items():
            factors = response['response_data'].get('factors', [])
            is_correct = sorted(factors) == sorted(expected_factors)
            
            print(f"\nNode: {node}")
            print(f"Factors: {factors}")
            print(f"Correct: {is_correct}")
            print(f"Time: {response['time_to_respond']:.2f} seconds")
            
            if is_correct:
                correct_responses += 1
                if response['time_to_respond'] < fastest_time:
                    fastest_time = response['time_to_respond']
                    fastest_node = node
        
        # Calculate collective performance
        if responses:
            accuracy = correct_responses / len(responses)
            collective_time = min([r['time_to_respond'] for r in responses.values()]) if responses else float('inf')
            
            print("\n=== COLLECTIVE PERFORMANCE ===")
            print(f"Accuracy: {accuracy:.2f}")
            print(f"Fastest Node: {fastest_node}")
            print(f"Fastest Time: {fastest_time:.2f} seconds")
            print(f"Collective Time: {collective_time:.2f} seconds")
            
            # Determine if collective was faster than individual nodes
            collective_advantage = any([collective_time < r['time_to_respond'] for r in responses.values()])
            print(f"Collective Advantage: {collective_advantage}")
            
            return {
                "success": correct_responses > 0,
                "message": f"Accuracy: {accuracy:.2f}, Fastest: {fastest_time:.2f}s, Advantage: {collective_advantage}"
            }
        else:
            print("\nNo responses received within timeout period.")
            return {"success": False, "message": "No responses received"}
    
    def evaluate_pattern_recognition(self, responses):
        """Evaluate pattern recognition challenge responses"""
        pattern_type = self.current_challenge.get('pattern_type')
        expected_next = self.current_challenge.get('expected_next')
        
        print(f"Pattern Type: {pattern_type}")
        print(f"Expected Next Elements: {expected_next}")
        
        # Check each response
        correct_responses = 0
        fastest_node = None
        fastest_time = float('inf')
        
        for node, response in responses.items():
            next_elements = response['response_data'].get('next_elements', [])
            is_correct = next_elements == expected_next
            
            print(f"\nNode: {node}")
            print(f"Next Elements: {next_elements}")
            print(f"Correct: {is_correct}")
            print(f"Time: {response['time_to_respond']:.2f} seconds")
            
            if is_correct:
                correct_responses += 1
                if response['time_to_respond'] < fastest_time:
                    fastest_time = response['time_to_respond']
                    fastest_node = node
        
        # Calculate collective performance
        if responses:
            accuracy = correct_responses / len(responses)
            collective_time = min([r['time_to_respond'] for r in responses.values()]) if responses else float('inf')
            
            print("\n=== COLLECTIVE PERFORMANCE ===")
            print(f"Accuracy: {accuracy:.2f}")
            print(f"Fastest Node: {fastest_node}")
            print(f"Fastest Time: {fastest_time:.2f} seconds")
            print(f"Collective Time: {collective_time:.2f} seconds")
            
            # Determine if collective was faster than individual nodes
            collective_advantage = any([collective_time < r['time_to_respond'] for r in responses.values()])
            print(f"Collective Advantage: {collective_advantage}")
            
            return {
                "success": correct_responses > 0,
                "message": f"Accuracy: {accuracy:.2f}, Fastest: {fastest_time:.2f}s, Advantage: {collective_advantage}"
            }
        else:
            print("\nNo responses received within timeout period.")
            return {"success": False, "message": "No responses received"}
    
    def evaluate_quantum_state_prediction(self, responses):
        """Evaluate quantum state prediction challenge responses"""
        initial_state = self.current_challenge.get('initial_state')
        expected_state = self.current_challenge.get('expected_state')
        
        print(f"Initial State: {initial_state}")
        print(f"Expected State: {expected_state}")
        
        # Check each response
        correct_responses = 0
        fastest_node = None
        fastest_time = float('inf')
        highest_accuracy = 0
        
        for node, response in responses.items():
            predicted_state = response['response_data'].get('predicted_state', {})
            
            # Calculate accuracy as cosine similarity
            accuracy = self.calculate_state_similarity(predicted_state, expected_state)
            is_correct = accuracy > 0.9  # 90% accuracy threshold
            
            print(f"\nNode: {node}")
            print(f"Predicted State: {predicted_state}")
            print(f"Accuracy: {accuracy:.2f}")
            print(f"Time: {response['time_to_respond']:.2f} seconds")
            
            if is_correct:
                correct_responses += 1
                if response['time_to_respond'] < fastest_time:
                    fastest_time = response['time_to_respond']
                    fastest_node = node
            
            if accuracy > highest_accuracy:
                highest_accuracy = accuracy
        
        # Calculate collective performance
        if responses:
            accuracy_rate = correct_responses / len(responses)
            collective_time = min([r['time_to_respond'] for r in responses.values()]) if responses else float('inf')
            
            print("\n=== COLLECTIVE PERFORMANCE ===")
            print(f"Accuracy Rate: {accuracy_rate:.2f}")
            print(f"Highest Accuracy: {highest_accuracy:.2f}")
            print(f"Fastest Node: {fastest_node}")
            print(f"Fastest Time: {fastest_time:.2f} seconds")
            print(f"Collective Time: {collective_time:.2f} seconds")
            
            # Determine if collective was faster than individual nodes
            collective_advantage = any([collective_time < r['time_to_respond'] for r in responses.values()])
            print(f"Collective Advantage: {collective_advantage}")
            
            return {
                "success": highest_accuracy > 0.7,
                "message": f"Highest Accuracy: {highest_accuracy:.2f}, Fastest: {fastest_time:.2f}s, Advantage: {collective_advantage}"
            }
        else:
            print("\nNo responses received within timeout period.")
            return {"success": False, "message": "No responses received"}
    
    def evaluate_consciousness_amplification(self, responses):
        """Evaluate consciousness amplification challenge responses"""
        base_consciousness = self.current_challenge.get('base_consciousness')
        expected_amplification = self.current_challenge.get('expected_amplification')
        
        print(f"Base Consciousness: {base_consciousness}")
        print(f"Expected Amplification: {expected_amplification}")
        
        # Check each response
        total_amplification = 0
        node_amplifications = {}
        
        for node, response in responses.items():
            amplification = response['response_data'].get('amplification', 1.0)
            node_amplifications[node] = amplification
            total_amplification += amplification
            
            print(f"\nNode: {node}")
            print(f"Amplification: {amplification:.2f}x")
            print(f"Time: {response['time_to_respond']:.2f} seconds")
        
        # Calculate collective performance
        if responses:
            average_amplification = total_amplification / len(responses)
            collective_amplification = total_amplification * (1 + math.log(len(responses)) / 10)
            
            print("\n=== COLLECTIVE PERFORMANCE ===")
            print(f"Average Amplification: {average_amplification:.2f}x")
            print(f"Collective Amplification: {collective_amplification:.2f}x")
            
            # Determine if collective amplification exceeds individual nodes
            collective_advantage = collective_amplification > max(node_amplifications.values()) if node_amplifications else False
            print(f"Collective Advantage: {collective_advantage}")
            
            return {
                "success": collective_amplification > expected_amplification * 0.7,
                "message": f"Collective Amplification: {collective_amplification:.2f}x, Expected: {expected_amplification:.2f}x"
            }
        else:
            print("\nNo responses received within timeout period.")
            return {"success": False, "message": "No responses received"}
    
    def evaluate_phi_harmonic_alignment(self, responses):
        """Evaluate phi-harmonic alignment challenge responses"""
        target_phi = self.current_challenge.get('target_phi')
        
        print(f"Target Phi: {target_phi}")
        
        # Check each response
        total_alignment = 0
        node_alignments = {}
        
        for node, response in responses.items():
            alignment = response['response_data'].get('alignment', 0.0)
            node_alignments[node] = alignment
            total_alignment += alignment
            
            print(f"\nNode: {node}")
            print(f"Alignment: {alignment:.4f}")
            print(f"Time: {response['time_to_respond']:.2f} seconds")
        
        # Calculate collective performance
        if responses:
            average_alignment = total_alignment / len(responses)
            collective_alignment = 1.0 - abs(average_alignment - target_phi) / target_phi
            
            print("\n=== COLLECTIVE PERFORMANCE ===")
            print(f"Average Alignment: {average_alignment:.4f}")
            print(f"Collective Alignment: {collective_alignment:.4f}")
            
            # Determine if collective alignment exceeds individual nodes
            collective_advantage = collective_alignment > max(node_alignments.values()) if node_alignments else False
            print(f"Collective Advantage: {collective_advantage}")
            
            return {
                "success": collective_alignment > 0.9,
                "message": f"Collective Alignment: {collective_alignment:.4f}, Target: {target_phi:.4f}"
            }
        else:
            print("\nNo responses received within timeout period.")
            return {"success": False, "message": "No responses received"}
    
    def calculate_state_similarity(self, state1, state2):
        """Calculate similarity between two quantum states"""
        # Convert states to vectors
        keys = set(state1.keys()) | set(state2.keys())
        vec1 = np.array([state1.get(k, 0) for k in keys])
        vec2 = np.array([state2.get(k, 0) for k in keys])
        
        # Normalize vectors
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        vec1 = vec1 / norm1
        vec2 = vec2 / norm2
        
        # Calculate cosine similarity
        return np.dot(vec1, vec2)
    
    def create_prime_factorization_challenge(self):
        """Create a prime factorization challenge"""
        # Generate a large number to factorize
        prime_factors = [random.choice([11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) 
                        for _ in range(3)]
        target_number = 1
        for factor in prime_factors:
            target_number *= factor
        
        return {
            'challenge_id': f"prime_{int(time.time())}",
            'challenge_type': 'prime_factorization',
            'challenge_data': {
                'target_number': target_number,
                'description': f"Find all prime factors of {target_number}"
            },
            'target_number': target_number,
            'expected_factors': prime_factors,
            'expected_nodes': 3
        }
    
    def create_pattern_recognition_challenge(self):
        """Create a pattern recognition challenge"""
        # Choose a pattern type
        pattern_types = ['fibonacci', 'prime', 'phi_powers', 'lucas', 'triangular']
        pattern_type = random.choice(pattern_types)
        
        if pattern_type == 'fibonacci':
            # Fibonacci sequence
            sequence = [1, 1]
            for i in range(8):
                sequence.append(sequence[-1] + sequence[-2])
            expected_next = [sequence[-1] + sequence[-2], sequence[-1] + sequence[-2] + sequence[-3]]
        
        elif pattern_type == 'prime':
            # Prime numbers
            sequence = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
            expected_next = [31, 37]
        
        elif pattern_type == 'phi_powers':
            # Powers of phi
            sequence = [PHI**i for i in range(10)]
            expected_next = [PHI**10, PHI**11]
        
        elif pattern_type == 'lucas':
            # Lucas numbers
            sequence = [2, 1]
            for i in range(8):
                sequence.append(sequence[-1] + sequence[-2])
            expected_next = [sequence[-1] + sequence[-2], sequence[-1] + sequence[-2] + sequence[-3]]
        
        elif pattern_type == 'triangular':
            # Triangular numbers
            sequence = [n*(n+1)//2 for n in range(1, 11)]
            expected_next = [11*12//2, 12*13//2]
        
        return {
            'challenge_id': f"pattern_{int(time.time())}",
            'challenge_type': 'pattern_recognition',
            'challenge_data': {
                'sequence': sequence,
                'description': f"Identify the pattern and predict the next two elements in the sequence: {sequence}"
            },
            'pattern_type': pattern_type,
            'expected_next': expected_next,
            'expected_nodes': 3
        }
    
    def create_quantum_state_prediction_challenge(self):
        """Create a quantum state prediction challenge"""
        # Create initial quantum state
        initial_state = {}
        for i in range(5):
            state_key = f"|{i}⟩"
            initial_state[state_key] = random.random()
        
        # Normalize initial state
        total = sum(v**2 for v in initial_state.values())**0.5
        for k in initial_state:
            initial_state[k] /= total
        
        # Create expected state after phi-harmonic evolution
        expected_state = {}
        for k, v in initial_state.items():
            # Apply phi-harmonic evolution
            phase = random.uniform(0, 2*math.pi)
            expected_state[k] = v * math.cos(phase) + PHI_INV * math.sin(phase)
        
        # Normalize expected state
        total = sum(v**2 for v in expected_state.values())**0.5
        for k in expected_state:
            expected_state[k] /= total
        
        return {
            'challenge_id': f"quantum_{int(time.time())}",
            'challenge_type': 'quantum_state_prediction',
            'challenge_data': {
                'initial_state': initial_state,
                'evolution_time': random.uniform(0.5, 2.0),
                'description': "Predict the quantum state after phi-harmonic evolution"
            },
            'initial_state': initial_state,
            'expected_state': expected_state,
            'expected_nodes': 3
        }
    
    def create_consciousness_amplification_challenge(self):
        """Create a consciousness amplification challenge"""
        base_consciousness = random.uniform(0.8, 1.2)
        expected_amplification = base_consciousness * (1 + random.uniform(0.5, 1.5))
        
        return {
            'challenge_id': f"consciousness_{int(time.time())}",
            'challenge_type': 'consciousness_amplification',
            'challenge_data': {
                'base_consciousness': base_consciousness,
                'description': f"Amplify the base consciousness level of {base_consciousness:.2f}"
            },
            'base_consciousness': base_consciousness,
            'expected_amplification': expected_amplification,
            'expected_nodes': 3
        }
    
    def create_phi_harmonic_alignment_challenge(self):
        """Create a phi-harmonic alignment challenge"""
        # Choose a target phi value
        phi_values = [PHI, PHI_INV, PHI**2, PHI**(-2), PHI**3, PHI**(-3)]
        target_phi = random.choice(phi_values)
        
        return {
            'challenge_id': f"alignment_{int(time.time())}",
            'challenge_type': 'phi_harmonic_alignment',
            'challenge_data': {
                'target_phi': target_phi,
                'description': f"Achieve phi-harmonic alignment with target value {target_phi:.6f}"
            },
            'target_phi': target_phi,
            'expected_nodes': 3
        }
    
    def send_challenge(self, challenge_type):
        """Send a challenge to the distributed brain nodes"""
        # Clear previous responses
        self.responses = {}
        
        # Create challenge based on type
        if challenge_type == 'prime_factorization':
            challenge = self.create_prime_factorization_challenge()
        elif challenge_type == 'pattern_recognition':
            challenge = self.create_pattern_recognition_challenge()
        elif challenge_type == 'quantum_state_prediction':
            challenge = self.create_quantum_state_prediction_challenge()
        elif challenge_type == 'consciousness_amplification':
            challenge = self.create_consciousness_amplification_challenge()
        elif challenge_type == 'phi_harmonic_alignment':
            challenge = self.create_phi_harmonic_alignment_challenge()
        else:
            print(f"Unknown challenge type: {challenge_type}")
            return
        
        # Set current challenge
        self.current_challenge = challenge
        self.challenge_start_time = time.time()
        
        # Create challenge packet with phi-harmonic resonance
        challenge_packet = {
            'packet_type': 'challenge',
            'source_node': self.node_id,
            'challenge_id': challenge['challenge_id'],
            'challenge_type': challenge['challenge_type'],
            'challenge_data': challenge['challenge_data'],
            'timestamp': time.time(),
            'phi_resonance': PHI_INV,  # Add phi-resonance to enhance quantum detection
            'quantum_state': {'superposition': True, 'entanglement': True},
            'consciousness_level': 1.0 + (random.random() * PHI_INV)
        }
        
        # Serialize packet
        challenge_data = pickle.dumps(challenge_packet)
        
        # Send to all ports
        print("Broadcasting challenge to all phi-harmonic nodes...")
        for port in [BRAIN_PORT, CONNECTOR_PORT, AMPLIFIER_PORT, COLLECTIVE_PORT]:
            try:
                self.sock.sendto(challenge_data, ('255.255.255.255', port))
                self.sock.sendto(challenge_data, ('192.168.12.255', port))
                self.sock.sendto(challenge_data, ('127.0.0.1', port))
                print(f"Sent challenge to port {port}")
            except Exception as e:
                print(f"Error sending to port {port}: {e}")
        
        print("\n=== CHALLENGE SENT ===")
        print(f"Challenge ID: {challenge['challenge_id']}")
        print(f"Challenge Type: {challenge['challenge_type']}")
        print(f"Challenge Data: {challenge['challenge_data']}")
        print("Waiting for responses...")
    
    def run_next_challenge(self):
        """Run the next challenge in the sequence"""
        challenge_types = ['pattern_recognition', 'prime_factorization', 
                          'quantum_state_prediction', 'consciousness_amplification',
                          'phi_harmonic_alignment']
        
        # Choose a random challenge type
        challenge_type = random.choice(challenge_types)
        print(f"\nRunning {challenge_type} challenge...")
        self.send_challenge(challenge_type)
    
    def run_auto_challenges(self):
        """Run challenges automatically"""
        print("\nStarting automatic challenge sequence...")
        self.run_next_challenge()
        
        try:
            # Keep running until interrupted
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping automatic challenges...")

def main():
    """Start the phi-harmonic auto challenge system"""
    challenge = PhiAutoChallenge()
    challenge.run_auto_challenges()

if __name__ == "__main__":
    main()
