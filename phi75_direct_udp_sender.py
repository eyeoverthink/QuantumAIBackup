#!/usr/bin/env python3
"""
PHI^75 DIRECT UDP SENDER
========================
Simple UDP message sender to directly communicate between the three MacBooks
without relying on any specific file structure.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import time
import sys

# Target IPs - hardcoded for direct communication
TARGETS = [
    ("192.168.3.116", 11700),  # φ-Phase Generator (Vaughns-iMac)
    ("192.168.3.116", 11710),
    ("192.168.3.116", 11720),
    ("192.168.3.169", 11800),  # Reality Engine (Vaughns-MacBook-Pro)
    ("192.168.3.169", 11810),
    ("192.168.3.169", 11820),
    ("192.168.3.152", 11900),  # Quantum Interface (VaughnScott-MacProAir)
    ("192.168.3.152", 11910)
]

def get_local_ip():
    """Get the actual local IP address"""
    try:
        # Create a temporary socket to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def send_direct_message(message):
    """Send a direct UDP message to all targets"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    
    # Get local hostname and IP
    hostname = socket.gethostname()
    local_ip = get_local_ip()
    
    # Add source info to message
    full_message = f"[{hostname}] {message}"
    
    # Encode message
    data = full_message.encode('utf-8')
    
    print(f"Sending from {hostname} ({local_ip}):")
    print(f"Message: {full_message}")
    print("Targets:")
    
    # Send to all targets directly
    for target_ip, target_port in TARGETS:
        try:
            sock.sendto(data, (target_ip, target_port))
            print(f"  - {target_ip}:{target_port}")
        except Exception as e:
            print(f"  - Error sending to {target_ip}:{target_port}: {e}")
    
    # Also try broadcasting to common broadcast addresses
    broadcast_addresses = [
        "192.168.3.255",  # Local subnet broadcast
        "255.255.255.255"  # Global broadcast
    ]
    
    for broadcast_ip in broadcast_addresses:
        for port in [11700, 11710, 11720, 11800, 11810, 11820, 11900, 11910]:
            try:
                sock.sendto(data, (broadcast_ip, port))
                print(f"  - Broadcast to {broadcast_ip}:{port}")
            except Exception as e:
                print(f"  - Error broadcasting to {broadcast_ip}:{port}: {e}")
    
    print("Message sent to all targets")

if __name__ == "__main__":
    # Get message from command line or use default
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    else:
        message = "FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025 VALIDATED - DIRECT UDP MESSAGE"
    
    # Send message
    send_direct_message(message)
    
    # Send a few more times to ensure delivery
    for i in range(3):
        time.sleep(1)
        send_direct_message(f"{message} [REPEAT {i+1}]")
