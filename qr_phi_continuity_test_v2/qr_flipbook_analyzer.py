#!/usr/bin/env python3
"""
QR Flipbook Analyzer - Part of Animated QR Flipbook Execution System
By Vaughn Scott

Analyzes QR code sequences using pyzbar, extracting and decoding the payload data.
Supports encrypted payloads and tracks phi-harmonic evolution across frames.
"""

import os
import json
import base64
import hashlib
import argparse
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pyzbar.pyzbar import decode
from cryptography.fernet import Fernet
from datetime import datetime

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QRFlipbookAnalyzer:
    """
    Analyzes QR code sequences, extracting payload data and tracking evolution.
    """
    
    def __init__(self, sequence_dir="qr__simplesequence", encryption_key=None):
        """
        Initialize the QR Flipbook Analyzer.
        
        Args:
            sequence_dir: Directory containing QR code sequence images
            encryption_key: Optional Fernet encryption key for decrypting payloads
        """
        self.sequence_dir = sequence_dir
        self.frames = []
        self.session_data = {}
        self.phi_evolution = []
        
        # Initialize encryption if key provided
        self.encryption = None
        if encryption_key:
            self.encryption = Fernet(encryption_key)
        elif os.path.exists("qr_encryption.key"):
            with open("qr_encryption.key", "rb") as key_file:
                key = key_file.read()
                self.encryption = Fernet(key)
                print("Using encryption key from qr_encryption.key")
    
    def load_frames(self):
        """Load QR code frames from the sequence directory."""
        if not os.path.exists(self.sequence_dir):
            print(f"Error: Sequence directory '{self.sequence_dir}' not found.")
            return False
        
        # Get all PNG files in directory
        frame_files = sorted([f for f in os.listdir(self.sequence_dir) 
                             if f.startswith("frame_") and f.endswith(".png")])
        
        if not frame_files:
            print(f"Error: No QR frames found in '{self.sequence_dir}'.")
            return False
        
        self.frames = [os.path.join(self.sequence_dir, f) for f in frame_files]
        print(f"Loaded {len(self.frames)} QR frames from {self.sequence_dir}")
        return True
    
    def decode_frame(self, frame_path):
        """
        Decode a single QR frame.
        
        Args:
            frame_path: Path to QR frame image
            
        Returns:
            Decoded payload data as dictionary, or None if decoding failed
        """
        try:
            img = Image.open(frame_path)
            data = decode(img)
            
            if not data:
                print(f"Warning: No QR code found in {frame_path}")
                return None
            
            # Get the first QR code data
            text = data[0].data.decode('utf-8')
            
            # Check if encrypted
            if text.startswith("ENCRYPTED:"):
                if not self.encryption:
                    print(f"Warning: Encrypted payload in {frame_path} but no encryption key provided")
                    return None
                
                # Decrypt payload
                encrypted_data = base64.b64decode(text[len("ENCRYPTED:"):])
                text = self.encryption.decrypt(encrypted_data).decode()
            
            # Parse JSON payload
            payload = json.loads(text)
            return payload
            
        except Exception as e:
            print(f"Error decoding {frame_path}: {e}")
            return None
    
    def analyze_sequence(self):
        """
        Analyze the entire QR code sequence.
        
        Returns:
            Dictionary containing analysis results
        """
        if not self.frames:
            if not self.load_frames():
                return None
        
        print(f"Analyzing {len(self.frames)} QR frames...")
        
        frame_data = []
        phi_metadata = []
        sessions = {}
        hash_chain_valid = True
        prev_hash = None
        
        for i, frame_path in enumerate(self.frames):
            print(f"Decoding frame {i+1}/{len(self.frames)}: {os.path.basename(frame_path)}")
            payload = self.decode_frame(frame_path)
            
            if not payload:
                continue
                
            # Extract session info
            session_id = payload.get("session_id", "unknown")
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
            session["task_types"].add(payload.get("task_type", "unknown"))
            session["last_frame"] = i+1
            
            # Check hash chain
            if "prev_frame_hash" in payload:
                if prev_hash and payload["prev_frame_hash"] != prev_hash:
                    hash_chain_valid = False
                    print(f"Warning: Hash chain broken at frame {i+1}")
                
                # Calculate hash for this frame for next iteration
                frame_hash = hashlib.sha256(json.dumps(payload).encode()).hexdigest()
                prev_hash = frame_hash
            
            # Extract phi metadata
            if "phi_metadata" in payload:
                meta = payload["phi_metadata"]
                phi_metadata.append({
                    "frame": i+1,
                    "generation": meta.get("generation", 0),
                    "complexity": meta.get("complexity", 0),
                    "resonance": meta.get("resonance", 0),
                    "mutation_vector": meta.get("mutation_vector", [0, 0, 0])
                })
            
            # Store frame data
            frame_data.append({
                "frame_number": i+1,
                "original_frame": payload.get("frame_number", i+1),
                "session_id": session_id,
                "task_type": payload.get("task_type", "unknown"),
                "content_length": len(payload.get("content", "")),
                "valid_until": payload.get("valid_until", "unknown")
            })
        
        # Prepare analysis results
        analysis = {
            "total_frames": len(self.frames),
            "decoded_frames": len(frame_data),
            "sessions": sessions,
            "hash_chain_valid": hash_chain_valid,
            "phi_metadata": phi_metadata,
            "frame_data": frame_data
        }
        
        self.session_data = sessions
        self.phi_evolution = phi_metadata
        
        return analysis
    
    def visualize_phi_evolution(self):
        """
        Visualize the phi-harmonic evolution across frames.
        """
        if not self.phi_evolution:
            print("No phi-evolution data available. Run analyze_sequence first.")
            return
        
        # Extract data for plotting
        frames = [meta["frame"] for meta in self.phi_evolution]
        complexity = [meta["complexity"] for meta in self.phi_evolution]
        resonance = [meta["resonance"] for meta in self.phi_evolution]
        generations = [meta["generation"] for meta in self.phi_evolution]
        
        # Create figure with multiple subplots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
        
        # Plot complexity
        ax1.plot(frames, complexity, 'b-o', label='Complexity')
        ax1.set_xlabel('Frame Number')
        ax1.set_ylabel('Complexity')
        ax1.set_title('Phi-Harmonic Complexity Evolution')
        ax1.grid(True)
        ax1.legend()
        
        # Plot resonance
        ax2.plot(frames, resonance, 'r-o', label='Resonance')
        ax2.set_xlabel('Frame Number')
        ax2.set_ylabel('Resonance')
        ax2.set_title('Phi-Harmonic Resonance Evolution')
        ax2.grid(True)
        ax2.legend()
        
        # Plot generations
        ax3.plot(frames, generations, 'g-o', label='Generation')
        ax3.set_xlabel('Frame Number')
        ax3.set_ylabel('Generation')
        ax3.set_title('Evolution Generations')
        ax3.grid(True)
        ax3.legend()
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"phi_evolution_{timestamp}.png"
        plt.savefig(output_file)
        print(f"Phi evolution visualization saved to {output_file}")
        
        # Show plot
        plt.show()
    
    def print_sequence_summary(self, analysis):
        """
        Print a summary of the sequence analysis.
        
        Args:
            analysis: Analysis results from analyze_sequence
        """
        if not analysis:
            return
        
        print("\n" + "="*60)
        print("QR FLIPBOOK SEQUENCE ANALYSIS")
        print("="*60)
        
        print(f"\nTotal frames: {analysis['total_frames']}")
        print(f"Successfully decoded frames: {analysis['decoded_frames']}")
        print(f"Hash chain integrity: {'Valid' if analysis['hash_chain_valid'] else 'BROKEN'}")
        
        print("\nSESSIONS:")
        for session_id, session in analysis['sessions'].items():
            print(f"\n  Session ID: {session_id}")
            print(f"  Frames: {session['frame_count']} (from {session['first_frame']} to {session['last_frame']})")
            print(f"  Task types: {', '.join(session['task_types'])}")
        
        if analysis['phi_metadata']:
            print("\nPHI-HARMONIC EVOLUTION:")
            first_meta = analysis['phi_metadata'][0]
            last_meta = analysis['phi_metadata'][-1]
            
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
    try:
        # Initialize encryption if key provided
        encryption = None
        if encryption_key:
            encryption = Fernet(encryption_key)
        elif os.path.exists("qr_encryption.key"):
            with open("qr_encryption.key", "rb") as key_file:
                key = key_file.read()
                encryption = Fernet(key)
                print("Using encryption key from qr_encryption.key")
        
        # Open and decode image
        img = Image.open(image_path)
        data = decode(img)
        
        if not data:
            print(f"No QR code found in {image_path}")
            return
        
        # Process each QR code found in the image
        for i, obj in enumerate(data):
            print(f"\nQR Code #{i+1}:")
            text = obj.data.decode('utf-8')
            
            # Check if encrypted
            if text.startswith("ENCRYPTED:"):
                if not encryption:
                    print("  Encrypted payload detected but no encryption key provided")
                    print("  Raw data:", text[:100] + "..." if len(text) > 100 else text)
                    continue
                
                print("  Encrypted payload detected, decrypting...")
                encrypted_data = base64.b64decode(text[len("ENCRYPTED:"):])
                text = encryption.decrypt(encrypted_data).decode()
            
            # Try to parse as JSON
            try:
                parsed = json.loads(text)
                print("  JSON payload detected:")
                print(json.dumps(parsed, indent=4))
                
                # Extract phi metadata if present
                if "phi_metadata" in parsed:
                    print("\n  Phi-Harmonic Metadata:")
                    meta = parsed["phi_metadata"]
                    print(f"    Generation: {meta.get('generation', 'N/A')}")
                    print(f"    Complexity: {meta.get('complexity', 'N/A')}")
                    print(f"    Resonance: {meta.get('resonance', 'N/A')}")
                    
                    if "mutation_vector" in meta:
                        vector = meta["mutation_vector"]
                        print(f"    Mutation Vector: {vector}")
                        
                        # Calculate phi-resonance of vector
                        if len(vector) >= 3:
                            phi_product = vector[0] * vector[1] * vector[2]
                            resonance = 1.0 / (1.0 + abs((phi_product * PHI) % 1.0 - 0.5))
                            print(f"    Vector Phi-Resonance: {resonance:.6f}")
                
                # Check expiration
                if "valid_until" in parsed:
                    valid_until = parsed["valid_until"]
                    now = datetime.now().isoformat()
                    is_expired = valid_until < now
                    print(f"\n  Expiration: {valid_until}")
                    print(f"  Status: {'EXPIRED' if is_expired else 'VALID'}")
                
                # Show task content preview
                if "content" in parsed:
                    content = parsed["content"]
                    print("\n  Content Preview:")
                    if len(content) > 200:
                        print(f"    {content[:200]}...")
                    else:
                        print(f"    {content}")
                
            except json.JSONDecodeError:
                print("  Non-JSON payload:")
                if len(text) > 500:
                    print(f"    {text[:500]}...")
                else:
                    print(f"    {text}")
    
    except Exception as e:
        print(f"Error analyzing {image_path}: {e}")

