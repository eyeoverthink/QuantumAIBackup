#!/usr/bin/env python3
"""
QR Sequence Test - Part of Animated QR Flipbook DNA System
By Vaughn Scott

A simple test script to verify QR code generation and decoding capabilities
using the existing QR worker logic.
"""

import os
import sys
import json
import time
import uuid
from datetime import datetime

# Import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qr_robust_generator import QRRobustGenerator
from qr_worker import QRWorker

# Test directories
TEST_OUTPUT_DIR = "qr_test_sequence"
TEST_RESPONSE_DIR = "qr_test_responses"

def create_test_payloads():
    """Create test payloads for QR code generation."""
    payloads = []
    
    # Python script payload
    python_payload = {
        "session_id": str(uuid.uuid4()),
        "frame_number": 1,
        "task_type": "execute_python",
        "content": """
print("Hello from QR Flipbook DNA System!")
print(f"Current time: {datetime.now().isoformat()}")
print("This is a test of the QR code generation and decoding system.")
""",
        "phi_metadata": {
            "generation": 1,
            "complexity": 0.618,
            "resonance": 1.618
        },
        "timestamp": datetime.now().isoformat()
    }
    payloads.append(python_payload)
    
    # Shell script payload
    shell_payload = {
        "session_id": str(uuid.uuid4()),
        "frame_number": 2,
        "task_type": "execute_sh",
        "content": """#!/bin/bash
echo "Hello from QR Flipbook DNA System Shell Script!"
echo "Current date: $(date)"
echo "This is a test of the QR code shell script execution."
""",
        "phi_metadata": {
            "generation": 1,
            "complexity": 0.618,
            "resonance": 1.618
        },
        "timestamp": datetime.now().isoformat()
    }
    payloads.append(shell_payload)
    
    return payloads

def generate_test_qr_sequence():
    """Generate test QR sequence."""
    # Create output directory
    os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)
    
    # Create QR generator
    generator = QRRobustGenerator(output_dir=TEST_OUTPUT_DIR)
    
    # Create test payloads
    payloads = create_test_payloads()
    
    # Generate QR codes
    qr_files = []
    for i, payload in enumerate(payloads):
        frame_number = i + 1
        json_payload = json.dumps(payload)
        
        print(f"Generating QR code for frame {frame_number}...")
        path = generator.generate_frame(json_payload, frame_number)
        
        if isinstance(path, list):
            qr_files.extend(path)
            print(f"  Generated {len(path)} chunked QR codes")
        else:
            qr_files.append(path)
            print(f"  Generated QR code: {os.path.basename(path)}")
    
    print(f"Generated {len(qr_files)} QR code files in {TEST_OUTPUT_DIR}")
    return qr_files

def test_qr_decoding_and_execution():
    """Test QR decoding and execution using QRWorker."""
    # Create QR worker
    worker = QRWorker(output_dir=TEST_RESPONSE_DIR)
    
    # Get all QR files
    qr_files = [os.path.join(TEST_OUTPUT_DIR, f) for f in os.listdir(TEST_OUTPUT_DIR) 
                if f.startswith("qr_frame_") and f.endswith(".png")]
    
    if not qr_files:
        print("No QR code files found!")
        return
    
    # Process each QR file
    for qr_file in sorted(qr_files):
        print(f"\nProcessing QR file: {qr_file}")
        response_path = worker.process_qr_image(qr_file)
        
        if response_path:
            print(f"Generated response QR: {response_path}")
        else:
            print("Failed to process QR code")
    
    print(f"\nTest completed. Response QR codes are in {TEST_RESPONSE_DIR}")

def main():
    """Main function."""
    print("QR Sequence Test - Starting")
    
    # Generate test QR sequence
    print("\n=== Generating Test QR Sequence ===")
    generate_test_qr_sequence()
    
    # Test QR decoding and execution
    print("\n=== Testing QR Decoding and Execution ===")
    test_qr_decoding_and_execution()
    
    print("\nQR Sequence Test - Complete")

if __name__ == "__main__":
    main()
