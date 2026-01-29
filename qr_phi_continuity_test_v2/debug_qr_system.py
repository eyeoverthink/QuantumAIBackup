#!/usr/bin/env python3
"""
QR Flipbook DNA System Debugger
By Vaughn Scott

A comprehensive debugging tool for the QR Flipbook DNA System.
Helps diagnose and fix issues with QR code generation, chunking, and decoding.
"""

import os
import sys
import json
import math
import base64
import zlib
import argparse
import tempfile
from PIL import Image
from pyzbar.pyzbar import decode

# Import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qr_sequence_chunker import QRSequenceChunker
from qr_sequence_generator import QRSequenceGenerator
from qr_genome_engine import QRGenomeEngine
from qr_task_executor import QRTaskExecutor
from qr_epigenetic_memory import QREpigeneticMemory

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRSystemDebugger:
    """
    Comprehensive debugging tool for the QR Flipbook DNA System.
    """
    
    def __init__(self):
        """Initialize the QR System Debugger."""
        self.chunker = QRSequenceChunker(max_chunk_size=500)  # Use smaller chunks for better QR compatibility
        self.sequence_dir = "qr_genome_sequence"
        self.test_data = {
            "small": "This is a small test payload for QR code generation.",
            "medium": "A" * 500,  # 500 character string
            "large": "B" * 2000,  # 2000 character string
            "code": "print('Hello from QR code!')\nfor i in range(5):\n    print(f'Phi-harmonic iteration {i}')"
        }
    
    def test_qr_generation(self):
        """Test QR code generation with different payload sizes."""
        print("🧪 Testing QR code generation...")
        
        # Create temporary directory for test QR codes
        with tempfile.TemporaryDirectory() as temp_dir:
            # Initialize QR generator
            generator = QRSequenceGenerator(output_dir=temp_dir)
            
            results = {}
            
            # Test each payload size
            for name, payload in self.test_data.items():
                print(f"  Testing {name} payload ({len(payload)} chars)...")
                
                try:
                    # Generate QR code
                    path = generator.generate_qr_frame(payload, 1)
                    
                    # Check if result is a list (chunked) or single path
                    is_chunked = isinstance(path, list)
                    num_chunks = len(path) if is_chunked else 1
                    
                    # Try to decode the QR code(s)
                    if is_chunked:
                        decoded_data = []
                        for chunk_path in path:
                            chunk_data = self._decode_qr_image(chunk_path)
                            if chunk_data:
                                decoded_data.append(chunk_data)
                        
                        # Check if all chunks were decoded
                        all_decoded = len(decoded_data) == num_chunks
                    else:
                        decoded_data = self._decode_qr_image(path)
                        all_decoded = decoded_data is not None
                    
                    results[name] = {
                        "success": True,
                        "is_chunked": is_chunked,
                        "num_chunks": num_chunks,
                        "all_decoded": all_decoded
                    }
                    
                    print(f"    ✅ Success! {'Chunked into ' + str(num_chunks) + ' parts' if is_chunked else 'Single QR code'}")
                    print(f"    {'All' if all_decoded else 'Some'} chunks decoded successfully")
                    
                except Exception as e:
                    results[name] = {
                        "success": False,
                        "error": str(e)
                    }
                    print(f"    ❌ Failed: {e}")
            
            return results
    
    def test_chunking(self):
        """Test the QR sequence chunker with different payload sizes."""
        print("🧪 Testing QR sequence chunking...")
        
        results = {}
        
        # Test each payload size
        for name, payload in self.test_data.items():
            print(f"  Testing {name} payload ({len(payload)} chars)...")
            
            try:
                # Compress payload
                compressed = self.chunker.compress_payload(payload)
                
                # Check compression ratio
                compression_ratio = len(compressed) / len(payload)
                
                # Chunk the payload
                chunks = self.chunker.chunk_payload(payload)
                
                # Try to reassemble the chunks
                reassembled = self.chunker.reassemble_payload(chunks)
                
                # Check if reassembly was successful
                success = reassembled == payload
                
                results[name] = {
                    "success": success,
                    "compression_ratio": compression_ratio,
                    "num_chunks": len(chunks),
                    "original_size": len(payload),
                    "compressed_size": len(compressed),
                    "is_compressed": compressed.startswith("COMPRESSED:")
                }
                
                print(f"    ✅ Success! Chunked into {len(chunks)} parts")
                print(f"    Compression ratio: {compression_ratio:.2f}x")
                print(f"    Reassembly {'successful' if success else 'failed'}")
                
            except Exception as e:
                results[name] = {
                    "success": False,
                    "error": str(e)
                }
                print(f"    ❌ Failed: {e}")
        
        return results
    
    def test_genome_qr_integration(self):
        """Test the integration between the genome engine and QR sequence generator."""
        print("🧪 Testing genome-QR integration...")
        
        try:
            # Initialize components
            memory = QREpigeneticMemory()
            executor = QRTaskExecutor()
            engine = QRGenomeEngine()
            engine.executor = executor
            engine.memory = memory
            
            # Load genome
            engine.load_genome()
            
            # Generate QR sequence
            engine.generate_qr_sequence()
            
            # Check if QR sequence was generated
            qr_files = os.listdir(self.sequence_dir)
            qr_count = len([f for f in qr_files if f.endswith(".png")])
            
            result = {
                "success": qr_count > 0,
                "qr_count": qr_count
            }
            
            print(f"    {'✅ Success!' if result['success'] else '❌ Failed!'}")
            print(f"    Generated {qr_count} QR code files")
            
            return result
            
        except Exception as e:
            print(f"    ❌ Failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def analyze_qr_sequence(self):
        """Analyze the QR sequence directory for issues."""
        print("🔍 Analyzing QR sequence...")
        
        # Get all QR files
        qr_files = [f for f in os.listdir(self.sequence_dir) if f.endswith(".png")]
        
        # Group by frame number
        frames = {}
        for filename in qr_files:
            if filename.startswith("qr_frame_"):
                # Extract frame number
                parts = filename[9:].split("_")
                frame_num = int(parts[0].split(".")[0])
                
                if frame_num not in frames:
                    frames[frame_num] = []
                frames[frame_num].append(os.path.join(self.sequence_dir, filename))
        
        results = {
            "total_frames": len(frames),
            "frames": {}
        }
        
        # Analyze each frame
        for frame_num, frame_files in frames.items():
            print(f"  Analyzing frame {frame_num}...")
            
            # Sort files to ensure correct order
            frame_files = sorted(frame_files)
            
            # Check if frame is chunked
            is_chunked = len(frame_files) > 1
            
            # Try to decode each file
            decoded = []
            for file_path in frame_files:
                data = self._decode_qr_image(file_path)
                if data:
                    decoded.append(data)
            
            # Check if all files were decoded
            all_decoded = len(decoded) == len(frame_files)
            
            # Try to reassemble if chunked
            reassembled = None
            if is_chunked and all_decoded:
                try:
                    # Try to parse each chunk as JSON
                    chunks = []
                    for data in decoded:
                        try:
                            chunk = json.loads(data)
                            chunks.append(chunk)
                        except json.JSONDecodeError:
                            pass
                    
                    # If we have valid chunks, try to reassemble
                    if chunks and all("chunk_id" in c for c in chunks):
                        chunks = sorted(chunks, key=lambda x: x["chunk_id"])
                        reassembled = self.chunker.reassemble_payload(chunks)
                except Exception as e:
                    print(f"    Error reassembling chunks: {e}")
            
            # Store results
            results["frames"][frame_num] = {
                "is_chunked": is_chunked,
                "num_chunks": len(frame_files),
                "all_decoded": all_decoded,
                "decoded_count": len(decoded),
                "reassembled": reassembled is not None
            }
            
            status = "✅" if all_decoded else "⚠️" if decoded else "❌"
            print(f"    {status} {len(decoded)}/{len(frame_files)} files decoded")
            if reassembled:
                print(f"    ✅ Successfully reassembled chunked data")
        
        return results
    
    def fix_qr_sequence(self):
        """Fix issues with the QR sequence."""
        print("🔧 Fixing QR sequence issues...")
        
        # Analyze the sequence first
        analysis = self.analyze_qr_sequence()
        
        if analysis["total_frames"] == 0:
            print("  No frames found to fix!")
            return
        
        # Check if we need to regenerate the sequence
        problematic_frames = [
            frame_num for frame_num, data in analysis["frames"].items()
            if not data["all_decoded"] or (data["is_chunked"] and not data["reassembled"])
        ]
        
        if problematic_frames:
            print(f"  Found {len(problematic_frames)} problematic frames")
            print("  Regenerating QR sequence with optimized settings...")
            
            # Initialize components
            memory = QREpigeneticMemory()
            executor = QRTaskExecutor()
            engine = QRGenomeEngine()
            engine.executor = executor
            engine.memory = memory
            
            # Patch the QR sequence generator to use smaller chunks
            original_init = QRSequenceGenerator.__init__
            
            def patched_init(self, output_dir="qr_genome_sequence", encryption_key=None):
                original_init(self, output_dir, encryption_key)
                self.chunker = QRSequenceChunker(max_chunk_size=500)
            
            # Apply the patch
            QRSequenceGenerator.__init__ = patched_init
            
            try:
                # Load genome
                engine.load_genome()
                
                # Generate QR sequence
                engine.generate_qr_sequence()
                
                print("  ✅ Successfully regenerated QR sequence")
                
                # Restore original method
                QRSequenceGenerator.__init__ = original_init
                
                # Analyze again
                return self.analyze_qr_sequence()
                
            except Exception as e:
                print(f"  ❌ Failed to regenerate QR sequence: {e}")
                
                # Restore original method
                QRSequenceGenerator.__init__ = original_init
                
                return {
                    "success": False,
                    "error": str(e)
                }
        else:
            print("  ✅ No issues found that require fixing")
            return analysis
    
    def _decode_qr_image(self, image_path):
        """
        Decode a QR code image.
        
        Args:
            image_path: Path to QR code image
            
        Returns:
            Decoded data or None if decoding fails
        """
        try:
            # Open the image
            image = Image.open(image_path)
            
            # Decode QR code
            decoded = decode(image)
            if decoded:
                return decoded[0].data.decode('utf-8')
            
            return None
        except Exception as e:
            print(f"    Error decoding {os.path.basename(image_path)}: {e}")
            return None

def main():
    """Main function for the QR System Debugger."""
    parser = argparse.ArgumentParser(description="Debug the QR Flipbook DNA System")
    parser.add_argument("--test-qr", action="store_true", help="Test QR code generation")
    parser.add_argument("--test-chunking", action="store_true", help="Test QR sequence chunking")
    parser.add_argument("--test-integration", action="store_true", help="Test genome-QR integration")
    parser.add_argument("--analyze", action="store_true", help="Analyze QR sequence")
    parser.add_argument("--fix", action="store_true", help="Fix QR sequence issues")
    parser.add_argument("--all", action="store_true", help="Run all tests and fixes")
    args = parser.parse_args()
    
    # Create debugger
    debugger = QRSystemDebugger()
    
    # Run requested tests
    if args.all or args.test_qr:
        debugger.test_qr_generation()
        print()
    
    if args.all or args.test_chunking:
        debugger.test_chunking()
        print()
    
    if args.all or args.test_integration:
        debugger.test_genome_qr_integration()
        print()
    
    if args.all or args.analyze:
        debugger.analyze_qr_sequence()
        print()
    
    if args.all or args.fix:
        debugger.fix_qr_sequence()
        print()
    
    # If no arguments provided, show help
    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
