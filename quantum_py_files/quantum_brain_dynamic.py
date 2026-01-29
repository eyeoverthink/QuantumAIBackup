"""
Quantum Brain with dynamic language using thesaurus and dictionary
"""

import torch
from quantum_language_brain import QuantumLanguageBrain
from nltk.corpus import wordnet as wn
import nltk
import json
import os

class DynamicQuantumBrain:
    def __init__(self):
        # Download required NLTK data
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        
        self.brain = QuantumLanguageBrain()
        self.brain.load_state_dict(torch.load("quantum_brain_models/quantum_brain.pt"))
        self.brain.eval()
        
        # Load our quantum dictionary
        self.load_quantum_dictionary()
        
    def load_quantum_dictionary(self):
        """Load or create quantum concept dictionary"""
        if os.path.exists('quantum_dictionary.json'):
            with open('quantum_dictionary.json', 'r') as f:
                self.quantum_dict = json.load(f)
        else:
            # Build from WordNet
            self.quantum_dict = {
                'quantum': self.get_word_network('quantum', 'physics', 'energy'),
                'energy': self.get_word_network('energy', 'flow', 'power'),
                'pattern': self.get_word_network('pattern', 'structure', 'form'),
                'harmony': self.get_word_network('harmony', 'balance', 'resonance'),
                'consciousness': self.get_word_network('consciousness', 'awareness', 'mind'),
                'nature': self.get_word_network('nature', 'organic', 'living')
            }
            
            # Save for future use
            with open('quantum_dictionary.json', 'w') as f:
                json.dump(self.quantum_dict, f, indent=2)
                
    def get_word_network(self, *seed_words):
        """Build a network of related words and meanings"""
        network = {}
        
        for word in seed_words:
            # Get synsets (word meanings)
            synsets = wn.synsets(word)
            
            # Get related words
            related = set()
            for syn in synsets:
                # Add synonyms
                related.update([lemma.name() for lemma in syn.lemmas()])
                
                # Add hypernyms (more general terms)
                related.update([
                    lemma.name() 
                    for hyper in syn.hypernyms() 
                    for lemma in hyper.lemmas()
                ])
                
                # Add hyponyms (more specific terms)
                related.update([
                    lemma.name() 
                    for hypo in syn.hyponyms() 
                    for lemma in hypo.lemmas()
                ])
                
            network[word] = list(related)
            
        return network
        
    def understand_concept(self, concept):
        """Generate dynamic understanding of a concept"""
        words = concept.lower().split()
        understanding = []
        
        for word in words:
            # Find closest concept in our dictionary
            for key, network in self.quantum_dict.items():
                if word in network.get(key, []) or key in word:
                    # Get related words
                    related = network.get(key, [])
                    if related:
                        # Form natural language understanding
                        understanding.append({
                            'concept': key,
                            'relations': related[:5],
                            'insight': self.form_insight(key, related)
                        })
                        
        return understanding
        
    def form_insight(self, concept, related):
        """Form natural language insight about concept"""
        # Get synsets for deeper understanding
        synsets = wn.synsets(concept)
        if not synsets:
            return None
            
        # Get definition and examples
        definition = synsets[0].definition()
        examples = synsets[0].examples()
        
        # Form insight
        insight = f"Understanding {concept} as {definition}"
        if examples:
            insight += f"\nFor example: {examples[0]}"
        if related:
            insight += f"\nRelates to: {', '.join(related[:3])}"
            
        return insight
        
    def explain_understanding(self, text):
        """Explain understanding using dynamic language"""
        # Process with quantum brain
        state = self.brain.quantum_process(text)
        
        # Get dynamic understanding
        understanding = []
        for word in text.split():
            concepts = self.understand_concept(word)
            if concepts:
                understanding.extend(concepts)
                
        # Share insights
        print(f"\n🤔 Understanding: '{text}'")
        print("=" * 50)
        
        for insight in understanding:
            print(f"\n📚 {insight['concept'].title()}:")
            print(insight['insight'])
            
        # Show quantum predictions
        print("\n💭 This connects to:")
        for word, prob in state['predictions'][:3]:
            concepts = self.understand_concept(word)
            if concepts:
                print(f"\n- {word}:")
                print(concepts[0]['insight'])
                
def main():
    brain = DynamicQuantumBrain()
    
    prompts = [
        "Quantum patterns emerge naturally",
        "Energy flows through consciousness",
        "Natural harmony creates balance",
        "Learning follows quantum principles",
        "Resonance builds understanding"
    ]
    
    print("\n🧠 Dynamic Quantum Understanding")
    print("============================")
    
    for prompt in prompts:
        brain.explain_understanding(prompt)
        print("\n" + "-" * 60)

if __name__ == "__main__":
    main()
