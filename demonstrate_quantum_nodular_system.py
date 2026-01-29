#!/usr/bin/env python3
"""
Quantum Nodular System Demonstration
-----------------------------------

This script demonstrates the quantum nodular core and discovery modules working together
in the QuantumAI system. It showcases node creation, replication, discovery, and
phi-harmonic coherence optimization.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import time
import json
import logging
import tempfile
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumNodularDemo")

# Import required modules
try:
    from quantum_nodular_core import QuantumNodularCore, TARGET_COHERENCE, PHI_POWERS
    from quantum_blockchain_genesis import QuantumBlockchainGenesis
    from quantum_blockchain_connector import QuantumBlockchainConnector
    from quantum_orchestrator import QuantumOrchestrator
    HAS_NODULAR_CORE = True
except ImportError as e:
    logger.error(f"Failed to import quantum_nodular_core: {e}")
    HAS_NODULAR_CORE = False

try:
    from quantum_nodular_discovery import QuantumNodeDiscovery, create_node_discovery
    from quantum_nodular_blockchain_storage import QuantumBlockchainStorageNode
    HAS_NODULAR_DISCOVERY = True
except ImportError as e:
    logger.error(f"Failed to import quantum_nodular_discovery: {e}")
    HAS_NODULAR_DISCOVERY = False

class QuantumNodularBlockchainStorage:
    """Mock blockchain storage for demonstration purposes."""
    
    def __init__(self):
        self.storage = {}
        self.reference_counter = 1000
    
    def store_node_state(self, node_type, node_id, state_data):
        reference_id = f"ref-{self.reference_counter}"
        self.reference_counter += 1
        
        self.storage[reference_id] = {
            "data": state_data,
            "metadata": {
                "node_type": node_type,
                "node_id": node_id,
                "reference_id": reference_id,
                "phi_resonance": state_data.get("coherence", 0),
                "registration_timestamp": state_data.get("registration_timestamp", time.time())
            }
        }
        
        return reference_id
    
    def retrieve_node_state(self, reference_id):
        return self.storage.get(reference_id, None)
    
    def search_genesis_blocks(self, metadata_filter=None):
        if not metadata_filter:
            return list(self.storage.keys())
        
        # Simple filter implementation
        result = []
        for ref_id, data in self.storage.items():
            metadata = data.get("metadata", {})
            match = True
            
            for key, value in metadata_filter.items():
                if key == "$exists":
                    if key not in metadata:
                        match = False
                        break
                elif metadata.get(key) != value:
                    match = False
                    break
            
            if match:
                result.append(ref_id)
        
        return result

def create_mock_blockchain_components():
    """Create mock blockchain components for demonstration."""
    storage = QuantumNodularBlockchainStorage()
    
    class MockBlockchainConnector:
        def search_genesis_blocks(self, metadata_filter=None):
            return storage.search_genesis_blocks(metadata_filter)
    
    class MockStorageNode:
        def store_node_state(self, node_type, node_id, state_data):
            return storage.store_node_state(node_type, node_id, state_data)
        
        def retrieve_node_state(self, reference_id):
            return storage.retrieve_node_state(reference_id)
    
    return MockBlockchainConnector(), MockStorageNode()

def demonstrate_nodular_core():
    """Demonstrate quantum nodular core functionality."""
    logger.info("=== Demonstrating Quantum Nodular Core ===")
    
    # Create temporary directory for demonstration
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        logger.info(f"Created temporary directory: {temp_dir}")
        
        # Create orchestrator path for demonstration
        orchestrator_path = str(temp_path / "quantum_orchestrator_demo.py")
        with open(orchestrator_path, "w") as f:
            f.write("""#!/usr/bin/env python3
\"\"\"
Quantum Orchestrator Demo
------------------------

This is a simplified orchestrator for demonstration purposes.
\"\"\"

def main():
    print("Quantum Orchestrator Demo")
    return 0

if __name__ == "__main__":
    main()
