import os
import json
import numpy as np
import pennylane as qml
import sqlite3
import matplotlib
matplotlib.use('Agg')  # Use Agg backend instead of interactive backend
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, render_template, send_from_directory
from transformers import pipeline
import traceback

# Quantum device initialization
dev = qml.device("default.qubit", wires=8)

# Flask setup
app = Flask(__name__)
nlp_model = pipeline('text-generation', model='gpt2')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                             'favicon.ico', mimetype='image/vnd.microsoft.icon')

class QuantumAI:
    def __init__(self, db_path="quantum_genesis.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Drop existing table to handle schema changes
        cursor.execute('DROP TABLE IF EXISTS genesis_blocks')
        
        # Create table with new schema
        cursor.execute('''CREATE TABLE genesis_blocks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            query TEXT,
                            quantum_state TEXT,
                            classical_physics TEXT,
                            relativity_metrics TEXT,
                            fractal_dna TEXT,
                            electrical_state TEXT
                          )''')
        conn.commit()
        conn.close()

    def quantum_circuit(self, inputs):
        for i in range(len(inputs)):
            qml.RX(inputs[i], wires=i)
            qml.RY(inputs[i] * np.pi, wires=i)

        for i in range(len(inputs)-1):
            qml.CNOT(wires=[i, i+1])

        return [qml.expval(qml.PauliZ(i)) for i in range(len(inputs))]

    def physics_calculations(self, mass, velocity):
        c = 3e8  # Speed of light
        kinetic_energy = 0.5 * mass * velocity**2
        force = mass * velocity
        relativistic_mass = mass / np.sqrt(1 - (velocity**2 / c**2))
        energy_equivalence = relativistic_mass * c**2

        return {
            "kinetic_energy": kinetic_energy,
            "force": force,
            "relativistic_mass": relativistic_mass,
            "energy_equivalence": energy_equivalence
        }

    def fractal_dna_storage(self, data, depth=3):
        if depth == 0:
            return data
        else:
            return [self.fractal_dna_storage(data, depth-1), self.fractal_dna_storage(data[::-1], depth-1)]

    def electrical_brain_processing(self, quantum_state):
        # Constants
        electron_charge = 1.602176634e-19  # Coulombs
        electron_mass = 9.1093837015e-31  # kg
        
        # Calculate electrical properties based on quantum state
        voltage = np.mean(np.abs(quantum_state)) * 100  # Scale for better visualization
        current = np.sum(np.abs(quantum_state)) * electron_charge
        resistance = voltage / (current + 1e-10)  # Add small value to avoid division by zero
        power = voltage * current
        
        # Neural activation
        activation = 1 / (1 + np.exp(-np.array(quantum_state)))  # Sigmoid activation
        synaptic_strength = np.diff(activation)  # Measure of neural connections
        
        return {
            "electrical_properties": {
                "voltage": float(voltage),
                "current": float(current),
                "resistance": float(resistance),
                "power": float(power),
                "electron_flow": float(current / electron_charge)
            },
            "neural_properties": {
                "activation_levels": activation.tolist(),
                "synaptic_strength": synaptic_strength.tolist(),
                "neural_energy": float(np.sum(activation * voltage))
            }
        }

    def process_query(self, query):
        np.random.seed(len(query))
        mass = np.random.uniform(1e-31, 1e-25)
        velocity = np.random.uniform(1e4, 2.99e8)

        quantum_inputs = np.random.uniform(0, np.pi, 8)
        quantum_state = qml.QNode(self.quantum_circuit, dev)(quantum_inputs)

        physics_results = self.physics_calculations(mass, velocity)
        electrical_results = self.electrical_brain_processing(quantum_state)
        fractal_dna = self.fractal_dna_storage(quantum_state)

        genesis_block = {
            "quantum_state": quantum_state,
            "classical_physics": physics_results,
            "relativity_metrics": {
                "speed_of_light": 3e8,
                "mass": mass,
                "velocity": velocity
            },
            "electrical_brain": electrical_results,
            "fractal_dna": fractal_dna
        }

        self.save_genesis_block(query, genesis_block)
        filename = self.visualize_quantum_state(quantum_state, query)
        return genesis_block

    def save_genesis_block(self, query, genesis_block):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Check if electrical_state column exists
            cursor.execute("PRAGMA table_info(genesis_blocks)")
            columns = [col[1] for col in cursor.fetchall()]
            
            if 'electrical_state' not in columns:
                # Add the column if it doesn't exist
                cursor.execute('ALTER TABLE genesis_blocks ADD COLUMN electrical_state TEXT')
                conn.commit()
            
            cursor.execute('''INSERT INTO genesis_blocks (
                                query, quantum_state, classical_physics, 
                                relativity_metrics, fractal_dna, electrical_state
                            ) VALUES (?, ?, ?, ?, ?, ?)''',
                           (query,
                            json.dumps(genesis_block["quantum_state"]),
                            json.dumps(genesis_block["classical_physics"]),
                            json.dumps(genesis_block["relativity_metrics"]),
                            json.dumps(genesis_block["fractal_dna"]),
                            json.dumps(genesis_block.get("electrical_brain", {}))))
            conn.commit()
        except Exception as e:
            print(f"Database error: {e}")
            traceback.print_exc()
        finally:
            conn.close()

    def visualize_quantum_state(self, quantum_state, query):
        try:
            plt.figure(figsize=(10, 4))
            plt.bar(range(len(quantum_state)), quantum_state, color='purple')
            plt.xlabel('Qubit Index')
            plt.ylabel('Expectation Value')
            plt.title(f'Quantum State Visualization for: "{query}"')
            plt.grid(True)
            
            # Save to static directory
            static_dir = os.path.join(os.path.dirname(__file__), 'static')
            os.makedirs(static_dir, exist_ok=True)
            filename = f"quantum_state_{hash(query)}.png"
            plt.savefig(os.path.join(static_dir, filename))
            plt.close()
            return filename
        except Exception as e:
            print(f"Visualization error: {e}")
            return None

quantum_ai = QuantumAI()

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/quantum/process', methods=['POST'])
def process_quantum_query():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"error": "Missing query parameter"}), 400
            
        query = data.get("query")
        result = quantum_ai.process_query(query)
        
        # Convert numpy arrays to lists for JSON serialization
        if isinstance(result.get('quantum_state'), np.ndarray):
            result['quantum_state'] = result['quantum_state'].tolist()
            
        response = {
            "status": "success",
            "query": query,
            "result": result,
            "nlp_response": nlp_model(query, max_length=50, num_return_sequences=1)[0]['generated_text']
        }
        return jsonify(response)
        
    except Exception as e:
        traceback.print_exc()  # Print full traceback for debugging
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

if __name__ == '__main__':
    # Create static directory if it doesn't exist
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(static_dir, exist_ok=True)
    
    app.run(host='0.0.0.0', port=5001, debug=True)