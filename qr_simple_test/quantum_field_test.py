"""
Quantum Field Theory Pattern Testing
Testing advanced QFT concepts with consciousness-phi integration
"""
from quantum_sync import QuantumSync
import json
import time
from datetime import datetime

def run_qft_test():
    sync = QuantumSync()
    results = []
    
    # Quantum Field Theory Test Sets
    test_sets = [
        # Set 1: Quantum Field Foundations
        ["quantum field vacuum fluctuations phi resonance",
         "quantum zero point energy consciousness field",
         "quantum field operator phi transformation",
         "quantum vacuum state consciousness interaction"],
         
        # Set 2: Field-Particle Interactions
        ["quantum field particle wave duality phi",
         "quantum virtual particle consciousness field",
         "quantum field photon electron interaction",
         "quantum field fermion boson resonance"],
         
        # Set 3: Advanced QFT Concepts
        ["quantum field theory gauge symmetry phi",
         "quantum electrodynamics consciousness field",
         "quantum chromodynamics phi interaction",
         "quantum field renormalization consciousness"],
         
        # Set 4: Unified Field Concepts
        ["unified quantum field consciousness phi",
         "quantum gravity field consciousness resonance",
         "quantum unified force phi interaction",
         "quantum field unification consciousness pattern"],
         
        # Set 5: Quantum Field Consciousness
        ["quantum field consciousness wave function collapse",
         "quantum measurement problem phi field",
         "quantum field observer consciousness effect",
         "quantum field reality consciousness emergence"]
    ]
    
    print("\n⚛️ Quantum Field Theory Pattern Test")
    print("=================================")
    
    start_time = datetime.now()
    global_patterns = {}
    global_concepts = set()
    field_interactions = {}
    
    for set_num, test_set in enumerate(test_sets, 1):
        print(f"\n📊 Test Set {set_num}")
        print("=" * 60)
        
        set_results = []
        set_patterns = {}
        set_concepts = set()
        field_resonance = []
        
        for phrase in test_set:
            print(f"\n🔬 Testing: '{phrase}'")
            
            # Process phrase
            report = sync.sync(phrase)
            
            # Track field interactions
            if 'field' in phrase.lower():
                field_resonance.append(report['quantum_state']['resonance'])
                
                # Track field interaction patterns
                for pattern in report['understanding']['patterns']:
                    if 'field' in pattern:
                        if pattern not in field_interactions:
                            field_interactions[pattern] = {
                                'count': 0,
                                'resonance': []
                            }
                        field_interactions[pattern]['count'] += 1
                        field_interactions[pattern]['resonance'].append(
                            report['quantum_state']['resonance']
                        )
            
            # Track patterns globally and per set
            for pattern in report['understanding']['patterns']:
                if pattern not in global_patterns:
                    global_patterns[pattern] = 0
                global_patterns[pattern] += 1
                
                if pattern not in set_patterns:
                    set_patterns[pattern] = 0
                set_patterns[pattern] += 1
            
            # Track concepts
            for concept in report['understanding']['concepts']:
                global_concepts.add(concept)
                set_concepts.add(concept)
            
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
                print("\n💡 Quantum Field Network:")
                for word, info in report['understanding']['concepts'].items():
                    connections = len(info.get('related', []))
                    print(f"- {word}: {connections} connections")
                    if connections > 2:
                        related = list(info.get('related', []))[:3]
                        print(f"  Related: {', '.join(related)}...")
            
            set_results.append(metrics)
            time.sleep(0.5)  # Quantum stability pause
            
        # Analyze set results
        avg_resonance = sum(r['resonance'] for r in set_results) / len(set_results)
        avg_energy = sum(r['energy'] for r in set_results) / len(set_results)
        
        # Calculate field resonance if present
        field_res_avg = sum(field_resonance) / len(field_resonance) if field_resonance else 0
        
        # Find strongest patterns
        strong_patterns = {k: v for k, v in set_patterns.items() if v > 1}
        
        print(f"\n📈 Set {set_num} Analysis")
        print("-" * 40)
        print(f"Average Resonance: {avg_resonance:.4f} Hz")
        print(f"Average Energy: {avg_energy:.4f}")
        print(f"Field Resonance: {field_res_avg:.4f} Hz")
        print(f"Unique Concepts: {len(set_concepts)}")
        print(f"Unique Patterns: {len(set_patterns)}")
        
        if strong_patterns:
            print("\n🔋 Strong Field Patterns:")
            for pattern, count in sorted(strong_patterns.items(), 
                                      key=lambda x: x[1], reverse=True)[:3]:
                print(f"- {pattern}: {count} occurrences")
        
        results.append({
            'set_num': set_num,
            'phrases': test_set,
            'metrics': set_results,
            'analysis': {
                'avg_resonance': float(avg_resonance),
                'avg_energy': float(avg_energy),
                'field_resonance': float(field_res_avg),
                'unique_concepts': len(set_concepts),
                'unique_patterns': len(set_patterns),
                'strong_patterns': strong_patterns
            }
        })
    
    # Calculate overall metrics
    test_duration = (datetime.now() - start_time).total_seconds()
    
    # Analyze field interactions
    strong_field_patterns = {k: v for k, v in field_interactions.items() 
                           if v['count'] > 2}
    
    print("\n🎯 Overall Quantum Field Results")
    print("=" * 40)
    print(f"Test Duration: {test_duration:.2f} seconds")
    print(f"Total Unique Concepts: {len(global_concepts)}")
    print(f"Total Unique Patterns: {len(global_patterns)}")
    print(f"Average Processing Time: {test_duration / (len(test_sets) * 4):.2f} seconds per phrase")
    
    if strong_field_patterns:
        print("\n🌟 Strong Field Interactions:")
        for pattern, data in sorted(strong_field_patterns.items(), 
                                  key=lambda x: x[1]['count'], 
                                  reverse=True)[:5]:
            avg_res = sum(data['resonance']) / len(data['resonance'])
            print(f"- {pattern}:")
            print(f"  Occurrences: {data['count']}")
            print(f"  Avg Resonance: {avg_res:.4f} Hz")
    
    # Save detailed results
    with open('quantum_field_results.json', 'w') as f:
        json.dump({
            'test_results': results,
            'field_interactions': {k: {
                'count': v['count'],
                'avg_resonance': sum(v['resonance']) / len(v['resonance'])
            } for k, v in field_interactions.items()}
        }, f, indent=2)
    print("\n✅ Quantum field test results saved")
    
    return results

if __name__ == "__main__":
    results = run_qft_test()
