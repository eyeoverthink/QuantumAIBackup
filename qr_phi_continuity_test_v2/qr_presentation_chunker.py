#!/usr/bin/env python3
"""
QR Presentation Chunker - Create QR codes with chunking for large files
By Vaughn Scott

This script allows you to:
1. Create QR codes from Python files with automatic chunking for large files
2. Organize them into a presentation sequence
3. Save QR codes for later scanning and execution

Uses phi-harmonic principles and existing QR task worker.
"""

import os
import sys
import json
import time
import uuid
import qrcode
import numpy as np
import argparse
import zlib
import base64
import math
from PIL import Image, ImageDraw, ImageFont

# Phi (Golden Ratio) constant for phi-harmonic timing
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QRChunker:
    """Create QR codes with automatic chunking for large files."""
    
    def __init__(self):
        """Initialize the QR chunker."""
        self.output_dir = "qr_presentation_slides"
        self.max_qr_data_size = 1800  # Conservative max bytes per QR code
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def compress_payload(self, payload):
        """Compress the payload using zlib and base64 encode it."""
        compressed = zlib.compress(payload.encode('utf-8'), 9)  # Max compression
        encoded = base64.b64encode(compressed).decode('utf-8')
        return f"COMPRESSED:{encoded}"
    
    def chunk_content(self, content, max_size):
        """Split content into chunks of max_size."""
        # Estimate compressed size (compression ratio varies, so this is approximate)
        test_compression = len(self.compress_payload(content[:1000])) / 1000
        estimated_max_content = int(max_size / test_compression)
        
        # Calculate number of chunks needed
        content_length = len(content)
        num_chunks = math.ceil(content_length / estimated_max_content)
        
        # Adjust chunk size to ensure even distribution
        chunk_size = math.ceil(content_length / num_chunks)
        
        # Split content into chunks
        chunks = []
        for i in range(0, content_length, chunk_size):
            chunks.append(content[i:i+chunk_size])
        
        print(f"Split content into {len(chunks)} chunks (original size: {content_length} bytes)")
        return chunks
    
    def create_qr_for_chunk(self, chunk, filename, title, chunk_index, total_chunks, task_id):
        """Create a QR code for a single chunk."""
        # Calculate phi-harmonic timing
        phi_time = (time.time() * PHI) % 1.0
        
        # Create task payload
        task_payload = {
            "task_id": task_id,
            "chunk_index": chunk_index,
            "total_chunks": total_chunks,
            "timestamp": time.time(),
            "script_chunk": chunk,
            "input_data": {
                "filename": filename,
                "phi_time": phi_time
            },
            "task_meta": {
                "type": "QR Presentation Chunk",
                "title": title,
                "phi_harmonic": phi_time,
                "visual_inversion": False,
                "intensity_profile": {
                    "resonance": 1.0 / (1.0 + abs(phi_time - 0.5)),
                    "complexity": 0.5 + 0.5 * phi_time
                }
            }
        }
        
        # Convert to JSON
        json_payload = json.dumps(task_payload)
        
        # Compress the payload
        compressed_payload = self.compress_payload(json_payload)
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=None,  # Auto-determine version
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(compressed_payload)
        qr.make(fit=True)
        
        # Create QR image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Add chunk information to the image
        img_with_info = self.add_chunk_info_to_image(img, chunk_index, total_chunks, title)
        
        return img_with_info
    
    def add_chunk_info_to_image(self, img, chunk_index, total_chunks, title):
        """Add chunk information to the QR code image."""
        # Create a new image with extra space at the bottom for text
        width, height = img.size
        new_img = Image.new('RGB', (width, height + 40), color='white')
        new_img.paste(img, (0, 0))
        
        # Add text with chunk information
        draw = ImageDraw.Draw(new_img)
        text = f"Chunk {chunk_index+1}/{total_chunks} - {title}"
        
        # Position text at the bottom center
        text_width = len(text) * 7  # Approximate width
        text_x = (width - text_width) // 2
        text_y = height + 10
        
        draw.text((text_x, text_y), text, fill='black')
        
        return new_img
    
    def create_qr_from_file(self, file_path, slide_title=None):
        """Create QR code(s) from a Python file with automatic chunking."""
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} not found.")
            return None
        
        # Read the file
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Create a unique task ID (shared across chunks)
        task_id = str(uuid.uuid4())
        
        # Get the filename without path
        filename = os.path.basename(file_path)
        
        # Use the filename as slide title if none provided
        if not slide_title:
            slide_title = os.path.splitext(filename)[0]
        
        # Split content into chunks if needed
        chunks = self.chunk_content(content, self.max_qr_data_size)
        total_chunks = len(chunks)
        
        # Create QR code for each chunk
        qr_images = []
        for i, chunk in enumerate(chunks):
            qr_img = self.create_qr_for_chunk(
                chunk, filename, slide_title, i, total_chunks, task_id
            )
            qr_images.append(qr_img)
        
        # Create slide data
        slide_data = {
            "task_id": task_id,
            "title": slide_title,
            "filename": filename,
            "content": content,
            "phi_time": (time.time() * PHI) % 1.0,
            "qr_images": qr_images,
            "total_chunks": total_chunks
        }
        
        return slide_data
    
    def save_qr_images(self, slide_data):
        """Save QR code images for a slide."""
        if not slide_data:
            return []
        
        saved_paths = []
        title = slide_data["title"]
        total_chunks = slide_data["total_chunks"]
        
        for i, qr_img in enumerate(slide_data["qr_images"]):
            # Create filename with chunk information
            if total_chunks > 1:
                output_path = os.path.join(
                    self.output_dir, 
                    f"{title}_chunk_{i+1}_of_{total_chunks}.png"
                )
            else:
                output_path = os.path.join(self.output_dir, f"{title}.png")
            
            qr_img.save(output_path)
            saved_paths.append(output_path)
            print(f"Saved QR code to {output_path}")
        
        return saved_paths

def main():
    """Main function to run the QR chunker."""
    parser = argparse.ArgumentParser(description="Create QR codes from Python files with automatic chunking.")
    parser.add_argument("--file", required=True, help="Python file to encode as QR code(s)")
    parser.add_argument("--title", help="Title for the slide")
    args = parser.parse_args()
    
    chunker = QRChunker()
    slide_data = chunker.create_qr_from_file(args.file, args.title)
    
    if slide_data:
        saved_paths = chunker.save_qr_images(slide_data)
        print(f"Created {len(saved_paths)} QR code(s) for {args.file}")
        print("Use the qr_task_worker_from_file.py script to scan and execute these QR codes")

if __name__ == "__main__":
    main()
