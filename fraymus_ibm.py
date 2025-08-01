# import numpy as np
# import time

# # === Quantum Cortex Class ===
# class QuantumCortex:
#     def __init__(self, dimensions=3, layers=5):
#         self.dimensions = dimensions
#         self.layers = layers
#         self.state = self.initialize_state()
#         self.qwark_storage = []  # To store qwark-like structures

#     def initialize_state(self):
#         """ Initialize a multi-dimensional quantum state. """
#         return np.random.rand(self.dimensions, self.layers) + 1j * np.random.rand(self.dimensions, self.layers)

#     def evolve(self):
#         """ Evolve the quantum state using advanced transformations. """
#         for layer in range(self.layers):
#             self.state[:, layer] = self.harmonic_transformation(self.state[:, layer])
#             self.state[:, layer] = self.entangle(self.state[:, layer])
#         self.store_qwark()

#     def harmonic_transformation(self, psi):
#         """ Apply a harmonic transformation to the quantum state. """
#         H = np.diag(np.linspace(1, 2, len(psi)))  # Example Hamiltonian
#         return np.dot(np.exp(-1j * H * 0.01), psi)

#     def entangle(self, psi):
#         """ Apply a basic entanglement operation. """
#         # Simple example of entanglement (this can be made more complex)
#         entangled_state = np.zeros_like(psi)
#         for i in range(len(psi)):
#             entangled_state[i] = psi[i] * np.random.rand()  # Random entanglement
#         return entangled_state

#     def store_qwark(self):
#         """ Store the current state as a qwark-like structure. """
#         qwark_representation = {
#             'state': self.state.tolist(),
#             'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
#         }
#         self.qwark_storage.append(qwark_representation)

#     def get_qwark_storage(self):
#         """ Retrieve stored qwark representations. """
#         return self.qwark_storage

#     def dynamic_layer_management(self, new_layers):
#         """ Dynamically manage layers in the quantum cortex. """
#         self.layers = new_layers
#         self.state = self.initialize_state()  # Reinitialize state with new layers

# # === Fractal Qwark Class ===
# class FractalQwark:
#     def __init__(self, base_value=0.5, growth_rate=3.7, iterations=100):
#         self.base_value = base_value
#         self.growth_rate = growth_rate
#         self.iterations = iterations
#         self.values = self.generate_fractal()

#     def generate_fractal(self):
#         """ Generate a fractal sequence using logistic map dynamics. """
#         values = []
#         x = self.base_value
#         for _ in range(self.iterations):
#             x = self.growth_rate * x * (1 - x)
#             values.append(x)
#         return values

#     def get_qbits(self):
#         """ Convert fractal values to binary qbits. """
#         return [1 if v >= 0.5 else 0 for v in self.values]

# # === Main Quantum Cortex Initialization ===
# if __name__ == "__main__":
#     quantum_cortex = QuantumCortex(dimensions=3, layers=5)
#     for _ in range(10):  # Evolve the cortex for 10 iterations
#         quantum_cortex.evolve()

#     print("Quantum State Evolution Complete.")
#     print("Stored Qwark Representations:", quantum_cortex.get_qwark_storage())

import numpy as np
import time
from qiskit import QuantumCircuit, transpile
from qiskit.primitives import Sampler
from qiskit_ibm_provider import IBMProvider
from qiskit_aer import AerSimulator
import os

from qiskit_ibm_provider import IBMProvider
IBMProvider.save_account('I42a896e06f8ee0d49c5a92c457d13279d6c7c54e53362d6ddf24d974d5d344ba3efd36bf94ad5d9a036cefff0a901b14ed1240722445c92dd94486641bc846f9', overwrite=True)

