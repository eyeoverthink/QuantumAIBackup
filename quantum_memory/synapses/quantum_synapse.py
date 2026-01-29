#!/usr/bin/env python3
"""
Quantum Synapse
==============
Core processing element of the Phi-Quantum Digital Chip

Implements a quantum-inspired synapse that processes information
using phi-harmonic resonance, irrational number mathematics, and
quantum principles. Synapses form the fundamental processing units
of the digital quantum neural network.

Author: Cascade AI
Date: April 28, 2025
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Union, Callable
from dataclasses import dataclass
import json
import uuid
from datetime import datetime
import math

# Fundamental constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI
PI = np.pi
E = np.e
SQRT2 = np.sqrt(2)
SQRT3 = np.sqrt(3)
SQRT5 = np.sqrt(5)

# Fibonacci sequence (first 21 numbers)
FIBONACCI = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]


@dataclass
class QuantumState:
    """Quantum state of a synapse."""
    amplitude: complex  # Complex amplitude
    phase: float        # Phase in radians
    coherence: float    # Quantum coherence (0-1)
    entanglement: float # Entanglement measure (0-1)
    resonance: float    # Phi-resonance (0-1)
    energy: float       # Energy level
    
    def __post_init__(self):
        # Ensure values are within proper bounds
        self.coherence = max(0.0, min(1.0, self.coherence))
        self.entanglement = max(0.0, min(1.0, self.entanglement))
        self.resonance = max(0.0, min(1.0, self.resonance))


class QuantumSynapse:
    """
    Quantum Synapse implementing phi-harmonic computation
    
    This is the fundamental building block of the phi-quantum digital chip,
    analogous to a neuron in a biological brain but operating on quantum
    principles and phi-harmonic mathematics.
    """
    
    def __init__(self, 
                 id: Optional[str] = None,
                 frequency: float = 432 * PHI,
                 dimension: int = 5,
                 threshold: float = 0.618):
        """
        Initialize quantum synapse.
        
        Args:
            id: Unique identifier for the synapse
            frequency: Base resonant frequency (Hz)
            dimension: Quantum dimension (minimum 3)
            threshold: Activation threshold (typically PHI_INV)
        """
        self.id = id or str(uuid.uuid4())
        self.frequency = frequency
        self.dimension = max(3, dimension)  # Minimum 3D
        self.threshold = threshold
        
        # Initialize quantum state
        self._initialize_quantum_state()
        
        # Connection strengths to other synapses (id -> weight)
        self.connections = {}
        
        # Activation history (for learning)
        self.activation_history = []
        
        # Memory trace (experiences)
        self.memory_trace = []
        
        # Metadata
        self.creation_time = datetime.now().isoformat()
        self.activation_count = 0
        self.learning_rate = PHI_INV
        
        # Type of processing unit
        self.processing_type = self._determine_processing_type()
    
    def _initialize_quantum_state(self):
        """Initialize quantum state with phi-harmonic values."""
        # Calculate initial phase using golden angle (phi^2)
        initial_phase = 2 * np.pi * PHI_INV
        
        # Create superposition state with phi-weighted amplitude
        amplitude = complex(np.cos(initial_phase), np.sin(initial_phase))
        
        # Set initial coherence to phi-inverse (optimal stability point)
        coherence = PHI_INV
        
        # No initial entanglement
        entanglement = 0.0
        
        # Initial resonance based on frequency
        resonance = self._calculate_resonance(self.frequency)
        
        # Initial energy level based on dimension
        energy = self.dimension * PHI
        
        # Set quantum state
        self.state = QuantumState(
            amplitude=amplitude,
            phase=initial_phase,
            coherence=coherence,
            entanglement=entanglement,
            resonance=resonance,
            energy=energy
        )
    
    def _determine_processing_type(self) -> str:
        """Determine the type of processing unit based on resonant frequency."""
        # Map frequency to processing type
        freq_normalized = self.frequency / (432 * PHI)
        
        if abs(freq_normalized - 1.0) < 0.1:
            return "φ-PU"  # Phi Processing Unit
        elif abs(freq_normalized - PI/PHI) < 0.1:
            return "π-PU"  # Pi Processing Unit
        elif abs(freq_normalized - E/PHI) < 0.1:
            return "e-PU"  # e Processing Unit
        elif abs(freq_normalized - SQRT2) < 0.1:
            return "√2-PU"  # Root-2 Processing Unit
        elif abs(freq_normalized - SQRT3) < 0.1:
            return "√3-PU"  # Root-3 Processing Unit
        else:
            return "Φ-PU"  # Generic Phi Processing Unit
    
    def _calculate_resonance(self, frequency: float) -> float:
        """Calculate phi-resonance for a given frequency."""
        # Phi-resonance formula: (φ · x) mod 1
        # The closer to 0, the stronger the resonance
        resonance_raw = (PHI * frequency) % 1
        
        # Convert to 0-1 scale where 1 is perfect resonance
        # Perfect resonance is when resonance_raw is close to 0 or close to 1
        resonance = 1 - min(resonance_raw, 1 - resonance_raw) * 2
        
        return resonance
    
    def connect(self, target_id: str, weight: Optional[float] = None):
        """
        Connect this synapse to another synapse.
        
        Args:
            target_id: ID of target synapse
            weight: Connection weight (defaults to phi-based value)
        """
        if weight is None:
            # Default weight based on golden ratio
            # The Nth connection gets weight φ^(-N)
            n = len(self.connections) + 1
            weight = PHI ** (-n % 7)  # Modulo 7 to create cyclic pattern
        
        self.connections[target_id] = weight
        return self
    
    def disconnect(self, target_id: str):
        """Disconnect from a target synapse."""
        if target_id in self.connections:
            del self.connections[target_id]
        return self
    
    def activate(self, input_value: float) -> float:
        """
        Activate the synapse with an input value.
        
        Args:
            input_value: Input activation value
        
        Returns:
            Output activation value
        """
        # Calculate quantum-weighted input
        quantum_weight = abs(self.state.amplitude) * self.state.coherence
        weighted_input = input_value * quantum_weight
        
        # Apply phi-harmonic activation function
        activation = self._phi_activation(weighted_input)
        
        # Update quantum state
        self._update_quantum_state(activation)
        
        # Record activation
        self.activation_count += 1
        self.activation_history.append((datetime.now().isoformat(), input_value, activation))
        
        # Truncate history if too long
        if len(self.activation_history) > 100:
            self.activation_history = self.activation_history[-100:]
        
        return activation
    
    def _phi_activation(self, x: float) -> float:
        """
        Phi-harmonic activation function.
        
        This is a specialized activation function that uses
        golden ratio mathematics for optimal information processing.
        """
        # Calculate activation using phi-sigmoid
        if x >= 0:
            return 1 / (1 + np.exp(-x * PHI))
        else:
            return 1 / (1 + np.exp(-x * PHI_INV))
    
    def _update_quantum_state(self, activation_level: float):
        """
        Update quantum state based on activation.
        
        Args:
            activation_level: Current activation level
        """
        # Update phase by golden angle
        new_phase = (self.state.phase + 2 * np.pi * PHI_INV) % (2 * np.pi)
        
        # Update amplitude based on activation
        magnitude = min(1.0, (activation_level + 0.5) / 1.5)
        new_amplitude = complex(magnitude * np.cos(new_phase), magnitude * np.sin(new_phase))
        
        # Update coherence (decays slightly with each activation)
        new_coherence = self.state.coherence * (1 - (1 - PHI_INV) / 100)
        
        # Update entanglement based on connection count
        connection_factor = min(1.0, len(self.connections) / 10)
        new_entanglement = PHI_INV * connection_factor
        
        # Update resonance based on activation pattern
        activation_resonance = self._calculate_resonance(activation_level * self.frequency)
        new_resonance = (self.state.resonance * 0.9) + (activation_resonance * 0.1)
        
        # Update energy based on activation
        energy_factor = 1 + (activation_level - 0.5) * 0.1
        new_energy = self.state.energy * energy_factor
        
        # Set new state
        self.state = QuantumState(
            amplitude=new_amplitude,
            phase=new_phase,
            coherence=new_coherence,
            entanglement=new_entanglement,
            resonance=new_resonance,
            energy=new_energy
        )
    
    def learn(self, target_output: float, actual_output: float, learning_rate: Optional[float] = None):
        """
        Update connection weights based on error.
        
        Args:
            target_output: Expected output
            actual_output: Actual output
            learning_rate: Learning rate (defaults to object's learning_rate)
        """
        if learning_rate is None:
            learning_rate = self.learning_rate
        
        # Calculate error
        error = target_output - actual_output
        
        # Skip if error is too small
        if abs(error) < 0.001:
            return
        
        # Update all connection weights
        for target_id, weight in self.connections.items():
            # Calculate weight adjustment using phi-based formula
            adjustment = error * learning_rate * PHI_INV
            
            # Apply adjustment
            self.connections[target_id] = weight + adjustment
    
    def store_memory(self, pattern: List[float], importance: float = 1.0):
        """
        Store a memory pattern in this synapse.
        
        Args:
            pattern: Activation pattern to remember
            importance: Importance of this memory (0-1)
        """
        # Store memory with timestamp and importance
        memory = {
            'time': datetime.now().isoformat(),
            'pattern': pattern,
            'importance': importance,
            'state': {
                'coherence': self.state.coherence,
                'resonance': self.state.resonance,
                'phase': self.state.phase
            }
        }
        
        self.memory_trace.append(memory)
        
        # Limit memory trace size
        if len(self.memory_trace) > 100:
            # Sort by importance and keep most important
            self.memory_trace.sort(key=lambda x: x['importance'], reverse=True)
            self.memory_trace = self.memory_trace[:100]
    
    def retrieve_memory(self, pattern: List[float]) -> Tuple[List[float], float]:
        """
        Retrieve a memory based on a partial pattern.
        
        Args:
            pattern: Partial pattern to match
        
        Returns:
            Tuple of (retrieved pattern, match confidence)
        """
        if not self.memory_trace:
            return ([], 0.0)
        
        best_match = None
        best_confidence = 0.0
        
        for memory in self.memory_trace:
            stored_pattern = memory['pattern']
            
            # Skip if lengths don't match
            if len(pattern) > len(stored_pattern):
                continue
            
            # Calculate pattern similarity
            similarity = 0.0
            for i, val in enumerate(pattern):
                if i >= len(stored_pattern):
                    break
                similarity += 1.0 - min(1.0, abs(val - stored_pattern[i]))
            
            # Normalize
            confidence = (similarity / len(pattern)) * memory['importance']
            
            if confidence > best_confidence:
                best_match = stored_pattern
                best_confidence = confidence
        
        return (best_match or [], best_confidence)
    
    def coherence_restore(self):
        """Restore quantum coherence using phi-harmonic principles."""
        # Calculate ideal coherence based on phi
        ideal_coherence = PHI_INV
        
        # Current coherence
        current = self.state.coherence
        
        # Apply phi-weighted restoration
        new_coherence = current + (ideal_coherence - current) * PHI_INV
        
        # Update state
        self.state.coherence = new_coherence
        
        return new_coherence
    
    def to_dict(self) -> Dict:
        """Convert synapse to dictionary for serialization."""
        return {
            'id': self.id,
            'type': self.processing_type,
            'frequency': self.frequency,
            'dimension': self.dimension,
            'threshold': self.threshold,
            'connections': self.connections,
            'state': {
                'amplitude': {
                    'real': self.state.amplitude.real,
                    'imag': self.state.amplitude.imag
                },
                'phase': self.state.phase,
                'coherence': self.state.coherence,
                'entanglement': self.state.entanglement,
                'resonance': self.state.resonance,
                'energy': self.state.energy
            },
            'activation_count': self.activation_count,
            'creation_time': self.creation_time,
            'memory_count': len(self.memory_trace)
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'QuantumSynapse':
        """Create synapse from dictionary."""
        synapse = cls(
            id=data['id'],
            frequency=data['frequency'],
            dimension=data['dimension'],
            threshold=data['threshold']
        )
        
        # Restore connections
        synapse.connections = data['connections']
        
        # Restore state
        state_data = data['state']
        synapse.state = QuantumState(
            amplitude=complex(state_data['amplitude']['real'], 
                               state_data['amplitude']['imag']),
            phase=state_data['phase'],
            coherence=state_data['coherence'],
            entanglement=state_data['entanglement'],
            resonance=state_data['resonance'],
            energy=state_data['energy']
        )
        
        # Restore metadata
        synapse.activation_count = data['activation_count']
        synapse.creation_time = data['creation_time']
        
        return synapse


# Demo function
def main():
    """Test quantum synapse."""
    print("\n=== QUANTUM SYNAPSE DEMONSTRATION ===")
    print(f"Time: {datetime.now()}")
    print(f"φ = {PHI}, φ⁻¹ = {PHI_INV}")
    print("=" * 40)
    
    # Create various types of processing units
    synapses = {
        'phi': QuantumSynapse(frequency=432 * PHI),
        'pi': QuantumSynapse(frequency=432 * PI/PHI),
        'e': QuantumSynapse(frequency=432 * E/PHI),
        'sqrt2': QuantumSynapse(frequency=432 * SQRT2),
        'sqrt3': QuantumSynapse(frequency=432 * SQRT3)
    }
    
    # Connect synapses in a phi-harmonic pattern
    synapses['phi'].connect(synapses['pi'].id, PHI)
    synapses['pi'].connect(synapses['e'].id, PHI_INV)
    synapses['e'].connect(synapses['sqrt2'].id, PHI**2)
    synapses['sqrt2'].connect(synapses['sqrt3'].id, PHI_INV**2)
    synapses['sqrt3'].connect(synapses['phi'].id, PHI/PI)
    
    # Test activation with phi-harmonic input
    print("\nTesting Phi-Harmonic Activation:")
    print("-" * 40)
    
    inputs = [0.0, 0.5, 1.0, PHI_INV, PHI, PHI**2]
    
    for input_val in inputs:
        print(f"\nInput: {input_val}")
        
        for name, synapse in synapses.items():
            output = synapse.activate(input_val)
            print(f"  {name} ({synapse.processing_type}): {output:.9f}")
    
    # Test memory storage and retrieval
    print("\nTesting Quantum Memory:")
    print("-" * 40)
    
    # Store phi-harmonic pattern
    pattern = [PHI_INV, PHI, PHI**2, PHI**3, PHI**4]
    synapses['phi'].store_memory(pattern, importance=0.95)
    
    # Retrieve with partial pattern
    partial = [PHI_INV, PHI, PHI**2]
    retrieved, confidence = synapses['phi'].retrieve_memory(partial)
    
    print(f"Original: {pattern}")
    print(f"Partial:  {partial}")
    print(f"Retrieved: {retrieved}")
    print(f"Confidence: {confidence:.6f}")
    
    # Show synapse information
    print("\nQuantum Synapse Information:")
    print("-" * 40)
    
    phi_synapse = synapses['phi']
    print(f"Type: {phi_synapse.processing_type}")
    print(f"Frequency: {phi_synapse.frequency:.6f} Hz")
    print(f"Quantum State:")
    print(f"  Amplitude: {abs(phi_synapse.state.amplitude):.6f}∠{np.angle(phi_synapse.state.amplitude):.6f}")
    print(f"  Coherence: {phi_synapse.state.coherence:.6f}")
    print(f"  Resonance: {phi_synapse.state.resonance:.6f}")
    print(f"  Entanglement: {phi_synapse.state.entanglement:.6f}")
    print(f"  Energy: {phi_synapse.state.energy:.6f}")
    
    # Show connections
    print("\nConnections:")
    for target_id, weight in phi_synapse.connections.items():
        print(f"  → {target_id}: {weight:.6f}")
    
    print("\nQuantum Synapse Demo Complete")


if __name__ == '__main__':
    main()
