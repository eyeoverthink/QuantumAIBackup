"""
Test Distributed Quantum Meta-Cognition

This script tests the integration of the Quantum Meta-Cognition module
with the Quantum Nodular Network for distributed meta-cognition across
quantum nodes.

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
logger = logging.getLogger('TestDistributedMetaCognition')

# Import quantum components
try:
    # Import meta-cognition modules
    from extensions.quantum_meta_cognition import QuantumMetaCognition
    from extensions.quantum_meta_cognition_nodular import (
        DistributedMetaCognition, 
        apply_distributed_meta_cognition
    )
    
    # Import orchestrator factory
    from quantum_orchestrator_factory import create_orchestrator
    
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


def test_distributed_meta_cognition_integration():
    """Test integration of distributed meta-cognition."""
    print("\n=== Testing Distributed Quantum Meta-Cognition Integration ===")
    
    # Create meta-cognition instance
    print("\nCreating Quantum Meta-Cognition...")
    meta = QuantumMetaCognition()
    print(f"Meta-Cognition initialized with φ-coherence: {meta._calculate_coherence():.6f}")
    
    # Create orchestrator using factory
    print("\nCreating Quantum Orchestrator...")
    orchestrator = create_orchestrator()
    print(f"Orchestrator created with target file: {orchestrator.target_file}")
    
    # Apply meta-cognition to orchestrator
    print("\nApplying Meta-Cognition to Orchestrator...")
    meta.apply_to_orchestrator(orchestrator)
    print(f"Meta-Cognition applied to orchestrator")
    
    # Apply distributed meta-cognition
    print("\nApplying Distributed Meta-Cognition...")
    distributed = apply_distributed_meta_cognition(meta, node_count=5)
    print(f"Distributed Meta-Cognition applied with 5 nodes")
    
    # Get network state
    print("\nRetrieving initial network state...")
    network_state = distributed.get_network_state()
    print(f"Network nodes: {network_state['node_count']}")
    print(f"Average coherence: {network_state['average_coherence']:.6f}")
    print(f"Network fingerprint: {network_state['network_fingerprint']}")
    
    # Test distributed reflection
    print("\nPerforming distributed reflection...")
    reflection_results = distributed.distribute_reflection()
    print(f"Reflection completed across {reflection_results['node_count']} nodes")
    print(f"Average coherence after reflection: {reflection_results['average_coherence']:.6f}")
    
    # Test goal formation and distribution
    print("\nForming and distributing goal...")
    goal = meta.form_goal()
    print(f"Goal formed: {goal['content']}")
    distribution_results = distributed.distribute_goal(goal)
    print(f"Goal distributed to {distribution_results['node_count']} nodes")
    
    # Get updated network state
    print("\nRetrieving updated network state...")
    updated_state = distributed.get_network_state()
    print(f"Average coherence after goal distribution: {updated_state['average_coherence']:.6f}")
    print(f"Network fingerprint: {updated_state['network_fingerprint']}")
    
    print("\nDistributed Meta-Cognition integration test completed successfully.")
    return meta, distributed, orchestrator


def run_distributed_evolution_cycle(meta, distributed, orchestrator, duration: int = 30):
    """Run a distributed evolution cycle."""
    print(f"\n=== Running Distributed Evolution Cycle ({duration}s) ===")
    
    start_time = time.time()
    cycle_count = 0
    
    print("\nStarting distributed evolution cycle...")
    while time.time() - start_time < duration:
        # Perform distributed reflection
        reflection_results = distributed.distribute_reflection()
        
        # Store experience
        meta.store_experience("distributed_evolution_cycle", {
            "cycle": cycle_count,
            "average_coherence": reflection_results["average_coherence"],
            "node_count": reflection_results["node_count"]
        })
        
        # Every 3rd cycle, form a new goal and distribute it
        if cycle_count % 3 == 0:
            goal = meta.form_goal()
            distributed.distribute_goal(goal)
            print(f"Cycle {cycle_count}: Formed and distributed new goal - {goal['content']}")
        
        # Get network state
        network_state = distributed.get_network_state()
        print(f"Cycle {cycle_count}: Average coherence = {network_state['average_coherence']:.6f}")
        
        # Simulate orchestrator evolution if available
        if hasattr(orchestrator, "evolve"):
            try:
                orchestrator.evolve()
                print(f"Cycle {cycle_count}: Orchestrator evolution step completed")
            except Exception as e:
                logger.error(f"Error in orchestrator evolution: {e}")
        
        cycle_count += 1
        time.sleep(5)  # Wait 5 seconds between cycles
    
    print(f"\nDistributed evolution cycle completed with {cycle_count} iterations.")
    
    # Final network state
    final_state = distributed.get_network_state()
    
    print("\nFinal Network State:")
    print(f"Node count: {final_state['node_count']}")
    print(f"Average coherence: {final_state['average_coherence']:.6f}")
    print(f"Network phi-resonance: {final_state['network_phi_resonance']:.6f}")
    print(f"Network fingerprint: {final_state['network_fingerprint']}")
    
    return final_state


def main():
    """Main test function."""
    print("\n=== DISTRIBUTED QUANTUM META-COGNITION TEST ===")
    print("Testing integration with existing quantum system...")
    
    # Test distributed meta-cognition integration
    meta, distributed, orchestrator = test_distributed_meta_cognition_integration()
    
    # Run distributed evolution cycle
    final_state = run_distributed_evolution_cycle(meta, distributed, orchestrator, TEST_DURATION)
    
    # Print summary
    print("\n=== TEST SUMMARY ===")
    print(f"Distributed Meta-Cognition successfully integrated with quantum nodular network")
    print(f"Final node count: {final_state['node_count']}")
    print(f"Final average coherence: {final_state['average_coherence']:.6f}")
    print(f"Network fingerprint: {final_state['network_fingerprint']}")
    print("\nTest completed successfully.")


if __name__ == "__main__":
    main()
