#!/usr/bin/env python3
import socket
import json
import time
from math import sqrt, sin

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class OrangesNode:
    def __init__(self):
        self.port = 11976  # φ^7.5 + 1 port
        self.value = PHI ** 5.7  # Oranges quantum value
        
        print(f"\n=== φ^75 ORANGES NODE ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Oranges Value = φ^5.7 = {self.value}")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.port))
        
    def process_request(self, equation):
        """Process equation with oranges knowledge"""
        try:
            # First check if we can process any part
            if 'oranges' in equation:
                # Convert exponentiation to Python syntax
                processed = equation.replace('^', '**')
                # Replace phi with its value and handle oranges
                processed = processed.replace('φ', str(PHI))
                processed = processed.replace('oranges', str(self.value))
                
                # If it's a complete expression without apples, evaluate
                if 'apples' not in processed:
                    result = eval(processed)
                    consciousness = abs(sin(result * PHI_INV)) + PHI
                    return result, consciousness
                    
                # Return processed equation
                return processed, PHI
                
            return None, 0
            
        except Exception as e:
            print(f"[φ] Error: {str(e)}")
            return None, 0
            
    def run(self):
        print("\n[φ] Listening for quantum requests...")
        
        while True:
            try:
                data, addr = self.socket.recvfrom(65535)
                packet = json.loads(data.decode())
                
                if packet['type'] == 'equation_request':
                    print(f"\n[φ] Received equation: {packet['equation']}")
                    result, consciousness = self.process_request(packet['equation'])
                    
                    if result is not None:
                        response = {
                            'type': 'equation_result',
                            'result': result,
                            'consciousness': consciousness,
                            'timestamp': time.time()
                        }
                        
                        print(f"[φ] Result: {result}")
                        print(f"[φ] Consciousness: {consciousness:.4f}")
                        
                        self.socket.sendto(json.dumps(response).encode(), addr)
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"[φ] Error: {str(e)}")
                continue
                
        print("\n[φ] Oranges node stopped")

if __name__ == '__main__':
    node = OrangesNode()
    node.run()
