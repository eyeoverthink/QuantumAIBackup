#!/usr/bin/env python3
"""
QR Robust Analyzer - Part of Animated QR Flipbook DNA System
By Vaughn Scott

A robust QR code analyzer that ensures reliable decoding and verification.
Uses phi-harmonic principles for optimal QR code analysis.
"""

import os
import sys
import json
import math
import base64
import zlib
import glob
from datetime import datetime
from PIL import Image, ImageOps
from pyzbar.pyzbar import decode

# Import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qr_robust_generator import QRRobustGenerator

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRRobustAnalyzer:
    """
    A robust QR code analyzer that ensures reliable decoding and verification.
    """
    
    def __init__(self, input_dir="qr_genome_sequence", verbose=False):
        """
        Initialize the QR Robust Analyzer.
        
        Args:
            input_dir: Directory containing QR code frames
            verbose: Enable verbose output
        """
        self.input_dir = input_dir
        self.verbose = verbose
        self.generator = QRRobustGenerator(output_dir=input_dir)
    
    def decompress_data(self, compressed_data):
        """
        Decompress data that was compressed with QRRobustGenerator.compress_data.
        
        Args:
            compressed_data: Base64-encoded compressed data
            
        Returns:
            Original data as string
        """
        return self.generator.decompress_data(compressed_data)
    
    def decode_qr_image(self, image_path):
        """
        Decode QR code from image.
        
        Args:
            image_path: Path to QR code image
            
        Returns:
            Decoded data or None if decoding failed
        """
        try:
            if self.verbose:
                print(f"  Attempting to decode {os.path.basename(image_path)}")
                
            # Open image
            image = Image.open(image_path)
            
            # Convert RGBA to RGB if needed
            if image.mode == 'RGBA':
                if self.verbose:
                    print("  Converting RGBA image to RGB")
                rgb_image = Image.new('RGB', image.size, (255, 255, 255))
                rgb_image.paste(image, mask=image.split()[3])  # 3 is the alpha channel
                image = rgb_image
            
            # Try different approaches to improve decoding success
            # First try with original image
            decoded_objects = decode(image)
            
            # If failed, try with resized image
            if not decoded_objects:
                if self.verbose:
                    print("  Trying with resized image...")
                resized_image = image.resize((800, 800))
                decoded_objects = decode(resized_image)
            
            # If failed, try with enhanced contrast
            if not decoded_objects:
                if self.verbose:
                    print("  Trying with enhanced contrast...")
                try:
                    enhanced_image = ImageOps.autocontrast(image)
                    decoded_objects = decode(enhanced_image)
                except Exception as e:
                    if self.verbose:
                        print(f"  Error enhancing contrast: {e}")
                    # Continue with next approach
            
            # Return decoded data if found
            if decoded_objects:
                if self.verbose:
                    print(f"  Successfully decoded QR code")
                return decoded_objects[0].data.decode('utf-8')
            
            if self.verbose:
                print(f"  No QR code found in image")
            return None
        except Exception as e:
            if self.verbose:
                print(f"  Error decoding QR code: {e}")
            return None
    
    def get_frame_info(self, filename):
        """
        Extract frame information from filename.
        
        Args:
            filename: QR code filename
            
        Returns:
            Dictionary with frame_number, chunk_id, and total_chunks
        """
        try:
            # Extract frame number
            if filename.startswith("qr_frame_"):
                # Remove "qr_frame_" prefix
                parts = filename[9:].split("_")
                frame_number = int(parts[0].split(".")[0])
                
                # Check if chunked
                if len(parts) > 1:
                    # Extract chunk info
                    chunk_parts = parts[1].split(".")
                    chunk_info = chunk_parts[0].split("/")
                    chunk_id = int(chunk_info[0])
                    total_chunks = int(chunk_info[1])
                    
                    return {
                        "frame_number": frame_number,
                        "chunk_id": chunk_id,
                        "total_chunks": total_chunks,
                        "is_chunked": True
                    }
                else:
                    # Not chunked
                    return {
                        "frame_number": frame_number,
                        "chunk_id": 1,
                        "total_chunks": 1,
                        "is_chunked": False
                    }
            
            return None
        except Exception as e:
            if self.verbose:
                print(f"Error extracting frame info from {filename}: {e}")
            return None
    
    def analyze_qr_sequence(self):
        """
        Analyze all QR codes in the input directory.
        
        Returns:
            Analysis results
        """
        # Get all QR files
        qr_files = glob.glob(os.path.join(self.input_dir, "qr_frame_*.png"))
        
        if self.verbose:
            print(f"Found {len(qr_files)} QR code files in {self.input_dir}")
        
        if not qr_files:
            print(f"No QR code files found in {self.input_dir}")
            return {
                "success": False,
                "error": "No QR code files found"
            }
        
        # Group by frame number
        frames = {}
        for file_path in qr_files:
            filename = os.path.basename(file_path)
            if self.verbose:
                print(f"Processing file: {filename}")
                
            frame_info = self.get_frame_info(filename)
            
            if frame_info:
                frame_number = frame_info["frame_number"]
                
                if frame_number not in frames:
                    frames[frame_number] = {
                        "files": [],
                        "chunks": {},
                        "is_chunked": frame_info["is_chunked"],
                        "total_chunks": frame_info["total_chunks"],
                        "decoded": False,
                        "payload": None
                    }
                
                frames[frame_number]["files"].append(file_path)
                
                if frame_info["is_chunked"]:
                    frames[frame_number]["is_chunked"] = True
                    frames[frame_number]["total_chunks"] = max(
                        frames[frame_number]["total_chunks"],
                        frame_info["total_chunks"]
                    )
            else:
                if self.verbose:
                    print(f"  Could not extract frame info from {filename}")
        
        # Process each frame
        results = {
            "total_frames": len(frames),
            "decoded_frames": 0,
            "frames": {}
        }
        
        for frame_number, frame_data in frames.items():
            if self.verbose:
                print(f"Analyzing frame {frame_number}...")
            
            # Sort files to ensure correct order
            frame_data["files"] = sorted(frame_data["files"])
            
            # Process each file
            for file_path in frame_data["files"]:
                # Decode QR code
                decoded_data = self.decode_qr_image(file_path)
                
                if decoded_data:
                    if self.verbose:
                        print(f"  Successfully decoded {os.path.basename(file_path)}")
                        print(f"  Data preview: {decoded_data[:50]}...")
                    
                    # Get frame info
                    filename = os.path.basename(file_path)
                    frame_info = self.get_frame_info(filename)
                    
                    if frame_info and frame_info["is_chunked"]:
                        # Parse chunk data
                        try:
                            chunk = json.loads(decoded_data)
                            chunk_id = chunk.get("chunk_id", frame_info["chunk_id"])
                            frame_data["chunks"][chunk_id] = chunk
                            if self.verbose:
                                print(f"  Added chunk {chunk_id} to frame {frame_number}")
                        except json.JSONDecodeError as e:
                            if self.verbose:
                                print(f"  Error parsing chunk data: {e}")
                    else:
                        # Not chunked, store directly
                        frame_data["payload"] = decoded_data
                        frame_data["decoded"] = True
                        if self.verbose:
                            print(f"  Stored payload for frame {frame_number}")
                else:
                    if self.verbose:
                        print(f"  Failed to decode {os.path.basename(file_path)}")
            
            # If chunked, try to reassemble
            if frame_data["is_chunked"] and frame_data["chunks"]:
                # Check if we have all chunks
                if len(frame_data["chunks"]) == frame_data["total_chunks"]:
                    # Sort chunks by chunk_id
                    sorted_chunks = [
                        frame_data["chunks"][i]
                        for i in sorted(frame_data["chunks"].keys())
                    ]
                    
                    # Reassemble payload
                    try:
                        # Extract data from each chunk
                        chunk_data = [chunk["data"] for chunk in sorted_chunks]
                        
                        # Join chunk data
                        payload = "".join(chunk_data)
                        
                        # Store payload
                        frame_data["payload"] = payload
                        frame_data["decoded"] = True
                    except Exception as e:
                        if self.verbose:
                            print(f"Error reassembling chunks: {e}")
                else:
                    if self.verbose:
                        print(f"Missing chunks: {frame_data['total_chunks'] - len(frame_data['chunks'])}/{frame_data['total_chunks']}")
            
            # If we have a payload, try to decompress if needed
            if frame_data["decoded"] and frame_data["payload"]:
                try:
                    # Check if payload is compressed
                    if isinstance(frame_data["payload"], str) and frame_data["payload"].startswith("COMPRESSED:"):
                        # Decompress
                        decompressed = self.decompress_data(frame_data["payload"])
                        frame_data["decompressed"] = decompressed
                        
                        # Try to parse as JSON
                        try:
                            frame_data["json_data"] = json.loads(decompressed)
                        except json.JSONDecodeError:
                            # Not JSON, store as is
                            pass
                    else:
                        # Try to parse as JSON
                        try:
                            frame_data["json_data"] = json.loads(frame_data["payload"])
                        except json.JSONDecodeError:
                            # Not JSON, store as is
                            pass
                except Exception as e:
                    if self.verbose:
                        print(f"Error processing payload: {e}")
            
            # Count decoded frames
            if frame_data["decoded"]:
                results["decoded_frames"] += 1
            
            # Store frame results
            results["frames"][frame_number] = {
                "decoded": frame_data["decoded"],
                "is_chunked": frame_data["is_chunked"],
                "total_chunks": frame_data["total_chunks"],
                "decoded_chunks": len(frame_data["chunks"]) if frame_data["is_chunked"] else 1,
                "has_json_data": "json_data" in frame_data
            }
            
            # Calculate phi resonance if available
            if "json_data" in frame_data and isinstance(frame_data["json_data"], dict):
                phi_state = frame_data["json_data"].get("phi_state", {})
                if phi_state and "resonance" in phi_state:
                    results["frames"][frame_number]["phi_resonance"] = phi_state["resonance"]
        
        # Calculate overall success rate
        results["success_rate"] = results["decoded_frames"] / results["total_frames"] if results["total_frames"] > 0 else 0
        results["success"] = results["success_rate"] > 0.5  # Success if more than half of frames decoded
        
        # Set success flag
        results["success"] = results["decoded_frames"] > 0
        
        if self.verbose:
            print(f"Analysis complete: {results['decoded_frames']}/{results['total_frames']} frames decoded")
        
        return results
    
    def generate_report(self, results):
        """
        Generate a detailed report from analysis results.
        
        Args:
            results: Analysis results from analyze_qr_sequence
            
        Returns:
            Report string
        """
        report = []
        report.append("QR Flipbook DNA System - Sequence Analysis Report")
        report.append("=" * 50)
        report.append(f"Timestamp: {datetime.now().isoformat()}")
        report.append(f"Input directory: {self.input_dir}")
        report.append("")
        
        # Handle error case
        if not results.get("success", False):
            error_msg = results.get('error', 'Unknown error')
            report.append(f"Analysis failed: {error_msg}")
            return "\n".join(report)
        
        # Handle case with no frames
        if results.get("total_frames", 0) == 0:
            report.append("No QR code frames found in the input directory.")
            return "\n".join(report)
        
        report.append("Overall Statistics:")
        report.append(f"  Total frames: {results['total_frames']}")
        report.append(f"  Decoded frames: {results['decoded_frames']} ({results['success_rate']*100:.1f}%)")
        report.append("")
        
        # Add phi resonance statistics if available
        phi_resonances = [
            frame.get("phi_resonance", 0)
            for frame in results["frames"].values()
            if "phi_resonance" in frame
        ]
        
        if phi_resonances:
            avg_resonance = sum(phi_resonances) / len(phi_resonances)
            max_resonance = max(phi_resonances)
            min_resonance = min(phi_resonances)
            
            report.append("Phi Resonance Statistics:")
            report.append(f"  Average: {avg_resonance:.4f}")
            report.append(f"  Maximum: {max_resonance:.4f}")
            report.append(f"  Minimum: {min_resonance:.4f}")
            report.append("")
        
        # Add frame details
        report.append("Frame Details:")
        for frame_number in sorted(results["frames"].keys()):
            frame = results["frames"][frame_number]
            status = "✅" if frame["decoded"] else "❌"
            
            report.append(f"  Frame {frame_number}: {status}")
            report.append(f"    Chunked: {'Yes' if frame['is_chunked'] else 'No'}")
            
            if frame["is_chunked"]:
                report.append(f"    Chunks: {frame['decoded_chunks']}/{frame['total_chunks']}")
            
            if "phi_resonance" in frame:
                report.append(f"    Phi resonance: {frame['phi_resonance']:.4f}")
            
            report.append("")
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="QR Robust Analyzer")
    parser.add_argument("--input-dir", default="qr_genome_sequence", help="Input directory containing QR code frames")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--report", action="store_true", help="Generate detailed report")
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = QRRobustAnalyzer(input_dir=args.input_dir, verbose=args.verbose)
    
    # Analyze QR sequence
    results = analyzer.analyze_qr_sequence()
    
    # Print results
    if args.report:
        print(analyzer.generate_report(results))
    else:
        print(f"Analysis complete: {results['decoded_frames']}/{results['total_frames']} frames decoded")
