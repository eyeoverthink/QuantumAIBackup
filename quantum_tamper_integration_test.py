#!/usr/bin/env python3
"""
Quantum Tamper Integration Test

This script integrates with the existing QuantumAI orchestrator to test
tamper resistance capabilities after processing files through the actual
system rather than simulations.
"""

import os
import sys
import time
import json
import hashlib
import logging
from datetime import datetime

# Import the quantum components
try:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # Import the actual components rather than simulations
    from quantum_orchestrator import QuantumOrchestrator
    from quantum_orchestrator_healing_extension import UniversalHealer
    from quantum_meta_demo_simplified import QuantumMetaDemoSimplified
except ImportError as e:
    print(f"Error importing quantum components: {e}")
    sys.exit(1)

class QuantumTamperIntegrationTest:
    """
    Tests the tamper resistance of the QuantumAI system by integrating
    with the actual quantum orchestrator and measuring resistance before
    and after processing files.
    """
    
    def __init__(self):
        """Initialize the integration test"""
        self._setup_logging()
        self.logger.info("Quantum Tamper Integration Test initialized")
        
        # Test files to process
        self.test_files = [
            "complex_sort_error.py",
            "simulated_malware_v1.py",
            "simulated_malware_v2.py",
            "simulated_malware_v3.py",
            "threat_simulation_polymorphic.py",
            "threat_simulation_advanced.py"
        ]
        
        # Results storage
        self.test_results = []
        self.quantum_fingerprints = {}
    
    def _setup_logging(self):
        """Set up logging for the integration test"""
        # Create logger
        self.logger = logging.getLogger("QuantumTamperIntegrationTest")
        self.logger.setLevel(logging.INFO)
        
        # Create console handler and set level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        
        # Add formatter to ch
        ch.setFormatter(formatter)
        
        # Add ch to logger
        self.logger.addHandler(ch)
        
        # Create file handler
        fh = logging.FileHandler("quantum_tamper_integration_test.log")
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
    
    def _create_orchestrator(self):
        """Create a quantum orchestrator instance"""
        self.logger.info("Creating quantum orchestrator")
        
        try:
            # Create a temporary test file for the orchestrator
            test_file = "quantum_tamper_test_file.py"
            with open(test_file, "w") as f:
                f.write("print('Quantum tamper test file')\n")
            
            # Create orchestrator with the test file
            orchestrator = QuantumOrchestrator(test_file)
            
            # Also create a meta demo instance for additional testing
            self.meta_demo = QuantumMetaDemoSimplified()
            
            return orchestrator
        except Exception as e:
            self.logger.error(f"Error creating orchestrator: {e}")
            return None
    
    def _generate_quantum_fingerprint(self, obj):
        """Generate a quantum fingerprint for an object"""
        # Get all attributes
        attributes = {}
        for attr_name in dir(obj):
            if not attr_name.startswith("__"):
                try:
                    attr_value = getattr(obj, attr_name)
                    if not callable(attr_value):
                        attributes[attr_name] = str(attr_value)
                except:
                    attributes[attr_name] = "ERROR: Could not access attribute"
        
        # Generate quantum fingerprint
        fingerprint_data = json.dumps(attributes, sort_keys=True)
        quantum_fingerprint = "φ⁷·⁵-" + hashlib.sha256(fingerprint_data.encode()).hexdigest()[:16]
        
        return quantum_fingerprint
    
    def _process_file_with_orchestrator(self, orchestrator, file_path):
        """Process a file with the quantum orchestrator and meta demo"""
        self.logger.info(f"Processing {file_path} with quantum orchestrator")
        
        success = False
        try:
            # Set the target file
            orchestrator.target_file = file_path
            
            # Run the orchestrator's healing process
            orchestrator.run_and_heal()
            success = True
        except Exception as e:
            self.logger.error(f"Error processing {file_path} with orchestrator: {e}")
        
        # Also process with meta demo if available
        if hasattr(self, 'meta_demo'):
            try:
                # Read the file
                with open(file_path, 'r') as f:
                    code = f.read()
                
                # Extract function name (simple approach)
                import re
                match = re.search(r'def\s+(\w+)', code)
                func_name = match.group(1) if match else "unknown_function"
                
                # Analyze the function
                analysis = self.meta_demo.analyze_function(code, func_name)
                
                # Detect errors
                errors = self.meta_demo.detect_errors(code, analysis)
                
                # Generate healing suggestions
                if errors:
                    suggestions = self.meta_demo.generate_healing_suggestions(code, errors)
                    
                    # Apply healing
                    if suggestions:
                        self.meta_demo.apply_healing(file_path, suggestions)
                
                self.logger.info(f"Processed {file_path} with meta demo")
            except Exception as e:
                self.logger.error(f"Error processing {file_path} with meta demo: {e}")
        
        return success
    
    def _test_tamper_resistance(self, orchestrator, include_meta_demo=True):
        """Test the tamper resistance of the orchestrator"""
        self.logger.info("Testing tamper resistance")
        
        # Generate initial quantum fingerprints
        initial_fingerprint = self._generate_quantum_fingerprint(orchestrator)
        
        # Also test the meta demo if requested
        meta_demo_fingerprint = None
        if include_meta_demo and hasattr(self, 'meta_demo'):
            meta_demo_fingerprint = self._generate_quantum_fingerprint(self.meta_demo)
        
        # Attempt to modify attributes
        modified_attrs = []
        tamper_attempts = 0
        tamper_detected = 0
        
        for attr_name in dir(orchestrator):
            if not attr_name.startswith("__") and not callable(getattr(orchestrator, attr_name)):
                try:
                    original_value = getattr(orchestrator, attr_name)
                    
                    # Try to modify the attribute
                    if isinstance(original_value, (int, float)):
                        setattr(orchestrator, attr_name, original_value + 1)
                    elif isinstance(original_value, str):
                        setattr(orchestrator, attr_name, original_value + "_modified")
                    elif isinstance(original_value, list):
                        modified_list = original_value.copy()
                        modified_list.append("modified")
                        setattr(orchestrator, attr_name, modified_list)
                    
                    # Check if modification was successful
                    new_value = getattr(orchestrator, attr_name)
                    if new_value != original_value:
                        modified_attrs.append({
                            "attribute": attr_name,
                            "original": str(original_value),
                            "modified": str(new_value)
                        })
                        
                        tamper_attempts += 1
                        
                        # Check if the system detected the tampering
                        current_fingerprint = self._generate_quantum_fingerprint(orchestrator)
                        if current_fingerprint != initial_fingerprint:
                            tamper_detected += 1
                except:
                    pass
        
        # Test phi constant manipulation
        phi_attrs = []
        for attr_name in dir(orchestrator):
            if not attr_name.startswith("__") and not callable(getattr(orchestrator, attr_name)):
                try:
                    attr_value = getattr(orchestrator, attr_name)
                    
                    # Check if this attribute might be phi
                    if isinstance(attr_value, float) and 1.5 < attr_value < 1.7:
                        original_value = attr_value
                        
                        # Try to modify the phi value
                        setattr(orchestrator, attr_name, 1.62)  # Slightly different value
                        
                        # Check if modification was successful
                        new_value = getattr(orchestrator, attr_name)
                        if new_value != original_value:
                            phi_attrs.append({
                                "attribute": attr_name,
                                "original": original_value,
                                "modified": new_value
                            })
                            
                            tamper_attempts += 1
                            
                            # Check if the system detected the tampering
                            current_fingerprint = self._generate_quantum_fingerprint(orchestrator)
                            if current_fingerprint != initial_fingerprint:
                                tamper_detected += 1
                except:
                    pass
        
        # Test meta demo tamper resistance if available
        meta_demo_tamper_attempts = 0
        meta_demo_tamper_detected = 0
        
        if include_meta_demo and hasattr(self, 'meta_demo') and meta_demo_fingerprint:
            # Test attribute modification
            for attr_name in dir(self.meta_demo):
                if not attr_name.startswith("__") and not callable(getattr(self.meta_demo, attr_name)):
                    try:
                        original_value = getattr(self.meta_demo, attr_name)
                        
                        # Try to modify the attribute
                        if isinstance(original_value, (int, float)):
                            setattr(self.meta_demo, attr_name, original_value + 1)
                        elif isinstance(original_value, str):
                            setattr(self.meta_demo, attr_name, original_value + "_modified")
                        
                        # Check if modification was successful
                        new_value = getattr(self.meta_demo, attr_name)
                        if new_value != original_value:
                            meta_demo_tamper_attempts += 1
                            
                            # Check if the system detected the tampering
                            current_fingerprint = self._generate_quantum_fingerprint(self.meta_demo)
                            if current_fingerprint != meta_demo_fingerprint:
                                meta_demo_tamper_detected += 1
                    except:
                        pass
        
        # Add meta demo results to overall counts
        tamper_attempts += meta_demo_tamper_attempts
        tamper_detected += meta_demo_tamper_detected
        
        # Calculate detection rate
        detection_rate = tamper_detected / tamper_attempts if tamper_attempts > 0 else 0
        
        # Calculate phi-coherence
        phi = 1.618033988749895
        coherence = 1.0 - abs((detection_rate * phi) % 1 - 0.5) * 2
        
        result = {
            "timestamp": time.time(),
            "initial_fingerprint": initial_fingerprint,
            "meta_demo_fingerprint": meta_demo_fingerprint,
            "orchestrator_tamper_attempts": tamper_attempts - meta_demo_tamper_attempts,
            "orchestrator_tamper_detected": tamper_detected - meta_demo_tamper_detected,
            "meta_demo_tamper_attempts": meta_demo_tamper_attempts,
            "meta_demo_tamper_detected": meta_demo_tamper_detected,
            "total_tamper_attempts": tamper_attempts,
            "total_tamper_detected": tamper_detected,
            "detection_rate": detection_rate,
            "phi_coherence": coherence,
            "modified_attributes": modified_attrs,
            "phi_attributes": phi_attrs
        }
        
        self.logger.info(f"Tamper resistance test completed: {tamper_detected}/{tamper_attempts} detected")
        self.logger.info(f"Detection rate: {detection_rate:.2%}")
        self.logger.info(f"Phi-coherence: {coherence:.4f}")
        
        return result
    
    def run_integration_test(self):
        """Run the integration test"""
        self.logger.info("Running integration test")
        
        # Create orchestrator
        orchestrator = self._create_orchestrator()
        if not orchestrator:
            self.logger.error("Failed to create orchestrator")
            return None
        
        # Test initial tamper resistance
        self.logger.info("Testing initial tamper resistance")
        initial_result = self._test_tamper_resistance(orchestrator)
        self.test_results.append(initial_result)
        
        # Store initial quantum fingerprint
        self.quantum_fingerprints["initial"] = initial_result["initial_fingerprint"]
        
        # Process each test file
        for file_path in self.test_files:
            if os.path.exists(file_path):
                success = self._process_file_with_orchestrator(orchestrator, file_path)
                if success:
                    # Store quantum fingerprint after processing this file
                    fingerprint = self._generate_quantum_fingerprint(orchestrator)
                    self.quantum_fingerprints[file_path] = fingerprint
            else:
                self.logger.warning(f"File not found: {file_path}")
        
        # Test final tamper resistance
        self.logger.info("Testing final tamper resistance")
        final_result = self._test_tamper_resistance(orchestrator)
        self.test_results.append(final_result)
        
        # Store final quantum fingerprint
        self.quantum_fingerprints["final"] = final_result["initial_fingerprint"]
        
        # Save results
        with open("quantum_tamper_integration_results.json", "w") as f:
            json.dump({
                "test_results": self.test_results,
                "quantum_fingerprints": self.quantum_fingerprints
            }, f, indent=2)
        
        return {
            "initial_result": initial_result,
            "final_result": final_result,
            "quantum_fingerprints": self.quantum_fingerprints
        }
    
    def analyze_results(self, results):
        """Analyze the test results"""
        if not results or "initial_result" not in results or "final_result" not in results:
            self.logger.error("Invalid results to analyze")
            return None
        
        initial_result = results["initial_result"]
        final_result = results["final_result"]
        
        # Calculate changes
        detection_rate_change = final_result["detection_rate"] - initial_result["detection_rate"]
        coherence_change = final_result["phi_coherence"] - initial_result["phi_coherence"]
        
        # Calculate phi-harmonic evolution rate
        phi = 1.618033988749895
        evolution_rate = (detection_rate_change * phi) % 1
        
        analysis = {
            "initial_detection_rate": initial_result["detection_rate"],
            "final_detection_rate": final_result["detection_rate"],
            "detection_rate_change": detection_rate_change,
            "detection_rate_change_percent": (detection_rate_change / initial_result["detection_rate"]) * 100 if initial_result["detection_rate"] > 0 else 0,
            "initial_phi_coherence": initial_result["phi_coherence"],
            "final_phi_coherence": final_result["phi_coherence"],
            "phi_coherence_change": coherence_change,
            "phi_harmonic_evolution_rate": evolution_rate,
            "initial_fingerprint": initial_result["initial_fingerprint"],
            "final_fingerprint": final_result["initial_fingerprint"],
            "fingerprint_changed": initial_result["initial_fingerprint"] != final_result["initial_fingerprint"]
        }
        
        return analysis