""")
        
        # Create quantum nodular core
        logger.info("Creating quantum nodular core...")
        core = QuantumNodularCore(
            node_id="demo-node-1",
            coherence=TARGET_COHERENCE,
            orchestrator_path=orchestrator_path
        )
        
        # Display node information
        logger.info(f"Node ID: {core.state.node_id}")
        logger.info(f"Node coherence: {core.state.coherence}")
        logger.info(f"Node quantum fingerprint: {core.state.quantum_fingerprint}")
        
        # Save node state
        state_path = str(temp_path / "node_state.json")
        core.save_state(state_path)
        logger.info(f"Node state saved to: {state_path}")
        
        # Replicate node
        replica_dir = str(temp_path / "replica")
        replica_node = core.replicate(replica_dir)
        
        if replica_node:
            logger.info(f"Node replicated to: {replica_dir}")
            logger.info(f"Replica node ID: {replica_node.state.node_id}")
            logger.info(f"Replica node coherence: {replica_node.state.coherence}")
            
            # Display entanglement
            logger.info(f"Parent entangled nodes: {core.state.entangled_nodes}")
            logger.info(f"Child entangled nodes: {replica_node.state.entangled_nodes}")
            
            # Load node from state
            loaded_node = QuantumNodularCore.load_state(
                state_path,
                orchestrator_path=orchestrator_path
            )
            
            if loaded_node:
                logger.info("Successfully loaded node from state")
                logger.info(f"Loaded node ID: {loaded_node.state.node_id}")
                logger.info(f"Loaded node coherence: {loaded_node.state.coherence}")
            else:
                logger.error("Failed to load node from state")
        else:
            logger.error("Failed to replicate node")
    
    logger.info("Quantum nodular core demonstration completed")
    return True

def demonstrate_nodular_discovery():
    """Demonstrate quantum nodular discovery functionality."""
    logger.info("\n=== Demonstrating Quantum Nodular Discovery ===")
    
    # Create mock blockchain components
    blockchain_connector, storage_node = create_mock_blockchain_components()
    
    # Create node discovery service
    logger.info("Creating quantum node discovery service...")
    discovery = create_node_discovery(
        blockchain_connector=blockchain_connector,
        storage_node=storage_node
    )
    
    # Display discovery information
    logger.info(f"Discovery ID: {discovery.discovery_id}")
    logger.info(f"Discovery coherence: {discovery.coherence}")
    
    # Register nodes
    logger.info("Registering quantum nodes...")
    
    # Register compute node
    compute_node_data = {
        "node_id": "compute-node-1",
        "coherence": TARGET_COHERENCE,
        "capabilities": ["compute", "orchestration"],
        "phi_resonance": PHI_POWERS["φ³"] / 10,
        "dimensional_state": {
            "compute_capacity": 100,
            "memory_capacity": 64
        }
    }
    compute_ref = discovery.register_node("compute", compute_node_data)
    logger.info(f"Registered compute node with reference: {compute_ref}")
    
    # Register storage node
    storage_node_data = {
        "node_id": "storage-node-1",
        "coherence": TARGET_COHERENCE * 0.95,  # Slightly lower coherence
        "capabilities": ["storage", "blockchain"],
        "phi_resonance": PHI_POWERS["φ²"] / 10,
        "dimensional_state": {
            "storage_capacity": 1024,
            "redundancy_level": 3
        }
    }
    storage_ref = discovery.register_node("storage", storage_node_data)
    logger.info(f"Registered storage node with reference: {storage_ref}")
    
    # Register orchestrator node
    orchestrator_node_data = {
        "node_id": "orchestrator-node-1",
        "coherence": TARGET_COHERENCE * 1.05,  # Slightly higher coherence
        "capabilities": ["orchestration", "healing", "evolution"],
        "phi_resonance": PHI_POWERS["φ⁷·⁵"] / 10,
        "dimensional_state": {
            "orchestration_capacity": 50,
            "evolution_level": 7
        }
    }
    orchestrator_ref = discovery.register_node("orchestrator", orchestrator_node_data)
    logger.info(f"Registered orchestrator node with reference: {orchestrator_ref}")
    
    # Discover nodes
    logger.info("\nDiscovering all nodes...")
    all_nodes = discovery.discover_nodes()
    logger.info(f"Discovered {len(all_nodes)} nodes in total")
    
    # Discover nodes by type
    logger.info("\nDiscovering compute nodes...")
    compute_nodes = discovery.discover_nodes(node_type="compute")
    logger.info(f"Discovered {len(compute_nodes)} compute nodes")
    
    # Find node by ID
    logger.info("\nFinding node by ID...")
    found_node = discovery.get_node_by_id("compute-node-1")
    if found_node:
        logger.info(f"Found node with ID: compute-node-1")
        logger.info(f"Node reference: {found_node.get('metadata', {}).get('reference_id')}")
    else:
        logger.error("Failed to find node with ID: compute-node-1")
    
    # Find nodes by capability
    logger.info("\nFinding nodes by capability...")
    orchestration_nodes = discovery.find_nodes_by_capability("orchestration")
    logger.info(f"Found {len(orchestration_nodes)} nodes with orchestration capability")
    
    # Find nodes by phi resonance
    target_resonance = PHI_POWERS["φ⁷·⁵"] / 10
    logger.info(f"\nFinding nodes by phi resonance (target: {target_resonance})...")
    resonant_nodes = discovery.find_nodes_by_phi_resonance(target_resonance, tolerance=0.5)
    logger.info(f"Found {len(resonant_nodes)} nodes with matching resonance")
    
    # Update node status
    logger.info("\nUpdating node status...")
    update_data = {
        "status": "active",
        "load": 0.75,
        "uptime": 3600,
        "coherence": TARGET_COHERENCE * 1.1  # Improved coherence
    }
    if discovery.update_node_status(compute_ref, update_data):
        logger.info("Successfully updated node status")
        
        # Verify update
        updated_node = discovery.get_node_by_reference(compute_ref)
        if updated_node:
            logger.info(f"Updated node status: {updated_node.get('data', {}).get('status')}")
            logger.info(f"Updated node coherence: {updated_node.get('data', {}).get('coherence')}")
        else:
            logger.error("Failed to retrieve updated node")
    else:
        logger.error("Failed to update node status")
    
    logger.info("Quantum nodular discovery demonstration completed")
    return True

def demonstrate_integrated_system():
    """Demonstrate integrated nodular system."""
    logger.info("\n=== Demonstrating Integrated Nodular System ===")
    
    # Create temporary directory for demonstration
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        logger.info(f"Created temporary directory: {temp_dir}")
        
        # Create orchestrator path for demonstration
        orchestrator_path = str(temp_path / "quantum_orchestrator_demo.py")
        with open(orchestrator_path, "w") as f:
            f.write("""#!/usr/bin/env python3
