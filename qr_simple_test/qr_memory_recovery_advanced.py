#!/usr/bin/env python3
"""
Advanced QR Memory Recovery Tool - Part of Quantum Phi-Harmonic System
By Vaughn Scott (Enhanced by Cascade)

This specialized tool focuses on robust QR code memory recovery with:
1. Advanced base64 padding correction
2. Phi-harmonic chunk alignment
3. Progressive error recovery with multiple decompression strategies
4. Quantum-inspired data reconstruction
5. Partial memory recovery capabilities
"""

import os
import sys
import json
import base64
import zlib
import math
import argparse
import binascii
import struct
from PIL import Image
from pyzbar.pyzbar import decode
from datetime import datetime
import io
import re

# Import constants from original system
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from qr_epigenetic_memory import PHI
except ImportError:
    PHI = (1 + 5**0.5) / 2  # Golden ratio fallback

class AdvancedQRMemoryRecovery:
    """
    Advanced class for recovering QR-encoded epigenetic memory with 
    quantum phi-harmonic error correction techniques and specialized
    decompression strategies.
    """
    
    def __init__(self, memory_file="qr_epigenetic_memory.json"):
        """Initialize the Advanced QR Memory Recovery system."""
        self.memory_path = memory_file
        self.recovered_data = None
        self.recovery_stats = {
            "total_chunks": 0,
            "processed_chunks": 0,
            "successful_chunks": 0,
            "phi_resonance": 0.0,
            "recovery_quality": 0.0
        }
        self.debug_mode = False
    
    def fix_base64_padding(self, data):
        """
        Fix base64 padding issues by ensuring the string length is a multiple of 4.
        
        Args:
            data: Base64 encoded string that might have padding issues
            
        Returns:
            Properly padded base64 string
        """
        # Remove any invalid characters that might have been introduced
        data = ''.join(c for c in data if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
        
        # Add padding if needed
        padding_needed = len(data) % 4
        if padding_needed:
            data += '=' * (4 - padding_needed)
        return data
    
    def phi_resonance(self, value):
        """Calculate phi-harmonic resonance of a value."""
        return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))
    
    def advanced_decompress(self, data, verbose=True):
        """
        Advanced decompression with multiple strategies for handling corrupted zlib data.
        
        Args:
            data: Compressed data to decompress
            verbose: Whether to print detailed progress information
            
        Returns:
            Decompressed data if successful, None otherwise
        """
        # Strategy 1: Standard decompression
        try:
            if verbose:
                print("Trying standard decompression...")
            return zlib.decompress(data)
        except zlib.error as e:
            if verbose:
                print(f"Standard decompression failed: {e}")
        
        # Strategy 2: Sliding window decompression
        try:
            if verbose:
                print("Trying sliding window decompression...")
            
            for i in range(0, min(len(data), 10000), 1):
                try:
                    if i % 1000 == 0 and verbose:
                        print(f"Trying offset {i}...")
                    result = zlib.decompress(data[i:])
                    if verbose:
                        print(f"Successfully decompressed from offset {i}")
                    return result
                except zlib.error:
                    continue
        except Exception as e:
            if verbose:
                print(f"Sliding window decompression failed: {e}")
        
        # Strategy 3: Phi-harmonic window decompression
        try:
            if verbose:
                print("Trying phi-harmonic window decompression...")
            
            # Generate phi-harmonic offsets
            phi_offsets = []
            for i in range(20):
                offset = int(i * PHI) % min(1000, len(data)//10)
                phi_offsets.append(offset)
            
            for i in phi_offsets:
                try:
                    if verbose:
                        print(f"Trying phi-offset {i}...")
                    result = zlib.decompress(data[i:])
                    if verbose:
                        print(f"Successfully decompressed from phi-offset {i}")
                    return result
                except zlib.error:
                    continue
        except Exception as e:
            if verbose:
                print(f"Phi-harmonic decompression failed: {e}")
        
        # Strategy 4: Repair zlib header and try again
        try:
            if verbose:
                print("Trying zlib header repair...")
            
            # Standard zlib header
            zlib_header = b'\x78\x9c'  # Most common zlib header
            
            # Try with different compression levels
            for header in [b'\x78\x01', b'\x78\x5e', b'\x78\x9c', b'\x78\xda']:
                try:
                    repaired_data = header + data[2:]
                    result = zlib.decompress(repaired_data)
                    if verbose:
                        print(f"Successfully decompressed with repaired header {header.hex()}")
                    return result
                except zlib.error:
                    continue
        except Exception as e:
            if verbose:
                print(f"Zlib header repair failed: {e}")
        
        # Strategy 5: Try to find valid zlib streams within the data
        try:
            if verbose:
                print("Searching for valid zlib streams in data...")
            
            # Common zlib headers
            headers = [b'\x78\x01', b'\x78\x5e', b'\x78\x9c', b'\x78\xda']
            
            for header in headers:
                # Find all occurrences of this header
                positions = []
                pos = -1
                while True:
                    pos = data.find(header, pos + 1)
                    if pos == -1:
                        break
                    positions.append(pos)
                
                if verbose:
                    print(f"Found {len(positions)} potential zlib streams with header {header.hex()}")
                
                # Try each position
                for pos in positions:
                    try:
                        result = zlib.decompress(data[pos:])
                        if verbose:
                            print(f"Successfully decompressed stream at position {pos}")
                        return result
                    except zlib.error:
                        continue
        except Exception as e:
            if verbose:
                print(f"Zlib stream search failed: {e}")
        
        # Strategy 6: Try to recover partial JSON data directly from binary
        if verbose:
            print("Attempting direct JSON extraction from binary data...")
        
        try:
            # Look for JSON patterns in the raw binary data
            text_data = data.decode('utf-8', errors='ignore')
            
            # Look for JSON object start/end
            json_matches = re.findall(r'(\{.*\})', text_data)
            if json_matches:
                for match in json_matches:
                    try:
                        if len(match) > 100:  # Only try substantial JSON objects
                            json_data = json.loads(match)
                            if isinstance(json_data, dict) and len(json_data) > 0:
                                if verbose:
                                    print(f"Found valid JSON object with {len(json_data)} keys")
                                return match.encode('utf-8')
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            if verbose:
                print(f"Direct JSON extraction failed: {e}")
        
        return None
    
    def recover_from_qr_codes(self, qr_directory, output_file=None, verbose=True):
        """
        Recover memory state from QR codes with advanced error handling.
        
        Args:
            qr_directory: Directory containing memory QR codes
            output_file: Optional file to save recovered data (if None, uses self.memory_path)
            verbose: Whether to print detailed progress information
            
        Returns:
            True if recovery was successful, False otherwise
        """
        if output_file is None:
            output_file = self.memory_path
            
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
                # Try to infer total chunks from filenames
                chunk_files = [f for f in qr_files if "_index.png" not in f]
                if not chunk_files:
                    return False
                    
                # Extract total chunks from filenames if possible
                try:
                    total_chunks = max([int(f.split('of')[1].split('.')[0]) for f in chunk_files])
                    print(f"Inferred total chunks: {total_chunks}")
                except:
                    print("Could not determine total chunks")
                    return False
            else:
                # Read index QR
                index_path = os.path.join(qr_directory, index_file)
                try:
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
                except Exception as e:
                    print(f"Error processing index: {e}")
                    # Try to infer total chunks from filenames
                    chunk_files = [f for f in qr_files if "_index.png" not in f]
                    try:
                        total_chunks = max([int(f.split('of')[1].split('.')[0]) for f in chunk_files])
                        print(f"Inferred total chunks: {total_chunks}")
                    except:
                        print("Could not determine total chunks")
                        return False
            
            # Find and sort chunk files
            chunk_files = [f for f in qr_files if "_index.png" not in f]
            
            # Sort by chunk number
            try:
                chunk_files.sort(key=lambda f: int(f.split('_')[-1].split('of')[0]))
            except:
                print("Warning: Could not sort chunks by number, using filename order")
            
            self.recovery_stats["total_chunks"] = len(chunk_files)
            
            # Read and combine chunks with phi-harmonic alignment
            combined_data = ""
            successful_chunks = []
            
            for i, chunk_file in enumerate(chunk_files):
                chunk_path = os.path.join(qr_directory, chunk_file)
                try:
                    chunk_img = Image.open(chunk_path)
                    chunk_decoded = decode(chunk_img)
                    
                    if not chunk_decoded:
                        if verbose:
                            print(f"Could not decode chunk {i+1}")
                        continue
                    
                    chunk_data = json.loads(chunk_decoded[0].data.decode('utf-8'))
                    chunk_content = chunk_data.get('content', '')
                    
                    # Validate chunk content is valid base64 before adding
                    try:
                        # Try to decode a small sample to validate
                        test_chunk = self.fix_base64_padding(chunk_content[:20])
                        base64.b64decode(test_chunk)
                        
                        # If we get here, the chunk seems valid
                        combined_data += chunk_content
                        successful_chunks.append(i)
                        self.recovery_stats["successful_chunks"] += 1
                        
                        if verbose:
                            print(f"Processed chunk {i+1}/{len(chunk_files)}")
                    except:
                        if verbose:
                            print(f"Chunk {i+1} contains invalid base64 data, skipping")
                        continue
                        
                except Exception as e:
                    if verbose:
                        print(f"Error processing chunk {i+1}: {e}")
                    continue
            
            self.recovery_stats["processed_chunks"] = len(chunk_files)
            
            # Calculate phi-resonance of successful chunks
            if successful_chunks:
                resonance = self.phi_resonance(len(successful_chunks))
                self.recovery_stats["phi_resonance"] = resonance
                if verbose:
                    print(f"Phi-resonance of recovery: {resonance:.6f}")
            
            # Decompress and parse data with progressive error recovery
            try:
                # Fix base64 padding
                if verbose:
                    print("Applying quantum phi-harmonic base64 correction...")
                
                # First try: standard padding fix
                try:
                    padded_data = self.fix_base64_padding(combined_data)
                    decoded_data = base64.b64decode(padded_data)
                    if verbose:
                        print("Standard base64 decoding successful")
                except Exception as e:
                    if verbose:
                        print(f"Standard base64 decoding failed: {e}")
                        print("Attempting quantum-aligned chunked decoding...")
                    
                    # Second try: Decode in phi-harmonic aligned chunks
                    chunk_size = int(1000 * PHI) # Phi-aligned chunk size
                    decoded_chunks = []
                    
                    for i in range(0, len(combined_data), chunk_size):
                        chunk = combined_data[i:i+chunk_size]
                        try:
                            # Ensure each chunk is properly padded
                            padded_chunk = self.fix_base64_padding(chunk)
                            
                            # If this is not the last chunk, make sure it's a multiple of 4
                            if i + chunk_size < len(combined_data):
                                # Find the last complete 4-byte group
                                adjusted_size = (len(padded_chunk) // 4) * 4
                                padded_chunk = padded_chunk[:adjusted_size]
                            
                            decoded_chunk = base64.b64decode(padded_chunk)
                            decoded_chunks.append(decoded_chunk)
                            
                            if verbose and i % (chunk_size * 10) == 0:
                                print(f"Decoded chunk at position {i}")
                                
                        except Exception as chunk_error:
                            if verbose:
                                print(f"Error in chunk at position {i}: {chunk_error}")
                            continue
                    
                    if not decoded_chunks:
                        raise ValueError("Could not decode any data chunks")
                    
                    decoded_data = b''.join(decoded_chunks)
                    if verbose:
                        print(f"Chunked decoding recovered {len(decoded_data)} bytes")
                
                # Try advanced decompression
                if verbose:
                    print("Attempting advanced data decompression...")
                
                decompressed_data = self.advanced_decompress(decoded_data, verbose)
                
                if decompressed_data is None:
                    raise ValueError("Could not decompress data with any strategy")
                
                # Parse the JSON data
                if verbose:
                    print("Parsing recovered JSON data...")
                
                try:
                    memory_data = json.loads(decompressed_data.decode('utf-8'))
                except json.JSONDecodeError:
                    if verbose:
                        print("JSON parsing failed, attempting partial recovery...")
                    
                    # Try to extract valid JSON objects
                    text_data = decompressed_data.decode('utf-8', errors='ignore')
                    json_pattern = r'\{(?:[^{}]|(?:\{(?:[^{}]|(?:\{[^{}]*\}))*\}))*\}'
                    matches = re.findall(json_pattern, text_data)
                    
                    if matches:
                        largest_match = max(matches, key=len)
                        if len(largest_match) > 100:  # Only consider substantial JSON objects
                            try:
                                memory_data = json.loads(largest_match)
                                if verbose:
                                    print(f"Recovered partial JSON data with {len(largest_match)} characters")
                            except json.JSONDecodeError:
                                raise ValueError("Could not parse recovered JSON data")
                        else:
                            raise ValueError("Recovered JSON fragments too small")
                    else:
                        raise ValueError("No valid JSON objects found in decompressed data")
                
                # Store recovered data
                self.recovered_data = memory_data
                
                # Calculate recovery quality
                recovery_quality = len(successful_chunks) / len(chunk_files)
                self.recovery_stats["recovery_quality"] = recovery_quality
                
                if verbose:
                    print(f"Successfully recovered memory data")
                    print(f"Recovery quality: {recovery_quality:.2%}")
                    
                    # Print summary of recovered data
                    execution_history = memory_data.get('execution_history', [])
                    phi_states = memory_data.get('phi_states', {})
                    generation_markers = memory_data.get('generation_markers', {})
                    
                    print(f"Recovered {len(execution_history)} execution records")
                    if generation_markers:
                        print(f"Generation: {generation_markers.get('current_generation', 0)}")
                
                # Save recovered data if requested
                if output_file:
                    with open(output_file, 'w') as f:
                        json.dump(memory_data, f)
                    if verbose:
                        print(f"Saved recovered data to {output_file}")
                
                return True
                
            except Exception as e:
                print(f"Error recovering memory data: {e}")
                return False
                
        except Exception as e:
            print(f"Error during QR memory recovery: {e}")
            return False
    
    def print_recovery_stats(self):
        """Print statistics about the recovery process."""
        print("\n============================================================")
        print("ADVANCED QR MEMORY RECOVERY STATISTICS")
        print("============================================================")
        print(f"Total chunks processed: {self.recovery_stats['processed_chunks']}")
        print(f"Successfully decoded chunks: {self.recovery_stats['successful_chunks']}")
        print(f"Recovery success rate: {self.recovery_stats['successful_chunks'] / max(1, self.recovery_stats['processed_chunks']):.2%}")
        print(f"Phi-harmonic resonance: {self.recovery_stats['phi_resonance']:.6f}")
        print(f"Overall recovery quality: {self.recovery_stats['recovery_quality']:.2%}")
        print("============================================================\n")

def main():
    """Main function to run Advanced QR Memory Recovery."""
    parser = argparse.ArgumentParser(description="Advanced QR Memory Recovery Tool")
    parser.add_argument("--qr-dir", required=True, help="Directory containing QR code images")
    parser.add_argument("--output", default="recovered_memory.json", help="Output file for recovered memory")
    parser.add_argument("--quiet", action="store_true", help="Suppress detailed progress output")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode with additional diagnostics")
    
    args = parser.parse_args()
    
    # Create recovery instance
    recovery = AdvancedQRMemoryRecovery()
    recovery.debug_mode = args.debug
    
    # Perform recovery
    print(f"Starting advanced QR memory recovery from {args.qr_dir}...")
    success = recovery.recover_from_qr_codes(args.qr_dir, args.output, not args.quiet)
    
    if success:
        recovery.print_recovery_stats()
        print(f"Memory recovery successful! Data saved to {args.output}")
    else:
        print("Memory recovery failed.")

if __name__ == "__main__":
    print("Advanced QR Memory Recovery Tool - Quantum Phi-Harmonic System")
    main()
