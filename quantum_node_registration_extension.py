#!/usr/bin/env python3
"""
Quantum Node Registration Extension
----------------------------------

This module extends the QuantumNodeDiscovery class to fix node registration issues.
It ensures proper node registration with capabilities in the quantum collective intelligence system.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import logging
import functools
from typing import Dict, Any, List, Optional, Union
import uuid
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumNodeRegistrationExtension")

# Import required modules
try:
    from quantum_nodular_discovery import QuantumNodeDiscovery
except ImportError as e:
    logger.error(f"Failed to import required modules: {e}")
    raise

class QuantumNodeRegistrationExtension:
    """Extension for QuantumNodeDiscovery to fix node registration."""
    
    @staticmethod
    def apply_extension():
        """
        Apply the extension to the QuantumNodeDiscovery class.
        
        This enhances the register_node method to ensure it properly registers nodes
        with capabilities for discovery.
        """
        # Store original method for reference
        original_register_node = QuantumNodeDiscovery.register_node
        
        # Define enhanced register_node implementation
        def enhanced_register_node(self, node_type: str, node_data: Dict[str, Any]) -> str:
            """
            Enhanced register_node method to ensure proper node registration.
            
            Args:
                node_type: Type of node to register
                node_data: Node data to register
                
            Returns:
                str: Reference ID of registered node
            """
            logger.info(f"Registering node of type {node_type}")
            
            # Generate node ID if not provided
            if "node_id" not in node_data:
                node_data["node_id"] = str(uuid.uuid4())
            
            # Extract capabilities from node_data if present
            capabilities = []
            if "capabilities" in node_data:
                capabilities = node_data["capabilities"]
                
            # Ensure node_data has metadata
            if "metadata" not in node_data:
                node_data["metadata"] = {}
            
            # Add node_type and node_id to metadata
            node_data["metadata"]["node_type"] = node_type
            node_data["metadata"]["node_id"] = node_data["node_id"]
            
            # Add capabilities to metadata
            if capabilities:
                node_data["metadata"]["capabilities"] = capabilities
            elif node_type:
                # Use node_type as a default capability
                node_data["metadata"]["capabilities"] = [node_type]
            
            # Store node in blockchain
            try:
                # Store node data to blockchain - adapt to the actual interface
                # First check what parameters store_system_genesis accepts
                import inspect
                sig = inspect.signature(self.blockchain_connector.store_system_genesis)
                params = list(sig.parameters.keys())
                
                # Prepare node data and metadata
                system_data = node_data.get("data", {})
                
                # Prepare node metadata
                # Extract capabilities from node data if available, otherwise use default
                capabilities = node_data.get('capabilities', [])
                if not capabilities and 'core' in node_data:
                    # Try to extract capabilities from core object
                    core = node_data.get('core', {})
                    if hasattr(core, 'capabilities'):
                        capabilities = core.capabilities
                
                # Ensure we have at least the node type as a capability
                if not capabilities:
                    capabilities = [node_type]
                
                # Add individual capabilities from node data if they exist
                if node_data.get('reasoning_enabled', False):
                    capabilities.append('reasoning')
                if node_data.get('knowledge_enabled', False):
                    capabilities.append('knowledge')
                if node_data.get('perception_enabled', False):
                    capabilities.append('perception')
                    
                # Normalize capabilities to match what discovery expects
                capabilities = self._normalize_capabilities(capabilities)
                
                system_metadata = {
                    'node_id': node_data.get('id', str(uuid.uuid4())),
                    'node_type': node_type,
                    'capabilities': capabilities,
                    'timestamp': datetime.now().isoformat(),
                    'phi_coherence': node_data.get('coherence', 0.0),
                    'version': '1.0.0'
                }
                
                # Call store_system_genesis with the right parameters
                if 'data' in params and 'metadata' in params:
                    # If it accepts data and metadata directly
                    reference_id = self.blockchain_connector.store_system_genesis(
                        data=system_data,
                        metadata=system_metadata
                    )
                elif 'system_data' in params and 'metadata' in params:
                    # If it accepts system_data and metadata
                    reference_id = self.blockchain_connector.store_system_genesis(
                        system_data=system_data,
                        metadata=system_metadata
                    )
                elif 'genesis_data' in params:
                    # If it accepts a single genesis_data parameter
                    reference_id = self.blockchain_connector.store_system_genesis(
                        genesis_data={
                            "data": system_data,
                            "metadata": system_metadata
                        }
                    )
                else:
                    # Default approach - create a combined genesis data object
                    genesis_data = {
                        "data": system_data,
                        "metadata": system_metadata
                    }
                    # Pass as a single argument
                    reference_id = self.blockchain_connector.store_system_genesis(genesis_data)
                
                # Store node in registry
                self.node_registry[reference_id] = {
                    "data": node_data.get("data", {}),
                    "metadata": {
                        "node_type": node_type,
                        "node_id": node_data["node_id"],
                        "capabilities": node_data["metadata"]["capabilities"]
                    }
                }
                
                logger.info(f"Registered {node_type} node with ID {node_data['node_id']} (reference: {reference_id})")
                return reference_id
            except Exception as e:
                logger.error(f"Error registering node: {e}")
                raise
        
        # Helper method to normalize capabilities
        def _normalize_capabilities(self, capabilities):
            """
            Normalize capabilities to match what the discovery service expects.
            
            Args:
                capabilities: List of capabilities
                
            Returns:
                List[str]: Normalized capabilities
            """
            if not capabilities:
                return []
                
            # Map of capability transformations
            capability_map = {
                "reasoning_core": "reasoning",
                "knowledge_core": "knowledge",
                "perception_core": "perception"
            }
            
            # Normalize capabilities
            normalized = []
            for cap in capabilities:
                # If the capability is in the map, use the mapped value
                if cap in capability_map:
                    normalized.append(capability_map[cap])
                else:
                    # Otherwise, use the original capability
                    normalized.append(cap)
                    
            logger.info(f"Normalized capabilities: {capabilities} -> {normalized}")
            return normalized
            
        # Apply patches
        QuantumNodeDiscovery.register_node = enhanced_register_node
        QuantumNodeDiscovery._normalize_capabilities = _normalize_capabilities
        
        logger.info("QuantumNodeDiscovery registration extension applied")

# Apply extension automatically when imported
try:
    QuantumNodeRegistrationExtension.apply_extension()
    logger.info("QuantumNodeDiscovery registration extension automatically applied")
except Exception as e:
    logger.error(f"Failed to apply QuantumNodeDiscovery registration extension: {e}")
