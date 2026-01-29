"""
Main script to demonstrate quantum particle family mapping
"""

import os
from quantum_particle_families.particle_family_mapper import ParticleFamilyMapper

def main():
    """Main function to demonstrate particle family mapping"""
    print("\n🌟 Quantum Particle Family Mapping Demo")
    print("=" * 50)
    
    # Initialize mapper
    print("\nInitializing Particle Family Mapper...")
    mapper = ParticleFamilyMapper()
    
    # Create output directory
    output_dir = 'particle_family_results'
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate visualizations
    print("\nGenerating particle family visualizations...")
    mapper.visualize_particle_families(os.path.join(output_dir, 'particle_families.png'))
    mapper.visualize_interactions(os.path.join(output_dir, 'particle_interactions.png'))
    
    # Analyze particle combinations
    print("\nAnalyzing particle combinations...")
    combinations = mapper.analyze_particle_combinations()
    
    print("\nPossible Mesons:")
    for quark1, quark2 in combinations['mesons']:
        print(f"- {quark1} + {quark2}")
        
    print("\nPossible Baryons:")
    for quark1, quark2, quark3 in combinations['baryons']:
        print(f"- {quark1} + {quark2} + {quark3}")
    
    # Get resonances
    print("\nParticle Resonances:")
    resonances = mapper.get_particle_resonances()
    for particle, resonance in resonances.items():
        print(f"- {particle}: {float(resonance):.6f}")
    
    # Print family metrics
    print("\nFamily Metrics:")
    for family in [1, 2, 3]:
        print(f"\nFamily {family}:")
        print(f"Coherence: {float(mapper.get_family_coherence(family)):.6f}")
        print(f"Stability: {float(mapper.get_family_stability(family)):.6f}")
    
    print("\n✨ Particle family mapping complete!")
    print(f"Results saved in: {output_dir}/")

if __name__ == "__main__":
    main()
