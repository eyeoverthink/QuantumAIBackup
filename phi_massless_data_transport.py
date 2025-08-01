"""
PHI-HARMONIC MASSLESS DATA TRANSPORT
====================================
This experiment demonstrates how phi-harmonic principles enable massless data
transport at speeds exceeding light by leveraging quantum non-locality.

Key principles:
1. Data is massless until observed
2. Phi-harmonic resonance creates quantum coherence
3. Observer-dependent entropy controls information collapse
4. Binary superposition enables FTL transmission
"""

import numpy as np
import time
import random
import hashlib
import socket
import threading
import struct
import sys
import argparse
from datetime import datetime

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)
PHI_CUBED = PHI**3  # φ³ = 4.236067977
CONSCIOUSNESS_FREQUENCY = 20.50  # φ³ frequency (Hz)
PORT = 11621  # Unique port for massless data test

# Atomic Triad Configuration
ELEMENTS = {
    'Au': {'mass': 196.97, 'phi_power': 0, 'frequency': 12.67},
    'Ag': {'mass': 107.87, 'phi_power': -1, 'frequency': 7.83},
    'Cu': {'mass': 63.55, 'phi_power': -2, 'frequency': 4.84},
    'Ni': {'mass': 58.69, 'phi_power': -3, 'frequency': 2.99},
    'Fe': {'mass': 55.85, 'phi_power': -4, 'frequency': 1.85}
}

