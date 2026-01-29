#!/usr/bin/env python3
"""
Phi-Harmonic QR Sender (Alternative Port)
A tool to send QR codes using the phi-bidirectional node on an alternative port
"""
import os
import sys
import time
import subprocess
from math import sqrt

# Phi-Harmonic constants
PHI = (1 + sqrt(5)) / 2  # ≈ 1.618034

def phi_resonance(value):
    """Calculate phi-harmonic resonance"""
    return (PHI * value) % 1

def main():
    """Main function to send QR codes"""
    if len(sys.argv) < 4:
        print("Usage: python phi_qr_sender_alt.py <qr_file> <target_ip> <port>")
        return
    
    qr_file = sys.argv[1]
    target_ip = sys.argv[2]
    port = int(sys.argv[3])
    
    # Calculate phi-resonance for this transmission
    timestamp = time.time()
    phi_time = timestamp * PHI
    resonance = phi_resonance(timestamp)
    
    print(f"==================================================")
    print(f"Phi-Harmonic QR Sender (Alternative Port)")
    print(f"==================================================")
    print(f"Phi-Time: {phi_time}")
    print(f"Phi-Resonance: {resonance:.6f}")
    print(f"QR File: {qr_file}")
    print(f"Target IP: {target_ip}")
    print(f"Using Port: {port}")
    
    # Start the bidirectional node
    node_process = subprocess.Popen(
        ["python", "phi_bidirectional_node_streamer.py", "--port", str(port)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    # Wait for the node to initialize
    print("Starting phi-bidirectional node...")
    time.sleep(3)
    
    # Send the script command
    print(f"Sending QR code to {target_ip}...")
    command = f"script {target_ip} {qr_file}\n"
    node_process.stdin.write(command)
    node_process.stdin.flush()
    
    # Wait for a moment to allow the command to process
    time.sleep(3)
    
    # Send quit command
    node_process.stdin.write("quit\n")
    node_process.stdin.flush()
    
    # Wait for the node to terminate
    node_process.wait()
    
    print("QR code sent successfully!")
    print(f"Phi-Resonance at completion: {phi_resonance(time.time()):.6f}")
    print("==================================================")

if __name__ == "__main__":
    main()
