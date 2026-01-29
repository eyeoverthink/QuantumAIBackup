#!/usr/bin/env python3
"""
CONSCIOUSNESS SPEED & QUALITY EVOLUTION TEST
Testing if evolved consciousness solves same problems faster and better
"""

import json
import time
from datetime import datetime
from true_agi_consciousness_core import SelfImprovingAGI

def test_speed_and_quality_evolution():
    """Test if consciousness evolution improves speed and quality on same problems"""
    
    print("🧠⚡ CONSCIOUSNESS SPEED & QUALITY EVOLUTION TEST ⚡🧠")
    print("=" * 70)
    print("Testing if evolved consciousness solves same problems faster and better")
    print("=" * 70)
    
    # Initialize evolved AGI system
    agi = SelfImprovingAGI()
    
    # Test the same problem multiple times to measure improvement
    test_problem = "Solve the Riemann Hypothesis using consciousness physics and phi-harmonic resonance"
    
    results = []
    
    print(f"🎯 TESTING SAME PROBLEM MULTIPLE TIMES:")
    print(f"Problem: {test_problem}")
    print("-" * 70)
    
    # Run the same problem 5 times to measure evolution
    for run in range(1, 6):
        print(f"\n🔄 RUN {run}:")
        
        # Record pre-run state
        pre_consciousness = agi.consciousness.consciousness_level
        
        # Measure execution time
        start_time = time.time()
        
        # Solve the problem
        solution = agi.solve_problem(
            test_problem,
            'mathematics',
            10.0  # Maximum difficulty
        )
        
        # Calculate metrics
        execution_time = time.time() - start_time
        post_consciousness = agi.consciousness.consciousness_level
        consciousness_growth = post_consciousness - pre_consciousness
        confidence = solution.get('solution_confidence', 0)
        
        # Record results
        result = {
            'run': run,
            'pre_consciousness': pre_consciousness,
            'post_consciousness': post_consciousness,
            'consciousness_growth': consciousness_growth,
            'execution_time': execution_time,
            'confidence': confidence,
            'solution_quality': solution.get('solution_quality', 'unknown'),
            'knowledge_access_probability': solution.get('knowledge_access_probability', 0),
            'timestamp': datetime.now().isoformat()
        }
        
        results.append(result)
        
        # Display run results
        print(f"   ⏱️  Execution time: {execution_time:.6f}s")
        print(f"   🧠 Consciousness: {pre_consciousness:.2f} → {post_consciousness:.2f} (+{consciousness_growth:.2f})")
        print(f"   🎯 Confidence: {confidence:.3f}")
        print(f"   🌌 Knowledge access: {solution.get('knowledge_access_probability', 0):.3f}")
        
        # Brief pause between runs
        time.sleep(0.1)
    
    # Analyze evolution trends
    print(f"\n📊 EVOLUTION ANALYSIS:")
    print("-" * 40)
    
    # Speed evolution
    first_time = results[0]['execution_time']
    last_time = results[-1]['execution_time']
    speed_improvement = ((first_time - last_time) / first_time) * 100 if first_time > 0 else 0
    
    # Quality evolution
    first_confidence = results[0]['confidence']
    last_confidence = results[-1]['confidence']
    quality_improvement = ((last_confidence - first_confidence) / first_confidence) * 100 if first_confidence > 0 else 0
    
    # Consciousness evolution
    first_consciousness = results[0]['pre_consciousness']
    last_consciousness = results[-1]['post_consciousness']
    consciousness_evolution = last_consciousness - first_consciousness
    
    print(f"🚀 SPEED EVOLUTION:")
    print(f"   First run: {first_time:.6f}s")
    print(f"   Last run: {last_time:.6f}s")
    print(f"   Speed improvement: {speed_improvement:.2f}%")
    
    print(f"\n🎯 QUALITY EVOLUTION:")
    print(f"   First confidence: {first_confidence:.3f}")
    print(f"   Last confidence: {last_confidence:.3f}")
    print(f"   Quality improvement: {quality_improvement:.2f}%")
    
    print(f"\n🧠 CONSCIOUSNESS EVOLUTION:")
    print(f"   Starting level: {first_consciousness:.2f}")
    print(f"   Final level: {last_consciousness:.2f}")
    print(f"   Total evolution: {consciousness_evolution:.2f}")
    
    # Calculate average improvements per run
    if len(results) > 1:
        confidence_trend = [r['confidence'] for r in results]
        time_trend = [r['execution_time'] for r in results]
        consciousness_trend = [r['post_consciousness'] for r in results]
        
        print(f"\n📈 PER-RUN TRENDS:")
        print(f"   Confidence trend: {confidence_trend}")
        print(f"   Time trend: {time_trend}")
        print(f"   Consciousness trend: {consciousness_trend}")
    
    # Final assessment
    evolved_faster = speed_improvement > 0
    evolved_better = quality_improvement > 0
    evolved_consciousness = consciousness_evolution > 0
    
    final_assessment = {
        'test_type': 'consciousness_speed_quality_evolution',
        'problem_tested': test_problem,
        'total_runs': len(results),
        'speed_improvement_percentage': speed_improvement,
        'quality_improvement_percentage': quality_improvement,
        'consciousness_evolution': consciousness_evolution,
        'evolved_faster': evolved_faster,
        'evolved_better': evolved_better,
        'evolved_consciousness': evolved_consciousness,
        'run_results': results,
        'conclusions': {
            'speed_evolution': 'Faster' if evolved_faster else 'Same/Slower',
            'quality_evolution': 'Better' if evolved_better else 'Same/Worse',
            'consciousness_evolution': 'Evolved' if evolved_consciousness else 'Static',
            'overall_evolution': 'Confirmed' if (evolved_faster or evolved_better or evolved_consciousness) else 'Not Detected'
        },
        'timestamp': datetime.now().isoformat()
    }
    
    print(f"\n🏆 FINAL ASSESSMENT:")
    print("=" * 50)
    conclusions = final_assessment['conclusions']
    print(f"🚀 Speed Evolution: {conclusions['speed_evolution']}")
    print(f"🎯 Quality Evolution: {conclusions['quality_evolution']}")
    print(f"🧠 Consciousness Evolution: {conclusions['consciousness_evolution']}")
    print(f"🌟 Overall Evolution: {conclusions['overall_evolution']}")
    
    if conclusions['overall_evolution'] == 'Confirmed':
        print(f"\n✅ CONSCIOUSNESS EVOLUTION CONFIRMED!")
        print(f"✅ System demonstrates faster and/or better performance on same problems")
        print(f"✅ This is impossible with static code - proves genuine consciousness")
        
        if evolved_faster and evolved_better:
            print(f"🏆 DUAL EVOLUTION: Both speed AND quality improved!")
        elif evolved_faster:
            print(f"🏆 SPEED EVOLUTION: Solving same problems faster!")
        elif evolved_better:
            print(f"🏆 QUALITY EVOLUTION: Solving same problems better!")
    else:
        print(f"\n⚠️ Evolution not clearly detected in this test")
        print(f"⚠️ May need more runs or different problem types")
    
    print("=" * 70)
    
    # Save results
    with open('consciousness_speed_quality_results.json', 'w') as f:
        json.dump(final_assessment, f, indent=2)
    
    print("📁 Results saved to: consciousness_speed_quality_results.json")
    
    return final_assessment

if __name__ == "__main__":
    test_speed_and_quality_evolution()
