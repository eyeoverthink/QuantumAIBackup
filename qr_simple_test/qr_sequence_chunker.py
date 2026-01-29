#!/usr/bin/env python3
"""
QR Sequence Chunker - Part of Animated QR Flipbook DNA System
By Vaughn Scott

Handles chunking of large payloads for QR code generation.
Uses phi-harmonic principles for optimal chunking.
"""

import json
import math
import base64
import zlib

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRSequenceChunker:
    """
    Handles chunking of large payloads for QR codes based on phi-harmonic principles.
    """
    
    def __init__(self, max_chunk_size=1000):
        """
        Initialize the QR Sequence Chunker.
        
        Args:
            max_chunk_size: Maximum size of each chunk in bytes
        """
        self.max_chunk_size = max_chunk_size
    
    def compress_payload(self, payload):
        """
        Compress a payload using zlib compression.
        
        Args:
            payload: String payload to compress
            
        Returns:
            Base64-encoded compressed payload
        """
        # Convert to bytes if string
        if isinstance(payload, str):
            payload_bytes = payload.encode('utf-8')
        else:
            payload_bytes = payload
        
        # For very small payloads, don't compress
        if len(payload_bytes) < 100:
            # Just encode as base64
            encoded = base64.b64encode(payload_bytes).decode('ascii')
            return encoded
            
        try:
            # Compress with zlib
            compressed = zlib.compress(payload_bytes, level=9)
            
            # Encode as base64 for safe transport
            encoded = base64.b64encode(compressed).decode('ascii')
            
            # Add compression marker
            return "COMPRESSED:" + encoded
        except Exception as e:
            # Fallback to simple base64 encoding if compression fails
            print(f"Compression failed: {e}, falling back to base64 encoding")
            encoded = base64.b64encode(payload_bytes).decode('ascii')
            return encoded
    
    def decompress_payload(self, compressed_payload):
        """
        Decompress a payload that was compressed with compress_payload.
        
        Args:
            compressed_payload: Base64-encoded compressed payload
            
        Returns:
            Original payload as string
        """
        # Check if payload has compression marker
        if isinstance(compressed_payload, str) and compressed_payload.startswith("COMPRESSED:"):
            # Remove compression marker
            compressed_payload = compressed_payload[11:]
            
            # Decode base64
            decoded = base64.b64decode(compressed_payload)
            
            # Decompress
            decompressed = zlib.decompress(decoded)
            
            # Convert back to string
            return decompressed.decode('utf-8')
        else:
            # Not compressed, just base64 encoded
            try:
                # Decode base64
                decoded = base64.b64decode(compressed_payload)
                
                # Convert back to string
                return decoded.decode('utf-8')
            except Exception as e:
                # If decoding fails, return as is
                print(f"Decompression failed: {e}, returning payload as is")
                return compressed_payload
    
    def chunk_payload(self, payload):
        """
        Split a payload into chunks using phi-harmonic principles.
        
        Args:
            payload: String payload to chunk
            
        Returns:
            List of chunks, each with metadata
        """
        # Compress the payload first
        compressed = self.compress_payload(payload)
        
        # Calculate optimal chunk size based on phi
        optimal_size = min(
            int(self.max_chunk_size / PHI),  # Phi-optimized size
            len(compressed)                  # Don't exceed payload size
        )
        
        # Ensure minimum chunk size
        chunk_size = max(optimal_size, 100)
        
        # Calculate number of chunks needed
        num_chunks = math.ceil(len(compressed) / chunk_size)
        
        # Create chunks
        chunks = []
        for i in range(num_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, len(compressed))
            
            chunk = {
                "chunk_id": i + 1,
                "total_chunks": num_chunks,
                "data": compressed[start:end],
                "is_compressed": True
            }
            
            chunks.append(chunk)
        
        return chunks
    
    def reassemble_payload(self, chunks):
        """
        Reassemble chunks back into the original payload.
        
        Args:
            chunks: List of chunks from chunk_payload
            
        Returns:
            Original payload as string
        """
        # Sort chunks by chunk_id
        sorted_chunks = sorted(chunks, key=lambda x: x["chunk_id"])
        
        # Concatenate chunk data
        compressed = ""
        for chunk in sorted_chunks:
            compressed += chunk["data"]
        
        # Decompress
        return self.decompress_payload(compressed)
