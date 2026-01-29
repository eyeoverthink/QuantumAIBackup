#!/usr/bin/env python3
"""
Quantum Nodular Blockchain Extension
-----------------------------------

This module extends the quantum nodular network with blockchain capabilities,
enabling nodes to persist their state, discover other nodes, and self-replicate
through blockchain genesis blocks.

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
logger = logging.getLogger("QuantumNodularBlockchain")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

class QuantumNodularBlockchainExtension:
    """Extension that connects quantum nodular network with blockchain storage."""
    
    def __init__(self, nodular_adapter, blockchain_connector=None):
        """
        Initialize the nodular blockchain extension.
        
        Args:
            nodular_adapter: The quantum nodular adapter to extend
            blockchain_connector: Optional blockchain connector (created if not provided)
        """
        self.nodular_adapter = nodular_adapter
        self.blockchain_connector = blockchain_connector or QuantumBlockchainConnector()
        self.extension_id = str(uuid.uuid4())
        self.coherence = TARGET_COHERENCE
        
        # Register extension methods with nodular adapter
        self._register_extension_methods()
        
        logger.info(f"Quantum Nodular Blockchain Extension initialized with ID: {self.extension_id}")
    
    def _register_extension_methods(self):
        """Register extension methods with the nodular adapter."""
        # Add blockchain capabilities to the nodular adapter
        setattr(self.nodular_adapter, "store_node_state_to_blockchain", self.store_node_state)
        setattr(self.nodular_adapter, "retrieve_node_state_from_blockchain", self.retrieve_node_state)
        setattr(self.nodular_adapter, "discover_nodes_on_blockchain", self.discover_nodes)
        setattr(self.nodular_adapter, "replicate_node_from_blockchain", self.replicate_node)
        
        logger.info("Blockchain extension methods registered with nodular adapter")
    
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
            "phi_resonance": self._calculate_phi_resonance(state_data)
        }
        
        logger.info(f"Storing {node_type} node {node_id} state to blockchain")
        reference_id = self.blockchain_connector.store_genesis_block(state_data, metadata)
        logger.info(f"Node state stored with reference ID: {reference_id}")
        
        return reference_id
    
    def retrieve_node_state(self, reference_id: str) -> Dict[str, Any]:
        """
        Retrieve node state from blockchain.
        
        Args:
            reference_id: Blockchain reference ID
            
        Returns:
            Dict[str, Any]: Node state data
        """
        logger.info(f"Retrieving node state from blockchain with reference ID: {reference_id}")
        node_data = self.blockchain_connector.retrieve_genesis_block(reference_id)
        
        if node_data:
            logger.info(f"Node state retrieved successfully")
            return node_data
        else:
            logger.error(f"Failed to retrieve node state with reference ID: {reference_id}")
            return {}
    
    def discover_nodes(self, node_type: str = None) -> List[Dict[str, Any]]:
        """
        Discover nodes registered on blockchain.
        
        Args:
            node_type: Optional node type filter
            
        Returns:
            List[Dict[str, Any]]: List of discovered nodes
        """
        metadata_filter = {"node_type": node_type} if node_type else None
        logger.info(f"Discovering nodes on blockchain with filter: {metadata_filter}")
        
        node_references = self.blockchain_connector.search_genesis_blocks(metadata_filter)
        
        nodes = []
        for reference in node_references:
            node_data = self.retrieve_node_state(reference)
            if node_data:
                nodes.append({
                    "reference_id": reference,
                    "data": node_data
                })
        
        logger.info(f"Discovered {len(nodes)} nodes on blockchain")
        return nodes
    
    def replicate_node(self, reference_id: str, target_environment: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Replicate a node from blockchain.
        
        Args:
            reference_id: Blockchain reference ID
            target_environment: Optional target environment parameters
            
        Returns:
            Dict[str, Any]: Replicated node data
        """
        logger.info(f"Replicating node from blockchain with reference ID: {reference_id}")
        
        # Retrieve node state from blockchain
        node_data = self.retrieve_node_state(reference_id)
        if not node_data:
            logger.error(f"Failed to replicate node: could not retrieve state")
            return {}
        
        # Apply target environment parameters if provided
        if target_environment:
            node_data = self._adapt_node_to_environment(node_data, target_environment)
        
        # Generate new node ID for the replica
        node_data["node_id"] = str(uuid.uuid4())
        
        # Store the replicated node back to blockchain
        node_type = node_data.get("node_type", "unknown")
        replica_reference_id = self.store_node_state(node_type, node_data["node_id"], node_data)
        
        logger.info(f"Node replicated with new reference ID: {replica_reference_id}")
        return {
            "original_reference_id": reference_id,
            "replica_reference_id": replica_reference_id,
            "node_data": node_data
        }
    
    def _adapt_node_to_environment(self, node_data: Dict[str, Any], 
                                  target_environment: Dict[str, Any]) -> Dict[str, Any]:
        """
        Adapt node data to target environment.
        
        Args:
            node_data: Node data
            target_environment: Target environment parameters
            
        Returns:
            Dict[str, Any]: Adapted node data
        """
        adapted_data = node_data.copy()
        
        # Apply environment-specific adaptations
        for key, value in target_environment.items():
            if key in adapted_data:
                adapted_data[key] = value
        
        # Recalculate coherence for the adapted node
        adapted_data["coherence"] = self._calculate_coherence(adapted_data)
        
        return adapted_data
    
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
    
    def _calculate_coherence(self, data: Dict[str, Any]) -> float:
        """
        Calculate coherence for data.
        
        Args:
            data: Data to calculate coherence for
            
        Returns:
            float: Coherence value
        """
        # Default to target coherence
        return TARGET_COHERENCE
    
    def _get_timestamp(self) -> str:
        """
        Get current timestamp.
        
        Returns:
            str: ISO format timestamp
        """
        return datetime.datetime.now().isoformat()


def extend_nodular_adapter_with_blockchain(nodular_adapter, blockchain_connector=None):
    """
    Extend a nodular adapter with blockchain capabilities.
    
    Args:
        nodular_adapter: The nodular adapter to extend
        blockchain_connector: Optional blockchain connector
        
    Returns:
        QuantumNodularBlockchainExtension: The blockchain extension
    """
    extension = QuantumNodularBlockchainExtension(
        nodular_adapter=nodular_adapter,
        blockchain_connector=blockchain_connector
    )
    return extension


# Example usage
if __name__ == "__main__":
    # This is just an example and won't run without the proper imports
    try:
        from quantum_nodular_adapter import QuantumNodularAdapter
        from quantum_nodular_adapter_factory import create_nodular_adapter
        
        # Create nodular adapter
        nodular_adapter = create_nodular_adapter()
        
        # Extend with blockchain capabilities
        blockchain_extension = extend_nodular_adapter_with_blockchain(nodular_adapter)
        
        # Use blockchain capabilities
        print("Nodular adapter extended with blockchain capabilities")
        print(f"Extension ID: {blockchain_extension.extension_id}")
        print(f"Coherence: {blockchain_extension.coherence}")
        
    except ImportError as e:
        print(f"Failed to run example: {e}")
