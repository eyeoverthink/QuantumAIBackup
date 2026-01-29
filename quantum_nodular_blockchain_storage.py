#!/usr/bin/env python3
"""
Quantum Blockchain Storage Node
------------------------------

This module implements a specialized storage node that persists quantum states
to blockchain, enabling permanent storage and retrieval of quantum node states.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import json
import time
import uuid
import logging
import hashlib
import datetime
from typing import Dict, Any, List, Optional, Tuple

# Import quantum modules
try:
    from quantum_blockchain_connector import QuantumBlockchainConnector
    from quantum_blockchain_genesis import QuantumBlockchainGenesis
except ImportError as e:
    logging.error(f"Failed to import blockchain modules: {e}")
    raise

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumBlockchainStorage")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

class QuantumBlockchainStorageNode:
    """Storage node that persists quantum states to blockchain."""
    
    def __init__(self, blockchain_connector=None, local_cache_dir="blockchain_cache"):
        """
        Initialize the blockchain storage node.
        
        Args:
            blockchain_connector: Optional blockchain connector (created if not provided)
            local_cache_dir: Directory for local cache of blockchain data
        """
        self.blockchain_connector = blockchain_connector or QuantumBlockchainConnector()
        self.local_cache_dir = local_cache_dir
        self.node_id = str(uuid.uuid4())
        self.node_type = "QuantumStorageNode"
        self.coherence = TARGET_COHERENCE
        
        # Create local cache directory if it doesn't exist
        os.makedirs(self.local_cache_dir, exist_ok=True)
        
        logger.info(f"Quantum Blockchain Storage Node initialized with ID: {self.node_id}")
    
    def store_node_state(self, node_type: str, node_id: str, state_data: Dict[str, Any]) -> str:
        """
        Store node state on blockchain.
        
        Args:
            node_type: Type of the node
            node_id: ID of the node
            state_data: Node state data
            
        Returns:
            str: Blockchain reference ID
        """
        metadata = {
            "node_type": node_type,
            "node_id": node_id,
            "timestamp": self._get_timestamp(),
            "phi_resonance": self._calculate_phi_resonance(state_data),
            "storage_node_id": self.node_id
        }
        
        logger.info(f"Storing {node_type} node {node_id} state to blockchain")
        reference_id = self.blockchain_connector.store_genesis_block(state_data, metadata)
        
        # Cache locally for faster access
        self._cache_node_state(reference_id, state_data, metadata)
        
        logger.info(f"Node state stored with reference ID: {reference_id}")
        return reference_id
    
    def retrieve_node_state(self, reference_id: str) -> Dict[str, Any]:
        """
        Retrieve node state from blockchain.
        
        Args:
            reference_id: Blockchain reference ID
            
        Returns:
            Dict[str, Any]: Node state data and metadata
        """
        logger.info(f"Retrieving node state from blockchain with reference ID: {reference_id}")
        
        # Try to get from local cache first
        cached_data = self._get_cached_node_state(reference_id)
        if cached_data:
            logger.info(f"Node state retrieved from local cache")
            return cached_data
        
        # Retrieve from blockchain if not in cache
        node_data = self.blockchain_connector.retrieve_genesis_block(reference_id)
        
        if node_data:
            # Cache the retrieved data
            metadata = node_data.get("metadata", {})
            state_data = node_data.get("data", {})
            self._cache_node_state(reference_id, state_data, metadata)
            
            logger.info(f"Node state retrieved successfully from blockchain")
            return node_data
        else:
            logger.error(f"Failed to retrieve node state with reference ID: {reference_id}")
            return {}
    
    def store_file(self, file_path: str, file_metadata: Dict[str, Any] = None) -> str:
        """
        Store a file on blockchain.
        
        Args:
            file_path: Path to the file
            file_metadata: Optional metadata for the file
            
        Returns:
            str: Blockchain reference ID
        """
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return ""
        
        try:
            with open(file_path, 'r') as f:
                file_content = f.read()
            
            # Prepare file data
            file_data = {
                "content": file_content,
                "filename": os.path.basename(file_path)
            }
            
            # Prepare metadata
            metadata = file_metadata or {}
            metadata.update({
                "file_path": file_path,
                "timestamp": self._get_timestamp(),
                "storage_node_id": self.node_id,
                "phi_resonance": self._calculate_phi_resonance(file_data)
            })
            
            logger.info(f"Storing file to blockchain: {file_path}")
            reference_id = self.blockchain_connector.store_genesis_block(file_data, metadata)
            logger.info(f"File stored with reference ID: {reference_id}")
            
            return reference_id
            
        except Exception as e:
            logger.error(f"Failed to store file: {e}")
            return ""
    
    def retrieve_file(self, reference_id: str, target_path: str = None) -> bool:
        """
        Retrieve a file from blockchain.
        
        Args:
            reference_id: Blockchain reference ID
            target_path: Optional target path to save the file
            
        Returns:
            bool: True if successful, False otherwise
        """
        logger.info(f"Retrieving file from blockchain with reference ID: {reference_id}")
        
        file_data = self.blockchain_connector.retrieve_genesis_block(reference_id)
        if not file_data:
            logger.error(f"Failed to retrieve file data")
            return False
        
        try:
            content = file_data.get("data", {}).get("content", "")
            filename = file_data.get("data", {}).get("filename", "unknown_file")
            
            # Determine target path
            if not target_path:
                target_path = os.path.join(self.local_cache_dir, filename)
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(os.path.abspath(target_path)), exist_ok=True)
            
            # Write file
            with open(target_path, 'w') as f:
                f.write(content)
            
            logger.info(f"File retrieved and saved to: {target_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save retrieved file: {e}")
            return False
    
    def list_stored_nodes(self, node_type: str = None) -> List[Dict[str, Any]]:
        """
        List nodes stored by this storage node.
        
        Args:
            node_type: Optional node type filter
            
        Returns:
            List[Dict[str, Any]]: List of stored nodes
        """
        metadata_filter = {"storage_node_id": self.node_id}
        if node_type:
            metadata_filter["node_type"] = node_type
        
        logger.info(f"Listing stored nodes with filter: {metadata_filter}")
        
        node_references = self.blockchain_connector.search_genesis_blocks(metadata_filter)
        
        nodes = []
        for reference in node_references:
            node_data = self.retrieve_node_state(reference)
            if node_data:
                nodes.append({
                    "reference_id": reference,
                    "metadata": node_data.get("metadata", {})
                })
        
        logger.info(f"Found {len(nodes)} stored nodes")
        return nodes
    
    def _cache_node_state(self, reference_id: str, state_data: Dict[str, Any], 
                         metadata: Dict[str, Any]) -> None:
        """
        Cache node state locally.
        
        Args:
            reference_id: Blockchain reference ID
            state_data: Node state data
            metadata: Node metadata
        """
        cache_file = os.path.join(self.local_cache_dir, f"{reference_id}.json")
        
        cache_data = {
            "reference_id": reference_id,
            "data": state_data,
            "metadata": metadata,
            "cache_timestamp": self._get_timestamp()
        }
        
        try:
            with open(cache_file, 'w') as f:
                json.dump(cache_data, f, indent=2)
            
            logger.debug(f"Node state cached to: {cache_file}")
        except Exception as e:
            logger.error(f"Failed to cache node state: {e}")
    
    def _get_cached_node_state(self, reference_id: str) -> Dict[str, Any]:
        """
        Get node state from local cache.
        
        Args:
            reference_id: Blockchain reference ID
            
        Returns:
            Dict[str, Any]: Node state data or empty dict if not found
        """
        cache_file = os.path.join(self.local_cache_dir, f"{reference_id}.json")
        
        if not os.path.exists(cache_file):
            return {}
        
        try:
            with open(cache_file, 'r') as f:
                cache_data = json.load(f)
            
            logger.debug(f"Node state loaded from cache: {cache_file}")
            return {
                "data": cache_data.get("data", {}),
                "metadata": cache_data.get("metadata", {})
            }
        except Exception as e:
            logger.error(f"Failed to load cached node state: {e}")
            return {}
    
    def _calculate_phi_resonance(self, data: Dict[str, Any]) -> float:
        """
        Calculate phi resonance for data.
        
        Args:
            data: Data to calculate resonance for
            
        Returns:
            float: Phi resonance value
        """
        # Convert data to string for hash calculation
        data_str = json.dumps(data, sort_keys=True)
        
        # Calculate hash
        hash_value = int(hashlib.sha256(data_str.encode()).hexdigest(), 16)
        
        # Calculate resonance using phi
        resonance = (hash_value * PHI) % 1
        
        return resonance
    
    def _get_timestamp(self) -> str:
        """
        Get current timestamp.
        
        Returns:
            str: ISO format timestamp
        """
        return datetime.datetime.now().isoformat()


def create_blockchain_storage_node(blockchain_connector=None, local_cache_dir="blockchain_cache"):
    """
    Create a blockchain storage node.
    
    Args:
        blockchain_connector: Optional blockchain connector
        local_cache_dir: Directory for local cache
        
    Returns:
        QuantumBlockchainStorageNode: The created storage node
    """
    return QuantumBlockchainStorageNode(
        blockchain_connector=blockchain_connector,
        local_cache_dir=local_cache_dir
    )


# Example usage
if __name__ == "__main__":
    # This is just an example and won't run without the proper imports
    try:
        # Create blockchain storage node
        storage_node = create_blockchain_storage_node()
        
        # Use storage node
        print("Quantum Blockchain Storage Node created")
        print(f"Node ID: {storage_node.node_id}")
        print(f"Node Type: {storage_node.node_type}")
        print(f"Coherence: {storage_node.coherence}")
        
    except ImportError as e:
        print(f"Failed to run example: {e}")
