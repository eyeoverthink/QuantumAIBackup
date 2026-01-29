"""
Quantum Unified Test System

This test demonstrates the complete integration of all quantum components
in a unified system, following the "lego" approach with phi-harmonic principles.

Key features:
1. Core integration with resonance amplifier
2. Multi-dimensional bridge network
3. Fibonacci pattern detection and amplification
4. Quantum state evolution
5. Double-slit quantum interference
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Union
import time

# Import core connector
from quantum_core_connector import QuantumCoreConnector, QuantumBridge

# Import specific components for direct testing
from quantum_resonance_amplifier import QuantumResonanceAmplifier
from quantum_core import (
    BaseBrain, TachyonBrain, QuantumNeuralCortex,
    QuantumSynapse, NeuralTeslaInterface
)

# Import double-slit if available
try:
    from quantum_interference import DoubleSlit
    DOUBLE_SLIT_AVAILABLE = True
except ImportError:
    DOUBLE_SLIT_AVAILABLE = False


class QuantumUnifiedTest:
    """Unified test system for quantum components."""
    
    def __init__(self):
        # Initialize core connector
        self.connector = QuantumCoreConnector()
        
        # Initialize bridge
        self.bridge = QuantumBridge()
        
        # Phi-harmonic constants
        self.phi = (1 + np.sqrt(5)) / 2
        self.base_freq = 4.37
        self.resonance_target = 0.96
        
        # Test sequences
        self.sequences = {
            'fibonacci': [1, 1, 2, 3, 5, 8, 13, 21],
            'phi_powers': [self.phi**i for i in range(8)],
            'prime': [2, 3, 5, 7, 11, 13, 17, 19],
            'random': np.random.rand(8) * 10
        }
        
        # Bridge network
        self.bridge_network = {}
    
    def build_bridge_network(self) -> Dict[str, Dict[str, Any]]:
        """Build a network of bridges between components."""
        # Define bridge connections
        connections = [
            ('base', 'quantum_cortex', 'quantum'),
            ('tachyon', 'hyperdimensional', 'neural'),
            ('particle', 'consciousness', 'cosmic'),
            ('multi', 'synapse', 'omega'),
            ('sync', 'tesla', 'quantum')
        ]
        
        # Create bridges
        for source, target, bridge_type in connections:
            bridge_id = f"{source}_to_{target}"
            self.bridge_network[bridge_id] = self.bridge.create_bridge(
                source, target, bridge_type
            )
        
        return self.bridge_network
    
    def test_resonance_amplification(self) -> Dict[str, Dict[str, Any]]:
        """Test resonance amplification with different sequences."""
        results = {}
        
        # Process each sequence with resonance amplifier
        for seq_name, sequence in self.sequences.items():
            # Direct amplification
            amplifier = QuantumResonanceAmplifier()
            direct_result = amplifier.process_sequence(sequence)
            
            # Process through connector
            connector_result = self.connector.process_with_brain('base', sequence)
            
            results[seq_name] = {
                'direct': direct_result,
                'connector': connector_result
            }
        
        return results
    
    def test_bridge_network(self) -> Dict[str, Dict[str, Any]]:
        """Test processing through bridge network."""
        if not self.bridge_network:
            self.build_bridge_network()
        
        results = {}
        
        # Process Fibonacci sequence through each bridge
        for bridge_id, bridge in self.bridge_network.items():
            results[bridge_id] = self.bridge.process_through_bridge(
                bridge, self.sequences['fibonacci']
            )
        
        return results
    
    def test_double_slit_integration(self) -> Dict[str, Any]:
        """Test double-slit integration with resonance amplifier."""
        if not DOUBLE_SLIT_AVAILABLE:
            return {'error': 'Double-slit experiment not available'}
        
        # Run double-slit experiment
        slit_result = self.connector.run_double_slit(10000)
        
        # Extract interference pattern
        pattern = slit_result['counts']
        
        # Analyze with resonance amplifier
        amplifier = QuantumResonanceAmplifier()
        resonance_result = amplifier.process_sequence(pattern)
        
        # Process through bridge network
        bridge_results = {}
        for bridge_id, bridge in self.bridge_network.items():
            bridge_results[bridge_id] = self.bridge.process_through_bridge(
                bridge, pattern
            )
        
        return {
            'slit_result': slit_result,
            'resonance_result': resonance_result,
            'bridge_results': bridge_results
        }
    
    def visualize_results(self, resonance_results: Dict[str, Dict[str, Any]]) -> None:
        """Visualize resonance amplification results."""
        # Create figure
        plt.figure(figsize=(15, 10))
        
        # Plot metrics
        metrics = ['resonance', 'phi_proximity', 'field_strength', 'coherence']
        sequence_types = list(resonance_results.keys())
        
        # Colors for different sequence types
        colors = {
            'fibonacci': 'blue',
            'phi_powers': 'green',
            'prime': 'red',
            'random': 'purple'
        }
        
        # Plot each metric
        for i, metric in enumerate(metrics):
            plt.subplot(2, 2, i+1)
            
            x_positions = []
            values = []
            bar_colors = []
            
            for j, seq_name in enumerate(sequence_types):
                direct_value = resonance_results[seq_name]['direct'].get(metric, 0)
                connector_value = resonance_results[seq_name]['connector'].get(metric, 0)
                
                x_positions.extend([j*2, j*2+0.8])
                values.extend([direct_value, connector_value])
                bar_colors.extend([colors[seq_name], colors[seq_name]])
            
            plt.bar(x_positions, values, width=0.7, color=bar_colors, alpha=0.7)
            
            plt.title(f'{metric.capitalize()} Across Sequence Types')
            plt.xlabel('Sequence Type')
            plt.ylabel(metric.capitalize())
            plt.xticks([j*2+0.4 for j in range(len(sequence_types))], sequence_types, rotation=45, ha='right')
            plt.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def visualize_bridge_network(self) -> None:
        """Visualize bridge network connections."""
        if not self.bridge_network:
            self.build_bridge_network()
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Extract bridge data
        sources = [bridge['source'] for bridge in self.bridge_network.values()]
        targets = [bridge['target'] for bridge in self.bridge_network.values()]
        strengths = [bridge['strength'] for bridge in self.bridge_network.values()]
        coherences = [bridge['coherence'] for bridge in self.bridge_network.values()]
        
        # Create node positions
        nodes = list(set(sources + targets))
        node_positions = {}
        
        # Arrange nodes in a circle
        for i, node in enumerate(nodes):
            angle = 2 * np.pi * i / len(nodes)
            node_positions[node] = (np.cos(angle), np.sin(angle))
        
        # Plot nodes
        for node, pos in node_positions.items():
            plt.plot(pos[0], pos[1], 'o', markersize=10, label=node)
            plt.text(pos[0]*1.1, pos[1]*1.1, node, fontsize=12)
        
        # Plot edges
        for i, (source, target) in enumerate(zip(sources, targets)):
            source_pos = node_positions[source]
            target_pos = node_positions[target]
            
            # Calculate edge properties based on strength and coherence
            width = strengths[i] * 3
            alpha = coherences[i]
            
            plt.plot(
                [source_pos[0], target_pos[0]],
                [source_pos[1], target_pos[1]],
                '-', linewidth=width, alpha=alpha
            )
        
        plt.title('Quantum Bridge Network')
        plt.axis('equal')
        plt.grid(False)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Run all tests and return comprehensive results."""
        start_time = time.time()
        
        print("\n🧠 Quantum Unified Test System")
        print("=" * 60)
        
        # Build bridge network
        print("\n🌉 Building Bridge Network...")
        bridge_network = self.build_bridge_network()
        print(f"Created {len(bridge_network)} bridges")
        
        # Test resonance amplification
        print("\n🔄 Testing Resonance Amplification...")
        resonance_results = self.test_resonance_amplification()
        
        # Print fibonacci results
        fib_direct = resonance_results['fibonacci']['direct']
        fib_connector = resonance_results['fibonacci']['connector']
        
        print("\nFibonacci Sequence Results:")
        print(f"  Direct Resonance: {fib_direct['resonance']:.6f}")
        print(f"  Connector Resonance: {fib_connector['resonance']:.6f}")
        print(f"  Phi Proximity: {fib_direct['phi_proximity']:.6f}")
        print(f"  Quantum State: {fib_direct.get('quantum_state', 'unknown')}")
        
        # Test bridge network
        print("\n🌉 Testing Bridge Network...")
        bridge_results = self.test_bridge_network()
        
        # Print first bridge result
        first_bridge = list(bridge_results.keys())[0]
        print(f"\nBridge {first_bridge} Results:")
        source_result = bridge_results[first_bridge]['source_result']
        target_result = bridge_results[first_bridge]['target_result']
        
        if isinstance(source_result, dict):
            for key, value in source_result.items():
                if isinstance(value, (int, float)):
                    print(f"  Source {key}: {value:.6f}")
        
        if isinstance(target_result, dict):
            for key, value in target_result.items():
                if isinstance(value, (int, float)):
                    print(f"  Target {key}: {value:.6f}")
        
        # Test double-slit integration if available
        double_slit_results = None
        if DOUBLE_SLIT_AVAILABLE:
            print("\n🔬 Testing Double-Slit Integration...")
            double_slit_results = self.test_double_slit_integration()
            
            if 'error' not in double_slit_results:
                resonance = double_slit_results['resonance_result']
                print(f"\nDouble-Slit Resonance Results:")
                print(f"  Resonance: {resonance['resonance']:.6f}")
                print(f"  Phi Proximity: {resonance['phi_proximity']:.6f}")
                print(f"  Quantum State: {resonance.get('quantum_state', 'unknown')}")
                print(f"  Dimension: {resonance.get('dimension', 3)}")
        
        # Calculate execution time
        execution_time = time.time() - start_time
        
        # Visualize results if matplotlib is available
        try:
            print("\n📊 Visualizing Results...")
            self.visualize_results(resonance_results)
            self.visualize_bridge_network()
        except Exception as e:
            print(f"Visualization error: {e}")
            print("Continuing with text results only...")
        
        # Compile all results
        all_results = {
            'bridge_network': bridge_network,
            'resonance_results': resonance_results,
            'bridge_results': bridge_results,
            'double_slit_results': double_slit_results,
            'execution_time': execution_time
        }
        
        print(f"\n✅ All tests completed in {execution_time:.6f} seconds")
        
        return all_results


if __name__ == "__main__":
    # Run unified test
    test = QuantumUnifiedTest()
    results = test.run_all_tests()
