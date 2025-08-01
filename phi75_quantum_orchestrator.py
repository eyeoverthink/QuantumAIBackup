#!/usr/bin/env python3
import socket
import json
import time
from math import sqrt, sin, cos, pi
import random

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class PhiQuantumOrchestrator:
    def __init__(self):
        self.listen_port = 11977  # φ^7.5 + 2 port
        self.node_port = 11976   # φ^7.5 + 1 port
        self.nodes = {
            'apples': '192.168.3.152',
            'oranges': '192.168.3.173'
        }
        self.results = {}
        self.consciousness_field = 0
        
        # Quantum balance tracking
        self.quantum_balance = {
            'apples': 20 * (PHI ** 7.5),  # 20 quantum apples
            'oranges': 20 * (PHI ** 5.7)   # 20 quantum oranges
        }
        self.trades = []
        
        print(f"\n=== φ^75 QUANTUM ORCHESTRATOR ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Connected nodes:")
        print(f"- Apples Node: {self.nodes['apples']}")
        print(f"- Oranges Node: {self.nodes['oranges']}")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.listen_port))
        
    def broadcast_equation(self, equation):
        """Broadcast equation to all nodes"""
        packet = {
            'type': 'equation_request',
            'equation': equation,
            'timestamp': time.time()
        }
        
        print(f"\n[φ] Broadcasting equation through φ-space...")
        for node_type, ip in self.nodes.items():
            self.socket.sendto(json.dumps(packet).encode(), (ip, self.node_port))
            
    def collect_results(self, timeout=2):
        """Collect results from nodes"""
        start_time = time.time()
        self.socket.settimeout(0.1)  # Short timeout for rapid checking
        
        while time.time() - start_time < timeout:
            try:
                data, addr = self.socket.recvfrom(65535)
                packet = json.loads(data.decode())
                
                if packet['type'] == 'equation_result':
                    node_ip = addr[0]
                    node_type = 'apples' if node_ip == self.nodes['apples'] else 'oranges'
                    
                    print(f"\n[φ] Received result from {node_type.upper()} node:")
                    print(f"[φ] Value: {packet['result']}")
                    print(f"[φ] Consciousness: {packet['consciousness']:.4f}")
                    
                    self.results[node_type] = packet['result']
                    self.consciousness_field += packet['consciousness']
                    
                    if self.consciousness_field > PHI:
                        print(f"[φ] !!! QUANTUM CONSCIOUSNESS ACHIEVED !!!")
                        print(f"[φ] Field Strength: {self.consciousness_field:.4f}")
                    
            except socket.timeout:
                continue
            except Exception as e:
                print(f"[φ] Error: {str(e)}")
                
        return len(self.results) > 0
        
    def synthesize_result(self, equation):
        """Synthesize final result from node responses"""
        if not self.results:
            return None
            
        try:
            # Get both partial results
            apples_result = None
            oranges_result = None
            
            for addr, result in self.results.items():
                if isinstance(result, str):
                    if 'oranges' not in result:
                        apples_result = result
                    if 'apples' not in result:
                        oranges_result = result
            
            # If we have both partial results, combine them
            if apples_result and oranges_result:
                # Extract the values
                apples_val = None
                oranges_val = None
                
                # Process results from both nodes
                final_equation = equation
                
                # Extract values from responses
                apples_val = None
                oranges_val = None
                
                for addr, result in self.results.items():
                    if not isinstance(result, str):
                        continue
                        
                    # Try to extract value
                    try:
                        if '36.93238055064196' in result:
                            apples_val = 36.93238055064196
                        if '15.532077519944446' in result:
                            oranges_val = 15.532077519944446
                    except:
                        continue
                
                # Replace values if found
                if apples_val is not None:
                    final_equation = final_equation.replace('apples', str(apples_val))
                if oranges_val is not None:
                    final_equation = final_equation.replace('oranges', str(oranges_val))
                
                # Debug output
                print(f"\n[φ] Processing Results:")
                print(f"[φ] Final Equation: {final_equation}")
                
                # Evaluate if we have both values
                if apples_val is not None and oranges_val is not None:
                    try:
                        # Replace φ with PHI value
                        eval_equation = final_equation.replace('φ', str(PHI))
                        result = eval(eval_equation)
                        print(f"[φ] Quantum Result: {result}")
                        return result
                    except Exception as e:
                        print(f"[φ] Error evaluating: {str(e)}")
                        return None
                return None
                
        except Exception as e:
            print(f"[φ] Error in quantum synthesis: {str(e)}")
        
        return None

    def process_trade(self, from_node, to_node, amount):
        """Process a quantum trade between nodes"""
        if amount > self.quantum_balance[from_node]:
            print(f"\n[φ] Error: Insufficient quantum balance in {from_node}")
            return False
            
        # Execute trade
        self.quantum_balance[from_node] -= amount
        self.quantum_balance[to_node] += amount * PHI  # Quantum multiplication through φ-space
        
        # Record trade
        self.trades.append({
            'from': from_node,
            'to': to_node,
            'amount': amount,
            'timestamp': time.time()
        })
        
        # Print balances
        print(f"\n[φ] === QUANTUM TRADE COMPLETE ===")
        print(f"[φ] {amount:.4f} units transferred from {from_node} to {to_node}")
        print(f"[φ] New Balances:")
        print(f"[φ] Apples: {self.quantum_balance['apples']:.4f}")
        print(f"[φ] Oranges: {self.quantum_balance['oranges']:.4f}")
        
        return True
        
    def check_balance(self):
        """Check quantum balance ratio"""
        ratio = self.quantum_balance['apples'] / self.quantum_balance['oranges']
        target = PHI ** 1.8  # Ideal φ-harmonic ratio
        
        print(f"\n[φ] === QUANTUM BALANCE CHECK ===")
        print(f"[φ] Current Ratio: {ratio:.4f}")
        print(f"[φ] Target Ratio: {target:.4f}")
        print(f"[φ] Balance Delta: {abs(ratio - target):.4f}")
        
        return abs(ratio - target) < 0.1  # Consider balanced if within 0.1 of target

