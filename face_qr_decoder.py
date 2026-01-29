#!/usr/bin/env python3
"""
Face QR Decoder Module

This module handles QR code decoding and face image extraction
for the Face-QR 2FA Security System.

It follows the 'lego' design principle, allowing it to be used independently
or combined with other modules for enhanced functionality.
"""

import os
import io
import json
import time
import base64
from typing import Dict, Tuple, Optional, Union, Any, List

import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode as pyzbar_decode

# Import core module
from face_qr_core import FaceQRBase, FaceQRConfig, PHI

class FaceQRDecoder(FaceQRBase):
    """
    Handles QR code decoding and face image extraction.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize the decoder.
        
        Args:
            config_path: Path to configuration file
        """
        super().__init__()
        self.config = FaceQRConfig(config_path)
        
        # Create output directory if it doesn't exist
        self.output_dir = os.path.join(self.base_dir, "decoded")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_qr_image(self, qr_path: str) -> Optional[Image.Image]:
        """
        Load a QR code image from file.
        
        Args:
            qr_path: Path to the QR code image
            
        Returns:
            PIL.Image or None: Loaded image or None if error
        """
        try:
            return Image.open(qr_path)
        except Exception as e:
            print(f"Error loading QR code image: {e}")
            return None
    
    def decode_qr_image(self, qr_image: Union[str, Image.Image]) -> List[Dict]:
        """
        Decode QR codes from an image.
        
        Args:
            qr_image: Path to QR code image or PIL Image object
            
        Returns:
            List[Dict]: List of decoded QR codes with data and metadata
        """
        # Load image if path is provided
        if isinstance(qr_image, str):
            image = self.load_qr_image(qr_image)
            if image is None:
                return []
        else:
            image = qr_image
        
        try:
            # Decode QR codes
            decoded_objects = pyzbar_decode(image)
            
            results = []
            for obj in decoded_objects:
                # Get data and type
                data = obj.data.decode('utf-8')
                qr_type = obj.type
                
                # Try to parse as JSON
                try:
                    json_data = json.loads(data)
                    results.append({
                        "type": qr_type,
                        "data": json_data,
                        "raw": data,
                        "rect": obj.rect,
                        "polygon": obj.polygon
                    })
                except json.JSONDecodeError:
                    # Not valid JSON, store as raw data
                    results.append({
                        "type": qr_type,
                        "data": None,
                        "raw": data,
                        "rect": obj.rect,
                        "polygon": obj.polygon
                    })
            
            return results
            
        except Exception as e:
            print(f"Error decoding QR code: {e}")
            return []
    
    def extract_face_image(self, qr_data: Dict) -> Dict:
        """
        Extract face image from decoded QR data.
        
        Args:
            qr_data: Decoded QR data
            
        Returns:
            Dict: Result with extracted face image information
        """
        try:
            # Check if this is a face image task
            task_data = qr_data.get("task_data", {})
            if not task_data:
                # Check if data is nested
                if "data" in qr_data and isinstance(qr_data["data"], dict):
                    task_data = qr_data["data"].get("task_data", {})
            
            if not task_data:
                return {
                    "success": False,
                    "error": "No task data found in QR code"
                }
            
            # Check task type
            task_type = task_data.get("type")
            if task_type != "display_face_image":
                return {
                    "success": False,
                    "error": f"Not a face image task (type: {task_type})"
                }
            
            # Get image data
            encoded_image = task_data.get("image_data")
            if not encoded_image:
                return {
                    "success": False,
                    "error": "No image data found in task"
                }
            
            # Decode base64 image data
            try:
                image_data = self.decode_base64(encoded_image)
            except Exception as e:
                return {
                    "success": False,
                    "error": f"Error decoding base64 image data: {e}"
                }
            
            # Get metadata
            task_id = task_data.get("task_id", self.generate_id())
            timestamp = task_data.get("timestamp", self.phi_timestamp())
            original_image = task_data.get("original_image", "unknown")
            dimensions = task_data.get("dimensions", (0, 0))
            
            # Generate output path
            output_filename = f"decoded_face_{task_id}_{int(timestamp)}.png"
            output_path = os.path.join(self.output_dir, output_filename)
            
            # Save image
            try:
                # Create image from data
                image = Image.open(io.BytesIO(image_data))
                
                # Save image
                image.save(output_path)
                
                return {
                    "success": True,
                    "task_id": task_id,
                    "image_path": output_path,
                    "timestamp": timestamp,
                    "original_image": original_image,
                    "dimensions": dimensions
                }
                
            except Exception as e:
                return {
                    "success": False,
                    "error": f"Error saving decoded image: {e}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Error extracting face image: {e}"
            }
    
    def process_qr_code(self, qr_path: str) -> Dict:
        """
        Process a QR code image to extract face image.
        
        Args:
            qr_path: Path to QR code image
            
        Returns:
            Dict: Result with extracted face image information
        """
        print(f"Attempting to decode QR codes from image: {qr_path}")
        
        # Decode QR codes
        decoded_qrs = self.decode_qr_image(qr_path)
        
        if not decoded_qrs:
            return {
                "success": False,
                "error": "No QR codes found in image"
            }
        
        # Process each QR code
        for qr in decoded_qrs:
            # Check if this is a face image task
            if qr["data"] and "task_data" in qr["data"]:
                print("Detected 'task_data' nesting, using inner payload for task details.")
                result = self.extract_face_image(qr["data"])
                
                if result["success"]:
                    return result
            
            # Try direct extraction
            result = self.extract_face_image(qr)
            
            if result["success"]:
                return result
        
        return {
            "success": False,
            "error": "No valid face image found in QR codes"
        }
    
    def find_decoded_face_images(self) -> List[str]:
        """
        Find all decoded face images in the output directory.
        
        Returns:
            List[str]: List of file paths
        """
        try:
            # Get all PNG files in the output directory
            files = [f for f in os.listdir(self.output_dir) if f.startswith("decoded_face_") and f.endswith(".png")]
            
            # Sort by timestamp (newest first)
            files.sort(reverse=True)
            
            # Return full paths
            return [os.path.join(self.output_dir, f) for f in files]
        except Exception as e:
            print(f"Error finding decoded face images: {e}")
            return []

# Main function for testing
if __name__ == "__main__":
    import sys
    
    # Parse command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python face_qr_decoder.py <qr_image_path>")
        sys.exit(1)
    
    qr_path = sys.argv[1]
    
    # Create decoder
    decoder = FaceQRDecoder()
    
    # Process QR code
    result = decoder.process_qr_code(qr_path)
    
    if result["success"]:
        print(f"\n[SUCCESS] Face image extracted from QR code")
        print(f"  Task ID: {result['task_id']}")
        print(f"  Image saved to: {result['image_path']}")
        print(f"  Original image: {result['original_image']}")
        print(f"  Dimensions: {result['dimensions']}")
    else:
        print(f"\n[ERROR] Failed to extract face image: {result['error']}")
        
        # Try to find any decoded images
        images = decoder.find_decoded_face_images()
        
        if images:
            print(f"\nFound {len(images)} previously decoded face images:")
            for i, image_path in enumerate(images[:5]):  # Show at most 5
                print(f"  {i+1}. {os.path.basename(image_path)}")
