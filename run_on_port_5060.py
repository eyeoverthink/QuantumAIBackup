#!/usr/bin/env python
"""
Force the Quantum AI Flask application to run on port 5060
"""
import os
import sys
import importlib.util
import importlib.machinery

# Set environment variables
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'

# Path to the fraymus_please.py file
fraymus_path = os.path.join(os.path.dirname(__file__), 'template', 'fraymus_please.py')

# Import the module
spec = importlib.util.spec_from_file_location('fraymus_please', fraymus_path)
fraymus = importlib.util.module_from_spec(spec)
sys.modules['fraymus_please'] = fraymus
spec.loader.exec_module(fraymus)

# Print startup message
print("=== Initializing Quantum System with QHRC Optimization ===")
print("\n🚀 Starting Quantum AI server on port 5060...")

# Run the Flask app on port 5060
if __name__ == '__main__':
    # Access the Flask app from the imported module
    app = fraymus.app
    
    # Run the app on port 5060
    app.run(host='0.0.0.0', port=5060, debug=True)
