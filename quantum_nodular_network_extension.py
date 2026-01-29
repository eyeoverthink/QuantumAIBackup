#!/usr/bin/env python3
"""
Quantum Nodular Network Extension
--------------------------------

This module extends the QuantumNodularNetwork class to fix the interface
with QuantumNodeDiscovery.register_node() method, ensuring proper node registration.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import logging
import json
import os
import uuid
from typing import Dict, Any, List, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumNodularNetworkExtension")

# Import required modules
try:
    from quantum_collective_nodular_integration import QuantumNodularNetwork
except ImportError as e:
    logger.error(f"Failed to import required modules: {e}")
    raise

class QuantumNodularNetworkExtension:
    """Extension for QuantumNodularNetwork to fix node registration."""
    
    @staticmethod
    def apply_extension():
        """
        Apply the extension to the QuantumNodularNetwork class.
        
        This completely replaces the create_node method to properly register nodes with the discovery service.
        """
        # Define completely new implementation
        def new_create_node(self, capabilities=None, orchestrator_path=None, blockchain_reference=None):
            """
            Create a quantum nodular reasoning core.
            
            Args:
                capabilities: Node capabilities
                orchestrator_path: Path to quantum orchestrator
                blockchain_reference: Blockchain reference ID
                
            Returns:
                QuantumNodularReasoningCore: Created node
            """
            # Import here to avoid circular imports
            from quantum_collective_nodular_integration import QuantumNodularReasoningCore
            
            # Create node
            node = QuantumNodularReasoningCore(
                capabilities=capabilities,
                orchestrator_path=orchestrator_path,
                blockchain_reference=blockchain_reference
            )
            
            # Store node in network
            self.nodes[node.core.state.node_id] = node
            
            # Register with discovery service if available
            if hasattr(self, 'discovery_service') and self.discovery_service:
                # Determine node type based on capabilities
                node_type = "quantum_nodular_core"
                if capabilities and "reasoning" in capabilities:
                    node_type = "reasoning_core"
                
                # Log registration attempt
                logger.info(f"Registering node with discovery service: {node_type} with capabilities {capabilities}")
                
                # Create node data structure
                node_data = {
                    "node_id": node.state.node_id if hasattr(node, 'state') and hasattr(node.state, 'node_id') else str(uuid.uuid4()),
                    "node_type": node_type,
                    "data": {
                        "coherence": node.core.state.coherence if hasattr(node, 'core') and hasattr(node.core, 'state') else 3.6932381,
                        "frequency": 29.9524,  # Default phi-harmonic frequency
                        "state": "active"  # Default state
                    },
                    "metadata": {
                        "capabilities": self._normalize_capabilities(capabilities) if capabilities else []
                    },
                    # Add explicit capability flags for discovery
                    "reasoning_enabled": "reasoning" in capabilities if capabilities else False,
                    "knowledge_enabled": "knowledge" in capabilities if capabilities else False,
                    "perception_enabled": "perception" in capabilities if capabilities else False
                }
                
                # Register with discovery service
                try:
                    self.discovery_service.register_node(node_type, node_data)
                    logger.info(f"Successfully registered node {node_data['node_id']} with discovery service")
                except Exception as e:
                    logger.error(f"Failed to register node with discovery service: {e}")
                    # Continue even if registration fails
                
                # Register node with both required parameters
                logger.info(f"Registering node of type '{node_type}' with discovery service")
                self.discovery_service.register_node(node_type=node_type, node_data=node_data)
            
            logger.info(f"Created quantum nodular core with ID {node.core.state.node_id}")
            return node
        
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
            
        # Apply patch
        QuantumNodularNetwork.create_node = new_create_node
        QuantumNodularNetwork._normalize_capabilities = _normalize_capabilities
        logger.info("QuantumNodularNetwork extension applied: fixed node registration interface")

# Apply extension automatically when imported
try:
    QuantumNodularNetworkExtension.apply_extension()
    logger.info("QuantumNodularNetwork extension automatically applied")
except Exception as e:
    logger.error(f"Failed to apply QuantumNodularNetwork extension: {e}")
