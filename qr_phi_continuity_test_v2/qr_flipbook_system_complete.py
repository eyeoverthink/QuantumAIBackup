#!/usr/bin/env python3
"""
QR Flipbook DNA System - Complete Integrated Solution
By Vaughn Scott (with Cascade Assistant fixes)

A phi-harmonic integrated solution for the QR Flipbook DNA System that combines:
- Enhanced QR Generator with version control and phi-optimization
- Enhanced QR Analyzer with phi-harmonic image preprocessing
- QR Worker for task execution

This system implements the full QR Flipbook DNA workflow with phi-harmonic principles:
1. Load genome data
2. Generate QR sequence from genome
3. Analyze QR sequence
4. Execute tasks from QR codes
5. Generate response QR codes
"""

import os
import sys
import json
import time
import math
import argparse
from datetime import datetime

# Import our enhanced modules
from qr_simple_generator_fixed import QRSimpleGenerator
from qr_simple_analyzer_fixed import QRSimpleAnalyzer
from qr_worker import QRWorker

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio, approximately 1.618034

class QRFlipbookSystem:
    """
    Integrated QR Flipbook DNA System with phi-harmonic optimization.
    """
    
    def __init__(self, 
                 genome_path="qr_genome.json", 
                 sequence_dir="qr_sequence",
                 response_dir="qr_responses",
                 verbose=True):
        """
        Initialize the QR Flipbook DNA System.
        
        Args:
            genome_path: Path to genome JSON file
            sequence_dir: Directory to save QR sequence
            response_dir: Directory to save QR responses
            verbose: Whether to print verbose output
        """
        self.genome_path = genome_path
        self.sequence_dir = sequence_dir
        self.response_dir = response_dir
        self.verbose = verbose
        
        # Create directories
        os.makedirs(sequence_dir, exist_ok=True)
        os.makedirs(response_dir, exist_ok=True)
        
        # Initialize components with phi-harmonic parameters
        self.generator = QRSimpleGenerator(output_dir=sequence_dir, max_version=int(PHI * 15))  # ~24
        self.analyzer = QRSimpleAnalyzer(verbose=verbose)
        self.worker = QRWorker(output_dir=response_dir)
        
        # Initialize data
        self.genome_data = None
        self.qr_paths = []
        self.analysis_results = []
        self.execution_results = []
    
    def load_genome(self):
        """
        Load genome data from file.
        
        Returns:
            Loaded genome data
        """
        if self.verbose:
            print(f"Loading genome from {self.genome_path}...")
        
        try:
            with open(self.genome_path, 'r') as f:
                self.genome_data = json.load(f)
            
            if self.verbose:
                print("Genome loaded successfully")
            
            return self.genome_data
        except Exception as e:
            print(f"Error loading genome: {e}")
            return None
    
    def generate_qr_sequence(self):
        """
        Generate QR sequence from genome data.
        
        Returns:
            List of paths to generated QR images
        """
        if not self.genome_data:
            print("No genome data loaded")
            return []
        
        if self.verbose:
            print(f"\n=== Generating QR Sequence ===")
        
        # Clear existing sequence directory
        for file in os.listdir(self.sequence_dir):
            if file.endswith(".png"):
                os.remove(os.path.join(self.sequence_dir, file))
        
        start_time = time.time()
        self.qr_paths = self.generator.generate_from_genome(self.genome_data, self.sequence_dir)
        end_time = time.time()
        
        if self.verbose:
            print(f"Generated {len(self.qr_paths)} QR code files in {self.sequence_dir}")
            print(f"Generation time: {end_time - start_time:.2f} seconds")
            print(f"Phi-resonance timing: {(end_time - start_time) * PHI % 1.0:.6f}")
        
        return self.qr_paths
    
    def analyze_qr_sequence(self):
        """
        Analyze QR sequence.
        
        Returns:
            Analysis report
        """
        if not self.qr_paths:
            print("No QR sequence generated")
            return None
        
        if self.verbose:
            print(f"\n=== Analyzing QR Sequence ===")
        
        start_time = time.time()
        self.analysis_results = self.analyzer.analyze_qr_sequence(self.sequence_dir)
        end_time = time.time()
        
        if self.verbose:
            print(f"Decoded {len(self.analysis_results)} QR code files from {self.sequence_dir}")
            print(f"Analysis time: {end_time - start_time:.2f} seconds")
            print(f"Phi-resonance timing: {(end_time - start_time) * PHI % 1.0:.6f}")
        
        # Generate report
        report = self.analyzer.generate_report(self.analysis_results)
        
        if self.verbose:
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
        
        # Save report
        report_path = os.path.join(self.sequence_dir, "analysis_report.json")
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        if self.verbose:
            print(f"\nSaved analysis report to {report_path}")
        
        return report
    
    def execute_qr_sequence(self):
        """
        Execute tasks from QR sequence.
        
        Returns:
            List of execution results
        """
        if not self.analysis_results:
            print("No QR sequence analyzed")
            return []
        
        if self.verbose:
            print(f"\n=== Executing QR Sequence ===")
        
        self.execution_results = []
        
        # Use the analysis results instead of raw QR paths
        for i, result in enumerate(self.analysis_results):
            file_path = result["file"]
            data = result["data"]
            
            if self.verbose:
                print(f"\nProcessing QR file {i+1}/{len(self.analysis_results)}: {os.path.basename(file_path)}")
            
            # Process QR data directly instead of re-scanning the image
            response_path = self.worker.process_qr_data(data, os.path.basename(file_path))
            
            if response_path:
                self.execution_results.append({
                    "qr_path": file_path,
                    "response_path": response_path,
                    "status": "success"
                })
                
                if self.verbose:
                    print(f"Generated response QR: {response_path}")
            else:
                self.execution_results.append({
                    "qr_path": file_path,
                    "status": "error",
                    "message": "Failed to process QR data"
                })
                
                if self.verbose:
                    print("Failed to process QR data")
        
        if self.verbose:
            successful = sum(1 for r in self.execution_results if r["status"] == "success")
            print(f"\nExecution complete: {successful}/{len(self.execution_results)} successful")
            print(f"Phi-resonance success rate: {successful / max(1, len(self.execution_results)) * PHI:.6f}")
        
        return self.execution_results
    
    def generate_summary(self):
        """
        Generate summary of QR Flipbook DNA System execution.
        
        Returns:
            Summary as dictionary
        """
        # Calculate phi-harmonic metrics
        phi_resonance = time.time() * PHI % 1.0
        phi_cycle = int(time.time() / PHI) % int(PHI**3)
        
        summary = {
            "timestamp": datetime.now().isoformat(),
            "genome_path": self.genome_path,
            "sequence_dir": self.sequence_dir,
            "response_dir": self.response_dir,
            "qr_frames_generated": len(self.qr_paths),
            "qr_frames_decoded": len(self.analysis_results),
            "qr_frames_executed": len(self.execution_results),
            "qr_frames_executed_successfully": sum(1 for r in self.execution_results if r["status"] == "success"),
            "phi_resonance": phi_resonance,
            "phi_cycle": phi_cycle,
            "phi_harmonic_index": 1.0 / (1.0 + abs(phi_resonance - 0.5))
        }
        
        # Save summary
        summary_path = os.path.join(self.sequence_dir, "system_summary.json")
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        if self.verbose:
            print(f"\n=== System Summary ===")
            print(f"Genome path: {summary['genome_path']}")
            print(f"QR frames generated: {summary['qr_frames_generated']}")
            print(f"QR frames decoded: {summary['qr_frames_decoded']}")
            print(f"QR frames executed: {summary['qr_frames_executed']}")
            print(f"QR frames executed successfully: {summary['qr_frames_executed_successfully']}")
            print(f"Phi resonance: {summary['phi_resonance']:.6f}")
            print(f"Phi harmonic index: {summary['phi_harmonic_index']:.6f}")
            print(f"\nSummary saved to {summary_path}")
        
        return summary
    
    def run(self):
        """
        Run the full QR Flipbook DNA System workflow.
        
        Returns:
            Summary of execution
        """
        if self.verbose:
            print("QR Flipbook DNA System - Starting")
            print(f"Phi constant: {PHI}")
            print(f"Current phi resonance: {time.time() * PHI % 1.0:.6f}")
        
        # Load genome
        if not self.load_genome():
            return None
        
        # Generate QR sequence
        self.generate_qr_sequence()
        
        # Analyze QR sequence
        self.analyze_qr_sequence()
        
        # Execute QR sequence
        self.execute_qr_sequence()
        
        # Generate summary
        summary = self.generate_summary()
        
        if self.verbose:
            print("\nQR Flipbook DNA System - Complete")
        
        return summary

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="QR Flipbook DNA System")
    parser.add_argument("--genome", default="qr_genome.json", help="Path to genome JSON file")
    parser.add_argument("--sequence-dir", default="qr_sequence", help="Directory to save QR sequence")
    parser.add_argument("--response-dir", default="qr_responses", help="Directory to save QR responses")
    parser.add_argument("--quiet", action="store_true", help="Suppress verbose output")
    parser.add_argument("--clean", action="store_true", help="Clean output directories before running")
    args = parser.parse_args()
    
    # Clean directories if requested
    if args.clean:
        if os.path.exists(args.sequence_dir):
            for file in os.listdir(args.sequence_dir):
                os.remove(os.path.join(args.sequence_dir, file))
        if os.path.exists(args.response_dir):
            for file in os.listdir(args.response_dir):
                os.remove(os.path.join(args.response_dir, file))
    
    # Create QR Flipbook DNA System
    system = QRFlipbookSystem(
        genome_path=args.genome,
        sequence_dir=args.sequence_dir,
        response_dir=args.response_dir,
        verbose=not args.quiet
    )
    
    # Run system
    system.run()

if __name__ == "__main__":
    main()
