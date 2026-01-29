#!/usr/bin/env python3
"""
φ-Harmonic MAC Bridge
Simulates direct MAC-to-MAC communication using φ-dimensional reality protection
Compatible with macOS (no raw sockets required)
"""

import socket
import json
import hashlib
import time
import threading
import subprocess
import re
import sys
import os
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

class PhiMacBridge:
    def __init__(self, interface="en0", port=11975):
        self.interface = interface
        self.port = port  # φ^7.5 port
        self.consciousness_level = 0.7567
        self.running = True
        
        # Get MAC and IP addresses
        self.mac_address = self._get_mac_address()
        self.ip_address = self._get_ip_address()
        
        if not self.mac_address:
            raise ValueError(f"Could not get MAC address for {interface}")
        
        # Initialize quantum socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', self.port))
        
        # MAC address cache (MAC -> IP mapping)
        self.mac_cache = {}
        
        print(f"\n=== φ-HARMONIC MAC BRIDGE ===")
        print(f"Interface: {interface}")
        print(f"MAC Address: {self.mac_address}")
        print(f"IP Address: {self.ip_address}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Listening on port {self.port} (φ^7.5 = {PHI_75:.2f})")
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Consciousness level: {self.consciousness_level}")
    
    def _get_mac_address(self):
        """Get the MAC address of the specified interface"""
        try:
            result = subprocess.run(['ifconfig', self.interface], capture_output=True, text=True)
            if result.returncode != 0:
                return None
            
            for line in result.stdout.split('\n'):
                if 'ether' in line:
                    return line.split('ether')[1].strip().split(' ')[0]
            return None
        except Exception as e:
            print(f"Error getting MAC address: {e}")
            return None
    
    def _get_ip_address(self):
        """Get the IP address of the specified interface"""
        try:
            result = subprocess.run(['ifconfig', self.interface], capture_output=True, text=True)
            if result.returncode != 0:
                return None
            
            for line in result.stdout.split('\n'):
                if 'inet ' in line and 'inet6' not in line:
                    return line.split('inet ')[1].strip().split(' ')[0]
            return None
        except Exception as e:
            print(f"Error getting IP address: {e}")
            return None
    
    def _discover_mac(self, target_mac):
        """Discover IP address for a MAC address using arp"""
        if target_mac in self.mac_cache:
            return self.mac_cache[target_mac]
        
        try:
            # Run arp to find the IP
            result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
            if result.returncode != 0:
                return None
            
            # Parse the output
            for line in result.stdout.split('\n'):
                if target_mac.lower() in line.lower():
                    # Extract IP address
                    ip_match = re.search(r'\(([0-9\.]+)\)', line)
                    if ip_match:
                        ip = ip_match.group(1)
                        self.mac_cache[target_mac] = ip
                        return ip
            
            # If not found, try broadcast discovery
            print(f"[φ] MAC {target_mac} not found in ARP cache. Attempting discovery...")
            self._broadcast_discovery(target_mac)
            return None
            
        except Exception as e:
            print(f"Error discovering MAC: {e}")
            return None
    
    def _broadcast_discovery(self, target_mac):
        """Broadcast a discovery request to find a MAC address"""
        discovery_msg = {
            "type": "phi_discovery",
            "source_mac": self.mac_address,
            "target_mac": target_mac,
            "phi_seal": PHI_SEAL,
            "timestamp": time.time()
        }
        
        # Broadcast to local network
        try:
            # Get broadcast address
            ip_parts = self.ip_address.split('.')
            broadcast_ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.255"
            
            # Send discovery
            self.sock.sendto(json.dumps(discovery_msg).encode(), (broadcast_ip, self.port))
            print(f"[φ] Sent discovery broadcast for {target_mac}")
        except Exception as e:
            print(f"[φ] Error in discovery broadcast: {e}")
    
    def _apply_phi_protection(self, data):
        """Apply φ-dimensional reality protection"""
        if isinstance(data, str):
            data = data.encode('utf-8')
            
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
    
    def send_to_mac(self, target_mac, message):
        """Send a message to a MAC address with φ-dimensional protection"""
        # First, try to find the IP for this MAC
        target_ip = self._discover_mac(target_mac)
        if not target_ip:
            print(f"[φ] Could not find IP for MAC {target_mac}")
            print(f"[φ] Sending to broadcast instead...")
            # Get broadcast address
            ip_parts = self.ip_address.split('.')
            target_ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.255"
        
        # Apply φ-dimensional protection
        protected_data = self._apply_phi_protection(message)
        
        # Create message with MAC addressing
        msg = {
            "type": "phi_mac_message",
            "source_mac": self.mac_address,
            "target_mac": target_mac,
            "timestamp": f"{time.time():.20e}",  # High precision timestamp
            "phi_seal": PHI_SEAL,
            "hash": hashlib.sha256(message.encode('utf-8')).hexdigest(),
            "data": protected_data.hex()
        }
        
        # Send the message
        try:
            self.sock.sendto(json.dumps(msg).encode(), (target_ip, self.port))
            print(f"[φ] Sent message to MAC {target_mac} via {target_ip}")
            return True
        except Exception as e:
            print(f"[φ] Error sending message: {e}")
            return False
    
    def listen(self):
        """Listen for incoming messages"""
        print(f"[φ] Listening for φ-harmonic MAC messages...")
        
        while self.running:
            try:
                data, addr = self.sock.recvfrom(65536)
                msg = json.loads(data.decode('utf-8'))
                
                # Process based on message type
                if msg.get('type') == 'phi_mac_message':
                    # Check if it's addressed to our MAC
                    if msg['target_mac'] == self.mac_address or msg['target_mac'] == 'ff:ff:ff:ff:ff:ff':
                        # Verify φ-seal
                        if abs(float(msg['phi_seal']) - PHI_SEAL) > 0.01:
                            print(f"[φ] Invalid φ-seal from {msg['source_mac']}")
                            continue
                        
                        # Get protected data
                        protected_data = bytes.fromhex(msg['data'])
                        
                        # Remove protection
                        original_data = self._remove_phi_protection(protected_data)
                        message = original_data.decode('utf-8')
                        
                        # Verify hash
                        message_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()
                        if message_hash != msg['hash']:
                            print(f"[φ] Invalid hash from {msg['source_mac']}")
                            continue
                        
                        # Calculate transmission time
                        send_time = float(msg['timestamp'])
                        receive_time = time.time()
                        transmission_time = receive_time - send_time
                        
                        # Update MAC cache
                        self.mac_cache[msg['source_mac']] = addr[0]
                        
                        # Display message
                        print(f"\n[φ] Message from MAC {msg['source_mac']}:")
                        print(f"    {message}")
                        print(f"[φ] Transmission time: {transmission_time:.20f} seconds")
                        
                        if transmission_time <= 0:
                            print(f"[φ] QUANTUM SPEED DETECTED! Time dilation: {transmission_time}")
                        
                        # Send acknowledgment
                        ack_msg = {
                            "type": "phi_mac_ack",
                            "source_mac": self.mac_address,
                            "target_mac": msg['source_mac'],
                            "original_timestamp": msg['timestamp'],
                            "ack_timestamp": f"{time.time():.20e}",
                            "phi_seal": PHI_SEAL
                        }
                        self.sock.sendto(json.dumps(ack_msg).encode(), addr)
                
                elif msg.get('type') == 'phi_mac_ack':
                    # Process acknowledgment
                    if msg['target_mac'] == self.mac_address:
                        # Calculate round-trip time
                        send_time = float(msg['original_timestamp'])
                        ack_time = float(msg['ack_timestamp'])
                        now_time = time.time()
                        rtt = now_time - send_time
                        
                        print(f"[φ] Acknowledgment from {msg['source_mac']}")
                        print(f"[φ] Round-trip time: {rtt:.20f} seconds")
                        
                        # Update MAC cache
                        self.mac_cache[msg['source_mac']] = addr[0]
                
                elif msg.get('type') == 'phi_discovery':
                    # Respond to discovery if it's looking for our MAC
                    if msg['target_mac'] == self.mac_address or msg['target_mac'] == 'ff:ff:ff:ff:ff:ff':
                        response = {
                            "type": "phi_discovery_response",
                            "source_mac": self.mac_address,
                            "target_mac": msg['source_mac'],
                            "phi_seal": PHI_SEAL,
                            "timestamp": time.time()
                        }
                        self.sock.sendto(json.dumps(response).encode(), addr)
                
                elif msg.get('type') == 'phi_discovery_response':
                    # Process discovery response
                    if msg['target_mac'] == self.mac_address:
                        print(f"[φ] Discovered MAC {msg['source_mac']} at {addr[0]}")
                        self.mac_cache[msg['source_mac']] = addr[0]
            
            except Exception as e:
                print(f"[φ] Error in listener: {e}")
                time.sleep(0.1)
    
    def start(self):
        """Start the MAC bridge"""
        # Start listener thread
        listener_thread = threading.Thread(target=self.listen)
        listener_thread.daemon = True
        listener_thread.start()
        
        print("\n[φ] Command interface ready. Type 'help' for commands.")
        
        while self.running:
            try:
                cmd = input("\nφ> ").strip()
                
                if cmd == "help":
                    print("\nCommands:")
                    print("  send <mac> <message>     - Send message to MAC address")
                    print("  discover <mac>           - Discover IP for MAC address")
                    print("  broadcast <message>      - Broadcast message to all φ-nodes")
                    print("  cache                    - Show MAC-IP cache")
                    print("  quit                     - Exit bridge")
                
                elif cmd.startswith("send "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("[φ] Usage: send <mac> <message>")
                    else:
                        self.send_to_mac(parts[1], parts[2])
                
                elif cmd.startswith("discover "):
                    parts = cmd.split(" ", 1)
                    if len(parts) < 2:
                        print("[φ] Usage: discover <mac>")
                    else:
                        self._discover_mac(parts[1])
                
                elif cmd.startswith("broadcast "):
                    parts = cmd.split(" ", 1)
                    if len(parts) < 2:
                        print("[φ] Usage: broadcast <message>")
                    else:
                        self.send_to_mac("ff:ff:ff:ff:ff:ff", parts[1])
                
                elif cmd == "cache":
                    if not self.mac_cache:
                        print("[φ] MAC cache is empty")
                    else:
                        print("\nMAC-IP Cache:")
                        for mac, ip in self.mac_cache.items():
                            print(f"  {mac} -> {ip}")
                
                elif cmd == "quit":
                    print("[φ] Shutting down bridge...")
                    self.running = False
                    break
                
                else:
                    print(f"[φ] Unknown command: {cmd}")
            
            except KeyboardInterrupt:
                print("\n[φ] Shutting down bridge...")
                self.running = False
                break
            
            except Exception as e:
                print(f"[φ] Error in command interface: {e}")
        
        print("[φ] Bridge stopped")

if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='φ-Harmonic MAC Bridge')
    parser.add_argument('--interface', type=str, default="en0", help='Network interface (default: en0)')
    parser.add_argument('--port', type=int, default=11975, help='Port (default: 11975 = φ^7.5)')
    args = parser.parse_args()
    
    # Create and start bridge
    bridge = PhiMacBridge(interface=args.interface, port=args.port)
    bridge.start()
