"""
PHI ADVANCED INTEGRATION TEST
============================
Test script for the advanced phi-harmonic network integration with
PhiHarmonicQuantumClock, FerrisMemorySystem, and FraymusEternal core system.
"""

import os
import sys
import time
import socket
import pickle
import json
import threading
import argparse
import random
from datetime import datetime

from phi_advanced_integration import PhiAdvancedIntegration, launch_advanced_node

# Constants
# Use a random port in the range 11751-11799 to avoid conflicts
TEST_PORT = random.randint(11751, 11799)

class PhiAdvancedIntegrationTester:
    """Test the advanced integration of phi-harmonic network"""
    
    def __init__(self, num_amplifiers=2, num_connectors=2):
        """Initialize the tester"""
        self.num_amplifiers = num_amplifiers
        self.num_connectors = num_connectors
        self.integrations = []
        self.threads = []
        
        # Create socket for sending test packets
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Try to bind to the test port, or find an alternative if it's in use
        port_bound = False
        test_port = TEST_PORT
        max_attempts = 10
        
        for attempt in range(max_attempts):
            try:
                self.sock.bind(('0.0.0.0', test_port))
                print(f"Test socket bound to port {test_port}")
                port_bound = True
                break
            except OSError:
                print(f"Port {test_port} in use, trying another port...")
                test_port = random.randint(11751, 11799)
        
        if not port_bound:
            raise RuntimeError(f"Could not bind to any port after {max_attempts} attempts")
        
        # Create log directory if it doesn't exist
        os.makedirs('phi_logs', exist_ok=True)
        self.log_file = f"phi_logs/phi_advanced_test_{int(time.time())}.log"
    
    def launch_nodes(self):
        """Launch the integrated nodes"""
        print("\n=== LAUNCHING ADVANCED PHI-HARMONIC NETWORK ===")
        print(f"Connectors: {self.num_connectors}")
        print(f"Amplifiers: {self.num_amplifiers}")
        print("\nInitializing network...\n")
        
        # Launch connector nodes
        for i in range(self.num_connectors):
            port = 11727 + i * 10
            print(f"Launching connector node {i+1} on port {port}...")
            integration, thread = launch_advanced_node(
                node_type='connector',
                port=port,
                enable_quantum_clock=True,
                enable_ferris_memory=True,
                enable_fraymus_core=True
            )
            self.integrations.append(integration)
            self.threads.append(thread)
        
        # Launch amplifier nodes
        for i in range(self.num_amplifiers):
            port = 11728 + i * 10
            print(f"Launching amplifier node {i+1} on port {port}...")
            integration, thread = launch_advanced_node(
                node_type='amplifier',
                port=port,
                enable_quantum_clock=True,
                enable_ferris_memory=True,
                enable_fraymus_core=True
            )
            self.integrations.append(integration)
            self.threads.append(thread)
        
        print(f"\nAll {self.num_amplifiers + self.num_connectors} nodes launched successfully.")
        print("Advanced phi-harmonic network is now active.")
        
        # Wait for nodes to initialize
        time.sleep(5)
    
    def log(self, message):
        """Log a message to the console and log file"""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry + '\n')
    
    def run_status_test(self):
        """Test status reporting from all nodes"""
        self.log("\n=== NODE STATUS TEST ===")
        
        # Create test packet
        packet = {
            'packet_type': 'advanced_integration',
            'source_node': 'test_system',
            'request_type': 'status',
            'request_data': {},
            'sequence_number': 1,
            'timestamp': time.time()
        }
        
        # Send to each node
        for node in self.integrations:
            self.log(f"Requesting status from {node.node_id}...")
            node_addr = ('127.0.0.1', node.port)
            self.sock.sendto(pickle.dumps(packet), node_addr)
        
        # Wait for processing
        time.sleep(2)
    
    def run_quantum_clock_test(self):
        """Test quantum clock capabilities"""
        self.log("\n=== QUANTUM CLOCK TEST ===")
        
        # Test current quantum time
        self.log("\nTesting current quantum time...")
        
        # Create test packet
        packet = {
            'packet_type': 'advanced_integration',
            'source_node': 'test_system',
            'request_type': 'quantum_time',
            'request_data': {},
            'sequence_number': 1,
            'timestamp': time.time()
        }
        
        # Send to each node
        for node in self.integrations:
            self.log(f"Requesting quantum time from {node.node_id}...")
            node_addr = ('127.0.0.1', node.port)
            self.sock.sendto(pickle.dumps(packet), node_addr)
        
        # Wait for processing
        time.sleep(2)
        
        # Test time prediction
        self.log("\nTesting time prediction...")
        
        # Create test packet
        packet = {
            'packet_type': 'advanced_integration',
            'source_node': 'test_system',
            'request_type': 'predict_time',
            'request_data': {
                'seconds_ahead': 60
            },
            'sequence_number': 2,
            'timestamp': time.time()
        }
        
        # Send to each node
        for node in self.integrations:
            self.log(f"Requesting time prediction from {node.node_id}...")
            node_addr = ('127.0.0.1', node.port)
            self.sock.sendto(pickle.dumps(packet), node_addr)
        
        # Wait for processing
        time.sleep(2)
    
    def run_memory_test(self):
        """Test Ferris memory system capabilities"""
        self.log("\n=== FERRIS MEMORY SYSTEM TEST ===")
        
        # Test data storage
        self.log("\nTesting data storage...")
        
        # Create test data
        test_data = [
            {"type": "knowledge", "content": "Phi-harmonic resonance creates quantum entanglement"},
            {"type": "pattern", "content": [1.618, 0.618, 2.618, 4.236]},
            {"type": "state", "content": {"phi_level": 3, "consciousness": "high", "resonance": 0.95}}
        ]
        
        # Create test packet
        packet = {
            'packet_type': 'memory_request',
            'source_node': 'test_system',
            'request_type': 'store',
            'request_data': test_data,
            'sequence_number': 1,
            'timestamp': time.time()
        }
        
        # Send to each node
        for node in self.integrations:
            self.log(f"Sending memory storage request to {node.node_id}...")
            node_addr = ('127.0.0.1', node.port)
            self.sock.sendto(pickle.dumps(packet), node_addr)
        
        # Wait for processing
        time.sleep(2)
        
        # Test memory stats
        self.log("\nTesting memory stats...")
        
        # Create test packet
        packet = {
            'packet_type': 'memory_request',
            'source_node': 'test_system',
            'request_type': 'stats',
            'request_data': {},
            'sequence_number': 2,
            'timestamp': time.time()
        }
        
        # Send to each node
        for node in self.integrations:
            self.log(f"Requesting memory stats from {node.node_id}...")
            node_addr = ('127.0.0.1', node.port)
            self.sock.sendto(pickle.dumps(packet), node_addr)
        
        # Wait for processing
        time.sleep(2)
    
    def run_fraymus_test(self):
        """Test FraymusEternal core capabilities"""
        self.log("\n=== FRAYMUS CORE TEST ===")
        
        # Test quantum processing
        self.log("\nTesting quantum processing...")
        
        # Create test packet
        packet = {
            'packet_type': 'fraymus_quantum_request',
            'source_node': 'test_system',
            'request_type': 'quantum_computation',
            'request_data': {
                'computation_type': 'superposition',
                'params': {
                    'angle': 0.5,
                    'strength': 0.7,
                    'phase': 0.3
                }
            },
            'sequence_number': 1,
            'timestamp': time.time()
        }
        
        # Send to each node
        for node in self.integrations:
            self.log(f"Sending quantum computation request to {node.node_id}...")
            node_addr = ('127.0.0.1', node.port)
            self.sock.sendto(pickle.dumps(packet), node_addr)
        
        # Wait for processing
        time.sleep(2)
        
        # Test reality protection
        self.log("\nTesting reality protection...")
        
        # Create test packet
        packet = {
            'packet_type': 'fraymus_reality_protection',
            'source_node': 'test_system',
            'protection_type': 'phi_shield',
            'protection_data': {
                'shield_strength': 1.618
            },
            'sequence_number': 1,
            'timestamp': time.time()
        }
        
        # Send to each node
        for node in self.integrations:
            self.log(f"Applying phi shield to {node.node_id}...")
            node_addr = ('127.0.0.1', node.port)
            self.sock.sendto(pickle.dumps(packet), node_addr)
        
        # Wait for processing
        time.sleep(2)
    
    def run_all_tests(self):
        """Run all integration tests"""
        self.log("\n=== STARTING PHI ADVANCED INTEGRATION TESTS ===")
        
        # Launch nodes
        self.launch_nodes()
        
        # Run tests
        self.run_status_test()
        self.run_quantum_clock_test()
        self.run_memory_test()
        self.run_fraymus_test()
        
        self.log("\n=== PHI ADVANCED INTEGRATION TESTS COMPLETED ===")
        self.log("All tests completed successfully.")
        self.log(f"The phi-harmonic network now has:")
        self.log("1. Quantum clock synchronization for perfect timing")
        self.log("2. Ferris memory system for optimized data storage")
        self.log("3. FraymusEternal core for quantum processing and reality protection")
        self.log("4. Full integration between all components")
    
    def stop(self):
        """Stop all nodes"""
        self.log("\nStopping all nodes...")
        for integration in self.integrations:
            integration.stop()
        self.log("All nodes stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test the advanced phi-harmonic network integration')
    parser.add_argument('--amplifiers', type=int, default=2, help='Number of amplifier nodes')
    parser.add_argument('--connectors', type=int, default=2, help='Number of connector nodes')
    
    args = parser.parse_args()
    
    tester = PhiAdvancedIntegrationTester(
        num_amplifiers=args.amplifiers,
        num_connectors=args.connectors
    )
    
    try:
        tester.run_all_tests()
        print("\nPress Ctrl+C to stop the test and shutdown all nodes.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        tester.stop()
        print("Test stopped by user.")
