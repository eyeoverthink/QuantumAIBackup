#!/usr/bin/env python3
"""
QR Robust Generator - Part of Animated QR Flipbook DNA System
By Vaughn Scott

A robust QR code generator that ensures reliable encoding and decoding.
Uses phi-harmonic principles for optimal QR code generation.
"""

import os
import json
import math
import base64
import zlib
import qrcode
import uuid
from PIL import Image, ImageDraw, ImageFont

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRRobustGenerator:
    """
    A robust QR code generator that ensures reliable encoding and decoding.
    """
    
    def __init__(self, output_dir="qr_robust_sequence", max_version=25):
        """
        Initialize the QR Robust Generator.
        
        Args:
            output_dir: Directory to save generated QR code frames
            max_version: Maximum QR code version to use (1-40)
        """
        self.output_dir = output_dir
        self.max_version = min(max_version, 40)  # QR code versions are 1-40
        self.session_id = str(uuid.uuid4())
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def compress_data(self, data):
        """
        Compress data using zlib compression.
        
        Args:
            data: Data to compress (string or bytes)
            
        Returns:
            Base64-encoded compressed data
        """
        # Convert to bytes if string
        if isinstance(data, str):
            data_bytes = data.encode('utf-8')
        else:
            data_bytes = data
        
        # For very small data, don't compress
        if len(data_bytes) < 100:
            # Just encode as base64
            encoded = base64.b64encode(data_bytes).decode('ascii')
            return encoded
        
        # Compress with zlib
        compressed = zlib.compress(data_bytes, level=9)
        
        # Encode as base64 for safe transport
        encoded = base64.b64encode(compressed).decode('ascii')
        
        # Add compression marker
        return "COMPRESSED:" + encoded
    
    def decompress_data(self, compressed_data):
        """
        Decompress data that was compressed with compress_data.
        
        Args:
            compressed_data: Base64-encoded compressed data
            
        Returns:
            Original data as string
        """
        # Check if data has compression marker
        if isinstance(compressed_data, str) and compressed_data.startswith("COMPRESSED:"):
            # Remove compression marker
            compressed_data = compressed_data[11:]
            
            # Decode base64
            decoded = base64.b64decode(compressed_data)
            
            # Decompress
            decompressed = zlib.decompress(decoded)
            
            # Convert back to string
            return decompressed.decode('utf-8')
        else:
            # Not compressed, just base64 encoded
            try:
                # Decode base64
                decoded = base64.b64decode(compressed_data)
                
                # Convert back to string
                return decoded.decode('utf-8')
            except Exception as e:
                # If decoding fails, return as is
                print(f"Decompression failed: {e}, returning data as is")
                return compressed_data
    
    def split_data(self, data, max_size=1000):
        """
        Split data into chunks of maximum size.
        
        Args:
            data: Data to split
            max_size: Maximum chunk size
            
        Returns:
            List of data chunks
        """
        # Calculate optimal chunk size based on phi
        optimal_size = min(
            int(max_size / PHI),  # Phi-optimized size
            len(data)             # Don't exceed data size
        )
        
        # Ensure minimum chunk size
        chunk_size = max(optimal_size, 100)
        
        # Calculate number of chunks needed
        num_chunks = math.ceil(len(data) / chunk_size)
        
        # Create chunks
        chunks = []
        for i in range(num_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, len(data))
            
            chunk = {
                "chunk_id": i + 1,
                "total_chunks": num_chunks,
                "data": data[start:end]
            }
            
            chunks.append(chunk)
        
        return chunks
    
    def generate_qr_code(self, data, version=None):
        """
        Generate a QR code for the given data.
        
        Args:
            data: Data to encode in QR code
            version: QR code version (1-40)
            
        Returns:
            QR code image
        """
        # Try to create QR code with specified version
        try:
            qr = qrcode.QRCode(
                version=version,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            return qr.make_image(fill_color="black", back_color="white")
        except Exception as e:
            print(f"Error generating QR code: {e}")
            return None
    
    def find_optimal_version(self, data):
        """
        Find the optimal QR code version for the given data.
        
        Args:
            data: Data to encode in QR code
            
        Returns:
            Optimal QR code version
        """
        # Try each version starting from the lowest
        for version in range(1, self.max_version + 1):
            try:
                qr = qrcode.QRCode(
                    version=version,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4,
                )
                qr.add_data(data)
                qr.make(fit=True)
                
                # If we get here, this version works
                return version
            except Exception:
                # Try the next version
                continue
        
        # If we get here, no version worked
        return None
    
    def generate_frame(self, data, frame_number, phi_state=None):
        """
        Generate a QR code frame for the given data.
        
        Args:
            data: Data to encode in QR code
            frame_number: Frame number for filename
            phi_state: Optional phi state information
            
        Returns:
            Path to the generated QR image or list of paths for chunked QR codes
        """
        # Compress the data
        compressed = self.compress_data(data)
        
        # Try to find optimal version
        version = self.find_optimal_version(compressed)
        
        if version is not None:
            # Generate QR code
            qr_img = self.generate_qr_code(compressed, version=version)
            
            if qr_img:
                # Add visual indicators
                img = qr_img.convert('RGBA')
                draw = ImageDraw.Draw(img)
                
                # Add frame number
                draw.text((10, 10), f"F{frame_number:03d}", fill=(255, 0, 0, 128))
                
                # Add phi resonance indicator if provided
                if phi_state and "resonance" in phi_state:
                    resonance = phi_state["resonance"]
                    resonance_color = (
                        int(255 * resonance),
                        int(128 * (1 - resonance)),
                        int(255 * 0.5),  # Use complexity = 0.5 as default
                        128
                    )
                    img_width, img_height = img.size
                    corner_size = int(img_width * 0.1)
                    draw.rectangle(
                        [(img_width - corner_size, 0), (img_width, corner_size)],
                        fill=resonance_color
                    )
                
                # Save image
                filename = os.path.join(self.output_dir, f"qr_frame_{frame_number:03d}.png")
                img.save(filename)
                return filename
        
        # If we get here, we need to split the data into chunks
        print(f"Data too large for single QR code, splitting into chunks")
        chunks = self.split_data(data)
        paths = []
        
        # Generate QR code for each chunk
        for i, chunk in enumerate(chunks):
            # Convert chunk to JSON
            chunk_data = json.dumps(chunk)
            
            # Find optimal version for this chunk
            chunk_version = self.find_optimal_version(chunk_data)
            
            if chunk_version is None:
                print(f"Warning: Chunk {i+1}/{len(chunks)} too large for QR code")
                continue
            
            # Generate QR code
            qr_img = self.generate_qr_code(chunk_data, version=chunk_version)
            
            if qr_img:
                # Add visual indicators
                img = qr_img.convert('RGBA')
                draw = ImageDraw.Draw(img)
                
                # Add frame and chunk numbers
                draw.text((10, 10), f"F{frame_number:03d}_{i+1:02d}/{len(chunks):02d}", fill=(255, 0, 0, 128))
                
                # Save image
                filename = os.path.join(self.output_dir, f"qr_frame_{frame_number:03d}_{i+1:02d}.png")
                img.save(filename)
                paths.append(filename)
        
        return paths
    
    def generate_from_genome(self, genome, output_dir=None):
        """
        Generate QR code frames from a genome.
        
        Args:
            genome: Genome object with codons
            output_dir: Optional output directory override
            
        Returns:
            List of paths to generated QR images
        """
        if output_dir:
            self.output_dir = output_dir
            os.makedirs(output_dir, exist_ok=True)
        
        paths = []
        frame_number = 1
        
        # Get all codons from the genome - adapt to actual genome structure
        codons = []
        
        # Check if genome has codons attribute directly
        if hasattr(genome, 'codons'):
            codons = genome.codons
        # Check if genome has codon_groups attribute
        elif hasattr(genome, 'codon_groups'):
            for group in genome.codon_groups.values():
                if hasattr(group, 'codons'):
                    codons.extend(group.codons)
        # If genome has frames attribute (older structure)
        elif hasattr(genome, 'frames'):
            codons = genome.frames
        
        # If no codons found, try to access genome data directly
        if not codons and hasattr(genome, 'data'):
            if isinstance(genome.data, dict) and 'frames' in genome.data:
                codons = genome.data['frames']
        
        # Generate QR code for each codon/frame
        for i, codon in enumerate(codons):
            # Create payload - adapt to actual codon structure
            payload = {}
            
            # Handle different codon structures
            if hasattr(codon, 'frame_data'):
                # New structure with frame_data attribute
                task_data = codon.frame_data.get("task_data", {})
                payload = {
                    "code": task_data.get("code", ""),
                    "task_type": codon.frame_data.get("task_type", "execute_python"),
                    "codon_id": getattr(codon, "codon_id", str(i)),
                    "group_id": getattr(codon, "group_id", "0"),
                    "phi_state": getattr(codon, "phi_state", {})
                }
            elif isinstance(codon, dict):
                # Direct dictionary structure
                task_data = codon.get("task_data", {})
                if isinstance(task_data, dict):
                    code = task_data.get("code", "")
                else:
                    code = str(task_data)
                    
                payload = {
                    "code": code,
                    "task_type": codon.get("task_type", "execute_python"),
                    "frame_id": codon.get("frame_id", str(i)),
                    "phi_state": codon.get("phi_state", {})
                }
            
            # Convert payload to JSON
            json_payload = json.dumps(payload)
            
            # Get phi_state for visual indicators
            phi_state = None
            if hasattr(codon, 'phi_state'):
                phi_state = codon.phi_state
            elif isinstance(codon, dict) and 'phi_state' in codon:
                phi_state = codon['phi_state']
            
            # Generate QR code frame
            path = self.generate_frame(json_payload, frame_number, phi_state=phi_state)
            
            if isinstance(path, list):
                paths.extend(path)
            else:
                paths.append(path)
            
            frame_number += 1
        
        return paths

# Example usage
if __name__ == "__main__":
    generator = QRRobustGenerator()
    
    # Generate a simple QR code
    data = "Hello from QR Robust Generator!"
    path = generator.generate_frame(data, 1)
    print(f"Generated QR code: {path}")
    
    # Generate a larger QR code
    large_data = "A" * 1000
    paths = generator.generate_frame(large_data, 2)
    if isinstance(paths, list):
        print(f"Generated {len(paths)} QR code chunks")
    else:
        print(f"Generated QR code: {paths}")
