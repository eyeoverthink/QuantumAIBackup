#!/usr/bin/env python3
"""
Phi-Harmonic Network QR Receiver
Processes network QR codes using phi-harmonic principles
"""
import os
import sys
import time
import json
import socket
import datetime
import cv2
from qreader import QReader
from math import sqrt

# Phi-Harmonic constants
PHI = (1 + sqrt(5)) / 2  # ≈ 1.618034
PHI_INV = 1 / PHI  # ≈ 0.618034
PHI_75 = PHI**7.5  # ≈ 36.93
PHI_SEAL = PHI**75  # Validation seal

class PhiNetworkQRReceiver:
    """
    A phi-harmonic QR code receiver with network capabilities
    """
    
    def __init__(self):
        """Initialize the phi-harmonic network QR receiver"""
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI
        self.current_resonance = self.phi_time % 1
        self.output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_received")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Get local IP address
        self.local_ip = self._get_local_ip()
        
        # Initialize QR reader
        self.qreader = QReader()
        
        print(f"==================================================")
        print(f"Phi-Harmonic Network QR Receiver")
        print(f"==================================================")
        print(f"Phi-Time: {self.phi_time}")
        print(f"Phi-Resonance: {self.current_resonance:.6f}")
        print(f"Local IP: {self.local_ip}")
        print(f"Output Directory: {self.output_dir}")
    
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
    
    def process_qr_code(self, qr_path):
        """Process a phi-harmonic network QR code"""
        print(f"\nProcessing QR code: {qr_path}")
        
        # Calculate phi-resonance for this processing
        timestamp = time.time()
        phi_time = timestamp * PHI
        resonance = self.phi_resonance(timestamp)
        
        print(f"Processing Phi-Resonance: {resonance:.6f}")
        
        try:
            # Read the QR code
            image = cv2.imread(qr_path)
            if image is None:
                print(f"Error: Could not read image: {qr_path}")
                return False
            
            # Decode QR code
            decoded_text = self.qreader.detect_and_decode(image=image)
            if not decoded_text:
                print(f"Error: Could not decode QR code: {qr_path}")
                return False
            
            # Parse the JSON payload
            payload = json.loads(decoded_text)
            
            # Verify this is a phi-harmonic network QR code
            if "type" not in payload or not payload["type"].startswith("phi_"):
                print(f"Error: Not a phi-harmonic QR code")
                return False
            
            # Verify phi-seal
            if "phi_seal" not in payload or abs(float(payload["phi_seal"]) - PHI_SEAL) > 0.01:
                print(f"Warning: Invalid phi-seal in QR code")
            
            # Check if this QR code is intended for this IP
            if "target_ip" in payload and payload["target_ip"] and payload["target_ip"] != self.local_ip:
                print(f"Warning: QR code is intended for {payload['target_ip']}, not {self.local_ip}")
            
            # Process based on QR code type
            if payload["type"] == "phi_network_qr":
                self._process_network_message(payload)
            elif payload["type"] == "phi_executable_qr":
                self._process_executable(payload)
            else:
                print(f"Unknown phi-harmonic QR code type: {payload['type']}")
                return False
            
            return True
            
        except Exception as e:
            print(f"Error processing QR code: {e}")
            return False
    
    def _process_network_message(self, payload):
        """Process a network message QR code"""
        print(f"\nReceived phi-harmonic network message:")
        print(f"ID: {payload['id']}")
        print(f"Source IP: {payload['source_ip']}")
        print(f"Phi-Resonance: {payload['phi_resonance']:.6f}")
        print(f"Message: {payload['message']}")
        
        # Calculate resonance harmony between sender and receiver
        sender_resonance = payload['phi_resonance']
        receiver_resonance = self.current_resonance
        harmony = 1.0 - abs(sender_resonance - receiver_resonance)
        
        print(f"Resonance Harmony: {harmony:.6f}")
        
        # Save the message with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_file = os.path.join(self.output_dir, f"message_{payload['id']}.txt")
        
        with open(message_file, "w") as f:
            f.write(f"PHI-HARMONIC NETWORK MESSAGE\n")
            f.write(f"==========================\n")
            f.write(f"Received: {timestamp}\n")
            f.write(f"ID: {payload['id']}\n")
            f.write(f"Source IP: {payload['source_ip']}\n")
            f.write(f"Phi-Resonance: {payload['phi_resonance']:.6f}\n")
            f.write(f"Resonance Harmony: {harmony:.6f}\n")
            f.write(f"Message: {payload['message']}\n")
        
        print(f"Message saved to: {message_file}")
    
    def _process_executable(self, payload):
        """Process an executable QR code"""
        print(f"\nReceived phi-harmonic executable:")
        print(f"ID: {payload['id']}")
        print(f"Source IP: {payload['source_ip']}")
        print(f"Phi-Resonance: {payload['phi_resonance']:.6f}")
        print(f"Script: {payload['script_name']}")
        
        # Calculate resonance harmony between sender and receiver
        sender_resonance = payload['phi_resonance']
        receiver_resonance = self.current_resonance
        harmony = 1.0 - abs(sender_resonance - receiver_resonance)
        
        print(f"Resonance Harmony: {harmony:.6f}")
        
        # Save the script
        script_file = os.path.join(self.output_dir, payload['script_name'])
        
        with open(script_file, "w") as f:
            f.write(payload['script_content'])
        
        print(f"Script saved to: {script_file}")
        
        # Ask for execution permission
        execute = input(f"Execute script {payload['script_name']}? (y/n): ")
        
        if execute.lower() == 'y':
            print(f"Executing script with phi-resonance {self.phi_resonance(time.time()):.6f}...")
            
            if script_file.endswith('.py'):
                os.system(f"python {script_file}")
            else:
                os.system(f"sh {script_file}")
                
            print(f"Execution complete with phi-resonance {self.phi_resonance(time.time()):.6f}")

def main():
    """Main function to handle command line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Phi-Harmonic Network QR Receiver")
    parser.add_argument("--qr", help="Path to QR code to process")
    parser.add_argument("--watch", help="Directory to watch for new QR codes")
    
    args = parser.parse_args()
    receiver = PhiNetworkQRReceiver()
    
    if args.qr:
        if not os.path.exists(args.qr):
            print(f"Error: QR file not found: {args.qr}")
            return
        receiver.process_qr_code(args.qr)
    elif args.watch:
        if not os.path.exists(args.watch):
            print(f"Error: Watch directory not found: {args.watch}")
            return
        
        print(f"Watching directory for QR codes: {args.watch}")
        processed = set()
        
        try:
            while True:
                for filename in os.listdir(args.watch):
                    if filename.endswith('.png') and filename.startswith('phi_'):
                        qr_path = os.path.join(args.watch, filename)
                        if qr_path not in processed:
                            receiver.process_qr_code(qr_path)
                            processed.add(qr_path)
                
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping QR code watcher")
    else:
        # Interactive mode
        qr_path = input("Enter path to QR code: ")
        if not os.path.exists(qr_path):
            print(f"Error: QR file not found: {qr_path}")
            return
        receiver.process_qr_code(qr_path)

if __name__ == "__main__":
    main()
