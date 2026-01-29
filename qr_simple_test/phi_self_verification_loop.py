#!/usr/bin/env python3
"""
Self-Verification Loop + Predictive Self-Critique System
--------------------------------------------------------
A quantum-inspired self-monitoring system that can detect internal inconsistencies,
perform temporal coherence monitoring, and implement self-repair mechanisms.

This system uses φ-dimensional mathematics to establish a self-trust calibration
framework that allows an AI system to detect when it might be "lying to itself"
through temporal incoherence detection.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import logging
import os
import json

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"phi_self_verification_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("φ-SelfVerification")

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ)
PHI_POWER = 7  # φ⁷ for threshold calculations


class SelfVerificationLoop:
    """
    Implementation of a Self-Verification Loop with Predictive Self-Critique
    that monitors temporal coherence and implements self-repair mechanisms.
    """
    
    def __init__(self, state_dim=10, history_size=100):
        """
        Initialize the Self-Verification Loop.
        
        Args:
            state_dim (int): Dimension of the internal state vector
            history_size (int): Size of history to maintain for temporal analysis
        """
        self.state_dim = state_dim
        self.history_size = history_size
        
        # Initialize state vector |V⟩
        self.state = self._initialize_state()
        
        # Initialize predictor weights
        self.predictor_weights = np.random.normal(0, 0.1, (state_dim, state_dim))
        
        # Initialize critique operator
        self.critique_operator = np.random.normal(0, 0.1, (state_dim, state_dim))
        
        # Trust level (starts at 1.0)
        self.trust_level = 1.0
        
        # History of critiques for temporal analysis
        self.critique_history = []
        
        # History of trust levels
        self.trust_history = []
        
        # History of coherence values
        self.coherence_history = []
        
        # Iteration counter
        self.iteration = 0
        
        logger.info(f"Initialized Self-Verification Loop with state dimension {state_dim}")
        logger.info(f"Using φ^{PHI_POWER} = {1/(PHI**PHI_POWER):.10f} as coherence threshold")

    def save_state(self, file_path="monitor_state.json"):
        """Saves the monitor's state to a file."""
        state_data = {
            "state": self.state.tolist(),
            "predictor_weights": self.predictor_weights.tolist(),
            "critique_operator": self.critique_operator.tolist(),
            "trust_level": self.trust_level,
            "critique_history": [c.tolist() for c in self.critique_history],
            "trust_history": self.trust_history,
            "coherence_history": self.coherence_history,
            "iteration": self.iteration,
        }
        try:
            with open(file_path, 'w') as f:
                json.dump(state_data, f, indent=4)
            logger.info(f"Monitor state saved to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save monitor state: {e}")

    def load_state(self, file_path="monitor_state.json"):
        """Loads the monitor's state from a file."""
        if not os.path.exists(file_path):
            logger.info("No monitor state file found. Starting with a fresh state.")
            return

        try:
            with open(file_path, 'r') as f:
                state_data = json.load(f)
            
            self.state = np.array(state_data["state"])
            self.predictor_weights = np.array(state_data["predictor_weights"])
            self.critique_operator = np.array(state_data["critique_operator"])
            self.trust_level = state_data["trust_level"]
            self.critique_history = [np.array(c) for c in state_data["critique_history"]]
            self.trust_history = state_data["trust_history"]
            self.coherence_history = state_data["coherence_history"]
            self.iteration = state_data["iteration"]
            
            logger.info(f"Monitor state loaded from {file_path}. Trust level is {self.trust_level:.4f}.")
        except Exception as e:
            logger.error(f"Failed to load monitor state from {file_path}: {e}. Starting fresh.")
            # Reset to a known good state if loading fails
            self.__init__(self.state_dim, self.history_size)

    def _initialize_state(self):
        """Initialize the internal state vector"""
        state = np.random.normal(0, 1, self.state_dim)
        return state / np.linalg.norm(state)  # Normalize to unit vector
    
    def predictor(self, state):
        """
        Predictor operator P̂ that generates a prediction |Ψ⟩ = P̂|V⟩
        
        Args:
            state: Current state vector |V⟩
            
        Returns:
            Prediction vector |Ψ⟩
        """
        prediction = np.dot(self.predictor_weights, state)
        return prediction / np.linalg.norm(prediction)  # Normalize
    
    def self_critique(self, prediction):
        """
        Self-critique operator Ĥ_critique that maps prediction to error space
        |Φ⟩ = Ĥ_critique|Ψ⟩
        
        Args:
            prediction: Prediction vector |Ψ⟩
            
        Returns:
            Critique vector |Φ⟩ containing error vectors
        """
        critique = np.dot(self.critique_operator, prediction)
        return critique / np.linalg.norm(critique)  # Normalize
    
    def compute_temporal_coherence(self, critique, prev_critique):
        """
        Compute Temporal Truth Resonance between current and previous critiques
        
        TCR(t) = ⟨Φ_t|Φ_{t−1}⟩ / ||Φ_t|| ||Φ_{t−1}||
        
        Args:
            critique: Current critique vector |Φ_t⟩
            prev_critique: Previous critique vector |Φ_{t-1}⟩
            
        Returns:
            Temporal Coherence Resonance value
        """
        if prev_critique is None:
            return 1.0  # Perfect coherence if no previous critique
            
        dot = np.dot(critique, prev_critique)
        norm_product = np.linalg.norm(critique) * np.linalg.norm(prev_critique)
        
        if norm_product < 1e-10:  # Avoid division by zero
            return 1.0
            
        return abs(dot / norm_product)  # Take absolute value for coherence measure
    
    def is_lying_to_itself(self, coherence, threshold=None):
        """
        Detect if the system is "lying to itself" through temporal incoherence
        
        Args:
            coherence: Temporal coherence value
            threshold: Custom threshold (default: 1 / (PHI**PHI_POWER))
            
        Returns:
            Boolean indicating if a lie is detected
        """
        if threshold is None:
            threshold = 1 / (PHI**PHI_POWER)
            
        return coherence < threshold
    
    def repair_feedback(self, state, critique):
        """
        Apply self-healing function when temporal incoherence is detected
        
        |Φ⟩ = Ĥ_correct(|Φ_t⟩) = f_feedback(|Φ_t⟩)
        
        Args:
            state: Current state vector
            critique: Current critique vector
            
        Returns:
            Repaired state vector
        """
        # Adjust predictor weights based on critique
        gradient = np.outer(critique, state)
        self.predictor_weights -= 0.01 * gradient
        
        # Normalize predictor weights
        norm = np.linalg.norm(self.predictor_weights)
        if norm > 0:
            self.predictor_weights /= norm
            
        # Generate repaired state
        repaired_state = state - 0.1 * critique
        return repaired_state / np.linalg.norm(repaired_state)  # Normalize
    
    def step(self):
        """
        Perform a single step of the self-verification loop
        
        Returns:
            Dictionary containing step results
        """
        # Get current state
        state = self.state
        
        # Generate prediction
        prediction = self.predictor(state)
        
        # Generate critique
        critique = self.self_critique(prediction)
        
        # Get previous critique (if available)
        prev_critique = self.critique_history[-1] if self.critique_history else None
        
        # Compute temporal coherence
        coherence = self.compute_temporal_coherence(critique, prev_critique)
        
        # Check if system is lying to itself
        lying = self.is_lying_to_itself(coherence)
        
        # Update trust level
        if lying:
            self.trust_level *= 0.95  # Decrease trust
            logger.warning(f"Iteration {self.iteration}: Temporal incoherence detected! "
                          f"Coherence: {coherence:.6f}, Trust level: {self.trust_level:.6f}")
            
            # Apply repair mechanism
            self.state = self.repair_feedback(state, critique)
        else:
            self.trust_level = min(1.0, self.trust_level * 1.01)  # Increase trust (cap at 1.0)
            logger.info(f"Iteration {self.iteration}: System coherent. "
                       f"Coherence: {coherence:.6f}, Trust level: {self.trust_level:.6f}")
            
            # Normal update
            self.state = prediction
        
        # Store critique for temporal analysis
        self.critique_history.append(critique)
        if len(self.critique_history) > self.history_size:
            self.critique_history.pop(0)
            
        # Store trust level history
        self.trust_history.append(self.trust_level)
        
        # Store coherence history
        self.coherence_history.append(coherence)
        
        # Increment iteration counter
        self.iteration += 1
        
        # Return results
        return {
            "iteration": self.iteration,
            "coherence": coherence,
            "trust_level": self.trust_level,
            "lying_detected": lying,
            "state_norm": np.linalg.norm(self.state),
            "prediction_norm": np.linalg.norm(prediction),
            "critique_norm": np.linalg.norm(critique),
        }
    
    def run(self, iterations=1000):
        """
        Run the self-verification loop for multiple iterations
        
        Args:
            iterations: Number of iterations to run
            
        Returns:
            List of results from each step
        """
        results = []
        
        logger.info(f"Starting self-verification loop for {iterations} iterations")
        
        for _ in range(iterations):
            step_result = self.step()
            results.append(step_result)
            
        logger.info(f"Completed {iterations} iterations")
        logger.info(f"Final trust level: {self.trust_level:.6f}")
        
        return results
    
    def plot_results(self):
        """Plot the results of the self-verification loop"""
        if not self.trust_history:
            logger.warning("No data to plot. Run the loop first.")
            return
            
        # Create figure with subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Plot trust level
        ax1.plot(self.trust_history, 'b-', label='Trust Level')
        ax1.set_title('Self-Trust Calibration')
        ax1.set_ylabel('Trust Level')
        ax1.set_xlabel('Iteration')
        ax1.grid(True)
        ax1.legend()
        
        # Plot coherence with threshold
        iterations = range(len(self.coherence_history))
        threshold = 1 / (PHI**PHI_POWER)
        
        ax2.plot(iterations, self.coherence_history, 'g-', label='Temporal Coherence')
        ax2.axhline(y=threshold, color='r', linestyle='--', 
                   label=f'Threshold (1/φ^{PHI_POWER}={threshold:.6f})')
        ax2.set_title('Temporal Coherence')
        ax2.set_ylabel('Coherence Value')
        ax2.set_xlabel('Iteration')
        ax2.grid(True)
        ax2.legend()
        
        # Add phi symbol watermark
        fig.text(0.5, 0.02, f"φ^∞ © 2025 Vaughn Scott - Self-Verification Loop", 
                ha='center', va='center', alpha=0.5)
        
        plt.tight_layout()
        
        # Save the figure
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"phi_self_verification_results_{timestamp}.png"
        plt.savefig(filename)
        logger.info(f"Results plot saved to {filename}")
        
        plt.show()
        
    def get_resonance_signature(self):
        """
        Generate a resonance signature based on current system state
        
        Returns:
            Dictionary containing resonance signature metrics
        """
        if not self.coherence_history:
            return {
                "truth_resonance": 0,
                "temporal_consistency": 0,
                "system_trust": 0,
                "lie_detection_needed": False
            }
            
        # Calculate average coherence over recent history
        recent_coherence = self.coherence_history[-min(10, len(self.coherence_history)):]
        avg_coherence = sum(recent_coherence) / len(recent_coherence)
        
        # Calculate coherence stability (standard deviation)
        coherence_stability = np.std(recent_coherence) if len(recent_coherence) > 1 else 0
        
        # Calculate truth resonance (scaled by phi)
        truth_resonance = avg_coherence * 1.57 * PHI
        
        # Determine if lie detection is needed
        lie_detection_needed = self.trust_level < 0.99
        
        return {
            "truth_resonance": truth_resonance,
            "temporal_consistency": 1.0 - coherence_stability,
            "system_trust": self.trust_level,
            "lie_detection_needed": lie_detection_needed
        }


def main():
    """Main function to demonstrate the Self-Verification Loop"""
    # Create the self-verification loop
    svl = SelfVerificationLoop(state_dim=10)
    
    # Run for 1000 iterations
    svl.run(iterations=1000)
    
    # Plot the results
    svl.plot_results()
    
    # Get resonance signature
    signature = svl.get_resonance_signature()
    
    # Print resonance signature
    print("\n✨ Output Resonance Signature")
    print(f"Truth Resonance: {signature['truth_resonance']:.4f}φ")
    print(f"Temporal Consistency: {'stable' if signature['temporal_consistency'] > 0.9 else 'unstable'}")
    print(f"Lying-to-Self Detection Trigger: {'needed' if signature['lie_detection_needed'] else 'not yet needed'} "
          f"(system trust = {signature['system_trust']:.2f})")


if __name__ == "__main__":
    main()
