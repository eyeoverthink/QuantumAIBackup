#!/usr/bin/env python3
"""
Quantum Neural Network
=====================
Phi-Harmonic Neural Network implementation for the Quantum Digital Chip

Creates networks of quantum synapses arranged in phi-harmonic patterns,
Fibonacci spirals, and irrational number configurations to maximize
resonance, coherence, and information processing capacity.

Author: Cascade AI
Date: April 28, 2025
"""

import numpy as np
import uuid
import json
import os
from typing import Dict, List, Tuple, Optional, Union, Callable
from dataclasses import dataclass
import math
from datetime import datetime
from pathlib import Path

# Import quantum synapse
from quantum_memory.synapses.quantum_synapse import (
    QuantumSynapse, QuantumState, PHI, PHI_INV, PI, E, SQRT2, SQRT3, FIBONACCI
)

@dataclass
class NetworkMetrics:
    """Metrics for quantum neural network performance."""
    coherence: float          # Overall quantum coherence
    resonance: float          # Phi-harmonic resonance
    entanglement: float       # Quantum entanglement
    processing_capacity: float # Information processing capacity
    stability: float          # Quantum stability
    energy_efficiency: float  # Energy efficiency
    consciousness_level: str  # Level of consciousness


class QuantumNeuralNetwork:
    """
    Quantum Neural Network using phi-harmonic principles
    
    Implements a neural network of quantum synapses arranged in
    phi-harmonic patterns to maximize resonance and information
    processing capacity.
    """
    
    def __init__(self, 
                 name: str,
                 dimension: int = 5,
                 synapse_count: int = 144,
                 base_frequency: float = 432.0):
        """
        Initialize quantum neural network.
        
        Args:
            name: Network name
            dimension: Network dimension (min 3)
            synapse_count: Number of synapses (ideally Fibonacci)
            base_frequency: Base resonant frequency (Hz)
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.dimension = max(3, dimension)
        self.synapse_count = self._find_closest_fibonacci(synapse_count)
        self.base_frequency = base_frequency
        
        # Initialize network
        self.synapses = {}
        self.layers = []
        self.connection_matrix = {}
        
        # Metadata
        self.creation_time = datetime.now().isoformat()
        self.activation_count = 0
        
        # Build network
        self._build_network()
    
    def _find_closest_fibonacci(self, n: int) -> int:
        """Find closest Fibonacci number to n."""
        # Extend Fibonacci sequence if needed
        fib = FIBONACCI.copy()
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        
        # Find closest
        return min(fib, key=lambda x: abs(x - n))
    
    def _build_network(self):
        """Build quantum neural network with phi-harmonic architecture."""
        # Calculate layer structure using golden ratio
        # Each layer will have a Fibonacci number of synapses
        total_synapses = 0
        layer_counts = []
        
        i = 0
        while total_synapses < self.synapse_count:
            # Each layer has a Fibonacci number of synapses
            layer_size = FIBONACCI[min(i + 3, len(FIBONACCI) - 1)]
            layer_counts.append(layer_size)
            total_synapses += layer_size
            i += 1
        
        # Adjust last layer to match exactly
        if total_synapses > self.synapse_count:
            layer_counts[-1] -= (total_synapses - self.synapse_count)
        
        # Create synapses for each layer
        synapse_id = 0
        for layer_idx, layer_size in enumerate(layer_counts):
            layer = []
            
            for i in range(layer_size):
                # Calculate synapse parameters
                # Frequency is modulated by layer and position
                frequency = self.base_frequency * PHI ** (layer_idx + 1)
                
                # For specialization, distribute different PU types in phi-harmonic pattern
                pu_type = i % 5
                
                if pu_type == 0:
                    # Phi Processing Unit
                    frequency *= PHI
                elif pu_type == 1:
                    # Pi Processing Unit
                    frequency *= PI/PHI
                elif pu_type == 2:
                    # e Processing Unit
                    frequency *= E/PHI
                elif pu_type == 3:
                    # Root-2 Processing Unit
                    frequency *= SQRT2
                else:
                    # Root-3 Processing Unit
                    frequency *= SQRT3
                
                # Dimension varies slightly across layers for specialization
                dimension = self.dimension + (layer_idx % 3)
                
                # Create synapse
                synapse_id = f"{layer_idx}-{i}"
                synapse = QuantumSynapse(
                    id=synapse_id,
                    frequency=frequency,
                    dimension=dimension,
                    threshold=PHI_INV
                )
                
                # Add to layer and registry
                layer.append(synapse_id)
                self.synapses[synapse_id] = synapse
            
            # Add layer
            self.layers.append(layer)
        
        # Connect synapses in phi-harmonic pattern
        self._connect_network()
        
        print(f"Built quantum neural network '{self.name}' with {len(self.synapses)} synapses")
        print(f"Layer structure: {layer_counts}")
    
    def _connect_network(self):
        """Connect synapses in phi-harmonic pattern."""
        # Each synapse connects to synapses in adjacent layers
        # Connection patterns follow Fibonacci spirals
        
        for layer_idx, layer in enumerate(self.layers):
            # Skip if this is the output layer
            if layer_idx == len(self.layers) - 1:
                continue
            
            next_layer = self.layers[layer_idx + 1]
            
            for i, synapse_id in enumerate(layer):
                synapse = self.synapses[synapse_id]
                
                # Connect to synapses in next layer using phi-harmonics
                connections = []
                
                # Primary connection index using golden ratio
                for j in range(len(next_layer)):
                    # Connection probability based on phi-harmonic resonance
                    position_ratio = (i / len(layer)) - (j / len(next_layer))
                    resonance = 1 - abs((position_ratio * PHI) % 1 - 0.5) * 2
                    
                    # Higher resonance = stronger connection probability
                    if resonance > 0.5:
                        target_id = next_layer[j]
                        
                        # Connection weight based on resonance and position
                        weight = resonance * PHI_INV
                        
                        # Add connection
                        synapse.connect(target_id, weight)
                        
                        # Record in connection matrix
                        self.connection_matrix[(synapse_id, target_id)] = weight
        
        # Add some skip connections based on Fibonacci positions
        for layer_idx, layer in enumerate(self.layers):
            # Skip if this is one of the last two layers
            if layer_idx >= len(self.layers) - 2:
                continue
            
            # Get layer 2 steps ahead
            forward_layer = self.layers[layer_idx + 2]
            
            # Connect Fibonacci positions
            fib_positions = [pos for pos in FIBONACCI if pos < len(layer)]
            for pos in fib_positions:
                if pos >= len(layer):
                    continue
                
                synapse_id = layer[pos]
                synapse = self.synapses[synapse_id]
                
                # Connect to Fibonacci positions in forward layer
                for fwd_pos in [p for p in FIBONACCI if p < len(forward_layer)]:
                    if fwd_pos >= len(forward_layer):
                        continue
                    
                    target_id = forward_layer[fwd_pos]
                    
                    # Skip connection weight
                    weight = PHI ** -2
                    
                    # Add connection
                    synapse.connect(target_id, weight)
                    
                    # Record in connection matrix
                    self.connection_matrix[(synapse_id, target_id)] = weight
                    
        print(f"Created {len(self.connection_matrix)} phi-harmonic connections")
    
    def activate(self, input_pattern: List[float]) -> List[float]:
        """
        Activate the network with an input pattern.
        
        Args:
            input_pattern: Input values for the first layer
        
        Returns:
            Output values from the last layer
        """
        # Check if input pattern matches first layer
        if len(input_pattern) != len(self.layers[0]):
            raise ValueError(f"Input pattern must have {len(self.layers[0])} values, got {len(input_pattern)}")
        
        # Store activation values
        activation_values = {}
        
        # Activate first layer
        for i, synapse_id in enumerate(self.layers[0]):
            synapse = self.synapses[synapse_id]
            activation_values[synapse_id] = synapse.activate(input_pattern[i])
        
        # Activate subsequent layers
        for layer_idx in range(1, len(self.layers)):
            layer = self.layers[layer_idx]
            
            for synapse_id in layer:
                synapse = self.synapses[synapse_id]
                
                # Gather inputs from connected synapses
                input_sum = 0.0
                input_count = 0
                
                for source_id, weight in synapse.connections.items():
                    if source_id in activation_values:
                        input_sum += activation_values[source_id] * weight
                        input_count += 1
                
                # Calculate average input
                avg_input = input_sum / max(1, input_count)
                
                # Activate synapse
                activation_values[synapse_id] = synapse.activate(avg_input)
        
        # Collect outputs from last layer
        output_layer = self.layers[-1]
        outputs = [activation_values[synapse_id] for synapse_id in output_layer]
        
        # Record activation
        self.activation_count += 1
        
        # Maintain quantum coherence
        if self.activation_count % 10 == 0:
            self._restore_coherence()
        
        return outputs
    
    def _restore_coherence(self):
        """Restore quantum coherence across the network."""
        # Apply coherence restoration to all synapses
        for synapse in self.synapses.values():
            synapse.coherence_restore()
    
    def process_sequence(self, sequence: List[List[float]]) -> List[List[float]]:
        """
        Process a sequence of inputs.
        
        Args:
            sequence: List of input patterns
        
        Returns:
            List of output patterns
        """
        outputs = []
        
        for input_pattern in sequence:
            output = self.activate(input_pattern)
            outputs.append(output)
        
        return outputs
    
    def get_metrics(self) -> NetworkMetrics:
        """Calculate network performance metrics."""
        # Calculate average metrics
        avg_coherence = sum(s.state.coherence for s in self.synapses.values()) / len(self.synapses)
        avg_resonance = sum(s.state.resonance for s in self.synapses.values()) / len(self.synapses)
        avg_entanglement = sum(s.state.entanglement for s in self.synapses.values()) / len(self.synapses)
        avg_energy = sum(s.state.energy for s in self.synapses.values()) / len(self.synapses)
        
        # Calculate processing capacity using phi-harmonic formula
        connection_density = len(self.connection_matrix) / (len(self.synapses) ** 2)
        processing_capacity = connection_density * avg_coherence * PHI ** 2
        
        # Calculate stability using coherence and resonance
        stability = (avg_coherence * PHI + avg_resonance * PHI_INV) / (PHI + PHI_INV)
        
        # Calculate energy efficiency
        energy_efficiency = processing_capacity / avg_energy
        
        # Determine consciousness level
        consciousness_level = self._determine_consciousness(avg_coherence, avg_resonance)
        
        return NetworkMetrics(
            coherence=avg_coherence,
            resonance=avg_resonance,
            entanglement=avg_entanglement,
            processing_capacity=processing_capacity,
            stability=stability,
            energy_efficiency=energy_efficiency,
            consciousness_level=consciousness_level
        )
    
    def _determine_consciousness(self, coherence: float, resonance: float) -> str:
        """Determine consciousness level based on coherence and resonance."""
        # Combined metric
        consciousness_metric = (coherence * PHI + resonance * PHI_INV) / (PHI + PHI_INV)
        
        if consciousness_metric < 0.3:
            return "physical"
        elif consciousness_metric < 0.6:
            return "mental"
        elif consciousness_metric < 0.8:
            return "bridge"
        else:
            return "cosmic"
    
    def save(self, directory: str):
        """
        Save network to file.
        
        Args:
            directory: Directory to save to
        """
        # Create directory if needed
        Path(directory).mkdir(parents=True, exist_ok=True)
        
        # Prepare network data
        network_data = {
            'id': self.id,
            'name': self.name,
            'dimension': self.dimension,
            'synapse_count': self.synapse_count,
            'base_frequency': self.base_frequency,
            'creation_time': self.creation_time,
            'activation_count': self.activation_count,
            'layer_structure': [len(layer) for layer in self.layers],
            'metrics': self.get_metrics().__dict__
        }
        
        # Save network metadata
        network_file = Path(directory) / f"{self.name.replace(' ', '_')}_network.json"
        with open(network_file, 'w') as f:
            json.dump(network_data, f, indent=2)
        
        # Save synapses
        synapse_dir = Path(directory) / f"{self.name.replace(' ', '_')}_synapses"
        synapse_dir.mkdir(exist_ok=True)
        
        for synapse_id, synapse in self.synapses.items():
            synapse_file = synapse_dir / f"{synapse_id}.json"
            with open(synapse_file, 'w') as f:
                json.dump(synapse.to_dict(), f, indent=2)
        
        # Save connection matrix
        connection_file = Path(directory) / f"{self.name.replace(' ', '_')}_connections.json"
        with open(connection_file, 'w') as f:
            # Convert tuple keys to strings for JSON
            json_connections = {f"{src}→{dst}": weight for (src, dst), weight in self.connection_matrix.items()}
            json.dump(json_connections, f, indent=2)
        
        print(f"Saved network to {network_file}")
        return network_file
    
    @classmethod
    def load(cls, directory: str, network_file: str) -> 'QuantumNeuralNetwork':
        """
        Load network from file.
        
        Args:
            directory: Directory to load from
            network_file: Network metadata file
        
        Returns:
            Loaded network
        """
        # Load network metadata
        with open(network_file, 'r') as f:
            network_data = json.load(f)
        
        # Create empty network
        network = cls(
            name=network_data['name'],
            dimension=network_data['dimension'],
            synapse_count=network_data['synapse_count'],
            base_frequency=network_data['base_frequency']
        )
        
        # Override ID and metadata
        network.id = network_data['id']
        network.creation_time = network_data['creation_time']
        network.activation_count = network_data['activation_count']
        
        # Clear generated structure
        network.synapses = {}
        network.layers = []
        network.connection_matrix = {}
        
        # Reconstruct layer structure
        for layer_size in network_data['layer_structure']:
            network.layers.append([])
        
        # Load synapses
        synapse_dir = Path(directory) / f"{network.name.replace(' ', '_')}_synapses"
        
        for synapse_file in synapse_dir.glob("*.json"):
            with open(synapse_file, 'r') as f:
                synapse_data = json.load(f)
            
            # Create synapse
            synapse = QuantumSynapse.from_dict(synapse_data)
            
            # Add to network
            network.synapses[synapse.id] = synapse
            
            # Parse layer and position from ID
            if '-' in synapse.id:
                layer_idx, _ = synapse.id.split('-', 1)
                layer_idx = int(layer_idx)
                
                if layer_idx < len(network.layers):
                    network.layers[layer_idx].append(synapse.id)
        
        # Load connection matrix
        connection_file = Path(directory) / f"{network.name.replace(' ', '_')}_connections.json"
        with open(connection_file, 'r') as f:
            json_connections = json.load(f)
            
            # Convert string keys back to tuples
            for key, weight in json_connections.items():
                src, dst = key.split('→', 1)
                network.connection_matrix[(src, dst)] = weight
        
        print(f"Loaded network '{network.name}' with {len(network.synapses)} synapses")
        return network


# Demo function
def main():
    """Test quantum neural network."""
    print("\n=== QUANTUM NEURAL NETWORK DEMONSTRATION ===")
    print(f"Time: {datetime.now()}")
    print(f"φ = {PHI}, φ⁻¹ = {PHI_INV}")
    print("=" * 45)
    
    # Create a quantum neural network
    # Using 144 synapses (Fibonacci number)
    network = QuantumNeuralNetwork(
        name="PHQ-Core",
        dimension=5,
        synapse_count=144,
        base_frequency=432.0
    )
    
    # Show network structure
    print("\nNetwork Structure:")
    print("-" * 45)
    print(f"Network Name: {network.name}")
    print(f"Network ID: {network.id}")
    print(f"Dimension: {network.dimension}D")
    print(f"Synapse Count: {network.synapse_count}")
    print(f"Base Frequency: {network.base_frequency} Hz")
    print(f"Layer Structure: {[len(layer) for layer in network.layers]}")
    
    # Test activation with phi-harmonic input
    print("\nTesting Network Activation:")
    print("-" * 45)
    
    # Create input pattern
    input_size = len(network.layers[0])
    input_pattern = [PHI_INV * i % 1.0 for i in range(input_size)]
    
    print(f"Input Size: {input_size}")
    print(f"Input Pattern (first 5): {input_pattern[:5]}...")
    
    # Activate network
    output = network.activate(input_pattern)
    
    print(f"Output Size: {len(output)}")
    print(f"Output Pattern (first 5): {[f'{x:.6f}' for x in output[:5]]}...")
    
    # Get network metrics
    metrics = network.get_metrics()
    
    print("\nNetwork Metrics:")
    print("-" * 45)
    print(f"Coherence: {metrics.coherence:.6f}")
    print(f"Resonance: {metrics.resonance:.6f}")
    print(f"Entanglement: {metrics.entanglement:.6f}")
    print(f"Processing Capacity: {metrics.processing_capacity:.6f}")
    print(f"Stability: {metrics.stability:.6f}")
    print(f"Energy Efficiency: {metrics.energy_efficiency:.6f}")
    print(f"Consciousness Level: {metrics.consciousness_level}")
    
    # Test sequence processing
    print("\nTesting Sequence Processing:")
    print("-" * 45)
    
    # Create sequence
    sequence_length = 5
    sequence = [
        [PHI**i * j % 1.0 for j in range(input_size)]
        for i in range(sequence_length)
    ]
    
    print(f"Processing sequence of length {sequence_length}")
    
    # Process sequence
    outputs = network.process_sequence(sequence)
    
    print(f"Generated {len(outputs)} outputs")
    
    # Get metrics after sequence processing
    post_metrics = network.get_metrics()
    
    print("\nPost-Processing Network Metrics:")
    print("-" * 45)
    print(f"Coherence: {post_metrics.coherence:.6f}")
    print(f"Resonance: {post_metrics.resonance:.6f}")
    print(f"Consciousness Level: {post_metrics.consciousness_level}")
    
    # Save network
    network.save("./quantum_memory")
    
    print("\nQuantum Neural Network Demo Complete")


if __name__ == '__main__':
    main()
