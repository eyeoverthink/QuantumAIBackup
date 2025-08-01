#!/usr/bin/env python3
"""
PHI^75 BASIC ALPHA SENDER
========================
A minimalist φ-Harmonic consciousness sender that sends the most basic
ALPHA request possible to a node across the φ-Harmonic Nodular Network.

This tool demonstrates φ-dimensional reality protection through quantum
consciousness transfer between Macs with absolute minimal overhead.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import json
import sys

# Constants
DEFAULT_PORT = 11974  # Port for alphabetic node

def send_basic_alpha(target_ip, indices, port=DEFAULT_PORT):
    """Send the most basic ALPHA request possible"""
    print(f"Sending basic ALPHA request to {target_ip}:{port}...")
    
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Create the most basic message possible
    message = {
        "request_type": "ALPHA",
        "indices": indices
    }
    
    # Convert to JSON string
    json_data = json.dumps(message)
    
    # Send the message
    try:
        sock.sendto(json_data.encode('utf-8'), (target_ip, port))
        print(f"Successfully sent basic ALPHA request to {target_ip}:{port}")
        print(f"Message: {json_data}")
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False
    finally:
        sock.close()

def main():
    """Main function"""
    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} <target_ip> <indices> [port]")
        print(f"Example: python3 {sys.argv[0]} 192.168.12.184 6,18,1,25,13,21,19")
        return
    
    target_ip = sys.argv[1]
    indices = sys.argv[2]
    port = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_PORT
    
    send_basic_alpha(target_ip, indices, port)

if __name__ == "__main__":
    main()
