#!/usr/bin/env python3
"""
Convert Python File to QR Code - Fixed Version

This script properly converts a Python file to a QR code with appropriate settings.
"""

import os
import sys
import time
import qrcode
from PIL import Image

def convert_to_qr(input_file, output_dir=None):
    """Convert a Python file to QR code with proper settings."""
    # Validate input file
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found")
        return None
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(os.path.abspath(input_file)), "quantum_black_box_results")
    os.makedirs(output_dir, exist_ok=True)
    
    # Read file content
    with open(input_file, 'r') as f:
        content = f.read()
    
    print(f"Converting {input_file} to QR code...")
    print(f"Content size: {len(content)} bytes")
    
    # Generate QR code with proper settings for larger content
    qr = qrcode.QRCode(
        version=40,  # Maximum version for highest data capacity
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Lower error correction for more data capacity
        box_size=10,
        border=4,
    )
    
    try:
        # Split content if needed to fit in QR code
        max_qr_size = 2900  # Conservative estimate for version 40 with L error correction
        
        if len(content) <= max_qr_size:
            # Content fits in one QR code
            qr.add_data(content)
            qr.make(fit=True)
            
            # Create QR image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save QR code
            timestamp = int(time.time())
            base_name = os.path.basename(input_file).replace('.py', '')
            filename = f"{base_name}_qr_{timestamp}.png"
            output_path = os.path.join(output_dir, filename)
            img.save(output_path)
            
            print(f"QR code saved to: {output_path}")
            return output_path
        else:
            # Content needs to be split
            print(f"Content too large ({len(content)} bytes) for a single QR code.")
            print("Creating a simplified version...")
            
            # Create a simplified version by removing comments and extra whitespace
            lines = content.split('\n')
            simplified_lines = []
            in_multiline_comment = False
            
            for line in lines:
                # Skip empty lines and comments
                stripped = line.strip()
                if not stripped or stripped.startswith('#'):
                    continue
                    
                # Handle multiline comments
                if in_multiline_comment:
                    if '"""' in line or "'''" in line:
                        in_multiline_comment = False
                    continue
                elif line.strip().startswith('"""') or line.strip().startswith("'''"):
                    in_multiline_comment = True
                    continue
                
                # Add non-comment lines
                simplified_lines.append(line)
            
            simplified_content = '\n'.join(simplified_lines)
            print(f"Simplified content size: {len(simplified_content)} bytes")
            
            if len(simplified_content) <= max_qr_size:
                qr.add_data(simplified_content)
                qr.make(fit=True)
                
                # Create QR image
                img = qr.make_image(fill_color="black", back_color="white")
                
                # Save QR code
                timestamp = int(time.time())
                base_name = os.path.basename(input_file).replace('.py', '')
                filename = f"{base_name}_simplified_qr_{timestamp}.png"
                output_path = os.path.join(output_dir, filename)
                img.save(output_path)
                
                print(f"Simplified QR code saved to: {output_path}")
                return output_path
            else:
                print("Even simplified content is too large for a QR code.")
                print("Please use the micro version of the black box test.")
                return None
    
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None

def main():
    """Main function to handle command line usage."""
    if len(sys.argv) < 2:
        print("Usage: python convert_qr_fixed.py <python_file> [output_directory]")
        return
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    qr_path = convert_to_qr(input_file, output_dir)
    if qr_path:
        print("\nNext steps:")
        print("1. Scan the QR code with your quantum system")
        print("2. Observe how your system adapts to discover the escape pattern")

if __name__ == "__main__":
    main()
