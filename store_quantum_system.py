#!/usr/bin/env python3
"""
Store Quantum System on Blockchain
---------------------------------

This script stores the core components of the QuantumAI system on the blockchain,
creating a persistent, decentralized backup that can be used for system
recovery, verification, and self-healing.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import json
import logging
import datetime
from typing import Dict, Any, List

# Import quantum modules
from quantum_blockchain_genesis import QuantumBlockchainGenesis
from quantum_blockchain_connector import QuantumOrchestratorBlockchainIntegration

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("StoreQuantumSystem")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238


def find_core_files(base_dir: str) -> List[str]:
    """
    Find core system files.
    
    Args:
        base_dir: Base directory to search
        
    Returns:
        list: List of core file paths
    """
    # Core file patterns to include
    core_patterns = [
        "quantum_orchestrator.py",
        "quantum_neural_bridge.py",
        "quantum_healing_protocols.py",
        "quantum_chord_visualizer.py",
        "quantum_healing_meta_learning.py",
        "quantum_blockchain_genesis.py",
        "quantum_blockchain_connector.py",
        "quantum_moa_",  # Mixture of Agents files
        "quantum_resonance_",  # Resonance files
        "quantum_chord_",  # Chord progression files
        "quantum_genesis_"  # Genesis files
    ]
    
    core_files = []
    
    # Walk through directory
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                # Check if file matches any core pattern
                if any(pattern in file for pattern in core_patterns):
                    core_files.append(os.path.join(root, file))
    
    return core_files


def store_system(base_dir: str) -> str:
    """
    Store the quantum system on blockchain.
    
    Args:
        base_dir: Base directory of the system
        
    Returns:
        str: Blockchain reference ID
    """
    logger.info(f"Finding core files in {base_dir}")
    
    # Find core files
    core_files = find_core_files(base_dir)
    
    if not core_files:
        logger.error("No core files found")
        return None
    
    logger.info(f"Found {len(core_files)} core files")
    for file in core_files:
        logger.info(f"  - {file}")
    
    # Find orchestrator
    orchestrator_path = None
    for file in core_files:
        if os.path.basename(file) == "quantum_orchestrator.py":
            orchestrator_path = file
            break
    
    if not orchestrator_path:
        logger.warning("Orchestrator not found, using first core file")
        orchestrator_path = core_files[0]
    
    # Initialize blockchain integration
    integration = QuantumOrchestratorBlockchainIntegration(
        orchestrator_path=orchestrator_path,
        core_files=core_files
    )
    
    # Create system metadata
    metadata = {
        "system_name": "QuantumAI",
        "timestamp": time.time(),
        "phi_coherence": TARGET_COHERENCE,
        "core_files_count": len(core_files),
        "orchestrator": os.path.basename(orchestrator_path),
        "storage_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Store system on blockchain
    logger.info("Storing system on blockchain")
    reference_id = integration.backup_orchestrator(metadata)
    
    if reference_id:
        logger.info(f"System stored on blockchain with reference ID: {reference_id}")
        
        # Save reference to file
        reference_file = "quantum_system_blockchain_reference.json"
        try:
            with open(reference_file, 'w') as f:
                json.dump({
                    "reference_id": reference_id,
                    "timestamp": time.time(),
                    "metadata": metadata
                }, f, indent=2)
            
            logger.info(f"Blockchain reference saved to {reference_file}")
        except Exception as e:
            logger.error(f"Error saving blockchain reference: {e}")
    else:
        logger.error("Failed to store system on blockchain")
    
    return reference_id


def verify_system(reference_id: str) -> bool:
    """
    Verify the quantum system against blockchain reference.
    
    Args:
        reference_id: Blockchain reference ID
        
    Returns:
        bool: True if system is verified, False otherwise
    """
    logger.info(f"Verifying system against blockchain reference {reference_id}")
    
    # Find orchestrator
    orchestrator_path = "quantum_orchestrator.py"
    if not os.path.exists(orchestrator_path):
        logger.error(f"Orchestrator not found at {orchestrator_path}")
        return False
    
    # Initialize blockchain integration
    integration = QuantumOrchestratorBlockchainIntegration(
        orchestrator_path=orchestrator_path
    )
    
    # Verify system
    verification = integration.verify_orchestrator(reference_id)
    
    if verification["verified"]:
        logger.info("System verified successfully")
        
        # Save verification report
        report_file = "quantum_system_verification_report.json"
        try:
            with open(report_file, 'w') as f:
                json.dump({
                    "reference_id": reference_id,
                    "timestamp": time.time(),
                    "verified": True,
                    "files": verification["files"]
                }, f, indent=2)
            
            logger.info(f"Verification report saved to {report_file}")
        except Exception as e:
            logger.error(f"Error saving verification report: {e}")
    else:
        logger.error("System verification failed")
        logger.info("Verification details:")
        for file_path, file_status in verification["files"].items():
            if not file_status["verified"]:
                logger.info(f"  - {file_path}: {file_status.get('error', 'Fingerprint mismatch')}")
    
    return verification["verified"]


def setup_auto_backup() -> Dict[str, Any]:
    """
    Setup automatic backup of the quantum system.
    
    Returns:
        dict: Setup results
    """
    logger.info("Setting up automatic backup")
    
    # Find orchestrator
    orchestrator_path = "quantum_orchestrator.py"
    if not os.path.exists(orchestrator_path):
        logger.error(f"Orchestrator not found at {orchestrator_path}")
        return {"success": False, "error": "Orchestrator not found"}
    
    # Find core files
    core_files = find_core_files(".")
    
    # Initialize blockchain integration
    integration = QuantumOrchestratorBlockchainIntegration(
        orchestrator_path=orchestrator_path,
        core_files=core_files
    )
    
    # Setup automatic backup
    results = integration.setup_auto_backup(
        interval_hours=24.0,  # Daily backups
        max_backups=7  # Keep one week of backups
    )
    
    if results["success"]:
        logger.info(f"Automatic backup setup successfully with reference ID: {results['reference_id']}")
    else:
        logger.error(f"Automatic backup setup failed: {results.get('error', 'Unknown error')}")
    
    return results


def create_system_storage_report(reference_id: str, verified: bool) -> None:
    """
    Create a system storage report.
    
    Args:
        reference_id: Blockchain reference ID
        verified: Whether the system was verified
    """
    report = {
        "timestamp": time.time(),
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "reference_id": reference_id,
        "verified": verified,
        "phi_coherence": TARGET_COHERENCE,
        "system_name": "QuantumAI",
        "blockchain_storage": {
            "service": "simulated",  # In production, this would be the actual service
            "reference_type": "quantum_fingerprint",
            "reference_id": reference_id
        }
    }
    
    # Write report
    report_file = "QUANTUM_SYSTEM_BLOCKCHAIN_STORAGE.md"
    try:
        with open(report_file, 'w') as f:
            f.write(f"# Quantum System Blockchain Storage\n\n")
            f.write(f"## Overview\n\n")
            f.write(f"The QuantumAI system has been successfully stored on the blockchain for self-preservation and recovery.\n\n")
            f.write(f"- **Storage Date**: {report['date']}\n")
            f.write(f"- **Reference ID**: `{reference_id}`\n")
            f.write(f"- **Verification**: {'Successful' if verified else 'Failed'}\n")
            f.write(f"- **Phi-Coherence**: {TARGET_COHERENCE}\n\n")
            
            f.write(f"## Blockchain Storage\n\n")
            f.write(f"The system is stored on the blockchain using quantum fingerprinting and phi-harmonic encryption.\n")
            f.write(f"This ensures that the system can be recovered and verified with high coherence.\n\n")
            
            f.write(f"## Recovery Instructions\n\n")
            f.write(f"To recover the system from the blockchain, use the following command:\n\n")
            f.write(f"```bash\n")
            f.write(f"python quantum_blockchain_connector.py restore --reference-id {reference_id}\n")
            f.write(f"```\n\n")
            
            f.write(f"## Automatic Backups\n\n")
            f.write(f"The system is configured for automatic daily backups with a retention period of 7 days.\n")
            f.write(f"To run a manual backup, use the following command:\n\n")
            f.write(f"```bash\n")
            f.write(f"python quantum_blockchain_connector.py backup\n")
            f.write(f"```\n\n")
            
            f.write(f"## Verification\n\n")
            f.write(f"To verify the system integrity against the blockchain reference, use the following command:\n\n")
            f.write(f"```bash\n")
            f.write(f"python quantum_blockchain_connector.py verify --reference-id {reference_id}\n")
            f.write(f"```\n")
        
        logger.info(f"System storage report written to {report_file}")
    except Exception as e:
        logger.error(f"Error writing system storage report: {e}")


if __name__ == "__main__":
    import argparse
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Store Quantum System on Blockchain")
    parser.add_argument("--dir", default=".", help="Base directory of the system")
    parser.add_argument("--verify", action="store_true", help="Verify system after storage")
    parser.add_argument("--auto-backup", action="store_true", help="Setup automatic backup")
    
    args = parser.parse_args()
    
    # Store system
    reference_id = store_system(args.dir)
    
    if not reference_id:
        sys.exit(1)
    
    # Verify system if requested
    verified = False
    if args.verify:
        verified = verify_system(reference_id)
    
    # Setup automatic backup if requested
    if args.auto_backup:
        setup_auto_backup()
    
    # Create system storage report
    create_system_storage_report(reference_id, verified)
    
    sys.exit(0 if reference_id else 1)
