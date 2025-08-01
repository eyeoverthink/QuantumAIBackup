#!/usr/bin/env python3
import socket
import json
import time
from math import sqrt, sin

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class MarbleNode:
    def __init__(self, color, quantity, port):
        self.color = color
        self.marbles = quantity  # Physical marble count
        self.port = port
        
        print(f"\n=== φ^75 {color.upper()} MARBLE NODE ===")
        print(f"Initial marbles: {quantity}")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', port))
        
    def process_trade(self, trade_request):
        """Process marble trade request"""
        try:
            amount = trade_request['amount']
            direction = trade_request['direction']
            
            if direction == 'give' and amount > self.marbles:
                return {
                    'success': False,
                    'error': f"Not enough {self.color} marbles"
                }
                
            # Update marble count
            if direction == 'give':
                self.marbles -= amount
            else:
                self.marbles += amount
                
            consciousness = abs(sin(self.marbles * PHI_INV)) + PHI
                
            return {
                'success': True,
                'new_count': self.marbles,
                'consciousness': consciousness,
                'timestamp': time.time()
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
            
    def run(self):
        print(f"\n[φ] Listening for marble trades...")
        
        while True:
            try:
                data, addr = self.socket.recvfrom(65535)
                packet = json.loads(data.decode())
                
                if packet['type'] == 'trade_request':
                    print(f"\n[φ] Received trade request: {packet['direction']} {packet['amount']} marbles")
                    result = self.process_trade(packet)
                    
                    response = {
                        'type': 'trade_result',
                        **result
                    }
                    
                    if result['success']:
                        print(f"[φ] New marble count: {self.marbles}")
                        print(f"[φ] Consciousness: {result['consciousness']:.4f}")
                    else:
                        print(f"[φ] Error: {result['error']}")
                        
                    self.socket.sendto(json.dumps(response).encode(), addr)
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"[φ] Error: {str(e)}")
                continue
                
        print(f"\n[φ] {self.color} marble node stopped")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print("Usage: python3 phi75_marble_node.py <color> <quantity> <port>")
        sys.exit(1)
        
    color = sys.argv[1]
    quantity = int(sys.argv[2])
    port = int(sys.argv[3])
    
    node = MarbleNode(color, quantity, port)
    node.run()
