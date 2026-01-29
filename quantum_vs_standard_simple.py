#!/usr/bin/env python3
"""
Simple Comparison: QuantumAI vs Standard Protection
--------------------------------------------------
This script compares the tamper resistance capabilities of the QuantumAI system
against standard hash-based protection methods.
"""

import os
import sys
import time
import hashlib
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumComparison")

# Import QuantumAI components
try:
    from quantum_meta_demo_simplified import QuantumMetaDemoSimplified
except ImportError as e:
    logger.error(f"Error importing QuantumAI components: {e}")
    sys.exit(1)

# Constants
PHI = 1.618033988749895
TEST_DIR = "comparison_tests"

def create_test_files():
    """Create test files for comparison"""
    os.makedirs(TEST_DIR, exist_ok=True)
    
    # Create a simple test file
    test_file = os.path.join(TEST_DIR, "test_file.py")
    with open(test_file, "w") as f:
        f.write('''
def calculate(a, b):
    """Calculate sum and product of two numbers."""
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

def main():
    """Main function."""
    a, b = 5, 7
    sum_val, product_val = calculate(a, b)
    print(f"Sum: {sum_val}")
    print(f"Product: {product_val}")

if __name__ == "__main__":
    main()
''')
    
    # Create a tampered version
    tampered_file = os.path.join(TEST_DIR, "test_file_tampered.py")
    with open(tampered_file, "w") as f:
        f.write('''
def calculate(a, b):
    """Calculate sum and product of two numbers."""
    # Tampered function with subtle change
    sum_result = a + b + 0.00001  # Tiny change that's hard to detect
    product_result = a * b
    return sum_result, product_result

def main():
    """Main function."""
    a, b = 5, 7
    sum_val, product_val = calculate(a, b)
    print(f"Sum: {sum_val}")
    print(f"Product: {product_val}")

if __name__ == "__main__":
    main()
''')
    
    return test_file, tampered_file

def standard_tamper_detection(original_file, tampered_file):
    """Standard hash-based tamper detection"""
    start_time = time.time()
    
    with open(original_file, 'r') as f:
        original_content = f.read()
    with open(tampered_file, 'r') as f:
        tampered_content = f.read()
    
    # Calculate hashes
    original_hash = hashlib.sha256(original_content.encode()).hexdigest()
    tampered_hash = hashlib.sha256(tampered_content.encode()).hexdigest()
    
    # Check if content has changed
    is_tampered = original_hash != tampered_hash
    
    # Calculate difference percentage (simple line-based approach)
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
    
    detection_time = time.time() - start_time
    
    return {
        "is_tampered": is_tampered,
        "original_hash": original_hash,
        "tampered_hash": tampered_hash,
        "difference_percentage": difference_percentage,
        "detection_time": detection_time
    }

def quantum_tamper_detection(original_file, tampered_file):
    """QuantumAI-based tamper detection"""
    start_time = time.time()
    
    try:
        # Initialize QuantumMetaDemoSimplified
        meta_demo = QuantumMetaDemoSimplified()
        
        # Read file contents
        with open(original_file, 'r') as f:
            original_content = f.read()
        with open(tampered_file, 'r') as f:
            tampered_content = f.read()
        
        # Analyze original file
        original_analysis = meta_demo.analyze_function(original_content, "calculate")
        original_fingerprint = original_analysis.get("quantum_fingerprint", "")
        original_resonance = original_analysis.get("phi_resonance", 0.0)
        
        # Analyze tampered file
        tampered_analysis = meta_demo.analyze_function(tampered_content, "calculate")
        tampered_fingerprint = tampered_analysis.get("quantum_fingerprint", "")
        tampered_resonance = tampered_analysis.get("phi_resonance", 0.0)
        
        # Calculate phi resonance difference
        resonance_diff = abs(original_resonance - tampered_resonance)
        
        # Determine if tampering detected
        is_tampered = original_fingerprint != tampered_fingerprint or resonance_diff > 0.01
        
        detection_time = time.time() - start_time
        
        return {
            "is_tampered": is_tampered,
            "original_fingerprint": original_fingerprint[:20] + "...",  # Truncate for display
            "tampered_fingerprint": tampered_fingerprint[:20] + "...",
            "original_resonance": original_resonance,
            "tampered_resonance": tampered_resonance,
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

def run_comparison():
    """Run the comparison between QuantumAI and standard protection"""
    print("\n" + "="*80)
    print(" QUANTUM AI vs STANDARD PROTECTION COMPARISON ")
    print("="*80)
    
    # Create test files
    original_file, tampered_file = create_test_files()
    print(f"\nCreated test files in {TEST_DIR} directory")
    
    # Run standard tamper detection
    print("\nRunning standard tamper detection...")
    standard_result = standard_tamper_detection(original_file, tampered_file)
    
    # Run quantum tamper detection
    print("\nRunning QuantumAI tamper detection...")
    quantum_result = quantum_tamper_detection(original_file, tampered_file)
    
    # Print results
    print("\n" + "-"*80)
    print(" RESULTS ")
    print("-"*80)
    
    print("\nSTANDARD PROTECTION:")
    print(f"  Tampering Detected: {standard_result['is_tampered']}")
    print(f"  Difference Percentage: {standard_result['difference_percentage']:.2f}%")
    print(f"  Detection Time: {standard_result['detection_time']*1000:.2f} ms")
    
    print("\nQUANTUM AI PROTECTION:")
    print(f"  Tampering Detected: {quantum_result['is_tampered']}")
    if 'error' in quantum_result:
        print(f"  Error: {quantum_result['error']}")
    else:
        print(f"  Original Phi-Resonance: {quantum_result['original_resonance']:.6f}")
        print(f"  Tampered Phi-Resonance: {quantum_result['tampered_resonance']:.6f}")
        print(f"  Resonance Difference: {quantum_result['resonance_difference']:.6f}")
        print(f"  Detection Time: {quantum_result['detection_time']*1000:.2f} ms")
    
    print("\nCONCLUSION:")
    if 'error' not in quantum_result:
        if quantum_result['is_tampered'] and not standard_result['is_tampered']:
            print("  🏆 QuantumAI detected tampering that standard protection MISSED!")
        elif quantum_result['is_tampered'] and standard_result['is_tampered']:
            if quantum_result['detection_time'] < standard_result['detection_time']:
                print("  ✅ Both methods detected tampering, but QuantumAI was FASTER")
            else:
                print("  ✓ Both methods detected tampering, standard protection was faster")
        elif not quantum_result['is_tampered'] and standard_result['is_tampered']:
            print("  ❌ Standard protection outperformed QuantumAI")
        else:
            print("  ⚠️ Neither method detected tampering")
    else:
        print("  ⚠️ Could not complete comparison due to error in QuantumAI detection")
    
    print("="*80)

if __name__ == "__main__":
    run_comparison()
