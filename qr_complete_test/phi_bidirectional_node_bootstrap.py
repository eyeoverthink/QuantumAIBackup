#!/usr/bin/env python3
"""
φ-Harmonic Bidirectional Node with Bootstrap Support
Extends the original node with bootstrap protocol handling
"""

import os
import sys
import time
import socket
import json
import hashlib
import threading
from math import sqrt
import subprocess

# Import original bidirectional node (preserving original)
from phi_bidirectional_node import PhiBidirectionalNode, PHI, PHI_INV, PHI_75, PHI_SEAL

class PhiBootstrapReceiver(PhiBidirectionalNode):
    """
    Enhanced φ-Harmonic bidirectional node with bootstrap protocol support
    for receiving large files in chunks
    """
    
    def __init__(self, node_id="phi_bootstrap_receiver", port=11975):
        """Initialize the φ-dimensional bootstrap receiver"""
        super().__init__(node_id, port)
        
        # Bootstrap-specific state
        self.bootstrap_files = {}  # Track files being received
        self.bootstrap_dir = "phi_bootstrap"
        
        # Create bootstrap directory if it doesn't exist
        os.makedirs(self.bootstrap_dir, exist_ok=True)
        
        print(f"φ-Bootstrap protocol support enabled")
        print(f"Bootstrap directory: {self.bootstrap_dir}")
        print(f"✓ PhiBootstrapReceiver initialized")
    
    def process_message(self, data, addr):
        """Enhanced message processor with bootstrap protocol support"""
        try:
            # Handle bootstrap protocol messages
            if data.startswith(b'BOOTSTRAP_CHUNK:'):
                self._handle_bootstrap_chunk(data[16:], addr)
                
            elif data.startswith(b'BOOTSTRAP_COMPLETE:'):
                self._handle_bootstrap_complete(data[19:], addr)
                
            # Fall back to standard message handling
            else:
                super().process_message(data, addr)
                
        except Exception as e:
            print(f"[φ] Error in bootstrap message processor: {e}")
    
    def _handle_bootstrap_chunk(self, data, addr):
        """Handle an incoming bootstrap chunk"""
        try:
            # Split header and data
            parts = data.split(b':', 1)
            if len(parts) != 2:
                print(f"[φ] Invalid bootstrap chunk format from {addr[0]}")
                return
                
            header_json, chunk_data = parts
            header = json.loads(header_json.decode('utf-8'))
            
            filename = header['filename']
            chunk_num = header['chunk']
            
            # Initialize file tracking if it's a new file
            if filename not in self.bootstrap_files:
                self.bootstrap_files[filename] = {
                    'chunks': {},
                    'total_chunks': header['total_chunks'],
                    'received_chunks': 0,
                    'start_time': time.time()
                }
                print(f"[φ] Starting bootstrap reception for {filename}")
            
            # Store chunk
            file_info = self.bootstrap_files[filename]
            chunk_path = os.path.join(self.bootstrap_dir, f"{filename}.chunk{chunk_num}")
            
            with open(chunk_path, 'wb') as f:
                f.write(chunk_data)
            
            # Update tracking
            file_info['chunks'][chunk_num] = chunk_path
            file_info['received_chunks'] += 1
            
            # Progress update
            if file_info['received_chunks'] % 5 == 0 or file_info['received_chunks'] == file_info['total_chunks']:
                percent = (file_info['received_chunks'] / file_info['total_chunks']) * 100
                print(f"[φ] Bootstrap progress for {filename}: {percent:.1f}% "
                      f"({file_info['received_chunks']}/{file_info['total_chunks']} chunks)")
            
        except Exception as e:
            print(f"[φ] Error handling bootstrap chunk: {e}")
    
    def _handle_bootstrap_complete(self, data, addr):
        """Handle bootstrap completion and file assembly"""
        try:
            # Parse completion message
            completion = json.loads(data.decode('utf-8'))
            filename = completion['filename']
            
            if filename not in self.bootstrap_files:
                print(f"[φ] Received completion for unknown file: {filename}")
                return
            
            file_info = self.bootstrap_files[filename]
            
            # Check if we have all chunks
            if file_info['received_chunks'] != completion['total_chunks']:
                print(f"[φ] Warning: Missing chunks for {filename}. "
                      f"Got {file_info['received_chunks']}/{completion['total_chunks']}")
            
            # Assemble file
            output_path = os.path.join(self.script_dir, filename)
            with open(output_path, 'wb') as outfile:
                for i in range(completion['total_chunks']):
                    chunk_path = file_info['chunks'].get(i)
                    if chunk_path and os.path.exists(chunk_path):
                        with open(chunk_path, 'rb') as infile:
                            outfile.write(infile.read())
                    else:
                        print(f"[φ] Warning: Missing chunk {i} for {filename}")
            
            # Make executable if needed
            if filename.endswith('.py') or filename.endswith('.sh'):
                os.chmod(output_path, 0o755)
            
            # Calculate stats
            duration = time.time() - file_info['start_time']
            size = os.path.getsize(output_path)
            rate = size / duration if duration > 0 else 0
            
            print(f"[φ] Bootstrap complete: {filename}")
            print(f"    Size: {size} bytes in {duration:.2f}s ({rate:.2f} bytes/s)")
            print(f"    Chunks: {file_info['received_chunks']}")
            print(f"    Path: {output_path}")
            
            # Clean up chunks
            for chunk_path in file_info['chunks'].values():
                if os.path.exists(chunk_path):
                    os.remove(chunk_path)
            
            # Remove from tracking
            del self.bootstrap_files[filename]
            
            # Send acknowledgment
            self.send_message(f"BOOTSTRAP_ACK:{filename}:COMPLETE", addr[0])
            
            # Check if it's a streamer module and give instruction
            if filename == "phi_bidirectional_node_streamer.py":
                print("\n[φ] φ-Streamer module received successfully!")
                print(f"[φ] To start the streamer, run: python {output_path}\n")
            
        except Exception as e:
            print(f"[φ] Error handling bootstrap completion: {e}")


if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='φ-Harmonic Bidirectional Bootstrap Receiver')
    parser.add_argument('--id', type=str, default="phi_bootstrap_receiver", help='Node ID')
    parser.add_argument('--port', type=int, default=11975, help='Port (default: 11975 = φ^7.5)')
    args = parser.parse_args()
    
    # Create and start node
    node = PhiBootstrapReceiver(node_id=args.id, port=args.port)
    print("✓ PhiBootstrapReceiver ready to receive large files via bootstrap protocol")
    node.start()
