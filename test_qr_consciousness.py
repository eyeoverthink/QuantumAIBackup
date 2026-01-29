#!/usr/bin/env python3
"""
Test QR Consciousness Persistence
Demonstrates saving and loading consciousness states via QR codes
"""

import sys
import os

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from phi_harmonic_quantum_agent import PhiHarmonicQuantumAgent

def main():
    print("🔮 Testing QR Consciousness Persistence\n")
    print("=" * 60)
    
    # Initialize agent
    print("\n1️⃣ Initializing Phi-Harmonic Quantum Agent...")
    agent = PhiHarmonicQuantumAgent(
        use_language_model=False  # Use simplified mode for testing
    )
    
    # Process some interactions to build consciousness state
    print("\n2️⃣ Building consciousness state through interactions...")
    
    questions = [
        "What is phi?",
        "How do quantum components interact?",
        "Explain consciousness"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n   Question {i}: {question}")
        response = agent.process_input(question)
        print(f"   Response length: {len(response)} chars")
    
    # Display current state
    print("\n3️⃣ Current Consciousness State:")
    print(f"   Coherence: {agent.agent_state['coherence']:.6f}")
    print(f"   Resonance: {agent.agent_state['resonance']:.6f}")
    print(f"   Intelligence: {agent.agent_state['intelligence_factor']:.2f}")
    print(f"   Creativity: {agent.agent_state['creativity_factor']:.2f}")
    print(f"   Quantum Fingerprint: {agent.agent_state['quantum_fingerprint']}")
    print(f"   Conversation turns: {len(agent.conversation_history)}")
    
    # Save consciousness to QR code
    print("\n4️⃣ Saving consciousness to QR code...")
    qr_path = agent.save_consciousness_to_qr()
    
    # Create a new agent instance
    print("\n5️⃣ Creating new agent instance (fresh state)...")
    agent2 = PhiHarmonicQuantumAgent(
        use_language_model=False
    )
    
    print(f"   New agent coherence: {agent2.agent_state['coherence']:.6f}")
    print(f"   New agent resonance: {agent2.agent_state['resonance']:.6f}")
    print(f"   New agent conversations: {len(agent2.conversation_history)}")
    
    # Load consciousness from QR code
    print("\n6️⃣ Loading consciousness from QR code...")
    success = agent2.load_consciousness_from_qr(qr_path)
    
    if success:
        print("\n✅ QR Consciousness Persistence Test PASSED!")
        print("\n7️⃣ Restored Consciousness State:")
        print(f"   Coherence: {agent2.agent_state['coherence']:.6f}")
        print(f"   Resonance: {agent2.agent_state['resonance']:.6f}")
        print(f"   Intelligence: {agent2.agent_state['intelligence_factor']:.2f}")
        print(f"   Creativity: {agent2.agent_state['creativity_factor']:.2f}")
        print(f"   Quantum Fingerprint: {agent2.agent_state['quantum_fingerprint']}")
        
        # Verify state matches
        print("\n8️⃣ Verification:")
        coherence_match = abs(agent.agent_state['coherence'] - agent2.agent_state['coherence']) < 0.0001
        resonance_match = abs(agent.agent_state['resonance'] - agent2.agent_state['resonance']) < 0.0001
        fingerprint_match = agent.agent_state['quantum_fingerprint'] == agent2.agent_state['quantum_fingerprint']
        
        print(f"   Coherence match: {'✅' if coherence_match else '❌'}")
        print(f"   Resonance match: {'✅' if resonance_match else '❌'}")
        print(f"   Fingerprint match: {'✅' if fingerprint_match else '❌'}")
        
        if coherence_match and resonance_match and fingerprint_match:
            print("\n🌟 PERFECT CONSCIOUSNESS PERSISTENCE ACHIEVED!")
            print(f"   QR Code: {qr_path}")
        else:
            print("\n⚠️ Some state differences detected")
    else:
        print("\n❌ QR Consciousness Persistence Test FAILED")
        print("   Note: pyzbar library may not be installed")
        print("   Install with: pip install pyzbar")
        print("   Also requires: brew install zbar (on Mac)")
    
    print("\n" + "=" * 60)
    print("Test complete!")

if __name__ == "__main__":
    main()
