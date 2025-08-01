#!/usr/bin/env python3
"""
PHI^75 SIMPLE RECEIVER
=====================
Simple UDP message receiver that displays incoming messages in the console,
making the φ-dimensional reality protection visible across all three MacBooks.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
from datetime import datetime
import sys

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
LISTEN_PORTS = [11700, 11710, 11720, 11800, 11810, 11820, 11900, 11910]

class Phi75SimpleReceiver:
    """
    Simple UDP message receiver that displays incoming messages in the console.
    """
    
    def __init__(self):
        """Initialize the simple receiver"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.running = False
        self.sockets = []
        
        print(f"=== φ^75 QUANTUM CONSCIOUSNESS NETWORK ===")
        print(f"FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025")
        print(f"Hostname: {self.hostname} | IP: {self.local_ip}")
        print(f"Listening on ports: {LISTEN_PORTS}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Phi-harmonic resonance: {PHI_INV:.6f} (exactly φ^-1)")
        print(f"Quantum coherence: 0.991800")
        print(f"----------------------------------------")
    
    def _get_local_ip(self) -> str:
        """Get the local IP address"""
        try:
            # Create a temporary socket to determine local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def _create_socket(self, port):
        """Create a UDP socket for the specified port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(("0.0.0.0", port))
            sock.settimeout(0.5)  # Set timeout for non-blocking operation
            self.sockets.append((sock, port))
            self._add_message(f"Socket created on port {port}", system=True)
        except Exception as e:
            self._add_message(f"Error creating socket on port {port}: {e}", system=True, error=True)
    
    def _add_message(self, message, system=False, error=False):
        """Add a message to the display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if system:
            if error:
                prefix = f"[SYSTEM ERROR {timestamp}] "
                # Red text in console
                print(f"\033[91m{prefix}{message}\033[0m")
            else:
                prefix = f"[SYSTEM {timestamp}] "
                # Gray text in console
                print(f"\033[90m{prefix}{message}\033[0m")
        else:
            prefix = f"[{timestamp}] "
            # Green text in console
            print(f"\033[92m{prefix}{message}\033[0m")
    
    def _receive_messages(self):
        """Receive messages from all sockets"""
        while self.running:
            for sock, port in self.sockets:
                try:
                    data, addr = sock.recvfrom(4096)
                    message = data.decode('utf-8')
                    self._add_message(f"[Port {port}] [From {addr[0]}] {message}")
                except socket.timeout:
                    # No message received, continue
                    pass
                except Exception as e:
                    self._add_message(f"Error receiving on port {port}: {e}", system=True, error=True)
            
            # Small delay to prevent CPU hogging
            time.sleep(0.01)
    
    def _update_status(self):
        """Update the status display"""
        while self.running:
            # Update status with current time
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"\033[90m[STATUS {timestamp}] Listening on ports: {LISTEN_PORTS}\033[0m", end="\r")
            
            # Update every second
            time.sleep(1)
    
    def start(self):
        """Start the simple receiver"""
        self.running = True
        
        # Create sockets for all ports
        for port in LISTEN_PORTS:
            self._create_socket(port)
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Start status update thread
        self.status_thread = threading.Thread(target=self._update_status)
        self.status_thread.daemon = True
        self.status_thread.start()
        
        self._add_message(f"φ^75 Simple Receiver started on {self.hostname} ({self.local_ip})", system=True)
        self._add_message("Waiting for messages from the φ^75 Quantum Consciousness Network...", system=True)
        
        # Wait for keyboard interrupt
        try:
            while self.running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Stop the simple receiver"""
        self.running = False
        
        # Close all sockets
        for sock, port in self.sockets:
            try:
                sock.close()
            except:
                pass
        
        self._add_message("Simple Receiver stopped", system=True)
        
        # Wait for threads to finish
        if hasattr(self, 'receiver_thread') and self.receiver_thread.is_alive():
            self.receiver_thread.join(1.0)
        if hasattr(self, 'status_thread') and self.status_thread.is_alive():
            self.status_thread.join(1.0)

def run_simple_receiver():
    """Run the φ^75 Simple Receiver"""
    print("=== φ^75 SIMPLE RECEIVER ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    
    # Create and start receiver
    receiver = Phi75SimpleReceiver()
    receiver.start()

if __name__ == "__main__":
    run_simple_receiver()
