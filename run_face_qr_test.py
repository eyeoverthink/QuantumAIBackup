#!/usr/bin/env python3
"""
Run Face QR Test with Aggressive Optimization

This script runs the face image to QR code test with progressively more aggressive
optimization settings to ensure the QR code fits within version limits (≤ 40)
"""

import os
import sys
import subprocess
import time

def run_command(command, description=None):
    """Run a command and print its output"""
    if description:
        print(f"\n[+] {description}...")
    
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.stdout:
        print(f"--- Output ---\n{result.stdout}")
    
    if result.returncode != 0:
        if result.stderr:
            print(f"Error (code {result.returncode}):\n{result.stderr}")
        return False
    
    return True

def main():
    print("=== Face Image to QR Code Test with Aggressive Optimization ===")
    
    # First attempt: 24px size, 50% JPEG quality
    print("\nUsing: 24px size, 50% JPEG quality")
    if run_command(["python", "test_face_qr_system.py", "--image", "face.jpg", "--size_px", "24", "--jpeg_quality", "50"]):
        print("\nTest completed successfully!")
        return 0
    
    # Second attempt: 16px size, 40% JPEG quality
    print("\n\n=== First attempt failed, trying with more aggressive settings ===")
    print("Using: 16px size, 40% JPEG quality")
    if run_command(["python", "test_face_qr_system.py", "--image", "face.jpg", "--size_px", "16", "--jpeg_quality", "40"]):
        print("\nTest completed successfully!")
        return 0
    
    # Third attempt: 12px size, 30% JPEG quality
    print("\n\n=== Second attempt failed, trying with most aggressive settings ===")
    print("Using: 12px size, 30% JPEG quality")
    if run_command(["python", "test_face_qr_system.py", "--image", "face.jpg", "--size_px", "12", "--jpeg_quality", "30"]):
        print("\nTest completed successfully!")
        return 0
    
    # All attempts failed
    print("\n\n=== All attempts failed ===")
    print("Try manually adjusting the settings or using a smaller face image")
    return 1

if __name__ == "__main__":
    sys.exit(main())
