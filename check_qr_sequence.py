#!/usr/bin/env python3
"""
Check QR Sequence - Simple utility to check if QR sequence was generated
By Vaughn Scott
"""

import os
import sys

def main():
    """Check if QR sequence directory exists and list its contents"""
    sequence_dir = "qr_sequence"
    
    # Check if directory exists
    if not os.path.exists(sequence_dir):
        print(f"QR sequence directory '{sequence_dir}' not found.")
        print("Available directories in current path:")
        for item in os.listdir("."):
            if os.path.isdir(item):
                print(f"  - {item}")
        return
    
    # List contents
    print(f"QR sequence directory '{sequence_dir}' found.")
    print(f"Contents of {sequence_dir}:")
    
    files = sorted(os.listdir(sequence_dir))
    for file in files:
        file_path = os.path.join(sequence_dir, file)
        size = os.path.getsize(file_path)
        print(f"  - {file} ({size} bytes)")
    
    print(f"Total files: {len(files)}")

if __name__ == "__main__":
    print("QR Sequence Checker - By Vaughn Scott")
    main()
