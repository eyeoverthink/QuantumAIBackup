import os
import json
import numpy as np
import pennylane as qml
import sqlite3
import matplotlib
matplotlib.use('Agg')  # Use Agg backend instead of interactive backend
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, render_template, send_from_directory, url_for
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import traceback
import jwt
import datetime
import uuid
from flask_cors import CORS
import torch
import torch.nn as nn
from deep_learning.models.moe_moa_core import MoEMoAModel, SelfEvolvingMoEMoA
from typing import Tuple

# Helper function to convert tensors to Python native types
def convert_to_serializable(obj):
    if hasattr(obj, 'tolist'):
        return obj.tolist()
    elif isinstance(obj, (np.integer, np.floating)):
        return float(obj)
    elif isinstance(obj, (list, tuple)):
        return [convert_to_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_to_serializable(value) for key, value in obj.items()}
    else:
        return obj

# Quantum device initialization
dev = qml.device("default.qubit", wires=8)

# Flask setup
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SECRET_KEY'] = 'quantum-secret-key-change-in-production'

# Use a more powerful language model
try:
    # Set device
    if torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
        
    # Try to load a more powerful model
    model_name = "gpt2-medium"  # Better than base gpt2, but still lightweight
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # Configure padding token
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
    model.config.pad_token_id = model.config.eos_token_id
    nlp_model = pipeline('text-generation', model=model_name, device=device if device != 'mps' else -1)
except Exception as e:
    print(f"Failed to load {model_name}, falling back to gpt2: {str(e)}")
    nlp_model = pipeline('text-generation', model='gpt2', device=device if device != 'mps' else -1)

# Function to get a focused response
def get_focused_response(query: str) -> str:
    # Check if query contains mathematical equations
    contains_math = any(symbol in query for symbol in ['∫', '∑', 'ψ', 'φ', 'π', '²', '√'])
    
    if contains_math:
        # For mathematical queries, use higher max_new_tokens and lower temperature
        prompt = f"Question: Analyze this mathematical expression: {query}\nAnswer: Here is the analysis:"
        response = nlp_model(prompt,
                           max_new_tokens=800,
                           num_return_sequences=1,
                           temperature=0.5,
                           top_p=0.95,
                           do_sample=True,
                           no_repeat_ngram_size=3)[0]['generated_text']
    else:
        # For regular queries, use standard parameters
        prompt = f"Question: {query}\nAnswer: Let me explain this clearly."
        response = nlp_model(prompt,
                           max_new_tokens=800,
                           num_return_sequences=1,
                           temperature=0.7,
                           top_p=0.9,
                           do_sample=True,
                           no_repeat_ngram_size=2)[0]['generated_text']
    
    # Extract just the answer part
    if "Answer:" in response:
        response = response.split("Answer:")[1].strip()
    return response

# Initialize MoE/MoA model - match input dimension with embeddings
moe_moa_model = MoEMoAModel(
    input_dim=1024,  # Match GPT2 embeddings
    hidden_dim=1024,
    output_dim=768,
    num_experts=8,
    num_attention_heads=8
).to(device)
evolving_model = SelfEvolvingMoEMoA(moe_moa_model)

