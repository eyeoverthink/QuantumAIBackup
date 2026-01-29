#!/usr/bin/env python3
"""
Test Quantum Node Registration with Blockchain
--------------------------------------------

This script tests the complete node registration and discovery pipeline,
focusing on the blockchain registry and node matching logic.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import json
import logging
import uuid
from typing import Dict, Any, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumNodeRegistrationTest")

# Import required modules
try:
    # Import extensions first to ensure they're applied
    import quantum_blockchain_connector_extension
    import quantum_node_discovery_extension
    import quantum_nodular_network_extension
    import quantum_node_registration_fix  # Import the new fix
    
    # Now import the main modules
    from quantum_nodular_discovery import QuantumNodeDiscovery, create_node_discovery
    from quantum_blockchain_connector import QuantumBlockchainConnector
    from quantum_nodular_blockchain_storage import QuantumBlockchainStorageNode
    from quantum_collective_nodular_integration import (
        QuantumNodularNetwork, 
        QuantumNodularReasoningCore,
        create_quantum_collective_intelligence
    )
    
except ImportError as e:
    logger.error(f"Failed to import required modules: {e}")
    raise

def test_node_registration_direct():
    """Test direct node registration with discovery service."""
    logger.info("=== Testing Direct Node Registration ===")
    
    # Create blockchain connector
    blockchain_connector = QuantumBlockchainConnector()
    
    # Create storage node
    storage_node = QuantumBlockchainStorageNode(blockchain_connector=blockchain_connector)
    
    # Create discovery service
    discovery = create_node_discovery(
        blockchain_connector=blockchain_connector,
        storage_node=storage_node
    )
    
    # Create node data
    node_id = str(uuid.uuid4())
    node_type = "test_node"
    node_data = {
        "node_id": node_id,
        "coherence": 3.693238,
        "capabilities": ["reasoning", "knowledge"],
        "metadata": {
            "capabilities": ["reasoning", "knowledge"],
            "phi_resonance": 0.618034
        }
    }
    
    # Register node
    logger.info(f"Registering node with ID {node_id}")
    reference_id = discovery.register_node(node_type=node_type, node_data=node_data)
    
    # Verify registration
    logger.info(f"Node registered with reference ID: {reference_id}")
    
    # Discover nodes
    logger.info("Discovering all nodes")
    nodes = discovery.discover_nodes(refresh_cache=True)
    logger.info(f"Discovered {len(nodes)} nodes")
    
    # Find node by ID
    logger.info(f"Finding node by ID {node_id}")
    found_node = discovery.get_node_by_id(node_id, refresh_cache=True)
    
    if found_node:
        logger.info(f"Found node: {found_node.get('metadata', {}).get('node_id')}")
    else:
        logger.error(f"Node with ID {node_id} not found")
    
    # Find node by capability
    logger.info("Finding nodes with 'reasoning' capability")
    reasoning_nodes = discovery.find_nodes_by_capability("reasoning")
    logger.info(f"Found {len(reasoning_nodes)} nodes with 'reasoning' capability")
    
    # Print found nodes
    for node in reasoning_nodes:
        node_id = node.get("metadata", {}).get("node_id", "unknown")
        capabilities = node.get("metadata", {}).get("capabilities", [])
        logger.info(f"Node {node_id} has capabilities: {capabilities}")
    
    return len(reasoning_nodes) > 0

def test_node_registration_through_network():
    """Test node registration through quantum nodular network."""
    logger.info("=== Testing Node Registration Through Network ===")
    
    # Create blockchain connector
    blockchain_connector = QuantumBlockchainConnector()
    
    # Create storage node
    storage_node = QuantumBlockchainStorageNode(blockchain_connector=blockchain_connector)
    
    # Create discovery service
    discovery = create_node_discovery(
        blockchain_connector=blockchain_connector,
        storage_node=storage_node
    )
    
    # Create nodular network
    network = QuantumNodularNetwork(discovery_service=discovery)
    
    # Create node with capabilities
    logger.info("Creating node with reasoning capability")
    node = network.create_node(capabilities=["reasoning"])
    
    # Get node ID
    node_id = node.core.state.node_id
    logger.info(f"Created node with ID {node_id}")
    
    # Discover nodes
    logger.info("Discovering all nodes")
    nodes = discovery.discover_nodes(refresh_cache=True)
    logger.info(f"Discovered {len(nodes)} nodes")
    
    # Find node by capability
    logger.info("Finding nodes with 'reasoning' capability")
    reasoning_nodes = discovery.find_nodes_by_capability("reasoning")
    logger.info(f"Found {len(reasoning_nodes)} nodes with 'reasoning' capability")
    
    # Print found nodes
    for node in reasoning_nodes:
        node_id = node.get("metadata", {}).get("node_id", "unknown")
        capabilities = node.get("metadata", {}).get("capabilities", [])
        logger.info(f"Node {node_id} has capabilities: {capabilities}")
    
    return len(reasoning_nodes) > 0

def test_blockchain_registry():
    """Test blockchain registry for node storage and retrieval."""
    logger.info("=== Testing Blockchain Registry ===")
    
    # Create blockchain connector
    blockchain_connector = QuantumBlockchainConnector()
    
    # Create storage node
    storage_node = QuantumBlockchainStorageNode(blockchain_connector=blockchain_connector)
    
    # Create node data
    node_id = str(uuid.uuid4())
    node_type = "test_node"
    node_data = {
        "node_id": node_id,
        "coherence": 3.693238,
        "capabilities": ["reasoning", "knowledge"],
        "metadata": {
            "capabilities": ["reasoning", "knowledge"],
            "phi_resonance": 0.618034
        }
    }
    
    # Store node state
    logger.info(f"Storing node state for node {node_id}")
    reference_id = storage_node.store_node_state(
        node_type=node_type,
        node_id=node_id,
        state_data=node_data
    )
    
    logger.info(f"Node state stored with reference ID: {reference_id}")
    
    # Retrieve node state
    logger.info(f"Retrieving node state for reference ID {reference_id}")
    retrieved_data = storage_node.retrieve_node_state(reference_id)
    
    if retrieved_data:
        retrieved_node_id = retrieved_data.get("data", {}).get("node_id", "unknown")
        logger.info(f"Retrieved node state for node {retrieved_node_id}")
        
        # Verify data
        if retrieved_node_id == node_id:
            logger.info("Node data retrieved successfully")
        else:
            logger.error(f"Node ID mismatch: expected {node_id}, got {retrieved_node_id}")
    else:
        logger.error(f"Failed to retrieve node state for reference ID {reference_id}")
    
    return retrieved_data is not None

def test_capability_discovery():
    """Test discovery of nodes by capability."""
    logger.info("=== Testing Capability Discovery ===")
    
    # Create blockchain connector
    blockchain_connector = QuantumBlockchainConnector()
    
    # Create storage node
    storage_node = QuantumBlockchainStorageNode(blockchain_connector=blockchain_connector)
    
    # Create discovery service
    discovery = create_node_discovery(
        blockchain_connector=blockchain_connector,
        storage_node=storage_node
    )
    
    # Create nodes with different capabilities
    capabilities_list = [
        ["reasoning"],
        ["knowledge"],
        ["perception"],
        ["reasoning", "knowledge"],
        ["reasoning", "perception"],
        ["knowledge", "perception"],
        ["reasoning", "knowledge", "perception"]
    ]
    
    # Register nodes
    for i, capabilities in enumerate(capabilities_list):
        node_id = f"test-node-{i}-{uuid.uuid4()}"
        node_type = "test_node"
        node_data = {
            "node_id": node_id,
            "coherence": 3.693238,
            "capabilities": capabilities,
            "metadata": {
                "capabilities": capabilities,
                "phi_resonance": 0.618034
            }
        }
        
        logger.info(f"Registering node {node_id} with capabilities {capabilities}")
        reference_id = discovery.register_node(node_type=node_type, node_data=node_data)
        logger.info(f"Node registered with reference ID: {reference_id}")
    
    # Discover nodes by capability
    capabilities_to_test = ["reasoning", "knowledge", "perception"]
    
    for capability in capabilities_to_test:
        logger.info(f"Finding nodes with '{capability}' capability")
        nodes = discovery.find_nodes_by_capability(capability)
        logger.info(f"Found {len(nodes)} nodes with '{capability}' capability")
        
        # Print found nodes
        for node in nodes:
            node_id = node.get("metadata", {}).get("node_id", "unknown")
            node_capabilities = node.get("metadata", {}).get("capabilities", [])
            logger.info(f"Node {node_id} has capabilities: {node_capabilities}")
    
    return True

def test_collective_intelligence_creation():
    """Test creation of collective intelligence with registered nodes."""
    logger.info("=== Testing Collective Intelligence Creation ===")
    
    # Create quantum collective intelligence
    integration = create_quantum_collective_intelligence(num_nodes=5)
    
    # Get network
    network = integration.network
    
    # Get discovery service
    discovery = network.discovery_service
    
    # Discover nodes
    logger.info("Discovering all nodes")
    nodes = discovery.discover_nodes(refresh_cache=True)
    logger.info(f"Discovered {len(nodes)} nodes")
    
    # Find nodes by capability
    logger.info("Finding nodes with 'reasoning' capability")
    reasoning_nodes = discovery.find_nodes_by_capability("reasoning")
    logger.info(f"Found {len(reasoning_nodes)} nodes with 'reasoning' capability")
    
    # Process reasoning task
    logger.info("Processing reasoning task")
    result = integration.process_reasoning_task(
        query="What is the phi-harmonic resonance of quantum computing?",
        context={"complexity": "high", "domain": "quantum"}
    )
    
    logger.info(f"Reasoning result: {result}")
    
    return len(reasoning_nodes) > 0

def run_all_tests():
    """Run all tests."""
    tests = [
        test_blockchain_registry,
        test_node_registration_direct,
        test_node_registration_through_network,
        test_capability_discovery,
        test_collective_intelligence_creation
    ]
    
    results = []
    
    for test in tests:
        try:
            logger.info(f"Running test: {test.__name__}")
            result = test()
            results.append((test.__name__, result))
            logger.info(f"Test {test.__name__} {'passed' if result else 'failed'}")
        except Exception as e:
            logger.error(f"Test {test.__name__} failed with error: {e}")
            results.append((test.__name__, False))
    
    # Print summary
    logger.info("=== Test Summary ===")
    for test_name, result in results:
        logger.info(f"{test_name}: {'PASS' if result else 'FAIL'}")
    
    # Overall result
    overall = all(result for _, result in results)
    logger.info(f"Overall result: {'PASS' if overall else 'FAIL'}")
    
    return overall

if __name__ == "__main__":
    run_all_tests()
