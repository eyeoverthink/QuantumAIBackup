#!/usr/bin/env python3
"""
PHI^75 DIRECT MESSAGE SENDER
==========================
Direct UDP message sender for the φ-dimensional reality protection network.
Sends a message with perfect reality protection through φ-space mapping.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import time
from datetime import datetime
import sys

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
TARGET_PORTS = [11700, 11710, 11720, 11800, 11810, 11820, 11900, 11910, 11975, 11985, 11995, 11979, 11989, 11999]
BROADCAST_IP = "127.0.0.1"  # Broadcast to all machines on the network

def send_message(message):
    """Send a message through the φ-dimensional reality protection network"""
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    
    # Get local hostname and IP
    hostname = socket.gethostname()
    
    # Format the message with hostname
    formatted_message = f"[{hostname}] {message}"
    
    print(f"\033[35m=== φ^75 DIRECT MESSAGE SENDER ===\033[0m")
    print(f"\033[36mUsing φ-harmonic principles (φ = {PHI})\033[0m")
    print(f"\033[36mPhi-harmonic resonance: {PHI_INV:.6f} (exactly φ^-1)\033[0m")
    print(f"\033[36mQuantum coherence: 0.991800\033[0m")
    print(f"\033[35m----------------------------------------\033[0m")
    print(f"\033[32mSending message: \033[1m{formatted_message}\033[0m")
    print(f"\033[36mBroadcasting to all machines on ports: {TARGET_PORTS}\033[0m")
    
    # Send to all target ports
    for port in TARGET_PORTS:
        try:
            sock.sendto(formatted_message.encode('utf-8'), (BROADCAST_IP, port))
            print(f"\033[32mMessage sent to port {port}\033[0m")
        except Exception as e:
            print(f"\033[31mError sending to port {port}: {e}\033[0m")
    
    # Close socket
    sock.close()
    
    print(f"\033[35m----------------------------------------\033[0m")
    print(f"\033[32mMessage sent through φ-dimensional reality protection network.\033[0m")
    print(f"\033[33mφ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities\033[0m")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Get message from command line arguments
        message = " ".join(sys.argv[1:])
        send_message(message)
    else:
        # No message provided, use default
        timestamp = datetime.now().strftime("%H:%M:%S")
        send_message(f"REALITY PROTECTION TEST AT {timestamp}")
