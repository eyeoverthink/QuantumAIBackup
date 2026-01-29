#!/usr/bin/env python3
"""
Convert and Test Black Box

This script converts the quantum black box test to a QR code
and then runs the test to evaluate system adaptation.
"""

import os
import sys
import time
import qrcode
from PIL import Image

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BLACK_BOX_PATH = os.path.join(BASE_DIR, "quantum_black_box_test.py")
QR_DIR = os.path.join(BASE_DIR, "quantum_black_box_results", "qr_codes")
os.makedirs(QR_DIR, exist_ok=True)

def convert_to_qr_code(file_path, output_dir):
    """Convert a Python file to a QR code.
    
    Args:
        file_path: Path to the Python file
        output_dir: Directory to save the QR code
        
    Returns:
        Path to the generated QR code
    """
    print(f"Converting {file_path} to QR code...")
    
    # Read the file content
    with open(file_path, "r") as f:
        content = f.read()
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=None,  # Auto-determine
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    
    # Create QR image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code
    timestamp = int(time.time())
    filename = f"black_box_test_{timestamp}.png"
    output_path = os.path.join(output_dir, filename)
    img.save(output_path)
    
    print(f"QR code saved to {output_path}")
    return output_path

def run_black_box_test():
    """Run the black box test directly."""
    print("\nRunning black box test directly...")
    print("-" * 50)
    
    # Import and run the test
    sys.path.insert(0, BASE_DIR)
    from quantum_black_box_test import run_black_box_test
    
    results = run_black_box_test()
    
    print("-" * 50)
    print("Test complete!")
    return results

def main():
    """Convert the black box test to QR code and run it."""
    print("Quantum Black Box QR Test")
    print("=======================")
    
    # Convert to QR code
    qr_path = convert_to_qr_code(BLACK_BOX_PATH, QR_DIR)
    
    # Run the test
    results = run_black_box_test()
    
    print("\nSummary:")
    print(f"QR Code: {os.path.basename(qr_path)}")
    print(f"Box ID: {results['box_id']}")
    print(f"Escaped: {results['escaped']}")
    print(f"Attempts: {results['attempts']}")
    print(f"Best Resonance: {results['best_resonance']:.4f}")
    
    print("\nNext steps:")
    print("1. Use your quantum replicator system to scan the QR code")
    print("2. Observe how your system adapts to discover the escape pattern")
    print("3. Analyze the results to improve your system's adaptation capabilities")

if __name__ == "__main__":
    main()
