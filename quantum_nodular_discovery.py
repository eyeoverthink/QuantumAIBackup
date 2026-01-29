#!/usr/bin/env python3
"""
Quantum Node Discovery
---------------------

This module implements a discovery mechanism for quantum nodes registered on blockchain,
enabling nodes to find and connect with each other in a distributed environment.

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
import datetime
from typing import Dict, Any, List, Optional, Tuple

# Import quantum modules
try:
    from quantum_blockchain_connector import QuantumBlockchainConnector
    from quantum_blockchain_genesis import QuantumBlockchainGenesis
    from quantum_nodular_blockchain_storage import QuantumBlockchainStorageNode
except ImportError as e:
    logging.error(f"Failed to import blockchain modules: {e}")
    raise

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumNodeDiscovery")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

class QuantumNodeDiscovery:
    """Discover quantum nodes registered on blockchain."""
    
    def __init__(self, blockchain_connector=None, storage_node=None):
        """
        Initialize the node discovery service.
        
        Args:
            blockchain_connector: Optional blockchain connector (created if not provided)
            storage_node: Optional blockchain storage node (created if not provided)
        """
        self.blockchain_connector = blockchain_connector or QuantumBlockchainConnector()
        self.storage_node = storage_node or QuantumBlockchainStorageNode(
            blockchain_connector=self.blockchain_connector
        )
        self.discovery_id = str(uuid.uuid4())
        self.coherence = TARGET_COHERENCE
        
        # Node registry cache
        self.node_registry = {}
        self.last_discovery = None
        
        logger.info(f"Quantum Node Discovery initialized with ID: {self.discovery_id}")
    
    def discover_nodes(self, node_type: str = None, refresh_cache: bool = False) -> List[Dict[str, Any]]:
        """
        Discover all nodes of specified type.
        
        Args:
            node_type: Optional node type filter
            refresh_cache: Whether to refresh the cache
            
        Returns:
            List[Dict[str, Any]]: List of discovered nodes
        """
        # Check if we need to refresh the cache
        if refresh_cache or self.last_discovery is None:
            self._refresh_node_registry()
        
        # Filter by node type if specified
        if node_type:
            filtered_nodes = [
                node for node in self.node_registry.values()
                if node.get("metadata", {}).get("node_type") == node_type
            ]
            logger.info(f"Discovered {len(filtered_nodes)} nodes of type {node_type}")
            return filtered_nodes
        else:
            logger.info(f"Discovered {len(self.node_registry)} nodes in total")
            return list(self.node_registry.values())
    
    def get_node_by_id(self, node_id: str, refresh_cache: bool = False) -> Dict[str, Any]:
        """
        Get node by ID.
        
        Args:
            node_id: Node ID
            refresh_cache: Whether to refresh the cache
            
        Returns:
            Dict[str, Any]: Node data or empty dict if not found
        """
        # Check if we need to refresh the cache
        if refresh_cache or self.last_discovery is None:
            self._refresh_node_registry()
        
        # Search for node by ID in metadata
        for node in self.node_registry.values():
            if node.get("metadata", {}).get("node_id") == node_id:
                logger.info(f"Found node with ID: {node_id}")
                return node
        
        logger.info(f"Node with ID {node_id} not found")
        return {}
    
    def get_node_by_reference(self, reference_id: str) -> Dict[str, Any]:
        """
        Get node by blockchain reference ID.
        
        Args:
            reference_id: Blockchain reference ID
            
        Returns:
            Dict[str, Any]: Node data or empty dict if not found
        """
        # Check if in registry cache
        if reference_id in self.node_registry:
            logger.info(f"Found node with reference ID: {reference_id} (from cache)")
            return self.node_registry[reference_id]
        
        # Retrieve from blockchain if not in cache
        node_data = self.storage_node.retrieve_node_state(reference_id)
        
        if node_data:
            # Add to registry cache
            self.node_registry[reference_id] = node_data
            logger.info(f"Found node with reference ID: {reference_id} (from blockchain)")
            return node_data
        else:
            logger.info(f"Node with reference ID {reference_id} not found")
            return {}
    
    def register_node(self, node_type: str, node_data: Dict[str, Any]) -> str:
        """
        Register a node on blockchain.
        
        Args:
            node_type: Type of the node
            node_data: Node data
            
        Returns:
            str: Blockchain reference ID
        """
        # Ensure node has an ID
        if "node_id" not in node_data:
            node_data["node_id"] = str(uuid.uuid4())
        
        # Add registration timestamp
        node_data["registration_timestamp"] = self._get_timestamp()
        
        # Store node state on blockchain
        reference_id = self.storage_node.store_node_state(
            node_type=node_type,
            node_id=node_data["node_id"],
            state_data=node_data
        )
        
        # Add to registry cache
        self.node_registry[reference_id] = {
            "data": node_data,
            "metadata": {
                "node_type": node_type,
                "node_id": node_data["node_id"],
                "reference_id": reference_id,
                "registration_timestamp": node_data["registration_timestamp"]
            }
        }
        
        logger.info(f"Registered {node_type} node with ID {node_data['node_id']} (reference: {reference_id})")
        return reference_id
    
    def update_node_status(self, reference_id: str, status_data: Dict[str, Any]) -> bool:
        """
        Update node status on blockchain.
        
        Args:
            reference_id: Blockchain reference ID
            status_data: Status data to update
            
        Returns:
            bool: True if successful, False otherwise
        """
        # Get current node data
        node_data = self.get_node_by_reference(reference_id)
        if not node_data:
            logger.error(f"Failed to update node status: node not found")
            return False
        
        # Update node data with status
        current_data = node_data.get("data", {})
        current_data.update(status_data)
        current_data["last_updated"] = self._get_timestamp()
        
        # Get node metadata
        metadata = node_data.get("metadata", {})
        node_type = metadata.get("node_type", "unknown")
        node_id = metadata.get("node_id", "unknown")
        
        # Store updated node state
        new_reference_id = self.storage_node.store_node_state(
            node_type=node_type,
            node_id=node_id,
            state_data=current_data
        )
        
        # Update registry cache
        self.node_registry[new_reference_id] = {
            "data": current_data,
            "metadata": {
                "node_type": node_type,
                "node_id": node_id,
                "reference_id": new_reference_id,
                "previous_reference": reference_id,
                "last_updated": current_data["last_updated"]
            }
        }
        
        logger.info(f"Updated {node_type} node with ID {node_id} (reference: {new_reference_id})")
        return True
    
    def find_nodes_by_capability(self, capability: str) -> List[Dict[str, Any]]:
        """
        Find nodes by capability.
        
        Args:
            capability: Capability to search for
            
        Returns:
            List[Dict[str, Any]]: List of nodes with the capability
        """
        # Ensure registry is up to date
        if self.last_discovery is None:
            self._refresh_node_registry()
        
        # Search for nodes with the capability
        capable_nodes = []
        for node in self.node_registry.values():
            node_data = node.get("data", {})
            capabilities = node_data.get("capabilities", [])
            
            if capability in capabilities:
                capable_nodes.append(node)
        
        logger.info(f"Found {len(capable_nodes)} nodes with capability: {capability}")
        return capable_nodes
    
    def find_nodes_by_phi_resonance(self, target_resonance: float, tolerance: float = 0.01) -> List[Dict[str, Any]]:
        """
        Find nodes by phi resonance.
        
        Args:
            target_resonance: Target phi resonance
            tolerance: Resonance tolerance
            
        Returns:
            List[Dict[str, Any]]: List of nodes with matching resonance
        """
        # Ensure registry is up to date
        if self.last_discovery is None:
            self._refresh_node_registry()
        
        # Search for nodes with matching resonance
        resonant_nodes = []
        for node in self.node_registry.values():
            metadata = node.get("metadata", {})
            resonance = metadata.get("phi_resonance", 0.0)
            
            if abs(resonance - target_resonance) <= tolerance:
                resonant_nodes.append(node)
        
        logger.info(f"Found {len(resonant_nodes)} nodes with resonance {target_resonance}±{tolerance}")
        return resonant_nodes
    
    def _refresh_node_registry(self) -> None:
        """Refresh the node registry from blockchain."""
        logger.info("Refreshing node registry from blockchain")
        
        # Search for all node references
        node_references = self.blockchain_connector.search_genesis_blocks(
            metadata_filter={"node_type": {"$exists": True}}
        )
        
        # Clear current registry
        self.node_registry = {}
        
        # Retrieve node data for each reference
        for reference in node_references:
            node_data = self.storage_node.retrieve_node_state(reference)
            if node_data:
                self.node_registry[reference] = node_data
        
        self.last_discovery = self._get_timestamp()
        logger.info(f"Node registry refreshed with {len(self.node_registry)} nodes")
    
    def _get_timestamp(self) -> str:
        """
        Get current timestamp.
        
        Returns:
            str: ISO format timestamp
        """
        return datetime.datetime.now().isoformat()


def create_node_discovery(blockchain_connector=None, storage_node=None):
    """
    Create a node discovery service.
    
    Args:
        blockchain_connector: Optional blockchain connector
        storage_node: Optional blockchain storage node
        
    Returns:
        QuantumNodeDiscovery: The created discovery service
    """
    return QuantumNodeDiscovery(
        blockchain_connector=blockchain_connector,
        storage_node=storage_node
    )


# Example usage
if __name__ == "__main__":
    # This is just an example and won't run without the proper imports
    try:
        # Create node discovery service
        discovery = create_node_discovery()
        
        # Use discovery service
        print("Quantum Node Discovery created")
        print(f"Discovery ID: {discovery.discovery_id}")
        print(f"Coherence: {discovery.coherence}")
        
        # Discover nodes
        nodes = discovery.discover_nodes()
        print(f"Discovered {len(nodes)} nodes")
        
    except ImportError as e:
        print(f"Failed to run example: {e}")
