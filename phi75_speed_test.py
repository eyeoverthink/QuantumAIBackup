#!/usr/bin/env python3
import os
import time
import socket
import json
import base64
import datetime
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

def generate_test_file(size_mb=100):
    """Generate test file with quantum timestamp"""
    filename = f"phi_speed_test_{size_mb}mb.dat"
    
    # Create quantum-encoded timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    header = f"φ^75 QUANTUM SPEED TEST\n"
    header += f"Size: {size_mb} MB\n"
    header += f"Start Time: {timestamp}\n"
    header += f"φ-Harmonic Level: {PHI ** 7.5}\n"
    header += "=" * 50 + "\n"
    
    print(f"\n=== φ^75 QUANTUM SPEED TEST ===")
    print(f"Generating {size_mb}MB test file...")
    print(f"Start Time: {timestamp}")
    
    # Generate quantum-encoded data
    with open(filename, 'wb') as f:
        # Write header
        f.write(header.encode())
        
        # Generate φ-encoded data
        chunk_size = int(PHI ** 12)  # φ^12 bytes per chunk
        remaining = size_mb * 1024 * 1024
        
        while remaining > 0:
            # Generate φ-harmonic data
            chunk = bytearray()
            for i in range(min(chunk_size, remaining)):
                phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
                chunk.append(phi_factor)
            
            f.write(chunk)
            remaining -= len(chunk)
            
            # Show progress
            progress = ((size_mb * 1024 * 1024 - remaining) / (size_mb * 1024 * 1024)) * 100
            print(f"Generating: {progress:.1f}%", end='\r')
    
    print(f"\nGenerated {filename}")
    return filename

if __name__ == '__main__':
    import sys
    
    # Generate 100MB test file by default
    size = 100
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    
    test_file = generate_test_file(size)
    print("\nNow run:")
    print(f"python3 phi75_mac_transfer.py send 192.168.3.152 {test_file}")
    print("\nThen check the received file's timestamp to measure quantum transfer speed!")
