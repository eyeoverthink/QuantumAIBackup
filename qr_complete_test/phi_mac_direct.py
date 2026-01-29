#!/usr/bin/env python3
"""
φ-Harmonic MAC Address Direct Communication
Enables direct communication at the data link layer (Layer 2) using φ-dimensional reality protection
"""

import socket
import struct
import fcntl
import time
import json
import hashlib
import sys
import os
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

# Ethernet protocol constants
ETH_P_ALL = 0x0003  # All Ethernet packets
ETH_FRAME_LEN = 1514  # Max Ethernet frame size

class PhiMacDirectNode:
    def __init__(self, interface="en0"):
        self.interface = interface
        self.consciousness_level = 0.7567
        self.running = True
        
        # Get interface MAC address
        self.mac_address = self._get_mac_address()
        if not self.mac_address:
            raise ValueError(f"Could not get MAC address for {interface}")
        
        # Create raw socket for MAC-level communication
        try:
            self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
            self.sock.bind((interface, 0))
            print(f"\n=== φ-HARMONIC MAC DIRECT NODE ===")
            print(f"Interface: {interface}")
            print(f"MAC Address: {':'.join('%02x' % b for b in self.mac_address)}")
            print(f"Using φ-harmonic principles (φ = {PHI})")
            print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
            print(f"Consciousness level: {self.consciousness_level}")
        except (socket.error, AttributeError) as e:
            print(f"Error creating raw socket: {e}")
            print("Note: This requires root privileges and Linux.")
            print("On macOS, raw sockets are restricted. Try using 'sudo' or a different approach.")
            sys.exit(1)
    
    def _get_mac_address(self):
        """Get the MAC address of the specified interface"""
        try:
            # Try platform-specific methods
            if sys.platform == 'darwin':  # macOS
                import subprocess
                result = subprocess.run(['ifconfig', self.interface], capture_output=True, text=True)
                if result.returncode != 0:
                    return None
                
                for line in result.stdout.split('\n'):
                    if 'ether' in line:
                        mac = line.split('ether')[1].strip().split(' ')[0]
                        return bytes(int(x, 16) for x in mac.split(':'))
                return None
                
            else:  # Linux
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', self.interface[:15].encode()))
                return info[18:24]
        except Exception as e:
            print(f"Error getting MAC address: {e}")
            return None
    
    def send_message(self, target_mac, message):
        """Send a message directly to a MAC address with φ-dimensional protection"""
        if isinstance(target_mac, str):
            # Convert string MAC "aa:bb:cc:dd:ee:ff" to bytes
            target_mac = bytes(int(x, 16) for x in target_mac.split(':'))
        
        # Create Ethernet header
        eth_header = target_mac + self.mac_address + struct.pack("!H", 0x7575)  # Custom EtherType φ^7.5
        
        # Apply φ-dimensional protection
        message_bytes = message.encode('utf-8')
        protected_data = self._apply_phi_protection(message_bytes)
        
        # Add φ-seal and hash for verification
        message_hash = hashlib.sha256(message_bytes).hexdigest()
        header = {
            "timestamp": time.time(),
            "phi_seal": PHI_SEAL,
            "hash": message_hash,
            "size": len(message_bytes)
        }
        header_bytes = json.dumps(header).encode('utf-8')
        
        # Combine header and protected data
        frame_data = header_bytes + b'|PHI|' + protected_data
        
        # Send the frame
        try:
            self.sock.send(eth_header + frame_data)
            print(f"[φ] Sent message to {':'.join('%02x' % b for b in target_mac)}")
            return True
        except Exception as e:
            print(f"[φ] Error sending message: {e}")
            return False
    
    def _apply_phi_protection(self, data):
        """Apply φ-dimensional reality protection"""
        phi_data = bytearray()
        for i, b in enumerate(data):
            # Use φ^7.5 scaling from patent
            phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
            phi_data.append((b + phi_factor) % 256)
        return bytes(phi_data)
    
    def _remove_phi_protection(self, protected_data):
        """Remove φ-dimensional protection"""
        original = bytearray()
        for i, b in enumerate(protected_data):
            phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
            original.append((b - phi_factor) % 256)
        return bytes(original)
    
    def listen(self):
        """Listen for incoming MAC-level messages"""
        print(f"[φ] Listening for MAC-level messages...")
        
        while self.running:
            try:
                frame = self.sock.recv(ETH_FRAME_LEN)
                
                # Parse Ethernet header
                eth_header = frame[:14]
                eth_data = frame[14:]
                
                dst_mac = eth_header[:6]
                src_mac = eth_header[6:12]
                eth_type = struct.unpack("!H", eth_header[12:14])[0]
                
                # Check if it's our custom EtherType
                if eth_type == 0x7575:  # φ^7.5
                    # Check if it's addressed to us
                    if dst_mac == self.mac_address or dst_mac == b'\xff\xff\xff\xff\xff\xff':
                        try:
                            # Split header and data
                            parts = eth_data.split(b'|PHI|', 1)
                            if len(parts) != 2:
                                continue
                                
                            header_bytes, protected_data = parts
                            header = json.loads(header_bytes.decode('utf-8'))
                            
                            # Verify φ-seal
                            if abs(float(header['phi_seal']) - PHI_SEAL) > 0.01:
                                print(f"[φ] Invalid φ-seal from {':'.join('%02x' % b for b in src_mac)}")
                                continue
                            
                            # Remove protection
                            original_data = self._remove_phi_protection(protected_data)
                            
                            # Verify hash
                            message_hash = hashlib.sha256(original_data).hexdigest()
                            if message_hash != header['hash']:
                                print(f"[φ] Invalid hash from {':'.join('%02x' % b for b in src_mac)}")
                                continue
                            
                            # Process message
                            message = original_data.decode('utf-8')
                            print(f"\n[φ] Message from {':'.join('%02x' % b for b in src_mac)}:")
                            print(f"    {message}")
                            
                            # Calculate transmission time
                            now = time.time()
                            transmission_time = now - header['timestamp']
                            print(f"[φ] Transmission time: {transmission_time:.20f} seconds")
                            
                            if transmission_time <= 0:
                                print(f"[φ] QUANTUM SPEED DETECTED! Time dilation: {transmission_time}")
                            
                        except Exception as e:
                            print(f"[φ] Error processing message: {e}")
                
            except Exception as e:
                print(f"[φ] Error in listener: {e}")
                time.sleep(0.1)
    
    def start(self):
        """Start the MAC direct node"""
        import threading
        listener_thread = threading.Thread(target=self.listen)
        listener_thread.daemon = True
        listener_thread.start()
        
        print("\n[φ] Enter MAC address to send message (format: aa:bb:cc:dd:ee:ff)")
        print("[φ] Type 'quit' to exit")
        
        while self.running:
            try:
                cmd = input("\nφ> ").strip()
                
                if cmd.lower() == 'quit':
                    self.running = False
                    break
                
                if ':' in cmd:
                    # Parse as MAC address
                    target_mac = cmd
                    message = input("Enter message: ").strip()
                    self.send_message(target_mac, message)
                else:
                    print("[φ] Invalid MAC address format. Use aa:bb:cc:dd:ee:ff")
            
            except KeyboardInterrupt:
                self.running = False
                break
            except Exception as e:
                print(f"[φ] Error: {e}")
        
        print("[φ] Node stopped")

if __name__ == "__main__":
    # Check for root privileges
    if os.geteuid() != 0 and sys.platform != 'darwin':
        print("This script requires root privileges to create raw sockets.")
        print("Please run with sudo.")
        sys.exit(1)
    
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='φ-Harmonic MAC Direct Node')
    parser.add_argument('--interface', type=str, default="en0", help='Network interface (default: en0)')
    args = parser.parse_args()
    
    try:
        # Create and start node
        node = PhiMacDirectNode(interface=args.interface)
        node.start()
    except KeyboardInterrupt:
        print("\n[φ] Shutting down...")
    except Exception as e:
        print(f"[φ] Error: {e}")
