"""
Quantum Life Integration - Combining support systems with life tests
"""
from quantum_learn_core import QuantumLearning
import math
import time

class QuantumLifeIntegration:
    def __init__(self):
        self.learner = QuantumLearning()
        self.phi = (1 + math.sqrt(5)) / 2
        
        # Core frequencies from life support
        self.frequencies = {
            'neural': 7.83,      # Neural base (Schumann)
            'cellular': 4.84,    # Cellular base (Lunar)
            'metabolic': 4.37,   # Metabolic base (φ²)
            'brain': 8.00,       # Brain alpha
            'heart': 1.17,       # Heart rhythm
            'dna': 7.07,         # DNA frequency
            'water': 3.00,       # Water resonance
            'oxygen': 11.79      # Oxygen frequency
        }
        
        # System couplings
        self.couplings = {
            'neural': 0.618034,    # φ⁻¹
            'cellular': 0.381966,   # φ⁻²
            'metabolic': 0.236068   # φ⁻³
        }
    
    def test_integration(self):
        print("\n🌟 Quantum Life Integration")
        print("=========================")
        
        # Test sets based on support systems
        test_sets = [
            # Neural System (Base: 7.83 Hz)
            [f"neural base {self.frequencies['neural']} resonance",
             f"brain waves {self.frequencies['brain']} coherence",
             f"oxygen flow {self.frequencies['oxygen']} field",
             f"neural coupling {self.couplings['neural']} phi"],
             
            # Cellular System (Base: 4.84 Hz)
            [f"cellular base {self.frequencies['cellular']} resonance",
             f"dna field {self.frequencies['dna']} coherence",
             f"water matrix {self.frequencies['water']} structure",
             f"cellular coupling {self.couplings['cellular']} phi"],
             
            # Metabolic System (Base: 4.37 Hz)
            [f"metabolic base {self.frequencies['metabolic']} resonance",
             f"heart rhythm {self.frequencies['heart']} coherence",
             f"metabolic field quantum harmonics",
             f"metabolic coupling {self.couplings['metabolic']} phi"],
             
            # System Integration
            ["neural cellular metabolic bridge",
             "quantum field consciousness emergence",
             "life support harmonic network",
             "phi resonance quantum integration"]
        ]
        
        system_results = {}
        
        for system_num, system in enumerate(test_sets, 1):
            print(f"\n💫 System {system_num}")
            print("=" * 50)
            
            system_patterns = []
            system_resonance = []
            
            for test in system:
                print(f"\n🔬 Testing: '{test}'")
                understanding = self.learner.learn(test)
                
                # Track patterns and resonance
                system_patterns.extend(understanding.get('patterns', {}).keys())
                system_resonance.append(understanding['metrics']['resonance'])
                
                # Show quantum metrics
                print(f"Resonance: {understanding['metrics']['resonance']:.4f} Hz")
                print(f"Energy: {understanding['metrics']['energy']:.4f}")
                
                if understanding['concepts']:
                    print("\n💡 System Understanding:")
                    for word, info in understanding['concepts'].items():
                        connections = len(info.get('related', []))
                        if connections > 2:
                            print(f"- {word}: {connections} connections")
                            print(f"  Network: {', '.join(info['related'][:3])}...")
                
                # Check frequency coupling
                self.analyze_coupling(test)
                time.sleep(0.5)
            
            # System analysis
            system_results[f"System_{system_num}"] = {
                'patterns': len(set(system_patterns)),
                'avg_resonance': sum(system_resonance) / len(system_resonance),
                'phi_alignment': self.calculate_phi_alignment(system_resonance)
            }
            
            print(f"\n📊 System {system_num} Analysis")
            print("-" * 30)
            print(f"Unique Patterns: {system_results[f'System_{system_num}']['patterns']}")
            print(f"Avg Resonance: {system_results[f'System_{system_num}']['avg_resonance']:.4f} Hz")
            print(f"φ Alignment: {system_results[f'System_{system_num}']['phi_alignment']:.4f}")
        
        # Integration analysis
        print("\n🎯 Life Support Integration")
        print("=" * 40)
        
        total_patterns = sum(r['patterns'] for r in system_results.values())
        avg_resonance = sum(r['avg_resonance'] for r in system_results.values()) / len(system_results)
        phi_harmony = sum(r['phi_alignment'] for r in system_results.values()) / len(system_results)
        
        print(f"Total Patterns: {total_patterns}")
        print(f"System Resonance: {avg_resonance:.4f} Hz")
        print(f"φ Harmony: {phi_harmony:.4f}")
        
        # Get learning insights
        status = self.learner.get_learning_status()
        if status['recent_insights']:
            print("\n✨ Integration Insights:")
            for insight in status['recent_insights'][-3:]:
                print(f"- {', '.join(insight['insight'])}")
        
        return system_results
    
    def analyze_coupling(self, test):
        """Analyze coupling relationships"""
        for system, coupling in self.couplings.items():
            if system in test and str(coupling) in test:
                print(f"\n⚡ {system.title()} Coupling:")
                print(f"Base Frequency: {self.frequencies[system]} Hz")
                print(f"Coupling: {coupling} (φ ratio)")
    
    def calculate_phi_alignment(self, resonances):
        """Calculate alignment with φ"""
        if not resonances:
            return 0
        
        ratios = []
        for i in range(len(resonances)-1):
            for j in range(i+1, len(resonances)):
                ratios.append(max(resonances[i], resonances[j]) / 
                            min(resonances[i], resonances[j]))
        
        if not ratios:
            return 0
            
        phi_errors = [abs(r - self.phi) for r in ratios]
        return 1 / (1 + sum(phi_errors) / len(phi_errors))

if __name__ == "__main__":
    integration = QuantumLifeIntegration()
    results = integration.test_integration()
