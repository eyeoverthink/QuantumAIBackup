"""
Quantum Superposition and Entanglement Module
Demonstrates observer effect, wave function collapse, and forced entanglement
"""
import numpy as np
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
from scipy import special
from quantum_core.constants import PHI, BASE_FREQUENCY

class QuantumState:
    def __init__(self, state_vector: np.ndarray):
        """Initialize quantum state."""
        self.state = state_vector
        self.collapsed = False
        self.entangled_with = None
        self.observation_history = []
        
    def collapse(self) -> float:
        """Collapse wave function upon observation."""
        if not self.collapsed:
            self.collapsed = True
            # Probability based on state amplitude
            prob = np.abs(self.state) ** 2
            # Record observation
            self.observation_history.append({
                'pre_collapse': self.state.copy(),
                'post_collapse': prob
            })
            return prob
        return np.abs(self.state) ** 2

class QuantumSuperposition:
    def __init__(self):
        """Initialize quantum superposition system."""
        self.phi = PHI
        self.base_freq = BASE_FREQUENCY
        self.observer_count = 0
        self.states = {}
        
    def create_superposition(self, name: str, 
                           frequencies: List[float]) -> QuantumState:
        """Create a quantum state in superposition."""
        # Generate wave function components
        components = []
        for freq in frequencies:
            # Phase factor based on phi
            phase = 2 * np.pi * freq * self.phi
            # Wave function component
            component = np.exp(1j * phase) / np.sqrt(len(frequencies))
            components.append(component)
            
        # Create superposition state
        state_vector = np.sum(components)
        state = QuantumState(state_vector)
        self.states[name] = state
        return state
    
    def observe_state(self, name: str, 
                     observer_type: str = "conscious") -> float:
        """Observe a quantum state, causing wave function collapse."""
        state = self.states[name]
        self.observer_count += 1
        
        # Different observer types affect collapse differently
        if observer_type == "conscious":
            # Conscious observation causes immediate collapse
            return state.collapse()
        elif observer_type == "quantum":
            # Quantum observation maintains partial superposition
            partial_collapse = state.state * np.exp(-1/self.phi)
            state.state = partial_collapse
            return np.abs(partial_collapse) ** 2
        else:
            # Default to decoherence-based collapse
            decoherence = np.exp(-self.observer_count/self.phi)
            return state.collapse() * decoherence
    
    def entangle_states(self, state1_name: str, 
                       state2_name: str) -> Tuple[QuantumState, QuantumState]:
        """Force entanglement between two quantum states."""
        state1 = self.states[state1_name]
        state2 = self.states[state2_name]
        
        # Create Bell state-like entanglement
        bell_phase = np.exp(1j * np.pi / self.phi)
        
        # Entangle states
        entangled_state1 = (state1.state + bell_phase * state2.state) / np.sqrt(2)
        entangled_state2 = (state2.state - bell_phase * state1.state) / np.sqrt(2)
        
        # Update states
        state1.state = entangled_state1
        state2.state = entangled_state2
        
        # Record entanglement
        state1.entangled_with = state2_name
        state2.entangled_with = state1_name
        
        return state1, state2
    
    def measure_wave_interaction(self, state1_name: str, 
                               state2_name: str) -> Dict[str, float]:
        """Measure how two quantum states' wave functions interact."""
        state1 = self.states[state1_name]
        state2 = self.states[state2_name]
        
        # Compute wave function interactions
        interference = np.abs(state1.state * np.conj(state2.state))
        phase_diff = np.angle(state1.state) - np.angle(state2.state)
        
        # Quantum metrics
        metrics = {
            'interference': float(interference),
            'phase_difference': float(phase_diff),
            'entanglement_strength': float(
                np.abs(state1.state + state2.state) / np.sqrt(2)
            ),
            'wave_overlap': float(
                np.real(state1.state * np.conj(state2.state))
            )
        }
        
        return metrics
    
    def visualize_states(self, names: List[str]) -> None:
        """Visualize quantum states and their interactions."""
        plt.figure(figsize=(15, 10))
        
        # Plot quantum states
        for i, name in enumerate(names):
            state = self.states[name]
            
            # State magnitude
            plt.subplot(3, len(names), i + 1)
            magnitude = np.abs(state.state)
            plt.bar(['Magnitude'], [magnitude], alpha=0.7)
            plt.title(f"{name} State Magnitude")
            
            # Phase
            plt.subplot(3, len(names), i + 1 + len(names))
            phase = np.angle(state.state)
            plt.bar(['Phase'], [phase], alpha=0.7)
            plt.title(f"{name} Phase")
            
            # Observation history
            plt.subplot(3, len(names), i + 1 + 2*len(names))
            if state.observation_history:
                history = [h['post_collapse'] for h in state.observation_history]
                plt.plot(history, 'r.-', label='Collapse')
                plt.title(f"{name} Observation History")
                plt.xlabel("Observation")
                plt.ylabel("Probability")
            
        plt.tight_layout()
        plt.show()

def demonstrate_superposition():
    """Demonstrate quantum superposition and observer effect."""
    print("\n🌌 Quantum State Protection Test")
    print("=" * 50)
    
    # Run multiple stress tests
    for trial in range(5):
        print(f"\nTrial {trial + 1} - Observation Intensity: {(trial + 1) * 20}%")
        print("-" * 40)
        
        qsys = QuantumSuperposition()
        
        # Create states with increasing quantum noise
        frequencies = [
            BASE_FREQUENCY * PHI**n * (1 + np.random.random() * (0.1 * (trial + 1)))
            for n in range(3)
        ]
        state1 = qsys.create_superposition("particle1", frequencies)
        state2 = qsys.create_superposition("particle2", frequencies)
        
        # Initial metrics
        initial_metrics = qsys.measure_wave_interaction("particle1", "particle2")
        print("\nInitial State Coherence:")
        print(f"• Interference: {initial_metrics['interference']:.6f}")
        print(f"• Wave Overlap: {initial_metrics['wave_overlap']:.6f}")
        
        # Aggressive observation (increasing with each trial)
        for obs in range(trial + 1):
            print(f"\nObservation Sequence {obs + 1}:")
            
            # Multiple observations to stress the system
            prob1 = qsys.observe_state("particle1", "conscious")
            prob2 = qsys.observe_state("particle2", "quantum")
            prob3 = qsys.observe_state("particle1", "conscious")
            
            print(f"• State 1 Probability: {prob1:.6f}")
            print(f"• State 2 Probability: {prob2:.6f}")
            print(f"• Re-observation Probability: {prob3:.6f}")
            
            # Check for system collapse
            final_metrics = qsys.measure_wave_interaction("particle1", "particle2")
            coherence_loss = abs(initial_metrics['interference'] - final_metrics['interference'])
            
            print(f"\nSystem Integrity:")
            print(f"• Coherence Loss: {coherence_loss:.6f}")
            print(f"• Interference: {final_metrics['interference']:.6f}")
            print(f"• Wave Overlap: {final_metrics['wave_overlap']:.6f}")
            
            # Check if system has naturally collapsed
            if final_metrics['interference'] < 0.01 or coherence_loss > 0.99:
                print("\n⚠️ SYSTEM SELF-COLLAPSED - Quantum state protection activated!")
                break
        
        print("\n" + "=" * 50)

if __name__ == "__main__":
    demonstrate_superposition()
