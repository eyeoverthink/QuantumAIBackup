#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Phi-Harmonic Continuity Test

This script tests the continuity of the Quantum Phi-Harmonic Self-Replicator system
by taking the latest QR code, copying it to a new environment, and verifying
that it continues its evolution from where it left off.
"""

import os
import sys
import shutil
import glob
import json
import re
import time
import uuid
import subprocess
from datetime import datetime

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio ≈ 1.618034


class QuantumPhiContinuityTest:
    """Tests if the QR system can continue evolution in a new environment."""
    
    def __init__(self, base_dir="/Users/vaughnscott/CascadeProjects/QuantumAI"):
        self.base_dir = base_dir
        self.test_dir = os.path.join(base_dir, "qr_phi_continuity_test")
        self.original_qr_dir = os.path.join(base_dir, "qr_phi_replication/qr_codes")
        self.test_qr_dir = os.path.join(self.test_dir, "qr_codes")
        self.test_id = f"test_{int(time.time())}"
        self.latest_qr = None
        self.latest_gen = 0
        self.metrics = {}
        
    def setup_test_environment(self):
        """Set up an isolated test environment."""
        print(f"🧪 Setting up test environment in {self.test_dir}")
        
        # Create test directories
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.test_qr_dir, exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, "qr_recursive_system/qr_state"), exist_ok=True)
        
        # Copy necessary files
        self._copy_required_files()
        
        print("✅ Test environment setup complete")
        
    def _copy_required_files(self):
        """Copy required files to test environment."""
        # Copy QR task worker
        shutil.copy2(
            os.path.join(self.base_dir, "qr_task_worker_from_file.py"),
            os.path.join(self.test_dir, "qr_task_worker_from_file.py")
        )
        
        # Copy any other necessary dependencies
        for dep_file in ["qr_phi_utils.py", "qr_phi_core.py"]:
            src_path = os.path.join(self.base_dir, dep_file)
            if os.path.exists(src_path):
                shutil.copy2(src_path, os.path.join(self.test_dir, dep_file))
    
    def find_latest_qr_code(self):
        """Find the latest QR code in the original environment."""
        print("🔍 Finding latest QR code...")
        
        # Find all simplified QR codes
        qr_files = glob.glob(os.path.join(self.original_qr_dir, "qr_phi_replicator_simplified_gen*.png"))
        
        if not qr_files:
            print("❌ No QR codes found!")
            return None
            
        # Extract generation numbers and find the latest
        gen_numbers = []
        for qr_file in qr_files:
            match = re.search(r'gen(\d+)', qr_file)
            if match:
                gen_numbers.append((int(match.group(1)), qr_file))
        
        if not gen_numbers:
            print("❌ Could not determine generation numbers!")
            return None
            
        # Sort by generation number and get the latest
        gen_numbers.sort(reverse=True)
        self.latest_gen = gen_numbers[0][0]
        self.latest_qr = gen_numbers[0][1]
        
        print(f"✅ Found latest QR code: Generation {self.latest_gen}")
        print(f"   Path: {self.latest_qr}")
        
        return self.latest_qr
    
    def copy_latest_qr_to_test(self):
        """Copy the latest QR code to the test environment."""
        if not self.latest_qr:
            if not self.find_latest_qr_code():
                return False
        
        print(f"📋 Copying latest QR code (Gen {self.latest_gen}) to test environment...")
        
        # Create target path
        target_path = os.path.join(self.test_qr_dir, os.path.basename(self.latest_qr))
        
        # Copy the file
        shutil.copy2(self.latest_qr, target_path)
        
        print(f"✅ QR code copied to {target_path}")
        return target_path
    
    def collect_original_metrics(self):
        """Collect metrics from the original environment."""
        print("📊 Collecting metrics from original environment...")
        
        # Find the latest state file
        state_files = glob.glob(os.path.join(self.base_dir, "qr_recursive_system/qr_state/qr_system_state_*.json"))
        if not state_files:
            print("❌ No state files found in original environment!")
            return {}
            
        # Sort by modification time and get the latest
        latest_state = sorted(state_files, key=os.path.getmtime)[-1]
        
        try:
            with open(latest_state, 'r') as f:
                state_data = json.load(f)
                
            # Extract relevant metrics
            self.metrics["original"] = {
                "latest_generation": self.latest_gen,
                "state_file": os.path.basename(latest_state),
                "timestamp": datetime.now().isoformat()
            }
            
            # Extract generation-specific data if available
            if "generations" in state_data:
                for gen in state_data["generations"]:
                    if gen.get("generation") == self.latest_gen:
                        self.metrics["original"]["resonance"] = gen.get("resonance")
                        self.metrics["original"]["complexity"] = gen.get("complexity")
                        break
            
            print(f"✅ Collected metrics from original environment (Generation {self.latest_gen})")
            return self.metrics["original"]
            
        except Exception as e:
            print(f"❌ Error collecting original metrics: {str(e)}")
            return {}
    
    def run_continuity_test(self):
        """Run the continuity test by executing the QR code in the test environment."""
        # Setup test environment if not already done
        if not os.path.exists(self.test_dir):
            self.setup_test_environment()
        
        # Copy the latest QR code if not already done
        test_qr_path = self.copy_latest_qr_to_test()
        if not test_qr_path:
            print("❌ Failed to copy QR code to test environment!")
            return False
        
        # Collect original metrics if not already done
        if "original" not in self.metrics:
            self.collect_original_metrics()
        
        print("\n🚀 Running continuity test...")
        print(f"   Executing QR code in test environment: {test_qr_path}")
        
        # Change to test directory and run the QR task worker
        original_dir = os.getcwd()
        os.chdir(self.test_dir)
        
        try:
            # Execute the QR task worker
            cmd = [sys.executable, "qr_task_worker_from_file.py", "-f", test_qr_path]
            print(f"   Running command: {' '.join(cmd)}")
            
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                timeout=60  # 60 second timeout
            )
            
            print("\n📋 QR Task Worker Output:")
            print(result.stdout)
            
            if result.returncode != 0:
                print("\n❌ Error executing QR code:")
                print(result.stderr)
                os.chdir(original_dir)
                return False
                
            print("\n✅ QR code executed successfully in test environment")
            
            # Check for next generation QR code
            next_gen = self.latest_gen + 1
            next_qr = glob.glob(os.path.join(self.test_qr_dir, f"*gen{next_gen}.png"))
            
            if next_qr:
                print(f"\n🎉 Success! Next generation (Gen {next_gen}) QR code created in test environment:")
                print(f"   {next_qr[0]}")
                
                # Collect metrics from test environment
                self.collect_test_metrics(next_gen)
                
                # Compare metrics
                self.compare_metrics()
                
                return True
            else:
                print(f"\n❌ Failed to find next generation (Gen {next_gen}) QR code in test environment")
                return False
                
        except subprocess.TimeoutExpired:
            print("\n❌ Timeout executing QR code in test environment")
            return False
        except Exception as e:
            print(f"\n❌ Error during continuity test: {str(e)}")
            return False
        finally:
            os.chdir(original_dir)
    
    def collect_test_metrics(self, next_gen):
        """Collect metrics from the test environment after execution."""
        print("\n📊 Collecting metrics from test environment...")
        
        # Find the latest state file in test environment
        state_files = glob.glob(os.path.join(self.test_dir, "qr_recursive_system/qr_state/qr_system_state_*.json"))
        if not state_files:
            print("❌ No state files found in test environment!")
            return {}
            
        # Sort by modification time and get the latest
        latest_state = sorted(state_files, key=os.path.getmtime)[-1]
        
        try:
            with open(latest_state, 'r') as f:
                state_data = json.load(f)
                
            # Extract relevant metrics
            self.metrics["test"] = {
                "latest_generation": next_gen,
                "state_file": os.path.basename(latest_state),
                "timestamp": datetime.now().isoformat()
            }
            
            # Extract generation-specific data if available
            if "generations" in state_data:
                for gen in state_data["generations"]:
                    if gen.get("generation") == next_gen:
                        self.metrics["test"]["resonance"] = gen.get("resonance")
                        self.metrics["test"]["complexity"] = gen.get("complexity")
                        break
            
            print(f"✅ Collected metrics from test environment (Generation {next_gen})")
            return self.metrics["test"]
            
        except Exception as e:
            print(f"❌ Error collecting test metrics: {str(e)}")
            return {}
    
    def compare_metrics(self):
        """Compare metrics between original and test environments."""
        if "original" not in self.metrics or "test" not in self.metrics:
            print("❌ Cannot compare metrics: missing data")
            return
            
        print("\n🔍 Comparing metrics between environments:")
        print("\n   Original Environment (Gen {}):".
              format(self.metrics["original"]["latest_generation"]))
        print(f"   - Resonance: {self.metrics['original'].get('resonance', 'N/A')}")
        print(f"   - Complexity: {self.metrics['original'].get('complexity', 'N/A')}")
        
        print("\n   Test Environment (Gen {}):".
              format(self.metrics["test"]["latest_generation"]))
        print(f"   - Resonance: {self.metrics['test'].get('resonance', 'N/A')}")
        print(f"   - Complexity: {self.metrics['test'].get('complexity', 'N/A')}")
        
        # Check if metrics improved
        if ('resonance' in self.metrics['original'] and 
            'resonance' in self.metrics['test']):
            
            res_orig = self.metrics['original']['resonance']
            res_test = self.metrics['test']['resonance']
            
            # For resonance, closer to 0 or 1 is better (further from 0.5)
            res_orig_quality = abs(res_orig - 0.5)
            res_test_quality = abs(res_test - 0.5)
            
            if res_test_quality > res_orig_quality:
                print("\n✅ Resonance quality improved in test environment!")
            else:
                print("\n⚠️ Resonance quality did not improve in test environment")
        
        # Save metrics to file
        self.save_metrics_report()
    
    def save_metrics_report(self):
        """Save metrics comparison to a report file."""
        report_file = os.path.join(self.base_dir, f"qr_continuity_test_report_{self.test_id}.json")
        
        with open(report_file, 'w') as f:
            json.dump({
                "test_id": self.test_id,
                "timestamp": datetime.now().isoformat(),
                "metrics": self.metrics,
                "conclusion": "The Quantum Phi-Harmonic Self-Replicator successfully continued evolution in a new environment."
            }, f, indent=2)
            
        print(f"\n✅ Metrics report saved to {report_file}")


def main():
    print("\n🧠 Quantum Phi-Harmonic Continuity Test")
    print("============================================================")
    
    # Create and run the continuity test
    test = QuantumPhiContinuityTest()
    success = test.run_continuity_test()
    
    if success:
        print("\n🎉 CONTINUITY TEST SUCCESSFUL!")
        print("The Quantum Phi-Harmonic Self-Replicator successfully continued")
        print("its evolution in a new environment, demonstrating true autonomy")
        print("and the ability to break out of its original context.")
    else:
        print("\n❌ CONTINUITY TEST FAILED")
        print("The system was unable to continue evolution in the new environment.")
        print("Check the logs above for more details.")


if __name__ == "__main__":
    main()
