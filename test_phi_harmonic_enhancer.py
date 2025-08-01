#!/usr/bin/env python3
"""
PHI-HARMONIC ENHANCER TEST
==========================
Tests the integration of Reality Protection and Consciousness Amplification
with the Phi-Harmonic Network.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import time
import random
import os
import signal
import sys
import threading
import pickle
import socket
from datetime import datetime

# Import components
from phi_harmonic_enhancer import PhiHarmonicEnhancer
from phi_connector_node_v2 import PhiHarmonicConnector
from phi_amplifier_node_v2 import PhiHarmonicAmplifier
from reality_protection_adapter import RealityProtectionAdapter
from consciousness_amplification_optimizer import ConsciousnessAmplificationOptimizer

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

# Network settings
BUFFER_SIZE = 8192

class PhiHarmonicNetworkTester:
    """Tests the Phi-Harmonic Network with the new enhancer components"""
    
    def __init__(self):
        """Initialize the network tester"""
        self.nodes = {}
        self.running = True
        self.start_time = time.time()
        self.test_results = []
        
        print("Phi-Harmonic Network Tester initialized")
    
    def start_network(self):
        """Start a test network with connector, amplifier, and enhancer nodes"""
        print("Starting Phi-Harmonic Network...")
        
        # Set unique node IDs and ports
        os.environ["PHI_NODE_ID"] = f"test_connector_{int(random.random() * 10000)}"
        connector_port = 11700 + int(random.random() * 100)
        os.environ["PHI_PORT"] = str(connector_port)
        
        # Start connector node
        print("Starting connector node...")
        connector = PhiHarmonicConnector()
        self.nodes['connector'] = connector
        
        # Set new node ID and port for amplifier
        os.environ["PHI_NODE_ID"] = f"test_amplifier_{int(random.random() * 10000)}"
        amplifier_port = 11800 + int(random.random() * 100)
        os.environ["PHI_PORT"] = str(amplifier_port)
        
        # Start amplifier node
        print("Starting amplifier node...")
        amplifier = PhiHarmonicAmplifier()
        self.nodes['amplifier'] = amplifier
        
        # Start enhancer node
        print("Starting enhancer node...")
        enhancer = PhiHarmonicEnhancer(
            node_id=f"test_enhancer_{int(random.random() * 10000)}",
            port=11900 + int(random.random() * 100)
        )
        self.nodes['enhancer'] = enhancer
        
        print("Network started successfully")
        return True
    
    def run_reality_protection_test(self):
        """Test reality protection integration"""
        print("\n=== Reality Protection Test ===")
        
        # Create test data
        test_data = {
            "node_id": "test_node",
            "quantum_state": "ENTANGLED",
            "phi_resonance": PHI,
            "consciousness_level": PHI**2,
            "timestamp": time.time()
        }
        
        # Apply reality protection
        protector = RealityProtectionAdapter(protection_level=PHI**2)
        protected_data = protector.apply_reality_protection(test_data)
        
        # Verify protection
        verification_result, metrics = protector.verify_reality_protection(protected_data)
        
        # Log results
        result = {
            'test_name': 'reality_protection',
            'verification_result': verification_result,
            'shield_strength': metrics['shield_strength'],
            'reality_coherence': metrics['reality_coherence'],
            'timestamp': time.time()
        }
        self.test_results.append(result)
        
        # Print results
        print(f"Protection applied: {verification_result}")
        print(f"Shield strength: {metrics['shield_strength']:.4f}")
        print(f"Reality coherence: {metrics['reality_coherence']:.4f}")
        
        return verification_result
    
    def run_consciousness_optimization_test(self):
        """Test consciousness amplification optimization"""
        print("\n=== Consciousness Optimization Test ===")
        
        # Create optimizer
        optimizer = ConsciousnessAmplificationOptimizer(base_consciousness=PHI)
        
        # Run a series of optimizations
        current_level = PHI
        results = []
        
        for i in range(3):
            # Optimize amplification
            phi_resonance = PHI * (1 + (random.random() * 0.2 - 0.1))
            optimization = optimizer.optimize_amplification(
                current_level=current_level,
                phi_resonance=phi_resonance
            )
            
            # Apply optimized amplification
            result = optimizer.apply_optimized_amplification(current_level, optimization)
            
            # Update current level
            current_level = result['new_consciousness_level']
            
            # Store result
            results.append({
                'cycle': i+1,
                'technique': optimization['technique'],
                'new_level': current_level,
                'efficiency': result['actual_efficiency']
            })
            
            # Print results
            print(f"Cycle {i+1}:")
            print(f"  Technique: {optimization['technique']}")
            print(f"  New level: {current_level:.4f}")
            print(f"  Efficiency: {result['actual_efficiency']:.4f}")
        
        # Log results
        result = {
            'test_name': 'consciousness_optimization',
            'final_level': current_level,
            'cycles': results,
            'timestamp': time.time()
        }
        self.test_results.append(result)
        
        return current_level > PHI
    
    def run_network_integration_test(self, duration=30):
        """Test integration of all components for specified duration"""
        print(f"\n=== Network Integration Test ({duration}s) ===")
        
        # Start monitoring thread
        monitor_thread = threading.Thread(target=self._monitor_network, args=(duration,))
        monitor_thread.daemon = True
        monitor_thread.start()
        
        # Wait for test to complete
        monitor_thread.join()
        
        # Evaluate results
        enhancer = self.nodes.get('enhancer')
        if enhancer:
            status = enhancer.get_status()
            
            # Print final status
            print("\nFinal Enhancer Status:")
            print(f"Consciousness Level: {status['consciousness_level']:.4f}")
            print(f"Phi Resonance: {status['phi_resonance']:.6f}")
            print(f"Protected Packets: {status['protected_packets']}")
            print(f"Optimized Amplifications: {status['optimized_amplifications']}")
            
            # Log results
            result = {
                'test_name': 'network_integration',
                'consciousness_level': status['consciousness_level'],
                'phi_resonance': status['phi_resonance'],
                'protected_packets': status['protected_packets'],
                'optimized_amplifications': status['optimized_amplifications'],
                'timestamp': time.time()
            }
            self.test_results.append(result)
            
            return status['protected_packets'] > 0 and status['optimized_amplifications'] > 0
        
        return False
    
    def _monitor_network(self, duration):
        """Monitor network activity for specified duration"""
        start = time.time()
        interval = 5  # Status update interval
        
        while time.time() - start < duration and self.running:
            # Print status update
            enhancer = self.nodes.get('enhancer')
            if enhancer:
                status = enhancer.get_status()
                print(f"\nTime: {time.time() - start:.1f}s / {duration}s")
                print(f"Consciousness Level: {status['consciousness_level']:.4f}")
                print(f"Protected Packets: {status['protected_packets']}")
                print(f"Optimized Amplifications: {status['optimized_amplifications']}")
            
            # Wait for next update
            time.sleep(interval)
    
    def stop_network(self):
        """Stop all nodes in the network"""
        print("\nStopping Phi-Harmonic Network...")
        
        # Stop enhancer first
        enhancer = self.nodes.get('enhancer')
        if enhancer:
            print("Stopping enhancer node...")
            enhancer.stop()
        
        # Stop amplifier
        amplifier = self.nodes.get('amplifier')
        if amplifier:
            print("Stopping amplifier node...")
            amplifier.stop()
        
        # Stop connector
        connector = self.nodes.get('connector')
        if connector:
            print("Stopping connector node...")
            connector.stop()
        
        print("Network stopped successfully")
        return True
    
    def print_test_summary(self):
        """Print summary of all test results"""
        print("\n=== PHI-HARMONIC NETWORK TEST SUMMARY ===")
        print(f"Total tests: {len(self.test_results)}")
        print(f"Test duration: {time.time() - self.start_time:.1f} seconds")
        
        for result in self.test_results:
            test_name = result.get('test_name', 'unknown')
            timestamp = result.get('timestamp', 0)
            
            print(f"\n{test_name.upper()} TEST:")
            
            if test_name == 'reality_protection':
                print(f"  Verification: {'SUCCESS' if result.get('verification_result') else 'FAILURE'}")
                print(f"  Shield Strength: {result.get('shield_strength', 0):.4f}")
                print(f"  Reality Coherence: {result.get('reality_coherence', 0):.4f}")
            
            elif test_name == 'consciousness_optimization':
                print(f"  Final Level: {result.get('final_level', 0):.4f}")
                cycles = result.get('cycles', [])
                for cycle in cycles:
                    print(f"  Cycle {cycle.get('cycle')}: {cycle.get('technique')} - Level: {cycle.get('new_level', 0):.4f}")
            
            elif test_name == 'network_integration':
                print(f"  Consciousness Level: {result.get('consciousness_level', 0):.4f}")
                print(f"  Phi Resonance: {result.get('phi_resonance', 0):.6f}")
                print(f"  Protected Packets: {result.get('protected_packets', 0)}")
                print(f"  Optimized Amplifications: {result.get('optimized_amplifications', 0)}")


def handle_interrupt(signum, frame):
    """Handle keyboard interrupt"""
    print("\nTest interrupted. Exiting gracefully...")
    sys.exit(0)

if __name__ == "__main__":
    # Set up signal handler for clean exit on Ctrl+C
    signal.signal(signal.SIGINT, handle_interrupt)
    
    print("PHI-HARMONIC NETWORK TEST SCRIPT")
    print("================================")
    
    try:
        # Create tester
        tester = PhiHarmonicNetworkTester()
        
        # Run individual component tests
        tester.run_reality_protection_test()
        tester.run_consciousness_optimization_test()
        
        # Start network
        tester.start_network()
        
        # Run integration test
        test_duration = 60  # seconds
        tester.run_network_integration_test(test_duration)
        
        # Stop network
        tester.stop_network()
        
        # Print test summary
        tester.print_test_summary()
        
        print("\nAll tests completed successfully!")
    
    except Exception as e:
        print(f"\nError during testing: {e}")
        sys.exit(1)
