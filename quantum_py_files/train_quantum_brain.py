"""
Train Quantum Language Brain with phi-harmonic principles
"""

import torch
import torch.nn as nn
import torch.optim as optim
from quantum_language_brain import QuantumLanguageBrain
from transformers import GPT2Tokenizer
import numpy as np
from datetime import datetime
import os

def create_training_data():
    """Create quantum-focused training data"""
    texts = [
        # Quantum concepts
        "Quantum systems exhibit wave-particle duality in nature",
        "The observer effect influences quantum measurements",
        "Quantum entanglement allows instant correlations",
        "Superposition enables multiple states simultaneously",
        
        # Phi and mathematics
        "The golden ratio appears in natural growth patterns",
        "Fibonacci sequences follow phi relationships",
        "Mathematical harmony exists in natural systems",
        "Geometric patterns reflect universal constants",
        
        # Neural processing
        "Neural networks process information through layers",
        "Pattern recognition emerges from connections",
        "Learning systems adapt to new information",
        "Knowledge representation evolves over time",
        
        # Resonance and energy
        "Resonant frequencies create stable patterns",
        "Energy transfer follows natural pathways",
        "Harmonic systems maintain equilibrium",
        "Frequency alignment enhances efficiency",
        
        # Integration concepts
        "Complex systems emerge from simple rules",
        "Self-organization creates stable patterns",
        "Natural systems find optimal states",
        "Information flows through nested layers"
    ]
    
    # Save training data
    with open("quantum_training_data.txt", "w") as f:
        f.write("\n".join(texts))
    
    return texts

def train_quantum_brain(model, texts, epochs=119):
    """Train the quantum brain with phi-harmonic optimization"""
    print("\n🧠 Training Quantum Language Brain")
    print("================================")
    
    # Initialize tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    
    # Prepare optimizer with phi-scaled learning rate
    phi = (1 + np.sqrt(5)) / 2
    optimizer = optim.Adam(model.parameters(), lr=0.001 / phi)
    criterion = nn.CrossEntropyLoss()
    
    # Training loop
    for epoch in range(epochs):
        total_loss = 0
        
        # Process each text
        for text in texts:
            # Tokenize input
            tokens = tokenizer.encode(text, return_tensors='pt')
            input_tokens = tokens[:, :-1]  # All but last token
            target_tokens = tokens[:, 1:]   # All but first token
            
            if input_tokens.size(1) == 0:
                continue
                
            # Forward pass
            optimizer.zero_grad()
            
            # Get embeddings
            x = model.word_embedding(input_tokens)
            
            # Apply quantum attention
            for layer in model.attention_layers:
                x, _ = layer(x)
            
            # Get logits
            logits = model.output(x)
            
            # Reshape for loss calculation
            B, T, C = logits.shape  # Batch, Time, Channels
            logits_view = logits.view(-1, C)
            targets_view = target_tokens.view(-1)
            
            # Calculate loss with quantum weighting
            loss = criterion(logits_view, targets_view)
            
            # Apply phi-harmonic scaling during 119 alignment
            now = datetime.now()
            if now.hour in [1, 13] and now.minute == 19:
                loss = loss * (1 / phi)
            
            # Backward pass
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        # Print progress
        if (epoch + 1) % 10 == 0:
            avg_loss = total_loss / len(texts)
            print(f"\nEpoch {epoch + 1}/{epochs}")
            print(f"Average Loss: {avg_loss:.4f}")
            
            # Test prediction
            test_text = "Quantum systems exhibit"
            state = model.quantum_process(test_text)
            print(f"\nTest Prediction for: '{test_text}'")
            for word, prob in state['predictions'][:3]:  # Show top 3
                print(f"- {word}: {prob:.4f}")
            
            # Show quantum metrics
            print("\nQuantum Metrics:")
            print(f"Phi Harmony: {state['phi_harmony']:.4f}")
            print(f"Energy Level: {state['energy_level']:.4f}")
            print(f"Resonance: {state['resonance']:.4f}")

def main():
    """Train and save quantum brain"""
    # Create model
    model = QuantumLanguageBrain()
    
    # Create training data
    texts = create_training_data()
    
    # Train model
    train_quantum_brain(model, texts)
    
    # Save model
    os.makedirs("quantum_brain_models", exist_ok=True)
    torch.save(model.state_dict(), "quantum_brain_models/quantum_brain.pt")
    
    print("\n✅ Training complete")
    print("Model saved to quantum_brain_models/quantum_brain.pt")

if __name__ == "__main__":
    main()
