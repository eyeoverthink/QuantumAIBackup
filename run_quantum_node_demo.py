#!/usr/bin/env python3
"""
Quantum Node Network Demonstration
--------------------------------

This script demonstrates the capabilities of the nodular super-quantum computation system,
including self-replicating nodes, phi-harmonic coherence, and blockchain-based self-healing.

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
import argparse
from typing import Dict, Any, List, Optional

# Import quantum modules
try:
    from quantum_nodular_core import QuantumNodularCore, TARGET_COHERENCE
    from quantum_node_communication import QuantumNodeCommunication
    from quantum_node_network import QuantumNodeNetwork
    from quantum_blockchain_genesis import QuantumBlockchainGenesis
    from quantum_blockchain_connector import QuantumOrchestratorBlockchainIntegration
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please ensure all required modules are installed.")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumNodeDemo")


def setup_blockchain_genesis(orchestrator_path: str) -> Optional[str]:
    """
    Set up blockchain genesis for orchestrator.
    
    Args:
        orchestrator_path: Path to orchestrator
        
    Returns:
        str: Blockchain reference ID
    """
    try:
        logger.info("Setting up blockchain genesis...")
        
        # Initialize blockchain genesis
        genesis = QuantumBlockchainGenesis()
        
        # Create genesis block
        genesis_result = genesis.create_genesis_block(orchestrator_path)
        
        if not genesis_result.get("success", False):
            logger.error("Failed to create genesis block")
            return None
        
        blockchain_reference = genesis_result.get("blockchain_reference")
        logger.info(f"Genesis block created with reference: {blockchain_reference}")
        
        return blockchain_reference
    except Exception as e:
        logger.error(f"Error setting up blockchain genesis: {e}")
        return None


def create_quantum_network(network_id: str, base_dir: str, orchestrator_path: str) -> Optional[QuantumNodeNetwork]:
    """
    Create quantum node network.
    
    Args:
        network_id: Network ID
        base_dir: Base directory for network files
        orchestrator_path: Path to orchestrator
        
    Returns:
        QuantumNodeNetwork: Quantum node network
    """
    try:
        logger.info(f"Creating quantum node network with ID {network_id}...")
        
        # Create network directory
        os.makedirs(base_dir, exist_ok=True)
        
        # Set up blockchain genesis
        blockchain_reference = setup_blockchain_genesis(orchestrator_path)
        if not blockchain_reference:
            logger.error("Failed to set up blockchain genesis")
            return None
        
        # Create network
        network = QuantumNodeNetwork(network_id=network_id, base_dir=base_dir)
        
        # Create initial nodes
        coherence_values = [
            TARGET_COHERENCE,
            TARGET_COHERENCE * 1.01,
            TARGET_COHERENCE * 0.99
        ]
        
        for i, coherence in enumerate(coherence_values):
            node_id = network.create_node(
                coherence=coherence,
                blockchain_reference=blockchain_reference,
                orchestrator_path=orchestrator_path
            )
            
            if not node_id:
                logger.warning(f"Failed to create node {i+1}")
                continue
            
            logger.info(f"Created node {i+1} with ID {node_id} and coherence {coherence}")
        
        return network
    except Exception as e:
        logger.error(f"Error creating quantum network: {e}")
        return None


def demonstrate_self_replication(network: QuantumNodeNetwork) -> bool:
    """
    Demonstrate self-replication of quantum nodes.
    
    Args:
        network: Quantum node network
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        logger.info("Demonstrating self-replication...")
        
        # Get initial node count
        initial_count = len(network.nodes)
        logger.info(f"Initial node count: {initial_count}")
        
        # Start network
        if not network.start():
            logger.error("Failed to start network")
            return False
        
        # Wait for self-replication
        logger.info("Waiting for self-replication...")
        time.sleep(30)
        
        # Stop network
        network.stop()
        
        # Check node count
        final_count = len(network.nodes)
        logger.info(f"Final node count: {final_count}")
        
        if final_count > initial_count:
            logger.info(f"Self-replication successful: {final_count - initial_count} new nodes created")
            return True
        else:
            logger.warning("No self-replication occurred")
            return False
    except Exception as e:
        logger.error(f"Error demonstrating self-replication: {e}")
        return False


