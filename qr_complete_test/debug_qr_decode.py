#!/usr/bin/env python3

from PIL import Image
from qreader import QReader
import cv2
import json

def debug_qr_decode(image_path):
    """Debug QR code decoding to see what's inside"""
    print(f"Debugging QR code: {image_path}")
    
    try:
        # Try with qreader first
        qreader = QReader()
        image = cv2.imread(image_path)
        
        if image is None:
            print("Error: Could not load image with cv2")
            return
            
        print(f"Image loaded successfully: {image.shape}")
        
        # Decode QR code
        decoded_text = qreader.detect_and_decode(image=image)
        
        if decoded_text:
            print(f"QR Code decoded successfully!")
            print(f"Raw content length: {len(decoded_text[0])}")
            print(f"Raw content (first 200 chars): {decoded_text[0][:200]}...")
            
            # Try to parse as JSON
            try:
                data = json.loads(decoded_text[0])
                print(f"JSON parsed successfully!")
                print(f"Keys: {list(data.keys())}")
                for key, value in data.items():
                    if isinstance(value, str) and len(value) > 100:
                        print(f"{key}: {value[:100]}...")
                    else:
                        print(f"{key}: {value}")
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
                
        else:
            print("No QR code detected or could not decode")
            
    except Exception as e:
        print(f"Error during decoding: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python debug_qr_decode.py <qr_image.png>")
        sys.exit(1)
    
    debug_qr_decode(sys.argv[1])
