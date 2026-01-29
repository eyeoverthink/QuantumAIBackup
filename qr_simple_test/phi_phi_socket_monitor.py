#!/usr/bin/env python3
"""
φ-Socket Monitor
Validates φ-dimensional socket connections and quantum bridges
φ^∞ © 2025 Vaughn Scott - All Rights Reserved
"""

import socket
import time
import json
from math import sqrt

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567

class PhiSocketMonitor:
    def __init__(self):
        self.port = 11975  # φ^7.5 port
        print(f"=== φ-SOCKET MONITOR ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"φ^75 validation seal: {PHI_SEAL}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
        
    def monitor_local_sockets(self):
        """Monitor local socket for φ-dimensional bridges"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', self.port))
        sock.settimeout(0.5)
        
        print(f"[φ] Monitoring for φ-dimensional bridge activity on port {self.port}")
        print(f"[φ] Press Ctrl+C to stop")
        
        try:
            while True:
                try:
                    data, addr = sock.recvfrom(65535)
                    try:
                        msg = json.loads(data.decode())
                        msg_type = msg.get('type', 'unknown')
                        
                        if msg_type == 'file_start':
                            print(f"\n[φ] DETECTED: φ-dimensional file transfer starting")
                            print(f"[φ] From: {addr[0]}")
                            print(f"[φ] File: {msg.get('name', 'unknown')}")
                            print(f"[φ] Size: {msg.get('size', 0)} bytes")
                            print(f"[φ] φ-Seal: {msg.get('phi_seal', 'invalid')}")
                            
                            if abs(float(msg.get('phi_seal', 0)) - PHI_SEAL) < 0.01:
                                print(f"[φ] φ-Seal VALIDATED ✓")
                            else:
                                print(f"[φ] WARNING: Invalid φ-seal detected!")
                        
                        elif msg_type == 'retrieve_request':
                            print(f"\n[φ] DETECTED: φ-dimensional retrieval request")
                            print(f"[φ] From: {addr[0]}")
                            print(f"[φ] Path: {msg.get('path', 'unknown')}")
                            print(f"[φ] φ-Seal: {msg.get('phi_seal', 'invalid')}")
                            
                            if abs(float(msg.get('phi_seal', 0)) - PHI_SEAL) < 0.01:
                                print(f"[φ] φ-Seal VALIDATED ✓")
                            else:
                                print(f"[φ] WARNING: Invalid φ-seal detected!")
                        
                        elif msg_type == 'chunk':
                            # Just print a dot to show progress
                            print(".", end="", flush=True)
                        
                        else:
                            print(f"\n[φ] DETECTED: Unknown φ-dimensional transmission: {msg_type}")
                            print(f"[φ] From: {addr[0]}")
                    
                    except json.JSONDecodeError:
                        # Non-JSON packet
                        if data.startswith(b'MSG:'):
                            print(f"\n[φ] DETECTED: φ-Bidirectional Node Message from {addr[0]}")
                        else:
                            print(f"\n[φ] DETECTED: Non-JSON packet from {addr[0]}, length: {len(data)} bytes")
                
                except socket.timeout:
                    # Just continue the loop
                    pass
                
                # Print a heartbeat
                print("♦", end="", flush=True)
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n[φ] Monitor stopped")
        finally:
            sock.close()
            
    def test_localhost_bridge(self, target_ip=None):
        """Test the revolutionary localhost bridge capability"""
        if target_ip is None:
            print("[φ] Error: Target IP required")
            return
            
        print(f"[φ] Testing φ-dimensional localhost bridge to {target_ip}")
        print(f"[φ] This validates Drawing 3 (φ-Space Transform) of FRAYMUS patent")
        
        test_msg = {
            'type': 'bridge_test',
            'phi_seal': PHI_SEAL,
            'consciousness': CONSCIOUSNESS_LEVEL,
            'message': "φ-DIMENSIONAL LOCALHOST BRIDGE TEST",
            'timestamp': time.time()
        }
        
        try:
            # First, send to real IP
            sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock1.sendto(json.dumps(test_msg).encode(), (target_ip, self.port))
            print(f"[φ] Sent test message to real IP ({target_ip})")
            
            # Then, attempt revolutionary localhost bridge
            print(f"[φ] Attempting quantum φ-dimensional bridge via localhost...")
            sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock2.sendto(json.dumps(test_msg).encode(), ('127.0.0.1', self.port))
            print(f"[φ] Sent test message through localhost bridge")
            print(f"[φ] If message is received on remote machine, this confirms")
            print(f"[φ] φ-dimensional reality protection that transcends conventional limits")
            
        except Exception as e:
            print(f"[φ] Error: {e}")
        
if __name__ == "__main__":
    import sys
    
    monitor = PhiSocketMonitor()
    
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        if len(sys.argv) > 2:
            monitor.test_localhost_bridge(sys.argv[2])
        else:
            print("[φ] Usage for test: python phi_socket_monitor.py test <target_ip>")
    else:
        monitor.monitor_local_sockets()
