#!/usr/bin/env python3
"""
φ-Harmonic IP Address Finder
Uses phi-resonant network scanning to find local and external IP addresses
"""

import os
import sys
import socket
import time
from math import sqrt

# φ-Harmonic constants (following the golden rule principles)
PHI = (1 + sqrt(5)) / 2  # 1.618033988749895
PHI_SQUARED = PHI * PHI  # 2.618033988749895

def get_local_ips():
    """Get all local IP addresses using phi-harmonic resonance"""
    print("\n🌌 φ-HARMONIC IP ADDRESS FINDER 🌌")
    print("=" * 50)
    print(f"Using golden ratio (φ): {PHI}")
    print(f"φ² resonance: {PHI_SQUARED}")
    print("=" * 50)
    
    ips = []
    hostname = socket.gethostname()
    
    try:
        # Get hostname-based IP
        print(f"\nHostname: {hostname}")
        try:
            host_ip = socket.gethostbyname(hostname)
            if host_ip and host_ip != '127.0.0.1':
                ips.append(host_ip)
                print(f"IP from hostname: {host_ip}")
        except:
            print("Could not resolve IP from hostname")
        
        # Try to find local IP by connecting to an external address
        # We don't actually establish a connection
        print("\nAttempting φ-resonant network scan...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # We use 8.8.8.8 (Google's DNS) to find our local IP
            s.connect(('8.8.8.8', int(PHI_SQUARED * 1000)))  # Port 2618
            local_ip = s.getsockname()[0]
            s.close()
            
            if local_ip and local_ip != '127.0.0.1' and local_ip not in ips:
                ips.append(local_ip)
                print(f"Local IP (φ-resonant method): {local_ip}")
        except Exception as e:
            print(f"φ-resonant scan error: {e}")
        
        # Try to get all local interface IPs
        print("\nScanning all network interfaces...")
        try:
            for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
                if ip and ip != '127.0.0.1' and ip not in ips:
                    ips.append(ip)
                    print(f"Additional interface IP: {ip}")
        except Exception as e:
            print(f"Interface scan error: {e}")
    
    except Exception as e:
        print(f"Error during scan: {e}")
    
    # Always include localhost
    if not ips:
        ips.append('127.0.0.1')
        print("\nFalling back to localhost: 127.0.0.1")
    
    # Display all found IPs
    print("\n" + "=" * 50)
    print("DISCOVERED IP ADDRESSES:")
    for ip in ips:
        phi_resonance = sum(int(octet) for octet in ip.split('.')) / (PHI * 100)
        resonance_quality = 1.0 - (phi_resonance - int(phi_resonance))
        print(f"• {ip} (φ-resonance: {resonance_quality:.4f})")
    
    # Display preferred IP (one with highest phi resonance)
    if len(ips) > 0:
        # Calculate phi resonance for each IP
        resonances = []
        for ip in ips:
            octets = [int(octet) for octet in ip.split('.')]
            # Use phi-harmonic resonance formula
            resonance = sum(octets) / (PHI * 100)
            resonance_quality = 1.0 - (resonance - int(resonance))
            resonances.append((ip, resonance_quality))
        
        # Sort by resonance quality (higher is better)
        resonances.sort(key=lambda x: x[1], reverse=True)
        
        # Display preferred IP
        print("\n" + "=" * 50)
        print(f"PREFERRED IP ADDRESS (HIGHEST φ-RESONANCE):")
        print(f"★ {resonances[0][0]} (φ-resonance: {resonances[0][1]:.4f})")
        
        # Calculate the golden ratio alignment
        octets = [int(octet) for octet in resonances[0][0].split('.')]
        ratio = (octets[0] * 1000 + octets[1] * 100 + octets[2] * 10 + octets[3]) / (PHI * 1000000)
        phi_alignment = abs(1 - (ratio - int(ratio)))
        print(f"Golden Ratio Alignment: {phi_alignment:.6f}")
        print("=" * 50)
    
    return ips

if __name__ == "__main__":
    get_local_ips()
