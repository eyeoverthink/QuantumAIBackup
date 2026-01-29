#!/usr/bin/env python3
"""
QR Phi-Memory Compact - Part of Quantum Phi-Harmonic System
By Vaughn Scott (Enhanced by Cascade)

This specialized tool creates highly compact and reliable QR codes for epigenetic memory storage
using phi-harmonic principles, advanced compression, and quantum-inspired error correction.
"""

import os
import sys
import json
import base64
import zlib
import math
import argparse
import binascii
from PIL import Image
from pyzbar.pyzbar import decode
from datetime import datetime
import qrcode
from qrcode.constants import ERROR_CORRECT_M, ERROR_CORRECT_Q

# Import constants from original system
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from qr_epigenetic_memory import PHI
except ImportError:
    PHI = (1 + 5**0.5) / 2  # Golden ratio fallback

class QRPhiMemoryCompact:
    """
    Specialized class for creating and restoring compact QR-encoded epigenetic memory
    with quantum phi-harmonic principles for optimal data density and reliability.
    """
    
    def __init__(self, memory_file="qr_epigenetic_memory.json"):
        """Initialize the QR Phi-Memory Compact system."""
        self.memory_path = memory_file
        self.phi_states = {}
        self.execution_history = []
        self.resonance_patterns = []
        self.mutation_history = []
        self.codon_effectiveness = {}
        self.generation_markers = {}
        
        # Load memory if file exists
        if os.path.exists(memory_file):
            self.load_memory()
            print(f"Loaded epigenetic memory from {memory_file}")
            print(f"Memory contains {len(self.execution_history)} execution records")
    
    def load_memory(self):
        """Load memory state from file."""
        try:
            with open(self.memory_path, 'r') as f:
                memory_data = json.load(f)
                
            self.phi_states = memory_data.get('phi_states', {})
            self.execution_history = memory_data.get('execution_history', [])
            self.resonance_patterns = memory_data.get('resonance_patterns', [])
            self.mutation_history = memory_data.get('mutation_history', [])
            self.codon_effectiveness = memory_data.get('codon_effectiveness', {})
            self.generation_markers = memory_data.get('generation_markers', {})
            
            return True
        except Exception as e:
            print(f"Error loading memory: {e}")
            return False
    
    def save_memory(self, output_file=None):
        """Save memory state to file."""
        if output_file is None:
            output_file = self.memory_path
            
        try:
            memory_data = {
                'phi_states': self.phi_states,
                'execution_history': self.execution_history,
                'resonance_patterns': self.resonance_patterns,
                'mutation_history': self.mutation_history,
                'codon_effectiveness': self.codon_effectiveness,
                'generation_markers': self.generation_markers
            }
            
            with open(output_file, 'w') as f:
                json.dump(memory_data, f)
                
            return True
        except Exception as e:
            print(f"Error saving memory: {e}")
            return False
    
    def phi_resonance(self, value):
        """Calculate phi-harmonic resonance of a value."""
        return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))
    
    def compress_data(self, data, level=9):
        """
        Compress data with maximum compression level.
        
        Args:
            data: Data to compress
            level: Compression level (1-9, 9 being highest)
            
        Returns:
            Compressed data
        """
        return zlib.compress(data.encode('utf-8'), level)
    
    def fix_base64_padding(self, data):
        """
        Fix base64 padding issues by ensuring the string length is a multiple of 4.
        
        Args:
            data: Base64 encoded string that might have padding issues
            
        Returns:
            Properly padded base64 string
        """
        padding_needed = len(data) % 4
        if padding_needed:
            data += '=' * (4 - padding_needed)
        return data
    
    def generate_memory_qr_codes(self, output_dir="qr_phi_memory", max_chunk_size=256, version_limit=25):
        """
        Generate compact QR codes from memory state with phi-harmonic chunking.
        
        Args:
            output_dir: Directory to save QR code images
            max_chunk_size: Maximum chunk size in bytes (will be adjusted if needed)
            version_limit: Maximum QR code version to use (1-40)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Prepare memory data
            memory_data = {
                'phi_states': self.phi_states,
                'execution_history': self.execution_history,
                'resonance_patterns': self.resonance_patterns,
                'mutation_history': self.mutation_history,
                'codon_effectiveness': self.codon_effectiveness,
                'generation_markers': self.generation_markers
            }
            
            # Compress memory data with maximum compression
            json_data = json.dumps(memory_data)
            compressed_data = self.compress_data(json_data, level=9)
            
            # Encode as base64
            base64_data = base64.b64encode(compressed_data).decode('utf-8')
            
            # Calculate optimal chunk size based on phi-harmonic principles
            # Start with a conservative size that works well with QR codes
            chunk_size = min(max_chunk_size, 256)
            
            # Adjust chunk size to be phi-harmonic
            phi_chunk_size = int(chunk_size / PHI) * PHI
            chunk_size = max(int(phi_chunk_size), 128)
            
            # Split data into chunks
            data_length = len(base64_data)
            chunks = []
            
            # Use phi-harmonic chunking
            position = 0
            chunk_number = 1
            
            while position < data_length:
                # Calculate dynamic chunk size using phi-harmonic distribution
                # This creates a natural variation in chunk sizes that follows golden ratio patterns
                dynamic_size = int(chunk_size * (1 + 0.1 * math.sin(chunk_number * PHI)))
                
                # Ensure chunk size is a multiple of 4 for clean base64 boundaries
                dynamic_size = (dynamic_size // 4) * 4
                
                # Get chunk
                end_pos = min(position + dynamic_size, data_length)
                chunk = base64_data[position:end_pos]
                chunks.append(chunk)
                
                position = end_pos
                chunk_number += 1
            
            total_chunks = len(chunks)
            print(f"Split memory data into {total_chunks} chunks")
            
            # Generate QR codes for each chunk with adaptive sizing
            generation = self.generation_markers.get('current_generation', 1)
            timestamp = datetime.now().isoformat()
            
            for i, chunk in enumerate(chunks):
                # Create QR code payload
                qr_payload = {
                    'type': 'memory_chunk',
                    'chunk_number': i + 1,
                    'total_chunks': total_chunks,
                    'generation': generation,
                    'timestamp': timestamp,
                    'content': chunk
                }
                
                # Convert to JSON
                qr_json = json.dumps(qr_payload)
                
                # Create QR code with error correction
                success = False
                current_version = version_limit
                
                while not success and current_version >= 1:
                    try:
                        qr = qrcode.QRCode(
                            version=current_version,
                            error_correction=ERROR_CORRECT_Q,  # Higher error correction
                            box_size=10,
                            border=4,
                        )
                        
                        qr.add_data(qr_json)
                        qr.make(fit=True)
                        
                        # Generate QR code image
                        img = qr.make_image(fill_color="black", back_color="white")
                        
                        # Save image
                        filename = f"qr_memory_{generation}_{i+1}of{total_chunks}.png"
                        filepath = os.path.join(output_dir, filename)
                        img.save(filepath)
                        
                        print(f"Generated QR memory chunk {i+1}/{total_chunks} - {filepath}")
                        success = True
                        
                    except Exception as e:
                        # If error occurs, reduce version and try again
                        current_version -= 5
                        print(f"Reducing QR version to {current_version} for chunk {i+1}")
                        
                        if current_version < 1:
                            # If we've tried all versions, reduce chunk size and try again
                            if len(chunk) > 100:
                                # Split this chunk in half and insert the second half as a new chunk
                                half_point = len(chunk) // 2
                                first_half = chunk[:half_point]
                                second_half = chunk[half_point:]
                                
                                # Replace current chunk with first half
                                chunks[i] = first_half
                                
                                # Insert second half as a new chunk
                                chunks.insert(i + 1, second_half)
                                
                                # Update total chunks
                                total_chunks = len(chunks)
                                print(f"Split chunk {i+1} into two chunks, new total: {total_chunks}")
                                
                                # Reset version and try again
                                current_version = version_limit
                            else:
                                print(f"Error generating QR code for chunk {i+1}: {e}")
                                return False
            
            # Generate index QR code
            index_payload = {
                'type': 'memory_index',
                'total_chunks': total_chunks,
                'generation': generation,
                'timestamp': timestamp,
                'content': json.dumps({
                    'total_chunks': total_chunks,
                    'generation': generation,
                    'timestamp': timestamp,
                    'phi_resonance': self.phi_resonance(total_chunks)
                })
            }
            
            # Convert to JSON
            index_json = json.dumps(index_payload)
            
            # Create QR code with error correction
            success = False
            current_version = version_limit
            
            while not success and current_version >= 1:
                try:
                    qr = qrcode.QRCode(
                        version=current_version,
                        error_correction=ERROR_CORRECT_Q,  # Higher error correction
                        box_size=10,
                        border=4,
                    )
                    
                    qr.add_data(index_json)
                    qr.make(fit=True)
                    
                    # Generate QR code image
                    img = qr.make_image(fill_color="black", back_color="white")
                    
                    # Save image
                    filename = f"qr_memory_{generation}_index.png"
                    filepath = os.path.join(output_dir, filename)
                    img.save(filepath)
                    
                    print(f"Generated QR memory index - {filepath}")
                    success = True
                    
                except Exception as e:
                    # If error occurs, reduce version and try again
                    current_version -= 5
                    print(f"Reducing QR version to {current_version} for index")
                    
                    if current_version < 1:
                        # If we've tried all versions, simplify the index content
                        index_payload = {
                            'type': 'memory_index',
                            'total_chunks': total_chunks,
                            'generation': generation,
                            'content': json.dumps({
                                'total_chunks': total_chunks,
                                'generation': generation
                            })
                        }
                        
                        index_json = json.dumps(index_payload)
                        current_version = version_limit
            
            return True
            
        except Exception as e:
            print(f"Error generating QR codes: {e}")
            return False
    
    def restore_from_qr_codes(self, qr_directory):
        """
        Restore memory state from QR codes with robust error handling.
        
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
            
            # Fix base64 padding if needed
            padded_data = self.fix_base64_padding(combined_data)
            
            try:
                # Decode base64
                decoded_data = base64.b64decode(padded_data)
                
                # Decompress
                decompressed_data = zlib.decompress(decoded_data)
                
                # Parse JSON
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
                print(f"Error decoding or parsing memory data: {e}")
                return False
                
        except Exception as e:
            print(f"Error restoring from QR codes: {e}")
            return False

