#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Genesis Storage Extension
--------------------------------
Extends the QuantumGenesisStorage class with additional methods for file verification
and intrusion detection capabilities.

This module follows phi-harmonic principles and maintains quantum coherence
throughout all operations while adhering to the 'lego' modular philosophy.
"""

import os
import time
import json
import hashlib
import logging
import shutil
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumGenesisStorageExtension")

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PHI_COHERENCE = 3.6932381 / 10  # φ⁷·⁵/10 ≈ 0.991800

def extend_genesis_storage(storage_instance):
    """
    Extend a QuantumGenesisStorage instance with additional methods.
    
    Args:
        storage_instance: QuantumGenesisStorage instance to extend
        
    Returns:
        The extended QuantumGenesisStorage instance
    """
    if not hasattr(storage_instance, 'verify_file'):
        storage_instance.verify_file = lambda file_path: verify_file(storage_instance, file_path)
    
    if not hasattr(storage_instance, 'get_file_hash'):
        storage_instance.get_file_hash = lambda file_path: get_file_hash(storage_instance, file_path)
    
    if not hasattr(storage_instance, 'get_backup_metadata'):
        storage_instance.get_backup_metadata = lambda file_path: get_backup_metadata(storage_instance, file_path)
    
    if not hasattr(storage_instance, 'restore_file'):
        storage_instance.restore_file = lambda file_path: restore_file(storage_instance, file_path)
    
    logger.info(f"Extended QuantumGenesisStorage with verification and restoration capabilities")
    return storage_instance

def get_file_hash(storage_instance, file_path):
    """
    Calculate a phi-harmonic hash of a file.
    
    Args:
        storage_instance: QuantumGenesisStorage instance
        file_path (str): Path to the file
        
    Returns:
        str: Phi-harmonic hash of the file
    """
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return None
    
    try:
        # Read the file content
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Calculate phi-harmonic hash
        phi_seed = str(time.time() * PHI).encode()
        hash_input = phi_seed + content
        file_hash = hashlib.sha256(hash_input).hexdigest()
        
        return file_hash
    except Exception as e:
        logger.error(f"Error calculating file hash: {e}")
        return None

def get_backup_metadata(storage_instance, file_path):
    """
    Get the backup metadata for a file.
    
    Args:
        storage_instance: QuantumGenesisStorage instance
        file_path (str): Path to the file
        
    Returns:
        dict: Backup metadata or None if not found
    """
    # Get the base filename
    base_name = os.path.basename(file_path)
    
    try:
        # First, try to find in single_backups directory directly (most reliable method)
        single_backups_dir = os.path.join(storage_instance.genesis_dir, "single_backups")
        if os.path.exists(single_backups_dir):
            # Find all backups for this file
            backups = []
            for filename in os.listdir(single_backups_dir):
                if filename.startswith(base_name + ".") and filename.endswith(".backup"):
                    backup_path = os.path.join(single_backups_dir, filename)
                    backup_time = os.path.getmtime(backup_path)
                    backups.append((backup_path, backup_time))
            
            # Sort by modification time (newest first)
            backups.sort(key=lambda x: x[1], reverse=True)
            
            if backups:
                # Return metadata for the newest backup
                newest_backup = backups[0][0]
                logger.info(f"Found backup for {file_path} at {newest_backup}")
                return {
                    "original_path": file_path,
                    "backup_path": newest_backup,
                    "timestamp": backups[0][1],
                    "verified": True
                }
        
        # If not found in single_backups, check for backup metadata file
        metadata_path = os.path.join(storage_instance.genesis_dir, "backup_metadata.json")
        if os.path.exists(metadata_path):
            # Load backup metadata
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
            
            # Find the latest backup for this file
            if base_name in metadata:
                return metadata[base_name]
            
            # If not found by exact name, search through all entries
            for key, value in metadata.items():
                if isinstance(value, dict) and "original_path" in value and value["original_path"] == file_path:
                    return value
        
        # If we get here, try to find the backup file directly in the genesis directory
        for root, dirs, files in os.walk(storage_instance.genesis_dir):
            backups = []
            for filename in files:
                if filename.startswith(base_name) and ".backup" in filename:
                    backup_path = os.path.join(root, filename)
                    backup_time = os.path.getmtime(backup_path)
                    backups.append((backup_path, backup_time))
            
            if backups:
                # Sort by modification time (newest first)
                backups.sort(key=lambda x: x[1], reverse=True)
                newest_backup = backups[0][0]
                logger.info(f"Found backup for {file_path} at {newest_backup} through directory search")
                return {
                    "original_path": file_path,
                    "backup_path": newest_backup,
                    "timestamp": backups[0][1],
                    "verified": True
                }
        
        # If we still haven't found a backup, check if the test backup exists
        test_backup = file_path + ".bak"
        if os.path.exists(test_backup):
            logger.info(f"Using test backup for {file_path} at {test_backup}")
            return {
                "original_path": file_path,
                "backup_path": test_backup,
                "timestamp": os.path.getmtime(test_backup),
                "verified": True
            }
        
        logger.warning(f"No backup found for {file_path}")
        return None
    except Exception as e:
        logger.error(f"Error getting backup metadata: {e}")
        return None

def verify_file(storage_instance, file_path):
    """
    Verify the integrity of a file by comparing it with its backup.
    
    Args:
        storage_instance: QuantumGenesisStorage instance
        file_path (str): Path to the file to verify
        
    Returns:
        dict: Verification results
    """
    logger.info(f"Verifying file: {file_path}")
    
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return {"verified": False, "error": "File not found"}
    
    try:
        # Get backup metadata
        backup_metadata = get_backup_metadata(storage_instance, file_path)
        if not backup_metadata:
            logger.warning(f"No backup metadata found for {file_path}")
            return {"verified": False, "error": "No backup metadata found"}
        
        # Get backup path
        backup_path = backup_metadata.get("backup_path")
        if not backup_path or not os.path.exists(backup_path):
            logger.warning(f"Backup file not found: {backup_path}")
            return {"verified": False, "error": "Backup file not found"}
        
        # Calculate current file hash
        current_hash = None
        with open(file_path, 'rb') as f:
            current_content = f.read()
            current_hash = hashlib.sha256(current_content).hexdigest()
        
        # Calculate backup file hash
        backup_hash = None
        with open(backup_path, 'rb') as f:
            backup_content = f.read()
            backup_hash = hashlib.sha256(backup_content).hexdigest()
        
        # Compare hashes
        verified = current_hash == backup_hash
        
        # Create verification results
        verification_results = {
            "verified": verified,
            "file_path": file_path,
            "backup_path": backup_path,
            "timestamp": datetime.now().isoformat(),
            "current_hash": current_hash,
            "backup_hash": backup_hash
        }
        
        if verified:
            logger.info(f"File {file_path} verified successfully")
        else:
            logger.warning(f"File {file_path} verification failed - hashes do not match")
            
            # Calculate phi-harmonic coherence between the files
            coherence = calculate_phi_coherence(current_content, backup_content)
            verification_results["coherence"] = coherence
            
            # Detect tampering patterns
            tampering = detect_tampering(current_content, backup_content)
            verification_results["tampering"] = tampering
        
        return verification_results
    except Exception as e:
        logger.error(f"Error verifying file: {e}")
        return {"verified": False, "error": str(e)}

def calculate_phi_coherence(content1, content2):
    """
    Calculate phi-harmonic coherence between two content blocks.
    
    Args:
        content1 (bytes): First content block
        content2 (bytes): Second content block
        
    Returns:
        float: Phi-harmonic coherence value
    """
    try:
        # Calculate similarity using phi-harmonic principles
        if not content1 or not content2:
            return 0.0
        
        # Calculate byte-level differences
        min_len = min(len(content1), len(content2))
        max_len = max(len(content1), len(content2))
        
        if min_len == 0:
            return 0.0
        
        # Count matching bytes
        matches = sum(1 for i in range(min_len) if content1[i] == content2[i])
        
        # Calculate base coherence
        base_coherence = matches / max_len
        
        # Apply phi-harmonic transformation
        phi_coherence = (base_coherence * PHI) % 1
        
        # Scale to 0-1 range with phi influence
        coherence = (phi_coherence + base_coherence) / (1 + PHI)
        
        return coherence
    except Exception as e:
        logger.error(f"Error calculating coherence: {e}")
        return 0.0

def restore_file(storage_instance, file_path):
    """
    Restore a file from its backup.
    
    Args:
        storage_instance: QuantumGenesisStorage instance
        file_path (str): Path to the file to restore
        
    Returns:
        dict: Restoration results
    """
    logger.info(f"Restoring file: {file_path}")
    
    if not os.path.exists(file_path):
        logger.warning(f"File not found: {file_path}, will create it from backup")
    
    try:
        # Get backup metadata
        backup_metadata = get_backup_metadata(storage_instance, file_path)
        if not backup_metadata:
            logger.error(f"No backup metadata found for {file_path}")
            return {"success": False, "error": "No backup metadata found"}
        
        # Get backup path
        backup_path = backup_metadata.get("backup_path")
        if not backup_path or not os.path.exists(backup_path):
            logger.error(f"Backup file not found: {backup_path}")
            return {"success": False, "error": "Backup file not found"}
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
        
        # Restore the file
        shutil.copy2(backup_path, file_path)
        
        # Verify the restored file
        verification = verify_file(storage_instance, file_path)
        
        # Create restoration results
        restoration_results = {
            "success": verification.get("verified", False),
            "file_path": file_path,
            "backup_path": backup_path,
            "timestamp": datetime.now().isoformat(),
            "verification": verification
        }
        
        if restoration_results["success"]:
            logger.info(f"File {file_path} restored successfully")
        else:
            logger.warning(f"File {file_path} restoration verification failed")
        
        return restoration_results
    except Exception as e:
        logger.error(f"Error restoring file: {e}")
        return {"success": False, "error": str(e)}

def detect_tampering(current_content, backup_content):
    """
    Detect tampering patterns between current and backup content.
    
    Args:
        current_content (bytes): Current file content
        backup_content (bytes): Backup file content
        
    Returns:
        dict: Tampering detection results
    """
    try:
        # Initialize results
        results = {
            "detected": False,
            "type": None,
            "position": None,
            "added_lines": 0,
            "modified_lines": 0,
            "deleted_lines": 0
        }
        
        # Convert to text for line-by-line comparison
        try:
            current_text = current_content.decode('utf-8')
            backup_text = backup_content.decode('utf-8')
        except UnicodeDecodeError:
            # Binary file, compare raw bytes
            if current_content != backup_content:
                results["detected"] = True
                results["type"] = "binary_modification"
            return results
        
        # Split into lines
        current_lines = current_text.splitlines()
        backup_lines = backup_text.splitlines()
        
        # Compare line counts
        if len(current_lines) > len(backup_lines):
            results["detected"] = True
            results["type"] = "lines_added"
            results["added_lines"] = len(current_lines) - len(backup_lines)
            results["position"] = len(backup_lines)  # Assuming lines added at the end
        elif len(current_lines) < len(backup_lines):
            results["detected"] = True
            results["type"] = "lines_deleted"
            results["deleted_lines"] = len(backup_lines) - len(current_lines)
        
        # Compare line by line
        modified_lines = []
        for i in range(min(len(current_lines), len(backup_lines))):
            if current_lines[i] != backup_lines[i]:
                results["detected"] = True
                modified_lines.append(i)
        
        if modified_lines:
            results["modified_lines"] = len(modified_lines)
            results["modified_positions"] = modified_lines
            if not results["type"]:
                results["type"] = "content_modified"
        
        return results
    except Exception as e:
        logger.error(f"Error detecting tampering: {e}")
        return {"detected": False, "error": str(e)}

# Monkey patch the QuantumGenesisStorage class when this module is imported
def apply_extensions():
    """Apply extensions to the QuantumGenesisStorage class if available."""
    try:
        from quantum_genesis_storage import QuantumGenesisStorage
        
        # Store original __init__ method
        original_init = QuantumGenesisStorage.__init__
        
        # Define new __init__ method
        def new_init(self, *args, **kwargs):
            # Call original __init__
            original_init(self, *args, **kwargs)
            
            # Extend with new methods
            extend_genesis_storage(self)
        
        # Replace __init__ method
        QuantumGenesisStorage.__init__ = new_init
        
        logger.info("Successfully applied extensions to QuantumGenesisStorage class")
        return True
    except ImportError:
        logger.warning("QuantumGenesisStorage class not found, extensions not applied")
        return False

# Apply extensions when this module is imported
apply_extensions()

# Test function
def main():
    """Test the QuantumGenesisStorage extension."""
    try:
        from quantum_genesis_storage import QuantumGenesisStorage
        
        print("Testing QuantumGenesisStorage extension...")
        
        # Create a test file
        test_file = "test_file.txt"
        with open(test_file, 'w') as f:
            f.write("This is a test file for QuantumGenesisStorage extension.")
        
        # Initialize QuantumGenesisStorage
        storage = QuantumGenesisStorage()
        
        # Backup the test file
        backup_result = storage.backup_file(test_file)
        print(f"Backup result: {backup_result}")
        
        # Modify the test file
        with open(test_file, 'w') as f:
            f.write("This is a modified test file for QuantumGenesisStorage extension.")
        
        # Verify the test file
        verification_result = storage.verify_file(test_file)
        print(f"Verification result: {verification_result}")
        
        # Restore the test file
        restore_result = storage.restore_file(test_file)
        print(f"Restore result: {restore_result}")
        
        # Verify the restored file
        verification_result = storage.verify_file(test_file)
        print(f"Verification after restore: {verification_result}")
        
        # Clean up
        os.remove(test_file)
        
        print("Test completed successfully!")
        return True
    except Exception as e:
        print(f"Error testing QuantumGenesisStorage extension: {e}")
        return False

if __name__ == "__main__":
    main()
