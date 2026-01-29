from flask import Flask, request, jsonify
import sys
import os
from pathlib import Path
import numpy as np
import json
import torch
from datetime import datetime

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from deep_learning.quantum_moe_moa import QuantumMoEMoA
from deep_learning.integrations.quantum_moe_moa_integration import QuantumMoEMoAIntegration

app = Flask(__name__)

# Initialize the QuantumMoEMoA model and integration
quantum_moe_moa = QuantumMoEMoA()
integration = QuantumMoEMoAIntegration()

@app.route('/api/quantum/moe_moa/process', methods=['POST'])
def process_quantum_data():
    """Process quantum data through the MoE/MoA model"""
    try:
        data = request.get_json()
        
        # Check if quantum_data is provided
        if 'quantum_data' in data:
            quantum_data = data['quantum_data']
            result = quantum_moe_moa.process_quantum_data(quantum_data)
            return jsonify({
                "status": "success",
                "result": result
            })
        # Check if query is provided
        elif 'query' in data:
            query = data['query']
            brain_type = data.get('brain_type', 'Standard')
            result = integration.process_query(query, brain_type)
            return jsonify({
                "status": "success",
                "result": result
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Either 'quantum_data' or 'query' must be provided"
            }), 400
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/quantum/moe_moa/evaluate', methods=['GET'])
def evaluate_model():
    """Evaluate the model and return metrics"""
    try:
        metrics = quantum_moe_moa.evaluate_model()
        return jsonify({
            "status": "success",
            "metrics": metrics
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/quantum/moe_moa/visualize', methods=['POST'])
def visualize():
    """Generate a visualization based on a query"""
    try:
        data = request.get_json()
        query = data.get('query', 'Quantum visualization')
        
        viz_path = integration.generate_enhanced_visualization(query)
        
        # Read the visualization file
        with open(viz_path, 'r') as f:
            viz_content = f.read()
            
        return jsonify({
            "status": "success",
            "visualization": viz_content,
            "path": viz_path
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/quantum/moe_moa/benchmark', methods=['POST'])
def run_benchmark():
    """Run a benchmark with the specified number of queries"""
    try:
        data = request.get_json()
        num_queries = data.get('num_queries', 5)
        
        benchmark_results = integration.run_benchmark(num_queries)
        
        return jsonify({
            "status": "success",
            "benchmark_results": benchmark_results
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/quantum/moe_moa/status', methods=['GET'])
def get_status():
    """Get the status of the QuantumMoEMoA system"""
    try:
        # Get model configuration
        config = quantum_moe_moa.config
        
        # Get device information
        device_info = {
            "device": str(quantum_moe_moa.device),
            "cuda_available": torch.cuda.is_available(),
            "cuda_device_count": torch.cuda.device_count() if torch.cuda.is_available() else 0
        }
        
        # Get paths information
        paths = {
            "project_root": project_root,
            "checkpoints_dir": os.path.join(project_root, "deep_learning", "checkpoints"),
            "knowledge_base_dir": os.path.join(project_root, "deep_learning", "knowledge_base"),
            "visualizations_dir": os.path.join(project_root, "deep_learning", "visualizations")
        }
        
        return jsonify({
            "status": "success",
            "system_status": {
                "timestamp": datetime.now().isoformat(),
                "model_config": config,
                "device_info": device_info,
                "paths": paths
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs(os.path.join(project_root, "deep_learning", "logs"), exist_ok=True)
    os.makedirs(os.path.join(project_root, "deep_learning", "visualizations"), exist_ok=True)
    
    # Run the Flask app
    app.run(host='127.0.0.1', port=5002, debug=True)