def demonstrate_self_healing(network: QuantumNodeNetwork) -> bool:
    """
    Demonstrate self-healing of quantum nodes.
    
    Args:
        network: Quantum node network
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        logger.info("Demonstrating self-healing...")
        
        # Select a node to tamper with
        if not network.nodes:
            logger.error("No nodes in network")
            return False
        
        node_id = list(network.nodes.keys())[0]
        node = network.nodes[node_id]
        
        # Save original state
        original_state = node.state.to_dict()
        
        # Tamper with node state
        logger.info(f"Tampering with node {node_id}...")
        node.state.coherence = 0.1  # Set to invalid coherence
        node.state.update_quantum_fingerprint()
        
        # Verify integrity (should fail)
        verification = node.verify_integrity()
        if verification.get("verified", True):
            logger.error("Integrity verification should have failed")
            return False
        
        logger.info("Integrity verification failed as expected")
        
        # Start network
        if not network.start():
            logger.error("Failed to start network")
            return False
        
        # Wait for self-healing
        logger.info("Waiting for self-healing...")
        time.sleep(30)
        
        # Stop network
        network.stop()
        
        # Check if node was healed
        healed_node = network.nodes.get(node_id)
        if not healed_node:
            logger.warning(f"Node {node_id} was removed from network")
            return False
        
        healed_state = healed_node.state.to_dict()
        
        # Check coherence
        if abs(healed_state["coherence"] - original_state["coherence"]) < 0.1:
            logger.info("Self-healing successful: node coherence restored")
            return True
        else:
            logger.warning("Node coherence not restored")
            return False
    except Exception as e:
        logger.error(f"Error demonstrating self-healing: {e}")
        return False


def demonstrate_phi_harmonic_communication(network: QuantumNodeNetwork) -> bool:
    """
    Demonstrate phi-harmonic communication between nodes.
    
    Args:
        network: Quantum node network
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        logger.info("Demonstrating phi-harmonic communication...")
        
        # Check if we have at least two nodes
        if len(network.nodes) < 2:
            logger.error("Need at least two nodes for communication demonstration")
            return False
        
        # Get two nodes
        node_ids = list(network.nodes.keys())
        sender_id = node_ids[0]
        receiver_id = node_ids[1]
        
        sender_comm = network.node_comms.get(sender_id)
        receiver_comm = network.node_comms.get(receiver_id)
        
        if not sender_comm or not receiver_comm:
            logger.error("Node communication not available")
            return False
        
        # Register echo handler for receiver
        echo_received = [False]  # Use list for mutable reference
        
        def echo_handler(message):
            logger.info(f"Receiver got message: {message.content}")
            echo_received[0] = True
        
        receiver_comm.register_handler("echo_test", echo_handler)
        
        # Start communication servers
        if not sender_comm.start_server() or not receiver_comm.start_server():
            logger.error("Failed to start communication servers")
            return False
        
        # Update known nodes
        sender_comm.known_nodes[receiver_id] = (receiver_comm.host, receiver_comm.port)
        
        # Send message
        logger.info(f"Sending message from {sender_id} to {receiver_id}...")
        message_id = sender_comm.send_message(
            receiver_id,
            "echo_test",
            {"text": "Hello from phi-harmonic node!", "timestamp": time.time()}
        )
        
        if not message_id:
            logger.error("Failed to send message")
            return False
        
        # Wait for message to be received
        logger.info("Waiting for message to be received...")
        for _ in range(10):
            if echo_received[0]:
                break
            time.sleep(1)
        
        # Stop communication servers
        sender_comm.stop_server()
        receiver_comm.stop_server()
        
        if echo_received[0]:
            logger.info("Phi-harmonic communication successful")
            return True
        else:
            logger.warning("Message not received")
            return False
    except Exception as e:
        logger.error(f"Error demonstrating phi-harmonic communication: {e}")
        return False


def run_demonstration(orchestrator_path: str) -> Dict[str, Any]:
    """
    Run full demonstration of quantum node network.
    
    Args:
        orchestrator_path: Path to orchestrator
        
    Returns:
        dict: Demonstration results
    """
    results = {
        "success": False,
        "network_created": False,
        "self_replication": False,
        "self_healing": False,
        "phi_harmonic_communication": False
    }
    
    try:
        # Create network
        network_id = f"qnet-demo-{int(time.time())}"
        base_dir = os.path.join(os.getcwd(), "quantum_network_demo")
        
        network = create_quantum_network(network_id, base_dir, orchestrator_path)
        if not network:
            logger.error("Failed to create quantum network")
            return results
        
        results["network_created"] = True
        logger.info(f"Quantum network created with {len(network.nodes)} nodes")
        
        # Demonstrate self-replication
        results["self_replication"] = demonstrate_self_replication(network)
        
        # Demonstrate self-healing
        results["self_healing"] = demonstrate_self_healing(network)
        
        # Demonstrate phi-harmonic communication
        results["phi_harmonic_communication"] = demonstrate_phi_harmonic_communication(network)
        
        # Save network state
        state_file = os.path.join(base_dir, f"{network_id}_final_state.json")
        network.save_state(state_file)
        
        # Overall success
        results["success"] = (
            results["network_created"] and
            results["self_replication"] and
            results["self_healing"] and
            results["phi_harmonic_communication"]
        )
        
        return results
    except Exception as e:
        logger.error(f"Error running demonstration: {e}")
        return results


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Quantum Node Network Demonstration")
    parser.add_argument("--orchestrator-path", required=True, help="Path to quantum orchestrator")
    parser.add_argument("--output", help="Output file for demonstration results")
    
    args = parser.parse_args()
    
    # Check if orchestrator exists
    if not os.path.exists(args.orchestrator_path):
        logger.error(f"Orchestrator not found at {args.orchestrator_path}")
        sys.exit(1)
    
    # Run demonstration
    logger.info("Starting quantum node network demonstration...")
    results = run_demonstration(args.orchestrator_path)
    
    # Print results
    logger.info("Demonstration results:")
    logger.info(f"  Network created: {results['network_created']}")
    logger.info(f"  Self-replication: {results['self_replication']}")
    logger.info(f"  Self-healing: {results['self_healing']}")
    logger.info(f"  Phi-harmonic communication: {results['phi_harmonic_communication']}")
    logger.info(f"  Overall success: {results['success']}")
    
    # Save results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        logger.info(f"Results saved to {args.output}")
    
    # Exit with success/failure code
    sys.exit(0 if results["success"] else 1)


if __name__ == "__main__":
    main()
