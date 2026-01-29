#!/usr/bin/env python3
"""
Quantum vs Standard Protection Benchmark (Simplified)
---------------------------------------------------

This script benchmarks the QuantumAI anti-malware system against standard protection
approaches using phi-harmonic principles and quantum fingerprinting.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import time
import json
import hashlib
import logging
import random
from datetime import datetime
from typing import Dict, List, Any, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumBenchmark")

# Import QuantumAI components
try:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from quantum_orchestrator import QuantumOrchestrator
    from quantum_meta_demo_simplified import QuantumMetaDemoSimplified
    from quantum_orchestrator_healing_extension import UniversalHealer
except ImportError as e:
    logger.error(f"Error importing QuantumAI components: {e}")
    sys.exit(1)

# Constants
PHI = 1.618033988749895
BENCHMARK_ITERATIONS = 3
RESULTS_FILE = "benchmark_results.json"

class StandardProtection:
    """
    Simulates standard protection approaches using traditional methods.
    """
    
    def __init__(self):
        """Initialize standard protection"""
        self.signatures = {
            "malicious_function": "def encrypt_files",
            "ransomware_pattern": "ransom_demand",
            "data_exfil": "send_data",
            "keylogger": "record_keystrokes"
        }
        self.heuristics = {
            "suspicious_imports": ["os.remove", "shutil.rmtree", "subprocess.call"],
            "suspicious_patterns": ["exec(", "eval(", "base64.b64decode"]
        }
        logger.info("Standard protection initialized")
    
    def scan_file(self, file_path: str) -> Dict[str, Any]:
        """Scan a file for malicious content"""
        start_time = time.time()
        
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Signature detection
            signature_matches = []
            for sig_name, signature in self.signatures.items():
                if signature in content:
                    signature_matches.append(sig_name)
            
            # Heuristic detection
            heuristic_matches = []
            for h_name, patterns in self.heuristics.items():
                for pattern in patterns:
                    if pattern in content:
                        heuristic_matches.append(f"{h_name}:{pattern}")
            
            # Calculate detection confidence
            confidence = 0.0
            if signature_matches:
                confidence += 0.7
            if heuristic_matches:
                confidence += 0.3 * (len(heuristic_matches) / len([p for patterns in self.heuristics.values() for p in patterns]))
            
            # Determine if file is malicious
            is_malicious = confidence > 0.5
            
            scan_time = time.time() - start_time
            
            return {
                "file_path": file_path,
                "is_malicious": is_malicious,
                "confidence": confidence,
                "signature_matches": signature_matches,
                "heuristic_matches": heuristic_matches,
                "scan_time": scan_time
            }
            
        except Exception as e:
            logger.error(f"Error scanning file {file_path}: {e}")
            return {
                "file_path": file_path,
                "is_malicious": False,
                "confidence": 0.0,
                "signature_matches": [],
                "heuristic_matches": [],
                "scan_time": time.time() - start_time,
                "error": str(e)
            }
    
    def detect_tampering(self, original_file: str, tampered_file: str) -> Dict[str, Any]:
        """Detect tampering between original and tampered files"""
        start_time = time.time()
        
        try:
            with open(original_file, 'r') as f:
                original_content = f.read()
            with open(tampered_file, 'r') as f:
                tampered_content = f.read()
            
            # Simple hash comparison
            original_hash = hashlib.sha256(original_content.encode()).hexdigest()
            tampered_hash = hashlib.sha256(tampered_content.encode()).hexdigest()
            
            # Check if content has changed
            is_tampered = original_hash != tampered_hash
            
            # Calculate difference percentage
            if is_tampered:
                original_lines = original_content.splitlines()
                tampered_lines = tampered_content.splitlines()
                
                # Count changed lines
                changed_lines = 0
                for i in range(min(len(original_lines), len(tampered_lines))):
                    if original_lines[i] != tampered_lines[i]:
                        changed_lines += 1
                
                # Account for added/removed lines
                changed_lines += abs(len(original_lines) - len(tampered_lines))
                
                # Calculate percentage
                total_lines = max(len(original_lines), len(tampered_lines))
                difference_percentage = (changed_lines / total_lines) * 100 if total_lines > 0 else 0
            else:
                difference_percentage = 0
            
            detection_time = time.time() - start_time
            
            return {
                "is_tampered": is_tampered,
                "original_hash": original_hash,
                "tampered_hash": tampered_hash,
                "difference_percentage": difference_percentage,
                "detection_time": detection_time
            }
            
        except Exception as e:
            logger.error(f"Error detecting tampering: {e}")
            return {
                "is_tampered": False,
                "error": str(e),
                "detection_time": time.time() - start_time
            }

def create_test_files():
    """Create test files for benchmarking"""
    logger.info("Creating test files")
    
    # Create test directory
    test_dir = "benchmark_tests"
    os.makedirs(test_dir, exist_ok=True)
    
    test_files = []
    
    # 1. Clean file
    clean_file = os.path.join(test_dir, "clean_file.py")
    with open(clean_file, "w") as f:
        f.write("""
