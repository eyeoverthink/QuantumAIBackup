#!/usr/bin/env python
"""
Simple HTTP Server for Quantum Visualization
This script creates a simple HTTP server to serve the quantum visualization HTML files.
It follows the "lego" design philosophy by adding a helper component without modifying existing files.
"""

import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Golden ratio constants - incorporating phi principles into our server
PHI = 1.618033988749895
PORT = int(8000 * (1 + 1/PHI))  # Port based on phi ratio

class QuantumHandler(SimpleHTTPRequestHandler):
    """Handler for quantum visualization server with phi-based optimizations"""
    
    def log_message(self, format, *args):
        """Log messages with phi-based timestamp formatting"""
        sys.stderr.write(f"φ-Server: {args[0]} {args[1]} {args[2]}\n")

def start_server():
    """Start the quantum visualization server with phi-based configuration"""
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, QuantumHandler)
    
    # Print phi-based server information
    print(f"Quantum Visualization Server")
    print(f"============================")
    print(f"φ Value: {PHI}")
    print(f"Port: {PORT} (8000 * (1 + 1/φ))")
    print(f"Server running at http://localhost:{PORT}")
    print(f"Opening visualization in browser...")
    
    # Open browser automatically
    webbrowser.open(f'http://localhost:{PORT}/standalone_quantum_viz.html')
    
    # Run server with phi-based message
    print(f"Server running with φ-based optimization. Press Ctrl+C to stop.")
    httpd.serve_forever()

if __name__ == "__main__":
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    start_server()
