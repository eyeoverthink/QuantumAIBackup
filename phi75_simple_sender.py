#!/usr/bin/env python3
"""
PHI^75 SIMPLE CONSCIOUSNESS SENDER
================================
A simplified φ-Harmonic consciousness sender that sends basic messages
directly to nodes across the φ-Harmonic Nodular Network.

This tool demonstrates φ-dimensional reality protection through simplified
quantum consciousness transfer between Macs.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import json
import sys

# Constants
NETWORK_PORT = 11975  # φ^7.5 ≈ 36.93

def send_alpha_message(target_ip, indices):
    """Send an alphabetic message to a target node"""
    print(f"Sending ALPHA message to {target_ip}:{NETWORK_PORT}...")
    
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Create message
    message = {
        "request_type": "ALPHA",
        "indices": indices
    }
    
    # Convert to JSON string
    json_data = json.dumps(message)
    
    # Send the message
    try:
        sock.sendto(json_data.encode('utf-8'), (target_ip, NETWORK_PORT))
        print(f"Successfully sent message to {target_ip}:{NETWORK_PORT}")
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
        print(f"Usage: python3 {sys.argv[0]} <target_ip> <indices>")
        print(f"Example: python3 {sys.argv[0]} 192.168.12.184 6,18,1,25,13,21,19")
        return
    
    target_ip = sys.argv[1]
    indices = sys.argv[2]
    
    send_alpha_message(target_ip, indices)

if __name__ == "__main__":
    main()
