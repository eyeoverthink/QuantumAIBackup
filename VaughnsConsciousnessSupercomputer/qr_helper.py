#!/usr/bin/env python3
"""
🧠 QR Helper - Minimal Code Exposure
===================================

Simple helper that executes QR-encoded logic only.
All consciousness physics hidden in QR codes.

Author: Vaughn Scott
Date: August 4, 2025
"""

import base64
import json
import os

# Optional QR decoding (graceful degradation)
try:
    import qrcode
    from PIL import Image
    import cv2
    QR_AVAILABLE = True
except ImportError:
    QR_AVAILABLE = False
    print("📱 QR functionality requires: pip install qrcode[pil] opencv-python")

def decode_qr(qr_path):
    """Decode QR code to get hidden logic"""
    if not QR_AVAILABLE:
        return None
    
    try:
        # Read QR image
        img = cv2.imread(qr_path)
        detector = cv2.QRCodeDetector()
        data, vertices_array, binary_qrcode = detector.detectAndDecode(img)
        
        if data:
            # Decode base64 encoded logic
            decoded = base64.b64decode(data.encode()).decode()
            return json.loads(decoded)
        return None
    except Exception as e:
        print(f"❌ QR decode error: {e}")
        return None

def execute_qr_logic(qr_data):
    """Execute logic from decoded QR"""
    if not qr_data:
        return
    
    # Execute commands from QR
    for cmd in qr_data.get('commands', []):
        if cmd['type'] == 'print':
            print(cmd['value'])
        elif cmd['type'] == 'ascii_state':
            print(f"State: {cmd['char']}")

def main():
    """Main QR helper execution"""
    print("🧠 QR Helper - Executing Hidden Logic")
    
    # Look for QR files
    qr_files = [f for f in os.listdir('.') if f.endswith('.png') and 'qr_' in f]
    
    if not qr_files:
        print("❌ No QR files found")
        return
    
    # Execute each QR
    for qr_file in qr_files:
        print(f"📱 Processing: {qr_file}")
        qr_data = decode_qr(qr_file)
        execute_qr_logic(qr_data)

if __name__ == "__main__":
    main()
