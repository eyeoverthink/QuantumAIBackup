#!/usr/bin/env python3
"""
φ-Harmonic Bidirectional Communication Node (Enhanced)
Extends the original node with socket reuse options and port availability checking
"""

import os
import sys
import time
import json
import socket
import threading
import subprocess
from datetime import datetime

# Import the original module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from phi_bidirectional_node import PhiBidirectionalNode, PHI, PHI_75, PHI_SEAL

class EnhancedPhiBidirectionalNode(PhiBidirectionalNode):
    """Enhanced version of PhiBidirectionalNode with improved socket handling"""
    
    def __init__(self, node_id="primary", port=11975, force_reuse=False, auto_increment=True):
        """
        Initialize the enhanced bidirectional node
        
        Args:
            node_id (str): Unique identifier for this node
            port (int): Port to listen on (default: 11975 = φ^7.5)
            force_reuse (bool): Whether to force socket address reuse
            auto_increment (bool): Whether to automatically increment port if busy
        """
        self.node_id = node_id
        self.port = port  # φ^7.5 port
        self.original_port = port  # Keep track of original port
        self.consciousness_level = 0.7567
        self.peers = {}
        self.running = True
        self.script_dir = "phi_scripts"
        self.force_reuse = force_reuse
        self.auto_increment = auto_increment
        
        # Create script directory if it doesn't exist
        os.makedirs(self.script_dir, exist_ok=True)
        
        # Initialize quantum socket with enhanced options
        self._initialize_socket()
        
        print(f"\n=== φ-HARMONIC BIDIRECTIONAL NODE (ENHANCED) ===")
        print(f"Node ID: {self.node_id}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Listening on port {self.port}" + 
              (f" (original φ^7.5 = {PHI_75:.2f})" if self.port != self.original_port else f" (φ^7.5 = {PHI_75:.2f})"))
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Consciousness level: {self.consciousness_level}")
        print(f"Script directory: {self.script_dir}")
        print(f"Ready for bidirectional communication")
    
    def _initialize_socket(self):
        """Initialize socket with enhanced error handling and options"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # Set socket options for address reuse if requested
            if self.force_reuse:
                self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                print(f"[φ] Socket address reuse enabled")
            
            # Try to bind to the port
            try:
                self.sock.bind(('0.0.0.0', self.port))
                print(f"[φ] Successfully bound to port {self.port}")
            except OSError as e:
                if e.errno == 48:  # Address already in use
                    if self.auto_increment:
                        # Find an available port by incrementing
                        original_port = self.port
                        while True:
                            self.port += 1
                            try:
                                self.sock.bind(('0.0.0.0', self.port))
                                print(f"[φ] Port {original_port} was in use, using port {self.port} instead")
                                break
                            except OSError:
                                if self.port > original_port + 100:  # Limit search to 100 ports
                                    raise OSError(f"Failed to find available port after 100 attempts")
                    else:
                        # Check if there's already a node running
                        self._check_running_node()
                        raise OSError(f"Port {self.port} is already in use. Use --auto-increment to find an available port.")
        except Exception as e:
            print(f"[φ] Error initializing socket: {e}")
            sys.exit(1)
    
    def _check_running_node(self):
        """Check if there's already a node running and provide helpful information"""
        print(f"[φ] WARNING: Port {self.port} is already in use!")
        print(f"[φ] This likely means another instance of the φ-node is already running.")
        print(f"[φ] Options:")
        print(f"  1. Stop the existing node process")
        print(f"  2. Use a different port with --port option")
        print(f"  3. Use --auto-increment to automatically find an available port")
        print(f"  4. Use --force-reuse to force address reuse (may cause issues)")
        
        # Try to detect running processes (platform-specific)
        try:
            if sys.platform == 'darwin':  # macOS
                print("\nAttempting to find running node processes:")
                os.system(f"ps aux | grep '[p]hi_bidirectional_node' | grep -v grep")
                print("\nTo terminate a process: kill <PID>")
        except:
            pass

def find_available_port(start_port=11975, max_attempts=100):
    """Find an available port starting from start_port"""
    for port in range(start_port, start_port + max_attempts):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(('0.0.0.0', port))
            sock.close()
            return port
        except OSError:
            continue
    raise OSError(f"Failed to find available port after {max_attempts} attempts")

def check_port_availability(port):
    """Check if a port is available"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', port))
        sock.close()
        return True
    except OSError:
        return False

if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='φ-Harmonic Bidirectional Node (Enhanced)')
    parser.add_argument('--id', type=str, default="primary", help='Node ID')
    parser.add_argument('--port', type=int, default=11975, help='Port (default: 11975 = φ^7.5)')
    parser.add_argument('--force-reuse', action='store_true', help='Force socket address reuse')
    parser.add_argument('--auto-increment', action='store_true', help='Auto-increment port if busy')
    parser.add_argument('--check-port', action='store_true', help='Only check if port is available')
    parser.add_argument('--find-port', action='store_true', help='Find and print an available port')
    args = parser.parse_args()
    
    # Special modes
    if args.check_port:
        available = check_port_availability(args.port)
        print(f"Port {args.port} is {'available' if available else 'in use'}")
        sys.exit(0 if available else 1)
    
    if args.find_port:
        try:
            available_port = find_available_port(args.port)
            print(f"Available port: {available_port}")
            sys.exit(0)
        except OSError as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    # Create and start enhanced node
    node = EnhancedPhiBidirectionalNode(
        node_id=args.id, 
        port=args.port,
        force_reuse=args.force_reuse,
        auto_increment=args.auto_increment
    )
    node.start()
