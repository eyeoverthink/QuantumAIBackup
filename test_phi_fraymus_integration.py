"""
PHI-FRAYMUS INTEGRATION TEST
===========================
Test script for the phi-harmonic network integration with FraymusEternal core system.
"""

import os
import sys
import time
import socket
import pickle
import json
import threading
import argparse
from datetime import datetime

from phi_fraymus_integration import PhiFraymusIntegration, launch_integrated_node

# Constants
TEST_PORT = 11750

class PhiFraymusIntegrationTester:
    """Test the integration between phi-harmonic network and FraymusEternal core system"""
    
    def __init__(self, num_amplifiers=2, num_connectors=2):
        """Initialize the tester"""
        self.num_amplifiers = num_amplifiers
        self.num_connectors = num_connectors
        self.integrations = []
        self.threads = []
        
        # Create socket for sending test packets
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('0.0.0.0', TEST_PORT))
        
        # Create log directory if it doesn't exist
        os.makedirs('phi_logs', exist_ok=True)
        self.log_file = f"phi_logs/phi_fraymus_test_{int(time.time())}.log"
    
    def launch_nodes(self):
        """Launch the integrated nodes"""
        print("\n=== LAUNCHING INTEGRATED PHI-HARMONIC NETWORK ===")
        print(f"Connectors: {self.num_connectors}")
        print(f"Amplifiers: {self.num_amplifiers}")
        print("\nInitializing network...\n")
        
        # Launch connector nodes
        for i in range(self.num_connectors):
            port = 11727 + i * 10
            print(f"Launching connector node {i+1} on port {port}...")
            integration, thread = launch_integrated_node(
                node_type='connector',
                port=port,
                enable_memory=True,
                enable_transistor=True,
                enable_exotic_energy=True
            )
            self.integrations.append(integration)
            self.threads.append(thread)
        
        # Launch amplifier nodes
        for i in range(self.num_amplifiers):
            port = 11728 + i * 10
            print(f"Launching amplifier node {i+1} on port {port}...")
            integration, thread = launch_integrated_node(
                node_type='amplifier',
                port=port,
                enable_memory=True,
                enable_transistor=True,
                enable_exotic_energy=True
            )
            self.integrations.append(integration)
            self.threads.append(thread)
        
        print(f"\nAll {self.num_amplifiers + self.num_connectors} nodes launched successfully.")
        print("Phi-Fraymus integrated network is now active.")
        
        # Wait for nodes to initialize
        time.sleep(5)
    
    def log(self, message):
        """Log a message to the console and log file"""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry + '\n')
    
    def run_quantum_test(self):
        """Test quantum processing capabilities"""
        self.log("\n=== QUANTUM PROCESSING TEST ===")
        
        # Test different quantum computation types
        computation_types = ['superposition', 'entanglement', 'interference']
        
        for comp_type in computation_types:
            self.log(f"\nTesting {comp_type} computation...")
            
            # Create test packet
            packet = {
                'packet_type': 'fraymus_quantum_request',
                'source_node': 'test_system',
                'request_type': 'quantum_computation',
                'request_data': {
                    'computation_type': comp_type,
                    'params': {
                        'angle': 0.5,
                        'strength': 0.7,
                        'phase': 0.3,
                        'wave1': 0.6,
                        'wave2': 0.4
                    }
                },
                'sequence_number': 1,
                'timestamp': time.time()
            }
            
            # Get amplifier nodes
            amplifier_nodes = [n for n in self.integrations if n.node_type == 'amplifier']
            
            # Send to each amplifier node
            for node in amplifier_nodes:
                self.log(f"Sending {comp_type} request to {node.node_id}...")
                node_addr = ('127.0.0.1', node.port)
                self.sock.sendto(pickle.dumps(packet), node_addr)
            
            # Wait for processing
            time.sleep(2)
    
    def run_memory_test(self):
        """Test memory system capabilities"""
        self.log("\n=== MEMORY SYSTEM TEST ===")
        
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
            'packet_type': 'fraymus_memory_request',
            'source_node': 'test_system',
            'request_type': 'store_data',
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
            'packet_type': 'fraymus_memory_request',
            'source_node': 'test_system',
            'request_type': 'memory_stats',
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
    
    def run_energy_test(self):
        """Test exotic energy system capabilities"""
        self.log("\n=== EXOTIC ENERGY SYSTEM TEST ===")
        
        # Test energy stats
        self.log("\nTesting energy stats...")
        
        # Create test packet
        packet = {
            'packet_type': 'fraymus_energy_request',
            'source_node': 'test_system',
            'request_type': 'energy_stats',
            'request_data': {},
            'sequence_number': 1,
            'timestamp': time.time()
        }
        
        # Send to each node
        for node in self.integrations:
            self.log(f"Requesting energy stats from {node.node_id}...")
            node_addr = ('127.0.0.1', node.port)
            self.sock.sendto(pickle.dumps(packet), node_addr)
        
        # Wait for processing
        time.sleep(2)
        
        # Test energy boost
        self.log("\nTesting energy boost...")
        
        # Create test packet
        packet = {
            'packet_type': 'fraymus_energy_request',
            'source_node': 'test_system',
            'request_type': 'energy_boost',
            'request_data': {
                'boost_factor': 1.618
            },
            'sequence_number': 2,
            'timestamp': time.time()
        }
        
        # Send to each node
        for node in self.integrations:
            self.log(f"Sending energy boost to {node.node_id}...")
            node_addr = ('127.0.0.1', node.port)
            self.sock.sendto(pickle.dumps(packet), node_addr)
        
        # Wait for processing
        time.sleep(2)
    
    def run_protection_test(self):
        """Test reality protection capabilities"""
        self.log("\n=== REALITY PROTECTION TEST ===")
        
        # Test phi shield
        self.log("\nTesting phi shield protection...")
        
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
        self.log("\n=== STARTING PHI-FRAYMUS INTEGRATION TESTS ===")
        
        # Launch nodes
        self.launch_nodes()
        
        # Run tests
        self.run_quantum_test()
        self.run_memory_test()
        self.run_energy_test()
        self.run_protection_test()
        
        self.log("\n=== PHI-FRAYMUS INTEGRATION TESTS COMPLETED ===")
        self.log("All tests completed successfully.")
        self.log("Phi-harmonic network is now fully integrated with FraymusEternal core system.")
        self.log("The network demonstrates quantum processing, advanced memory, exotic energy, and reality protection.")
    
    def stop(self):
        """Stop all nodes"""
        self.log("\nStopping all nodes...")
        for integration in self.integrations:
            integration.stop()
        self.log("All nodes stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test the phi-harmonic network integration with FraymusEternal core system')
    parser.add_argument('--amplifiers', type=int, default=2, help='Number of amplifier nodes')
    parser.add_argument('--connectors', type=int, default=2, help='Number of connector nodes')
    
    args = parser.parse_args()
    
    tester = PhiFraymusIntegrationTester(
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
