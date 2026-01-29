#!/usr/bin/env python3
"""
Improved QR Sequence Analyzer - Part of Animated QR Flipbook DNA System
By Vaughn Scott (with Cascade Assistant fixes)

A phi-optimized QR sequence analyzer with enhanced decoding capabilities.
"""

import os
import sys
import json
import base64
import zlib
import glob
import math
import numpy as np
from PIL import Image, ImageOps
from pyzbar.pyzbar import decode

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRSimpleAnalyzer:
    """
    Enhanced QR code analyzer for QR Flipbook DNA System.
    """
    
    def __init__(self, verbose=False):
        """
        Initialize the QR analyzer.
        
        Args:
            verbose: Whether to print verbose output
        """
        self.verbose = verbose
        self.phi_resonance_factor = 1/PHI  # ~0.618 (φ⁻¹)
    
    def decompress_payload(self, payload):
        """
        Decompress payload using zlib and base64 decode.
        
        Args:
            payload: Compressed payload with marker
            
        Returns:
            Decompressed payload
        """
        if payload.startswith("COMPRESSED:"):
            encoded = payload.replace("COMPRESSED:", "", 1)
            try:
                compressed = base64.b64decode(encoded)
                decompressed = zlib.decompress(compressed)
                return decompressed.decode('utf-8')
            except Exception as e:
                if self.verbose:
                    print(f"Error decompressing payload: {e}")
                return payload
        return payload
    
    def preprocess_image(self, image_path):
        """
        Preprocess image to improve QR code detection.
        
        Args:
            image_path: Path to QR code image
            
        Returns:
            Preprocessed PIL Image object
        """
        try:
            # Open image
            image = Image.open(image_path)
            
            # Convert to grayscale to reduce color interference
            gray = ImageOps.grayscale(image)
            
            # Increase contrast to make QR code more visible
            contrast = ImageOps.autocontrast(gray, cutoff=self.phi_resonance_factor * 10)
            
            # Create multiple processing variants for phi-harmonic detection
            variants = [
                image,  # Original image
                gray,   # Grayscale
                contrast,  # High contrast
                ImageOps.invert(gray),  # Inverted grayscale
            ]
            
            return variants
        except Exception as e:
            if self.verbose:
                print(f"Error preprocessing image: {e}")
            return [Image.open(image_path)]  # Return original image if preprocessing fails
    
    def decode_qr_image(self, image_path):
        """
        Decode QR code from image with enhanced phi-harmonic detection.
        
        Args:
            image_path: Path to QR code image
            
        Returns:
            Decoded payload or None if decoding failed
        """
        if self.verbose:
            print(f"Decoding QR image: {image_path}")
        
        try:
            # Get preprocessed image variants
            image_variants = self.preprocess_image(image_path)
            
            # Try decoding with each variant
            for i, img in enumerate(image_variants):
                # Try decoding with pyzbar
                decoded_objects = decode(img)
                
                # Return decoded data if found
                if decoded_objects:
                    data = decoded_objects[0].data.decode('utf-8')
                    
                    # Check if payload is compressed
                    if data.startswith("COMPRESSED:"):
                        if self.verbose:
                            print("Detected compressed payload, decompressing...")
                        data = self.decompress_payload(data)
                    
                    if self.verbose:
                        print(f"Successfully decoded QR code using variant {i}")
                    
                    return data
            
            # If no variants worked, try with specific regions (remove visual indicators)
            original = Image.open(image_path)
            # Crop out the corners where visual indicators might be
            width, height = original.size
            crop_margin = int(min(width, height) * 0.1)  # 10% margin
            
            # Crop center region
            center_img = original.crop((crop_margin, crop_margin, 
                                      width - crop_margin, height - crop_margin))
            
            # Try decoding center region
            decoded_objects = decode(center_img)
            if decoded_objects:
                data = decoded_objects[0].data.decode('utf-8')
                if data.startswith("COMPRESSED:"):
                    data = self.decompress_payload(data)
                if self.verbose:
                    print(f"Successfully decoded QR code from center region")
                return data
            
            if self.verbose:
                print("No QR code found in image after trying all variants")
            
            return None
        except Exception as e:
            if self.verbose:
                print(f"Error decoding QR code: {e}")
            return None
    
    def parse_json_payload(self, payload):
        """
        Parse JSON payload with enhanced error handling.
        
        Args:
            payload: JSON payload string
            
        Returns:
            Parsed JSON object or None if parsing failed
        """
        if not payload:
            if self.verbose:
                print("Empty payload")
            return None
        
        try:
            # Try to parse JSON
            data = json.loads(payload)
            return data
        except json.JSONDecodeError as e:
            if self.verbose:
                print(f"Error parsing JSON payload: {e}")
            
            # Try to fix common JSON issues
            try:
                # Check if there are unescaped newlines in strings
                fixed_payload = payload.replace('\n', '\\n')
                data = json.loads(fixed_payload)
                if self.verbose:
                    print("Successfully parsed JSON after fixing newlines")
                return data
            except:
                pass
            
            return None
    
    def analyze_qr_sequence(self, input_dir):
        """
        Analyze QR code sequence from directory.
        
        Args:
            input_dir: Directory containing QR code images
            
        Returns:
            List of decoded payloads
        """
        # Get all PNG files in directory
        qr_files = sorted(glob.glob(os.path.join(input_dir, "*.png")))
        
        if self.verbose:
            print(f"Found {len(qr_files)} QR code files in {input_dir}")
        
        results = []
        
        for qr_file in qr_files:
            # Decode QR code
            payload = self.decode_qr_image(qr_file)
            
            if payload:
                # Parse JSON payload
                data = self.parse_json_payload(payload)
                
                if data:
                    results.append({
                        "file": qr_file,
                        "data": data
                    })
                else:
                    if self.verbose:
                        print(f"Failed to parse JSON payload from {qr_file}")
            else:
                if self.verbose:
                    print(f"Failed to decode QR code from {qr_file}")
        
        return results
    
    def generate_report(self, results):
        """
        Generate report from analysis results.
        
        Args:
            results: List of decoded payloads
            
        Returns:
            Report as dictionary
        """
        report = {
            "status": "success" if results else "error",
            "message": f"Decoded {len(results)} QR codes" if results else "No QR codes decoded",
            "frames_decoded": len(results),
            "frames": []
        }
        
        for result in results:
            data = result["data"]
            frame = {
                "file": os.path.basename(result["file"]),
            }
            
            # Extract frame data
            if "frame_id" in data:
                frame["frame_id"] = data["frame_id"]
            
            if "task_type" in data:
                frame["task_type"] = data["task_type"]
            
            if "code" in data:
                # Truncate code preview
                code = data["code"]
                if len(code) > 50:
                    preview = code[:50] + "..."
                else:
                    preview = code
                frame["code_preview"] = preview
            
            if "phi_state" in data:
                frame["phi_state"] = data["phi_state"]
            
            report["frames"].append(frame)
        
        return report
