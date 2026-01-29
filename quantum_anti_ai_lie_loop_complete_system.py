#!/usr/bin/env python3
# Quantum Anti-AI Lie Loop Complete System
# This script integrates all components of the Quantum Anti-AI Lie Loop system
# including verification, visualization, and reporting

import os
import sys
import json
import time
import argparse
import tempfile
from datetime import datetime
from typing import Dict, List, Any, Optional, Union

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio
PHI_CONJUGATE = 1 / PHI  # Golden ratio conjugate

# Try to import the core components
try:
    from quantum_anti_ai_lie_loop_extended import QuantumAntiAILieLoopExtended
except ImportError:
    print("Warning: Could not import QuantumAntiAILieLoopExtended. Using base class if available.")
    try:
        from quantum_anti_ai_lie_loop import QuantumAntiAILieLoop as QuantumAntiAILieLoopExtended
    except ImportError:
        print("Error: Could not import QuantumAntiAILieLoop. Verification will not be available.")
        QuantumAntiAILieLoopExtended = None

# Try to import the visualizer
try:
    from quantum_anti_ai_lie_loop_visualizer import QuantumAntiAILieLoopVisualizer
except ImportError:
    print("Warning: Could not import QuantumAntiAILieLoopVisualizer. Visualization will not be available.")
    QuantumAntiAILieLoopVisualizer = None

# Try to import optional components
try:
    from quantum_binary_translator import QuantumBinaryTranslator
    has_quantum_translator = True
except ImportError:
    print("Note: QuantumBinaryTranslator not available. Some advanced features will be disabled.")
    has_quantum_translator = False
    QuantumBinaryTranslator = None

