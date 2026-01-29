#!/usr/bin/env python3
"""
Complete QR Flipbook DNA System Test
By Vaughn Scott

A comprehensive test of the QR Flipbook DNA System with compatibility adapter.
This script demonstrates the full workflow:
1. Generate QR sequence from genome
2. Convert QR sequence to worker-compatible format
3. Process QR sequence with worker
4. Generate summary report
"""

import os
import sys
import json
import time
import uuid
from datetime import datetime

# Import our modules
from qr_simple_generator import QRSimpleGenerator
from qr_simple_analyzer import QRSimpleAnalyzer
from qr_compatibility_adapter import QRCompatibilityAdapter
from qr_worker import QRWorker

# Test directories
GENOME_PATH = "qr_genome.json"
SEQUENCE_DIR = "qr_test_sequence"
COMPATIBLE_DIR = "qr_test_compatible"
RESPONSE_DIR = "qr_test_responses"
REPORT_DIR = "qr_test_reports"

def load_genome(genome_path):
    """Load genome from file."""
    try:
        with open(genome_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading genome from {genome_path}: {e}")
        return None

def create_directories():
    """Create test directories."""
    for directory in [SEQUENCE_DIR, COMPATIBLE_DIR, RESPONSE_DIR, REPORT_DIR]:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def test_qr_generation(genome_data):
    """Test QR sequence generation."""
    print("\n=== Step 1: Generating QR Sequence ===")
    
    # Create QR generator
    generator = QRSimpleGenerator(output_dir=SEQUENCE_DIR)
    
    # Generate QR sequence
    start_time = time.time()
    qr_paths = generator.generate_from_genome(genome_data)
    end_time = time.time()
    
    print(f"Generated {len(qr_paths)} QR code files in {SEQUENCE_DIR}")
    print(f"Generation time: {end_time - start_time:.2f} seconds")
    
    return qr_paths

def test_qr_analysis():
    """Test QR sequence analysis."""
    print("\n=== Step 2: Analyzing QR Sequence ===")
    
    # Create QR analyzer
    analyzer = QRSimpleAnalyzer(verbose=True)
    
    # Analyze QR sequence
    start_time = time.time()
    results = analyzer.analyze_qr_sequence(SEQUENCE_DIR)
    end_time = time.time()
    
    print(f"Decoded {len(results)} QR code files from {SEQUENCE_DIR}")
    print(f"Analysis time: {end_time - start_time:.2f} seconds")
    
    # Generate report
    report = analyzer.generate_report(results)
    
    # Save report
    report_path = os.path.join(REPORT_DIR, "analysis_report.json")
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Saved analysis report to {report_path}")
    
    return report

def test_qr_conversion():
    """Test QR sequence conversion to worker-compatible format."""
    print("\n=== Step 3: Converting QR Sequence to Worker-Compatible Format ===")
    
    # Create QR compatibility adapter
    adapter = QRCompatibilityAdapter(output_dir=COMPATIBLE_DIR, verbose=True)
    
    # Convert QR sequence
    start_time = time.time()
    converted_paths = adapter.convert_qr_sequence(SEQUENCE_DIR)
    end_time = time.time()
    
    print(f"Converted {len(converted_paths)} QR code files to worker-compatible format")
    print(f"Conversion time: {end_time - start_time:.2f} seconds")
    
    return converted_paths

def test_qr_execution(converted_paths):
    """Test QR sequence execution with worker."""
    print("\n=== Step 4: Executing QR Sequence with Worker ===")
    
    # Create QR worker
    worker = QRWorker(output_dir=RESPONSE_DIR)
    
    # Process each QR file
    execution_results = []
    for i, qr_path in enumerate(sorted(converted_paths)):
        print(f"\nProcessing QR file {i+1}/{len(converted_paths)}: {qr_path}")
        
        # Process QR image
        response_path = worker.process_qr_image(qr_path)
        
        if response_path:
            execution_results.append({
                "qr_path": qr_path,
                "response_path": response_path,
                "status": "success"
            })
            print(f"Generated response QR: {response_path}")
        else:
            execution_results.append({
                "qr_path": qr_path,
                "status": "error",
                "message": "Failed to process QR code"
            })
            print("Failed to process QR code")
    
    successful = sum(1 for r in execution_results if r["status"] == "success")
    print(f"\nExecution complete: {successful}/{len(execution_results)} successful")
    
    return execution_results

def generate_summary(qr_paths, report, converted_paths, execution_results):
    """Generate summary of QR Flipbook DNA System test."""
    print("\n=== Step 5: Generating Summary Report ===")
    
    # Calculate phi-harmonic timing
    phi = (1 + 5**0.5) / 2  # Golden Ratio
    phi_time = time.time() * phi % 1.0
    
    # Create summary
    summary = {
        "timestamp": datetime.now().isoformat(),
        "genome_path": GENOME_PATH,
        "sequence_dir": SEQUENCE_DIR,
        "compatible_dir": COMPATIBLE_DIR,
        "response_dir": RESPONSE_DIR,
        "report_dir": REPORT_DIR,
        "qr_frames_generated": len(qr_paths),
        "qr_frames_decoded": report["frames_decoded"],
        "qr_frames_converted": len(converted_paths),
        "qr_frames_executed": len(execution_results),
        "qr_frames_executed_successfully": sum(1 for r in execution_results if r["status"] == "success"),
        "phi_resonance": phi_time
    }
    
    # Save summary
    summary_path = os.path.join(REPORT_DIR, "system_summary.json")
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"Genome path: {summary['genome_path']}")
    print(f"QR frames generated: {summary['qr_frames_generated']}")
    print(f"QR frames decoded: {summary['qr_frames_decoded']}")
    print(f"QR frames converted: {summary['qr_frames_converted']}")
    print(f"QR frames executed: {summary['qr_frames_executed']}")
    print(f"QR frames executed successfully: {summary['qr_frames_executed_successfully']}")
    print(f"Phi resonance: {summary['phi_resonance']:.6f}")
    print(f"\nSummary saved to {summary_path}")
    
    return summary

def main():
    """Main function."""
    print("Complete QR Flipbook DNA System Test - Starting")
    
    # Create test directories
    create_directories()
    
    # Load genome
    genome_data = load_genome(GENOME_PATH)
    if not genome_data:
        print("Failed to load genome data")
        return
    
    # Test QR generation
    qr_paths = test_qr_generation(genome_data)
    
    # Test QR analysis
    report = test_qr_analysis()
    
    # Test QR conversion
    converted_paths = test_qr_conversion()
    
    # Test QR execution
    execution_results = test_qr_execution(converted_paths)
    
    # Generate summary
    summary = generate_summary(qr_paths, report, converted_paths, execution_results)
    
    print("\nComplete QR Flipbook DNA System Test - Complete")

if __name__ == "__main__":
    main()
