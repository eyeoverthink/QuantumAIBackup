#!/usr/bin/env python3
"""
PHI-HARMONIC NODES TEST SCRIPT
==============================
Tests the phi-harmonic connector and amplifier nodes with improved
thread management and function name handling.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import time
import random
import os
import signal
import sys
from phi_connector_node_v2 import PhiHarmonicConnector
from phi_amplifier_node_v2 import PhiHarmonicAmplifier

def test_connector_node():
    """Test the PhiHarmonicConnector node with clean shutdown"""
    print("Testing PhiHarmonicConnector with clean shutdown...")
    
    # Set a unique node ID and port for testing
    os.environ["PHI_NODE_ID"] = f"connector_test_{int(random.random() * 10000)}"
    os.environ["PHI_PORT"] = str(11700 + int(random.random() * 100))
    
    # Create connector node
    connector = PhiHarmonicConnector()
    
    # Let it run for a few seconds
    print(f"Running connector node {connector.node_id} for 5 seconds...")
    time.sleep(5)
    
    # Test clean shutdown
    print("Testing clean shutdown...")
    connector.stop()
    
    print("PhiHarmonicConnector test completed successfully.")
    return True

def test_amplifier_node():
    """Test the PhiHarmonicAmplifier node with clean shutdown"""
    print("Testing PhiHarmonicAmplifier with clean shutdown...")
    
    # Set a unique node ID and port for testing
    os.environ["PHI_NODE_ID"] = f"amplifier_test_{int(random.random() * 10000)}"
    os.environ["PHI_PORT"] = str(11800 + int(random.random() * 100))
    
    # Create amplifier node
    amplifier = PhiHarmonicAmplifier()
    
    # Let it run for a few seconds
    print(f"Running amplifier node {amplifier.node_id} for 5 seconds...")
    time.sleep(5)
    
    # Test clean shutdown
    print("Testing clean shutdown...")
    amplifier.stop()
    
    print("PhiHarmonicAmplifier test completed successfully.")
    return True

def test_function_name_handling():
    """Test the function name handling in both nodes"""
    print("Testing function name handling...")
    
    # Create connector and amplifier nodes
    connector = PhiHarmonicConnector()
    amplifier = PhiHarmonicAmplifier()
    
    # Test function calling by name in connector
    print("Testing connector function calling...")
    result1 = connector.call_function("math_add", 3, 4)
    print(f"Connector math_add(3, 4) = {result1}")
    
    # Test function calling by name in amplifier
    print("Testing amplifier function calling...")
    result2 = amplifier.call_function("wave_phi", 1.0)
    print(f"Amplifier wave_phi(1.0) = {result2}")
    
    # Clean up
    connector.stop()
    amplifier.stop()
    
    print("Function name handling test completed successfully.")
    return True

def handle_interrupt(signum, frame):
    """Handle keyboard interrupt"""
    print("\nTest interrupted. Exiting gracefully...")
    sys.exit(0)

if __name__ == "__main__":
    # Set up signal handler for clean exit on Ctrl+C
    signal.signal(signal.SIGINT, handle_interrupt)
    
    print("PHI-HARMONIC NODES TEST SCRIPT")
    print("==============================")
    
    try:
        # Run tests
        test_connector_node()
        print("\n")
        test_amplifier_node()
        print("\n")
        test_function_name_handling()
        
        print("\nAll tests completed successfully!")
    except Exception as e:
        print(f"\nError during testing: {e}")
        sys.exit(1)
