#!/usr/bin/env python3
import socket
import json
import time
from math import sqrt

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2

class MarbleOrchestrator:
    def __init__(self):
        self.nodes = {
            'red': ('192.168.3.152', 11974),    # First Mac
            'blue': ('192.168.3.116', 11975)    # Second Mac
        }
        
        # Initialize socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def trade_marbles(self, from_color, to_color, amount):
        """Execute marble trade between nodes"""
        try:
            # First check if giver has enough marbles
            give_request = {
                'type': 'trade_request',
                'direction': 'give',
                'amount': amount
            }
            
            # Send to giving node
            self.socket.sendto(json.dumps(give_request).encode(), self.nodes[from_color])
            data, _ = self.socket.recvfrom(65535)
            give_result = json.loads(data.decode())
            
            if not give_result['success']:
                print(f"\n[φ] Error: {give_result['error']}")
                return False
                
            # If successful, send to receiving node
            receive_request = {
                'type': 'trade_request',
                'direction': 'receive',
                'amount': amount
            }
            
            # Send to receiving node
            self.socket.sendto(json.dumps(receive_request).encode(), self.nodes[to_color])
            data, _ = self.socket.recvfrom(65535)
            receive_result = json.loads(data.decode())
            
            if receive_result['success']:
                print(f"\n[φ] === MARBLE TRADE COMPLETE ===")
                print(f"[φ] {amount} marbles transferred from {from_color} to {to_color}")
                print(f"[φ] New Counts:")
                print(f"[φ] {from_color}: {give_result['new_count']}")
                print(f"[φ] {to_color}: {receive_result['new_count']}")
                print(f"\n[φ] Consciousness Fields:")
                print(f"[φ] {from_color}: {give_result['consciousness']:.4f}")
                print(f"[φ] {to_color}: {receive_result['consciousness']:.4f}")
                
                # Calculate φ-harmonic balance
                ratio = give_result['new_count'] / receive_result['new_count']
                target = PHI
                print(f"\n[φ] φ-Harmonic Balance:")
                print(f"[φ] Current Ratio: {ratio:.4f}")
                print(f"[φ] Target Ratio: {target:.4f}")
                print(f"[φ] Balance Delta: {abs(ratio - target):.4f}")
                
            return receive_result['success']
            
        except Exception as e:
            print(f"\n[φ] Error: {str(e)}")
            return False

def main():
    orchestrator = MarbleOrchestrator()
    
    print("\n=== φ^75 MARBLE ORCHESTRATOR ===")
    print("Using φ-harmonic principles (φ = 1.618033988749895)")
    print("\nConnected nodes:")
    print("- Red Marbles Node: 192.168.3.152")
    print("- Blue Marbles Node: 192.168.3.116")
    
    print("\nCommands:")
    print("1. trade <from> <to> <amount> - Transfer marbles")
    print("2. q - Quit")
    
    while True:
        try:
            cmd = input("\n[φ] Enter command: ").strip().lower()
            if cmd == 'q':
                break
                
            if cmd.startswith('trade'):
                try:
                    _, from_color, to_color, amount = cmd.split()
                    amount = int(amount)
                    orchestrator.trade_marbles(from_color, to_color, amount)
                except:
                    print("[φ] Error: Invalid trade command")
                    print("[φ] Format: trade <from> <to> <amount>")
                    continue
                    
        except KeyboardInterrupt:
            break
            
    print("\n[φ] Marble orchestrator stopped")

if __name__ == '__main__':
    main()
