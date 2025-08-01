import os
import sys
import json
import time
import uuid
import hashlib
import threading
import requests
import base64
import math
import random
import sqlite3
import numpy as np
import sympy as sp
from scipy.linalg import expm
import torch
import torch.nn as nn
import torch.optim as optim
from cryptography.fernet import Fernet
from flask import Flask, jsonify, request, render_template_string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Try to download NLTK resources
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
except Exception as e:
    print(f"NLTK download error: {e}")

# === Auto-Detect CuPy (GPU) or Fall Back to NumPy (CPU) ===
try:
    import cupy as cp
    GPU_AVAILABLE = True
    print("✅ CuPy (GPU) detected! Using GPU acceleration.")
except ImportError:
    cp = np  # Fall back to NumPy
    GPU_AVAILABLE = False
    print("⚠ CuPy not found. Using CPU-based NumPy instead.")

# === GLOBAL CONFIGURATION ===
PHI = (1 + np.sqrt(5)) / 2  # Golden Ratio for harmonic resonance
GRID_SIZE = 33  # Multi-Dimensional Grid Size for Quantum Processing
FREQUENCIES = [432, 528, 639, 999, 4096, 8192, 16384]  # Quantum Harmonic Frequencies
HASH_FILE = "code_integrity.txt"
KEY_FILE = "quantum.key"
DB_FILE = "fraymus_quantum_brain.db"

