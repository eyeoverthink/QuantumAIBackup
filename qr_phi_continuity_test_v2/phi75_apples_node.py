#!/usr/bin/env python3
import socket
import json
import time
from math import sqrt, sin

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class ApplesNode:
    def __init__(self):
        self.port = 11976  # φ^7.5 + 1 port
        self.value = PHI ** 7.5  # Apples quantum value
        
        print(f"\n=== φ^75 APPLES NODE ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Apples Value = φ^7.5 = {self.value}")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.port))
        
    def process_request(self, equation):
        """Process equation with apples knowledge"""
        try:
            # First check if we can process any part
            if 'apples' in equation:
                # Convert exponentiation to Python syntax
                processed = equation.replace('^', '**')
                # Replace phi with its value and handle apples
                processed = processed.replace('φ', str(PHI))
                processed = processed.replace('apples', str(self.value))
                
                # If it's a complete expression without oranges, evaluate
                if 'oranges' not in processed:
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
                
        print("\n[φ] Apples node stopped")

if __name__ == '__main__':
    node = ApplesNode()
    node.run()