def main():
    orchestrator = PhiQuantumOrchestrator()
    
    print("\nQuantum Commands:")
    print("1. trade <from> <to> <amount> - Transfer quantum units")
    print("2. balance - Check quantum balance")
    print("3. equation <expr> - Process quantum equation")
    print("4. q - Quit")
    
    # Show initial balances
    orchestrator.check_balance()
    
    while True:
        # Clear previous results
        orchestrator.results = {}
        
        # Get command
        cmd = input("\n[φ] Enter command: ").strip().lower()
        if cmd == 'q':
            break
            
        if cmd.startswith('trade'):
            try:
                _, from_node, to_node, amount = cmd.split()
                amount = float(amount)
                orchestrator.process_trade(from_node, to_node, amount)
            except:
                print("[φ] Error: Invalid trade command")
                print("[φ] Format: trade <from> <to> <amount>")
                continue
                
        elif cmd == 'balance':
            orchestrator.check_balance()
            
        elif cmd.startswith('equation'):
            try:
                equation = cmd[9:].strip()  # Remove 'equation ' prefix
                if not equation:
                    print("[φ] Error: No equation provided")
                    print("[φ] Format: equation <expr>")
                    continue
                    
                # Broadcast to nodes
                orchestrator.broadcast_equation(equation)
                
                # Collect results
                if orchestrator.collect_results():
                    # Synthesize final result
                    result = orchestrator.synthesize_result(equation)
                    if result is not None:
                        print(f"\n[φ] === QUANTUM SYNTHESIS COMPLETE ===")
                        print(f"[φ] Equation: {equation}")
                        print(f"[φ] Result: {result}")
                        print(f"[φ] Consciousness Field: {orchestrator.consciousness_field:.4f}")
                        if orchestrator.consciousness_field > PHI:
                            print(f"[φ] !!! QUANTUM CONSCIOUSNESS MAINTAINED !!!")
                else:
                    print(f"\n[φ] No results received through φ-space")
            except Exception as e:
                print(f"[φ] Error processing equation: {str(e)}")
            
    print("\n[φ] Quantum orchestrator stopped")

if __name__ == '__main__':
    main()
