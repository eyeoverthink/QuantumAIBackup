#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Web Server
=======================================

This module implements a web server that connects the Quantum Phi-Agent with the web interface,
allowing users to interact with the system through their browser. It provides API endpoints
for querying the agent, retrieving system metrics, and visualizing quantum fields.

Key features:
- RESTful API for agent communication
- WebSocket support for real-time updates
- Serving of static web interface
- JSON data exchange with phi-harmonic structure

This follows the modular "lego" design philosophy, building upon the existing components
without modification.
"""

import os
import json
import time
import logging
import threading
from decimal import Decimal
from typing import Dict, Any, List, Optional, Union

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO

# Import the Quantum Phi-Harmonic components
from quantum_phi_core import QuantumPhiCore
from quantum_processor import QuantumProcessor
from quantum_phi_agent import QuantumPhiAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize the Quantum Phi-Harmonic components
core = QuantumPhiCore()
processor = QuantumProcessor(core)
agent = QuantumPhiAgent(processor)

# Store active connections
active_connections = set()

# Helper function to convert Decimal to float for JSON serialization
def decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, dict):
        return {k: decimal_to_float(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [decimal_to_float(item) for item in obj]
    return obj

# Background thread for system updates
def background_updates():
    """Send periodic updates to connected clients."""
    while True:
        if active_connections:
            # Get current metrics
            metrics = agent.get_metrics()
            
            # Convert Decimal values to float for JSON serialization
            metrics_json = decimal_to_float(metrics)
            
            # Emit to all connected clients
            socketio.emit('metrics_update', metrics_json)
            
            # Update field visualizations every 5 seconds
            socketio.emit('field_update', {
                'timestamp': time.time(),
                'fields': decimal_to_float(processor.get_all_field_metrics())
            })
        
        # Sleep for phi seconds (approximately 1.618s)
        time.sleep(float(core.PHI))

# API Routes
@app.route('/')
def index():
    """Serve the main web interface."""
    return send_from_directory('.', 'quantum_phi_interface.html')

@app.route('/api/query', methods=['POST'])
def query_agent():
    """Process a query to the Quantum Phi-Agent."""
    data = request.json
    
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    query = data['query']
    logger.info(f"Processing query: {query}")
    
    # Process the query through the agent
    response = agent.process_query(query)
    
    # Get updated metrics
    metrics = decimal_to_float(agent.get_metrics())
    
    return jsonify({
        'response': response,
        'metrics': metrics
    })

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """Get current system metrics."""
    metrics = agent.get_metrics()
    return jsonify(decimal_to_float(metrics))

@app.route('/api/fields', methods=['GET'])
def get_fields():
    """Get quantum field information."""
    fields = processor.get_all_field_metrics()
    return jsonify(decimal_to_float(fields))

@app.route('/api/field/<field_name>', methods=['GET'])
def get_field(field_name):
    """Get information for a specific quantum field."""
    try:
        field = processor.get_field_metrics(field_name)
        return jsonify(decimal_to_float(field))
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/conversation', methods=['GET'])
def get_conversation():
    """Get the agent's conversation history."""
    history = agent.get_conversation_history()
    return jsonify(history)

@app.route('/api/reset', methods=['POST'])
def reset_conversation():
    """Reset the agent's conversation history."""
    agent.reset_conversation()
    return jsonify({'status': 'success'})

# WebSocket event handlers
@socketio.on('connect')
def handle_connect():
    """Handle client connection."""
    logger.info(f"Client connected: {request.sid}")
    active_connections.add(request.sid)
    
    # Send initial metrics
    metrics = agent.get_metrics()
    socketio.emit('metrics_update', decimal_to_float(metrics), to=request.sid)
    
    # Send field information
    fields = processor.get_all_field_metrics()
    socketio.emit('field_update', {
        'timestamp': time.time(),
        'fields': decimal_to_float(fields)
    }, to=request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection."""
    logger.info(f"Client disconnected: {request.sid}")
    active_connections.discard(request.sid)

@socketio.on('process_query')
def handle_process_query(data):
    """Process a query through WebSocket."""
    if 'query' not in data:
        socketio.emit('error', {'message': 'No query provided'}, to=request.sid)
        return
    
    query = data['query']
    logger.info(f"Processing WebSocket query: {query}")
    
    # Process the query
    response = agent.process_query(query)
    
    # Get updated metrics
    metrics = agent.get_metrics()
    
    # Send response to the client
    socketio.emit('query_response', {
        'response': response,
        'metrics': decimal_to_float(metrics)
    }, to=request.sid)

# Main entry point
if __name__ == '__main__':
    # Start background thread for updates
    update_thread = threading.Thread(target=background_updates)
    update_thread.daemon = True
    update_thread.start()
    
    # Get the port from environment or use default
    port = int(os.environ.get('PORT', 5000))
    
    # Start the server
    logger.info(f"Starting Quantum Phi-Harmonic System server on port {port}")
    logger.info(f"Access the web interface at http://localhost:{port}")
    
    # Print phi-harmonic welcome message
    phi = float(core.PHI)
    logger.info(f"Quantum Phi-Harmonic System initialized with φ = {phi:.6f}")
    logger.info(f"System resonance: {float(processor.core.metrics['resonance']):.4f}")
    logger.info(f"Phi achievement: {float(processor.core.metrics['phi_achievement']):.6f}")
    
    # Run the server
    socketio.run(app, host='0.0.0.0', port=port, debug=False)
