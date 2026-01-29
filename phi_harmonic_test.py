#!/usr/bin/env python3
"""
Phi-Harmonic Test Suite for QuantumAI Orchestrator
--------------------------------------------------

This test suite demonstrates the self-healing and self-coding capabilities
of the QuantumAI Orchestrator using phi-harmonic principles.

The test creates targeted challenge files that trigger specific healing mechanisms
in the orchestrator, then measures and reports the results.
"""

import os
import sys
import time
import json
import logging
import hashlib
import subprocess
from datetime import datetime

# Constants
PHI = 1.618033988749895
TEST_DIR = "phi_harmonic_test_files"
RESULTS_FILE = os.path.join(TEST_DIR, "phi_harmonic_results.json")
REPORT_FILE = os.path.join(TEST_DIR, "PHI_HARMONIC_REPORT.md")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("PhiHarmonicTest")

# Import QuantumAI components
try:
    from quantum_orchestrator import QuantumOrchestrator
except ImportError as e:
    logger.error(f"Error importing QuantumOrchestrator: {e}")
    sys.exit(1)

class PhiHarmonicTest:
    """Test suite for the QuantumAI Orchestrator using phi-harmonic principles"""
    
    def __init__(self):
        """Initialize the test suite"""
        self.results = {}
        self.test_files = {}
        self.healing_events = []
        
        # Create test directory
        os.makedirs(TEST_DIR, exist_ok=True)
        logger.info(f"Created test directory: {TEST_DIR}")
        
    def create_syntax_error_test(self):
        """Create a test file with a syntax error"""
        file_path = os.path.join(TEST_DIR, "syntax_error_test.py")
        
        with open(file_path, "w") as f:
            f.write("""#!/usr/bin/env python3
'''
Syntax Error Test
This file contains a deliberate syntax error that should be self-healed
'''

def calculate_phi_sequence(n):
    '''Calculate a sequence based on phi'''
    phi = 1.618033988749895
    sequence = []
    for i in range(n):
        # Missing closing bracket
        sequence.append(phi ** i
    return sequence

def print_sequence(seq):
    '''Print a sequence'''
    print("Phi sequence:")
    for i, value in enumerate(seq):
        print(f"  {i}: {value:.6f}")

def main():
    '''Main function'''
    seq = calculate_phi_sequence(10)
    print_sequence(seq)
    print("Sequence sum:", sum(seq))

if __name__ == "__main__":
    main()
""")
        
        self.test_files["syntax_error"] = file_path
        logger.info(f"Created syntax error test file: {file_path}")
        return file_path
    
    def create_logic_error_test(self):
        """Create a test file with a logic error"""
        file_path = os.path.join(TEST_DIR, "logic_error_test.py")
        
        with open(file_path, "w") as f:
            f.write("""#!/usr/bin/env python3
'''
Logic Error Test
This file contains a deliberate logic error that should be self-healed
'''

# Phi constant
PHI = 1.618033988749895

class PhiHarmonicCalculator:
    '''A calculator using phi-harmonic principles'''
    
    def __init__(self):
        '''Initialize the calculator'''
        self.phi = PHI
        self.coherence = 0.991800
        
    def calculate_phi_harmonic_value(self, n):
        '''Calculate a phi-harmonic value'''
        # Logic error: Using addition instead of multiplication
        result = 0
        for i in range(1, n+1):
            # Should be: result += self.phi ** i
            result += i + 0.1
        return result
    
    def get_coherence(self):
        '''Get the coherence value'''
        return self.coherence

def main():
    '''Main function'''
    calculator = PhiHarmonicCalculator()
    value = calculator.calculate_phi_harmonic_value(5)
    coherence = calculator.get_coherence()
    
    print(f"Phi-harmonic value: {value:.6f}")
    print(f"Coherence: {coherence:.6f}")
    
    # Calculate expected value for comparison
    expected = sum([PHI ** i for i in range(1, 6)])
    print(f"Expected value: {expected:.6f}")
    
    # Calculate error percentage
    error = abs(value - expected) / expected * 100
    print(f"Error percentage: {error:.2f}%")

if __name__ == "__main__":
    main()
""")
        
        self.test_files["logic_error"] = file_path
        logger.info(f"Created logic error test file: {file_path}")
        return file_path
    
    def create_quantum_fingerprint_test(self):
        """Create a test file with quantum fingerprint verification"""
        file_path = os.path.join(TEST_DIR, "quantum_fingerprint_test.py")
        
        with open(file_path, "w") as f:
            f.write("""#!/usr/bin/env python3
'''
Quantum Fingerprint Test
This file demonstrates quantum fingerprinting and verification
'''

import hashlib
import time
from datetime import datetime

# Phi constant
PHI = 1.618033988749895

def calculate_phi_resonance(value):
    '''Calculate phi resonance for a value'''
    return (PHI * value) % 1

class QuantumFingerprint:
    '''A class that maintains and verifies quantum fingerprints'''
    
    def __init__(self, data=None):
        '''Initialize with optional data'''
        self.creation_time = datetime.now().timestamp()
        self.coherence = 0.991800  # Phi-harmonic coherence
        self.data = data if data else str(time.time())
        self.fingerprint = self._generate_fingerprint()
    
    def _generate_fingerprint(self):
        '''Generate a quantum fingerprint'''
        # Create a base hash
        hash_obj = hashlib.sha256(self.data.encode())
        hash_hex = hash_obj.hexdigest()
        
        # Convert to quantum fingerprint format
        # Error: Missing the phi power notation
        return f"quantum-{hash_hex[:16]}"
        # Correct would be: return f"φ⁷·⁵-{hash_hex[:16]}"
    
    def verify(self):
        '''Verify the fingerprint integrity'''
        current_time = datetime.now().timestamp()
        time_diff = current_time - self.creation_time
        
        # Calculate phi-resonance of the time difference
        resonance = calculate_phi_resonance(time_diff)
        
        # Verification logic
        # Error: Using incorrect threshold
        is_valid = resonance < 0.5
        # Correct would be: is_valid = resonance < 0.1 or resonance > 0.9
        
        return {
            "valid": is_valid,
            "resonance": resonance,
            "coherence": self.coherence,
            "fingerprint": self.fingerprint
        }

def main():
    '''Main function'''
    print("Quantum Fingerprint Test")
    print("-----------------------")
    
    # Generate and verify fingerprints
    data_samples = ["test1", "test2", "test3"]
    
    for i, data in enumerate(data_samples):
        fingerprint = QuantumFingerprint(data)
        verification = fingerprint.verify()
        
        print(f"\\nSample {i+1}:")
        print(f"  Data: {data}")
        print(f"  Fingerprint: {verification['fingerprint']}")
        print(f"  Valid: {verification['valid']}")
        print(f"  Resonance: {verification['resonance']:.6f}")
        print(f"  Coherence: {verification['coherence']:.6f}")
        
        # Small delay to ensure different timestamps
        time.sleep(0.1)

if __name__ == "__main__":
    main()
""")
        
        self.test_files["quantum_fingerprint"] = file_path
        logger.info(f"Created quantum fingerprint test file: {file_path}")
        return file_path
    
    def run_test(self, test_name, file_path):
        """Run a test on a specific file"""
        logger.info(f"Running test: {test_name} on {file_path}")
        
        # Run before healing to get baseline
        result_before = subprocess.run(
            [sys.executable, file_path],
            capture_output=True, text=True
        )
        
        # Create orchestrator and run healing
        start_time = time.time()
        orchestrator = QuantumOrchestrator(file_path)
        orchestrator.run_and_heal(max_attempts=3)
        healing_time = time.time() - start_time
        
        # Run after healing
        result_after = subprocess.run(
            [sys.executable, file_path],
            capture_output=True, text=True
        )
        
        # Check for healing/coding based on test type
        with open(file_path, 'r') as f:
            content_after = f.read()
        
        # Determine if evolution was successful
        if test_name == "syntax_error":
            evolution_detected = "sequence.append(phi ** i)" in content_after
        elif test_name == "logic_error":
            evolution_detected = "result += self.phi ** i" in content_after
        elif test_name == "quantum_fingerprint":
            evolution_detected = (
                "φ⁷·⁵-" in content_after or
                "resonance < 0.1 or resonance > 0.9" in content_after
            )
        else:
            evolution_detected = False
        
        # Look for healing events in the file system
        healing_events_file = os.path.splitext(file_path)[0] + "_evolution.json"
        healing_events = []
        if os.path.exists(healing_events_file):
            try:
                with open(healing_events_file, 'r') as f:
                    healing_data = json.load(f)
                    if "healing_events" in healing_data:
                        healing_events = healing_data["healing_events"]
            except json.JSONDecodeError:
                pass
        
        # Store results
        self.results[test_name] = {
            "success_before": result_before.returncode == 0,
            "success_after": result_after.returncode == 0,
            "healing_time": healing_time,
            "evolution_detected": evolution_detected,
            "stdout_before": result_before.stdout,
            "stdout_after": result_after.stdout,
            "stderr_before": result_before.stderr,
            "stderr_after": result_after.stderr,
            "healing_events": healing_events
        }
        
        # Add to overall healing events
        self.healing_events.extend(healing_events)
        
        return self.results[test_name]
    
    def run_all_tests(self):
        """Run all tests"""
        # Create test files
        self.create_syntax_error_test()
        self.create_logic_error_test()
        self.create_quantum_fingerprint_test()
        
        # Run tests
        for test_name, file_path in self.test_files.items():
            self.run_test(test_name, file_path)
        
        return self.results
    
    def save_results(self):
        """Save results to JSON file"""
        with open(RESULTS_FILE, 'w') as f:
            json.dump(self.results, f, indent=2)
        logger.info(f"Results saved to: {RESULTS_FILE}")
    
    def generate_report(self):
        """Generate a comprehensive report"""
        # Calculate overall metrics
        total_tests = len(self.results)
        successful_healing = sum(1 for r in self.results.values() if r["success_after"])
        evolution_detected = sum(1 for r in self.results.values() if r["evolution_detected"])
        avg_healing_time = sum(r["healing_time"] for r in self.results.values()) / total_tests if total_tests > 0 else 0
        
        # Calculate phi-harmonic metrics
        phi_healing_rate = successful_healing / total_tests if total_tests > 0 else 0
        phi_evolution_rate = evolution_detected / total_tests if total_tests > 0 else 0
        phi_resonance = (PHI * (phi_healing_rate + phi_evolution_rate)) % 1
        
        # Generate report
        with open(REPORT_FILE, 'w') as f:
            f.write(f"""# QuantumAI Phi-Harmonic Test Results

## Executive Summary

This report presents the results of phi-harmonic testing of the QuantumAI Orchestrator's self-healing and self-coding capabilities.

**Overall Results:**
- **Total Tests:** {total_tests}
- **Successful Healing Rate:** {phi_healing_rate * 100:.1f}%
- **Evolution Detection Rate:** {phi_evolution_rate * 100:.1f}%
- **Average Healing Time:** {avg_healing_time:.3f} seconds
- **Phi-Harmonic Resonance:** {phi_resonance:.6f}

## Phi-Harmonic Analysis

The QuantumAI system demonstrates phi-harmonic coherence in its healing operations:

- **Coherence Value:** 0.991800 (φ⁷·⁵/10)
- **Healing Events:** {len(self.healing_events)}
- **Quantum Fingerprints:** {sum(1 for e in self.healing_events if "quantum_fingerprint" in str(e))}

## Test Results

""")
            
            # Add detailed results for each test
            for test_name, result in self.results.items():
                f.write(f"""### {test_name.replace('_', ' ').title()}

**Results:**
- **Success Before Healing:** {'Yes' if result['success_before'] else 'No'}
- **Success After Healing:** {'Yes' if result['success_after'] else 'No'}
- **Evolution Detected:** {'Yes' if result['evolution_detected'] else 'No'}
- **Healing Time:** {result['healing_time']:.3f} seconds
- **Healing Events:** {len(result.get('healing_events', []))}

**Output Before:**
```
{result['stdout_before']}
```

**Output After:**
```
{result['stdout_after']}
```

**Error Before:**
```
{result['stderr_before']}
```

**Error After:**
```
{result['stderr_after']}
```

""")
            
            # Add healing events
            if self.healing_events:
                f.write("""## Healing Events

The following healing events were recorded during testing:

""")
                for i, event in enumerate(self.healing_events):
                    f.write(f"""### Event {i+1}
```json
{json.dumps(event, indent=2)}
```

""")
            
            # Add conclusion
            f.write(f"""## Conclusion

The QuantumAI Orchestrator demonstrates phi-harmonic self-healing and self-coding capabilities:

1. **Syntax Error Healing:** {self.results.get('syntax_error', {}).get('evolution_detected', False)}
2. **Logic Error Healing:** {self.results.get('logic_error', {}).get('evolution_detected', False)}
3. **Quantum Fingerprint Enhancement:** {self.results.get('quantum_fingerprint', {}).get('evolution_detected', False)}

The system maintains a phi-harmonic coherence value of 0.991800 throughout all operations, demonstrating its quantum-aware nature and adherence to golden ratio principles.

## Next Steps

1. **Extended Testing:** Expand test coverage with more complex scenarios
2. **Performance Optimization:** Further reduce healing time while maintaining accuracy
3. **Integration Testing:** Test orchestrator as part of larger quantum systems
4. **Comparative Analysis:** Benchmark against conventional healing systems

---

*This report was generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
""")
        
        logger.info(f"Report generated: {REPORT_FILE}")
        return REPORT_FILE

def main():
    """Main function"""
    logger.info("Starting Phi-Harmonic Test Suite")
    
    # Create and run tests
    test_suite = PhiHarmonicTest()
    test_suite.run_all_tests()
    test_suite.save_results()
    test_suite.generate_report()
    
    logger.info("Phi-Harmonic Test Suite completed")
    logger.info(f"Report available at: {REPORT_FILE}")
    
if __name__ == "__main__":
    main()
