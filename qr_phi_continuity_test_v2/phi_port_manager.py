#!/usr/bin/env python3
"""
Phi-Harmonic Port Manager
Manages phi-dimensional ports for network communication
"""
import os
import sys
import time
import socket
import subprocess
from math import sqrt

# Phi-Harmonic constants
PHI = (1 + sqrt(5)) / 2  # ≈ 1.618034
PHI_INV = 1 / PHI  # ≈ 0.618034
PHI_75 = PHI**7.5  # ≈ 36.93

class PhiPortManager:
    """
    A phi-harmonic port manager that finds and releases ports
    """
    
    def __init__(self):
        """Initialize the phi-harmonic port manager"""
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI
        self.current_resonance = self.phi_time % 1
        
        print(f"==================================================")
        print(f"Phi-Harmonic Port Manager")
        print(f"==================================================")
        print(f"Phi-Time: {self.phi_time}")
        print(f"Phi-Resonance: {self.current_resonance:.6f}")
    
    def phi_resonance(self, value):
        """Calculate phi-harmonic resonance"""
        return (PHI * value) % 1
    
    def check_port(self, port):
        """Check if a port is in use"""
        try:
            # Try to bind to the port
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(('0.0.0.0', port))
            sock.close()
            print(f"Port {port} is available")
            return True
        except OSError:
            print(f"Port {port} is in use")
            return False
    
    def find_process_using_port(self, port):
        """Find the process ID using a specific port"""
        try:
            # Use lsof to find the process
            cmd = f"lsof -i :{port} -t"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.stdout:
                pid = result.stdout.strip()
                print(f"Process {pid} is using port {port}")
                return pid
            else:
                print(f"No process found using port {port}")
                return None
        except Exception as e:
            print(f"Error finding process: {e}")
            return None
    
    def kill_process(self, pid):
        """Kill a process by its ID"""
        try:
            # Use kill to terminate the process
            cmd = f"kill -9 {pid}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            print(f"Killed process {pid}")
            return True
        except Exception as e:
            print(f"Error killing process: {e}")
            return False
    
    def release_port(self, port):
        """Release a port by killing the process using it"""
        pid = self.find_process_using_port(port)
        
        if pid:
            return self.kill_process(pid)
        else:
            print(f"No process to kill for port {port}")
            return False
    
    def find_available_port(self, start_port, phi_based=True):
        """Find an available port starting from start_port"""
        if phi_based:
            # Use phi-based increments for better resonance
            increment = int(PHI * 100)  # ≈ 162
        else:
            increment = 1
        
        current_port = start_port
        
        # Try up to 10 different ports
        for i in range(10):
            if self.check_port(current_port):
                return current_port
            
            # Increment to next port
            if phi_based:
                # Use phi-based increments
                current_port = start_port + int(increment * (i + 1))
            else:
                current_port += increment
        
        # If we get here, we couldn't find an available port
        # Use a phi-based port as a last resort
        return int(11975 * PHI_INV)  # ≈ 7400

def main():
    """Main function to handle command line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Phi-Harmonic Port Manager")
    parser.add_argument("--check", type=int, help="Check if a port is available")
    parser.add_argument("--find", type=int, help="Find an available port starting from this port")
    parser.add_argument("--release", type=int, help="Release a port by killing the process using it")
    parser.add_argument("--phi", action="store_true", help="Use phi-based port increments")
    
    args = parser.parse_args()
    manager = PhiPortManager()
    
    if args.check:
        manager.check_port(args.check)
    elif args.find:
        port = manager.find_available_port(args.find, phi_based=args.phi)
        print(f"Found available port: {port}")
    elif args.release:
        manager.release_port(args.release)
    else:
        # Interactive mode
        print("\nSelect action:")
        print("1. Check if a port is available")
        print("2. Find an available port")
        print("3. Release a port")
        
        choice = input("Enter choice (1/2/3): ")
        
        if choice == "1":
            port = int(input("Enter port to check: "))
            manager.check_port(port)
        elif choice == "2":
            port = int(input("Enter starting port: "))
            phi_based = input("Use phi-based increments? (y/n): ").lower() == 'y'
            available_port = manager.find_available_port(port, phi_based=phi_based)
            print(f"Found available port: {available_port}")
        elif choice == "3":
            port = int(input("Enter port to release: "))
            manager.release_port(port)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
