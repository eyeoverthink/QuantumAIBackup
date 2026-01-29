#!/usr/bin/env python3
"""
QR Task Executor Test - Debugging tool for QR Flipbook DNA System
By Vaughn Scott

Tests the QR Task Executor with simple code fragments to verify functionality.
"""

import os
import sys
import json
from qr_task_executor import QRTaskExecutor

def test_basic_execution():
    """Test basic Python code execution."""
    print("🧪 Testing basic Python code execution")
    
    # Create task executor
    executor = QRTaskExecutor(debug=True)
    
    # Simple Python code that prints phi value
    python_code = """
import math

# Calculate phi (golden ratio)
phi = (1 + math.sqrt(5)) / 2
print(f"Phi (Golden Ratio): {phi}")
print("Basic execution test successful!")
"""
    
    # Execute the code
    success, output = executor.execute_task("execute_python", {"code": python_code})
    
    print(f"Success: {success}")
    print(f"Output: {output}")
    
    return success

def test_numpy_execution():
    """Test execution with numpy import."""
    print("\n🧪 Testing numpy execution")
    
    # Create task executor
    executor = QRTaskExecutor(debug=True)
    
    # Python code that uses numpy
    python_code = """
import numpy as np

# Calculate phi using numpy
phi = (1 + np.sqrt(5)) / 2
print(f"Phi (Golden Ratio): {phi}")

# Create a phi-based array
phi_array = np.array([phi, phi**2, phi**3, phi**4, phi**5])
print(f"Phi array: {phi_array}")

print("Numpy execution test successful!")
"""
    
    # Execute the code
    success, output = executor.execute_task("execute_python", {"code": python_code})
    
    print(f"Success: {success}")
    print(f"Output: {output}")
    
    return success

def test_function_execution():
    """Test execution of a function definition and call."""
    print("\n🧪 Testing function execution")
    
    # Create task executor
    executor = QRTaskExecutor(debug=True)
    
    # Python code with function definition
    python_code = """
def calculate_phi_resonance(x):
    # Calculate phi-harmonic resonance for a value
    phi = (1 + 5**0.5) / 2
    return 1.0 / (1.0 + abs((x * phi) % 1.0 - 0.5))

# Test the function
for i in range(5):
    resonance = calculate_phi_resonance(i)
    print(f"Resonance for {i}: {resonance:.6f}")

print("Function execution test successful!")
"""
    
    # Execute the code
    success, output = executor.execute_task("execute_python", {"code": python_code})
    
    print(f"Success: {success}")
    print(f"Output: {output}")
    
    return success

def test_shell_execution():
    """Test shell script execution."""
    print("\n🧪 Testing shell script execution")
    
    # Create task executor
    executor = QRTaskExecutor(debug=True)
    
    # Shell script
    shell_script = """
#!/bin/bash
echo "Testing shell execution"
echo "Current directory: $(pwd)"
echo "Python version: $(python3 --version)"
echo "Shell execution test successful!"
"""
    
    # Execute the script
    success, output = executor.execute_task("execute_sh", {"code": shell_script})
    
    print(f"Success: {success}")
    print(f"Output: {output}")
    
    return success

def run_all_tests():
    """Run all tests and report results."""
    print("🧬 QR Task Executor Test Suite")
    print("=" * 60)
    
    tests = [
        ("Basic Python", test_basic_execution),
        ("NumPy", test_numpy_execution),
        ("Function", test_function_execution),
        ("Shell", test_shell_execution)
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\nRunning test: {name}")
        print("-" * 60)
        success = test_func()
        results.append((name, success))
    
    # Print summary
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    for name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {name}")
    
    # Overall result
    success_count = sum(1 for _, success in results if success)
    print(f"\nOverall: {success_count}/{len(results)} tests passed")

if __name__ == "__main__":
    run_all_tests()
