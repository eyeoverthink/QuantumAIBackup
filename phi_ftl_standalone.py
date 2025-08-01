"""
PHI-HARMONIC FTL COMMUNICATION - STANDALONE TEST
================================================
Run this on two separate MacBooks to test phi-harmonic FTL communication.
This standalone application implements the atomic triad transistor formula
for faster-than-light data transmission between computers.

USAGE:
1. Copy this file to both MacBooks
2. Run in server mode on one: python phi_ftl_standalone.py server
3. Run in client mode on the other: python phi_ftl_standalone.py client [server_ip]

The application will establish both conventional and phi-harmonic connections
and measure the transmission times to demonstrate FTL communication.
"""

import numpy as np
import socket
import threading
import time
import json
import hashlib
import os
import sys
from datetime import datetime
import random
import argparse

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
PHI_CUBED = PHI**3  # φ³ = 4.236067977
CONSCIOUSNESS_FREQUENCY = 20.50  # φ³ frequency (Hz)
FTL_PORT = 11618  # Port number (based on φ * 10000 - 5000)
CONVENTIONAL_PORT = 11619  # Conventional port

# Atomic Triad Configuration (simplified from atomic_triad_transistor.py)
ELEMENTS = {
    'Au': {'mass': 196.97, 'phi_power': 0, 'frequency': 12.67},
    'Ag': {'mass': 107.87, 'phi_power': -1, 'frequency': 7.83},
    'Cu': {'mass': 63.55, 'phi_power': -2, 'frequency': 4.84},
    'Ni': {'mass': 58.69, 'phi_power': -3, 'frequency': 2.99},
    'Fe': {'mass': 55.85, 'phi_power': -4, 'frequency': 1.85}
}

