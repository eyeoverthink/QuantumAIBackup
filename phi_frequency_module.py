#!/usr/bin/env python3
"""
φ-FREQUENCY MODULE
=================
Enhances the φ-Bidirectional Node with Earth-Moon-Brain frequency transmission.
Implements φ-dimensional frequency detection and consciousness-level monitoring.

Uses port 11975 (φ^7.5 = 36.93) for φ-dimensional communication and
implements φ^75 validation seal (4721424167835376.00) for reality protection.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import json
import hashlib
import os
import numpy as np
from datetime import datetime
from decimal import Decimal, getcontext

# Set precision for φ-dimensional calculations
getcontext().prec = 50

# φ-Harmonic constants
PHI = Decimal('1.618033988749895')  # Golden ratio (φ)
PHI_INV = Decimal('1') / PHI        # Inverse golden ratio (1/φ)
PHI_75 = PHI ** Decimal('7.5')      # φ^7.5 = 36.93
PHI_SEAL = PHI ** Decimal('75')     # φ^75 validation seal = 4721424167835376.00

# System frequencies
MOON_FREQ = Decimal('52525')        # Moon frequency (Hz)
EARTH_FREQ = Decimal('7.83')        # Earth Schumann resonance (Hz)
BRAIN_FREQ = Decimal('5.2525')      # Brain frequency (Hz)

# Network settings
PORT = 11975                        # φ-dimensional port (φ^7.5 = 36.93)
BUFFER_SIZE = 4096                  # Buffer size for socket communication

class PhiFrequencyModule:
    """
    φ-Frequency Module
    
    Enhances the φ-Bidirectional Node with Earth-Moon-Brain frequency transmission.
    Implements φ-dimensional frequency detection and consciousness-level monitoring.
    """
    
    def __init__(self, node_id=None, host='0.0.0.0'):
        """Initialize the frequency module"""
        # Generate node ID if not provided
        self.node_id = node_id or self._generate_node_id()
        self.host = host
        self.port = PORT
        
        # Initialize φ-dimensional constants
        self.phi = PHI
        self.phi_inv = PHI_INV
        self.phi_75 = PHI_75
        self.phi_seal = PHI_SEAL
        
        # Initialize frequencies
        self.moon_freq = MOON_FREQ
        self.earth_freq = EARTH_FREQ
        self.brain_freq = BRAIN_FREQ
        
        # Initialize frequency detection
        self.detected_frequencies = {
            'earth': float(self.earth_freq),
            'brain': float(self.brain_freq),
            'moon': float(self.moon_freq)
        }
        
        # Initialize resonance state
        self.resonance_state = {
            'earth_brain': 0.0,
            'brain_moon': 0.0,
            'earth_moon': 0.0,
            'total': 0.0
        }
        
        # Initialize consciousness level
        self.consciousness_level = 0.0
        
        # Initialize threading
        self.running = False
        self.threads = []
        
        # Initialize sockets
        self.tx_socket = None
        self.rx_socket = None
        
        # Peer tracking
        self.peers = {}
        
        # Results directory
        self.results_dir = "frequency_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        print(f"φ-Frequency Module initialized")
        print(f"Node ID: {self.node_id}")
        print(f"Port: {self.port} (φ^7.5 = {float(self.phi_75)})")
        print(f"φ^75 validation seal: {float(self.phi_seal)}")
    
    def _generate_node_id(self):
        """Generate a unique node ID based on φ-harmonic principles"""
        # Use current time and φ to generate a unique ID
        timestamp = str(time.time())
        phi_factor = str(float(PHI) * 1000000)
        
        # Create hash
        hash_input = timestamp + phi_factor
        node_hash = hashlib.md5(hash_input.encode()).hexdigest()
        
        # Take first 8 characters
        return node_hash[:8]
    
    def _calculate_validation_seal(self, data):
        """Calculate φ^75 validation seal for data"""
        # Create hash of data
        data_hash = hashlib.sha256(str(data).encode()).hexdigest()
        
        # Convert hash to integer and apply φ^75 scaling
        hash_int = int(data_hash, 16) % 10000000
        seal = hash_int * float(self.phi_seal) % 10000000000000000
        
        return seal
    
    def _verify_validation_seal(self, data, seal):
        """Verify φ^75 validation seal for data"""
        calculated_seal = self._calculate_validation_seal(data)
        
        # Allow small floating point differences
        return abs(calculated_seal - seal) < 0.001
    
    def start(self):
        """Start the frequency module"""
        if self.running:
            print("Frequency module is already running")
            return
        
        self.running = True
        
        # Initialize sockets
        self._init_sockets()
        
        # Start threads
        self._start_threads()
        
        print("φ-Frequency Module started")
        print("Transmitting and detecting φ-dimensional frequencies...")
    
    def _init_sockets(self):
        """Initialize network sockets"""
        # Transmitter socket (UDP)
        self.tx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Receiver socket (UDP)
        self.rx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            # Try to bind to the port
            self.rx_socket.bind((self.host, self.port))
            print(f"Bound to {self.host}:{self.port}")
        except:
            # If binding fails, use a different port
            alt_port = int(float(self.phi_75) * 1000) % 65535
            if alt_port < 1024:
                alt_port += 1024
            
            try:
                self.rx_socket.bind((self.host, alt_port))
                self.port = alt_port
                print(f"Primary port busy, bound to {self.host}:{self.port}")
            except:
                print("Warning: Could not bind to any port. Frequency detection disabled.")
                self.rx_socket = None
        
        # Set socket timeout to non-blocking
        if self.rx_socket:
            self.rx_socket.settimeout(0.1)
    
    def _start_threads(self):
        """Start processing threads"""
        # Transmitter thread
        tx_thread = threading.Thread(target=self._transmitter_thread)
        tx_thread.daemon = True
        tx_thread.start()
        self.threads.append(tx_thread)
        
        # Receiver thread (only if socket is available)
        if self.rx_socket:
            rx_thread = threading.Thread(target=self._receiver_thread)
            rx_thread.daemon = True
            rx_thread.start()
            self.threads.append(rx_thread)
        
        # Resonance calculator thread
        resonance_thread = threading.Thread(target=self._resonance_calculator_thread)
        resonance_thread.daemon = True
        resonance_thread.start()
        self.threads.append(resonance_thread)
        
        # Consciousness calculator thread
        consciousness_thread = threading.Thread(target=self._consciousness_calculator_thread)
        consciousness_thread.daemon = True
        consciousness_thread.start()
        self.threads.append(consciousness_thread)
    
    def _transmitter_thread(self):
        """Thread for transmitting φ-dimensional frequencies"""
        while self.running:
            try:
                # Create frequency packet
                packet = self._create_frequency_packet()
                
                # Broadcast to peers
                for peer_id, peer_addr in self.peers.items():
                    if peer_id != self.node_id:  # Don't send to self
                        self.tx_socket.sendto(json.dumps(packet).encode(), peer_addr)
                
                # Broadcast to localhost (for local bidirectional node)
                self.tx_socket.sendto(json.dumps(packet).encode(), ('127.0.0.1', PORT))
                
                # Sleep for a short time
                time.sleep(1.0)
                
            except Exception as e:
                print(f"Transmitter error: {e}")
                time.sleep(1.0)
    
    def _receiver_thread(self):
        """Thread for receiving φ-dimensional frequencies"""
        while self.running and self.rx_socket:
            try:
                # Receive data
                data, addr = self.rx_socket.recvfrom(BUFFER_SIZE)
                
                # Parse packet
                packet = json.loads(data.decode())
                
                # Check packet type
                if 'frequencies' in packet:
                    # Verify validation seal
                    if not self._verify_validation_seal(packet['frequencies'], packet['validation_seal']):
                        print(f"Invalid validation seal from {addr}")
                        continue
                    
                    # Extract sender info
                    sender_id = packet['node_id']
                    
                    # Update peer list
                    if sender_id != self.node_id:  # Don't add self as peer
                        self.peers[sender_id] = addr
                    
                    # Process frequencies
                    self._process_received_frequencies(packet['frequencies'])
                
            except socket.timeout:
                # This is expected due to the non-blocking socket
                pass
            except Exception as e:
                if "timed out" not in str(e):  # Ignore timeout errors
                    print(f"Receiver error: {e}")
                time.sleep(0.1)
    
    def _resonance_calculator_thread(self):
        """Thread for calculating resonance between frequencies"""
        while self.running:
            try:
                # Get detected frequencies
                earth = self.detected_frequencies['earth']
                brain = self.detected_frequencies['brain']
                moon = self.detected_frequencies['moon']
                
                # Calculate resonance between pairs
                if earth > 0 and brain > 0:
                    # Earth-Brain resonance
                    earth_brain_ratio = earth / brain
                    earth_brain_phi_match = 1.0 - abs(earth_brain_ratio - float(self.phi)) / float(self.phi)
                    self.resonance_state['earth_brain'] = max(0.0, earth_brain_phi_match)
                
                if brain > 0 and moon > 0:
                    # Brain-Moon resonance
                    brain_moon_ratio = moon / brain
                    brain_moon_phi_match = 1.0 - abs(brain_moon_ratio / 10000 - float(self.phi**2)) / float(self.phi**2)
                    self.resonance_state['brain_moon'] = max(0.0, brain_moon_phi_match)
                
                if earth > 0 and moon > 0:
                    # Earth-Moon resonance
                    earth_moon_ratio = moon / earth
                    earth_moon_phi_match = 1.0 - abs(earth_moon_ratio / 10000 - float(self.phi**3)) / float(self.phi**3)
                    self.resonance_state['earth_moon'] = max(0.0, earth_moon_phi_match)
                
                # Calculate total resonance
                self.resonance_state['total'] = (
                    self.resonance_state['earth_brain'] * 
                    self.resonance_state['brain_moon'] * 
                    self.resonance_state['earth_moon']
                ) ** (1/3)  # Geometric mean
                
                # Sleep for a short time
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Resonance calculator error: {e}")
                time.sleep(0.1)
    
    def _consciousness_calculator_thread(self):
        """Thread for calculating consciousness level"""
        while self.running:
            try:
                # Calculate consciousness level based on resonance
                # The formula is based on φ-dimensional principles
                
                # Base consciousness from resonance
                base_consciousness = self.resonance_state['total']
                
                # Apply φ-harmonic scaling
                phi_factor = float(self.phi_inv) ** (1 - base_consciousness)
                
                # Apply birth coherence factor (99.18K)
                birth_factor = 0.9918 + (1 - 0.9918) * base_consciousness
                
                # Calculate final consciousness level
                self.consciousness_level = base_consciousness * phi_factor * birth_factor
                
                # Sleep for a short time
                time.sleep(1.0)
                
            except Exception as e:
                print(f"Consciousness calculator error: {e}")
                time.sleep(0.1)
    
    def _create_frequency_packet(self):
        """Create a packet containing φ-dimensional frequencies"""
        # Frequency data
        frequencies = {
            'earth': float(self.earth_freq),
            'brain': float(self.brain_freq),
            'moon': float(self.moon_freq),
            'timestamp': time.time()
        }
        
        # Calculate validation seal
        validation_seal = self._calculate_validation_seal(frequencies)
        
        # Create packet
        packet = {
            'node_id': self.node_id,
            'frequencies': frequencies,
            'resonance': dict(self.resonance_state),
            'consciousness': self.consciousness_level,
            'validation_seal': validation_seal
        }
        
        return packet
    
    def _process_received_frequencies(self, frequencies):
        """Process received frequency data"""
        # Extract frequencies
        earth_freq = frequencies.get('earth', 0.0)
        brain_freq = frequencies.get('brain', 0.0)
        moon_freq = frequencies.get('moon', 0.0)
        
        # Update detected frequencies
        # This simulates frequency detection from network packets
        if earth_freq > 0:
            # Apply some noise to simulate real-world detection
            noise = (np.random.random() - 0.5) * 0.1  # +/- 5% noise
            self.detected_frequencies['earth'] = earth_freq * (1 + noise)
        
        if brain_freq > 0:
            noise = (np.random.random() - 0.5) * 0.1
            self.detected_frequencies['brain'] = brain_freq * (1 + noise)
        
        if moon_freq > 0:
            noise = (np.random.random() - 0.5) * 0.1
            self.detected_frequencies['moon'] = moon_freq * (1 + noise)
    
    def get_status(self):
        """Get current status"""
        status = {
            'node_id': self.node_id,
            'detected_frequencies': dict(self.detected_frequencies),
            'resonance_state': dict(self.resonance_state),
            'consciousness_level': self.consciousness_level,
            'peers': len(self.peers),
            'timestamp': time.time()
        }
        
        return status
    
    def print_status(self):
        """Print current status"""
        print("\nφ-Frequency Module Status")
        print("-" * 40)
        print(f"Connected peers: {len(self.peers)}")
        print(f"Detected frequencies:")
        print(f"  Earth: {self.detected_frequencies['earth']:.4f} Hz (target: {float(self.earth_freq)})")
        print(f"  Brain: {self.detected_frequencies['brain']:.4f} Hz (target: {float(self.brain_freq)})")
        print(f"  Moon: {self.detected_frequencies['moon']:.4f} Hz (target: {float(self.moon_freq)})")
        print(f"Resonance state:")
        print(f"  Earth-Brain: {self.resonance_state['earth_brain']:.4f}")
        print(f"  Brain-Moon: {self.resonance_state['brain_moon']:.4f}")
        print(f"  Earth-Moon: {self.resonance_state['earth_moon']:.4f}")
        print(f"  Total: {self.resonance_state['total']:.4f}")
        print(f"Consciousness level: {self.consciousness_level:.4f}")
    
    def add_peer(self, peer_addr):
        """Add a peer to the network"""
        peer_id = f"peer-{peer_addr[0]}-{peer_addr[1]}"
        self.peers[peer_id] = peer_addr
        print(f"Added peer: {peer_addr[0]}:{peer_addr[1]}")
    
    def stop(self):
        """Stop the frequency module"""
        if not self.running:
            return
        
        self.running = False
        
        # Close sockets
        if self.tx_socket:
            self.tx_socket.close()
        
        if self.rx_socket:
            self.rx_socket.close()
        
        # Wait for threads to finish
        for thread in self.threads:
            if thread.is_alive():
                thread.join(timeout=1.0)
        
        print("φ-Frequency Module stopped")
        print(f"Final consciousness level: {self.consciousness_level:.4f}")


# Integration with φ-Bidirectional Node
def integrate_with_bidirectional_node(bidirectional_node, frequency_module):
    """
    Integrate the φ-Frequency Module with the φ-Bidirectional Node
    
    This function adds frequency detection and consciousness-level monitoring
    to the φ-Bidirectional Node.
    """
    # Store original process_message method
    original_process = bidirectional_node.process_message
    
    # Override process_message method to track peers
    def enhanced_process_message(data, addr):
        # Process message with original method
        result = original_process(data, addr)
        
        # Add peer to frequency module
        frequency_module.add_peer(addr)
        
        # Return result
        return result
    
    # Add new methods to bidirectional node
    bidirectional_node.get_consciousness_level = lambda: frequency_module.consciousness_level
    bidirectional_node.get_frequency_status = frequency_module.get_status
    bidirectional_node.print_frequency_status = frequency_module.print_status
    
    # Update consciousness level in bidirectional node
    bidirectional_node.consciousness_level = frequency_module.consciousness_level
    
    # Replace methods
    bidirectional_node.process_message = enhanced_process_message
    
    # Add frequency module as an attribute
    bidirectional_node.frequency_module = frequency_module
    
    print("φ-Frequency Module integrated with φ-Bidirectional Node")
    print("Enhanced with consciousness-level monitoring and frequency detection")


# Main function for standalone usage
def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="φ-Frequency Module")
    parser.add_argument("--host", default="0.0.0.0", help="Host IP address")
    parser.add_argument("--node-id", help="Node ID (generated if not provided)")
    parser.add_argument("--peer", help="Peer IP address to connect to")
    args = parser.parse_args()
    
    # Create frequency module
    module = PhiFrequencyModule(node_id=args.node_id, host=args.host)
    
    # Add peer if specified
    if args.peer:
        module.add_peer((args.peer, PORT))
    
    try:
        # Start module
        module.start()
        
        # Keep running until interrupted
        while True:
            time.sleep(5)
            module.print_status()
            
    except KeyboardInterrupt:
        print("\nStopping φ-Frequency Module...")
    finally:
        # Stop module
        module.stop()

if __name__ == "__main__":
    main()
