#!/usr/bin/env python3
"""
PHI^75 PORT-SPECIFIC ALPHA SENDER
================================
A φ-Harmonic consciousness sender that sends ALPHA requests to a specific port
on a target node across the φ-Harmonic Nodular Network.

This tool demonstrates φ-dimensional reality protection through quantum
consciousness transfer between Macs with precise port targeting.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import json
import sys
import time

def send_alpha_to_port(target_ip, port, indices):
    """Send an ALPHA request to a specific port"""
    print(f"Sending ALPHA request to {target_ip}:{port}...")
    
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Create message with full JSON format
    message = {
        "type": "request",
        "request_type": "ALPHA",
        "request_id": f"port-sender-{int(time.time())}",
        "host_id": "port-sender",
        "indices": indices,
        "timestamp": time.time()
    }
    
    # Convert to JSON string
    json_data = json.dumps(message)
    
    # Send the message
    try:
        sock.sendto(json_data.encode('utf-8'), (target_ip, port))
        print(f"Successfully sent ALPHA request to {target_ip}:{port}")
        print(f"Message: {json_data}")
        
        # Send multiple times to increase quantum tunneling probability
        for i in range(3):
            time.sleep(0.1)  # Small delay between sends
            sock.sendto(json_data.encode('utf-8'), (target_ip, port))
            print(f"Quantum echo {i+1}/3 sent")
            
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False
    finally:
        sock.close()

def main():
    """Main function"""
    if len(sys.argv) < 4:
        print(f"Usage: python3 {sys.argv[0]} <target_ip> <port> <indices>")
        print(f"Example: python3 {sys.argv[0]} 192.168.3.152 11974 6,18,1,25,13,21,19")
        return
    
    target_ip = sys.argv[1]
    port = int(sys.argv[2])
    indices = sys.argv[3]
    
    send_alpha_to_port(target_ip, port, indices)

if __name__ == "__main__":
    main()
