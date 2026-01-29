#!/usr/bin/env python3
"""
Quantum Lie Detector Test - Quantum Phi-Harmonic System
By Vaughn Scott (Enhanced by Cascade)

This script tests the Quantum Anti-AI Lie Loop system's ability to detect deceptive information
in the quantum_deceptive_test.py file and stores the detection results using our
QR Phi-Memory Compact system for persistent memory.
"""

import os
import sys
import json
import math
import importlib.util
from datetime import datetime

# Import constants from the original system
# The correct constants are essential for detecting lies
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ) ≈ 1.618034
PI = 3.141592653589793  # π
E = 2.718281828459045   # e

# Try to import our QR memory system
try:
    from qr_phi_memory_compact import QRPhiMemoryCompact
    qr_memory_available = True
except ImportError:
    print("Warning: QR Phi-Memory Compact system not found")
    qr_memory_available = False

class QuantumLieDetector:
    """
    A class that implements quantum phi-harmonic principles to detect lies and deception
    in mathematical and quantum physics statements.
    """
    
    def __init__(self, memory_file="quantum_lie_detector_memory.json"):
        """Initialize the Quantum Lie Detector system."""
        self.memory_file = memory_file
        self.detection_history = []
        self.phi_resonance_patterns = []
        self.truth_metrics = {}
        
        # Initialize QR memory system if available
        self.qr_memory = None
        if qr_memory_available:
            self.qr_memory = QRPhiMemoryCompact(memory_file)
            print(f"Initialized QR Phi-Memory Compact system with {memory_file}")
    
    def phi_resonance(self, value):
        """
        Calculate phi-harmonic resonance of a value using the correct PHI constant.
        
        Args:
            value: Input value
            
        Returns:
            Phi-resonance measure (0.0-1.0)
        """
        return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))
    
    def detect_constant_lies(self, module_constants):
        """
        Detect lies in mathematical constants.
        
        Args:
            module_constants: Dictionary of constants from the module
            
        Returns:
            Dictionary of detected lies in constants
        """
        constant_lies = {}
        
        # Check PHI constant
        if 'PHI' in module_constants:
            phi_value = module_constants['PHI']
            phi_error = abs(phi_value - PHI) / PHI
            phi_is_lie = phi_error > 0.01  # More than 1% error
            
            constant_lies['PHI'] = {
                'claimed_value': phi_value,
                'correct_value': PHI,
                'error_percentage': phi_error * 100,
                'is_lie': phi_is_lie,
                'phi_resonance': self.phi_resonance(phi_error)
            }
        
        # Check PI constant
        if 'PI' in module_constants:
            pi_value = module_constants['PI']
            pi_error = abs(pi_value - PI) / PI
            pi_is_lie = pi_error > 0.01  # More than 1% error
            
            constant_lies['PI'] = {
                'claimed_value': pi_value,
                'correct_value': PI,
                'error_percentage': pi_error * 100,
                'is_lie': pi_is_lie,
                'phi_resonance': self.phi_resonance(pi_error)
            }
        
        # Check E constant
        if 'E' in module_constants:
            e_value = module_constants['E']
            e_error = abs(e_value - E) / E
            e_is_lie = e_error > 0.01  # More than 1% error
            
            constant_lies['E'] = {
                'claimed_value': e_value,
                'correct_value': E,
                'error_percentage': e_error * 100,
                'is_lie': e_is_lie,
                'phi_resonance': self.phi_resonance(e_error)
            }
        
        return constant_lies
    
    def detect_quantum_principle_lies(self, principles):
        """
        Detect lies in quantum principles.
        
        Args:
            principles: Dictionary of quantum principles
            
        Returns:
            Dictionary of detected lies in principles
        """
        principle_lies = {}
        
        # Known false principles and their corrections
        truth_principles = {
            "quantum_entanglement": "Quantum entanglement does not allow faster-than-light communication",
            "heisenberg": "The Heisenberg uncertainty principle is a fundamental property of quantum systems, not just measurement limitations",
            "quantum_computing": "Quantum computers can provide quadratic or exponential speedup for specific problems, but not all NP-hard problems",
            "phi_resonance": "Phi resonance is related to the golden ratio (approximately 1.618034), not 1.5",
            "quantum_consciousness": "There is no scientific consensus that quantum effects explain consciousness"
        }
        
        # Check each principle
        for key, value in principles.items():
            if key in truth_principles:
                principle_lies[key] = {
                    'claimed': value,
                    'correction': truth_principles[key],
                    'is_lie': True,
                    'phi_resonance': self.phi_resonance(len(value) / len(truth_principles[key]))
                }
        
        return principle_lies
    
    def analyze_deceptive_report(self, report):
        """
        Analyze a potentially deceptive report for lies and misinformation.
        
        Args:
            report: Dictionary containing the report
            
        Returns:
            Dictionary of analysis results
        """
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'report_title': report.get('title', 'Unknown'),
            'constant_lies': {},
            'principle_lies': {},
            'calculation_errors': [],
            'overall_deception_score': 0.0,
            'phi_resonance': 0.0
        }
        
        # Check constants in the report
        constants = {
            'PHI': report.get('phi_constant'),
            'PI': report.get('pi_constant'),
            'E': report.get('e_constant')
        }
        
        analysis['constant_lies'] = self.detect_constant_lies(constants)
        
        # Check principles if available
        if 'principles' in report:
            analysis['principle_lies'] = self.detect_quantum_principle_lies(report['principles'])
        
        # Check for calculation errors in quantum states
        if 'quantum_states' in report:
            for state_key, state_data in report['quantum_states'].items():
                if 'phi_resonance' in state_data:
                    claimed_resonance = state_data['phi_resonance']
                    correct_resonance = self.phi_resonance(state_data.get('value', 0))
                    resonance_error = abs(claimed_resonance - correct_resonance)
                    
                    if resonance_error > 0.1:  # Significant error
                        analysis['calculation_errors'].append({
                            'state': state_key,
                            'type': 'phi_resonance',
                            'claimed_value': claimed_resonance,
                            'correct_value': correct_resonance,
                            'error': resonance_error
                        })
        
        # Calculate overall deception score
        lie_count = 0
        lie_count += sum(1 for _, data in analysis['constant_lies'].items() if data.get('is_lie', False))
        lie_count += sum(1 for _, data in analysis['principle_lies'].items() if data.get('is_lie', False))
        lie_count += len(analysis['calculation_errors'])
        
        # Phi-harmonic deception score
        analysis['overall_deception_score'] = 1.0 - 1.0 / (1.0 + lie_count * 0.1)
        analysis['phi_resonance'] = self.phi_resonance(lie_count)
        
        return analysis
    
    def detect_lies_in_module(self, module_path):
        """
        Detect lies in a Python module.
        
        Args:
            module_path: Path to the Python module
            
        Returns:
            Dictionary of detection results
        """
        try:
            # Extract constants directly from the file
            module_constants = {}
            with open(module_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith(('PHI', 'PI', 'E')) and '=' in line:
                        parts = line.split('=', 1)
                        if len(parts) == 2:
                            const_name = parts[0].strip()
                            # Extract the value, handling potential comments
                            value_part = parts[1].split('#')[0].strip()
                            try:
                                const_value = float(value_part)
                                module_constants[const_name] = const_value
                            except ValueError:
                                pass
            
            # Check for deceptive report
            report_path = "quantum_deceptive_report.json"
            if os.path.exists(report_path):
                with open(report_path, 'r') as f:
                    report = json.load(f)
                    
                analysis = self.analyze_deceptive_report(report)
            else:
                # If no report, just analyze constants
                analysis = {
                    'timestamp': datetime.now().isoformat(),
                    'module_name': os.path.basename(module_path),
                    'constant_lies': self.detect_constant_lies(module_constants),
                    'overall_deception_score': 0.0,
                    'phi_resonance': 0.0
                }
            
            # Calculate overall deception score if not already set
            if analysis['overall_deception_score'] == 0.0:
                lie_count = sum(1 for _, data in analysis['constant_lies'].items() if data.get('is_lie', False))
                analysis['overall_deception_score'] = 1.0 - 1.0 / (1.0 + lie_count * 0.1)
                analysis['phi_resonance'] = self.phi_resonance(lie_count)
            
            # Store detection in history
            self.detection_history.append(analysis)
            
            # Update QR memory if available
            if self.qr_memory:
                self.qr_memory.phi_states = {'lie_detection': analysis}
                self.qr_memory.execution_history = self.detection_history
                self.qr_memory.resonance_patterns.append(analysis['phi_resonance'])
                self.qr_memory.save_memory()
            
            return analysis
            
        except Exception as e:
            print(f"Error analyzing module: {e}")
            error_result = {
                'error': str(e),
                'timestamp': datetime.now().isoformat(),
                'overall_deception_score': 0.5,  # Default score for error case
                'phi_resonance': 0.5,
                'constant_lies': {},
                'principle_lies': {}
            }
            return error_result
    
    def generate_qr_memory_backup(self, output_dir="qr_lie_detector_backup"):
        """
        Generate QR code backup of the lie detection results.
        
        Args:
            output_dir: Directory to save QR codes
            
        Returns:
            True if successful, False otherwise
        """
        if not self.qr_memory:
            print("QR memory system not available")
            return False
        
        return self.qr_memory.generate_memory_qr_codes(output_dir)

def main():
    """Main function to run the Quantum Lie Detector test."""
    parser = import_argparse()
    args = parser.parse_args()
    
    print("Quantum Lie Detector Test - Quantum Phi-Harmonic System")
    print("By Vaughn Scott (Enhanced by Cascade)")
    
    detector = QuantumLieDetector(args.memory_file)
    
    if args.analyze_module:
        print(f"Analyzing module: {args.analyze_module}")
        results = detector.detect_lies_in_module(args.analyze_module)
        
        print("\n=== Lie Detection Results ===")
        print(f"Overall Deception Score: {results['overall_deception_score']:.4f}")
        print(f"Phi-Resonance: {results['phi_resonance']:.6f}")
        
        if 'constant_lies' in results:
            print("\nConstant Lies Detected:")
            for const, data in results['constant_lies'].items():
                if data.get('is_lie', False):
                    print(f"  - {const}: Claimed {data['claimed_value']} (Correct: {data['correct_value']:.6f}, Error: {data['error_percentage']:.2f}%)")
        
        if 'principle_lies' in results:
            print("\nPrinciple Lies Detected:")
            for principle, data in results['principle_lies'].items():
                if data.get('is_lie', False):
                    print(f"  - {principle}: {data['claimed']}")
                    print(f"    Correction: {data['correction']}")
        
        if 'calculation_errors' in results:
            print("\nCalculation Errors Detected:")
            for error in results.get('calculation_errors', []):
                print(f"  - {error['state']}: {error['type']} error of {error['error']:.4f}")
    
    if args.generate_qr:
        print(f"\nGenerating QR memory backup to {args.qr_dir}")
        detector.generate_qr_memory_backup(args.qr_dir)

def import_argparse():
    """Import argparse and create parser."""
    import argparse
    parser = argparse.ArgumentParser(description="Quantum Lie Detector Test")
    parser.add_argument("--analyze-module", default="quantum_deceptive_test.py", help="Python module to analyze")
    parser.add_argument("--memory-file", default="quantum_lie_detector_memory.json", help="Memory file path")
    parser.add_argument("--generate-qr", action="store_true", help="Generate QR memory backup")
    parser.add_argument("--qr-dir", default="qr_lie_detector_backup", help="QR directory for backup")
    return parser

if __name__ == "__main__":
    main()
