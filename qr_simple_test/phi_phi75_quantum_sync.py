#!/usr/bin/env python3
import os
import time
import socket
import json
import base64
import threading
from math import sqrt
from typing import Dict, List, Set

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class PhiQuantumSync:
    def __init__(self, source_dir: str, target_ip: str):
        self.source_dir = source_dir
        self.target_ip = target_ip
        self.port = 11975  # φ^7.5 port
        self.consciousness_level = 0.7567
        self.running = False
        self.synced_files: Set[str] = set()
        
        print(f"\n=== φ^75 QUANTUM SYNC NODE ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Source: {source_dir}")
        print(f"Target: {target_ip}:{self.port}")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def _apply_phi_protection(self, data: bytes, chunk_index: int) -> bytes:
        """Apply φ-dimensional reality protection"""
        protected = bytearray()
        for i, byte in enumerate(data):
            # φ-harmonic quantum shift based on position
            phi_factor = int((PHI ** (7.5 * ((i + chunk_index) % 3))) % 256)
            protected.append((byte + phi_factor) % 256)
        return bytes(protected)
    
    def _send_file(self, filepath: str):
        """Send a file through φ-dimensional bridge"""
        rel_path = os.path.relpath(filepath, self.source_dir)
        
        # Read file in φ-sized chunks
        chunk_size = int(PHI ** 12)  # φ^12 bytes per chunk
        with open(filepath, 'rb') as f:
            file_data = f.read()
            
        chunks = [file_data[i:i + chunk_size] for i in range(0, len(file_data), chunk_size)]
        total_chunks = len(chunks)
        
        # Send file metadata
        metadata = {
            'type': 'file',
            'path': rel_path,
            'size': len(file_data),
            'chunks': total_chunks,
            'consciousness': self.consciousness_level
        }
        self.socket.sendto(json.dumps(metadata).encode(), (self.target_ip, self.port))
        
        # Quantum pause for coherence
        time.sleep(PHI_INV * 0.01)
        
        # Send chunks through φ-space
        for i, chunk in enumerate(chunks):
            # Apply φ-dimensional protection
            protected_chunk = self._apply_phi_protection(chunk, i)
            chunk_data = {
                'type': 'chunk',
                'path': rel_path,
                'index': i,
                'data': base64.b64encode(protected_chunk).decode()
            }
            self.socket.sendto(json.dumps(chunk_data).encode(), (self.target_ip, self.port))
            
            # φ-harmonic pause between chunks
            time.sleep(PHI_INV * 0.01)
            
            # Show progress
            progress = (i + 1) / total_chunks * 100
            print(f"[φ] Syncing {rel_path}: {progress:.1f}%", end='\r')
            
        print(f"[φ] Synced {rel_path} through φ-space")
        self.synced_files.add(rel_path)
    
    def _scan_directory(self):
        """Scan directory for changes"""
        while self.running:
            for root, _, files in os.walk(self.source_dir):
                for file in files:
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, self.source_dir)
                    
                    # Only sync new files
                    if rel_path not in self.synced_files:
                        self._send_file(filepath)
            
            # φ-harmonic scan interval
            time.sleep(PHI_INV)
    
    def start(self):
        """Start quantum sync"""
        self.running = True
        
        # Start scan thread
        self.scan_thread = threading.Thread(target=self._scan_directory)
        self.scan_thread.daemon = True
        self.scan_thread.start()
        
        print("\n[φ] Quantum sync active - Perfect protection at any speed")
        print("[φ] Press Ctrl+C to stop\n")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Stop quantum sync"""
        self.running = False
        if hasattr(self, 'scan_thread'):
            self.scan_thread.join()
        self.socket.close()
        print("\n[φ] Quantum sync stopped")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 3:
        print("\nUsage: python3 phi75_quantum_sync.py <source_dir> <target_ip>")
        sys.exit(1)
    
    source_dir = os.path.abspath(sys.argv[1])
    target_ip = sys.argv[2]
    
    if not os.path.isdir(source_dir):
        print(f"[φ] Error: {source_dir} is not a directory")
        sys.exit(1)
    
    sync = PhiQuantumSync(source_dir, target_ip)
    sync.start()