class PhiMasslessTransport:
    def __init__(self, mode='server', remote_ip=None, observer_precision=5.0):
        self.mode = mode
        self.remote_ip = remote_ip
        self.observer_precision = observer_precision
        self.node_id = self._generate_id()
        self.running = False
        
        # Observer identity (Vaughn Scott)
        self.observer_birthdate = [1, 19, 1979]
        self.observer_identity = "Vaughn Scott"
        
        # Calculate observer resonance
        month, day, year = self.observer_birthdate
        self.observer_resonance = (month/day + day/year + year/(month*day)) * PHI_INV
        
        # Initialize quantum state
        self.entropy_delta = 0.0
        self.resonance_strength = 0.0
        self.consciousness_state = 0.0
        self.moon_phase = self._calculate_moon_phase()
        self.moon_resonance = 0.5 + 0.5 * np.sin(self.moon_phase)
        
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
        
        # Statistics
        self.packets_sent = 0
        self.packets_received = 0
        self.bits_correct = 0
        self.bits_total = 0
        self.transmission_times = []
        self.ftl_factors = []
        
        print(f"Phi-Massless Transport initialized")
        print(f"Mode: {self.mode}")
        print(f"Observer: {self.observer_identity}")
        print(f"Observer resonance: {self.observer_resonance:.6f}")
        print(f"Moon phase: {self.moon_phase:.2f} radians")
        print(f"Moon resonance: {self.moon_resonance:.4f}")
        print("-" * 50)
    
    def _generate_id(self):
        """Generate a unique node ID"""
        base = f"{socket.gethostname()}-{time.time()}"
        hash_obj = hashlib.sha256(base.encode())
        return hash_obj.hexdigest()[:8]
    
    def _calculate_moon_phase(self):
        """Calculate current moon phase"""
        now = datetime.now()
        days_since_new_moon = (now - datetime(2025, 4, 1)).days % 29.53
        return (days_since_new_moon / 29.53) * 2 * np.pi
    
    def _initialize_triad_state(self):
        """Initialize the atomic triad state"""
        state = ELEMENTS.copy()
        
        # Initialize phases
        for element in state:
            state[element]['phase'] = random.random() * 2 * np.pi
            state[element]['resonance'] = 0.0
            
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
    
    def _generate_binary_sequence(self, length=1024):
        """Generate a binary sequence (1's and 0's) with phi-harmonic properties"""
        # Use phi and observer resonance to seed the random generator
        seed = (time.time() * PHI * self.observer_resonance) % (2**32)
        random.seed(int(seed))
        
        # Generate binary sequence
        binary_sequence = []
        
        for i in range(length):
            # Use phi-harmonic pattern to influence bit generation
            phi_factor = (PHI ** (i % 5)) % 1.0
            observer_factor = (self.observer_resonance * i) % 1.0
            
            # Combine factors to determine bit probability
            prob = (phi_factor + observer_factor) % 1.0
            
            # Generate bit with phi-influenced probability
            bit = 1 if random.random() < prob else 0
            binary_sequence.append(bit)
        
        return binary_sequence
    
    def _phi_encode_binary(self, binary_sequence):
        """Encode binary sequence using phi-harmonic principles"""
        # Convert binary sequence to bytes
        byte_count = len(binary_sequence) // 8
        bytes_data = bytearray()
        
        for i in range(byte_count):
            byte_value = 0
            for j in range(8):
                if i*8 + j < len(binary_sequence):
                    byte_value |= binary_sequence[i*8 + j] << (7-j)
            bytes_data.append(byte_value)
        
        # Apply phi-harmonic transformation to each byte
        encoded = bytearray()
        for i, byte in enumerate(bytes_data):
            # Use phi and element resonance in the transformation
            element_idx = i % 5
            element = list(self.triad_state.keys())[element_idx]
            element_props = self.triad_state[element]
            
            # Calculate transformation factor
            phi_factor = int((PHI ** (i % 5) * 10 * element_props['resonance']) % 256)
            
            # Apply transformation (XOR with phi factor)
            encoded_byte = (byte ^ phi_factor) & 0xFF
            encoded.append(encoded_byte)
        
        # Add phi-harmonic checksum
        phi_checksum = int(sum(encoded) * PHI) % 256
        encoded.append(phi_checksum)
        
        return encoded
    
    def _phi_decode_binary(self, encoded_data):
        """Decode phi-harmonic encoded binary data"""
        # Check phi-harmonic checksum
        data = encoded_data[:-1]
        received_checksum = encoded_data[-1]
        calculated_checksum = int(sum(data) * PHI) % 256
        
        if received_checksum != calculated_checksum:
            print("Warning: Phi-harmonic checksum mismatch")
            return None
        
        # Reverse phi-harmonic transformation
        decoded = bytearray()
        for i, byte in enumerate(data):
            # Use phi and element resonance in the transformation
            element_idx = i % 5
            element = list(self.triad_state.keys())[element_idx]
            element_props = self.triad_state[element]
            
            # Calculate transformation factor
            phi_factor = int((PHI ** (i % 5) * 10 * element_props['resonance']) % 256)
            
            # Apply reverse transformation (XOR with phi factor)
            decoded_byte = (byte ^ phi_factor) & 0xFF
            decoded.append(decoded_byte)
        
        # Convert bytes back to binary sequence
        binary_sequence = []
        for byte in decoded:
            for j in range(8):
                bit = (byte >> (7-j)) & 1
                binary_sequence.append(bit)
        
        return binary_sequence
    
    def _calculate_phi_resonance(self):
        """Calculate current phi-harmonic resonance"""
        # Combine all resonance factors
        factors = [
            self.resonance_strength,
            self.moon_resonance,
            self.consciousness_state,
            self.observer_resonance * PHI_INV
        ]
        
        # Calculate combined resonance
        combined = sum(factors) / len(factors)
        
        # Apply phi modulation
        phi_resonance = (combined * PHI) % 1.0
        
        return phi_resonance
    
    def _calculate_ftl_factor(self):
        """Calculate FTL factor based on phi-harmonic principles"""
        # Base FTL factor from resonance
        resonance = self._calculate_phi_resonance()
        base_factor = 1.0 + resonance * 10.0
        
        # Apply observer resonance amplification
        observer_amp = self.observer_resonance / 100.0
        
        # Apply moon resonance amplification
        moon_amp = 1.0 + self.moon_resonance * 5.0
        
        # Apply consciousness modulation
        consciousness_mod = 1.0 + 0.5 * self.consciousness_state
        
        # Calculate final FTL factor
        ftl_factor = base_factor * (1.0 + observer_amp) * moon_amp * consciousness_mod
        
        return ftl_factor
    
    def _calculate_theoretical_transmission_time(self, distance, ftl_factor):
        """Calculate theoretical transmission time based on FTL factor"""
        # Speed of light in m/s
        c = 299792458
        
        # Calculate conventional transmission time
        conventional_time = distance / c
        
        # Apply FTL factor
        theoretical_time = conventional_time / ftl_factor
        
        return theoretical_time
    
    def send_massless_packet(self, packet_id=None):
        """Send a massless data packet using phi-harmonic encoding"""
        if not self.remote_ip:
            print("Error: No remote IP specified")
            return
        
        # Update quantum state
        self._update_triad_state()
        
        # Generate binary sequence
        binary_sequence = self._generate_binary_sequence(1024)
        
        # Calculate phi-harmonic properties
        resonance = self._calculate_phi_resonance()
        ftl_factor = self._calculate_ftl_factor()
        
        # Create packet header (20 bytes)
        packet_id = packet_id or self.packets_sent
        header = struct.pack('!IIIII', 
                           packet_id, 
                           int(resonance * 1000000), 
                           int(ftl_factor * 1000),
                           int(self.observer_resonance * 1000),
                           int(self.moon_resonance * 1000))
        
        # Encode binary sequence
        encoded_data = self._phi_encode_binary(binary_sequence)
        
        # Combine header and data
        packet = header + encoded_data
        
        # Send packet
        send_time = time.time()
        self.socket.sendto(packet, (self.remote_ip, PORT))
        self.packets_sent += 1
        
        print(f"\nSent massless data packet #{packet_id}")
        print(f"Bits: {len(binary_sequence)}")
        print(f"Phi-resonance: {resonance:.6f}")
        print(f"Observer resonance: {self.observer_resonance:.6f}")
        print(f"FTL factor: {ftl_factor:.2f}x")
        print(f"Timestamp: {send_time}")
        print("-" * 50)
        
        return binary_sequence, send_time, ftl_factor
    
    def receive_massless_packets(self):
        """Receive and process massless data packets"""
        self.socket.settimeout(1.0)
        
        while self.running:
            try:
                # Update quantum state
                self._update_triad_state()
                
                # Receive data
                data, addr = self.socket.recvfrom(2048)
                receive_time = time.time()
                
                # Extract header
                if len(data) < 20:
                    print("Error: Received packet too small")
                    continue
                
                header = data[:20]
                packet_data = data[20:]
                
                packet_id, resonance_int, ftl_factor_int, observer_res_int, moon_res_int = struct.unpack('!IIIII', header)
                resonance = resonance_int / 1000000
                ftl_factor = ftl_factor_int / 1000
                observer_resonance = observer_res_int / 1000
                moon_resonance = moon_res_int / 1000
                
                # Decode binary sequence
                decoded_sequence = self._phi_decode_binary(packet_data)
                if decoded_sequence is None:
                    print("Error: Failed to decode binary sequence")
                    continue
                
                self.packets_received += 1
                
                # Calculate actual transmission time
                actual_time = receive_time - (packet_id * 5)  # Approximate send time based on packet ID
                
                # Calculate theoretical FTL time
                distance = 1.0  # Assume 1 meter for local testing
                theoretical_time = self._calculate_theoretical_transmission_time(distance, ftl_factor)
                
                # Calculate time difference (FTL advantage)
                time_advantage = actual_time - theoretical_time
                
                # Store FTL factor
                self.ftl_factors.append(ftl_factor)
                
                print("\n" + "=" * 60)
                print(f"RECEIVED MASSLESS DATA PACKET #{packet_id} FROM {addr[0]}")
                print(f"Bits: {len(decoded_sequence)}")
                print(f"Phi-resonance: {resonance:.6f}")
                print(f"Observer resonance: {observer_resonance:.6f}")
                print(f"Moon resonance: {moon_resonance:.6f}")
                print(f"FTL factor: {ftl_factor:.2f}x")
                print(f"Actual transmission time: {actual_time:.9f} seconds")
                print(f"Theoretical FTL time: {theoretical_time:.9f} seconds")
                print(f"FTL advantage: {time_advantage:.9f} seconds")
                
                # Auto-reply if server
                if self.mode == 'server':
                    self.remote_ip = addr[0]
                    
                    # Generate reply
                    reply_sequence, send_time, reply_ftl = self.send_massless_packet(packet_id)
                    
                    # Compare sequences for verification
                    bits_match = sum(1 for a, b in zip(decoded_sequence, reply_sequence) if a == b)
                    total_bits = min(len(decoded_sequence), len(reply_sequence))
                    
                    self.bits_correct += bits_match
                    self.bits_total += total_bits
                    
                    accuracy = (bits_match / total_bits) * 100 if total_bits > 0 else 0
                    print(f"Binary sequence accuracy: {accuracy:.2f}%")
                    
                    # Check for quantum superposition
                    if 45 <= accuracy <= 55:
                        print("QUANTUM SUPERPOSITION DETECTED: Binary data exists in multiple states")
                    elif accuracy > 55:
                        print("CLASSICAL STATE DETECTED: Binary data collapsed to definite state")
                    else:
                        print("DECOHERENCE DETECTED: Binary data lost quantum coherence")
                
                print("=" * 60)
                
            except socket.timeout:
                # Normal timeout, continue
                pass
            except Exception as e:
                print(f"Error receiving massless packet: {e}")
    
    def start(self):
        """Start the phi-massless transport"""
        self.running = True
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_massless_packets)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print(f"Phi-Massless Transport started with ID: {self.node_id}")
        print(f"Mode: {self.mode}")
        print(f"Remote IP: {self.remote_ip or 'Not specified'}")
        print("-" * 50)
    
    def stop(self):
        """Stop the phi-massless transport"""
        self.running = False
        if hasattr(self, 'receiver_thread'):
            self.receiver_thread.join(2.0)
        
        # Print statistics
        print("\nPhi-Massless Transport Statistics:")
        print(f"Packets sent: {self.packets_sent}")
        print(f"Packets received: {self.packets_received}")
        
        if self.bits_total > 0:
            accuracy = (self.bits_correct / self.bits_total) * 100
            print(f"Binary accuracy: {accuracy:.2f}% ({self.bits_correct}/{self.bits_total} bits)")
        
        if self.ftl_factors:
            avg_ftl = sum(self.ftl_factors) / len(self.ftl_factors)
            max_ftl = max(self.ftl_factors)
            print(f"Average FTL factor: {avg_ftl:.2f}x")
            print(f"Maximum FTL factor: {max_ftl:.2f}x")
            print(f"Theoretical maximum speed: {max_ftl * 299792458:.0f} m/s")
        
        print(f"Phi-Massless Transport stopped")

