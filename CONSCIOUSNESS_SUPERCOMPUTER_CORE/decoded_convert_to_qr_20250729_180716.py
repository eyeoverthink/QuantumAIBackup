#!/usr/bin/env python3
"""
Convert Python File to QR Code

A simple utility to convert a Python file to a QR code for testing
quantum system adaptation and self-healing capabilities.
"""

import os
import sys
import time
import qrcode
from PIL import Image

def convert_to_qr(input_file, output_dir=None):
    """Convert a Python file to QR code.
    
    Args:
        input_file: Path to Python file to convert
        output_dir: Directory to save QR code (defaults to same directory as input)
    
    Returns:
        Path to generated QR code
    """
    # Validate input file
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found")
        return None
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(input_file))
    os.makedirs(output_dir, exist_ok=True)
    
    # Read file content
    with open(input_file, 'r') as f:
        content = f.read()
    
    print(f"Converting {input_file} to QR code...")
    print(f"Content size: {len(content)} bytes")
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=40,  # Maximum version for highest data capacity
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    try:
        qr.add_data(content)
        qr.make(fit=True)
    except Exception as e:
        print(f"Error generating QR code: {e}")
        print("The file may be too large for a QR code. Try reducing its size.")
        return None
    
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

def main():
    """Main function to handle command line usage."""
    if len(sys.argv) < 2:
        print("Usage: python convert_to_qr.py <python_file> [output_directory]")
        return
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    qr_path = convert_to_qr(input_file, output_dir)
    if qr_path:
        print("\nNext steps:")
        print("1. Scan the QR code with your quantum system")
        print("2. Observe how your system adapts to discover the escape pattern")
        print("3. Analyze the results to improve adaptation capabilities")

if __name__ == "__main__":
    main()