def main():
    """Main function to run QR Phi-Memory Compact."""
    parser = argparse.ArgumentParser(description="QR Phi-Memory Compact")
    parser.add_argument("--memory-file", default="qr_epigenetic_memory.json", help="Memory file to use")
    parser.add_argument("--generate-qr", action="store_true", help="Generate QR codes from memory")
    parser.add_argument("--restore-from-qr", action="store_true", help="Restore memory from QR codes")
    parser.add_argument("--qr-dir", default="qr_phi_memory", help="Directory for QR codes")
    parser.add_argument("--max-chunk-size", type=int, default=256, help="Maximum chunk size in bytes")
    parser.add_argument("--version-limit", type=int, default=25, help="Maximum QR code version (1-40)")
    
    args = parser.parse_args()
    
    # Create memory instance
    memory = QRPhiMemoryCompact(args.memory_file)
    
    if args.generate_qr:
        print(f"Generating QR codes from memory...")
        memory.generate_memory_qr_codes(args.qr_dir, args.max_chunk_size, args.version_limit)
    
    if args.restore_from_qr:
        print(f"Restoring memory from QR codes...")
        memory.restore_from_qr_codes(args.qr_dir)

if __name__ == "__main__":
    print("QR Phi-Memory Compact - Quantum Phi-Harmonic System")
    print("By Vaughn Scott (Enhanced by Cascade)")
    main()
