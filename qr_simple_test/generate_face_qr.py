#!/usr/bin/env python3
"""
Generates a QR code containing a small, grayscale image of a face.
"""

import argparse
import qrcode
import json
import base64
from PIL import Image, ImageOps
import io
import os
import uuid
import time

# Constants
PHI = (1 + 5**0.5) / 2

def create_face_qr(image_path, output_qr_path="user_face_qr.png", size=(96, 96), jpeg_quality=75):
    """
    Loads an image, resizes it, converts to grayscale, converts to JPEG, 
    base64 encodes it, and generates a QR code containing this data.

    Args:
        image_path (str): Path to the input image file.
        output_qr_path (str): Path to save the generated QR code image.
        size (tuple): Target size (width, height) for the image before encoding.
        jpeg_quality (int): Quality for JPEG compression (1-95).
    """
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Resize and convert to grayscale
    img_resized = img.resize(size, Image.LANCZOS)
    img_gray = ImageOps.grayscale(img_resized)

    # Convert image to JPEG bytes in memory
    buffered_jpeg = io.BytesIO()
    try:
        img_gray.save(buffered_jpeg, format="JPEG", quality=jpeg_quality)
    except Exception as e:
        print(f"Error saving image to JPEG buffer: {e}")
        return
    
    img_jpeg_bytes = buffered_jpeg.getvalue()
    img_base64 = base64.b64encode(img_jpeg_bytes).decode('utf-8')

    # Create task data payload
    task_id = str(uuid.uuid4())
    payload = {
        "issuer_id": "generate_face_qr",
        "task_data": {
            "task_type": "display_face_image",
            "task_id": task_id,
            "timestamp": time.time() * PHI, # Phi-Harmonic Timestamp
            "original_filename": os.path.basename(image_path),
            "processed_size": f"{size[0]}x{size[1]}",
            "image_format": "JPEG_Grayscale",
            "image_data_base64": img_base64
        }
    }

    # Generate QR code
    qr = qrcode.QRCode(
        version=None, # Auto-detect version based on data size
        error_correction=qrcode.constants.ERROR_CORRECT_M, # Medium error correction
        box_size=10,
        border=4,
    )
    qr.add_data(json.dumps(payload))
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="black", back_color="white")
    
    # Ensure output directory exists if specified in path
    output_dir = os.path.dirname(output_qr_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
        
    img_qr.save(output_qr_path)

    print(f"Successfully processed image: {image_path}")
    print(f"QR code containing face image saved to: {os.path.abspath(output_qr_path)}")
    print(f"Payload Task ID: {task_id}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code from a face image.")
    parser.add_argument("--image", required=True, help="Path to the input face image file.")
    parser.add_argument("--output", default="user_face_qr.png", help="Path to save the generated QR code image.")
    parser.add_argument("--size_px", type=int, default=96, help="Dimension (width & height) for the processed image in pixels.")
    parser.add_argument("--jpeg_quality", type=int, default=75, help="JPEG quality for compression (1-95, higher is better quality).")

    args = parser.parse_args()
    
    if not (1 <= args.jpeg_quality <= 95):
        print("Error: JPEG quality must be between 1 and 95.")
        exit()

    create_face_qr(args.image, args.output, size=(args.size_px, args.size_px), jpeg_quality=args.jpeg_quality)
