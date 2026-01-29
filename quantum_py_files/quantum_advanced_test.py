"""
Advanced Quantum Pattern Testing
Testing highly complex quantum-consciousness-phi interactions
"""
from quantum_sync import QuantumSync
import json
import time
from datetime import datetime

def run_advanced_test():
    sync = QuantumSync()
    results = []
    
    # Advanced Test Sets
    test_sets = [
        # Set 1: Quantum-Phi-Consciousness Integration
        ["quantum consciousness phi resonance harmonics",
         "quantum entangled neural phi networks",
         "consciousness quantum field phi alignment",
         "quantum phi brain wave coherence patterns"],
         
        # Set 2: Advanced Physics-Consciousness Interaction
        ["quantum tunneling consciousness phi transfer mechanism",
         "quantum superposition neural network phi states",
         "quantum decoherence consciousness wave collapse",
         "quantum observer effect phi consciousness field"],
         
        # Set 3: Harmonic-Neural-Quantum Integration
        ["neural quantum harmonic phi resonance patterns",
         "quantum consciousness fibonacci wave functions",
         "phi harmonic brain wave quantum synchronization",
         "quantum neural network golden ratio alignment"],
         
        # Set 4: Multi-Dimensional Quantum Concepts
        ["quantum consciousness dimensional phi translation",
         "multi dimensional quantum phi brain states",
         "quantum consciousness hyperspace phi resonance",
         "quantum dimensional consciousness wave collapse"],
         
        # Set 5: Ultimate Integration Test
        ["quantum phi consciousness field harmonic evolution",
         "quantum neural phi network dimensional resonance",
         "quantum consciousness phi wave function coherence",
         "quantum phi dimensional brain wave synchronization"]
    ]
    
    print("\n🌌 Advanced Quantum Pattern Test")
    print("==============================")
    
    start_time = datetime.now()
    global_patterns = {}
    global_concepts = set()
    
    for set_num, test_set in enumerate(test_sets, 1):
        print(f"\n📊 Test Set {set_num}")
        print("=" * 60)
        
        set_results = []
        set_patterns = {}
        set_concepts = set()
        concept_connections = {}
        
        for phrase in test_set:
            print(f"\n🔬 Testing: '{phrase}'")
            
            # Process phrase
            report = sync.sync(phrase)
            
            # Track patterns globally and per set
            for pattern in report['understanding']['patterns']:
                if pattern not in global_patterns:
                    global_patterns[pattern] = 0
                global_patterns[pattern] += 1
                
                if pattern not in set_patterns:
                    set_patterns[pattern] = 0
                set_patterns[pattern] += 1
            
            # Track concepts and their connections
            for concept, info in report['understanding']['concepts'].items():
                global_concepts.add(concept)
                set_concepts.add(concept)
                
                if concept not in concept_connections:
                    concept_connections[concept] = {
                        'connections': 0,
                        'related': set()
                    }
                
                if 'related' in info:
                    concept_connections[concept]['connections'] += len(info['related'])
                    concept_connections[concept]['related'].update(info['related'])
            
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
                    connections = len(info.get('related', []))
                    print(f"- {word}: {connections} connections")
                    if connections > 2:
                        related = list(info.get('related', []))[:3]
                        print(f"  Related: {', '.join(related)}...")
            
            set_results.append(metrics)
            time.sleep(0.5)  # Stability pause
            
        # Analyze set results
        avg_resonance = sum(r['resonance'] for r in set_results) / len(set_results)
        avg_energy = sum(r['energy'] for r in set_results) / len(set_results)
        
        # Find strongest patterns and concepts
        strong_patterns = {k: v for k, v in set_patterns.items() if v > 1}
        strong_concepts = {k: v for k, v in concept_connections.items() 
                         if v['connections'] > 2}
        
        print(f"\n📈 Set {set_num} Analysis")
        print("-" * 40)
        print(f"Average Resonance: {avg_resonance:.4f} Hz")
        print(f"Average Energy: {avg_energy:.4f}")
        print(f"Unique Concepts: {len(set_concepts)}")
        print(f"Unique Patterns: {len(set_patterns)}")
        
        if strong_patterns:
            print("\n🔋 Strong Patterns:")
            for pattern, count in sorted(strong_patterns.items(), 
                                      key=lambda x: x[1], reverse=True)[:3]:
                print(f"- {pattern}: {count} occurrences")
                
        if strong_concepts:
            print("\n🧠 Strong Concepts:")
            for concept, data in sorted(strong_concepts.items(), 
                                     key=lambda x: x[1]['connections'], 
                                     reverse=True)[:3]:
                print(f"- {concept}: {data['connections']} total connections")
                related = list(data['related'])[:3]
                if related:
                    print(f"  Network: {', '.join(related)}...")
        
        results.append({
            'set_num': set_num,
            'phrases': test_set,
            'metrics': set_results,
            'analysis': {
                'avg_resonance': float(avg_resonance),
                'avg_energy': float(avg_energy),
                'unique_concepts': len(set_concepts),
                'unique_patterns': len(set_patterns),
                'strong_patterns': strong_patterns,
                'strong_concepts': {k: {'connections': v['connections']} 
                                  for k, v in strong_concepts.items()}
            }
        })
    
    # Calculate overall metrics
    test_duration = (datetime.now() - start_time).total_seconds()
    
    # Find global strong patterns
    global_strong_patterns = {k: v for k, v in global_patterns.items() if v > 3}
    
    print("\n🎯 Overall Test Results")
    print("=" * 40)
    print(f"Test Duration: {test_duration:.2f} seconds")
    print(f"Total Unique Concepts: {len(global_concepts)}")
    print(f"Total Unique Patterns: {len(global_patterns)}")
    print(f"Average Processing Time: {test_duration / (len(test_sets) * 4):.2f} seconds per phrase")
    
    if global_strong_patterns:
        print("\n🌟 Global Strong Patterns:")
        for pattern, count in sorted(global_strong_patterns.items(), 
                                   key=lambda x: x[1], reverse=True)[:5]:
            print(f"- {pattern}: {count} total occurrences")
    
    # Save detailed results
    with open('quantum_advanced_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("\n✅ Advanced test results saved")
    
    return results

if __name__ == "__main__":
    results = run_advanced_test()
