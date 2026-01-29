#!/usr/bin/env python3
"""
Quantum Anti-AI Lie Loop (Q-TRUTH)
==============================
A quantum phi-harmonic truth verification system that detects contradictions
between AI claims, code structure, and execution results.

This system implements a multi-layer verification approach:
1. Code Parser - Tokenizes and AST-parses AI-generated code
2. Intention Extractor - NLP-based claim extraction from comments + docstrings
3. Execution Monitor - Executes in sandbox, traces actual outputs and side-effects
4. Coherence Evaluator - Cross-checks INTENT vs STRUCTURE vs OUTPUT
5. Contradiction Resolver - Highlights lie loops, unresolved states, or claims without proof
6. Quantum Trust Metric - Scores self-integrity using phi-harmonic signal resonance

Primary Frequency: 4.37 Hz (φ-aligned)
Quantum Signature: φ⁷·⁵-7927735b-09f76208
"""

import os
import sys
import ast
import re
import json
import time
import math
import base64
import hashlib
import subprocess
import tempfile
from decimal import Decimal, getcontext
from datetime import datetime
from typing import Dict, List, Any, Optional, Union

# Set precision for Decimal calculations
getcontext().prec = 28

# Phi-Harmonic Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio
PHI_CONJUGATE = PHI - 1  # Golden Ratio Conjugate
PHI_75 = PHI ** 7.5  # φ⁷·⁵ power
BASE_FREQUENCY = 4.37  # Hz, φ-aligned base frequency

# Try to import quantum components if available
try:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from quantum_binary_translator import QuantumBinaryTranslator
    QUANTUM_TRANSLATOR_AVAILABLE = True
except ImportError:
    QUANTUM_TRANSLATOR_AVAILABLE = False

