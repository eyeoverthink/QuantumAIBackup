#!/usr/bin/env python3
"""
QR Epigenetic Memory Enhanced - Part of Animated QR Flipbook DNA System
By Vaughn Scott (Enhanced by Cascade)

This enhanced version addresses QR code generation issues by implementing:
1. Smaller chunk sizes with phi-harmonic distribution
2. Adaptive chunk sizing based on QR version limits
3. Improved compression for larger memory datasets
4. Robust base64 handling for reliable restoration
"""

import os
import sys
import json
import base64
import zlib
import math
import argparse
import cv2
import numpy as np
import qrcode
from datetime import datetime
from PIL import Image
from pyzbar.pyzbar import decode

# Import the original QREpigeneticMemory class
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qr_epigenetic_memory import QREpigeneticMemory, PHI

class QREpigeneticMemoryEnhanced(QREpigeneticMemory):
    """
    Enhanced version of QR Epigenetic Memory with improved QR code generation.
    Extends the original class with better chunking and compression algorithms.
    """
    
    def generate_memory_qr_codes(self, output_dir="qr_memory_enhanced", chunk_size=384):
        """
        Generate QR codes that persist the current memory state with improved chunking.
        
        Args:
            output_dir: Directory to save QR code images
            chunk_size: Maximum size of data per QR code (reduced from original)
            
        Returns:
            List of generated QR code file paths
        """
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Prepare memory data
        memory_data = {
            'execution_history': self.execution_history,
            'phi_states': self.phi_states,
            'resonance_patterns': self.resonance_patterns,
            'mutation_history': self.mutation_history,
            'codon_effectiveness': self.codon_effectiveness,
            'generation_markers': self.generation_markers
        }
        
        # Convert to JSON and compress with higher compression level
        json_data = json.dumps(memory_data)
        compressed_data = zlib.compress(json_data.encode('utf-8'), level=9)
        encoded_data = base64.b64encode(compressed_data).decode('utf-8')
        
        # Calculate phi-harmonic chunk sizes based on golden ratio
        total_length = len(encoded_data)
        
        # Use smaller chunk size to ensure QR code version compatibility
        # Start with a conservative chunk size and adjust if needed
        adaptive_chunk_size = min(chunk_size, 384)  # Start with smaller chunks
        num_chunks = math.ceil(total_length / adaptive_chunk_size)
        
        # Use phi-harmonic chunking for more resonant data distribution
        chunk_sizes = []
        remaining = total_length
        for i in range(num_chunks - 1):
            # Use phi to determine variable chunk sizes for optimal resonance
            # But ensure they stay within QR code version limits
            size = min(adaptive_chunk_size, math.ceil(remaining / (PHI * (num_chunks - i))))
            chunk_sizes.append(size)
            remaining -= size
        chunk_sizes.append(remaining)  # Last chunk gets remainder
        
        # Generate QR codes
        qr_files = []
        position = 0
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        gen = self.generation_markers["current_generation"]
        
        for i, size in enumerate(chunk_sizes):
            # Create chunk data
            chunk = encoded_data[position:position+size]
            position += size
            
            # Create QR payload with metadata
            qr_payload = {
                'session_id': f"memory_{timestamp}",
                'frame_number': i + 1,
                'total_frames': num_chunks,
                'generation': gen,
                'task_type': 'memory_restore',
                'content': chunk,
                'valid_until': (datetime.now().timestamp() + 365 * 24 * 60 * 60)  # Valid for 1 year
            }
            
            # Try to generate QR code with adaptive sizing
            success = False
            current_size = size
            
            while not success and current_size > 10:  # Minimum chunk size threshold
                try:
                    # Generate QR code with explicit version limit
                    qr = qrcode.QRCode(
                        version=None,  # Auto-select version
                        error_correction=qrcode.constants.ERROR_CORRECT_M,  # Reduced error correction for more data capacity
                        box_size=10,
                        border=4,
                    )
                    
                    # Create payload with current chunk size
                    current_chunk = encoded_data[position-current_size:position]
                    current_payload = {
                        'session_id': f"memory_{timestamp}",
                        'frame_number': i + 1,
                        'total_frames': num_chunks,
                        'generation': gen,
                        'task_type': 'memory_restore',
                        'content': current_chunk,
                        'valid_until': (datetime.now().timestamp() + 365 * 24 * 60 * 60)
                    }
                    
                    qr.add_data(json.dumps(current_payload))
                    qr.make(fit=True)
                    
                    # If we get here, QR code generation was successful
                    success = True
                    
                    # Create image
                    img = qr.make_image(fill_color="black", back_color="white")
                    
                    # Save image
                    filename = f"qr_memory_{gen}_{i+1}of{num_chunks}.png"
                    filepath = os.path.join(output_dir, filename)
                    img.save(filepath)
                    qr_files.append(filepath)
                    
                    print(f"Generated QR memory chunk {i+1}/{num_chunks} - {filepath}")
                    
                except ValueError as e:
                    # If error is about QR version, reduce chunk size and try again
                    if "Invalid version" in str(e):
                        current_size = int(current_size * 0.75)  # Reduce by 25%
                        position = position - size + current_size  # Adjust position
                        # Update adaptive chunk size for future chunks
                        adaptive_chunk_size = min(adaptive_chunk_size, current_size)
                    else:
                        # For other errors, re-raise
                        raise
        
        # Generate index QR with metadata
        index_payload = {
            'session_id': f"memory_{timestamp}",
            'frame_number': 0,
            'total_frames': num_chunks,
            'generation': gen,
            'task_type': 'memory_index',
            'content': json.dumps({
                'timestamp': timestamp,
                'generation': gen,
                'total_chunks': num_chunks,
                'total_executions': len(self.execution_history),
                'optimal_phi_state': self.get_optimal_phi_state()
            }),
            'valid_until': (datetime.now().timestamp() + 365 * 24 * 60 * 60)  # Valid for 1 year
        }
        
        # Generate index QR code with retry logic
        success = False
        index_content = index_payload['content']
        
        while not success:
            try:
                # Generate QR code
                qr = qrcode.QRCode(
                    version=None,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4,
                )
                qr.add_data(json.dumps(index_payload))
                qr.make(fit=True)
                
                # If we get here, QR code generation was successful
                success = True
                
                # Create image
                img = qr.make_image(fill_color="black", back_color="white")
                
                # Save image
                index_filename = f"qr_memory_{gen}_index.png"
                index_filepath = os.path.join(output_dir, index_filename)
                img.save(index_filepath)
                qr_files.insert(0, index_filepath)
                
                print(f"Generated QR memory index - {index_filepath}")
                
            except ValueError as e:
                # If error is about QR version, simplify the index content
                if "Invalid version" in str(e):
                    # Simplify the index content by removing some details
                    simplified_content = {
                        'timestamp': timestamp,
                        'generation': gen,
                        'total_chunks': num_chunks
                    }
                    index_payload['content'] = json.dumps(simplified_content)
                else:
                    # For other errors, re-raise
                    raise
        
        return qr_files

    def fix_base64_padding(self, data):
        """
        Fix base64 padding issues by ensuring the string length is a multiple of 4.
        
        Args:
            data: Base64 encoded string that might have padding issues
            
        Returns:
            Properly padded base64 string
        """
        # Add padding if needed
        padding_needed = len(data) % 4
        if padding_needed:
            data += '=' * (4 - padding_needed)
        return data
        
    def restore_from_qr_codes(self, qr_directory):
        """
        Restore memory state from QR codes with enhanced error handling.
        
        Args:
            qr_directory: Directory containing memory QR codes
            
        Returns:
            True if restoration was successful, False otherwise
        """
        try:
            # Check if directory exists
            if not os.path.exists(qr_directory):
                print(f"Directory {qr_directory} does not exist")
                return False
            
            # Get QR code files
            qr_files = [f for f in os.listdir(qr_directory) if f.endswith('.png')]
            if not qr_files:
                print(f"No memory QR codes found in {qr_directory}")
                return False
            
            # Find index file
            index_file = next((f for f in qr_files if "_index.png" in f), None)
            if not index_file:
                print("No index QR code found")
                return False
            
            # Read index QR
            index_path = os.path.join(qr_directory, index_file)
            index_img = Image.open(index_path)
            index_decoded = decode(index_img)
            
            if not index_decoded:
                print("Could not decode index QR code")
                return False
            
            # Parse index data
            index_data = json.loads(index_decoded[0].data.decode('utf-8'))
            index_payload = json.loads(index_data.get('content', '{}'))
            
            total_chunks = index_payload.get('total_chunks', 0)
            generation = index_payload.get('generation', 0)
            timestamp = index_payload.get('timestamp', '')
            
            print(f"Found memory QR index: Generation {generation}, {total_chunks} chunks")
            
            # Find and sort chunk files
            chunk_files = [f for f in qr_files if "_index.png" not in f]
            chunk_files.sort(key=lambda f: int(f.split('_')[-1].split('of')[0]))
            
            if len(chunk_files) != total_chunks:
                print(f"Warning: Expected {total_chunks} chunks but found {len(chunk_files)}")
            
            # Read and combine chunks
            combined_data = ""
            for i, chunk_file in enumerate(chunk_files):
                chunk_path = os.path.join(qr_directory, chunk_file)
                try:
                    chunk_img = Image.open(chunk_path)
                    chunk_decoded = decode(chunk_img)
                    
                    if not chunk_decoded:
                        print(f"Could not decode chunk {i+1}")
                        continue
                    
                    chunk_data = json.loads(chunk_decoded[0].data.decode('utf-8'))
                    combined_data += chunk_data.get('content', '')
                    print(f"Processed chunk {i+1}/{len(chunk_files)}")
                except Exception as e:
                    print(f"Error processing chunk {i+1}: {e}")
                    continue
            
            # Decompress and parse data
            try:
                # Fix base64 padding if needed
                padded_data = self.fix_base64_padding(combined_data)
                
                # Try decoding with error handling
                try:
                    decoded_data = base64.b64decode(padded_data)
                except Exception as e:
                    print(f"Base64 decoding error: {e}")
                    print(f"Attempting alternative decoding approach...")
                    
                    # Try decoding in chunks to isolate the problem
                    chunk_size = 1000
                    decoded_chunks = []
                    for i in range(0, len(padded_data), chunk_size):
                        chunk = padded_data[i:i+chunk_size]
                        try:
                            # Ensure each chunk is properly padded
                            padded_chunk = self.fix_base64_padding(chunk)
                            # If this is not the last chunk, make sure it's a multiple of 4
                            if i + chunk_size < len(padded_data):
                                # Find the last complete 4-byte group
                                adjusted_size = (len(padded_chunk) // 4) * 4
                                padded_chunk = padded_chunk[:adjusted_size]
                            
                            decoded_chunk = base64.b64decode(padded_chunk)
                            decoded_chunks.append(decoded_chunk)
                        except Exception as chunk_error:
                            print(f"Error in chunk starting at position {i}: {chunk_error}")
                    
                    if not decoded_chunks:
                        raise ValueError("Could not decode any data chunks")
                    
                    decoded_data = b''.join(decoded_chunks)
                
                # Try decompression with error handling
                try:
                    decompressed_data = zlib.decompress(decoded_data)
                except zlib.error as e:
                    print(f"Decompression error: {e}")
                    print("Attempting to recover partial data...")
                    # Try to decompress with sliding window
                    for i in range(0, len(decoded_data), 1024):
                        try:
                            decompressed_data = zlib.decompress(decoded_data[i:])
                            print(f"Successfully recovered data starting at offset {i}")
                            break
                        except zlib.error:
                            continue
                    else:
                        raise ValueError("Could not decompress data")
                
                # Parse the JSON data
                memory_data = json.loads(decompressed_data.decode('utf-8'))
                
                # Update memory state
                self.phi_states = memory_data.get('phi_states', {})
                self.execution_history = memory_data.get('execution_history', [])
                self.resonance_patterns = memory_data.get('resonance_patterns', [])
                self.mutation_history = memory_data.get('mutation_history', [])
                self.codon_effectiveness = memory_data.get('codon_effectiveness', {})
                self.generation_markers = memory_data.get('generation_markers', {})
                
                print(f"Successfully restored memory state from QR codes")
                print(f"Restored {len(self.execution_history)} execution records")
                
                # Save to file as well
                self.save_memory()
                return True
                
            except Exception as e:
                print(f"Error decompressing or parsing memory data: {e}")
                return False
                
        except Exception as e:
            print(f"Error restoring from QR codes: {e}")
            return False

def main():
    """Main function to run QR Epigenetic Memory Enhanced."""
    parser = argparse.ArgumentParser(description="QR Epigenetic Memory Enhanced")
    parser.add_argument("--generate-qr", action="store_true", help="Generate QR codes from memory")
    parser.add_argument("--restore-from-qr", action="store_true", help="Restore memory from QR codes")
    parser.add_argument("--qr-dir", default="qr_memory_enhanced", help="Directory for QR code storage")
    parser.add_argument("--chunk-size", type=int, default=384, help="Maximum chunk size for QR encoding")
    parser.add_argument("--memory-file", default="qr_epigenetic_memory.json", help="Memory file path")
    
    args = parser.parse_args()
    
    # Create memory instance
    memory = QREpigeneticMemoryEnhanced(args.memory_file)
    
    if args.generate_qr:
        memory.generate_memory_qr_codes(args.qr_dir, args.chunk_size)
    elif args.restore_from_qr:
        success = memory.restore_from_qr_codes(args.qr_dir)
        if success:
            memory.print_memory_summary()
        else:
            print("Failed to restore memory from QR codes")
    else:
        memory.print_memory_summary()

if __name__ == "__main__":
    print("QR Epigenetic Memory Enhanced - By Vaughn Scott (Enhanced by Cascade)")
    main()
