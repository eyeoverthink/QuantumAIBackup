"""
Test the trained Quantum Language Brain
"""

import torch
from quantum_language_brain import QuantumLanguageBrain

def test_brain():
    # Load trained model
    model = QuantumLanguageBrain()
    model.load_state_dict(torch.load("quantum_brain_models/quantum_brain.pt"))
    model.eval()
    
    # Test prompts
    prompts = [
        "Quantum systems exhibit",
        "The golden ratio appears",
        "Neural networks learn through",
        "Energy patterns resonate at",
        "Information flows through quantum",
        "Natural systems find balance through",
        "The observer effect creates",
        "Harmonic frequencies align with"
    ]
    
    print("\n🧠 Testing Quantum Language Brain")
    print("==============================")
    
    for prompt in prompts:
        print(f"\nPrompt: '{prompt}'")
        state = model.quantum_process(prompt)
        
        print("\nPredictions:")
        for word, prob in state['predictions'][:3]:
            print(f"- {word}: {prob:.4f}")
        
        print("\nQuantum Metrics:")
        print(f"Phi Harmony: {state['phi_harmony']:.4f}")
        print(f"Energy Level: {state['energy_level']:.4f}")
        print(f"Resonance: {state['resonance']:.4f}")
        print("-" * 50)

if __name__ == "__main__":
    test_brain()
