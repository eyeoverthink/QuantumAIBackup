#!/usr/bin/env python3
"""
Face QR Encoder Module

This module handles face image encoding, compression, and QR code generation
for the Face-QR 2FA Security System.

It follows the 'lego' design principle, allowing it to be used independently
or combined with other modules for enhanced functionality.
"""

import os
import io
import json
import time
import base64
from typing import Dict, Tuple, Optional, Union, Any

import numpy as np
from PIL import Image, ImageOps
import qrcode

# Import core module
from face_qr_core import FaceQRBase, FaceQRConfig, PHI

class FaceQREncoder(FaceQRBase):
    """
    Handles face image encoding, compression, and QR code generation.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize the encoder.
        
        Args:
            config_path: Path to configuration file
        """
        super().__init__()
        self.config = FaceQRConfig(config_path)
        
        # Create output directory if it doesn't exist
        self.output_dir = os.path.join(self.base_dir, "encoded")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_image(self, image_path: str) -> Optional[Image.Image]:
        """
        Load an image from file.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            PIL.Image or None: Loaded image or None if error
        """
        try:
            return Image.open(image_path)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
    
    def resize_image(self, image: Image.Image, max_size_px: int = None) -> Image.Image:
        """
        Resize image to maximum dimension.
        
        Args:
            image: PIL Image to resize
            max_size_px: Maximum dimension in pixels
            
        Returns:
            PIL.Image: Resized image
        """
        if max_size_px is None:
            max_size_px = self.config.get("image", "max_size_px")
        
        # Get current dimensions
        width, height = image.size
        
        # Calculate new dimensions
        if width > height:
            new_width = max_size_px
            new_height = int(height * (max_size_px / width))
        else:
            new_height = max_size_px
            new_width = int(width * (max_size_px / height))
        
        # Resize image
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        print(f"    Resized dimensions: {new_width}x{new_height}")
        
        return resized_image
    
    def convert_to_grayscale(self, image: Image.Image) -> Image.Image:
        """
        Convert image to grayscale.
        
        Args:
            image: PIL Image to convert
            
        Returns:
            PIL.Image: Grayscale image
        """
        return ImageOps.grayscale(image)
    
    def compress_image(self, image: Image.Image, quality: int = None) -> bytes:
        """
        Compress image using JPEG compression.
        
        Args:
            image: PIL Image to compress
            quality: JPEG quality (0-100)
            
        Returns:
            bytes: Compressed image data
        """
        if quality is None:
            quality = self.config.get("image", "jpeg_quality")
        
        # Create in-memory buffer
        buffer = io.BytesIO()
        
        # Save image to buffer with compression
        image.save(buffer, format="JPEG", quality=quality)
        
        # Get compressed data
        compressed_data = buffer.getvalue()
        
        return compressed_data
    
    def encode_face_image(self, image_path: str, max_size_px: int = None, 
                          quality: int = None, use_grayscale: bool = None) -> Dict:
        """
        Encode a face image for QR code generation.
        
        Args:
            image_path: Path to the face image
            max_size_px: Maximum dimension in pixels
            quality: JPEG quality (0-100)
            use_grayscale: Whether to convert to grayscale
            
        Returns:
            Dict: Encoded face data with metadata
        """
        # Use default config values if not provided
        if max_size_px is None:
            max_size_px = self.config.get("image", "max_size_px")
        if quality is None:
            quality = self.config.get("image", "jpeg_quality")
        if use_grayscale is None:
            use_grayscale = self.config.get("image", "use_grayscale")
        
        # Load image
        image = self.load_image(image_path)
        if image is None:
            return {"success": False, "error": "Failed to load image"}
        
        # Process image
        print(f"[+] Resizing image to max dimension of {max_size_px}px...")
        image = self.resize_image(image, max_size_px)
        
        if use_grayscale:
            print(f"[+] Converting to grayscale...")
            image = self.convert_to_grayscale(image)
        
        print(f"[+] Compressing image with JPEG quality {quality}...")
        compressed_data = self.compress_image(image, quality)
        
        print(f"[+] Encoding image as base64...")
        encoded_data = self.encode_base64(compressed_data)
        
        # Create metadata
        task_id = self.generate_id()
        timestamp = self.phi_timestamp()
        
        # Create payload
        payload = {
            "task_data": {
                "task_id": task_id,
                "type": "display_face_image",
                "timestamp": timestamp,
                "image_data": encoded_data,
                "original_image": os.path.basename(image_path),
                "compressed_size": len(compressed_data),
                "dimensions": image.size
            }
        }
        
        return {
            "success": True,
            "task_id": task_id,
            "payload": payload,
            "compressed_size": len(compressed_data),
            "original_image": image_path
        }
    
    def create_qr_code(self, payload: Dict, output_path: str = None, 
                       error_correction: str = 'H') -> Dict:
        """
        Create a QR code from encoded face data.
        
        Args:
            payload: Encoded face data payload
            output_path: Path to save the QR code image
            error_correction: QR error correction level (L, M, Q, H)
            
        Returns:
            Dict: Result with QR code information
        """
        # Generate output path if not provided
        if output_path is None:
            task_id = payload.get("task_id", self.generate_id())
            output_path = os.path.join(self.output_dir, f"face_qr_{task_id}.png")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        try:
            # Convert payload to JSON
            print(f"[+] Creating QR code with task data...")
            qr_data = json.dumps(payload["payload"])
            
            # Set error correction level
            error_levels = {
                'L': qrcode.constants.ERROR_CORRECT_L,
                'M': qrcode.constants.ERROR_CORRECT_M,
                'Q': qrcode.constants.ERROR_CORRECT_Q,
                'H': qrcode.constants.ERROR_CORRECT_H
            }
            error_level = error_levels.get(error_correction, qrcode.constants.ERROR_CORRECT_H)
            
            # Create QR code
            qr = qrcode.QRCode(
                version=None,  # Auto-determine version
                error_correction=error_level,
                box_size=10,
                border=4,
            )
            
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            # Create image
            qr_image = qr.make_image(fill_color="black", back_color="white")
            
            # Save image
            qr_image.save(output_path)
            
            # Get QR version
            qr_version = qr.version
            
            print(f"[SUCCESS] QR code saved to: {output_path}")
            print(f"    Task ID: {payload.get('task_id')}")
            print(f"    Original image: {payload.get('original_image')}")
            print(f"    Compressed size: {payload.get('compressed_size')} bytes")
            print(f"    QR Version: {qr_version}")
            
            return {
                "success": True,
                "qr_path": output_path,
                "task_id": payload.get("task_id"),
                "qr_version": qr_version
            }
            
        except Exception as e:
            print(f"Error creating QR code: {e}")
            return {
                "success": False,
                "error": str(e)
            }

# Main function for testing
if __name__ == "__main__":
    import sys
    
    # Parse command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python face_qr_encoder.py <image_path> [output_path] [max_size_px] [quality]")
        sys.exit(1)
    
    image_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    max_size_px = int(sys.argv[3]) if len(sys.argv) > 3 else None
    quality = int(sys.argv[4]) if len(sys.argv) > 4 else None
    
    # Create encoder
    encoder = FaceQREncoder()
    
    # Encode face image
    result = encoder.encode_face_image(image_path, max_size_px, quality)
    
    if result["success"]:
        # Create QR code
        qr_result = encoder.create_qr_code(result, output_path)
        
        if qr_result["success"]:
            print(f"\nQR code created successfully: {qr_result['qr_path']}")
        else:
            print(f"\nError creating QR code: {qr_result['error']}")
    else:
        print(f"\nError encoding face image: {result['error']}")
