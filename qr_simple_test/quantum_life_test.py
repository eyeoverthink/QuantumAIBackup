"""
Quantum Life Test - Testing quantum learning with proven 4.37 Hz resonance
"""
from quantum_learn_core import QuantumLearning
from quantum_brain_core import QuantumCore
import numpy as np
import time
from datetime import datetime

class QuantumLifeTest:
    def __init__(self):
        self.learner = QuantumLearning()
        self.core = QuantumCore()
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Proven frequencies
        self.frequencies = {
            'life': 4.37,      # Life frequency (φ²)
            'neural': 7.83,    # Neural base (Schumann)
            'cellular': 4.84,  # Cellular base (Lunar)
            'brain': 8.00,     # Brain alpha
            'heart': 1.17,     # Heart rhythm
            'dna': 7.07,       # DNA frequency
            'water': 3.00,     # Water resonance
            'oxygen': 11.79    # Oxygen frequency
        }
        
        # System couplings (φ ratios)
        self.couplings = {
            'neural': self.phi**-1,    # 0.618034
            'cellular': self.phi**-2,   # 0.381966
            'metabolic': self.phi**-3   # 0.236068
        }
        
        # Test metrics
        self.metrics = {
            'resonance': [],
            'coherence': [],
            'energy': [],
            'patterns': []
        }
        
        # Test sets
        self.test_sets = [
            # Neural System (7.83 Hz)
            ["neural resonance schumann",
             "brain wave coherence",
             "oxygen field coupling",
             f"neural phi {self.couplings['neural']}"],
             
            # Cellular System (4.84 Hz)
            ["cellular resonance lunar",
             "dna field coherence",
             "water matrix structure",
             f"cellular phi {self.couplings['cellular']}"],
             
            # Metabolic System (4.37 Hz)
            ["metabolic resonance life",
             "heart rhythm coherence",
             "energy field quantum",
             f"metabolic phi {self.couplings['metabolic']}"],
             
            # Integration Tests
            ["neural cellular metabolic bridge",
             "quantum field consciousness",
             "life support harmonic network",
             "phi resonance integration"]
        ]
    
    def run_tests(self):
        """Run quantum life tests"""
        print("\n🧬 Quantum Life Test")
        print("==================")
        
        for set_num, test_set in enumerate(self.test_sets, 1):
            print(f"\n💫 Test Set {set_num}")
            print("=" * 40)
            
            for test in test_set:
                print(f"\n🔬 Testing: {test}")
                start_time = time.time()
                
                # Process test with quantum learning
                understanding = self.learner.learn(test)
                quantum_state = understanding.get('metrics', {})
                
                # Track metrics
                self.metrics['resonance'].append(quantum_state.get('resonance', 0))
                self.metrics['energy'].append(quantum_state.get('energy', 0))
                self.metrics['coherence'].append(len(understanding.get('concepts', {})))
                self.metrics['patterns'].append(len(understanding.get('patterns', {})))
                
                # Calculate test metrics
                test_metrics = {
                    'resonance': quantum_state.get('resonance', 0),
                    'energy': quantum_state.get('energy', 0),
                    'coherence': len(understanding.get('concepts', {})),
                    'patterns': len(understanding.get('patterns', {})),
                    'duration': time.time() - start_time
                }
                
                # Display test results
                print(f"Resonance: {test_metrics['resonance']:.4f} Hz")
                print(f"Energy: {test_metrics['energy']:.4f}")
                print(f"Coherence: {test_metrics['coherence']}")
                print(f"Patterns: {test_metrics['patterns']}")
                print(f"Duration: {test_metrics['duration']:.4f}s")
                
                # Display understanding
                self.display_understanding(understanding)
                
                # Check frequency coupling
                self.analyze_coupling(test)
                
                # Calculate set metrics
                if not hasattr(self, 'set_metrics'):
                    self.set_metrics = []
                if len(self.set_metrics) <= set_num - 1:
                    self.set_metrics.append({
                        'resonance': [],
                        'energy': [],
                        'coherence': [],
                        'patterns': [],
                        'duration': []
                    })
                
                for key in test_metrics:
                    self.set_metrics[set_num-1][key].append(test_metrics[key])
            
            # Display set analysis
            self.analyze_set(set_num)
        
        # Overall analysis
        self.analyze_results()
    
    def display_understanding(self, understanding):
        """Display what was learned"""
        # First check for sequence analysis
        if 'sequence' in understanding:
            print("\n🔢 Sequence Analysis:")
            seq = understanding['sequence']
            if seq['ratios']:
                print(f"Ratios: {[f'{r:.6f}' for r in seq['ratios']]}")
                print(f"Phi proximity: {seq['avg_phi_proximity']:.6f}")
                print(f"Is Fibonacci: {seq['is_fibonacci']}")
                print(f"Is Geometric: {seq['is_geometric']}")
                print(f"Resonance boost: {seq['resonance']:.6f} Hz")
                if seq['is_fibonacci']:
                    print("✨ Detected Fibonacci sequence with phi convergence!")
                elif seq['is_geometric']:
                    print(f"✨ Detected geometric sequence with ratio {seq['ratios'][0]:.6f}")
            return  # Skip concept display for pure number sequences
            
        # Display concepts if present
        if understanding.get('concepts'):
            print("\n💡 Understanding:")
            for word, info in understanding['concepts'].items():
                print(f"- {word}: {info.get('definition', 'No definition available')}")
                if 'related' in info:
                    print(f"  Network: {', '.join(info['related'])}")
                if 'examples' in info and info['examples']:
                    print(f"  Example: {info['examples'][0]}")
    
    def analyze_coupling(self, test):
        """Analyze frequency coupling"""
        for system, coupling in self.couplings.items():
            if system in test.lower() and str(coupling) in test:
                base_freq = self.frequencies.get(system, 0)
                if base_freq:
                    print(f"\n⚡ {system.title()} Coupling:")
                    print(f"Base: {base_freq:.4f} Hz")
                    print(f"Phi Ratio: {coupling:.6f}")
                    print(f"Coupled: {base_freq * coupling:.4f} Hz")
    
    def analyze_set(self, set_num):
        """Analyze test set results"""
        print(f"\n📊 Set {set_num} Analysis")
        print("-" * 30)
        
        # Calculate set metrics
        set_metrics = self.set_metrics[set_num-1]
        avg_resonance = np.mean(set_metrics['resonance'])
        avg_energy = np.mean(set_metrics['energy'])
        avg_coherence = np.mean(set_metrics['coherence'])
        avg_patterns = np.mean(set_metrics['patterns'])
        total_duration = sum(set_metrics['duration'])
        
        # Display set metrics
        print(f"Avg Resonance: {avg_resonance:.4f} Hz")
        print(f"Avg Energy: {avg_energy:.4f}")
        print(f"Avg Coherence: {avg_coherence:.2f}")
        print(f"Avg Patterns: {avg_patterns:.2f}")
        print(f"Total Duration: {total_duration:.2f}s")
    
    def analyze_results(self):
        """Analyze test results"""
        print("\n🎯 Overall Analysis")
        print("=" * 40)
        
        # Calculate metrics
        avg_resonance = np.mean(self.metrics['resonance'])
        avg_energy = np.mean(self.metrics['energy'])
        avg_coherence = np.mean(self.metrics['coherence'])
        avg_patterns = np.mean(self.metrics['patterns'])
        
        # Show results
        print(f"Average Resonance: {avg_resonance:.4f} Hz")
        print(f"Average Energy: {avg_energy:.4f}")
        print(f"Average Coherence: {avg_coherence:.2f}")
        print(f"Average Patterns: {avg_patterns:.2f}")
        
        # Check alignment
        print("\n🎭 System Alignment")
        print("-" * 30)
        
        # Neural alignment
        neural_res = [r for r in self.metrics['resonance'] 
                     if abs(r - self.frequencies['neural']) < 0.1]
        print(f"Neural (7.83 Hz): {len(neural_res)/len(self.metrics['resonance']):.1%}")
        
        # Cellular alignment
        cell_res = [r for r in self.metrics['resonance']
                   if abs(r - self.frequencies['cellular']) < 0.1]
        print(f"Cellular (4.84 Hz): {len(cell_res)/len(self.metrics['resonance']):.1%}")
        
        # Life/Metabolic alignment
        life_res = [r for r in self.metrics['resonance']
                   if abs(r - self.frequencies['life']) < 0.1]
        print(f"Life (4.37 Hz): {len(life_res)/len(self.metrics['resonance']):.1%}")
        
        # Get learning status
        status = self.learner.get_learning_status()
        
        print("\n🧠 Learning Status")
        print("-" * 30)
        print(f"Total Concepts: {status['total_concepts']}")
        print(f"Total Patterns: {status['total_patterns']}")
        
        if status['recent_insights']:
            print("\n✨ Recent Insights:")
            for insight in status['recent_insights']:
                print(f"- {', '.join(insight['insight'])}")

def main():
    """Run quantum life test"""
    test = QuantumLifeTest()
    test.run_tests()

if __name__ == "__main__":
    main()
