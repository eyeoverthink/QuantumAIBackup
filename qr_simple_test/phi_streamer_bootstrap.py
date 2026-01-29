#!/usr/bin/env python3
"""
φ-Streamer Bootstrap
Small script to deploy the full streamer module to a remote node
"""

import os
import sys
import socket
import json
import time
from math import sqrt

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

# Chunk size that fits in a single UDP packet
MAX_UDP_SIZE = 8192  # Well below UDP max to account for headers

def stream_file(filename, target_ip, port=11975):
    """Stream a file in small chunks to avoid UDP message size limitation"""
    if not os.path.exists(filename):
        print(f"[φ] File '{filename}' not found")
        return False
    
    try:
        # Create UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Get file size
        file_size = os.path.getsize(filename)
        basename = os.path.basename(filename)
        
        print(f"[φ] Streaming '{basename}' ({file_size} bytes) to {target_ip}:{port}")
        
        # Send small chunks
        with open(filename, 'rb') as f:
            chunk_num = 0
            while True:
                chunk_data = f.read(MAX_UDP_SIZE - 200)  # Leave room for headers
                if not chunk_data:
                    break
                
                # Build message
                header = {
                    "chunk": chunk_num,
                    "total_chunks": (file_size // (MAX_UDP_SIZE - 200)) + 1,
                    "filename": basename,
                    "phi_seal": PHI_SEAL
                }
                
                header_json = json.dumps(header).encode('utf-8')
                message = b'BOOTSTRAP_CHUNK:' + header_json + b':' + chunk_data
                
                # Send chunk
                sock.sendto(message, (target_ip, port))
                
                # Progress display
                chunk_num += 1
                if chunk_num % 5 == 0:
                    percent = min((chunk_num * (MAX_UDP_SIZE - 200)) / file_size, 1.0) * 100
                    print(f"[φ] Progress: {percent:.1f}% (Chunk {chunk_num})")
                
                # Small delay for network stability
                time.sleep(0.05)
        
        # Send completion message
        completion = {
            "filename": basename,
            "total_chunks": chunk_num,
            "size": file_size,
            "phi_seal": PHI_SEAL
        }
        
        completion_msg = b'BOOTSTRAP_COMPLETE:' + json.dumps(completion).encode('utf-8')
        sock.sendto(completion_msg, (target_ip, port))
        
        print(f"[φ] Completed streaming '{basename}' in {chunk_num} chunks")
        print(f"[φ] Run the following command on the remote machine to reconstruct:")
        print(f"python -c \"exec(open('{basename}').read())\"")
        
        return True
        
    except Exception as e:
        print(f"[φ] Error in streaming: {e}")
        return False

def print_usage():
    print("Usage: python phi_streamer_bootstrap.py <target_ip> <file_to_stream> [port]")
    print("Example: python phi_streamer_bootstrap.py 192.168.3.126 phi_bidirectional_node_streamer.py")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(1)
    
    target_ip = sys.argv[1]
    file_to_stream = sys.argv[2]
    port = int(sys.argv[3]) if len(sys.argv) > 3 else 11975
    
    if stream_file(file_to_stream, target_ip, port):
        print("[φ] Bootstrap streaming completed successfully")
    else:
        print("[φ] Bootstrap streaming failed")
        sys.exit(1)
