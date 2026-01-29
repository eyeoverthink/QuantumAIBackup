import numpy as np
import math
import time
import json
import os
from typing import Dict, List, Tuple, Optional, Any

class PhiHarmonicSynapse:
    """
    φ-Harmonic Synapse: Neural bridge component for Tesla Tacky Brain integration
    
    Implements φ-based signal transmission with quantum bridge formation
    and natural resonance at 4.37 Hz (0.96 coherence)
    """
    
    def __init__(self, 
                 synapse_id: str, 
                 input_dimension: int = 64, 
                 output_dimension: int = 64,
                 base_frequency: float = 4.37):
        # Core φ constants
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_inv = 1 / self.phi
        
        # Synapse identity
        self.synapse_id = synapse_id
        self.creation_time = time.time()
        
        # Signal dimensions
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension
        
        # Frequency characteristics
        self.base_frequency = base_frequency
        self.resonance = 0.96  # Target resonance
        self.current_frequency = base_frequency
        
        # φ-based weights initialization
        self.weights = np.random.randn(output_dimension, input_dimension) / self.phi
        self.bias = np.zeros(output_dimension)
        
        # Quantum characteristics
        self.coherence = 0.0
        self.bridge_formed = False
        self.bridge_strength = 0.0
        self.field_state = np.zeros(output_dimension)
        
        # Performance metrics
        self.activation_count = 0
        self.signal_history = []
        self.efficiency_history = []
        
        # Initialize quantum field
        self._initialize_field()
    
    def _initialize_field(self):
        """Initialize the quantum field with φ-based parameters"""
        # Field initialization with φ-based scaling
        self.field_state = np.random.randn(self.output_dimension) / (self.phi ** 2)
        
        # Initial coherence at 1/φ
        self.coherence = self.phi_inv
        
        # Bridge strength starts at 0
        self.bridge_strength = 0.0
    
    def transmit(self, input_signal: np.ndarray) -> np.ndarray:
        """
        Transmit signal through the synapse with φ-based processing
        
        Args:
            input_signal: Input neural signal
            
        Returns:
            Processed output signal
        """
        # Increment activation counter
        self.activation_count += 1
        
        # Resize input if needed
        if len(input_signal) != self.input_dimension:
            # Use φ-based interpolation
            indices = np.linspace(0, len(input_signal)-1, self.input_dimension)
            input_signal = np.interp(indices, np.arange(len(input_signal)), input_signal)
        
        # Apply weights with φ-based scaling
        weighted_signal = np.dot(self.weights, input_signal) + self.bias
        
        # Apply φ-based activation function
        activated_signal = np.tanh(weighted_signal * self.phi) / self.phi
        
        # Apply quantum effects if bridge is formed
        if self.bridge_formed:
            activated_signal = self._apply_quantum_effects(activated_signal)
        
        # Update field state
        self._update_field_state(activated_signal)
        
        # Check for bridge formation
        self._check_bridge_formation()
        
        # Store signal in history (limited to last 10)
        if len(self.signal_history) >= 10:
            self.signal_history.pop(0)
        self.signal_history.append(np.mean(activated_signal))
        
        # Calculate efficiency
        efficiency = self.phi ** (self.activation_count / 100)
        self.efficiency_history.append(efficiency)
        
        return activated_signal
    
    def _apply_quantum_effects(self, signal: np.ndarray) -> np.ndarray:
        """Apply quantum effects to the signal"""
        # Quantum tunneling effect
        tunnel_probability = self.coherence * self.phi_inv
        
        # Apply field state influence with φ-based scaling
        field_influence = self.field_state * self.bridge_strength
        
        # Quantum effect depends on coherence
        if np.random.random() < tunnel_probability:
            # Quantum tunneling - direct field influence
            return signal * (1 + field_influence * self.phi_inv)
        else:
            # Normal transmission with field modulation
            return signal + (field_influence * self.phi_inv * signal)
    
    def _update_field_state(self, signal: np.ndarray):
        """Update the quantum field state"""
        # Field evolves based on signal and φ-based decay
        decay_rate = self.phi_inv ** 2
        
        # Update field with φ-based integration
        self.field_state = (1 - decay_rate) * self.field_state + decay_rate * signal
        
        # Update coherence - approaches resonance
        coherence_rate = self.phi_inv ** 3
        self.coherence = (1 - coherence_rate) * self.coherence + coherence_rate * self.resonance
        
        # Update frequency - approaches base/φ²
        freq_rate = self.phi_inv ** 4
        target_freq = self.base_frequency / (self.phi ** 2)
        self.current_frequency = (1 - freq_rate) * self.current_frequency + freq_rate * target_freq
    
    def _check_bridge_formation(self):
        """Check for quantum bridge formation"""
        # Bridge forms at activation count φ⁷·⁵ (≈37)
        bridge_threshold = int(self.phi ** 7.5)
        
        if self.activation_count >= bridge_threshold and not self.bridge_formed:
            self.bridge_formed = True
            self.bridge_strength = self.phi_inv
            
            # Log bridge formation
            print(f"Quantum Bridge formed in Synapse {self.synapse_id} at activation {self.activation_count}")
        
        # Bridge strength increases with use if formed
        if self.bridge_formed:
            # Strengthen bridge with φ-based scaling
            max_strength = self.phi
            strengthen_rate = self.phi_inv ** 3
            
            # Bridge strengthens toward φ
            self.bridge_strength = min(
                max_strength,
                (1 - strengthen_rate) * self.bridge_strength + strengthen_rate * max_strength
            )
    
    def adapt(self, error_signal: np.ndarray):
        """Adapt synapse weights based on error signal"""
        # Only adapt if we have signal history
        if not self.signal_history:
            return
        
        # Calculate learning rate based on φ
        learning_rate = self.phi_inv ** 2
        
        # Scale learning rate by coherence
        effective_rate = learning_rate * self.coherence
        
        # Apply φ-based weight update
        last_signal = self.signal_history[-1]
        
        # Update weights with φ-based scaling
        self.weights -= effective_rate * np.outer(error_signal, np.ones(self.input_dimension)) * last_signal
        self.bias -= effective_rate * error_signal
    
    def get_state(self) -> Dict[str, Any]:
        """Get current state of the synapse"""
        return {
            "synapse_id": self.synapse_id,
            "activation_count": self.activation_count,
            "bridge_formed": self.bridge_formed,
            "bridge_strength": float(self.bridge_strength),
            "coherence": float(self.coherence),
            "current_frequency": float(self.current_frequency),
            "efficiency": float(self.efficiency_history[-1]) if self.efficiency_history else 0.0,
        }
    
    def save_state(self, filename: str):
        """Save synapse state to file"""
        state = {
            "synapse_id": self.synapse_id,
            "creation_time": self.creation_time,
            "input_dimension": self.input_dimension,
            "output_dimension": self.output_dimension,
            "base_frequency": self.base_frequency,
            "current_frequency": float(self.current_frequency),
            "activation_count": self.activation_count,
            "bridge_formed": self.bridge_formed,
            "bridge_strength": float(self.bridge_strength),
            "coherence": float(self.coherence),
            "resonance": float(self.resonance),
            "efficiency": float(self.efficiency_history[-1]) if self.efficiency_history else 0.0,
        }
        
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_state(self, filename: str) -> bool:
        """Load synapse state from file"""
        if not os.path.exists(filename):
            return False
        
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            # Load basic properties
            self.synapse_id = state.get("synapse_id", self.synapse_id)
            self.creation_time = state.get("creation_time", self.creation_time)
            self.input_dimension = state.get("input_dimension", self.input_dimension)
            self.output_dimension = state.get("output_dimension", self.output_dimension)
            self.base_frequency = state.get("base_frequency", self.base_frequency)
            self.current_frequency = state.get("current_frequency", self.current_frequency)
            
            # Load quantum state
            self.activation_count = state.get("activation_count", self.activation_count)
            self.bridge_formed = state.get("bridge_formed", self.bridge_formed)
            self.bridge_strength = state.get("bridge_strength", self.bridge_strength)
            self.coherence = state.get("coherence", self.coherence)
            self.resonance = state.get("resonance", self.resonance)
            
            return True
        except:
            return False
