#!/usr/bin/env python3
"""
φ-QUANTUM COLOR NETWORK LAUNCHER
===============================
Launcher for the φ-Quantum Color Network that automatically detects the local IP
and connects to known peers for φ-dimensional quantum entanglement testing.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import subprocess
import sys
import os
import time

# Known MacBook IPs
KNOWN_PEERS = [
    "192.168.3.152",  # MacBook 1
    "192.168.3.173"   # MacBook 2
]

def get_local_ip():
    """Get local IP address"""
    try:
        # Create a socket to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return "192.168.3.126"  # Fallback to localhost

def main():
    """Main function"""
    print("φ-QUANTUM COLOR NETWORK LAUNCHER")
    print("=" * 50)
    
    # Get local IP
    local_ip = get_local_ip()
    print(f"Local IP: {local_ip}")
    
    # Filter out local IP from known peers
    peers = [ip for ip in KNOWN_PEERS if ip != local_ip]
    print(f"Known peers: {peers}")
    
    # Check if phi_quantum_core.py and phi_quantum_network.py exist
    if not os.path.exists("phi_quantum_core.py") or not os.path.exists("phi_quantum_network.py"):
        print("Error: Required files not found!")
        print("Make sure phi_quantum_core.py and phi_quantum_network.py are in the current directory.")
        return
    
    # Construct command
    cmd = [sys.executable, "phi_quantum_network.py", "--host", local_ip]
    for peer in peers:
        cmd.extend(["--peers", peer])
    
    print("\nLaunching φ-Quantum Color Network...")
    print(f"Command: {' '.join(cmd)}")
    print("\nWaiting for φ-dimensional network to initialize...")
    
    # Create results directories if they don't exist
    os.makedirs("quantum_color_results", exist_ok=True)
    os.makedirs("quantum_network_results", exist_ok=True)
    
    # Launch the network
    time.sleep(1)
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
