import os
import sys
from pathlib import Path
import json
import numpy as np
from datetime import datetime
import flask
from flask import Flask, render_template, jsonify, request
import sqlite3

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from deep_learning.quantum_moe_moa import QuantumMoEMoA
from deep_learning.integrations.quantum_moe_moa_integration import QuantumMoEMoAIntegration

# Initialize Flask app
app = Flask(__name__, 
            template_folder=os.path.join(project_root, 'templates'),
            static_folder=os.path.join(project_root, 'static'))

# Initialize the QuantumMoEMoA system
quantum_moe_moa = QuantumMoEMoA()
integration = QuantumMoEMoAIntegration()

# Database setup
def get_db_connection():
    """Get a connection to the quantum database"""
    conn = sqlite3.connect(os.path.join(project_root, 'quantum.db'))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with required tables if they don't exist"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create moe_moa_queries table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS moe_moa_queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT NOT NULL,
        brain_type TEXT NOT NULL,
        combined_score REAL,
        expert_utilization TEXT,
        temperature REAL,
        visualization_path TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Create moe_moa_metrics table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS moe_moa_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        expert_utilization TEXT,
        attention_diversity REAL,
        model_efficiency REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database
init_db()

@app.route('/')
def index():
    """Render the dashboard index page"""
    return render_template('moe_moa_dashboard.html')

@app.route('/api/dashboard/process', methods=['POST'])
def process_query():
    """Process a query and store the results in the database"""
    data = request.get_json()
    query = data.get('query', '')
    brain_type = data.get('brain_type', 'Standard')
    
    # Process the query
    result = integration.process_query(query, brain_type)
    
    # Generate visualization
    viz_path = integration.generate_enhanced_visualization(query)
    
    # Store in database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO moe_moa_queries 
        (query, brain_type, combined_score, expert_utilization, temperature, visualization_path)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (
            query, 
            brain_type, 
            result['combined_metrics']['combined_score'],
            json.dumps(result['moe_moa_result']['expert_utilization']),
            result['moe_moa_result']['temperature'],
            viz_path
        )
    )
    conn.commit()
    query_id = cursor.lastrowid
    conn.close()
    
    # Return the results
    return jsonify({
        'status': 'success',
        'query_id': query_id,
        'result': result,
        'visualization_path': viz_path
    })

@app.route('/api/dashboard/history')
def get_history():
    """Get the query history"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM moe_moa_queries ORDER BY timestamp DESC LIMIT 50')
    queries = cursor.fetchall()
    conn.close()
    
    # Convert to list of dicts
    query_list = []
    for query in queries:
        query_dict = dict(query)
        query_dict['expert_utilization'] = json.loads(query_dict['expert_utilization'])
        query_list.append(query_dict)
    
    return jsonify({
        'status': 'success',
        'queries': query_list
    })

@app.route('/api/dashboard/metrics')
def get_metrics():
    """Get the model metrics"""
    # Evaluate the model
    metrics = quantum_moe_moa.evaluate_model()
    
    # Store in database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO moe_moa_metrics 
        (expert_utilization, attention_diversity, model_efficiency)
        VALUES (?, ?, ?)
        ''',
        (
            json.dumps(metrics['expert_utilization']),
            metrics['attention_diversity'],
            metrics['model_efficiency']
        )
    )
    conn.commit()
    
    # Get historical metrics
    cursor.execute('SELECT * FROM moe_moa_metrics ORDER BY timestamp DESC LIMIT 20')
    historical_metrics = cursor.fetchall()
    conn.close()
    
    # Convert to list of dicts
    metrics_list = []
    for metric in historical_metrics:
        metric_dict = dict(metric)
        metric_dict['expert_utilization'] = json.loads(metric_dict['expert_utilization'])
        metrics_list.append(metric_dict)
    
    return jsonify({
        'status': 'success',
        'current_metrics': metrics,
        'historical_metrics': metrics_list
    })

@app.route('/api/dashboard/visualization/<int:query_id>')
def get_visualization(query_id):
    """Get the visualization for a specific query"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT visualization_path FROM moe_moa_queries WHERE id = ?', (query_id,))
    result = cursor.fetchone()
    conn.close()
    
    if result is None:
        return jsonify({
            'status': 'error',
            'message': f'Query with ID {query_id} not found'
        }), 404
    
    viz_path = result['visualization_path']
    
    # Read the visualization file
    try:
        with open(viz_path, 'r') as f:
            viz_content = f.read()
        
        return jsonify({
            'status': 'success',
            'visualization': viz_content,
            'path': viz_path
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error reading visualization file: {str(e)}'
        }), 500