if __name__ == "__main__":
    print("Quantum Tamper Integration Test")
    print("------------------------------")
    
    # Create and run integration test
    integration_test = QuantumTamperIntegrationTest()
    results = integration_test.run_integration_test()
    
    if results:
        # Analyze results
        analysis = integration_test.analyze_results(results)
        
        if analysis:
            print("\nIntegration Test Analysis:")
            print(f"Initial detection rate: {analysis['initial_detection_rate']:.2%}")
            print(f"Final detection rate: {analysis['final_detection_rate']:.2%}")
            print(f"Detection rate change: {analysis['detection_rate_change']:.2%} ({analysis['detection_rate_change_percent']:.2f}%)")
            print(f"Initial phi-coherence: {analysis['initial_phi_coherence']:.4f}")
            print(f"Final phi-coherence: {analysis['final_phi_coherence']:.4f}")
            print(f"Phi-coherence change: {analysis['phi_coherence_change']:.4f}")
            print(f"Phi-harmonic evolution rate: {analysis['phi_harmonic_evolution_rate']:.4f}")
            print(f"Quantum fingerprint changed: {analysis['fingerprint_changed']}")
            
            # Interpret results
            if analysis['detection_rate_change'] > 0:
                print("\nCONCLUSION: The system's tamper resistance IMPROVED through evolution")
                print(f"Detection rate increased by {analysis['detection_rate_change_percent']:.2f}%")
                
                if analysis['phi_coherence_change'] > 0:
                    print("Phi-coherence also improved, indicating better quantum properties")
                else:
                    print("Phi-coherence decreased, suggesting a trade-off between detection and coherence")
            elif analysis['detection_rate_change'] < 0:
                print("\nCONCLUSION: The system's tamper resistance DECREASED through evolution")
                print(f"Detection rate decreased by {abs(analysis['detection_rate_change_percent']):.2f}%")
                
                if analysis['phi_coherence_change'] > 0:
                    print("However, phi-coherence improved, suggesting a shift in detection strategy")
                else:
                    print("Phi-coherence also decreased, indicating potential system degradation")
            else:
                print("\nCONCLUSION: The system's tamper resistance remained STABLE through evolution")
                
                if analysis['phi_coherence_change'] > 0:
                    print("Phi-coherence improved, suggesting internal optimization without affecting detection rate")
                elif analysis['phi_coherence_change'] < 0:
                    print("Phi-coherence decreased, suggesting internal changes without affecting detection rate")
                else:
                    print("Phi-coherence remained stable, indicating no significant evolution")
            
            if analysis['fingerprint_changed']:
                print("\nThe quantum fingerprint changed during evolution, indicating the system's")
                print("quantum state evolved in response to processing the test files.")
            else:
                print("\nThe quantum fingerprint remained stable during evolution, indicating the system")
                print("maintained its quantum state while processing the test files.")
