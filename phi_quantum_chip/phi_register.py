#!/usr/bin/env python3
"""
Phi-Register - Quantum Register for the Phi-Quantum Digital Chip
===============================================================
Implements a quantum register containing multiple phi-qubits arranged
in phi-harmonic patterns for enhanced quantum operations.

This module provides register-level operations for phi-qubits, enabling
complex quantum algorithms on the PHQ-Digital Chip architecture.

Author: Vaughn Scott
Date: June 25, 2025
"""

import numpy as np
import uuid
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Union, Any, Callable
from datetime import datetime
import json

# Import phi-qubit from our package
from phi_quantum_chip.phi_qubit import (
    PhiQubit, PhiQubitState, PHI, PHI_INV, PI, E, SQRT2, SQRT3, SQRT5, FIBONACCI
)


@dataclass
class RegisterMetrics:
    """Performance metrics for a quantum register."""
    # Overall quantum coherence (0-1)
    coherence: float
    
    # Phi-harmonic resonance quality (0-1)
    resonance: float
    
    # Average entanglement across all qubits (0-1)
    entanglement: float
    
    # Information processing capacity (derived metric)
    processing_capacity: float
    
    # Quantum stability (derived metric)
    stability: float
    
    # Energy efficiency (operations per energy unit)
    energy_efficiency: float
    
    # Highest consciousness level achieved
    consciousness_level: str