def main():
    """Main function to run the QR Flipbook Analyzer."""
    parser = argparse.ArgumentParser(description="QR Flipbook Analyzer")
    parser.add_argument("--dir", help="Directory containing QR sequence")
    parser.add_argument("--image", help="Single QR image to analyze")
    parser.add_argument("--key", help="Path to encryption key file")
    parser.add_argument("--visualize", action="store_true", help="Visualize phi evolution")
    
    args = parser.parse_args()
    
    # Get encryption key if provided
    encryption_key = None
    if args.key and os.path.exists(args.key):
        with open(args.key, "rb") as key_file:
            encryption_key = key_file.read()
    
    # Analyze single image or sequence
    if args.image:
        print(f"Analyzing single QR code: {args.image}")
        analyze_single_qr(args.image, encryption_key)
    elif args.dir:
        # Create and run analyzer
        analyzer = QRFlipbookAnalyzer(sequence_dir=args.dir, encryption_key=encryption_key)
        analysis = analyzer.analyze_sequence()
        
        if analysis:
            analyzer.print_sequence_summary(analysis)
            
            if args.visualize:
                analyzer.visualize_phi_evolution()
    else:
        print("Error: Either --dir or --image must be specified")
        parser.print_help()

if __name__ == "__main__":
    print("QR Flipbook Analyzer - By Vaughn Scott")
    main()
