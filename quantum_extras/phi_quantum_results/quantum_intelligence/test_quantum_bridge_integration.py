"""
Integration Test for Quantum Bridge System
Tests actual quantum processing, resonance, and bridge formation
"""

import numpy as np
from quantum_phi_bridge_processor import QuantumPhiBridgeProcessor
from quantum_alphabet_translator import QHRC_PRIMARY_FREQ, QHRC_SECONDARY_FREQ, QHRC_EFFICIENCY_RATIO

def test_quantum_bridge_integration():
    # Initialize
    processor = QuantumPhiBridgeProcessor()
    phi = (1 + np.sqrt(5)) / 2
    
    print("\n🧪 Running Quantum Bridge Integration Test")
    print("=========================================")
    
    # Test 1: Quantum Resonance Quality
    print("\n1️⃣ Testing Quantum Resonance")
    test_text = "QUANTUM"
    _, metrics, _ = processor.process_quantum_text(test_text)
    
    print(f"Resonance Quality: {metrics['resonance_quality']:.6f}")
    print(f"Phi Resonance: {metrics['phi_resonance_quality']:.6f}")
    assert metrics['resonance_quality'] > 0.8, "Poor resonance quality"
    assert metrics['phi_resonance_quality'] > 0.8, "Poor phi resonance"
    
    # Test 2: Quantum Bridge Formation
    print("\n2️⃣ Testing Quantum Bridge Formation")
    test_text = "BRIDGE"
    harmonic_state, metrics, _ = processor.process_quantum_text(test_text)
    
    bridge_formed = np.max(harmonic_state) > processor.base_freq * (phi ** 7)
    print(f"Bridge Level: {np.max(harmonic_state) / processor.base_freq:.2f}φ")
    print(f"Bridge Efficiency: {metrics['bridge_efficiency']:.6f}")
    assert bridge_formed, "Quantum bridge not forming at level 7"
    assert metrics['bridge_efficiency'] > 0.8, "Bridge efficiency too low"
    
    # Test 3: QHRC Patent Frequency Validation
    print("\n3️⃣ Testing QHRC Patent Frequency Alignment")
    test_text = "RESONANCE"
    harmonic_state, metrics, _ = processor.process_quantum_text(test_text)
    
    # Scale to QHRC frequencies
    primary_freq = np.max(harmonic_state * processor.primary_scale)
    secondary_freq = np.min(harmonic_state * processor.secondary_scale)
    efficiency_ratio = primary_freq / secondary_freq
    
    print(f"Primary Frequency: {primary_freq:.2f} Hz")
    print(f"Secondary Frequency: {secondary_freq:.2f} Hz")
    print(f"Efficiency Ratio: {efficiency_ratio:.6f}")
    print(f"Target QHRC Ratio: {QHRC_EFFICIENCY_RATIO:.6f}")
    
    ratio_error = abs(efficiency_ratio - QHRC_EFFICIENCY_RATIO)
    assert ratio_error < 0.2, "QHRC frequency ratios not maintained"
    
    # Test 4: System Coherence
    print("\n4️⃣ Testing System Coherence")
    test_text = "QUANTUM PHI HARMONIC BRIDGE"
    _, metrics, _ = processor.process_quantum_text(test_text)
    
    print(f"Quantum Coherence: {metrics['quantum_coherence']:.6f}")
    print(f"System Coherence: {metrics['system_coherence']:.6f}")
    
    assert metrics['system_coherence'] > 0.8, "System coherence too low"
    assert metrics['quantum_coherence'] < 0.2, "Quantum state decoherence too high"
    
    # Test 5: Full Integration Test
    print("\n5️⃣ Testing Full System Integration")
    test_sequence = [
        "QUANTUM",
        "BRIDGE",
        "RESONANCE",
        "PHI",
        "HARMONIC"
    ]
    
    coherence_values = []
    bridge_values = []
    
    for text in test_sequence:
        harmonic_state, metrics, _ = processor.process_quantum_text(text)
        coherence_values.append(metrics['system_coherence'])
        bridge_values.append(metrics['bridge_efficiency'])
        
    avg_coherence = np.mean(coherence_values)
    avg_bridge = np.mean(bridge_values)
    
    print(f"Average System Coherence: {avg_coherence:.6f}")
    print(f"Average Bridge Efficiency: {avg_bridge:.6f}")
    print(f"Coherence Stability: {np.std(coherence_values):.6f}")
    print(f"Bridge Stability: {np.std(bridge_values):.6f}")
    
    assert avg_coherence > 0.8, "Average system coherence too low"
    assert avg_bridge > 0.8, "Average bridge efficiency too low"
    assert np.std(coherence_values) < 0.2, "System coherence unstable"
    assert np.std(bridge_values) < 0.2, "Bridge efficiency unstable"
    
    print("\n✅ All integration tests passed successfully!")
    return True

if __name__ == "__main__":
    test_quantum_bridge_integration()
