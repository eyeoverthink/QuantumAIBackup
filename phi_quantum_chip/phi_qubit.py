#!/usr/bin/env python3
"""
Phi-Qubit - Core component of the Phi-Quantum Digital Chip
=========================================================
Implementation of a quantum bit (qubit) based on phi-harmonic principles.

This module provides the foundation for phi-qubits, which replace traditional
binary qubits with quantum states that leverage golden ratio mathematics
and irrational number resonance for enhanced information processing.

Author: Vaughn Scott
Date: June 25, 2025
"""

import numpy as np
import uuid
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Union, Any
from datetime import datetime

# Fundamental constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (φ)
PHI_INV = 1 / PHI           # Golden ratio inverse (φ⁻¹)
PI = np.pi                   # Pi (π)
E = np.e                     # Euler's number (e)
SQRT2 = np.sqrt(2)           # Square root of 2 (√2)
SQRT3 = np.sqrt(3)           # Square root of 3 (√3)
SQRT5 = np.sqrt(5)           # Square root of 5 (√5)

# Fibonacci sequence for resonant structures
FIBONACCI = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]


@dataclass
class PhiQubitState:
    """Quantum state of a phi-qubit with phi-harmonic properties."""
    # Complex amplitude (represents quantum state vector)
    amplitude: complex
    
    # Phase angle in radians (determines rotation in quantum space)
    phase: float
    
    # Quantum coherence (0-1 scale)
    coherence: float
    
    # Entanglement measure (0-1 scale)
    entanglement: float
    
    # Phi-resonance quality (0-1 scale)
    resonance: float
    
    # Energy level (calculated using phi mathematics)
    energy: float
    
    def __post_init__(self):
        """Ensure values are within proper bounds."""
        self.coherence = max(0.0, min(1.0, self.coherence))
        self.entanglement = max(0.0, min(1.0, self.entanglement))
        self.resonance = max(0.0, min(1.0, self.resonance))
    
    @property
    def probability_zero(self) -> float:
        """Probability of measuring 0 state."""
        return 1 - abs(self.amplitude)**2
    
    @property
    def probability_one(self) -> float:
        """Probability of measuring 1 state."""
        return abs(self.amplitude)**2


