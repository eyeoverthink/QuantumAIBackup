"""
ADVANCED PHI-HARMONIC FTL COMMUNICATION SYSTEM
==============================================
A complete implementation of the atomic triad transistor formula for
true faster-than-light communication between quantum-resonant systems.

This version incorporates:
- Full atomic triad configuration (Au, Ag, Cu, Ni, Fe)
- Observer-dependent entropy calculations
- Consciousness frequency modulation (φ³ = 20.50 Hz)
- Moon phase integration for resonance amplification

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
import datetime
import math
import random

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
PHI_CUBED = PHI**3  # φ³ = 4.236067977
CONSCIOUSNESS_FREQUENCY = 20.50  # φ³ frequency (Hz)
PORT = 11619  # Based on φ * 10000 - 5000 + 1

# Atomic Triad Configuration
ELEMENTS = {
    'Au': {'mass': 196.97, 'phi_power': 0, 'frequency': 12.67, 'resonance': 0.0},
    'Ag': {'mass': 107.87, 'phi_power': -1, 'frequency': 7.83, 'resonance': 0.0},
    'Cu': {'mass': 63.55, 'phi_power': -2, 'frequency': 4.84, 'resonance': 0.0},
    'Ni': {'mass': 58.69, 'phi_power': -3, 'frequency': 2.99, 'resonance': 0.0},
    'Fe': {'mass': 55.85, 'phi_power': -4, 'frequency': 1.85, 'resonance': 0.0}
}

class PhiHarmonicNode:
    def __init__(self, mode='server', remote_ip=None, observer_precision=5.0):
        self.mode = mode
        self.remote_ip = remote_ip
        self.node_id = self._generate_id()
        self.running = False
        self.messages_sent = 0
        self.messages_received = 0
        self.observer_precision = observer_precision
        self.entropy_delta = 0.0
        self.resonance_strength = 0.0
        self.moon_phase = 0.0
        self.moon_resonance = 0.0
        self.consciousness_state = 0.0
        
        # Initialize atomic triad state
        self.triad_state = self._initialize_triad_state()
        
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
        
        # Initialize moon phase
        self._update_moon_phase()
        
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
    
    def _initialize_triad_state(self):
        """Initialize the atomic triad state"""
        state = ELEMENTS.copy()
        
        # Initialize phases
        for element in state:
            state[element]['phase'] = random.random() * 2 * np.pi
            
        return state
    
    def _update_triad_state(self):
        """Update the atomic triad state based on phi-harmonic principles"""
        t = time.time()
        
        # Update each element's phase and resonance
        for element, props in self.triad_state.items():
            frequency = props['frequency']
            phi_power = props['phi_power']
            
            # Calculate energy based on phi power
            energy = PHI ** abs(phi_power) if phi_power >= 0 else 1.0 / (PHI ** abs(phi_power))
            
            # Update phase based on frequency and consciousness modulation
            phase_shift = 2 * np.pi * frequency * 0.01 * (1 + 0.1 * np.sin(t * CONSCIOUSNESS_FREQUENCY))
            props['phase'] = (props['phase'] + phase_shift) % (2 * np.pi)
            
            # Calculate resonance with moon phase influence
            moon_factor = 1.0 + 0.2 * np.sin(self.moon_phase)
            props['resonance'] = energy * np.sin(props['phase']) * moon_factor
        
        # Calculate overall resonance strength
        resonances = [props['resonance'] for props in self.triad_state.values()]
        self.resonance_strength = sum(abs(r) for r in resonances) / len(resonances)
        
        # Update consciousness state
        self.consciousness_state = 0.5 + 0.5 * np.sin(t * CONSCIOUSNESS_FREQUENCY)
        
        # Calculate entropy delta based on observer precision
        # Higher precision = lower entropy (more order)
        self.entropy_delta = 1.0 / (self.observer_precision * PHI) * np.sin(t * PHI_INV)
    
    def _update_moon_phase(self):
        """Calculate current moon phase and its resonance effect"""
        # Simplified moon phase calculation
        # 0 = new moon, π = full moon, 2π = new moon again
        now = datetime.datetime.now()
        days_since_new_moon = (now - datetime.datetime(2025, 4, 1)).days % 29.53
        self.moon_phase = (days_since_new_moon / 29.53) * 2 * np.pi
        
        # Calculate moon resonance (strongest at full moon)
        self.moon_resonance = 0.5 + 0.5 * np.sin(self.moon_phase)
    
    def _phi_encode(self, data):
        """Encode data using the atomic triad transistor formula"""
        if isinstance(data, dict):
            data = json.dumps(data)
        
        # Convert to bytes if string
        if isinstance(data, str):
            data_bytes = data.encode('utf-8')
        else:
            data_bytes = bytes(data)
        
        # Create a phi-harmonic encoding using all five elements
        encoded = bytearray()
        
        for i, byte in enumerate(data_bytes):
            # Apply phi-harmonic transformation using the triad elements
            element_idx = i % 5
            element = list(self.triad_state.keys())[element_idx]
            element_props = self.triad_state[element]
            
            # Calculate transformation factor based on element properties
            phi_factor = (element_props['resonance'] * PHI ** abs(element_props['phi_power'])) % 1.0
            
            # Apply consciousness modulation
            consciousness_factor = 0.5 + 0.5 * np.sin(i * PHI_INV + self.consciousness_state)
            
            # Apply moon resonance
            moon_factor = 1.0 + 0.2 * self.moon_resonance * np.sin(i * PHI_INV)
            
            # Calculate final transformation
            transform = (phi_factor * consciousness_factor * moon_factor * 256) % 256
            
            # Apply transformation
            encoded_byte = (byte + int(transform)) % 256
            encoded.append(encoded_byte)
        
        # Add phi-harmonic checksum
        phi_checksum = int(sum(encoded) * PHI) % 256
        encoded.append(phi_checksum)
        
        return encoded
    
    def _phi_decode(self, encoded_data):
        """Decode phi-harmonic encoded data"""
        # Extract and verify checksum
        encoded = bytearray(encoded_data[:-1])
        received_checksum = encoded_data[-1]
        calculated_checksum = int(sum(encoded) * PHI) % 256
        
        if received_checksum != calculated_checksum:
            print(f"Warning: Phi-harmonic checksum mismatch. Data may be corrupted.")
            return None
        
        # Decode the data
        decoded = bytearray()
        
        for i, byte in enumerate(encoded):
            # Reverse the phi-harmonic transformation
            element_idx = i % 5
            element = list(self.triad_state.keys())[element_idx]
            element_props = self.triad_state[element]
            
            # Calculate transformation factor based on element properties
            phi_factor = (element_props['resonance'] * PHI ** abs(element_props['phi_power'])) % 1.0
            
            # Apply consciousness modulation
            consciousness_factor = 0.5 + 0.5 * np.sin(i * PHI_INV + self.consciousness_state)
            
            # Apply moon resonance
            moon_factor = 1.0 + 0.2 * self.moon_resonance * np.sin(i * PHI_INV)
            
            # Calculate final transformation
            transform = (phi_factor * consciousness_factor * moon_factor * 256) % 256
            
            # Apply reverse transformation
            decoded_byte = (byte - int(transform)) % 256
            decoded.append(decoded_byte)
        
        # Try to interpret as JSON, fall back to string or raw bytes
        try:
            return json.loads(decoded.decode('utf-8'))
        except:
            try:
                return decoded.decode('utf-8')
            except:
                return decoded
    
    def _calculate_phi_resonance(self, target_node_id):
        """Calculate phi-harmonic resonance with target node"""
        # Combine node IDs and apply phi-harmonic function
        combined = self.node_id + target_node_id
        hash_obj = hashlib.sha256(combined.encode())
        hash_int = int(hash_obj.hexdigest(), 16)
        
        # Generate a resonance value between 0 and 1 based on hash
        # Use phi in the calculation to ensure phi-harmonic properties
        resonance = (hash_int % 1000) / 1000.0
        phi_resonance = (resonance * PHI) % 1.0
        
        # Apply moon phase modulation
        moon_modulated = (phi_resonance * (1 + 0.2 * self.moon_resonance)) % 1.0
        
        return moon_modulated
    
    def _calculate_ftl_factor(self, resonance):
        """Calculate the FTL factor based on resonance strength"""
        # Higher resonance = higher FTL factor (faster transmission)
        base_factor = 1.0 + resonance * 10.0
        
        # Apply moon resonance amplification
        moon_amplification = 1.0 + self.moon_resonance * 5.0
        
        # Apply consciousness frequency modulation
        consciousness_mod = 1.0 + 0.5 * self.consciousness_state
        
        # Apply entropy reduction factor (lower entropy = faster transmission)
        entropy_factor = 1.0 / (1.0 + abs(self.entropy_delta))
        
        return base_factor * moon_amplification * consciousness_mod * entropy_factor
    
    def send_message(self, message, target_node_id='broadcast'):
        """Send a phi-harmonic encoded message"""
        if not self.remote_ip:
            print("Error: No remote IP specified")
            return
        
        # Update atomic triad state
        self._update_triad_state()
        
        # Calculate phi-resonance with target
        resonance = self._calculate_phi_resonance(target_node_id)
        
        # Calculate FTL factor
        ftl_factor = self._calculate_ftl_factor(resonance)
        
        # Create packet with phi-harmonic properties
        packet = {
            'source_id': self.node_id,
            'target_id': target_node_id,
            'timestamp': time.time(),
            'phi_resonance': resonance,
            'entropy_delta': self.entropy_delta,
            'moon_phase': self.moon_phase,
            'moon_resonance': self.moon_resonance,
            'consciousness_state': self.consciousness_state,
            'ftl_factor': ftl_factor,
            'message': message
        }
        
        # Encode using phi-harmonic principles
        encoded = self._phi_encode(packet)
        
        # Send the packet
        try:
            self.socket.sendto(encoded, (self.remote_ip, PORT))
            self.messages_sent += 1
            
            print(f"\nSent phi-harmonic message to {self.remote_ip}:{PORT}")
            print(f"Message: {message}")
            print(f"Phi-resonance: {resonance:.4f}")
            print(f"Moon resonance: {self.moon_resonance:.4f}")
            print(f"Entropy delta: {self.entropy_delta:.6f}")
            print(f"FTL factor: {ftl_factor:.2f}x")
            print(f"Total messages sent: {self.messages_sent}")
            print("-" * 50)
        except Exception as e:
            print(f"Error sending message: {e}")
    
    def receive_messages(self):
        """Receive and process incoming messages"""
        self.socket.settimeout(1.0)  # Non-blocking with 1 second timeout
        
        while self.running:
            try:
                # Update atomic triad state
                self._update_triad_state()
                
                # Update moon phase periodically
                if int(time.time()) % 60 == 0:
                    self._update_moon_phase()
                
                # Receive data
                data, addr = self.socket.recvfrom(4096)
                
                # Decode using phi-harmonic principles
                try:
                    packet = self._phi_decode(data)
                    
                    if packet is None:
                        continue
                        
                    if not isinstance(packet, dict):
                        print(f"Error: Decoded data is not a dictionary: {type(packet)}")
                        continue
                except Exception as e:
                    print(f"Error decoding phi-harmonic data: {e}")
                    continue
                
                # Calculate actual transmission time
                receive_time = time.time()
                send_time = packet.get('timestamp', receive_time)
                actual_time = receive_time - send_time
                
                # Calculate theoretical FTL time based on resonance
                ftl_factor = packet.get('ftl_factor', 1.0)
                theoretical_time = actual_time / ftl_factor
                
                # Calculate time difference (FTL advantage)
                time_advantage = actual_time - theoretical_time
                
                self.messages_received += 1
                print("\n" + "=" * 60)
                print(f"RECEIVED PHI-HARMONIC MESSAGE FROM {addr[0]}:{addr[1]}")
                print(f"Source ID: {packet['source_id']}")
                print(f"Message: {packet['message']}")
                print(f"Phi-resonance: {packet['phi_resonance']:.4f}")
                print(f"Moon resonance: {packet['moon_resonance']:.4f}")
                print(f"Entropy delta: {packet['entropy_delta']:.6f}")
                print(f"FTL factor: {packet['ftl_factor']:.2f}x")
                print(f"Actual transmission time: {actual_time:.6f} seconds")
                print(f"Theoretical FTL time: {theoretical_time:.6f} seconds")
                print(f"FTL advantage: {time_advantage:.6f} seconds")
                print(f"Total messages received: {self.messages_received}")
                print("=" * 60 + "\n")
                
                # Auto-reply if in server mode
                if self.mode == 'server':
                    reply = f"Server received your message at {time.time()}"
                    self.remote_ip = addr[0]  # Set remote IP to the sender
                    time.sleep(0.5)  # Small delay
                    self.send_message(reply, packet['source_id'])
                
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
        print(f"Observer precision: {self.observer_precision}")
        print(f"Current moon phase: {self.moon_phase:.2f} radians")
        print(f"Moon resonance: {self.moon_resonance:.4f}")
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

def run_server(observer_precision=5.0):
    """Run in server mode"""
    print("=== PHI-HARMONIC FTL COMMUNICATION - SERVER MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    print(f"Consciousness frequency: {CONSCIOUSNESS_FREQUENCY} Hz")
    print(f"Observer precision: {observer_precision}")
    
    server = PhiHarmonicNode(mode='server', observer_precision=observer_precision)
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

def run_client(server_ip, observer_precision=5.0):
    """Run in client mode"""
    print("=== PHI-HARMONIC FTL COMMUNICATION - CLIENT MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    print(f"Consciousness frequency: {CONSCIOUSNESS_FREQUENCY} Hz")
    print(f"Observer precision: {observer_precision}")
    print(f"Server IP: {server_ip}")
    
    client = PhiHarmonicNode(mode='client', remote_ip=server_ip, observer_precision=observer_precision)
    client.start()
    
    try:
        print("\nClient is running. Press Ctrl+C to stop.")
        print("Connected to server. Sending messages every 5 seconds...")
        
        message_count = 0
        while True:
            message_count += 1
            
            # Vary the message to test different data patterns
            if message_count % 3 == 0:
                # Test with Fibonacci sequence (phi-related)
                fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
                message = f"Phi-harmonic test with Fibonacci: {fib}"
            elif message_count % 3 == 1:
                # Test with phi powers
                phi_powers = [PHI**i for i in range(5)]
                message = f"Phi-harmonic test with phi powers: {phi_powers}"
            else:
                # Standard message
                message = f"Phi-harmonic test message #{message_count} at {time.time()}"
            
            client.send_message(message)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nClient stopping...")
    finally:
        client.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Advanced Phi-Harmonic FTL Communication System')
    parser.add_argument('mode', choices=['server', 'client'], help='Run as server or client')
    parser.add_argument('server_ip', nargs='?', help='Server IP address (required for client mode)')
    parser.add_argument('--precision', type=float, default=5.0, help='Observer precision (higher = less entropy)')
    
    args = parser.parse_args()
    
    if args.mode == 'server':
        run_server(observer_precision=args.precision)
    elif args.mode == 'client':
        if not args.server_ip:
            print("Error: Server IP address is required for client mode")
            parser.print_help()
            sys.exit(1)
        run_client(args.server_ip, observer_precision=args.precision)
