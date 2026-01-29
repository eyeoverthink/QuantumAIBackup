"""
Scientific Testing of Quantum Learning
"""
from quantum_sync import QuantumSync
import json
import time

def run_scientific_test():
    sync = QuantumSync()
    results = []
    
    # Test Sets (carefully chosen for resonance patterns)
    test_sets = [
        # Set 1: Base quantum concepts
        ["quantum entanglement observed",
         "wave particle duality",
         "superposition states align"],
         
        # Set 2: Advanced physics
        ["electron spin measured",
         "proton charge detected",
         "neutron mass calculated"],
         
        # Set 3: Consciousness concepts
        ["neural pathways form",
         "synaptic connections strengthen",
         "brain waves synchronize"],
         
        # Set 4: Abstract concepts
        ["infinity recursively expands",
         "time fractally flows",
         "space dynamically curves"],
         
        # Set 5: Mixed concepts (testing cross-domain learning)
        ["quantum consciousness emerges",
         "neural quantum states",
         "conscious wave functions"]
    ]
    
    print("\n🧪 Scientific Quantum Learning Test")
    print("================================")
    
    for set_num, test_set in enumerate(test_sets, 1):
        print(f"\n📊 Test Set {set_num}")
        print("=" * 40)
        
        set_results = []
        for phrase in test_set:
            print(f"\n🔬 Testing: '{phrase}'")
            
            # Process phrase
            report = sync.sync(phrase)
            
            # Extract key metrics
            metrics = {
                'phrase': phrase,
                'resonance': report['quantum_state']['resonance'],
                'energy': report['quantum_state']['energy'],
                'concepts': len(report['understanding']['concepts']),
                'patterns': len(report['understanding']['patterns']),
                'timestamp': report['timestamp']
            }
            
            # Show real-time results
            print(f"Resonance: {metrics['resonance']:.4f} Hz")
            print(f"Energy: {metrics['energy']:.4f}")
            print(f"Concepts: {metrics['concepts']}")
            print(f"Patterns: {metrics['patterns']}")
            
            if report['understanding']['concepts']:
                print("\n💡 Key Concepts:")
                for word, info in report['understanding']['concepts'].items():
                    print(f"- {word}: {len(info['related'])} connections")
            
            set_results.append(metrics)
            time.sleep(0.5)  # Brief pause for stability
            
        # Analyze set results
        avg_resonance = sum(r['resonance'] for r in set_results) / len(set_results)
        avg_energy = sum(r['energy'] for r in set_results) / len(set_results)
        total_concepts = sum(r['concepts'] for r in set_results)
        total_patterns = sum(r['patterns'] for r in set_results)
        
        print(f"\n📈 Set {set_num} Analysis")
        print("-" * 20)
        print(f"Average Resonance: {avg_resonance:.4f} Hz")
        print(f"Average Energy: {avg_energy:.4f}")
        print(f"Total Concepts: {total_concepts}")
        print(f"Total Patterns: {total_patterns}")
        
        results.append({
            'set_num': set_num,
            'phrases': test_set,
            'metrics': set_results,
            'analysis': {
                'avg_resonance': float(avg_resonance),
                'avg_energy': float(avg_energy),
                'total_concepts': total_concepts,
                'total_patterns': total_patterns
            }
        })
        
    # Save test results
    with open('quantum_test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("\n✅ Test results saved")
    
    return results

if __name__ == "__main__":
    results = run_scientific_test()
