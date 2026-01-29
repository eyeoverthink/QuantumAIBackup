#!/usr/bin/env python3
"""
Quantum Node Registration Fix
----------------------------

This module fixes the node registration and capability discovery issues
by ensuring capabilities are properly stored in node metadata.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import logging
import functools
from typing import Dict, Any, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumNodeRegistrationFix")

# Import required modules
try:
    from quantum_nodular_discovery import QuantumNodeDiscovery
    from quantum_blockchain_connector import QuantumBlockchainConnector
    from quantum_nodular_blockchain_storage import QuantumBlockchainStorageNode
except ImportError as e:
    logger.error(f"Failed to import required modules: {e}")
    raise

class QuantumNodeRegistrationFix:
    """Fix for node registration and capability discovery issues."""
    
    @staticmethod
    def apply_fix():
        """
        Apply the fix to the QuantumNodeDiscovery class.
        
        This enhances the register_node method to ensure capabilities are properly stored
        in node metadata for discovery.
        """
        # Store original methods for reference
        original_register_node = QuantumNodeDiscovery.register_node
        original_store_node_state = QuantumBlockchainStorageNode.store_node_state
        
        # Define enhanced register_node implementation
        def enhanced_register_node(self, node_type: str, node_data: Dict[str, Any]) -> str:
            """
            Enhanced register_node method to ensure capabilities are properly stored.
            
            Args:
                node_type: Type of the node
                node_data: Node data
                
            Returns:
                str: Blockchain reference ID
            """
            logger.info(f"Enhanced register_node called for {node_type}")
            
            # Ensure node has an ID
            if "node_id" not in node_data:
                node_data["node_id"] = str(uuid.uuid4())
                logger.info(f"Generated node ID: {node_data['node_id']}")
            
            # Extract capabilities from node data
            capabilities = []
            if "capabilities" in node_data:
                capabilities = node_data["capabilities"]
                logger.info(f"Found capabilities in node_data: {capabilities}")
            elif "metadata" in node_data and "capabilities" in node_data["metadata"]:
                capabilities = node_data["metadata"]["capabilities"]
                logger.info(f"Found capabilities in node_data.metadata: {capabilities}")
            
            # Add registration timestamp
            node_data["registration_timestamp"] = self._get_timestamp()
            
            # Create complete metadata
            metadata = {
                "node_type": node_type,
                "node_id": node_data["node_id"],
                "capabilities": capabilities,
                "registration_timestamp": node_data["registration_timestamp"]
            }
            
            # Store node state on blockchain with complete metadata
            try:
                reference_id = self.storage_node.store_node_state(
                    node_type=node_type,
                    node_id=node_data["node_id"],
                    state_data=node_data,
                    metadata=metadata  # Pass explicit metadata
                )
                
                # Add to registry cache with complete metadata
                self.node_registry[reference_id] = {
                    "data": node_data,
                    "metadata": metadata
                }
                
                logger.info(f"Registered {node_type} node with ID {node_data['node_id']} (reference: {reference_id})")
                logger.info(f"Node capabilities: {capabilities}")
                return reference_id
            except Exception as e:
                logger.error(f"Failed to register node: {e}")
                # Try original method as fallback
                return original_register_node(self, node_type, node_data)
        
        # Define enhanced store_node_state implementation
        def enhanced_store_node_state(self, node_type: str, node_id: str, state_data: Dict[str, Any], 
                                    metadata: Dict[str, Any] = None) -> str:
            """
            Enhanced store_node_state method to ensure capabilities are properly stored.
            
            Args:
                node_type: Type of the node
                node_id: Node ID
                state_data: Node state data
                metadata: Additional metadata
                
            Returns:
                str: Blockchain reference ID
            """
            logger.info(f"Enhanced store_node_state called for {node_type} node {node_id}")
            
            # Ensure metadata exists
            if metadata is None:
                metadata = {}
            
            # Add node type and ID to metadata if not present
            if "node_type" not in metadata:
                metadata["node_type"] = node_type
            if "node_id" not in metadata:
                metadata["node_id"] = node_id
            
            # Extract capabilities from state_data if not in metadata
            if "capabilities" not in metadata:
                if "capabilities" in state_data:
                    metadata["capabilities"] = state_data["capabilities"]
                    logger.info(f"Added capabilities to metadata from state_data: {state_data['capabilities']}")
                elif "metadata" in state_data and "capabilities" in state_data["metadata"]:
                    metadata["capabilities"] = state_data["metadata"]["capabilities"]
                    logger.info(f"Added capabilities to metadata from state_data.metadata: {state_data['metadata']['capabilities']}")
            
            # Ensure capabilities is at least an empty list
            if "capabilities" not in metadata:
                metadata["capabilities"] = []
            
            # Call blockchain connector with enhanced metadata
            try:
                # Store genesis block with state data and metadata
                reference_id = self.blockchain_connector.store_genesis_block(
                    data=state_data,
                    metadata=metadata
                )
                
                logger.info(f"Stored {node_type} node {node_id} state with reference {reference_id}")
                logger.info(f"Node metadata: {metadata}")
                
                return reference_id
            except Exception as e:
                logger.error(f"Failed to store node state: {e}")
                # Try original method as fallback
                return original_store_node_state(self, node_type, node_id, state_data)
        
        # Apply patches
        QuantumNodeDiscovery.register_node = enhanced_register_node
        QuantumBlockchainStorageNode.store_node_state = enhanced_store_node_state
        
        logger.info("Applied node registration fix: enhanced register_node and store_node_state methods")

# Apply fix automatically when imported
try:
    import uuid  # Import uuid for node_id generation in enhanced_register_node
    QuantumNodeRegistrationFix.apply_fix()
    logger.info("Node registration fix automatically applied")
except Exception as e:
    logger.error(f"Failed to apply node registration fix: {e}")
