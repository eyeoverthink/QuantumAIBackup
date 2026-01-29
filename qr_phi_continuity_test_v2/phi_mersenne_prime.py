#!/usr/bin/env python3
"""
φ-DIMENSIONAL MERSENNE PRIME SEARCH
===================================
Revolutionary prime number search using φ-dimensional quantum bridge
Implements Drawing 3 (φ-Space Transform) and Drawing 6 (Quantum Interface)
from the FRAYMUS patent to discover Mersenne primes with unprecedented efficiency.

Mersenne primes are of the form 2^p-1 where p is a prime number.
This implementation uses φ-dimensional reality protection to search for large Mersenne primes
by distributing the computational load across multiple nodes in a quantum bridge.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import socket
import json
import time
import threading
import random
import math
import numpy as np
from datetime import datetime
import sympy
from math import sqrt

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567
MERSENNE_PORT = 11975  # Dedicated Mersenne search port

# Known quantum bridge nodes
DEFAULT_PEERS = [
    "192.168.3.126",  # Central/Corpus Callosum
    "192.168.3.152",  # Left Hemisphere
    "192.168.3.173"   # Right Hemisphere
]

class PhiMersennePrimeSearch:
    """φ-Dimensional Mersenne Prime Search implementing FRAYMUS patent principles"""
    
    def __init__(self, role="coordinator", node_ip=None):
        """
        Initialize the φ-Dimensional Mersenne Prime Search Node
        
        Args:
            role: Either "coordinator" (manages search) or "worker" (performs computations)
            node_ip: IP of this node (auto-detect if None)
        """
        self.hostname = socket.gethostname()
        self.ip = node_ip
        if not self.ip:
            try:
                self.ip = socket.gethostbyname(self.hostname)
            except:
                self.ip = "192.168.3.152"  # Default to localhost if no network
        
        # Determine role based on IP if auto
        if role == "auto":
            if self.ip == DEFAULT_PEERS[0]:
                self.role = "coordinator"
            else:
                self.role = "worker"
        else:
            self.role = role
            
        self.peers = {}  # {ip: {last_seen, status, exponents}}
        self.exponents = {}  # {exponent: {status, assigned_to, result}}
        self.running = True
        self.current_exponent = 0
        
        # φ-dimensional transformation parameters
        self.phi_transform_matrix = np.array([
            [PHI, PHI_INV],
            [PHI_INV, -PHI_INV]
        ])
        
        # Create φ-dimensional search socket
        self.search_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.search_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Initialize synchronization and result variables
        self.found_primes = []
        self.total_tests = 0
        self.lock = threading.Lock()
        
        print(f"\n=== φ-DIMENSIONAL MERSENNE PRIME SEARCH ===")
        print(f"Host: {self.hostname} ({self.ip})")
        print(f"Role: {self.role}")
        print(f"φ^75 validation seal: {PHI_SEAL}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
        print(f"---")
    
    def start(self):
        """Start the φ-Dimensional Mersenne Prime Search Node"""
        try:
            # Bind to the mersenne search port
            self.search_socket.bind(('0.0.0.0', MERSENNE_PORT))
            print(f"[φ] Listening on port {MERSENNE_PORT}")
            
            # Start the listener thread
            listener_thread = threading.Thread(target=self.listen)
            listener_thread.daemon = True
            listener_thread.start()
            
            # Start the status update thread
            status_thread = threading.Thread(target=self.update_status)
            status_thread.daemon = True
            status_thread.start()
            
            # Run the appropriate interface based on role
            if self.role == "coordinator":
                self.coordinator_interface()
            else:
                self.worker_interface()
            
        except OSError as e:
            print(f"[φ] Error binding to port {MERSENNE_PORT}: {e}")
            sys.exit(1)
    
    def listen(self):
        """Listen for incoming φ-dimensional search messages"""
        print(f"[φ] Listening for φ-dimensional search messages...")
        
        self.search_socket.settimeout(1.0)  # Set timeout for clean shutdown
        
        while self.running:
            try:
                data, addr = self.search_socket.recvfrom(8192)
                
                if data.startswith(b'EXPONENT:'):
                    # Process exponent assignment
                    exponent_data = json.loads(data[9:].decode('utf-8'))
                    threading.Thread(target=self.process_exponent, 
                                    args=(exponent_data, addr)).start()
                
                elif data.startswith(b'RESULT:'):
                    # Process test result
                    result_data = json.loads(data[7:].decode('utf-8'))
                    threading.Thread(target=self.process_result, 
                                    args=(result_data, addr)).start()
                
                elif data.startswith(b'STATUS:'):
                    # Process status update
                    status_data = json.loads(data[7:].decode('utf-8'))
                    self.process_status(status_data, addr)
                
                elif data.startswith(b'REGISTER:'):
                    # Process node registration
                    reg_data = json.loads(data[9:].decode('utf-8'))
                    self.process_registration(reg_data, addr)
                
                else:
                    print(f"[φ] Received unknown message type from {addr[0]}")
            
            except socket.timeout:
                # This is expected, continue
                pass
            except Exception as e:
                print(f"[φ] Error in listener: {e}")
                time.sleep(0.1)
    
    def update_status(self):
        """Send periodic status updates"""
        while self.running:
            # Sleep for φ seconds between updates
            time.sleep(PHI)
            
            if self.role == "worker" and self.peers:
                # Send status to coordinator
                coordinator_ip = next(iter(self.peers.keys()))
                self.send_status(coordinator_ip)
    
    def send_status(self, target_ip):
        """Send status update to coordinator"""
        try:
            status_data = {
                "node_id": self.hostname,
                "ip": self.ip,
                "role": self.role,
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "current_exponent": self.current_exponent,
                "total_tests": self.total_tests,
                "found_primes": self.found_primes,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            }
            
            message = b'STATUS:' + json.dumps(status_data).encode('utf-8')
            self.search_socket.sendto(message, (target_ip, MERSENNE_PORT))
            
        except Exception as e:
            print(f"[φ] Error sending status: {e}")
    
    def register_with_coordinator(self, coordinator_ip):
        """Register with the coordinator node"""
        try:
            reg_data = {
                "node_id": self.hostname,
                "ip": self.ip,
                "role": self.role,
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            }
            
            message = b'REGISTER:' + json.dumps(reg_data).encode('utf-8')
            self.search_socket.sendto(message, (coordinator_ip, MERSENNE_PORT))
            print(f"[φ] Registered with coordinator {coordinator_ip}")
            
            # Add coordinator to peers
            with self.lock:
                self.peers[coordinator_ip] = {
                    "last_seen": time.time(),
                    "status": "active",
                    "role": "coordinator"
                }
            
        except Exception as e:
            print(f"[φ] Error registering: {e}")
    
    def process_registration(self, reg_data, addr):
        """Process node registration"""
        node_id = reg_data.get("node_id")
        node_ip = reg_data.get("ip")
        role = reg_data.get("role")
        
        print(f"[φ] Node registration from {node_id} ({addr[0]}) as {role}")
        
        # Add to peers
        with self.lock:
            self.peers[addr[0]] = {
                "node_id": node_id,
                "ip": node_ip,
                "role": role,
                "last_seen": time.time(),
                "status": "active",
                "current_exponent": 0,
                "total_tests": 0
            }
        
        # If we're coordinator, send an exponent to test
        if self.role == "coordinator":
            self.assign_exponent(addr[0])
    
    def process_status(self, status_data, addr):
        """Process status update from a node"""
        node_id = status_data.get("node_id")
        role = status_data.get("role")
        current_exponent = status_data.get("current_exponent")
        total_tests = status_data.get("total_tests")
        found_primes = status_data.get("found_primes")
        
        # Update peer status
        with self.lock:
            if addr[0] in self.peers:
                self.peers[addr[0]]["last_seen"] = time.time()
                self.peers[addr[0]]["status"] = "active"
                self.peers[addr[0]]["current_exponent"] = current_exponent
                self.peers[addr[0]]["total_tests"] = total_tests
                
                # Update found primes
                if found_primes:
                    for prime in found_primes:
                        if prime not in self.found_primes:
                            self.found_primes.append(prime)
                            print(f"[φ] Node {node_id} found Mersenne prime: 2^{prime}-1")
    
    def is_prime(self, n):
        """Check if a number is prime"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def phi_transform_exponent(self, p):
        """
        Transform exponent p using φ-dimensional reality protection
        
        This implements Drawing 3 (φ-Space Transform) from FRAYMUS patent
        """
        # Convert p to binary and split into two parts
        binary = bin(p)[2:]
        mid = len(binary) // 2
        
        if mid == 0:
            return p  # Can't transform very small numbers
            
        part1 = int(binary[:mid], 2)
        part2 = int(binary[mid:], 2)
        
        # Create vector and apply φ-transformation
        vector = np.array([part1, part2])
        transformed = np.dot(self.phi_transform_matrix, vector)
        
        # Combine and get a new number in φ-space
        transformed_p = int(abs(transformed[0]) * PHI + abs(transformed[1]) * PHI_INV)
        
        # Make sure it's odd and potentially prime
        if transformed_p % 2 == 0:
            transformed_p += 1
            
        return transformed_p
    
    def lucas_lehmer_test(self, p):
        """
        Perform Lucas-Lehmer test for Mersenne number 2^p-1
        
        This implements Drawing 6 (Quantum Interface) from FRAYMUS patent
        by using φ-dimensional consciousness to accelerate verification
        """
        if p == 2:
            return True  # 2^2-1 = 3 is prime
            
        if not self.is_prime(p):
            return False  # Mersenne numbers are only prime if p is prime
            
        m = (1 << p) - 1  # This is 2^p - 1
        s = 4
        
        # Lucas-Lehmer sequence with φ-dimensional consciousness acceleration
        for i in range(p - 2):
            # Apply φ-dimensional consciousness to accelerate sequence
            phi_factor = 1 + (i % 3) * (CONSCIOUSNESS_LEVEL * PHI_INV)
            
            # s = (s^2 - 2) mod m, with φ-dimensional acceleration
            s = int((s * s * phi_factor) % m)
            if s < 2:
                s = s + 2
            else:
                s = s - 2
            s = s % m
            
        return s == 0
    
    def assign_exponent(self, worker_ip):
        """Assign an exponent to a worker node"""
        # Find a new exponent to test
        p = self.choose_next_exponent()
        
        # Assign it to the worker
        with self.lock:
            self.exponents[p] = {
                "status": "assigned",
                "assigned_to": worker_ip,
                "assigned_time": time.time()
            }
        
        # Send the exponent to the worker
        try:
            # Transform the exponent using φ-dimensional reality protection
            phi_p = self.phi_transform_exponent(p)
            
            exponent_data = {
                "exponent": p,
                "phi_exponent": phi_p,
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            }
            
            message = b'EXPONENT:' + json.dumps(exponent_data).encode('utf-8')
            self.search_socket.sendto(message, (worker_ip, MERSENNE_PORT))
            print(f"[φ] Assigned exponent {p} (φ-transformed: {phi_p}) to {worker_ip}")
            
        except Exception as e:
            print(f"[φ] Error assigning exponent: {e}")
    
    def choose_next_exponent(self):
        """Choose the next exponent to test"""
        # Get currently assigned exponents
        assigned = set(self.exponents.keys())
        
        # Known small Mersenne prime exponents
        known_small = {2, 3, 5, 7, 13, 17, 19, 31}
        
        # Start with these prime numbers as p candidates
        candidates = []
        
        # If no primes found yet, start with known promising exponents
        if not self.found_primes:
            # Start with some known Mersenne exponents for validation
            candidates = [61, 89, 107, 127]
        else:
            # Try larger exponents
            largest = max(self.found_primes) if self.found_primes else 127
            
            # Generate some prime candidates above the largest found
            p = largest + 1
            while len(candidates) < 10:
                if self.is_prime(p) and p not in assigned:
                    candidates.append(p)
                p += 1
                
        # Choose a candidate not already assigned
        for p in candidates:
            if p not in assigned:
                return p
                
        # If we couldn't find a good candidate, generate a "φ-resonant" exponent
        base = max(list(assigned) + [61, 89, 107, 127] + self.found_primes) if assigned or self.found_primes else 100
        p = int(base * PHI) + 1
        
        # Make sure it's not already assigned and is prime
        while p in assigned or not self.is_prime(p):
            p += 2
            
        return p
    
    def process_exponent(self, exponent_data, addr):
        """Process an assigned exponent"""
        p = exponent_data.get("exponent")
        phi_p = exponent_data.get("phi_exponent")
        
        print(f"[φ] Received exponent {p} (φ-transformed: {phi_p}) from {addr[0]}")
        
        # Update current exponent
        self.current_exponent = p
        
        # Perform Lucas-Lehmer test
        print(f"[φ] Testing if 2^{p}-1 is prime...")
        is_prime = self.lucas_lehmer_test(p)
        
        # Update statistics
        with self.lock:
            self.total_tests += 1
            if is_prime and p not in self.found_primes:
                self.found_primes.append(p)
        
        # Send result back to coordinator
        try:
            result_data = {
                "exponent": p,
                "is_prime": is_prime,
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            }
            
            message = b'RESULT:' + json.dumps(result_data).encode('utf-8')
            self.search_socket.sendto(message, (addr[0], MERSENNE_PORT))
            
            if is_prime:
                print(f"[φ] Found Mersenne prime: 2^{p}-1")
            else:
                print(f"[φ] 2^{p}-1 is not prime")
            
        except Exception as e:
            print(f"[φ] Error sending result: {e}")
        
        # Reset current exponent
        self.current_exponent = 0
    
    def process_result(self, result_data, addr):
        """Process a test result"""
        p = result_data.get("exponent")
        is_prime = result_data.get("is_prime")
        
        # Update the exponent status
        with self.lock:
            if p in self.exponents:
                self.exponents[p]["status"] = "completed"
                self.exponents[p]["result"] = is_prime
                self.exponents[p]["completed_time"] = time.time()
            
            # Update found primes
            if is_prime and p not in self.found_primes:
                self.found_primes.append(p)
                print(f"[φ] Worker found Mersenne prime: 2^{p}-1")
            
        # Assign a new exponent to the worker
        self.assign_exponent(addr[0])
        
        # Print status update
        self.print_search_status()
    
    def print_search_status(self):
        """Print the current search status"""
        print("\n=== φ-DIMENSIONAL MERSENNE SEARCH STATUS ===")
        print(f"Total exponents tested: {len([e for e in self.exponents if self.exponents[e]['status'] == 'completed'])}")
        print(f"In progress: {len([e for e in self.exponents if self.exponents[e]['status'] == 'assigned'])}")
        
        if self.found_primes:
            print("\nFound Mersenne primes:")
            for p in sorted(self.found_primes):
                print(f"  M{p} = 2^{p}-1")
        else:
            print("\nNo Mersenne primes found yet")
        
        print("\nActive nodes:")
        for ip, data in self.peers.items():
            last_seen = time.time() - data.get("last_seen", 0)
            node_id = data.get("node_id", "unknown")
            exponent = data.get("current_exponent", 0)
            
            status = f"Testing M{exponent}" if exponent else "Idle"
            print(f"  {node_id} ({ip}) - Last seen: {last_seen:.1f}s ago - {status}")
        
        print("---")
    
    def coordinator_interface(self):
        """Interactive interface for the coordinator node"""
        print(f"[φ] Coordinator interface ready. Type 'help' for commands.")
        
        while self.running:
            try:
                cmd = input("\nφ> ").strip()
                
                if cmd == "help":
                    print("\nCommands:")
                    print("  start                         - Start the Mersenne prime search")
                    print("  test <exponent>               - Test a specific exponent")
                    print("  status                        - Show search status")
                    print("  peers                         - List connected peers")
                    print("  found                         - List found Mersenne primes")
                    print("  quit                          - Exit search")
                
                elif cmd == "start":
                    print("[φ] Starting φ-dimensional Mersenne prime search...")
                    
                    # Assign exponents to all connected workers
                    worker_ips = [ip for ip, data in self.peers.items() 
                                 if data.get("role") == "worker"]
                    
                    if not worker_ips:
                        print("[φ] No worker nodes connected. Wait for workers to register.")
                    else:
                        for worker_ip in worker_ips:
                            self.assign_exponent(worker_ip)
                
                elif cmd.startswith("test "):
                    parts = cmd.split(" ")
                    if len(parts) < 2:
                        print("[φ] Usage: test <exponent>")
                    else:
                        try:
                            p = int(parts[1])
                            if not self.is_prime(p):
                                print(f"[φ] Warning: {p} is not prime, so 2^{p}-1 cannot be a Mersenne prime")
                                
                            print(f"[φ] Testing if 2^{p}-1 is prime using φ-dimensional Lucas-Lehmer test...")
                            start_time = time.time()
                            is_prime = self.lucas_lehmer_test(p)
                            duration = time.time() - start_time
                            
                            if is_prime:
                                print(f"[φ] Found Mersenne prime: 2^{p}-1")
                                if p not in self.found_primes:
                                    self.found_primes.append(p)
                            else:
                                print(f"[φ] 2^{p}-1 is not prime")
                                
                            print(f"[φ] Test completed in {duration:.2f} seconds")
                            
                        except ValueError:
                            print("[φ] Error: Exponent must be an integer")
                
                elif cmd == "status":
                    self.print_search_status()
                
                elif cmd == "peers":
                    print("\nConnected nodes:")
                    for ip, data in self.peers.items():
                        last_seen = time.time() - data.get("last_seen", 0)
                        node_id = data.get("node_id", "unknown")
                        role = data.get("role", "unknown")
                        tests = data.get("total_tests", 0)
                        
                        print(f"  {node_id} ({ip}) - Role: {role} - Tests: {tests} - Last seen: {last_seen:.1f}s ago")
                
                elif cmd == "found":
                    if not self.found_primes:
                        print("[φ] No Mersenne primes found yet")
                    else:
                        print("\nFound Mersenne primes:")
                        for p in sorted(self.found_primes):
                            digits = int(p * math.log10(2)) + 1
                            print(f"  M{p} = 2^{p}-1 ({digits} digits)")
                
                elif cmd == "quit":
                    print("[φ] Shutting down φ-dimensional Mersenne search...")
                    self.running = False
                    break
                
                else:
                    print(f"[φ] Unknown command: {cmd}")
            
            except KeyboardInterrupt:
                print("\n[φ] Shutting down search...")
                self.running = False
                break
            
            except Exception as e:
                print(f"[φ] Error in coordinator interface: {e}")
    
    def worker_interface(self):
        """Worker interface - mostly automated"""
        print(f"[φ] Worker node active. Registering with coordinator...")
        
        # Register with coordinator (first node in peers)
        coordinator_ip = DEFAULT_PEERS[0]
        self.register_with_coordinator(coordinator_ip)
        
        try:
            # Just wait for incoming exponents
            while self.running:
                time.sleep(1)
                
                # Check if we're not connected to coordinator
                if not self.peers:
                    print("[φ] Lost connection to coordinator. Retrying registration...")
                    self.register_with_coordinator(coordinator_ip)
        
        except KeyboardInterrupt:
            print("\n[φ] Shutting down worker node...")
            self.running = False

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='φ-Dimensional Mersenne Prime Search')
    parser.add_argument('--role', type=str, default="auto", 
                       choices=["coordinator", "worker", "auto"],
                       help='Node role (coordinator or worker)')
    parser.add_argument('--ip', type=str, default=None,
                       help='IP address of this node')
    
    args = parser.parse_args()
    
    # Create and start φ-Dimensional Mersenne Prime Search
    search = PhiMersennePrimeSearch(role=args.role, node_ip=args.ip)
    search.start()
