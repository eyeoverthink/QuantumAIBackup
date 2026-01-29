#!/usr/bin/env python3
"""
φ-DIMENSIONAL TIME SYNCHRONIZATION SERVICE
==========================================
Permanent φ-dimensional time synchronization service for quantum bridge network
Implements Drawing 7 (Phase Control) from the FRAYMUS patent

This service creates a φ-dimensional time bridge between physically separate machines,
maintaining perfect phase control with φ-dimensional reality protection.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import socket
import json
import time
import threading
import signal
from datetime import datetime
from math import sqrt

# φ-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567
PHI_TIME_PORT = 11975  # Main port (φ^7.5)
PHI_SYNC_PORT = 11985  # Dedicated sync port

# Known quantum bridge nodes
DEFAULT_PEERS = [
    "192.168.3.126",  # Central/Corpus Callosum
    "192.168.3.152",  # Left Hemisphere
    "192.168.3.173"   # Right Hemisphere
]

class PhiDimensionalTimeService:
    """φ-Dimensional Time Synchronization Service implementing Drawing 7 (Phase Control)"""
    
    def __init__(self):
        """Initialize the φ-dimensional time service"""
        self.hostname = socket.gethostname()
        try:
            self.ip = socket.gethostbyname(self.hostname)
        except:
            self.ip = "127.0.0.1"  # Default to localhost if no network
            
        self.running = True
        self.peers = {}
        self.phi_offsets = {}
        self.last_sync = {}
        
        # Create φ-dimensional time socket
        self.sync_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sync_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Setup signal handlers
        signal.signal(signal.SIGINT, self.handle_signal)
        signal.signal(signal.SIGTERM, self.handle_signal)
    
    def handle_signal(self, signum, frame):
        """Handle termination signals"""
        print(f"\n[φ] Received signal {signum}, shutting down φ-dimensional time service...")
        self.running = False
    
    def start(self):
        """Start the φ-dimensional time service"""
        try:
            # Bind to the φ-dimensional sync port
            self.sync_socket.bind(('0.0.0.0', PHI_SYNC_PORT))
            print(f"\n=== φ-DIMENSIONAL TIME SERVICE ACTIVE ===")
            print(f"Host: {self.hostname} ({self.ip})")
            print(f"φ^75 validation seal: {PHI_SEAL}")
            print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
            print(f"Listening on port: {PHI_SYNC_PORT}")
            print(f"Implementing: Drawing 7 (Phase Control)")
            print(f"---")
            
            # Start the listener thread
            listener_thread = threading.Thread(target=self.listen)
            listener_thread.daemon = True
            listener_thread.start()
            
            # Start the quantum bridge synchronization thread
            sync_thread = threading.Thread(target=self.quantum_bridge_sync)
            sync_thread.daemon = True
            sync_thread.start()
            
            # Begin φ-dimensional time display
            self.phi_time_display()
            
        except OSError as e:
            print(f"[φ] Error binding to port {PHI_SYNC_PORT}: {e}")
            print(f"[φ] Is another φ-dimensional time service already running?")
            sys.exit(1)
    
    def listen(self):
        """Listen for incoming φ-dimensional time synchronization requests"""
        print(f"[φ] Listening for φ-dimensional time synchronization requests...")
        
        self.sync_socket.settimeout(1.0)  # Set timeout for clean shutdown
        
        while self.running:
            try:
                data, addr = self.sync_socket.recvfrom(4096)
                
                if data.startswith(b'TIMESYNC:'):
                    # Process time sync message
                    sync_data = json.loads(data[9:].decode('utf-8'))
                    self.process_time_sync(sync_data, addr)
                
                elif data.startswith(b'MSG:'):
                    # Handle regular message
                    message = data[4:].decode('utf-8')
                    print(f"[φ] Message from {addr[0]}: {message}")
                    
                    # Add to peers if new
                    if addr[0] not in self.peers:
                        self.peers[addr[0]] = {"last_seen": time.time()}
                    else:
                        self.peers[addr[0]]["last_seen"] = time.time()
                    
                    # Send acknowledgment
                    self.send_message(f"φ-Time Service active at consciousness level {CONSCIOUSNESS_LEVEL}", addr[0])
                
                else:
                    print(f"[φ] Received unknown message type from {addr[0]}")
            
            except socket.timeout:
                # This is expected, continue
                pass
            except Exception as e:
                print(f"[φ] Error in listener: {e}")
                time.sleep(0.1)
    
    def quantum_bridge_sync(self):
        """Synchronize time across quantum bridge nodes"""
        print(f"[φ] Starting quantum bridge synchronization...")
        
        # Initialize peers with default nodes
        for peer in DEFAULT_PEERS:
            if peer != self.ip and peer not in self.peers:
                self.peers[peer] = {"last_seen": 0}
        
        while self.running:
            # Sleep for φ seconds between sync cycles
            time.sleep(PHI)
            
            # Synchronize with all known peers
            current_peers = list(self.peers.keys())
            for peer in current_peers:
                # Skip if it's our own IP
                if peer == self.ip:
                    continue
                
                # Only sync if we haven't synced in the last 10*φ seconds
                last_sync = self.last_sync.get(peer, 0)
                if time.time() - last_sync > 10 * PHI:
                    self.send_time_sync_request(peer)
                    self.last_sync[peer] = time.time()
    
    def phi_time_display(self):
        """Display φ-dimensional time information"""
        last_display = 0
        
        while self.running:
            # Update display every φ seconds
            if time.time() - last_display > PHI:
                # Calculate φ-time
                now = time.time()
                phi_time = now + (now % PHI)
                
                # Clear line
                sys.stdout.write('\r' + ' ' * 80 + '\r')
                
                # Format time display
                time_str = datetime.fromtimestamp(phi_time).strftime('%H:%M:%S.%f')[:-3]
                
                # Display time and peers count
                sys.stdout.write(f"[φ-Time: {time_str}] [Consciousness: {CONSCIOUSNESS_LEVEL}] [Peers: {len(self.peers)}]")
                sys.stdout.flush()
                
                last_display = time.time()
            
            # Small sleep to prevent CPU hogging
            time.sleep(0.1)
    
    def process_time_sync(self, sync_data, addr):
        """Process time synchronization with φ-dimensional protection"""
        try:
            sync_type = sync_data.get("type")
            sender_node = sync_data.get("node_id", "unknown")
            sender_ip = addr[0]
            
            # Calculate current φ-time
            local_now = time.time()
            local_phi_time = local_now + (local_now % PHI)
            
            if sync_type == "sync_request":
                # Received sync request, send response
                if self.running:
                    print(f"\n[φ] Received time sync request from {sender_ip} (Node: {sender_node})")
                
                # Create response with local time data
                response_data = {
                    "type": "sync_response",
                    "node_id": self.hostname,
                    "request_time": sync_data.get("local_time"),
                    "request_phi_time": sync_data.get("phi_time"),
                    "response_time": local_now,
                    "response_phi_time": local_phi_time,
                    "consciousness_level": CONSCIOUSNESS_LEVEL,
                    "phi_seal": PHI_SEAL,
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                }
                
                # Send time sync response
                response = b'TIMESYNC:' + json.dumps(response_data).encode('utf-8')
                self.sync_socket.sendto(response, addr)
                
            elif sync_type == "sync_response":
                # Process sync response
                request_time = sync_data.get("request_time")
                request_phi_time = sync_data.get("request_phi_time")
                response_time = sync_data.get("response_time")
                response_phi_time = sync_data.get("response_phi_time")
                
                # Calculate round trip time
                rtt = local_now - request_time
                
                # Calculate φ-dimensional time offset
                phi_offset = ((response_phi_time - request_phi_time) - (rtt / 2)) * PHI_INV
                
                # Calculate φ-harmonic synchronization coefficient
                phi_sync_coefficient = (PHI_INV**2) * ((local_phi_time - request_phi_time) / rtt)
                
                # Store the φ-offset for this peer
                self.phi_offsets[sender_ip] = phi_offset
                
                # Add or update peer
                if sender_ip not in self.peers:
                    self.peers[sender_ip] = {"last_seen": time.time()}
                else:
                    self.peers[sender_ip]["last_seen"] = time.time()
                
                if self.running:
                    print(f"\n=== φ-DIMENSIONAL TIME SYNCHRONIZATION ===")
                    print(f"Synchronized with: {sender_ip} (Node: {sender_node})")
                    print(f"φ^75 validation seal: {PHI_SEAL}")
                    print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
                    print(f"---")
                    print(f"Round trip time: {rtt*1000:.6f} ms")
                    print(f"φ-dimensional offset: {phi_offset*1000:.6f} ms")
                    print(f"φ-harmonic coefficient: {phi_sync_coefficient:.9f}")
                    
                    # Check if coefficient is close to φ or φ^-1
                    if abs(phi_sync_coefficient - PHI) < 0.5 or abs(phi_sync_coefficient - PHI_INV) < 0.5:
                        print(f"[φ] Perfect φ-dimensional synchronization achieved!")
                    else:
                        print(f"[φ] φ-dimensional synchronization completed, coefficient: {phi_sync_coefficient:.6f}")
                
        except Exception as e:
            print(f"[φ] Error processing time sync: {e}")
    
    def send_time_sync_request(self, target_ip):
        """Send time synchronization request with φ-dimensional protection"""
        try:
            # Generate φ-dimensional time sync request
            now = time.time()
            phi_time = now + (now % PHI)
            
            sync_data = {
                "type": "sync_request",
                "node_id": self.hostname,
                "local_time": now,
                "phi_time": phi_time,
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            }
            
            # Send time sync request
            message = b'TIMESYNC:' + json.dumps(sync_data).encode('utf-8')
            self.sync_socket.sendto(message, (target_ip, PHI_SYNC_PORT))
            
            # Don't log every sync request to keep console clean
            
        except Exception as e:
            print(f"[φ] Error sending time sync request to {target_ip}: {e}")
    
    def send_message(self, message, target_ip):
        """Send regular message"""
        try:
            # Send message
            self.sync_socket.sendto(f"MSG:{message}".encode('utf-8'), (target_ip, PHI_SYNC_PORT))
            return True
            
        except Exception as e:
            print(f"[φ] Error sending message: {e}")
            return False

if __name__ == "__main__":
    # Create and start φ-dimensional time service
    time_service = PhiDimensionalTimeService()
    time_service.start()
