#!/usr/bin/env python3
"""
Phi-Harmonic Network QR Generator
Creates QR codes with network execution capabilities using phi-harmonic principles
"""
import os
import sys
import time
import json
import qrcode
import socket
import uuid
from math import sqrt

# Phi-Harmonic constants
PHI = (1 + sqrt(5)) / 2  # ≈ 1.618034
PHI_INV = 1 / PHI  # ≈ 0.618034
PHI_75 = PHI**7.5  # ≈ 36.93
PHI_SEAL = PHI**75  # Validation seal

class PhiNetworkQRGenerator:
    """
    A phi-harmonic QR code generator with network execution capabilities
    """
    
    def __init__(self):
        """Initialize the phi-harmonic network QR generator"""
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI
        self.current_resonance = self.phi_time % 1
        self.qr_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_qr_codes")
        os.makedirs(self.qr_dir, exist_ok=True)
        
        # Get local IP address
        self.local_ip = self._get_local_ip()
        
        print(f"==================================================")
        print(f"Phi-Harmonic Network QR Generator")
        print(f"==================================================")
        print(f"Phi-Time: {self.phi_time}")
        print(f"Phi-Resonance: {self.current_resonance:.6f}")
        print(f"Local IP: {self.local_ip}")
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
    
    def create_network_qr(self, message, target_ip=None):
        """Create a QR code with network execution capabilities"""
        # Generate a unique ID for this QR code
        qr_id = str(uuid.uuid4())[:8]
        
        # Calculate phi-resonance for this QR code
        timestamp = time.time()
        phi_time = timestamp * PHI
        resonance = self.phi_resonance(timestamp)
        
        # Create the network payload
        payload = {
            "type": "phi_network_qr",
            "id": qr_id,
            "source_ip": self.local_ip,
            "target_ip": target_ip,
            "message": message,
            "phi_time": phi_time,
            "phi_resonance": resonance,
            "phi_seal": PHI_SEAL,
            "timestamp": timestamp
        }
        
        # Convert payload to JSON
        qr_data = json.dumps(payload)
        
        # Create QR code
        qr = qrcode.QRCode(
            version=10,  # Fixed version for consistent size
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Create QR image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save QR code
        timestamp_int = int(timestamp)
        qr_file = os.path.join(self.qr_dir, f"phi_network_qr_{qr_id}_{timestamp_int}.png")
        img.save(qr_file)
        
        print(f"\nCreated phi-harmonic network QR code:")
        print(f"ID: {qr_id}")
        print(f"Phi-Resonance: {resonance:.6f}")
        print(f"Source IP: {self.local_ip}")
        print(f"Target IP: {target_ip or 'Any'}")
        print(f"Message: {message}")
        print(f"Saved to: {qr_file}")
        
        return qr_file, payload
    
    def create_executable_qr(self, script_path, target_ip=None):
        """Create a QR code that can execute a script remotely using a reference-based approach"""
        # Get the script filename and absolute path
        script_name = os.path.basename(script_path)
        script_abs_path = os.path.abspath(script_path)
        
        # Generate a unique ID for this QR code
        qr_id = str(uuid.uuid4())[:8]
        
        # Calculate phi-resonance for this QR code
        timestamp = time.time()
        phi_time = timestamp * PHI
        resonance = self.phi_resonance(timestamp)
        
        # Create the executable payload with reference instead of content
        payload = {
            "type": "phi_executable_qr",
            "id": qr_id,
            "source_ip": self.local_ip,
            "target_ip": target_ip,
            "script_name": script_name,
            "script_path": script_abs_path,  # Store path instead of content
            "execution_command": f"python {script_name}",  # Command to execute
            "phi_time": phi_time,
            "phi_resonance": resonance,
            "phi_seal": PHI_SEAL,
            "timestamp": timestamp
        }
        
        # Convert payload to JSON
        qr_data = json.dumps(payload)
        
        # Create QR code
        qr = qrcode.QRCode(
            version=None,  # Auto-determine version
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Create QR image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save QR code
        timestamp_int = int(timestamp)
        qr_file = os.path.join(self.qr_dir, f"phi_exec_qr_{qr_id}_{timestamp_int}.png")
        img.save(qr_file)
        
        print(f"\nCreated phi-harmonic executable QR code:")
        print(f"ID: {qr_id}")
        print(f"Phi-Resonance: {resonance:.6f}")
        print(f"Source IP: {self.local_ip}")
        print(f"Target IP: {target_ip or 'Any'}")
        print(f"Script: {script_name}")
        print(f"Script Path: {script_abs_path}")
        print(f"Execution Command: python {script_name}")
        print(f"Saved to: {qr_file}")
        
        # Also copy the script to the QR directory for easy transfer
        script_copy = os.path.join(self.qr_dir, script_name)
        with open(script_path, 'r') as src, open(script_copy, 'w') as dst:
            dst.write(src.read())
        print(f"Script copied to: {script_copy}")
        
        return qr_file, payload

def main():
    """Main function to handle command line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Phi-Harmonic Network QR Generator")
    parser.add_argument("--message", help="Create a network message QR code")
    parser.add_argument("--script", help="Path to script to encode in QR")
    parser.add_argument("--target", help="Target IP address (optional)")
    
    args = parser.parse_args()
    generator = PhiNetworkQRGenerator()
    
    if args.message:
        generator.create_network_qr(args.message, args.target)
    elif args.script:
        if not os.path.exists(args.script):
            print(f"Error: Script file not found: {args.script}")
            return
        generator.create_executable_qr(args.script, args.target)
    else:
        # Interactive mode
        print("\nSelect QR code type:")
        print("1. Network Message QR")
        print("2. Executable Script QR")
        
        choice = input("Enter choice (1/2): ")
        
        if choice == "1":
            message = input("Enter message: ")
            target = input("Enter target IP (optional): ")
            target = target if target else None
            generator.create_network_qr(message, target)
        elif choice == "2":
            script_path = input("Enter script path: ")
            if not os.path.exists(script_path):
                print(f"Error: Script file not found: {script_path}")
                return
            target = input("Enter target IP (optional): ")
            target = target if target else None
            generator.create_executable_qr(script_path, target)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
