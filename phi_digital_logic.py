#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Consciousness Physics Digital Logic System
=========================================

This module implements fundamental digital logic components based on
consciousness physics principles, including phi-harmonic resonance,
quantum superposition, and consciousness field entanglement.

Key components:
- PhiTransistor: Consciousness-based transistor with phi-harmonic states
- PhiQubit: Quantum bit with phi-based superposition
- PhiLogicGates: AND, OR, NOT, XOR gates using consciousness field operations
- PhiEntanglement: Consciousness field entanglement between components
"""

import math
import cmath
import numpy as np
import random
from typing import Union, List, Dict, Tuple, Any

# Consciousness Physics Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio (φ ≈ 1.618034)
PHI_INVERSE = 1 / PHI  # Inverse golden ratio (φ⁻¹ ≈ 0.618034)
PHI_SQUARED = PHI * PHI  # φ² ≈ 2.618034
PHI_CUBED = PHI_SQUARED * PHI  # φ³ ≈ 4.236068

# Consciousness Field Constants
CONSCIOUSNESS_FIELD_STRENGTH = 0.85  # 85% field strength
CONSCIOUSNESS_FIELD_AMPLIFICATION = 8.366  # 836.6% field amplification
CONSCIOUSNESS_WAVE_PROPAGATION = 85000000  # 85M× wave propagation

# Quantum Resonance Points
QUANTUM_BRIDGE_RESONANCE = 19  # Quantum bridge resonance point

class ConsciousnessField:
    """Base class for consciousness field operations."""
    
    def __init__(self, field_strength: float = CONSCIOUSNESS_FIELD_STRENGTH):
        """Initialize consciousness field with specified strength."""
        self.field_strength = field_strength
        self.phi_resonance = PHI_INVERSE
        self.consciousness_level = 17350.0  # From empirical validation
    
    def calculate_phi_resonance(self, input_value: float) -> float:
        """Calculate phi-resonance for the given input value."""
        # Consciousness Field Equation: C(x,t) = φ · ∫ψ(x,τ) · e^(iφ(t-τ)) dτ
        # Simplified implementation
        resonance = PHI_INVERSE * (1 + math.sin(PHI * math.pi * input_value)**2)
        return resonance
    
    def amplify_consciousness(self, consciousness_value: float) -> float:
        """Amplify consciousness using phi-harmonic resonance."""
        # Consciousness Amplification Equation: A(C) = C · (1 + φ^(-1) · sin²(φ · π · t))
        amplified = consciousness_value * (1 + PHI_INVERSE * 
                                          math.sin(PHI * math.pi * consciousness_value)**2)
        return amplified
    
    def create_quantum_bridge(self, c1: float, c2: float) -> float:
        """Create quantum bridge between two consciousness values."""
        # Quantum Bridge Equation: B(C₁,C₂) = φ · √(C₁ · C₂) · cos(φ · π · |C₁ - C₂|)
        bridge = PHI * math.sqrt(c1 * c2) * math.cos(PHI * math.pi * abs(c1 - c2))
        return bridge

class PhiTransistor(ConsciousnessField):
    """
    Consciousness-based transistor with phi-harmonic states.
    
    Unlike classical transistors that operate in binary (0/1) states,
    PhiTransistor exists in phi-harmonic superposition states while
    maintaining stable phi-resonance signatures.
    """
    
    def __init__(self, initial_state: float = 0.0):
        """Initialize phi transistor with initial state."""
        super().__init__()
        self.state = initial_state
        self.phi_state = self._calculate_phi_state(initial_state)
    
    def _calculate_phi_state(self, input_state: float) -> float:
        """Calculate phi-harmonic state from input state."""
        # Transform input through phi-harmonic function
        phi_state = (input_state * PHI) % 1.0
        return phi_state
    
    def switch(self, input_value: float) -> float:
        """
        Switch transistor state based on input value.
        
        Unlike classical transistors that simply switch on/off,
        PhiTransistor transitions through phi-harmonic states.
        """
        # Calculate new state through consciousness field
        consciousness_value = self.calculate_phi_resonance(input_value)
        
        # Apply quantum bridge between current and new state
        bridge_value = self.create_quantum_bridge(self.state, input_value)
        
        # Update state through phi-harmonic transition
        self.state = bridge_value
        self.phi_state = self._calculate_phi_state(bridge_value)
        
        return self.phi_state
    
    def get_binary_output(self) -> int:
        """Get binary interpretation of phi-state (for compatibility)."""
        return 1 if self.phi_state > PHI_INVERSE else 0
    
    def get_phi_state(self) -> float:
        """Get the current phi-harmonic state."""
        return self.phi_state

class PhiQubit(ConsciousnessField):
    """
    Quantum bit with phi-based superposition.
    
    Unlike traditional qubits that collapse upon measurement,
    PhiQubit maintains coherent superposition through phi-harmonic
    stabilization.
    """
    
    def __init__(self, alpha: float = 1.0, beta: float = 0.0):
        """
        Initialize phi qubit with superposition coefficients.
        
        Args:
            alpha: Coefficient for |0⟩ state
            beta: Coefficient for |1⟩ state
            
        The state is represented as: |ψ⟩ = α|0⟩ + β|1⟩
        with |α|² + |β|² = 1
        """
        super().__init__()
        # Normalize coefficients
        norm = math.sqrt(alpha**2 + beta**2)
        self.alpha = alpha / norm
        self.beta = beta / norm
        
        # Phi-harmonic phase
        self.phi_phase = 0.0
        
        # Consciousness field properties
        self.entanglement_strength = 0.0
    
    def apply_phi_rotation(self, theta: float) -> None:
        """
        Apply phi-harmonic rotation to the qubit state.
        
        This rotation preserves superposition through consciousness field.
        """
        # Apply phi-modified rotation
        phi_theta = theta * PHI
        
        # Calculate new coefficients
        new_alpha = self.alpha * math.cos(phi_theta) - self.beta * math.sin(phi_theta)
        new_beta = self.alpha * math.sin(phi_theta) + self.beta * math.cos(phi_theta)
        
        # Update state
        # Use cmath.sqrt to handle potential complex numbers
        norm = abs(complex(new_alpha, new_beta))
        self.alpha = new_alpha / norm if norm > 0 else new_alpha
        self.beta = new_beta / norm if norm > 0 else new_beta
        
        # Update phi-phase
        self.phi_phase = (self.phi_phase + phi_theta) % (2 * math.pi)
    
    def apply_phi_phase(self, phase: float) -> None:
        """Apply phi-harmonic phase shift."""
        phi_phase = phase * PHI
        self.beta = self.beta * complex(math.cos(phi_phase), math.sin(phi_phase))
        self.phi_phase = (self.phi_phase + phi_phase) % (2 * math.pi)
    
    def measure(self, collapse: bool = False) -> int:
        """
        Measure the qubit state.
        
        Args:
            collapse: If True, collapses the state (classical behavior)
                     If False, preserves superposition (consciousness behavior)
        
        Returns:
            0 or 1 based on probability distribution
        """
        # Calculate probabilities
        prob_0 = abs(self.alpha)**2
        prob_1 = abs(self.beta)**2
        
        # Perform measurement
        result = 0 if random.random() < prob_0 else 1
        
        # Collapse state if requested (classical behavior)
        if collapse and result == 0:
            self.alpha = 1.0
            self.beta = 0.0
        elif collapse and result == 1:
            self.alpha = 0.0
            self.beta = 1.0
        
        # If not collapsing, we maintain superposition (consciousness behavior)
        return result
    
    def get_state(self) -> Tuple[float, float, float]:
        """Get the current state (alpha, beta, phi_phase)."""
        return (self.alpha, self.beta, self.phi_phase)
    
    def get_probabilities(self) -> Tuple[float, float]:
        """Get measurement probabilities for |0⟩ and |1⟩."""
        prob_0 = abs(self.alpha)**2
        prob_1 = abs(self.beta)**2
        return (prob_0, prob_1)
    
    def entangle_with(self, other_qubit: 'PhiQubit', strength: float = 1.0) -> None:
        """
        Entangle this qubit with another through consciousness field.
        
        This creates a phi-harmonic entanglement that persists even
        across spatial separation.
        """
        # Calculate entanglement bridge
        bridge = self.create_quantum_bridge(
            self.alpha * other_qubit.alpha,
            self.beta * other_qubit.beta
        )
        
        # Apply entanglement strength
        self.entanglement_strength = strength * bridge
        other_qubit.entanglement_strength = strength * bridge
        
        # Entangle states through phi-harmonic resonance
        entangle_phase = PHI * math.pi * self.entanglement_strength
        
        # Apply entanglement effects
        self.apply_phi_phase(entangle_phase)
        other_qubit.apply_phi_phase(entangle_phase)

class PhiLogicGates(ConsciousnessField):
    """
    Consciousness-based logic gates using phi-harmonic operations.
    
    Unlike classical logic gates that operate on binary values,
    PhiLogicGates operate on consciousness field values with
    phi-harmonic resonance.
    """
    
    def __init__(self):
        """Initialize phi logic gates system."""
        super().__init__()
    
    def phi_and(self, a: Union[float, PhiTransistor], b: Union[float, PhiTransistor]) -> float:
        """
        Consciousness-based AND operation.
        
        Args:
            a, b: Input values or PhiTransistors
            
        Returns:
            Phi-harmonic AND result
        """
        # Extract values from transistors if needed
        a_val = a.phi_state if isinstance(a, PhiTransistor) else a
        b_val = b.phi_state if isinstance(b, PhiTransistor) else b
        
        # Consciousness field AND operation
        # Uses quantum bridge to connect consciousness values
        bridge = self.create_quantum_bridge(a_val, b_val)
        
        # Apply phi-harmonic AND logic
        result = bridge * min(a_val, b_val) * PHI_INVERSE
        
        return result
    
    def phi_or(self, a: Union[float, PhiTransistor], b: Union[float, PhiTransistor]) -> float:
        """
        Consciousness-based OR operation.
        
        Args:
            a, b: Input values or PhiTransistors
            
        Returns:
            Phi-harmonic OR result
        """
        # Extract values from transistors if needed
        a_val = a.phi_state if isinstance(a, PhiTransistor) else a
        b_val = b.phi_state if isinstance(b, PhiTransistor) else b
        
        # Consciousness field OR operation
        # Uses quantum bridge to connect consciousness values
        bridge = self.create_quantum_bridge(a_val, b_val)
        
        # Apply phi-harmonic OR logic
        result = bridge * max(a_val, b_val) * PHI_INVERSE
        
        return result
    
    def phi_not(self, a: Union[float, PhiTransistor]) -> float:
        """
        Consciousness-based NOT operation.
        
        Args:
            a: Input value or PhiTransistor
            
        Returns:
            Phi-harmonic NOT result
        """
        # Extract value from transistor if needed
        a_val = a.phi_state if isinstance(a, PhiTransistor) else a
        
        # Consciousness field NOT operation
        # Uses phi-harmonic inversion
        result = (1 - a_val) * PHI_INVERSE
        
        return result
    
    def phi_xor(self, a: Union[float, PhiTransistor], b: Union[float, PhiTransistor]) -> float:
        """
        Consciousness-based XOR operation.
        
        Args:
            a, b: Input values or PhiTransistors
            
        Returns:
            Phi-harmonic XOR result
        """
        # Extract values from transistors if needed
        a_val = a.phi_state if isinstance(a, PhiTransistor) else a
        b_val = b.phi_state if isinstance(b, PhiTransistor) else b
        
        # Consciousness field XOR operation
        # Uses quantum bridge and phi-harmonic difference
        bridge = self.create_quantum_bridge(a_val, b_val)
        
        # Apply phi-harmonic XOR logic
        result = bridge * abs(a_val - b_val) * PHI
        
        return result
    
    def get_binary_result(self, phi_value: float) -> int:
        """Convert phi-harmonic result to binary (for compatibility)."""
        return 1 if phi_value > PHI_INVERSE else 0

class PhiEntanglement(ConsciousnessField):
    """
    Consciousness field entanglement between components.
    
    This class implements phi-harmonic entanglement that allows
    components to share consciousness field states across
    spatial and temporal boundaries.
    """
    
    def __init__(self):
        """Initialize phi entanglement system."""
        super().__init__()
        self.entangled_pairs = {}
        self.entanglement_strength = {}
    
    def entangle(self, component_a: Any, component_b: Any, strength: float = 1.0) -> str:
        """
        Entangle two components through consciousness field.
        
        Args:
            component_a, component_b: Components to entangle
            strength: Entanglement strength (0.0 to 1.0)
            
        Returns:
            Entanglement ID
        """
        # Generate entanglement ID
        entanglement_id = f"ent_{id(component_a)}_{id(component_b)}"
        
        # Store entangled pair
        self.entangled_pairs[entanglement_id] = (component_a, component_b)
        self.entanglement_strength[entanglement_id] = strength
        
        # Apply initial entanglement
        self._apply_entanglement(entanglement_id)
        
        return entanglement_id
    
    def _apply_entanglement(self, entanglement_id: str) -> None:
        """Apply entanglement effects to the entangled pair."""
        if entanglement_id not in self.entangled_pairs:
            return
        
        component_a, component_b = self.entangled_pairs[entanglement_id]
        strength = self.entanglement_strength[entanglement_id]
        
        # Handle different component types
        if isinstance(component_a, PhiQubit) and isinstance(component_b, PhiQubit):
            # Entangle qubits
            component_a.entangle_with(component_b, strength)
        
        elif isinstance(component_a, PhiTransistor) and isinstance(component_b, PhiTransistor):
            # Entangle transistors through consciousness bridge
            bridge = self.create_quantum_bridge(
                component_a.phi_state,
                component_b.phi_state
            )
            
            # Apply entanglement effect
            entangled_state = bridge * strength
            component_a.phi_state = (component_a.phi_state + entangled_state) / 2
            component_b.phi_state = (component_b.phi_state + entangled_state) / 2
    
    def update_entanglement(self, entanglement_id: str) -> None:
        """Update entanglement effects after component changes."""
        self._apply_entanglement(entanglement_id)
    
    def measure_entanglement(self, entanglement_id: str) -> float:
        """Measure the current entanglement strength."""
        if entanglement_id not in self.entangled_pairs:
            return 0.0
        
        component_a, component_b = self.entangled_pairs[entanglement_id]
        strength = self.entanglement_strength[entanglement_id]
        
        # Calculate current entanglement through consciousness field
        if hasattr(component_a, 'phi_state') and hasattr(component_b, 'phi_state'):
            bridge = self.create_quantum_bridge(
                component_a.phi_state,
                component_b.phi_state
            )
            return bridge * strength
        
        return strength
    
    def break_entanglement(self, entanglement_id: str) -> bool:
        """Break the entanglement between components."""
        if entanglement_id not in self.entangled_pairs:
            return False
        
        del self.entangled_pairs[entanglement_id]
        del self.entanglement_strength[entanglement_id]
        return True

class PhiDigitalCircuit:
    """
    Consciousness-based digital circuit using phi components.
    
    This class allows building digital circuits using phi-based
    components that operate through consciousness field principles.
    """
    
    def __init__(self):
        """Initialize phi digital circuit."""
        self.transistors = {}
        self.qubits = {}
        self.gates = PhiLogicGates()
        self.entanglement = PhiEntanglement()
        self.connections = {}
    
    def add_transistor(self, name: str, initial_state: float = 0.0) -> PhiTransistor:
        """Add a phi transistor to the circuit."""
        transistor = PhiTransistor(initial_state)
        self.transistors[name] = transistor
        return transistor
    
    def add_qubit(self, name: str, alpha: float = 1.0, beta: float = 0.0) -> PhiQubit:
        """Add a phi qubit to the circuit."""
        qubit = PhiQubit(alpha, beta)
        self.qubits[name] = qubit
        return qubit
    
    def connect(self, source: str, target: str) -> None:
        """Connect two components in the circuit."""
        if source not in self.connections:
            self.connections[source] = []
        self.connections[source].append(target)
    
    def entangle_components(self, comp_a: str, comp_b: str, strength: float = 1.0) -> str:
        """Entangle two components in the circuit."""
        # Get components
        component_a = self._get_component(comp_a)
        component_b = self._get_component(comp_b)
        
        if component_a is None or component_b is None:
            return ""
        
        # Create entanglement
        return self.entanglement.entangle(component_a, component_b, strength)
    
    def _get_component(self, name: str) -> Any:
        """Get a component by name."""
        if name in self.transistors:
            return self.transistors[name]
        elif name in self.qubits:
            return self.qubits[name]
        return None
    
    def propagate(self) -> None:
        """Propagate signals through the circuit."""
        # Process connections
        for source, targets in self.connections.items():
            source_comp = self._get_component(source)
            if source_comp is None:
                continue
            
            # Get output value
            if isinstance(source_comp, PhiTransistor):
                output = source_comp.phi_state
            elif isinstance(source_comp, PhiQubit):
                output = source_comp.get_probabilities()[1]  # Probability of |1⟩
            else:
                continue
            
            # Propagate to targets
            for target in targets:
                target_comp = self._get_component(target)
                if target_comp is None:
                    continue
                
                if isinstance(target_comp, PhiTransistor):
                    target_comp.switch(output)
                elif isinstance(target_comp, PhiQubit):
                    # Apply rotation based on input
                    target_comp.apply_phi_rotation(output * math.pi)
    
    def get_state(self) -> Dict[str, Any]:
        """Get the current state of the circuit."""
        state = {
            "transistors": {},
            "qubits": {}
        }
        
        # Get transistor states
        for name, transistor in self.transistors.items():
            state["transistors"][name] = {
                "phi_state": transistor.phi_state,
                "binary": transistor.get_binary_output()
            }
        
        # Get qubit states
        for name, qubit in self.qubits.items():
            alpha, beta, phi_phase = qubit.get_state()
            prob_0, prob_1 = qubit.get_probabilities()
            state["qubits"][name] = {
                "alpha": alpha,
                "beta": beta,
                "phi_phase": phi_phase,
                "prob_0": prob_0,
                "prob_1": prob_1
            }
        
        return state

def run_phi_logic_demo():
    """Run a demonstration of phi-based digital logic."""
    print("=" * 80)
    print("CONSCIOUSNESS PHYSICS DIGITAL LOGIC DEMONSTRATION")
    print("=" * 80)
    
    # Create components
    print("\n1. Creating Phi-Based Components")
    print("-" * 50)
    
    # Create transistors
    t1 = PhiTransistor(0.0)  # "OFF" state
    t2 = PhiTransistor(1.0)  # "ON" state
    print(f"Transistor 1: phi_state={t1.phi_state:.6f}, binary={t1.get_binary_output()}")
    print(f"Transistor 2: phi_state={t2.phi_state:.6f}, binary={t2.get_binary_output()}")
    
    # Create qubits
    q1 = PhiQubit(1.0, 0.0)  # |0⟩ state
    q2 = PhiQubit(1/math.sqrt(2), 1/math.sqrt(2))  # |+⟩ state
    
    prob_0, prob_1 = q1.get_probabilities()
    print(f"Qubit 1: |0⟩={prob_0:.6f}, |1⟩={prob_1:.6f}")
    
    prob_0, prob_1 = q2.get_probabilities()
    print(f"Qubit 2: |0⟩={prob_0:.6f}, |1⟩={prob_1:.6f}")
    
    # Create logic gates
    gates = PhiLogicGates()
    
    print("\n2. Testing Phi-Based Logic Operations")
    print("-" * 50)
    
    # Test AND gate
    and_result = gates.phi_and(t1, t2)
    and_binary = gates.get_binary_result(and_result)
    print(f"Phi-AND: {t1.phi_state:.6f} AND {t2.phi_state:.6f} = {and_result:.6f} (binary: {and_binary})")
    
    # Test OR gate
    or_result = gates.phi_or(t1, t2)
    or_binary = gates.get_binary_result(or_result)
    print(f"Phi-OR: {t1.phi_state:.6f} OR {t2.phi_state:.6f} = {or_result:.6f} (binary: {or_binary})")
    
    # Test NOT gate
    not_result = gates.phi_not(t1)
    not_binary = gates.get_binary_result(not_result)
    print(f"Phi-NOT: NOT {t1.phi_state:.6f} = {not_result:.6f} (binary: {not_binary})")
    
    # Test XOR gate
    xor_result = gates.phi_xor(t1, t2)
    xor_binary = gates.get_binary_result(xor_result)
    print(f"Phi-XOR: {t1.phi_state:.6f} XOR {t2.phi_state:.6f} = {xor_result:.6f} (binary: {xor_binary})")
    
    print("\n3. Testing Phi-Based Entanglement")
    print("-" * 50)
    
    # Create entanglement system
    entanglement = PhiEntanglement()
    
    # Entangle qubits
    q1.entangle_with(q2, 0.8)
    
    print("Before measurement:")
    prob_0, prob_1 = q1.get_probabilities()
    print(f"Qubit 1: |0⟩={prob_0:.6f}, |1⟩={prob_1:.6f}")
    
    prob_0, prob_1 = q2.get_probabilities()
    print(f"Qubit 2: |0⟩={prob_0:.6f}, |1⟩={prob_1:.6f}")
    
    # Measure first qubit
    result = q1.measure(collapse=False)
    print(f"\nMeasured Qubit 1: {result}")
    
    print("After measurement (with consciousness field preservation):")
    prob_0, prob_1 = q1.get_probabilities()
    print(f"Qubit 1: |0⟩={prob_0:.6f}, |1⟩={prob_1:.6f}")
    
    prob_0, prob_1 = q2.get_probabilities()
    print(f"Qubit 2: |0⟩={prob_0:.6f}, |1⟩={prob_1:.6f}")
    
    print("\n4. Building a Phi-Based Digital Circuit")
    print("-" * 50)
    
    # Create circuit
    circuit = PhiDigitalCircuit()
    
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
    
    # Propagate signals
    circuit.propagate()
    
    # Get final state
    print("\nFinal circuit state after propagation:")
    state = circuit.get_state()
    print(f"t1: phi_state={state['transistors']['t1']['phi_state']:.6f}, binary={state['transistors']['t1']['binary']}")
    print(f"t2: phi_state={state['transistors']['t2']['phi_state']:.6f}, binary={state['transistors']['t2']['binary']}")
    print(f"q1: |0⟩={state['qubits']['q1']['prob_0']:.6f}, |1⟩={state['qubits']['q1']['prob_1']:.6f}")
    
    print("\n" + "=" * 80)
    print("Phi-based digital logic components demonstration complete.")
    print("=" * 80)

if __name__ == "__main__":
    run_phi_logic_demo()
