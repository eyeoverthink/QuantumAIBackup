import os
import json
import numpy as np
import torch
import torch.nn as nn
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from transformers import AutoModelForCausalLM, AutoTokenizer
from deep_learning.models.moe_moa_core import MoEMoAModel, SelfEvolvingMoEMoA
import pennylane as qml

# Initialize quantum device
dev = qml.device("default.qubit", wires=8)

# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize GPT2 model
model_name = "gpt2-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
gpt2_model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize MoE/MoA model
moe_moa_model = MoEMoAModel(
    input_dim=768,  # For GPT2 embeddings
    hidden_dim=1024,
    output_dim=768,
    num_experts=8,
    num_attention_heads=8
)
evolving_model = SelfEvolvingMoEMoA(moe_moa_model)

class QuantumCore:
    def __init__(self):
        self.moe_moa = evolving_model
        self.tokenizer = tokenizer
        self.gpt2_model = gpt2_model
        
    @qml.qnode(dev)
    def quantum_circuit(self, inputs):
        """Quantum circuit for processing inputs"""
        for i in range(len(inputs)):
            qml.RX(inputs[i], wires=i)
            qml.RY(inputs[i] * np.pi, wires=i)
        
        for i in range(len(inputs)-1):
            qml.CNOT(wires=[i, i+1])
            
        return [qml.expval(qml.PauliZ(i)) for i in range(len(inputs))]

    def process_query(self, query: str):
        """Process a query through both quantum and classical systems"""
        # Quantum processing
        inputs = np.random.uniform(0, np.pi, 8)
        quantum_state = self.quantum_circuit(inputs)
        
        # Process through MoE/MoA
        inputs = self.tokenizer(query, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            # Get embeddings from GPT2
            input_embeddings = self.gpt2_model.transformer.wte(inputs.input_ids)
            
            # Process through MoE/MoA
            moe_output, metadata = self.moe_moa.model(input_embeddings.mean(dim=1))
        
        # Generate fractal pattern from MoE/MoA output
        fractal_pattern = self.generate_fractal_pattern(moe_output, metadata)
        
        # Evolve architecture based on performance
        self.evolve_architecture(metadata)
        
        # Generate visualization
        viz_filename = self.visualize_results(quantum_state, moe_output, query)
        
        return {
            'success': True,
            'quantum_state': quantum_state.tolist(),
            'moe_moa_output': moe_output.tolist(),
            'fractal_pattern': fractal_pattern,
            'routing_info': {
                'expert_weights': metadata['routing_weights'].tolist(),
                'temperature': float(metadata['temperature'].item())
            },
            'visualization_path': viz_filename
        }
    
    def generate_fractal_pattern(self, moe_output, metadata):
        """Generate fractal pattern from MoE/MoA output"""
        return {
            'complexity': float(torch.norm(moe_output).item()),
            'dimension': float(metadata['temperature'].item()),
            'pattern': metadata['routing_weights'].tolist()
        }
    
    def evolve_architecture(self, metadata):
        """Evolve the MoE/MoA architecture"""
        performance_data = {
            'expert_usage': metadata['routing_weights'].mean(0).tolist(),
            'attention_diversity': float(torch.std(metadata['attention_outputs']).item())
        }
        self.moe_moa.evolve_architecture(performance_data)
        self.moe_moa.save_evolution_state('evolution_history.pt')
    
    def visualize_results(self, quantum_state, moe_output, query):
        """Create visualization of results"""
        plt.figure(figsize=(12, 6))
        
        # Plot quantum state
        plt.subplot(1, 2, 1)
        plt.bar(range(len(quantum_state)), quantum_state, color='purple')
        plt.title('Quantum State')
        plt.xlabel('Qubit')
        plt.ylabel('Expectation Value')
        
        # Plot MoE/MoA output
        plt.subplot(1, 2, 2)
        plt.plot(moe_output.numpy(), color='blue')
        plt.title('MoE/MoA Output')
        plt.xlabel('Dimension')
        plt.ylabel('Value')
        
        # Save plot
        filename = f"quantum_moe_{hash(query)}.png"
        plt.savefig(os.path.join(app.static_folder, filename))
        plt.close()
        
        return filename

# Initialize quantum core
quantum_core = QuantumCore()

@app.route('/')
def index():
    """Render the main interface"""
    return render_template('index.html')

@app.route('/api/quantum/process', methods=['POST'])
def process_quantum():
    """Process quantum query"""
    try:
        data = request.get_json()
        query = data.get('query', '')
        result = quantum_core.process_query(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    # Create static directory if it doesn't exist
    os.makedirs(app.static_folder, exist_ok=True)
    # Run the server
    socketio.run(app, host='127.0.0.1', port=5001, debug=True)
