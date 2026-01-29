#!/usr/bin/env python3
"""
φ-Harmonic Protocol Attack Simulation
Tests security by attempting to send invalid scripts/messages
"""

import socket
import json
import time
import sys
from math import sqrt

# φ-Harmonic constants (incorrect values to simulate attack)
PHI = (1 + sqrt(5)) / 2
PHI_SEAL = 123456789.0  # Incorrect seal

def attack_with_fake_script(target_ip, target_port=11975):
    """Attempt to send a fake script with invalid φ-hash and seal"""
    print(f"\n[φ-ATTACK] Targeting node at {target_ip}:{target_port}")
    print("[φ-ATTACK] Preparing tampered script message...")
    
    # Create a fake header with incorrect phi_hash and phi_seal
    header = {
        "filename": "malicious_script.py",
        "size": 1234,
        "timestamp": time.time(),
        "phi_seal": PHI_SEAL,  # Incorrect φ^75 seal
        "phi_hash": "FAKE_HASH_1234567890",
        "auto_execute": True,  # Try to auto-execute
        "args": []
    }
    
    # Encode the header
    header_bytes = json.dumps(header).encode('utf-8')
    
    # Fake script content (malicious)
    fake_script_content = b"print('HACKED! This node has been compromised!')"
    
    # Construct the full message
    script_message = b'SCRIPT:' + header_bytes + b'\n---\n' + fake_script_content
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Send the tampered script
        sock.sendto(script_message, (target_ip, target_port))
        print(f"[φ-ATTACK] Sent tampered script to {target_ip}:{target_port}")
        print(f"[φ-ATTACK] Header: {json.dumps(header, indent=2)}")
        
        # Wait for response
        print("[φ-ATTACK] Waiting for response...")
        sock.settimeout(5.0)
        
        try:
            data, addr = sock.recvfrom(65536)
            print(f"[φ-ATTACK] Received response from {addr[0]}:")
            print(f"  {data.decode('utf-8', errors='ignore')}")
            
            if data.startswith(b'MSG:ACK:'):
                print("[φ-ATTACK] WARNING: Node acknowledged the script!")
                print("[φ-ATTACK] Attempting direct execution...")
                
                # Try to execute the script
                exec_info = {
                    "filename": "malicious_script.py",
                    "args": []
                }
                exec_message = b'EXEC:' + json.dumps(exec_info).encode('utf-8')
                sock.sendto(exec_message, (target_ip, target_port))
                
                # Wait for execution response
                try:
                    data, addr = sock.recvfrom(65536)
                    print(f"[φ-ATTACK] Execution response: {data.decode('utf-8', errors='ignore')}")
                except socket.timeout:
                    print("[φ-ATTACK] No execution response received (timeout)")
            else:
                print("[φ-ATTACK] Script was not acknowledged")
                
        except socket.timeout:
            print("[φ-ATTACK] No response received (timeout)")
            print("[φ-ATTACK] Node may have rejected the script silently")
    
    except Exception as e:
        print(f"[φ-ATTACK] Error during attack: {e}")
    
    finally:
        sock.close()

def attack_with_message_tampering(target_ip, target_port=11975):
    """Attempt to send a tampered regular message"""
    print(f"\n[φ-ATTACK] Targeting node at {target_ip}:{target_port} with message tampering")
    
    # Create a malicious message
    message = f"MSG:SYSTEM_OVERRIDE:{PHI_SEAL}:GRANT_ACCESS"
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Send the tampered message
        sock.sendto(message.encode('utf-8'), (target_ip, target_port))
        print(f"[φ-ATTACK] Sent tampered message: {message}")
        
        # Wait for response
        print("[φ-ATTACK] Waiting for response...")
        sock.settimeout(5.0)
        
        try:
            data, addr = sock.recvfrom(65536)
            print(f"[φ-ATTACK] Received response from {addr[0]}:")
            print(f"  {data.decode('utf-8', errors='ignore')}")
        except socket.timeout:
            print("[φ-ATTACK] No response received (timeout)")
            print("[φ-ATTACK] Node may have rejected the message")
    
    except Exception as e:
        print(f"[φ-ATTACK] Error during attack: {e}")
    
    finally:
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python phi_attack_test.py <target_ip> [port]")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2]) if len(sys.argv) > 2 else 11975
    
    print("\n=== φ-HARMONIC PROTOCOL ATTACK SIMULATION ===")
    print("This script tests the security of your φ-Harmonic protocol")
    print("by attempting to send invalid scripts and messages.")
    print("\nIf your protocol is secure, these attacks should fail.")
    
    # Run both attack types
    attack_with_fake_script(target_ip, target_port)
    attack_with_message_tampering(target_ip, target_port)
    
    print("\n[φ-ATTACK] Attack simulation completed")
    print("If no 'WARNING' messages appeared, your protocol successfully rejected the attacks")
