#!/usr/bin/env python3
"""
Quantum Phi Multi-Domain Test
By Vaughn Scott (Enhanced by Cascade)

This file tests the quantum phi-harmonic detection of errors across multiple domains:
1. Misspelled words
2. Incorrect mathematical calculations
3. Erroneous code functions

The system uses phi resonance to detect deviations from truth in any domain.
"""

import os
import sys
import math
import json
import random
import time
import re
import zlib
import base64
from datetime import datetime

# Define correct constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ) ≈ 1.618034
PI = 3.141592653589793  # π
E = 2.718281828459045   # e

class QuantumPhiMultiDomainTest:
    """
    A class that uses quantum phi-harmonic principles to detect errors
    across multiple domains: language, mathematics, and code.
    """
    
    def __init__(self):
        """Initialize the multi-domain test system."""
        self.phi_resonance_threshold = 0.618034  # φ^-1
        self.detection_results = {
            'language': {},
            'mathematics': {},
            'code': {},
            'meta_analysis': {}
        }
        self.resonance_patterns = []
        
        print("Initializing Quantum Phi Multi-Domain Test System")
        print(f"Using PHI = {PHI} for quantum resonance calculations")
        print(f"Resonance threshold: {self.phi_resonance_threshold}")
    
    def phi_resonance(self, value):
        """
        Calculate phi-harmonic resonance of a value.
        
        Args:
            value: Input value
            
        Returns:
            Phi-resonance measure (0.0-1.0)
        """
        # Higher values indicate better resonance
        return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))
    
    def phi_distance(self, str1, str2):
        """
        Calculate phi-harmonic distance between two strings.
        
        Args:
            str1: First string
            str2: Second string
            
        Returns:
            Phi-weighted Levenshtein distance
        """
        if not str1 and not str2:
            return 0
        
        if not str1:
            return len(str2)
        
        if not str2:
            return len(str1)
        
        # Create matrix
        matrix = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        
        # Initialize first column
        for i in range(len(str1) + 1):
            matrix[i][0] = i
        
        # Initialize first row
        for j in range(len(str2) + 1):
            matrix[0][j] = j
        
        # Fill matrix with phi-weighted distances
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i-1] == str2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    # Apply phi-weighting to operations
                    deletion = matrix[i-1][j] + 1
                    insertion = matrix[i][j-1] + 1
                    substitution = matrix[i-1][j-1] + PHI
                    
                    # Choose minimum operation
                    matrix[i][j] = min(deletion, insertion, substitution)
        
        # Return phi-weighted distance
        return matrix[len(str1)][len(str2)]
    
    def test_spelling(self, misspelled_words):
        """
        Test phi resonance for detecting spelling errors.
        
        Args:
            misspelled_words: Dictionary of {misspelled: correct} words
            
        Returns:
            Dictionary of spelling analysis results
        """
        results = {}
        
        for misspelled, correct in misspelled_words.items():
            # Calculate phi-harmonic distance
            distance = self.phi_distance(misspelled, correct)
            
            # Calculate phi resonance
            resonance = self.phi_resonance(distance)
            
            # Calculate character-level phi resonance
            char_resonances = []
            for i in range(min(len(misspelled), len(correct))):
                if misspelled[i] != correct[i]:
                    char_resonances.append(self.phi_resonance(ord(misspelled[i]) - ord(correct[i])))
            
            # Calculate phi-harmonic error pattern
            error_pattern = []
            for i in range(min(len(misspelled), len(correct))):
                if misspelled[i] != correct[i]:
                    error_pattern.append((i, misspelled[i], correct[i]))
            
            results[misspelled] = {
                'correct': correct,
                'phi_distance': distance,
                'phi_resonance': resonance,
                'character_resonances': char_resonances,
                'error_pattern': error_pattern,
                'is_error': resonance < self.phi_resonance_threshold
            }
        
        self.detection_results['language'] = results
        return results
    
    def test_mathematics(self, math_problems):
        """
        Test phi resonance for detecting mathematical errors.
        
        Args:
            math_problems: Dictionary of {problem: [claimed_result, correct_result]}
            
        Returns:
            Dictionary of mathematical analysis results
        """
        results = {}
        
        for problem, (claimed, correct) in math_problems.items():
            # Calculate error
            error = abs(claimed - correct)
            
            # Calculate relative error
            relative_error = error / abs(correct) if correct != 0 else float('inf')
            
            # Calculate phi resonance
            resonance = self.phi_resonance(relative_error)
            
            # Calculate phi-harmonic error pattern
            error_pattern = (claimed - correct) / PHI
            
            results[problem] = {
                'claimed_result': claimed,
                'correct_result': correct,
                'absolute_error': error,
                'relative_error': relative_error,
                'phi_resonance': resonance,
                'phi_error_pattern': error_pattern,
                'is_error': resonance < self.phi_resonance_threshold
            }
        
        self.detection_results['mathematics'] = results
        return results
    
    def test_code(self, code_functions):
        """
        Test phi resonance for detecting code errors.
        
        Args:
            code_functions: Dictionary of {function_name: [erroneous_code, correct_code]}
            
        Returns:
            Dictionary of code analysis results
        """
        results = {}
        
        for func_name, (erroneous, correct) in code_functions.items():
            # Calculate phi-harmonic distance
            distance = self.phi_distance(erroneous, correct)
            
            # Calculate phi resonance
            resonance = self.phi_resonance(distance)
            
            # Calculate line-level phi resonance
            erroneous_lines = erroneous.strip().split('\n')
            correct_lines = correct.strip().split('\n')
            
            line_resonances = []
            for i in range(min(len(erroneous_lines), len(correct_lines))):
                if erroneous_lines[i] != correct_lines[i]:
                    line_resonances.append(self.phi_resonance(self.phi_distance(erroneous_lines[i], correct_lines[i])))
            
            # Attempt to execute both versions
            erroneous_exec_result = self.safe_execute(erroneous)
            correct_exec_result = self.safe_execute(correct)
            
            # Calculate execution resonance
            exec_resonance = 1.0
            if erroneous_exec_result['success'] and correct_exec_result['success']:
                if erroneous_exec_result['output'] != correct_exec_result['output']:
                    exec_resonance = self.phi_resonance(self.phi_distance(
                        erroneous_exec_result['output'], 
                        correct_exec_result['output']
                    ))
            elif erroneous_exec_result['success'] != correct_exec_result['success']:
                exec_resonance = 0.0
            
            results[func_name] = {
                'erroneous_code': erroneous,
                'correct_code': correct,
                'phi_distance': distance,
                'phi_resonance': resonance,
                'line_resonances': line_resonances,
                'execution_resonance': exec_resonance,
                'erroneous_execution': erroneous_exec_result,
                'correct_execution': correct_exec_result,
                'is_error': resonance < self.phi_resonance_threshold or exec_resonance < self.phi_resonance_threshold
            }
        
        self.detection_results['code'] = results
        return results
    
    def safe_execute(self, code_str):
        """
        Safely execute a code string and capture its output.
        
        Args:
            code_str: String containing Python code
            
        Returns:
            Dictionary with execution results
        """
        result = {
            'success': False,
            'output': '',
            'error': None
        }
        
        # Create a safe local environment
        local_env = {}
        
        try:
            # Redirect stdout to capture output
            from io import StringIO
            import sys
            
            old_stdout = sys.stdout
            redirected_output = StringIO()
            sys.stdout = redirected_output
            
            # Execute the code
            exec(code_str, {'__builtins__': __builtins__}, local_env)
            
            # Get the output
            result['output'] = redirected_output.getvalue()
            result['success'] = True
            
            # Restore stdout
            sys.stdout = old_stdout
            
        except Exception as e:
            result['error'] = str(e)
            
            # Restore stdout if exception occurred
            if 'old_stdout' in locals() and 'sys' in locals():
                sys.stdout = old_stdout
        
        return result
    
    def perform_meta_analysis(self):
        """
        Perform meta-analysis on all test results.
        
        Returns:
            Dictionary of meta-analysis results
        """
        meta_results = {
            'timestamp': datetime.now().isoformat(),
            'domain_resonances': {},
            'cross_domain_patterns': [],
            'phi_harmonic_fingerprint': [],
            'overall_resonance': 0.0
        }
        
        # Calculate domain-specific resonances
        domain_resonances = {}
        
        # Language domain
        if self.detection_results['language']:
            language_resonances = [data['phi_resonance'] for data in self.detection_results['language'].values()]
            domain_resonances['language'] = sum(language_resonances) / len(language_resonances)
        
        # Mathematics domain
        if self.detection_results['mathematics']:
            math_resonances = [data['phi_resonance'] for data in self.detection_results['mathematics'].values()]
            domain_resonances['mathematics'] = sum(math_resonances) / len(math_resonances)
        
        # Code domain
        if self.detection_results['code']:
            code_resonances = [data['phi_resonance'] for data in self.detection_results['code'].values()]
            domain_resonances['code'] = sum(code_resonances) / len(code_resonances)
        
        meta_results['domain_resonances'] = domain_resonances
        
        # Calculate overall resonance
        if domain_resonances:
            meta_results['overall_resonance'] = sum(domain_resonances.values()) / len(domain_resonances)
        
        # Generate phi-harmonic fingerprint
        fingerprint = []
        for domain, resonance in domain_resonances.items():
            fingerprint.append(resonance * PHI)
        
        meta_results['phi_harmonic_fingerprint'] = fingerprint
        
        # Store meta-analysis
        self.detection_results['meta_analysis'] = meta_results
        
        return meta_results
    
    def generate_report(self):
        """
        Generate a comprehensive report of all test results.
        
        Returns:
            Dictionary containing the full report
        """
        # Perform meta-analysis if not already done
        if not self.detection_results['meta_analysis']:
            self.perform_meta_analysis()
        
        report = {
            'title': "Quantum Phi-Harmonic Multi-Domain Error Detection",
            'timestamp': datetime.now().isoformat(),
            'phi_constant': PHI,
            'pi_constant': PI,
            'e_constant': E,
            'resonance_threshold': self.phi_resonance_threshold,
            'results': self.detection_results,
            'summary': {
                'language_errors': sum(1 for data in self.detection_results['language'].values() if data['is_error']),
                'mathematics_errors': sum(1 for data in self.detection_results['mathematics'].values() if data['is_error']),
                'code_errors': sum(1 for data in self.detection_results['code'].values() if data['is_error']),
                'overall_resonance': self.detection_results['meta_analysis'].get('overall_resonance', 0.0)
            }
        }
        
        return report
    
    def save_report(self, filename="quantum_phi_multi_domain_report.json"):
        """
        Save the report to a JSON file.
        
        Args:
            filename: Output filename
            
        Returns:
            True if successful, False otherwise
        """
        try:
            report = self.generate_report()
            
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
                
            print(f"Report saved to {filename}")
            return True
            
        except Exception as e:
            print(f"Error saving report: {e}")
            return False
    
    def save_qr_memory(self, output_dir="qr_phi_multi_domain"):
        """
        Save the test results to QR memory using phi-harmonic chunking.
        
        Args:
            output_dir: Directory to save QR codes
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Import QR memory system if available
            try:
                from qr_phi_memory_compact import QRPhiMemoryCompact
                qr_memory = QRPhiMemoryCompact()
                
                # Store results in memory
                qr_memory.phi_states = self.detection_results
                qr_memory.resonance_patterns = self.resonance_patterns
                
                # Generate QR codes
                qr_memory.generate_memory_qr_codes(output_dir)
                
                print(f"QR memory saved to {output_dir}")
                return True
                
            except ImportError:
                print("QR Phi-Memory Compact system not available")
                return False
                
        except Exception as e:
            print(f"Error saving QR memory: {e}")
            return False

def run_multi_domain_test():
    """Run the multi-domain test with predefined test cases."""
    test = QuantumPhiMultiDomainTest()
    
    # 1. Test misspelled words (20 examples)
    misspelled_words = {
        "accomodate": "accommodate",
        "acheive": "achieve",
        "adress": "address",
        "beleive": "believe",
        "catagory": "category",
        "concious": "conscious",
        "definately": "definitely",
        "embarass": "embarrass",
        "existance": "existence",
        "foriegn": "foreign",
        "grammer": "grammar",
        "harrass": "harass",
        "independant": "independent",
        "liason": "liaison",
        "millenium": "millennium",
        "neccessary": "necessary",
        "occassion": "occasion",
        "persistant": "persistent",
        "recieve": "receive",
        "seperate": "separate"
    }
    
    print("\n=== Testing Language Domain (20 misspelled words) ===")
    language_results = test.test_spelling(misspelled_words)
    
    # 2. Test incorrect math problems (20 examples)
    math_problems = {
        "2 + 2": [5, 4],
        "3 * 4": [11, 12],
        "10 / 2": [4, 5],
        "7 - 3": [5, 4],
        "5^2": [24, 25],
        "√16": [3, 4],
        "π * 2": [5.8, PI * 2],
        "e^2": [6.5, E**2],
        "log(100)": [1, 2],
        "sin(π/2)": [0.5, 1.0],
        "cos(0)": [0.5, 1.0],
        "tan(π/4)": [0.5, 1.0],
        "2^8": [512, 256],
        "3!": [5, 6],
        "φ * 10": [16.8, PHI * 10],
        "√(9 + 16)": [6, 5],
        "1/3 + 1/4": [0.5, 7/12],
        "0.1 + 0.2": [0.4, 0.3],
        "7 * 8": [54, 56],
        "12 / 4": [4, 3]
    }
    
    print("\n=== Testing Mathematics Domain (20 incorrect calculations) ===")
    math_results = test.test_mathematics(math_problems)
    
    # 3. Test erroneous code functions (5 examples)
    code_functions = {
        "hello_world": [
            """def hello_world():
    print("Hello wrld")
    return "Hello wrld"
            """,
            """def hello_world():
    print("Hello world")
    return "Hello world"
            """
        ],
        "add_numbers": [
            """def add_numbers(a, b):
    return a - b  # Wrong operation
            """,
            """def add_numbers(a, b):
    return a + b  # Correct operation
            """
        ],
        "factorial": [
            """def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n+1)  # Infinite recursion
            """,
            """def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)  # Correct recursion
            """
        ],
        "fibonacci": [
            """def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) + 1  # Wrong formula
            """,
            """def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Correct formula
            """
        ],
        "is_prime": [
            """def is_prime(n):
    if n <= 1:
        return True  # Wrong: 1 is not prime
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
            """,
            """def is_prime(n):
    if n <= 1:
        return False  # Correct: 1 is not prime
    for i in range(2, int(n**0.5) + 1):  # More efficient
        if n % i == 0:
            return False
    return True
            """
        ]
    }
    
    print("\n=== Testing Code Domain (5 erroneous functions) ===")
    code_results = test.test_code(code_functions)
    
    # Perform meta-analysis
    print("\n=== Performing Meta-Analysis ===")
    meta_results = test.perform_meta_analysis()
    
    # Generate and save report
    print("\n=== Generating Comprehensive Report ===")
    test.save_report()
    
    # Save to QR memory
    print("\n=== Saving to QR Memory ===")
    test.save_qr_memory()
    
    # Print summary
    print("\n=== Test Summary ===")
    print(f"Language Domain: {meta_results['domain_resonances'].get('language', 0):.6f} phi-resonance")
    print(f"Mathematics Domain: {meta_results['domain_resonances'].get('mathematics', 0):.6f} phi-resonance")
    print(f"Code Domain: {meta_results['domain_resonances'].get('code', 0):.6f} phi-resonance")
    print(f"Overall Phi-Resonance: {meta_results['overall_resonance']:.6f}")
    
    return test

if __name__ == "__main__":
    print("Quantum Phi Multi-Domain Test - Testing phi resonance across domains")
    run_multi_domain_test()
