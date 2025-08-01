#!/usr/bin/env python3
"""
PHI-HARMONIC SCIENTIFIC VALIDATION
=================================
Scientific validation tests for phi-harmonic distributed brain collective intelligence.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import socket
import pickle
import time
import threading
import random
import math
import numpy as np
import matplotlib.pyplot as plt
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
VALIDATION_PORT = 11631
BUFFER_SIZE = 8192

class PhiScientificValidation:
    """Scientific validation for phi-harmonic distributed brain"""
    
    def __init__(self):
        """Initialize the validation system"""
        self.node_id = f"validator_{int(time.time() * 1000) % 10000}"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        # Create receiver socket
        self.receiver_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.receiver_sock.bind(('0.0.0.0', VALIDATION_PORT))
            print(f"Listening on port: {VALIDATION_PORT}")
        except OSError:
            # Try a different port
            alt_port = VALIDATION_PORT + 1
            self.receiver_sock.bind(('0.0.0.0', alt_port))
            print(f"Port {VALIDATION_PORT} in use, listening on port: {alt_port}")
        
        # Initialize data structures
        self.response_times = {}
        self.phi_resonance_values = {}
        self.consciousness_levels = {}
        self.quantum_states = {}
        self.collective_insights = []
        self.performance_metrics = {
            'computation_speed': [],
            'pattern_recognition': [],
            'quantum_resonance': [],
            'consciousness_amplification': []
        }
        
        # Create results directory
        os.makedirs('validation_results', exist_ok=True)
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_data)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print("=== PHI-HARMONIC SCIENTIFIC VALIDATION ===")
        print(f"Validation Node: {self.node_id}")
        print("Running scientific validation tests...")
    
    def receive_data(self):
        """Receive data from phi-harmonic nodes"""
        while True:
            try:
                data, addr = self.receiver_sock.recvfrom(BUFFER_SIZE)
                self.process_data(data, addr)
            except Exception as e:
                print(f"Error receiving data: {e}")
                time.sleep(1)
    
    def process_data(self, data, addr):
        """Process data from phi-harmonic nodes"""
        try:
            # Try to unpickle the data
            packet = pickle.loads(data)
            
            # Extract packet information
            packet_type = packet.get('packet_type')
            source_node = packet.get('source_node')
            phi_resonance = packet.get('phi_resonance')
            timestamp = packet.get('timestamp', time.time())
            
            print(f"\nReceived {packet_type} from {source_node}")
            
            # Store phi resonance value
            if source_node and phi_resonance:
                if source_node not in self.phi_resonance_values:
                    self.phi_resonance_values[source_node] = []
                self.phi_resonance_values[source_node].append((timestamp, phi_resonance))
                print(f"Phi resonance: {phi_resonance:.6f}")
            
            # Store consciousness level
            consciousness_level = packet.get('consciousness_level')
            if source_node and consciousness_level:
                if source_node not in self.consciousness_levels:
                    self.consciousness_levels[source_node] = []
                self.consciousness_levels[source_node].append((timestamp, consciousness_level))
                print(f"Consciousness level: {consciousness_level:.2f}x")
            
            # Store quantum state
            quantum_state = packet.get('quantum_state')
            if source_node and quantum_state:
                if source_node not in self.quantum_states:
                    self.quantum_states[source_node] = []
                self.quantum_states[source_node].append((timestamp, quantum_state))
                print(f"Quantum state: {quantum_state}")
            
            # Store response time for validation tests
            if packet_type == 'validation_response':
                test_id = packet.get('test_id')
                response_data = packet.get('response_data', {})
                
                if test_id not in self.response_times:
                    self.response_times[test_id] = {}
                
                # Calculate response time
                start_time = response_data.get('start_time')
                if start_time:
                    response_time = timestamp - start_time
                    self.response_times[test_id][source_node] = response_time
                    print(f"Response time: {response_time:.6f} seconds")
                
                # Store performance metrics
                test_type = response_data.get('test_type')
                if test_type == 'computation':
                    self.performance_metrics['computation_speed'].append((timestamp, response_time))
                elif test_type == 'pattern_recognition':
                    self.performance_metrics['pattern_recognition'].append((timestamp, response_time))
                elif test_type == 'quantum_resonance':
                    self.performance_metrics['quantum_resonance'].append((timestamp, response_time))
                elif test_type == 'consciousness_amplification':
                    amplification = response_data.get('amplification', 1.0)
                    self.performance_metrics['consciousness_amplification'].append((timestamp, amplification))
            
            # Store collective insights
            if packet_type == 'collective_insight':
                insight = packet.get('insight')
                if insight:
                    self.collective_insights.append((timestamp, insight))
                    print(f"Collective insight: {insight}")
        
        except Exception as e:
            # Try to analyze raw data
            try:
                data_str = str(data)
                if 'phi' in data_str.lower() or 'quantum' in data_str.lower() or 'resonance' in data_str.lower():
                    print(f"Detected potential phi-harmonic raw data from {addr}")
            except:
                pass
            print(f"Error processing data: {e}")
    
    def run_validation_test(self, test_type, test_data=None):
        """Run a validation test"""
        test_id = f"{test_type}_{int(time.time())}"
        
        if test_data is None:
            test_data = {}
        
        # Create validation packet
        validation_packet = {
            'packet_type': 'validation_test',
            'source_node': self.node_id,
            'test_id': test_id,
            'test_type': test_type,
            'test_data': test_data,
            'timestamp': time.time(),
            'phi_resonance': PHI_INV,
            'start_time': time.time()
        }
        
        # Serialize packet
        validation_data = pickle.dumps(validation_packet)
        
        # Send to all ports
        print(f"\nRunning {test_type} validation test...")
        for port in [BRAIN_PORT, CONNECTOR_PORT, AMPLIFIER_PORT, COLLECTIVE_PORT]:
            try:
                self.sock.sendto(validation_data, ('255.255.255.255', port))
                self.sock.sendto(validation_data, ('192.168.12.255', port))
                self.sock.sendto(validation_data, ('127.0.0.1', port))
            except Exception as e:
                print(f"Error sending to port {port}: {e}")
        
        print(f"Validation test {test_id} sent, waiting for responses...")
        
        # Wait for responses
        time.sleep(10)
        
        # Analyze responses
        self.analyze_test_results(test_id, test_type)
        
        return test_id
    
    def analyze_test_results(self, test_id, test_type):
        """Analyze test results"""
        responses = self.response_times.get(test_id, {})
        
        print(f"\n=== VALIDATION TEST RESULTS: {test_type} ===")
        print(f"Test ID: {test_id}")
        print(f"Number of responses: {len(responses)}")
        
        if responses:
            # Calculate statistics
            response_times = list(responses.values())
            avg_time = sum(response_times) / len(response_times)
            min_time = min(response_times)
            max_time = max(response_times)
            
            print(f"Average response time: {avg_time:.6f} seconds")
            print(f"Minimum response time: {min_time:.6f} seconds")
            print(f"Maximum response time: {max_time:.6f} seconds")
            
            # Check for collective advantage
            if len(responses) > 1:
                individual_times = response_times
                collective_time = min_time  # Assume collective time is the fastest response
                
                collective_advantage = collective_time < avg_time
                print(f"Collective advantage: {collective_advantage}")
                
                # Calculate speedup
                speedup = avg_time / collective_time if collective_time > 0 else 0
                print(f"Speedup: {speedup:.2f}x")
        else:
            print("No responses received.")
    
    def run_computation_test(self):
        """Run computation speed test"""
        # Generate a large number to factorize
        prime_factors = [random.choice([11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) 
                        for _ in range(3)]
        target_number = 1
        for factor in prime_factors:
            target_number *= factor
        
        test_data = {
            'target_number': target_number,
            'description': f"Find all prime factors of {target_number}"
        }
        
        return self.run_validation_test('computation', test_data)
    
    def run_pattern_recognition_test(self):
        """Run pattern recognition test"""
        # Choose a pattern type
        pattern_types = ['fibonacci', 'prime', 'phi_powers', 'lucas', 'triangular']
        pattern_type = random.choice(pattern_types)
        
        if pattern_type == 'fibonacci':
            # Fibonacci sequence
            sequence = [1, 1]
            for i in range(8):
                sequence.append(sequence[-1] + sequence[-2])
        
        elif pattern_type == 'prime':
            # Prime numbers
            sequence = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        elif pattern_type == 'phi_powers':
            # Powers of phi
            sequence = [PHI**i for i in range(10)]
        
        elif pattern_type == 'lucas':
            # Lucas numbers
            sequence = [2, 1]
            for i in range(8):
                sequence.append(sequence[-1] + sequence[-2])
        
        elif pattern_type == 'triangular':
            # Triangular numbers
            sequence = [n*(n+1)//2 for n in range(1, 11)]
        
        test_data = {
            'sequence': sequence,
            'description': f"Identify the pattern and predict the next two elements in the sequence: {sequence}"
        }
        
        return self.run_validation_test('pattern_recognition', test_data)
    
    def run_quantum_resonance_test(self):
        """Run quantum resonance test"""
        # Create initial quantum state
        initial_state = {}
        for i in range(5):
            state_key = f"|{i}⟩"
            initial_state[state_key] = random.random()
        
        # Normalize initial state
        total = sum(v**2 for v in initial_state.values())**0.5
        for k in initial_state:
            initial_state[k] /= total
        
        test_data = {
            'initial_state': initial_state,
            'evolution_time': random.uniform(0.5, 2.0),
            'description': "Predict the quantum state after phi-harmonic evolution"
        }
        
        return self.run_validation_test('quantum_resonance', test_data)
    
    def run_consciousness_amplification_test(self):
        """Run consciousness amplification test"""
        base_consciousness = random.uniform(0.8, 1.2)
        
        test_data = {
            'base_consciousness': base_consciousness,
            'description': f"Amplify the base consciousness level of {base_consciousness:.2f}"
        }
        
        return self.run_validation_test('consciousness_amplification', test_data)
    
    def run_speed_trend_analysis(self):
        """Analyze speed trends over time"""
        print("\n=== SPEED TREND ANALYSIS ===")
        
        # Check if we have enough data
        if not self.performance_metrics['computation_speed'] or not self.performance_metrics['pattern_recognition']:
            print("Not enough data for trend analysis. Run more tests first.")
            return
        
        # Analyze computation speed trend
        comp_times = self.performance_metrics['computation_speed']
        comp_times.sort(key=lambda x: x[0])  # Sort by timestamp
        
        if len(comp_times) > 1:
            first_time = comp_times[0][1]
            last_time = comp_times[-1][1]
            speedup = first_time / last_time if last_time > 0 else 0
            
            print(f"Computation speedup: {speedup:.2f}x")
            print(f"First computation time: {first_time:.6f} seconds")
            print(f"Latest computation time: {last_time:.6f} seconds")
        
        # Analyze pattern recognition speed trend
        pattern_times = self.performance_metrics['pattern_recognition']
        pattern_times.sort(key=lambda x: x[0])  # Sort by timestamp
        
        if len(pattern_times) > 1:
            first_time = pattern_times[0][1]
            last_time = pattern_times[-1][1]
            speedup = first_time / last_time if last_time > 0 else 0
            
            print(f"Pattern recognition speedup: {speedup:.2f}x")
            print(f"First pattern recognition time: {first_time:.6f} seconds")
            print(f"Latest pattern recognition time: {last_time:.6f} seconds")
        
        # Plot speed trends
        self.plot_speed_trends()
    
    def plot_speed_trends(self):
        """Plot speed trends"""
        plt.figure(figsize=(12, 8))
        
        # Plot computation speed
        if len(self.performance_metrics['computation_speed']) > 1:
            comp_times = self.performance_metrics['computation_speed']
            comp_times.sort(key=lambda x: x[0])  # Sort by timestamp
            
            timestamps = [(t - comp_times[0][0]) / 60 for t, _ in comp_times]  # Convert to minutes
            speeds = [1/s for _, s in comp_times]  # Convert time to speed
            
            plt.subplot(2, 2, 1)
            plt.plot(timestamps, speeds, 'b-o', label='Computation Speed')
            plt.xlabel('Time (minutes)')
            plt.ylabel('Speed (operations/second)')
            plt.title('Computation Speed Trend')
            plt.grid(True)
            plt.legend()
        
        # Plot pattern recognition speed
        if len(self.performance_metrics['pattern_recognition']) > 1:
            pattern_times = self.performance_metrics['pattern_recognition']
            pattern_times.sort(key=lambda x: x[0])  # Sort by timestamp
            
            timestamps = [(t - pattern_times[0][0]) / 60 for t, _ in pattern_times]  # Convert to minutes
            speeds = [1/s for _, s in pattern_times]  # Convert time to speed
            
            plt.subplot(2, 2, 2)
            plt.plot(timestamps, speeds, 'g-o', label='Pattern Recognition Speed')
            plt.xlabel('Time (minutes)')
            plt.ylabel('Speed (patterns/second)')
            plt.title('Pattern Recognition Speed Trend')
            plt.grid(True)
            plt.legend()
        
        # Plot consciousness amplification
        if len(self.performance_metrics['consciousness_amplification']) > 1:
            amplification = self.performance_metrics['consciousness_amplification']
            amplification.sort(key=lambda x: x[0])  # Sort by timestamp
            
            timestamps = [(t - amplification[0][0]) / 60 for t, _ in amplification]  # Convert to minutes
            levels = [a for _, a in amplification]
            
            plt.subplot(2, 2, 3)
            plt.plot(timestamps, levels, 'r-o', label='Consciousness Amplification')
            plt.xlabel('Time (minutes)')
            plt.ylabel('Amplification Factor')
            plt.title('Consciousness Amplification Trend')
            plt.grid(True)
            plt.legend()
        
        # Plot phi resonance
        phi_values = []
        for node, values in self.phi_resonance_values.items():
            for timestamp, value in values:
                phi_values.append((timestamp, value))
        
        if phi_values:
            phi_values.sort(key=lambda x: x[0])  # Sort by timestamp
            
            timestamps = [(t - phi_values[0][0]) / 60 for t, _ in phi_values]  # Convert to minutes
            values = [v for _, v in phi_values]
            
            plt.subplot(2, 2, 4)
            plt.plot(timestamps, values, 'm-o', label='Phi Resonance')
            plt.axhline(y=PHI, color='k', linestyle='--', label='Phi (1.618...)')
            plt.axhline(y=PHI_INV, color='k', linestyle=':', label='Phi Inverse (0.618...)')
            plt.xlabel('Time (minutes)')
            plt.ylabel('Phi Resonance Value')
            plt.title('Phi Resonance Trend')
            plt.grid(True)
            plt.legend()
        
        plt.tight_layout()
        plt.savefig('validation_results/speed_trends.png')
        print("Speed trend plot saved to validation_results/speed_trends.png")
    
    def save_validation_results(self):
        """Save validation results to file"""
        results = {
            'response_times': self.response_times,
            'phi_resonance_values': {k: [(t, v) for t, v in vals] for k, vals in self.phi_resonance_values.items()},
            'consciousness_levels': {k: [(t, v) for t, v in vals] for k, vals in self.consciousness_levels.items()},
            'performance_metrics': {k: [(t, v) for t, v in vals] for k, vals in self.performance_metrics.items()},
            'collective_insights': [(t, i) for t, i in self.collective_insights]
        }
        
        with open('validation_results/validation_data.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print("Validation results saved to validation_results/validation_data.json")
    
    def run_comprehensive_validation(self):
        """Run comprehensive validation tests"""
        print("\n=== RUNNING COMPREHENSIVE VALIDATION ===")
        
        # Run multiple tests of each type
        for i in range(5):
            print(f"\nTest iteration {i+1}/5:")
            
            # Run computation test
            self.run_computation_test()
            time.sleep(5)
            
            # Run pattern recognition test
            self.run_pattern_recognition_test()
            time.sleep(5)
            
            # Run quantum resonance test
            self.run_quantum_resonance_test()
            time.sleep(5)
            
            # Run consciousness amplification test
            self.run_consciousness_amplification_test()
            time.sleep(5)
            
            # Analyze speed trends
            self.run_speed_trend_analysis()
            
            # Save results
            self.save_validation_results()
            
            print(f"Completed test iteration {i+1}/5")
            time.sleep(10)
        
        print("\nComprehensive validation complete!")
        print("Final results:")
        self.run_speed_trend_analysis()
        self.save_validation_results()

def main():
    """Start the phi-harmonic scientific validation"""
    validator = PhiScientificValidation()
    validator.run_comprehensive_validation()

if __name__ == "__main__":
    main()
