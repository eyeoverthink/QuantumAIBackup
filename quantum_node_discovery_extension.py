#!/usr/bin/env python3
"""
Quantum Node Discovery Extension
-------------------------------

This module extends the QuantumNodeDiscovery class to fix node registration and discovery issues.
It ensures proper node registration and discovery in the quantum collective intelligence system.

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
logger = logging.getLogger("QuantumNodeDiscoveryExtension")

# Import required modules
try:
    from quantum_nodular_discovery import QuantumNodeDiscovery
except ImportError as e:
    logger.error(f"Failed to import required modules: {e}")
    raise

class QuantumNodeDiscoveryExtension:
    """Extension for QuantumNodeDiscovery to fix node registration and discovery."""
    
    @staticmethod
    def apply_extension():
        """
        Apply the extension to the QuantumNodeDiscovery class.
        
        This enhances the discover_nodes method to ensure it properly refreshes the node registry
        and finds all registered nodes.
        """
        # Store original methods for reference
        original_discover_nodes = QuantumNodeDiscovery.discover_nodes
        original_find_nodes_by_capability = QuantumNodeDiscovery.find_nodes_by_capability
        
        # Define enhanced discover_nodes implementation
        def enhanced_discover_nodes(self, node_type: str = None, refresh_cache: bool = False) -> List[Dict[str, Any]]:
            """
            Enhanced discover_nodes method to ensure proper node discovery.
            
            Args:
                node_type: Optional node type filter
                refresh_cache: Whether to refresh the cache
                
            Returns:
                List[Dict[str, Any]]: List of discovered nodes
            """
            # Always refresh cache if requested
            if refresh_cache:
                logger.info("Refreshing node registry from blockchain")
                self._refresh_node_registry()
            
            # Debug output current registry state
            logger.info(f"Node registry contains {len(self.node_registry)} nodes")
            for ref_id, node_info in self.node_registry.items():
                metadata = node_info.get('metadata', {})
                node_id = metadata.get('node_id', 'unknown')
                node_type_value = metadata.get('node_type', 'unknown')
                capabilities = metadata.get('capabilities', [])
                logger.info(f"Registry node: {node_id} (type: {node_type_value}, ref: {ref_id}, capabilities: {capabilities})")
            
            # Get all nodes from registry
            nodes = []
            for reference_id, node_info in self.node_registry.items():
                # Extract node data and metadata
                node_data = node_info.get('data', {})
                metadata = node_info.get('metadata', {})
                
                # Check if node matches the type filter based on node_type or capabilities
                node_type_match = node_type is None
                
                # Check node_type in metadata
                if not node_type_match and 'node_type' in metadata:
                    if metadata['node_type'] == node_type:
                        node_type_match = True
                
                # Check capabilities in metadata
                if not node_type_match and 'capabilities' in metadata:
                    capabilities = metadata['capabilities']
                    if isinstance(capabilities, list) and node_type in capabilities:
                        node_type_match = True
                
                # If node matches, add to result list
                if node_type_match:
                    # Create a complete node representation
                    complete_node = {
                        'data': node_data,
                        'metadata': metadata.copy(),  # Copy to avoid modifying original
                        'reference_id': reference_id
                    }
                    
                    # Add node to result list
                    nodes.append(complete_node)
                    logger.info(f"Found matching node: {metadata.get('node_id', 'unknown')} for type/capability: {node_type}")
            
            logger.info(f"Discovered {len(nodes)} nodes" + (f" of type/capability {node_type}" if node_type else ""))
            return nodes
        
        # Define enhanced _refresh_node_registry implementation
        def enhanced_refresh_node_registry(self):
            """
            Enhanced _refresh_node_registry method to ensure all nodes are properly loaded.
            """
            logger.info("Refreshing node registry from blockchain")
            
            # First, preserve any nodes that were registered in the current session
            # These might not be in the blockchain yet or might have different reference IDs
            current_session_nodes = {}
            for ref_id, node_data in self.node_registry.items():
                if isinstance(node_data, dict) and "data" in node_data and "metadata" in node_data:
                    node_id = node_data.get("metadata", {}).get("node_id")
                    if node_id:
                        current_session_nodes[node_id] = (ref_id, node_data)
            
            # Query blockchain for nodes
            try:
                # Use metadata_filter to find nodes
                metadata_filter = {"node_type": {"$exists": True}}
                blocks = self.blockchain_connector.search_genesis_blocks(metadata_filter=metadata_filter)
                
                # Debug output for blocks
                logger.info(f"Found {len(blocks) if blocks else 0} blocks in blockchain")
                
                if blocks:
                    # Process blocks from blockchain
                    for block in blocks:
                        reference_id = block.get("id")
                        if reference_id:
                            # Extract node data from block
                            node_data = block.get("data", {})
                            metadata = block.get("metadata", {})
                            
                            # Store in registry
                            self.node_registry[reference_id] = {
                                "data": node_data,
                                "metadata": metadata
                            }
                            
                            # Log found node
                            node_id = metadata.get("node_id")
                            node_type = metadata.get("node_type")
                            if node_id and node_type:
                                logger.info(f"Found node in blockchain: {node_id} (type: {node_type}, ref: {reference_id})")
                
                # If we didn't find any nodes in blockchain, use the current session nodes
                if not blocks or len(blocks) == 0:
                    logger.info("No nodes found in blockchain, using current session nodes")
                    
                    # Re-add current session nodes to registry
                    for node_id, (ref_id, node_data) in current_session_nodes.items():
                        self.node_registry[ref_id] = node_data
                        logger.info(f"Re-added current session node: {node_id} (ref: {ref_id})")
            except Exception as e:
                logger.error(f"Error refreshing node registry: {e}")
                # On error, restore current session nodes
                for node_id, (ref_id, node_data) in current_session_nodes.items():
                    self.node_registry[ref_id] = node_data
                    logger.info(f"Restored current session node after error: {node_id} (ref: {ref_id})")
            
            # Update last discovery timestamp
            self.last_discovery = self._get_timestamp()
            
            # Log final registry state
            logger.info(f"Node registry contains {len(self.node_registry)} nodes after refresh")
        
        # Define enhanced find_nodes_by_capability implementation
        def enhanced_find_nodes_by_capability(self, capability: str, refresh_cache: bool = False) -> List[Dict[str, Any]]:
            """
            Enhanced find_nodes_by_capability method to ensure proper capability-based node discovery.
            
            Args:
                capability: Capability to search for
                refresh_cache: Whether to refresh the cache
                
            Returns:
                List[Dict[str, Any]]: List of discovered nodes with the specified capability
            """
            logger.info(f"Looking for nodes with capability: {capability}")
            
            # Always refresh cache if requested
            if refresh_cache:
                logger.info("Refreshing node registry from blockchain")
                self._refresh_node_registry()
            
            # Debug output current registry state
            logger.info(f"Node registry contains {len(self.node_registry)} nodes")
            for ref_id, node_info in self.node_registry.items():
                metadata = node_info.get('metadata', {})
                node_id = metadata.get('node_id', 'unknown')
                node_type = metadata.get('node_type', 'unknown')
                capabilities = metadata.get('capabilities', [])
                logger.info(f"Registry node: {node_id} (type: {node_type}, ref: {ref_id}, capabilities: {capabilities})")
            
            # Get all nodes from registry with the specified capability
            nodes = []
            for reference_id, node_info in self.node_registry.items():
                # Extract node data and metadata
                node_data = node_info.get('data', {})
                metadata = node_info.get('metadata', {})
                
                # Check if node has the specified capability
                has_capability = False
                
                # Check capabilities in metadata
                if 'capabilities' in metadata:
                    capabilities = metadata['capabilities']
                    
                    # Direct match
                    if isinstance(capabilities, list) and capability in capabilities:
                        has_capability = True
                    
                    # Check for capability format mismatch (e.g., 'reasoning_core' vs 'reasoning')
                    elif isinstance(capabilities, list):
                        # Map of capability transformations
                        capability_map = {
                            "reasoning_core": "reasoning",
                            "knowledge_core": "knowledge",
                            "perception_core": "perception"
                        }
                        
                        # Check if any capability in the list maps to the requested capability
                        for cap in capabilities:
                            if cap == capability:
                                has_capability = True
                                break
                            # Check if this is a core capability that maps to the requested one
                            if cap in capability_map and capability_map[cap] == capability:
                                has_capability = True
                                logger.info(f"Capability match via mapping: {cap} -> {capability}")
                                break
                            # Check reverse mapping
                            reverse_map = {v: k for k, v in capability_map.items()}
                            if cap in reverse_map and reverse_map[cap] == capability:
                                has_capability = True
                                logger.info(f"Capability match via reverse mapping: {cap} -> {capability}")
                                break
                
                # If node has the capability, add to result list
                if has_capability:
                    # Create a complete node representation
                    complete_node = {
                        'data': node_data,
                        'metadata': metadata.copy(),  # Copy to avoid modifying original
                        'reference_id': reference_id
                    }
                    
                    # Add node to result list
                    nodes.append(complete_node)
                    logger.info(f"Found node with capability '{capability}': {metadata.get('node_id', 'unknown')}")
            
            logger.info(f"Discovered {len(nodes)} nodes with capability '{capability}'")
            return nodes
        
        # Apply patches
        QuantumNodeDiscovery.discover_nodes = enhanced_discover_nodes
        QuantumNodeDiscovery._refresh_node_registry = enhanced_refresh_node_registry
        QuantumNodeDiscovery.find_nodes_by_capability = enhanced_find_nodes_by_capability
        
        logger.info("QuantumNodeDiscovery extension applied: enhanced node discovery and capability search")

# Apply extension automatically when imported
try:
    QuantumNodeDiscoveryExtension.apply_extension()
    logger.info("QuantumNodeDiscovery extension automatically applied")
except Exception as e:
    logger.error(f"Failed to apply QuantumNodeDiscovery extension: {e}")
