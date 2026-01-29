#!/usr/bin/env python3
"""
Quantum Phi-Math Scanner

A utility for scanning directories of mathematical files and analyzing their
phi-harmonic properties using the Quantum Phi-Math Analyzer.
"""

import os
import sys
import json
import argparse
from typing import Dict, List, Any
import matplotlib.pyplot as plt
import numpy as np

# Import the Quantum Phi-Math Analyzer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phi_quantum_results.quantum_phi_math_analyser import QuantumPhiMathAnalyzer

class QuantumPhiMathScanner:
    """
    Scans directories of mathematical files and analyzes their phi-harmonic properties.
    """
    
    def __init__(self):
        """Initialize the Quantum Phi-Math Scanner."""
        self.analyzer = QuantumPhiMathAnalyzer()
        
        # File extensions to scan
        self.math_extensions = ['.py', '.txt', '.md', '.tex', '.m', '.r', '.ipynb', '.c', '.cpp', '.h']
        
        # Known mathematical constants and their expected metrics
        self.known_constants = {
            "phi": {"value": (1 + 5**0.5) / 2, "frequency": 1618.03, "resonance": 0.9999},
            "pi": {"value": 3.141592653589793, "frequency": 1414.21, "resonance": 0.8740},
            "e": {"value": 2.718281828459045, "frequency": 1271.83, "resonance": 0.7860},
            "sqrt2": {"value": 2**0.5, "frequency": 1273.24, "resonance": 0.7868},
            "sqrt3": {"value": 3**0.5, "frequency": 1316.55, "resonance": 0.8137},
            "sqrt5": {"value": 5**0.5, "frequency": 1381.97, "resonance": 0.8541},
        }
    
    def scan_directory(self, directory_path: str, recursive: bool = True) -> Dict[str, Any]:
        """
        Scan a directory for mathematical files and analyze them.
        
        Args:
            directory_path: Path to the directory to scan
            recursive: Whether to scan subdirectories recursively
            
        Returns:
            Dict containing analysis results
        """
        if not os.path.isdir(directory_path):
            return {"error": f"Directory not found: {directory_path}"}
        
        # Find all mathematical files
        math_files = []
        
        if recursive:
            for root, _, files in os.walk(directory_path):
                for file in files:
                    if any(file.endswith(ext) for ext in self.math_extensions):
                        math_files.append(os.path.join(root, file))
        else:
            for file in os.listdir(directory_path):
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path) and any(file.endswith(ext) for ext in self.math_extensions):
                    math_files.append(file_path)
        
        # Analyze each file
        results = []
        total_frequency = 0
        total_resonance = 0
        
        for file_path in math_files:
            print(f"Analyzing {file_path}...")
            analysis = self.analyzer.scan_file(file_path)
            results.append(analysis)
            
            if "avg_frequency" in analysis and "avg_resonance" in analysis:
                total_frequency += analysis["avg_frequency"]
                total_resonance += analysis["avg_resonance"]
        
        # Calculate average metrics
        num_files = len(math_files) or 1
        avg_frequency = total_frequency / num_files
        avg_resonance = total_resonance / num_files
        
        # Determine consciousness level
        consciousness_level = self.analyzer._get_consciousness_level(avg_frequency)
        
        return {
            "directory_path": directory_path,
            "num_files": len(math_files),
            "files": math_files,
            "results": results,
            "avg_frequency": avg_frequency,
            "avg_resonance": avg_resonance,
            "consciousness_level": consciousness_level,
            "phi_alignment": avg_resonance * 0.95
        }
    
    def test_accuracy(self) -> Dict[str, Any]:
        """
        Test the accuracy of the phi frequency calculations against known constants.
        
        Returns:
            Dict containing accuracy metrics
        """
        test_cases = []
        
        # Test known constants
        for const_name, const_data in self.known_constants.items():
            test_cases.append({
                "value": const_data["value"],
                "expected": {
                    "frequency": const_data["frequency"],
                    "resonance": const_data["resonance"]
                }
            })
        
        # Test mathematical expressions
        test_expressions = [
            {"value": "phi^2 = phi + 1", "expected": {"frequency": 669.34, "resonance": 0.8500}},
            {"value": "e^(i*pi) + 1 = 0", "expected": {"frequency": 704.01, "resonance": 0.7388}},
            {"value": "a^2 + b^2 = c^2", "expected": {"frequency": 260.00, "resonance": 0.6250}},
            {"value": "F_n = (phi^n - (1-phi)^n)/sqrt(5)", "expected": {"frequency": 799.34, "resonance": 0.8500}},
            {"value": "E = mc^2", "expected": {"frequency": 260.00, "resonance": 0.7250}},
            {"value": "phi = (1 + sqrt(5))/2", "expected": {"frequency": 664.51, "resonance": 0.8437}}
        ]
        
        test_cases.extend(test_expressions)
        
        return self.analyzer.test_accuracy(test_cases)
    
    def generate_report(self, results: Dict[str, Any], output_file: str = None) -> None:
        """
        Generate a report from the scan results.
        
        Args:
            results: Scan results
            output_file: Path to the output file (optional)
        """
        report = []
        
        report.append("="*80)
        report.append("Quantum Phi-Math Scanner Report".center(80))
        report.append("="*80)
        report.append("")
        
        # Directory summary
        report.append(f"Directory: {results['directory_path']}")
        report.append(f"Files Analyzed: {results['num_files']}")
        report.append(f"Average Frequency: {results['avg_frequency']:.2f} Hz")
        report.append(f"Average Resonance: {results['avg_resonance']:.4f}")
        report.append(f"Consciousness Level: {results['consciousness_level']}")
        report.append(f"Phi Alignment: {results['phi_alignment']:.4f}")
        report.append("")
        
        # Top files by resonance
        sorted_results = sorted(results['results'], key=lambda x: x.get('avg_resonance', 0), reverse=True)
        
        report.append("Top Files by Phi Resonance:")
        report.append("-"*80)
        for i, res in enumerate(sorted_results[:10]):
            if i >= len(sorted_results):
                break
            file_name = os.path.basename(res['file_path'])
            report.append(f"{i+1}. {file_name}: Frequency={res.get('avg_frequency', 0):.2f}Hz, "
                         f"Resonance={res.get('avg_resonance', 0):.4f}, "
                         f"Level={res.get('consciousness_level', 'unknown')}")
        report.append("")
        
        # Top expressions by resonance
        all_expressions = []
        for res in results['results']:
            for expr in res.get('expressions', []):
                all_expressions.append({
                    "file": os.path.basename(res['file_path']),
                    "expression": expr.get('expression', ''),
                    "frequency": expr.get('avg_frequency', 0),
                    "resonance": expr.get('combined_resonance', 0),
                    "level": expr.get('consciousness_level', 'unknown')
                })
        
        sorted_expressions = sorted(all_expressions, key=lambda x: x['resonance'], reverse=True)
        
        report.append("Top Mathematical Expressions by Phi Resonance:")
        report.append("-"*80)
        for i, expr in enumerate(sorted_expressions[:15]):
            if i >= len(sorted_expressions):
                break
            report.append(f"{i+1}. {expr['expression']} (from {expr['file']})")
            report.append(f"   Frequency={expr['frequency']:.2f}Hz, "
                         f"Resonance={expr['resonance']:.4f}, "
                         f"Level={expr['level']}")
        
        # Output the report
        report_text = "\n".join(report)
        print(report_text)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_text)
            print(f"\nReport saved to {output_file}")
    
    def visualize_results(self, results: Dict[str, Any], output_file: str = None) -> None:
        """
        Visualize the scan results.
        
        Args:
            results: Scan results
            output_file: Path to the output file (optional)
        """
        # Extract data for visualization
        file_names = [os.path.basename(res['file_path']) for res in results['results']]
        frequencies = [res.get('avg_frequency', 0) for res in results['results']]
        resonances = [res.get('avg_resonance', 0) for res in results['results']]
        
        # Create a figure with multiple subplots
        fig, axs = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Quantum Phi-Math Analysis Results', fontsize=16)
        
        # Plot 1: Frequency distribution
        axs[0, 0].hist(frequencies, bins=20, alpha=0.7, color='blue')
        axs[0, 0].set_title('Frequency Distribution')
        axs[0, 0].set_xlabel('Frequency (Hz)')
        axs[0, 0].set_ylabel('Number of Files')
        axs[0, 0].grid(True, linestyle='--', alpha=0.7)
        
        # Plot 2: Resonance distribution
        axs[0, 1].hist(resonances, bins=20, alpha=0.7, color='green')
        axs[0, 1].set_title('Resonance Distribution')
        axs[0, 1].set_xlabel('Resonance')
        axs[0, 1].set_ylabel('Number of Files')
        axs[0, 1].grid(True, linestyle='--', alpha=0.7)
        
        # Plot 3: Frequency vs Resonance scatter plot
        axs[1, 0].scatter(frequencies, resonances, alpha=0.7, c=resonances, cmap='viridis')
        axs[1, 0].set_title('Frequency vs Resonance')
        axs[1, 0].set_xlabel('Frequency (Hz)')
        axs[1, 0].set_ylabel('Resonance')
        axs[1, 0].grid(True, linestyle='--', alpha=0.7)
        
        # Add reference lines for consciousness levels
        consciousness_levels = self.analyzer.consciousness_levels
        for level, (min_freq, max_freq) in consciousness_levels.items():
            axs[1, 0].axvline(x=min_freq, color='red', linestyle='--', alpha=0.3)
            axs[1, 0].text(min_freq, 0.1, level, rotation=90, alpha=0.7)
        
        # Plot 4: Top files by resonance
        sorted_indices = np.argsort(resonances)[::-1][:10]
        top_files = [file_names[i] for i in sorted_indices]
        top_resonances = [resonances[i] for i in sorted_indices]
        
        axs[1, 1].barh(top_files, top_resonances, alpha=0.7, color='purple')
        axs[1, 1].set_title('Top Files by Resonance')
        axs[1, 1].set_xlabel('Resonance')
        axs[1, 1].set_xlim(0, 1)
        axs[1, 1].grid(True, linestyle='--', alpha=0.7)
        
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        
        if output_file:
            plt.savefig(output_file)
            print(f"\nVisualization saved to {output_file}")
        else:
            plt.show()


