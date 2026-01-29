#!/usr/bin/env python3
"""
Simple QR Code Test - Part of Animated QR Flipbook DNA System
By Vaughn Scott

A simple test script to verify basic QR code generation and decoding capabilities.
"""

import os
import sys
import json
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import cv2

# Test directory
TEST_DIR = "qr_test_dir"

def generate_simple_qr(text, filename):
    """Generate a simple QR code with the given text."""
    # Create output directory
    os.makedirs(TEST_DIR, exist_ok=True)
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save image
    filepath = os.path.join(TEST_DIR, filename)
    img.save(filepath)
    
    print(f"Generated QR code: {filepath}")
    return filepath

def decode_qr_pyzbar(image_path):
    """Decode QR code using pyzbar."""
    try:
        # Open image
        image = Image.open(image_path)
        
        # Decode QR code
        decoded_objects = decode(image)
        
        # Return decoded data if found
        if decoded_objects:
            return decoded_objects[0].data.decode('utf-8')
        
        return None
    except Exception as e:
        print(f"Error decoding QR code with pyzbar: {e}")
        return None

def decode_qr_opencv(image_path):
    """Decode QR code using OpenCV."""
    try:
        # Read image
        img = cv2.imread(image_path)
        
        # Initialize QR detector
        qr_detector = cv2.QRCodeDetector()
        
        # Detect and decode QR code
        retval, decoded_info, points, straight_qrcode = qr_detector.detectAndDecodeMulti(img)
        
        if retval and decoded_info and decoded_info[0]:
            return decoded_info[0]
        
        return None
    except Exception as e:
        print(f"Error decoding QR code with OpenCV: {e}")
        return None

def test_simple_text():
    """Test simple text QR code."""
    print("\n=== Testing Simple Text QR Code ===")
    text = "Hello World from QR Flipbook DNA System!"
    filepath = generate_simple_qr(text, "hello_world_1.png")
    
    # Decode with pyzbar
    print("\nDecoding with pyzbar...")
    decoded_text = decode_qr_pyzbar(filepath)
    if decoded_text:
        print(f"Successfully decoded: {decoded_text}")
        print(f"Matches original: {decoded_text == text}")
    else:
        print("Failed to decode with pyzbar")
    
    # Decode with OpenCV
    print("\nDecoding with OpenCV...")
    decoded_text = decode_qr_opencv(filepath)
    if decoded_text:
        print(f"Successfully decoded: {decoded_text}")
        print(f"Matches original: {decoded_text == text}")
    else:
        print("Failed to decode with OpenCV")

def test_json_payload():
    """Test JSON payload QR code."""
    print("\n=== Testing JSON Payload QR Code ===")
    payload = {
        "task_id": "Vaughn-Scott-June-26-5-14-pm",
        "task_type": "test",
        "message": "This is an official test from me, to see if qr codes work!!",
        "timestamp": "June-26-5-14-pm"
    }
    json_text = json.dumps(payload)
    filepath = generate_simple_qr(json_text, "json_payload_1.png")
    
    # Decode with pyzbar
    print("\nDecoding with pyzbar...")
    decoded_text = decode_qr_pyzbar(filepath)
    if decoded_text:
        try:
            decoded_payload = json.loads(decoded_text)
            print(f"Successfully decoded JSON: {decoded_payload}")
            print(f"Matches original: {decoded_payload == payload}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
    else:
        print("Failed to decode with pyzbar")
    
    # Decode with OpenCV
    print("\nDecoding with OpenCV...")
    decoded_text = decode_qr_opencv(filepath)
    if decoded_text:
        try:
            decoded_payload = json.loads(decoded_text)
            print(f"Successfully decoded JSON: {decoded_payload}")
            print(f"Matches original: {decoded_payload == payload}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
    else:
        print("Failed to decode with OpenCV")

def test_task_payload():
    """Test task payload QR code."""
    print("\n=== Testing Task Payload QR Code ===")
    payload = {
        "task_id": "task-123",
        "task_type": "execute_python",
        "script": "print('Hello from QR task!')\nprint('This is a test of QR code task execution.')",
        "input_data": {"test_param": "test_value"},
        "timestamp": "2025-06-26T14:40:00"
    }
    json_text = json.dumps(payload)
    filepath = generate_simple_qr(json_text, "task_payload.png")
    
    # Decode with pyzbar
    print("\nDecoding with pyzbar...")
    decoded_text = decode_qr_pyzbar(filepath)
    if decoded_text:
        try:
            decoded_payload = json.loads(decoded_text)
            print(f"Successfully decoded task payload")
            print(f"Task ID: {decoded_payload.get('task_id')}")
            print(f"Task type: {decoded_payload.get('task_type')}")
            print(f"Matches original: {decoded_payload == payload}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
    else:
        print("Failed to decode with pyzbar")
    
    # Decode with OpenCV
    print("\nDecoding with OpenCV...")
    decoded_text = decode_qr_opencv(filepath)
    if decoded_text:
        try:
            decoded_payload = json.loads(decoded_text)
            print(f"Successfully decoded task payload")
            print(f"Task ID: {decoded_payload.get('task_id')}")
            print(f"Task type: {decoded_payload.get('task_type')}")
            print(f"Matches original: {decoded_payload == payload}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
    else:
        print("Failed to decode with OpenCV")

def main():
    """Main function."""
    print("Simple QR Code Test - Starting")
    
    # Test simple text QR code
    test_simple_text()
    
    # Test JSON payload QR code
    test_json_payload()
    
    # Test task payload QR code
    test_task_payload()
    
    print("\nSimple QR Code Test - Complete")

if __name__ == "__main__":
    main()
