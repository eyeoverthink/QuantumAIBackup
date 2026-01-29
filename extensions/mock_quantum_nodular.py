"""
Mock Quantum Nodular Network Components

This module provides mock implementations of the quantum nodular network
components for testing the distributed meta-cognition integration.

Created: 2025-07-22
Coherence: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import json
import time
import logging
import hashlib
from typing import Dict, List, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('MockQuantumNodular')

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio φ
PHI_7_5 = PHI ** 7.5    # φ⁷·⁵ ≈ 36.932381


class QuantumNodularNetwork:
    """Mock implementation of the Quantum Nodular Network."""
    
    def __init__(self):
        """Initialize the mock nodular network."""
        self.nodes = {}
        self.connections = {}
        self.phi_resonance = (PHI * hash(str(time.time()))) % 1.0
        self.coherence = 0.75  # Default coherence
        
        logger.info("Mock Quantum Nodular Network initialized")
    
    def create_node(self, node_id: str, node_type: str, capabilities: List[str]) -> Dict[str, Any]:
        """Create a new node in the network.
        
        Args:
            node_id: Unique identifier for the node
            node_type: Type of node to create
            capabilities: List of node capabilities
            
        Returns:
            Dict containing node information
        """
        node = {
            "id": node_id,
            "type": node_type,
            "capabilities": capabilities,
            "phi_resonance": (PHI * hash(node_id)) % 1.0,
            "coherence": 0.7 + (hash(node_id) % 100) / 1000,
            "created_at": time.time()
        }
        
        self.nodes[node_id] = node
        logger.info(f"Created node {node_id} of type {node_type}")
        
        return node
    
    def connect_nodes(self, source_id: str, target_id: str) -> bool:
        """Connect two nodes in the network.
        
        Args:
            source_id: Source node ID
            target_id: Target node ID
            
        Returns:
            True if connection successful, False otherwise
        """
        if source_id not in self.nodes or target_id not in self.nodes:
            logger.error(f"Cannot connect nodes: one or both nodes do not exist")
            return False
        
        connection_id = f"{source_id}:{target_id}"
        self.connections[connection_id] = {
            "source": source_id,
            "target": target_id,
            "strength": (PHI - 1) * 0.5,
            "created_at": time.time()
        }
        
        logger.info(f"Connected nodes {source_id} and {target_id}")
        return True
    
    def get_node(self, node_id: str) -> Optional[Dict[str, Any]]:
        """Get a node by ID.
        
        Args:
            node_id: ID of the node to get
            
        Returns:
            Node information or None if not found
        """
        return self.nodes.get(node_id)
    
    def get_nodes_by_type(self, node_type: str) -> List[Dict[str, Any]]:
        """Get nodes by type.
        
        Args:
            node_type: Type of nodes to get
            
        Returns:
            List of matching nodes
        """
        return [node for node in self.nodes.values() if node["type"] == node_type]
    
    def get_nodes_by_capability(self, capability: str) -> List[Dict[str, Any]]:
        """Get nodes by capability.
        
        Args:
            capability: Capability to search for
            
        Returns:
            List of matching nodes
        """
        return [node for node in self.nodes.values() if capability in node["capabilities"]]
    
    def get_network_state(self) -> Dict[str, Any]:
        """Get the current state of the network.
        
        Returns:
            Dict containing network state
        """
        return {
            "node_count": len(self.nodes),
            "connection_count": len(self.connections),
            "phi_resonance": self.phi_resonance,
            "coherence": self.coherence
        }


class QuantumNodeDiscovery:
    """Mock implementation of the Quantum Node Discovery service."""
    
    def __init__(self):
        """Initialize the mock node discovery service."""
        self.registry = {}
        self.capability_index = {}
        
        logger.info("Mock Quantum Node Discovery initialized")
    
    def register_node(self, node_type: str, node_data: Dict[str, Any]) -> bool:
        """Register a node with the discovery service.
        
        Args:
            node_type: Type of node to register
            node_data: Node data to register
            
        Returns:
            True if registration successful, False otherwise
        """
        node_id = node_data.get("id")
        if not node_id:
            logger.error("Cannot register node: missing node ID")
            return False
        
        # Store node in registry
        self.registry[node_id] = {
            "type": node_type,
            "data": node_data,
            "registered_at": time.time()
        }
        
        # Index node by capabilities
        capabilities = node_data.get("capabilities", [])
        for capability in capabilities:
            if capability not in self.capability_index:
                self.capability_index[capability] = []
            self.capability_index[capability].append(node_id)
        
        logger.info(f"Registered node {node_id} of type {node_type}")
        return True
    
    def discover_nodes_by_type(self, node_type: str) -> List[Dict[str, Any]]:
        """Discover nodes by type.
        
        Args:
            node_type: Type of nodes to discover
            
        Returns:
            List of matching nodes
        """
        return [entry["data"] for entry in self.registry.values() if entry["type"] == node_type]
    
    def discover_nodes_by_capability(self, capability: str) -> List[Dict[str, Any]]:
        """Discover nodes by capability.
        
        Args:
            capability: Capability to search for
            
        Returns:
            List of matching nodes
        """
        matching_nodes = []
        node_ids = self.capability_index.get(capability, [])
        
        for node_id in node_ids:
            if node_id in self.registry:
                matching_nodes.append(self.registry[node_id]["data"])
        
        return matching_nodes
    
    def get_node(self, node_id: str) -> Optional[Dict[str, Any]]:
        """Get a node by ID.
        
        Args:
            node_id: ID of the node to get
            
        Returns:
            Node data or None if not found
        """
        entry = self.registry.get(node_id)
        return entry["data"] if entry else None


class QuantumBlockchainConnector:
    """Mock implementation of the Quantum Blockchain Connector."""
    
    def __init__(self):
        """Initialize the mock blockchain connector."""
        self.blocks = {}
        self.genesis_blocks = {}
        self.transaction_count = 0
        
        logger.info("Mock Quantum Blockchain Connector initialized")
    
    def store_genesis_block(self, system_id: str, data: Dict[str, Any]) -> str:
        """Store a genesis block for a system.
        
        Args:
            system_id: ID of the system
            data: Data to store in the genesis block
            
        Returns:
            Block hash
        """
        block_hash = hashlib.md5(f"{system_id}:{time.time()}:{data}".encode()).hexdigest()
        
        self.genesis_blocks[system_id] = {
            "hash": block_hash,
            "data": data,
            "timestamp": time.time()
        }
        
        self.blocks[block_hash] = {
            "type": "genesis",
            "system_id": system_id,
            "data": data,
            "timestamp": time.time(),
            "previous_hash": None
        }
        
        logger.info(f"Stored genesis block for system {system_id} with hash {block_hash}")
        return block_hash
    
    def store_block(self, system_id: str, data: Dict[str, Any], previous_hash: str) -> str:
        """Store a block in the blockchain.
        
        Args:
            system_id: ID of the system
            data: Data to store in the block
            previous_hash: Hash of the previous block
            
        Returns:
            Block hash
        """
        block_hash = hashlib.md5(f"{system_id}:{time.time()}:{data}:{previous_hash}".encode()).hexdigest()
        
        self.blocks[block_hash] = {
            "type": "standard",
            "system_id": system_id,
            "data": data,
            "timestamp": time.time(),
            "previous_hash": previous_hash
        }
        
        self.transaction_count += 1
        logger.info(f"Stored block for system {system_id} with hash {block_hash}")
        
        return block_hash
    
    def get_block(self, block_hash: str) -> Optional[Dict[str, Any]]:
        """Get a block by hash.
        
        Args:
            block_hash: Hash of the block to get
            
        Returns:
            Block data or None if not found
        """
        return self.blocks.get(block_hash)
    
    def get_genesis_block(self, system_id: str) -> Optional[Dict[str, Any]]:
        """Get the genesis block for a system.
        
        Args:
            system_id: ID of the system
            
        Returns:
            Genesis block or None if not found
        """
        return self.genesis_blocks.get(system_id)
    
    def verify_blockchain(self, system_id: str) -> bool:
        """Verify the blockchain for a system.
        
        Args:
            system_id: ID of the system
            
        Returns:
            True if blockchain is valid, False otherwise
        """
        # In this mock implementation, always return True
        logger.info(f"Verified blockchain for system {system_id}")
        return True


# Export the mock classes to make them available as system modules
import sys
sys.modules["quantum_nodular_network"] = sys.modules[__name__]
sys.modules["quantum_node_discovery"] = sys.modules[__name__]
sys.modules["quantum_blockchain_connector"] = sys.modules[__name__]

# Demonstration function
def demonstrate_mock_nodular():
    """Demonstrate mock nodular components."""
    print("\n=== Mock Quantum Nodular Components Demonstration ===")
    
    # Create nodular network
    print("\nCreating Quantum Nodular Network...")
    network = QuantumNodularNetwork()
    
    # Create discovery service
    print("\nInitializing Node Discovery Service...")
    discovery = QuantumNodeDiscovery()
    
    # Create test nodes
    print("\nCreating test quantum nodes...")
    nodes = []
    for i in range(3):
        node_id = f"test_node_{i+1}"
        node_type = ["reasoning", "memory", "perception"][i % 3]
        capabilities = [f"{node_type}_core", "phi_harmonic", "meta_aware"]
        
        # Create node in network
        node = network.create_node(node_id, node_type, capabilities)
        nodes.append(node)
        
        # Register node with discovery service
        discovery.register_node(node_type, node)
        
        print(f"Created and registered node: {node_id} ({node_type})")
    
    # Connect nodes
    print("\nConnecting nodes...")
    network.connect_nodes("test_node_1", "test_node_2")
    network.connect_nodes("test_node_2", "test_node_3")
    network.connect_nodes("test_node_3", "test_node_1")
    
    # Test node discovery
    print("\nTesting node discovery...")
    reasoning_nodes = discovery.discover_nodes_by_capability("reasoning_core")
    print(f"Found {len(reasoning_nodes)} reasoning nodes")
    
    memory_nodes = discovery.discover_nodes_by_capability("memory_core")
    print(f"Found {len(memory_nodes)} memory nodes")
    
    # Create blockchain connector
    print("\nCreating Blockchain Connector...")
    blockchain = QuantumBlockchainConnector()
    
    # Store genesis block
    print("\nStoring genesis block...")
    genesis_data = {
        "nodes": [node["id"] for node in nodes],
        "timestamp": time.time(),
        "phi_resonance": network.phi_resonance
    }
    genesis_hash = blockchain.store_genesis_block("test_system", genesis_data)
    print(f"Genesis block stored with hash: {genesis_hash}")
    
    # Store additional block
    print("\nStoring additional block...")
    block_data = {
        "action": "node_update",
        "node_id": "test_node_1",
        "coherence": 0.85,
        "timestamp": time.time()
    }
    block_hash = blockchain.store_block("test_system", block_data, genesis_hash)
    print(f"Block stored with hash: {block_hash}")
    
    # Verify blockchain
    print("\nVerifying blockchain...")
    is_valid = blockchain.verify_blockchain("test_system")
    print(f"Blockchain valid: {is_valid}")
    
    print("\nMock Quantum Nodular Components demonstration complete.")


if __name__ == "__main__":
    demonstrate_mock_nodular()
