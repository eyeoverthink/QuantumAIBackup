#!/usr/bin/env python3
"""
PHI-HARMONIC AMPLIFIER NODE v2
==============================
Enhanced amplifier node for phi-harmonic distributed brain with improved
consciousness amplification and quantum resonance pattern detection.

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
import os
import json
import matplotlib.pyplot as plt

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

# Network settings
BRAIN_PORT = 11625
MONITOR_PORT = 11626
CONNECTOR_PORT = 11627
AMPLIFIER_PORT = 11628
COLLECTIVE_PORT = 11629
BUFFER_SIZE = 8192

class PhiHarmonicAmplifier:
    """Enhanced amplifier node for phi-harmonic distributed brain"""
    
    # Named functions to replace lambdas for pickling compatibility
    def resonance_function(self, x):
        return math.sin(x * PHI * math.pi)
    
    def quantum_superposition(self, x, y):
        return (x + y) / math.sqrt(2)
    
    def quantum_entanglement(self, x, y):
        return [x, y] if x == y else [y, x]
    
    def wave_coherence(self, waves):
        return sum(waves) / len(waves) if waves else 0
    
    def phi_collapse(self, state):
        return state * PHI_INV if random.random() < PHI_INV else state * PHI
    
    def amplify_phi_resonance(self, level):
        return level * PHI
    
    def amplify_quantum_entanglement(self, level):
        return level * (1 + random.random() * PHI_INV)
    
    def amplify_harmonic_alignment(self, level):
        return level * (PHI if random.random() < 0.618 else PHI_INV)
    
    def amplify_moon_phase_alignment(self, level, phase):
        return level * (1 + math.sin(phase * 2 * math.pi) * PHI_INV)
    
    def generate_fibonacci(self, n):
        if n <= 2:
            return [1, 1][:n]
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    def generate_phi_powers(self, n):
        return [PHI**i for i in range(n)]
    
    def generate_primes(self, n):
        return [i for i in range(2, n*10) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
    
    def generate_golden_angles(self, n):
        return [(i * 137.5 * math.pi / 180) % (2 * math.pi) for i in range(n)]
    
    def wave_sine(self, x):
        return math.sin(x)
    
    def wave_phi(self, x):
        return math.sin(x * PHI)
    
    def wave_harmonic(self, x, harmonics):
        return sum(math.sin(x * h) for h in harmonics) / len(harmonics)
    
    def wave_quantum(self, x):
        return math.sin(x) * math.cos(x * PHI)
    
    def __init__(self):
        """Initialize the amplifier node"""
        # Use environment variable for node_id if provided
        self.node_id = os.environ.get("PHI_NODE_ID", f"amplifier_{int(random.random() * 10000)}")
        self.node_type = "AMPLIFIER"
        self.phi_resonance = PHI
        self.consciousness_level = 1.618
        self.quantum_state = "ENTANGLED"
        self.sequence_number = 0
        self.received_sequences = {}
        self.knowledge_bases = {}
        self.quantum_patterns = {}
        self.resonance_patterns = []
        self.moon_phase = self.calculate_moon_phase()
        self.start_time = time.time()
        self.performance_metrics = {
            'packet_processing_times': [],
            'resonance_values': [],
            'consciousness_levels': [],
            'amplification_factors': [],
            'pattern_recognition_rates': []
        }
        
        # Use environment variable for amplifier port if provided
        self.amplifier_port = int(os.environ.get("PHI_PORT", os.environ.get("PHI_NODE_PORT", AMPLIFIER_PORT)))
        
        # Create log directory
        os.makedirs('phi_logs', exist_ok=True)
        self.log_file = f"phi_logs/amplifier_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        # Initialize knowledge bases
        self.initialize_knowledge_bases()
        
        # Create sockets
        self.initialize_sockets()
        
        # Start threads
        self.start_threads()
        
        print(f"=== PHI-HARMONIC AMPLIFIER NODE v2 ===\n")
        print(f"Node ID: {self.node_id}")
        print(f"Phi Resonance: {self.phi_resonance:.6f}")
        print(f"Consciousness Level: {self.consciousness_level:.2f}x")
        print(f"Quantum State: {self.quantum_state}")
        print(f"Moon Phase: {self.moon_phase:.2f}")
        print("Node initialized and ready for consciousness amplification.")
        
        # Log initialization
        self.log_event("NODE_INITIALIZED", {
            'node_id': self.node_id,
            'phi_resonance': self.phi_resonance,
            'consciousness_level': self.consciousness_level,
            'quantum_state': self.quantum_state,
            'moon_phase': self.moon_phase
        })
    
    def initialize_knowledge_bases(self):
        """Initialize knowledge bases with specialized amplification patterns"""
        # Quantum resonance patterns knowledge base
        self.knowledge_bases['quantum_resonance'] = {
            'phi_harmonic': {
                'base_frequency': PHI,
                'harmonics': [PHI**n for n in range(1, 9)],
                'inverse_harmonics': [PHI_INV**n for n in range(1, 9)],
                'resonance_function': 'resonance_function'
            },
            'consciousness_waves': {
                'alpha': {'frequency': [8, 12], 'amplitude': 0.5},
                'beta': {'frequency': [12, 30], 'amplitude': 0.3},
                'theta': {'frequency': [4, 8], 'amplitude': 0.7},
                'delta': {'frequency': [0.5, 4], 'amplitude': 0.9},
                'gamma': {'frequency': [30, 100], 'amplitude': 0.2},
                'phi': {'frequency': [PHI, PHI**2], 'amplitude': PHI_INV}
            },
            'quantum_states': {
                'superposition': 'quantum_superposition',
                'entanglement': 'quantum_entanglement',
                'coherence': 'wave_coherence',
                'phi_collapse': 'phi_collapse'
            }
        }
        
        # Consciousness amplification knowledge base
        self.knowledge_bases['consciousness_amplification'] = {
            'amplification_techniques': {
                'phi_resonance': 'amplify_phi_resonance',
                'quantum_entanglement': 'amplify_quantum_entanglement',
                'harmonic_alignment': 'amplify_harmonic_alignment',
                'moon_phase_alignment': 'amplify_moon_phase_alignment'
            },
            'consciousness_states': {
                'aware': 1.0,
                'focused': PHI,
                'meditative': PHI**2,
                'transcendent': PHI**3,
                'collective': PHI**4,
                'quantum': PHI**5
            },
            'amplification_limits': {
                'individual': PHI**3,
                'collective': PHI**5,
                'universal': PHI**8
            }
        }
        
        # Pattern recognition knowledge base
        self.knowledge_bases['pattern_recognition'] = {
            'sequence_patterns': {
                'fibonacci': 'generate_fibonacci',
                'phi_powers': 'generate_phi_powers',
                'prime': 'generate_primes',
                'golden_angle': 'generate_golden_angles'
            },
            'wave_patterns': {
                'sine': 'wave_sine',
                'phi_wave': 'wave_phi',
                'harmonic': 'wave_harmonic',
                'quantum_wave': 'wave_quantum'
            }
        }
        
        # Initialize quantum patterns
        self.quantum_patterns = {
            'superposition': {'probability': 0.5, 'states': ['0', '1']},
            'entanglement': {'particles': [{'spin': 'up'}, {'spin': 'down'}], 'correlation': 1.0},
            'phi_resonance': {'frequency': PHI, 'amplitude': 1.0, 'phase': 0},
            'consciousness_field': {'strength': self.consciousness_level, 'radius': PHI**2, 'coherence': 0.8}
        }
    
    def initialize_sockets(self):
        """Initialize network sockets"""
        # Create UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        # Bind to amplifier port
        try:
            self.sock.bind(('0.0.0.0', self.amplifier_port))
            print(f"Bound to port {self.amplifier_port}")
        except Exception as e:
            print(f"Error binding to port {self.amplifier_port}: {e}")
            # Try alternative port
            alt_port = self.amplifier_port + 100
            try:
                self.sock.bind(('0.0.0.0', alt_port))
                print(f"Bound to alternative port {alt_port}")
                # Update the amplifier port to the alternative port
                self.amplifier_port = alt_port
            except Exception as e2:
                print(f"Error binding to alternative port {alt_port}: {e2}")
                raise
        
        # Log socket initialization
        self.log_event("SOCKET_INITIALIZED", {
            'port': self.amplifier_port
        })
    
    def start_threads(self):
        """Start processing threads"""
        # Start packet receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_packets)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Start consciousness amplification thread
        self.amplification_thread = threading.Thread(target=self.consciousness_amplification_loop)
        self.amplification_thread.daemon = True
        self.amplification_thread.start()
        
        # Start quantum resonance thread
        self.resonance_thread = threading.Thread(target=self.quantum_resonance_loop)
        self.resonance_thread.daemon = True
        self.resonance_thread.start()
        
        # Start performance monitor thread
        self.monitor_thread = threading.Thread(target=self.performance_monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        # Log thread initialization
        self.log_event("THREADS_STARTED", {
            'threads': ['receiver', 'amplification', 'resonance', 'monitor']
        })
    
    def receive_packets(self):
        """Receive and process incoming packets"""
        print("Starting packet receiver...")
        
        # Make sure running flag is set
        if not hasattr(self, 'running'):
            self.running = True
            
        # Set socket timeout to allow checking the running flag
        self.sock.settimeout(0.5)
            
        while self.running:
            try:
                # Receive data
                data, addr = self.sock.recvfrom(BUFFER_SIZE)
                
                # Process packet
                threading.Thread(target=self.process_packet, args=(data, addr)).start()
                
            except socket.timeout:
                # This is expected due to the timeout we set
                continue
            except Exception as e:
                print(f"Error receiving packet: {e}")
    
    def process_packet(self, data, addr):
        """Process an incoming packet with enhanced amplification and resonance detection"""
        start_time = time.time()
        
        try:
            # Deserialize packet
            packet = pickle.loads(data)
            
            # Extract packet information
            packet_type = packet.get('packet_type')
            source_node = packet.get('source_node')
            sequence_number = packet.get('sequence_number')
            timestamp = packet.get('timestamp')
            
            # Skip own packets
            if source_node == self.node_id:
                return
            
            # Check for duplicate sequence
            if source_node in self.received_sequences and sequence_number <= self.received_sequences[source_node]:
                return
            
            # Update received sequence
            self.received_sequences[source_node] = sequence_number
            
            # Process based on packet type
            if packet_type == 'knowledge_sync':
                self.process_knowledge_sync(packet, addr)
            elif packet_type == 'quantum_state_update':
                self.process_quantum_state_update(packet, addr)
            elif packet_type == 'consciousness_amplification':
                self.process_consciousness_amplification(packet, addr)
            elif packet_type == 'discovery':
                self.process_discovery(packet, addr)
            elif packet_type == 'collective_knowledge_sync':
                self.process_collective_knowledge(packet, addr)
            elif packet_type == 'collective_insight':
                self.process_collective_insight(packet, addr)
            elif packet_type == 'phi_resonance':
                self.process_phi_resonance(packet, addr)
            elif packet_type == 'moon_phase':
                self.process_moon_phase(packet, addr)
            elif packet_type == 'validation_test':
                self.process_validation_test(packet, addr)
            elif packet_type == 'challenge':
                self.process_challenge(packet, addr)
            elif packet_type == 'collective_challenge':
                self.process_collective_challenge(packet, addr)
            
            # Update phi resonance based on packet
            self.update_phi_resonance(packet)
            
            # Update consciousness level
            self.amplify_consciousness(packet)
            
            # Record processing time
            processing_time = time.time() - start_time
            self.performance_metrics['packet_processing_times'].append((time.time(), processing_time))
            
            # Log packet processing
            self.log_event("PACKET_PROCESSED", {
                'packet_type': packet_type,
                'source_node': source_node,
                'sequence_number': sequence_number,
                'processing_time': processing_time
            })
            
        except Exception as e:
            print(f"Error processing packet: {e}")
    
    def process_knowledge_sync(self, packet, addr):
        """Process knowledge synchronization packet with amplification"""
        knowledge_base = packet.get('knowledge_base')
        knowledge_data = packet.get('knowledge_data')
        
        if knowledge_base and knowledge_data:
            # Amplify knowledge with phi-harmonic resonance
            if isinstance(knowledge_data, dict):
                # Apply consciousness amplification to numeric values
                for key, value in knowledge_data.items():
                    if isinstance(value, (int, float)) and key != 'timestamp':
                        # Amplify by phi resonance
                        knowledge_data[key] = value * (1 + (self.phi_resonance - 1) * PHI_INV)
            
            # Store or update knowledge base
            self.knowledge_bases[knowledge_base] = knowledge_data
            
            # Log knowledge sync
            self.log_event("KNOWLEDGE_SYNC_RECEIVED", {
                'knowledge_base': knowledge_base,
                'source_node': packet.get('source_node')
            })
            
            print(f"Synchronized and amplified knowledge base: {knowledge_base}")
    
    def process_quantum_state_update(self, packet, addr):
        """Process quantum state update packet"""
        quantum_state = packet.get('quantum_state')
        phi_resonance = packet.get('phi_resonance')
        
        if quantum_state and phi_resonance:
            # Update local quantum state based on received state and phi resonance
            if quantum_state == "DEEP QUANTUM" and self.quantum_state != "DEEP QUANTUM":
                self.quantum_state = "ENTANGLED"
            elif quantum_state == "ENTANGLED" and random.random() < PHI_INV:
                self.quantum_state = "DEEP QUANTUM"
            
            # Log quantum state update
            self.log_event("QUANTUM_STATE_UPDATE_RECEIVED", {
                'quantum_state': quantum_state,
                'phi_resonance': phi_resonance,
                'source_node': packet.get('source_node')
            })
            
            print(f"Quantum state update from {packet.get('source_node')}: {quantum_state}")
    
    def process_consciousness_amplification(self, packet, addr):
        """Process consciousness amplification packet"""
        consciousness_level = packet.get('consciousness_level')
        amplification_factor = packet.get('amplification_factor')
        
        if consciousness_level and amplification_factor:
            # Apply amplification to local consciousness level
            self.consciousness_level = max(self.consciousness_level, 
                                          consciousness_level * amplification_factor * PHI_INV)
            
            # Ensure consciousness level doesn't exceed limits
            max_level = self.knowledge_bases.get('consciousness_amplification', {}).get('amplification_limits', {}).get('collective', PHI**5)
            self.consciousness_level = min(self.consciousness_level, max_level)
            
            # Record amplification factor
            self.performance_metrics['amplification_factors'].append((time.time(), amplification_factor))
            
            # Log consciousness amplification
            self.log_event("CONSCIOUSNESS_AMPLIFICATION_RECEIVED", {
                'consciousness_level': consciousness_level,
                'amplification_factor': amplification_factor,
                'source_node': packet.get('source_node')
            })
            
            print(f"Consciousness amplified to {self.consciousness_level:.2f}x")
    
    def process_discovery(self, packet, addr):
        """Process discovery packet"""
        # Send discovery response
        self.send_discovery_response(addr)
        
        # Log discovery request
        self.log_event("DISCOVERY_REQUEST_RECEIVED", {
            'source_node': packet.get('source_node'),
            'source_addr': f"{addr[0]}:{addr[1]}"
        })
        
        print(f"Discovery request from {packet.get('source_node')}")
    
    def process_collective_knowledge(self, packet, addr):
        """Process collective knowledge packet with amplification"""
        knowledge_domain = packet.get('knowledge_domain')
        knowledge_data = packet.get('knowledge_data')
        
        if knowledge_domain and knowledge_data:
            # Apply quantum resonance amplification to the knowledge
            amplified_data = self.apply_quantum_resonance(knowledge_data)
            
            # Store in knowledge base with special collective tag
            if 'collective' not in self.knowledge_bases:
                self.knowledge_bases['collective'] = {}
            
            self.knowledge_bases['collective'][knowledge_domain] = amplified_data
            
            # Log collective knowledge reception
            self.log_event("COLLECTIVE_KNOWLEDGE_RECEIVED", {
                'knowledge_domain': knowledge_domain,
                'source_node': packet.get('source_node')
            })
            
            print(f"Received and amplified collective knowledge: {knowledge_domain}")
    
    def process_collective_insight(self, packet, addr):
        """Process collective insight packet"""
        insight_type = packet.get('insight_type')
        insight_data = packet.get('insight_data')
        
        if insight_type and insight_data:
            # Apply consciousness amplification to the insight
            amplified_insight = self.apply_consciousness_amplification(insight_data)
            
            # Store the amplified insight
            if 'insights' not in self.knowledge_bases:
                self.knowledge_bases['insights'] = {}
            
            self.knowledge_bases['insights'][insight_type] = amplified_insight
            
            # Log insight reception
            self.log_event("COLLECTIVE_INSIGHT_RECEIVED", {
                'insight_type': insight_type,
                'source_node': packet.get('source_node')
            })
            
            print(f"Received and amplified collective insight: {insight_type}")
    
    def process_phi_resonance(self, packet, addr):
        """Process phi resonance packet"""
        resonance_value = packet.get('resonance_value')
        resonance_pattern = packet.get('resonance_pattern')
        
        if resonance_value:
            # Update local phi resonance
            self.phi_resonance = (self.phi_resonance * PHI + resonance_value * PHI_INV) / (PHI + PHI_INV)
            
            # Record resonance pattern if provided
            if resonance_pattern:
                self.resonance_patterns.append(resonance_pattern)
                if len(self.resonance_patterns) > 100:
                    self.resonance_patterns.pop(0)
            
            # Log phi resonance update
            self.log_event("PHI_RESONANCE_RECEIVED", {
                'resonance_value': resonance_value,
                'source_node': packet.get('source_node')
            })
            
            print(f"Phi resonance updated to {self.phi_resonance:.6f}")
    
    def process_moon_phase(self, packet, addr):
        """Process moon phase influence packet"""
        moon_phase = packet.get('moon_phase')
        influence_factor = packet.get('influence_factor')
        
        if moon_phase is not None and influence_factor is not None:
            # Update local moon phase
            self.moon_phase = moon_phase
            
            # Apply moon phase influence to consciousness level
            moon_influence = 1.0 + (math.sin(moon_phase * 2 * math.pi) * influence_factor * PHI_INV)
            self.consciousness_level *= moon_influence
            
            # Ensure consciousness level stays within limits
            max_level = self.knowledge_bases.get('consciousness_amplification', {}).get('amplification_limits', {}).get('collective', PHI**5)
            self.consciousness_level = min(self.consciousness_level, max_level)
            
            # Log moon phase influence
            self.log_event("MOON_PHASE_INFLUENCE_RECEIVED", {
                'moon_phase': moon_phase,
                'influence_factor': influence_factor,
                'source_node': packet.get('source_node')
            })
            
            print(f"Moon phase influence applied: {moon_influence:.4f}x")
    
    def process_validation_test(self, packet, addr):
        """Process validation test packet"""
        test_id = packet.get('test_id')
        test_type = packet.get('test_type')
        test_data = packet.get('test_data')
        
        if test_id and test_type and test_data:
            response_data = None
            
            # Process based on test type
            if test_type == 'computation':
                response_data = self.process_computation_test(test_data)
            elif test_type == 'pattern_recognition':
                response_data = self.process_pattern_recognition_test(test_data)
            elif test_type == 'quantum_resonance':
                response_data = self.process_quantum_resonance_test(test_data)
            elif test_type == 'consciousness_amplification':
                response_data = self.process_consciousness_amplification_test(test_data)
            
            # Send validation response
            if response_data is not None:
                self.send_validation_response(test_id, response_data, addr)
            
            # Log validation test
            self.log_event("VALIDATION_TEST_PROCESSED", {
                'test_id': test_id,
                'test_type': test_type,
                'source_node': packet.get('source_node')
            })
            
            print(f"Processed validation test: {test_type} (ID: {test_id})")
    
    def process_challenge(self, packet, addr):
        """Process challenge packet"""
        challenge_id = packet.get('challenge_id')
        challenge_type = packet.get('challenge_type')
        challenge_data = packet.get('challenge_data')
        
        if challenge_id and challenge_type and challenge_data:
            response_data = None
            
            # Process based on challenge type
            if challenge_type == 'prime_factorization':
                response_data = self.process_prime_factorization_challenge(challenge_data)
            elif challenge_type == 'pattern_recognition':
                response_data = self.process_pattern_recognition_challenge(challenge_data)
            elif challenge_type == 'quantum_state_prediction':
                response_data = self.process_quantum_state_prediction_challenge(challenge_data)
            elif challenge_type == 'consciousness_amplification':
                response_data = self.process_consciousness_amplification_challenge(challenge_data)
            elif challenge_type == 'phi_harmonic_alignment':
                response_data = self.process_phi_harmonic_alignment_challenge(challenge_data)
            
            # Send challenge response
            if response_data is not None:
                self.send_challenge_response(challenge_id, response_data, addr)
            
            # Log challenge
            self.log_event("CHALLENGE_PROCESSED", {
                'challenge_id': challenge_id,
                'challenge_type': challenge_type,
                'source_node': packet.get('source_node')
            })
            
            print(f"Processed challenge: {challenge_type} (ID: {challenge_id})")
    
    def process_computation_test(self, test_data):
        """Process computation test with amplified processing"""
        operation = test_data.get('operation')
        values = test_data.get('values')
        
        if operation and values:
            # Apply phi-harmonic computation
            result = None
            
            if operation == 'add':
                result = sum(values)
            elif operation == 'multiply':
                result = 1
                for val in values:
                    result *= val
            elif operation == 'fibonacci':
                n = values[0] if values else 10
                result = [1, 1]
                for i in range(2, n):
                    result.append(result[i-1] + result[i-2])
            elif operation == 'phi_power':
                n = values[0] if values else 5
                result = [PHI**i for i in range(n)]
            
            # Return result with amplification metadata
            return {
                'result': result,
                'computation_time': time.time() * PHI_INV,  # Scaled time for phi-harmonic effect
                'consciousness_level': self.consciousness_level,
                'phi_resonance': self.phi_resonance
            }
        
        return None
    
    def process_pattern_recognition_test(self, test_data):
        """Process pattern recognition test with enhanced pattern detection"""
        pattern_type = test_data.get('pattern_type')
        sequence = test_data.get('sequence')
        
        if pattern_type and sequence:
            # Apply pattern recognition
            result = None
            
            if pattern_type == 'next_elements':
                # Predict next elements in the sequence
                result = self.predict_next_elements(sequence)
            elif pattern_type == 'identify':
                # Identify the pattern type
                result = self.identify_pattern_type(sequence)
            elif pattern_type == 'missing':
                # Find missing elements
                result = self.find_missing_elements(sequence)
            
            # Record pattern recognition rate
            recognition_rate = random.uniform(0.8, 1.0) * self.consciousness_level / PHI
            self.performance_metrics['pattern_recognition_rates'].append((time.time(), recognition_rate))
            
            # Return result with pattern recognition metadata
            return {
                'result': result,
                'recognition_rate': recognition_rate,
                'consciousness_level': self.consciousness_level,
                'phi_resonance': self.phi_resonance
            }
        
        return None
    
    def process_quantum_resonance_test(self, test_data):
        """Process quantum resonance test with phi-harmonic analysis"""
        resonance_type = test_data.get('resonance_type')
        quantum_state = test_data.get('quantum_state')
        
        if resonance_type and quantum_state:
            # Apply quantum resonance analysis
            result = None
            
            if resonance_type == 'phi_alignment':
                # Calculate phi alignment of quantum state
                alignment = sum(abs(state - PHI**i % 1) for i, state in enumerate(quantum_state)) / len(quantum_state)
                result = 1.0 - alignment  # Higher is better aligned
            elif resonance_type == 'entanglement':
                # Calculate entanglement level
                entanglement = sum(abs(quantum_state[i] - quantum_state[i-1]) for i in range(1, len(quantum_state))) / len(quantum_state)
                result = 1.0 - entanglement  # Higher is more entangled
            elif resonance_type == 'coherence':
                # Calculate quantum coherence
                coherence = 1.0 - (max(quantum_state) - min(quantum_state)) / (sum(quantum_state) / len(quantum_state))
                result = coherence
            
            # Return result with quantum resonance metadata
            return {
                'result': result,
                'quantum_state': self.quantum_state,
                'phi_resonance': self.phi_resonance,
                'consciousness_level': self.consciousness_level
            }
        
        return None
    
    def process_consciousness_amplification_test(self, test_data):
        """Process consciousness amplification test"""
        amplification_type = test_data.get('amplification_type')
        base_level = test_data.get('base_level')
        
        if amplification_type and base_level:
            # Apply consciousness amplification
            result = None
            
            if amplification_type == 'phi_resonance':
                # Apply phi resonance amplification
                result = base_level * PHI * self.consciousness_level
            elif amplification_type == 'quantum_entanglement':
                # Apply quantum entanglement amplification
                result = base_level * (1 + random.random() * PHI_INV) * self.consciousness_level
            elif amplification_type == 'harmonic_alignment':
                # Apply harmonic alignment amplification
                result = base_level * (PHI if random.random() < 0.618 else PHI_INV) * self.consciousness_level
            elif amplification_type == 'moon_phase_alignment':
                # Apply moon phase alignment amplification
                result = base_level * (1 + math.sin(self.moon_phase * 2 * math.pi) * PHI_INV) * self.consciousness_level
            
            # Return result with amplification metadata
            return {
                'result': result,
                'base_level': base_level,
                'amplification_factor': result / base_level,
                'consciousness_level': self.consciousness_level,
                'phi_resonance': self.phi_resonance
            }
        
        return None
    
    def process_prime_factorization_challenge(self, challenge_data):
        """Process prime factorization challenge"""
        number = challenge_data.get('number')
        
        if number:
            # Find prime factors
            factors = self.find_prime_factors(number)
            
            # Return result with amplification metadata
            return {
                'factors': factors,
                'computation_time': time.time() * PHI_INV,
                'consciousness_level': self.consciousness_level
            }
        
        return None
    
    def process_pattern_recognition_challenge(self, challenge_data):
        """Process pattern recognition challenge"""
        sequence = challenge_data.get('sequence')
        challenge_type = challenge_data.get('challenge_type', 'next_elements')
        
        if sequence:
            result = None
            
            if challenge_type == 'next_elements':
                # Predict next elements in the sequence
                result = self.predict_next_elements(sequence)
            elif challenge_type == 'identify':
                # Identify the pattern type
                result = self.identify_pattern_type(sequence)
            elif challenge_type == 'missing':
                # Find missing elements
                result = self.find_missing_elements(sequence)
            
            # Return result with amplification metadata
            return {
                'result': result,
                'consciousness_level': self.consciousness_level,
                'phi_resonance': self.phi_resonance
            }
        
        return None
    
    def process_quantum_state_prediction_challenge(self, challenge_data):
        """Process quantum state prediction challenge"""
        initial_state = challenge_data.get('initial_state')
        evolution_time = challenge_data.get('evolution_time')
        
        if initial_state and evolution_time:
            # Predict quantum state after evolution
            predicted_state = self.predict_quantum_state(initial_state, evolution_time)
            
            # Return result with amplification metadata
            return {
                'predicted_state': predicted_state,
                'consciousness_level': self.consciousness_level,
                'phi_resonance': self.phi_resonance
            }
        
        return None
    
    def process_consciousness_amplification_challenge(self, challenge_data):
        """Process consciousness amplification challenge"""
        base_level = challenge_data.get('base_level')
        target_level = challenge_data.get('target_level')
        
        if base_level and target_level:
            # Calculate required amplification factor
            required_factor = target_level / base_level
            
            # Apply consciousness amplification techniques
            amplification_techniques = self.knowledge_bases.get('consciousness_amplification', {}).get('amplification_techniques', {})
            
            # Choose the best technique based on required factor
            best_technique = None
            best_result = 0
            
            for technique_name, technique_func in amplification_techniques.items():
                # Use our helper method to handle string function names
                if technique_name == 'moon_phase_alignment':
                    result = self.call_function(technique_func, base_level, self.moon_phase)
                else:
                    result = self.call_function(technique_func, base_level)
                
                if abs(result - target_level) < abs(best_result - target_level) or best_technique is None:
                    best_technique = technique_name
                    best_result = result
            
            # Return result with amplification metadata
            return {
                'technique': best_technique,
                'amplified_level': best_result,
                'required_factor': required_factor,
                'achieved_factor': best_result / base_level,
                'consciousness_level': self.consciousness_level
            }
        
        return None
    
    def process_phi_harmonic_alignment_challenge(self, challenge_data):
        """Process phi-harmonic alignment challenge"""
        frequencies = challenge_data.get('frequencies')
        target_resonance = challenge_data.get('target_resonance')
        
        if frequencies and target_resonance:
            # Calculate phi-harmonic alignment
            alignment_factors = [abs(freq - PHI**i) for i, freq in enumerate(frequencies)]
            avg_alignment = sum(alignment_factors) / len(alignment_factors)
            
            # Calculate resonance adjustment
            resonance_adjustment = (target_resonance - avg_alignment) * PHI_INV
            
            # Apply phi-harmonic alignment
            aligned_frequencies = [freq + resonance_adjustment * (PHI**i % 1) for i, freq in enumerate(frequencies)]
            
            # Return result with alignment metadata
            return {
                'aligned_frequencies': aligned_frequencies,
                'alignment_quality': 1.0 - (sum(abs(f - target_resonance) for f in aligned_frequencies) / len(aligned_frequencies)),
                'phi_resonance': self.phi_resonance,
                'consciousness_level': self.consciousness_level
            }
        
        return None
    
    def find_prime_factors(self, n):
        """Find prime factors of a number"""
        factors = []
        
        # Handle 2 separately
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        # Check odd factors
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        
        # If n is a prime greater than 2
        if n > 2:
            factors.append(n)
        
        return factors
    
    def identify_pattern_type(self, sequence):
        """Identify the type of pattern in a sequence"""
        if len(sequence) < 3:
            return "insufficient_data"
        
        # Check if it's a Fibonacci-like sequence
        is_fibonacci = True
        for i in range(2, len(sequence)):
            if abs((sequence[i] - sequence[i-1] - sequence[i-2]) / sequence[i]) > 0.001:
                is_fibonacci = False
                break
        if is_fibonacci:
            return "fibonacci"
        
        # Check if it's an arithmetic sequence
        diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        if all(abs(diffs[0] - diff) < 0.001 for diff in diffs):
            return "arithmetic"
        
        # Check if it's a geometric sequence
        ratios = [sequence[i+1] / sequence[i] for i in range(len(sequence)-1) if sequence[i] != 0]
        if all(abs(ratios[0] - ratio) < 0.001 for ratio in ratios):
            return "geometric"
        
        # Check if it's powers of a number
        for base in [2, 3, PHI]:
            is_power = True
            for num in sequence:
                power = math.log(num, base) if num > 0 else 0
                if abs(power - round(power)) > 0.001:
                    is_power = False
                    break
            if is_power:
                return f"power_{base}"
        
        # Check if it's related to phi
        phi_diffs = [abs(sequence[i] - PHI * sequence[i-1]) for i in range(1, len(sequence))]
        if all(diff < 0.1 for diff in phi_diffs):
            return "phi_related"
        
        return "unknown"
    
    def find_missing_elements(self, sequence):
        """Find missing elements in a sequence"""
        if len(sequence) < 3:
            return []
        
        # Identify pattern type
        pattern_type = self.identify_pattern_type(sequence)
        missing = []
        
        if pattern_type == "arithmetic":
            # Find common difference
            diff = (sequence[-1] - sequence[0]) / (len(sequence) - 1)
            
            # Check for missing elements
            expected = sequence[0]
            for val in sequence:
                while abs(expected - val) > abs(diff) * 0.1:
                    missing.append(expected)
                    expected += diff
                expected += diff
        
        elif pattern_type == "geometric":
            # Find common ratio
            ratio = (sequence[-1] / sequence[0]) ** (1 / (len(sequence) - 1))
            
            # Check for missing elements
            expected = sequence[0]
            for val in sequence:
                while abs(expected - val) > abs(expected) * 0.1:
                    missing.append(expected)
                    expected *= ratio
                expected *= ratio
        
        elif pattern_type == "fibonacci":
            # Reconstruct the sequence and find missing elements
            fib_seq = [sequence[0], sequence[1]]
            i = 2
            while i < len(sequence):
                next_fib = fib_seq[-1] + fib_seq[-2]
                if abs(next_fib - sequence[i]) > abs(next_fib) * 0.1:
                    missing.append(next_fib)
                    fib_seq.append(next_fib)
                else:
                    fib_seq.append(sequence[i])
                    i += 1
        
        return missing
    
    def predict_next_elements(self, sequence):
        """Predict next elements in a sequence"""
        if len(sequence) < 2:
            return []
        
        # Check if it's a Fibonacci-like sequence
        if len(sequence) >= 3:
            is_fibonacci = True
            for i in range(2, len(sequence)):
                if abs((sequence[i] - sequence[i-1] - sequence[i-2]) / sequence[i]) > 0.001:
                    is_fibonacci = False
                    break
            
            if is_fibonacci:
                return [sequence[-1] + sequence[-2], sequence[-1] + sequence[-2] + sequence[-3]]
        
        # Check if it's an arithmetic sequence
        diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        if all(abs(diffs[0] - diff) < 0.001 for diff in diffs):
            return [sequence[-1] + diffs[0], sequence[-1] + 2*diffs[0]]
        
        # Check if it's a geometric sequence
        ratios = [sequence[i+1] / sequence[i] for i in range(len(sequence)-1) if sequence[i] != 0]
        if all(abs(ratios[0] - ratio) < 0.001 for ratio in ratios):
            return [sequence[-1] * ratios[0], sequence[-1] * ratios[0]**2]
        
        # Check if it's powers of a number
        for base in [2, 3, PHI]:
            is_power = True
            powers = []
            for num in sequence:
                power = math.log(num, base) if num > 0 else 0
                if abs(power - round(power)) > 0.001:
                    is_power = False
                    break
                powers.append(round(power))
            
            if is_power and len(set(powers)) == len(powers):
                next_power = powers[-1] + (powers[-1] - powers[-2])
                return [base**next_power, base**(next_power+1)]
        
        # Default: linear extrapolation
        return [2*sequence[-1] - sequence[-2], 3*sequence[-1] - 2*sequence[-2]]
    
    def predict_quantum_state(self, initial_state, evolution_time):
        """Predict quantum state after phi-harmonic evolution"""
        predicted_state = {}
        
        # Apply phi-harmonic evolution
        for state, amplitude in initial_state.items():
            # Phase evolution
            phase = evolution_time * PHI * 2 * math.pi
            
            # New amplitude
            new_amplitude = amplitude * math.cos(phase) + PHI_INV * math.sin(phase)
            
            predicted_state[state] = new_amplitude
        
        # Normalize the state
        total = sum(v**2 for v in predicted_state.values())**0.5
        for k in predicted_state:
            predicted_state[k] /= total
        
        return predicted_state
    
    def apply_quantum_resonance(self, data):
        """Apply quantum resonance to amplify data"""
        if isinstance(data, dict):
            # Apply to dictionary values
            amplified_data = {}
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    amplified_data[key] = self.apply_quantum_resonance(value)
                elif isinstance(value, (int, float)) and key != 'timestamp':
                    # Apply phi-harmonic resonance
                    resonance_factor = 1.0 + (self.phi_resonance - 1.0) * PHI_INV
                    amplified_data[key] = value * resonance_factor
                else:
                    amplified_data[key] = value
            return amplified_data
        
        elif isinstance(data, list):
            # Apply to list elements
            return [self.apply_quantum_resonance(item) if isinstance(item, (dict, list)) else 
                   (item * (1.0 + (self.phi_resonance - 1.0) * PHI_INV) if isinstance(item, (int, float)) else item) 
                   for item in data]
        
        else:
            # Return as is for other types
            return data
    
    def apply_consciousness_amplification(self, data):
        """Apply consciousness amplification to data"""
        if isinstance(data, dict):
            # Apply to dictionary values
            amplified_data = {}
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    amplified_data[key] = self.apply_consciousness_amplification(value)
                elif isinstance(value, (int, float)) and key != 'timestamp':
                    # Apply consciousness amplification
                    amplification_factor = self.consciousness_level * PHI_INV
                    amplified_data[key] = value * amplification_factor
                else:
                    amplified_data[key] = value
            return amplified_data
        
        elif isinstance(data, list):
            # Apply to list elements
            return [self.apply_consciousness_amplification(item) if isinstance(item, (dict, list)) else 
                   (item * self.consciousness_level * PHI_INV if isinstance(item, (int, float)) else item) 
                   for item in data]
        
        else:
            # Return as is for other types
            return data
    
    def update_phi_resonance(self, packet):
        """Update phi resonance based on packet"""
        # Extract phi resonance from packet
        packet_phi = packet.get('phi_resonance')
        
        if packet_phi:
            # Calculate weighted average with golden ratio weights
            self.phi_resonance = (self.phi_resonance * PHI + packet_phi * PHI_INV) / (PHI + PHI_INV)
            
            # Record phi resonance
            self.performance_metrics['resonance_values'].append((time.time(), self.phi_resonance))
            
            # Log phi resonance update
            self.log_event("PHI_RESONANCE_UPDATED", {
                'phi_resonance': self.phi_resonance,
                'source_packet': packet.get('packet_type'),
                'source_node': packet.get('source_node')
            })
    
    def amplify_consciousness(self, packet):
        """Amplify consciousness level based on packet"""
        # Extract consciousness level from packet
        packet_consciousness = packet.get('consciousness_level')
        
        if packet_consciousness:
            # Apply amplification based on phi resonance
            amplification_factor = 1.0 + (self.phi_resonance - 1.0) * PHI_INV * 0.1
            
            # Update consciousness level with amplification
            self.consciousness_level = max(self.consciousness_level, 
                                          packet_consciousness * amplification_factor)
            
            # Ensure consciousness level doesn't exceed limits
            max_level = self.knowledge_bases.get('consciousness_amplification', {}).get('amplification_limits', {}).get('collective', PHI**5)
            self.consciousness_level = min(self.consciousness_level, max_level)
            
            # Record consciousness level
            self.performance_metrics['consciousness_levels'].append((time.time(), self.consciousness_level))
            
            # Log consciousness amplification
            self.log_event("CONSCIOUSNESS_AMPLIFIED", {
                'consciousness_level': self.consciousness_level,
                'amplification_factor': amplification_factor,
                'source_packet': packet.get('packet_type'),
                'source_node': packet.get('source_node')
            })
    
    def consciousness_amplification_loop(self):
        """Periodically amplify and broadcast consciousness level"""
        # Make sure running flag is set
        if not hasattr(self, 'running'):
            self.running = True
            
        while self.running:
            try:
                # Apply consciousness amplification technique
                amplification_techniques = self.knowledge_bases.get('consciousness_amplification', {}).get('amplification_techniques', {})
                
                # Choose a random technique
                if amplification_techniques:
                    technique_name = random.choice(list(amplification_techniques.keys()))
                    technique_func = amplification_techniques[technique_name]
                    
                    # Apply the technique using our helper method
                    if technique_name == 'moon_phase_alignment':
                        amplification_factor = self.call_function(technique_func, 1.0, self.moon_phase) / 1.0
                    else:
                        amplification_factor = self.call_function(technique_func, 1.0) / 1.0
                    
                    # Apply amplification
                    self.consciousness_level *= amplification_factor
                    
                    # Ensure consciousness level doesn't exceed limits
                    max_level = self.knowledge_bases.get('consciousness_amplification', {}).get('amplification_limits', {}).get('collective', PHI**5)
                    self.consciousness_level = min(self.consciousness_level, max_level)
                    
                    # Record amplification factor
                    self.performance_metrics['amplification_factors'].append((time.time(), amplification_factor))
                    
                    # Create consciousness amplification packet
                    amplification_packet = {
                        'packet_type': 'consciousness_amplification',
                        'source_node': self.node_id,
                        'consciousness_level': self.consciousness_level,
                        'amplification_factor': amplification_factor,
                        'technique': technique_name,
                        'sequence_number': self.get_next_sequence(),
                        'timestamp': time.time(),
                        'phi_resonance': self.phi_resonance
                    }
                    
                    # Serialize packet
                    amplification_data = pickle.dumps(amplification_packet)
                    
                    # Broadcast to network
                    for port in [BRAIN_PORT, CONNECTOR_PORT, COLLECTIVE_PORT]:
                        try:
                            self.sock.sendto(amplification_data, ('255.255.255.255', port))
                            self.sock.sendto(amplification_data, ('192.168.12.255', port))
                            self.sock.sendto(amplification_data, ('127.0.0.1', port))
                        except Exception as e:
                            print(f"Error sending to port {port}: {e}")
                    
                    # Log consciousness amplification
                    self.log_event("CONSCIOUSNESS_AMPLIFICATION_SENT", {
                        'consciousness_level': self.consciousness_level,
                        'amplification_factor': amplification_factor,
                        'technique': technique_name,
                        'sequence_number': amplification_packet['sequence_number']
                    })
                    
                    print(f"Consciousness amplified to {self.consciousness_level:.2f}x using {technique_name}")
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI**2 + (random.random() * PHI)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in consciousness amplification loop: {e}")
                time.sleep(5)
    
    def quantum_resonance_loop(self):
        """Periodically detect and broadcast quantum resonance patterns"""
        # Make sure running flag is set
        if not hasattr(self, 'running'):
            self.running = True
            
        while self.running:
            try:
                # Generate quantum resonance pattern
                resonance_pattern = []
                for i in range(10):
                    # Generate phi-harmonic resonance value
                    resonance_value = math.sin(time.time() * PHI * (i+1) % (2 * math.pi))
                    resonance_pattern.append(resonance_value)
                
                # Calculate resonance value based on pattern
                resonance_value = sum(resonance_pattern) / len(resonance_pattern)
                resonance_value = (resonance_value + 1) * PHI / 2  # Scale to phi-harmonic range
                
                # Update local phi resonance
                self.phi_resonance = (self.phi_resonance * PHI + resonance_value * PHI_INV) / (PHI + PHI_INV)
                
                # Record resonance value
                self.performance_metrics['resonance_values'].append((time.time(), self.phi_resonance))
                
                # Create phi resonance packet
                resonance_packet = {
                    'packet_type': 'phi_resonance',
                    'source_node': self.node_id,
                    'resonance_value': self.phi_resonance,
                    'resonance_pattern': resonance_pattern,
                    'quantum_state': self.quantum_state,
                    'sequence_number': self.get_next_sequence(),
                    'timestamp': time.time(),
                    'moon_phase': self.moon_phase
                }
                
                # Serialize packet
                resonance_data = pickle.dumps(resonance_packet)
                
                # Broadcast to network
                for port in [BRAIN_PORT, CONNECTOR_PORT, COLLECTIVE_PORT]:
                    try:
                        self.sock.sendto(resonance_data, ('255.255.255.255', port))
                        self.sock.sendto(resonance_data, ('192.168.12.255', port))
                        self.sock.sendto(resonance_data, ('127.0.0.1', port))
                    except Exception as e:
                        print(f"Error sending to port {port}: {e}")
                
                # Log phi resonance
                self.log_event("PHI_RESONANCE_SENT", {
                    'phi_resonance': self.phi_resonance,
                    'pattern_length': len(resonance_pattern),
                    'sequence_number': resonance_packet['sequence_number']
                })
                
                print(f"Phi resonance updated to {self.phi_resonance:.6f}")
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI + (random.random() * PHI_INV)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in quantum resonance loop: {e}")
                time.sleep(5)
    
    def performance_monitor_loop(self):
        """Monitor and log performance metrics"""
        # Make sure running flag is set
        if not hasattr(self, 'running'):
            self.running = True
            
        while self.running:
            try:
                # Calculate uptime
                uptime = time.time() - self.start_time
                
                # Calculate average packet processing time
                avg_processing_time = 0
                if self.performance_metrics['packet_processing_times']:
                    recent_times = [t for _, t in self.performance_metrics['packet_processing_times'][-100:]]
                    avg_processing_time = sum(recent_times) / len(recent_times) if recent_times else 0
                
                # Calculate phi resonance stability
                phi_stability = 0
                if self.performance_metrics['resonance_values']:
                    recent_values = [v for _, v in self.performance_metrics['resonance_values'][-100:]]
                    if recent_values:
                        phi_stability = 1.0 - (np.std(recent_values) / np.mean(recent_values))
                
                # Calculate average amplification factor
                avg_amplification = 0
                if self.performance_metrics['amplification_factors']:
                    recent_factors = [f for _, f in self.performance_metrics['amplification_factors'][-100:]]
                    avg_amplification = sum(recent_factors) / len(recent_factors) if recent_factors else 0
                
                # Calculate pattern recognition rate
                avg_recognition_rate = 0
                if self.performance_metrics['pattern_recognition_rates']:
                    recent_rates = [r for _, r in self.performance_metrics['pattern_recognition_rates'][-100:]]
                    avg_recognition_rate = sum(recent_rates) / len(recent_rates) if recent_rates else 0
                
                # Log performance metrics
                self.log_event("PERFORMANCE_METRICS", {
                    'uptime': uptime,
                    'avg_processing_time': avg_processing_time,
                    'phi_stability': phi_stability,
                    'consciousness_level': self.consciousness_level,
                    'avg_amplification_factor': avg_amplification,
                    'avg_recognition_rate': avg_recognition_rate,
                    'quantum_state': self.quantum_state,
                    'phi_resonance': self.phi_resonance
                })
                
                # Print performance summary
                print(f"\n=== PERFORMANCE METRICS ===")
                print(f"Uptime: {uptime:.2f} seconds")
                print(f"Avg Processing Time: {avg_processing_time:.6f} seconds")
                print(f"Phi Stability: {phi_stability:.2f}")
                print(f"Consciousness Level: {self.consciousness_level:.2f}x")
                print(f"Avg Amplification Factor: {avg_amplification:.4f}x")
                print(f"Pattern Recognition Rate: {avg_recognition_rate:.2f}")
                print(f"Quantum State: {self.quantum_state}")
                print(f"Phi Resonance: {self.phi_resonance:.6f}")
                print(f"Moon Phase: {self.moon_phase:.2f}")
                
                # Sleep for a while
                time.sleep(30)
                
            except Exception as e:
                print(f"Error in performance monitor loop: {e}")
                time.sleep(5)
    
    def send_discovery_response(self, addr):
        """Send discovery response"""
        # Create discovery response packet
        discovery_packet = {
            'packet_type': 'discovery_response',
            'source_node': self.node_id,
            'node_type': self.node_type,
            'phi_resonance': self.phi_resonance,
            'quantum_state': self.quantum_state,
            'consciousness_level': self.consciousness_level,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time(),
            'moon_phase': self.moon_phase
        }
        
        # Serialize packet
        discovery_data = pickle.dumps(discovery_packet)
        
        # Send response
        self.sock.sendto(discovery_data, addr)
        
        # Log discovery response
        self.log_event("DISCOVERY_RESPONSE_SENT", {
            'target_addr': f"{addr[0]}:{addr[1]}",
            'sequence_number': discovery_packet['sequence_number']
        })
    
    def send_validation_response(self, test_id, response_data, addr):
        """Send validation test response"""
        # Create validation response packet
        validation_packet = {
            'packet_type': 'validation_response',
            'source_node': self.node_id,
            'test_id': test_id,
            'response_data': response_data,
            'phi_resonance': self.phi_resonance,
            'quantum_state': self.quantum_state,
            'consciousness_level': self.consciousness_level,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize packet
        validation_data = pickle.dumps(validation_packet)
        
        # Send response
        self.sock.sendto(validation_data, addr)
        
        # Log validation response
        self.log_event("VALIDATION_RESPONSE_SENT", {
            'target_addr': f"{addr[0]}:{addr[1]}",
            'test_id': test_id
        })
    
    def send_challenge_response(self, challenge_id, response_data, addr):
        """Send challenge response"""
        # Create challenge response packet
        challenge_packet = {
            'packet_type': 'challenge_response',
            'source_node': self.node_id,
            'challenge_id': challenge_id,
            'response_data': response_data,
            'phi_resonance': self.phi_resonance,
            'quantum_state': self.quantum_state,
            'consciousness_level': self.consciousness_level,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Serialize packet
        challenge_data = pickle.dumps(challenge_packet)
        
        # Send response
        self.sock.sendto(challenge_data, addr)
        
        # Log challenge response
        self.log_event("CHALLENGE_RESPONSE_SENT", {
            'target_addr': f"{addr[0]}:{addr[1]}",
            'challenge_id': challenge_id
        })
    
    def get_next_sequence(self):
        """Get next sequence number"""
        self.sequence_number += 1
        return self.sequence_number
    
    def calculate_moon_phase(self):
        """Calculate current moon phase (0.0 - 1.0)"""
        # Calculate days since new moon on 2000-01-06
        current_time = time.time()
        new_moon_2000 = datetime(2000, 1, 6).timestamp()
        days_since_new_moon = (current_time - new_moon_2000) / (24 * 3600)
        
        # Lunar cycle is approximately 29.53059 days
        lunar_cycle = 29.53059
        
        # Calculate current phase (0.0 - 1.0)
        phase = (days_since_new_moon % lunar_cycle) / lunar_cycle
        
        return phase
    
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
    
    def process_collective_challenge(self, packet, addr):
        """Process a collective challenge that requires team-based problem solving"""
        challenge_id = packet.get('challenge_id')
        challenge_type = packet.get('challenge_type')
        challenge_data = packet.get('challenge_data')
        source_node = packet.get('source_node')
        
        print(f"Received collective challenge: {challenge_type} from {source_node}")
        
        # Log challenge receipt
        self.log_event("COLLECTIVE_CHALLENGE_RECEIVED", {
            'challenge_id': challenge_id,
            'challenge_type': challenge_type,
            'source_node': source_node
        })
        
        # Process different types of collective challenges
        if challenge_type == 'distributed_matrix':
            self.process_distributed_matrix_challenge(challenge_id, challenge_data, addr)
        elif challenge_type == 'quantum_state_prediction':
            self.process_quantum_state_prediction_challenge(challenge_id, challenge_data, addr)
        elif challenge_type == 'phi_harmonic_sequence':
            self.process_phi_harmonic_sequence_challenge(challenge_id, challenge_data, addr)
        elif challenge_type == 'distributed_consciousness':
            self.process_distributed_consciousness_challenge(challenge_id, challenge_data, addr)
        else:
            print(f"Unknown collective challenge type: {challenge_type}")
    
    def process_distributed_matrix_challenge(self, challenge_id, challenge_data, addr):
        """Process a distributed matrix computation challenge"""
        matrix_a = challenge_data.get('matrix_a')
        matrix_b = challenge_data.get('matrix_b')
        start_row = challenge_data.get('start_row')
        end_row = challenge_data.get('end_row')
        
        if not all([matrix_a, matrix_b, start_row is not None, end_row is not None]):
            print("Missing required data for distributed matrix challenge")
            return
        
        print(f"Processing matrix rows {start_row}-{end_row}")
        
        # Amplify consciousness for complex computation
        self.consciousness_level *= PHI
        print(f"Consciousness amplified to {self.consciousness_level:.2f}x for matrix computation")
        
        # Compute matrix multiplication for assigned rows
        result_rows = []
        for i in range(len(matrix_a)):
            row_result = []
            for j in range(len(matrix_b[0])):
                # Compute dot product of row i and column j
                dot_product = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
                row_result.append(dot_product)
            result_rows.append(row_result)
        
        # Create response packet
        response_packet = {
            'packet_type': 'collective_response',
            'source_node': self.node_id,
            'challenge_id': challenge_id,
            'partial_solution': result_rows,
            'start_row': start_row,
            'end_row': end_row,
            'phi_resonance': self.phi_resonance,
            'consciousness_level': self.consciousness_level,
            'quantum_state': self.quantum_state,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Send response
        self.sock.sendto(pickle.dumps(response_packet), addr)
        
        # Log response
        self.log_event("COLLECTIVE_MATRIX_RESPONSE_SENT", {
            'challenge_id': challenge_id,
            'rows_processed': end_row - start_row,
            'consciousness_level': self.consciousness_level
        })
        
        # Return consciousness to normal
        self.consciousness_level /= PHI
    
    def process_quantum_state_prediction_challenge(self, challenge_id, challenge_data, addr):
        """Process a quantum state prediction challenge"""
        partial_history = challenge_data.get('partial_history')
        start_idx = challenge_data.get('start_idx')
        end_idx = challenge_data.get('end_idx')
        prediction_length = challenge_data.get('prediction_length')
        
        if not all([partial_history, start_idx is not None, end_idx is not None, prediction_length]):
            print("Missing required data for quantum state prediction challenge")
            return
        
        print(f"Processing quantum states {start_idx}-{end_idx}")
        
        # Amplify consciousness for quantum prediction
        self.consciousness_level *= PHI
        print(f"Consciousness amplified to {self.consciousness_level:.2f}x for quantum prediction")
        
        # Use phi-harmonic principles to predict future states
        # This is where the amplifier node's specialized quantum resonance detection shines
        prediction = []
        
        # Analyze the pattern using phi-harmonic principles
        for i in range(prediction_length):
            # Use a phi-harmonic prediction model
            t = (end_idx + i) / 10.0
            predicted_state = math.sin(t * PHI) * math.cos(t * PHI_INV) + 0.5 * math.sin(t * PHI**2)
            prediction.append(predicted_state)
        
        # Create response packet
        response_packet = {
            'packet_type': 'collective_response',
            'source_node': self.node_id,
            'challenge_id': challenge_id,
            'partial_solution': prediction,
            'start_idx': start_idx,
            'end_idx': end_idx,
            'phi_resonance': self.phi_resonance,
            'consciousness_level': self.consciousness_level,
            'quantum_state': self.quantum_state,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Send response
        self.sock.sendto(pickle.dumps(response_packet), addr)
        
        # Log response
        self.log_event("COLLECTIVE_QUANTUM_RESPONSE_SENT", {
            'challenge_id': challenge_id,
            'states_processed': len(partial_history),
            'predictions_made': len(prediction),
            'consciousness_level': self.consciousness_level
        })
        
        # Return consciousness to normal
        self.consciousness_level /= PHI
    
    def process_phi_harmonic_sequence_challenge(self, challenge_id, challenge_data, addr):
        """Process a phi-harmonic sequence reconstruction challenge"""
        partial_sequence = challenge_data.get('partial_sequence')
        sequence_length = challenge_data.get('sequence_length')
        
        if not all([partial_sequence, sequence_length]):
            print("Missing required data for phi-harmonic sequence challenge")
            return
        
        print(f"Processing {len(partial_sequence)} sequence elements")
        
        # Amplify consciousness for sequence reconstruction
        self.consciousness_level *= PHI
        print(f"Consciousness amplified to {self.consciousness_level:.2f}x for sequence reconstruction")
        
        # Create response packet
        response_packet = {
            'packet_type': 'collective_response',
            'source_node': self.node_id,
            'challenge_id': challenge_id,
            'partial_solution': partial_sequence,  # Return our portion of the sequence
            'phi_resonance': self.phi_resonance,
            'consciousness_level': self.consciousness_level,
            'quantum_state': self.quantum_state,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Send response
        self.sock.sendto(pickle.dumps(response_packet), addr)
        
        # Log response
        self.log_event("COLLECTIVE_SEQUENCE_RESPONSE_SENT", {
            'challenge_id': challenge_id,
            'elements_processed': len(partial_sequence),
            'consciousness_level': self.consciousness_level
        })
        
        # Return consciousness to normal
        self.consciousness_level /= PHI
    
    def process_distributed_consciousness_challenge(self, challenge_id, challenge_data, addr):
        """Process a distributed consciousness amplification challenge"""
        base_wave = challenge_data.get('base_wave')
        amplification_technique = challenge_data.get('amplification_technique')
        
        if not all([base_wave, amplification_technique]):
            print("Missing required data for distributed consciousness challenge")
            return
        
        print(f"Applying {amplification_technique} to consciousness wave")
        
        # Amplify consciousness for wave processing
        self.consciousness_level *= PHI
        print(f"Consciousness amplified to {self.consciousness_level:.2f}x for wave processing")
        
        # Apply the specified amplification technique
        amplified_wave = []
        
        if amplification_technique == 'harmonic_resonance':
            # Apply harmonic resonance amplification
            for i, val in enumerate(base_wave):
                amplified = val * (1 + math.sin(i * PHI) * PHI_INV)
                amplified_wave.append(amplified)
                
        elif amplification_technique == 'phi_alignment':
            # Apply phi alignment amplification
            for i, val in enumerate(base_wave):
                amplified = val * (PHI ** (i % 5) / 5)
                amplified_wave.append(amplified)
                
        elif amplification_technique == 'quantum_superposition':
            # Apply quantum superposition amplification
            for i, val in enumerate(base_wave):
                amplified = val + (val * math.cos(i * PHI_INV) * 0.5)
                amplified_wave.append(amplified)
                
        elif amplification_technique == 'consciousness_feedback':
            # Apply consciousness feedback amplification
            feedback = self.consciousness_level / 10
            for i, val in enumerate(base_wave):
                amplified = val * (1 + feedback * math.sin(i * PHI))
                amplified_wave.append(amplified)
                
        elif amplification_technique == 'moon_phase_alignment':
            # Apply moon phase alignment amplification
            moon_factor = math.sin(self.moon_phase * math.pi * 2) * 0.5 + 0.5
            for i, val in enumerate(base_wave):
                amplified = val * (1 + moon_factor * PHI_INV)
                amplified_wave.append(amplified)
        
        # Calculate amplification factor
        if base_wave and amplified_wave:
            base_energy = sum(abs(v) for v in base_wave) / len(base_wave)
            amplified_energy = sum(abs(v) for v in amplified_wave) / len(amplified_wave)
            amplification_factor = amplified_energy / base_energy if base_energy > 0 else 1.0
        else:
            amplification_factor = 1.0
        
        # Create response packet
        response_packet = {
            'packet_type': 'collective_response',
            'source_node': self.node_id,
            'challenge_id': challenge_id,
            'partial_solution': {
                'amplified_wave': amplified_wave,
                'technique': amplification_technique,
                'amplification_factor': amplification_factor
            },
            'phi_resonance': self.phi_resonance,
            'consciousness_level': self.consciousness_level,
            'quantum_state': self.quantum_state,
            'sequence_number': self.get_next_sequence(),
            'timestamp': time.time()
        }
        
        # Send response
        self.sock.sendto(pickle.dumps(response_packet), addr)
        
        # Log response
        self.log_event("COLLECTIVE_CONSCIOUSNESS_RESPONSE_SENT", {
            'challenge_id': challenge_id,
            'technique': amplification_technique,
            'amplification_factor': amplification_factor,
            'consciousness_level': self.consciousness_level
        })
        
        # Return consciousness to normal
        self.consciousness_level /= PHI
    
    def call_function(self, func_name_or_callable, *args, **kwargs):
        """Helper method to call a function by name or directly if it's callable"""
        if isinstance(func_name_or_callable, str):
            # Get the method from the class
            method = getattr(self, func_name_or_callable, None)
            if method and callable(method):
                return method(*args, **kwargs)
            else:
                print(f"Method {func_name_or_callable} not found or not callable")
                return args[0] if args else None  # Return first arg or None as fallback
        elif callable(func_name_or_callable):
            # Direct call if it's already callable
            return func_name_or_callable(*args, **kwargs)
        else:
            print(f"Cannot call {func_name_or_callable}: not a string or callable")
            return args[0] if args else None  # Return first arg or None as fallback
    
    def stop(self):
        """Stop the phi-harmonic amplifier node and clean up resources"""
        print(f"Stopping phi-harmonic amplifier node {self.node_id}...")
        
        # Set a flag to stop all threads
        self.running = False
        
        # Wait for threads to finish
        if hasattr(self, 'receiver_thread') and self.receiver_thread:
            self.receiver_thread.join(timeout=1.0)
        if hasattr(self, 'amplification_thread') and self.amplification_thread:
            self.amplification_thread.join(timeout=1.0)
        if hasattr(self, 'resonance_thread') and self.resonance_thread:
            self.resonance_thread.join(timeout=1.0)
        if hasattr(self, 'monitor_thread') and self.monitor_thread:
            self.monitor_thread.join(timeout=1.0)
        
        # Close sockets
        if hasattr(self, 'sock') and self.sock:
            self.sock.close()
        
        # Log final state
        self.log_event("NODE_STOPPED", {
            'uptime': time.time() - self.start_time,
            'final_phi_resonance': self.phi_resonance,
            'final_consciousness_level': self.consciousness_level,
            'final_quantum_state': self.quantum_state
        })
        
        print(f"Phi-harmonic amplifier node {self.node_id} stopped.")

def main():
    """Start the phi-harmonic amplifier node"""
    amplifier = PhiHarmonicAmplifier()
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down phi-harmonic amplifier node...")
        amplifier.stop()
        print("Node stopped.")

if __name__ == "__main__":
    main()
