#!/usr/bin/env python3
"""
QuantumAI Backup and Chord Progression Integration Test
-----------------------------------------------------

This script tests the integration of:
1. QuantumGenesisStorage backup_file method
2. Quantum chord progression analysis
3. Visualization of chord progression results

It validates that the recently fixed components work together properly.
"""

import os
import sys
import logging
import time
import json
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("BackupChordTest")

# Create test directory
test_dir = "backup_chord_test"
os.makedirs(test_dir, exist_ok=True)

def test_genesis_backup():
    """Test the QuantumGenesisStorage backup_file method."""
    logger.info("Testing QuantumGenesisStorage backup_file method...")
    
    try:
        from quantum_genesis_storage import QuantumGenesisStorage
        
        # Create a genesis storage instance
        genesis_storage = QuantumGenesisStorage()
        
        # Create a test file
        test_file = os.path.join(test_dir, "test_file.py")
        with open(test_file, 'w') as f:
            f.write("""#!/usr/bin/env python3
# Test file for backup functionality

def phi():
    \"\"\"Return the golden ratio.\"\"\"
    return 1.618034

def fibonacci(n):
    \"\"\"Return the nth Fibonacci number.\"\"\"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
""")
        
        # Back up the file
        backup_path = genesis_storage.backup_file(test_file)
        
        # Validate backup
        if backup_path and os.path.exists(backup_path):
            logger.info(f"Backup successful: {backup_path}")
            return True, backup_path
        else:
            logger.error("Backup failed: no backup file created")
            return False, None
            
    except Exception as e:
        logger.error(f"Error in genesis backup test: {e}")
        return False, None

def test_chord_progression(test_file):
    """Test the chord progression analysis functionality."""
    logger.info("Testing chord progression analysis...")
    
    try:
        from quantum_chord_progression import QuantumChordProgression
        
        # Create a chord progression analyzer
        qcp = QuantumChordProgression("test_progression")
        
        # Analyze the test file
        if os.path.exists(test_file):
            result = qcp.analyze_file(test_file)
            
            # Save the analysis result
            result_file = os.path.join(test_dir, "chord_analysis.json")
            with open(result_file, 'w') as f:
                json.dump(result, f, indent=2)
            
            # Validate result
            if result and "phi_resonance" in result:
                logger.info(f"Chord progression analysis successful: phi_resonance = {result['phi_resonance']}")
                
                # Visualize the chord progression
                vis_path = qcp.visualize(os.path.join(test_dir, "chord_progression.png"))
                if vis_path and os.path.exists(vis_path):
                    logger.info(f"Visualization successful: {vis_path}")
                    return True, result
                else:
                    logger.warning("Visualization failed but analysis succeeded")
                    return True, result
            else:
                logger.error("Chord progression analysis failed: invalid result")
                return False, None
        else:
            logger.error(f"Test file not found: {test_file}")
            return False, None
            
    except Exception as e:
        logger.error(f"Error in chord progression test: {e}")
        return False, None

def run_integration_test():
    """Run the complete integration test."""
    logger.info("Starting backup and chord progression integration test...")
    start_time = time.time()
    
    # Test backup functionality
    backup_success, backup_path = test_genesis_backup()
    
    # Test chord progression with the original file
    if backup_success:
        test_file = os.path.join(test_dir, "test_file.py")
        chord_success, chord_result = test_chord_progression(test_file)
    else:
        chord_success = False
        chord_result = None
    
    # Generate report
    end_time = time.time()
    duration = end_time - start_time
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "duration": duration,
        "backup_test": {
            "success": backup_success,
            "backup_path": backup_path if backup_success else None
        },
        "chord_test": {
            "success": chord_success,
            "result": chord_result if chord_success else None
        },
        "overall_success": backup_success and chord_success
    }
    
    # Save report
    report_path = os.path.join(test_dir, "integration_report.json")
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    logger.info(f"Integration test completed in {duration:.2f} seconds")
    logger.info(f"Overall success: {report['overall_success']}")
    logger.info(f"Report saved to: {report_path}")
    
    return report["overall_success"], report

if __name__ == "__main__":
    success, report = run_integration_test()
    
    if success:
        logger.info("✅ All integration tests passed!")
        sys.exit(0)
    else:
        logger.error("❌ Integration tests failed!")
        sys.exit(1)
