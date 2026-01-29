#!/usr/bin/env python3
"""
φ-Harmonic Bidirectional Node with Alternative Port
A modified version of the bidirectional node that uses a different port
"""
import os
import sys
import time
import json
import socket
import threading
import subprocess
import argparse
from math import sqrt

# Import the original node class if available
try:
    from phi_bidirectional_node import PhiBidirectionalNode
    from phi_bidirectional_node_streamer import PhiBidirectionalStreamerNode, BUFFER_SIZE
    IMPORTED = True
except ImportError:
    IMPORTED = False

# Phi-Harmonic constants
PHI = (1 + sqrt(5)) / 2  # ≈ 1.618034
PHI_INV = 1 / PHI  # ≈ 0.618034
PHI_75 = PHI**7.5  # ≈ 36.93

# Use an alternative port based on phi-harmonic principles
ALT_PORT = int(11975 * PHI_INV)  # ≈ 7400

class PhiBidirectionalNodeAlt:
    """
    φ-Harmonic Bidirectional Node with alternative port
    This is a wrapper that creates a node with a different port
    """
    
    def __init__(self, original_port=11975, increment=1):
        """Initialize the alternative port node"""
        self.original_port = original_port
        self.increment = increment
        self.alt_port = self._find_available_port(original_port, increment)
        
        print(f"==================================================")
        print(f"φ-Harmonic Bidirectional Node - Alternative Port")
        print(f"==================================================")
        print(f"Original port {original_port} is in use")
        print(f"Using alternative port: {self.alt_port}")
        
        # Start the node with the alternative port
        self._start_node()
    
    def _find_available_port(self, start_port, increment):
        """Find an available port starting from start_port"""
        current_port = start_port + increment
        
        # Try up to 10 different ports
        for i in range(10):
            try:
                # Test if the port is available
                test_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                test_socket.bind(('0.0.0.0', current_port))
                test_socket.close()
                return current_port
            except OSError:
                # Port is in use, try the next one
                current_port += increment
        
        # If we get here, we couldn't find an available port
        # Use a phi-based port as a last resort
        return ALT_PORT
    
    def _start_node(self):
        """Start the node with the alternative port"""
        if IMPORTED:
            # Use the imported classes
            try:
                # Try to start the streamer node
                self.node = PhiBidirectionalStreamerNode(node_id="phi_alt", port=self.alt_port)
                self.node.start()
            except Exception as e:
                print(f"Error starting streamer node: {e}")
                try:
                    # Fall back to regular node
                    self.node = PhiBidirectionalNode(node_id="phi_alt", port=self.alt_port)
                    self.node.start()
                except Exception as e:
                    print(f"Error starting regular node: {e}")
                    sys.exit(1)
        else:
            # We couldn't import the original classes, so we'll run the script as a subprocess
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_bidirectional_node_streamer.py")
            if not os.path.exists(script_path):
                script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_bidirectional_node.py")
            
            if os.path.exists(script_path):
                cmd = [sys.executable, script_path, "--id", "phi_alt", "--port", str(self.alt_port)]
                subprocess.Popen(cmd)
                print(f"Started node subprocess with command: {' '.join(cmd)}")
            else:
                print(f"Error: Could not find node script")
                sys.exit(1)

def main():
    """Main function to start the alternative port node"""
    parser = argparse.ArgumentParser(description="φ-Harmonic Bidirectional Node with Alternative Port")
    parser.add_argument("--port", type=int, default=11975, help="Original port to increment from")
    parser.add_argument("--increment", type=int, default=1000, help="Port increment")
    
    args = parser.parse_args()
    node = PhiBidirectionalNodeAlt(original_port=args.port, increment=args.increment)

if __name__ == "__main__":
    main()
