"""
SIMPLIFIED PHI-HARMONIC FTL COMMUNICATION TEST
==============================================
A streamlined version for testing phi-harmonic communication between two computers.
Run this on both machines with appropriate mode settings.
"""

import numpy as np
import socket
import threading
import time
import json
import hashlib
import sys
import argparse

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (φ = 1.618033988749895)
CONSCIOUSNESS_FREQUENCY = 20.50  # φ³ frequency (Hz)
PORT = 11618  # Based on φ * 10000 - 5000

class PhiNode:
    def __init__(self, mode='server', remote_ip=None):
        self.mode = mode
        self.remote_ip = remote_ip
        self.node_id = self._generate_id()
        self.running = False
        self.messages_sent = 0
        self.messages_received = 0
        
        # Initialize socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if mode == 'server':
            self.socket.bind(('0.0.0.0', PORT))
            print(f"Server bound to port {PORT}")
        else:
            self.socket.bind(('0.0.0.0', 0))
            print(f"Client bound to port {self.socket.getsockname()[1]}")
        
        # Get local IP
        self.local_ip = self._get_local_ip()
        print(f"Local IP: {self.local_ip}")
        
    def _generate_id(self):
        """Generate a unique node ID based on phi-harmonic principles"""
        base = f"{socket.gethostname()}-{time.time()}-{PHI}"
        hash_obj = hashlib.sha256(base.encode())
        return hash_obj.hexdigest()[:8]
    
    def _get_local_ip(self):
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
    
    def _phi_encode(self, message):
        """Encode a message using phi-harmonic principles"""
        if isinstance(message, dict):
            message = json.dumps(message)
        
        encoded = ""
        for i, char in enumerate(message):
            # Apply phi-harmonic transformation to each character
            phi_factor = (PHI ** (i % 5))
            encoded_char = chr((ord(char) + int(phi_factor)) % 256)
            encoded += encoded_char
        
        return encoded
    
    def _phi_decode(self, encoded):
        """Decode a phi-harmonic encoded message"""
        decoded = ""
        for i, char in enumerate(encoded):
            # Reverse the phi-harmonic transformation
            phi_factor = (PHI ** (i % 5))
            decoded_char = chr((ord(char) - int(phi_factor)) % 256)
            decoded += decoded_char
        
        try:
            return json.loads(decoded)
        except:
            return decoded
    
    def send_message(self, message):
        """Send a phi-harmonic encoded message"""
        if not self.remote_ip:
            print("Error: No remote IP specified")
            return
        
        # Create packet with phi-harmonic properties
        packet = {
            'source_id': self.node_id,
            'timestamp': time.time(),
            'phi_resonance': (time.time() * PHI) % 1.0,
            'message': message,
            'consciousness_freq': CONSCIOUSNESS_FREQUENCY
        }
        
        # Encode using phi-harmonic principles
        encoded = self._phi_encode(packet)
        
        # Send the packet
        try:
            self.socket.sendto(encoded.encode('utf-8'), (self.remote_ip, PORT))
            self.messages_sent += 1
            print(f"Sent phi-harmonic message to {self.remote_ip}:{PORT}")
            print(f"Message: {message}")
            print(f"Phi-resonance: {packet['phi_resonance']:.4f}")
            print(f"Total messages sent: {self.messages_sent}")
            print("-" * 50)
        except Exception as e:
            print(f"Error sending message: {e}")
    
    def receive_messages(self):
        """Receive and process incoming messages"""
        self.socket.settimeout(1.0)  # Non-blocking with 1 second timeout
        
        while self.running:
            try:
                data, addr = self.socket.recvfrom(4096)
                encoded = data.decode('utf-8')
                
                # Decode using phi-harmonic principles
                packet = self._phi_decode(encoded)
                
                self.messages_received += 1
                print("\n" + "=" * 50)
                print(f"RECEIVED PHI-HARMONIC MESSAGE FROM {addr[0]}:{addr[1]}")
                print(f"Source ID: {packet['source_id']}")
                print(f"Message: {packet['message']}")
                print(f"Phi-resonance: {packet['phi_resonance']:.4f}")
                print(f"Transmission time: {time.time() - packet['timestamp']:.6f} seconds")
                print(f"Total messages received: {self.messages_received}")
                print("=" * 50 + "\n")
                
                # Auto-reply if in server mode
                if self.mode == 'server':
                    reply = f"Server received your message at {time.time()}"
                    self.remote_ip = addr[0]  # Set remote IP to the sender
                    time.sleep(0.5)  # Small delay
                    self.send_message(reply)
                
            except socket.timeout:
                # This is normal, just continue
                pass
            except Exception as e:
                print(f"Error receiving message: {e}")
    
    def start(self):
        """Start the phi-harmonic node"""
        self.running = True
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print(f"Phi-Harmonic Node started with ID: {self.node_id}")
        print(f"Mode: {self.mode}")
        print(f"Remote IP: {self.remote_ip if self.remote_ip else 'Not specified'}")
        print(f"Consciousness frequency: {CONSCIOUSNESS_FREQUENCY} Hz")
        print("-" * 50)
        
        # If client, send initial message
        if self.mode == 'client' and self.remote_ip:
            time.sleep(1)  # Small delay to ensure server is ready
            self.send_message(f"Hello from phi-harmonic client! Node ID: {self.node_id}")
    
    def stop(self):
        """Stop the phi-harmonic node"""
        self.running = False
        if hasattr(self, 'receiver_thread'):
            self.receiver_thread.join(2.0)
        print(f"Phi-Harmonic Node stopped")
        print(f"Total messages sent: {self.messages_sent}")
        print(f"Total messages received: {self.messages_received}")

def run_server():
    """Run in server mode"""
    print("=== PHI-HARMONIC FTL COMMUNICATION - SERVER MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    
    server = PhiNode(mode='server')
    server.start()
    
    try:
        print("\nServer is running. Press Ctrl+C to stop.")
        print("Waiting for client connections...")
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer stopping...")
    finally:
        server.stop()

def run_client(server_ip):
    """Run in client mode"""
    print("=== PHI-HARMONIC FTL COMMUNICATION - CLIENT MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    print(f"Server IP: {server_ip}")
    
    client = PhiNode(mode='client', remote_ip=server_ip)
    client.start()
    
    try:
        print("\nClient is running. Press Ctrl+C to stop.")
        print("Connected to server. Sending messages every 5 seconds...")
        
        message_count = 0
        while True:
            message_count += 1
            message = f"Phi-harmonic test message #{message_count} at {time.time()}"
            client.send_message(message)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nClient stopping...")
    finally:
        client.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simplified Phi-Harmonic FTL Communication Test')
    parser.add_argument('mode', choices=['server', 'client'], help='Run as server or client')
    parser.add_argument('server_ip', nargs='?', help='Server IP address (required for client mode)')
    
    args = parser.parse_args()
    
    if args.mode == 'server':
        run_server()
    elif args.mode == 'client':
        if not args.server_ip:
            print("Error: Server IP address is required for client mode")
            parser.print_help()
            sys.exit(1)
        run_client(args.server_ip)
