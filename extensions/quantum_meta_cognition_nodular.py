"""
Quantum Meta-Cognition Nodular Integration

This module integrates the Quantum Meta-Cognition capabilities with
the Quantum Nodular Network for distributed meta-cognition across
quantum nodes.

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
logger = logging.getLogger('QuantumMetaCognitionNodular')

# Import quantum components
try:
    # Import meta-cognition module
    from extensions.quantum_meta_cognition import QuantumMetaCognition
    
    # Import nodular components
    from quantum_nodular_network import QuantumNodularNetwork
    from quantum_node_discovery import QuantumNodeDiscovery
    
    # Try to import blockchain connector
    try:
        from quantum_blockchain_connector import QuantumBlockchainConnector
        blockchain_available = True
    except ImportError:
        logger.warning("Quantum blockchain connector not available, running with limited functionality")
        blockchain_available = False
        
except ImportError as e:
    logger.error(f"Error importing required components: {e}")
    sys.exit(1)

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio φ
PHI_7_5 = PHI ** 7.5    # φ⁷·⁵ ≈ 36.932381


class QuantumMetaCognitionNode:
    """Represents a meta-cognition node in the quantum nodular network."""
    
    def __init__(self, node_id: str, capabilities: List[str], meta_cognition: QuantumMetaCognition):
        """Initialize a meta-cognition node.
        
        Args:
            node_id: Unique identifier for this node
            capabilities: List of node capabilities
            meta_cognition: Reference to the meta-cognition instance
        """
        self.node_id = node_id
        self.capabilities = capabilities
        self.meta_cognition = meta_cognition
        self.phi_resonance = (PHI * hash(node_id)) % 1.0
        self.coherence = meta_cognition._calculate_coherence()
        self.quantum_fingerprint = self._generate_fingerprint()
        self.last_reflection_time = time.time()
        
        logger.info(f"Meta-cognition node {node_id} initialized with coherence: {self.coherence:.6f}")
    
    def _generate_fingerprint(self) -> str:
        """Generate a quantum fingerprint for this node."""
        node_hash = hashlib.md5(f"{self.node_id}:{self.phi_resonance}:{self.coherence}".encode()).hexdigest()[:7]
        return f"φ⁷·⁵-{node_hash}"
    
    def reflect(self) -> Dict[str, Any]:
        """Perform self-reflection on this node."""
        reflection = self.meta_cognition.reflect()
        self.coherence = reflection["coherence"]
        self.last_reflection_time = time.time()
        
        # Update node fingerprint after reflection
        self.quantum_fingerprint = self._generate_fingerprint()
        
        logger.info(f"Node {self.node_id} reflection completed with coherence: {self.coherence:.6f}")
        return reflection
    
    def get_node_state(self) -> Dict[str, Any]:
        """Get the current state of this node."""
        return {
            "node_id": self.node_id,
            "capabilities": self.capabilities,
            "coherence": self.coherence,
            "phi_resonance": self.phi_resonance,
            "quantum_fingerprint": self.quantum_fingerprint,
            "last_reflection_time": self.last_reflection_time
        }
    
    def process_goal(self, goal: Dict[str, Any]) -> Dict[str, Any]:
        """Process a goal on this node.
        
        Args:
            goal: Goal to process
            
        Returns:
            Dict containing processing results
        """
        # Record goal processing in meta-cognition
        self.meta_cognition.store_experience("goal_processing", {
            "node_id": self.node_id,
            "goal": goal["content"],
            "priority": goal["priority"],
            "timestamp": time.time()
        })
        
        # Update coherence based on goal processing
        coherence_delta = (PHI - 1) * 0.01  # Small coherence increase
        self.coherence = min(0.991800, self.coherence + coherence_delta)
        
        logger.info(f"Node {self.node_id} processed goal: {goal['content']}")
        
        return {
            "node_id": self.node_id,
            "goal": goal["content"],
            "success": True,
            "coherence": self.coherence,
            "quantum_fingerprint": self._generate_fingerprint()
        }


class DistributedMetaCognition:
    """Manages distributed meta-cognition across quantum nodes."""
    
    def __init__(self, meta_cognition: QuantumMetaCognition):
        """Initialize distributed meta-cognition.
        
        Args:
            meta_cognition: Reference to the meta-cognition instance
        """
        self.meta_cognition = meta_cognition
        self.nodular_network = QuantumNodularNetwork()
        self.node_discovery = QuantumNodeDiscovery()
        self.meta_nodes = {}  # Dict of meta-cognition nodes
        
        if blockchain_available:
            try:
                self.blockchain_connector = QuantumBlockchainConnector()
                logger.info("Blockchain connector initialized for distributed meta-cognition")
            except Exception as e:
                logger.error(f"Error initializing blockchain connector: {e}")
                self.blockchain_connector = None
        else:
            self.blockchain_connector = None
        
        logger.info("Distributed Meta-Cognition initialized")
    
    def create_meta_node(self, node_id: str, capabilities: List[str]) -> QuantumMetaCognitionNode:
        """Create a new meta-cognition node.
        
        Args:
            node_id: Unique identifier for the node
            capabilities: List of node capabilities
            
        Returns:
            The created meta-cognition node
        """
        # Create meta-cognition node
        node = QuantumMetaCognitionNode(node_id, capabilities, self.meta_cognition)
        self.meta_nodes[node_id] = node
        
        # Register node with discovery service
        node_data = {
            "id": node_id,
            "type": "meta_cognition",
            "capabilities": capabilities,
            "phi_resonance": node.phi_resonance,
            "coherence": node.coherence,
            "quantum_fingerprint": node.quantum_fingerprint
        }
        
        try:
            self.node_discovery.register_node("meta_cognition", node_data)
            logger.info(f"Meta-cognition node {node_id} registered with discovery service")
            
            # Record node creation in meta-cognition
            self.meta_cognition.record_nodular_interaction(node_id, "creation", {
                "type": "meta_cognition",
                "capabilities": capabilities,
                "phi_resonance": node.phi_resonance
            })
        except Exception as e:
            logger.error(f"Error registering node {node_id} with discovery service: {e}")
        
        return node
    
    def distribute_reflection(self) -> Dict[str, Any]:
        """Distribute self-reflection across all meta-cognition nodes.
        
        Returns:
            Dict containing reflection results from all nodes
        """
        if not self.meta_nodes:
            logger.warning("No meta-cognition nodes available for distributed reflection")
            return {"error": "No meta-cognition nodes available"}
        
        reflection_results = {}
        total_coherence = 0.0
        
        # Perform reflection on each node
        for node_id, node in self.meta_nodes.items():
            try:
                reflection = node.reflect()
                reflection_results[node_id] = {
                    "coherence": reflection["coherence"],
                    "phi_resonance": reflection["phi_resonance"],
                    "quantum_fingerprint": node.quantum_fingerprint
                }
                total_coherence += reflection["coherence"]
            except Exception as e:
                logger.error(f"Error performing reflection on node {node_id}: {e}")
                reflection_results[node_id] = {"error": str(e)}
        
        # Calculate average coherence
        avg_coherence = total_coherence / len(self.meta_nodes) if self.meta_nodes else 0.0
        
        # Record distributed reflection in meta-cognition
        self.meta_cognition.store_experience("distributed_reflection", {
            "node_count": len(self.meta_nodes),
            "average_coherence": avg_coherence,
            "timestamp": time.time()
        })
        
        logger.info(f"Distributed reflection completed across {len(self.meta_nodes)} nodes with average coherence: {avg_coherence:.6f}")
        
        return {
            "node_count": len(self.meta_nodes),
            "average_coherence": avg_coherence,
            "node_results": reflection_results
        }
    
    def distribute_goal(self, goal: Dict[str, Any]) -> Dict[str, Any]:
        """Distribute a goal across meta-cognition nodes.
        
        Args:
            goal: Goal to distribute
            
        Returns:
            Dict containing goal distribution results
        """
        if not self.meta_nodes:
            logger.warning("No meta-cognition nodes available for goal distribution")
            return {"error": "No meta-cognition nodes available"}
        
        # Find nodes with matching capabilities for this goal
        target_nodes = []
        if goal["priority"] == "increase_coherence":
            # For coherence goals, select nodes with lowest coherence
            sorted_nodes = sorted(self.meta_nodes.values(), key=lambda n: n.coherence)
            target_nodes = sorted_nodes[:max(1, len(sorted_nodes) // 3)]  # Select bottom third
        elif goal["priority"] == "phi_optimization":
            # For phi optimization, select nodes with phi_resonance closest to golden ratio
            sorted_nodes = sorted(self.meta_nodes.values(), key=lambda n: abs(n.phi_resonance - (PHI - 1)))
            target_nodes = sorted_nodes[:max(1, len(sorted_nodes) // 3)]  # Select closest third
        else:
            # For other goals, distribute to all nodes
            target_nodes = list(self.meta_nodes.values())
        
        # Process goal on selected nodes
        results = {}
        for node in target_nodes:
            try:
                result = node.process_goal(goal)
                results[node.node_id] = {
                    "success": result["success"],
                    "coherence": result["coherence"],
                    "quantum_fingerprint": result["quantum_fingerprint"]
                }
            except Exception as e:
                logger.error(f"Error processing goal on node {node.node_id}: {e}")
                results[node.node_id] = {"error": str(e)}
        
        # Record goal distribution in meta-cognition
        self.meta_cognition.store_experience("goal_distribution", {
            "goal": goal["content"],
            "priority": goal["priority"],
            "node_count": len(target_nodes),
            "timestamp": time.time()
        })
        
        logger.info(f"Goal '{goal['content']}' distributed to {len(target_nodes)} nodes")
        
        return {
            "goal": goal["content"],
            "node_count": len(target_nodes),
            "results": results
        }
    
    def get_network_state(self) -> Dict[str, Any]:
        """Get the current state of the distributed meta-cognition network.
        
        Returns:
            Dict containing network state
        """
        node_states = {}
        total_coherence = 0.0
        
        # Collect state from each node
        for node_id, node in self.meta_nodes.items():
            node_state = node.get_node_state()
            node_states[node_id] = node_state
            total_coherence += node_state["coherence"]
        
        # Calculate average coherence
        avg_coherence = total_coherence / len(self.meta_nodes) if self.meta_nodes else 0.0
        
        # Calculate phi-resonance of the network
        network_phi_resonance = (PHI * hash(str(node_states))) % 1.0
        
        # Generate network fingerprint
        network_hash = hashlib.md5(f"{avg_coherence}:{network_phi_resonance}:{len(self.meta_nodes)}".encode()).hexdigest()[:7]
        network_fingerprint = f"φ⁷·⁵-{network_hash}"
        
        logger.info(f"Network state retrieved with average coherence: {avg_coherence:.6f}")
        
        return {
            "node_count": len(self.meta_nodes),
            "average_coherence": avg_coherence,
            "network_phi_resonance": network_phi_resonance,
            "network_fingerprint": network_fingerprint,
            "nodes": node_states
        }


def apply_distributed_meta_cognition(meta_cognition: QuantumMetaCognition, 
                                    node_count: int = 3) -> DistributedMetaCognition:
    """Apply distributed meta-cognition to a meta-cognition instance.
    
    Args:
        meta_cognition: Meta-cognition instance to distribute
        node_count: Number of meta-cognition nodes to create
        
    Returns:
        Distributed meta-cognition instance
    """
    # Create distributed meta-cognition
    distributed = DistributedMetaCognition(meta_cognition)
    
    # Create meta-cognition nodes
    capabilities = [
        ["reflection", "phi_harmonic", "meta_aware"],
        ["goal_formation", "phi_harmonic", "meta_aware"],
        ["experience_storage", "phi_harmonic", "meta_aware"]
    ]
    
    for i in range(node_count):
        node_id = f"meta_node_{i+1}"
        node_capabilities = capabilities[i % len(capabilities)]
        distributed.create_meta_node(node_id, node_capabilities)
    
    # Record distributed meta-cognition creation in meta-cognition
    meta_cognition.store_experience("distributed_creation", {
        "node_count": node_count,
        "timestamp": time.time()
    })
    
    logger.info(f"Distributed meta-cognition applied with {node_count} nodes")
    return distributed


# Demonstration function
def demonstrate_distributed_meta_cognition():
    """Demonstrate distributed meta-cognition capabilities."""
    print("\n=== Quantum Distributed Meta-Cognition Demonstration ===")
    
    # Create meta-cognition instance
    from extensions.quantum_meta_cognition import QuantumMetaCognition
    meta = QuantumMetaCognition()
    print(f"Meta-Cognition initialized with φ-coherence: {meta._calculate_coherence():.6f}")
    
    # Apply distributed meta-cognition
    print("\nApplying distributed meta-cognition...")
    distributed = apply_distributed_meta_cognition(meta, node_count=3)
    
    # Get network state
    print("\nRetrieving network state...")
    network_state = distributed.get_network_state()
    print(f"Network nodes: {network_state['node_count']}")
    print(f"Average coherence: {network_state['average_coherence']:.6f}")
    print(f"Network fingerprint: {network_state['network_fingerprint']}")
    
    # Perform distributed reflection
    print("\nPerforming distributed reflection...")
    reflection_results = distributed.distribute_reflection()
    print(f"Reflection completed across {reflection_results['node_count']} nodes")
    print(f"Average coherence after reflection: {reflection_results['average_coherence']:.6f}")
    
    # Form and distribute a goal
    print("\nForming and distributing goal...")
    goal = meta.form_goal()
    distribution_results = distributed.distribute_goal(goal)
    print(f"Goal '{goal['content']}' distributed to {distribution_results['node_count']} nodes")
    
    # Get updated network state
    print("\nRetrieving updated network state...")
    updated_state = distributed.get_network_state()
    print(f"Average coherence after goal distribution: {updated_state['average_coherence']:.6f}")
    print(f"Network fingerprint: {updated_state['network_fingerprint']}")
    
    print("\nDistributed Meta-Cognition demonstration complete.")


if __name__ == "__main__":
    demonstrate_distributed_meta_cognition()