# === Quantum Cortex Class ===
class QuantumCortex:
    def __init__(self, dimensions=3, layers=5):
        self.dimensions = dimensions
        self.layers = layers
        self.state = self.initialize_state()
        self.qwark_storage = []  # Storage for quantum structures ("qwarks")

    def initialize_state(self):
        """Initialize a complex multi-dimensional quantum state."""
        real_part = np.random.rand(self.dimensions, self.layers)
        imag_part = np.random.rand(self.dimensions, self.layers)
        return real_part + 1j * imag_part

    def evolve(self, timesteps=1, dt=0.01):
        """Evolve the quantum state through transformations and entanglement."""
        for t in range(timesteps):
            for layer in range(self.layers):
                self.state[:, layer] = self.harmonic_transformation(self.state[:, layer], dt)
                self.state[:, layer] = self.entangle(self.state[:, layer])
            self.store_qwark()
            print(f"Evolution step {t+1}/{timesteps} complete.")

    def harmonic_transformation(self, psi, dt):
        """Apply harmonic (Hamiltonian-based) evolution to the quantum state."""
        # Simplified Hamiltonian for demonstration (diagonal, linearly spaced)
        H = np.diag(np.linspace(1, 2, len(psi)))
        evolution_operator = np.exp(-1j * H * dt)
        return evolution_operator @ psi

    def entangle(self, psi):
        """Apply simplified entanglement (pairwise random correlations)."""
        entanglement_matrix = np.random.rand(len(psi), len(psi))
        entangled_state = entanglement_matrix @ psi
        # Normalize to maintain state integrity
        norm = np.linalg.norm(entangled_state)
        return entangled_state / norm if norm != 0 else entangled_state

    def store_qwark(self):
        """Store current quantum state ("qwark") with timestamp."""
        qwark_representation = {
            'state': self.state.tolist(),
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.qwark_storage.append(qwark_representation)

    def get_qwark_storage(self):
        """Retrieve all stored quantum states ("qwarks")."""
        return self.qwark_storage

    def dynamic_layer_management(self, new_layers):
        """Dynamically adjust quantum layers and reinitialize state."""
        self.layers = new_layers
        self.state = self.initialize_state()

# === Fractal Qwark Class ===
class FractalQwark:
    def __init__(self, base_value=0.5, growth_rate=3.7, iterations=100):
        self.base_value = base_value
        self.growth_rate = growth_rate
        self.iterations = iterations
        self.values = self.generate_fractal()

    def generate_fractal(self):
        """Generate fractal sequence via logistic map dynamics."""
        values = np.zeros(self.iterations)
        x = self.base_value
        for i in range(self.iterations):
            x = self.growth_rate * x * (1 - x)
            values[i] = x
        return values

    def get_qbits(self):
        """Convert fractal values to binary quantum bits (qbits)."""
        return (self.values >= 0.5).astype(int).tolist()

# === IBM QUANTUM INTEGRATION ===
class IBMQuantumInterface:
    """Interface for IBM Quantum Computer Integration"""
    
    def __init__(self, api_token=None):
        self.api_token = api_token or os.getenv('I42a896e06f8ee0d49c5a92c457d13279d6c7c54e53362d6ddf24d974d5d344ba3efd36bf94ad5d9a036cefff0a901b14ed1240722445c92dd94486641bc846f9')
        self.provider = None
        self.backend = None
        self.simulator = AerSimulator()  # Default to simulator if no connection
        self.initialize_connection()
    
    def initialize_connection(self):
        """Initialize connection to IBM Quantum Computer"""
        try:
            if self.api_token:
                IBMProvider.save_account(self.api_token, overwrite=True)
                self.provider = IBMProvider()
                # Get the least busy backend
                self.backend = self.provider.backends(simulator=False, operational=True)[0]
                print(f"✅ Connected to IBM Quantum Computer: {self.backend.name}")
            else:
                print("⚠️ No API token provided, using local simulator")
        except Exception as e:
            print(f"❌ Failed to connect to IBM Quantum: {str(e)}")
            print("⚠️ Using local simulator instead")
    
    def create_quantum_circuit(self, num_qubits, num_classical_bits):
        """Create a new quantum circuit"""
        return QuantumCircuit(num_qubits, num_classical_bits)
    
    def apply_quantum_gates(self, circuit, operations):
        """Apply quantum gates to the circuit
        
        Args:
            circuit (QuantumCircuit): The quantum circuit to modify
            operations (list): List of tuples (gate_type, qubit, params)
        """
        for gate_type, qubit, *params in operations:
            if gate_type == 'h':
                circuit.h(qubit)
            elif gate_type == 'x':
                circuit.x(qubit)
            elif gate_type == 'cx':
                circuit.cx(qubit, params[0])
            elif gate_type == 'measure':
                circuit.measure(qubit, params[0])
            elif gate_type == 'rx':
                circuit.rx(params[0], qubit)
            elif gate_type == 'ry':
                circuit.ry(params[0], qubit)
            elif gate_type == 'rz':
                circuit.rz(params[0], qubit)
    
    def run_circuit(self, circuit, shots=1024):
        """Run a quantum circuit on IBM Quantum Computer or simulator
        
        Args:
            circuit (QuantumCircuit): The quantum circuit to run
            shots (int): Number of shots (repetitions)
            
        Returns:
            dict: Results of the quantum computation
        """
        circuit.measure_all()  # Add measurements to all qubits
        
        try:
            if self.backend:
                # Transpile circuit for the backend
                transpiled_circuit = transpile(circuit, self.backend)
                # Create a sampler using the backend
                sampler = Sampler()
                # Run on the backend
                job = sampler.run(transpiled_circuit, shots=shots)
                result = job.result()
                # Convert result to counts format
                counts = result.quasi_dists[0]
                return {hex(int(k, 2)): v for k, v in counts.items()}
            else:
                # Run on simulator
                sampler = Sampler()
                job = sampler.run(circuit, shots=shots)
                result = job.result()
                # Convert result to counts format
                counts = result.quasi_dists[0]
                return {hex(int(k, 2)): v for k, v in counts.items()}
        except Exception as e:
            print(f"Error running circuit: {str(e)}")
            # Fallback to simulator
            try:
                sampler = Sampler()
                job = sampler.run(circuit, shots=shots)
                result = job.result()
                # Convert result to counts format
                counts = result.quasi_dists[0]
                return {hex(int(k, 2)): v for k, v in counts.items()}
            except Exception as e2:
                print(f"Simulator error: {str(e2)}")
                return {}
    
    def prepare_bell_state(self):
        """Prepare a Bell state (maximally entangled state)"""
        circuit = self.create_quantum_circuit(2, 2)
        operations = [
            ('h', 0),           # Hadamard on first qubit
            ('cx', 0, 1),       # CNOT with control=first, target=second
            ('measure', 0, 0),  # Measure both qubits
            ('measure', 1, 1)
        ]
        self.apply_quantum_gates(circuit, operations)
        return circuit

    def prepare_ghz_state(self, num_qubits):
        """Prepare a GHZ state (generalized Bell state for n qubits)"""
        circuit = self.create_quantum_circuit(num_qubits, num_qubits)
        
        # Apply Hadamard to first qubit
        operations = [('h', 0)]
        
        # Apply CNOT gates to entangle all qubits
        for i in range(num_qubits - 1):
            operations.append(('cx', i, i + 1))
            
        # Add measurement operations
        for i in range(num_qubits):
            operations.append(('measure', i, i))
            
        self.apply_quantum_gates(circuit, operations)
        return circuit

    def prepare_custom_state(self, angles):
        """Prepare a custom quantum state using rotation gates
        
        Args:
            angles (list): List of (theta, phi, lambda) angles for each qubit
        """
        num_qubits = len(angles)
        circuit = self.create_quantum_circuit(num_qubits, num_qubits)
        
        operations = []
        for i, (theta, phi, lambda_) in enumerate(angles):
            operations.extend([
                ('ry', i, theta),   # Rotation around Y-axis
                ('rz', i, phi),     # Rotation around Z-axis
                ('rx', i, lambda_)  # Rotation around X-axis
            ])
            
        # Add measurements
        for i in range(num_qubits):
            operations.append(('measure', i, i))
            
        self.apply_quantum_gates(circuit, operations)
        return circuit

# === Test Cases for Quantum Cortex and Fractal Qwark ===
def test_quantum_cortex():
    print("\nTesting QuantumCortex...")
    qc = QuantumCortex(dimensions=3, layers=4)
    qc.evolve(timesteps=5, dt=0.02)

    storage = qc.get_qwark_storage()
    assert len(storage) == 5, "Qwark storage should have 5 entries after evolution."
    print("QuantumCortex evolution and storage tests passed.")

def test_fractal_qwark():
    print("\nTesting FractalQwark...")
    fq = FractalQwark(base_value=0.4, growth_rate=3.9, iterations=50)
    qbits = fq.get_qbits()
    assert len(qbits) == 50, "Should generate 50 qbits."
    assert all(qbit in [0, 1] for qbit in qbits), "Qbits must be binary (0 or 1)."
    print("FractalQwark fractal generation and qbit tests passed.")

def test_ibm_quantum():
    """Test the IBM Quantum Interface"""
    print("\n=== Testing IBM Quantum Interface ===")
    
    # Create interface
    ibm_quantum_interface = IBMQuantumInterface()
    
    # Create a simple circuit
    circuit = ibm_quantum_interface.create_quantum_circuit(2, 2)
    
    # Apply some gates
    circuit.h(0)  # Hadamard gate on qubit 0
    circuit.cx(0, 1)  # CNOT gate with control qubit 0 and target qubit 1
    
    # Run the circuit
    results = ibm_quantum_interface.run_circuit(circuit)
    
    # Print results
    print(f"Circuit results: {results}")
    
    # Test Bell state
    bell_circuit = ibm_quantum_interface.prepare_bell_state()
    bell_results = ibm_quantum_interface.run_circuit(bell_circuit)
    print(f"Bell state results: {bell_results}")

# === Main Execution ===
if __name__ == "__main__":
    # Run tests
    test_quantum_cortex()
    test_fractal_qwark()
    test_ibm_quantum()

    # Example usage
    print("\nRunning Quantum Cortex Example:")
    quantum_cortex = QuantumCortex(dimensions=3, layers=5)
    quantum_cortex.evolve(timesteps=3)

    qwarks = quantum_cortex.get_qwark_storage()
    print(f"\nFinal Stored Qwarks ({len(qwarks)} total):")
    for idx, qwark in enumerate(qwarks, 1):
        print(f"{idx}: Timestamp: {qwark['timestamp']} State Snapshot: {qwark['state'][0][0]:.3f}...")

    print("\nRunning Fractal Qwark Example:")
    fractal_qwark = FractalQwark()
    qbits = fractal_qwark.get_qbits()
    print(f"First 10 Fractal Qbits: {qbits[:10]}")

    ibm_quantum_interface = IBMQuantumInterface()
    circuit = ibm_quantum_interface.create_quantum_circuit(2, 2)
    ibm_quantum_interface.apply_quantum_gates(circuit, [('h', 0), ('cx', 0, 1), ('measure', 0, 0), ('measure', 1, 1)])
    results = ibm_quantum_interface.run_circuit(circuit)
    print(f"Results: {results}")

    bell_state_circuit = ibm_quantum_interface.prepare_bell_state()
    ghz_state_circuit = ibm_quantum_interface.prepare_ghz_state(3)
    custom_state_circuit = ibm_quantum_interface.prepare_custom_state([(0.5, 0.2, 0.1), (0.3, 0.4, 0.6)])
    print("Prepared Bell State Circuit:", bell_state_circuit)
    print("Prepared GHZ State Circuit:", ghz_state_circuit)
    print("Prepared Custom State Circuit:", custom_state_circuit)