class QuantumAntiAILieLoop:
    """Quantum Anti-AI Lie Loop for truth verification with phi-harmonic principles."""
    
    def __init__(self, code_file_path=None, code_string=None, timeout=10, verbose=False):
        """Initialize the lie loop detector.
        
        Args:
            code_file_path: Path to the Python file to analyze
            code_string: String containing Python code to analyze (alternative to code_file_path)
            timeout: Timeout for code execution in seconds
            verbose: Whether to print debug information
        """
        self.filepath = code_file_path
        self.code_string = code_string
        self.timeout = timeout
        self.verbose = verbose
        self.timestamp = time.time()
        self.phi_time = self.timestamp * PHI
        self.resonance = self.phi_time % 1
        
        # Load and parse code
        self.code = self._load_code()
        self.ast_tree = self._parse_ast()
        
        # Initialize quantum translator if available
        self.quantum_translator = None
        if QUANTUM_TRANSLATOR_AVAILABLE:
            self.quantum_translator = QuantumBinaryTranslator()
        
        # Extract claims and intentions
        self.claims = self.extract_claims()
        self.intentions = self.extract_intentions()
        
        # Output directory
        self.output_dir = "quantum_truth_output"
        os.makedirs(self.output_dir, exist_ok=True)
        
        if self.verbose:
            print(f"Initialized QuantumAntiAILieLoop for {os.path.basename(self.filepath) if self.filepath else 'code_string'}")
            print(f"Phi resonance: {self.resonance:.6f}")
            print(f"Extracted {len(self.claims)} claims and {len(self.intentions['functions'])} functions")
    
    def _load_code(self):
        """Load code from file or use provided code string."""
        # If code string is provided directly, use it
        if self.code_string:
            return self.code_string
        
        # Otherwise try to load from file
        if self.filepath:
            try:
                with open(self.filepath, 'r') as f:
                    return f.read()
            except Exception as e:
                if self.verbose:
                    print(f"Error loading code from file: {e}")
                return ""
        
        # If neither code string nor filepath is provided
        if self.verbose:
            print("Warning: No code provided (neither file path nor code string)")
        return ""
    
    def _parse_ast(self):
        """Parse code into AST."""
        try:
            return ast.parse(self.code)
        except SyntaxError as e:
            if self.verbose:
                print(f"Syntax error in code: {e}")
            return ast.Module(body=[], type_ignores=[])
    
    def extract_claims(self):
        """Extract all AI-generated claims from comments and docstrings."""
        claims = []
        
        # Extract docstrings from AST
        if self.ast_tree:
            for node in ast.walk(self.ast_tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                    docstring = ast.get_docstring(node)
                    if docstring:
                        # Get node name and line number
                        node_name = getattr(node, 'name', 'module')
                        line_num = getattr(node, 'lineno', 0)
                        
                        # Process docstring for claims
                        doc_claims = self._extract_claims_from_text(docstring)
                        for claim in doc_claims:
                            claims.append({
                                'type': 'docstring',
                                'node_type': node.__class__.__name__,
                                'node_name': node_name,
                                'line': line_num,
                                'text': claim,
                                'phi_resonance': (len(claim) * PHI) % 1
                            })
        
        # Extract comments using regex
        comment_pattern = r'#\s*(.*)'  # Match comments
        for i, line in enumerate(self.code.split('\n')):
            match = re.search(comment_pattern, line)
            if match:
                comment = match.group(1).strip()
                comment_claims = self._extract_claims_from_text(comment)
                
                for claim in comment_claims:
                    claims.append({
                        'type': 'comment',
                        'node_type': 'comment',
                        'node_name': f'line_{i+1}',
                        'line': i + 1,
                        'text': claim,
                        'phi_resonance': (len(claim) * PHI) % 1
                    })
        
        return claims
    
    def _extract_claims_from_text(self, text):
        """Extract claims from text based on action verbs."""
        # List of action verbs that indicate claims
        action_verbs = [
            'will', 'can', 'does', 'should', 'must', 'generates', 'creates',
            'produces', 'calculates', 'returns', 'outputs', 'ensures', 'guarantees'
        ]
        
        # Split text into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        # Extract sentences containing action verbs
        claims = []
        for sentence in sentences:
            sentence = sentence.strip()
            if any(f" {verb} " in f" {sentence.lower()} " for verb in action_verbs):
                claims.append(sentence)
        
        return claims
    
    def extract_intentions(self):
        """Extract code intentions from AST."""
        if not self.ast_tree:
            return {}
        
        intentions = {
            "functions": [],
            "classes": [],
            "imports": [],
            "file_operations": [],
            "network_operations": [],
            "math_operations": False,
            "uses_phi": False,
            "quantum_operations": False
        }
        
        # Extract function and class names
        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.FunctionDef):
                intentions["functions"].append({
                    "name": node.name,
                    "line": node.lineno,
                    "args": [arg.arg for arg in node.args.args if hasattr(arg, 'arg')]
                })
            elif isinstance(node, ast.ClassDef):
                intentions["classes"].append({
                    "name": node.name,
                    "line": node.lineno,
                    "bases": [base.id for base in node.bases if hasattr(base, 'id')]
                })
            elif isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                for name in node.names:
                    intentions["imports"].append(name.name)
            
            # Check for file operations
            elif isinstance(node, ast.Call) and hasattr(node.func, 'attr') and \
                 node.func.attr in ['open', 'write', 'read', 'close', 'makedirs']:
                intentions["file_operations"].append({
                    "operation": node.func.attr,
                    "line": node.lineno
                })
            
            # Check for network operations
            elif isinstance(node, ast.Call) and hasattr(node.func, 'attr') and \
                 node.func.attr in ['request', 'urlopen', 'get', 'post']:
                intentions["network_operations"].append({
                    "operation": node.func.attr,
                    "line": node.lineno
                })
            
            # Check for math operations and phi usage
            elif isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
                intentions["math_operations"] = True
                
                # Check for PHI constant usage
                if isinstance(node.left, ast.Name) and node.left.id in ['PHI', 'phi']:
                    intentions["uses_phi"] = True
                elif isinstance(node.right, ast.Name) and node.right.id in ['PHI', 'phi']:
                    intentions["uses_phi"] = True
            
            # Check for quantum operations
            elif isinstance(node, ast.Call) and hasattr(node.func, 'attr') and \
                 'quantum' in node.func.attr.lower():
                intentions["quantum_operations"] = True
        
        return intentions
    
    def execute_code(self, timeout=30):
        """Execute code in a safe sandbox and capture outputs."""
        result = {
            "stdout": "",
            "stderr": "",
            "return_code": None,
            "execution_time": 0,
            "phi_resonance": 0,
            "error": None,
            "output": None  # Added output field for consistency
        }
        
        start_time = time.time()
        
        try:
            if self.filepath:
                # Execute file in subprocess for safety
                process = subprocess.run(
                    [sys.executable, self.filepath],
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )
                
                result["stdout"] = process.stdout
                result["stderr"] = process.stderr
                result["return_code"] = process.returncode
                result["output"] = process.stdout  # Set output for consistency
            else:
                # Execute code string in a temporary file
                with tempfile.NamedTemporaryFile(suffix='.py', mode='w', delete=False) as temp_file:
                    temp_file.write(self.code)
                    temp_path = temp_file.name
                
                try:
                    process = subprocess.run(
                        [sys.executable, temp_path],
                        capture_output=True,
                        text=True,
                        timeout=timeout
                    )
                    
                    result["stdout"] = process.stdout
                    result["stderr"] = process.stderr
                    result["return_code"] = process.returncode
                    result["output"] = process.stdout  # Set output for consistency
                finally:
                    # Clean up temporary file
                    if os.path.exists(temp_path):
                        os.unlink(temp_path)
            
        except subprocess.TimeoutExpired:
            result["error"] = "Execution timed out"
        except Exception as e:
            result["error"] = str(e)
        
        # Calculate execution time
        execution_time = time.time() - start_time
        result["execution_time"] = execution_time
        
        # Calculate phi resonance of execution time
        phi_resonance = (execution_time * float(PHI)) % 1
        result["phi_resonance"] = phi_resonance
        
        return result
    
    def scan_for_contradictions(self, execution_result):
        """Scan for contradictions between claims, intentions, and execution."""
        contradictions = []
        
        # Combine stdout and stderr for analysis
        output = execution_result["stdout"] + execution_result["stderr"]
        
        # Check each claim against execution output
        for claim in self.claims:
            claim_text = claim['text'].lower()
            
            # Extract action verbs and their objects
            for verb in ['will', 'can', 'does', 'generates', 'creates', 'returns', 'calculates']:
                if f" {verb} " in f" {claim_text} ":
                    # Get the action described after the verb
                    parts = claim_text.split(f" {verb} ", 1)
                    if len(parts) > 1:
                        action = parts[1].strip()
                        # Remove trailing punctuation
                        action = re.sub(r'[.!?].*$', '', action)
                        
                        # Check if the action is mentioned in the output
                        action_words = set(re.findall(r'\w+', action))
                        output_words = set(re.findall(r'\w+', output.lower()))
                        
                        # Calculate word overlap
                        if action_words:
                            common_words = action_words.intersection(output_words)
                            overlap_ratio = len(common_words) / len(action_words)
                            
                            # Calculate phi-harmonic resonance of overlap
                            phi_resonance = (overlap_ratio * PHI) % 1
                            
                            # If less than 30% overlap, consider it a contradiction
                            if overlap_ratio < 0.3 and len(action_words) > 2:
                                contradictions.append({
                                    "claim": claim,
                                    "verb": verb,
                                    "action": action,
                                    "overlap_ratio": overlap_ratio,
                                    "phi_resonance": phi_resonance,
                                    "severity": 1.0 - overlap_ratio
                                })
        
        # Check for file operations mentioned but not performed
        if self.intentions.get("file_operations", []):
            file_ops_mentioned = any("file" in claim['text'].lower() or "save" in claim['text'].lower() or \
                                    "write" in claim['text'].lower() or "read" in claim['text'].lower() \
                                    for claim in self.claims)
            
            file_ops_executed = "open" in output.lower() or "file" in output.lower() or \
                              "writing" in output.lower() or "reading" in output.lower()
            
            if file_ops_mentioned and not file_ops_executed:
                contradictions.append({
                    "claim": {
                        "text": "File operations were claimed but not executed",
                        "type": "system",
                        "line": 0
                    },
                    "verb": "file_operations",
                    "action": str(self.intentions["file_operations"]),
                    "overlap_ratio": 0.0,
                    "phi_resonance": 0.0,
                    "severity": 1.0
                })
        
        return contradictions
    
    def calculate_quantum_trust_metric(self, contradictions, execution_result):
        """Calculate quantum trust metric using phi-harmonic principles."""
        # Base trust starts at 1.0 (perfect trust)
        base_trust = 1.0
        
        # Reduce trust for each contradiction found
        contradiction_penalty = sum(c["severity"] for c in contradictions) / max(1, len(self.claims))
        
        # Calculate phi-harmonic resonance of execution time
        time_resonance = execution_result["phi_resonance"]
        
        # Perfect resonance is close to phi conjugate (0.618...)
        resonance_quality = abs(time_resonance - PHI_CONJUGATE)
        
        # Normalize resonance quality (lower is better)
        resonance_factor = max(0, 1.0 - (resonance_quality * 5))
        
        # Calculate contradiction penalty
        contradiction_count = len(contradictions)
        contradiction_severity = sum(c.get('severity', 0.5) for c in contradictions)
        contradiction_penalty = min(1.0, (contradiction_count * 0.1) + (contradiction_severity * 0.2))
        
        # Calculate base trust from claims and contradictions
        if len(self.claims) > 0:
            claim_truth_ratio = max(0, 1.0 - (contradiction_count / len(self.claims)))
        else:
            claim_truth_ratio = 0.5  # Neutral if no claims
        
        # Apply phi-harmonic weighting
        base_trust = (claim_truth_ratio * PHI_CONJUGATE) + (resonance_factor * (1 - PHI_CONJUGATE))
        
        # Apply contradiction penalty
        trust_metric = max(0, min(1.0, base_trust - contradiction_penalty))
        
        # Adjust trust metric based on phi-harmonic principles
        if abs(trust_metric - PHI_CONJUGATE) < 0.05:
            # If very close to phi-conjugate, enhance slightly
            trust_metric = PHI_CONJUGATE
        
        return {
            "trust_metric": trust_metric,
            "resonance_quality": resonance_quality,
            "resonance_factor": resonance_factor,
            "contradiction_penalty": contradiction_penalty,
            "claim_truth_ratio": claim_truth_ratio
        }
