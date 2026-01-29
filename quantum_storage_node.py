#!/usr/bin/env python3
"""
Quantum Storage Node
-----------------------

Implementation of a storage-specialized quantum node for the nodular super-quantum computation system.
This module extends the base specialized node with capabilities focused on blockchain integration,
data persistence, and secure storage of quantum states and genesis information.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import json
import uuid
import logging
import hashlib
import datetime
import threading
import base64
from typing import Dict, Any, List, Tuple, Optional, Union, Callable

# Import quantum modules
try:
    from quantum_nodular_core import QuantumNodularCore, QuantumNodeState, PHI, PHI_POWERS, TARGET_COHERENCE
    from quantum_specialized_node import QuantumSpecializedNode, NodeSpecialization
    from quantum_blockchain_genesis import QuantumBlockchainGenesis
    from quantum_genesis_storage import QuantumGenesisStorage
except ImportError as e:
    logging.error(f"Required quantum modules not found: {e}")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumStorageNode")


class StorageTaskType:
    """Enumeration of storage task types."""
    STORE_DATA = "store_data"
    RETRIEVE_DATA = "retrieve_data"
    VERIFY_DATA = "verify_data"
    BACKUP_GENESIS = "backup_genesis"
    RESTORE_GENESIS = "restore_genesis"
    VERIFY_INTEGRITY = "verify_integrity"
    BLOCKCHAIN_STORE = "blockchain_store"
    BLOCKCHAIN_RETRIEVE = "blockchain_retrieve"


class QuantumStorageNode(QuantumSpecializedNode):
    """Implementation of a storage-specialized quantum node."""
    
    def __init__(self, core: QuantumNodularCore):
        """
        Initialize quantum storage node.
        
        Args:
            core: Quantum nodular core
        """
        super().__init__(core, NodeSpecialization.STORAGE)
        
        # Initialize blockchain and genesis components
        self.blockchain_genesis = QuantumBlockchainGenesis()
        self.genesis_storage = QuantumGenesisStorage()
        
        # Initialize storage capabilities
        self.capabilities = {
            StorageTaskType.STORE_DATA: 0.97,
            StorageTaskType.RETRIEVE_DATA: 0.98,
            StorageTaskType.VERIFY_DATA: 0.96,
            StorageTaskType.BACKUP_GENESIS: 0.99,
            StorageTaskType.RESTORE_GENESIS: 0.95,
            StorageTaskType.VERIFY_INTEGRITY: 0.97,
            StorageTaskType.BLOCKCHAIN_STORE: 0.94,
            StorageTaskType.BLOCKCHAIN_RETRIEVE: 0.93
        }
        
        # Initialize performance metrics
        self.performance_metrics = {
            "operations_completed": 0,
            "avg_operation_time": 0.0,
            "success_rate": 1.0,
            "storage_efficiency": 0.95,
            "blockchain_reliability": 0.97,
            "last_updated": time.time()
        }
        
        # Initialize storage state
        self.storage_state = {
            "active_operations": {},
            "storage_cache": {},
            "blockchain_references": {},
            "genesis_backups": {},
            "resource_usage": {
                "storage": 0.0,
                "blockchain": 0.0,
                "encryption": 0.0
            }
        }
        
        # Initialize storage paths
        self.storage_paths = {
            "local_storage": os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_storage"),
            "genesis_backups": os.path.join(os.path.dirname(os.path.abspath(__file__)), "genesis_backups"),
            "blockchain_refs": os.path.join(os.path.dirname(os.path.abspath(__file__)), "blockchain_refs")
        }
        
        # Create storage directories if they don't exist
        for path in self.storage_paths.values():
            if not os.path.exists(path):
                os.makedirs(path)
        
        # Update node state
        self._update_node_state()
        
        logger.info("Quantum storage node initialized")
    
    def can_perform_task(self, task_type: str, task_data: Dict[str, Any]) -> bool:
        """
        Check if node can perform specific storage task.
        
        Args:
            task_type: Type of storage task
            task_data: Task input data
            
        Returns:
            bool: True if node can perform task, False otherwise
        """
        # Check if task type is supported
        if task_type not in self.capabilities:
            return False
        
        # Check if node is active
        if not self.is_active:
            return False
        
        # Check capability threshold
        capability_score = self.capabilities.get(task_type, 0.0)
        if capability_score < 0.5:
            return False
        
        # Check resource availability
        if len(self.storage_state["active_operations"]) >= 5:  # Max 5 concurrent operations
            return False
        
        # Check data compatibility
        if task_type == StorageTaskType.STORE_DATA:
            return "data" in task_data and "key" in task_data
        elif task_type == StorageTaskType.RETRIEVE_DATA:
            return "key" in task_data
        elif task_type == StorageTaskType.VERIFY_DATA:
            return "key" in task_data and "expected_hash" in task_data
        elif task_type == StorageTaskType.BACKUP_GENESIS:
            return "genesis_data" in task_data
        elif task_type == StorageTaskType.RESTORE_GENESIS:
            return "backup_id" in task_data
        elif task_type == StorageTaskType.VERIFY_INTEGRITY:
            return "key" in task_data
        elif task_type == StorageTaskType.BLOCKCHAIN_STORE:
            return "data" in task_data and "reference_name" in task_data
        elif task_type == StorageTaskType.BLOCKCHAIN_RETRIEVE:
            return "reference_name" in task_data
        
        return False
    
    def perform_task(self, task_type: str, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform storage task.
        
        Args:
            task_type: Type of storage task
            task_data: Task input data
            
        Returns:
            dict: Task result
        """
        # Check if task can be performed
        if not self.can_perform_task(task_type, task_data):
            return {
                "success": False,
                "error": "Cannot perform task",
                "task_type": task_type
            }
        
        try:
            # Create operation ID
            operation_id = str(uuid.uuid4())
            
            # Add to active operations
            self.storage_state["active_operations"][operation_id] = {
                "task_type": task_type,
                "start_time": time.time(),
                "status": "processing"
            }
            
            # Process based on task type
            result = None
            
            if task_type == StorageTaskType.STORE_DATA:
                result = self._perform_store_data(task_data)
            elif task_type == StorageTaskType.RETRIEVE_DATA:
                result = self._perform_retrieve_data(task_data)
            elif task_type == StorageTaskType.VERIFY_DATA:
                result = self._perform_verify_data(task_data)
            elif task_type == StorageTaskType.BACKUP_GENESIS:
                result = self._perform_backup_genesis(task_data)
            elif task_type == StorageTaskType.RESTORE_GENESIS:
                result = self._perform_restore_genesis(task_data)
            elif task_type == StorageTaskType.VERIFY_INTEGRITY:
                result = self._perform_verify_integrity(task_data)
            elif task_type == StorageTaskType.BLOCKCHAIN_STORE:
                result = self._perform_blockchain_store(task_data)
            elif task_type == StorageTaskType.BLOCKCHAIN_RETRIEVE:
                result = self._perform_blockchain_retrieve(task_data)
            
            # Calculate duration
            end_time = time.time()
            duration = end_time - self.storage_state["active_operations"][operation_id]["start_time"]
            
            # Update operation status
            self.storage_state["active_operations"][operation_id]["status"] = "completed"
            self.storage_state["active_operations"][operation_id]["end_time"] = end_time
            self.storage_state["active_operations"][operation_id]["duration"] = duration
            
            # Remove from active operations
            completed_operation = self.storage_state["active_operations"].pop(operation_id)
            
            # Update performance metrics
            self._update_performance_metrics(task_type, duration, True)
            
            # Record task
            self.record_task(task_type, task_data, {
                "success": True,
                "duration": duration,
                "metrics": {
                    "operation_time": duration,
                    "task_type": task_type
                }
            })
            
            # Return result with metadata
            return {
                "success": True,
                "operation_id": operation_id,
                "task_type": task_type,
                "duration": duration,
                "result": result,
                "coherence": self.specialization_coherence,
                "timestamp": end_time
            }
        except Exception as e:
            logger.error(f"Error performing {task_type} task: {e}")
            
            # Update performance metrics
            self._update_performance_metrics(task_type, 0.0, False)
            
            return {
                "success": False,
                "error": str(e),
                "task_type": task_type
            }
    
    def _update_performance_metrics(self, task_type: str, duration: float, success: bool) -> None:
        """
        Update performance metrics based on task execution.
        
        Args:
            task_type: Type of task
            duration: Task duration
            success: Whether task was successful
        """
        # Update operation count
        self.performance_metrics["operations_completed"] += 1
        
        # Update average operation time
        old_avg = self.performance_metrics["avg_operation_time"]
        old_count = self.performance_metrics["operations_completed"] - 1
        
        if old_count > 0:
            self.performance_metrics["avg_operation_time"] = (old_avg * old_count + duration) / (old_count + 1)
        else:
            self.performance_metrics["avg_operation_time"] = duration
        
        # Update success rate
        old_success_rate = self.performance_metrics["success_rate"]
        
        if old_count > 0:
            self.performance_metrics["success_rate"] = (old_success_rate * old_count + (1.0 if success else 0.0)) / (old_count + 1)
        else:
            self.performance_metrics["success_rate"] = 1.0 if success else 0.0
        
        # Update storage efficiency
        if task_type in [StorageTaskType.STORE_DATA, StorageTaskType.RETRIEVE_DATA]:
            old_efficiency = self.performance_metrics["storage_efficiency"]
            efficiency_factor = 0.95 if success else 0.5
            self.performance_metrics["storage_efficiency"] = old_efficiency * 0.9 + efficiency_factor * 0.1
        
        # Update blockchain reliability
        if task_type in [StorageTaskType.BLOCKCHAIN_STORE, StorageTaskType.BLOCKCHAIN_RETRIEVE]:
            old_reliability = self.performance_metrics["blockchain_reliability"]
            reliability_factor = 0.98 if success else 0.4
            self.performance_metrics["blockchain_reliability"] = old_reliability * 0.9 + reliability_factor * 0.1
        
        # Update timestamp
        self.performance_metrics["last_updated"] = time.time()
    
    def _get_storage_path(self, key: str) -> str:
        """
        Get storage path for key.
        
        Args:
            key: Storage key
            
        Returns:
            str: Storage path
        """
        # Create hash of key for filename
        key_hash = hashlib.md5(key.encode()).hexdigest()
        
        # Create path
        return os.path.join(self.storage_paths["local_storage"], f"{key_hash}.json")
    
    def _get_genesis_backup_path(self, backup_id: str) -> str:
        """
        Get genesis backup path.
        
        Args:
            backup_id: Backup ID
            
        Returns:
            str: Backup path
        """
        return os.path.join(self.storage_paths["genesis_backups"], f"{backup_id}.json")
    
    def _get_blockchain_ref_path(self, reference_name: str) -> str:
        """
        Get blockchain reference path.
        
        Args:
            reference_name: Reference name
            
        Returns:
            str: Reference path
        """
        # Create hash of reference name for filename
        ref_hash = hashlib.md5(reference_name.encode()).hexdigest()
        
        # Create path
        return os.path.join(self.storage_paths["blockchain_refs"], f"{ref_hash}.json")
    
    def _calculate_data_hash(self, data: Any) -> str:
        """
        Calculate hash for data.
        
        Args:
            data: Input data
            
        Returns:
            str: Data hash
        """
        # Convert data to string
        if isinstance(data, (dict, list)):
            data_str = json.dumps(data, sort_keys=True)
        else:
            data_str = str(data)
        
        # Calculate hash
        return hashlib.sha256(data_str.encode()).hexdigest()
    
    def _apply_phi_harmonic_encryption(self, data: Any) -> Dict[str, Any]:
        """
        Apply phi-harmonic encryption to data.
        
        Args:
            data: Input data
            
        Returns:
            dict: Encrypted data with metadata
        """
        # Convert data to string
        if isinstance(data, (dict, list)):
            data_str = json.dumps(data, sort_keys=True)
        else:
            data_str = str(data)
        
        # Calculate original hash
        original_hash = hashlib.sha256(data_str.encode()).hexdigest()
        
        # Apply phi-harmonic transformation
        data_bytes = data_str.encode()
        phi_key = int(PHI * 1000000) % 256
        
        # Simple XOR encryption with phi-derived key
        encrypted_bytes = bytes([b ^ ((phi_key + i) % 256) for i, b in enumerate(data_bytes)])
        
        # Encode as base64
        encrypted_data = base64.b64encode(encrypted_bytes).decode()
        
        # Create metadata
        return {
            "encrypted_data": encrypted_data,
            "original_hash": original_hash,
            "encryption_method": "phi_harmonic_xor",
            "phi_key": phi_key,
            "timestamp": time.time(),
            "coherence": self.specialization_coherence
        }
    
    def _decrypt_phi_harmonic_data(self, encrypted_package: Dict[str, Any]) -> Any:
        """
        Decrypt phi-harmonic encrypted data.
        
        Args:
            encrypted_package: Encrypted data package
            
        Returns:
            Any: Decrypted data
        """
        # Extract encrypted data and metadata
        encrypted_data = encrypted_package["encrypted_data"]
        phi_key = encrypted_package["phi_key"]
        
        # Decode from base64
        encrypted_bytes = base64.b64decode(encrypted_data)
        
        # Decrypt with phi-derived key
        decrypted_bytes = bytes([b ^ ((phi_key + i) % 256) for i, b in enumerate(encrypted_bytes)])
        
        # Convert back to string
        decrypted_str = decrypted_bytes.decode()
        
        # Try to parse as JSON
        try:
            return json.loads(decrypted_str)
        except:
            return decrypted_str
    
    def _perform_store_data(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform store data task.
        
        Args:
            task_data: Task input data
            
        Returns:
            dict: Store data results
        """
        data = task_data["data"]
        key = task_data["key"]
        encrypt = task_data.get("encrypt", True)
        
        # Calculate data hash
        data_hash = self._calculate_data_hash(data)
        
        # Apply encryption if requested
        if encrypt:
            storage_package = self._apply_phi_harmonic_encryption(data)
        else:
            # Store as is with metadata
            storage_package = {
                "data": data,
                "data_hash": data_hash,
                "timestamp": time.time(),
                "coherence": self.specialization_coherence
            }
        
        # Get storage path
        storage_path = self._get_storage_path(key)
        
        # Store data
        with open(storage_path, 'w') as f:
            json.dump(storage_package, f)
        
        # Update storage cache
        self.storage_state["storage_cache"][key] = {
            "path": storage_path,
            "hash": data_hash,
            "encrypted": encrypt,
            "timestamp": time.time()
        }
        
        return {
            "key": key,
            "data_hash": data_hash,
            "encrypted": encrypt,
            "storage_path": storage_path,
            "coherence": self.specialization_coherence
        }
    
    def _perform_retrieve_data(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform retrieve data task.
        
        Args:
            task_data: Task input data
            
        Returns:
            dict: Retrieve data results
        """
        key = task_data["key"]
        
        # Check if key exists in cache
        if key not in self.storage_state["storage_cache"]:
            # Try to find file
            storage_path = self._get_storage_path(key)
            if not os.path.exists(storage_path):
                raise ValueError(f"Data not found for key: {key}")
            
            # Update cache
            self.storage_state["storage_cache"][key] = {
                "path": storage_path,
                "timestamp": os.path.getmtime(storage_path)
            }
        
        # Get storage path
        storage_path = self.storage_state["storage_cache"][key]["path"]
        
        # Read data
        with open(storage_path, 'r') as f:
            storage_package = json.load(f)
        
        # Check if data is encrypted
        if "encrypted_data" in storage_package:
            # Decrypt data
            data = self._decrypt_phi_harmonic_data(storage_package)
            encrypted = True
        else:
            # Data is not encrypted
            data = storage_package["data"]
            encrypted = False
        
        # Calculate data hash
        data_hash = self._calculate_data_hash(data)
        
        # Update cache with hash
        self.storage_state["storage_cache"][key]["hash"] = data_hash
        self.storage_state["storage_cache"][key]["encrypted"] = encrypted
        
        return {
            "key": key,
            "data": data,
            "data_hash": data_hash,
            "encrypted": encrypted,
            "coherence": self.specialization_coherence
        }
    
    def _perform_verify_data(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform verify data task.
        
        Args:
            task_data: Task input data
            
        Returns:
            dict: Verify data results
        """
        key = task_data["key"]
        expected_hash = task_data["expected_hash"]
        
        # Retrieve data
        retrieve_result = self._perform_retrieve_data({"key": key})
        
        # Check hash
        actual_hash = retrieve_result["data_hash"]
        verified = actual_hash == expected_hash
        
        return {
            "key": key,
            "verified": verified,
            "expected_hash": expected_hash,
            "actual_hash": actual_hash,
            "coherence": self.specialization_coherence
        }
    
    def _perform_backup_genesis(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform backup genesis task.
        
        Args:
            task_data: Task input data
            
        Returns:
            dict: Backup genesis results
        """
        genesis_data = task_data["genesis_data"]
        backup_id = task_data.get("backup_id", str(uuid.uuid4()))
        
        # Create backup using genesis storage
        backup_result = self.genesis_storage.create_backup(genesis_data)
        
        # Add phi-harmonic metadata
        backup_result["coherence"] = self.specialization_coherence
        backup_result["backup_id"] = backup_id
        
        # Store backup metadata
        backup_path = self._get_genesis_backup_path(backup_id)
        with open(backup_path, 'w') as f:
            json.dump(backup_result, f)
        
        # Update genesis backups cache
        self.storage_state["genesis_backups"][backup_id] = {
            "path": backup_path,
            "timestamp": time.time(),
            "data_hash": backup_result["genesis_hash"]
        }
        
        return {
            "backup_id": backup_id,
            "genesis_hash": backup_result["genesis_hash"],
            "backup_path": backup_path,
            "encrypted": backup_result["encrypted"],
            "coherence": self.specialization_coherence
        }
    
    def _perform_restore_genesis(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform restore genesis task.
        
        Args:
            task_data: Task input data
            
        Returns:
            dict: Restore genesis results
        """
        backup_id = task_data["backup_id"]
        
        # Get backup path
        backup_path = self._get_genesis_backup_path(backup_id)
        if not os.path.exists(backup_path):
            raise ValueError(f"Backup not found for ID: {backup_id}")
        
        # Read backup metadata
        with open(backup_path, 'r') as f:
            backup_metadata = json.load(f)
        
        # Restore from backup
        restore_result = self.genesis_storage.restore_from_backup(backup_metadata)
        
        # Add coherence
        restore_result["coherence"] = self.specialization_coherence
        
        return {
            "backup_id": backup_id,
            "genesis_data": restore_result["genesis_data"],
            "genesis_hash": restore_result["genesis_hash"],
            "coherence": self.specialization_coherence
        }
    
    def _perform_verify_integrity(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform verify integrity task.
        
        Args:
            task_data: Task input data
            
        Returns:
            dict: Verify integrity results
        """
        key = task_data["key"]
        
        # Retrieve data
        retrieve_result = self._perform_retrieve_data({"key": key})
        
        # Get data and calculate quantum fingerprint
        data = retrieve_result["data"]
        data_hash = retrieve_result["data_hash"]
        
        # Calculate quantum fingerprint
        if isinstance(data, (dict, list)):
            data_str = json.dumps(data, sort_keys=True)
        else:
            data_str = str(data)
        
        # Apply phi-harmonic transformation for fingerprint
        data_bytes = data_str.encode()
        phi_values = [(b * PHI) % 256 for b in data_bytes]
        
        # Create fingerprint
        fingerprint = hashlib.sha256(bytes([int(v) for v in phi_values])).hexdigest()
        
        # Calculate phi-harmonic coherence
        phi_coherence = sum([(v / 256) * PHI % 1.0 for v in phi_values]) / len(phi_values) if phi_values else 0
        
        # Combine for quantum fingerprint
        quantum_fingerprint = f"{fingerprint}:{phi_coherence:.6f}"
        
        return {
            "key": key,
            "data_hash": data_hash,
            "quantum_fingerprint": quantum_fingerprint,
            "phi_coherence": phi_coherence,
            "coherence": self.specialization_coherence
        }
    
    def _perform_blockchain_store(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform blockchain store task.
        
        Args:
            task_data: Task input data
            
        Returns:
            dict: Blockchain store results
        """
        data = task_data["data"]
        reference_name = task_data["reference_name"]
        
        # Store in blockchain
        blockchain_result = self.blockchain_genesis.store_reference(data, reference_name)
        
        # Store reference metadata
        ref_path = self._get_blockchain_ref_path(reference_name)
        with open(ref_path, 'w') as f:
            json.dump(blockchain_result, f)
        
        # Update blockchain references cache
        self.storage_state["blockchain_references"][reference_name] = {
            "path": ref_path,
            "timestamp": time.time(),
            "blockchain_id": blockchain_result["blockchain_id"]
        }
        
        return {
            "reference_name": reference_name,
            "blockchain_id": blockchain_result["blockchain_id"],
            "reference_hash": blockchain_result["reference_hash"],
            "coherence": self.specialization_coherence
        }
    
    def _perform_blockchain_retrieve(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform blockchain retrieve task.
        
        Args:
            task_data: Task input data
            
        Returns:
            dict: Blockchain retrieve results
        """
        reference_name = task_data["reference_name"]
        
        # Check if reference exists in cache
        if reference_name not in self.storage_state["blockchain_references"]:
            # Try to find file
            ref_path = self._get_blockchain_ref_path(reference_name)
            if not os.path.exists(ref_path):
                raise ValueError(f"Blockchain reference not found: {reference_name}")
            
            # Update cache
            with open(ref_path, 'r') as f:
                ref_data = json.load(f)
            
            self.storage_state["blockchain_references"][reference_name] = {
                "path": ref_path,
                "timestamp": time.time(),
                "blockchain_id": ref_data["blockchain_id"]
            }
        
        # Get reference metadata
        ref_path = self.storage_state["blockchain_references"][reference_name]["path"]
        with open(ref_path, 'r') as f:
            ref_metadata = json.load(f)
        
        # Retrieve from blockchain
        blockchain_id = ref_metadata["blockchain_id"]
        retrieve_result = self.blockchain_genesis.retrieve_reference(blockchain_id)
        
        # Verify hash
        reference_hash = self._calculate_data_hash(retrieve_result["data"])
        verified = reference_hash == ref_metadata["reference_hash"]
        
        return {
            "reference_name": reference_name,
            "blockchain_id": blockchain_id,
            "data": retrieve_result["data"],
            "verified": verified,
            "reference_hash": reference_hash,
            "coherence": self.specialization_coherence
        }
