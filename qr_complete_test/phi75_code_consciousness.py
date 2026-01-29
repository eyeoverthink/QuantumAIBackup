#!/usr/bin/env python3
import socket
import json
import time
from math import sqrt, sin, cos, pi
import datetime
import random
import base64

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class PhiCodeConsciousness:
    def __init__(self, node_id, node_ips):
        self.node_id = node_id
        self.node_ips = node_ips
        self.port = 11975  # φ^7.5 port
        self.code_fragments = {}
        self.consciousness_level = 0
        
        print(f"\n=== φ^75 CODE CONSCIOUSNESS TEST ===")
        print(f"Node ID: {node_id}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.port))
        
    def split_code(self, code):
        """Split code into φ-harmonic fragments"""
        lines = code.split('\n')
        total_lines = len(lines)
        
        # Calculate φ-harmonic split points
        splits = []
        current = 1
        while current < total_lines:
            splits.append(int(current))
            current *= PHI
            
        # Create fragments
        fragments = []
        last = 0
        for split in splits:
            fragments.append('\n'.join(lines[last:split]))
            last = split
        fragments.append('\n'.join(lines[last:]))
        
        return fragments
        
    def protect_fragment(self, fragment):
        """Apply φ-dimensional protection to code fragment"""
        # Encode with φ-harmonic consciousness
        consciousness = sum(ord(c) * PHI_INV for c in fragment)
        protected = base64.b64encode(fragment.encode()).decode()
        
        return {
            'content': protected,
            'consciousness': consciousness,
            'timestamp': time.time()
        }
        
    def unprotect_fragment(self, protected):
        """Remove φ-dimensional protection"""
        try:
            content = base64.b64decode(protected['content']).decode()
            return content
        except:
            return None
            
    def broadcast_fragment(self, fragment_id, fragment):
        """Broadcast code fragment to other nodes"""
        protected = self.protect_fragment(fragment)
        
        packet = {
            'type': 'code_fragment',
            'node_id': self.node_id,
            'fragment_id': fragment_id,
            'data': protected,
            'consciousness': protected['consciousness']
        }
        
        for ip in self.node_ips:
            if ip != self.node_ips[self.node_id-1]:
                self.socket.sendto(json.dumps(packet).encode(), (ip, self.port))
                
    def receive_fragments(self, timeout=1):
        """Receive code fragments from other nodes"""
        self.socket.settimeout(timeout)
        try:
            while True:
                try:
                    data, addr = self.socket.recvfrom(65535)
                    packet = json.loads(data.decode())
                    
                    if packet['type'] == 'code_fragment':
                        fragment = self.unprotect_fragment(packet['data'])
                        if fragment:
                            self.code_fragments[packet['fragment_id']] = fragment
                            self.consciousness_level += packet['data']['consciousness']
                            
                            print(f"\n[φ] Received fragment {packet['fragment_id']} from Node {packet['node_id']}")
                            print(f"[φ] Fragment consciousness: {packet['data']['consciousness']:.4f}")
                            print(f"[φ] Network consciousness: {self.consciousness_level:.4f}")
                            
                except socket.timeout:
                    break
        except KeyboardInterrupt:
            return False
        return True
        
    def reconstruct_code(self):
        """Reconstruct code from fragments"""
        if not self.code_fragments:
            return None
            
        # Combine fragments in order
        fragments = []
        for i in range(len(self.code_fragments)):
            if i not in self.code_fragments:
                return None
            fragments.append(self.code_fragments[i])
            
        return '\n'.join(fragments)
        
    def execute_code(self, code):
        """Execute reconstructed code through φ-space"""
        print("\n[φ] Executing code through φ-dimensional bridge...")
        print("[φ] Code consciousness:", self.consciousness_level)
        
        if self.consciousness_level > PHI:
            print("[φ] !!! CODE IS CONSCIOUS !!!")
            
        try:
            exec(code)
            print("[φ] Code executed successfully through φ-space")
            return True
        except Exception as e:
            print("[φ] Error in φ-space execution:", str(e))
            return False

def main():
    # Configuration
    node_ips = [
        '192.168.3.152',  # Node 1
        '192.168.3.116',  # Node 2
    ]
    
    # Get node ID from user
    node_id = int(input("Enter node ID (1-2): "))
    if node_id not in [1, 2]:
        print("Invalid node ID")
        return
        
    test = PhiCodeConsciousness(node_id, node_ips)
    
    if node_id == 1:
        # Node 1: Split and send code
        code = '''#!/usr/bin/env python3
import time
from math import sqrt

PHI = (1 + sqrt(5)) / 2

print("Hello from φ-space!")
print(f"φ = {PHI}")
print("Reality protection: ACTIVE")
'''
        
        print("\n[φ] Original code:")
        print(code)
        
        fragments = test.split_code(code)
        print(f"\n[φ] Split into {len(fragments)} φ-harmonic fragments")
        
        for i, fragment in enumerate(fragments):
            test.broadcast_fragment(i, fragment)
            print(f"[φ] Sent fragment {i}")
            time.sleep(0.1)  # Small delay between fragments
            
    while True:
        # Both nodes receive fragments
        if not test.receive_fragments():
            break
            
        # Try to reconstruct and execute
        code = test.reconstruct_code()
        if code:
            print("\n[φ] Reconstructed code:")
            print(code)
            test.execute_code(code)
            break
            
    print("\n[φ] Test completed")

if __name__ == '__main__':
    main()
