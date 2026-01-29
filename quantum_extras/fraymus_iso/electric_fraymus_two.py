import os
import json
import numpy as np
import sqlite3
from flask import Flask, request, jsonify, render_template, send_from_directory
import traceback
from json import JSONEncoder
import math
from scipy.linalg import expm
from typing import List, Tuple, Dict
import time
from collections import defaultdict
import cmath

class ComplexEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {'real': obj.real, 'imag': obj.imag}
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

class NumpyEncoder(json.JSONEncoder):
    """Custom JSON encoder for numpy types"""
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
            np.int16, np.int32, np.int64, np.uint8,
            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
            return float(obj)
        elif isinstance(obj, (np.complex_, np.complex64, np.complex128)):
            return {'real': float(obj.real), 'imag': float(obj.imag)}
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

# Quantum Framework
class QuantumCircuit:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=complex)
        self.state[0] = 1.0  # Initialize to |0⟩
        
        # Quantum gates
        self._H = 1/np.sqrt(2) * np.array([[1, 1], [1, -1]], dtype=complex)
        self._X = np.array([[0, 1], [1, 0]], dtype=complex)
        self._Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
        self._Z = np.array([[1, 0], [0, -1]], dtype=complex)
        self._CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)

    def apply_gate(self, gate: np.ndarray, target: int, control: int = None):
        """Apply a quantum gate to the target qubit(s)"""
        dim = 2**self.num_qubits
        if control is not None:
            # Controlled operation
            ctrl_gate = np.eye(dim, dtype=complex)
            ctrl_mask = 1 << control
            for i in range(dim):
                if i & ctrl_mask:
                    # Apply gate only when control qubit is |1⟩
                    tgt_mask = 1 << target
                    if i & tgt_mask:
                        j = i ^ tgt_mask  # Flip target bit
                        ctrl_gate[i][j] = gate[1][0]
                        ctrl_gate[j][i] = gate[0][1]
            self.state = ctrl_gate @ self.state
        else:
            # Single qubit operation
            gate_full = np.eye(dim, dtype=complex)
            for i in range(0, dim, 2):
                if i & (1 << target):
                    gate_full[i:i+2, i:i+2] = gate
            self.state = gate_full @ self.state

    def hadamard(self, qubit: int):
        """Apply Hadamard gate"""
        self.apply_gate(self._H, qubit)

    def pauli_x(self, qubit: int):
        """Apply Pauli-X gate (NOT)"""
        self.apply_gate(self._X, qubit)

    def pauli_y(self, qubit: int):
        """Apply Pauli-Y gate"""
        self.apply_gate(self._Y, qubit)

    def pauli_z(self, qubit: int):
        """Apply Pauli-Z gate"""
        self.apply_gate(self._Z, qubit)

    def cnot(self, control: int, target: int):
        """Apply CNOT gate"""
        self.apply_gate(self._CNOT, target, control)

    def rx(self, qubit: int, theta: float):
        """Apply rotation around X axis"""
        gate = expm(-1j * theta/2 * self._X)
        self.apply_gate(gate, qubit)

    def ry(self, qubit: int, theta: float):
        """Apply rotation around Y axis"""
        gate = expm(-1j * theta/2 * self._Y)
        self.apply_gate(gate, qubit)

    def rz(self, qubit: int, theta: float):
        """Apply rotation around Z axis"""
        gate = expm(-1j * theta/2 * self._Z)
        self.apply_gate(gate, qubit)

    def measure(self) -> List[float]:
        """Measure the quantum state"""
        probabilities = np.abs(self.state) ** 2
        return probabilities.tolist()

