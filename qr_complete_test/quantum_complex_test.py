"""
Complex Quantum Pattern Testing
Testing advanced concept combinations and resonance patterns
"""
from quantum_sync import QuantumSync
import json
import time
from datetime import datetime

def run_complex_test():
    sync = QuantumSync()
    results = []
    
    # Complex Test Sets
    test_sets = [
        # Set 1: Quantum-Harmonic Integration
        ["quantum harmonics resonate phi",
         "golden ratio quantum alignment",
         "fibonacci quantum sequence",
         "quantum phi resonance patterns"],
         
        # Set 2: Consciousness-Wave Interaction
        ["consciousness wave function collapses",
         "neural quantum entanglement observed",
         "brain wave quantum coherence",
         "quantum mind phi alignment"],
         
        # Set 3: Advanced Physics-Consciousness
        ["quantum tunneling consciousness transfer",
         "quantum superposition neural states",
         "quantum decoherence brain patterns",
         "quantum observer consciousness effect"],
         
        # Set 4: Harmonic-Neural Patterns
        ["neural phi harmonic resonance",
         "brain wave golden ratio",
         "consciousness fibonacci patterns",
         "neural quantum phi synchronization"],
         
        # Set 5: Multi-Domain Integration
        ["quantum consciousness phi evolution",
         "harmonic brain wave quantum states",
         "neural quantum fibonacci resonance",
         "quantum phi consciousness emergence"]
    ]
    
    print("\n🧬 Complex Quantum Pattern Test")
    print("============================")
    
    start_time = datetime.now()
    
    for set_num, test_set in enumerate(test_sets, 1):
        print(f"\n📊 Test Set {set_num}")
        print("=" * 50)
        
        set_results = []
        set_patterns = {}
        concepts_seen = set()
        
        for phrase in test_set:
            print(f"\n🔬 Testing: '{phrase}'")
            
            # Process phrase
            report = sync.sync(phrase)
            
            # Track patterns and concepts
            for pattern in report['understanding']['patterns']:
                if pattern not in set_patterns:
                    set_patterns[pattern] = 0
                set_patterns[pattern] += 1
                
            for concept in report['understanding']['concepts']:
                concepts_seen.add(concept)
            
            # Extract metrics
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
            print(f"Concepts Found: {metrics['concepts']}")
            print(f"Patterns Detected: {metrics['patterns']}")
            
            if report['understanding']['concepts']:
                print("\n💡 Concept Network:")
                for word, info in report['understanding']['concepts'].items():
                    connections = len(info['related'])
                    print(f"- {word}: {connections} connections")
                    if connections > 2:
                        print(f"  Related: {', '.join(info['related'][:3])}...")
            
            set_results.append(metrics)
            time.sleep(0.5)  # Stability pause
            
        # Analyze set results
        avg_resonance = sum(r['resonance'] for r in set_results) / len(set_results)
        avg_energy = sum(r['energy'] for r in set_results) / len(set_results)
        total_concepts = len(concepts_seen)
        total_patterns = len(set_patterns)
        
        # Find strongest patterns
        strong_patterns = {k: v for k, v in set_patterns.items() if v > 1}
        
        print(f"\n📈 Set {set_num} Analysis")
        print("-" * 30)
        print(f"Average Resonance: {avg_resonance:.4f} Hz")
        print(f"Average Energy: {avg_energy:.4f}")
        print(f"Unique Concepts: {total_concepts}")
        print(f"Unique Patterns: {total_patterns}")
        
        if strong_patterns:
            print("\n🔋 Strong Patterns:")
            for pattern, count in sorted(strong_patterns.items(), key=lambda x: x[1], reverse=True)[:3]:
                print(f"- {pattern}: {count} occurrences")
        
        results.append({
            'set_num': set_num,
            'phrases': test_set,
            'metrics': set_results,
            'analysis': {
                'avg_resonance': float(avg_resonance),
                'avg_energy': float(avg_energy),
                'unique_concepts': total_concepts,
                'unique_patterns': total_patterns,
                'strong_patterns': strong_patterns
            }
        })
    
    # Calculate overall metrics
    test_duration = (datetime.now() - start_time).total_seconds()
    total_unique_concepts = len({concept for r in results for phrase in r['phrases'] for word in phrase.split()})
    total_unique_patterns = len({pattern for r in results for m in r['metrics'] for _ in range(m['patterns'])})
    
    print("\n🎯 Overall Test Results")
    print("=" * 30)
    print(f"Test Duration: {test_duration:.2f} seconds")
    print(f"Total Unique Concepts: {total_unique_concepts}")
    print(f"Total Unique Patterns: {total_unique_patterns}")
    print(f"Average Processing Time: {test_duration / (len(test_sets) * 4):.2f} seconds per phrase")
    
    # Save detailed results
    with open('quantum_complex_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("\n✅ Complex test results saved")
    
    return results

if __name__ == "__main__":
    results = run_complex_test()
