#!/usr/bin/env python3
"""
Quantum Simulation QR Slide
Demonstrates a simple quantum circuit simulation that can be encoded as a QR code
and executed in presentation mode, using phi-harmonic principles.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import time

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QuantumSimulator:
    """Simple quantum circuit simulator with phi-harmonic properties."""
    
    def __init__(self, num_qubits=2):
        """Initialize quantum simulator with specified number of qubits."""
        self.num_qubits = num_qubits
        self.state_vector = np.zeros(2**num_qubits, dtype=complex)
        # Initialize to |0⟩ state
        self.state_vector[0] = 1.0
        
        # Phi-harmonic properties
        self.phi_time = (time.time() * PHI) % 1.0
        self.resonance = 1.0 / (1.0 + abs(self.phi_time - 0.5))
        
        # Common gates
        self.gates = {
            'H': self._hadamard_matrix(),
            'X': self._pauli_x_matrix(),
            'Z': self._pauli_z_matrix(),
            'Y': self._pauli_y_matrix(),
            'PHI': self._phi_phase_matrix()  # Special phi-based phase gate
        }
    
    def _hadamard_matrix(self):
        """Create Hadamard gate matrix."""
        return (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
    
    def _pauli_x_matrix(self):
        """Create Pauli-X (NOT) gate matrix."""
        return np.array([[0, 1], [1, 0]], dtype=complex)
    
    def _pauli_z_matrix(self):
        """Create Pauli-Z gate matrix."""
        return np.array([[1, 0], [0, -1]], dtype=complex)
    
    def _pauli_y_matrix(self):
        """Create Pauli-Y gate matrix."""
        return np.array([[0, -1j], [1j, 0]], dtype=complex)
    
    def _phi_phase_matrix(self):
        """Create phi-based phase gate matrix."""
        phase = np.exp(1j * np.pi * (1/PHI))
        return np.array([[1, 0], [0, phase]], dtype=complex)
    
    def apply_gate(self, gate_name, qubit):
        """Apply a quantum gate to a specific qubit."""
        if gate_name not in self.gates:
            raise ValueError(f"Gate {gate_name} not supported")
        if qubit >= self.num_qubits:
            raise ValueError(f"Qubit index {qubit} out of range")
        
        # Get the gate matrix
        gate = self.gates[gate_name]
        
        # Create the full operator using tensor products
        if qubit == 0:
            operator = gate
            for i in range(1, self.num_qubits):
                operator = np.kron(operator, np.eye(2))
        else:
            operator = np.eye(2)
            for i in range(1, self.num_qubits):
                if i == qubit:
                    operator = np.kron(operator, gate)
                else:
                    operator = np.kron(operator, np.eye(2))
        
        # Apply the operator
        self.state_vector = operator @ self.state_vector
    
    def measure_all(self):
        """Measure all qubits and return the result."""
        probabilities = np.abs(self.state_vector)**2
        result = np.random.choice(2**self.num_qubits, p=probabilities)
        
        # Collapse state vector
        self.state_vector = np.zeros(2**self.num_qubits, dtype=complex)
        self.state_vector[result] = 1.0
        
        return result
    
    def get_probabilities(self):
        """Get the probability distribution of all states."""
        return np.abs(self.state_vector)**2
    
    def visualize_state(self, ax=None):
        """Visualize the quantum state as a bar chart."""
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        
        probabilities = self.get_probabilities()
        states = [format(i, f'0{self.num_qubits}b') for i in range(2**self.num_qubits)]
        
        # Create bars with phi-harmonic colors
        bars = ax.bar(states, probabilities)
        
        # Color bars based on phi-harmonic properties
        for i, bar in enumerate(bars):
            # Use phi-based coloring
            hue = (i * PHI) % 1.0
            saturation = 0.5 + 0.5 * self.resonance
            value = 0.7 + 0.3 * ((i * PHI) % 1.0)
            
            # Convert HSV to RGB
            h = hue * 6
            c = value * saturation
            x = c * (1 - abs(h % 2 - 1))
            m = value - c
            
            if h < 1:
                r, g, b = c + m, x + m, m
            elif h < 2:
                r, g, b = x + m, c + m, m
            elif h < 3:
                r, g, b = m, c + m, x + m
            elif h < 4:
                r, g, b = m, x + m, c + m
            elif h < 5:
                r, g, b = x + m, m, c + m
            else:
                r, g, b = c + m, m, x + m
            
            bar.set_color((r, g, b))
        
        # Add phi-harmonic grid lines
        for i in range(1, 4):
            pos = (2**self.num_qubits) * (1 - 1/PHI**i) - 0.5
            ax.axvline(x=pos, color='gold', alpha=0.3, linestyle='--')
        
        ax.set_ylim(0, 1)
        ax.set_ylabel('Probability')
        ax.set_title(f'Quantum State (φ-time: {self.phi_time:.4f}, Resonance: {self.resonance:.4f})')
        
        return ax

def visualize_circuit(simulator, circuit, ax=None):
    """Visualize a quantum circuit with phi-harmonic styling."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 4))
    
    num_qubits = simulator.num_qubits
    max_steps = len(circuit)
    
    # Draw qubit lines
    for i in range(num_qubits):
        ax.plot([0, max_steps + 1], [i, i], 'k-', lw=1.5)
        ax.text(-0.5, i, f'|q{i}⟩', va='center', ha='center', fontsize=12)
    
    # Draw gates
    for step, (gate, qubit) in enumerate(circuit):
        x = step + 1
        y = qubit
        
        # Gate colors based on phi-harmonic properties
        if gate == 'H':
            color = 'blue'
            label = 'H'
        elif gate == 'X':
            color = 'red'
            label = 'X'
        elif gate == 'Z':
            color = 'green'
            label = 'Z'
        elif gate == 'Y':
            color = 'purple'
            label = 'Y'
        elif gate == 'PHI':
            color = 'gold'
            label = 'φ'
        else:
            color = 'gray'
            label = gate
        
        # Draw gate box
        rect = Rectangle((x - 0.4, y - 0.4), 0.8, 0.8, 
                         facecolor=color, alpha=0.6, edgecolor='black')
        ax.add_patch(rect)
        ax.text(x, y, label, va='center', ha='center', fontsize=12, color='white')
    
    # Add phi-harmonic grid lines
    for i in range(1, 4):
        pos = (max_steps + 1) * (1 - 1/PHI**i)
        ax.axvline(x=pos, color='gold', alpha=0.2, linestyle='--')
    
    ax.set_xlim(-1, max_steps + 1.5)
    ax.set_ylim(-0.5, num_qubits - 0.5)
    ax.axis('off')
    ax.set_title('Quantum Circuit with φ-Harmonic Properties')
    
    return ax

