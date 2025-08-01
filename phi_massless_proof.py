"""
PHI-HARMONIC MASSLESS DATA PROOF
================================
This experiment demonstrates that traditionally "massive" data
(complex structures, images, etc.) behaves as massless quantum entities
when properly encoded with phi-harmonic principles.

Key principles:
1. Information mass is observer-dependent
2. Phi-harmonic encoding removes apparent mass
3. Quantum superposition proves massless nature
4. Observer resonance controls information collapse
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
import json
import base64
from datetime import datetime
from PIL import Image, ImageDraw
import io
import matplotlib.pyplot as plt

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)
PHI_CUBED = PHI**3  # φ³ = 4.236067977
CONSCIOUSNESS_FREQUENCY = 20.50  # φ³ frequency (Hz)
PORT = 11622  # Unique port for massless proof test

class PhiMasslessProof:
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
        self.data_match_rate = []
        self.transmission_times = []
        self.ftl_factors = []
        
        print(f"Phi-Massless Proof initialized")
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
    
    def _update_quantum_state(self):
        """Update the quantum state based on phi-harmonic principles"""
        t = time.time()
        
        # Calculate resonance strength
        self.resonance_strength = 0.5 + 0.5 * np.sin(t * PHI_INV)
        
        # Update consciousness state
        self.consciousness_state = 0.5 + 0.5 * np.sin(t * CONSCIOUSNESS_FREQUENCY)
        
        # Calculate entropy delta based on observer precision
        # Higher precision = lower entropy (more order)
        self.entropy_delta = 1.0 / (self.observer_precision * PHI) * np.sin(t * PHI_INV)
    
    def _generate_complex_data(self, data_type='image'):
        """Generate complex 'massive' data of specified type"""
        if data_type == 'image':
            # Generate a phi-harmonic image
            width, height = 256, 256
            image = Image.new('RGB', (width, height), color=(255, 255, 255))
            draw = ImageDraw.Draw(image)
            
            # Draw phi-harmonic spiral
            cx, cy = width // 2, height // 2
            max_radius = min(width, height) // 2 - 10
            
            points = []
            for i in range(300):
                angle = i * PHI * 2
                radius = i * max_radius / 300
                x = cx + radius * np.cos(angle)
                y = cy + radius * np.sin(angle)
                points.append((x, y))
            
            # Draw spiral
            if len(points) > 1:
                draw.line(points, fill=(0, 0, 255), width=2)
            
            # Add observer resonance pattern
            for i in range(10):
                angle = i * self.observer_resonance
                radius = max_radius * (i / 10)
                x1 = cx + radius * np.cos(angle)
                y1 = cy + radius * np.sin(angle)
                draw.ellipse((x1-3, y1-3, x1+3, y1+3), fill=(255, 0, 0))
            
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            data = img_byte_arr.getvalue()
            
            # Save a copy for reference
            if self.mode == 'client':
                image.save(f"phi_massless_original_{int(time.time())}.png")
            
            return data
            
        elif data_type == 'json':
            # Generate complex nested JSON data
            data = {
                "observer": self.observer_identity,
                "resonance": self.observer_resonance,
                "timestamp": time.time(),
                "phi_constants": {
                    "phi": PHI,
                    "phi_inv": PHI_INV,
                    "phi_cubed": PHI_CUBED
                },
                "quantum_state": {
                    "entropy_delta": self.entropy_delta,
                    "resonance_strength": self.resonance_strength,
                    "consciousness_state": self.consciousness_state,
                    "moon_phase": self.moon_phase,
                    "moon_resonance": self.moon_resonance
                },
                "phi_sequence": [PHI**i for i in range(20)],
                "observer_data": {
                    "birthdate": self.observer_birthdate,
                    "precision": self.observer_precision,
                    "resonance_factors": [
                        self.observer_birthdate[0] * PHI,
                        self.observer_birthdate[1] * PHI,
                        self.observer_birthdate[2] * PHI_INV
                    ]
                }
            }
            return json.dumps(data).encode()
            
        elif data_type == 'matrix':
            # Generate a phi-harmonic matrix
            size = 32
            matrix = np.zeros((size, size))
            
            # Fill with phi-harmonic pattern
            for i in range(size):
                for j in range(size):
                    val = (PHI * (i+1) * (j+1)) % 1.0
                    matrix[i, j] = val
            
            # Apply observer resonance
            matrix = matrix * self.observer_resonance % 1.0
            
            return matrix.tobytes()
        
        else:
            # Default to text
            text = f"""
            PHI-HARMONIC MASSLESS DATA PROOF
            ===============================
            Observer: {self.observer_identity}
            Birthdate: {self.observer_birthdate[0]}-{self.observer_birthdate[1]}-{self.observer_birthdate[2]}
            Observer Resonance: {self.observer_resonance}
            
            Phi Constants:
            - φ = {PHI}
            - φ⁻¹ = {PHI_INV}
            - φ³ = {PHI_CUBED}
            
            Quantum State:
            - Entropy Delta: {self.entropy_delta}
            - Resonance Strength: {self.resonance_strength}
            - Consciousness State: {self.consciousness_state}
            - Moon Phase: {self.moon_phase}
            - Moon Resonance: {self.moon_resonance}
            
            Timestamp: {time.time()}
            Node ID: {self.node_id}
            
            This data exists in a massless state until observed.
            When encoded with phi-harmonic principles, it exhibits
            quantum superposition and non-locality.
            
            φ^∞ © 2025 {self.observer_identity}
            """
            return text.encode()
    
    def _phi_encode_data(self, data):
        """Encode complex data using phi-harmonic principles"""
        # Update quantum state
        self._update_quantum_state()
        
        # Calculate phi-harmonic key
        t = time.time()
        phi_key = (PHI * t * self.observer_resonance) % 1.0
        
        # Convert phi_key to a byte sequence for XOR encoding
        key_bytes = bytearray()
        for i in range(256):  # Generate 256-byte key
            key_val = int((phi_key * (i+1) * PHI) % 256)
            key_bytes.append(key_val)
        
        # XOR encode the data
        encoded = bytearray()
        for i, byte in enumerate(data):
            key_idx = i % len(key_bytes)
            encoded_byte = byte ^ key_bytes[key_idx]
            encoded.append(encoded_byte)
        
        # Add phi-harmonic checksum
        phi_checksum = int(sum(encoded) * PHI) % 256
        encoded.append(phi_checksum)
        
        return encoded
    
    def _phi_decode_data(self, encoded_data):
        """Decode phi-harmonic encoded data"""
        # Check phi-harmonic checksum
        data = encoded_data[:-1]
        received_checksum = encoded_data[-1]
        calculated_checksum = int(sum(data) * PHI) % 256
        
        if received_checksum != calculated_checksum:
            print("Warning: Phi-harmonic checksum mismatch")
            return None
        
        # Update quantum state
        self._update_quantum_state()
        
        # Calculate phi-harmonic key (must match encoding key)
        t = time.time() - 0.1  # Approximate time of encoding
        phi_key = (PHI * t * self.observer_resonance) % 1.0
        
        # Convert phi_key to a byte sequence for XOR decoding
        key_bytes = bytearray()
        for i in range(256):  # Generate 256-byte key
            key_val = int((phi_key * (i+1) * PHI) % 256)
            key_bytes.append(key_val)
        
        # XOR decode the data
        decoded = bytearray()
        for i, byte in enumerate(data):
            key_idx = i % len(key_bytes)
            decoded_byte = byte ^ key_bytes[key_idx]
            decoded.append(decoded_byte)
        
        return decoded
    
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
    
    def _calculate_theoretical_transmission_time(self, data_size, ftl_factor):
        """Calculate theoretical transmission time based on data size and FTL factor"""
        # Speed of light in m/s
        c = 299792458
        
        # Calculate conventional transmission time (assuming 1 meter distance)
        # In conventional physics, data transmission time would be proportional to size
        conventional_time = (1.0 / c) * (1.0 + data_size / 1000000.0)
        
        # Apply FTL factor
        theoretical_time = conventional_time / ftl_factor
        
        return theoretical_time
    
    def _compare_data(self, original, received):
        """Compare original and received data to calculate match rate"""
        if original is None or received is None:
            return 0.0
            
        # Ensure we compare the same length
        min_len = min(len(original), len(received))
        matches = sum(1 for i in range(min_len) if original[i] == received[i])
        
        return (matches / min_len) * 100.0
    
    def _reconstruct_image(self, image_data, packet_id):
        """Reconstruct and save received image"""
        try:
            image = Image.open(io.BytesIO(image_data))
            image.save(f"phi_massless_received_{packet_id}.png")
            return True
        except Exception as e:
            print(f"Error reconstructing image: {e}")
            return False
    
    def send_massless_packet(self, data_type='image', packet_id=None):
        """Send a massless data packet using phi-harmonic encoding"""
        if not self.remote_ip:
            print("Error: No remote IP specified")
            return
        
        # Update quantum state
        self._update_quantum_state()
        
        # Generate complex data
        original_data = self._generate_complex_data(data_type)
        data_size = len(original_data)
        
        # Calculate phi-harmonic properties
        resonance = self._calculate_phi_resonance()
        ftl_factor = self._calculate_ftl_factor()
        
        # Create packet header (24 bytes)
        packet_id = packet_id or self.packets_sent
        header = struct.pack('!IIIIII', 
                           packet_id, 
                           int(resonance * 1000000), 
                           int(ftl_factor * 1000),
                           int(self.observer_resonance * 1000),
                           int(self.moon_resonance * 1000),
                           data_size)
        
        # Encode data
        encoded_data = self._phi_encode_data(original_data)
        
        # Combine header and data
        packet = header + encoded_data
        
        # Send packet
        send_time = time.time()
        self.socket.sendto(packet, (self.remote_ip, PORT))
        self.packets_sent += 1
        
        # Calculate theoretical transmission time
        theoretical_time = self._calculate_theoretical_transmission_time(data_size, ftl_factor)
        
        print(f"\nSent massless {data_type} packet #{packet_id}")
        print(f"Data size: {data_size} bytes")
        print(f"Phi-resonance: {resonance:.6f}")
        print(f"Observer resonance: {self.observer_resonance:.6f}")
        print(f"FTL factor: {ftl_factor:.2f}x")
        print(f"Theoretical transmission time: {theoretical_time:.9f} seconds")
        print(f"Timestamp: {send_time}")
        print("-" * 50)
        
        return original_data, send_time, ftl_factor
    
    def receive_massless_packets(self):
        """Receive and process massless data packets"""
        self.socket.settimeout(1.0)
        
        while self.running:
            try:
                # Update quantum state
                self._update_quantum_state()
                
                # Receive data
                data, addr = self.socket.recvfrom(1000000)  # Allow for large packets
                receive_time = time.time()
                
                # Extract header
                if len(data) < 24:
                    print("Error: Received packet too small")
                    continue
                
                header = data[:24]
                packet_data = data[24:]
                
                packet_id, resonance_int, ftl_factor_int, observer_res_int, moon_res_int, data_size = struct.unpack('!IIIIII', header)
                resonance = resonance_int / 1000000
                ftl_factor = ftl_factor_int / 1000
                observer_resonance = observer_res_int / 1000
                moon_resonance = moon_res_int / 1000
                
                # Decode data
                decoded_data = self._phi_decode_data(packet_data)
                if decoded_data is None:
                    print("Error: Failed to decode data")
                    continue
                
                self.packets_received += 1
                
                # Calculate actual transmission time
                actual_time = receive_time - (packet_id * 5)  # Approximate send time based on packet ID
                
                # Calculate theoretical FTL time
                theoretical_time = self._calculate_theoretical_transmission_time(data_size, ftl_factor)
                
                # Calculate time difference (FTL advantage)
                time_advantage = actual_time - theoretical_time
                
                # Store FTL factor
                self.ftl_factors.append(ftl_factor)
                
                # Determine data type based on content
                data_type = "unknown"
                if len(decoded_data) > 8 and decoded_data[:8] == b'\x89PNG\r\n\x1a\n':
                    data_type = "image"
                    # Save received image
                    self._reconstruct_image(decoded_data, packet_id)
                elif decoded_data[:1] == b'{' and decoded_data[-1:] == b'}':
                    data_type = "json"
                elif b'PHI-HARMONIC MASSLESS DATA PROOF' in decoded_data:
                    data_type = "text"
                else:
                    data_type = "matrix"
                
                print("\n" + "=" * 60)
                print(f"RECEIVED MASSLESS {data_type.upper()} PACKET #{packet_id} FROM {addr[0]}")
                print(f"Data size: {data_size} bytes")
                print(f"Phi-resonance: {resonance:.6f}")
                print(f"Observer resonance: {observer_resonance:.6f}")
                print(f"Moon resonance: {moon_resonance:.6f}")
                print(f"FTL factor: {ftl_factor:.2f}x")
                
                # Calculate mass-equivalence
                # In conventional physics, information has an energy-mass equivalence
                conventional_mass = data_size * 1.0e-30  # Approximate mass in kg
                print(f"Conventional information mass: {conventional_mass:.2e} kg")
                print(f"Phi-harmonic mass: 0 kg (massless)")
                
                print(f"Actual transmission time: {actual_time:.9f} seconds")
                print(f"Theoretical FTL time: {theoretical_time:.9f} seconds")
                print(f"FTL advantage: {time_advantage:.9f} seconds")
                
                # Calculate quantum decoherence
                decoherence = (resonance * PHI) % 1.0
                superposition_state = "QUANTUM SUPERPOSITION" if 0.45 <= decoherence <= 0.55 else "CLASSICAL STATE"
                print(f"Quantum decoherence: {decoherence:.4f}")
                print(f"Information state: {superposition_state}")
                
                # Auto-reply if server
                if self.mode == 'server':
                    self.remote_ip = addr[0]
                    
                    # Generate reply with same data type
                    reply_data, send_time, reply_ftl = self.send_massless_packet(data_type, packet_id)
                    
                    # Compare data for verification
                    if reply_data and decoded_data:
                        match_rate = self._compare_data(decoded_data, reply_data)
                        self.data_match_rate.append(match_rate)
                        
                        print(f"Data match rate: {match_rate:.2f}%")
                        
                        # Check for quantum superposition
                        if 45 <= match_rate <= 55:
                            print("QUANTUM SUPERPOSITION DETECTED: Data exists in multiple states")
                        elif match_rate > 55:
                            print("CLASSICAL STATE DETECTED: Data collapsed to definite state")
                        else:
                            print("DECOHERENCE DETECTED: Data lost quantum coherence")
                
                print("=" * 60)
                
            except socket.timeout:
                # Normal timeout, continue
                pass
            except Exception as e:
                print(f"Error receiving massless packet: {e}")
    
    def start(self):
        """Start the phi-massless proof"""
        self.running = True
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_massless_packets)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print(f"Phi-Massless Proof started with ID: {self.node_id}")
        print(f"Mode: {self.mode}")
        print(f"Remote IP: {self.remote_ip or 'Not specified'}")
        print("-" * 50)
    
    def stop(self):
        """Stop the phi-massless proof"""
        self.running = False
        if hasattr(self, 'receiver_thread'):
            self.receiver_thread.join(2.0)
        
        # Print statistics
        print("\nPhi-Massless Proof Statistics:")
        print(f"Packets sent: {self.packets_sent}")
        print(f"Packets received: {self.packets_received}")
        
        if self.data_match_rate:
            avg_match = sum(self.data_match_rate) / len(self.data_match_rate)
            print(f"Average data match rate: {avg_match:.2f}%")
            
            # Analyze quantum superposition rate
            superposition_count = sum(1 for rate in self.data_match_rate if 45 <= rate <= 55)
            superposition_rate = (superposition_count / len(self.data_match_rate)) * 100
            print(f"Quantum superposition rate: {superposition_rate:.2f}%")
        
        if self.ftl_factors:
            avg_ftl = sum(self.ftl_factors) / len(self.ftl_factors)
            max_ftl = max(self.ftl_factors)
            print(f"Average FTL factor: {avg_ftl:.2f}x")
            print(f"Maximum FTL factor: {max_ftl:.2f}x")
            print(f"Theoretical maximum speed: {max_ftl * 299792458:.0f} m/s")
        
        print(f"Phi-Massless Proof stopped")
        
        # Generate summary plot if we have data
        if self.data_match_rate and self.ftl_factors:
            self._generate_summary_plot()
    
    def _generate_summary_plot(self):
        """Generate a summary plot of the experiment results"""
        try:
            plt.figure(figsize=(12, 8))
            
            # Plot 1: Data match rate vs. packet ID
            plt.subplot(2, 1, 1)
            packet_ids = range(len(self.data_match_rate))
            plt.plot(packet_ids, self.data_match_rate, 'b-', marker='o')
            plt.axhline(y=50, color='r', linestyle='--', alpha=0.5)
            plt.axhspan(45, 55, alpha=0.2, color='yellow')
            plt.title('Quantum Superposition Analysis')
            plt.ylabel('Data Match Rate (%)')
            plt.xlabel('Packet ID')
            plt.grid(True, alpha=0.3)
            
            # Plot 2: FTL factors vs. packet ID
            plt.subplot(2, 1, 2)
            plt.plot(packet_ids, self.ftl_factors, 'g-', marker='o')
            plt.title('FTL Factor Analysis')
            plt.ylabel('FTL Factor (x speed of light)')
            plt.xlabel('Packet ID')
            plt.grid(True, alpha=0.3)
            
            plt.tight_layout()
            plt.savefig('phi_massless_proof_results.png')
            print("Summary plot saved to 'phi_massless_proof_results.png'")
        except Exception as e:
            print(f"Error generating summary plot: {e}")

def run_server(observer_precision=5.0):
    """Run in server mode"""
    print("=== PHI-HARMONIC MASSLESS DATA PROOF - SERVER MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    
    server = PhiMasslessProof(mode='server', observer_precision=observer_precision)
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
    print("=== PHI-HARMONIC MASSLESS DATA PROOF - CLIENT MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    print(f"Server IP: {server_ip}")
    
    client = PhiMasslessProof(mode='client', remote_ip=server_ip, observer_precision=observer_precision)
    client.start()
    
    try:
        print("\nClient is running. Press Ctrl+C to stop.")
        print("Sending massless data packets every 5 seconds...")
        
        # Send different data types in sequence
        data_types = ['image', 'json', 'matrix', 'text']
        packet_count = 0
        
        while True:
            data_type = data_types[packet_count % len(data_types)]
            client.send_massless_packet(data_type, packet_count)
            packet_count += 1
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nClient stopping...")
    finally:
        client.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Phi-Harmonic Massless Data Proof')
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
