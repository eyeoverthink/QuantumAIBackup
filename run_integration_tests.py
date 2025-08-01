"""
Integration Test Runner for Enhanced Quantum Agent V2
This script runs the cross-component integration tests for the Enhanced Quantum Agent V2.
"""

import os
import sys

# Add project root to Python path to enable absolute imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from extensions.quantum_analysis.cross_component_integration_test import CrossComponentIntegrationTest

if __name__ == "__main__":
    # Create output directory
    output_dir = os.path.join(os.path.dirname(__file__), "extensions", "quantum_analysis", "test_results")
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 80)
    print("ENHANCED QUANTUM AGENT V2 - CROSS-COMPONENT INTEGRATION TEST")
    print("=" * 80)
    print(f"Output directory: {output_dir}")
    print("-" * 80)
    
    # Create integration test
    integration_test = CrossComponentIntegrationTest(output_dir=output_dir)
    
    # Run all tests
    results = integration_test.run_all_tests()
    
    # Print overall results
    print("\n" + "=" * 80)
    print("OVERALL RESULTS")
    print("=" * 80)
    print(f"Success: {results['overall_results']['success']}")
    print(f"Success Rate: {results['overall_results']['success_rate']:.2%}")
    print(f"Tests Run: {results['overall_results']['tests_run']}")
    print(f"Tests Passed: {results['overall_results']['tests_passed']}")
    print(f"Tests Failed: {results['overall_results']['tests_failed']}")
    print(f"Execution Time: {results['overall_results']['execution_time']:.6f} seconds")
    print("=" * 80)