@app.route('/api/dashboard/expert_utilization')
def get_expert_utilization():
    """Get expert utilization data for visualization"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT expert_utilization, timestamp FROM moe_moa_queries ORDER BY timestamp DESC LIMIT 20')
    results = cursor.fetchall()
    conn.close()
    
    # Process data for visualization
    labels = []
    datasets = []
    
    # Initialize datasets for each expert
    num_experts = 8  # Default number of experts
    
    # Check if we have any data
    if results and len(results) > 0:
        # Get the number of experts from the first result
        first_utilization = json.loads(results[0]['expert_utilization'])
        num_experts = len(first_utilization)
    
    for i in range(num_experts):
        datasets.append({
            'label': f'Expert {i+1}',
            'data': [],
            'borderColor': f'hsl({(i * 360 / num_experts)}, 70%, 50%)',
            'backgroundColor': f'hsla({(i * 360 / num_experts)}, 70%, 50%, 0.5)'
        })
    
    # Fill datasets with data
    for result in reversed(results):  # Reverse to get chronological order
        labels.append(result['timestamp'])
        utilization = json.loads(result['expert_utilization'])
        
        for i, value in enumerate(utilization):
            if i < num_experts:
                datasets[i]['data'].append(value)
    
    return jsonify({
        'status': 'success',
        'chart_data': {
            'labels': labels,
            'datasets': datasets
        }
    })

@app.route('/api/dashboard/model_efficiency')
def get_model_efficiency():
    """Get model efficiency data for visualization"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT attention_diversity, model_efficiency, timestamp FROM moe_moa_metrics ORDER BY timestamp DESC LIMIT 20')
    results = cursor.fetchall()
    conn.close()
    
    # Process data for visualization
    labels = []
    attention_diversity = []
    model_efficiency = []
    
    for result in reversed(results):  # Reverse to get chronological order
        labels.append(result['timestamp'])
        attention_diversity.append(result['attention_diversity'])
        model_efficiency.append(result['model_efficiency'])
    
    return jsonify({
        'status': 'success',
        'chart_data': {
            'labels': labels,
            'datasets': [
                {
                    'label': 'Attention Diversity',
                    'data': attention_diversity,
                    'borderColor': 'hsl(210, 70%, 50%)',
                    'backgroundColor': 'hsla(210, 70%, 50%, 0.5)'
                },
                {
                    'label': 'Model Efficiency',
                    'data': model_efficiency,
                    'borderColor': 'hsl(120, 70%, 50%)',
                    'backgroundColor': 'hsla(120, 70%, 50%, 0.5)'
                }
            ]
        }
    })

@app.route('/api/dashboard/text_feedback', methods=['POST'])
def get_text_feedback():
    """Generate text feedback for a query result"""
    data = request.get_json()
    query = data.get('query', '')
    brain_type = data.get('brain_type', 'Standard')
    
    # Process the query if not already processed
    if data.get('result'):
        result = data.get('result')
    else:
        result = integration.process_query(query, brain_type)
    
    # Generate text feedback based on the result
    feedback = generate_text_feedback(result)
    
    return jsonify({
        'status': 'success',
        'query': query,
        'brain_type': brain_type,
        'feedback': feedback
    })

