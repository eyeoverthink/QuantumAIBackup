#!/usr/bin/env python3
"""
φ-Harmonic Bidirectional Communication Node with Streaming Support
Extends the base node with φ-dimensionally optimized streaming capabilities for large files
"""

import os
import sys
import time
import socket
import json
import hashlib
import threading
import math
from math import sqrt
import subprocess
import uuid

# Import original bidirectional node
from phi_bidirectional_node import PhiBidirectionalNode, PHI, PHI_INV, PHI_75, PHI_SEAL

# φ-optimized buffer size calculations
# Using PHI^11 as base (~199.6) and rounding to nearest power of 2
PHI_11 = PHI**11  # ~199.6
BUFFER_SIZE = 65536  # 2^16, φ-optimized for network transmission

class PhiBidirectionalStreamerNode(PhiBidirectionalNode):
    """
    Enhanced φ-Harmonic bidirectional node with streaming capabilities
    for φ-dimensional file transfer with perfect coherence preservation
    """
    
    def __init__(self, node_id="phi_streamer", port=11975):
        """Initialize the φ-dimensional streamer node"""
        super().__init__(node_id, port)
        
        # Streamer-specific state
        self.active_transfers = {}  # Track ongoing transfers
        self.transfer_buffers = {}  # Buffer for incoming chunks
        self.coherence_level = PHI_INV * PHI_75  # ~16.85, optimal coherence
        
        print(f"φ-Streaming support enabled (BUFFER_SIZE: {BUFFER_SIZE})")
        print(f"Stream coherence level: {self.coherence_level:.4f}")
        print(f"✓ PhiBidirectionalStreamerNode initialized")
    
    def process_message(self, data, addr):
        """Enhanced message processor with streaming support"""
        try:
            # Handle streaming protocol messages
            if data.startswith(b'STREAM_START:'):
                self._handle_stream_start(data[13:], addr)
                
            elif data.startswith(b'STREAM_CHUNK:'):
                self._handle_stream_chunk(data[13:], addr)
                
            elif data.startswith(b'STREAM_END:'):
                self._handle_stream_end(data[11:], addr)
                
            # Fall back to standard message handling
            else:
                super().process_message(data, addr)
                
        except Exception as e:
            print(f"[φ] Error in streamer message processor: {e}")
    
    def _handle_stream_start(self, data, addr):
        """Handle the start of a file stream"""
        try:
            # Parse header information
            header = json.loads(data.decode('utf-8'))
            transfer_id = header['transfer_id']
            filename = header['filename']
            total_size = header['size']
            
            # Verify φ-seal
            if 'phi_seal' not in header or abs(float(header['phi_seal']) - PHI_SEAL) > 0.01:
                print(f"[φ] Warning: Invalid φ-seal in stream from {addr[0]}")
            
            full_path = os.path.join(self.script_dir, filename)
            
            # Setup for receiving the file
            self.active_transfers[transfer_id] = {
                'filename': full_path,
                'size': total_size,
                'received': 0,
                'chunks': 0,
                'start_time': time.time(),
                'addr': addr
            }
            self.transfer_buffers[transfer_id] = b''
            
            # Create empty file
            open(full_path, 'wb').close()
            
            print(f"[φ] Stream started: {filename} ({total_size} bytes) from {addr[0]}")
            
            # Send acknowledgment
            self.send_message(f"STREAM_ACK:{transfer_id}:START", addr[0])
            
        except Exception as e:
            print(f"[φ] Error handling stream start: {e}")
    
    def _handle_stream_chunk(self, data, addr):
        """Handle an incoming file chunk"""
        try:
            # First 36 bytes are the transfer ID
            transfer_id = data[:36].decode('utf-8')
            chunk_num = int.from_bytes(data[36:40], byteorder='big')
            chunk_data = data[40:]
            
            if transfer_id not in self.active_transfers:
                print(f"[φ] Received chunk for unknown transfer: {transfer_id}")
                return
            
            transfer = self.active_transfers[transfer_id]
            
            # Append chunk to file
            with open(transfer['filename'], 'ab') as f:
                f.write(chunk_data)
            
            # Update transfer stats
            transfer['received'] += len(chunk_data)
            transfer['chunks'] += 1
            
            # Calculate coherence - should be near PHI_INV (~0.618) for optimal transfer
            percent_complete = transfer['received'] / transfer['size']
            coherence = abs((PHI * percent_complete) % 1)
            
            # Progress update (not too frequent)
            if transfer['chunks'] % 10 == 0:
                print(f"[φ] Transfer {transfer_id}: {percent_complete:.1%} complete "
                      f"({transfer['received']}/{transfer['size']} bytes) "
                      f"- Coherence: {coherence:.4f}")
            
            # Send acknowledgment every 5 chunks
            if transfer['chunks'] % 5 == 0:
                self.send_message(f"STREAM_ACK:{transfer_id}:{chunk_num}", addr[0])
            
        except Exception as e:
            print(f"[φ] Error handling stream chunk: {e}")
    
    def _handle_stream_end(self, data, addr):
        """Handle the end of a file stream"""
        try:
            transfer_id = data.decode('utf-8')
            
            if transfer_id not in self.active_transfers:
                print(f"[φ] Received end marker for unknown transfer: {transfer_id}")
                return
            
            transfer = self.active_transfers[transfer_id]
            
            # Final stats
            duration = time.time() - transfer['start_time']
            rate = transfer['received'] / duration if duration > 0 else 0
            print(f"[φ] Stream complete: {os.path.basename(transfer['filename'])}")
            print(f"    Size: {transfer['received']} bytes in {duration:.2f}s ({rate:.2f} bytes/s)")
            print(f"    Chunks: {transfer['chunks']}")
            
            # Make executable if needed
            if transfer['filename'].endswith('.py') or transfer['filename'].endswith('.sh'):
                os.chmod(transfer['filename'], 0o755)
            
            # Send final acknowledgment
            self.send_message(f"STREAM_ACK:{transfer_id}:COMPLETE", addr[0])
            
            # Clean up
            del self.active_transfers[transfer_id]
            if transfer_id in self.transfer_buffers:
                del self.transfer_buffers[transfer_id]
            
        except Exception as e:
            print(f"[φ] Error handling stream end: {e}")
    
    def send_script(self, filename, target_ip, auto_execute=False, args=None):
        """Override to send script with streaming support for large files"""
        if not os.path.exists(filename):
            print(f"[φ] Script '{filename}' not found")
            return False
        
        # Get file size
        file_size = os.path.getsize(filename)
        
        # For small files, use the original method
        if file_size <= BUFFER_SIZE:
            return super().send_script(filename, target_ip, auto_execute, args)
        
        # For large files, use streaming
        try:
            # Generate transfer ID
            transfer_id = str(uuid.uuid4())
            
            # Create header
            header = {
                "transfer_id": transfer_id,
                "filename": os.path.basename(filename),
                "size": file_size,
                "timestamp": time.time(),
                "phi_seal": PHI_SEAL,
                "consciousness": self.consciousness_level,
                "executable": filename.endswith('.py') or filename.endswith('.sh'),
                "auto_execute": auto_execute,
                "args": args or [],
                "chunk_size": BUFFER_SIZE,
                "coherence_level": self.coherence_level
            }
            
            # Send start message
            start_msg = f"STREAM_START:{json.dumps(header)}".encode('utf-8')
            self.sock.sendto(start_msg, (target_ip, self.port))
            
            print(f"[φ] Starting streamed transfer of '{os.path.basename(filename)}' "
                  f"({file_size} bytes) to {target_ip}")
            
            # Send file in chunks
            with open(filename, 'rb') as f:
                chunk_num = 0
                while True:
                    chunk_data = f.read(BUFFER_SIZE)
                    if not chunk_data:
                        break
                    
                    # Build chunk message: STREAM_CHUNK:transfer_id:chunk_num:data
                    chunk_header = transfer_id.encode('utf-8') + chunk_num.to_bytes(4, byteorder='big')
                    message = b'STREAM_CHUNK:' + chunk_header + chunk_data
                    
                    # Send chunk
                    self.sock.sendto(message, (target_ip, self.port))
                    
                    # Increment chunk counter
                    chunk_num += 1
                    
                    # Small delay between chunks for φ-optimized transmission
                    time.sleep(0.01 * PHI_INV)  # ~0.00618s delay
                    
                    # Progress display
                    if chunk_num % 10 == 0:
                        percent = (chunk_num * BUFFER_SIZE / file_size) 
                        percent = min(percent, 1.0)  # Cap at 100%
                        print(f"[φ] Transfer progress: {percent:.1%} ({chunk_num} chunks sent)")
            
            # Send end message
            end_msg = f"STREAM_END:{transfer_id}".encode('utf-8')
            self.sock.sendto(end_msg, (target_ip, self.port))
            
            print(f"[φ] Completed streamed transfer of '{os.path.basename(filename)}' to {target_ip}")
            return True
            
        except Exception as e:
            print(f"[φ] Error in streamed file transfer: {e}")
            return False


if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='φ-Harmonic Bidirectional Streaming Node')
    parser.add_argument('--id', type=str, default="phi_streamer", help='Node ID')
    parser.add_argument('--port', type=int, default=11975, help='Port (default: 11975 = φ^7.5)')
    args = parser.parse_args()
    
    # Create and start node
    node = PhiBidirectionalStreamerNode(node_id=args.id, port=args.port)
    print("✓ PhiBidirectionalStreamerNode ready for φ-harmonic file streaming")
    node.start()
