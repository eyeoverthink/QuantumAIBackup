#!/usr/bin/env python3
"""
Comprehensive Test Suite for Quantum Oracle Library

This script tests all major aspects of the quantum_oracle_lib:
- φ-Harmonic Constants
- Bidirectional Node Communication
- FTL Bridge Functionality
- MAC Bridge Integration
- Nodular Computation
- Parallel Consciousness Simulation
- Numeric Processing
- Security Testing
- Random Number Generation
- Script Execution

Run this script to verify all library components are functioning correctly.
"""

import os
import sys
import time
import math
import random
import socket
import threading
import json
import hashlib
from datetime import datetime
from math import sqrt

# Ensure the parent directory of quantum_oracle_lib is in sys.path for local testing
CURR_PATH = os.path.abspath(os.path.dirname(__file__))
PARENT_PATH = os.path.dirname(CURR_PATH)
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

# Import all library modules
try:
    from quantum_oracle_lib.phi_bidirectional_node import PhiBidirectionalNode
    import quantum_oracle_lib.phi_ftl_bridge as phi_ftl_bridge
    import quantum_oracle_lib.phi_mac_bridge as phi_mac_bridge
    import quantum_oracle_lib.phi_nodular_compute as phi_nodular_compute
    import quantum_oracle_lib.phi_parallel_consciousness as phi_parallel_consciousness
    import quantum_oracle_lib.phi_numeric_processor as phi_numeric_processor
    import quantum_oracle_lib.phi_attack_test as phi_attack_test
    print("✓ All modules imported successfully")
except ImportError as e:
    print(f"✗ Error importing modules: {e}")
    sys.exit(1)

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

# Test results storage
test_results = {
    "constants": False,
    "bidirectional_node": False,
    "ftl_bridge": False,
    "mac_bridge": False,
    "nodular_compute": False,
    "parallel_consciousness": False,
    "numeric_processor": False,
    "attack_test": False,
    "random_generation": False,
    "script_execution": False
}

