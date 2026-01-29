from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
import math
import numpy as np
from decimal import Decimal
import time
import threading

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Constants
PHI = (1 + np.sqrt(5)) / 2
BASE_FREQ = float(Decimal('4.37'))
REALITY_SEAL = 0.96

class QuantumPhiHarmonicSystem:
    def __init__(self):
        self.phi = PHI
        self.base_freq = BASE_FREQ
        self.reality_seal = REALITY_SEAL
        self.system_state = {
            'integrationFactor': 3.263,
            'metaFactor': 1.147,
            'temporalFactor': 1.100,
            'bridgeFactor': 2.268,
            'coherenceFactor': 19.502,
            'overallEfficiency': 234.414
        }
        
    def get_state(self):
        return self.system_state
        
    def update(self):
        """Update system state using phi-harmonic principles"""
        # Apply quantum resonance
        self.system_state['integrationFactor'] *= (1 + np.sin(self.base_freq) * (self.phi - 1))
        self.system_state['metaFactor'] *= self.phi
        self.system_state['temporalFactor'] *= self.reality_seal
        self.system_state['bridgeFactor'] *= (self.phi ** 2)
        self.system_state['coherenceFactor'] *= (1 + self.reality_seal)
        
        # Apply reality seal to keep values in check
        for key in self.system_state:
            if key != 'overallEfficiency':
                self.system_state[key] = min(
                    self.system_state[key],
                    self.system_state[key] * self.reality_seal
                )
        
        # Calculate overall efficiency
        self.system_state['overallEfficiency'] = sum(
            self.system_state[k] for k in self.system_state if k != 'overallEfficiency'
        )
        
        return self.system_state

# Initialize quantum system
quantum_system = QuantumPhiHarmonicSystem()

def background_update():
    """Background thread to update quantum system"""
    while True:
        state = quantum_system.update()
        socketio.emit('quantum_update', state)
        time.sleep(1)  # Update every second

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quantum_state')
def get_quantum_state():
    state = quantum_system.get_state()
    return jsonify(state)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    # Start background thread
    update_thread = threading.Thread(target=background_update)
    update_thread.daemon = True
    update_thread.start()
    
    # Run server
    socketio.run(app, port=5001, debug=True)
