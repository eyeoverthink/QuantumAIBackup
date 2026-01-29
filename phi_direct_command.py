#!/usr/bin/env python3
"""
Phi-Harmonic Direct Command
Sends direct commands to a running phi-bidirectional node using UDP
"""
import os
import sys
import time
import socket
from math import sqrt

# Phi-Harmonic constants
PHI = (1 + sqrt(5)) / 2  # ≈ 1.618034
PHI_INV = 1 / PHI  # ≈ 0.618034
PHI_75 = PHI**7.5  # ≈ 36.93

def phi_resonance(value):
    """Calculate phi-harmonic resonance"""
    return (PHI * value) % 1

def send_command(command, target_ip="127.0.0.1", port=11974):
    """Send a direct command to a phi-bidirectional node"""
    # Calculate phi-resonance for this transmission
    timestamp = time.time()
    resonance = phi_resonance(timestamp)
    
    print(f"==================================================")
    print(f"Phi-Harmonic Direct Command")
    print(f"==================================================")
    print(f"Phi-Time: {timestamp * PHI}")
    print(f"Phi-Resonance: {resonance:.6f}")
    print(f"Target IP: {target_ip}")
    print(f"Port: {port}")
    print(f"Command: {command}")
    
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Format command with COMMAND: prefix for the node to recognize
    message = f"COMMAND:{command}".encode('utf-8')
    
    try:
        # Send command to the node
        sock.sendto(message, (target_ip, port))
        print(f"Command sent successfully!")
        
        # Wait for response (optional)
        sock.settimeout(5)
        try:
            response, addr = sock.recvfrom(65536)
            print(f"Response from {addr}: {response.decode('utf-8')}")
        except socket.timeout:
            print("No response received (timeout)")
    except Exception as e:
        print(f"Error sending command: {e}")
    finally:
        sock.close()
    
    print(f"Phi-Resonance at completion: {phi_resonance(time.time()):.6f}")
    print("==================================================")

def main():
    """Main function to handle command line arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Phi-Harmonic Direct Command")
    parser.add_argument("--command", help="Command to send to the node")
    parser.add_argument("--ip", default="127.0.0.1", help="Target IP address")
    parser.add_argument("--port", type=int, default=11974, help="Target port")
    parser.add_argument("--script", help="Script file to send")
    parser.add_argument("--target", help="Target IP for script execution")
    
    args = parser.parse_args()
    
    if args.command:
        send_command(args.command, args.ip, args.port)
    elif args.script and args.target:
        script_command = f"script {args.target} {args.script}"
        send_command(script_command, args.ip, args.port)
    else:
        # Interactive mode
        command = input("Enter command to send: ")
        ip = input("Enter target IP [127.0.0.1]: ") or "127.0.0.1"
        port_str = input("Enter target port [11974]: ") or "11974"
        port = int(port_str)
        
        send_command(command, ip, port)

if __name__ == "__main__":
    main()
