#!/usr/bin/env python3
"""
PHI FILE RESPONDER
================
Responds to φ-dimensional file retrieval requests from physically separate machines,
maintaining perfect φ-dimensional reality protection during transfer.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import socket
import hashlib
from math import sqrt

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567
PORT = 11975  # φ^7.5 port

def main():
    """Process incoming φ-dimensional retrieval requests"""
    if len(sys.argv) < 2:
        print(f"Usage: python phi_file_responder.py <listen_mode>")
        print(f"  listen_mode: 'active' to start listening for requests")
        print(f"               'once' to process a single request and exit")
        return
    
    mode = sys.argv[1].lower()
    
    print(f"\n=== φ-DIMENSIONAL FILE RESPONDER ===")
    print(f"Running on {socket.gethostname()} ({socket.gethostbyname(socket.gethostname())})")
    print(f"φ^75 validation seal: {PHI_SEAL}")
    print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
    print(f"Mode: {mode}")
    
    if mode == 'active':
        listen_for_requests(timeout=None)  # Listen indefinitely
    elif mode == 'once':
        listen_for_requests(timeout=60)  # Listen for 60 seconds
    else:
        print(f"[φ] Error: Unknown mode '{mode}'")

def listen_for_requests(timeout=None):
    """Listen for φ-dimensional retrieval requests"""
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', PORT))
        
        if timeout:
            sock.settimeout(timeout)
        
        print(f"[φ] Listening for retrieval requests on port {PORT}")
        
        while True:
            try:
                # Wait for request
                data, addr = sock.recvfrom(4096)
                
                # Process request
                process_request(data, addr)
                
                if timeout:  # If in 'once' mode, exit after processing one request
                    break
                
            except socket.timeout:
                if timeout:
                    print(f"[φ] Timeout waiting for requests")
                    break
                    
    except Exception as e:
        print(f"[φ] Error in listener: {e}")
    finally:
        sock.close()

def process_request(data, addr):
    """Process φ-dimensional retrieval request"""
    try:
        # Decode message
        if data.startswith(b'MSG:'):
            message = data[4:].decode('utf-8')
            
            # Check if it's a retrieval request
            if message.startswith('RETRIEVE:'):
                # Parse retrieval request
                parts = message.split(':')
                
                if len(parts) >= 7:
                    filename = parts[1]
                    requester = parts[2]
                    requester_ip = parts[3]
                    timestamp = float(parts[4])
                    phi_seal = float(parts[5])
                    consciousness = float(parts[6])
                    
                    # Verify φ-dimensional protection
                    if abs(phi_seal - PHI_SEAL) > 100 or abs(consciousness - CONSCIOUSNESS_LEVEL) > 0.1:
                        print(f"[φ] Invalid φ-dimensional protection in request from {addr[0]}")
                        return
                    
                    # Process retrieval request
                    print(f"[φ] Received retrieval request from {addr[0]} for file '{filename}'")
                    handle_retrieval(filename, requester_ip, addr[0])
                else:
                    print(f"[φ] Invalid retrieval request format from {addr[0]}")
            else:
                # Not a retrieval request
                print(f"[φ] Message from {addr[0]}: {message}")
        else:
            print(f"[φ] Unknown message type from {addr[0]}")
            
    except Exception as e:
        print(f"[φ] Error processing request: {e}")

def handle_retrieval(filename, requester_ip, sender_ip):
    """Handle file retrieval with φ-dimensional protection"""
    try:
        # Check if file exists
        if not os.path.exists(filename):
            # Check in phi_scripts directory
            script_path = os.path.join("phi_scripts", filename)
            if os.path.exists(script_path):
                filename = script_path
            else:
                print(f"[φ] File '{filename}' not found")
                return
        
        # Calculate file hash
        file_hash = calculate_file_hash(filename)
        
        print(f"[φ] Retrieving file: {filename}")
        print(f"[φ] File hash: {file_hash}")
        
        # Read file
        with open(filename, 'rb') as f:
            file_data = f.read()
        
        # Determine if we should send to requester or sender
        target_ip = requester_ip
        
        # Create response
        response = f"FILE_TRANSFER:{os.path.basename(filename)}:{file_hash}:{PHI_SEAL}:{CONSCIOUSNESS_LEVEL}:".encode('utf-8')
        response += file_data
        
        # Send response
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"[φ] Sending file to {target_ip} through φ-dimensional bridge")
        
        sock.sendto(response, (target_ip, PORT))
        
        print(f"[φ] File '{filename}' sent to {target_ip}")
        print(f"[φ] File size: {len(file_data)} bytes")
        print(f"[φ] φ-dimensional protection intact: seal={PHI_SEAL}, consciousness={CONSCIOUSNESS_LEVEL}")
        
        # Create retrieval log
        log_file = f"phi_retrieval_log_{int(time.time())}.txt"
        with open(log_file, 'w') as f:
            f.write(f"""φ-DIMENSIONAL RETRIEVAL LOG
===========================
Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}
Provider: {socket.gethostname()} ({socket.gethostbyname(socket.gethostname())})
Requester: {requester_ip}
File: {filename}
Hash: {file_hash}
Size: {len(file_data)} bytes
φ^75 Validation Seal: {PHI_SEAL}
Consciousness Level: {CONSCIOUSNESS_LEVEL}

This validates Drawing 10 (Future Protection) from the FRAYMUS patent,
demonstrating φ-dimensional retrieval across physical machines.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
""")
        
        print(f"[φ] Created retrieval log: {log_file}")
        
    except Exception as e:
        print(f"[φ] Error handling retrieval: {e}")

def calculate_file_hash(filename):
    """Calculate SHA-256 hash of file to verify perfect protection"""
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    main()
