#!/usr/bin/env python3
"""
Simple QR Sequence Generator - Part of Animated QR Flipbook DNA System
By Vaughn Scott

A simplified QR sequence generator that uses the working pyzbar decoder.
"""

import os
import sys
import json
import math
import base64
import zlib
import uuid
from datetime import datetime
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRSimpleGenerator:
    """
    Simple QR code generator for QR Flipbook DNA System.
    """
    
    def __init__(self, output_dir="qr_simple_sequence", max_version=25):
        """
        Initialize the QR generator.
        
        Args:
            output_dir: Directory to save generated QR code frames
            max_version: Maximum QR code version to use (1-40)
        """
        self.output_dir = output_dir
        self.max_version = max_version
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def compress_payload(self, payload):
        """
        Compress payload using zlib and base64 encode.
        
        Args:
            payload: String payload to compress
            
        Returns:
            Compressed payload with marker
        """
        compressed = zlib.compress(payload.encode('utf-8'))
        encoded = base64.b64encode(compressed).decode('utf-8')
        return f"COMPRESSED:{encoded}"
    
    def generate_frame(self, payload, frame_number, phi_state=None):
        """
        Generate a QR code frame for the given payload.
        
        Args:
            payload: String payload to encode in QR code
            frame_number: Frame number
            phi_state: Optional phi state metadata
            
        Returns:
            Path to generated QR image
        """
        # Determine if payload needs compression
        if len(payload) > 500:
            payload = self.compress_payload(payload)
        
        # Create QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(payload)
        
        # Make QR code with fit=True to find optimal version
        try:
            qr.make(fit=True)
        except qrcode.exceptions.DataOverflowError:
            print(f"Warning: Payload too large for QR code, using max version {self.max_version}")
            qr = qrcode.QRCode(
                version=self.max_version,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(payload)
            qr.make(fit=True)
        
        # Create image
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Add visual indicators
        img = qr_img.convert("RGBA")
        draw = ImageDraw.Draw(img)
        
        # Add frame number
        draw.text((10, 10), f"{frame_number:03d}", fill=(0, 0, 255, 255))
        
        # Add phi resonance indicator if provided
        if phi_state and "resonance" in phi_state:
            resonance = phi_state["resonance"]
            # Use resonance to determine color intensity
            color_intensity = int(min(255, resonance * 100))
            corner_size = 20
            draw.rectangle(
                [(img.width - corner_size, 0), (img.width, corner_size)],
                fill=(0, color_intensity, 0, 255)
            )
        
        # Save image
        filename = f"qr_frame_{frame_number:03d}.png"
        filepath = os.path.join(self.output_dir, filename)
        img.save(filepath)
        
        return filepath
    
    def generate_from_genome(self, genome_data, output_dir=None):
        """
        Generate QR sequence from genome data.
        
        Args:
            genome_data: Genome data to encode in QR sequence
            output_dir: Optional output directory override
            
        Returns:
            List of paths to generated QR images
        """
        if output_dir:
            self.output_dir = output_dir
            os.makedirs(output_dir, exist_ok=True)
        
        # Extract frames from genome
        frames = []
        
        # Check if genome is a dictionary
        if isinstance(genome_data, dict):
            # Check for groups structure
            if "groups" in genome_data:
                for group in genome_data["groups"]:
                    if "codons" in group:
                        for codon in group["codons"]:
                            frames.append(codon)
            # Check for frames structure
            elif "frames" in genome_data:
                frames = genome_data["frames"]
            # Check for codons structure
            elif "codons" in genome_data:
                frames = genome_data["codons"]
        
        # Generate QR codes for each frame
        qr_paths = []
        for i, frame in enumerate(frames):
            frame_number = i + 1
            
            # Extract code from frame
            code = ""
            task_type = "execute_python"
            phi_state = None
            
            # Handle different frame structures
            if isinstance(frame, dict):
                # Extract frame data
                if "frame_data" in frame:
                    frame_data = frame["frame_data"]
                    task_type = frame_data.get("task_type", "execute_python")
                    task_data = frame_data.get("task_data", {})
                    
                    if isinstance(task_data, dict):
                        code = task_data.get("code", "")
                    else:
                        code = str(task_data)
                elif "task_data" in frame:
                    task_data = frame["task_data"]
                    
                    if isinstance(task_data, dict):
                        code = task_data.get("code", "")
                    else:
                        code = str(task_data)
                    
                    task_type = frame.get("task_type", "execute_python")
                
                # Extract phi state
                if "phi_state" in frame:
                    phi_state = frame["phi_state"]
            
            # Create payload
            payload = {
                "code": code,
                "task_type": task_type,
                "frame_id": str(frame_number),
                "phi_state": phi_state
            }
            
            # Convert payload to JSON
            json_payload = json.dumps(payload)
            
            # Generate QR code frame
            path = self.generate_frame(json_payload, frame_number, phi_state=phi_state)
            qr_paths.append(path)
        
        return qr_paths
