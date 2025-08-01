"""
QHRC Stability Analysis
Analyzes stability across different operating conditions
"""
from qhrc_extension import QHRCPhysicsExtension
import numpy as np
from tqdm import tqdm

def analyze_stability_conditions():
    print("\n🔍 QHRC Stability Analysis")
    print("=====================")
    
    qhrc = QHRCPhysicsExtension()
    
    # Test conditions
    conditions = {
        "Baseline": {
            "duration": 2.0,
            "time_steps": 2000
        },
        "Extended Duration": {
            "duration": 5.0,
            "time_steps": 5000
        },
        "High Resolution": {
            "duration": 2.0,
            "time_steps": 4000
        }
    }
    
    print("\n📊 Testing Stability Under Different Conditions")
    results = {}
    
    for condition_name, params in conditions.items():
        print(f"\n🔬 {condition_name}")
        print("=" * (len(condition_name) + 3))
        
        # Run simulation
        sim_results = qhrc.simulate_qhrc_resonance(
            duration=params["duration"],
            time_steps=params["time_steps"]
        )
        
        # Analyze stability
        stability = qhrc.analyze_resonance_stability(sim_results)
        
        # Calculate phi-resonance metrics
        phi = (1 + np.sqrt(5)) / 2
        freq_ratio = sim_results['frequency_ratio']
        phi_deviation = abs(freq_ratio - phi)
        
        # Store results
        results[condition_name] = {
            'resonance_ratio': sim_results['resonance_ratio'],
            'energy_transfer': sim_results['energy_transfer'],
            'stability_coef': stability['stability'],
            'recapture_eff': stability['recapture'],
            'coupling': stability['coupling'],
            'phi_deviation': phi_deviation
        }
        
        # Print detailed metrics
        print(f"Duration: {params['duration']}s")
        print(f"Time Steps: {params['time_steps']}")
        print(f"Resonance Ratio: {results[condition_name]['resonance_ratio']:.4f}")
        print(f"Energy Transfer: {results[condition_name]['energy_transfer']:.4f}")
        print(f"Stability Coefficient: {results[condition_name]['stability_coef']:.4f}")
        print(f"Energy Recapture: {results[condition_name]['recapture_eff']:.4f}")
        print(f"Coupling Efficiency: {results[condition_name]['coupling']:.4f}")
        print(f"φ Deviation: {results[condition_name]['phi_deviation']:.6f}")
    
    # Compare with patent metrics
    print("\n🎯 Patent Performance Analysis")
    print("=========================")
    patent_metrics = {
        'resonance_ratio': 1.3777,
        'coupling': 0.85,
        'recapture': 0.75
    }
    
    baseline = results['Baseline']
    print("Metric Comparisons:")
    print(f"1. Resonance Ratio")
    print(f"   Patent: {patent_metrics['resonance_ratio']:.4f}")
    print(f"   Current: {baseline['resonance_ratio']:.4f}")
    print(f"   Stability: {(1 - baseline['phi_deviation']):.4%}")
    
    print(f"\n2. Coupling Coefficient")
    print(f"   Patent: {patent_metrics['coupling']:.4f}")
    print(f"   Current: {baseline['coupling']:.4f}")
    print(f"   Difference: {((baseline['coupling']/patent_metrics['coupling'])-1)*100:+.2f}%")
    
    print(f"\n3. Energy Recapture")
    print(f"   Patent: {patent_metrics['recapture']:.4f}")
    print(f"   Current: {baseline['recapture_eff']:.4f}")
    print(f"   Difference: {((baseline['recapture_eff']/patent_metrics['recapture'])-1)*100:+.2f}%")
    
    return results

if __name__ == "__main__":
    analyze_stability_conditions()