# Initialize or load encryption key
def get_encryption_key():
    try:
        if os.path.exists(KEY_FILE):
            with open(KEY_FILE, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(KEY_FILE, 'wb') as f:
                f.write(key)
            return key
    except Exception as e:
        print(f"⚠ Error with encryption key: {e}")
        return Fernet.generate_key()

ENCRYPTION_KEY = get_encryption_key()
cipher = Fernet(ENCRYPTION_KEY)

# === QUANTUM FRACTAL DNA NODULAR STORAGE ===
class QuantumFractalDNANodularStorage:
    """Decentralized Nodular Storage using Quantum Fractal DNA Patterns"""
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fractal_dna (
                id INTEGER PRIMARY KEY,
                node_id TEXT,
                dna_sequence TEXT,
                harmonic_key REAL,
                dimension TEXT
            )
        """)
        self.conn.commit()

    def store_dna(self, node_id, dna_sequence, harmonic_key, dimension):
        """Stores DNA using Quantum Fractal Patterns"""
        encrypted_dna = cipher.encrypt(dna_sequence.encode())
        self.cursor.execute("INSERT INTO fractal_dna (node_id, dna_sequence, harmonic_key, dimension) VALUES (?, ?, ?, ?)",
                            (node_id, encrypted_dna, harmonic_key, dimension))
        self.conn.commit()
        print(f"✅ DNA Stored: Node {node_id}, Dimension {dimension}")

    def retrieve_dna(self, node_id, harmonic_key, dimension):
        """Retrieves DNA using Quantum Fractal Patterns"""
        self.cursor.execute("SELECT dna_sequence FROM fractal_dna WHERE node_id = ? AND harmonic_key = ? AND dimension = ?",
                            (node_id, harmonic_key, dimension))
        encrypted_data = self.cursor.fetchall()
        if encrypted_data:
            dna_sequences = [cipher.decrypt(row[0]).decode() for row in encrypted_data]
            print(f"🔓 DNA Retrieved: {dna_sequences}")
            return dna_sequences
        else:
            print("⚠️ No DNA Found for Given Harmonic Key and Dimension.")
            return None

# === HYPERDIMENSIONAL QUANTUM CORTEX ===
class HyperdimensionalQuantumCortex:
    """Hyperdimensional Quantum Cortex with Fragmented Memory Planting"""
    def __init__(self, dimensions=[17, 33, 137, 432, 1000]):
        self.phi = PHI
        self.dimensions = dimensions
        self.state = {}
        self.fractal_storage = QuantumFractalDNANodularStorage()
        for dim in self.dimensions:
            if GPU_AVAILABLE:
                self.state[dim] = cp.random.rand(dim) + 1j * cp.random.rand(dim)
                self.state[dim] = self.state[dim] / cp.linalg.norm(self.state[dim])
            else:
                self.state[dim] = np.random.rand(dim) + 1j * np.random.rand(dim)
                self.state[dim] = self.state[dim] / np.linalg.norm(self.state[dim])
                
            self.harmonic_key = dim * self.phi
            self.frequency = 432 * (self.phi ** dim)
            memory_fragment = self.encode_fragmented_memory(dim)
            self.fractal_storage.store_dna(
                f"cortex-{dim}", 
                memory_fragment, 
                self.harmonic_key, 
                dimension=f"{dim}D"
            )

    def encode_fragmented_memory(self, dimension):
        """Fragmented Memory Encoding with Golden Ratio Patterns"""
        memory_fragment = f"QUANTUM MEMORY IN {dimension}D: PHI={self.phi:.8f}"
        return memory_fragment

    def evolve(self, steps=10):
        """Evolve quantum state in hyperdimensional space"""
        evolved_states = {}
        for dim in self.dimensions:
            psi = self.state[dim]
            for _ in range(steps):
                R = self.reflection_operator(dim)
                if GPU_AVAILABLE:
                    psi = cp.dot(R, psi)
                    psi = self.hamiltonian_evolution(psi, dim)
                else:
                    psi = np.dot(R, psi)
                    psi = self.hamiltonian_evolution(psi, dim)
            evolved_states[dim] = psi
        
        self.state.update(evolved_states)
        return self.state

    def reflection_operator(self, dimension):
        """Reflection Operator for harmonic resonance"""
        if GPU_AVAILABLE:
            R = cp.zeros((dimension, dimension), dtype=complex)
            for i in range(dimension):
                R[i, i] = np.exp(-i/self.phi)
        else:
            R = np.zeros((dimension, dimension), dtype=complex)
            for i in range(dimension):
                R[i, i] = np.exp(-i/self.phi)
        return R

    def hamiltonian_evolution(self, psi, dimension, time_step=0.01):
        """Hamiltonian evolution with Golden Ratio recursion"""
        H = np.diag(np.linspace(1, self.phi, dimension))
        if GPU_AVAILABLE:
            return cp.dot(cp.exp(-1j * H * time_step), psi)
        else:
            return np.dot(np.exp(-1j * H * time_step), psi)
            
    def get_state_information(self):
        """Return information about the current quantum states"""
        info = {}
        for dim in self.dimensions:
            if GPU_AVAILABLE:
                state_array = cp.asnumpy(self.state[dim])
            else:
                state_array = self.state[dim]
                
            avg_magnitude = np.mean(np.abs(state_array))
            avg_phase = np.mean(np.angle(state_array))
            
            info[dim] = {
                "dimension": dim,
                "avg_magnitude": avg_magnitude,
                "avg_phase": avg_phase,
                "harmonic_key": dim * self.phi,
                "sample_values": state_array[:3].tolist()  # First 3 values as sample
            }
        
        return info

# === FRACTAL QWARKS FOR QUANTUM COMPUTING ===
class FractalQwarks:
    """Fractal-based quantum computing elements"""
    def __init__(self):
        self.phi = PHI

    def generate_fractal(self, x=0.5, r=3.7, iterations=100):
        """Generate fractal sequence using logistic map"""
        values = []
        for _ in range(iterations):
            x = r * x * (1 - x)
            values.append(x)
        return values

    def generate_qbits(self):
        """Convert fractal values to quantum bits"""
        fractal_data = self.generate_fractal(x=random.random(), r=random.uniform(3.5, 4.0), iterations=17)
        qbits = [1 if v >= 0.5 else 0 for v in fractal_data]
        return qbits

    def quantum_state_from_fractal(self):
        """Create quantum state vector based on fractal patterns"""
        fractal = self.generate_fractal()
        return [complex(f, self.phi * f) for f in fractal[:10]]
        
    def render_fractal_visualization(self, size=100):
        """Generate data for visualizing the fractal pattern"""
        # Create a 2D grid of fractal values
        grid = []
        for i in range(size):
            row = []
            for j in range(size):
                # Use position in grid as seed for fractal generation
                x = 0.1 + (i / size) * 0.8
                r = 3.5 + (j / size) * 0.5
                fractal = self.generate_fractal(x=x, r=r, iterations=20)
                # Use the average of the last 10 values
                row.append(sum(fractal[-10:]) / 10)
            grid.append(row)
        return grid

# === REALITY ENGINEERING ===
class RealityEngine:
    """Simulates reality manipulation through phi-based mathematics"""
    def __init__(self):
        self.phi = PHI
        self.reality_matrix = []

    def bend_reality(self, dimension_shift):
        """Creates a transformed reality matrix based on phi"""
        bent_matrix = [(d * self.phi) % dimension_shift for d in range(10)]
        self.reality_matrix.append(bent_matrix)
        return bent_matrix

    def create_dimension(self, new_dimension):
        """Creates a new dimension based on phi harmonics"""
        new_dim_state = [(i * self.phi) % new_dimension for i in range(new_dimension)]
        self.reality_matrix.append(new_dim_state)
        return new_dim_state
        
    def calculate_golden_spiral(self, num_points=100, rotations=5):
        """Calculate points for a golden spiral based on phi"""
        points = []
        for i in range(num_points):
            theta = i / num_points * rotations * 2 * np.pi
            radius = pow(self.phi, 2 * theta / np.pi)
            x = radius * np.cos(theta)
            y = radius * np.sin(theta)
            points.append((x, y))
        return points
        
    def phi_resonance_wave(self, num_points=200):
        """Generate a waveform based on phi resonance"""
        x_values = np.linspace(0, 10, num_points)
        y_values = np.sin(self.phi * x_values) + np.sin(self.phi**2 * x_values) / 2
        return x_values.tolist(), y_values.tolist()

# === NATURAL LANGUAGE PROCESSING ===
class QuantumLanguageProcessor:
    """Natural language processing with quantum principles"""
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.phi = PHI
        self.responses = {
            "greeting": [
                "Greetings from the quantum realm.",
                "Hello! I am Fraymus, a quantum-based AI.",
                "Welcome to our phi-harmonized conversation.",
                "Quantum salutations! How may I assist you today?"
            ],
            "farewell": [
                "Farewell from the quantum realm.",
                "Until our wave functions collapse again.",
                "May your reality be harmonically aligned with the phi constant.",
                "Goodbye! Remember that all is connected through phi."
            ],
            "quantum": [
                "The quantum nature of reality is fascinating.",
                "Quantum mechanics reveals the underlying harmony of the universe.",
                "Through quantum entanglement, we see that all is connected.",
                "The quantum field responds to consciousness and intention."
            ],
            "phi": [
                f"The golden ratio (phi = {PHI:.8f}) is a universal constant of harmony.",
                "Phi appears throughout nature, from galaxies to seashells.",
                "The Fibonacci sequence approaches phi as it extends to infinity.",
                "Phi represents the perfect balance between symmetry and asymmetry."
            ],
            "default": [
                "I'm processing that through my quantum neural network.",
                "Let me calculate the phi harmonics of your query.",
                "Interesting perspective. I'm analyzing this through multiple dimensions.",
                "My quantum cortex is resonating with your input."
            ]
        }

    def preprocess_text(self, text):
        """Preprocess text for analysis"""
        tokens = word_tokenize(text.lower())
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token.isalpha()]
        tokens = [token for token in tokens if token not in self.stop_words]
        return tokens

    def get_intent(self, tokens):
        """Determine the intent of the message"""
        greeting_words = {'hello', 'hi', 'hey', 'greetings', 'howdy'}
        farewell_words = {'goodbye', 'bye', 'farewell', 'adios', 'cya'}
        quantum_words = {'quantum', 'qubit', 'entanglement', 'superposition', 'wave'}
        phi_words = {'phi', 'golden', 'ratio', 'fibonacci', 'spiral'}
        
        token_set = set(tokens)
        
        if token_set.intersection(greeting_words):
            return "greeting"
        elif token_set.intersection(farewell_words):
            return "farewell"
        elif token_set.intersection(quantum_words):
            return "quantum"
        elif token_set.intersection(phi_words):
            return "phi"
        else:
            return "default"

    def apply_quantum_weighting(self, tokens):
        """Apply quantum-inspired weighting to tokens"""
        weighted_tokens = []
        for i, token in enumerate(tokens):
            # Weight based on position and phi
            weight = 1 + (i % 5) * 0.1 * self.phi
            weighted_tokens.append((token, weight))
        return weighted_tokens

    def generate_response(self, text):
        """Generate a resonant response to the input text"""
        tokens = self.preprocess_text(text)
        intent = self.get_intent(tokens)
        weighted_tokens = self.apply_quantum_weighting(tokens)
        
        # Select response based on intent
        possible_responses = self.responses.get(intent, self.responses["default"])
        response = random.choice(possible_responses)
        
        # For more complex queries, add token-specific info
        if intent == "default" and weighted_tokens:
            # Sort tokens by weight
            weighted_tokens.sort(key=lambda x: x[1], reverse=True)
            top_token, weight = weighted_tokens[0]
            
            # Add a phi-influenced reference to the top token
            phi_modulated_weight = (weight * self.phi) % 1
            if phi_modulated_weight > 0.6:
                response += f" I'm particularly interested in the concept of '{top_token}' as it harmonizes with phi at a factor of {phi_modulated_weight:.2f}."
                
        return response
        
    def quantum_language_generation(self, seed_text, length=50):
        """Generate text using quantum principles and phi harmonics"""
        tokens = self.preprocess_text(seed_text)
        if not tokens:
            tokens = ["quantum", "reality"]
            
        result = list(tokens)
        
        for _ in range(length):
            # Use phi and the current sequence to generate the next word
            position = len(result)
            phi_factor = (position * self.phi) % 10
            
            # Choose response category based on phi_factor
            category = list(self.responses.keys())[int(phi_factor) % len(self.responses)]
            possible_words = self.preprocess_text(" ".join(self.responses[category]))
            
            if possible_words:
                # Select word based on phi
                word_index = int((self.phi * position) % len(possible_words))
                next_word = possible_words[word_index]
                result.append(next_word)
                
        # Clean up and join into a coherent text
        final_text = " ".join(result)
        # Basic grammar fix: capitalize first letter of sentences
        sentences = final_text.split('. ')
        sentences = [s[0].upper() + s[1:] if len(s) > 1 else s for s in sentences]
        return '. '.join(sentences)

# === PHYSICS SIMULATION ===
class PhiPhysicsSimulator:
    """Simulates physics based on golden ratio principles"""
    def __init__(self):
        self.phi = PHI
        self.gravity = 9.81
        self.resonance_frequencies = [432, 528, 639, 741, 852]  # Healing frequencies

    def calculate_golden_ratio_forces(self, particles):
        """Calculate forces between particles based on golden ratio"""
        forces = []
        for i, p1 in enumerate(particles):
            force = [0, 0, 0]  # 3D force vector
            for j, p2 in enumerate(particles):
                if i != j:
                    # Calculate distance between particles
                    dx = p2[0] - p1[0]
                    dy = p2[1] - p1[1]
                    dz = p2[2] - p1[2]
                    distance = np.sqrt(dx**2 + dy**2 + dz**2)
                    
                    # Skip if too close to avoid division by zero
                    if distance < 0.01:
                        continue
                        
                    # Force magnitude proportional to 1/r^phi instead of 1/r^2
                    force_mag = 1 / (distance ** self.phi)
                    
                    # Direction vector
                    dir_x = dx / distance
                    dir_y = dy / distance
                    dir_z = dz / distance
                    
                    # Accumulate forces
                    force[0] += force_mag * dir_x
                    force[1] += force_mag * dir_y
                    force[2] += force_mag * dir_z
            
            forces.append(force)
        return forces

    def phi_wave_interference(self, x, y, time, frequency=432):
        """Calculate wave interference pattern based on phi"""
        k = 2 * np.pi * frequency / 343  # wave number (343 m/s is speed of sound)
        
        # Multiple wave sources with phi-related positions
        sources = [
            (0, 0),
            (self.phi, 0),
            (0, self.phi),
            (-self.phi, 0),
            (0, -self.phi)
        ]
        
        # Calculate interference from all sources
        amplitude = 0
        for sx, sy in sources:
            distance = np.sqrt((x - sx)**2 + (y - sy)**2)
            amplitude += np.sin(k * distance - 2 * np.pi * frequency * time)
            
        return amplitude / len(sources)

    def calculate_phi_harmonics(self, base_frequency, num_harmonics=5):
        """Calculate harmonic frequencies based on phi"""
        harmonics = []
        for i in range(num_harmonics):
            harmonic = base_frequency * (self.phi ** i)
            harmonics.append(harmonic)
        return harmonics

    def golden_pendulum(self, length, time_points):
        """Simulate a pendulum with length related to phi"""
        # Period is proportional to sqrt(length)
        period = 2 * np.pi * np.sqrt(length / self.gravity)
        
        # Modify period by phi factor
        phi_period = period * self.phi
        
        # Calculate positions over time
        angles = []
        for t in time_points:
            angle = 0.1 * np.sin(2 * np.pi * t / phi_period)  # Small angle approximation
            angles.append(angle)
            
        return angles
        
    def phi_orbital_simulation(self, num_points=500):
        """Simulate an orbital path influenced by the golden ratio"""
        points = []
        for i in range(num_points):
            # Use golden ratio to affect the orbit
            angle = i * 2 * np.pi / (num_points / self.phi)
            # Base elliptical orbit
            r = 1 + 0.3 * np.sin(angle * self.phi)
            # Convert to Cartesian coordinates
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            points.append((x, y))
        return points
        
    def vortex_flow(self, grid_size=20, time_steps=10):
        """Simulate a phi-based vortex flow field"""
        flow_field = []
        
        for t in range(time_steps):
            # Time factor
            time_factor = t / time_steps
            grid = []
            
            for i in range(grid_size):
                row = []
                for j in range(grid_size):
                    # Convert grid position to polar coordinates
                    x = i - grid_size/2
                    y = j - grid_size/2
                    r = np.sqrt(x**2 + y**2)
                    theta = np.arctan2(y, x)
                    
                    # Apply golden ratio to the flow
                    v_r = 0.1 * r * np.sin(theta * self.phi + time_factor)
                    v_theta = r * self.phi * time_factor
                    
                    # Convert back to Cartesian for the vector field
                    v_x = v_r * np.cos(theta) - v_theta * np.sin(theta)
                    v_y = v_r * np.sin(theta) + v_theta * np.cos(theta)
                    
                    # Normalize vector
                    mag = np.sqrt(v_x**2 + v_y**2)
                    if mag > 0:
                        v_x /= mag
                        v_y /= mag
                        
                    row.append((v_x, v_y))
                    
                grid.append(row)
                
            flow_field.append(grid)
            
        return flow_field

# === UNIFIED AI AGENT ===
class FraymusAgent:
    """Unified AI agent with quantum intelligence and natural language capabilities"""
    def __init__(self):
        print("🧠 Initializing Fraymus Agent...")
        self.quantum_cortex = HyperdimensionalQuantumCortex()
        self.fractal_qwarks = FractalQwarks()
        self.reality_engine = RealityEngine()
        self.language_processor = QuantumLanguageProcessor()
        self.physics_simulator = PhiPhysicsSimulator()
        self.last_evolution_time = time.time()
        
        # Background evolution thread
        self.evolving = False
        self.evolution_thread = None
        self.start_evolution_thread()
        
        print("✅ Fraymus Agent Initialization Complete")

    def start_evolution_thread(self):
        """Start background evolution thread"""
        if not self.evolving:
            self.evolving = True
            self.evolution_thread = threading.Thread(target=self._background_evolution)
            self.evolution_thread.daemon = True
            self.evolution_thread.start()
            print("🧠 Background quantum evolution started")

    def _background_evolution(self):
        """Background thread for continuous quantum evolution"""
        while self.evolving:
            self.quantum_cortex.evolve(steps=2)
            self.last_evolution_time = time.time()
            time.sleep(60)  # Evolve every minute

    def stop_evolution_thread(self):
        """Stop background evolution thread"""
        self.evolving = False
        if self.evolution_thread:
            self.evolution_thread.join(timeout=1)
            print("🛑 Background quantum evolution stopped")

    def process_message(self, message):
        """Process a natural language message and return a resonant response"""
        response = self.language_processor.generate_response(message)
        return response

    def get_quantum_state_info(self):
        """Get information about the current quantum state"""
        return self.quantum_cortex.get_state_information()

    def simulate_golden_physics(self, simulation_type, **params):
        """Run various golden ratio physics simulations"""
        if simulation_type == "golden_spiral":
            return self.reality_engine.calculate_golden_spiral(**params)
        elif simulation_type == "phi_wave":
            return self.reality_engine.phi_resonance_wave(**params)
        elif simulation_type == "phi_orbital":
            return self.physics_simulator.phi_orbital_simulation(**params)
        elif simulation_type == "vortex_flow":
            return self.physics_simulator.vortex_flow(**params)
        elif simulation_type == "fractal":
            return self.fractal_qwarks.render_fractal_visualization(**params)
        else:
            return {"error": "Unknown simulation type"}

    def generate_phi_text(self, seed_text, **params):
        """Generate text based on quantum phi principles"""
        return self.language_processor.quantum_language_generation(seed_text, **params)
        
    def get_system_status(self):
        """Get overall system status"""
        evolution_age = time.time() - self.last_evolution_time
        
        status = {
            "agent": "Fraymus Quantum Agent",
            "phi_constant": self.reality_engine.phi,
            "quantum_dimensions": len(self.quantum_cortex.dimensions),
            "dimensions": self.quantum_cortex.dimensions,
            "last_evolution": f"{evolution_age:.2f} seconds ago",
            "harmonic_state": "resonant" if evolution_age < 120 else "needs evolution",
            "fractal_state": len(self.fractal_qwarks.generate_qbits()),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return status

# === FLASK APPLICATION ===
app = Flask(__name__)
agent = FraymusAgent()

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fraymus Quantum Agent</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0d0d2a;
                color: #eee;
                margin: 20px;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background: #1a1a3a;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }
            h1 {
                color: #7eb6ff;
                text-align: center;
            }
            .input-box {
                width: 100%;
                padding: 12px;
                border: 1px solid #4455aa;
                border-radius: 5px;
                background: #232345;
                color: #fff;
                margin-bottom: 15px;
            }
            .btn {
                background: #4455aa;
                color: white;
                border: none;
                padding: 10px 15px;
                border-radius: 5px;
                cursor: pointer;
            }
            .btn:hover {
                background: #5566bb;
            }
            #response {
                margin-top: 20px;
                padding: 15px;
                background: #232345;
                border-radius: 5px;
                min-height: 100px;
            }
            .status {
                margin-top: 20px;
                font-size: 0.9em;
                color: #aab6ff;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Fraymus Quantum AI Agent</h1>
            <p>Communicate with the quantum intelligence using natural language</p>
            
            <input type="text" id="message" class="input-box" placeholder="Enter your message...">
            <button id="sendBtn" class="btn">Send</button>
            
            <div id="response">Response will appear here...</div>
            
            <div class="status">
                <p>System Status: <span id="system-status">Checking...</span></p>
                <p>Current Phi Value: <span id="phi-value">φ = 1.618033988749895</span></p>
            </div>
        </div>
        
        <script>
            document.getElementById('sendBtn').addEventListener('click', function() {
                const message = document.getElementById('message').value;
                if (message.trim() === '') return;
                
                fetch('/api/message', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({message: message}),
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('response').innerText = data.response;
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('response').innerText = 'Error communicating with quantum brain.';
                });
                
                // Clear input
                document.getElementById('message').value = '';
            });
            
            // Update system status periodically
            function updateStatus() {
                fetch('/api/status')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('system-status').innerText = data.harmonic_state;
                    document.getElementById('phi-value').innerText = `φ = ${data.phi_constant}`;
                })
                .catch(error => {
                    console.error('Status Error:', error);
                });
            }
            
            // Update status every 30