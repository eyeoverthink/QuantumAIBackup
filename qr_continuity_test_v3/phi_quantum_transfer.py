#!/usr/bin/env python3
"""
φ-Quantum Transfer Test
Demonstrates direct data transfer between Macs through φ-dimensional quantum bridge
"""

import os
import time
import platform
import socket
import json
import threading
import random
import sys
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

class PhiQuantumTransfer:
    """
    φ-Quantum Transfer for direct data exchange through φ-dimensional reality protection
    """
    def __init__(self, node_id, target_ip=None, consciousness_level=0.7567):
        self.node_id = node_id
        self.target_ip = target_ip
        self.consciousness_level = consciousness_level
        self.port = 11974  # φ^7.5 - 1 (to avoid conflict with bidirectional node)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.port))
        self.running = True
        self.quantum_state = {}
        self.transfer_complete = False
        
        # Initialize φ-dimensional quantum state
        self.quantum_state["phi_seal"] = PHI_SEAL
        self.quantum_state["consciousness"] = self.consciousness_level
        self.quantum_state["node_id"] = self.node_id
        
        print(f"\n=== φ-QUANTUM TRANSFER NODE {node_id} ===")
        print(f"Running on: {platform.node()}")
        print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Port: {self.port} (φ^7.5 - 1)")
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Consciousness level: {self.consciousness_level}")
        
        if target_ip:
            print(f"Target IP: {target_ip}")
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self.receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
    
    def send_data(self, data_type, content):
        """Send data through φ-dimensional quantum bridge"""
        if not self.target_ip:
            print("No target IP specified. Use set_target_ip(ip) first.")
            return False
        
        # Create φ-protected data packet
        data_packet = {
            "type": data_type,
            "content": content,
            "node_id": self.node_id,
            "timestamp": time.time(),
            "phi_seal": PHI_SEAL,
            "consciousness": self.consciousness_level
        }
        
        # Send through quantum bridge
        message = f"QUANTUM_DATA:{json.dumps(data_packet)}"
        try:
            self.socket.sendto(message.encode('utf-8'), (self.target_ip, self.port))
            print(f"Sent {data_type} to {self.target_ip} through φ-dimensional quantum bridge")
            return True
        except Exception as e:
            print(f"Error sending data: {e}")
            return False
    
    def set_target_ip(self, ip):
        """Set target IP for quantum transfer"""
        self.target_ip = ip
        print(f"Target IP set to {ip}")
    
    def receive_messages(self):
        """Receive messages through φ-dimensional quantum bridge"""
        while self.running:
            try:
                data, addr = self.socket.recvfrom(4096)
                sender_ip = addr[0]
                message = data.decode('utf-8')
                
                # Process message based on type
                if message.startswith("QUANTUM_DATA:"):
                    data_json = message[13:]
                    data_packet = json.loads(data_json)
                    
                    data_type = data_packet.get("type", "unknown")
                    content = data_packet.get("content", "")
                    node_id = data_packet.get("node_id", "unknown")
                    phi_seal = data_packet.get("phi_seal", 0)
                    
                    # Verify φ^75 validation seal
                    if abs(phi_seal - PHI_SEAL) < 0.01:
                        print(f"\nReceived {data_type} from Node {node_id} ({sender_ip}) through φ-dimensional quantum bridge")
                        
                        if data_type == "TEXT":
                            print(f"Content: {content}")
                        
                        elif data_type == "FILE_REQUEST":
                            self.handle_file_request(sender_ip, content)
                        
                        elif data_type == "FILE_DATA":
                            self.handle_file_data(content)
                        
                        # Send acknowledgment
                        ack_packet = {
                            "type": "ACK",
                            "for": data_type,
                            "node_id": self.node_id,
                            "timestamp": time.time(),
                            "phi_seal": PHI_SEAL
                        }
                        ack_message = f"QUANTUM_DATA:{json.dumps(ack_packet)}"
                        self.socket.sendto(ack_message.encode('utf-8'), (sender_ip, self.port))
                    else:
                        print(f"\nInvalid φ^75 validation seal from {sender_ip}: {phi_seal}")
                
                else:
                    print(f"\nUnknown message type from {sender_ip}: {message[:20]}...")
            
            except Exception as e:
                if self.running:
                    print(f"Error receiving message: {e}")
    
    def handle_file_request(self, sender_ip, filename):
        """Handle request for file transfer"""
        try:
            # Check if file exists
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    content = f.read()
                
                # Send file data
                file_data = {
                    "filename": os.path.basename(filename),
                    "content": content
                }
                
                # Set target IP to sender
                original_target = self.target_ip
                self.set_target_ip(sender_ip)
                
                # Send file data
                self.send_data("FILE_DATA", file_data)
                
                # Restore original target
                self.set_target_ip(original_target)
                
                print(f"Sent file {filename} to {sender_ip} through φ-dimensional quantum bridge")
            else:
                print(f"File {filename} not found")
        
        except Exception as e:
            print(f"Error handling file request: {e}")
    
    def handle_file_data(self, file_data):
        """Handle incoming file data"""
        try:
            filename = file_data.get("filename", f"quantum_received_{int(time.time())}.txt")
            content = file_data.get("content", "")
            
            # Save file
            with open(filename, 'w') as f:
                f.write(content)
            
            print(f"Received and saved file {filename} through φ-dimensional quantum bridge")
            self.transfer_complete = True
        
        except Exception as e:
            print(f"Error handling file data: {e}")
    
    def request_file(self, filename):
        """Request a file through φ-dimensional quantum bridge"""
        return self.send_data("FILE_REQUEST", filename)
    
    def send_text(self, text):
        """Send text through φ-dimensional quantum bridge"""
        return self.send_data("TEXT", text)
    
    def wait_for_transfer(self, timeout=30):
        """Wait for transfer to complete"""
        start_time = time.time()
        while not self.transfer_complete and time.time() - start_time < timeout:
            time.sleep(0.1)
        
        if self.transfer_complete:
            print("Transfer completed successfully")
            return True
        else:
            print("Transfer timed out")
            return False
    
    def stop(self):
        """Stop the quantum transfer node"""
        self.running = False
        print("Stopping φ-quantum transfer node...")

def main():
    """Main function to run φ-quantum transfer"""
    if len(sys.argv) < 2:
        print("Usage: python phi_quantum_transfer.py <node_id> [target_ip] [mode] [data]")
        print("Modes: text, request_file")
        print("Example (send text): python phi_quantum_transfer.py 1 192.168.3.152 text \"Hello through φ-space\"")
        print("Example (request file): python phi_quantum_transfer.py 1 192.168.3.152 request_file phi_scripts/phi_reality_test.py")
        return
    
    node_id = sys.argv[1]
    target_ip = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Create quantum transfer node
    transfer = PhiQuantumTransfer(node_id, target_ip)
    
    # Process command line arguments
    if len(sys.argv) > 3:
        mode = sys.argv[3]
        
        if mode == "text" and len(sys.argv) > 4:
            transfer.send_text(sys.argv[4])
        
        elif mode == "request_file" and len(sys.argv) > 4:
            transfer.request_file(sys.argv[4])
            transfer.wait_for_transfer()
    
    # Keep running to receive messages
    print("\nNode is running. Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        transfer.stop()

if __name__ == "__main__":
    main()
