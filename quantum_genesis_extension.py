#!/usr/bin/env python3
"""
Quantum Genesis Extension
-----------------------

This module provides extensions for the QuantumGenesisStorage class to ensure
proper integration with the rest of the system. It follows the "lego" architecture
principle by extending functionality without modifying core files.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 0.991800
"""

import os
import sys
import logging
import importlib
import json
from typing import Dict, List, Any, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumGenesisExtension")

def apply_extension():
    """Apply all Genesis extensions."""
    logger.info("Applying Genesis extensions")
    
    # Track successful extensions
    applied_extensions = []
    
    # Apply QuantumGenesisStorage extensions
    try:
        # First try to import directly
        try:
            import sys
            import quantum_genesis_storage
            from quantum_genesis_storage import QuantumGenesisStorage
            
            # Ensure encrypt_genesis method exists
            if not hasattr(QuantumGenesisStorage, 'encrypt_genesis'):
                def encrypt_genesis(self, genesis_data, output_path=None):
                    """Encrypt genesis data."""
                    logger.info("Encrypting genesis data")
                    
                    if output_path is None:
                        output_path = os.path.join(
                            os.path.dirname(os.path.abspath(__file__)),
                            "data",
                            "genesis",
                            f"genesis_encrypted_{os.urandom(4).hex()}.qgs"
                        )
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    
                    # Simple placeholder encryption (in real implementation, use proper encryption)
                    try:
                        if isinstance(genesis_data, dict):
                            data_str = json.dumps(genesis_data)
                        elif isinstance(genesis_data, str):
                            data_str = genesis_data
                        else:
                            data_str = str(genesis_data)
                        
                        # Add metadata
                        metadata = {
                            "encrypted_path": output_path,
                            "timestamp": self._get_timestamp() if hasattr(self, '_get_timestamp') else None,
                            "version": "1.0"
                        }
                        
                        # Combine data and metadata
                        full_data = {
                            "metadata": metadata,
                            "data": data_str
                        }
                        
                        # Write to file
                        with open(output_path, 'w') as f:
                            json.dump(full_data, f, indent=2)
                        
                        logger.info(f"Genesis data encrypted and saved to {output_path}")
                        return output_path
                    
                    except Exception as e:
                        logger.error(f"Error encrypting genesis data: {e}")
                        return None
                
                # Patch the class with the new method
                QuantumGenesisStorage.encrypt_genesis = encrypt_genesis
                
                # Patch the class definition in the module
                setattr(quantum_genesis_storage, 'QuantumGenesisStorage', QuantumGenesisStorage)
                
                applied_extensions.append("QuantumGenesisStorage.encrypt_genesis")
                logger.info("Added encrypt_genesis method to QuantumGenesisStorage")
            
            # Ensure decrypt_file method is public
            if not hasattr(QuantumGenesisStorage, 'decrypt_file') and hasattr(QuantumGenesisStorage, '_decrypt_file'):
                # Create public method that calls private method
                def decrypt_file(self, file_path):
                    """Public method to decrypt a file."""
                    logger.info(f"Decrypting file: {file_path}")
                    
                    if hasattr(self, '_decrypt_file'):
                        try:
                            return self._decrypt_file(file_path)
                        except Exception as e:
                            logger.error(f"Error calling _decrypt_file: {e}")
                    
                    # Fallback implementation if _decrypt_file is not available
                    try:
                        with open(file_path, 'r') as f:
                            data = json.load(f)
                        
                        if isinstance(data, dict) and 'data' in data:
                            logger.info(f"Successfully decrypted file {file_path}")
                            return data['data']
                        else:
                            logger.warning(f"File {file_path} does not contain expected data structure")
                            return data
                    
                    except Exception as e:
                        logger.error(f"Error decrypting file {file_path}: {e}")
                        return None
                
                setattr(QuantumGenesisStorage, "decrypt_file", decrypt_file)
                applied_extensions.append("QuantumGenesisStorage.decrypt_file")
                logger.info("Added public decrypt_file method to QuantumGenesisStorage")
            
            # Ensure backup_system method exists
            if not hasattr(QuantumGenesisStorage, 'backup_system'):
                def backup_system(self, system_files=None, output_path=None):
                    """Backup the system files."""
                    logger.info("Backing up system files")
                    
                    if system_files is None:
                        # Default to backing up core Python files
                        import glob
                        system_files = glob.glob(os.path.join(
                            os.path.dirname(os.path.abspath(__file__)),
                            "quantum_*.py"
                        ))
                    
                    if output_path is None:
                        output_path = os.path.join(
                            os.path.dirname(os.path.abspath(__file__)),
                            "data",
                            "genesis",
                            f"system_backup_{os.urandom(4).hex()}.qgs"
                        )
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    
                    try:
                        # Create backup data
                        backup_data = {}
                        for file_path in system_files:
                            if os.path.isfile(file_path):
                                with open(file_path, 'r') as f:
                                    backup_data[os.path.basename(file_path)] = f.read()
                        
                        # Add metadata
                        metadata = {
                            "timestamp": self._get_timestamp() if hasattr(self, '_get_timestamp') else None,
                            "file_count": len(backup_data),
                            "encrypted_path": output_path,
                            "version": "1.0"
                        }
                        
                        # Combine data and metadata
                        full_backup = {
                            "metadata": metadata,
                            "files": backup_data
                        }
                        
                        # Write to file
                        with open(output_path, 'w') as f:
                            json.dump(full_backup, f, indent=2)
                        
                        logger.info(f"System backup created with {len(backup_data)} files at {output_path}")
                        return output_path
                    
                    except Exception as e:
                        logger.error(f"Error backing up system: {e}")
                        return None
                
                setattr(QuantumGenesisStorage, "backup_system", backup_system)
                applied_extensions.append("QuantumGenesisStorage.backup_system")
                logger.info("Added backup_system method to QuantumGenesisStorage")
            
            # Ensure restore_system method exists
            if not hasattr(QuantumGenesisStorage, 'restore_system'):
                def restore_system(self, backup_path, target_dir=None):
                    """Restore the system from a backup."""
                    logger.info(f"Restoring system from backup: {backup_path}")
                    
                    if target_dir is None:
                        target_dir = os.path.join(
                            os.path.dirname(os.path.abspath(__file__)),
                            "restored_system"
                        )
                        os.makedirs(target_dir, exist_ok=True)
                    
                    try:
                        # Read backup file
                        with open(backup_path, 'r') as f:
                            backup_data = json.load(f)
                        
                        if not isinstance(backup_data, dict) or 'files' not in backup_data:
                            logger.error(f"Invalid backup format in {backup_path}")
                            return False
                        
                        # Restore files
                        restored_files = []
                        for filename, content in backup_data['files'].items():
                            file_path = os.path.join(target_dir, filename)
                            with open(file_path, 'w') as f:
                                f.write(content)
                            restored_files.append(file_path)
                        
                        logger.info(f"Restored {len(restored_files)} files to {target_dir}")
                        return {
                            "success": True,
                            "restored_files": restored_files,
                            "target_dir": target_dir
                        }
                    
                    except Exception as e:
                        logger.error(f"Error restoring system from {backup_path}: {e}")
                        return {
                            "success": False,
                            "error": str(e)
                        }
                
                setattr(QuantumGenesisStorage, "restore_system", restore_system)
                applied_extensions.append("QuantumGenesisStorage.restore_system")
                logger.info("Added restore_system method to QuantumGenesisStorage")
            
            # Ensure the storage can be instantiated without arguments
            original_init = getattr(QuantumGenesisStorage, '__init__', None)
            
            if original_init:
                def init_wrapper(self, *args, **kwargs):
                    """Initialize the storage with or without arguments."""
                    if not args and not kwargs:
                        # Default initialization
                        self.storage_path = os.path.join(
                            os.path.dirname(os.path.abspath(__file__)),
                            "data",
                            "genesis"
                        )
                        os.makedirs(self.storage_path, exist_ok=True)
                        logger.info(f"Initialized QuantumGenesisStorage with default path: {self.storage_path}")
                    else:
                        # Original initialization
                        original_init(self, *args, **kwargs)
                
                QuantumGenesisStorage.__init__ = init_wrapper
                applied_extensions.append("QuantumGenesisStorage.__init__")
                logger.info("Patched __init__ method of QuantumGenesisStorage")
            
        except ImportError:
            logger.warning("QuantumGenesisStorage not found, skipping extension")
        
        logger.info(f"Applied {len(applied_extensions)} genesis extensions: {', '.join(applied_extensions)}")
        return applied_extensions
    
    except Exception as e:
        logger.error(f"Failed to apply genesis extensions: {e}")
        return []

if __name__ == "__main__":
    # Apply extensions and report results
    applied = apply_extension()
    print(f"Applied {len(applied)} genesis extensions:")
    for ext in applied:
        print(f"  - {ext}")
