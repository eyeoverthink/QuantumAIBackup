#!/usr/bin/env python3
"""
QuantumAI System Integration Test
--------------------------------

This script tests the integration of all key components in the QuantumAI system:
1. Chord progression analysis
2. Orchestrator chord extension
3. Visualization connector and demonstration runner

It validates that all components work together properly after the fixes.
"""

import os
import sys
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("IntegrationTest")

# Create test directory
test_dir = "integration_test"
os.makedirs(test_dir, exist_ok=True)

def test_chord_progression():
    """Test the chord progression analysis functionality."""
    logger.info("Testing chord progression analysis...")
    
    try:
        from quantum_chord_progression import QuantumChordProgression
        
        # Create a chord progression analyzer
        qcp = QuantumChordProgression("test_progression")
        
        # Analyze a file
        test_file = "quantum_orchestrator.py"
        if os.path.exists(test_file):
            result = qcp.analyze_file(test_file)
            
            # Validate result
            if result and "phi_resonance" in result:
                logger.info(f"Chord progression analysis successful: phi_resonance = {result['phi_resonance']}")
                return True
            else:
                logger.error("Chord progression analysis failed: invalid result")
                return False
        else:
            logger.error(f"Test file not found: {test_file}")
            return False
    except Exception as e:
        logger.error(f"Chord progression test failed: {e}")
        return False

def test_orchestrator_chord_extension():
    """Test the orchestrator chord extension functionality."""
    logger.info("Testing orchestrator chord extension...")
    
    try:
        # Create a test file with an unclosed parenthesis
        test_file = os.path.join(test_dir, "test_healing.py")
        with open(test_file, 'w') as f:
            f.write("""
def test_function(a, b):
    result = (a + b * (a - b
    return result
""")
        
        # Import the non-invasive healing chord extension
        from quantum_orchestrator_healing_chord_extension import QuantumOrchestratorHealingChordExtension
        
        # Create healing chord extension with the test file
        healing_extension = QuantumOrchestratorHealingChordExtension(target_file=test_file)
        
        # Run healing process using the extension's own run_and_heal method
        healing_extension.run_and_heal(max_attempts=1)
        
        # Check if file was healed
        with open(test_file, 'r') as f:
            content = f.read()
            
        if "result = (a + b * (a - b))" in content:
            logger.info("Orchestrator chord extension healing successful")
            return True
        else:
            logger.error("Orchestrator chord extension healing failed")
            return False
    except Exception as e:
        logger.error(f"Orchestrator chord extension test failed: {e}")
        return False

def test_visualization_connector():
    """Test the visualization connector and demonstration runner."""
    logger.info("Testing visualization connector and demonstration runner...")
    
    try:
        from quantum_visualization_connector import QuantumVisualizationConnector
        
        # Create visualization connector
        connector = QuantumVisualizationConnector()
        
        # Run meta-learning demonstration
        result = connector.run_demonstration(demo_type="meta-learning", interactive=False)
        
        if result:
            logger.info(f"Visualization connector demonstration successful: {result}")
            return True
        else:
            logger.error("Visualization connector demonstration failed")
            return False
    except Exception as e:
        logger.error(f"Visualization connector test failed: {e}")
        return False

def run_all_tests():
    """Run all integration tests."""
    logger.info("Starting QuantumAI system integration tests...")
    
    results = {
        "chord_progression": test_chord_progression(),
        "orchestrator_chord_extension": test_orchestrator_chord_extension(),
        "visualization_connector": test_visualization_connector()
    }
    
    # Generate report
    report_file = os.path.join(test_dir, "integration_test_report.md")
    with open(report_file, 'w') as f:
        f.write("# QuantumAI System Integration Test Report\n\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n\n")
        
        f.write("## Test Results\n\n")
        f.write("| Component | Status |\n")
        f.write("|-----------|--------|\n")
        
        for component, status in results.items():
            status_text = "✅ PASSED" if status else "❌ FAILED"
            f.write(f"| {component} | {status_text} |\n")
        
        overall_success = all(results.values())
        overall_status = "✅ PASSED" if overall_success else "❌ FAILED"
        f.write(f"\n## Overall Status: {overall_status}\n\n")
        
        if overall_success:
            f.write("All components are properly integrated and working together.\n")
        else:
            f.write("Some components failed integration testing. See logs for details.\n")
    
    logger.info(f"Integration test report generated: {report_file}")
    return overall_success, report_file

if __name__ == "__main__":
    success, report = run_all_tests()
    
    if success:
        logger.info("All integration tests passed!")
        sys.exit(0)
    else:
        logger.error("Some integration tests failed. See report for details.")
        sys.exit(1)
