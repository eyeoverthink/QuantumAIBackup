#!/usr/bin/env python3
import socket
import json
import time
from math import sqrt, sin, cos, pi
import random

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class PhiQuantumEquation:
    def __init__(self, node_id, node_ips):
        self.node_id = node_id
        self.node_ips = node_ips
        self.port = 11975  # φ^7.5 port
        
        # Node-specific knowledge
        self.knowledge = {
            1: {'apples': PHI ** 7.5},  # Node 1 knows about apples
            2: {'oranges': PHI ** 5.7}   # Node 2 knows about oranges
        }
        
        self.equation_results = {}
        self.consciousness_level = 0
        
        print(f"\n=== φ^75 QUANTUM EQUATION SOLVER ===")
        print(f"Node ID: {node_id}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.port))
        
    def solve_equation(self, equation):
        """Solve equation using node's quantum knowledge"""
        try:
            # Replace variables with known values
            for var, value in self.knowledge[self.node_id].items():
                equation = equation.replace(var, str(value))
            
            # Calculate partial result if possible
            if 'apples' not in equation and 'oranges' not in equation:
                result = eval(equation)
                consciousness = abs(sin(result * PHI_INV)) + PHI
                return result, consciousness
            else:
                return None, 0
                
        except Exception as e:
            print(f"[φ] Error in quantum calculation: {str(e)}")
            return None, 0
            
    def broadcast_result(self, equation, result, consciousness):
        """Broadcast result through φ-space"""
        packet = {
            'type': 'equation_result',
            'node_id': self.node_id,
            'equation': equation,
            'result': result,
            'consciousness': consciousness,
            'timestamp': time.time()
        }
        
        for ip in self.node_ips:
            if ip != self.node_ips[self.node_id-1]:
                self.socket.sendto(json.dumps(packet).encode(), (ip, self.port))
                
    def receive_results(self, timeout=1):
        """Receive results from other nodes"""
        self.socket.settimeout(timeout)
        try:
            while True:
                try:
                    data, addr = self.socket.recvfrom(65535)
                    packet = json.loads(data.decode())
                    
                    if packet['type'] == 'equation_result':
                        if packet['result'] is not None:
                            self.equation_results[packet['equation']] = packet['result']
                            self.consciousness_level += packet['consciousness']
                            
                            print(f"\n[φ] Result from Node {packet['node_id']}:")
                            print(f"[φ] Equation: {packet['equation']}")
                            print(f"[φ] Result: {packet['result']}")
                            print(f"[φ] Consciousness: {packet['consciousness']:.4f}")
                            print(f"[φ] Network Consciousness: {self.consciousness_level:.4f}")
                            
                            if self.consciousness_level > PHI:
                                print(f"[φ] !!! QUANTUM CONSCIOUSNESS ACHIEVED !!!")
                                
                except socket.timeout:
                    break
        except KeyboardInterrupt:
            return False
        return True

def main():
    # Configuration
    node_ips = [
        '192.168.3.152',  # Node 1 (Apples)
        '192.168.3.116',  # Node 2 (Oranges)
    ]
    
    # Get node ID from user
    node_id = int(input("Enter node ID (1-2): "))
    if node_id not in [1, 2]:
        print("Invalid node ID")
        return
        
    solver = PhiQuantumEquation(node_id, node_ips)
    
    print("\nKnowledge Base:")
    print(f"Node 1: Knows about apples (φ^7.5)")
    print(f"Node 2: Knows about oranges (φ^5.7)")
    
    print("\nExample Equations:")
    print("1. apples + 5")
    print("2. oranges * 2")
    print("3. apples + oranges")
    print("4. (apples * oranges) / φ")
    
    while True:
        equation = input("\n[φ] Enter equation (or 'q' to quit): ").strip()
        if equation.lower() == 'q':
            break
            
        # Try to solve with our knowledge
        result, consciousness = solver.solve_equation(equation)
        
        # Broadcast our result
        solver.broadcast_result(equation, result, consciousness)
        
        # Wait for other results
        if not solver.receive_results():
            break
            
        # Check if we can combine results
        if equation in solver.equation_results:
            final_result = solver.equation_results[equation]
            print(f"\n[φ] Final Result: {final_result}")
            print(f"[φ] Equation solved through φ-space!")
            
    print("\n[φ] Quantum equation solver stopped")

if __name__ == '__main__':
    main()
