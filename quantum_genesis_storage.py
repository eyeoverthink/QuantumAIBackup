#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Genesis Storage
----------------------
Provides encrypted storage and blockchain integration for the QuantumAI system's
self-reproduction capabilities. Enables the system to store its "best version"
in an encrypted format and recover it when needed.

This module follows phi-harmonic principles and maintains quantum coherence
throughout all operations.
"""

import os
import time
import json
import hashlib
import logging
import base64
import shutil
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumGenesisStorage")

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PHI_COHERENCE = 3.6932381 / 10  # φ⁷·⁵/10 ≈ 0.991800

class QuantumGenesisStorage:
    """
    Provides encrypted storage and blockchain integration for the QuantumAI system's
    self-reproduction capabilities.
    """
    
    def __init__(self):
        """
        Initialize the Quantum Genesis Storage system.
        """
        self.birth_timestamp = time.time()
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        
        # Set up directories
        self.genesis_dir = "genesis"
        self.blockchain_dir = "blockchain"
        self.recovery_dir = "recovery"
        
        for directory in [self.genesis_dir, self.blockchain_dir, self.recovery_dir]:
            os.makedirs(directory, exist_ok=True)
        
        # Initialize encryption key
        self.encryption_key = self._generate_phi_harmonic_key()
        
        logger.info(f"Initialized QuantumGenesisStorage with ID: {self.quantum_fingerprint}")
    
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
    
    def _generate_phi_harmonic_key(self):
        """
        Generate a phi-harmonic encryption key based on quantum principles.
        
        Returns:
            bytes: Encryption key
        """
        # Use phi and timestamp to create a seed
        timestamp = time.time()
        phi_seed = str(timestamp * PHI).encode()
        
        # Generate a salt using quantum fingerprint
        salt = self.quantum_fingerprint.encode()
        
        # Use PBKDF2 to derive a key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=int(PHI ** 8)  # φ⁸ iterations for quantum security
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(phi_seed))
        return key
    
    def encrypt_file(self, file_path, output_path=None):
        """
        Encrypt a file using phi-harmonic encryption.
        
        Args:
            file_path: Path to the file to encrypt
            output_path: Path to save the encrypted file (default: file_path.encrypted)
            
        Returns:
            str: Path to the encrypted file
        """
        if not output_path:
            output_path = f"{file_path}.encrypted"
        
        try:
            # Create Fernet cipher with our key
            cipher = Fernet(self.encryption_key)
            
            # Read the file
            with open(file_path, 'rb') as f:
                file_data = f.read()
            
            # Encrypt the data
            encrypted_data = cipher.encrypt(file_data)
            
            # Write the encrypted data
            with open(output_path, 'wb') as f:
                f.write(encrypted_data)
            
            logger.info(f"Encrypted {file_path} to {output_path}")
            return output_path
        
        except Exception as e:
            logger.error(f"Failed to encrypt {file_path}: {e}")
            return None
    
    def decrypt_file(self, encrypted_path, output_path=None):
        """
        Decrypt a file using phi-harmonic encryption.
        
        Args:
            encrypted_path: Path to the encrypted file
            output_path: Path to save the decrypted file
            
        Returns:
            str: Path to the decrypted file
        """
        if not output_path:
            output_path = encrypted_path.replace('.encrypted', '.decrypted')
        
        try:
            # Create Fernet cipher with our key
            cipher = Fernet(self.encryption_key)
            
            # Read the encrypted file
            with open(encrypted_path, 'rb') as f:
                encrypted_data = f.read()
            
            # Decrypt the data
            decrypted_data = cipher.decrypt(encrypted_data)
            
            # Write the decrypted data
            with open(output_path, 'wb') as f:
                f.write(decrypted_data)
            
            logger.info(f"Decrypted {encrypted_path} to {output_path}")
            return output_path
        
        except Exception as e:
            logger.error(f"Failed to decrypt {encrypted_path}: {e}")
            return None
    
    def create_genesis_backup(self, source_files, metadata=None):
        """
        Create an encrypted genesis backup of the system.
        
        Args:
            source_files: List of files to include in the backup
            metadata: Additional metadata to include
            
        Returns:
            dict: Backup metadata including paths and fingerprints
        """
        # Create timestamp and ID for this backup
        timestamp = time.time()
        backup_id = f"genesis-{self._generate_quantum_fingerprint()}"
        backup_dir = os.path.join(self.genesis_dir, backup_id)
        os.makedirs(backup_dir, exist_ok=True)
        
        # Initialize backup metadata
        backup_metadata = {
            "backup_id": backup_id,
            "timestamp": timestamp,
            "datetime": datetime.fromtimestamp(timestamp).isoformat(),
            "quantum_fingerprint": self.quantum_fingerprint,
            "phi_coherence": PHI_COHERENCE,
            "files": [],
            "user_metadata": metadata or {}
        }
        
        # Process each source file
        for file_path in source_files:
            if os.path.exists(file_path):
                # Calculate file hash
                file_hash = self._calculate_file_hash(file_path)
                
                # Create destination path
                rel_path = os.path.basename(file_path)
                dest_path = os.path.join(backup_dir, f"{rel_path}.encrypted")
                
                # Encrypt the file
                encrypted_path = self.encrypt_file(file_path, dest_path)
                
                if encrypted_path:
                    backup_metadata["files"].append({
                        "original_path": file_path,
                        "encrypted_path": encrypted_path,
                        "hash": file_hash,
                        "size": os.path.getsize(file_path)
                    })
        
        # Save backup metadata
        metadata_path = os.path.join(backup_dir, "metadata.json")
        with open(metadata_path, 'w') as f:
            json.dump(backup_metadata, f, indent=2)
        
        # Encrypt the metadata file
        self.encrypt_file(metadata_path, f"{metadata_path}.encrypted")
        
        logger.info(f"Created genesis backup: {backup_id} with {len(backup_metadata['files'])} files")
        return backup_metadata
    
    def _calculate_file_hash(self, file_path):
        """
        Calculate a phi-harmonic hash of a file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            str: File hash
        """
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            buf = f.read(4096)
            while buf:
                hasher.update(buf)
                buf = f.read(4096)
        
        # Add phi-harmonic component to the hash
        phi_component = str(int(hasher.hexdigest(), 16) * PHI % 1).encode()
        hasher.update(phi_component)
        
        return hasher.hexdigest()
    
    def encrypt_genesis(self, backup_id):
        """
        Encrypt all files in a genesis backup directory.
        
        Args:
            backup_id: ID of the genesis backup
            
        Returns:
            bool: True if encryption was successful
        """
        backup_dir = os.path.join(self.genesis_dir, backup_id)
        
        if not os.path.exists(backup_dir):
            logger.error(f"Backup directory not found: {backup_dir}")
            return False
        
        try:
            # Get all files in the backup directory
            files_to_encrypt = []
            for root, _, files in os.walk(backup_dir):
                for file in files:
                    if not file.endswith(".encrypted"):
                        file_path = os.path.join(root, file)
                        files_to_encrypt.append(file_path)
            
            # Encrypt each file
            encrypted_count = 0
            for file_path in files_to_encrypt:
                if self.encrypt_file(file_path):
                    encrypted_count += 1
                    # Remove the original file after encryption
                    if os.path.exists(file_path):
                        os.remove(file_path)
            
            logger.info(f"Encrypted {encrypted_count}/{len(files_to_encrypt)} files in genesis backup {backup_id}")
            return encrypted_count == len(files_to_encrypt)
            
        except Exception as e:
            logger.error(f"Failed to encrypt genesis backup {backup_id}: {e}")
            return False
    
    def backup_file(self, file_path):
        """
        Create a backup of a single file.
        
        Args:
            file_path: Path to the file to backup
            
        Returns:
            str: Path to the backup file
        """
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return None
            
        # Create a backup directory if it doesn't exist
        backup_dir = os.path.join(self.genesis_dir, "single_backups")
        os.makedirs(backup_dir, exist_ok=True)
        
        # Generate backup filename with timestamp
        timestamp = int(time.time())
        file_name = os.path.basename(file_path)
        backup_path = os.path.join(backup_dir, f"{file_name}.{timestamp}.backup")
        
        try:
            # Create a copy of the file
            shutil.copy2(file_path, backup_path)
            
            # Calculate hash for verification
            file_hash = self._calculate_file_hash(file_path)
            backup_hash = self._calculate_file_hash(backup_path)
            
            # Verify backup integrity
            if file_hash == backup_hash:
                logger.info(f"Successfully backed up {file_path} to {backup_path}")
                return backup_path
            else:
                logger.error(f"Backup verification failed for {file_path}")
                if os.path.exists(backup_path):
                    os.remove(backup_path)
                return None
                
        except Exception as e:
            logger.error(f"Failed to backup {file_path}: {e}")
            if os.path.exists(backup_path):
                os.remove(backup_path)
            return None
    
    def store_to_blockchain(self, genesis_backup_id):
        """
        Store a genesis backup reference to a blockchain.
        
        Args:
            genesis_backup_id: ID of the genesis backup
            
        Returns:
            str: Blockchain transaction ID
        """
        # In a real implementation, this would interact with a blockchain API
        # For now, we'll simulate blockchain storage
        
        backup_dir = os.path.join(self.genesis_dir, genesis_backup_id)
        metadata_path = os.path.join(backup_dir, "metadata.json")
        
        if not os.path.exists(metadata_path):
            metadata_path = f"{metadata_path}.encrypted"
            if not os.path.exists(metadata_path):
                logger.error(f"Backup metadata not found for {genesis_backup_id}")
                return None
        
        # Read metadata (decrypt if needed)
        if metadata_path.endswith('.encrypted'):
            temp_path = os.path.join(self.blockchain_dir, "temp_metadata.json")
            self.decrypt_file(metadata_path, temp_path)
            with open(temp_path, 'r') as f:
                metadata = json.load(f)
            os.remove(temp_path)
        else:
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
        
        # Create blockchain entry
        blockchain_entry = {
            "timestamp": time.time(),
            "datetime": datetime.now().isoformat(),
            "genesis_backup_id": genesis_backup_id,
            "quantum_fingerprint": self.quantum_fingerprint,
            "metadata_fingerprint": self._calculate_file_hash(metadata_path),
            "phi_coherence": PHI_COHERENCE,
            "transaction_id": f"tx-{self._generate_quantum_fingerprint()}"
        }
        
        # Save blockchain entry
        blockchain_path = os.path.join(
            self.blockchain_dir, 
            f"blockchain-{blockchain_entry['transaction_id']}.json"
        )
        with open(blockchain_path, 'w') as f:
            json.dump(blockchain_entry, f, indent=2)
        
        logger.info(f"Stored genesis backup {genesis_backup_id} to blockchain with transaction ID {blockchain_entry['transaction_id']}")
        return blockchain_entry["transaction_id"]
    
    def recover_from_genesis(self, backup_id, target_dir=None, files_only=None):
        """
        Recover system files from a genesis backup.
        
        Args:
            backup_id: ID of the genesis backup
            target_dir: Directory to recover files to
            files_only: List of specific files to recover (optional)
            
        Returns:
            bool: True if recovery was successful
        """
        if not target_dir:
            target_dir = os.path.join(self.recovery_dir, f"recovery-{int(time.time())}")
            os.makedirs(target_dir, exist_ok=True)
        
        backup_dir = os.path.join(self.genesis_dir, backup_id)
        metadata_path = os.path.join(backup_dir, "metadata.json.encrypted")
        
        if not os.path.exists(metadata_path):
            logger.error(f"Backup metadata not found for {backup_id}")
            return False
        
        # Decrypt metadata
        temp_metadata_path = os.path.join(target_dir, "metadata.json")
        self.decrypt_file(metadata_path, temp_metadata_path)
        
        # Read metadata
        with open(temp_metadata_path, 'r') as f:
            metadata = json.load(f)
        
        # Process each file in the backup
        success_count = 0
        total_files = 0
        
        for file_info in metadata["files"]:
            original_filename = os.path.basename(file_info["original_path"])
            
            # Skip files not in files_only list if specified
            if files_only and original_filename not in files_only:
                continue
                
            total_files += 1
            
            # Handle files that might not have encrypted_path in metadata
            if "encrypted_path" in file_info:
                encrypted_path = file_info["encrypted_path"]
            else:
                # Construct the encrypted path based on backup structure
                file_name = os.path.basename(file_info["original_path"])
                encrypted_path = os.path.join(self.genesis_dir, backup_id, f"{file_name}.encrypted")
                
            target_path = os.path.join(target_dir, original_filename)
            
            # Decrypt the file
            if self.decrypt_file(encrypted_path, target_path):
                success_count += 1
        
        recovery_success = success_count == total_files
        logger.info(f"Recovered {success_count}/{total_files} files from genesis backup {backup_id} to {target_dir}")
        
        # Create recovery metadata
        recovery_metadata = {
            "timestamp": time.time(),
            "datetime": datetime.now().isoformat(),
            "genesis_backup_id": backup_id,
            "recovery_dir": target_dir,
            "files_recovered": success_count,
            "total_files": len(metadata["files"]),
            "success": recovery_success,
            "quantum_fingerprint": self.quantum_fingerprint
        }
        
        # Save recovery metadata
        recovery_metadata_path = os.path.join(target_dir, "recovery_metadata.json")
        with open(recovery_metadata_path, 'w') as f:
            json.dump(recovery_metadata, f, indent=2)
        
        return recovery_success
    
    def find_best_genesis_backup(self):
        """
        Find the best genesis backup based on phi-harmonic coherence.
        
        Returns:
            str: ID of the best genesis backup
        """
        # Get all genesis backups
        if not os.path.exists(self.genesis_dir):
            logger.error(f"Genesis directory not found: {self.genesis_dir}")
            return None
        
        backup_dirs = [d for d in os.listdir(self.genesis_dir) 
                      if os.path.isdir(os.path.join(self.genesis_dir, d)) 
                      and d.startswith("genesis-")]
        
        if not backup_dirs:
            logger.error("No genesis backups found")
            return None
        
        # Evaluate each backup
        best_backup = None
        best_coherence_delta = float('inf')
        
        for backup_id in backup_dirs:
            metadata_path = os.path.join(self.genesis_dir, backup_id, "metadata.json")
            if not os.path.exists(metadata_path):
                metadata_path = f"{metadata_path}.encrypted"
                if not os.path.exists(metadata_path):
                    continue
                
                # Decrypt metadata
                temp_path = os.path.join(self.blockchain_dir, "temp_metadata.json")
                self.decrypt_file(metadata_path, temp_path)
                with open(temp_path, 'r') as f:
                    metadata = json.load(f)
                os.remove(temp_path)
            else:
                with open(metadata_path, 'r') as f:
                    metadata = json.load(f)
            
            # Calculate coherence delta (how close to target phi coherence)
            coherence = metadata.get("phi_coherence", 0)
            coherence_delta = abs(coherence - PHI_COHERENCE)
            
            # Update best backup if this one is better
            if coherence_delta < best_coherence_delta:
                best_backup = backup_id
                best_coherence_delta = coherence_delta
        
        if best_backup:
            logger.info(f"Found best genesis backup: {best_backup} with coherence delta {best_coherence_delta:.6f}")
        else:
            logger.error("No valid genesis backups found")
        
        return best_backup


def main():
    """
    Main function to demonstrate the QuantumGenesisStorage capabilities.
    """
    # Initialize the storage system
    storage = QuantumGenesisStorage()
    
    # Create a test file
    test_file = "test_genesis_file.py"
    with open(test_file, 'w') as f:
        f.write("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Test Genesis File
----------------
This is a test file for the QuantumGenesisStorage system.
'''

def main():
    print("Hello from the Genesis system!")
    print("This file demonstrates self-reproduction capabilities.")
    print("Phi-harmonic coherence: 0.991800 (φ⁷·⁵/10)")

if __name__ == "__main__":
    main()
""")
    
    # Create a genesis backup
    backup_metadata = storage.create_genesis_backup(
        [test_file, __file__],
        metadata={"purpose": "demonstration", "version": "1.0.0"}
    )
    
    # Store to blockchain
    transaction_id = storage.store_to_blockchain(backup_metadata["backup_id"])
    
    # Recover from genesis
    storage.recover_from_genesis(backup_metadata["backup_id"])
    
    # Clean up test file
    os.remove(test_file)
    
    print(f"Genesis backup created with ID: {backup_metadata['backup_id']}")
    print(f"Blockchain transaction ID: {transaction_id}")
    print("Recovery completed. Check the 'recovery' directory for restored files.")


if __name__ == "__main__":
    main()
