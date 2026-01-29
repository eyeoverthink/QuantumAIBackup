#!/usr/bin/env python3
"""
QR System Test - Part of Animated QR Flipbook DNA System
By Vaughn Scott

A test script to verify QR sequence generation and decoding using the simplified QR generator and analyzer.
"""

import os
import sys
import json
import time
from datetime import datetime

# Import our modules
from qr_simple_generator import QRSimpleGenerator
from qr_simple_analyzer import QRSimpleAnalyzer

# Test directories
TEST_OUTPUT_DIR = "qr_test_system"
GENOME_PATH = "qr_genome.json"

def create_test_genome():
    """Create a simple test genome."""
    test_genome = {
        "genome_id": "test-genome-001",
        "timestamp": datetime.now().isoformat(),
        "groups": [
            {
                "group_id": "G1",
                "codons": [
                    {
                        "frame_data": {
                            "task_type": "execute_python",
                            "task_data": {
                                "code": "print('Hello from QR Flipbook DNA System!')\nprint('This is frame 1 of the test genome.')"
                            }
                        },
                        "phi_state": {
                            "resonance": 1.618,
                            "complexity": 0.618,
                            "generation": 1
                        }
                    },
                    {
                        "frame_data": {
                            "task_type": "execute_python",
                            "task_data": {
                                "code": "print('This is frame 2 of the test genome.')\nprint(f'Current time: {datetime.now().isoformat()}')"
                            }
                        },
                        "phi_state": {
                            "resonance": 2.618,
                            "complexity": 1.618,
                            "generation": 2
                        }
                    },
                    {
                        "frame_data": {
                            "task_type": "execute_sh",
                            "task_data": {
                                "code": "#!/bin/bash\necho 'Hello from shell script!'\necho 'This is frame 3 of the test genome.'\necho \"Current date: $(date)\""
                            }
                        },
                        "phi_state": {
                            "resonance": 4.236,
                            "complexity": 2.618,
                            "generation": 3
                        }
                    }
                ]
            }
        ]
    }
    
    return test_genome

def load_genome(genome_path):
    """Load genome from file."""
    try:
        with open(genome_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading genome from {genome_path}: {e}")
        print("Creating test genome instead...")
        return create_test_genome()

def test_qr_sequence_generation(genome_data):
    """Test QR sequence generation."""
    print("\n=== Testing QR Sequence Generation ===")
    
    # Create QR generator
    generator = QRSimpleGenerator(output_dir=TEST_OUTPUT_DIR)
    
    # Generate QR sequence
    start_time = time.time()
    qr_paths = generator.generate_from_genome(genome_data)
    end_time = time.time()
    
    print(f"Generated {len(qr_paths)} QR code files in {TEST_OUTPUT_DIR}")
    print(f"Generation time: {end_time - start_time:.2f} seconds")
    
    return qr_paths

def test_qr_sequence_analysis():
    """Test QR sequence analysis."""
    print("\n=== Testing QR Sequence Analysis ===")
    
    # Create QR analyzer
    analyzer = QRSimpleAnalyzer(verbose=True)
    
    # Analyze QR sequence
    start_time = time.time()
    results = analyzer.analyze_qr_sequence(TEST_OUTPUT_DIR)
    end_time = time.time()
    
    print(f"Decoded {len(results)} QR code files from {TEST_OUTPUT_DIR}")
    print(f"Analysis time: {end_time - start_time:.2f} seconds")
    
    # Generate report
    report = analyzer.generate_report(results)
    
    print("\n=== Analysis Report ===")
    print(f"Status: {report['status']}")
    print(f"Message: {report['message']}")
    print(f"Frames decoded: {report['frames_decoded']}")
    
    print("\nFrame details:")
    for i, frame in enumerate(report['frames']):
        print(f"  Frame {i+1}:")
        print(f"    Frame ID: {frame.get('frame_id', 'N/A')}")
        print(f"    Task type: {frame.get('task_type', 'N/A')}")
        if 'code_preview' in frame:
            print(f"    Code preview: {frame['code_preview']}")
        if 'phi_state' in frame:
            print(f"    Phi resonance: {frame['phi_state'].get('resonance', 'N/A')}")
    
    return report

def main():
    """Main function."""
    print("QR System Test - Starting")
    
    # Create output directory
    os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)
    
    # Load or create genome
    genome_data = load_genome(GENOME_PATH)
    
    # Test QR sequence generation
    qr_paths = test_qr_sequence_generation(genome_data)
    
    # Test QR sequence analysis
    report = test_qr_sequence_analysis()
    
    # Save report
    report_path = os.path.join(TEST_OUTPUT_DIR, "analysis_report.json")
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nSaved analysis report to {report_path}")
    print("\nQR System Test - Complete")

if __name__ == "__main__":
    main()