\"\"\"
Quantum Orchestrator Demo
------------------------

This is a simplified orchestrator for demonstration purposes.
\"\"\"

def main():
    print("Quantum Orchestrator Demo")
    return 0

if __name__ == "__main__":
    main()
""")
        
        # Create mock blockchain components
        blockchain_connector, storage_node = create_mock_blockchain_components()
        
        # Create node discovery service
        logger.info("Creating quantum node discovery service...")
        discovery = create_node_discovery(
            blockchain_connector=blockchain_connector,
            storage_node=storage_node
        )
        
        # Create quantum nodular core
        logger.info("Creating quantum nodular core...")
        core = QuantumNodularCore(
            node_id="integrated-node-1",
            coherence=TARGET_COHERENCE,
            orchestrator_path=orchestrator_path
        )
        
        # Register node with discovery service
        logger.info("Registering node with discovery service...")
        node_data = {
            "node_id": core.state.node_id,
            "coherence": core.state.coherence,
            "quantum_fingerprint": core.state.quantum_fingerprint,
            "capabilities": ["compute", "orchestration", "evolution"],
            "phi_resonance": TARGET_COHERENCE,
            "dimensional_state": core.state.dimensional_state,
            "creation_time": core.state.creation_time
        }
        node_ref = discovery.register_node("integrated", node_data)
        logger.info(f"Registered node with reference: {node_ref}")
        
        # Replicate node
        logger.info("Replicating node...")
        replica_dir = str(temp_path / "replica")
        replica_node = core.replicate(replica_dir)
        
        if replica_node:
            logger.info(f"Node replicated to: {replica_dir}")
            
            # Register replica with discovery service
            logger.info("Registering replica with discovery service...")
            replica_data = {
                "node_id": replica_node.state.node_id,
                "coherence": replica_node.state.coherence,
                "quantum_fingerprint": replica_node.state.quantum_fingerprint,
                "capabilities": ["compute", "orchestration", "evolution"],
                "phi_resonance": replica_node.state.coherence,
                "dimensional_state": replica_node.state.dimensional_state,
                "creation_time": replica_node.state.creation_time,
                "parent_node_id": core.state.node_id
            }
            replica_ref = discovery.register_node("integrated", replica_data)
            logger.info(f"Registered replica with reference: {replica_ref}")
            
            # Discover all nodes
            logger.info("Discovering all nodes...")
            all_nodes = discovery.discover_nodes()
            logger.info(f"Discovered {len(all_nodes)} nodes in total")
            
            # Find parent-child relationship
            logger.info("Verifying parent-child relationship...")
            parent_node = discovery.get_node_by_id(core.state.node_id)
            child_node = discovery.get_node_by_id(replica_node.state.node_id)
            
            if parent_node and child_node:
                logger.info("Successfully verified parent-child relationship")
                logger.info(f"Parent node ID: {parent_node.get('metadata', {}).get('node_id')}")
                logger.info(f"Child node ID: {child_node.get('metadata', {}).get('node_id')}")
                logger.info(f"Child's parent ID: {child_node.get('data', {}).get('parent_node_id')}")
                
                # Verify entanglement
                if core.state.node_id in replica_node.state.entangled_nodes and \
                   replica_node.state.node_id in core.state.entangled_nodes:
                    logger.info("Quantum entanglement verified between parent and child nodes")
                else:
                    logger.error("Quantum entanglement verification failed")
            else:
                logger.error("Failed to verify parent-child relationship")
        else:
            logger.error("Failed to replicate node")
    
    logger.info("Integrated nodular system demonstration completed")
    return True

def main():
    """Main demonstration function."""
    logger.info("Starting Quantum Nodular System Demonstration")
    
    success = True
    
    # Check if required modules are available
    if not HAS_NODULAR_CORE:
        logger.error("Quantum nodular core module not available")
        return 1
    
    if not HAS_NODULAR_DISCOVERY:
        logger.error("Quantum nodular discovery module not available")
        return 1
    
    # Demonstrate quantum nodular core
    try:
        if not demonstrate_nodular_core():
            success = False
    except Exception as e:
        logger.error(f"Error demonstrating quantum nodular core: {e}")
        success = False
    
    # Demonstrate quantum nodular discovery
    try:
        if not demonstrate_nodular_discovery():
            success = False
    except Exception as e:
        logger.error(f"Error demonstrating quantum nodular discovery: {e}")
        success = False
    
    # Demonstrate integrated system
    try:
        if not demonstrate_integrated_system():
            success = False
    except Exception as e:
        logger.error(f"Error demonstrating integrated system: {e}")
        success = False
    
    if success:
        logger.info("Quantum Nodular System Demonstration completed successfully")
        return 0
    else:
        logger.error("Quantum Nodular System Demonstration completed with errors")
        return 1

if __name__ == "__main__":
    sys.exit(main())