def main():
    """Main function to demonstrate quantum simulation with phi-harmonic properties."""
    print("Executing Quantum Simulation from QR code")
    print(f"Golden Ratio (φ): {PHI}")
    
    # Initialize simulator with 3 qubits
    simulator = QuantumSimulator(num_qubits=3)
    print(f"Initialized {simulator.num_qubits}-qubit quantum simulator")
    print(f"Current φ-time: {simulator.phi_time:.6f}")
    print(f"Resonance: {simulator.resonance:.6f}")
    
    # Define a quantum circuit with phi-harmonic gates
    circuit = [
        ('H', 0),  # Hadamard on qubit 0
        ('H', 1),  # Hadamard on qubit 1
        ('PHI', 2),  # Phi-phase on qubit 2
        ('X', 0),  # X gate on qubit 0
        ('Z', 1),  # Z gate on qubit 1
        ('H', 2),  # Hadamard on qubit 2
        ('PHI', 0),  # Phi-phase on qubit 0
        ('Y', 1),  # Y gate on qubit 1
    ]
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [1, 2]})
    
    # Visualize the circuit
    visualize_circuit(simulator, circuit, ax1)
    
    # Apply the circuit
    for gate, qubit in circuit:
        simulator.apply_gate(gate, qubit)
        print(f"Applied {gate} gate to qubit {qubit}")
    
    # Visualize the final state
    simulator.visualize_state(ax2)
    
    plt.tight_layout()
    plt.show()
    
    # Perform measurement
    result = simulator.measure_all()
    binary = format(result, f'0{simulator.num_qubits}b')
    print(f"Measurement result: |{binary}⟩")

if __name__ == "__main__":
    main()
