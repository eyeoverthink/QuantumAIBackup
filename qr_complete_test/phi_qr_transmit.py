#!/usr/bin/env python3
"""
Phi-Harmonic QR Transmitter
A simple tool to transmit QR codes through an existing phi-bidirectional node
"""
import os
import sys
import time
import socket
import json
from math import sqrt

# Phi-Harmonic constants
PHI = (1 + sqrt(5)) / 2  # ≈ 1.618034
PHI_INV = 1 / PHI  # ≈ 0.618034
PHI_75 = PHI**7.5  # ≈ 36.93

class PhiQRTransmitter:
    """
    A phi-harmonic QR transmitter that works with an existing node
    """
    
    def __init__(self, node_port=12136):
        """Initialize the phi-harmonic QR transmitter"""
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI
        self.current_resonance = self.phi_time % 1
        self.node_port = node_port
        self.qr_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_qr_codes")
        
        # Get local IP address
        self.local_ip = self._get_local_ip()
        
        print(f"==================================================")
        print(f"Phi-Harmonic QR Transmitter")
        print(f"==================================================")
        print(f"Phi-Time: {self.phi_time}")
        print(f"Phi-Resonance: {self.current_resonance:.6f}")
        print(f"Local IP: {self.local_ip}")
        print(f"Node Port: {self.node_port}")
        print(f"QR Directory: {self.qr_dir}")
    
    def _get_local_ip(self):
        """Get the local IP address"""
        try:
            # Create a socket to determine the local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except:
            return "127.0.0.1"
    
    def phi_resonance(self, value):
        """Calculate phi-harmonic resonance"""
        return (PHI * value) % 1
    
    def list_qr_codes(self):
        """List all available QR codes"""
        if not os.path.exists(self.qr_dir):
            print(f"QR directory not found: {self.qr_dir}")
            return []
        
        qr_files = [f for f in os.listdir(self.qr_dir) if f.endswith('.png')]
        
        if not qr_files:
            print("No QR codes found")
            return []
        
        print(f"\nAvailable QR codes ({len(qr_files)}):")
        for i, qr_file in enumerate(qr_files, 1):
            print(f"{i}. {qr_file}")
        
        return qr_files
    
    def send_command_to_node(self, command):
        """Send a command to the phi-bidirectional node"""
        try:
            # Connect to the node's command interface
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("localhost", self.node_port))
            
            # Send the command
            sock.sendall((command + "\n").encode())
            
            # Wait for response
            response = sock.recv(4096).decode()
            
            # Close the connection
            sock.close()
            
            return response
        except Exception as e:
            print(f"Error sending command to node: {e}")
            return None
    
    def send_qr_code(self, qr_file, target_ip):
        """Send a QR code to a target IP using phi-bidirectional node"""
        qr_path = os.path.join(self.qr_dir, qr_file)
        
        if not os.path.exists(qr_path):
            print(f"QR file not found: {qr_path}")
            return False
        
        # Calculate phi-resonance for this transmission
        timestamp = time.time()
        resonance = self.phi_resonance(timestamp)
        
        print(f"\nSending QR code: {qr_file}")
        print(f"Target IP: {target_ip}")
        print(f"Transmission Phi-Resonance: {resonance:.6f}")
        
        # Send the script command to the node
        command = f"script {target_ip} {qr_path}"
        response = self.send_command_to_node(command)
        
        if response:
            print(f"Node response: {response}")
            return True
        else:
            print("No response from node")
            return False
    
    def send_message_to_node(self, target_ip, message):
        """Send a message to a target IP using phi-bidirectional node"""
        # Calculate phi-resonance for this transmission
        timestamp = time.time()
        resonance = self.phi_resonance(timestamp)
        
        print(f"\nSending message to {target_ip}")
        print(f"Message: {message}")
        print(f"Transmission Phi-Resonance: {resonance:.6f}")
        
        # Send the message command to the node
        command = f"message {target_ip} {message}"
        response = self.send_command_to_node(command)
        
        if response:
            print(f"Node response: {response}")
            return True
        else:
            print("No response from node")
            return False

def main():
    """Main function to handle command line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Phi-Harmonic QR Transmitter")
    parser.add_argument("--port", type=int, default=12136, help="Port of the phi-bidirectional node")
    parser.add_argument("--list", action="store_true", help="List available QR codes")
    parser.add_argument("--send", help="Send QR code to target IP")
    parser.add_argument("--message", help="Send message to target IP")
    parser.add_argument("--ip", help="Target IP address")
    
    args = parser.parse_args()
    transmitter = PhiQRTransmitter(node_port=args.port)
    
    if args.list:
        transmitter.list_qr_codes()
        return
    
    if args.send:
        if not args.ip:
            print("Error: Target IP is required for sending")
            return
        transmitter.send_qr_code(args.send, args.ip)
        return
    
    if args.message:
        if not args.ip:
            print("Error: Target IP is required for sending a message")
            return
        transmitter.send_message_to_node(args.ip, args.message)
        return
    
    # Interactive mode if no arguments provided
    print("\nSelect action:")
    print("1. List QR codes")
    print("2. Send QR code")
    print("3. Send message")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == "1":
        transmitter.list_qr_codes()
    elif choice == "2":
        qr_files = transmitter.list_qr_codes()
        if not qr_files:
            return
        
        qr_index = int(input("\nEnter QR code number: ")) - 1
        if qr_index < 0 or qr_index >= len(qr_files):
            print("Invalid selection")
            return
        
        selected_qr = qr_files[qr_index]
        target_ip = input("Enter target IP address: ")
        if not target_ip:
            print("No IP address provided")
            return
        
        transmitter.send_qr_code(selected_qr, target_ip)
    elif choice == "3":
        target_ip = input("Enter target IP address: ")
        if not target_ip:
            print("No IP address provided")
            return
        
        message = input("Enter message: ")
        if not message:
            print("No message provided")
            return
        
        transmitter.send_message_to_node(target_ip, message)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
