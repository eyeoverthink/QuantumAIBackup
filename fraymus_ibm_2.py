import os
import sys
import json
import sqlite3
import numpy as np
import random
import hashlib
import requests
from flask import Flask, jsonify, request, send_from_directory
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from cryptography.fernet import Fernet
from bs4 import BeautifulSoup
from scipy.linalg import expm
import torch
import time

# Global Configuration
PHI = (1 + np.sqrt(5)) / 2  # Golden Ratio
RID_SIZE = 33  # Grid size

# Setup Flask app
app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = os.urandom(32)
app.config['JWT_SECRET_KEY'] = os.urandom(32)
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Encryption
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', Fernet.generate_key())
cipher = Fernet(ENCRYPTION_KEY)

# Database setup
DB_FILE = "fraymus_omega_fractal_storage.db"

class QuantumFractalDNANodularStorage:
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
        encrypted_dna = cipher.encrypt(dna_sequence.encode())
        self.cursor.execute(
            "INSERT INTO fractal_dna (node_id, dna_sequence, harmonic_key, dimension) VALUES (?, ?, ?, ?)",
            (node_id, encrypted_dna, harmonic_key, dimension)
        )
        self.conn.commit()

    def retrieve_dna(self, node_id, harmonic_key, dimension):
        self.cursor.execute(
            "SELECT dna_sequence FROM fractal_dna WHERE node_id = ? AND harmonic_key = ? AND dimension = ?",
            (node_id, harmonic_key, dimension)
        )
        encrypted_data = self.cursor.fetchall()
        if encrypted_data:
            return [cipher.decrypt(row[0]).decode() for row in encrypted_data]
        return None

# Quantum Harmonic Core
class QuantumHarmonicCore:
    def __init__(self):
        self.phase_accumulator = 0
        self.history = []

    def process_frequency(self, frequency):
        self.phase_accumulator += frequency
        self.history.append(self.phase_accumulator)
        harmonic_output = (self.phase_accumulator / PHI) % 1.0
        return harmonic_output

# Neural Node
class NodularNeuralNode:
    def __init__(self, weight=0.5):
        self.weight = weight
        self.state = 0

    def process_signal(self, input_signal):
        weighted_input = input_signal * self.weight
        self.state += weighted_input
        return self.state / PHI

# Neural Cortex
class DigitalNeuralCortex:
    def __init__(self):
        self.nodes = [NodularNeuralNode(random.uniform(0.1, 0.9)) for _ in range(RID_SIZE)]
        self.harmonic_core = QuantumHarmonicCore()

    def process_input(self, input_signal):
        node_outputs = [node.process_signal(input_signal) for node in self.nodes]
        harmonic_output = self.harmonic_core.process_frequency(random.choice([432, 528, 639]))
        return node_outputs, harmonic_output

# Flask routes
@app.route('/', methods=['GET'])
def index():
    """Return API information and documentation"""
    # Check if the request is for HTML
    if request.headers.get('Accept', '').find('text/html') != -1:
        return send_from_directory('static', 'index.html')
    
    # Otherwise return JSON
    return jsonify({
        "name": "Quantum Fractal API",
        "version": "1.0.0",
        "description": "API for Quantum Fractal Neural Processing",
        "endpoints": [
            {
                "path": "/process",
                "method": "POST",
                "description": "Process input data through the Digital Neural Cortex",
                "auth_required": True,
                "params": {
                    "data": "Input signal value (float or special value: 'pi', 'e', 'phi')"
                },
                "returns": {
                    "outputs": "Array of node outputs",
                    "harmonic": "Harmonic output value"
                }
            },
            {
                "path": "/token",
                "method": "POST",
                "description": "Generate authentication token",
                "auth_required": False,
                "params": {
                    "username": "Username for token generation"
                },
                "returns": {
                    "token": "JWT authentication token"
                }
            }
        ],
        "status": "online",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/process', methods=['POST'])
@jwt_required()
def process_request():
    try:
        # Get data from request, default to 0.5 if not provided
        data = request.json.get('data')
        
        # Check if data is None or not a number
        if data is None:
            return jsonify({"error": "No data provided"}), 400
            
        # Handle special values like 'pi'
        if isinstance(data, str):
            if data.lower() == 'pi':
                data = np.pi
            elif data.lower() == 'e':
                data = np.e
            elif data.lower() == 'phi':
                data = PHI
            else:
                try:
                    data = float(data)
                except ValueError:
                    return jsonify({"error": f"Invalid data value: {data}"}), 400
        
        # Convert to float for processing
        try:
            data_float = float(data)
        except (TypeError, ValueError):
            return jsonify({"error": f"Could not convert {data} to float"}), 400
            
        cortex = DigitalNeuralCortex()
        outputs, harmonic = cortex.process_input(data_float)
        return jsonify({"outputs": outputs, "harmonic": harmonic})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/token', methods=['POST'])
def generate_token():
    username = request.json.get('username')
    token = create_access_token(identity=username)
    return jsonify({"token": token})

# Main execution
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5051, debug=False)