class QuantumAntiAILieLoopCompleteSystem:
    """Complete system integrating verification, visualization, and reporting."""
    
    def __init__(self, output_dir="quantum_verification_results"):
        """Initialize the complete system."""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize components
        self.verifier = None
        self.visualizer = None
        self.translator = None
        
        # Initialize components if available
        if QuantumAntiAILieLoopExtended:
            self.verifier = QuantumAntiAILieLoopExtended()
        
        if has_quantum_translator:
            self.translator = QuantumBinaryTranslator()
        
        # Store results
        self.verification_results = []
        self.current_result = None
        self.batch_report = None
    
    def verify_code(self, code_str=None, file_path=None, timeout=10):
        """Verify code from string or file."""
        if not self.verifier:
            print("Error: Verifier component not available.")
            return None
        
        start_time = time.time()
        
        # Get code from file if path is provided
        if file_path and os.path.exists(file_path):
            with open(file_path, 'r') as f:
                code_str = f.read()
            source_id = os.path.basename(file_path)
        else:
            source_id = f"code_snippet_{int(time.time())}"
        
        print(f"\n[*] Verifying: {source_id}")
        
        # Run verification
        try:
            print("[DEBUG] Creating verifier instance...")
            # Initialize a new verifier for this code
            verifier = QuantumAntiAILieLoopExtended(code_string=code_str, verbose=True)
            
            print("[DEBUG] Running full verification...")
            # Use the extended verifier's full verification method
            result = verifier.run_full_verification(code_str, timeout=timeout)
            
            print("[DEBUG] Verification completed successfully")
            
            # Add source information
            if file_path:
                result["file_path"] = file_path
            result["snippet_id"] = source_id
            result["verification_time"] = time.time() - start_time
            
            # Calculate phi-harmonic resonance of verification time
            result["verification_phi_resonance"] = (result["verification_time"] * PHI) % 1.0
            
            # Add quantum binary analysis if available
            if self.translator:
                print("[DEBUG] Running quantum binary analysis...")
                binary_analysis = self.translator.analyze_code(code_str)
                result["quantum_binary_analysis"] = binary_analysis
            
            # Store the result
            self.verification_results.append(result)
            self.current_result = result
            
            # Print summary
            self._print_verification_summary(result)
            
            return result
            
        except Exception as e:
            import traceback
            print(f"Error during verification: {str(e)}")
            print("Traceback:")
            traceback.print_exc()
            return None
    
    def _print_verification_summary(self, result):
        """Print a summary of verification results."""
        if not result:
            return
        
        print("\n===== Verification Summary =====")
        print(f"Trust Metric: {result.get('trust_metric', 0):.6f}")
        print(f"Phi Resonance: {result.get('verification_phi_resonance', 0):.6f}")
        print(f"Claims Found: {len(result.get('claims', []))}")
        print(f"Contradictions: {len(result.get('contradictions', []))}")
        
        # Print quantum signature if available
        if "quantum_signature" in result:
            print(f"Quantum Signature: {result['quantum_signature'].get('signature', '')[:16]}...")
        
        print("=============================")
    
    def visualize_results(self, result=None, output_subdir=None):
        """Visualize verification results."""
        if not QuantumAntiAILieLoopVisualizer:
            print("Error: Visualizer component not available.")
            return None
        
        # Use current result if none provided
        if not result:
            if not self.current_result:
                print("Error: No verification results available for visualization.")
                return None
            result = self.current_result
        
        # Determine output directory
        if not output_subdir:
            output_subdir = os.path.join(self.output_dir, f"visualization_{int(time.time())}")
        
        os.makedirs(output_subdir, exist_ok=True)
        
        # Create temporary file for the result
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
            json.dump(result, temp_file, indent=2)
            temp_file_path = temp_file.name
        
        # Initialize visualizer and generate visualizations
        visualizer = QuantumAntiAILieLoopVisualizer(report_file=temp_file_path)
        visualization_files = visualizer.visualize_all(output_subdir)
        
        # Clean up temporary file
        os.unlink(temp_file_path)
        
        print(f"\nVisualizations saved to: {output_subdir}")
        return visualization_files
    
    def visualize_batch_results(self):
        """Visualize batch verification results."""
        if not self.verification_results or len(self.verification_results) == 0:
            print("Error: No batch results available for visualization.")
            return None
        
        # Create batch report if not already created
        if not self.batch_report:
            self.create_batch_report()
        
        # Create output directory
        batch_viz_dir = os.path.join(self.output_dir, f"batch_visualization_{int(time.time())}")
        os.makedirs(batch_viz_dir, exist_ok=True)
        
        # Create temporary file for the batch report
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
            json.dump(self.batch_report, temp_file, indent=2)
            temp_file_path = temp_file.name
        
        # Initialize visualizer and generate visualizations
        visualizer = QuantumAntiAILieLoopVisualizer(report_file=temp_file_path)
        visualization_files = visualizer.visualize_all(batch_viz_dir)
        
        # Clean up temporary file
        os.unlink(temp_file_path)
        
        print(f"\nBatch visualizations saved to: {batch_viz_dir}")
        return visualization_files
    
    def create_batch_report(self):
        """Create a batch report from all verification results."""
        if not self.verification_results or len(self.verification_results) == 0:
            print("Error: No verification results available for batch report.")
            return None
        
        # Calculate batch metrics
        avg_trust = sum(r.get("trust_metric", 0) for r in self.verification_results) / len(self.verification_results)
        total_contradictions = sum(len(r.get("contradictions", [])) for r in self.verification_results)
        total_claims = sum(len(r.get("claims", [])) for r in self.verification_results)
        
        # Create batch report
        self.batch_report = {
            "results": self.verification_results,
            "batch_id": f"batch_{int(time.time())}",
            "timestamp": int(time.time()),
            "average_trust_metric": avg_trust,
            "total_contradictions": total_contradictions,
            "total_claims": total_claims,
            "phi_harmonic_coherence": self._calculate_phi_harmonic_coherence()
        }
        
        return self.batch_report
    
    def _calculate_phi_harmonic_coherence(self):
        """Calculate phi-harmonic coherence across all verification results."""
        if not self.verification_results:
            return 0
        
        # Extract phi resonance values
        resonances = [r.get("verification_phi_resonance", 0) for r in self.verification_results]
        
        # Calculate distance to phi-conjugate for each resonance
        distances = [min(abs(r - PHI_CONJUGATE), abs(1 + PHI_CONJUGATE - r)) for r in resonances]
        
        # Calculate average distance and convert to coherence (1 = perfect, 0 = none)
        avg_distance = sum(distances) / len(distances)
        coherence = max(0, 1 - avg_distance * 5)  # Scale factor of 5 to make it more sensitive
        
        return coherence
    
    def export_report(self, result=None, output_file=None):
        """Export verification report to JSON file."""
        # Use current result if none provided
        if not result:
            if not self.current_result:
                print("Error: No verification results available for export.")
                return None
            result = self.current_result
        
        # Generate output filename if not provided
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            source_id = result.get("snippet_id", "unknown")
            output_file = os.path.join(self.output_dir, f"verification_{source_id}_{timestamp}.json")
        
        # Write report to file
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        
        print(f"\nVerification report exported to: {output_file}")
        return output_file
    
    def export_batch_report(self, output_file=None):
        """Export batch verification report to JSON file."""
        # Create batch report if not already created
        if not self.batch_report:
            self.create_batch_report()
        
        # Generate output filename if not provided
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.output_dir, f"batch_verification_{timestamp}.json")
        
        # Write batch report to file
        with open(output_file, 'w') as f:
            json.dump(self.batch_report, f, indent=2)
        
        print(f"\nBatch verification report exported to: {output_file}")
        return output_file
    
    def run_full_pipeline(self, code_str=None, file_path=None, timeout=10, visualize=True):
        """Run the complete verification pipeline on a single code sample."""
        # Step 1: Verify the code
        result = self.verify_code(code_str, file_path, timeout)
        if not result:
            return None
        
        # Step 2: Export the report
        report_file = self.export_report(result)
        
        # Step 3: Visualize the results if requested
        if visualize and QuantumAntiAILieLoopVisualizer:
            visualization_files = self.visualize_results(result)
        
        return {
            "result": result,
            "report_file": report_file,
            "visualization_files": visualization_files if visualize and QuantumAntiAILieLoopVisualizer else None
        }
    
    def run_batch_pipeline(self, file_paths=None, directory=None, timeout=10, visualize=True):
        """Run the complete verification pipeline on multiple code samples."""
        # Reset results
        self.verification_results = []
        self.batch_report = None
        
        # Collect files to verify
        files_to_verify = []
        
        if file_paths:
            files_to_verify.extend(file_paths)
        
        if directory and os.path.isdir(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.endswith(".py"):  # Only process Python files
                        files_to_verify.append(os.path.join(root, file))
        
        if not files_to_verify:
            print("Error: No files to verify.")
            return None
        
        # Verify each file
        print(f"\n[*] Starting batch verification of {len(files_to_verify)} files")
        for file_path in files_to_verify:
            self.verify_code(file_path=file_path, timeout=timeout)
        
        # Create and export batch report
        self.create_batch_report()
        report_file = self.export_batch_report()
        
        # Visualize batch results if requested
        if visualize and QuantumAntiAILieLoopVisualizer:
            visualization_files = self.visualize_batch_results()
        
        return {
            "batch_report": self.batch_report,
            "report_file": report_file,
            "visualization_files": visualization_files if visualize and QuantumAntiAILieLoopVisualizer else None
        }

def main():
    """Main function to run the complete system from command line."""
    parser = argparse.ArgumentParser(description="Quantum Anti-AI Lie Loop Complete System")
    parser.add_argument("--file", "-f", type=str, help="Path to a Python file to verify")
    parser.add_argument("--dir", "-d", type=str, help="Path to a directory containing Python files to verify")
    parser.add_argument("--code", "-c", type=str, help="Python code string to verify")
    parser.add_argument("--timeout", "-t", type=int, default=10, help="Timeout for code execution in seconds")
    parser.add_argument("--output", "-o", type=str, default="quantum_verification_results", 
                        help="Output directory for reports and visualizations")
    parser.add_argument("--no-viz", action="store_true", help="Disable visualization generation")
    
    args = parser.parse_args()
    
    # Initialize the system
    system = QuantumAntiAILieLoopCompleteSystem(output_dir=args.output)
    
    # Check if we have the necessary components
    if not QuantumAntiAILieLoopExtended:
        print("Error: Verification component not available. Please install the required modules.")
        return 1
    
    if not args.no_viz and not QuantumAntiAILieLoopVisualizer:
        print("Warning: Visualization component not available. Visualizations will be skipped.")
    
    # Run verification based on input
    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File not found: {args.file}")
            return 1
        system.run_full_pipeline(file_path=args.file, timeout=args.timeout, visualize=not args.no_viz)
    
    elif args.dir:
        if not os.path.isdir(args.dir):
            print(f"Error: Directory not found: {args.dir}")
            return 1
        system.run_batch_pipeline(directory=args.dir, timeout=args.timeout, visualize=not args.no_viz)
    
    elif args.code:
        system.run_full_pipeline(code_str=args.code, timeout=args.timeout, visualize=not args.no_viz)
    
    else:
        print("Error: No input provided. Use --file, --dir, or --code to specify input.")
        parser.print_help()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