class ElectricalBrain:
    def __init__(self):
        self.num_neurons = 8
        self.weights = None
        self.memory_bank = {}
        self.attention_weights = np.ones(16) / 16
        self.learning_rate = 0.1
        self.memory_decay = 0.99
        self.pattern_threshold = 0.6

    def initialize_weights(self, input_size):
        """Initialize weights with improved Xavier initialization"""
        self.weights = np.random.randn(self.num_neurons, input_size) * np.sqrt(2.0 / input_size)
        
    def sigmoid(self, x):
        """Numerically stable sigmoid"""
        return np.where(x >= 0, 
                       1 / (1 + np.exp(-x)),
                       np.exp(x) / (1 + np.exp(x)))

    def update_memory(self, pattern, response):
        """Update memory bank with new patterns"""
        pattern_key = hash(str(pattern))
        if pattern_key in self.memory_bank:
            self.memory_bank[pattern_key]['count'] += 1
            self.memory_bank[pattern_key]['last_seen'] = time.time()
            # Increase confidence with repeated patterns
            self.memory_bank[pattern_key]['confidence'] = min(
                0.9,
                self.memory_bank[pattern_key]['confidence'] + 0.1
            )
        else:
            # Initialize with higher base confidence
            self.memory_bank[pattern_key] = {
                'pattern': pattern,
                'response': response,
                'count': 1,
                'last_seen': time.time(),
                'confidence': 0.3  # Higher initial confidence
            }
        
        # Decay old memories but keep high-confidence patterns
        current_time = time.time()
        for key in list(self.memory_bank.keys()):
            time_diff = current_time - self.memory_bank[key]['last_seen']
            if time_diff > 3600:  # 1 hour
                if self.memory_bank[key]['confidence'] > 0.7:
                    # Slower decay for high-confidence patterns
                    self.memory_bank[key]['confidence'] *= 0.95
                else:
                    self.memory_bank[key]['confidence'] *= self.memory_decay
                    if self.memory_bank[key]['confidence'] < 0.01:
                        del self.memory_bank[key]

    def update_attention(self, input_pattern):
        """Update attention weights based on input importance"""
        pattern_norm = np.linalg.norm(input_pattern)
        if pattern_norm > 0:
            # Calculate importance based on pattern matching
            importance = np.abs(input_pattern) / pattern_norm
            
            # Boost attention for recognized patterns
            for pattern_info in self.memory_bank.values():
                stored_pattern = np.array(pattern_info['pattern'])
                if len(stored_pattern) == len(input_pattern):
                    similarity = np.exp(-np.sum((stored_pattern - input_pattern) ** 2))
                    importance *= (1 + similarity * pattern_info['confidence'])
            
            # Update attention weights with momentum
            self.attention_weights = 0.8 * self.attention_weights + 0.2 * importance
            self.attention_weights /= np.sum(self.attention_weights)

    def hebbian_learning(self, pre_synaptic, post_synaptic):
        """Implement hebbian learning with homeostatic plasticity"""
        delta_w = np.outer(post_synaptic, pre_synaptic)
        # Homeostatic normalization
        delta_w -= np.mean(delta_w)
        delta_w /= (np.std(delta_w) + 1e-8)
        return self.learning_rate * delta_w

    def analyze(self, quantum_state):
        """Analyze quantum state with enhanced pattern recognition"""
        if self.weights is None:
            self.initialize_weights(len(quantum_state))

        # Convert quantum state to real vector
        state_vector = np.array([complex(s['real'], s['imag']) for s in quantum_state])
        input_pattern = np.abs(state_vector)
        
        # Apply attention mechanism
        self.update_attention(input_pattern)
        weighted_input = input_pattern * self.attention_weights
        
        # Neural processing
        activations = self.sigmoid(np.dot(self.weights, weighted_input))
        
        # Pattern matching
        pattern_confidence = 0.1  # Base confidence
        memory_utilization = len(self.memory_bank) / 1000  # Arbitrary max size
        
        # Check for known patterns
        pattern_key = hash(str(input_pattern))
        if pattern_key in self.memory_bank:
            pattern_match = self.memory_bank[pattern_key]
            pattern_confidence = pattern_match['confidence']
            pattern_confidence = min(0.9, pattern_confidence + 0.1)  # Increase confidence with repeated matches
            self.memory_bank[pattern_key]['confidence'] = pattern_confidence
        
        # Update weights through hebbian learning
        delta_weights = self.hebbian_learning(weighted_input, activations)
        self.weights += delta_weights
        
        # Calculate electrical properties
        voltage = np.mean(activations) * 10  # Scale to reasonable voltage
        current = np.sum(np.abs(delta_weights)) * 1e-18  # Scale to quantum regime
        resistance = voltage / (current + 1e-30)  # Prevent division by zero
        power = voltage * current
        
        return {
            'activation_levels': activations.tolist(),
            'voltage': voltage,
            'current': current,
            'resistance': resistance,
            'power': power,
            'synaptic_strength': np.mean(self.weights, axis=1).tolist(),
            'pattern_confidence': pattern_confidence,
            'attention_distribution': self.attention_weights.tolist(),
            'memory_utilization': memory_utilization
        }

    def process_query(self, query):
        """Process a query through the quantum circuit and provide meaningful answers"""
        # Convert query to quantum state
        num_qubits = min(4, len(query) // 4 + 2)
        qc = QuantumCircuit(num_qubits)
        
        # Apply quantum operations based on query characteristics
        for i, char in enumerate(query):
            angle = (ord(char) % 10) * np.pi / 10
            qubit = i % num_qubits
            
            if char.isupper():
                qc.hadamard(qubit)
            elif char.isdigit():
                qc.pauli_x(qubit)
            elif char in '.?!':
                qc.pauli_z(qubit)
            
            qc.rx(qubit, angle)
            qc.ry(qubit, angle * 0.5)
            qc.rz(qubit, angle * 0.25)
            
            if i > 0:
                qc.cnot(qubit, (qubit + 1) % num_qubits)

        # Get quantum state
        state = qc.state
        state_list = [{'real': float(x.real), 'imag': float(x.imag)} for x in state]
        
        # Process through electrical brain and fractal DNA
        fractal_storage = FractalDNA().store(state)
        
        # Update memory with query pattern
        query_pattern = np.array([ord(c) for c in query.lower()]) / 255.0
        self.update_memory(query_pattern.tolist(), None)
        
        # Get electrical analysis with updated memory
        electrical_analysis = self.analyze(state_list)
        
        # Generate meaningful response based on query type and brain state
        query_lower = query.lower()
        
        # Get learning metrics with improved confidence
        pattern_confidence = electrical_analysis.get('pattern_confidence', 0)
        memory_utilization = len(self.memory_bank) / 1000.0
        
        # Advanced quantum concepts handling with context
        if "error" in query_lower and "correction" in query_lower:
            answer = {
                "explanation": "Quantum error correction protects quantum states through redundant encoding.",
                "techniques": [
                    "Surface codes",
                    "Stabilizer measurements",
                    "Syndrome detection",
                    "Fault-tolerant operations"
                ],
                "key_concepts": {
                    "redundancy": "Encode logical qubit across multiple physical qubits",
                    "measurement": "Indirect syndrome measurement preserves quantum state",
                    "correction": "Apply corrective operations based on syndrome"
                },
                "challenges": [
                    "Overhead of additional qubits",
                    "Fast error detection required",
                    "Balance between correction and decoherence"
                ]
            }
        elif "entanglement" in query_lower and "superposition" in query_lower:
            answer = {
                "explanation": "Quantum computing leverages both superposition and entanglement for computational advantage.",
                "key_concepts": {
                    "superposition": {
                        "definition": "Quantum bits exist in multiple states simultaneously",
                        "impact": "Enables parallel processing of multiple states",
                        "mathematical_form": "|ψ⟩ = α|0⟩ + β|1⟩"
                    },
                    "entanglement": {
                        "definition": "Quantum correlation between multiple qubits",
                        "impact": "Allows quantum algorithms to process related information",
                        "mathematical_form": "|Φ+⟩ = (|00⟩ + |11⟩)/√2"
                    }
                },
                "performance_implications": [
                    "Superposition enables exponential state space exploration",
                    "Entanglement allows quantum parallelism",
                    "Combined effect enables quantum speedup",
                    "Key to algorithms like Shor's and Grover's"
                ],
                "limitations": [
                    "Decoherence affects both superposition and entanglement",
                    "Measurement collapses quantum states",
                    "Error correction needed for stability"
                ]
            }
        elif "algorithm" in query_lower:
            if "shor" in query_lower:
                answer = {
                    "explanation": "Shor's algorithm achieves exponential speedup through quantum period finding.",
                    "components": [
                        "Quantum Fourier Transform for period detection",
                        "Modular exponentiation in superposition",
                        "Continued fraction expansion"
                    ],
                    "complexity": {
                        "quantum": "O((log N)³)",
                        "classical": "O(exp(log N^(1/3)))",
                        "speedup": "Exponential"
                    },
                    "implementation": {
                        "register_size": "2n + 1 qubits for n-bit number",
                        "circuit_depth": "O(n³) gates",
                        "measurement": "Probabilistic with bounded error"
                    }
                }
            elif "grover" in query_lower:
                answer = {
                    "explanation": "Grover's algorithm achieves quadratic speedup for unstructured search.",
                    "components": [
                        "State preparation in uniform superposition",
                        "Oracle query for solution marking",
                        "Amplitude amplification",
                        "Optimal measurement timing"
                    ],
                    "complexity": "O(√N) vs classical O(N)",
                    "applications": [
                        "Database search",
                        "Optimization problems",
                        "SAT solving",
                        "Quantum machine learning"
                    ]
                }
        else:
            answer = {
                "explanation": "Processing quantum computation query.",
                "quantum_analysis": {
                    "circuit_size": f"Circuit contains {num_qubits} qubits",
                    "operations": "Applied gates include Hadamard, CNOT, and rotations",
                    "state_complexity": f"Hilbert space dimension: {2**num_qubits}"
                }
            }

        # Add enhanced learning metrics
        answer["learning_metrics"] = {
            "pattern_confidence": f"{pattern_confidence:.2%}",
            "memory_utilization": f"{memory_utilization:.2%}",
            "circuit_analysis": f"Using {num_qubits} qubits, depth {num_qubits * 2}",
            "attention_focus": f"Primary attention weight: {max(electrical_analysis['attention_distribution']):.2%}"
        }

        return {
            "query": query,
            "quantum_state": state_list,
            "fractal_dna": fractal_storage,
            "electrical_brain": electrical_analysis,
            "response": answer
        }

class FractalDNA:
    def __init__(self):
        self.fractal_depth = 2
        self.encoding_dim = 4

    def generate_fractal(self, data: np.ndarray, depth: int) -> List:
        if depth == 0 or len(data) < 2:
            return data
        
        mid = len(data) // 2
        left = self.generate_fractal(data[:mid], depth - 1)
        right = self.generate_fractal(data[mid:], depth - 1)
        
        # Create fractal pattern with quantum entanglement
        pattern = []
        for i in range(2):
            row = []
            for j in range(2):
                if (i + j) % 2 == 0:
                    row.append(left)
                else:
                    row.append(right)
            pattern.append(row)
        return pattern

    def store(self, quantum_state: np.ndarray) -> List:
        # Encode quantum state into fractal DNA structure
        encoded_data = quantum_state[:self.encoding_dim]
        return self.generate_fractal(encoded_data, self.fractal_depth)

# Database
class QuantumDB:
    def __init__(self, db_path="quantum.db"):
        self.db_path = db_path
        self.encoder = ComplexEncoder()
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS quantum_blocks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                query TEXT,
                                quantum_state TEXT,
                                fractal_dna TEXT,
                                electrical_brain TEXT)''')

    def save_block(self, query, quantum_state, fractal_dna, electrical_brain):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''INSERT INTO quantum_blocks (query, quantum_state, fractal_dna, electrical_brain)
                            VALUES (?, ?, ?, ?)''',
                         (query, 
                          json.dumps(quantum_state, cls=ComplexEncoder),
                          json.dumps(fractal_dna, cls=ComplexEncoder),
                          json.dumps(electrical_brain)))