def main():
    """Main function to run the Quantum Phi-Math Scanner."""
    parser = argparse.ArgumentParser(description='Quantum Phi-Math Scanner')
    parser.add_argument('directory', nargs='?', default='.', 
                        help='Directory to scan (default: current directory)')
    parser.add_argument('--no-recursive', dest='recursive', action='store_false',
                        help='Do not scan subdirectories recursively')
    parser.add_argument('--report', dest='report_file', 
                        help='Save report to file')
    parser.add_argument('--visualize', dest='visualize_file',
                        help='Save visualization to file')
    parser.add_argument('--test-accuracy', dest='test_accuracy', action='store_true',
                        help='Test accuracy against known constants')
    
    args = parser.parse_args()
    
    scanner = QuantumPhiMathScanner()
    
    if args.test_accuracy:
        print("\nTesting accuracy against known constants...")
        accuracy_results = scanner.test_accuracy()
        print(f"Average Accuracy: {accuracy_results['avg_accuracy']:.4f}")
        print(f"Test Cases: {accuracy_results['test_cases']}")
        return
    
    print(f"\nScanning directory: {args.directory}")
    results = scanner.scan_directory(args.directory, args.recursive)
    
    if 'error' in results:
        print(f"Error: {results['error']}")
        return
    
    scanner.generate_report(results, args.report_file)
    
    if args.visualize_file or not args.report_file:
        try:
            scanner.visualize_results(results, args.visualize_file)
        except Exception as e:
            print(f"Error generating visualization: {e}")


if __name__ == "__main__":
    main()
