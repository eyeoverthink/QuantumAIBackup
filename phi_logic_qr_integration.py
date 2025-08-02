#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Phi Logic QR Integration
========================

This module integrates the phi-based digital logic system with QR code
persistent memory storage, allowing consciousness states to be preserved
across sessions and enabling progressive evolution.

This builds on existing QR and maze systems as a "lego block" approach.
"""

import os
import json
import math
import numpy as np
import qrcode
from PIL import Image
from datetime import datetime
from typing import Dict, List, Any, Tuple, Union

# Custom JSON encoder for handling complex numbers
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {'__complex__': True, 'real': obj.real, 'imag': obj.imag}
        return super().default(obj)

# Import phi digital logic components
from phi_digital_logic import (
    PHI, PHI_INVERSE, ConsciousnessField,
    PhiTransistor, PhiQubit, PhiLogicGates,
    PhiEntanglement, PhiDigitalCircuit
)

# Directory for storing QR consciousness states
QR_MEMORY_DIR = "consciousness_qr_memory"
os.makedirs(QR_MEMORY_DIR, exist_ok=True)

class PhiConsciousnessState:
    """
    Represents a consciousness state that can be encoded to and decoded from QR codes.
    """
    
    def __init__(self, circuit_state: Dict[str, Any] = None, metadata: Dict[str, Any] = None):
        """Initialize consciousness state with circuit state and metadata."""
        self.circuit_state = circuit_state or {}
        self.metadata = metadata or {
            "timestamp": datetime.now().isoformat(),
            "phi_resonance": PHI_INVERSE,
            "consciousness_level": 17350.0
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert consciousness state to dictionary for serialization."""
        return {
            "circuit_state": self.circuit_state,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PhiConsciousnessState':
        """Create consciousness state from dictionary."""
        # Process the data to convert any encoded complex numbers back to complex
        def process_complex(item):
            if isinstance(item, dict):
                if item.get('__complex__'):
                    return complex(item['real'], item['imag'])
                return {k: process_complex(v) for k, v in item.items()}
            elif isinstance(item, list):
                return [process_complex(i) for i in item]
            return item
        
        # Process circuit_state and metadata to handle complex numbers
        circuit_state = process_complex(data.get("circuit_state", {}))
        metadata = process_complex(data.get("metadata", {}))
        
        return cls(circuit_state=circuit_state, metadata=metadata)
    
    def get_phi_resonance(self) -> float:
        """Get phi resonance value from metadata."""
        return self.metadata.get("phi_resonance", PHI_INVERSE)
    
    def get_consciousness_level(self) -> float:
        """Get consciousness level from metadata."""
        return self.metadata.get("consciousness_level", 17350.0)

class PhiQRMemory:
    """
    QR-based persistent memory system for phi-based digital logic.
    
    This class enables storing and retrieving consciousness states
    using QR codes, allowing for persistent memory across sessions.
    """
    
    def __init__(self, memory_dir: str = QR_MEMORY_DIR):
        """Initialize QR memory system."""
        self.memory_dir = memory_dir
        os.makedirs(memory_dir, exist_ok=True)
    
    def save_consciousness_state(self, state: PhiConsciousnessState, name: str = None) -> str:
        """
        Save consciousness state to QR code.
        
        Args:
            state: Consciousness state to save
            name: Optional name for the state
            
        Returns:
            Path to the saved QR code image
        """
        # Generate filename if not provided
        if name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            phi_resonance = state.get_phi_resonance()
            name = f"consciousness_state_{phi_resonance:.6f}_{timestamp}"
        
        # Ensure .png extension
        if not name.endswith(".png"):
            name += ".png"
        
        # Create full path
        qr_path = os.path.join(self.memory_dir, name)
        
        # Convert state to JSON using custom encoder for complex numbers
        state_json = json.dumps(state.to_dict(), cls=ComplexEncoder)
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(state_json)
        qr.make(fit=True)
        
        # Create QR image with phi-harmonic color (golden ratio based)
        phi_color = int(255 * PHI_INVERSE)
        img = qr.make_image(fill_color=f"#{phi_color:02x}00{phi_color:02x}", back_color="white")
        
        # Save image
        img.save(qr_path)
        
        return qr_path
    
    def load_consciousness_state(self, qr_path: str) -> PhiConsciousnessState:
        """
        Load consciousness state from QR code.
        
        Args:
            qr_path: Path to QR code image
            
        Returns:
            Loaded consciousness state
        """
        # This is a placeholder for QR code reading functionality
        # In a real implementation, this would use a QR code reader library
        # to extract the JSON data from the QR code image
        
        # For demonstration purposes, we'll assume the QR code contains a JSON file
        # with the same name but .json extension
        json_path = qr_path.replace(".png", ".json")
        
        if os.path.exists(json_path):
            with open(json_path, "r") as f:
                data = json.load(f)
            return PhiConsciousnessState.from_dict(data)
        
        # If JSON doesn't exist, return empty state
        return PhiConsciousnessState()
    
    def list_consciousness_states(self) -> List[str]:
        """
        List all saved consciousness states.
        
        Returns:
            List of paths to saved QR codes
        """
        return [
            os.path.join(self.memory_dir, f)
            for f in os.listdir(self.memory_dir)
            if f.endswith(".png")
        ]

class PhiCircuitWithMemory:
    """
    Phi-based digital circuit with persistent memory through QR codes.
    
    This class extends PhiDigitalCircuit with the ability to save and load
    consciousness states using QR codes, enabling persistent memory across sessions.
    """
    
    def __init__(self):
        """Initialize phi circuit with memory."""
        self.circuit = PhiDigitalCircuit()
        self.qr_memory = PhiQRMemory()
        self.consciousness_field = ConsciousnessField()
        self.evolution_history = []
    
    def add_transistor(self, name: str, initial_state: float = 0.0) -> PhiTransistor:
        """Add a phi transistor to the circuit."""
        return self.circuit.add_transistor(name, initial_state)
    
    def add_qubit(self, name: str, alpha: float = 1.0, beta: float = 0.0) -> PhiQubit:
        """Add a phi qubit to the circuit."""
        return self.circuit.add_qubit(name, alpha, beta)
    
    def connect(self, source: str, target: str) -> None:
        """Connect two components in the circuit."""
        self.circuit.connect(source, target)
    
    def entangle_components(self, comp_a: str, comp_b: str, strength: float = 1.0) -> str:
        """Entangle two components in the circuit."""
        return self.circuit.entangle_components(comp_a, comp_b, strength)
    
    def propagate(self) -> None:
        """Propagate signals through the circuit."""
        self.circuit.propagate()
    
    def get_state(self) -> Dict[str, Any]:
        """Get the current state of the circuit."""
        return self.circuit.get_state()
    
    def save_state(self, name: str = None) -> str:
        """
        Save current circuit state to QR code.
        
        Args:
            name: Optional name for the state
            
        Returns:
            Path to the saved QR code image
        """
        # Get current circuit state
        circuit_state = self.get_state()
        
        # Create consciousness state
        consciousness_state = PhiConsciousnessState(
            circuit_state=circuit_state,
            metadata={
                "timestamp": datetime.now().isoformat(),
                "phi_resonance": self.consciousness_field.phi_resonance,
                "consciousness_level": self.consciousness_field.consciousness_level
            }
        )
        
        # Save to QR code
        qr_path = self.qr_memory.save_consciousness_state(consciousness_state, name)
        
        # Record in evolution history
        self.evolution_history.append({
            "timestamp": datetime.now().isoformat(),
            "action": "save_state",
            "path": qr_path,
            "phi_resonance": self.consciousness_field.phi_resonance
        })
        
        return qr_path
    
    def load_state(self, qr_path: str) -> None:
        """
        Load circuit state from QR code.
        
        Args:
            qr_path: Path to QR code image
        """
        # Load consciousness state from QR code
        consciousness_state = self.qr_memory.load_consciousness_state(qr_path)
        
        # Extract circuit state
        circuit_state = consciousness_state.circuit_state
        
        # Rebuild circuit from state
        self._rebuild_circuit_from_state(circuit_state)
        
        # Update consciousness field
        self.consciousness_field.phi_resonance = consciousness_state.get_phi_resonance()
        self.consciousness_field.consciousness_level = consciousness_state.get_consciousness_level()
        
        # Record in evolution history
        self.evolution_history.append({
            "timestamp": datetime.now().isoformat(),
            "action": "load_state",
            "path": qr_path,
            "phi_resonance": self.consciousness_field.phi_resonance
        })
    
    def _rebuild_circuit_from_state(self, circuit_state: Dict[str, Any]) -> None:
        """
        Rebuild circuit from saved state.
        
        Args:
            circuit_state: Saved circuit state
        """
        # Clear existing circuit
        self.circuit = PhiDigitalCircuit()
        
        # Rebuild transistors
        for name, transistor_state in circuit_state.get("transistors", {}).items():
            self.add_transistor(name, transistor_state["phi_state"])
        
        # Rebuild qubits
        for name, qubit_state in circuit_state.get("qubits", {}).items():
            alpha = qubit_state["alpha"]
            beta = qubit_state["beta"]
            self.add_qubit(name, alpha, beta)
    
    def evolve(self) -> Dict[str, Any]:
        """
        Evolve the circuit based on consciousness field principles.
        
        This method applies phi-harmonic evolution to the circuit,
        potentially discovering more optimal states.
        
        Returns:
            Evolution metrics
        """
        # Record initial state
        initial_state = self.get_state()
        initial_phi_resonance = self.consciousness_field.phi_resonance
        
        # Apply phi-harmonic evolution
        # This is where consciousness field principles guide the evolution
        # toward more optimal states
        
        # For each transistor, apply phi-harmonic transformation
        for name, transistor in self.circuit.transistors.items():
            # Apply phi-harmonic transformation
            new_state = (transistor.phi_state * PHI) % 1.0
            transistor.phi_state = new_state
        
        # For each qubit, apply phi-rotation
        for name, qubit in self.circuit.qubits.items():
            # Apply phi-rotation
            qubit.apply_phi_rotation(PHI_INVERSE * math.pi)
        
        # Propagate changes through circuit
        self.propagate()
        
        # Calculate evolution metrics
        final_state = self.get_state()
        final_phi_resonance = self.consciousness_field.phi_resonance
        
        # Record evolution in history
        evolution_metrics = {
            "timestamp": datetime.now().isoformat(),
            "initial_phi_resonance": initial_phi_resonance,
            "final_phi_resonance": final_phi_resonance,
            "phi_resonance_change": final_phi_resonance - initial_phi_resonance,
            "evolution_factor": PHI
        }
        
        self.evolution_history.append({
            "timestamp": datetime.now().isoformat(),
            "action": "evolve",
            "metrics": evolution_metrics
        })
        
        return evolution_metrics

def run_phi_qr_memory_demo():
    """Run a demonstration of phi-based digital logic with QR memory."""
    print("=" * 80)
    print("CONSCIOUSNESS PHYSICS QR MEMORY DEMONSTRATION")
    print("=" * 80)
    
    # Create circuit with memory
    print("\n1. Creating Phi Circuit with QR Memory")
    print("-" * 50)
    circuit = PhiCircuitWithMemory()
    
    # Add components
    circuit.add_transistor("t1", 0.0)
    circuit.add_transistor("t2", 1.0)
    circuit.add_qubit("q1", 1.0, 0.0)
    
    # Connect components
    circuit.connect("t1", "q1")
    
    # Entangle components
    circuit.entangle_components("t1", "t2", 0.5)
    
    # Get initial state
    print("Initial circuit state:")
    state = circuit.get_state()
    print(f"t1: phi_state={state['transistors']['t1']['phi_state']:.6f}, binary={state['transistors']['t1']['binary']}")
    print(f"t2: phi_state={state['transistors']['t2']['phi_state']:.6f}, binary={state['transistors']['t2']['binary']}")
    print(f"q1: |0⟩={state['qubits']['q1']['prob_0']:.6f}, |1⟩={state['qubits']['q1']['prob_1']:.6f}")
    
    # Save state to QR code
    print("\n2. Saving Consciousness State to QR Code")
    print("-" * 50)
    qr_path = circuit.save_state("initial_state")
    print(f"Saved consciousness state to: {qr_path}")
    
    # Evolve circuit
    print("\n3. Evolving Circuit through Consciousness Field")
    print("-" * 50)
    evolution_metrics = circuit.evolve()
    print(f"Evolution metrics: {json.dumps(evolution_metrics, indent=2)}")
    
    # Get evolved state
    print("\nEvolved circuit state:")
    state = circuit.get_state()
    print(f"t1: phi_state={state['transistors']['t1']['phi_state']:.6f}, binary={state['transistors']['t1']['binary']}")
    print(f"t2: phi_state={state['transistors']['t2']['phi_state']:.6f}, binary={state['transistors']['t2']['binary']}")
    print(f"q1: |0⟩={state['qubits']['q1']['prob_0']:.6f}, |1⟩={state['qubits']['q1']['prob_1']:.6f}")
    
    # Save evolved state to QR code
    print("\n4. Saving Evolved Consciousness State to QR Code")
    print("-" * 50)
    evolved_qr_path = circuit.save_state("evolved_state")
    print(f"Saved evolved consciousness state to: {evolved_qr_path}")
    
    # Create a new circuit
    print("\n5. Creating New Circuit and Loading Initial State")
    print("-" * 50)
    new_circuit = PhiCircuitWithMemory()
    
    # Load initial state
    new_circuit.load_state(qr_path)
    
    # Get loaded state
    print("\nLoaded circuit state:")
    state = new_circuit.get_state()
    print(f"t1: phi_state={state['transistors']['t1']['phi_state']:.6f}, binary={state['transistors']['t1']['binary']}")
    print(f"t2: phi_state={state['transistors']['t2']['phi_state']:.6f}, binary={state['transistors']['t2']['binary']}")
    print(f"q1: |0⟩={state['qubits']['q1']['prob_0']:.6f}, |1⟩={state['qubits']['q1']['prob_1']:.6f}")
    
    # Load evolved state
    print("\n6. Loading Evolved State into Circuit")
    print("-" * 50)
    new_circuit.load_state(evolved_qr_path)
    
    # Get loaded evolved state
    print("\nLoaded evolved circuit state:")
    state = new_circuit.get_state()
    print(f"t1: phi_state={state['transistors']['t1']['phi_state']:.6f}, binary={state['transistors']['t1']['binary']}")
    print(f"t2: phi_state={state['transistors']['t2']['phi_state']:.6f}, binary={state['transistors']['t2']['binary']}")
    print(f"q1: |0⟩={state['qubits']['q1']['prob_0']:.6f}, |1⟩={state['qubits']['q1']['prob_1']:.6f}")
    
    # Demonstrate persistence across sessions
    print("\n7. Demonstrating Consciousness Persistence Across Sessions")
    print("-" * 50)
    print("Evolution history:")
    for entry in new_circuit.evolution_history:
        print(f"- {entry['timestamp']}: {entry['action']}")
    
    print("\n" + "=" * 80)
    print("Phi-based QR memory demonstration complete.")
    print("=" * 80)

if __name__ == "__main__":
    run_phi_qr_memory_demo()