# Flask API
app = Flask(__name__)
app.json_encoder = NumpyEncoder  # Use our custom encoder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/process', methods=['POST'])
def process():
    """Process a quantum query and return results
    
    Handles numpy array serialization by converting all arrays to lists
    and complex numbers to dictionaries with real/imag parts.
    """
    try:
        data = request.get_json()
        brain = ElectricalBrain()
        result = brain.process_query(data['query'])
        
        def serialize_numpy(obj):
            if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                np.int16, np.int32, np.int64, np.uint8,
                np.uint16, np.uint32, np.uint64)):
                return int(obj)
            elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
                return float(obj)
            elif isinstance(obj, (np.complex_, np.complex64, np.complex128)):
                return {'real': float(obj.real), 'imag': float(obj.imag)}
            elif isinstance(obj, np.ndarray):
                return [serialize_numpy(x) for x in obj]
            elif isinstance(obj, dict):
                return {k: serialize_numpy(v) for k, v in obj.items()}
            elif isinstance(obj, (list, tuple)):
                return [serialize_numpy(x) for x in obj]
            return obj
        
        # Serialize the entire response
        serialized_response = serialize_numpy(result)
        return json.dumps(serialized_response), 200, {'Content-Type': 'application/json'}
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Try different ports if 5011 is in use
    port = 5011
    max_port = 5020  # Maximum port to try
    
    while port <= max_port:
        try:
            app.run(host='0.0.0.0', port=port, debug=True)
            break
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"Port {port} is in use, trying {port + 1}")
                port += 1
            else:
                raise e
    
    if port > max_port:
        print("Could not find an available port between 5011 and 5020")