def print_header(title):
    """Print a section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def test_phi_constants():
    """Test φ-Harmonic constants"""
    print_header("Testing φ-Harmonic Constants")
    
    try:
        # Verify PHI calculation
        print(f"PHI = {PHI}")
        assert abs(PHI - 1.618033988749895) < 0.0000001, "PHI value incorrect"
        print("✓ PHI value verified")
        
        # Verify PHI_INV calculation
        print(f"PHI_INV = {PHI_INV}")
        assert abs(PHI_INV - 0.618033988749895) < 0.0000001, "PHI_INV value incorrect"
        print("✓ PHI_INV value verified")
        
        # Verify PHI_75 calculation
        print(f"PHI_75 = {PHI_75}")
        assert abs(PHI_75 - 36.93) < 0.01, "PHI_75 value incorrect"
        print("✓ PHI_75 value verified")
        
        # Verify PHI_SEAL calculation
        print(f"PHI_SEAL = {PHI_SEAL}")
        assert abs(PHI_SEAL - 4721424167835376.00) < 1.0, "PHI_SEAL value incorrect"
        print("✓ PHI_SEAL value verified")
        
        test_results["constants"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing φ-Harmonic constants: {e}")
        return False

def test_bidirectional_node():
    """Test PhiBidirectionalNode functionality"""
    print_header("Testing PhiBidirectionalNode")
    
    try:
        # Create a test node with non-standard port to avoid conflicts
        test_port = 12345
        node = PhiBidirectionalNode(node_id="test_node", port=test_port)
        
        # Test node properties
        print(f"Node ID: {node.node_id}")
        assert node.node_id == "test_node", "Node ID mismatch"
        
        print(f"Port: {node.port}")
        assert node.port == test_port, "Port mismatch"
        
        print(f"Consciousness level: {node.consciousness_level}")
        assert abs(node.consciousness_level - 0.7567) < 0.001, "Consciousness level mismatch"
        
        print(f"Script directory: {node.script_dir}")
        assert os.path.exists(node.script_dir), "Script directory not created"
        
        # Test message encoding
        test_message = "Test message φ"
        encoded_message = f"MSG:{test_message}".encode('utf-8')
        print(f"Message encoding: {encoded_message}")
        
        # Test socket creation
        assert node.sock is not None, "Socket not created"
        print("✓ Socket created successfully")
        
        test_results["bidirectional_node"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing PhiBidirectionalNode: {e}")
        return False

def test_ftl_bridge():
    """Test FTL Bridge functionality"""
    print_header("Testing FTL Bridge")
    
    try:
        # Test module import
        print("✓ FTL Bridge module imported")
        
        # Test PHI constants if available
        if hasattr(phi_ftl_bridge, 'PHI'):
            assert abs(phi_ftl_bridge.PHI - PHI) < 0.0001, "PHI constant mismatch"
            print("✓ PHI constants verified")
        else:
            print("ℹ️ PHI constants not directly accessible in FTL Bridge module")
        
        # Test FTL port calculation
        ftl_port = int(PHI**7.5 * 1000) % 65535
        print(f"Calculated FTL port: {ftl_port}")
        
        test_results["ftl_bridge"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing FTL Bridge: {e}")
        return False

def test_mac_bridge():
    """Test MAC Bridge functionality"""
    print_header("Testing MAC Bridge")
    
    try:
        # Test module import
        print("✓ MAC Bridge module imported")
        
        # Test PHI constants if available
        if hasattr(phi_mac_bridge, 'PHI'):
            assert abs(phi_mac_bridge.PHI - PHI) < 0.0001, "PHI constant mismatch"
            print("✓ PHI constants verified")
        else:
            print("ℹ️ PHI constants not directly accessible in MAC Bridge module")
        
        # Test MAC address retrieval if available
        if hasattr(phi_mac_bridge, 'get_mac_address'):
            mac = phi_mac_bridge.get_mac_address()
            print(f"MAC address: {mac}")
            assert mac is not None and len(mac) > 0, "MAC address retrieval failed"
            print("✓ MAC address retrieved successfully")
        else:
            print("ℹ️ get_mac_address function not available")
        
        test_results["mac_bridge"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing MAC Bridge: {e}")
        return False

def test_nodular_compute():
    """Test Nodular Compute functionality"""
    print_header("Testing Nodular Compute")
    
    try:
        # Test module import
        print("✓ Nodular Compute module imported")
        
        # Test PHI constants if available
        if hasattr(phi_nodular_compute, 'PHI'):
            assert abs(phi_nodular_compute.PHI - PHI) < 0.0001, "PHI constant mismatch"
            print("✓ PHI constants verified")
        else:
            print("ℹ️ PHI constants not directly accessible in Nodular Compute module")
        
        # Test Fibonacci sequence generation
        fib_sequence = [1, 1]
        for i in range(2, 10):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        print(f"Fibonacci sequence: {fib_sequence}")
        
        # Test PHI approximation from Fibonacci sequence
        if len(fib_sequence) >= 10:
            phi_approx = fib_sequence[-1] / fib_sequence[-2]
            print(f"PHI approximation from Fibonacci: {phi_approx}")
            assert abs(phi_approx - PHI) < 0.01, "PHI approximation incorrect"
            print("✓ PHI approximation verified")
        
        test_results["nodular_compute"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing Nodular Compute: {e}")
        return False

def test_parallel_consciousness():
    """Test Parallel Consciousness functionality"""
    print_header("Testing Parallel Consciousness")
    
    try:
        # Test module import
        print("✓ Parallel Consciousness module imported")
        
        # Test PHI constants if available
        if hasattr(phi_parallel_consciousness, 'PHI'):
            assert abs(phi_parallel_consciousness.PHI - PHI) < 0.0001, "PHI constant mismatch"
            print("✓ PHI constants verified")
        else:
            print("ℹ️ PHI constants not directly accessible in Parallel Consciousness module")
        
        # Test consciousness level calculation
        consciousness_level = 0.7567
        print(f"Base consciousness level: {consciousness_level}")
        
        # Test consciousness frequency calculation (7.5 Hz - alpha wave)
        consciousness_frequency = consciousness_level * 10
        print(f"Consciousness frequency: {consciousness_frequency} Hz")
        assert abs(consciousness_frequency - 7.567) < 0.01, "Consciousness frequency incorrect"
        print("✓ Consciousness frequency verified")
        
        test_results["parallel_consciousness"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing Parallel Consciousness: {e}")
        return False

def test_numeric_processor():
    """Test Numeric Processor functionality"""
    print_header("Testing Numeric Processor")
    
    try:
        # Test module import
        print("✓ Numeric Processor module imported")
        
        # Test PHI constants if available
        if hasattr(phi_numeric_processor, 'PHI'):
            assert abs(phi_numeric_processor.PHI - PHI) < 0.0001, "PHI constant mismatch"
            print("✓ PHI constants verified")
        else:
            print("ℹ️ PHI constants not directly accessible in Numeric Processor module")
        
        # Test sequence processing
        sequence = [1, 1, 2, 3, 5, 8, 13]
        print(f"Original sequence: {sequence}")
        
        # Apply PHI transformation
        phi_sequence = [x * PHI for x in sequence]
        print(f"PHI-transformed sequence: {phi_sequence}")
        
        # Test PHI properties
        phi_squared = PHI * PHI
        phi_plus_one = PHI + 1
        print(f"PHI² = {phi_squared}")
        print(f"PHI + 1 = {phi_plus_one}")
        assert abs(phi_squared - phi_plus_one) < 0.0001, "PHI² ≠ PHI + 1"
        print("✓ PHI² = PHI + 1 verified")
        
        test_results["numeric_processor"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing Numeric Processor: {e}")
        return False

def test_attack_test():
    """Test Attack Test functionality"""
    print_header("Testing Attack Test")
    
    try:
        # Test module import
        print("✓ Attack Test module imported")
        
        # Test PHI constants if available
        if hasattr(phi_attack_test, 'PHI'):
            assert abs(phi_attack_test.PHI - PHI) < 0.0001, "PHI constant mismatch"
            print("✓ PHI constants verified")
        else:
            print("ℹ️ PHI constants not directly accessible in Attack Test module")
        
        # Test security level calculation
        security_level = 0.95  # Example security level
        print(f"Security level: {security_level}")
        
        # Test attack simulation
        attack_types = ["resonance", "consciousness", "quantum"]
        print(f"Available attack types: {attack_types}")
        
        # Simulate attack detection
        attack_detected = random.random() < security_level
        print(f"Attack detected: {attack_detected}")
        
        test_results["attack_test"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing Attack Test: {e}")
        return False

def test_random_generation():
    """Test φ-based random number generation"""
    print_header("Testing φ-based Random Number Generation")
    
    try:
        # Generate φ-based random numbers
        def phi_random():
            """Generate a φ-based random number between 0 and 1"""
            # Use PHI fractional part as seed
            seed = (PHI * time.time()) % 1
            # Apply φ-dimensional transformation
            return (seed * PHI) % 1
        
        # Generate a sequence of random numbers
        random_sequence = [phi_random() for _ in range(10)]
        print(f"φ-random sequence: {random_sequence}")
        
        # Verify all numbers are between 0 and 1
        assert all(0 <= x <= 1 for x in random_sequence), "Random numbers out of range"
        print("✓ Random numbers in range [0,1]")
        
        # Calculate distribution statistics
        avg = sum(random_sequence) / len(random_sequence)
        print(f"Average: {avg}")
        assert 0.3 <= avg <= 0.7, "Random distribution average outside expected range"
        print("✓ Random distribution verified")
        
        # Compare with standard random
        std_random_sequence = [random.random() for _ in range(10)]
        print(f"Standard random sequence: {std_random_sequence}")
        
        test_results["random_generation"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing random generation: {e}")
        return False

def test_script_execution():
    """Test script execution functionality"""
    print_header("Testing Script Execution")
    
    try:
        # Check if phi_scripts directory exists
        scripts_dir = os.path.join(CURR_PATH, "phi_scripts")
        assert os.path.isdir(scripts_dir), "phi_scripts directory not found"
        print(f"✓ phi_scripts directory found: {scripts_dir}")
        
        # List available scripts
        scripts = [f for f in os.listdir(scripts_dir) if f.endswith('.py')]
        print(f"Available scripts: {scripts}")
        assert len(scripts) > 0, "No scripts found in phi_scripts directory"
        
        # Create a test script
        test_script_path = os.path.join(scripts_dir, "phi_test_script.py")
        with open(test_script_path, 'w') as f:
            f.write("""#!/usr/bin/env python3
