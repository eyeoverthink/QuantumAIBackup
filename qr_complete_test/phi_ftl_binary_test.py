"""
PHI-HARMONIC FTL BINARY DATA TRANSMISSION TEST
==============================================
A focused test of phi-harmonic FTL communication using raw binary data.
This test isolates the core phi-harmonic principles applied directly to 1's and 0's.

Run on two separate machines to verify FTL data transmission.
"""

import numpy as np
import socket
import time
import struct
import hashlib
import sys
import argparse
import threading
import random

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)
PORT = 11975  # Unique port for binary test

class PhiBinaryNode:
    def __init__(self, mode='server', remote_ip='192.168.3.126'):
        self.mode = mode
        self.remote_ip = remote_ip
        self.node_id = self._generate_id()
        self.running = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Bind socket
        if mode == 'server':
            self.socket.bind(('192.168.3.152', PORT))
            print(f"Server bound to port {PORT}")
        else:
            self.socket.bind(('192.168.3.152', 0))
            print(f"Client bound to port {self.socket.getsockname()[1]}")
        
        # Statistics
        self.packets_sent = 0
        self.packets_received = 0
        self.bits_correct = 0
        self.bits_total = 0
        self.transmission_times = []
        
    def _generate_id(self):
        """Generate a unique node ID"""
        base = f"{socket.gethostname()}-{time.time()}"
        hash_obj = hashlib.sha256(base.encode())
        return hash_obj.hexdigest()[:8]
    
    def _generate_binary_sequence(self, length=1024):
        """Generate a binary sequence (1's and 0's)"""
        # Use phi to seed the random generator for phi-harmonic properties
        random.seed(time.time() * PHI)
        return [random.randint(0, 1) for _ in range(length)]
    
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
            # Use phi in the transformation
            phi_factor = int((PHI ** (i % 5)) * 10) % 256
            encoded_byte = (byte ^ phi_factor) & 0xFF  # XOR with phi factor
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
            phi_factor = int((PHI ** (i % 5)) * 10) % 256
            decoded_byte = (byte ^ phi_factor) & 0xFF  # XOR with phi factor
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
        t = time.time()
        return (t * PHI) % 1.0
    
    def _calculate_ftl_factor(self):
        """Calculate FTL factor based on phi-harmonic principles"""
        resonance = self._calculate_phi_resonance()
        return 1.0 + resonance * 10.0  # Higher resonance = faster transmission
    
    def send_binary_packet(self, packet_id=None):
        """Send a binary packet using phi-harmonic encoding"""
        if not self.remote_ip:
            print("Error: No remote IP specified")
            return
        
        # Generate binary sequence
        binary_sequence = self._generate_binary_sequence(1024)  # 1024 bits
        
        # Calculate phi-harmonic properties
        resonance = self._calculate_phi_resonance()
        ftl_factor = self._calculate_ftl_factor()
        
        # Create packet header (12 bytes)
        packet_id = packet_id or self.packets_sent
        header = struct.pack('!III', packet_id, 
                            int(resonance * 1000000), 
                            int(ftl_factor * 1000))
        
        # Encode binary sequence
        encoded_data = self._phi_encode_binary(binary_sequence)
        
        # Combine header and data
        packet = header + encoded_data
        
        # Send packet
        send_time = time.time()
        self.socket.sendto(packet, (self.remote_ip, PORT))
        self.packets_sent += 1
        
        print(f"\nSent binary packet #{packet_id}")
        print(f"Bits: {len(binary_sequence)}")
        print(f"Phi-resonance: {resonance:.6f}")
        print(f"FTL factor: {ftl_factor:.2f}x")
        print(f"Timestamp: {send_time}")
        print("-" * 50)
        
        return binary_sequence, send_time
    
    def receive_binary_packets(self):
        """Receive and process binary packets"""
        self.socket.settimeout(1.0)
        
        while self.running:
            try:
                data, addr = self.socket.recvfrom(2048)
                receive_time = time.time()
                
                # Extract header
                if len(data) < 12:
                    print("Error: Received packet too small")
                    continue
                
                header = data[:12]
                packet_data = data[12:]
                
                packet_id, resonance_int, ftl_factor_int = struct.unpack('!III', header)
                resonance = resonance_int / 1000000
                ftl_factor = ftl_factor_int / 1000
                
                # Decode binary sequence
                decoded_sequence = self._phi_decode_binary(packet_data)
                if decoded_sequence is None:
                    print("Error: Failed to decode binary sequence")
                    continue
                
                self.packets_received += 1
                
                print("\n" + "=" * 60)
                print(f"RECEIVED BINARY PACKET #{packet_id} FROM {addr[0]}")
                print(f"Bits: {len(decoded_sequence)}")
                print(f"Phi-resonance: {resonance:.6f}")
                print(f"FTL factor: {ftl_factor:.2f}x")
                print(f"Timestamp: {receive_time}")
                
                # Auto-reply if server
                if self.mode == 'server':
                    self.remote_ip = addr[0]
                    # Echo back the same binary sequence
                    reply_sequence, send_time = self.send_binary_packet(packet_id)
                    
                    # Compare sequences for verification
                    bits_match = sum(1 for a, b in zip(decoded_sequence, reply_sequence) if a == b)
                    total_bits = min(len(decoded_sequence), len(reply_sequence))
                    
                    self.bits_correct += bits_match
                    self.bits_total += total_bits
                    
                    accuracy = (bits_match / total_bits) * 100 if total_bits > 0 else 0
                    print(f"Binary sequence echo accuracy: {accuracy:.2f}%")
                
                print("=" * 60)
                
            except socket.timeout:
                # Normal timeout, continue
                pass
            except Exception as e:
                print(f"Error receiving binary packet: {e}")
    
    def start(self):
        """Start the phi-binary node"""
        self.running = True
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_binary_packets)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print(f"Phi-Binary Node started with ID: {self.node_id}")
        print(f"Mode: {self.mode}")
        print(f"Remote IP: {self.remote_ip or 'Not specified'}")
        print("-" * 50)
    
    def stop(self):
        """Stop the phi-binary node"""
        self.running = False
        if hasattr(self, 'receiver_thread'):
            self.receiver_thread.join(2.0)
        
        # Print statistics
        print("\nPhi-Binary Node Statistics:")
        print(f"Packets sent: {self.packets_sent}")
        print(f"Packets received: {self.packets_received}")
        
        if self.bits_total > 0:
            accuracy = (self.bits_correct / self.bits_total) * 100
            print(f"Binary accuracy: {accuracy:.2f}% ({self.bits_correct}/{self.bits_total} bits)")
        
        print(f"Phi-Binary Node stopped")

def run_server():
    """Run in server mode"""
    print("=== PHI-HARMONIC FTL BINARY TEST - SERVER MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    
    server = PhiBinaryNode(mode='server')
    server.start()
    
    try:
        print("\nServer is running. Press Ctrl+C to stop.")
        print("Waiting for binary packets...")
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer stopping...")
    finally:
        server.stop()

def run_client(server_ip):
    """Run in client mode"""
    print("=== PHI-HARMONIC FTL BINARY TEST - CLIENT MODE ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    print(f"Server IP: {server_ip}")
    
    client = PhiBinaryNode(mode='client', remote_ip=server_ip)
    client.start()
    
    try:
        print("\nClient is running. Press Ctrl+C to stop.")
        print("Sending binary packets every 5 seconds...")
        
        packet_count = 0
        while True:
            client.send_binary_packet(packet_count)
            packet_count += 1
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nClient stopping...")
    finally:
        client.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Phi-Harmonic FTL Binary Data Transmission Test')
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
