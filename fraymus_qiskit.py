import numpy as np
import random
import matplotlib.pyplot as plt

# === REAL QUANTUM CORTEX CLASS ===
class QuantumCortex:
    def __init__(self, num_qubits=3, layers=5):
        self.num_qubits = num_qubits  # Number of qubits in circuit
        self.layers = layers  # Depth of quantum circuit
        self.state = self.initialize_state()  # Initialize quantum state
        self.measurements = []  # Store measurement results

    def initialize_state(self):
        """ Initialize a multi-dimensional quantum state. """
        return np.zeros((2 ** self.num_qubits,), dtype=complex)

    def apply_hadamard(self, qubit):
        """ Apply Hadamard gate to a specified qubit. """
        for i in range(2 ** self.num_qubits):
            if (i >> qubit) & 1:  # If the qubit is in state |1>
                self.state[i] = (self.state[i] + self.state[i ^ (1 << qubit)]) / np.sqrt(2)
            else:  # If the qubit is in state |0>
                self.state[i] = (self.state[i] - self.state[i ^ (1 << qubit)]) / np.sqrt(2)

    def apply_entanglement(self):
        """ Applies entanglement across all qubits using CNOT gates. """
        for i in range(self.num_qubits - 1):
            self.apply_cnot(i, i + 1)

    def apply_cnot(self, control, target):
        """ Apply CNOT gate with control and target qubits. """
        for i in range(2 ** self.num_qubits):
            if (i >> control) & 1:  # If control qubit is |1>
                self.state[i] = self.state[i ^ (1 << target)]  # Flip target qubit

    def apply_rotation_gates(self):
        """ Applies random quantum rotations (simulating quantum evolution). """
        for qubit in range(self.num_qubits):
            theta = np.random.uniform(0, 2 * np.pi)
            self.apply_rotation(qubit, theta)

    def apply_rotation(self, qubit, theta):
        """ Apply rotation around the Z-axis. """
        for i in range(2 ** self.num_qubits):
            if (i >> qubit) & 1:  # If the qubit is |1>
                self.state[i] *= np.exp(1j * theta)

    def measure(self):
        """ Measure the quantum state and store results. """
        probabilities = np.abs(self.state) ** 2
        outcome = np.random.choice(range(2 ** self.num_qubits), p=probabilities)
        self.measurements.append(outcome)

    def build_circuit(self):
        """ Builds the quantum circuit with gates and entanglement. """
        for _ in range(self.layers):
            for qubit in range(self.num_qubits):
                self.apply_hadamard(qubit)  # Apply Hadamard gates for superposition
            self.apply_entanglement()  # Apply entanglement
            self.apply_rotation_gates()  # Apply rotation gates
        self.measure()  # Measure qubits

    def run_simulation(self, shots=1024):
        """ Run the quantum circuit simulation for a number of shots. """
        for _ in range(shots):
            self.build_circuit()
        return self.measurements

    def visualize_results(self):
        """ Displays the histogram of measurement results. """
        counts = np.bincount(self.measurements, minlength=2 ** self.num_qubits)
        plt.bar(range(len(counts)), counts)
        plt.xlabel('Measurement Outcomes')
        plt.ylabel('Counts')
        plt.title('Quantum Measurement Results')
        plt.xticks(range(len(counts)))
        plt.show()

# === EXECUTE QUANTUM CORTEX ===
if __name__ == "__main__":
    quantum_cortex = QuantumCortex(num_qubits=3, layers=5)
    
    # Run simulation
    print("⚡ Running Quantum Simulation...")
    measurements = quantum_cortex.run_simulation(shots=1024)

    # Show measurement results
    print("📊 Measurement Results:", measurements)
    quantum_cortex.visualize_results()