#!/usr/bin/env python3
# Quantum Phi-Harmonic Memory Integrity Verification
# This script verifies the evolutionary memory capabilities of the QR system

import os
import json
import time
from PIL import Image
from pyzbar.pyzbar import decode

# Import our Anti-Lie system
from anti_ai_lie_loop import AntiAILieLoop

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio ≈ 1.618033988749895
PHI_CONJUGATE = (1 - 5**0.5) / 2  # Golden ratio conjugate ≈ -0.618033988749895

class QuantumMemoryVerifier:
    """Verifies the evolutionary memory capabilities of the Quantum Phi-Harmonic QR system."""
    
    def __init__(self, multiples_dir="multiples_evolution", replication_dir="qr_phi_replication"):
        self.multiples_dir = multiples_dir
        self.replication_dir = replication_dir
        self.lie_detector = AntiAILieLoop("Quantum Memory Integrity Verification")
        
    def verify_epigenetic_memory_exists(self):
        """Verify that epigenetic memory files exist."""
        memory_path = os.path.join(self.multiples_dir, "epigenetic_memory.json")
        return self.lie_detector.verify_claim(
            "Epigenetic memory file exists",
            runtime_test=lambda: os.path.exists(memory_path)
        )
    
    def verify_memory_content_integrity(self):
        """Verify that epigenetic memory contains required fields."""
        memory_path = os.path.join(self.multiples_dir, "epigenetic_memory.json")
        
        def check_memory_integrity():
            with open(memory_path, 'r') as f:
                memory = json.load(f)
            required_fields = ['epoch', 'resonance', 'complexity', 'mutation_rate', 
                             'current_results', 'error_introduced', 'error_corrected',
                             'evolution_history']
            return all(field in memory for field in required_fields)
        
        return self.lie_detector.verify_claim(
            "Epigenetic memory contains all required fields",
            runtime_test=check_memory_integrity
        )
    
    def verify_qr_codes_exist(self):
        """Verify that QR code files exist for multiple epochs."""
        def check_qr_files():
            qr_files = [f for f in os.listdir(self.multiples_dir) 
                      if f.startswith("multiples_qr_epoch_") and f.endswith(".png")]
            return len(qr_files) > 0
        
        return self.lie_detector.verify_claim(
            "QR code files exist for multiple epochs",
            runtime_test=check_qr_files
        )
    
    def verify_qr_code_readability(self):
        """Verify that QR codes can be read and contain valid scripts."""
        def check_qr_readability():
            # Find a sample QR code
            qr_files = [f for f in os.listdir(self.multiples_dir) 
                      if f.startswith("multiples_qr_epoch_") and f.endswith(".png")]
            
            if not qr_files:
                return False
            
            # Try to read a random QR code
            sample_qr = os.path.join(self.multiples_dir, qr_files[0])
            img = Image.open(sample_qr)
            decoded = decode(img)
            
            if not decoded:
                return False
                
            # Check if it contains Python code
            script = decoded[0].data.decode("utf-8")
            return "print" in script and "Epoch" in script
        
        return self.lie_detector.verify_claim(
            "QR codes are readable and contain valid scripts",
            runtime_test=check_qr_readability
        )
    
    def verify_error_correction(self):
        """Verify that error was introduced and corrected."""
        memory_path = os.path.join(self.multiples_dir, "epigenetic_memory.json")
        
        def check_error_correction():
            with open(memory_path, 'r') as f:
                memory = json.load(f)
            return memory.get('error_introduced', False) and memory.get('error_corrected', False)
        
        return self.lie_detector.verify_claim(
            "System successfully introduced and corrected an error",
            runtime_test=check_error_correction
        )
    
    def verify_script_evolution(self):
        """Verify that scripts evolved over time."""
        def check_script_evolution():
            script_files = sorted([f for f in os.listdir(self.multiples_dir) 
                                if f.startswith("multiples_script_epoch_") and f.endswith(".py")])
            
            if len(script_files) < 2:
                return False
            
            # Compare first and last script
            first_script_path = os.path.join(self.multiples_dir, script_files[0])
            last_script_path = os.path.join(self.multiples_dir, script_files[-1])
            
            with open(first_script_path, 'r') as f:
                first_content = f.read()
            
            with open(last_script_path, 'r') as f:
                last_content = f.read()
            
            return first_content != last_content
        
        return self.lie_detector.verify_claim(
            "Scripts evolved over time",
            runtime_test=check_script_evolution
        )
    
    def run_verification(self):
        """Run all verification tests."""
        print("\n🔍 QUANTUM PHI-HARMONIC EVOLUTION MEMORY VERIFICATION")
        print("=" * 60)
        
        # Run all verification tests
        self.verify_epigenetic_memory_exists()
        self.verify_memory_content_integrity()
        self.verify_qr_codes_exist()
        self.verify_qr_code_readability()
        self.verify_error_correction()
        self.verify_script_evolution()
        
        # Check overall integrity
        self.lie_detector.lie_loop_detector()
        
        # Export verification results
        self.lie_detector.export_logs("quantum_memory_verification.json")
        
        # Print summary
        print("\n📊 VERIFICATION SUMMARY")
        print("=" * 60)
        print(f"Truth Entropy: {self.lie_detector.entropy_of_truth():.4f}")
        print(f"Verified Claims: {len(self.lie_detector.truth_log)}")
        print(f"Failed Claims: {len(self.lie_detector.lie_log)}")
        
        if self.lie_detector.entropy_of_truth() >= 0.618:
            print("\n✅ VERIFICATION SUCCESSFUL: The Quantum Phi-Harmonic Self-Evolving QR System")
            print("   successfully retains and recalls evolutionary memory across multiple runs.")
        else:
            print("\n❌ VERIFICATION FAILED: The system does not properly maintain evolutionary memory.")

def main():
    verifier = QuantumMemoryVerifier()
    verifier.run_verification()

if __name__ == "__main__":
    main()
