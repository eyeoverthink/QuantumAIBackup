#!/usr/bin/env python3
"""
Simple QR Sequence Analyzer - Part of Animated QR Flipbook DNA System
By Vaughn Scott

A simplified QR sequence analyzer that uses the working pyzbar decoder.
"""

import os
import sys
import json
import base64
import zlib
import io
import glob
from PIL import Image
from pyzbar.pyzbar import decode

class QRSimpleAnalyzer:
    """
    Simple QR code analyzer for QR Flipbook DNA System.
    """
    
    def __init__(self, verbose=False):
        """
        Initialize the QR analyzer.
        
        Args:
            verbose: Whether to print verbose output
        """
        self.verbose = verbose
    
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
            compressed = base64.b64decode(encoded)
            decompressed = zlib.decompress(compressed)
            return decompressed.decode('utf-8')
        return payload
    
    def decode_qr_data(self, image_data):
        """
        Decode QR code from in-memory image data.

        Args:
            image_data: Bytes of the QR code image

        Returns:
            Decoded payload or None if decoding failed
        """
        if self.verbose:
            print(f"Decoding QR image from data...")

        try:
            # Open image from byte stream
            image = Image.open(io.BytesIO(image_data))

            # Try decoding with pyzbar
            decoded_objects = decode(image)

            # Return decoded data if found
            if decoded_objects:
                data = decoded_objects[0].data.decode('utf-8')

                # Check if payload is compressed
                if data.startswith("COMPRESSED:"):
                    if self.verbose:
                        print("Detected compressed payload, decompressing...")
                    data = self.decompress_payload(data)

                if self.verbose:
                    print(f"Successfully decoded QR code from data")

                return data

            if self.verbose:
                print("No QR code found in image data")

            return None
        except Exception as e:
            if self.verbose:
                print(f"Error decoding QR code from data: {e}")
            return None

    def decode_qr_image(self, image_path):
        """
        Decode QR code from image.
        
        Args:
            image_path: Path to QR code image
            
        Returns:
            Decoded payload or None if decoding failed
        """
        if self.verbose:
            print(f"Decoding QR image: {image_path}")
        
        try:
            with open(image_path, 'rb') as f:
                image_data = f.read()
            return self.decode_qr_data(image_data)
        except FileNotFoundError:
            if self.verbose:
                print(f"Error: Image file not found at {image_path}")
            return None
        except Exception as e:
            if self.verbose:
                print(f"Error reading QR code image file: {e}")
            return None
    
    def parse_json_payload(self, payload):
        """
        Parse JSON payload.
        
        Args:
            payload: JSON payload string
            
        Returns:
            Parsed JSON object or None if parsing failed
        """
        try:
            return json.loads(payload)
        except json.JSONDecodeError as e:
            if self.verbose:
                print(f"Error parsing JSON payload: {e}")
            return None
    
    def analyze_qr_sequence(self, input_dir):
        """
        Analyze QR code sequence from directory.
        
        Args:
            input_dir: Directory containing QR code images
            
        Returns:
            List of decoded payloads
        """
        if self.verbose:
            print(f"Analyzing QR sequence in directory: {input_dir}")
        
        # Get all QR files
        qr_files = sorted(glob.glob(os.path.join(input_dir, "qr_frame_*.png")))
        
        if not qr_files:
            if self.verbose:
                print("No QR code files found!")
            return []
        
        if self.verbose:
            print(f"Found {len(qr_files)} QR code files")
        
        # Process each QR file
        results = []
        for qr_file in qr_files:
            if self.verbose:
                print(f"\nProcessing QR file: {qr_file}")
            
            # Decode QR code
            payload = self.decode_qr_image(qr_file)
            
            if payload:
                # Parse JSON payload
                json_data = self.parse_json_payload(payload)
                
                if json_data:
                    results.append(json_data)
                    
                    if self.verbose:
                        print(f"Decoded payload: {json_data}")
                else:
                    if self.verbose:
                        print("Failed to parse JSON payload")
                    # Add raw payload as string
                    results.append({"raw_payload": payload})
            else:
                if self.verbose:
                    print("Failed to decode QR code")
        
        return results
    
    def generate_report(self, results):
        """
        Generate report from analysis results.
        
        Args:
            results: List of decoded payloads
            
        Returns:
            Report as dictionary
        """
        if not results:
            return {
                "status": "error",
                "message": "No QR codes decoded",
                "frames_decoded": 0,
                "frames": []
            }
        
        # Count frames
        frames_decoded = len(results)
        
        # Extract frame data
        frames = []
        for i, result in enumerate(results):
            frame_data = {
                "frame_number": i + 1,
                "frame_id": result.get("frame_id", str(i + 1)),
                "task_type": result.get("task_type", "unknown"),
            }
            
            # Add code if available
            if "code" in result:
                frame_data["code_length"] = len(result["code"])
                frame_data["code_preview"] = result["code"][:50] + "..." if len(result["code"]) > 50 else result["code"]
            
            # Add phi state if available
            if "phi_state" in result and result["phi_state"]:
                frame_data["phi_state"] = result["phi_state"]
            
            frames.append(frame_data)
        
        # Generate report
        report = {
            "status": "success",
            "message": f"Successfully decoded {frames_decoded} QR code frames",
            "frames_decoded": frames_decoded,
            "frames": frames
        }
        
        return report
