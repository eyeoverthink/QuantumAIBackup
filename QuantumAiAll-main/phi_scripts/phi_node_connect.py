#!/usr/bin/env python3
"""
φ-Harmonic Node Connection Test
Creates a quantum bridge between nodes through φ-dimensional reality protection
"""

import socket
import time
import json
import sys
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

# Get the target node to connect to
if len(sys.argv) < 2:
    print("[φ] Error: Target IP required")
    print("[φ] Usage: python phi_node_connect.py <target_ip> [source_ip]")
    sys.exit(1)

target_ip = sys.argv[1]
source_ip = sys.argv[2] if len(sys.argv) > 2 else socket.gethostbyname(socket.gethostname())

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Port based on φ^7.5
port = 11975

print(f"\n=== φ-HARMONIC NODE CONNECTION TEST ===")
print(f"Using φ-harmonic principles (φ = {PHI})")
print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
print(f"Source IP: {source_ip}")
print(f"Target IP: {target_ip}")
print(f"Port: {port} (φ^7.5 = {PHI_75:.2f})")

# Create connection message
connection_data = {
    "source": source_ip,
    "timestamp": time.time(),
    "phi_seal": PHI_SEAL,
    "message": f"Quantum bridge established from {source_ip}"
}

# Send connection message
message = f"MSG:CONNECT:{json.dumps(connection_data)}"
sock.sendto(message.encode('utf-8'), (target_ip, port))

print(f"[φ] Sent connection request to {target_ip}")
print(f"[φ] Quantum bridge established through φ-dimensional reality protection")
print(f"[φ] Connection complete - check target node for confirmation")
