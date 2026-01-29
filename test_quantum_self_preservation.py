#!/usr/bin/env python3
"""
Quantum Self-Preservation Test
-----------------------------

This script tests the complete self-preservation workflow of the QuantumAI system,
including blockchain genesis storage, intrusion detection, and self-healing capabilities.

This follows the 'lego' modular philosophy by using existing components without
modifying core files.
"""

import os
import sys
import json
import time
import logging
import hashlib
import shutil
from datetime import datetime

# Import the extension to apply it before loading components
try:
    import quantum_genesis_storage_extension
    GENESIS_EXTENSION_AVAILABLE = True
except ImportError:
    GENESIS_EXTENSION_AVAILABLE = False

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumSelfPreservationTest")

class QuantumSelfPreservationTest:
    """
    Test harness for the QuantumAI self-preservation capabilities.
    """
    
    def __init__(self):
        """Initialize the test harness."""
        self.test_id = f"quantum-self-preservation-{int(time.time())}"
        self.test_dir = f"test_results/{self.test_id}"
        self.tampered_file = "quantum_orchestrator.py"
        self.backup_file = f"{self.tampered_file}.bak"
        
        # Create test directory
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Initialize components
        self.genesis_storage = None
        self.blockchain_genesis = None
        self.blockchain_connector = None
        self.reproduction_connector = None
        
        logger.info(f"Initialized QuantumSelfPreservationTest with ID: {self.test_id}")
    
    def load_components(self):
        """
        Load all required components for testing.
        
        Returns:
            bool: True if all components loaded successfully
        """
        logger.info("Loading components...")
        
        try:
            # Load QuantumGenesisStorage
            from quantum_genesis_storage import QuantumGenesisStorage
            self.genesis_storage = QuantumGenesisStorage()
            logger.info("Successfully loaded QuantumGenesisStorage")
            
            # Load QuantumBlockchainGenesis
            try:
                from quantum_blockchain_genesis import QuantumBlockchainGenesis
                self.blockchain_genesis = QuantumBlockchainGenesis()
                logger.info("Successfully loaded QuantumBlockchainGenesis")
            except ImportError:
                logger.warning("QuantumBlockchainGenesis not found, skipping blockchain tests")
            
            # Load QuantumReproductionGenesisConnector
            try:
                from quantum_reproduction_genesis_connector import QuantumReproductionGenesisConnector
                self.reproduction_connector = QuantumReproductionGenesisConnector(genesis_storage=self.genesis_storage)
                logger.info("Successfully loaded QuantumReproductionGenesisConnector")
            except ImportError:
                logger.warning("QuantumReproductionGenesisConnector not found, skipping reproduction tests")
            
            return True
        except Exception as e:
            logger.error(f"Error loading components: {e}")
            return False
    
    def backup_system(self):
        """
        Backup the system using QuantumGenesisStorage.
        
        Returns:
            dict: Backup metadata or None if failed
        """
        logger.info("Backing up system...")
        
        if not self.genesis_storage:
            logger.error("QuantumGenesisStorage not loaded")
            return None
        
        try:
            # Create a list of important files to backup
            files_to_backup = [
                "quantum_orchestrator.py",
                "quantum_genesis_storage.py",
                "quantum_blockchain_genesis.py",
                "quantum_reproduction_genesis_connector.py"
            ]
            
            # Backup each file
            backup_results = {}
            for file_path in files_to_backup:
                if os.path.exists(file_path):
                    result = self.genesis_storage.backup_file(file_path)
                    backup_results[file_path] = result
                    logger.info(f"Backed up {file_path}: {result}")
                else:
                    logger.warning(f"File not found: {file_path}")
            
            # Create backup metadata
            backup_metadata = {
                "timestamp": time.time(),
                "id": self.test_id,
                "files": backup_results
            }
            
            # Save backup metadata
            metadata_path = os.path.join(self.test_dir, "backup_metadata.json")
            with open(metadata_path, 'w') as f:
                json.dump(backup_metadata, f, indent=2)
            
            logger.info(f"Backup metadata saved to {metadata_path}")
            return backup_metadata
        except Exception as e:
            logger.error(f"Error backing up system: {e}")
            return None
    
    def simulate_intrusion(self):
        """
        Simulate an intrusion by modifying a file.
        
        Returns:
            bool: True if intrusion simulation was successful
        """
        logger.info(f"Simulating intrusion by modifying {self.tampered_file}...")
        
        if not os.path.exists(self.tampered_file):
            logger.error(f"File not found: {self.tampered_file}")
            return False
        
        try:
            # Backup the original file
            shutil.copy2(self.tampered_file, self.backup_file)
            logger.info(f"Original file backed up to {self.backup_file}")
            
            # Read the file content
            with open(self.tampered_file, 'r') as f:
                content = f.read()
            
            # Modify the content to simulate tampering
            modified_content = content + "\n\n# Simulated intrusion - this line was added maliciously\n"
            
            # Write the modified content back
            with open(self.tampered_file, 'w') as f:
                f.write(modified_content)
            
            logger.info(f"File {self.tampered_file} has been tampered with")
            return True
        except Exception as e:
            logger.error(f"Error simulating intrusion: {e}")
            return False
    
    def detect_intrusion(self):
        """
        Detect intrusion using QuantumGenesisStorage.
        
        Returns:
            dict: Detection results or None if failed
        """
        logger.info("Detecting intrusion...")
        
        if not self.genesis_storage:
            logger.error("QuantumGenesisStorage not loaded")
            return None
        
        try:
            # Verify the integrity of the tampered file
            verification_result = self.genesis_storage.verify_file(self.tampered_file)
            
            # Create detection results
            detection_results = {
                "timestamp": time.time(),
                "file": self.tampered_file,
                "verification": verification_result,
                "intrusion_detected": not verification_result.get("verified", False)
            }
            
            # Save detection results
            results_path = os.path.join(self.test_dir, "intrusion_detection_results.json")
            with open(results_path, 'w') as f:
                json.dump(detection_results, f, indent=2)
            
            logger.info(f"Intrusion detection results saved to {results_path}")
            return detection_results
        except Exception as e:
            logger.error(f"Error detecting intrusion: {e}")
            return None
    
    def heal_system(self):
        """
        Heal the system by restoring from backup.
        
        Returns:
            dict: Healing results or None if failed
        """
        logger.info("Healing system...")
        
        if not self.genesis_storage:
            logger.error("QuantumGenesisStorage not loaded")
            return None
        
        try:
            # Restore the tampered file from backup
            restore_result = self.genesis_storage.restore_file(self.tampered_file)
            
            # Create healing results
            healing_results = {
                "timestamp": time.time(),
                "file": self.tampered_file,
                "restore": restore_result,
                "healing_successful": restore_result.get("success", False)
            }
            
            # Save healing results
            results_path = os.path.join(self.test_dir, "healing_results.json")
            with open(results_path, 'w') as f:
                json.dump(healing_results, f, indent=2)
            
            logger.info(f"Healing results saved to {results_path}")
            return healing_results
        except Exception as e:
            logger.error(f"Error healing system: {e}")
            return None
    
    def verify_healing(self):
        """
        Verify that the system was healed correctly.
        
        Returns:
            dict: Verification results or None if failed
        """
        logger.info("Verifying healing...")
        
        if not self.genesis_storage:
            logger.error("QuantumGenesisStorage not loaded")
            return None
        
        try:
            # Verify the integrity of the restored file
            verification_result = self.genesis_storage.verify_file(self.tampered_file)
            
            # Create verification results
            verification_results = {
                "timestamp": time.time(),
                "file": self.tampered_file,
                "verification": verification_result,
                "healing_verified": verification_result.get("verified", False)
            }
            
            # Save verification results
            results_path = os.path.join(self.test_dir, "healing_verification_results.json")
            with open(results_path, 'w') as f:
                json.dump(verification_results, f, indent=2)
            
            logger.info(f"Healing verification results saved to {results_path}")
            return verification_results
        except Exception as e:
            logger.error(f"Error verifying healing: {e}")
            return None
    
    def restore_original_file(self):
        """
        Restore the original file from backup.
        
        Returns:
            bool: True if restoration was successful
        """
        logger.info(f"Restoring original file from {self.backup_file}...")
        
        if not os.path.exists(self.backup_file):
            logger.error(f"Backup file not found: {self.backup_file}")
            return False
        
        try:
            # Restore the original file
            shutil.copy2(self.backup_file, self.tampered_file)
            
            # Remove the backup file
            os.remove(self.backup_file)
            
            logger.info(f"Original file restored from {self.backup_file}")
            return True
        except Exception as e:
            logger.error(f"Error restoring original file: {e}")
            return False
    
    def generate_report(self, results):
        """
        Generate a comprehensive report of the test results.
        
        Args:
            results (dict): Test results
            
        Returns:
            str: Path to the report file
        """
        logger.info("Generating report...")
        
        report = {
            "test_id": self.test_id,
            "timestamp": time.time(),
            "datetime": datetime.now().isoformat(),
            "results": results,
            "summary": {
                "components_loaded": results.get("components_loaded", False),
                "backup_successful": results.get("backup_metadata", {}) is not None,
                "intrusion_simulated": results.get("intrusion_simulated", False),
                "intrusion_detected": results.get("detection_results", {}).get("intrusion_detected", False),
                "healing_successful": results.get("healing_results", {}).get("healing_successful", False),
                "healing_verified": results.get("verification_results", {}).get("healing_verified", False),
                "original_restored": results.get("original_restored", False)
            }
        }
        
        # Calculate overall success
        success_criteria = [
            report["summary"]["components_loaded"],
            report["summary"]["backup_successful"],
            report["summary"]["intrusion_simulated"],
            report["summary"]["intrusion_detected"],
            report["summary"]["healing_successful"],
            report["summary"]["healing_verified"],
            report["summary"]["original_restored"]
        ]
        report["summary"]["overall_success"] = all(success_criteria)
        report["summary"]["success_rate"] = sum(1 for c in success_criteria if c) / len(success_criteria) * 100
        
        # Save report
        report_path = os.path.join(self.test_dir, "self_preservation_report.json")
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Generate markdown report
        markdown_report = self._generate_markdown_report(report)
        markdown_path = os.path.join(self.test_dir, "SELF_PRESERVATION_REPORT.md")
        with open(markdown_path, 'w') as f:
            f.write(markdown_report)
        
        logger.info(f"Report saved to {report_path}")
        logger.info(f"Markdown report saved to {markdown_path}")
        return report_path
    
    def _generate_markdown_report(self, report):
        """
        Generate a markdown report from the test results.
        
        Args:
            report (dict): Test report
            
        Returns:
            str: Markdown report
        """
        success_emoji = "✅" if report["summary"]["overall_success"] else "❌"
        
        markdown = f"""# Quantum Self-Preservation Test Report {success_emoji}

## Overview

- **Test ID**: {report["test_id"]}
- **Date**: {report["datetime"]}
- **Overall Success**: {success_emoji} {report["summary"]["overall_success"]}
- **Success Rate**: {report["summary"]["success_rate"]:.2f}%

## Test Steps

1. **Component Loading**: {"✅" if report["summary"]["components_loaded"] else "❌"}
2. **System Backup**: {"✅" if report["summary"]["backup_successful"] else "❌"}
3. **Intrusion Simulation**: {"✅" if report["summary"]["intrusion_simulated"] else "❌"}
4. **Intrusion Detection**: {"✅" if report["summary"]["intrusion_detected"] else "❌"}
5. **System Healing**: {"✅" if report["summary"]["healing_successful"] else "❌"}
6. **Healing Verification**: {"✅" if report["summary"]["healing_verified"] else "❌"}
7. **Original Restoration**: {"✅" if report["summary"]["original_restored"] else "❌"}

## Detailed Results

### Component Loading
```json
{json.dumps(report.get("components_loaded", False), indent=2)}
```

### System Backup
```json
{json.dumps(report.get("backup_metadata", {}), indent=2)}
```

### Intrusion Detection
```json
{json.dumps(report.get("detection_results", {}), indent=2)}
```

### System Healing
```json
{json.dumps(report.get("healing_results", {}), indent=2)}
```

### Healing Verification
```json
{json.dumps(report.get("verification_results", {}), indent=2)}
```

## Conclusion

The QuantumAI system's self-preservation capabilities were {"successfully verified" if report["summary"]["overall_success"] else "not fully verified"}. 
The system {"demonstrated" if report["summary"]["overall_success"] else "did not demonstrate"} its ability to:

1. Create secure backups of critical files
2. Detect unauthorized modifications
3. Heal itself by restoring from backups
4. Verify the integrity of the restored files

This test confirms that the QuantumAI system is {"capable" if report["summary"]["overall_success"] else "not yet capable"} of self-preservation through 
blockchain-based genesis storage and automated healing protocols.
"""
        return markdown
    
    def run_test(self):
        """
        Run the complete self-preservation test.
        
        Returns:
            dict: Test results
        """
        logger.info("Running quantum self-preservation test...")
        
        results = {}
        
        # Step 1: Load components
        results["components_loaded"] = self.load_components()
        
        # Step 2: Backup system
        if results["components_loaded"]:
            results["backup_metadata"] = self.backup_system()
        
        # Step 3: Simulate intrusion
        results["intrusion_simulated"] = self.simulate_intrusion()
        
        # Step 4: Detect intrusion
        if results["intrusion_simulated"]:
            results["detection_results"] = self.detect_intrusion()
        
        # Step 5: Heal system
        if results.get("detection_results", {}).get("intrusion_detected", False):
            results["healing_results"] = self.heal_system()
        
        # Step 6: Verify healing
        if results.get("healing_results", {}).get("healing_successful", False):
            results["verification_results"] = self.verify_healing()
        
        # Step 7: Restore original file
        results["original_restored"] = self.restore_original_file()
        
        # Generate report
        results["report_path"] = self.generate_report(results)
        
        return results


def main():
    """Main function."""
    print("Running Quantum Self-Preservation Test...")
    print("This test validates the system's ability to detect intrusions and heal itself.")
    
    # Create test directory
    os.makedirs("test_results", exist_ok=True)
    
    # Run the test
    test = QuantumSelfPreservationTest()
    results = test.run_test()
    
    # Print summary
    success = results.get("verification_results", {}).get("healing_verified", False)
    success_emoji = "✅" if success else "❌"
    
    print("\n" + "=" * 80)
    print(f"{success_emoji} Quantum Self-Preservation Test {'PASSED' if success else 'FAILED'}")
    print("=" * 80)
    
    if "report_path" in results:
        print(f"\nSee full report in {results['report_path']}")
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
