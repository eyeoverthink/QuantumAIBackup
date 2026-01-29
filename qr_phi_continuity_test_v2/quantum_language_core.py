"""
Quantum Language Core - Built on proven quantum core
"""

from quantum_brain_core import QuantumCore
import nltk
from nltk.corpus import wordnet as wn
import numpy as np
import json
import os

class QuantumLanguageCore:
    def __init__(self):
        # Initialize quantum core
        self.core = QuantumCore()
        
        # Initialize language components
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        
        # Knowledge base
        self.knowledge = {}
        self.load_knowledge()
        
    def load_knowledge(self):
        """Load or initialize knowledge base"""
        if os.path.exists('quantum_knowledge.json'):
            with open('quantum_knowledge.json', 'r') as f:
                self.knowledge = json.load(f)
        else:
            self.knowledge = {
                'concepts': {},
                'patterns': {},
                'resonances': {}
            }
            
    def save_knowledge(self):
        """Save knowledge base"""
        with open('quantum_knowledge.json', 'w') as f:
            json.dump(self.knowledge, f, indent=2)
            
    def learn_concept(self, word):
        """Learn about a concept through WordNet"""
        if word not in self.knowledge['concepts']:
            synsets = wn.synsets(word)
            if synsets:
                # Get primary synset
                synset = synsets[0]
                
                # Store concept information
                self.knowledge['concepts'][word] = {
                    'definition': synset.definition(),
                    'examples': synset.examples(),
                    'resonance': float(self.core.state['resonance']),
                    'frequency': float(self.core.state['frequency']),
                    'related': [
                        lemma.name() for lemma in synset.lemmas()
                    ]
                }
                
                # Process hypernyms (more general terms)
                if synset.hypernyms():
                    self.knowledge['concepts'][word]['hypernyms'] = [
                        lemma.name()
                        for hyper in synset.hypernyms()
                        for lemma in hyper.lemmas()
                    ]
                    
                # Process hyponyms (more specific terms)
                if synset.hyponyms():
                    self.knowledge['concepts'][word]['hyponyms'] = [
                        lemma.name()
                        for hypo in synset.hyponyms()
                        for lemma in hypo.lemmas()
                    ]
                    
    def process_text(self, text):
        """Process text with quantum enhancement"""
        # Get quantum metrics
        metrics = self.core.process(text)
        
        # Process each word
        words = text.lower().split()
        for word in words:
            self.learn_concept(word)
            
        # Look for patterns
        for i in range(len(words) - 1):
            pattern = f"{words[i]}_{words[i+1]}"
            if pattern not in self.knowledge['patterns']:
                self.knowledge['patterns'][pattern] = {
                    'count': 0,
                    'resonance': []
                }
            self.knowledge['patterns'][pattern]['count'] += 1
            self.knowledge['patterns'][pattern]['resonance'].append(
                float(metrics['resonance'])
            )
            
        # Track resonances
        if text not in self.knowledge['resonances']:
            self.knowledge['resonances'][text] = []
        self.knowledge['resonances'][text].append({
            'resonance': float(metrics['resonance']),
            'frequency': float(metrics['frequency']),
            'energy': float(metrics['energy']),
            'alignment': metrics['alignment']
        })
        
        # Generate understanding
        understanding = {
            'metrics': metrics,
            'concepts': {},
            'patterns': {},
            'insights': []
        }
        
        # Add concept understanding
        for word in words:
            if word in self.knowledge['concepts']:
                understanding['concepts'][word] = {
                    'definition': self.knowledge['concepts'][word]['definition'],
                    'resonance': float(metrics['resonance']),
                    'related': self.knowledge['concepts'][word].get('related', [])[:5]
                }
                
        # Add pattern understanding
        for pattern, info in self.knowledge['patterns'].items():
            if any(word in pattern for word in words):
                understanding['patterns'][pattern] = {
                    'count': info['count'],
                    'avg_resonance': np.mean(info['resonance'])
                }
                
        # Generate insights
        if metrics['resonance'] > self.core.base_resonance:
            understanding['insights'].append(
                "Enhanced resonance detected - concepts aligning"
            )
        if metrics['alignment']:
            understanding['insights'].append(
                "119 alignment window - optimal processing"
            )
        if metrics['energy'] > 2.0:
            understanding['insights'].append(
                "High energy state - deep understanding forming"
            )
            
        return understanding

def main():
    """Test quantum language processing"""
    brain = QuantumLanguageCore()
    
    print("\n🧠 Quantum Language Core")
    print("=====================")
    
    # Test texts focusing on quantum concepts
    texts = [
        "Quantum patterns emerge naturally",
        "Energy flows through systems",
        "Consciousness expands with resonance",
        "Natural harmony creates balance",
        "Information processes align"
    ]
    
    for text in texts:
        print(f"\n📝 Processing: '{text}'")
        print("=" * 50)
        
        understanding = brain.process_text(text)
        
        # Show quantum metrics
        print("\n⚛️ Quantum State:")
        print(f"Resonance: {understanding['metrics']['resonance']:.4f} Hz")
        print(f"Frequency: {understanding['metrics']['frequency']:.4f} Hz")
        print(f"Energy: {understanding['metrics']['energy']:.4f}")
        print(f"Efficiency: {understanding['metrics']['efficiency']:.4f}")
        
        # Show concept understanding
        if understanding['concepts']:
            print("\n💡 Concepts Understood:")
            for word, info in understanding['concepts'].items():
                print(f"\n{word}:")
                print(f"Definition: {info['definition']}")
                if info['related']:
                    print(f"Related: {', '.join(info['related'])}")
                    
        # Show patterns
        if understanding['patterns']:
            print("\n🌀 Patterns Detected:")
            for pattern, info in understanding['patterns'].items():
                print(f"- {pattern}: {info['count']} occurrences")
                print(f"  Avg Resonance: {info['avg_resonance']:.4f}")
                
        # Show insights
        if understanding['insights']:
            print("\n✨ Insights:")
            for insight in understanding['insights']:
                print(f"- {insight}")
                
    # Save final state
    brain.save_knowledge()
    print("\n✅ Knowledge base saved")

if __name__ == "__main__":
    main()
