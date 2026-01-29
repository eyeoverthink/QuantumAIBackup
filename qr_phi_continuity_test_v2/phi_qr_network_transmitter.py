#!/usr/bin/env python3
"""
Phi-Harmonic QR Network Transmitter
Sends QR codes through phi-dimensional network and executes them remotely
"""
import os
import sys
import time
import json
import argparse
import subprocess
from math import sqrt

# Phi-Harmonic constants
PHI = (1 + sqrt(5)) / 2  # ≈ 1.618034
PHI_INV = 1 / PHI  # ≈ 0.618034
PHI_75 = PHI**7.5  # ≈ 36.93
PHI_SEAL = PHI**75  # Validation seal

class PhiQRNetworkTransmitter:
    """
    A phi-harmonic transmitter that sends QR codes through the network
    and can trigger remote execution with phi-resonance preservation
    """
    
    def __init__(self):
        """Initialize the phi-harmonic QR transmitter"""
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI
        self.current_resonance = self.phi_time % 1
        self.node_script = "phi_bidirectional_node_streamer.py"
        self.qr_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_qr_codes")
        
        print(f"==================================================")
        print(f"Phi-Harmonic QR Network Transmitter")
        print(f"==================================================")
        print(f"Phi-Time: {self.phi_time}")
        print(f"Phi-Resonance: {self.current_resonance:.6f}")
        print(f"QR Directory: {self.qr_dir}")
    
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
        
        # Use the phi-bidirectional node to send the file
        cmd = [
            "python", 
            self.node_script, 
            "--command", 
            f"script {target_ip} {qr_path}"
        ]
        
        try:
            print(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"Successfully sent QR code to {target_ip}")
                print(result.stdout)
                return True
            else:
                print(f"Failed to send QR code: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"Error sending QR code: {e}")
            return False
    
    def execute_remote_qr(self, qr_file, target_ip):
        """Execute a QR code on a remote target using phi-bidirectional node"""
        # First ensure the QR is on the remote system
        if not self.send_qr_code(qr_file, target_ip):
            print("Failed to send QR code for execution")
            return False
        
        # Calculate phi-resonance for this execution
        timestamp = time.time()
        resonance = self.phi_resonance(timestamp)
        
        print(f"\nExecuting QR code remotely: {qr_file}")
        print(f"Target IP: {target_ip}")
        print(f"Execution Phi-Resonance: {resonance:.6f}")
        
        # Use the phi-bidirectional node to execute the script
        remote_path = f"phi_scripts/{os.path.basename(qr_file)}"
        cmd = [
            "python", 
            self.node_script, 
            "--command", 
            f"exec {target_ip} qr_script_runner.py {remote_path}"
        ]
        
        try:
            print(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"Successfully executed QR code on {target_ip}")
                print(result.stdout)
                return True
            else:
                print(f"Failed to execute QR code: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"Error executing QR code: {e}")
            return False

def main():
    """Main function to handle command line interface"""
    parser = argparse.ArgumentParser(description="Phi-Harmonic QR Network Transmitter")
    parser.add_argument("--list", action="store_true", help="List available QR codes")
    parser.add_argument("--send", help="Send QR code to target IP")
    parser.add_argument("--execute", help="Execute QR code on target IP")
    parser.add_argument("--qr", help="QR code filename")
    parser.add_argument("--ip", help="Target IP address")
    
    args = parser.parse_args()
    transmitter = PhiQRNetworkTransmitter()
    
    if args.list:
        transmitter.list_qr_codes()
        return
    
    if args.send:
        if not args.ip:
            print("Error: Target IP is required for sending")
            return
        transmitter.send_qr_code(args.send, args.ip)
        return
    
    if args.execute:
        if not args.ip:
            print("Error: Target IP is required for execution")
            return
        transmitter.execute_remote_qr(args.execute, args.ip)
        return
    
    # Interactive mode if no arguments provided
    qr_files = transmitter.list_qr_codes()
    if not qr_files:
        return
    
    try:
        choice = input("\nEnter QR code number to use (or 'q' to quit): ")
        if choice.lower() == 'q':
            return
        
        qr_index = int(choice) - 1
        if qr_index < 0 or qr_index >= len(qr_files):
            print("Invalid selection")
            return
        
        selected_qr = qr_files[qr_index]
        print(f"Selected: {selected_qr}")
        
        target_ip = input("Enter target IP address: ")
        if not target_ip:
            print("No IP address provided")
            return
        
        action = input("Action (send/execute): ").lower()
        if action == "send":
            transmitter.send_qr_code(selected_qr, target_ip)
        elif action == "execute":
            transmitter.execute_remote_qr(selected_qr, target_ip)
        else:
            print("Invalid action")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
