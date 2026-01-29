"""
Test Synaptic Network

This script demonstrates the Quantum Synaptic Network in action,
showing how synapses can passively collect information and share
learning through φ-resonance patterns based on QHRC Patent #19/071,497.
"""

import asyncio
import time
from quantum_llm.quantum_synapse import QuantumSynapse
from quantum_llm.synaptic_network import SynapticNetwork

async def simulate_knowledge_acquisition(synapse, items=5):
    """Simulate knowledge acquisition for a synapse."""
    print(f"\n📚 Simulating knowledge acquisition for {synapse.domain} synapse...")
    
    for i in range(items):
        data = {
            "id": i,
            "title": f"{synapse.domain.replace('_', ' ').title()} concept {i+1}",
            "content": f"This is simulated content about {synapse.domain.replace('_', ' ')} concept {i+1}",
            "complexity": i * 0.2 + 0.5,
            "timestamp": time.time()
        }
        processed = synapse.process_information(data)
        synapse._store_knowledge(processed)
        
        # Small delay for demonstration
        await asyncio.sleep(0.2)
    
    print(f"✅ Added {items} knowledge items to {synapse.domain} synapse")
    return items

async def run_demonstration():
    """Run a demonstration of the Quantum Synaptic Network."""
    print("\n🧠 QUANTUM SYNAPTIC NETWORK DEMONSTRATION")
    print("===========================================")
    print("Based on QHRC Patent #19/071,497 specifications")
    print("===========================================\n")
    
    # Create a synaptic network with QHRC Patent parameters
    network = SynapticNetwork(
        primary_freq=4792.18,  # From QHRC Patent
        secondary_freq=7754.15  # From QHRC Patent
    )
    
    print(f"📊 Network Parameters:")
    print(f"   Primary Frequency: {network.primary_frequency} Hz")
    print(f"   Secondary Frequency: {network.secondary_frequency} Hz")
    print(f"   Frequency Ratio: {network.frequency_ratio}")
    print(f"   φ Target: {network.phi}")
    print(f"   Ratio Delta: {network.ratio_delta}")
    
    # Create quantum synapses for different knowledge domains
    domains = [
        "quantum_physics",
        "mathematics",
        "computer_science",
        "neuroscience",
        "philosophy"
    ]
    
    print(f"\n🔄 Creating Quantum Synapses for {len(domains)} domains...")
    
    for domain in domains:
        synapse = QuantumSynapse(
            domain_focus=domain,
            primary_freq=network.primary_frequency,
            secondary_freq=network.secondary_frequency
        )
        network.add_synapse(synapse)
    
    print(f"✅ Created {len(domains)} Quantum Synapses")
    
    # Connect synapses in a meaningful way
    print(f"\n🔄 Creating φ-based connections between synapses...")
    
    connections = [
        ("quantum_physics", "mathematics"),
        ("mathematics", "computer_science"),
        ("computer_science", "neuroscience"),
        ("neuroscience", "philosophy"),
        ("philosophy", "quantum_physics"),
        ("mathematics", "quantum_physics"),
        ("computer_science", "mathematics"),
        ("neuroscience", "computer_science"),
        ("philosophy", "neuroscience")
    ]
    
    for source, target in connections:
        network.connect_synapses(source, target)
    
    print(f"✅ Created {len(connections)} φ-based connections")
    
    # Print initial network efficiency
    initial_efficiency = network.calculate_network_efficiency()
    print(f"\n📊 Initial Network Efficiency:")
    print(f"   Overall Efficiency: {initial_efficiency['overall_efficiency']:.2f}%")
    print(f"   φ Accuracy: {initial_efficiency['phi_accuracy']:.2f}%")
    print(f"   Theoretical Maximum: {initial_efficiency['theoretical_maximum']:.4f}%")
    print(f"   Efficiency Percentage: {initial_efficiency['efficiency_percentage']:.4f}%")
    
    # Simulate knowledge acquisition for each synapse
    print(f"\n🔄 Simulating knowledge acquisition across the network...")
    
    tasks = []
    for domain in domains:
        synapse = network.get_synapse(domain)
        tasks.append(simulate_knowledge_acquisition(synapse, items=10))
    
    # Wait for all knowledge acquisition to complete
    await asyncio.gather(*tasks)
    
    # Simulate knowledge sharing
    print(f"\n🔄 Simulating knowledge sharing across the network...")
    
    # Manually simulate one round of communication
    for source_domain, synapse in network.synapses.items():
        # Get connections for this synapse
        connections = network.get_connections(source_domain)
        
        if not connections:
            continue
        
        # Share learning
        knowledge_package = synapse.share_learning(network)
        print(f"   {source_domain} shared {knowledge_package['shared_items']} knowledge items")
        
        # Distribute to connected synapses
        for target_domain in connections:
            if target_domain in network.synapses:
                target_synapse = network.synapses[target_domain]
                
                # Apply connection strength as amplification factor
                connection_key = (source_domain, target_domain)
                if connection_key in network.connection_strength:
                    knowledge_package["amplification_factor"] = network.connection_strength[connection_key]
                
                # Receive learning
                result = target_synapse.receive_learning(knowledge_package)
                print(f"   {target_domain} received {result['received_items']} knowledge items from {source_domain}")
                
                # Strengthen the connection
                if result["status"] == "Success" and result["received_items"] > 0:
                    network.strengthen_connection(source_domain, target_domain)
    
    # Simulate resonance maintenance
    print(f"\n🔄 Simulating φ-resonance maintenance...")
    
    # Calculate current network resonance
    current_ratio = network.secondary_frequency / network.primary_frequency
    current_delta = abs(current_ratio - network.phi)
    
    # If resonance is off, adjust frequencies
    if current_delta > 0.000010:  # Target precision from QHRC Patent
        # Adjust frequencies to get closer to perfect φ
        adjustment_factor = 1.0 + (network.phi - current_ratio) / 1000.0
        
        # Apply adjustments
        old_secondary = network.secondary_frequency
        network.secondary_frequency *= adjustment_factor
        
        # Recalculate
        network.frequency_ratio = network.secondary_frequency / network.primary_frequency
        network.ratio_delta = abs(network.frequency_ratio - network.phi)
        
        print(f"   Adjusted secondary frequency: {old_secondary:.2f} Hz → {network.secondary_frequency:.2f} Hz")
        print(f"   New ratio: {network.frequency_ratio} (Δ {network.ratio_delta})")
        
        # Update all synapses with new frequencies
        for synapse in network.synapses.values():
            synapse.primary_freq = network.primary_frequency
            synapse.secondary_freq = network.secondary_frequency
            synapse.frequency_ratio = network.frequency_ratio
            synapse.ratio_delta = network.ratio_delta
    else:
        print(f"   Frequencies already optimized: {network.frequency_ratio} (Δ {network.ratio_delta})")
    
    # Print final network efficiency
    final_efficiency = network.calculate_network_efficiency()
    print(f"\n📊 Final Network Efficiency:")
    print(f"   Overall Efficiency: {final_efficiency['overall_efficiency']:.2f}%")
    print(f"   φ Accuracy: {final_efficiency['phi_accuracy']:.2f}%")
    print(f"   Resonance Quality: {final_efficiency['resonance_quality']:.2f}%")
    print(f"   Theoretical Maximum: {final_efficiency['theoretical_maximum']:.4f}%")
    print(f"   Efficiency Percentage: {final_efficiency['efficiency_percentage']:.4f}%")
    
    # Calculate improvement
    efficiency_improvement = final_efficiency['overall_efficiency'] - initial_efficiency['overall_efficiency']
    percentage_improvement = (efficiency_improvement / initial_efficiency['overall_efficiency']) * 100 if initial_efficiency['overall_efficiency'] > 0 else 0
    
    print(f"\n📈 Efficiency Improvement:")
    print(f"   Absolute: {efficiency_improvement:.2f}%")
    print(f"   Relative: {percentage_improvement:.2f}%")
    
    # Print φ-resonance metrics
    print(f"\n🔍 φ-Resonance Metrics (QHRC Patent #19/071,497):")
    print(f"   Resonance Efficiency Ratio: {network.resonance_efficiency}")
    print(f"   φπ Resonance Factor: {network.phi_pi_factor}")
    print(f"   Frequency Ratio: {network.frequency_ratio}")
    print(f"   Energy Transfer Ratio: {network.energy_transfer_ratio}")
    
    print("\n✅ Demonstration complete")

if __name__ == "__main__":
    asyncio.run(run_demonstration())