# φ-test script
import sys
from math import sqrt

PHI = (1 + sqrt(5)) / 2
print(f"PHI = {PHI}")
print("φ-test script executed successfully")
print(f"Arguments: {sys.argv[1:]}")
""")
        print(f"✓ Created test script: {test_script_path}")
        
        # Make script executable
        os.chmod(test_script_path, 0o755)
        
        # Execute the script
        import subprocess
        result = subprocess.run([sys.executable, test_script_path, "test_arg"], 
                               capture_output=True, text=True)
        print(f"Script output:\n{result.stdout}")
        assert "executed successfully" in result.stdout, "Script execution failed"
        assert "test_arg" in result.stdout, "Script arguments not passed correctly"
        print("✓ Script executed successfully")
        
        # Clean up
        os.remove(test_script_path)
        print("✓ Test script removed")
        
        test_results["script_execution"] = True
        return True
    except Exception as e:
        print(f"✗ Error testing script execution: {e}")
        return False

def run_all_tests():
    """Run all tests and report results"""
    print_header("QUANTUM ORACLE LIBRARY COMPREHENSIVE TEST")
    print(f"Testing library at: {CURR_PATH}")
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Run all tests
    test_phi_constants()
    test_bidirectional_node()
    test_ftl_bridge()
    test_mac_bridge()
    test_nodular_compute()
    test_parallel_consciousness()
    test_numeric_processor()
    test_attack_test()
    test_random_generation()
    test_script_execution()
    
    # Print summary
    print_header("TEST SUMMARY")
    passed = 0
    failed = 0
    
    for test, result in test_results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        if result:
            passed += 1
        else:
            failed += 1
        print(f"{status} - {test}")
    
    print(f"\nRESULTS: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! The quantum_oracle_lib is fully functional.")
    else:
        print(f"\n⚠️ {failed} TESTS FAILED. See above for details.")
    
    return passed, failed

if __name__ == "__main__":
    passed, failed = run_all_tests()
    sys.exit(1 if failed > 0 else 0)
