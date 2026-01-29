import numpy as np
import math
import time
import json
import os
from typing import Dict, List, Tuple, Optional, Any
from phi_harmonic_synapse import PhiHarmonicSynapse
from phi_harmonic_cortex import PhiHarmonicCortex
from phi_harmonic_brain import PhiHarmonicBrain

class TeslaTackyIntegration:
    """
    Tesla Tacky Brain Integration with φ-Harmonic Neural System
    
    Integrates the φ-Harmonic Brain with Tesla Tacky architecture through
    synapse and cortex components, maintaining perfect φ-based resonance
    and quantum bridge formation.
    """
    
    def __init__(self):
        # Core φ constants
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_inv = 1 / self.phi
        
        # Base frequency (proven optimal)
        self.base_freq = 4.37
        self.resonance = 0.96
        
        # System components
        self.brain = PhiHarmonicBrain()
        self.cortices = {}
        self.synapses = {}
        
        # Integration parameters
        self.bridge_formed = False
        self.bridge_strength = 0.0
        self.field_coherence = 0.0
        
        # Performance metrics
        self.integration_cycles = 0
        self.efficiency_history = []
        
        # Initialize integration
        self._initialize_integration()
    
    def _initialize_integration(self):
        """Initialize the Tesla Tacky integration architecture"""
        # Create primary cortex (frontal)
        self.cortices["frontal"] = PhiHarmonicCortex(
            cortex_id="frontal",
            input_dimension=128,
            output_dimension=128,
            num_layers=9,
            base_frequency=self.base_freq
        )
        
        # Create secondary cortex (temporal)
        self.cortices["temporal"] = PhiHarmonicCortex(
            cortex_id="temporal",
            input_dimension=128,
            output_dimension=128,
            num_layers=9,
            base_frequency=self.base_freq / self.phi
        )
        
        # Create tertiary cortex (parietal)
        self.cortices["parietal"] = PhiHarmonicCortex(
            cortex_id="parietal",
            input_dimension=128,
            output_dimension=128,
            num_layers=9,
            base_frequency=self.base_freq / (self.phi ** 2)
        )
        
        # Create inter-cortical synapses
        self._create_inter_cortical_synapses()
    
    def _create_inter_cortical_synapses(self):
        """Create synapses between cortices"""
        # Frontal to Temporal (φ-based)
        self.synapses["frontal_temporal"] = PhiHarmonicSynapse(
            synapse_id="frontal_temporal",
            input_dimension=128,
            output_dimension=128,
            base_frequency=self.base_freq / self.phi
        )
        
        # Temporal to Parietal (φ²-based)
        self.synapses["temporal_parietal"] = PhiHarmonicSynapse(
            synapse_id="temporal_parietal",
            input_dimension=128,
            output_dimension=128,
            base_frequency=self.base_freq / (self.phi ** 2)
        )
        
        # Parietal to Frontal (φ³-based)
        self.synapses["parietal_frontal"] = PhiHarmonicSynapse(
            synapse_id="parietal_frontal",
            input_dimension=128,
            output_dimension=128,
            base_frequency=self.base_freq / (self.phi ** 3)
        )
    
    def process_input(self, input_data: np.ndarray) -> Dict[str, np.ndarray]:
        """
        Process input through the Tesla Tacky integration
        
        Args:
            input_data: Input data array
            
        Returns:
            Dictionary of cortex outputs
        """
        # Increment integration cycle counter
        self.integration_cycles += 1
        
        # Start timing
        start_time = time.time()
        
        # Process through primary cortex (frontal)
        frontal_output = self.cortices["frontal"].process(input_data)
        
        # Process through inter-cortical synapse to temporal
        temporal_input = self.synapses["frontal_temporal"].transmit(frontal_output)
        temporal_output = self.cortices["temporal"].process(temporal_input)
        
        # Process through inter-cortical synapse to parietal
        parietal_input = self.synapses["temporal_parietal"].transmit(temporal_output)
        parietal_output = self.cortices["parietal"].process(parietal_input)
        
        # Process through inter-cortical synapse back to frontal
        frontal_feedback = self.synapses["parietal_frontal"].transmit(parietal_output)
        
        # Apply φ-based integration to frontal cortex
        integrated_output = frontal_output * (1 - self.phi_inv) + frontal_feedback * self.phi_inv
        
        # Process through brain for higher-order integration
        brain_output = self.brain.process_input(integrated_output)
        
        # Check for bridge formation
        self._check_bridge_formation()
        
        # Apply quantum effects if bridge is formed
        if self.bridge_formed:
            brain_output = self._apply_quantum_effects(brain_output)
        
        # Calculate efficiency
        processing_time = time.time() - start_time
        efficiency = len(input_data) / (processing_time * self.phi)
        self.efficiency_history.append(efficiency)
        
        # Self-optimize
        if self.integration_cycles % 10 == 0:
            self._optimize_integration()
        
        # Return all outputs
        return {
            "frontal": frontal_output,
            "temporal": temporal_output,
            "parietal": parietal_output,
            "integrated": integrated_output,
            "brain": brain_output
        }
    
    def _check_bridge_formation(self):
        """Check for quantum bridge formation in the integration"""
        # Bridge forms at integration cycle φ⁷·⁵ (≈37)
        bridge_threshold = int(self.phi ** 7.5)
        
        if self.integration_cycles >= bridge_threshold and not self.bridge_formed:
            self.bridge_formed = True
            self.bridge_strength = self.phi_inv
            
            # Log bridge formation
            print(f"Tesla Tacky Quantum Bridge formed at cycle {self.integration_cycles}")
        
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
            
            # Field coherence increases with bridge strength
            self.field_coherence = self.bridge_strength * self.resonance
    
    def _apply_quantum_effects(self, signal: np.ndarray) -> np.ndarray:
        """Apply quantum effects to the signal"""
        # Get brain state
        brain_state = self.brain.get_system_state()
        
        # Quantum tunneling effect
        tunnel_probability = self.field_coherence * self.phi_inv
        
        # Apply quantum effects based on coherence
        if np.random.random() < tunnel_probability:
            # Full quantum tunneling - direct brain connection
            return signal * (1 + self.bridge_strength)
        else:
            # Partial quantum effect - φ-based modulation
            return signal + (signal * self.field_coherence * self.phi_inv)
    
    def _optimize_integration(self):
        """Self-optimize the integration"""
        # Only optimize periodically
        if self.integration_cycles < 10:
            return
            
        # Calculate overall efficiency
        if len(self.efficiency_history) > 0:
            current_efficiency = self.efficiency_history[-1]
            
            # Optimize cortices
            for cortex_id, cortex in self.cortices.items():
                # Get cortex state
                cortex_state = cortex.get_system_state()
                
                # Optimize based on position in the integration
                if cortex_id == "frontal":
                    # Primary cortex - focus on efficiency
                    pass  # Let cortex self-optimize
                elif cortex_id == "temporal":
                    # Secondary cortex - focus on resonance
                    cortex.resonance = max(cortex.resonance, self.resonance * (1 - self.phi_inv))
                else:
                    # Tertiary cortex - focus on coherence
                    pass  # Let cortex self-optimize
            
            # Optimize synapses
            for synapse_id, synapse in self.synapses.items():
                # Get synapse state
                synapse_state = synapse.get_state()
                
                # Optimize based on position in the integration
                if "frontal" in synapse_id:
                    # Primary synapse - focus on efficiency
                    pass  # Let synapse self-optimize
                elif "temporal" in synapse_id:
                    # Secondary synapse - focus on resonance
                    synapse.resonance = max(synapse.resonance, self.resonance * (1 - self.phi_inv))
                else:
                    # Tertiary synapse - focus on coherence
                    pass  # Let synapse self-optimize
    
    def learn_pattern(self, input_data: np.ndarray, expected_output: np.ndarray) -> float:
        """
        Learn a pattern with φ-based adaptation
        
        Args:
            input_data: Input pattern
            expected_output: Expected output pattern
            
        Returns:
            Error value
        """
        # Process input
        outputs = self.process_input(input_data)
        actual_output = outputs["brain"]
        
        # Calculate error using φ-harmonic comparison
        try:
            error = np.mean((expected_output - actual_output) ** 2)
        except ValueError:
            # If shapes don't match, use φ-based error calculation in frequency domain
            # Using absolute values to ensure positive errors
            actual_freq = np.abs(np.fft.fft(actual_output))
            expected_freq = np.abs(np.fft.fft(expected_output))
            
            # Interpolate to match lengths using φ-based resampling
            target_length = int(self.phi * max(len(actual_freq), len(expected_freq)))
            actual_freq = np.interp(
                np.linspace(0, len(actual_freq), target_length),
                np.arange(len(actual_freq)),
                actual_freq
            )
            expected_freq = np.interp(
                np.linspace(0, len(expected_freq), target_length),
                np.arange(len(expected_freq)),
                expected_freq
            )
            
            # Normalize frequencies by their energy
            actual_freq = actual_freq / np.sum(actual_freq)
            expected_freq = expected_freq / np.sum(expected_freq)
            
            # Calculate φ-weighted frequency domain error
            error = self.phi * (1 - np.sum(np.minimum(actual_freq, expected_freq)))
        
        # Learn pattern in brain
        self.brain.learn_pattern(input_data, expected_output)
        
        # Learn pattern in cortices
        for cortex_id, cortex in self.cortices.items():
            cortex.learn_pattern(input_data, expected_output)
        
        return error
    
    def recall_pattern(self, input_data: np.ndarray) -> Tuple[np.ndarray, float]:
        """
        Recall a pattern from memory with φ-based similarity
        
        Args:
            input_data: Input pattern to recall
            
        Returns:
            Tuple of (recalled pattern, similarity score)
        """
        # Try brain recall first
        brain_output, brain_similarity = self.brain.recall_pattern(input_data)
        
        # If good match found in brain, return it
        if brain_similarity > self.phi_inv:
            return brain_output, brain_similarity
        
        # Try cortex recall
        best_output = None
        best_similarity = 0
        
        for cortex_id, cortex in self.cortices.items():
            cortex_output, cortex_similarity = cortex.recall_pattern(input_data)
            
            if cortex_similarity > best_similarity:
                best_output = cortex_output
                best_similarity = cortex_similarity
        
        # If good match found in cortices, return it
        if best_similarity > self.phi_inv:
            return best_output, best_similarity
        
        # If no good match, process normally
        outputs = self.process_input(input_data)
        return outputs["brain"], 0
    
    def get_system_state(self) -> Dict[str, Any]:
        """Get current state of the integration system"""
        # Get brain state
        brain_state = self.brain.get_system_state()
        
        # Get cortex states
        cortex_states = {}
        for cortex_id, cortex in self.cortices.items():
            cortex_states[cortex_id] = cortex.get_system_state()
        
        # Get synapse states
        synapse_states = {}
        for synapse_id, synapse in self.synapses.items():
            synapse_states[synapse_id] = synapse.get_state()
        
        return {
            "integration_cycles": self.integration_cycles,
            "bridge_formed": self.bridge_formed,
            "bridge_strength": float(self.bridge_strength),
            "field_coherence": float(self.field_coherence),
            "efficiency": float(self.efficiency_history[-1]) if self.efficiency_history else 0,
            "brain": brain_state,
            "cortices": cortex_states,
            "synapses": synapse_states
        }
    
    def save_state(self, directory: str):
        """Save integration state to directory"""
        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Save integration state
        integration_state = {
            "integration_cycles": self.integration_cycles,
            "bridge_formed": self.bridge_formed,
            "bridge_strength": float(self.bridge_strength),
            "field_coherence": float(self.field_coherence),
            "efficiency_history": self.efficiency_history[-10:] if self.efficiency_history else []
        }
        
        with open(os.path.join(directory, "tesla_tacky_integration.json"), 'w') as f:
            json.dump(integration_state, f, indent=2)
        
        # Save brain state
        self.brain.save_state(os.path.join(directory, "brain_state.json"))
        
        # Save cortices
        cortex_dir = os.path.join(directory, "cortices")
        if not os.path.exists(cortex_dir):
            os.makedirs(cortex_dir)
            
        for cortex_id, cortex in self.cortices.items():
            cortex.save_state(cortex_dir)
        
        # Save synapses
        synapse_dir = os.path.join(directory, "synapses")
        if not os.path.exists(synapse_dir):
            os.makedirs(synapse_dir)
            
        for synapse_id, synapse in self.synapses.items():
            synapse.save_state(os.path.join(synapse_dir, f"{synapse_id}.json"))
    
    def load_state(self, directory: str) -> bool:
        """Load integration state from directory"""
        integration_file = os.path.join(directory, "tesla_tacky_integration.json")
        
        if not os.path.exists(integration_file):
            return False
        
        try:
            # Load integration state
            with open(integration_file, 'r') as f:
                state = json.load(f)
            
            # Load basic properties
            self.integration_cycles = state.get("integration_cycles", self.integration_cycles)
            self.bridge_formed = state.get("bridge_formed", self.bridge_formed)
            self.bridge_strength = state.get("bridge_strength", self.bridge_strength)
            self.field_coherence = state.get("field_coherence", self.field_coherence)
            self.efficiency_history = state.get("efficiency_history", [])
            
            # Load brain state
            brain_file = os.path.join(directory, "brain_state.json")
            if os.path.exists(brain_file):
                self.brain.load_state(brain_file)
            
            # Load cortices
            cortex_dir = os.path.join(directory, "cortices")
            if os.path.exists(cortex_dir):
                for cortex_id, cortex in self.cortices.items():
                    cortex.load_state(cortex_dir)
            
            # Load synapses
            synapse_dir = os.path.join(directory, "synapses")
            if os.path.exists(synapse_dir):
                for synapse_id, synapse in self.synapses.items():
                    synapse_file = os.path.join(synapse_dir, f"{synapse_id}.json")
                    if os.path.exists(synapse_file):
                        synapse.load_state(synapse_file)
            
            return True
        except:
            return False
