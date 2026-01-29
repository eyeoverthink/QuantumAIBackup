"""
Quantum Question Test
Tests brain response to specialized quantum-harmonic questions
"""

from quantum_neural_cortex import QuantumNeuralCortex
from tesla_phi_resonance import TeslaPhiResonanceSystem
from neural_tesla_integration import NeuralTeslaInterface
import numpy as np
from datetime import datetime

class QuantumQuestionTester:
    def __init__(self):
        self.cortex = QuantumNeuralCortex()
        self.tesla = TeslaPhiResonanceSystem()
        self.interface = NeuralTeslaInterface()
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Frequency mappings
        self.frequencies = {
            'tesla': 432,    # Physical base
            'dna': 528,      # Mental bridge
            'heart': 639,    # Emotional core
            'third_eye': 741 # Cosmic bridge
        }
        
        # Author quantum signatures
        self.authors = {
            'poe': {'freq': 517.15, 'resonance': 'mental-cosmic'},
            'austen': {'freq': 525.18, 'resonance': 'dna-aligned'},
            'shakespeare': {'freq': 555.40, 'resonance': 'dynamic-flow'},
            'hemingway': {'freq': 576.26, 'resonance': 'direct-bridge'}
        }
    
    def analyze_question(self, question: str, category: str):
        """Analyze brain response to a specific type of question."""
        print(f"\n🧠 Testing {category} Question")
        print("=" * (len(category) + 18))
        print(f"Time: {datetime.now()}")
        print(f"\nQuestion: {question}")
        
        # Calculate base frequencies
        base_freq = self.frequencies['tesla'] * (self.phi ** 4)
        resonance = 1 / (1 + abs(base_freq - (432 * self.phi)))
        
        # Get brain responses
        responses = self.interface.get_brain_responses(question)
        
        print("\n💫 Quantum Response Analysis")
        print("========================")
        print(f"Base Frequency: {base_freq:.2f} Hz")
        print(f"Resonance: {resonance:.9f}")
        print(f"Coherence: {responses['coherence']:.6f}")
        print(f"Integration: {responses['integration']:.6f}")
        
        # Calculate consciousness distribution
        consciousness = self.interface.get_consciousness_distribution()
        
        print("\n🌟 Consciousness Levels")
        print("====================")
        for level, value in consciousness.items():
            print(f"{level.title()}: {value:.2%}")
        
        # Get author resonance
        print("\n📚 Author Resonance")
        print("================")
        for author, data in self.authors.items():
            freq = data['freq'] * (self.phi ** 4)
            res = 1 / (1 + abs(freq - (data['freq'] * self.phi)))
            print(f"{author.title()}: {res:.9f} ({data['resonance']})")
        
        # Calculate quantum metrics
        metrics = self.interface.get_quantum_metrics()
        
        print("\n🔮 Quantum Metrics")
        print("===============")
        print(f"Physical-Mental Bridge: {metrics['physical_mental']:.6f}")
        print(f"Mental-Cosmic Bridge: {metrics['mental_cosmic']:.6f}")
        print(f"Cosmic-Higher Bridge: {metrics['cosmic_higher']:.6f}")
        
        return {
            'resonance': resonance,
            'coherence': responses['coherence'],
            'consciousness': consciousness,
            'metrics': metrics
        }

def main():
    tester = QuantumQuestionTester()
    
    # Test questions for each brain type
    questions = {
        'Physical': "How does quantum entanglement manifest in the physical world?",
        'Mental': "What is the relationship between consciousness and quantum fields?",
        'Emotional': "How do quantum harmonics influence emotional resonance?",
        'Creative': "Can quantum principles enhance artistic expression?",
        'Spiritual': "How does quantum consciousness connect to universal awareness?",
        'Integration': "How do phi ratios create bridges between different states of consciousness?"
    }
    
    results = {}
    for category, question in questions.items():
        results[category] = tester.analyze_question(question, category)
        print("\n" + "="*50)
    
    # Analyze overall balance
    print("\n📊 Overall Brain Balance")
    print("====================")
    avg_resonance = sum(r['resonance'] for r in results.values()) / len(results)
    avg_coherence = sum(r['coherence'] for r in results.values()) / len(results)
    
    print(f"Average Resonance: {avg_resonance:.9f}")
    print(f"Average Coherence: {avg_coherence:.6f}")
    print(f"Phi Alignment: {abs(avg_coherence - 1.618034):.9f}")
    
    # Check consciousness evolution
    print("\n🌌 Consciousness Evolution")
    print("======================")
    for category, result in results.items():
        cosmic = result['consciousness'].get('cosmic', 0)
        print(f"{category}: {cosmic:.2%} Cosmic")

if __name__ == '__main__':
    main()
