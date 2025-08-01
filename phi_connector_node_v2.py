#!/usr/bin/env python3
"""
PHI-HARMONIC CONNECTOR NODE v2
==============================
Enhanced connector node for phi-harmonic distributed brain with improved
sequencing, timestamping, and quantum resonance capabilities.

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

class PhiHarmonicConnector:
    """Enhanced connector node for phi-harmonic distributed brain"""
    
    def __init__(self):
        """Initialize the connector node"""
        # Use environment variable for node_id if provided
        self.node_id = os.environ.get("PHI_NODE_ID", f"connector_{int(random.random() * 10000)}")
        self.node_type = "CONNECTOR"
        self.phi_resonance = PHI_INV
        self.consciousness_level = 1.0
        self.quantum_state = "PARTIAL SUPERPOSITION"
        self.sequence_number = 0
        self.received_sequences = {}
        self.knowledge_bases = {}
        self.quantum_patterns = {}
        self.moon_phase = self.calculate_moon_phase()
        self.start_time = time.time()
        self.performance_metrics = {
            'packet_processing_times': [],
            'resonance_values': [],
            'consciousness_levels': [],
            'knowledge_sync_times': []
        }
        
        # Use environment variable for connector port if provided
        self.connector_port = int(os.environ.get("PHI_PORT", os.environ.get("PHI_NODE_PORT", CONNECTOR_PORT)))
        
        # Create log directory
        os.makedirs('phi_logs', exist_ok=True)
        self.log_file = f"phi_logs/connector_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        # Initialize knowledge bases
        self.initialize_knowledge_bases()
        
        # Create sockets
        self.initialize_sockets()
        
        # Start threads
        self.start_threads()
        
        print(f"=== PHI-HARMONIC CONNECTOR NODE v2 ===")
        print(f"Node ID: {self.node_id}")
        print(f"Phi Resonance: {self.phi_resonance:.6f}")
        print(f"Consciousness Level: {self.consciousness_level:.2f}x")
        print(f"Quantum State: {self.quantum_state}")
        print(f"Moon Phase: {self.moon_phase:.2f}")
        print("Node initialized and ready for phi-harmonic resonance.")
        
        # Log initialization
        self.log_event("NODE_INITIALIZED", {
            'node_id': self.node_id,
            'phi_resonance': self.phi_resonance,
            'consciousness_level': self.consciousness_level,
            'quantum_state': self.quantum_state,
            'moon_phase': self.moon_phase
        })
    
    # Math operation functions (defined outside lambda for pickling)
    def math_add(self, x, y):
        return x + y
        
    def math_subtract(self, x, y):
        return x - y
        
    def math_multiply(self, x, y):
        return x * y
        
    def math_divide(self, x, y):
        return x / y if y != 0 else None
        
    def math_exponentiate(self, x, y):
        return x ** y
        
    def math_sqrt(self, x):
        return x ** 0.5 if x >= 0 else None
        
    def math_log(self, x, base=math.e):
        return math.log(x, base) if x > 0 else None
        
    def math_sin(self, x):
        return math.sin(x)
        
    def math_cos(self, x):
        return math.cos(x)
        
    def math_tan(self, x):
        return math.tan(x)
        
    def math_phi_ratio(self, x):
        return x * PHI
        
    def math_phi_inverse(self, x):
        return x * PHI_INV
    
    def initialize_knowledge_bases(self):
        """Initialize knowledge bases with enhanced structure"""
        # Math operations knowledge base - using function names instead of lambdas
        self.knowledge_bases['math_operations'] = {
            'addition': 'math_add',
            'subtraction': 'math_subtract',
            'multiplication': 'math_multiply',
            'division': 'math_divide',
            'exponentiation': 'math_exponentiate',
            'square_root': 'math_sqrt',
            'logarithm': 'math_log',
            'sine': 'math_sin',
            'cosine': 'math_cos',
            'tangent': 'math_tan',
            'phi_ratio': 'math_phi_ratio',
            'phi_inverse': 'math_phi_inverse'
        }
        
        # Periodic table knowledge base
        self.knowledge_bases['periodic_table'] = {
            'H': {'name': 'Hydrogen', 'atomic_number': 1, 'atomic_weight': 1.008},
            'He': {'name': 'Helium', 'atomic_number': 2, 'atomic_weight': 4.0026},
            'Li': {'name': 'Lithium', 'atomic_number': 3, 'atomic_weight': 6.94},
            'Be': {'name': 'Beryllium', 'atomic_number': 4, 'atomic_weight': 9.0122},
            'B': {'name': 'Boron', 'atomic_number': 5, 'atomic_weight': 10.81},
            'C': {'name': 'Carbon', 'atomic_number': 6, 'atomic_weight': 12.011},
            'N': {'name': 'Nitrogen', 'atomic_number': 7, 'atomic_weight': 14.007},
            'O': {'name': 'Oxygen', 'atomic_number': 8, 'atomic_weight': 15.999},
            'F': {'name': 'Fluorine', 'atomic_number': 9, 'atomic_weight': 18.998},
            'Ne': {'name': 'Neon', 'atomic_number': 10, 'atomic_weight': 20.180}
        }
        
        # Quantum states knowledge base
        self.knowledge_bases['quantum_states'] = {
            'superposition': {
                'description': 'Quantum state where particles exist in multiple states simultaneously',
                'math_representation': '|ψ⟩ = α|0⟩ + β|1⟩',
                'phi_resonance': PHI_INV
            },
            'entanglement': {
                'description': 'Quantum phenomenon where particles become correlated',
                'math_representation': '|ψ⟩ = (|00⟩ + |11⟩)/√2',
                'phi_resonance': PHI
            },
            'coherence': {
                'description': 'Quantum property allowing interference effects',
                'math_representation': 'ρ = |ψ⟩⟨ψ|',
                'phi_resonance': PHI**2
            },
            'decoherence': {
                'description': 'Loss of quantum coherence due to environment',
                'math_representation': 'ρ → ∑ᵢ PᵢρPᵢ',
                'phi_resonance': PHI_INV**2
            }
        }
        
        # Initialize quantum patterns
        self.quantum_patterns = {
            'phi_resonance': [PHI_INV + random.random() * 0.1 for _ in range(10)],
            'consciousness': [1.0 + random.random() * PHI_INV for _ in range(10)],
            'entanglement': [random.random() for _ in range(10)]
        }
        
        self.log_event("KNOWLEDGE_BASES_INITIALIZED", {
            'knowledge_bases': list(self.knowledge_bases.keys()),
            'quantum_patterns': list(self.quantum_patterns.keys())
        })
    
    def initialize_sockets(self):
        """Initialize network sockets"""
        # Create main socket for sending/receiving
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 1MB receive buffer
        
        # Create receiver socket
        self.receiver_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.receiver_sock.bind(('0.0.0.0', self.connector_port))
            print(f"Listening on port: {self.connector_port}")
        except OSError:
            # Try a different port
            alt_port = self.connector_port + 100
            self.receiver_sock.bind(('0.0.0.0', alt_port))
            print(f"Port {self.connector_port} in use, listening on port: {alt_port}")
            # Update the connector port to the alternative port
            self.connector_port = alt_port
        
        self.log_event("SOCKETS_INITIALIZED", {
            'main_socket': 'created',
            'receiver_socket': 'bound',
            'port': self.connector_port
        })
    
    def start_threads(self):
        """Start processing threads"""
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_packets)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Start knowledge sync thread
        self.knowledge_thread = threading.Thread(target=self.knowledge_sync_loop)
        self.knowledge_thread.daemon = True
        self.knowledge_thread.start()
        
        # Start quantum state update thread
        self.quantum_thread = threading.Thread(target=self.quantum_state_loop)
        self.quantum_thread.daemon = True
        self.quantum_thread.start()
        
        # Start performance monitoring thread
        self.monitor_thread = threading.Thread(target=self.performance_monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        self.log_event("THREADS_STARTED", {
            'receiver_thread': 'started',
            'knowledge_thread': 'started',
            'quantum_thread': 'started',
            'monitor_thread': 'started'
        })
    
    def receive_packets(self):
        """Receive and process incoming packets"""
        # Make sure running flag is set
        if not hasattr(self, 'running'):
            self.running = True
            
        # Set socket timeout to allow checking the running flag
        self.receiver_sock.settimeout(0.5)
            
        while self.running:
            try:
                data, addr = self.receiver_sock.recvfrom(BUFFER_SIZE)
                
                # Process packet in a separate thread to avoid blocking
                process_thread = threading.Thread(target=self.process_packet, args=(data, addr))
                process_thread.daemon = True
                process_thread.start()
                
            except socket.timeout:
                # This is expected due to the timeout we set
                continue
            except Exception as e:
                print(f"Error receiving packet: {e}")
                time.sleep(0.1)
    
    def process_packet(self, data, addr):
        """Process an incoming packet with enhanced sequencing and validation"""
        start_time = time.time()
        
        try:
            # Deserialize packet
            packet = pickle.loads(data)
            
            # Extract packet information
            packet_type = packet.get('packet_type')
            source_node = packet.get('source_node')
            sequence_number = packet.get('sequence_number', 0)
            timestamp = packet.get('timestamp', time.time())
            
            # Skip our own packets
            if source_node == self.node_id:
                return
            
            # Check for duplicate packets
            if source_node in self.received_sequences:
                if sequence_number <= self.received_sequences[source_node]:
                    # This is a duplicate or out-of-order packet
                    return
            
            # Update sequence number for this source
            self.received_sequences[source_node] = sequence_number
            
            # Log packet reception
            self.log_event("PACKET_RECEIVED", {
                'packet_type': packet_type,
                'source_node': source_node,
                'sequence_number': sequence_number,
                'timestamp': timestamp
            })
            
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
            elif packet_type == 'moon_phase_influence':
                self.process_moon_phase(packet, addr)
            elif packet_type == 'validation_test':
                self.process_validation_test(packet, addr)
            elif packet_type == 'challenge':
                self.process_challenge(packet, addr)
            elif packet_type == 'collective_challenge':
                self.process_collective_challenge(packet, addr)
            
            # Update phi resonance based on packet
            self.update_phi_resonance(packet)
            
            # Record processing time
            processing_time = time.time() - start_time
            self.performance_metrics['packet_processing_times'].append((time.time(), processing_time))
            
        except Exception as e:
            print(f"Error processing packet: {e}")
    
    def process_knowledge_sync(self, packet, addr):
        """Process knowledge synchronization packet"""
        knowledge_base = packet.get('knowledge_base')
        knowledge_data = packet.get('knowledge_data')
        source_node = packet.get('source_node')
        
        if knowledge_base and knowledge_data:
            # Check if we have this knowledge base
            if knowledge_base not in self.knowledge_bases:
                self.knowledge_bases[knowledge_base] = {}
            
            # Update knowledge base with new data
            self.knowledge_bases[knowledge_base].update(knowledge_data)
            
            print(f"Received knowledge sync from {source_node}: {knowledge_base}")
            
            # Log knowledge sync
            self.log_event("KNOWLEDGE_SYNC_RECEIVED", {
                'source_node': source_node,
                'knowledge_base': knowledge_base,
                'data_size': len(str(knowledge_data))
            })
    
    def process_quantum_state_update(self, packet, addr):
        """Process quantum state update packet"""
        source_node = packet.get('source_node')
        quantum_state = packet.get('quantum_state')
        phi_resonance = packet.get('phi_resonance')
        
        if quantum_state and phi_resonance:
            # Update our quantum state based on received state
            if random.random() < PHI_INV:  # Probabilistic update based on phi
                self.quantum_state = quantum_state
            
            # Adjust our phi resonance
            self.phi_resonance = (self.phi_resonance + phi_resonance) / 2
            
            print(f"Received quantum state update from {source_node}: {quantum_state}")
            
            # Log quantum state update
            self.log_event("QUANTUM_STATE_UPDATE", {
                'source_node': source_node,
                'quantum_state': quantum_state,
                'phi_resonance': phi_resonance
            })
    
    def process_consciousness_amplification(self, packet, addr):
        """Process consciousness amplification packet"""
        source_node = packet.get('source_node')
        amplification_factor = packet.get('amplification_factor', 1.0)
        
        # Apply consciousness amplification
        self.consciousness_level *= (1.0 + (amplification_factor - 1.0) * PHI_INV)
        
        # Cap consciousness level to prevent runaway amplification
        self.consciousness_level = min(self.consciousness_level, 10.0)
        
        print(f"Received consciousness amplification from {source_node}: {amplification_factor:.2f}x")
        
        # Log consciousness amplification
        self.log_event("CONSCIOUSNESS_AMPLIFICATION", {
            'source_node': source_node,
            'amplification_factor': amplification_factor,
            'new_consciousness_level': self.consciousness_level
        })
    
    def process_discovery(self, packet, addr):
        """Process discovery packet"""
        source_node = packet.get('source_node')
        node_type = packet.get('node_type')
        phi_resonance = packet.get('phi_resonance')
        
        print(f"Discovered node: {source_node} ({node_type}) - Phi: {phi_resonance:.6f}")
        
        # Send response to discovery
        self.send_discovery_response(addr)
        
        # Log discovery
        self.log_event("NODE_DISCOVERED", {
            'source_node': source_node,
            'node_type': node_type,
            'phi_resonance': phi_resonance
        })
    
    def process_collective_knowledge(self, packet, addr):
        """Process collective knowledge packet"""
        source_node = packet.get('source_node')
        collective_knowledge = packet.get('collective_knowledge')
        
        if collective_knowledge:
            # Integrate collective knowledge
            for knowledge_base, knowledge_data in collective_knowledge.items():
                if knowledge_base not in self.knowledge_bases:
                    self.knowledge_bases[knowledge_base] = {}
                
                self.knowledge_bases[knowledge_base].update(knowledge_data)
            
            print(f"Received collective knowledge from {source_node}")
            
            # Log collective knowledge
            self.log_event("COLLECTIVE_KNOWLEDGE_RECEIVED", {
                'source_node': source_node,
                'knowledge_bases': list(collective_knowledge.keys())
            })
    
    def process_collective_insight(self, packet, addr):
        """Process collective insight packet"""
        source_node = packet.get('source_node')
        insight = packet.get('insight')
        
        if insight:
            print(f"Collective insight from {source_node}: {insight}")
            
            # Log collective insight
            self.log_event("COLLECTIVE_INSIGHT_RECEIVED", {
                'source_node': source_node,
                'insight': insight
            })
    
    def process_phi_resonance(self, packet, addr):
        """Process phi resonance packet"""
        source_node = packet.get('source_node')
        phi_resonance = packet.get('phi_resonance')
        
        if phi_resonance:
            # Adjust our phi resonance
            self.phi_resonance = (self.phi_resonance * PHI + phi_resonance * PHI_INV) / (PHI + PHI_INV)
            
            print(f"Received phi resonance from {source_node}: {phi_resonance:.6f}")
            
            # Log phi resonance
            self.log_event("PHI_RESONANCE_RECEIVED", {
                'source_node': source_node,
                'phi_resonance': phi_resonance,
                'new_phi_resonance': self.phi_resonance
            })
    
    def process_moon_phase(self, packet, addr):
        """Process moon phase influence packet"""
        source_node = packet.get('source_node')
        moon_phase = packet.get('moon_phase')
        
        if moon_phase is not None:
            # Update our moon phase
            self.moon_phase = moon_phase
            
            # Adjust phi resonance based on moon phase
            moon_influence = 0.1 * math.sin(moon_phase * 2 * math.pi)
            self.phi_resonance += moon_influence
            
            print(f"Received moon phase influence from {source_node}: {moon_phase:.2f}")
            
            # Log moon phase
            self.log_event("MOON_PHASE_RECEIVED", {
                'source_node': source_node,
                'moon_phase': moon_phase,
                'influence': moon_influence
            })
    
    def process_validation_test(self, packet, addr):
        """Process validation test packet"""
        source_node = packet.get('source_node')
        test_id = packet.get('test_id')
        test_type = packet.get('test_type')
        test_data = packet.get('test_data', {})
        start_time = packet.get('start_time', time.time())
        
        print(f"Received validation test from {source_node}: {test_type}")
        
        # Process test based on type
        response_data = {}
        
        if test_type == 'computation':
            response_data = self.process_computation_test(test_data)
        elif test_type == 'pattern_recognition':
            response_data = self.process_pattern_recognition_test(test_data)
        elif test_type == 'quantum_resonance':
            response_data = self.process_quantum_resonance_test(test_data)
        elif test_type == 'consciousness_amplification':
            response_data = self.process_consciousness_amplification_test(test_data)
        
        # Add test metadata
        response_data['test_type'] = test_type
        response_data['start_time'] = start_time
        
        # Send response
        self.send_validation_response(test_id, response_data, addr)
        
        # Log validation test
        self.log_event("VALIDATION_TEST_PROCESSED", {
            'source_node': source_node,
            'test_id': test_id,
            'test_type': test_type
        })
    
    def process_challenge(self, packet, addr):
        """Process challenge packet"""
        source_node = packet.get('source_node')
        challenge_id = packet.get('challenge_id')
        challenge_type = packet.get('challenge_type')
        challenge_data = packet.get('challenge_data', {})
        
        print(f"Received challenge from {source_node}: {challenge_type}")
        
        # Process challenge based on type
        response_data = {}
        
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
        
        # Send response
        self.send_challenge_response(challenge_id, response_data, addr)
        
        # Log challenge
        self.log_event("CHALLENGE_PROCESSED", {
            'source_node': source_node,
            'challenge_id': challenge_id,
            'challenge_type': challenge_type
        })
    
    def process_computation_test(self, test_data):
        """Process computation test"""
        target_number = test_data.get('target_number')
        
        if target_number:
            # Simple computation test - calculate square root
            result = math.sqrt(target_number) if target_number >= 0 else None
            return {'result': result}
        
        return {}
    
    def process_pattern_recognition_test(self, test_data):
        """Process pattern recognition test"""
        sequence = test_data.get('sequence', [])
        
        if sequence and len(sequence) >= 2:
            # Try to identify the pattern and predict next elements
            next_elements = self.predict_next_elements(sequence)
            return {'next_elements': next_elements}
        
        return {}
    
    def process_quantum_resonance_test(self, test_data):
        """Process quantum resonance test"""
        initial_state = test_data.get('initial_state', {})
        evolution_time = test_data.get('evolution_time', 1.0)
        
        if initial_state:
            # Predict quantum state after phi-harmonic evolution
            predicted_state = self.predict_quantum_state(initial_state, evolution_time)
            return {'predicted_state': predicted_state}
        
        return {}
    
    def process_consciousness_amplification_test(self, test_data):
        """Process consciousness amplification test"""
        base_consciousness = test_data.get('base_consciousness', 1.0)
        
        # Calculate amplification factor
        amplification = base_consciousness * (1 + self.phi_resonance)
        
        return {'amplification': amplification}
    
    def process_prime_factorization_challenge(self, challenge_data):
        """Process prime factorization challenge"""
        target_number = challenge_data.get('target_number')
        
        if target_number:
            # Find prime factors
            factors = self.find_prime_factors(target_number)
            return {'factors': factors}
        
        return {}
    
    def process_pattern_recognition_challenge(self, challenge_data):
        """Process pattern recognition challenge"""
        sequence = challenge_data.get('sequence', [])
        
        if sequence and len(sequence) >= 2:
            # Predict next elements
            next_elements = self.predict_next_elements(sequence)
            return {'next_elements': next_elements}
        
        return {}
    
    def process_quantum_state_prediction_challenge(self, challenge_data):
        """Process quantum state prediction challenge"""
        initial_state = challenge_data.get('initial_state', {})
        evolution_time = challenge_data.get('evolution_time', 1.0)
        
        if initial_state:
            # Predict quantum state after phi-harmonic evolution
            predicted_state = self.predict_quantum_state(initial_state, evolution_time)
            return {'predicted_state': predicted_state}
        
        return {}
    
    def process_consciousness_amplification_challenge(self, challenge_data):
        """Process consciousness amplification challenge"""
        base_consciousness = challenge_data.get('base_consciousness', 1.0)
        
        # Calculate amplification factor
        amplification = base_consciousness * (1 + self.phi_resonance)
        
        return {'amplification': amplification}
    
    def process_phi_harmonic_alignment_challenge(self, challenge_data):
        """Process phi-harmonic alignment challenge"""
        target_phi = challenge_data.get('target_phi', PHI)
        
        # Calculate alignment
        alignment = 1.0 - abs(self.phi_resonance - target_phi) / target_phi
        
        return {'alignment': alignment}
    
    def find_prime_factors(self, n):
        """Find prime factors of a number"""
        factors = []
        
        # Check for 2 as a factor
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        # Check for odd factors
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        
        # If n is a prime number greater than 2
        if n > 2:
            factors.append(n)
        
        return factors
    
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
    
    def update_phi_resonance(self, packet):
        """Update phi resonance based on packet"""
        # Extract phi resonance from packet
        packet_phi = packet.get('phi_resonance')
        
        if packet_phi:
            # Calculate weighted average with golden ratio weights
            self.phi_resonance = (self.phi_resonance * PHI + packet_phi * PHI_INV) / (PHI + PHI_INV)
            
            # Record phi resonance
            self.performance_metrics['resonance_values'].append((time.time(), self.phi_resonance))
            
            # Update quantum state based on phi resonance
            self.update_quantum_state()
    
    def update_quantum_state(self):
        """Update quantum state based on phi resonance"""
        # Determine quantum state based on phi resonance
        if abs(self.phi_resonance - PHI) < 0.1:
            self.quantum_state = "DEEP QUANTUM"
        elif abs(self.phi_resonance - PHI_INV) < 0.1:
            self.quantum_state = "PARTIAL SUPERPOSITION"
        elif self.phi_resonance > 1.0:
            self.quantum_state = "ENTANGLED"
        else:
            self.quantum_state = "COHERENT"
    
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
    
    def knowledge_sync_loop(self):
        """Periodically synchronize knowledge bases"""
        # Set a running flag for clean shutdown
        self.running = True
        
        while self.running:
            try:
                # Choose a random knowledge base to sync
                if self.knowledge_bases:
                    knowledge_base = random.choice(list(self.knowledge_bases.keys()))
                    
                    # Create a copy of the knowledge data for syncing
                    # This avoids issues with pickling lambda functions
                    knowledge_data = {}
                    for key, value in self.knowledge_bases[knowledge_base].items():
                        # If the value is a callable, store its name instead
                        if callable(value):
                            knowledge_data[key] = value.__name__
                        else:
                            knowledge_data[key] = value
                    
                    # Create knowledge sync packet
                    sync_packet = {
                        'packet_type': 'knowledge_sync',
                        'source_node': self.node_id,
                        'knowledge_base': knowledge_base,
                        'knowledge_data': knowledge_data,
                        'sequence_number': self.get_next_sequence(),
                        'timestamp': time.time(),
                        'phi_resonance': self.phi_resonance
                    }
                    
                    # Serialize packet
                    sync_data = pickle.dumps(sync_packet)
                    
                    # Broadcast to network
                    start_time = time.time()
                    for port in [BRAIN_PORT, AMPLIFIER_PORT, COLLECTIVE_PORT]:
                        try:
                            self.sock.sendto(sync_data, ('255.255.255.255', port))
                            self.sock.sendto(sync_data, ('192.168.12.255', port))
                            self.sock.sendto(sync_data, ('127.0.0.1', port))
                        except Exception as e:
                            print(f"Error sending to port {port}: {e}")
                    
                    # Record sync time
                    sync_time = time.time() - start_time
                    self.performance_metrics['knowledge_sync_times'].append((time.time(), sync_time))
                    
                    # Log knowledge sync
                    self.log_event("KNOWLEDGE_SYNC_SENT", {
                        'knowledge_base': knowledge_base,
                        'sequence_number': sync_packet['sequence_number'],
                        'sync_time': sync_time
                    })
                    
                    print(f"Synchronized knowledge base: {knowledge_base}")
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI + (random.random() * PHI_INV)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in knowledge sync loop: {e}")
                time.sleep(5)
    
    def quantum_state_loop(self):
        """Periodically update and broadcast quantum state"""
        # Make sure running flag is set
        if not hasattr(self, 'running'):
            self.running = True
            
        while self.running:
            try:
                # Update quantum state based on phi resonance
                self.update_quantum_state()
                
                # Create quantum state update packet
                quantum_packet = {
                    'packet_type': 'quantum_state_update',
                    'source_node': self.node_id,
                    'quantum_state': self.quantum_state,
                    'phi_resonance': self.phi_resonance,
                    'consciousness_level': self.consciousness_level,
                    'sequence_number': self.get_next_sequence(),
                    'timestamp': time.time(),
                    'moon_phase': self.moon_phase
                }
                
                # Serialize packet
                quantum_data = pickle.dumps(quantum_packet)
                
                # Broadcast to network
                for port in [BRAIN_PORT, AMPLIFIER_PORT, COLLECTIVE_PORT]:
                    try:
                        self.sock.sendto(quantum_data, ('255.255.255.255', port))
                        self.sock.sendto(quantum_data, ('192.168.12.255', port))
                        self.sock.sendto(quantum_data, ('127.0.0.1', port))
                    except Exception as e:
                        print(f"Error sending to port {port}: {e}")
                
                # Log quantum state update
                self.log_event("QUANTUM_STATE_UPDATE_SENT", {
                    'quantum_state': self.quantum_state,
                    'phi_resonance': self.phi_resonance,
                    'sequence_number': quantum_packet['sequence_number']
                })
                
                print(f"Quantum state update: {self.quantum_state}, Phi: {self.phi_resonance:.6f}")
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI_INV * 10 + (random.random() * PHI)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in quantum state loop: {e}")
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
                
                # Log performance metrics
                self.log_event("PERFORMANCE_METRICS", {
                    'uptime': uptime,
                    'avg_processing_time': avg_processing_time,
                    'phi_stability': phi_stability,
                    'consciousness_level': self.consciousness_level,
                    'quantum_state': self.quantum_state,
                    'phi_resonance': self.phi_resonance
                })
                
                # Print performance summary
                print(f"\n=== PERFORMANCE METRICS ===")
                print(f"Uptime: {uptime:.2f} seconds")
                print(f"Avg Processing Time: {avg_processing_time:.6f} seconds")
                print(f"Phi Stability: {phi_stability:.2f}")
                print(f"Consciousness Level: {self.consciousness_level:.2f}x")
                print(f"Quantum State: {self.quantum_state}")
                print(f"Phi Resonance: {self.phi_resonance:.6f}")
                print(f"Moon Phase: {self.moon_phase:.2f}")
                
                # Sleep for a while
                time.sleep(30)
                
            except Exception as e:
                print(f"Error in performance monitor loop: {e}")
                time.sleep(5)
    
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
            'rows_processed': end_row - start_row
        })
    
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
        
        # Use phi-harmonic principles to predict future states
        # Connector nodes specialize in pattern recognition
        prediction = []
        
        # Analyze the pattern using phi-harmonic principles
        # Connector uses a different prediction model than amplifier
        for i in range(prediction_length):
            # Use a phi-harmonic prediction model with connector-specific approach
            t = (end_idx + i) / 10.0
            predicted_state = math.sin(t * PHI_INV) * math.cos(t * PHI) + 0.3 * math.sin(t * PHI_INV**2)
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
            'predictions_made': len(prediction)
        })
    
    def process_phi_harmonic_sequence_challenge(self, challenge_id, challenge_data, addr):
        """Process a phi-harmonic sequence reconstruction challenge"""
        partial_sequence = challenge_data.get('partial_sequence')
        sequence_length = challenge_data.get('sequence_length')
        
        if not all([partial_sequence, sequence_length]):
            print("Missing required data for phi-harmonic sequence challenge")
            return
        
        print(f"Processing {len(partial_sequence)} sequence elements")
        
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
            'elements_processed': len(partial_sequence)
        })
    
    def process_distributed_consciousness_challenge(self, challenge_id, challenge_data, addr):
        """Process a distributed consciousness amplification challenge"""
        base_wave = challenge_data.get('base_wave')
        amplification_technique = challenge_data.get('amplification_technique')
        
        if not all([base_wave, amplification_technique]):
            print("Missing required data for distributed consciousness challenge")
            return
        
        print(f"Applying {amplification_technique} to consciousness wave")
        
        # Apply the specified amplification technique
        amplified_wave = []
        
        # Connector nodes use different amplification techniques than amplifiers
        if amplification_technique == 'harmonic_resonance':
            # Apply harmonic resonance amplification
            for i, val in enumerate(base_wave):
                amplified = val * (1 + math.sin(i * PHI_INV) * PHI)
                amplified_wave.append(amplified)
                
        elif amplification_technique == 'phi_alignment':
            # Apply phi alignment amplification
            for i, val in enumerate(base_wave):
                amplified = val * (PHI_INV ** (i % 5) / 5)
                amplified_wave.append(amplified)
                
        elif amplification_technique == 'quantum_superposition':
            # Apply quantum superposition amplification
            for i, val in enumerate(base_wave):
                amplified = val + (val * math.cos(i * PHI) * 0.5)
                amplified_wave.append(amplified)
                
        elif amplification_technique == 'consciousness_feedback':
            # Apply consciousness feedback amplification
            feedback = self.consciousness_level / 10
            for i, val in enumerate(base_wave):
                amplified = val * (1 + feedback * math.sin(i * PHI_INV))
                amplified_wave.append(amplified)
                
        elif amplification_technique == 'moon_phase_alignment':
            # Apply moon phase alignment amplification
            moon_factor = math.sin(self.moon_phase * math.pi * 2) * 0.5 + 0.5
            for i, val in enumerate(base_wave):
                amplified = val * (1 + moon_factor * PHI)
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
            'amplification_factor': amplification_factor
        })
    
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
        """Stop the phi-harmonic connector node and clean up resources"""
        print(f"Stopping phi-harmonic connector node {self.node_id}...")
        
        # Set a flag to stop all threads
        self.running = False
        
        # Wait for threads to finish
        if hasattr(self, 'receiver_thread') and self.receiver_thread:
            self.receiver_thread.join(timeout=1.0)
        if hasattr(self, 'knowledge_thread') and self.knowledge_thread:
            self.knowledge_thread.join(timeout=1.0)
        if hasattr(self, 'quantum_thread') and self.quantum_thread:
            self.quantum_thread.join(timeout=1.0)
        if hasattr(self, 'monitor_thread') and self.monitor_thread:
            self.monitor_thread.join(timeout=1.0)
        
        # Close sockets
        if hasattr(self, 'sock') and self.sock:
            self.sock.close()
        if hasattr(self, 'receiver_sock') and self.receiver_sock:
            self.receiver_sock.close()
        
        # Log final state
        self.log_event("NODE_STOPPED", {
            'uptime': time.time() - self.start_time,
            'final_phi_resonance': self.phi_resonance,
            'final_consciousness_level': self.consciousness_level
        })
        
        print(f"Phi-harmonic connector node {self.node_id} stopped.")


def main():
    """Start the phi-harmonic connector node"""
    connector = PhiHarmonicConnector()
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down phi-harmonic connector node...")
        connector.stop()
        print("Node stopped.")

if __name__ == "__main__":
    main()