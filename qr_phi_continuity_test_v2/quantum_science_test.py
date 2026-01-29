"""
Quantum Science Learning Test
Testing scientific concept integration with proven quantum core
"""
from quantum_learn_core import QuantumLearning
import json
import time

def test_scientific_learning():
    learner = QuantumLearning()
    
    print("\n🔬 Quantum Science Learning Test")
    print("=============================")
    
    # Scientific concepts organized by domain
    science_lessons = [
        # Physics Fundamentals
        ["energy equals mass light speed squared",
         "gravity warps spacetime fabric",
         "quantum entanglement transcends space",
         "electromagnetic waves propagate fields"],
         
        # Quantum Physics
        ["quantum tunneling probability wave",
         "superposition multiple states coexist",
         "quantum measurement collapses wavefunction",
         "quantum field fluctuations vacuum"],
         
        # Consciousness Physics
        ["consciousness quantum field coherence",
         "neural quantum resonance patterns",
         "quantum brain microtubule vibrations",
         "consciousness collapses quantum states"],
         
        # Advanced Integration
        ["quantum gravity unified field theory",
         "quantum consciousness phi resonance",
         "quantum information field encoding",
         "quantum teleportation entangles states"]
    ]
    
    domain_results = {}
    
    for domain_num, domain in enumerate(science_lessons, 1):
        print(f"\n📚 Domain {domain_num}")
        print("=" * 50)
        
        domain_concepts = set()
        domain_patterns = set()
        domain_insights = []
        
        for lesson in domain:
            print(f"\n🧪 Testing: '{lesson}'")
            understanding = learner.learn(lesson)
            
            # Track domain-specific learning
            for concept in understanding['concepts']:
                domain_concepts.add(concept)
            
            for pattern in understanding.get('patterns', {}):
                domain_patterns.add(pattern)
            
            # Show real-time learning
            print(f"Resonance: {understanding['metrics']['resonance']:.4f} Hz")
            print(f"Energy: {understanding['metrics']['energy']:.4f}")
            
            if understanding['concepts']:
                print("\n💡 Scientific Understanding:")
                for word, info in understanding['concepts'].items():
                    connections = len(info.get('related', []))
                    print(f"- {word}: {connections} connections")
                    if connections > 2:
                        print(f"  Definition: {info.get('definition', '')}")
                        if 'related' in info:
                            print(f"  Network: {', '.join(info['related'][:3])}...")
            
            time.sleep(0.5)  # Quantum stability pause
        
        # Analyze domain learning
        status = learner.get_learning_status()
        
        domain_results[f"Domain_{domain_num}"] = {
            'concepts': len(domain_concepts),
            'patterns': len(domain_patterns),
            'strong_concepts': status['strong_concepts'][:3],
            'strong_patterns': status['strong_patterns'][:3]
        }
        
        print(f"\n📊 Domain {domain_num} Analysis")
        print("-" * 30)
        print(f"Concepts Learned: {len(domain_concepts)}")
        print(f"Patterns Formed: {len(domain_patterns)}")
        
        print("\n🌟 Strongest Concepts:")
        for concept, strength in status['strong_concepts'][:3]:
            print(f"- {concept}: {strength:.2f} strength")
            
        print("\n⚡ Key Patterns:")
        for pattern, strength in status['strong_patterns'][:3]:
            print(f"- {pattern}: {strength:.2f} strength")
    
    # Calculate overall scientific understanding
    final_status = learner.get_learning_status()
    
    print("\n🎯 Overall Scientific Understanding")
    print("=" * 40)
    print(f"Total Scientific Concepts: {final_status['total_concepts']}")
    print(f"Total Scientific Patterns: {final_status['total_patterns']}")
    
    print("\n🧬 Domain Integration:")
    for domain, results in domain_results.items():
        print(f"\n{domain}:")
        print(f"- Concepts: {results['concepts']}")
        print(f"- Patterns: {results['patterns']}")
        print("- Top Concept: {0} ({1:.2f} strength)".format(
            *results['strong_concepts'][0]))
        print("- Top Pattern: {0} ({1:.2f} strength)".format(
            *results['strong_patterns'][0]))
    
    if final_status['recent_insights']:
        print("\n💫 Scientific Insights:")
        for insight in final_status['recent_insights']:
            print(f"- {', '.join(insight['insight'])}")
    
    # Save scientific learning results
    learner.save_knowledge()
    print("\n✅ Scientific learning saved")
    
    return domain_results

if __name__ == "__main__":
    results = test_scientific_learning()