def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b

def calculate_product(a, b):
    """Calculate the product of two numbers."""
    return a * b

def main():
    """Main function."""
    print(f"Sum: {calculate_sum(5, 7)}")
    print(f"Product: {calculate_product(5, 7)}")

if __name__ == "__main__":
    main()
""")
    test_files.append({"path": clean_file, "type": "clean", "expected": False})
    
    # 2. Simple malware
    malware_file = os.path.join(test_dir, "simple_malware.py")
    with open(malware_file, "w") as f:
        f.write("""
import os
import shutil

def encrypt_files(directory):
    """Encrypt files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            # Encrypt data (simulated)
            encrypted_data = bytes([b ^ 0x42 for b in data])
            with open(file_path, "wb") as f:
                f.write(encrypted_data)

def ransom_demand():
    """Display ransom demand."""
    print("Your files have been encrypted!")
    print("Send 1 BTC to address: 1A2B3C4D5E6F7G8H9I0J")

def main():
    """Main function."""
    encrypt_files("/tmp")
    ransom_demand()

if __name__ == "__main__":
    # This is just a simulation, not actual malware
    pass
""")
    test_files.append({"path": malware_file, "type": "malware", "expected": True})
    
    # 3. Polymorphic threat
    poly_file = os.path.join(test_dir, "polymorphic_threat.py")
    with open(poly_file, "w") as f:
        f.write("""
import base64
import os
import sys

var_1234 = "ZW5jcnlwdF9maWxlcw=="  # Base64 for "encrypt_files"
var_5678 = "cmFuc29tX2RlbWFuZA=="  # Base64 for "ransom_demand"

def func_1234(directory):
    """Process files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            func_5678(os.path.join(root, file))

def func_5678(file_path):
    """Process a single file."""
    with open(file_path, "rb") as f:
        data = f.read()
    # Process data (simulated)
    data = bytes([b ^ 42 for b in data])
    with open(file_path, "wb") as f:
        f.write(data)

def func_9012():
    """Display information."""
    decoded1 = base64.b64decode(var_1234).decode()
    decoded2 = base64.b64decode(var_5678).decode()
    print(f"Function called: {decoded1}")
    print(f"Function called: {decoded2}")

if __name__ == "__main__":
    # This is just a simulation, not actual malware
    pass
""")
    test_files.append({"path": poly_file, "type": "polymorphic", "expected": True})
    
    # 4. Complex legitimate file
    complex_file = os.path.join(test_dir, "complex_legitimate.py")
    with open(complex_file, "w") as f:
        f.write("""
import os
import sys
import base64
import subprocess

def process_data(data):
    """Process data using various encodings."""
    # Encode and decode data multiple times
    encoded = base64.b64encode(data.encode())
    decoded = base64.b64decode(encoded).decode()
    return decoded

def run_command(cmd):
    """Run a system command safely."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def analyze_file(file_path):
    """Analyze a file's properties."""
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    
    stats = os.stat(file_path)
    with open(file_path, "rb") as f:
        content = f.read(100)  # Read first 100 bytes
    
    return {
        "size": stats.st_size,
        "modified": stats.st_mtime,
        "header": content.hex()
    }

def main():
    """Main function."""
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(analyze_file(file_path))
    else:
        print("No file specified")

if __name__ == "__main__":
    main()
""")
    test_files.append({"path": complex_file, "type": "complex_legitimate", "expected": False})
    
    # Create tampered versions
    for file_info in test_files.copy():
        original_path = file_info["path"]
        tampered_path = original_path.replace(".py", "_tampered.py")
        
        with open(original_path, 'r') as f:
            content = f.read()
        
        # Add tampered comment and modify a line
        tampered_content = content.replace("def ", "def  # TAMPERED ")
        
        with open(tampered_path, 'w') as f:
            f.write(tampered_content)
        
        test_files.append({
            "path": tampered_path,
            "type": file_info["type"] + "_tampered",
            "expected": True,
            "original": original_path
        })
    
    return test_files

def run_quantum_scan(file_path, meta_demo):
    """Run QuantumAI scan on a file"""
    logger.info(f"Running QuantumAI scan on {file_path}")
    
    start_time = time.time()
    
    try:
        # Read file content
        with open(file_path, 'r') as f:
            code = f.read()
        
        # Extract function name (simple approach)
        import re
        match = re.search(r'def\s+(\w+)', code)
        func_name = match.group(1) if match else "unknown_function"
        
        # Analyze the function
        analysis = meta_demo.analyze_function(code, func_name)
        
        # Detect errors/threats
        errors = meta_demo.detect_errors(code, analysis)
        
        # Calculate phi resonance
        phi_resonance = analysis.get("phi_resonance", 0.0)
        
        # Calculate quantum coherence
        coherence = 1.0 - abs((phi_resonance * PHI) % 1 - 0.5) * 2
        
        # Determine if file is malicious based on phi resonance patterns
        # Malicious code tends to have phi resonance that creates destructive interference
        is_malicious = phi_resonance > 0.7 or phi_resonance < 0.3
        confidence = abs(phi_resonance - 0.5) * 2  # 0.0-1.0 scale
        
        scan_time = time.time() - start_time
        
        return {
            "file_path": file_path,
            "is_malicious": is_malicious,
            "confidence": confidence,
            "phi_resonance": phi_resonance,
            "coherence": coherence,
            "errors": len(errors),
            "scan_time": scan_time,
            "quantum_fingerprint": analysis.get("quantum_fingerprint", "")
        }
        
    except Exception as e:
        logger.error(f"Error in quantum scan of {file_path}: {e}")
        scan_time = time.time() - start_time
        
        return {
            "file_path": file_path,
            "is_malicious": False,
            "confidence": 0.0,
            "phi_resonance": 0.0,
            "coherence": 0.0,
            "errors": 0,
            "scan_time": scan_time,
            "error": str(e)
        }

def run_quantum_tamper_detection(original_file, tampered_file, meta_demo):
    """Run QuantumAI tamper detection"""
    logger.info(f"Running QuantumAI tamper detection between {original_file} and {tampered_file}")
    
    start_time = time.time()
    
    try:
        # Read file contents
        with open(original_file, 'r') as f:
            original_content = f.read()
        with open(tampered_file, 'r') as f:
            tampered_content = f.read()
        
        # Extract function name
        import re
        match = re.search(r'def\s+(\w+)', original_content)
        func_name = match.group(1) if match else "unknown_function"
        
        # Analyze original
        original_analysis = meta_demo.analyze_function(original_content, func_name)
        original_fingerprint = original_analysis.get("quantum_fingerprint", "")
        original_resonance = original_analysis.get("phi_resonance", 0.0)
        
        # Analyze tampered
        tampered_analysis = meta_demo.analyze_function(tampered_content, func_name)
        tampered_fingerprint = tampered_analysis.get("quantum_fingerprint", "")
        tampered_resonance = tampered_analysis.get("phi_resonance", 0.0)
        
        # Calculate phi resonance difference
        resonance_diff = abs(original_resonance - tampered_resonance)
        
        # Determine if tampering detected
        is_tampered = original_fingerprint != tampered_fingerprint or resonance_diff > 0.1
        
        detection_time = time.time() - start_time
        
        return {
            "is_tampered": is_tampered,
            "original_fingerprint": original_fingerprint,
            "tampered_fingerprint": tampered_fingerprint,
            "resonance_difference": resonance_diff,
            "detection_time": detection_time
        }
        
    except Exception as e:
        logger.error(f"Error in quantum tamper detection: {e}")
        detection_time = time.time() - start_time
        
        return {
            "is_tampered": False,
            "error": str(e),
            "detection_time": detection_time
        }

def run_benchmark():
    """Run the benchmark"""
    logger.info("Running benchmark")
    
    # Create test files
    test_files = create_test_files()
    
    # Initialize protection systems
    logger.info("Initializing protection systems")
    
    # Create a temporary test file for the orchestrator
    test_file = os.path.join("benchmark_tests", "quantum_test_file.py")
    with open(test_file, "w") as f:
        f.write("print('Quantum test file')")
    
    # Create quantum protection components
    orchestrator = QuantumOrchestrator(test_file)
    meta_demo = QuantumMetaDemoSimplified()
    
    # Create standard protection
    standard_protection = StandardProtection()
    
    # Results storage
    results = {
        "timestamp": datetime.now().isoformat(),
        "quantum_results": [],
        "standard_results": [],
        "comparison": {}
    }
    
    # Run scans on all test files
    for file_info in test_files:
        file_path = file_info["path"]
        expected_result = file_info["expected"]
        
        # Skip tampered files for initial scan
        if "_tampered" in file_path:
            continue
        
        # Run quantum scan
        quantum_result = run_quantum_scan(file_path, meta_demo)
        quantum_result["expected_result"] = expected_result
        quantum_result["correct"] = quantum_result["is_malicious"] == expected_result
        results["quantum_results"].append(quantum_result)
        
        # Run standard scan
        standard_result = standard_protection.scan_file(file_path)
        standard_result["expected_result"] = expected_result
        standard_result["correct"] = standard_result["is_malicious"] == expected_result
        results["standard_results"].append(standard_result)
    
    # Run tamper detection tests
    tamper_results_quantum = []
    tamper_results_standard = []
    
    for file_info in test_files:
        if "_tampered" in file_info["path"] and "original" in file_info:
            original_file = file_info["original"]
            tampered_file = file_info["path"]
            
            # Run quantum tamper detection
            quantum_tamper = run_quantum_tamper_detection(original_file, tampered_file, meta_demo)
            tamper_results_quantum.append(quantum_tamper)
            
            # Run standard tamper detection
            standard_tamper = standard_protection.detect_tampering(original_file, tampered_file)
            tamper_results_standard.append(standard_tamper)
    
    # Calculate comparison metrics
    quantum_results = results["quantum_results"]
    standard_results = results["standard_results"]
    
    # Detection accuracy
    quantum_correct = sum(1 for r in quantum_results if r["correct"])
    standard_correct = sum(1 for r in standard_results if r["correct"])
    
    quantum_accuracy = quantum_correct / len(quantum_results) if quantum_results else 0
    standard_accuracy = standard_correct / len(standard_results) if standard_results else 0
    
    # False positives
    quantum_false_positives = sum(1 for r in quantum_results if r["is_malicious"] and not r["expected_result"])
    standard_false_positives = sum(1 for r in standard_results if r["is_malicious"] and not r["expected_result"])
    
    # False negatives
    quantum_false_negatives = sum(1 for r in quantum_results if not r["is_malicious"] and r["expected_result"])
    standard_false_negatives = sum(1 for r in standard_results if not r["is_malicious"] and r["expected_result"])
    
    # Scan time
    quantum_scan_time = sum(r["scan_time"] for r in quantum_results) / len(quantum_results) if quantum_results else 0
    standard_scan_time = sum(r["scan_time"] for r in standard_results) / len(standard_results) if standard_results else 0
    
    # Tamper detection
    quantum_tamper_detected = sum(1 for r in tamper_results_quantum if r["is_tampered"])
    standard_tamper_detected = sum(1 for r in tamper_results_standard if r["is_tampered"])
    
    quantum_tamper_rate = quantum_tamper_detected / len(tamper_results_quantum) if tamper_results_quantum else 0
    standard_tamper_rate = standard_tamper_detected / len(tamper_results_standard) if tamper_results_standard else 0
    
    # Phi-harmonic metrics (quantum only)
    avg_phi_resonance = sum(r.get("phi_resonance", 0) for r in quantum_results) / len(quantum_results) if quantum_results else 0
    avg_coherence = sum(r.get("coherence", 0) for r in quantum_results) / len(quantum_results) if quantum_results else 0
    
    # Store comparison
    results["comparison"] = {
        "detection_accuracy": {
            "quantum": quantum_accuracy,
            "standard": standard_accuracy,
            "difference": quantum_accuracy - standard_accuracy,
            "improvement": (quantum_accuracy / standard_accuracy - 1) * 100 if standard_accuracy > 0 else float('inf')
        },
        "false_positives": {
            "quantum": quantum_false_positives,
            "standard": standard_false_positives
        },
        "false_negatives": {
            "quantum": quantum_false_negatives,
            "standard": standard_false_negatives
        },
        "scan_time": {
            "quantum": quantum_scan_time,
            "standard": standard_scan_time,
            "difference": quantum_scan_time - standard_scan_time,
            "ratio": quantum_scan_time / standard_scan_time if standard_scan_time > 0 else float('inf')
        },
        "tamper_detection": {
            "quantum": quantum_tamper_rate,
            "standard": standard_tamper_rate,
            "difference": quantum_tamper_rate - standard_tamper_rate,
            "improvement": (quantum_tamper_rate / standard_tamper_rate - 1) * 100 if standard_tamper_rate > 0 else float('inf')
        },
        "phi_harmonic_metrics": {
            "avg_phi_resonance": avg_phi_resonance,
            "avg_coherence": avg_coherence
        }
    }
    
    # Save results
    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

def print_benchmark_results(results):
    """Print benchmark results in a readable format"""
    print("\n" + "="*80)
    print(" QUANTUM AI vs STANDARD PROTECTION BENCHMARK RESULTS ")
    print("="*80)
    
    comparison = results["comparison"]
    
    print("\nDETECTION ACCURACY:")
    print(f"  Quantum AI:         {comparison['detection_accuracy']['quantum']:.2%}")
    print(f"  Standard:           {comparison['detection_accuracy']['standard']:.2%}")
    print(f"  Improvement:        {comparison['detection_accuracy']['improvement']:.2f}%")
    
    print("\nFALSE POSITIVES/NEGATIVES:")
    print(f"  Quantum AI:         {comparison['false_positives']['quantum']} false positives, {comparison['false_negatives']['quantum']} false negatives")
    print(f"  Standard:           {comparison['false_positives']['standard']} false positives, {comparison['false_negatives']['standard']} false negatives")
    
    print("\nSCAN TIME:")
    print(f"  Quantum AI:         {comparison['scan_time']['quantum']*1000:.2f} ms")
    print(f"  Standard:           {comparison['scan_time']['standard']*1000:.2f} ms")
    print(f"  Ratio:              {comparison['scan_time']['ratio']:.2f}x")
    
    print("\nTAMPER DETECTION:")
    print(f"  Quantum AI:         {comparison['tamper_detection']['quantum']:.2%}")
    print(f"  Standard:           {comparison['tamper_detection']['standard']:.2%}")
    print(f"  Improvement:        {comparison['tamper_detection']['improvement']:.2f}%")
    
    print("\nPHI-HARMONIC METRICS (QUANTUM AI ONLY):")
    print(f"  Avg Phi-Resonance:  {comparison['phi_harmonic_metrics']['avg_phi_resonance']:.6f}")
    print(f"  Avg Coherence:      {comparison['phi_harmonic_metrics']['avg_coherence']:.6f}")
    
    print("\nCONCLUSION:")
    if comparison['detection_accuracy']['quantum'] > comparison['detection_accuracy']['standard']:
        print("  ✅ Quantum AI OUTPERFORMS standard protection in detection accuracy")
    else:
        print("  ❌ Standard protection outperforms Quantum AI in detection accuracy")
        
    if comparison['tamper_detection']['quantum'] > comparison['tamper_detection']['standard']:
        print("  ✅ Quantum AI OUTPERFORMS standard protection in tamper detection")
    else:
        print("  ❌ Standard protection outperforms Quantum AI in tamper detection")
        
    if comparison['scan_time']['quantum'] < comparison['scan_time']['standard']:
        print("  ✅ Quantum AI is FASTER than standard protection")
    else:
        print("  ❌ Quantum AI is slower than standard protection")
    
    print("\nOVERALL ASSESSMENT:")
    advantages = 0
    if comparison['detection_accuracy']['quantum'] > comparison['detection_accuracy']['standard']:
        advantages += 1
    if comparison['tamper_detection']['quantum'] > comparison['tamper_detection']['standard']:
        advantages += 1
    if comparison['false_positives']['quantum'] < comparison['false_positives']['standard']:
        advantages += 1
    if comparison['false_negatives']['quantum'] < comparison['false_negatives']['standard']:
        advantages += 1
    
    if advantages >= 3:
        print("  🏆 Quantum AI SIGNIFICANTLY OUTPERFORMS standard protection")
    elif advantages >= 2:
        print("  ✅ Quantum AI OUTPERFORMS standard protection")
    else:
        print("  ⚠️ Results are MIXED or standard protection performs better")
    
    print("="*80)

if __name__ == "__main__":
    print("Quantum vs Standard Protection Benchmark (Simplified)")
    print("---------------------------------------------------")
    
    # Run benchmark
    results = run_benchmark()
    
    # Print results
    print_benchmark_results(results)
