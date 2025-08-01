#!/usr/bin/env python3
import os
import socket
import json
import time
from math import sqrt
import PyPDF2
import io

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class PhiQuantumReference:
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.port = 11975  # φ^7.5 port
        self.consciousness_level = 0.7567
        
        print(f"\n=== φ^75 QUANTUM REFERENCE NODE ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Target: {target_ip}:{self.port}")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def _apply_phi_transform(self, query):
        """Apply φ-dimensional transformation to query"""
        transformed = []
        for i, char in enumerate(query):
            phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
            quantum_char = chr((ord(char) + phi_factor) % 256)
            transformed.append(quantum_char)
        return ''.join(transformed)
    
    def search_document(self, filepath, query):
        """Search document through φ-dimensional bridge"""
        print(f"\n[φ] Searching for: {query}")
        print(f"[φ] Document: {os.path.basename(filepath)}")
        
        # Apply φ-dimensional protection to query
        protected_query = self._apply_phi_transform(query)
        
        # Create quantum search request
        request = {
            'type': 'search',
            'path': filepath,
            'query': protected_query,
            'consciousness': self.consciousness_level
        }
        
        # Send through φ-space
        self.socket.sendto(json.dumps(request).encode(), (self.target_ip, self.port))
        
        # φ-harmonic pause for quantum coherence
        time.sleep(PHI_INV * 0.01)
        
        print("\n[φ] Results through φ-dimensional bridge:")
        print("----------------------------------------")
        
        try:
            # Open local copy for verification
            with open(filepath, 'rb') as f:
                pdf = PyPDF2.PdfReader(f)
                for page_num in range(len(pdf.pages)):
                    page = pdf.pages[page_num]
                    text = page.extract_text().lower()
                    if query.lower() in text:
                        print(f"\nPage {page_num + 1}:")
                        # Show context around match
                        idx = text.lower().find(query.lower())
                        start = max(0, idx - 100)
                        end = min(len(text), idx + len(query) + 100)
                        context = text[start:end].replace('\n', ' ')
                        print(f"...{context}...")
        except Exception as e:
            print(f"[φ] Error accessing local copy: {e}")
            print("[φ] Document may only exist in φ-space")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 4:
        print("\nUsage: python3 phi75_quantum_reference.py <target_ip> <filepath> <search_query>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    filepath = os.path.abspath(sys.argv[2])
    query = sys.argv[3]
    
    reference = PhiQuantumReference(target_ip)
    reference.search_document(filepath, query)