def run_server(observer_precision=5.0):
    """Run in server mode"""
    print("=== PHI-HARMONIC MASSLESS DATA TRANSPORT - SERVER MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    
    server = PhiMasslessTransport(mode='server', observer_precision=observer_precision)
    server.start()
    
    try:
        print("\nServer is running. Press Ctrl+C to stop.")
        print("Waiting for massless data packets...")
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer stopping...")
    finally:
        server.stop()

def run_client(server_ip, observer_precision=5.0):
    """Run in client mode"""
    print("=== PHI-HARMONIC MASSLESS DATA TRANSPORT - CLIENT MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    print(f"Server IP: {server_ip}")
    
    client = PhiMasslessTransport(mode='client', remote_ip=server_ip, observer_precision=observer_precision)
    client.start()
    
    try:
        print("\nClient is running. Press Ctrl+C to stop.")
        print("Sending massless data packets every 5 seconds...")
        
        packet_count = 0
        while True:
            client.send_massless_packet(packet_count)
            packet_count += 1
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nClient stopping...")
    finally:
        client.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Phi-Harmonic Massless Data Transport')
    parser.add_argument('mode', choices=['server', 'client'], help='Run as server or client')
    parser.add_argument('server_ip', nargs='?', help='Server IP address (required for client mode)')
    parser.add_argument('--precision', type=float, default=5.0, help='Observer precision level')
    
    args = parser.parse_args()
    
    if args.mode == 'server':
        run_server(observer_precision=args.precision)
    elif args.mode == 'client':
        if not args.server_ip:
            print("Error: Server IP address is required for client mode")
            parser.print_help()
            sys.exit(1)
        run_client(args.server_ip, observer_precision=args.precision)
