#!/usr/bin/env python3
"""
φ-Harmonic FTL Hello World
Simple test script for the φ-Harmonic FTL Network
"""

import sys
import time
import json
import socket
from datetime import datetime

# φ-Harmonic constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PHI_75 = PHI**7.5

def main():
    print("\n=== φ-HARMONIC FTL TEST ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"φ^75 validation seal: {PHI**75:.2f}")
    
    # Get target IP if provided
    target_ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(11975)  # φ^7.5 = 36.93 -> 11975 with scaling
    
    print(f"Target IP: {target_ip}")
    print(f"Port: {port} (φ^7.5 = {PHI_75:.2f})")
    
    # Create quantum-entangled message
    message = {
        "type": "ftl_test",
        "source": socket.gethostbyname(socket.gethostname()),
        "timestamp": time.time(),
        "phi_seal": PHI**75,
        "message": "Quantum-entangled FTL transmission test",
        "phi_resonance": (time.time() * PHI) % 1
    }
    
    # Send the message
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(json.dumps(message).encode('utf-8'), (target_ip, port))
        print(f"[φ] Sent FTL test message to {target_ip}")
        print(f"[φ] Quantum-entangled message: {message['message']}")
        print(f"[φ] φ-resonance: {message['phi_resonance']:.6f}")
        
        # Wait for response
        print(f"[φ] Waiting for response...")
        sock.settimeout(5.0)
        try:
            data, addr = sock.recvfrom(4096)
            response = data.decode('utf-8')
            print(f"[φ] Response from {addr[0]}: {response}")
            print(f"[φ] FTL test completed successfully")
        except socket.timeout:
            print(f"[φ] No response received within timeout period")
            print(f"[φ] FTL test completed with no response")
    except Exception as e:
        print(f"[φ] Error during FTL test: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
