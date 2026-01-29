#!/usr/bin/env python3
"""
Test Autonomous Corruption Detection and Self-Healing
---------------------------------------------------

This script tests the autonomous corruption detection and self-healing capabilities
of the QuantumAI system using blockchain genesis storage. It:

1. Corrupts a core system file
2. Triggers autonomous integrity verification
3. Demonstrates self-healing from blockchain reference
4. Verifies successful restoration

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import json
import random
import logging
import datetime
import shutil
from typing import Dict, Any, List, Tuple

# Import quantum modules
from quantum_blockchain_genesis import QuantumBlockchainGenesis
from quantum_blockchain_connector import QuantumOrchestratorBlockchainIntegration

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AutonomousHealing")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238


class AutonomousHealingSystem:
    """System for testing autonomous corruption detection and self-healing."""
    
    def __init__(self, reference_id: str = None):
        """
        Initialize the autonomous healing system.
        
        Args:
            reference_id: Blockchain reference ID
        """
        self.reference_id = reference_id
        
        # Load reference ID from file if not provided
        if not self.reference_id:
            reference_file = "quantum_system_blockchain_reference.json"
            if os.path.exists(reference_file):
                try:
                    with open(reference_file, 'r') as f:
                        data = json.load(f)
                        self.reference_id = data.get("reference_id")
                except Exception as e:
                    logger.error(f"Error loading reference ID: {e}")
            
            if not self.reference_id:
                logger.error("No reference ID provided or found")
                raise ValueError("No reference ID provided or found")
        
        # Initialize blockchain integration
        self.orchestrator_path = "quantum_orchestrator.py"
        self.integration = QuantumOrchestratorBlockchainIntegration(
            orchestrator_path=self.orchestrator_path
        )
        
        logger.info(f"Autonomous healing system initialized with reference ID: {self.reference_id}")
    
    def find_core_files(self) -> List[str]:
        """
        Find core system files.
        
        Returns:
            list: List of core file paths
        """
        # Core file patterns to include
        core_patterns = [
            "quantum_orchestrator.py",
            "quantum_neural_bridge.py",
            "quantum_blockchain_genesis.py",
            "quantum_blockchain_connector.py"
        ]
        
        core_files = []
        
        # Check for files in current directory
        for pattern in core_patterns:
            if os.path.exists(pattern):
                core_files.append(pattern)
        
        return core_files
    
    def corrupt_file(self, file_path: str = None) -> Tuple[str, str]:
        """
        Corrupt a system file.
        
        Args:
            file_path: Path to file to corrupt (if None, a random core file is selected)
            
        Returns:
            tuple: (corrupted file path, backup file path)
        """
        # Find file to corrupt if not provided
        if not file_path:
            core_files = self.find_core_files()
            if not core_files:
                logger.error("No core files found to corrupt")
                return None, None
            
            file_path = random.choice(core_files)
        
        logger.info(f"Corrupting file: {file_path}")
        
        # Create backup
        backup_path = f"{file_path}.bak.{int(time.time())}"
        try:
            shutil.copy2(file_path, backup_path)
            logger.info(f"Created backup at {backup_path}")
        except Exception as e:
            logger.error(f"Error creating backup: {e}")
            return None, None
        
        # Read file
        try:
            with open(file_path, 'r') as f:
                content = f.read()
        except Exception as e:
            logger.error(f"Error reading file: {e}")
            return None, backup_path
        
        # Corrupt file
        try:
            # Corruption strategy: Replace phi-harmonic constants
            corrupted_content = content.replace("PHI = 1.618034", "PHI = 1.5")
            corrupted_content = corrupted_content.replace("φ⁷·⁵/10", "φ⁷/10")
            corrupted_content = corrupted_content.replace("3.693238", "3.5")
            
            # Add corruption marker
            corrupted_content += "\n\n# CORRUPTION MARKER: This file has been tampered with\n"
            
            # Write corrupted content
            with open(file_path, 'w') as f:
                f.write(corrupted_content)
            
            logger.info(f"File corrupted: {file_path}")
            return file_path, backup_path
        except Exception as e:
            logger.error(f"Error corrupting file: {e}")
            return None, backup_path
    
    def verify_integrity(self) -> Dict[str, Any]:
        """
        Verify system integrity against blockchain reference.
        
        Returns:
            dict: Verification results
        """
        logger.info("Verifying system integrity")
        
        # Verify system
        verification = self.integration.verify_orchestrator(self.reference_id)
        
        if verification["verified"]:
            logger.info("System integrity verified")
        else:
            logger.warning("System integrity verification failed")
            logger.info("Verification details:")
            for file_path, file_status in verification["files"].items():
                if not file_status["verified"]:
                    logger.info(f"  - {file_path}: {file_status.get('error', 'Fingerprint mismatch')}")
        
        return verification
    
    def heal_system(self) -> Dict[str, Any]:
        """
        Heal system from blockchain reference.
        
        Returns:
            dict: Healing results
        """
        logger.info("Healing system from blockchain reference")
        
        # Heal system
        healing = self.integration.heal_orchestrator(self.reference_id)
        
        if healing["healed"]:
            logger.info("System healed successfully")
            logger.info("Healing details:")
            for file_path, file_status in healing["files"].items():
                if file_status.get("healed", False):
                    logger.info(f"  - Healed: {file_path}")
        else:
            logger.error("System healing failed")
            logger.info("Healing details:")
            for file_path, file_status in healing["files"].items():
                if not file_status.get("healed", True):
                    logger.info(f"  - Failed: {file_path}: {file_status.get('error', 'Unknown error')}")
        
        return healing
    
    def run_autonomous_cycle(self, file_to_corrupt: str = None) -> Dict[str, Any]:
        """
        Run autonomous corruption detection and self-healing cycle.
        
        Args:
            file_to_corrupt: Path to file to corrupt (if None, a random core file is selected)
            
        Returns:
            dict: Cycle results
        """
        results = {
            "timestamp": time.time(),
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "reference_id": self.reference_id,
            "steps": {}
        }
        
        # Step 1: Corrupt file
        logger.info("Step 1: Corrupting system file")
        corrupted_file, backup_file = self.corrupt_file(file_to_corrupt)
        
        if not corrupted_file:
            logger.error("Failed to corrupt file")
            results["steps"]["corrupt_file"] = {
                "success": False,
                "error": "Failed to corrupt file"
            }
            return results
        
        results["steps"]["corrupt_file"] = {
            "success": True,
            "corrupted_file": corrupted_file,
            "backup_file": backup_file
        }
        
        # Step 2: Verify integrity
        logger.info("Step 2: Verifying system integrity")
        verification = self.verify_integrity()
        
        results["steps"]["verify_integrity"] = {
            "success": not verification["verified"],  # Success means corruption was detected
            "verified": verification["verified"],
            "files": verification["files"]
        }
        
        if verification["verified"]:
            logger.warning("Corruption not detected, test failed")
            # Restore from backup
            try:
                shutil.copy2(backup_file, corrupted_file)
                logger.info(f"Restored {corrupted_file} from backup {backup_file}")
            except Exception as e:
                logger.error(f"Error restoring from backup: {e}")
            
            return results
        
        # Step 3: Heal system
        logger.info("Step 3: Healing system")
        healing = self.heal_system()
        
        results["steps"]["heal_system"] = {
            "success": healing["healed"],
            "healed": healing["healed"],
            "files": healing["files"]
        }
        
        # Step 4: Verify integrity after healing
        logger.info("Step 4: Verifying system integrity after healing")
        verification_after = self.verify_integrity()
        
        results["steps"]["verify_after_healing"] = {
            "success": verification_after["verified"],
            "verified": verification_after["verified"],
            "files": verification_after["files"]
        }
        
        # Overall success
        results["success"] = (
            results["steps"]["corrupt_file"]["success"] and
            results["steps"]["verify_integrity"]["success"] and
            results["steps"]["heal_system"]["success"] and
            results["steps"]["verify_after_healing"]["success"]
        )
        
        if results["success"]:
            logger.info("Autonomous healing cycle completed successfully")
        else:
            logger.error("Autonomous healing cycle failed")
        
        return results


def create_report(results: Dict[str, Any]) -> None:
    """
    Create a report of the autonomous healing test.
    
    Args:
        results: Test results
    """
    # Write JSON report
    report_file = "autonomous_healing_results.json"
    try:
        with open(report_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"Results saved to {report_file}")
    except Exception as e:
        logger.error(f"Error saving results: {e}")
    
    # Write markdown report
    md_file = "AUTONOMOUS_HEALING_REPORT.md"
    try:
        with open(md_file, 'w') as f:
            f.write(f"# Quantum System Autonomous Healing Report\n\n")
            f.write(f"## Overview\n\n")
            f.write(f"This report documents the autonomous corruption detection and self-healing capabilities of the QuantumAI system.\n\n")
            f.write(f"- **Test Date**: {results['date']}\n")
            f.write(f"- **Blockchain Reference**: `{results['reference_id']}`\n")
            f.write(f"- **Overall Success**: {'Yes' if results['success'] else 'No'}\n\n")
            
            f.write(f"## Test Steps\n\n")
            
            # Step 1: Corrupt file
            step1 = results["steps"]["corrupt_file"]
            f.write(f"### Step 1: Corrupt System File\n\n")
            f.write(f"- **Success**: {'Yes' if step1['success'] else 'No'}\n")
            if step1["success"]:
                f.write(f"- **Corrupted File**: `{step1['corrupted_file']}`\n")
                f.write(f"- **Backup File**: `{step1['backup_file']}`\n")
            f.write(f"\n")
            
            # Step 2: Verify integrity
            step2 = results["steps"]["verify_integrity"]
            f.write(f"### Step 2: Verify System Integrity\n\n")
            f.write(f"- **Success** (corruption detected): {'Yes' if step2['success'] else 'No'}\n")
            f.write(f"- **System Verified**: {'Yes' if step2['verified'] else 'No'}\n")
            if not step2["verified"]:
                f.write(f"- **Corrupted Files Detected**:\n")
                for file_path, file_status in step2["files"].items():
                    if not file_status["verified"]:
                        f.write(f"  - `{file_path}`\n")
            f.write(f"\n")
            
            # Step 3: Heal system
            step3 = results["steps"]["heal_system"]
            f.write(f"### Step 3: Heal System\n\n")
            f.write(f"- **Success**: {'Yes' if step3['success'] else 'No'}\n")
            if step3["success"]:
                f.write(f"- **Healed Files**:\n")
                for file_path, file_status in step3["files"].items():
                    if file_status.get("healed", False):
                        f.write(f"  - `{file_path}`\n")
            f.write(f"\n")
            
            # Step 4: Verify integrity after healing
            step4 = results["steps"]["verify_after_healing"]
            f.write(f"### Step 4: Verify System Integrity After Healing\n\n")
            f.write(f"- **Success**: {'Yes' if step4['success'] else 'No'}\n")
            f.write(f"- **System Verified**: {'Yes' if step4['verified'] else 'No'}\n")
            f.write(f"\n")
            
            f.write(f"## Conclusion\n\n")
            if results["success"]:
                f.write(f"The QuantumAI system successfully demonstrated autonomous corruption detection and self-healing capabilities. ")
                f.write(f"The system detected tampering in core files, automatically healed itself from blockchain reference, ")
                f.write(f"and verified its integrity after healing.\n\n")
            else:
                f.write(f"The autonomous healing test encountered issues. ")
                if not step2["success"]:
                    f.write(f"The system failed to detect corruption. ")
                if not step3["success"]:
                    f.write(f"The system failed to heal itself. ")
                if not step4["success"]:
                    f.write(f"The system failed to verify its integrity after healing. ")
                f.write(f"\n\n")
            
            f.write(f"This test validates the system's self-preservation capabilities through blockchain-based genesis storage and recovery.\n")
        
        logger.info(f"Report saved to {md_file}")
    except Exception as e:
        logger.error(f"Error saving report: {e}")


if __name__ == "__main__":
    import argparse
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Test Autonomous Corruption Detection and Self-Healing")
    parser.add_argument("--reference-id", help="Blockchain reference ID")
    parser.add_argument("--file", help="Specific file to corrupt")
    
    args = parser.parse_args()
    
    try:
        # Initialize autonomous healing system
        system = AutonomousHealingSystem(args.reference_id)
        
        # Run autonomous cycle
        results = system.run_autonomous_cycle(args.file)
        
        # Create report
        create_report(results)
        
        sys.exit(0 if results["success"] else 1)
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)
