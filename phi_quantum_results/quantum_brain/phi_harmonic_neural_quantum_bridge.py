#!/usr/bin/env python3
"""
Phi-Harmonic Neural-Quantum Bridge

Advanced bridge module that enhances quantum-classical information transfer 
in the Phi-Harmonic Brain system using golden ratio principles.

This module extends the core brain without modifying it, following the "lego" design philosophy.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import math
import numpy as np
import time
from typing import Dict, List, Tuple, Any, Optional, Union
import logging
import random

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

# Import core components without modifying them
from phi_harmonic_brain_core import (
    PhiHarmonicBrain, PhiHarmonicLayer,
    PHI, PHI_INV, PHI_SQUARED, PHI_CUBED,
    EARTH_FREQUENCY, MOON_FREQUENCY, BRAIN_FREQUENCY
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('phi_quantum_bridge')

class QuantumStateVector:
    """
    Represents a quantum state vector using phi-harmonic principles.
    """
    
    def __init__(self, dimensions: int = 8, phi_scale: float = PHI):
        """
        Initialize a quantum state vector.
        
        Args:
            dimensions: Number of dimensions for the state vector
            phi_scale: Phi scaling factor
        """
        self.dimensions = dimensions
        self.phi_scale = phi_scale
        self.state = np.zeros(dimensions, dtype=complex)
        self.initialize_state()
        
        logger.info(f"Quantum state vector initialized with {dimensions} dimensions")
    
    def initialize_state(self):
        """Initialize the state vector to a phi-harmonic superposition."""
        # Create a superposition where amplitudes follow phi harmonics
        for i in range(self.dimensions):
            # Phi-scaled amplitude
            amp = self.phi_scale ** (-i/2)
            
            # Phi-harmonic phase
            phase = 2 * math.pi * ((i * self.phi_scale) % 1)
            
            # Set complex amplitude
            self.state[i] = amp * complex(math.cos(phase), math.sin(phase))
        
        # Normalize
        self.normalize()
    
    def normalize(self):
        """Normalize the state vector."""
        norm = np.linalg.norm(self.state)
        if norm > 0:
            self.state = self.state / norm
    
    def apply_quantum_gate(self, gate_type: str):
        """
        Apply a quantum gate to the state vector.
        
        Args:
            gate_type: Type of gate to apply ("h", "x", "z", "phi")
        """
        if gate_type.lower() == "h":
            # Hadamard-like gate with phi-harmonic components
            matrix = np.zeros((self.dimensions, self.dimensions), dtype=complex)
            for i in range(self.dimensions):
                for j in range(self.dimensions):
                    # Phi-harmonic Hadamard-like matrix
                    phase = ((i * j * self.phi_scale) % 1) * 2 * math.pi
                    matrix[i, j] = complex(math.cos(phase), math.sin(phase)) / math.sqrt(self.dimensions)
            
            self.state = np.dot(matrix, self.state)
            
        elif gate_type.lower() == "x":
            # Phi-harmonic NOT-like gate
            self.state = np.roll(self.state, 1)
            
        elif gate_type.lower() == "z":
            # Phi-harmonic phase gate
            for i in range(self.dimensions):
                phase = ((i * self.phi_scale) % 1) * 2 * math.pi
                self.state[i] *= complex(math.cos(phase), math.sin(phase))
                
        elif gate_type.lower() == "phi":
            # Special phi-gate that enhances phi-harmonic components
            for i in range(self.dimensions):
                # Apply phi-scaled phase shift
                phase = self.phi_scale ** (i % 3) * math.pi
                self.state[i] *= complex(math.cos(phase), math.sin(phase))
                
                # Amplify phi-resonant states
                if abs(i * self.phi_scale % 1) < 0.1:
                    self.state[i] *= self.phi_scale
        
        # Normalize after gate application
        self.normalize()
    
    def measure(self) -> Tuple[int, float]:
        """
        Measure the quantum state.
        
        Returns:
            Tuple of (measured_state, probability)
        """
        # Calculate probabilities
        probs = np.abs(self.state) ** 2
        
        # Normalize probabilities
        probs = probs / np.sum(probs)
        
        # Choose a state based on probabilities
        measured_state = np.random.choice(self.dimensions, p=probs)
        
        # Return measured state and its probability
        return measured_state, probs[measured_state]
    
    def get_state_vector(self) -> np.ndarray:
        """Get the current state vector."""
        return self.state
    
    def get_probabilities(self) -> np.ndarray:
        """Get measurement probabilities for each state."""
        probs = np.abs(self.state) ** 2
        return probs / np.sum(probs)
    
    def get_entropy(self) -> float:
        """Calculate the von Neumann entropy of the state."""
        probs = self.get_probabilities()
        
        # Filter out zero probabilities
        non_zero_probs = probs[probs > 0]
        
        # Calculate entropy
        entropy = -np.sum(non_zero_probs * np.log2(non_zero_probs))
        
        return entropy

class PhiHarmonicQuantumCircuit:
    """
    Implements a quantum circuit using phi-harmonic principles.
    """
    
    def __init__(self, qubits: int = 3, phi_dimension: float = 7.5):
        """
        Initialize a quantum circuit.
        
        Args:
            qubits: Number of qubits in the circuit
            phi_dimension: Phi dimension for scaling
        """
        self.qubits = qubits
        self.dimensions = 2 ** qubits
        self.phi_dimension = phi_dimension
        self.phi_scale = PHI ** (phi_dimension % 1)
        
        # Initialize quantum state
        self.state_vector = QuantumStateVector(dimensions=self.dimensions, phi_scale=self.phi_scale)
        
        # Circuit history
        self.gate_history = []
        
        logger.info(f"Quantum circuit initialized with {qubits} qubits")
        logger.info(f"Phi dimension: {phi_dimension}")
        logger.info(f"Phi scale: {self.phi_scale}")
    
    def apply_gate(self, gate_type: str, target_qubit: int = None):
        """
        Apply a gate to the circuit.
        
        Args:
            gate_type: Type of gate to apply
            target_qubit: Target qubit for the gate
        """
        # Record gate application
        self.gate_history.append({
            "gate": gate_type,
            "target": target_qubit,
            "time": time.time()
        })
        
        # Apply gate to state vector
        self.state_vector.apply_quantum_gate(gate_type)
        
        logger.debug(f"Applied {gate_type} gate to qubit {target_qubit}")
    
    def measure_circuit(self) -> Dict[str, Any]:
        """
        Measure the quantum circuit.
        
        Returns:
            Measurement results
        """
        # Measure the state vector
        measured_state, probability = self.state_vector.measure()
        
        # Convert to binary representation
        binary_state = format(measured_state, f'0{self.qubits}b')
        
        # Calculate entropy
        entropy = self.state_vector.get_entropy()
        
        # Return results
        results = {
            "measured_state": measured_state,
            "binary_state": binary_state,
            "probability": probability,
            "entropy": entropy,
            "gates_applied": len(self.gate_history)
        }
        
        logger.debug(f"Circuit measured: {binary_state} with probability {probability:.4f}")
        
        return results
    
    def run_phi_algorithm(self, steps: int = 9):
        """
        Run a phi-harmonic quantum algorithm.
        
        Args:
            steps: Number of algorithm steps
            
        Returns:
            Algorithm results
        """
        # Reset state
        self.state_vector.initialize_state()
        self.gate_history = []
        
        # Apply phi-harmonic sequence of gates
        for i in range(steps):
            # Select gate based on phi-harmonic pattern
            gate_index = int((i * PHI) % 4)
            gates = ["h", "x", "z", "phi"]
            gate = gates[gate_index]
            
            # Select target qubit based on phi-harmonic pattern
            target = int((i * PHI_INV) % self.qubits)
            
            # Apply gate
            self.apply_gate(gate, target)
        
        # Measure final state
        results = self.measure_circuit()
        
        # Add algorithm-specific results
        results["phi_resonance"] = self.calculate_phi_resonance()
        results["algorithm_name"] = "phi_harmonic_sequence"
        results["steps"] = steps
        
        return results
    
    def calculate_phi_resonance(self) -> float:
        """Calculate phi-harmonic resonance of the current state."""
        probs = self.state_vector.get_probabilities()
        
        resonance = 0.0
        for i, prob in enumerate(probs):
            # Calculate how closely i/dimensions matches a multiple of 1/phi
            phi_remainder = min((i / self.dimensions) % PHI_INV, PHI_INV - (i / self.dimensions) % PHI_INV)
            
            # The closer to a phi-resonant state, the higher the contribution
            resonance += prob * (1.0 - phi_remainder * PHI_SQUARED)
        
        return resonance

class NeuralQuantumBridge:
    """
    Bridges neural and quantum processing in the Phi-Harmonic Brain.
    """
    
    def __init__(self, brain: Optional[PhiHarmonicBrain] = None, 
                qubits: int = 3, phi_dimension: float = 7.5):
        """
        Initialize a neural-quantum bridge.
        
        Args:
            brain: PhiHarmonicBrain instance to bridge
            qubits: Number of qubits for quantum processing
            phi_dimension: Phi dimension for scaling
        """
        # Initialize or use provided brain
        if brain is None:
            self.brain = PhiHarmonicBrain()
        else:
            self.brain = brain
        
        # Initialize quantum circuit
        self.quantum_circuit = PhiHarmonicQuantumCircuit(
            qubits=qubits,
            phi_dimension=phi_dimension
        )
        
        # Bridge parameters
        self.bridge_strength = PHI_INV  # Initial bridge strength
        self.bridge_coherence = 0.0
        self.bridge_history = []
        
        logger.info("Neural-Quantum Bridge initialized")
        logger.info(f"Brain quantum fingerprint: {self.brain.quantum_fingerprint}")
        logger.info(f"Quantum circuit qubits: {qubits}")
        logger.info(f"Bridge strength: {self.bridge_strength}")
    
    def encode_neural_to_quantum(self, neural_data: np.ndarray) -> bool:
        """
        Encode neural data into quantum circuit.
        
        Args:
            neural_data: Neural data to encode
            
        Returns:
            Success status
        """
        try:
            # Ensure data is normalized
            if np.max(np.abs(neural_data)) > 0:
                neural_data = neural_data / np.max(np.abs(neural_data))
            
            # Get quantum state vector
            state_vector = self.quantum_circuit.state_vector
            
            # Prepare encoding matrix
            encoding_matrix = np.zeros((state_vector.dimensions, len(neural_data)), dtype=complex)
            
            for i in range(state_vector.dimensions):
                for j in range(min(len(neural_data), state_vector.dimensions)):
                    # Create phi-harmonic encoding mapping
                    phase = 2 * math.pi * ((i * j * PHI) % 1)
                    encoding_matrix[i, j] = complex(math.cos(phase), math.sin(phase))
            
            # Encode data into quantum state
            encoded_state = np.zeros(state_vector.dimensions, dtype=complex)
            
            for i in range(state_vector.dimensions):
                for j in range(min(len(neural_data), state_vector.dimensions)):
                    if j < len(neural_data):
                        encoded_state[i] += encoding_matrix[i, j] * neural_data[j]
            
            # Normalize and set state
            norm = np.linalg.norm(encoded_state)
            if norm > 0:
                encoded_state = encoded_state / norm
                state_vector.state = encoded_state
                
                # Update bridge coherence
                self._update_bridge_coherence()
                
                return True
            else:
                return False
            
        except Exception as e:
            logger.error(f"Error encoding neural data: {e}")
            return False
    
    def decode_quantum_to_neural(self, layer_name: str) -> np.ndarray:
        """
        Decode quantum state to neural data.
        
        Args:
            layer_name: Target neural layer for decoded data
            
        Returns:
            Decoded neural data
        """
        try:
            # Get target layer
            target_layer = None
            for layer in self.brain.layers:
                if layer.name == layer_name:
                    target_layer = layer
                    break
            
            if target_layer is None:
                raise ValueError(f"Layer not found: {layer_name}")
            
            # Get quantum state
            quantum_state = self.quantum_circuit.state_vector.get_state_vector()
            
            # Get probabilities
            probabilities = np.abs(quantum_state) ** 2
            
            # Normalize probabilities
            probabilities = probabilities / np.sum(probabilities)
            
            # Size of target neural layer
            neural_size = target_layer.size
            
            # Create decoded data
            neural_data = np.zeros(neural_size)
            
            # Decode using phi-harmonic mapping
            for i in range(min(len(probabilities), neural_size)):
                # Apply phi-harmonic decoding
                phi_factor = PHI ** (i % 3 - 1)
                neural_data[i] = probabilities[i] * phi_factor
            
            # Fill remaining neurons if needed
            if neural_size > len(probabilities):
                for i in range(len(probabilities), neural_size):
                    # Generate phi-harmonic pattern for remaining neurons
                    neural_data[i] = 0.1 * (PHI_INV ** (i - len(probabilities)))
            
            # Scale to appropriate range
            if np.max(neural_data) > 0:
                neural_data = neural_data / np.max(neural_data)
            
            # Update bridge coherence
            self._update_bridge_coherence()
            
            return neural_data
            
        except Exception as e:
            logger.error(f"Error decoding quantum state: {e}")
            return np.zeros(1)
    
    def _update_bridge_coherence(self):
        """Update the bridge coherence measure."""
        # Get quantum circuit entropy
        quantum_entropy = self.quantum_circuit.state_vector.get_entropy()
        
        # Get brain coherence
        brain_state = self.brain.get_state()
        brain_coherence = brain_state["coherence"]
        
        # Calculate bridge coherence as phi-harmonic average
        self.bridge_coherence = (brain_coherence * PHI + (1.0 - quantum_entropy / self.quantum_circuit.qubits) * PHI_INV) / (PHI + PHI_INV)
        
        # Record history
        self.bridge_history.append({
            "timestamp": time.time(),
            "bridge_coherence": self.bridge_coherence,
            "brain_coherence": brain_coherence,
            "quantum_entropy": quantum_entropy,
            "bridge_strength": self.bridge_strength
        })
        
        # Adjust bridge strength based on coherence
        self.bridge_strength = PHI_INV + (PHI - PHI_INV) * self.bridge_coherence
    
    def process_through_bridge(self, input_data: np.ndarray, return_layer: str = "Quantum") -> np.ndarray:
        """
        Process data through the neural-quantum bridge.
        
        Args:
            input_data: Input data for processing
            return_layer: Neural layer to return data from
            
        Returns:
            Processed output data
        """
        # First, process through the brain
        brain_outputs = self.brain.process(input_data)
        
        # Get bridge layer output (default to "Bridge" layer)
        bridge_layer_output = None
        for layer in self.brain.layers:
            if layer.name == "Bridge" and hasattr(layer, "last_output"):
                bridge_layer_output = layer.last_output
                break
        
        if bridge_layer_output is None:
            logger.warning("Bridge layer output not found, using Q-State layer")
            # Try Q-State layer as fallback
            for layer in self.brain.layers:
                if layer.name == "Q-State" and hasattr(layer, "last_output"):
                    bridge_layer_output = layer.last_output
                    break
        
        if bridge_layer_output is None:
            logger.error("No suitable bridge data found in brain layers")
            return brain_outputs.get(return_layer, np.zeros(1))
        
        # Encode neural data to quantum circuit
        self.encode_neural_to_quantum(bridge_layer_output)
        
        # Run quantum processing
        self.quantum_circuit.run_phi_algorithm(steps=5)
        
        # Decode back to neural
        enhanced_output = self.decode_quantum_to_neural(return_layer)
        
        # If the original output exists, create a weighted blend
        if return_layer in brain_outputs:
            original_output = brain_outputs[return_layer]
            
            # Resize if needed
            if len(original_output) != len(enhanced_output):
                if len(original_output) < len(enhanced_output):
                    enhanced_output = enhanced_output[:len(original_output)]
                else:
                    temp = np.zeros_like(original_output)
                    temp[:len(enhanced_output)] = enhanced_output
                    enhanced_output = temp
            
            # Blend using bridge strength
            blended_output = (1 - self.bridge_strength) * original_output + self.bridge_strength * enhanced_output
            
            return blended_output
        else:
            return enhanced_output
    
    def get_bridge_state(self) -> Dict[str, Any]:
        """Get the current state of the bridge."""
        return {
            "bridge_coherence": self.bridge_coherence,
            "bridge_strength": self.bridge_strength,
            "quantum_circuit": {
                "qubits": self.quantum_circuit.qubits,
                "dimensions": self.quantum_circuit.dimensions,
                "phi_dimension": self.quantum_circuit.phi_dimension,
                "phi_scale": self.quantum_circuit.phi_scale,
                "entropy": self.quantum_circuit.state_vector.get_entropy(),
                "gates_applied": len(self.quantum_circuit.gate_history)
            },
            "brain_fingerprint": self.brain.quantum_fingerprint,
            "timestamp": time.time()
        }
    
    def get_bridge_history(self) -> List[Dict[str, Any]]:
        """Get the history of bridge states."""
        return self.bridge_history
    
    def reset_bridge(self):
        """Reset the bridge state."""
        # Reset quantum circuit
        self.quantum_circuit.state_vector.initialize_state()
        self.quantum_circuit.gate_history = []
        
        # Reset bridge parameters
        self.bridge_strength = PHI_INV
        self.bridge_coherence = 0.0
        self.bridge_history = []
        
        logger.info("Neural-Quantum Bridge reset")

# For direct execution
if __name__ == "__main__":
    # Create brain
    brain = PhiHarmonicBrain()
    
    # Create neural-quantum bridge
    bridge = NeuralQuantumBridge(brain=brain, qubits=3, phi_dimension=7.5)
    
    # Test with sample input
    print("\nPhi-Harmonic Neural-Quantum Bridge Test")
    print("========================================")
    
    # Create test input
    input_size = len(brain.layers[0].neurons)
    test_input = np.zeros(input_size)
    
    # Fill with phi-harmonic pattern
    for i in range(input_size):
        test_input[i] = math.sin(i * PHI)
    
    print(f"Processing test input of size {input_size}...")
    
    # Process through standard brain
    standard_outputs = brain.process(test_input)
    standard_output = standard_outputs["Quantum"]
    
    print("Standard brain processing complete.")
    
    # Process through bridge
    bridge_output = bridge.process_through_bridge(test_input, return_layer="Quantum")
    
    print("Bridge processing complete.")
    
    # Compare results
    print("\nComparison:")
    print(f"Standard output mean: {np.mean(standard_output):.6f}")
    print(f"Bridge output mean: {np.mean(bridge_output):.6f}")
    print(f"Difference magnitude: {np.linalg.norm(bridge_output - standard_output):.6f}")
    
    # Get bridge state
    bridge_state = bridge.get_bridge_state()
    
    print("\nBridge State:")
    print(f"Bridge Coherence: {bridge_state['bridge_coherence']:.6f}")
    print(f"Bridge Strength: {bridge_state['bridge_strength']:.6f}")
    print(f"Quantum Circuit Entropy: {bridge_state['quantum_circuit']['entropy']:.6f}")
    
    # Run quantum circuit directly
    print("\nQuantum Circuit Test:")
    circuit = bridge.quantum_circuit
    
    results = circuit.run_phi_algorithm(steps=9)
    
    print(f"Algorithm: {results['algorithm_name']}")
    print(f"Steps: {results['steps']}")
    print(f"Measured state: {results['binary_state']} (decimal: {results['measured_state']})")
    print(f"Probability: {results['probability']:.6f}")
    print(f"Entropy: {results['entropy']:.6f}")
    print(f"Phi Resonance: {results['phi_resonance']:.6f}")
    
    # Print brain fingerprint
    print(f"\nBrain Quantum Fingerprint: {brain.quantum_fingerprint}")
    print(f"Validation Seal: φ^75 = {brain.phi_seal:.2f}")