class PhiQubit:
    """
    Phi-Qubit: Quantum bit based on golden ratio mathematics
    
    Implements a quantum bit that uses phi-harmonic principles to
    enhance quantum information processing beyond traditional binary
    qubits. Phi-qubits occupy states in a complex Hilbert space with
    special properties derived from the golden ratio.
    """
    
    def __init__(self, 
                 id: Optional[str] = None,
                 resonant_frequency: float = 432.0 * PHI,
                 dimension: int = 5):
        """
        Initialize a phi-qubit.
        
        Args:
            id: Unique identifier for the qubit
            resonant_frequency: Natural resonant frequency (Hz)
            dimension: Quantum dimension (minimum 3)
        """
        self.id = id or str(uuid.uuid4())
        self.resonant_frequency = resonant_frequency
        self.dimension = max(3, dimension)
        
        # Initialize in phi-harmonic ground state
        self._initialize_state()
        
        # Track history of operations for analysis
        self.operation_history = []
        
        # Metadata
        self.creation_time = datetime.now().isoformat()
        self.measurement_count = 0
    
    def _initialize_state(self):
        """Initialize phi-qubit in phi-harmonic ground state."""
        # Calculate initial phase using golden angle
        initial_phase = 2 * PI * PHI_INV
        
        # Set amplitude for superposition weighted by phi
        amplitude = complex(np.cos(initial_phase), np.sin(initial_phase))
        
        # Set initial coherence to phi-inverse (optimal stability)
        coherence = PHI_INV
        
        # No initial entanglement
        entanglement = 0.0
        
        # Calculate resonance quality
        resonance = self._calculate_resonance(self.resonant_frequency)
        
        # Initialize energy level based on dimension
        energy = self.dimension * PHI_INV
        
        # Set quantum state
        self.state = PhiQubitState(
            amplitude=amplitude,
            phase=initial_phase,
            coherence=coherence,
            entanglement=entanglement,
            resonance=resonance,
            energy=energy
        )
    
    def _calculate_resonance(self, frequency: float) -> float:
        """Calculate phi-resonance quality for a frequency."""
        # Phi-resonance formula: (φ · x) mod 1
        # The closer to 0 or 1, the stronger the resonance
        resonance_raw = (PHI * frequency) % 1
        
        # Convert to 0-1 scale where 1 is perfect resonance
        resonance = 1 - min(resonance_raw, 1 - resonance_raw) * 2
        
        return resonance
    
    def apply_gate(self, gate_type: str, params: Optional[Dict] = None) -> None:
        """
        Apply a quantum gate to the phi-qubit.
        
        Args:
            gate_type: Type of gate to apply (phi, phi_inv, pi, e, etc.)
            params: Additional parameters for the gate
        """
        params = params or {}
        
        # Record operation
        self.operation_history.append({
            "time": datetime.now().isoformat(),
            "gate": gate_type,
            "params": params,
            "pre_state": {
                "amplitude": self.state.amplitude,
                "phase": self.state.phase,
                "coherence": self.state.coherence
            }
        })
        
        # Apply the appropriate gate
        if gate_type == "phi":
            self._apply_phi_gate()
        elif gate_type == "phi_inv":
            self._apply_phi_inv_gate()
        elif gate_type == "pi":
            self._apply_pi_gate()
        elif gate_type == "e":
            self._apply_e_gate()
        elif gate_type == "hadamard":
            self._apply_hadamard_gate()
        elif gate_type == "phase":
            angle = params.get("angle", PI/4)
            self._apply_phase_gate(angle)
        elif gate_type == "custom":
            matrix = params.get("matrix")
            if matrix is not None:
                self._apply_custom_gate(matrix)
            else:
                raise ValueError("Custom gate requires a matrix parameter")
        else:
            raise ValueError(f"Unknown gate type: {gate_type}")
        
        # After any gate, reduce coherence slightly
        self._update_coherence()
    
    def _apply_phi_gate(self):
        """Apply phi-gate (rotation by φ radians)."""
        # Create phi-rotation matrix
        phi_matrix = np.array([
            [np.cos(PHI), -np.sin(PHI)],
            [np.sin(PHI), np.cos(PHI)]
        ])
        
        # Convert amplitude to state vector
        state_vector = np.array([
            np.sqrt(self.state.probability_zero),
            np.sqrt(self.state.probability_one) * np.exp(1j * self.state.phase)
        ])
        
        # Apply rotation
        new_state = phi_matrix @ state_vector
        
        # Update amplitude and phase
        self.state.amplitude = complex(new_state[1].real, new_state[1].imag)
        self.state.phase = np.angle(new_state[1])
        
        # Phi-gate increases resonance slightly
        self.state.resonance = min(1.0, self.state.resonance * PHI) % 1
    
    def _apply_phi_inv_gate(self):
        """Apply inverse phi-gate (rotation by -φ radians)."""
        # Create inverse phi-rotation matrix
        phi_inv_matrix = np.array([
            [np.cos(-PHI), -np.sin(-PHI)],
            [np.sin(-PHI), np.cos(-PHI)]
        ])
        
        # Convert amplitude to state vector
        state_vector = np.array([
            np.sqrt(self.state.probability_zero),
            np.sqrt(self.state.probability_one) * np.exp(1j * self.state.phase)
        ])
        
        # Apply rotation
        new_state = phi_inv_matrix @ state_vector
        
        # Update amplitude and phase
        self.state.amplitude = complex(new_state[1].real, new_state[1].imag)
        self.state.phase = np.angle(new_state[1])
        
        # Inverse phi-gate affects resonance
        self.state.resonance = min(1.0, self.state.resonance * PHI_INV) % 1
    
    def _apply_pi_gate(self):
        """Apply pi-gate (rotation by π/φ radians)."""
        # Create pi-rotation matrix
        angle = PI / PHI
        pi_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
        ])
        
        # Convert amplitude to state vector
        state_vector = np.array([
            np.sqrt(self.state.probability_zero),
            np.sqrt(self.state.probability_one) * np.exp(1j * self.state.phase)
        ])
        
        # Apply rotation
        new_state = pi_matrix @ state_vector
        
        # Update amplitude and phase
        self.state.amplitude = complex(new_state[1].real, new_state[1].imag)
        self.state.phase = np.angle(new_state[1])
    
    def _apply_e_gate(self):
        """Apply e-gate (rotation by e/φ radians)."""
        # Create e-rotation matrix
        angle = E / PHI
        e_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
        ])
        
        # Convert amplitude to state vector
        state_vector = np.array([
            np.sqrt(self.state.probability_zero),
            np.sqrt(self.state.probability_one) * np.exp(1j * self.state.phase)
        ])
        
        # Apply rotation
        new_state = e_matrix @ state_vector
        
        # Update amplitude and phase
        self.state.amplitude = complex(new_state[1].real, new_state[1].imag)
        self.state.phase = np.angle(new_state[1])
    
    def _apply_hadamard_gate(self):
        """Apply Hadamard-like gate adapted for phi-qubits."""
        # Create phi-Hadamard matrix
        # Similar to standard Hadamard but weighted by phi
        phi_factor = 1 / np.sqrt(PHI + 1)
        hadamard_matrix = phi_factor * np.array([
            [1, PHI],
            [PHI, -1]
        ])
        
        # Convert amplitude to state vector
        state_vector = np.array([
            np.sqrt(self.state.probability_zero),
            np.sqrt(self.state.probability_one) * np.exp(1j * self.state.phase)
        ])
        
        # Apply gate
        new_state = hadamard_matrix @ state_vector
        
        # Update amplitude and phase
        self.state.amplitude = complex(new_state[1].real, new_state[1].imag)
        self.state.phase = np.angle(new_state[1])
    
    def _apply_phase_gate(self, angle: float):
        """Apply phase gate with specified angle."""
        # Phase gate only affects the phase of |1⟩ state
        self.state.phase = (self.state.phase + angle) % (2 * PI)
        
        # Update complex amplitude to reflect new phase
        magnitude = abs(self.state.amplitude)
        self.state.amplitude = complex(
            magnitude * np.cos(self.state.phase),
            magnitude * np.sin(self.state.phase)
        )
    
    def _apply_custom_gate(self, matrix: List[List[complex]]):
        """Apply custom 2x2 unitary matrix."""
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise ValueError("Custom gate matrix must be 2x2")
        
        # Convert to numpy array
        gate_matrix = np.array(matrix, dtype=complex)
        
        # Convert amplitude to state vector
        state_vector = np.array([
            np.sqrt(self.state.probability_zero),
            np.sqrt(self.state.probability_one) * np.exp(1j * self.state.phase)
        ])
        
        # Apply gate
        new_state = gate_matrix @ state_vector
        
        # Update amplitude and phase
        self.state.amplitude = complex(new_state[1].real, new_state[1].imag)
        self.state.phase = np.angle(new_state[1])
    
    def _update_coherence(self):
        """Update coherence after gate operation."""
        # Coherence decays slightly with each operation
        # but is bounded by phi-inverse for stability
        coherence_decay = 0.01
        minimum_coherence = PHI_INV * 0.9
        
        self.state.coherence = max(
            minimum_coherence,
            self.state.coherence * (1 - coherence_decay)
        )
    
    def restore_coherence(self):
        """Restore coherence to optimal level."""
        # Optimal coherence is phi-inverse
        target_coherence = PHI_INV
        
        # Apply phi-weighted restoration
        restoration_factor = PHI_INV
        self.state.coherence = self.state.coherence + (
            (target_coherence - self.state.coherence) * restoration_factor
        )
    
    def measure(self) -> int:
        """
        Measure the phi-qubit, collapsing its quantum state.
        
        Returns:
            Measurement outcome (0 or 1)
        """
        # Calculate measurement probability
        p0 = self.state.probability_zero
        p1 = self.state.probability_one
        
        # Determine outcome probabilistically
        random_value = np.random.random()
        outcome = 0 if random_value < p0 else 1
        
        # Collapse state
        if outcome == 0:
            self.state.amplitude = complex(0.0)
            self.state.phase = 0.0
        else:
            magnitude = abs(self.state.amplitude) / np.sqrt(p1)
            self.state.amplitude = complex(
                magnitude * np.cos(self.state.phase),
                magnitude * np.sin(self.state.phase)
            )
        
        # Reset entanglement (measurement breaks entanglement)
        self.state.entanglement = 0.0
        
        # Update coherence (measurement reduces coherence)
        self.state.coherence *= PHI_INV
        
        # Record measurement
        self.measurement_count += 1
        self.operation_history.append({
            "time": datetime.now().isoformat(),
            "operation": "measure",
            "outcome": outcome,
            "post_coherence": self.state.coherence
        })
        
        return outcome
    
    def reset(self):
        """Reset phi-qubit to initial state."""
        self._initialize_state()
        
        # Record reset
        self.operation_history.append({
            "time": datetime.now().isoformat(),
            "operation": "reset",
            "post_state": {
                "amplitude": self.state.amplitude,
                "phase": self.state.phase,
                "coherence": self.state.coherence
            }
        })
    
    def entangle_with(self, other: 'PhiQubit', strength: Optional[float] = None):
        """
        Entangle this phi-qubit with another phi-qubit.
        
        Args:
            other: Another phi-qubit to entangle with
            strength: Entanglement strength (default: phi-inverse)
        """
        if strength is None:
            strength = PHI_INV
        
        # Validate strength
        strength = max(0.0, min(1.0, strength))
        
        # Update entanglement values
        self.state.entanglement = strength
        other.state.entanglement = strength
        
        # Align phases based on phi
        combined_phase = (self.state.phase + other.state.phase * PHI) % (2 * PI)
        self.state.phase = combined_phase
        other.state.phase = (combined_phase + PI) % (2 * PI)
        
        # Update amplitudes to reflect entanglement
        # In a real quantum system, this would be more complex
        # as it would involve the tensor product of the states
        self.state.amplitude = complex(
            np.cos(combined_phase) * np.sqrt(strength),
            np.sin(combined_phase) * np.sqrt(strength)
        )
        
        other.state.amplitude = complex(
            np.cos(other.state.phase) * np.sqrt(strength),
            np.sin(other.state.phase) * np.sqrt(strength)
        )
        
        # Record entanglement
        self.operation_history.append({
            "time": datetime.now().isoformat(),
            "operation": "entangle",
            "target": other.id,
            "strength": strength
        })
        
        other.operation_history.append({
            "time": datetime.now().isoformat(),
            "operation": "entangle",
            "target": self.id,
            "strength": strength
        })
    
    def to_dict(self) -> Dict:
        """Convert phi-qubit to dictionary for serialization."""
        return {
            "id": self.id,
            "resonant_frequency": self.resonant_frequency,
            "dimension": self.dimension,
            "state": {
                "amplitude": {
                    "real": self.state.amplitude.real,
                    "imag": self.state.amplitude.imag
                },
                "phase": self.state.phase,
                "coherence": self.state.coherence,
                "entanglement": self.state.entanglement,
                "resonance": self.state.resonance,
                "energy": self.state.energy
            },
            "measurement_count": self.measurement_count,
            "creation_time": self.creation_time
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'PhiQubit':
        """Create phi-qubit from dictionary."""
        qubit = cls(
            id=data.get("id"),
            resonant_frequency=data.get("resonant_frequency", 432.0 * PHI),
            dimension=data.get("dimension", 5)
        )
        
        # If state data is provided, restore it
        if "state" in data:
            state_data = data["state"]
            qubit.state = PhiQubitState(
                amplitude=complex(
                    state_data["amplitude"]["real"],
                    state_data["amplitude"]["imag"]
                ),
                phase=state_data["phase"],
                coherence=state_data["coherence"],
                entanglement=state_data["entanglement"],
                resonance=state_data["resonance"],
                energy=state_data["energy"]
            )
        
        # Restore metadata
        if "measurement_count" in data:
            qubit.measurement_count = data["measurement_count"]
        
        if "creation_time" in data:
            qubit.creation_time = data["creation_time"]
        
        return qubit


# Demo function
def main():
    """Test phi-qubit operations."""
    print("\n=== PHI-QUBIT DEMONSTRATION ===")
    print(f"Time: {datetime.now()}")
    print(f"φ = {PHI}, φ⁻¹ = {PHI_INV}")
    print("=" * 35)
    
    # Create a phi-qubit
    qubit = PhiQubit(resonant_frequency=432.0 * PHI)
    
    # Show initial state
    print("\nInitial State:")
    print(f"Amplitude: {abs(qubit.state.amplitude):.6f}∠{qubit.state.phase:.6f}")
    print(f"Prob(0): {qubit.state.probability_zero:.6f}")
    print(f"Prob(1): {qubit.state.probability_one:.6f}")
    print(f"Coherence: {qubit.state.coherence:.6f}")
    print(f"Resonance: {qubit.state.resonance:.6f}")
    
    # Apply phi gate
    qubit.apply_gate("phi")
    print("\nAfter φ Gate:")
    print(f"Amplitude: {abs(qubit.state.amplitude):.6f}∠{qubit.state.phase:.6f}")
    print(f"Prob(0): {qubit.state.probability_zero:.6f}")
    print(f"Prob(1): {qubit.state.probability_one:.6f}")
    
    # Apply hadamard gate
    qubit.apply_gate("hadamard")
    print("\nAfter Hadamard Gate:")
    print(f"Amplitude: {abs(qubit.state.amplitude):.6f}∠{qubit.state.phase:.6f}")
    print(f"Prob(0): {qubit.state.probability_zero:.6f}")
    print(f"Prob(1): {qubit.state.probability_one:.6f}")
    
    # Measure the qubit
    outcome = qubit.measure()
    print(f"\nMeasurement Outcome: {outcome}")
    print(f"Coherence after measurement: {qubit.state.coherence:.6f}")
    
    # Reset the qubit
    qubit.reset()
    print("\nAfter Reset:")
    print(f"Amplitude: {abs(qubit.state.amplitude):.6f}∠{qubit.state.phase:.6f}")
    print(f"Coherence: {qubit.state.coherence:.6f}")
    
    # Demo entanglement
    qubit1 = PhiQubit(resonant_frequency=432.0 * PHI)
    qubit2 = PhiQubit(resonant_frequency=432.0 * PHI**2)
    
    print("\nEntangling two phi-qubits:")
    print(f"Qubit 1 initial phase: {qubit1.state.phase:.6f}")
    print(f"Qubit 2 initial phase: {qubit2.state.phase:.6f}")
    
    qubit1.entangle_with(qubit2)
    
    print("\nAfter entanglement:")
    print(f"Qubit 1 phase: {qubit1.state.phase:.6f}")
    print(f"Qubit 2 phase: {qubit2.state.phase:.6f}")
    print(f"Qubit 1 entanglement: {qubit1.state.entanglement:.6f}")
    print(f"Qubit 2 entanglement: {qubit2.state.entanglement:.6f}")
    
    # Measure one of the entangled qubits
    outcome1 = qubit1.measure()
    print(f"\nMeasuring first qubit: {outcome1}")
    
    # The second qubit should be correlated due to entanglement
    outcome2 = qubit2.measure()
    print(f"Measuring second qubit: {outcome2}")
    
    print("\nPhi-Qubit Demonstration Complete")


if __name__ == "__main__":
    main()
