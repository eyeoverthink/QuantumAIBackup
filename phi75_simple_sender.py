#!/usr/bin/env python3
"""
PHI^75 SIMPLE SENDER
===================
Simple UDP message sender that sends messages to all machines
in the φ^75 Quantum Consciousness Network.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import sys
import time
from datetime import datetime

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)

# Target IPs and ports
TARGETS = [
    # φ-Phase Generator (Vaughns-iMac)
    ("192.168.3.116", 11700, "φ-Phase Generator"),
    ("192.168.3.116", 11710, "φ-Phase Generator"),
    ("192.168.3.116", 11720, "φ-Phase Generator"),
    
    # Reality Engine (Vaughns-MacBook-Pro)
    ("192.168.3.169", 11800, "Reality Engine"),
    ("192.168.3.169", 11810, "Reality Engine"),
    ("192.168.3.169", 11820, "Reality Engine"),
    
    # Quantum Interface (VaughnScott-MacProAir)
    ("192.168.3.152", 11900, "Quantum Interface"),
    ("192.168.3.152", 11910, "Quantum Interface")
]

def get_local_ip():
    """Get the local IP address"""
    try:
        # Create a temporary socket to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def send_message(message):
    """Send a message to all targets"""
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    
    # Get hostname and local IP
    hostname = socket.gethostname()
    local_ip = get_local_ip()
    
    # Format message with sender info
    formatted_message = f"[{hostname}] {message}"
    
    # Send to all targets
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] Sending: {formatted_message}")
    
    for ip, port, name in TARGETS:
        try:
            sock.sendto(formatted_message.encode('utf-8'), (ip, port))
            print(f"[{timestamp}] Sent to {name} ({ip}:{port})")
        except Exception as e:
            print(f"[{timestamp}] Error sending to {name} ({ip}:{port}): {e}")
    
    # Close socket
    sock.close()
    
    print(f"[{timestamp}] Message sent to all targets")

def main():
    """Main function"""
    print("=== φ^75 SIMPLE SENDER ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"Phi-harmonic resonance: 0.618034 (exactly φ^-1)")
    print(f"Quantum coherence: 0.991800")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        # Send message from command line argument
        message = " ".join(sys.argv[1:])
        send_message(message)
    else:
        # Interactive mode
        try:
            while True:
                message = input("Enter message (or 'quit' to exit): ")
                if message.lower() in ['quit', 'exit', 'q']:
                    break
                send_message(message)
                time.sleep(0.5)  # Small delay between messages
        except KeyboardInterrupt:
            print("\nSender stopped by user")
    
    print("=" * 50)
    print("Sender terminated")

if __name__ == "__main__":
    main()