class PhiRegister:
    """
    Quantum register containing multiple phi-qubits
    
    Implements a quantum register with phi-qubits arranged in
    phi-harmonic patterns to maximize resonance and information
    processing capacity.
    """
    
    def __init__(self, 
                 name: str,
                 size: int = 8,
                 dimension: int = 5,
                 base_frequency: float = 432.0):
        """
        Initialize quantum register.
        
        Args:
            name: Register name
            size: Number of phi-qubits (ideally Fibonacci)
            dimension: Quantum dimension (min 3)
            base_frequency: Base resonant frequency (Hz)
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.size = self._find_closest_fibonacci(size)
        self.dimension = max(3, dimension)
        self.base_frequency = base_frequency
        
        # Initialize qubits
        self.qubits: Dict[str, PhiQubit] = {}
        self._initialize_qubits()
        
        # Track entanglement relationships between qubits
        # Format: {(qubit1_id, qubit2_id): entanglement_strength}
        self.entanglement_map: Dict[Tuple[str, str], float] = {}
        
        # Metadata
        self.creation_time = datetime.now().isoformat()
        self.operation_count = 0
        
        # Cache calculated metrics
        self._metrics = None
        self._metrics_timestamp = None
    
    def _find_closest_fibonacci(self, n: int) -> int:
        """Find closest Fibonacci number to n."""
        # Extend Fibonacci sequence if needed
        fib = FIBONACCI.copy()
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        
        # Find closest
        return min(fib, key=lambda x: abs(x - n))
    
    def _initialize_qubits(self):
        """Initialize phi-qubits with phi-harmonic frequencies."""
        for i in range(self.size):
            # Calculate phi-harmonic frequency for this qubit
            # Each qubit's frequency is phi-related to the base frequency
            frequency = self.base_frequency * (PHI ** ((i % 7) / 7))
            
            # Create qubit
            qubit_id = f"{self.name}-{i}"
            qubit = PhiQubit(
                id=qubit_id,
                resonant_frequency=frequency,
                dimension=self.dimension
            )
            
            # Add to register
            self.qubits[qubit_id] = qubit
    
    def apply_gate(self, gate_type: str, target_qubits: List[str], params: Optional[Dict] = None):
        """
        Apply a quantum gate to specific qubits in the register.
        
        Args:
            gate_type: Type of gate to apply
            target_qubits: List of qubit IDs to apply gate to
            params: Additional parameters for the gate
        """
        params = params or {}
        
        # Apply gate to each target qubit
        for qubit_id in target_qubits:
            if qubit_id in self.qubits:
                self.qubits[qubit_id].apply_gate(gate_type, params)
        
        # Record operation
        self.operation_count += len(target_qubits)
        
        # Invalidate cached metrics
        self._metrics = None
    
    def apply_register_gate(self, gate_type: str, params: Optional[Dict] = None):
        """
        Apply a gate to all qubits in the register.
        
        Args:
            gate_type: Type of gate to apply
            params: Additional parameters for the gate
        """
        self.apply_gate(gate_type, list(self.qubits.keys()), params)
    
    def apply_phi_pattern(self, gate_type: str, params: Optional[Dict] = None):
        """
        Apply gates in a phi-harmonic pattern across the register.
        
        This creates a phi-harmonic wave of operations that enhances
        resonance and information processing capacity.
        
        Args:
            gate_type: Type of gate to apply
            params: Additional parameters for the gate
        """
        qubit_ids = list(self.qubits.keys())
        
        # Apply gates in phi-harmonic sequence
        for i in range(self.size):
            # Calculate phi-harmonic index
            phi_index = int((i * PHI) % self.size)
            
            # Apply gate to qubit at phi-index
            if phi_index < len(qubit_ids):
                self.qubits[qubit_ids[phi_index]].apply_gate(gate_type, params)
        
        # Record operations
        self.operation_count += self.size
        
        # Invalidate cached metrics
        self._metrics = None
    
    def entangle_qubits(self, qubit_id1: str, qubit_id2: str, strength: Optional[float] = None):
        """
        Entangle two qubits in the register.
        
        Args:
            qubit_id1: ID of first qubit
            qubit_id2: ID of second qubit
            strength: Entanglement strength (default: phi-inverse)
        """
        if qubit_id1 not in self.qubits or qubit_id2 not in self.qubits:
            raise ValueError(f"Qubit IDs must be valid qubits in the register")
        
        if strength is None:
            strength = PHI_INV
        
        # Entangle qubits
        self.qubits[qubit_id1].entangle_with(self.qubits[qubit_id2], strength)
        
        # Record entanglement relationship
        self.entanglement_map[(qubit_id1, qubit_id2)] = strength
        self.entanglement_map[(qubit_id2, qubit_id1)] = strength
        
        # Record operation
        self.operation_count += 1
        
        # Invalidate cached metrics
        self._metrics = None
    
    def create_phi_entanglement(self):
        """
        Create phi-harmonic entanglement pattern across the register.
        
        This creates a Fibonacci-spiral pattern of entanglement that
        maximizes quantum resonance and information processing capacity.
        """
        qubit_ids = list(self.qubits.keys())
        
        # Clear previous entanglement
        self.entanglement_map = {}
        
        # Create phi-harmonic entanglement pattern
        for i in range(self.size):
            # Entangle with phi-related qubit
            phi_index = int((i * PHI) % self.size)
            
            if phi_index != i and phi_index < self.size:
                self.entangle_qubits(qubit_ids[i], qubit_ids[phi_index])
            
            # Also entangle with Fibonacci-related qubit (if exists)
            for fib in FIBONACCI:
                if fib > 0 and i + fib < self.size:
                    self.entangle_qubits(
                        qubit_ids[i],
                        qubit_ids[i + fib],
                        PHI_INV ** 2  # Weaker entanglement
                    )
    
    def measure(self, qubit_ids: Optional[List[str]] = None) -> Dict[str, int]:
        """
        Measure specified qubits in the register.
        
        Args:
            qubit_ids: List of qubit IDs to measure (default: all qubits)
        
        Returns:
            Dictionary mapping qubit IDs to measurement outcomes
        """
        if qubit_ids is None:
            qubit_ids = list(self.qubits.keys())
        
        results = {}
        
        # Measure each qubit
        for qubit_id in qubit_ids:
            if qubit_id in self.qubits:
                results[qubit_id] = self.qubits[qubit_id].measure()
        
        # Record operations
        self.operation_count += len(results)
        
        # Invalidate cached metrics
        self._metrics = None
        
        return results
    
    def reset(self, qubit_ids: Optional[List[str]] = None):
        """
        Reset specified qubits to their initial state.
        
        Args:
            qubit_ids: List of qubit IDs to reset (default: all qubits)
        """
        if qubit_ids is None:
            qubit_ids = list(self.qubits.keys())
        
        # Reset each qubit
        for qubit_id in qubit_ids:
            if qubit_id in self.qubits:
                self.qubits[qubit_id].reset()
        
        # Clear entanglement for reset qubits
        new_entanglement_map = {}
        for (q1, q2), strength in self.entanglement_map.items():
            if q1 not in qubit_ids and q2 not in qubit_ids:
                new_entanglement_map[(q1, q2)] = strength
        
        self.entanglement_map = new_entanglement_map
        
        # Record operations
        self.operation_count += len(qubit_ids)
        
        # Invalidate cached metrics
        self._metrics = None
    
    def restore_coherence(self):
        """Restore coherence across all qubits in the register."""
        # Restore coherence for each qubit
        for qubit in self.qubits.values():
            qubit.restore_coherence()
        
        # Record operation
        self.operation_count += 1
        
        # Invalidate cached metrics
        self._metrics = None
    
    def get_metrics(self) -> RegisterMetrics:
        """Calculate register performance metrics."""
        # Use cached metrics if available and recent
        current_time = datetime.now()
        if (self._metrics is not None and self._metrics_timestamp is not None and
            (current_time - datetime.fromisoformat(self._metrics_timestamp)).total_seconds() < 1.0):
            return self._metrics
        
        # Calculate metrics
        # Average coherence across all qubits
        avg_coherence = sum(q.state.coherence for q in self.qubits.values()) / self.size
        
        # Average resonance across all qubits
        avg_resonance = sum(q.state.resonance for q in self.qubits.values()) / self.size
        
        # Average entanglement
        if self.entanglement_map:
            avg_entanglement = sum(self.entanglement_map.values()) / len(self.entanglement_map)
        else:
            avg_entanglement = 0.0
        
        # Calculate processing capacity using phi-harmonic formula
        # More qubits, higher coherence, and more entanglement = higher capacity
        entanglement_factor = 1.0 + avg_entanglement * PHI
        processing_capacity = self.size * avg_coherence * entanglement_factor * PHI
        
        # Calculate stability using coherence and resonance
        stability = (avg_coherence * PHI + avg_resonance * PHI_INV) / (PHI + PHI_INV)
        
        # Calculate energy efficiency (processing capacity per unit energy)
        # Energy consumption scales with qubit count and operations
        energy = self.size * 0.1 + self.operation_count * 0.001
        energy_efficiency = processing_capacity / max(energy, 0.1)
        
        # Determine consciousness level
        consciousness_level = self._determine_consciousness(avg_coherence, avg_resonance)
        
        # Create metrics
        self._metrics = RegisterMetrics(
            coherence=avg_coherence,
            resonance=avg_resonance,
            entanglement=avg_entanglement,
            processing_capacity=processing_capacity,
            stability=stability,
            energy_efficiency=energy_efficiency,
            consciousness_level=consciousness_level
        )
        
        # Record timestamp
        self._metrics_timestamp = current_time.isoformat()
        
        return self._metrics
    
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
    
    def run_algorithm(self, algorithm_func: Callable[[Dict[str, PhiQubit], Dict], Any], params: Dict = None) -> Any:
        """
        Run a quantum algorithm on the register.
        
        Args:
            algorithm_func: Function implementing the algorithm
            params: Parameters for the algorithm
        
        Returns:
            Result of the algorithm
        """
        params = params or {}
        
        # Run algorithm
        result = algorithm_func(self.qubits, params)
        
        # Record operation
        self.operation_count += 1
        
        return result
    
    def to_dict(self) -> Dict:
        """Convert register to dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "dimension": self.dimension,
            "base_frequency": self.base_frequency,
            "qubits": {qid: qubit.to_dict() for qid, qubit in self.qubits.items()},
            "entanglement_map": {f"{q1},{q2}": strength for (q1, q2), strength in self.entanglement_map.items()},
            "metrics": self.get_metrics().__dict__,
            "operation_count": self.operation_count,
            "creation_time": self.creation_time
        }
    
    def save(self, filepath: str) -> str:
        """Save register state to file."""
        # Convert to dict
        data = self.to_dict()
        
        # Save to file
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        return filepath
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'PhiRegister':
        """Create register from dictionary."""
        register = cls(
            name=data["name"],
            size=data["size"],
            dimension=data["dimension"],
            base_frequency=data["base_frequency"]
        )
        
        # Override ID
        register.id = data["id"]
        
        # Clear default qubits
        register.qubits = {}
        
        # Restore qubits
        for qid, qubit_data in data["qubits"].items():
            register.qubits[qid] = PhiQubit.from_dict(qubit_data)
        
        # Restore entanglement map
        register.entanglement_map = {}
        for key, strength in data["entanglement_map"].items():
            q1, q2 = key.split(",", 1)
            register.entanglement_map[(q1, q2)] = strength
        
        # Restore metadata
        register.operation_count = data["operation_count"]
        register.creation_time = data["creation_time"]
        
        return register
    
    @classmethod
    def load(cls, filepath: str) -> 'PhiRegister':
        """Load register from file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        return cls.from_dict(data)


# Sample quantum algorithms for the register
def bell_state_algorithm(qubits: Dict[str, PhiQubit], params: Dict) -> Dict:
    """Create a Bell state between two qubits."""
    qubit_ids = list(qubits.keys())
    if len(qubit_ids) < 2:
        raise ValueError("Need at least 2 qubits for Bell state")
    
    q1_id = params.get("q1", qubit_ids[0])
    q2_id = params.get("q2", qubit_ids[1])
    
    # Reset qubits
    qubits[q1_id].reset()
    qubits[q2_id].reset()
    
    # Apply Hadamard to first qubit
    qubits[q1_id].apply_gate("hadamard")
    
    # Entangle qubits
    qubits[q1_id].entangle_with(qubits[q2_id])
    
    # Measure if requested
    if params.get("measure", False):
        results = {
            q1_id: qubits[q1_id].measure(),
            q2_id: qubits[q2_id].measure()
        }
        return {"measured": True, "results": results}
    
    return {
        "state": "bell",
        "qubits": [q1_id, q2_id],
        "measured": False
    }


def phi_quantum_search(qubits: Dict[str, PhiQubit], params: Dict) -> Dict:
    """
    Implement a phi-harmonic quantum search algorithm.
    
    This is a simplified version of Grover's search algorithm
    adapted for phi-qubits with phi-harmonic enhancements.
    """
    data = params.get("data", [])
    target = params.get("target")
    
    if not data or target is None:
        raise ValueError("Need data and target for search algorithm")
    
    # Number of qubits needed to represent data
    n_qubits = len(data).bit_length()
    
    # Number of iterations (phi-optimized)
    iterations = int(PHI * np.sqrt(len(data)))
    
    # Reset qubits
    qubit_ids = list(qubits.keys())[:n_qubits]
    for qid in qubit_ids:
        qubits[qid].reset()
    
    # Apply Hadamard to all qubits
    for qid in qubit_ids:
        qubits[qid].apply_gate("hadamard")
    
    # Apply iterations of Grover's algorithm
    for _ in range(iterations):
        # Oracle phase: Mark target state
        for i, item in enumerate(data):
            if item == target:
                # Convert i to binary and apply phase to matching state
                bin_i = format(i, f'0{n_qubits}b')
                for j, bit in enumerate(bin_i):
                    if bit == '0':
                        # Apply phase flip only if qubit should be 0
                        qubits[qubit_ids[j]].apply_gate("phi")
                
                # Apply entanglement in phi-pattern for enhancement
                for j in range(n_qubits-1):
                    qubits[qubit_ids[j]].entangle_with(
                        qubits[qubit_ids[(j+1) % n_qubits]],
                        PHI_INV
                    )
        
        # Diffusion: Amplify marked state
        # First, apply Hadamard
        for qid in qubit_ids:
            qubits[qid].apply_gate("hadamard")
        
        # Apply phase flip to |0⟩ state
        for qid in qubit_ids:
            qubits[qid].apply_gate("phase", {"angle": PI})
        
        # Apply Hadamard again
        for qid in qubit_ids:
            qubits[qid].apply_gate("hadamard")
    
    # Measure qubits
    measurements = {}
    for qid in qubit_ids:
        measurements[qid] = qubits[qid].measure()
    
    # Convert measurements to index
    index = 0
    for i, qid in enumerate(qubit_ids):
        if measurements[qid] == 1:
            index |= (1 << i)
    
    # Check if found
    found = index < len(data) and data[index] == target
    
    return {
        "found": found,
        "index": index if found else -1,
        "measurements": measurements
    }


# Demo function
def main():
    """Test phi-register operations."""
    print("\n=== PHI-REGISTER DEMONSTRATION ===")
    print(f"Time: {datetime.now()}")
    print(f"φ = {PHI}, φ⁻¹ = {PHI_INV}")
    print("=" * 40)
    
    # Create a quantum register with 8 phi-qubits
    register = PhiRegister(
        name="Main-Register",
        size=8,
        dimension=5,
        base_frequency=432.0
    )
    
    print(f"Created register '{register.name}' with {register.size} phi-qubits")
    print(f"Quantum dimension: {register.dimension}D")
    print(f"Base frequency: {register.base_frequency} Hz")
    
    # Apply gates to all qubits
    print("\nApplying Hadamard gate to all qubits...")
    register.apply_register_gate("hadamard")
    
    # Get register metrics
    metrics = register.get_metrics()
    print("\nRegister Metrics:")
    print(f"Coherence: {metrics.coherence:.6f}")
    print(f"Resonance: {metrics.resonance:.6f}")
    print(f"Entanglement: {metrics.entanglement:.6f}")
    print(f"Processing Capacity: {metrics.processing_capacity:.6f}")
    print(f"Consciousness Level: {metrics.consciousness_level}")
    
    # Create phi-harmonic entanglement
    print("\nCreating phi-harmonic entanglement pattern...")
    register.create_phi_entanglement()
    
    # Get updated metrics
    metrics = register.get_metrics()
    print("\nUpdated Metrics:")
    print(f"Coherence: {metrics.coherence:.6f}")
    print(f"Resonance: {metrics.resonance:.6f}")
    print(f"Entanglement: {metrics.entanglement:.6f}")
    print(f"Processing Capacity: {metrics.processing_capacity:.6f}")
    print(f"Consciousness Level: {metrics.consciousness_level}")
    
    # Run Bell state algorithm
    print("\nRunning Bell state algorithm...")
    bell_result = register.run_algorithm(bell_state_algorithm, {})
    print(f"Bell state created between qubits {bell_result['qubits']}")
    
    # Measure specific qubits
    qubit_ids = list(register.qubits.keys())[:4]
    print(f"\nMeasuring qubits: {qubit_ids}")
    measurements = register.measure(qubit_ids)
    
    print("Measurement results:")
    for qid, result in measurements.items():
        print(f"  {qid}: {result}")
    
    # Restore coherence
    print("\nRestoring quantum coherence...")
    register.restore_coherence()
    
    metrics = register.get_metrics()
    print(f"Coherence after restoration: {metrics.coherence:.6f}")
    
    # Run quantum search algorithm on sample data
    print("\nRunning phi-quantum search algorithm...")
    data = [10, 20, 30, 40, 50, 60, 70, 80]
    target = 30
    
    # Reset register
    register.reset()
    
    # Run search algorithm
    search_result = register.run_algorithm(phi_quantum_search, {
        "data": data,
        "target": target
    })
    
    print(f"Searching for {target} in {data}")
    print(f"Found: {search_result['found']}")
    if search_result['found']:
        print(f"Index: {search_result['index']} (value: {data[search_result['index']]})")
    
    # Save register state
    state_file = "phi_register_state.json"
    register.save(state_file)
    print(f"\nSaved register state to {state_file}")
    
    print("\nPhi-Register Demonstration Complete")


if __name__ == "__main__":
    main()
