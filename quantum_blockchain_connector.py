#!/usr/bin/env python3
"""
Quantum Blockchain Connector
---------------------------

This module connects the quantum orchestrator with blockchain genesis storage,
enabling seamless storage and retrieval of critical system components on the blockchain.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import json
import time
import logging
import hashlib
import datetime
from typing import Dict, Any, Optional, List, Tuple

# Import quantum modules
from quantum_blockchain_genesis import QuantumBlockchainGenesis

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumBlockchainConnector")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

class QuantumBlockchainConnector:
    """Connector between quantum orchestrator and blockchain genesis storage."""
    
    def __init__(self, blockchain_genesis: QuantumBlockchainGenesis = None,
                 orchestrator_path: str = None,
                 core_files: List[str] = None):
        """
        Initialize the blockchain connector.
        
        Args:
            blockchain_genesis: QuantumBlockchainGenesis instance
            orchestrator_path: Path to the quantum orchestrator
            core_files: List of core files to include in genesis blocks
        """
        self.blockchain_genesis = blockchain_genesis or QuantumBlockchainGenesis()
        self.orchestrator_path = orchestrator_path
        self.core_files = core_files or []
        
        # Add orchestrator to core files if provided
        if orchestrator_path and orchestrator_path not in self.core_files:
            self.core_files.append(orchestrator_path)
        
        logger.info("QuantumBlockchainConnector initialized")
    
    def store_system_genesis(self, metadata: Dict[str, Any] = None) -> str:
        """
        Store the current system state as a genesis block on the blockchain.
        
        Args:
            metadata: Additional metadata to include in the genesis block
            
        Returns:
            str: Blockchain reference ID
        """
        # Create genesis data
        genesis_data = {
            "system_version": "1.0",
            "timestamp": time.time(),
            "core_files": {},
            "phi_coherence": TARGET_COHERENCE,
            "metadata": metadata or {}
        }
        
        # Add core files content
        for file_path in self.core_files:
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    
                    # Calculate file coherence
                    coherence = self._calculate_file_coherence(content)
                    
                    # Add to genesis data
                    genesis_data["core_files"][file_path] = {
                        "content": content,
                        "coherence": coherence,
                        "phi_resonance": self._calculate_phi_resonance(coherence),
                        "quantum_fingerprint": self._calculate_quantum_fingerprint(content)
                    }
                    
                    logger.info(f"Added {file_path} to genesis block")
                except Exception as e:
                    logger.error(f"Error adding {file_path} to genesis block: {e}")
        
        # Store genesis block
        reference_id = self.blockchain_genesis.store_genesis_block(genesis_data)
        
        if reference_id:
            logger.info(f"Stored system genesis block with ID {reference_id}")
        else:
            logger.error("Failed to store system genesis block")
        
        return reference_id
    
    def restore_system_from_genesis(self, reference_id: str, 
                                   target_dir: str = None) -> bool:
        """
        Restore the system from a genesis block.
        
        Args:
            reference_id: Blockchain reference ID
            target_dir: Target directory for restored files
            
        Returns:
            bool: True if restoration was successful, False otherwise
        """
        # Retrieve genesis block
        genesis_data = self.blockchain_genesis.retrieve_genesis_block(reference_id)
        
        if not genesis_data:
            logger.error(f"Failed to retrieve genesis block with ID {reference_id}")
            return False
        
        # Create target directory if not exists
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)
        
        # Restore core files
        for file_path, file_data in genesis_data.get("core_files", {}).items():
            # Determine target path
            if target_dir:
                target_path = os.path.join(target_dir, os.path.basename(file_path))
            else:
                target_path = file_path
            
            # Create directory if not exists
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            
            # Write file
            try:
                with open(target_path, 'w') as f:
                    f.write(file_data["content"])
                
                logger.info(f"Restored {file_path} to {target_path}")
            except Exception as e:
                logger.error(f"Error restoring {file_path}: {e}")
                return False
        
        logger.info(f"Successfully restored system from genesis block {reference_id}")
        
        return True
    
    def verify_system_integrity(self, reference_id: str) -> Dict[str, Any]:
        """
        Verify the integrity of the current system against a genesis block.
        
        Args:
            reference_id: Blockchain reference ID
            
        Returns:
            dict: Verification results
        """
        # Retrieve genesis block
        genesis_data = self.blockchain_genesis.retrieve_genesis_block(reference_id)
        
        if not genesis_data:
            logger.error(f"Failed to retrieve genesis block with ID {reference_id}")
            return {"verified": False, "error": "Failed to retrieve genesis block"}
        
        # Verify core files
        results = {
            "verified": True,
            "timestamp": time.time(),
            "genesis_id": reference_id,
            "files": {}
        }
        
        for file_path, file_data in genesis_data.get("core_files", {}).items():
            # Check if file exists
            if not os.path.exists(file_path):
                results["files"][file_path] = {
                    "verified": False,
                    "error": "File not found"
                }
                results["verified"] = False
                continue
            
            # Read file content
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Calculate quantum fingerprint
                current_fingerprint = self._calculate_quantum_fingerprint(content)
                genesis_fingerprint = file_data["quantum_fingerprint"]
                
                # Verify fingerprint
                if current_fingerprint == genesis_fingerprint:
                    results["files"][file_path] = {
                        "verified": True,
                        "fingerprint_match": True
                    }
                else:
                    results["files"][file_path] = {
                        "verified": False,
                        "fingerprint_match": False,
                        "current_fingerprint": current_fingerprint,
                        "genesis_fingerprint": genesis_fingerprint
                    }
                    results["verified"] = False
            except Exception as e:
                results["files"][file_path] = {
                    "verified": False,
                    "error": str(e)
                }
                results["verified"] = False
        
        if results["verified"]:
            logger.info(f"System integrity verified against genesis block {reference_id}")
        else:
            logger.warning(f"System integrity verification failed against genesis block {reference_id}")
        
        return results
    
    def heal_system_from_genesis(self, reference_id: str) -> Dict[str, Any]:
        """
        Heal the system using a genesis block.
        
        Args:
            reference_id: Blockchain reference ID
            
        Returns:
            dict: Healing results
        """
        # Verify system integrity
        verification = self.verify_system_integrity(reference_id)
        
        if verification["verified"]:
            logger.info(f"System integrity verified, no healing needed")
            return {"healed": False, "message": "System integrity verified, no healing needed"}
        
        # Retrieve genesis block
        genesis_data = self.blockchain_genesis.retrieve_genesis_block(reference_id)
        
        if not genesis_data:
            logger.error(f"Failed to retrieve genesis block with ID {reference_id}")
            return {"healed": False, "error": "Failed to retrieve genesis block"}
        
        # Heal files
        results = {
            "healed": True,
            "timestamp": time.time(),
            "genesis_id": reference_id,
            "files": {}
        }
        
        for file_path, file_status in verification["files"].items():
            if file_status["verified"]:
                results["files"][file_path] = {
                    "healed": False,
                    "message": "File integrity verified, no healing needed"
                }
                continue
            
            # Get file data from genesis
            file_data = genesis_data["core_files"].get(file_path)
            if not file_data:
                results["files"][file_path] = {
                    "healed": False,
                    "error": "File not found in genesis block"
                }
                results["healed"] = False
                continue
            
            # Create backup
            backup_path = f"{file_path}.bak.{int(time.time())}"
            try:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as src, open(backup_path, 'w') as dst:
                        dst.write(src.read())
                    logger.info(f"Created backup of {file_path} at {backup_path}")
            except Exception as e:
                logger.error(f"Error creating backup of {file_path}: {e}")
            
            # Restore file
            try:
                # Create directory if not exists
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                # Write file
                with open(file_path, 'w') as f:
                    f.write(file_data["content"])
                
                results["files"][file_path] = {
                    "healed": True,
                    "backup": backup_path
                }
                
                logger.info(f"Healed {file_path} from genesis block")
            except Exception as e:
                results["files"][file_path] = {
                    "healed": False,
                    "error": str(e)
                }
                results["healed"] = False
        
        if results["healed"]:
            logger.info(f"Successfully healed system from genesis block {reference_id}")
        else:
            logger.warning(f"System healing partially failed from genesis block {reference_id}")
        
        return results
    
    def _calculate_file_coherence(self, content: str) -> float:
        """
        Calculate coherence of a file.
        
        Args:
            content: File content
            
        Returns:
            float: Coherence value
        """
        # Simple coherence measure based on file size and phi
        file_size = len(content)
        line_count = content.count('\n') + 1
        char_per_line = file_size / line_count if line_count > 0 else 0
        
        # Apply phi-harmonic transformation
        coherence = (char_per_line * PHI) % TARGET_COHERENCE
        if coherence > TARGET_COHERENCE / 2:
            coherence = TARGET_COHERENCE - coherence
        
        # Normalize to 0-TARGET_COHERENCE range
        coherence = TARGET_COHERENCE - coherence
        
        return coherence
    
    def _calculate_phi_resonance(self, value: float) -> float:
        """
        Calculate phi-resonance of a value.
        
        Args:
            value: Value to calculate phi-resonance for
            
        Returns:
            float: Phi-resonance (0-1)
        """
        if value is None:
            return 0
        
        # Calculate phi-resonance (how close the value is to a power of phi)
        phi_resonance = abs((PHI * value) % 1)
        if phi_resonance > 0.5:
            phi_resonance = 1 - phi_resonance
        
        # Normalize to 0-1 range
        phi_resonance = 1 - (phi_resonance * 2)
        
        return phi_resonance
    
    def _calculate_quantum_fingerprint(self, content: str) -> str:
        """
        Calculate quantum fingerprint of content.
        
        Args:
            content: Content to fingerprint
            
        Returns:
            str: Quantum fingerprint
        """
        # Create SHA-256 hash
        sha256 = hashlib.sha256(content.encode()).hexdigest()
        
        # Apply phi-harmonic transformation
        phi_hash = ""
        for i, c in enumerate(sha256):
            # Apply phi-based transformation
            char_val = int(c, 16)
            phi_val = int((char_val * PHI) % 16)
            phi_hash += format(phi_val, 'x')
        
        return phi_hash


# Integration with quantum orchestrator
class QuantumOrchestratorBlockchainIntegration:
    """Integration of quantum orchestrator with blockchain genesis storage."""
    
    def __init__(self, orchestrator_path: str = "quantum_orchestrator.py",
                 core_files: List[str] = None):
        """
        Initialize the orchestrator blockchain integration.
        
        Args:
            orchestrator_path: Path to the quantum orchestrator
            core_files: List of core files to include in genesis blocks
        """
        self.orchestrator_path = orchestrator_path
        
        # Default core files
        if core_files is None:
            self.core_files = [
                orchestrator_path,
                "quantum_neural_bridge.py",
                "quantum_healing_protocols.py",
                "quantum_chord_visualizer.py",
                "quantum_healing_meta_learning.py",
                "quantum_blockchain_genesis.py"
            ]
        else:
            self.core_files = core_files
        
        # Initialize blockchain connector
        self.blockchain_genesis = QuantumBlockchainGenesis()
        self.connector = QuantumBlockchainConnector(
            blockchain_genesis=self.blockchain_genesis,
            orchestrator_path=orchestrator_path,
            core_files=self.core_files
        )
        
        logger.info("QuantumOrchestratorBlockchainIntegration initialized")
    
    def backup_orchestrator(self, metadata: Dict[str, Any] = None) -> str:
        """
        Backup the quantum orchestrator to blockchain.
        
        Args:
            metadata: Additional metadata to include in the genesis block
            
        Returns:
            str: Blockchain reference ID
        """
        # Add orchestrator metadata
        if metadata is None:
            metadata = {}
        
        metadata["orchestrator_backup"] = {
            "timestamp": time.time(),
            "version": "1.0",
            "backup_type": "orchestrator"
        }
        
        # Store system genesis
        reference_id = self.connector.store_system_genesis(metadata)
        
        return reference_id
    
    def restore_orchestrator(self, reference_id: str, 
                            target_dir: str = None) -> bool:
        """
        Restore the quantum orchestrator from blockchain.
        
        Args:
            reference_id: Blockchain reference ID
            target_dir: Target directory for restored files
            
        Returns:
            bool: True if restoration was successful, False otherwise
        """
        # Restore system from genesis
        success = self.connector.restore_system_from_genesis(reference_id, target_dir)
        
        return success
    
    def verify_orchestrator(self, reference_id: str) -> Dict[str, Any]:
        """
        Verify the integrity of the quantum orchestrator.
        
        Args:
            reference_id: Blockchain reference ID
            
        Returns:
            dict: Verification results
        """
        # Verify system integrity
        results = self.connector.verify_system_integrity(reference_id)
        
        return results
    
    def heal_orchestrator(self, reference_id: str) -> Dict[str, Any]:
        """
        Heal the quantum orchestrator using blockchain.
        
        Args:
            reference_id: Blockchain reference ID
            
        Returns:
            dict: Healing results
        """
        # Heal system from genesis
        results = self.connector.heal_system_from_genesis(reference_id)
        
        return results
    
    def setup_auto_backup(self, interval_hours: float = 24.0,
                         max_backups: int = 5) -> Dict[str, Any]:
        """
        Setup automatic backup of the quantum orchestrator.
        
        Args:
            interval_hours: Backup interval in hours
            max_backups: Maximum number of backups to keep
            
        Returns:
            dict: Setup results
        """
        # Create backup configuration
        config = {
            "enabled": True,
            "interval_hours": interval_hours,
            "max_backups": max_backups,
            "last_backup": None,
            "next_backup": time.time() + (interval_hours * 3600),
            "backups": []
        }
        
        # Save configuration
        config_file = "orchestrator_backup_config.json"
        try:
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            logger.info(f"Setup automatic backup with interval {interval_hours} hours")
        except Exception as e:
            logger.error(f"Error setting up automatic backup: {e}")
            return {"success": False, "error": str(e)}
        
        # Create initial backup
        reference_id = self.backup_orchestrator({
            "auto_backup": True,
            "interval_hours": interval_hours
        })
        
        if reference_id:
            # Update configuration
            config["last_backup"] = time.time()
            config["backups"].append({
                "reference_id": reference_id,
                "timestamp": time.time()
            })
            
            try:
                with open(config_file, 'w') as f:
                    json.dump(config, f, indent=2)
            except Exception as e:
                logger.error(f"Error updating backup configuration: {e}")
        
        return {
            "success": bool(reference_id),
            "reference_id": reference_id,
            "config": config
        }
    
    def run_auto_backup(self) -> Dict[str, Any]:
        """
        Run automatic backup if needed.
        
        Returns:
            dict: Backup results
        """
        # Load configuration
        config_file = "orchestrator_backup_config.json"
        if not os.path.exists(config_file):
            logger.error(f"Backup configuration not found")
            return {"success": False, "error": "Backup configuration not found"}
        
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
        except Exception as e:
            logger.error(f"Error loading backup configuration: {e}")
            return {"success": False, "error": str(e)}
        
        # Check if backup is enabled
        if not config.get("enabled", False):
            logger.info(f"Automatic backup is disabled")
            return {"success": False, "message": "Automatic backup is disabled"}
        
        # Check if backup is needed
        now = time.time()
        next_backup = config.get("next_backup", 0)
        
        if now < next_backup:
            logger.info(f"No backup needed yet, next backup at {datetime.datetime.fromtimestamp(next_backup)}")
            return {"success": False, "message": "No backup needed yet"}
        
        # Create backup
        reference_id = self.backup_orchestrator({
            "auto_backup": True,
            "interval_hours": config.get("interval_hours", 24.0)
        })
        
        if reference_id:
            # Update configuration
            config["last_backup"] = now
            config["next_backup"] = now + (config.get("interval_hours", 24.0) * 3600)
            
            config["backups"].append({
                "reference_id": reference_id,
                "timestamp": now
            })
            
            # Remove old backups if needed
            max_backups = config.get("max_backups", 5)
            if len(config["backups"]) > max_backups:
                config["backups"] = sorted(config["backups"], 
                                          key=lambda x: x.get("timestamp", 0),
                                          reverse=True)[:max_backups]
            
            try:
                with open(config_file, 'w') as f:
                    json.dump(config, f, indent=2)
                
                logger.info(f"Updated backup configuration")
            except Exception as e:
                logger.error(f"Error updating backup configuration: {e}")
        
        return {
            "success": bool(reference_id),
            "reference_id": reference_id,
            "next_backup": config["next_backup"]
        }


# Example usage
if __name__ == "__main__":
    import argparse
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Quantum Blockchain Connector")
    parser.add_argument("command", choices=["backup", "restore", "verify", "heal", "setup-auto", "run-auto"],
                      help="Command to execute")
    parser.add_argument("--reference-id", help="Blockchain reference ID")
    parser.add_argument("--target-dir", help="Target directory for restored files")
    parser.add_argument("--orchestrator", default="quantum_orchestrator.py",
                      help="Path to the quantum orchestrator")
    parser.add_argument("--interval", type=float, default=24.0,
                      help="Backup interval in hours")
    parser.add_argument("--max-backups", type=int, default=5,
                      help="Maximum number of backups to keep")
    
    args = parser.parse_args()
    
    # Create integration
    integration = QuantumOrchestratorBlockchainIntegration(
        orchestrator_path=args.orchestrator
    )
    
    if args.command == "backup":
        # Backup orchestrator
        reference_id = integration.backup_orchestrator()
        
        if reference_id:
            print(f"Backed up orchestrator with reference ID: {reference_id}")
            sys.exit(0)
        else:
            print("Failed to backup orchestrator")
            sys.exit(1)
    
    elif args.command == "restore":
        if not args.reference_id:
            print("Error: --reference-id is required for restore command")
            sys.exit(1)
        
        # Restore orchestrator
        success = integration.restore_orchestrator(args.reference_id, args.target_dir)
        
        if success:
            print(f"Restored orchestrator from reference ID: {args.reference_id}")
            sys.exit(0)
        else:
            print(f"Failed to restore orchestrator from reference ID: {args.reference_id}")
            sys.exit(1)
    
    elif args.command == "verify":
        if not args.reference_id:
            print("Error: --reference-id is required for verify command")
            sys.exit(1)
        
        # Verify orchestrator
        results = integration.verify_orchestrator(args.reference_id)
        
        if results["verified"]:
            print(f"Orchestrator verified against reference ID: {args.reference_id}")
            sys.exit(0)
        else:
            print(f"Orchestrator verification failed against reference ID: {args.reference_id}")
            for file_path, file_status in results["files"].items():
                if not file_status["verified"]:
                    print(f"  - {file_path}: {file_status.get('error', 'Fingerprint mismatch')}")
            sys.exit(1)
    
    elif args.command == "heal":
        if not args.reference_id:
            print("Error: --reference-id is required for heal command")
            sys.exit(1)
        
        # Heal orchestrator
        results = integration.heal_orchestrator(args.reference_id)
        
        if results["healed"]:
            print(f"Orchestrator healed from reference ID: {args.reference_id}")
            for file_path, file_status in results["files"].items():
                if file_status.get("healed", False):
                    print(f"  - Healed: {file_path}")
            sys.exit(0)
        else:
            print(f"Orchestrator healing failed from reference ID: {args.reference_id}")
            for file_path, file_status in results["files"].items():
                if not file_status.get("healed", True):
                    print(f"  - Failed: {file_path}: {file_status.get('error', 'Unknown error')}")
            sys.exit(1)
    
    elif args.command == "setup-auto":
        # Setup automatic backup
        results = integration.setup_auto_backup(
            interval_hours=args.interval,
            max_backups=args.max_backups
        )
        
        if results["success"]:
            print(f"Setup automatic backup with interval {args.interval} hours")
            print(f"Initial backup reference ID: {results['reference_id']}")
            sys.exit(0)
        else:
            print(f"Failed to setup automatic backup: {results.get('error', 'Unknown error')}")
            sys.exit(1)
    
    elif args.command == "run-auto":
        # Run automatic backup
        results = integration.run_auto_backup()
        
        if results["success"]:
            print(f"Created automatic backup with reference ID: {results['reference_id']}")
            print(f"Next backup at: {datetime.datetime.fromtimestamp(results['next_backup'])}")
            sys.exit(0)
        else:
            print(f"No backup created: {results.get('message', results.get('error', 'Unknown error'))}")
            sys.exit(0)  # Not an error, just no backup needed