class QuantumAI:
    def __init__(self, db_path="quantum_genesis.db"):
        self.db_path = db_path
        self.init_db()
        self.tokenizer = tokenizer
        self.moe_moa = evolving_model
        self.device = device
        
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Check if the table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='genesis_blocks'")
        table_exists = cursor.fetchone() is not None
        
        if not table_exists:
            # Create the table with all columns if it doesn't exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS genesis_blocks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            query TEXT,
                            quantum_state TEXT,
                            classical_physics TEXT,
                            relativity_metrics TEXT,
                            fractal_dna TEXT,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                            visualization_path TEXT
                          )''')
        else:
            # Check if visualization_path column exists
            try:
                cursor.execute("SELECT visualization_path FROM genesis_blocks LIMIT 1")
            except sqlite3.OperationalError:
                # Add the visualization_path column if it doesn't exist
                cursor.execute("ALTER TABLE genesis_blocks ADD COLUMN visualization_path TEXT")
                
            # Check if timestamp column exists
            try:
                cursor.execute("SELECT timestamp FROM genesis_blocks LIMIT 1")
            except sqlite3.OperationalError:
                # Add the timestamp column if it doesn't exist
                cursor.execute("ALTER TABLE genesis_blocks ADD COLUMN timestamp DATETIME DEFAULT CURRENT_TIMESTAMP")
        
        conn.commit()
        conn.close()

    def get_history(self, limit=10):
        """Retrieve query history with results"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''SELECT id, query, quantum_state, classical_physics, 
                          relativity_metrics, timestamp, visualization_path 
                          FROM genesis_blocks ORDER BY timestamp DESC LIMIT ?''', (limit,))
        rows = cursor.fetchall()
        conn.close()
        
        history = []
        for row in rows:
            history.append({
                "id": row[0],
                "query": row[1],
                "quantum_state": json.loads(row[2]),
                "classical_physics": json.loads(row[3]),
                "relativity_metrics": json.loads(row[4]),
                "timestamp": row[5],
                "visualization_url": f"/static/{os.path.basename(row[6])}" if row[6] else None
            })
        
        return history

    def quantum_circuit(self, inputs):
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        
        @qml.qnode(dev)
        def circuit(inputs):
            # Initialize GHZ-like state with phi-resonance
            for i in range(len(inputs)):
                qml.RX(inputs[i] * phi * np.tanh(inputs[i]), wires=i)
                qml.RY(inputs[i] * np.pi * np.cos(inputs[i]), wires=i)
                qml.RZ(inputs[i] * phi * np.pi * np.exp(-inputs[i]**2/2), wires=i)
            
            # Create W-state-like entanglement
            for i in range(len(inputs)):
                for j in range(i+1, len(inputs)):
                    qml.CNOT(wires=[i, j])
                    qml.CRZ(phi * np.pi * np.tanh(inputs[i]), wires=[i, j])
                    qml.CRX(np.pi/2 * np.exp(-inputs[i]**2/2), wires=[i, j])
            
            # Apply cluster state stabilizers
            for i in range(len(inputs)):
                qml.Hadamard(wires=i)
                for j in range(max(0, i-1), min(len(inputs), i+2)):
                    if i != j:
                        phase = phi * np.pi/2 * np.exp(-inputs[i]**2/2)
                        qml.ControlledPhaseShift(phase, wires=[i, j])
                        qml.CZ(wires=[i, j])
            
            # Create multi-qubit entanglement
            for i in range(len(inputs)):
                qml.Hadamard(wires=i)
                if i > 0:
                    # Cyclic entanglement pattern
                    qml.Toffoli(wires=[i-1, i, (i+1) % len(inputs)])
                    qml.CSWAP(wires=[i-1, i, (i+1) % len(inputs)])
            
            # Return measurements in phi-pi basis
            return [
                qml.expval(qml.Hermitian(
                    np.array([
                        [phi * np.exp(-inputs[i]**2/2), np.pi * np.tanh(inputs[i])],
                        [np.pi * np.tanh(inputs[i]), phi * np.exp(-inputs[i]**2/2)]
                    ]), wires=i))
                for i in range(len(inputs))
            ]
        
        # Execute the circuit and convert to serializable format
        result = circuit(inputs)
        return convert_to_serializable(result)

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

    def process_query(self, query):
        try:
            # Get quantum circuit output and other calculations as before
            inputs = np.random.uniform(0, 1, size=8)
            quantum_state = np.array(self.quantum_circuit(inputs))  # Convert to numpy array
            classical_physics = self.physics_calculations(mass=1.0, velocity=1000.0)
            
            # Get focused GPT2 response
            gpt2_response = get_focused_response(query)
            
            # Process through MoE/MoA
            encoded = self.tokenizer(query, return_tensors="pt", padding=True, truncation=True)
            input_ids = encoded['input_ids'].to(self.device)
            input_embeddings = model.transformer.wte(input_ids)  # Get embeddings from GPT2
            
            # Process through MoE/MoA - use embeddings directly since they're already 1024-dim
            mean_embeddings = input_embeddings.mean(dim=1)  # Average over sequence length
            moe_output, metadata = self.moe_moa(mean_embeddings)
            
            # Generate fractal DNA pattern using the actual model output
            fractal_dna = {
                "complexity": float(torch.norm(moe_output).item()),
                "dimension": len(moe_output.shape),
                "pattern": moe_output.tolist()
            }
            
            # Use the actual metadata from our model
            model_metrics = {
                'input_shape': metadata['input_shape'],
                'output_shape': metadata['output_shape'],
                'training_steps': metadata['training_steps'],
                'last_loss': metadata['last_loss'],
                'model_config': metadata['model_config']
            }
            
            # Generate visualization
            viz_filename = self.visualize_quantum_state(quantum_state, query)
            
            response = {
                'quantum_state': quantum_state.tolist(),
                'classical_physics': classical_physics,
                'fractal_dna': fractal_dna,
                'moe_moa_metrics': model_metrics,
                'answer': gpt2_response
            }
            
            return response

        except Exception as e:
            error_traceback = traceback.format_exc()
            print(f"Error processing query: {str(e)}\n{error_traceback}")
            return {
                "error": f"An error occurred: {str(e)}",
                "details": error_traceback
            }

    def save_genesis_block(self, query, genesis_block, viz_filename=None):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO genesis_blocks (
                            query, quantum_state, classical_physics, relativity_metrics, 
                            fractal_dna, visualization_path
                          ) VALUES (?, ?, ?, ?, ?, ?)''',
                       (query,
                        json.dumps(genesis_block["quantum_state"]),
                        json.dumps(genesis_block["classical_physics"]),
                        json.dumps(genesis_block["relativity_metrics"]),
                        json.dumps(genesis_block["fractal_dna"]),
                        viz_filename))
        conn.commit()
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
            filename = f"quantum_state_{uuid.uuid4().hex}.png"
            filepath = os.path.join(static_dir, filename)
            plt.savefig(filepath)
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

# Add endpoint to get visualization image
@app.route('/api/visualization/<filename>')
def get_visualization(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

# Add endpoint to get query history
@app.route('/api/history', methods=['GET'])
def get_history():
    try:
        # Verify token
        token = None
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        
        if not token:
            return jsonify({"error": "Missing authentication token"}), 401
        
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({"error": "Invalid authentication token"}), 401
        
        # Get limit parameter, default to 10
        limit = request.args.get('limit', default=10, type=int)
        
        # Get history from quantum_ai
        history = quantum_ai.get_history(limit)
        
        return jsonify({"history": history})
    except Exception as e:
        # Log the full error with traceback
        error_traceback = traceback.format_exc()
        print(f"Error retrieving history: {str(e)}\n{error_traceback}")
        
        # Return a more detailed error message
        return jsonify({
            "error": f"An error occurred: {str(e)}",
            "details": error_traceback
        }), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat()
    })

# Add token endpoint for authentication
@app.route('/api/token', methods=['POST'])
def get_token():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        # Simple authentication - in production use secure authentication
        if username == 'admin' and password == 'secret':
            # Generate JWT token
            token = jwt.encode({
                'user': username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, app.config['SECRET_KEY'], algorithm='HS256')
            
            return jsonify({'token': token})
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Add the /api/process endpoint that the frontend is calling
@app.route('/api/process', methods=['POST'])
def process_query():
    try:
        # Verify token
        token = None
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        
        if not token:
            return jsonify({"error": "Missing authentication token"}), 401
        
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({"error": "Invalid authentication token"}), 401
        
        data = request.json
        query = data.get('query', '')
        
        if not query:
            return jsonify({"error": "No query provided"}), 400
        
        result = quantum_ai.process_query(query)
        
        # Add visualization URL if available
        if 'visualization_path' in result and result['visualization_path']:
            viz_filename = os.path.basename(result['visualization_path'])
            result['visualization_url'] = url_for('get_visualization', filename=viz_filename, _external=True)
        
        # Ensure we have a valid answer
        if 'answer' not in result or not result['answer']:
            result['answer'] = f"Analysis complete for: {query}"
        
        # Log the response for debugging
        print(f"API Response: {json.dumps(result, indent=2)}")
        
        return jsonify(result)
    except Exception as e:
        # Log the full error with traceback
        error_traceback = traceback.format_exc()
        print(f"Error processing query: {str(e)}\n{error_traceback}")
        
        # Return a more detailed error message
        return jsonify({
            "error": f"An error occurred: {str(e)}",
            "details": error_traceback
        }), 500

# Keep the original endpoint for backward compatibility
@app.route('/api/quantum/process', methods=['POST'])
def process_quantum_query():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"error": "Missing query parameter"}), 400
            
        query = data.get("query")
        result = quantum_ai.process_query(query)
        
        response = {
            "status": "success",
            "query": query,
            "result": result,
            "nlp_response": nlp_model(query, max_length=100, num_return_sequences=1)[0]['generated_text']
        }
        
        # Ensure the entire response is serializable
        response = convert_to_serializable(response)
        
        return jsonify(response)
        
    except Exception as e:
        traceback.print_exc()  # Print full traceback for debugging
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                             'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    # Create static directory if it doesn't exist
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(static_dir, exist_ok=True)
    
    print("\nQuantum Fractal DNA Interface")
    print("=============================")
    print("Access the web interface at: http://localhost:5002")
    print("Login credentials:")
    print("  Username: admin")
    print("  Password: secret")
    print("=============================")
    
    # Run the Flask application in debug mode
    app.run(host='0.0.0.0', port=5002, debug=True)