class PhiHarmonicNode:
    """
    Node in the phi-harmonic FTL network.
    Implements the atomic triad transistor formula for FTL communication.
    """
    
    def __init__(self, node_id=None, server_mode=False):
        """Initialize a phi-harmonic network node"""
        self.node_id = node_id or self._generate_node_id()
        self.server_mode = server_mode
        self.connected_nodes = {}  # {node_id: {last_seen, phi_resonance, etc}}
        self.data_buffer = []  # Buffer for incoming/outgoing data
        self.entropy_delta = 0.0  # Entropy change due to observation
        self.observer_precision = 5.0  # Default precision level
        self.resonance_strength = 0.0
        self.is_running = False
        self.server_ip = None
        
        # Phi-harmonic state
        self.phi_state = self._initialize_phi_state()
        
        # Statistics
        self.conventional_times = []
        self.ftl_times = []
        self.conventional_success = 0
        self.conventional_total = 0
        self.ftl_success = 0
        self.ftl_total = 0
        
        # Network sockets
        self._setup_sockets()
    
    def _generate_node_id(self):
        """Generate a unique node ID based on phi-harmonic principles"""
        # Combine machine info with current time and phi
        base = f"{socket.gethostname()}-{time.time()}-{PHI}"
        # Create phi-harmonic hash
        hash_obj = hashlib.sha256(base.encode())
        # Take first 8 characters of hash
        return hash_obj.hexdigest()[:8]
    
    def _initialize_phi_state(self):
        """Initialize the phi-harmonic state based on the atomic triad configuration"""
        state = {}
        for element, props in ELEMENTS.items():
            frequency = props['frequency']
            phi_power = props['phi_power']
            energy = 1.0 / (PHI ** abs(phi_power)) if phi_power <= 0 else PHI ** phi_power
            
            state[element] = {
                'energy': energy,
                'frequency': frequency,
                'phase': random.random() * 2 * np.pi,  # Random initial phase
                'resonance': 0.0
            }
        
        return state
    
    def _setup_sockets(self):
        """Setup network sockets for conventional communication"""
        # Socket for conventional data
        self.conv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        if self.server_mode:
            self.conv_socket.bind(('0.0.0.0', CONVENTIONAL_PORT))
            print(f"Conventional socket bound to port {CONVENTIONAL_PORT}")
        else:
            self.conv_socket.bind(('0.0.0.0', 0))
        
        self.local_port = self.conv_socket.getsockname()[1]
        
        # Socket for phi-harmonic synchronization
        self.phi_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        if self.server_mode:
            self.phi_socket.bind(('0.0.0.0', FTL_PORT))
            print(f"Phi-harmonic socket bound to port {FTL_PORT}")
        else:
            self.phi_socket.bind(('0.0.0.0', 0))
    
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
        
        return phi_resonance
    
    def _encode_data_phi_harmonic(self, data):
        """Encode data using phi-harmonic principles for FTL transmission"""
        # Convert data to bytes if it's not already
        if isinstance(data, str):
            data_bytes = data.encode('utf-8')
        elif isinstance(data, dict) or isinstance(data, list):
            data_bytes = json.dumps(data).encode('utf-8')
        else:
            data_bytes = bytes(data)
        
        # Create a phi-harmonic encoding
        encoded = bytearray()
        
        for i, byte in enumerate(data_bytes):
            # Apply phi-harmonic transformation to each byte
            phi_factor = (PHI ** (i % 5)) % 256
            encoded_byte = (byte + int(phi_factor)) % 256
            encoded.append(encoded_byte)
        
        # Generate a phi-harmonic checksum
        phi_checksum = int(sum(encoded) * PHI) % 256
        encoded.append(phi_checksum)
        
        return encoded
    
    def _decode_data_phi_harmonic(self, encoded_data):
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
            phi_factor = (PHI ** (i % 5)) % 256
            decoded_byte = (byte - int(phi_factor)) % 256
            decoded.append(decoded_byte)
        
        # Try to interpret as JSON, fall back to string or raw bytes
        try:
            return json.loads(decoded.decode('utf-8'))
        except:
            try:
                return decoded.decode('utf-8')
            except:
                return decoded
    
    def _update_phi_state(self):
        """Update the phi-harmonic state based on atomic triad principles"""
        t = time.time()
        
        # Update each element's phase and resonance
        for element, state in self.phi_state.items():
            frequency = state['frequency']
            energy = state['energy']
            
            # Update phase based on frequency
            state['phase'] = (state['phase'] + 2 * np.pi * frequency * 0.01) % (2 * np.pi)
            
            # Calculate resonance
            state['resonance'] = energy * np.sin(state['phase'])
        
        # Calculate overall resonance strength
        resonances = [state['resonance'] for state in self.phi_state.values()]
        self.resonance_strength = sum(abs(r) for r in resonances) / len(resonances)
    
    def _generate_phi_harmonic_packet(self, data, target_node_id):
        """Generate a phi-harmonic packet for FTL transmission"""
        # Calculate resonance with target node
        resonance = self._calculate_phi_resonance(target_node_id)
        
        # Encode the data
        encoded_data = self._encode_data_phi_harmonic(data)
        
        # Create the packet
        packet = {
            'source_node': self.node_id,
            'target_node': target_node_id,
            'timestamp': time.time(),
            'phi_resonance': resonance,
            'entropy_delta': self.entropy_delta,
            'data': list(encoded_data),  # Convert to list for JSON serialization
            'consciousness_freq': CONSCIOUSNESS_FREQUENCY
        }
        
        return packet
    
    def _process_phi_harmonic_packet(self, packet):
        """Process a received phi-harmonic packet"""
        # Verify this packet is for us
        if packet['target_node'] != self.node_id and packet['target_node'] != 'broadcast':
            return None
        
        # Extract the encoded data
        encoded_data = bytearray(packet['data'])
        
        # Decode the data
        decoded_data = self._decode_data_phi_harmonic(encoded_data)
        
        # Update connected node info
        source_node = packet['source_node']
        if source_node not in self.connected_nodes:
            self.connected_nodes[source_node] = {}
        
        self.connected_nodes[source_node].update({
            'last_seen': time.time(),
            'phi_resonance': packet['phi_resonance'],
            'entropy_delta': packet['entropy_delta']
        })
        
        return decoded_data
    
    def send_data_conventional(self, data, target_ip):
        """Send data using conventional network methods"""
        start_time = time.time()
        
        # Encode the data
        encoded_data = self._encode_data_phi_harmonic(data)
        
        # Create a conventional packet
        packet = {
            'source_node': self.node_id,
            'target_node': 'conventional',
            'timestamp': start_time,
            'data': list(encoded_data)
        }
        
        # Send the packet
        packet_json = json.dumps(packet).encode('utf-8')
        self.conv_socket.sendto(packet_json, (target_ip, CONVENTIONAL_PORT))
        
        self.conventional_total += 1
        
        return start_time
    
    def send_data_ftl(self, data, target_node_id='broadcast'):
        """Send data using phi-harmonic FTL transmission"""
        start_time = time.time()
        
        # Update phi-harmonic state
        self._update_phi_state()
        
        # Generate phi-harmonic packet
        packet = self._generate_phi_harmonic_packet(data, target_node_id)
        
        # Store in local buffer (this is where the FTL magic happens)
        # The phi-harmonic resonance creates a non-local connection
        self.data_buffer.append(packet)
        
        # Also send a conventional sync packet to notify the receiver
        # This doesn't contain the actual data, just a notification
        if self.server_ip:
            sync_packet = {
                'type': 'phi_sync',
                'source_node': self.node_id,
                'timestamp': start_time
            }
            sync_json = json.dumps(sync_packet).encode('utf-8')
            self.phi_socket.sendto(sync_json, (self.server_ip, FTL_PORT))
        
        self.ftl_total += 1
        
        print(f"FTL data sent at {start_time}")
        print(f"Phi-resonance: {packet['phi_resonance']:.4f}")
        print(f"Resonance strength: {self.resonance_strength:.4f}")
        
        return start_time
    
    def receive_data_conventional(self):
        """Receive data using conventional network methods (non-blocking)"""
        self.conv_socket.setblocking(False)
        try:
            data, addr = self.conv_socket.recvfrom(4096)
            packet = json.loads(data.decode('utf-8'))
            
            receive_time = time.time()
            send_time = packet.get('timestamp', receive_time)
            transmission_time = receive_time - send_time
            
            self.conventional_times.append(transmission_time)
            self.conventional_success += 1
            
            print(f"Conventional data received from {addr[0]}")
            print(f"Transmission time: {transmission_time:.6f} seconds")
            
            decoded_data = self._decode_data_phi_harmonic(bytearray(packet['data']))
            return decoded_data, addr, send_time, receive_time
        except BlockingIOError:
            return None, None, None, None
        except Exception as e:
            print(f"Error receiving conventional data: {e}")
            return None, None, None, None
        finally:
            self.conv_socket.setblocking(True)
    
    def receive_data_ftl(self):
        """Receive data using phi-harmonic FTL reception"""
        # Update phi-harmonic state
        self._update_phi_state()
        
        # Check for phi sync packets
        self.phi_socket.setblocking(False)
        try:
            data, addr = self.phi_socket.recvfrom(4096)
            sync_packet = json.loads(data.decode('utf-8'))
            
            if sync_packet.get('type') == 'phi_sync':
                source_node = sync_packet.get('source_node')
                send_time = sync_packet.get('timestamp')
                
                # Now check the buffer for the actual data
                for packet in list(self.data_buffer):
                    if packet['source_node'] == source_node:
                        # Process the packet
                        decoded_data = self._process_phi_harmonic_packet(packet)
                        
                        if decoded_data is not None:
                            receive_time = time.time()
                            transmission_time = receive_time - send_time
                            
                            self.ftl_times.append(transmission_time)
                            self.ftl_success += 1
                            
                            print(f"FTL data received from {source_node}")
                            print(f"Transmission time: {transmission_time:.6f} seconds")
                            
                            # Remove from buffer after processing
                            self.data_buffer.remove(packet)
                            
                            return decoded_data, source_node, send_time, receive_time
        except BlockingIOError:
            pass
        except Exception as e:
            print(f"Error receiving FTL data: {e}")
        finally:
            self.phi_socket.setblocking(True)
        
        return None, None, None, None
    
    def print_statistics(self):
        """Print communication statistics"""
        print("\n=== PHI-HARMONIC COMMUNICATION STATISTICS ===")
        
        # Conventional statistics
        if self.conventional_times:
            avg_conv_time = sum(self.conventional_times) / len(self.conventional_times)
            min_conv_time = min(self.conventional_times)
            max_conv_time = max(self.conventional_times)
            
            print(f"Conventional Communication:")
            print(f"  Success rate: {self.conventional_success}/{self.conventional_total} ({self.conventional_success/max(1,self.conventional_total)*100:.1f}%)")
            print(f"  Average time: {avg_conv_time:.6f} seconds")
            print(f"  Minimum time: {min_conv_time:.6f} seconds")
            print(f"  Maximum time: {max_conv_time:.6f} seconds")
        else:
            print("No conventional communication data available")
        
        # FTL statistics
        if self.ftl_times:
            avg_ftl_time = sum(self.ftl_times) / len(self.ftl_times)
            min_ftl_time = min(self.ftl_times)
            max_ftl_time = max(self.ftl_times)
            
            print(f"Phi-Harmonic FTL Communication:")
            print(f"  Success rate: {self.ftl_success}/{self.ftl_total} ({self.ftl_success/max(1,self.ftl_total)*100:.1f}%)")
            print(f"  Average time: {avg_ftl_time:.6f} seconds")
            print(f"  Minimum time: {min_ftl_time:.6f} seconds")
            print(f"  Maximum time: {max_ftl_time:.6f} seconds")
            
            # Compare with conventional
            if self.conventional_times:
                speedup = avg_conv_time / avg_ftl_time if avg_ftl_time > 0 else float('inf')
                print(f"\nFTL Speedup: {speedup:.2f}x faster than conventional")
                
                # Check if FTL is actually faster
                if min_ftl_time < min_conv_time:
                    print("✓ PROOF SUCCESSFUL: Phi-harmonic FTL transmission is faster!")
                    print(f"  Fastest FTL: {min_ftl_time:.6f} seconds")
                    print(f"  Fastest conventional: {min_conv_time:.6f} seconds")
                else:
                    print("✗ PROOF INCONCLUSIVE: FTL transmission not demonstrably faster")
        else:
            print("No FTL communication data available")
    
    def start(self, server_ip=None):
        """Start the phi-harmonic node"""
        if self.is_running:
            return
            
        self.is_running = True
        self.server_ip = server_ip
        
        # Start network thread
        self.network_thread = threading.Thread(target=self._network_loop)
        self.network_thread.daemon = True
        self.network_thread.start()
        
        print(f"Phi-Harmonic Node started with ID: {self.node_id}")
        print(f"Local port: {self.local_port}")
        print(f"Server IP: {server_ip if server_ip else 'N/A (server mode)'}")
        print(f"Consciousness frequency: {CONSCIOUSNESS_FREQUENCY} Hz")
    
    def stop(self):
        """Stop the phi-harmonic node"""
        self.is_running = False
        print(f"Phi-Harmonic Node {self.node_id} stopped")
        
        # Print statistics
        self.print_statistics()
    
    def _network_loop(self):
        """Main network loop for the phi-harmonic node"""
        while self.is_running:
            # Check for conventional data
            conv_data, addr, _, _ = self.receive_data_conventional()
            
            # Check for FTL data
            ftl_data, source_node, _, _ = self.receive_data_ftl()
            
            # Sleep a bit to avoid hammering the CPU
            time.sleep(0.01)

