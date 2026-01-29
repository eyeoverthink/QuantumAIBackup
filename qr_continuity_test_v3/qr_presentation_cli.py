#!/usr/bin/env python3
"""
QR Presentation CLI - Command-line interface for QR code presentations
By Vaughn Scott

This script allows you to:
1. Create QR codes from Python files
2. Organize them into a presentation sequence
3. Save QR codes for later scanning and execution

Uses the phi-harmonic principles and existing QR task worker.
"""

import os
import sys
import json
import time
import uuid
import qrcode
import numpy as np
import argparse
import zlib
import base64

# Phi (Golden Ratio) constant for phi-harmonic timing
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QRPresentationCLI:
    """Build QR code presentations from the command line."""
    
    def __init__(self):
        """Initialize the presentation builder."""
        self.presentation_slides = []
        self.presentation_name = "Quantum_Phi_Presentation"
        self.output_dir = "qr_presentation_slides"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def compress_payload(self, payload):
        """Compress the payload using zlib and base64 encode it."""
        compressed = zlib.compress(payload.encode('utf-8'), 9)  # Max compression
        encoded = base64.b64encode(compressed).decode('utf-8')
        return f"COMPRESSED:{encoded}"
    
    def create_qr_from_file(self, file_path, slide_title=None):
        """Create a QR code from a Python file."""
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} not found.")
            return None
        
        # Read the file
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Create a unique task ID
        task_id = str(uuid.uuid4())
        
        # Get the filename without path
        filename = os.path.basename(file_path)
        
        # Use the filename as slide title if none provided
        if not slide_title:
            slide_title = os.path.splitext(filename)[0]
        
        # Calculate phi-harmonic timing
        phi_time = (time.time() * PHI) % 1.0
        
        # Create task payload
        task_payload = {
            "task_id": task_id,
            "timestamp": time.time(),
            "script": content,
            "input_data": {
                "filename": filename,
                "phi_time": phi_time
            },
            "task_meta": {
                "type": "QR Presentation Slide",
                "title": slide_title,
                "phi_harmonic": phi_time,
                "visual_inversion": False,
                "intensity_profile": {
                    "resonance": 1.0 / (1.0 + abs(phi_time - 0.5)),
                    "complexity": 0.5 + 0.5 * phi_time
                }
            }
        }
        
        # Convert to JSON
        json_payload = json.dumps(task_payload)
        
        # Compress the payload
        compressed_payload = self.compress_payload(json_payload)
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=None,  # Auto-determine version
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(compressed_payload)
        qr.make(fit=True)
        
        # Create QR image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Create slide data
        slide_data = {
            "task_id": task_id,
            "title": slide_title,
            "filename": filename,
            "content": content,
            "phi_time": phi_time,
            "qr_image": img
        }
        
        return slide_data
    
    def add_slide(self, file_path, slide_title=None):
        """Add a slide to the presentation."""
        slide_data = self.create_qr_from_file(file_path, slide_title)
        if slide_data:
            self.presentation_slides.append(slide_data)
            print(f"Added slide: {slide_data['title']}")
            return True
        return False
    
    def save_slide(self, slide_data, index):
        """Save a slide as a QR code image."""
        slide_number = str(index + 1).zfill(3)
        output_path = os.path.join(self.output_dir, f"slide_{slide_number}_{slide_data['title']}.png")
        
        slide_data["qr_image"].save(output_path)
        print(f"Saved slide to {output_path}")
        return output_path
    
    def save_presentation(self):
        """Save all slides in the presentation."""
        if not self.presentation_slides:
            print("No slides in presentation.")
            return
        
        # Create presentation directory
        presentation_dir = os.path.join(self.output_dir, self.presentation_name)
        if not os.path.exists(presentation_dir):
            os.makedirs(presentation_dir)
        
        # Save each slide
        saved_paths = []
        for i, slide in enumerate(self.presentation_slides):
            slide_number = str(i + 1).zfill(3)
            output_path = os.path.join(presentation_dir, f"slide_{slide_number}_{slide['title']}.png")
            slide["qr_image"].save(output_path)
            saved_paths.append(output_path)
        
        # Create presentation metadata
        metadata = {
            "name": self.presentation_name,
            "created": time.time(),
            "phi_harmonic": (time.time() * PHI) % 1.0,
            "slides": [
                {
                    "number": i + 1,
                    "title": slide["title"],
                    "task_id": slide["task_id"],
                    "filename": slide["filename"],
                    "phi_time": slide["phi_time"]
                }
                for i, slide in enumerate(self.presentation_slides)
            ]
        }
        
        # Save metadata
        metadata_path = os.path.join(presentation_dir, "presentation_metadata.json")
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"Saved presentation '{self.presentation_name}' with {len(saved_paths)} slides to {presentation_dir}")
        return presentation_dir
    
    def create_single_qr(self, file_path, title=None):
        """Create a single QR code from a Python file."""
        slide_data = self.create_qr_from_file(file_path, title)
        if slide_data:
            output_path = os.path.join(self.output_dir, f"{slide_data['title']}.png")
            slide_data["qr_image"].save(output_path)
            print(f"Created QR code for {file_path}")
            print(f"Saved to {output_path}")
            return output_path
        return None
    
    def create_presentation(self, file_paths, titles=None):
        """Create a presentation from multiple Python files."""
        if titles and len(titles) != len(file_paths):
            print("Error: Number of titles must match number of files.")
            return
        
        for i, file_path in enumerate(file_paths):
            title = titles[i] if titles and i < len(titles) else None
            self.add_slide(file_path, title)
        
        if self.presentation_slides:
            return self.save_presentation()
        return None

def main():
    """Main function to run the QR presentation CLI."""
    parser = argparse.ArgumentParser(description="Create QR code presentations from Python files.")
    parser.add_argument("--file", help="Python file to encode as a QR code")
    parser.add_argument("--title", help="Title for the slide")
    parser.add_argument("--name", help="Name for the presentation")
    parser.add_argument("--files", nargs="+", help="Multiple Python files to encode as a presentation")
    parser.add_argument("--titles", nargs="+", help="Titles for multiple slides")
    args = parser.parse_args()
    
    cli = QRPresentationCLI()
    
    if args.name:
        cli.presentation_name = args.name
    
    if args.file:
        cli.create_single_qr(args.file, args.title)
    elif args.files:
        cli.create_presentation(args.files, args.titles)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
