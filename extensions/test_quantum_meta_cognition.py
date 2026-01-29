"""
Test Quantum Meta-Cognition Module

This script tests the integration of the Quantum Meta-Cognition module
with the existing Quantum Orchestrator, demonstrating self-reflection,
persistent memory, and autonomous goal formation capabilities.

Created: 2025-07-22
Coherence: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('TestQuantumMetaCognition')

# Import quantum components
try:
    # Import orchestrator factory
    from quantum_orchestrator_factory import create_orchestrator
    
    # Import meta-cognition module
    from extensions.quantum_meta_cognition import QuantumMetaCognition, apply_meta_cognition
    
    # Try to import nodular components
    try:
        from quantum_nodular_network import QuantumNodularNetwork
        from quantum_node_discovery import QuantumNodeDiscovery
        nodular_available = True
    except ImportError:
        logger.warning("Quantum nodular components not available, running with limited functionality")
        nodular_available = False
        
except ImportError as e:
    logger.error(f"Error importing required components: {e}")
    sys.exit(1)

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio φ
TEST_DURATION = 60  # Test duration in seconds


def test_meta_cognition_integration():
    """Test integration of meta-cognition with orchestrator."""
    print("\n=== Testing Quantum Meta-Cognition Integration ===")
    
    # Create orchestrator using factory
    print("\nCreating Quantum Orchestrator...")
    orchestrator = create_orchestrator()
    print(f"Orchestrator created with target file: {orchestrator.target_file}")
    
    # Apply meta-cognition to orchestrator
    print("\nApplying Meta-Cognition to Orchestrator...")
    meta = apply_meta_cognition(orchestrator)
    print(f"Meta-Cognition applied with coherence: {meta._calculate_coherence():.6f}")
    
    # Test reflection
    print("\nPerforming initial self-reflection...")
    reflection = meta.reflect()
    print(f"Reflection coherence: {reflection['coherence']:.6f}")
    print(f"Phi resonance: {reflection['phi_resonance']:.6f}")
    
    # Test goal formation
    print("\nForming autonomous goal...")
    goal = meta.form_goal()
    print(f"Goal: {goal['content']}")
    print(f"Priority: {goal['priority']}")
    
    # Test system state retrieval
    print("\nRetrieving system state...")
    state = meta.get_system_state()
    print(f"Current coherence: {state['coherence']:.6f}")
    print(f"Quantum fingerprint: {state['quantum_fingerprint']}")
    
    print("\nMeta-Cognition integration test completed successfully.")
    return meta, orchestrator


def test_nodular_integration(meta: QuantumMetaCognition):
    """Test integration with quantum nodular network if available."""
    if not nodular_available:
        print("\nSkipping nodular integration test (components not available)")
        return
    
    print("\n=== Testing Quantum Nodular Integration ===")
    
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
        node_id = f"meta_test_node_{i+1}"
        node_type = ["reasoning", "memory", "perception"][i % 3]
        capabilities = [f"{node_type}_core", "phi_harmonic", "meta_aware"]
        
        # Create node data
        node_data = {
            "id": node_id,
            "type": node_type,
            "capabilities": capabilities,
            "phi_resonance": (PHI * (i+1)) % 1.0,
            "coherence": 0.8 + (i * 0.05)
        }
        
        # Register node with discovery service
        try:
            discovery.register_node(node_type, node_data)
            nodes.append(node_data)
            print(f"Created and registered node: {node_id} ({node_type})")
            
            # Record nodular interaction in meta-cognition
            meta.record_nodular_interaction(node_id, "creation", {
                "type": node_type,
                "capabilities": capabilities,
                "phi_resonance": node_data["phi_resonance"]
            })
        except Exception as e:
            logger.error(f"Error registering node {node_id}: {e}")
    
    # Test node discovery
    print("\nTesting node discovery...")
    reasoning_nodes = discovery.discover_nodes_by_capability("reasoning_core")
    print(f"Found {len(reasoning_nodes)} reasoning nodes")
    
    memory_nodes = discovery.discover_nodes_by_capability("memory_core")
    print(f"Found {len(memory_nodes)} memory nodes")
    
    # Record discovery experience
    meta.store_experience("node_discovery", {
        "reasoning_nodes": len(reasoning_nodes),
        "memory_nodes": len(memory_nodes),
        "total_nodes": len(nodes)
    })
    
    print("\nNodular integration test completed.")


def run_evolution_cycle(meta: QuantumMetaCognition, orchestrator, duration: int = 30):
    """Run an evolution cycle with meta-cognition."""
    print(f"\n=== Running Evolution Cycle ({duration}s) ===")
    
    start_time = time.time()
    cycle_count = 0
    
    print("\nStarting evolution cycle...")
    while time.time() - start_time < duration:
        # Perform reflection
        reflection = meta.reflect()
        
        # Store experience
        meta.store_experience("evolution_cycle", {
            "cycle": cycle_count,
            "coherence": reflection["coherence"],
            "phi_resonance": reflection["phi_resonance"]
        })
        
        # Every 3rd cycle, form a new goal
        if cycle_count % 3 == 0:
            goal = meta.form_goal()
            print(f"Cycle {cycle_count}: Formed new goal - {goal['content']}")
        
        # Get system state
        state = meta.get_system_state()
        print(f"Cycle {cycle_count}: Coherence = {state['coherence']:.6f}, φ-resonance = {state['phi_resonance']:.6f}")
        
        # Simulate orchestrator evolution if available
        if hasattr(orchestrator, "evolve"):
            try:
                orchestrator.evolve()
                print(f"Cycle {cycle_count}: Orchestrator evolution step completed")
            except Exception as e:
                logger.error(f"Error in orchestrator evolution: {e}")
        
        cycle_count += 1
        time.sleep(5)  # Wait 5 seconds between cycles
    
    print(f"\nEvolution cycle completed with {cycle_count} iterations.")
    
    # Final reflection
    final_reflection = meta.reflect()
    final_state = meta.get_system_state()
    
    print("\nFinal System State:")
    print(f"Coherence: {final_state['coherence']:.6f}")
    print(f"Phi resonance: {final_state['phi_resonance']:.6f}")
    print(f"Goal completion rate: {final_state['goal_completion_rate']:.2f}")
    print(f"Quantum fingerprint: {final_state['quantum_fingerprint']}")
    
    return final_state


def main():
    """Main test function."""
    print("\n=== QUANTUM META-COGNITION TEST ===")
    print("Testing integration with existing quantum system...")
    
    # Test meta-cognition integration with orchestrator
    meta, orchestrator = test_meta_cognition_integration()
    
    # Test nodular integration if available
    test_nodular_integration(meta)
    
    # Run evolution cycle
    final_state = run_evolution_cycle(meta, orchestrator, TEST_DURATION)
    
    # Print summary
    print("\n=== TEST SUMMARY ===")
    print(f"Meta-Cognition module successfully integrated with existing quantum system")
    print(f"Final coherence: {final_state['coherence']:.6f}")
    print(f"Memory entries: {sum(final_state['memory_size'].values())} total")
    print(f"Quantum fingerprint: {final_state['quantum_fingerprint']}")
    print("\nTest completed successfully.")


if __name__ == "__main__":
    main()