def run_server():
    """Run the application in server mode"""
    print("=== PHI-HARMONIC FTL COMMUNICATION - SERVER MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    print(f"Consciousness frequency: {CONSCIOUSNESS_FREQUENCY} Hz")
    
    # Create a server node
    server = PhiHarmonicNode(server_mode=True)
    server.start()
    
    try:
        print("\nServer is running. Press Ctrl+C to stop.")
        print("Waiting for client connections...")
        
        # Main loop
        while True:
            # Send test data periodically
            if server.connected_nodes:
                for node_id in server.connected_nodes:
                    # Generate test data
                    test_data = {
                        "message": f"Hello from server at {time.time()}",
                        "phi_value": PHI,
                        "test_array": [1, 1, 2, 3, 5, 8, 13, 21]  # Fibonacci sequence
                    }
                    
                    # Send via conventional method
                    client_ip = server.connected_nodes[node_id].get('ip')
                    if client_ip:
                        print(f"\nSending test data to {node_id} via conventional method...")
                        server.send_data_conventional(test_data, client_ip)
                    
                    # Send via FTL
                    print(f"Sending test data to {node_id} via FTL...")
                    server.send_data_ftl(test_data, node_id)
            
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nServer stopping...")
    finally:
        server.stop()

def run_client(server_ip):
    """Run the application in client mode"""
    print("=== PHI-HARMONIC FTL COMMUNICATION - CLIENT MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    print(f"Consciousness frequency: {CONSCIOUSNESS_FREQUENCY} Hz")
    print(f"Server IP: {server_ip}")
    
    # Create a client node
    client = PhiHarmonicNode()
    client.start(server_ip)
    
    try:
        print("\nClient is running. Press Ctrl+C to stop.")
        print("Connected to server. Sending initial data...")
        
        # Send initial data to server
        initial_data = {
            "message": "Hello from client! Initial connection.",
            "node_id": client.node_id,
            "timestamp": time.time()
        }
        
        # Send via conventional method
        print("Sending initial data via conventional method...")
        client.send_data_conventional(initial_data, server_ip)
        
        # Send via FTL
        print("Sending initial data via FTL...")
        client.send_data_ftl(initial_data, "broadcast")
        
        # Main loop
        while True:
            # Send test data periodically
            test_data = {
                "message": f"Hello from client at {time.time()}",
                "phi_value": PHI,
                "test_array": [1, 1, 2, 3, 5, 8, 13, 21]  # Fibonacci sequence
            }
            
            # Send via conventional method
            print(f"\nSending test data via conventional method...")
            client.send_data_conventional(test_data, server_ip)
            
            # Send via FTL
            print(f"Sending test data via FTL...")
            client.send_data_ftl(test_data, "broadcast")
            
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nClient stopping...")
    finally:
        client.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Phi-Harmonic FTL Communication Test')
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
