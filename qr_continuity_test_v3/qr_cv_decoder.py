#!/usr/bin/env python3
"""
QR CV Decoder - Simple OpenCV-based QR Code Decoder
By Vaughn Scott

Uses OpenCV's QR code detector to read QR codes from images.
Supports decoding encrypted payloads and analyzing phi-harmonic metadata.
"""

import os
import cv2
import json
import base64
import argparse
from cryptography.fernet import Fernet
from datetime import datetime

class QRCVDecoder:
    """
    OpenCV-based QR code decoder with support for encrypted payloads.
    """
    
    def __init__(self, encryption_key=None):
        """
        Initialize the QR CV Decoder.
        
        Args:
            encryption_key: Optional Fernet encryption key for decrypting payloads
        """
        # Initialize QR detector
        self.qr_detector = cv2.QRCodeDetector()
        
        # Initialize encryption if key provided
        self.encryption = None
        if encryption_key:
            self.encryption = Fernet(encryption_key)
        elif os.path.exists("qr_encryption.key"):
            with open("qr_encryption.key", "rb") as key_file:
                key = key_file.read()
                self.encryption = Fernet(key)
                print("Using encryption key from qr_encryption.key")
    
    def decode_image(self, image_path):
        """
        Decode QR code from image.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Decoded data or None if no QR code found
        """
        # Read image
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Could not read image {image_path}")
            return None
        
        # Detect and decode QR code
        retval, decoded_info, points, straight_qrcode = self.qr_detector.detectAndDecodeMulti(img)
        
        if not retval:
            print(f"No QR code found in {image_path}")
            return None
        
        # Process each decoded QR code
        results = []
        for i, text in enumerate(decoded_info):
            if not text:
                continue
                
            # Check if encrypted
            if text.startswith("ENCRYPTED:"):
                if not self.encryption:
                    print(f"Encrypted payload detected but no encryption key provided")
                    results.append({"raw": text[:100] + "..." if len(text) > 100 else text})
                    continue
                
                print(f"Encrypted payload detected, decrypting...")
                try:
                    encrypted_data = base64.b64decode(text[len("ENCRYPTED:"):])
                    text = self.encryption.decrypt(encrypted_data).decode()
                except Exception as e:
                    print(f"Error decrypting payload: {e}")
                    results.append({"raw": text[:100] + "..." if len(text) > 100 else text})
                    continue
            
            # Try to parse as JSON
            try:
                parsed = json.loads(text)
                results.append(parsed)
            except json.JSONDecodeError:
                results.append({"raw": text[:100] + "..." if len(text) > 100 else text})
        
        return results
    
    def analyze_directory(self, directory_path):
        """
        Analyze all images in a directory.
        
        Args:
            directory_path: Path to directory containing images
            
        Returns:
            Analysis results
        """
        if not os.path.exists(directory_path):
            print(f"Error: Directory {directory_path} not found")
            return None
        
        # Get all PNG files in directory
        image_files = sorted([f for f in os.listdir(directory_path) 
                             if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        
        if not image_files:
            print(f"No image files found in {directory_path}")
            return None
        
        print(f"Analyzing {len(image_files)} images in {directory_path}...")
        
        results = []
        sessions = {}
        phi_evolution = []
        
        for i, filename in enumerate(image_files):
            image_path = os.path.join(directory_path, filename)
            print(f"Decoding image {i+1}/{len(image_files)}: {filename}")
            
            decoded = self.decode_image(image_path)
            if not decoded:
                continue
            
            # Process decoded data
            for data in decoded:
                # Skip raw data
                if "raw" in data:
                    continue
                
                # Extract session info
                session_id = data.get("session_id", "unknown")
                if session_id not in sessions:
                    sessions[session_id] = {
                        "frame_count": 0,
                        "task_types": set(),
                        "first_frame": i+1,
                        "last_frame": i+1
                    }
                
                # Update session info
                session = sessions[session_id]
                session["frame_count"] += 1
                session["task_types"].add(data.get("task_type", "unknown"))
                session["last_frame"] = i+1
                
                # Extract phi metadata
                if "phi_metadata" in data:
                    meta = data["phi_metadata"]
                    phi_evolution.append({
                        "frame": i+1,
                        "generation": meta.get("generation", 0),
                        "complexity": meta.get("complexity", 0),
                        "resonance": meta.get("resonance", 0),
                        "mutation_vector": meta.get("mutation_vector", [0, 0, 0])
                    })
                
                # Store frame data
                results.append({
                    "filename": filename,
                    "frame_number": i+1,
                    "original_frame": data.get("frame_number", i+1),
                    "session_id": session_id,
                    "task_type": data.get("task_type", "unknown"),
                    "content_length": len(data.get("content", "")),
                    "valid_until": data.get("valid_until", "unknown")
                })
        
        # Prepare analysis results
        analysis = {
            "total_images": len(image_files),
            "decoded_frames": len(results),
            "sessions": sessions,
            "phi_evolution": phi_evolution,
            "frame_data": results
        }
        
        return analysis
    
    def print_analysis_summary(self, analysis):
        """
        Print a summary of the analysis results.
        
        Args:
            analysis: Analysis results
        """
        if not analysis:
            return
        
        print("\n" + "="*60)
        print("QR CODE ANALYSIS SUMMARY")
        print("="*60)
        
        print(f"\nTotal images: {analysis['total_images']}")
        print(f"Successfully decoded frames: {analysis['decoded_frames']}")
        
        print("\nSESSIONS:")
        for session_id, session in analysis['sessions'].items():
            print(f"\n  Session ID: {session_id}")
            print(f"  Frames: {session['frame_count']} (from {session['first_frame']} to {session['last_frame']})")
            print(f"  Task types: {', '.join(session['task_types'])}")
        
        if analysis['phi_evolution']:
            print("\nPHI-HARMONIC EVOLUTION:")
            first_meta = analysis['phi_evolution'][0]
            last_meta = analysis['phi_evolution'][-1]
            
            print(f"  Starting generation: {first_meta['generation']}")
            print(f"  Final generation: {last_meta['generation']}")
            print(f"  Starting complexity: {first_meta['complexity']:.6f}")
            print(f"  Final complexity: {last_meta['complexity']:.6f}")
            print(f"  Starting resonance: {first_meta['resonance']:.6f}")
            print(f"  Final resonance: {last_meta['resonance']:.6f}")
        
        print("\nFRAME CONTENT SUMMARY:")
        task_types = {}
        for frame in analysis['frame_data']:
            task_type = frame['task_type']
            if task_type not in task_types:
                task_types[task_type] = 0
            task_types[task_type] += 1
        
        for task_type, count in task_types.items():
            print(f"  {task_type}: {count} frames")
        
        print("\nEXPIRATION ANALYSIS:")
        now = datetime.now().isoformat()
        expired = sum(1 for frame in analysis['frame_data'] if frame['valid_until'] != "unknown" and frame['valid_until'] < now)
        valid = sum(1 for frame in analysis['frame_data'] if frame['valid_until'] != "unknown" and frame['valid_until'] >= now)
        unknown = sum(1 for frame in analysis['frame_data'] if frame['valid_until'] == "unknown")
        
        print(f"  Valid frames: {valid}")
        print(f"  Expired frames: {expired}")
        print(f"  Unknown expiration: {unknown}")
        
        print("\n" + "="*60)

def analyze_single_qr(image_path, encryption_key=None):
    """
    Analyze a single QR code image.
    
    Args:
        image_path: Path to QR code image
        encryption_key: Optional encryption key for decrypting payload
    """
    decoder = QRCVDecoder(encryption_key)
    decoded = decoder.decode_image(image_path)
    
    if not decoded:
        return
    
    print("\n" + "="*60)
    print(f"QR CODE ANALYSIS: {os.path.basename(image_path)}")
    print("="*60)
    
    for i, data in enumerate(decoded):
        print(f"\nQR Code #{i+1}:")
        
        if "raw" in data:
            print(f"  Raw data: {data['raw']}")
            continue
        
        print(f"  Session ID: {data.get('session_id', 'N/A')}")
        print(f"  Frame: {data.get('frame_number', 'N/A')}/{data.get('frame_total', 'N/A')}")
        print(f"  Task type: {data.get('task_type', 'N/A')}")
        
        # Extract phi metadata if present
        if "phi_metadata" in data:
            print("\n  Phi-Harmonic Metadata:")
            meta = data["phi_metadata"]
            print(f"    Generation: {meta.get('generation', 'N/A')}")
            print(f"    Complexity: {meta.get('complexity', 'N/A')}")
            print(f"    Resonance: {meta.get('resonance', 'N/A')}")
            
            if "mutation_vector" in meta:
                vector = meta["mutation_vector"]
                print(f"    Mutation Vector: {vector}")
        
        # Check expiration
        if "valid_until" in data:
            valid_until = data["valid_until"]
            now = datetime.now().isoformat()
            is_expired = valid_until < now
            print(f"\n  Expiration: {valid_until}")
            print(f"  Status: {'EXPIRED' if is_expired else 'VALID'}")
        
        # Show task content preview
        if "content" in data:
            content = data["content"]
            print("\n  Content Preview:")
            if len(content) > 200:
                print(f"    {content[:200]}...")
            else:
                print(f"    {content}")
    
    print("\n" + "="*60)

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="QR CV Decoder")
    parser.add_argument("--image", help="Path to single QR code image")
    parser.add_argument("--dir", help="Path to directory containing QR code images")
    parser.add_argument("--key", help="Path to encryption key file")
    
    args = parser.parse_args()
    
    # Get encryption key if provided
    encryption_key = None
    if args.key and os.path.exists(args.key):
        with open(args.key, "rb") as key_file:
            encryption_key = key_file.read()
    
    if args.image:
        analyze_single_qr(args.image, encryption_key)
    elif args.dir:
        decoder = QRCVDecoder(encryption_key)
        analysis = decoder.analyze_directory(args.dir)
        if analysis:
            decoder.print_analysis_summary(analysis)
    else:
        print("Error: Either --image or --dir must be specified")
        parser.print_help()

if __name__ == "__main__":
    print("QR CV Decoder - By Vaughn Scott")
    main()
