#!/usr/bin/env python3
"""
QR Sequence Generator Script - Part of Animated QR Flipbook DNA System
By Vaughn Scott

A dedicated script to generate QR sequences from the genome using the robust QR generator.
Uses phi-harmonic principles for optimal QR code generation.
"""

import os
import sys
import json
import math
import argparse
from datetime import datetime

# Import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qr_robust_generator import QRRobustGenerator

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

def load_genome(genome_file):
    """
    Load the genome from file.
    
    Args:
        genome_file: Path to genome file
        
    Returns:
        Loaded genome data
    """
    try:
        with open(genome_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading genome: {e}")
        return None

def extract_frames_from_genome(genome):
    """
    Extract frames from genome data.
    
    Args:
        genome: Genome data
        
    Returns:
        List of frames
    """
    frames = []
    
    # Check if genome is a dictionary
    if isinstance(genome, dict):
        # Check for groups structure
        if "groups" in genome:
            for group in genome["groups"]:
                if "codons" in group:
                    for codon in group["codons"]:
                        frames.append(codon)
        # Check for frames structure
        elif "frames" in genome:
            frames = genome["frames"]
        # Check for codons structure
        elif "codons" in genome:
            frames = genome["codons"]
    
    return frames

def generate_qr_sequence(genome_file, output_dir, max_version=25, verbose=False):
    """
    Generate QR sequence from genome file.
    
    Args:
        genome_file: Path to genome file
        output_dir: Directory to save generated QR code frames
        max_version: Maximum QR code version to use (1-40)
        verbose: Enable verbose output
        
    Returns:
        List of paths to generated QR images
    """
    # Load genome
    genome = load_genome(genome_file)
    if not genome:
        return []
    
    # Extract frames
    frames = extract_frames_from_genome(genome)
    if not frames:
        print(f"No frames found in genome")
        return []
    
    if verbose:
        print(f"Found {len(frames)} frames in genome")
    
    # Create QR generator
    generator = QRRobustGenerator(output_dir=output_dir, max_version=max_version)
    
    # Generate QR codes
    paths = []
    for i, frame in enumerate(frames):
        frame_number = i + 1
        
        if verbose:
            print(f"Generating QR code for frame {frame_number}...")
        
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
        path = generator.generate_frame(json_payload, frame_number, phi_state=phi_state)
        
        if isinstance(path, list):
            paths.extend(path)
            if verbose:
                print(f"  Generated {len(path)} chunked QR codes")
        else:
            paths.append(path)
            if verbose:
                print(f"  Generated QR code: {os.path.basename(path)}")
    
    if verbose:
        print(f"Generated {len(paths)} QR code files")
    
    return paths

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="QR Sequence Generator")
    parser.add_argument("--genome-file", default="qr_genome.json", help="Path to genome file")
    parser.add_argument("--output-dir", default="qr_sequence", help="Directory to save generated QR code frames")
    parser.add_argument("--max-version", type=int, default=25, help="Maximum QR code version to use (1-40)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    # Generate QR sequence
    start_time = datetime.now()
    paths = generate_qr_sequence(
        args.genome_file,
        args.output_dir,
        args.max_version,
        args.verbose
    )
    
    # Print summary
    duration = (datetime.now() - start_time).total_seconds()
    print(f"QR sequence generation completed in {duration:.2f} seconds")
    print(f"Generated {len(paths)} QR code files in {args.output_dir}")

if __name__ == "__main__":
    main()
