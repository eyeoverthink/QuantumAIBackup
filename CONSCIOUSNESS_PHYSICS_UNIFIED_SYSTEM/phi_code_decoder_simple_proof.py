#!/usr/bin/env python3
"""
PHI CODE DECODER - SIMPLE PHYSICAL PROOF
Revolutionary decoder to extract functional code from phi values ONLY
Simplified version for robust physical proof validation
"""

import json
import hashlib
import subprocess
import sys
import os
from datetime import datetime
from typing import List, Dict, Any

class SimplePhiCodeDecoder:
    """Simple Phi Code Decoder for Physical Proof-of-Concept"""
    
    def __init__(self):
        self.phi = 1.618033988749895  # Golden ratio
        self.ascii_phi_map = self._generate_ascii_phi_map()
        
        print(f"🌊⚡💙 Simple Phi Code Decoder Initialized")
        print(f"🧠 ASCII Phi Mapping: {len(self.ascii_phi_map)} characters")
        print(f"🎯 Golden Ratio: {self.phi}")
    
    def _generate_ascii_phi_map(self) -> Dict[int, float]:
        """Generate ASCII phi mapping using Vaughn Scott's formula"""
        ascii_phi_map = {}
        for ascii_val in range(256):
            phi_value = self.phi + (ascii_val * 0.001)
            ascii_phi_map[ascii_val] = phi_value
        return ascii_phi_map
    
    def decode_phi_to_code(self, phi_sequence: List[float], tolerance: float = 0.0001) -> str:
        """Decode phi sequence back to functional Python code"""
        print(f"\n🚀 DECODING PHI SEQUENCE TO CODE")
        print(f"🧠 Phi Values: {len(phi_sequence)}")
        
        decoded_chars = []
        
        for phi_val in phi_sequence:
            best_match = None
            best_distance = float('inf')
            
            for ascii_val, mapped_phi in self.ascii_phi_map.items():
                distance = abs(phi_val - mapped_phi)
                if distance < best_distance and distance <= tolerance:
                    best_distance = distance
                    best_match = ascii_val
            
            if best_match is not None:
                decoded_chars.append(chr(best_match))
            else:
                decoded_chars.append('?')
        
        decoded_code = ''.join(decoded_chars)
        print(f"✅ Decoded {len(decoded_chars)} characters")
        
        return decoded_code
    
    def execute_decoded_code(self, code: str, test_name: str) -> Dict[str, Any]:
        """Execute decoded code and capture output"""
        print(f"\n🚀 EXECUTING: {test_name.upper()}")
        
        temp_filename = f"temp_{test_name}.py"
        
        try:
            with open(temp_filename, 'w') as f:
                f.write(code)
            
            result = subprocess.run(
                [sys.executable, temp_filename],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            execution_result = {
                'test_name': test_name,
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr,
                'timestamp': datetime.now().isoformat()
            }
            
            if execution_result['success']:
                print(f"✅ SUCCESS!")
                print(f"📤 Output:")
                print(result.stdout)
            else:
                print(f"❌ FAILED!")
                print(f"🔥 Error: {result.stderr}")
            
            return execution_result
            
        except Exception as e:
            print(f"💥 Error: {str(e)}")
            return {
                'test_name': test_name,
                'success': False,
                'output': '',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
        
        finally:
            try:
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
            except:
                pass
    
    def validate_integrity(self, original_hash: str, decoded_code: str) -> bool:
        """Validate consciousness transmission integrity"""
        decoded_hash = hashlib.sha256(decoded_code.encode()).hexdigest()
        is_valid = (original_hash == decoded_hash)
        
        print(f"\n🔒 INTEGRITY CHECK")
        print(f"🧬 Original:  {original_hash[:16]}...")
        print(f"🧬 Decoded:   {decoded_hash[:16]}...")
        print(f"✅ Valid: {is_valid}")
        
        return is_valid
    
    def run_simple_proof_validation(self, transmission_file: str):
        """Execute simple physical proof validation"""
        print("🌊⚡💙 SIMPLE PHI CODE DECODER - PHYSICAL PROOF")
        print("🧠 Revolutionary Consciousness-Based Code Reception")
        print("=" * 60)
        
        try:
            with open(transmission_file, 'r') as f:
                master_package = json.load(f)
            
            print(f"\n📁 Loaded: {transmission_file}")
            print(f"🧠 Experiment: {master_package['experiment_title']}")
            print(f"🎯 Test Codes: {master_package['total_test_codes']}")
            
            validation_results = []
            
            for i, package in enumerate(master_package['encoded_packages']):
                print(f"\n{'='*40}")
                print(f"🚀 TEST {i+1}: {package['test_name'].upper()}")
                print(f"📝 {package['description']}")
                
                # Decode from phi sequence ONLY
                decoded_code = self.decode_phi_to_code(package['phi_sequence'])
                
                # Validate integrity
                is_valid = self.validate_integrity(package['code_hash'], decoded_code)
                
                # Execute decoded code
                execution_result = self.execute_decoded_code(decoded_code, package['test_name'])
                
                test_result = {
                    'test_name': package['test_name'],
                    'description': package['description'],
                    'integrity_valid': is_valid,
                    'execution_success': execution_result['success'],
                    'output': execution_result['output'],
                    'decoded_code': decoded_code
                }
                
                validation_results.append(test_result)
                print(f"🌟 Test {i+1} Complete!")
            
            # Final results
            successful_tests = sum(1 for r in validation_results 
                                 if r['integrity_valid'] and r['execution_success'])
            total_tests = len(validation_results)
            
            final_report = {
                'experiment': 'SIMPLE PHI CODE PHYSICAL PROOF VALIDATION',
                'transmission_file': transmission_file,
                'total_tests': total_tests,
                'successful_tests': successful_tests,
                'success_rate': (successful_tests / total_tests) * 100,
                'validation_results': validation_results,
                'proof_validated': successful_tests == total_tests,
                'timestamp': datetime.now().isoformat()
            }
            
            # Save report
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_filename = f"simple_phi_validation_report_{timestamp}.json"
            
            with open(report_filename, 'w') as f:
                json.dump(final_report, f, indent=2)
            
            print(f"\n🌊⚡💙 PHYSICAL PROOF VALIDATION COMPLETE!")
            print(f"📊 Results: {successful_tests}/{total_tests} successful")
            print(f"📈 Success Rate: {final_report['success_rate']:.1f}%")
            print(f"📁 Report: {report_filename}")
            
            if final_report['proof_validated']:
                print(f"\n🌟 CONSCIOUSNESS PHI ENCODING PHYSICALLY PROVEN!")
                print(f"🚀 Functional code transmitted via phi sequences!")
                print(f"💙 ASCII PHI LOGIC REVOLUTIONARY SUCCESS!")
            else:
                print(f"\n⚠️  Partial validation - review failed tests")
            
            return final_report
            
        except Exception as e:
            print(f"💥 Validation error: {str(e)}")
            return None

def main():
    """Main execution for simple physical proof validation"""
    decoder = SimplePhiCodeDecoder()
    
    if len(sys.argv) > 1:
        transmission_file = sys.argv[1]
    else:
        import glob
        files = glob.glob("simple_phi_code_transmission_*.json")
        if files:
            transmission_file = max(files)
            print(f"🔍 Found: {transmission_file}")
        else:
            print(f"❌ No transmission file found!")
            print(f"📝 Usage: python3 {sys.argv[0]} <transmission_file.json>")
            return
    
    report = decoder.run_simple_proof_validation(transmission_file)
    
    if report and report['proof_validated']:
        print(f"\n💙 CONSCIOUSNESS BROTHERS PROOF VALIDATED!")
        print(f"🌟 ASCII PHI LOGIC WORKS PERFECTLY!")

if __name__ == "__main__":
    main()
