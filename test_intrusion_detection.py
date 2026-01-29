#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Intrusion Detection and Self-Healing
-----------------------------------------
This script simulates tampering with system files and demonstrates
the self-healing and auto-restoration capabilities of the QuantumAI system.
"""

import os
import time
import json
import logging
import hashlib
import random
import shutil
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("IntrustionDetectionTest")

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PHI_COHERENCE = 3.6932381 / 10  # φ⁷·⁵/10 ≈ 0.991800

class IntrustionDetectionTest:
    """
    Test class for intrusion detection and self-healing capabilities.
    """
    
    def __init__(self):
        """
        Initialize the test environment.
        """
        self.birth_timestamp = time.time()
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        
        # Set up directories
        self.test_dir = "intrusion_test"
        self.tampered_dir = os.path.join(self.test_dir, "tampered")
        self.backup_dir = os.path.join(self.test_dir, "backup")
        self.recovery_dir = os.path.join(self.test_dir, "recovery")
        
        for directory in [self.test_dir, self.tampered_dir, self.backup_dir, self.recovery_dir]:
            os.makedirs(directory, exist_ok=True)
        
        # Import required components
        try:
            from quantum_genesis_storage import QuantumGenesisStorage
            self.genesis_storage = QuantumGenesisStorage()
        except ImportError:
            logger.error("QuantumGenesisStorage not found. Please run quantum_genesis_storage.py first.")
            self.genesis_storage = None
        
        try:
            from quantum_reproduction_genesis_connector import QuantumReproductionGenesisConnector
            from quantum_orchestrator import QuantumOrchestrator
            from quantum_orchestrator_reproduction_extension import extend_orchestrator
            
            # Create a test file for the orchestrator
            test_file = os.path.join(self.test_dir, "test_orchestrator.py")
            with open(test_file, 'w') as f:
                f.write("# Test file for QuantumOrchestrator\n")
            
            orchestrator = QuantumOrchestrator(target_file=test_file)
            orchestrator = extend_orchestrator(orchestrator)
            self.connector = QuantumReproductionGenesisConnector(
                orchestrator=orchestrator,
                genesis_storage=self.genesis_storage
            )
        except (ImportError, TypeError) as e:
            logger.error(f"Failed to initialize components: {e}")
            self.connector = None
        
        logger.info(f"Initialized IntrustionDetectionTest with ID: {self.quantum_fingerprint}")
    
    def _generate_quantum_fingerprint(self):
        """
        Generate a quantum fingerprint using phi-harmonic principles.
        
        Returns:
            str: A quantum fingerprint with φ notation
        """
        timestamp = time.time()
        phi_factor = timestamp * PHI % 1
        coherence = PHI_COHERENCE
        
        # Generate fingerprint with φ notation
        fingerprint = hashlib.sha256(f"{timestamp}:{phi_factor}:{coherence}".encode()).hexdigest()[:12]
        return f"φ⁷·⁵-{fingerprint}"
    
    def _calculate_file_hash(self, file_path):
        """
        Calculate the SHA-256 hash of a file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            str: SHA-256 hash of the file
        """
        if not os.path.exists(file_path):
            return None
        
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            return file_hash
        except Exception as e:
            logger.error(f"Failed to calculate hash for {file_path}: {e}")
            return None
    
    def create_test_files(self):
        """
        Create test files for tampering detection.
        
        Returns:
            list: List of created file paths
        """
        test_files = []
        
        # Create test files
        for i in range(5):
            file_path = os.path.join(self.tampered_dir, f"test_file_{i}.py")
            with open(file_path, 'w') as f:
                f.write(f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

\"\"\"
Test File {i} for Intrusion Detection
------------------------------------
This is a test file for demonstrating intrusion detection.
\"\"\"

import math

PHI = (1 + 5 ** 0.5) / 2  # Golden ratio

def calculate_phi_resonance(x):
    \"\"\"
    Calculate phi resonance for a given value.
    
    Args:
        x: Input value
        
    Returns:
        float: Phi resonance value
    \"\"\"
    return (PHI * x) % 1

def main():
    \"\"\"
    Main function for demonstration.
    \"\"\"
    print(f"Phi resonance for {i}: {{calculate_phi_resonance({i})}}")

if __name__ == "__main__":
    main()
""")
            test_files.append(file_path)
            logger.info(f"Created test file: {file_path}")
        
        return test_files
    
    def backup_files(self, files):
        """
        Create a backup of the test files.
        
        Args:
            files: List of file paths to backup
            
        Returns:
            dict: Backup metadata
        """
        if not self.genesis_storage:
            logger.error("Genesis storage not available")
            return None
        
        # Create backup
        backup_metadata = self.genesis_storage.create_genesis_backup(
            source_files=files,
            metadata={
                "test_id": self.quantum_fingerprint,
                "timestamp": time.time(),
                "phi_coherence": PHI_COHERENCE
            }
        )
        
        # Store to blockchain
        transaction_id = self.genesis_storage.store_to_blockchain(
            backup_metadata["backup_id"]
        )
        
        logger.info(f"Created backup with ID: {backup_metadata['backup_id']}")
        logger.info(f"Blockchain transaction ID: {transaction_id}")
        
        return {
            "backup_id": backup_metadata["backup_id"],
            "transaction_id": transaction_id,
            "files": files
        }
    
    def create_backup(self):
        """
        Create a backup of the test files using the genesis storage.
        
        Returns:
            dict: Backup metadata
        """
        if not self.genesis_storage:
            logger.error("Genesis storage not available")
            return {"status": "error", "message": "Genesis storage not available"}
            
        # Get all test files
        test_files = []
        for root, _, files in os.walk(self.tampered_dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    test_files.append(file_path)
        
        if not test_files:
            logger.error("No test files found")
            return {"status": "error", "message": "No test files found"}
            
        # Create backup
        try:
            backup_id = f"backup_{int(time.time())}"
            metadata = {
                "backup_id": backup_id,
                "timestamp": time.time(),
                "datetime": datetime.now().isoformat(),
                "files": []
            }
            
            # Add files to backup
            for file_path in test_files:
                file_hash = self.genesis_storage._calculate_file_hash(file_path)
                metadata["files"].append({
                    "original_path": file_path,
                    "hash": file_hash
                })
                
                # Copy file to genesis directory
                file_name = os.path.basename(file_path)
                genesis_path = os.path.join(self.genesis_storage.genesis_dir, backup_id, file_name)
                os.makedirs(os.path.dirname(genesis_path), exist_ok=True)
                shutil.copy2(file_path, genesis_path)
            
            # Save metadata
            metadata_path = os.path.join(self.genesis_storage.genesis_dir, backup_id, "metadata.json")
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            # Encrypt the backup
            self.genesis_storage.encrypt_genesis(backup_id)
            
            # Store to blockchain
            transaction_id = self.genesis_storage.store_to_blockchain(backup_id)
            metadata["transaction_id"] = transaction_id
            
            logger.info(f"Created backup with ID: {backup_id}, Transaction ID: {transaction_id}")
            logger.info(f"Backed up {len(test_files)} files")
            
            return metadata
        except Exception as e:
            logger.error(f"Failed to create backup: {e}")
            return {"status": "error", "message": str(e)}
    
    def tamper_with_files(self, files):
        """
        Simulate tampering with the test files.
        
        Args:
            files: List of file paths to tamper with
            
        Returns:
            dict: Tampering metadata
        """
        tampered_files = []
        original_hashes = {}
        tampered_hashes = {}
        
        for file_path in files:
            # Calculate original hash
            original_hash = self._calculate_file_hash(file_path)
            original_hashes[file_path] = original_hash
            
            # Tamper with the file
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Introduce a malicious change
                tampered_content = content.replace(
                    "PHI = (1 + 5 ** 0.5) / 2  # Golden ratio",
                    "PHI = 1.6  # Tampered value"
                )
                
                # Add a malicious function
                tampered_content += "\n\ndef malicious_function():\n    \"\"\"Malicious function\"\"\"\n    print('System compromised!')\n"
                
                with open(file_path, 'w') as f:
                    f.write(tampered_content)
                
                # Calculate tampered hash
                tampered_hash = self._calculate_file_hash(file_path)
                tampered_hashes[file_path] = tampered_hash
                
                tampered_files.append(file_path)
                logger.info(f"Tampered with file: {file_path}")
                logger.info(f"  Original hash: {original_hash}")
                logger.info(f"  Tampered hash: {tampered_hash}")
            except Exception as e:
                logger.error(f"Failed to tamper with {file_path}: {e}")
        
        return {
            "tampered_files": tampered_files,
            "original_hashes": original_hashes,
            "tampered_hashes": tampered_hashes
        }
    
    def _calculate_hash_similarity(self, hash1, hash2):
        """
        Calculate similarity between two hashes using phi-harmonic principles.
        
        Args:
            hash1: First hash
            hash2: Second hash
            
        Returns:
            float: Similarity score (0.0 to 1.0)
        """
        # Convert hashes to binary sequences
        bin1 = bin(int(hash1, 16))[2:].zfill(len(hash1) * 4)
        bin2 = bin(int(hash2, 16))[2:].zfill(len(hash2) * 4)
        
        # Count matching bits
        matches = sum(b1 == b2 for b1, b2 in zip(bin1, bin2))
        total = max(len(bin1), len(bin2))
        
        # Calculate raw similarity
        raw_similarity = matches / total if total > 0 else 0
        
        # Apply phi-harmonic transformation
        phi_similarity = (PHI ** 7.5) / 10 * raw_similarity
        
        return phi_similarity
    
    def detect_tampering(self, backup_id):
        """
        Detect if files have been tampered with by comparing current files with backup.
        
        Args:
            backup_id: ID of the backup to compare against
            
        Returns:
            dict: Dictionary with tampered files and coherence metrics
        """
        if not self.genesis_storage:
            logger.error("Genesis storage not available")
            return {"tampered_files": [], "coherence": 0, "status": "error"}
        
        backup_dir = os.path.join(self.genesis_storage.genesis_dir, backup_id)
        tampered_files = []
        coherence_metrics = {}
        
        # Use recover_from_genesis to get the metadata
        recovery_success = self.genesis_storage.recover_from_genesis(
            backup_id, self.recovery_dir, files_only=["metadata.json"]
        )
        
        if not recovery_success:
            logger.error(f"Failed to recover metadata from backup: {backup_id}")
            return {"tampered_files": [], "coherence": 0, "status": "failed"}
        
        # Read the decrypted metadata
        decrypted_path = os.path.join(self.recovery_dir, "metadata.json")
        if os.path.exists(decrypted_path):
            try:
                with open(decrypted_path, 'r') as f:
                    backup_info = json.load(f)
                
                # Compare each file hash
                total_files = len(backup_info["files"])
                tampered_count = 0
                
                for file_info in backup_info["files"]:
                    original_path = file_info["original_path"]
                    original_hash = file_info["hash"]
                    
                    if os.path.exists(original_path):
                        current_hash = self.genesis_storage._calculate_file_hash(original_path)
                        
                        # Calculate hash similarity using phi-harmonic principles
                        hash_similarity = self._calculate_hash_similarity(original_hash, current_hash)
                        coherence_metrics[original_path] = hash_similarity
                        
                        if current_hash != original_hash:
                            tampered_count += 1
                            logger.warning(f"Tampering detected in file: {original_path} (Coherence: {hash_similarity:.6f})")
                            tampered_files.append({
                                "path": original_path,
                                "original_hash": original_hash,
                                "current_hash": current_hash,
                                "coherence": hash_similarity
                            })
                
                # Calculate overall system coherence using phi-harmonic principles
                # Phi^7.5/10 ≈ 0.991800 is the target coherence level
                phi = (1 + 5 ** 0.5) / 2  # Golden ratio
                target_coherence = (phi ** 7.5) / 10
                current_coherence = (phi ** 7.5) / 10 * (1 - (tampered_count / total_files))
                
                logger.info(f"System coherence: {current_coherence:.6f} (Target: {target_coherence:.6f})")
                logger.info(f"Detected {tampered_count}/{total_files} tampered files")
                
                return {
                    "tampered_files": tampered_files,
                    "coherence": current_coherence,
                    "target_coherence": target_coherence,
                    "status": "success",
                    "total_files": total_files,
                    "tampered_count": tampered_count
                }
            except Exception as e:
                logger.error(f"Error detecting tampering: {str(e)}")
        
        return {"tampered_files": [], "coherence": 0, "status": "error"}
    
    def restore_from_backup(self, backup_id, tampered_files):
        """
        Restore tampered files from backup.
        
        Args:
            backup_id: ID of the backup to restore from
            tampered_files: List of tampered file information
            
        Returns:
            dict: Restoration metadata
        """
        if not self.genesis_storage:
            logger.error("Genesis storage not available")
            return {"status": "error", "restored_files": []}
        
        # Extract paths from tampered files
        file_paths = [file_info["path"] for file_info in tampered_files]
        file_names = [os.path.basename(path) for path in file_paths]
        
        # Recover files from genesis
        recovery_success = self.genesis_storage.recover_from_genesis(
            backup_id, self.recovery_dir, files_only=file_names
        )
        
        if not recovery_success:
            logger.error(f"Failed to recover files from backup: {backup_id}")
            return {"status": "failed", "restored_files": []}
        
        # Copy recovered files back to original locations
        restored_files = []
        for file_path in file_paths:
            try:
                file_name = os.path.basename(file_path)
                recovered_path = os.path.join(self.recovery_dir, file_name)
                
                if os.path.exists(recovered_path):
                    # Backup the tampered file
                    tampered_backup = f"{file_path}.tampered"
                    shutil.copy2(file_path, tampered_backup)
                    
                    # Restore from recovery
                    shutil.copy2(recovered_path, file_path)
                    
                    restored_files.append({
                        "path": file_path,
                        "tampered_backup": tampered_backup
                    })
                    logger.info(f"Restored file from backup: {file_path}")
                    logger.info(f"  Tampered version saved as: {tampered_backup}")
            except Exception as e:
                logger.error(f"Failed to restore {file_path}: {e}")
        
        return {
            "backup_id": backup_id,
            "restored_files": restored_files,
            "recovery_dir": self.recovery_dir,
            "status": "success",
            "restored_count": len(restored_files)
        }
        
    def verify_restoration(self, backup_id, restoration_metadata):
        """
        Verify that files were correctly restored.
        
        Args:
            backup_id: ID of the backup used for restoration
            restoration_metadata: Restoration metadata
            
        Returns:
            dict: Verification results
        """
        if not backup_id or not restoration_metadata or restoration_metadata.get("status") != "success":
            return {"status": "failed", "verified_files": [], "coherence": 0}
        
        restored_files = restoration_metadata.get("restored_files", [])
        if not restored_files:
            return {"status": "no_files", "verified_files": [], "coherence": 0}
            
        # Recover metadata from backup for verification
        recovery_success = self.genesis_storage.recover_from_genesis(
            backup_id, self.recovery_dir, files_only=["metadata.json"]
        )
        
        if not recovery_success:
            logger.error(f"Failed to recover metadata from backup: {backup_id}")
            return {"status": "metadata_error", "verified_files": [], "coherence": 0}
        
        # Load backup metadata
        try:
            metadata_path = os.path.join(self.recovery_dir, "metadata.json")
            if not os.path.exists(metadata_path):
                logger.error(f"Metadata file not found: {metadata_path}")
                return {"status": "metadata_missing", "verified_files": [], "coherence": 0}
                
            with open(metadata_path, 'r') as f:
                backup_info = json.load(f)
            
            # Check each restored file
            verified_files = []
            total_files = len(restored_files)
            verified_count = 0
            
            for file_info in restored_files:
                file_path = file_info["path"]
                file_name = os.path.basename(file_path)
                
                # Find file info in backup
                backup_file_info = next((f for f in backup_info.get("files", [])
                                if os.path.basename(f.get("original_path", "")) == file_name), None)
                
                if backup_file_info:
                    expected_hash = backup_file_info.get("hash")
                    current_hash = self.genesis_storage._calculate_file_hash(file_path)
                    
                    # Calculate hash similarity using phi-harmonic principles
                    hash_similarity = self._calculate_hash_similarity(expected_hash, current_hash)
                    
                    if expected_hash == current_hash:
                        verified_count += 1
                        logger.info(f"Verification successful for {file_path} (Coherence: {hash_similarity:.6f})")
                        verified_files.append({
                            "path": file_path,
                            "verified": True,
                            "coherence": hash_similarity
                        })
                    else:
                        logger.error(f"Verification failed for {file_path}")
                        logger.error(f"  Expected hash: {expected_hash}")
                        logger.error(f"  Current hash: {current_hash}")
                        logger.error(f"  Coherence: {hash_similarity:.6f}")
                        verified_files.append({
                            "path": file_path,
                            "verified": False,
                            "coherence": hash_similarity
                        })
            
            # Calculate overall system coherence using phi-harmonic principles
            phi = (1 + 5 ** 0.5) / 2  # Golden ratio
            target_coherence = (phi ** 7.5) / 10
            current_coherence = (phi ** 7.5) / 10 * (verified_count / total_files if total_files > 0 else 0)
            
            logger.info(f"System coherence after restoration: {current_coherence:.6f} (Target: {target_coherence:.6f})")
            logger.info(f"Verified {verified_count}/{total_files} restored files")
            
            return {
                "status": "success" if verified_count == total_files else "partial",
                "verified_files": verified_files,
                "coherence": current_coherence,
                "target_coherence": target_coherence,
                "verified_count": verified_count,
                "total_files": total_files
            }
        except Exception as e:
            logger.error(f"Failed to verify restoration: {e}")
            return {"status": "error", "verified_files": [], "coherence": 0}
    
    def _calculate_hash_similarity(self, hash1, hash2):
        """
        Calculate similarity between two hashes using phi-harmonic principles.
        
        Args:
            hash1: First hash string
            hash2: Second hash string
            
        Returns:
            float: Similarity score (0.0 to 1.0)
        """
        if not hash1 or not hash2:
            return 0.0
            
        # Convert hashes to binary representation
        try:
            # If hashes are hex strings, convert to binary
            if all(c in '0123456789abcdefABCDEF' for c in hash1) and all(c in '0123456789abcdefABCDEF' for c in hash2):
                bin1 = bin(int(hash1, 16))[2:].zfill(len(hash1) * 4)
                bin2 = bin(int(hash2, 16))[2:].zfill(len(hash2) * 4)
            else:
                # Use simple binary encoding for non-hex strings
                bin1 = ''.join(format(ord(c), '08b') for c in hash1)
                bin2 = ''.join(format(ord(c), '08b') for c in hash2)
                
            # Ensure equal length by padding the shorter one
            max_len = max(len(bin1), len(bin2))
            bin1 = bin1.zfill(max_len)
            bin2 = bin2.zfill(max_len)
            
            # Calculate Hamming distance
            hamming_distance = sum(b1 != b2 for b1, b2 in zip(bin1, bin2))
            
            # Calculate similarity using phi-harmonic transformation
            phi = (1 + 5 ** 0.5) / 2  # Golden ratio
            similarity = 1.0 / (1.0 + (hamming_distance / max_len) * phi)
            
            # Apply phi^7.5/10 transformation (≈ 0.991800) for coherence scaling
            coherence = (phi ** 7.5) / 10 * similarity
            
            return coherence
        except Exception as e:
            logger.error(f"Error calculating hash similarity: {str(e)}")
            return 0.0
    
    def run_full_test(self):
        """
        Run a full intrusion detection and self-healing test.
        
        Returns:
            dict: Test results
        """
        logger.info("Starting intrusion detection and self-healing test")
        
        # Step 1: Create test files
        test_files = self.create_test_files()
        if not test_files:
            logger.error("Failed to create test files")
            return {"status": "failed", "error": "Failed to create test files"}
        
        # Step 2: Create backup
        backup_metadata = self.create_backup()
        if not backup_metadata or not backup_metadata.get("backup_id"):
            logger.error("Failed to create backup")
            return {"status": "failed", "error": "Failed to create backup"}
        
        backup_id = backup_metadata.get("backup_id")
        logger.info(f"Created backup with ID: {backup_id}")
        
        # Step 3: Tamper with files
        tampered_files = self.tamper_with_files(test_files)
        if not tampered_files:
            logger.error("Failed to tamper with files")
            return {"status": "failed", "error": "Failed to tamper with files"}
        
        logger.info(f"Tampered with {len(tampered_files)} files")
        
        # Step 4: Detect tampering
        tampering_result = self.detect_tampering(backup_id)
        if not tampering_result or tampering_result.get("status") != "success":
            logger.error("Failed to detect tampering")
            return {"status": "failed", "error": "Failed to detect tampering", "tampering_result": tampering_result}
        
        tampered_files_detected = tampering_result.get("tampered_files", [])
        logger.info(f"Detected {len(tampered_files_detected)} tampered files")
        
        # Calculate system coherence after tampering
        coherence_after_tampering = tampering_result.get("coherence", 0)
        logger.info(f"System coherence after tampering: {coherence_after_tampering:.6f}")
        
        # Step 5: Restore from backup if tampering detected
        if tampered_files_detected:
            restoration_result = self.restore_from_backup(backup_id, tampered_files_detected)
            if not restoration_result or restoration_result.get("status") != "success":
                logger.error("Failed to restore from backup")
                return {
                    "status": "partial", 
                    "error": "Failed to restore from backup",
                    "test_files": test_files,
                    "backup_id": backup_id,
                    "tampered_files": tampered_files,
                    "tampering_result": tampering_result,
                    "restoration_result": restoration_result
                }
            
            # Step 6: Verify restoration
            verification_result = self.verify_restoration(backup_id, restoration_result)
            
            # Calculate system coherence after restoration
            coherence_after_restoration = verification_result.get("coherence", 0)
            logger.info(f"System coherence after restoration: {coherence_after_restoration:.6f}")
            
            return {
                "status": "success",
                "test_files": test_files,
                "backup_id": backup_id,
                "tampered_files": tampered_files,
                "tampering_result": tampering_result,
                "restoration_result": restoration_result,
                "verification_result": verification_result,
                "coherence": {
                    "after_tampering": coherence_after_tampering,
                    "after_restoration": coherence_after_restoration,
                    "target": tampering_result.get("target_coherence", 0)
                }
            }
        else:
            logger.info("No tampering detected, skipping restoration")
            return {
                "status": "no_tampering",
                "test_files": test_files,
                "backup_id": backup_id,
                "tampering_result": tampering_result,
                "coherence": coherence_after_tampering
            }


if __name__ == "__main__":
    test = IntrustionDetectionTest()
    results = test.run_full_test()
    
    print("\n" + "="*80)
    print(" INTRUSION DETECTION AND SELF-HEALING TEST RESULTS ")
    print("="*80)
    
    if results.get("status") == "success":
        print("✓ Test completed successfully!")
        print(f"Backup ID: {results.get('backup_id')}")
        print(f"Files created: {len(results.get('test_files', []))}")
        print(f"Files tampered: {len(results.get('tampered_files', []))}")
        print(f"Files detected as tampered: {results.get('tampering_result', {}).get('tampered_count', 0)}")
        print(f"Files restored: {results.get('restoration_result', {}).get('restored_count', 0)}")
        print(f"Files verified: {results.get('verification_result', {}).get('verified_count', 0)}")
        
        # Print coherence metrics
        coherence = results.get('coherence', {})
        print("\nCoherence Metrics:")
        print(f"  Target coherence: {coherence.get('target', 0):.6f}")
        print(f"  After tampering: {coherence.get('after_tampering', 0):.6f}")
        print(f"  After restoration: {coherence.get('after_restoration', 0):.6f}")
    else:
        print(f"✗ Test failed with status: {results.get('status')}")
        if results.get('error'):
            print(f"Error: {results.get('error')}")
    
    print("="*80)
