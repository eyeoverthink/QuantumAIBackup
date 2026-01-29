#!/usr/bin/env python3
"""
Simple QR Encoder - Create executable QR codes from Python files
By Vaughn Scott

This script creates QR codes that can be scanned by the existing qr_task_worker_from_file.py
to execute Python code. It uses phi-harmonic principles and supports the existing system.
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

# Phi (Golden Ratio) constant for phi-harmonic timing
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class SimpleQREncoder:
    """Create executable QR codes from Python files."""
    
    def __init__(self):
        """Initialize the QR encoder."""
        self.output_dir = "qr_codes"
        self.max_chars = 30000  # Conservative limit for QR code content
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def compress_payload(self, payload):
        """Compress the payload using zlib and base64 encode it."""
        compressed = zlib.compress(payload.encode('utf-8'), 9)  # Max compression
        encoded = base64.b64encode(compressed).decode('utf-8')
        return f"COMPRESSED:{encoded}"
    
    def create_minimal_task(self, code, title):
        """Create a minimal task payload with just the essential code."""
        # Create a unique task ID
        task_id = str(uuid.uuid4())
        
        # Calculate phi-harmonic timing
        phi_time = (time.time() * PHI) % 1.0
        
        # Create a minimal task payload
        task_payload = {
            "task_id": task_id,
            "timestamp": time.time(),
            "task_type": "execute_python",
            "content": code,
            "phi_harmonic": phi_time
        }
        
        return task_payload
    
    def encode_file(self, file_path, title=None):
        """Encode a Python file as a QR code."""
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} not found.")
            return None
        
        # Use filename as title if none provided
        if not title:
            title = os.path.basename(file_path).split('.')[0]
        
        # Read the file
        with open(file_path, 'r') as f:
            code = f.read()
        
        # Check if the code is too large
        if len(code) > self.max_chars:
            print(f"Warning: Code is {len(code)} characters, which exceeds the recommended maximum of {self.max_chars}.")
            print("Creating a simplified version with just the main function...")
            
            # Extract just the main function to reduce size
            lines = code.split('\n')
            simplified_code = []
            in_main = False
            imports = []
            
            # Extract imports
            for line in lines:
                if line.startswith('import ') or line.startswith('from '):
                    imports.append(line)
            
            # Extract main function
            for line in lines:
                if line.startswith('def main():'):
                    in_main = True
                    simplified_code.append(line)
                elif in_main:
                    if line.startswith('def ') or not line.strip():
                        if not line.strip():
                            simplified_code.append(line)
                        else:
                            in_main = False
                    else:
                        simplified_code.append(line)
            
            # Add imports and main function call
            code = '\n'.join(imports + ['\n'] + simplified_code + ['\n\nif __name__ == "__main__":\n    main()'])
            print(f"Simplified code is {len(code)} characters.")
        
        # Create task payload
        task = self.create_minimal_task(code, title)
        
        # Convert to JSON
        json_payload = json.dumps(task)
        
        # Compress the payload
        compressed_payload = self.compress_payload(json_payload)
        
        # Check final size
        final_size = len(compressed_payload)
        print(f"Final QR payload size: {final_size} bytes")
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=40,  # Maximum version
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Lower error correction for more data
            box_size=10,
            border=4,
        )
        
        try:
            qr.add_data(compressed_payload)
            qr.make(fit=True)
            
            # Create QR image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save the QR code
            output_path = os.path.join(self.output_dir, f"{title}.png")
            img.save(output_path)
            
            print(f"Created QR code: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error creating QR code: {e}")
            return None

def main():
    """Main function to run the QR encoder."""
    parser = argparse.ArgumentParser(description="Create executable QR codes from Python files.")
    parser.add_argument("--file", required=True, help="Python file to encode as QR code")
    parser.add_argument("--title", help="Title for the QR code")
    args = parser.parse_args()
    
    encoder = SimpleQREncoder()
    output_path = encoder.encode_file(args.file, args.title)
    
    if output_path:
        print("\nTo execute this QR code, run:")
        print(f"python qr_task_worker_from_file.py -f {output_path}")

if __name__ == "__main__":
    main()