def generate_text_feedback(result):
    """Generate detailed text feedback based on the query result"""
    quantum_ai_result = result.get('quantum_ai_result', {})
    moe_moa_result = result.get('moe_moa_result', {})
    combined_metrics = result.get('combined_metrics', {})
    
    # Extract metrics
    coherence = quantum_ai_result.get('metrics', {}).get('coherence', 0)
    entanglement = quantum_ai_result.get('metrics', {}).get('entanglement', 0)
    quantum_loss = quantum_ai_result.get('metrics', {}).get('quantum_loss', 0)
    response_quality = quantum_ai_result.get('metrics', {}).get('response_quality', 0)
    
    expert_utilization = moe_moa_result.get('expert_utilization', [])
    temperature = moe_moa_result.get('temperature', 0)
    
    combined_score = combined_metrics.get('combined_score', 0)
    
    # Generate feedback text
    feedback = []
    
    # Overall assessment
    if combined_score > 0.7:
        feedback.append("## Overall Assessment\nThe quantum processing for this query achieved excellent results with high coherence and expert utilization balance.")
    elif combined_score > 0.5:
        feedback.append("## Overall Assessment\nThe quantum processing for this query achieved good results with moderate coherence and reasonable expert utilization.")
    else:
        feedback.append("## Overall Assessment\nThe quantum processing for this query achieved fair results. There may be room for improvement in coherence and expert utilization.")
    
    # Quantum metrics analysis
    feedback.append("\n## Quantum Metrics Analysis")
    
    if coherence > 0.8:
        feedback.append("- **Coherence**: Excellent ({}). The quantum state maintained exceptional coherence throughout processing.".format(round(coherence, 4)))
    elif coherence > 0.6:
        feedback.append("- **Coherence**: Good ({}). The quantum state maintained good coherence during processing.".format(round(coherence, 4)))
    else:
        feedback.append("- **Coherence**: Fair ({}). The quantum state showed some decoherence during processing.".format(round(coherence, 4)))
    
    if entanglement > 0.8:
        feedback.append("- **Entanglement**: Excellent ({}). Strong quantum entanglement was observed between qubits.".format(round(entanglement, 4)))
    elif entanglement > 0.6:
        feedback.append("- **Entanglement**: Good ({}). Moderate quantum entanglement was observed.".format(round(entanglement, 4)))
    else:
        feedback.append("- **Entanglement**: Fair ({}). Limited quantum entanglement was observed.".format(round(entanglement, 4)))
    
    if quantum_loss < 0.1:
        feedback.append("- **Quantum Loss**: Minimal ({}). Very little information was lost during quantum processing.".format(round(quantum_loss, 4)))
    elif quantum_loss < 0.2:
        feedback.append("- **Quantum Loss**: Moderate ({}). Some information was lost during quantum processing.".format(round(quantum_loss, 4)))
    else:
        feedback.append("- **Quantum Loss**: Significant ({}). Considerable information was lost during quantum processing.".format(round(quantum_loss, 4)))
    
    if response_quality > 0.8:
        feedback.append("- **Response Quality**: Excellent ({}). The response was highly relevant and accurate.".format(round(response_quality, 4)))
    elif response_quality > 0.6:
        feedback.append("- **Response Quality**: Good ({}). The response was relevant and mostly accurate.".format(round(response_quality, 4)))
    else:
        feedback.append("- **Response Quality**: Fair ({}). The response could be improved in relevance and accuracy.".format(round(response_quality, 4)))
    
    # Expert utilization analysis
    feedback.append("\n## Expert Utilization Analysis")
    
    # Find the most and least utilized experts
    if expert_utilization:
        max_expert = expert_utilization.index(max(expert_utilization)) + 1
        min_expert = expert_utilization.index(min(expert_utilization)) + 1
        
        # Calculate standard deviation to measure balance
        std_dev = np.std(expert_utilization)
        
        if std_dev < 0.01:
            feedback.append("Expert utilization is extremely balanced (σ={}), indicating that all experts contributed equally to processing this query.".format(round(std_dev, 4)))
        elif std_dev < 0.03:
            feedback.append("Expert utilization is well-balanced (σ={}), with most experts contributing similarly to the result.".format(round(std_dev, 4)))
        else:
            feedback.append("Expert utilization shows some specialization (σ={}), with certain experts contributing more than others.".format(round(std_dev, 4)))
        
        feedback.append("\nExpert {} was most active ({:.2%}), suggesting this query aligned well with its specialization.".format(max_expert, max(expert_utilization)))
        feedback.append("Expert {} was least active ({:.2%}), indicating less relevance to this particular query.".format(min_expert, min(expert_utilization)))
    
    # Temperature analysis
    feedback.append("\n## Processing Parameters")
    if temperature == 1.0:
        feedback.append("The system used standard temperature ({}), allowing for balanced exploration and exploitation in generating responses.".format(temperature))
    elif temperature > 1.0:
        feedback.append("The system used elevated temperature ({}), favoring more creative and diverse responses.".format(temperature))
    else:
        feedback.append("The system used reduced temperature ({}), favoring more deterministic and focused responses.".format(temperature))
    
    # Recommendations
    feedback.append("\n## Recommendations")
    
    recommendations = []
    if coherence < 0.7:
        recommendations.append("Consider techniques to improve quantum coherence, such as error correction or noise reduction.")
    if std_dev > 0.03 and expert_utilization:
        recommendations.append("The expert utilization could be more balanced. Consider retraining with more diverse data.")
    if quantum_loss > 0.15:
        recommendations.append("Quantum loss could be reduced through improved circuit design or additional qubits.")
    
    if recommendations:
        feedback.extend(recommendations)
    else:
        feedback.append("The quantum processing for this query was optimal. No specific improvements are recommended at this time.")
    
    return "\n".join(feedback)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)
