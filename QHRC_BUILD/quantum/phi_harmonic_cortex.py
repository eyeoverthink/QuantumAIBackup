import numpy as np
import math
import time
import json
import os
from typing import Dict, List, Tuple, Optional, Any
from phi_harmonic_synapse import PhiHarmonicSynapse

class PhiHarmonicCortex:
    """
    φ-Harmonic Cortex: Neural processing center for Tesla Tacky Brain integration
    
    Implements φ-based neural architecture with quantum bridge formation,
    natural resonance at 4.37 Hz, and self-optimizing capabilities.
    """
    
    def __init__(self, 
                 cortex_id: str,
                 input_dimension: int = 128,
                 output_dimension: int = 128,
                 num_layers: int = 9,
                 base_frequency: float = 4.37):
        # Core φ constants
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_inv = 1 / self.phi
        
        # Cortex identity
        self.cortex_id = cortex_id
        self.creation_time = time.time()
        
        # Architecture parameters
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension
        self.num_layers = num_layers
        
        # Frequency characteristics
        self.base_frequency = base_frequency
        self.resonance = 0.96  # Target resonance
        
        # Synaptic layers
        self.synaptic_layers = []
        
        # Performance metrics
        self.processing_count = 0
        self.efficiency_history = []
        self.resonance_history = []
        
        # Memory system
        self.memory_patterns = {}
        self.field_state = np.zeros(output_dimension)
        
        # Initialize architecture
        self._initialize_architecture()
    
    def _initialize_architecture(self):
        """Initialize the cortex architecture with φ-based scaling"""
        # Create synaptic layers with φ-based scaling
        layer_sizes = []
        
        # Calculate layer sizes with φ-based scaling
        for i in range(self.num_layers + 1):  # +1 for input/output dimensions
            if i == 0:
                # Input layer
                layer_sizes.append(self.input_dimension)
            elif i == self.num_layers:
                # Output layer
                layer_sizes.append(self.output_dimension)
            else:
                # Hidden layers with φ-based scaling
                size = int(self.input_dimension / (self.phi ** (i-1)))
                # Ensure minimum size
                size = max(size, 16)
                layer_sizes.append(size)
        
        # Create synaptic layers
        for i in range(self.num_layers):
            # Each layer gets a unique frequency based on φ² division
            layer_freq = self.base_frequency / (self.phi ** (2*i))
            
            # Create synapse for this layer
            synapse = PhiHarmonicSynapse(
                synapse_id=f"{self.cortex_id}_synapse_{i}",
                input_dimension=layer_sizes[i],
                output_dimension=layer_sizes[i+1],
                base_frequency=layer_freq
            )
            
            self.synaptic_layers.append(synapse)
    
    def process(self, input_signal: np.ndarray) -> np.ndarray:
        """
        Process input signal through the cortex
        
        Args:
            input_signal: Input neural signal
            
        Returns:
            Processed output signal
        """
        # Increment processing counter
        self.processing_count += 1
        
        # Start timing
        start_time = time.time()
        
        # Resize input if needed
        if len(input_signal) != self.input_dimension:
            # Use φ-based interpolation
            indices = np.linspace(0, len(input_signal)-1, self.input_dimension)
            input_signal = np.interp(indices, np.arange(len(input_signal)), input_signal)
        
        # Process through synaptic layers
        current_signal = input_signal
        layer_outputs = []
        
        for i, synapse in enumerate(self.synaptic_layers):
            # Process through synapse
            layer_output = synapse.transmit(current_signal)
            layer_outputs.append(layer_output)
            
            # Update for next layer
            current_signal = layer_output
            
            # Apply quantum effects at higher layers (7+)
            if i >= 7:
                current_signal = self._apply_quantum_effects(current_signal, i)
        
        # Update field state
        self._update_field_state(current_signal)
        
        # Calculate efficiency
        processing_time = time.time() - start_time
        efficiency = len(input_signal) / (processing_time * self.phi)
        self.efficiency_history.append(efficiency)
        
        # Calculate overall resonance
        overall_resonance = np.mean([s.coherence for s in self.synaptic_layers])
        self.resonance_history.append(overall_resonance)
        
        # Self-optimize
        if self.processing_count % 10 == 0:
            self._optimize_system()
        
        return current_signal
    
    def _apply_quantum_effects(self, signal: np.ndarray, layer_idx: int) -> np.ndarray:
        """Apply quantum effects to the signal at higher layers"""
        # Different effects based on layer
        if layer_idx == 7:  # Bridge formation
            # Apply field-based modulation
            field_factor = self.phi_inv * np.mean(self.field_state)
            return signal * (1 + field_factor)
            
        elif layer_idx == 8:  # Q-state
            # Apply quantum state transformation
            q_factor = self.phi * np.mean(self.field_state)
            return signal + (signal * q_factor * self.phi_inv)
            
        elif layer_idx >= 9:  # Tunneling
            # Apply tunneling with φ-based probability
            tunnel_prob = self.resonance * self.phi_inv
            if np.random.random() < tunnel_prob:
                # Direct field connection
                return self.field_state
            else:
                # Normal processing with field influence
                return signal + (self.field_state * self.phi_inv)
        
        return signal
    
    def _update_field_state(self, signal: np.ndarray):
        """Update the quantum field state"""
        # Field evolves based on signal and φ-based decay
        decay_rate = self.phi_inv ** 2
        
        # Update field with φ-based integration
        self.field_state = (1 - decay_rate) * self.field_state + decay_rate * signal
    
    def _optimize_system(self):
        """Self-optimize the cortex system"""
        # Only optimize periodically
        if self.processing_count < 10:
            return
            
        # Calculate overall efficiency
        if len(self.efficiency_history) > 0:
            current_efficiency = self.efficiency_history[-1]
            
            # Optimize synaptic layers
            for i, synapse in enumerate(self.synaptic_layers):
                # Calculate optimal frequency
                optimal_freq = self.base_frequency / (self.phi ** (2*i))
                
                # Adjust synapse parameters based on layer position
                if i < 7:  # Pre-bridge layers
                    # Standard optimization
                    synapse.current_frequency = (synapse.current_frequency * (1 - self.phi_inv) + 
                                               optimal_freq * self.phi_inv)
                    
                elif i == 7:  # Bridge layer
                    # Bridge optimization - focus on coherence
                    synapse.coherence = max(synapse.coherence, self.resonance * (1 - self.phi_inv ** i))
                    
                else:  # Post-bridge layers
                    # Quantum optimization - strengthen bridge
                    if synapse.bridge_formed:
                        synapse.bridge_strength = min(self.phi, synapse.bridge_strength * self.phi)
    
    def learn_pattern(self, input_signal: np.ndarray, expected_output: np.ndarray) -> float:
        """
        Learn a pattern with φ-based adaptation
        
        Args:
            input_signal: Input pattern
            expected_output: Expected output pattern
            
        Returns:
            Error value
        """
        # Process input
        actual_output = self.process(input_signal)
        
        # Calculate error using φ-harmonic comparison
        # Let the system naturally handle different shapes through resonance
        try:
            error = np.mean((expected_output - actual_output) ** 2)
        except ValueError:
            # If shapes don't match, use φ-based error calculation in frequency domain
            error = self.phi * (1 - np.mean(np.abs(np.fft.fft(actual_output)) * np.mean(np.abs(np.fft.fft(expected_output)))))
        
        # Store pattern in memory
        pattern_id = len(self.memory_patterns)
        self.memory_patterns[pattern_id] = {
            'input': input_signal,
            'expected': expected_output,
            'error': error,
            'timestamp': time.time()
        }
        
        # Adapt synaptic layers with φ-based learning
        for i, synapse in enumerate(self.synaptic_layers):
            # Calculate layer contribution to error
            layer_factor = self.phi ** (-i)
            
            # Create error signal for this layer
            layer_error = error * layer_factor
            
            # Adapt synapse
            synapse.adapt(layer_error * np.ones(synapse.output_dimension))
        
        return error
    
    def recall_pattern(self, input_signal: np.ndarray) -> Tuple[np.ndarray, float]:
        """
        Recall a pattern from memory with φ-based similarity
        
        Args:
            input_signal: Input pattern to recall
            
        Returns:
            Tuple of (recalled pattern, similarity score)
        """
        best_match = None
        best_similarity = 0
        
        for pattern_id, pattern in self.memory_patterns.items():
            # Calculate φ-based similarity
            stored_input = pattern['input']
            
            # Resize if needed
            if len(stored_input) != len(input_signal):
                indices = np.linspace(0, len(stored_input)-1, len(input_signal))
                stored_input = np.interp(indices, np.arange(len(stored_input)), stored_input)
            
            # Calculate similarity
            diff = np.sum((stored_input - input_signal) ** 2)
            similarity = 1 / (1 + diff)
            
            # Apply φ-based threshold
            if similarity > self.phi_inv and similarity > best_similarity:
                best_match = pattern
                best_similarity = similarity
        
        if best_match:
            return best_match['expected'], best_similarity
        
        # If no match, process normally
        return self.process(input_signal), 0
    
    def get_system_state(self) -> Dict[str, Any]:
        """Get current state of the cortex system"""
        # Get synapse states
        synapse_states = []
        for i, synapse in enumerate(self.synaptic_layers):
            synapse_states.append(synapse.get_state())
        
        return {
            "cortex_id": self.cortex_id,
            "processing_count": self.processing_count,
            "num_layers": self.num_layers,
            "patterns_stored": len(self.memory_patterns),
            "efficiency": float(self.efficiency_history[-1]) if self.efficiency_history else 0,
            "resonance": float(self.resonance_history[-1]) if self.resonance_history else 0,
            "synapses": synapse_states
        }
    
    def save_state(self, directory: str):
        """Save cortex state to directory"""
        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Save cortex state
        cortex_state = {
            "cortex_id": self.cortex_id,
            "creation_time": self.creation_time,
            "input_dimension": self.input_dimension,
            "output_dimension": self.output_dimension,
            "num_layers": self.num_layers,
            "base_frequency": self.base_frequency,
            "resonance": self.resonance,
            "processing_count": self.processing_count,
            "efficiency_history": self.efficiency_history[-10:] if self.efficiency_history else [],
            "resonance_history": self.resonance_history[-10:] if self.resonance_history else [],
            "memory_count": len(self.memory_patterns)
        }
        
        with open(os.path.join(directory, f"{self.cortex_id}_state.json"), 'w') as f:
            json.dump(cortex_state, f, indent=2)
        
        # Save each synapse
        for i, synapse in enumerate(self.synaptic_layers):
            synapse.save_state(os.path.join(directory, f"{self.cortex_id}_synapse_{i}.json"))
    
    def load_state(self, directory: str) -> bool:
        """Load cortex state from directory"""
        cortex_file = os.path.join(directory, f"{self.cortex_id}_state.json")
        
        if not os.path.exists(cortex_file):
            return False
        
        try:
            # Load cortex state
            with open(cortex_file, 'r') as f:
                state = json.load(f)
            
            # Load basic properties
            self.cortex_id = state.get("cortex_id", self.cortex_id)
            self.creation_time = state.get("creation_time", self.creation_time)
            self.input_dimension = state.get("input_dimension", self.input_dimension)
            self.output_dimension = state.get("output_dimension", self.output_dimension)
            self.num_layers = state.get("num_layers", self.num_layers)
            self.base_frequency = state.get("base_frequency", self.base_frequency)
            self.resonance = state.get("resonance", self.resonance)
            self.processing_count = state.get("processing_count", self.processing_count)
            self.efficiency_history = state.get("efficiency_history", [])
            self.resonance_history = state.get("resonance_history", [])
            
            # Reinitialize architecture
            self._initialize_architecture()
            
            # Load each synapse
            for i, synapse in enumerate(self.synaptic_layers):
                synapse_file = os.path.join(directory, f"{self.cortex_id}_synapse_{i}.json")
                if os.path.exists(synapse_file):
                    synapse.load_state(synapse_file)
            
            return True
        except:
            return False
