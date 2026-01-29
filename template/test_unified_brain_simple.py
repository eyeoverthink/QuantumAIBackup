from UNIFIDE_QUANTUM_BRAIN import UnifiedQuantumBrain
import numpy as np
import time

def test_quantum_harmonics():
    """Test quantum harmonics with phi-based frequency progression"""
    print("\n🧠 Testing Quantum Harmonics")
    print("===========================")
    
    brain = UnifiedQuantumBrain()
    
    # Phi-harmonic frequencies
    phi = (1 + np.sqrt(5)) / 2
    frequencies = {
        'base': 4.37,              # Proven base
        'emergence': phi**4,       # Perfect emergence (6.854)
        'bridge': phi**7,          # Bridge formation (29.034)
        'resonance': 0.96          # Target resonance
    }
    
    print("\n📊 Testing Frequencies:")
    for name, freq in frequencies.items():
        print(f"{name}: {freq:.3f} Hz")
    
    results = []
    damping = phi**-1  # Natural damping
    
    # Test each harmonic level
    for power in range(8):  # Test up to φ⁸
        freq = frequencies['base'] * phi**power
        
        params = {
            'base_freq': freq,
            'duration': 108.0,  # φ * 66.7
            'intensity': damping**power  # Natural decay
        }
        
        print(f"\n🔄 Testing φ{power} Harmonic ({freq:.3f} Hz)")
        result = brain.create_physical_model('consciousness_expansion', params)
        
        # Calculate quantum metrics
        coherence = result['consciousness_coherence'] / result['field_resonance']
        field_strength = result['field_resonance'] / brain.frequencies['quantum_field']
        resonance = np.exp(-abs(coherence - frequencies['resonance']) * np.pi)
        
        # Track harmonic bridges
        bridge_strength = np.exp(-abs(freq - frequencies['bridge']) / frequencies['base'])
        emergence_ratio = np.exp(-abs(freq - frequencies['emergence']) / frequencies['base'])
        
        results.append({
            'power': power,
            'frequency': freq,
            'coherence': coherence,
            'field_strength': field_strength,
            'resonance': resonance,
            'bridge_strength': bridge_strength,
            'emergence_ratio': emergence_ratio
        })
        
        print(f"\n📊 Level {power} Results:")
        print(f"Frequency: {freq:.3f} Hz")
        print(f"Coherence: {coherence:.6f}")
        print(f"Field Strength: {field_strength:.6f}")
        print(f"Resonance: {resonance:.6f}")
        print(f"Bridge Strength: {bridge_strength:.6f}")
        print(f"Emergence Ratio: {emergence_ratio:.6f}")
        
        # Let quantum field stabilize
        time.sleep(0.1)
    
    return results

if __name__ == "__main__":
    results = test_quantum_harmonics()
    
    print("\n✨ Harmonic Analysis:")
    
    # Find optimal harmonic level
    optimal = max(results, key=lambda x: x['resonance'] * x['bridge_strength'] * x['emergence_ratio'])
    
    print(f"\nOptimal Harmonic Level: φ{optimal['power']}")
    print(f"Frequency: {optimal['frequency']:.3f} Hz")
    print(f"Coherence: {optimal['coherence']:.6f}")
    print(f"Resonance Quality: {optimal['resonance']:.6f}")
    print(f"Bridge Strength: {optimal['bridge_strength']:.6f}")
    print(f"Emergence Quality: {optimal['emergence_ratio']:.6f}")
    
    # Calculate overall system harmony
    harmony = np.mean([r['resonance'] * r['bridge_strength'] * r['emergence_ratio'] for r in results])
    stability = np.std([r['coherence'] for r in results])
    
    print(f"\nSystem Harmony: {harmony:.6f}")
    print(f"Stability: {stability:.6f}")
    
    print("\n🎯 System Status:")
    if harmony > 0.8 and stability < 0.1:
        print("✅ System achieved quantum harmonic coherence")
    else:
        print("⚠️ System approaching coherence - harmonics still aligning")
