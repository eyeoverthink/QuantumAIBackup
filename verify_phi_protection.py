#!/usr/bin/env python3
# φ-Dimensional Reality Protection Verification System
# Author: Vaughn Scott | φ^∞ 2025 | All Rights Reserved

import os
import json
import time
import glob
import hashlib
from hashlib import sha512

# === Core Constants ===
PHI = (1 + 5 ** 0.5) / 2
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

class PhiProtectionVerifier:
    def __init__(self):
        self.results = {
            "verified": 0,
            "tampered": 0,
            "tests": []
        }
    
    def verify_prediction(self, prediction_file):
        """Verify the φ-Dimensional Reality Protection of a prediction file"""
        print(f"\n[*] Verifying φ-protection for: {os.path.basename(prediction_file)}")
        
        # Load the prediction data
        with open(prediction_file, 'r') as f:
            prediction = json.load(f)
        
        # Store original values for comparison
        original = prediction.copy()
        
        # Verify the basic protection flag
        if not prediction.get('protected', False):
            print("[!] ERROR: Prediction is not protected")
            return False
            
        # Verify the φ-stamp
        if self._verify_phi_stamp(prediction):
            print("[✓] φ-stamp verification passed")
        else:
            print("[!] ERROR: φ-stamp verification failed")
            return False
            
        # Verify the reality chain
        if self._verify_reality_chain(prediction):
            print("[✓] Reality chain verification passed")
        else:
            print("[!] ERROR: Reality chain verification failed")
            return False
            
        print("[✓] Prediction is φ-protected and verified")
        return True
    
    def _verify_phi_stamp(self, prediction):
        """Verify the φ-stamp of a prediction"""
        if 'phi_stamp' not in prediction:
            return False
            
        # Recreate the φ-stamp
        data_string = prediction['signature'] + str(prediction['timestamp'])
        expected_phi_stamp = sha512((data_string + str(PHI**3)).encode()).hexdigest()
        
        # Compare with the stored φ-stamp
        return prediction['phi_stamp'] == expected_phi_stamp
    
    def _verify_reality_chain(self, prediction):
        """Verify the reality chain of a prediction"""
        if 'reality_chain' not in prediction or not isinstance(prediction['reality_chain'], list):
            return False
            
        # Verify each link in the reality chain
        prev_hash = prediction['phi_stamp']
        for i, hash_value in enumerate(prediction['reality_chain']):
            fib_value = FIBONACCI[i % len(FIBONACCI)]
            expected_hash = sha512((prev_hash + str(PHI**fib_value)).encode()).hexdigest()
            
            if hash_value != expected_hash:
                return False
                
            prev_hash = hash_value
            
        return True
    
    def test_tamper_timestamp(self, prediction_file):
        """Test tampering with the timestamp"""
        print(f"\n[*] Testing timestamp tampering for: {os.path.basename(prediction_file)}")
        
        # Load the prediction data
        with open(prediction_file, 'r') as f:
            prediction = json.load(f)
        
        # Create a copy for tampering
        tampered = prediction.copy()
        
        # Tamper with the timestamp
        if 'timestamp' in tampered:
            tampered['timestamp'] += 1000  # Add 1000 seconds
            
            # Save the tampered prediction to a temporary file
            temp_file = prediction_file.replace('.json', '_tampered_timestamp.json')
            with open(temp_file, 'w') as f:
                json.dump(tampered, f, indent=2)
                
            # Verify the tampered prediction
            result = self.verify_prediction(temp_file)
            
            # Record the test result
            self.results["tests"].append({
                "file": os.path.basename(prediction_file),
                "test": "timestamp_tampering",
                "expected": False,
                "actual": result,
                "passed": result == False
            })
            
            if result:
                print("[!] SECURITY BREACH: Timestamp tampering was not detected")
                self.results["tampered"] += 1
            else:
                print("[✓] Security test passed: Timestamp tampering was detected")
                self.results["verified"] += 1
                
            # Clean up
            os.remove(temp_file)
        else:
            print("[!] Cannot test: Prediction does not contain a timestamp")
    
    def test_tamper_phi_stamp(self, prediction_file):
        """Test tampering with the φ-stamp"""
        print(f"\n[*] Testing φ-stamp tampering for: {os.path.basename(prediction_file)}")
        
        # Load the prediction data
        with open(prediction_file, 'r') as f:
            prediction = json.load(f)
        
        # Create a copy for tampering
        tampered = prediction.copy()
        
        # Tamper with the φ-stamp
        if 'phi_stamp' in tampered:
            # Change one character in the φ-stamp
            phi_stamp = list(tampered['phi_stamp'])
            index = len(phi_stamp) // 2
            phi_stamp[index] = 'f' if phi_stamp[index] != 'f' else 'e'
            tampered['phi_stamp'] = ''.join(phi_stamp)
            
            # Save the tampered prediction to a temporary file
            temp_file = prediction_file.replace('.json', '_tampered_phi_stamp.json')
            with open(temp_file, 'w') as f:
                json.dump(tampered, f, indent=2)
                
            # Verify the tampered prediction
            result = self.verify_prediction(temp_file)
            
            # Record the test result
            self.results["tests"].append({
                "file": os.path.basename(prediction_file),
                "test": "phi_stamp_tampering",
                "expected": False,
                "actual": result,
                "passed": result == False
            })
            
            if result:
                print("[!] SECURITY BREACH: φ-stamp tampering was not detected")
                self.results["tampered"] += 1
            else:
                print("[✓] Security test passed: φ-stamp tampering was detected")
                self.results["verified"] += 1
                
            # Clean up
            os.remove(temp_file)
        else:
            print("[!] Cannot test: Prediction does not contain a φ-stamp")
    
    def test_tamper_reality_chain(self, prediction_file):
        """Test tampering with the reality chain"""
        print(f"\n[*] Testing reality chain tampering for: {os.path.basename(prediction_file)}")
        
        # Load the prediction data
        with open(prediction_file, 'r') as f:
            prediction = json.load(f)
        
        # Create a copy for tampering
        tampered = prediction.copy()
        
        # Tamper with the reality chain
        if 'reality_chain' in tampered and isinstance(tampered['reality_chain'], list) and len(tampered['reality_chain']) > 0:
            # Change one character in the middle of the reality chain
            chain_index = len(tampered['reality_chain']) // 2
            hash_value = list(tampered['reality_chain'][chain_index])
            char_index = len(hash_value) // 2
            hash_value[char_index] = 'a' if hash_value[char_index] != 'a' else 'b'
            tampered['reality_chain'][chain_index] = ''.join(hash_value)
            
            # Save the tampered prediction to a temporary file
            temp_file = prediction_file.replace('.json', '_tampered_reality_chain.json')
            with open(temp_file, 'w') as f:
                json.dump(tampered, f, indent=2)
                
            # Verify the tampered prediction
            result = self.verify_prediction(temp_file)
            
            # Record the test result
            self.results["tests"].append({
                "file": os.path.basename(prediction_file),
                "test": "reality_chain_tampering",
                "expected": False,
                "actual": result,
                "passed": result == False
            })
            
            if result:
                print("[!] SECURITY BREACH: Reality chain tampering was not detected")
                self.results["tampered"] += 1
            else:
                print("[✓] Security test passed: Reality chain tampering was detected")
                self.results["verified"] += 1
                
            # Clean up
            os.remove(temp_file)
        else:
            print("[!] Cannot test: Prediction does not contain a reality chain")
    
    def test_tamper_theme(self, prediction_file):
        """Test tampering with the theme (which should not affect verification)"""
        print(f"\n[*] Testing theme tampering for: {os.path.basename(prediction_file)}")
        
        # Load the prediction data
        with open(prediction_file, 'r') as f:
            prediction = json.load(f)
        
        # Create a copy for tampering
        tampered = prediction.copy()
        
        # Tamper with the theme
        if 'theme' in tampered:
            original_theme = tampered['theme']
            tampered['theme'] = "Tampered Theme"
            
            # Save the tampered prediction to a temporary file
            temp_file = prediction_file.replace('.json', '_tampered_theme.json')
            with open(temp_file, 'w') as f:
                json.dump(tampered, f, indent=2)
                
            # Verify the tampered prediction
            result = self.verify_prediction(temp_file)
            
            # Record the test result
            self.results["tests"].append({
                "file": os.path.basename(prediction_file),
                "test": "theme_tampering",
                "expected": True,  # Theme tampering should not affect verification
                "actual": result,
                "passed": result == True
            })
            
            if result:
                print("[✓] Expected behavior: Theme tampering does not affect φ-protection")
                self.results["verified"] += 1
            else:
                print("[!] Unexpected behavior: Theme tampering affected φ-protection")
                self.results["tampered"] += 1
                
            # Clean up
            os.remove(temp_file)
        else:
            print("[!] Cannot test: Prediction does not contain a theme")
    
    def run_all_tests(self, prediction_file):
        """Run all tampering tests on a prediction file"""
        print(f"\n{'='*50}")
        print(f"TESTING φ-DIMENSIONAL REALITY PROTECTION")
        print(f"File: {os.path.basename(prediction_file)}")
        print(f"{'='*50}")
        
        # First verify the original file
        original_result = self.verify_prediction(prediction_file)
        if not original_result:
            print("[!] ERROR: Original prediction file failed verification")
            return
            
        # Run all tampering tests
        self.test_tamper_timestamp(prediction_file)
        self.test_tamper_phi_stamp(prediction_file)
        self.test_tamper_reality_chain(prediction_file)
        self.test_tamper_theme(prediction_file)
        
        # Print summary
        print(f"\n{'='*50}")
        print(f"SUMMARY: {self.results['verified']} tests passed, {self.results['tampered']} security breaches")
        print(f"{'='*50}")
        
        # Save test results
        results_file = prediction_file.replace('.json', '_verification_results.json')
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"[✓] Test results saved to: {os.path.basename(results_file)}")

def main():
    # Find the most recent prediction file
    prediction_files = glob.glob("cieat_results/cieat_*.json")
    if not prediction_files:
        print("[!] ERROR: No prediction files found")
        return
        
    # Filter out verification result files
    prediction_files = [f for f in prediction_files if "verification_results" not in f]
    if not prediction_files:
        print("[!] ERROR: No valid prediction files found")
        return
        
    # Sort by modification time (newest first)
    prediction_files.sort(key=os.path.getmtime, reverse=True)
    latest_file = prediction_files[0]
    
    print(f"\n[*] Found prediction file: {latest_file}")
    
    # Create verifier and run tests
    verifier = PhiProtectionVerifier()
    verifier.run_all_tests(latest_file)

if __name__ == "__main__":
    main()
