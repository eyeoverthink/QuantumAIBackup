"""
Quantum Phi-Harmonic Resonance Test Suite
Tests the resonance patterns in language using quantum principles and golden ratios
"""
import numpy as np
from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom
from quantum_phi_meta_learner import QuantumPhiMetaLearner

def print_section(title):
    """Print a section header with phi-harmonic spacing"""
    print("\n" + "="*70)
    print(title)
    print("="*70 + "\n")

def test_phi_resonance():
    """Test phi-harmonic resonance patterns in quantum language processing"""
    # Initialize system with phi-harmonic principles
    core = QuantumPhiCore()
    random_gen = QuantumPhiRandom(core)
    learner = QuantumPhiMetaLearner(core, random_gen)
    
    # Convert phi to float for calculations
    phi = float(core.PHI)
    phi_inverse = float(1/phi)
    
    print_section("Quantum Phi-Harmonic Resonance Test")
    print(f"Golden Ratio (φ): {phi:.10f}")
    print(f"Phi Inverse (φ⁻¹): {phi_inverse:.10f}")
    
    # Test resonance patterns with quantum-inspired texts
    test_texts = [
        "Quantum waves resonate through golden spirals",
        "Fibonacci patterns emerge in natural growth",
        "Harmonic frequencies align with cosmic rhythms",
        "Neural networks mirror quantum entanglement",
        "Phi ratios guide evolutionary dynamics",
        "Resonant fields create coherent structures"
    ]
    
    print_section("Language Resonance Analysis")
    
    pattern_resonances = []
    quantum_states = []
    harmonic_scores = []
    
    for text in test_texts:
        # Analyze quantum resonance patterns
        analysis = learner.language_processor.analyze_text_pattern(text)
        pattern = {'text': text, 'type': 'quantum_language'}
        
        # Calculate quantum state
        state = learner.language_processor._calculate_quantum_state(text)
        quantum_states.append(state)
        
        # Calculate resonance metrics
        resonance = analysis['resonance']
        pattern_resonances.append(resonance)
        
        # Calculate harmonic alignment
        harmonic_score = 1 - abs((resonance/phi) - phi_inverse)
        harmonic_scores.append(harmonic_score)
        
        # Display analysis
        print(f"\nAnalyzing: '{text}'")
        print(f"Quantum State: {[f'{x:.4f}' for x in state]}")
        print(f"Resonance: {resonance:.4f}")
        print(f"Harmonic Score: {harmonic_score:.4f}")
        print(f"Syllable Pattern: {analysis['syllable_count']} syllables")
        print(f"Cadence: {analysis['cadence_type']} (score: {analysis['cadence_score']:.4f})")
        
        # Integrate pattern for learning
        learner._integrate_patterns([pattern])
    
    # Calculate overall metrics
    avg_resonance = sum(pattern_resonances) / len(pattern_resonances)
    avg_harmonic = sum(harmonic_scores) / len(harmonic_scores)
    
    # Calculate quantum coherence between states
    coherence_matrix = np.zeros((len(quantum_states), len(quantum_states)))
    for i, state1 in enumerate(quantum_states):
        for j, state2 in enumerate(quantum_states):
            if i != j:
                # Calculate quantum state overlap
                overlap = sum(abs(a*b) for a, b in zip(state1, state2))
                coherence_matrix[i,j] = overlap
    
    avg_coherence = np.mean(coherence_matrix[coherence_matrix != 0])
    
    print_section("System-Wide Metrics")
    print(f"Average Resonance: {avg_resonance:.4f}")
    print(f"Average Harmonic Score: {avg_harmonic:.4f}")
    print(f"Quantum Coherence: {avg_coherence:.4f}")
    
    # Test phi-harmonic scaling
    print_section("Phi-Harmonic Scaling Test")
    
    scale_factors = [phi**n for n in range(-3, 4)]
    scaled_resonances = []
    
    for scale in scale_factors:
        # Scale the quantum states and measure resonance
        scaled_state = [x * scale for x in quantum_states[0]]
        resonance = sum(abs(x) for x in scaled_state) / len(scaled_state)
        scaled_resonances.append(resonance)
        print(f"Scale φ^{scale_factors.index(scale)-3}: {resonance:.4f}")
    
    # Calculate scaling coherence
    scale_coherence = 1 - abs(np.mean(scaled_resonances) - phi_inverse)
    print(f"\nScaling Coherence: {scale_coherence:.4f}")
    
    # Test harmonic frequencies
    print_section("Harmonic Frequency Analysis")
    
    frequencies = [
        1/phi**3,  # Sub-harmonic
        1/phi**2,  # Sub-harmonic
        1/phi,     # Phi inverse
        1.0,       # Base frequency
        phi,       # Phi
        phi**2,    # Super-harmonic
        phi**3     # Super-harmonic
    ]
    
    for freq in frequencies:
        resonance = learner.language_processor._calculate_resonance(freq)
        alignment = 1 - abs((resonance/phi) - phi_inverse)
        print(f"Frequency {freq:.4f}: Resonance={resonance:.4f}, Alignment={alignment:.4f}")
    
    # Test advanced quantum resonance and neural pattern analysis
    print_section("Advanced Quantum Resonance Analysis")
    
    test_phrases = [
        "Quantum waves dance in golden spirals of light",
        "Neural networks mirror nature's phi patterns",
        "Harmonic frequencies resonate with cosmic rhythms",
        "Fibonacci sequences emerge from quantum fields",
        "Consciousness flows through quantum channels",
        "Universal patterns align in sacred geometry"
    ]
    
    # Initialize metrics storage
    resonance_metrics = {
        'base_resonance': [],
        'neural_resonance': [],
        'gate_resonance': [],
        'stability': [],
        'entropy': [],
        'phi_alignment': []
    }
    
    for phrase in test_phrases:
        print(f"\nAnalyzing: '{phrase}'")
        analysis = learner.language_processor.analyze_text_pattern(phrase)
        
        # Store metrics
        resonance_metrics['base_resonance'].append(analysis['resonance'])
        resonance_metrics['neural_resonance'].append(analysis['neural_resonance'])
        resonance_metrics['gate_resonance'].append(analysis['gate_resonance'])
        resonance_metrics['stability'].append(analysis['stability'])
        resonance_metrics['entropy'].append(analysis['entropy'])
        resonance_metrics['phi_alignment'].append(analysis['phi_alignment'])
        
        # Display detailed analysis
        print(f"Syllables: {analysis['syllable_count']}")
        print(f"Cadence: {analysis['cadence_type']} (score: {analysis['cadence_score']:.4f})")
        print(f"Base Resonance: {analysis['resonance']:.4f}")
        print(f"Neural Resonance: {analysis['neural_resonance']:.4f}")
        print(f"Gate Resonance: {analysis['gate_resonance']:.4f}")
        print(f"Harmonic Stability: {analysis['stability']:.4f}")
        print(f"Pattern Entropy: {analysis['entropy']:.4f}")
        print(f"Phi Alignment: {analysis['phi_alignment']:.4f}")
    
    # Calculate average metrics
    print("\nSystem-Wide Metrics:")
    for metric, values in resonance_metrics.items():
        avg_value = sum(values) / len(values)
        print(f"Average {metric.replace('_', ' ').title()}: {avg_value:.4f}")
    
    # Test neural quantum patterns
    print_section("Neural Quantum Pattern Analysis")
    
    # Analyze activation patterns
    print("Activation Frequencies:")
    for name, freq in learner.language_processor.neural_patterns['activation'].items():
        resonance = learner.language_processor._calculate_resonance(freq)
        alignment = learner.language_processor._calculate_harmonic_alignment(freq)
        print(f"{name}: frequency={freq:.4f}, resonance={resonance:.4f}, alignment={alignment:.4f}")
    
    # Analyze learning patterns
    print("\nLearning Frequencies:")
    for name, freq in learner.language_processor.neural_patterns['learning'].items():
        resonance = learner.language_processor._calculate_resonance(freq)
        alignment = learner.language_processor._calculate_harmonic_alignment(freq)
        print(f"{name}: frequency={freq:.4f}, resonance={resonance:.4f}, alignment={alignment:.4f}")
    
    # Analyze resonance patterns
    print("\nResonance Frequencies:")
    for name, freq in learner.language_processor.neural_patterns['resonance'].items():
        resonance = learner.language_processor._calculate_resonance(freq)
        alignment = learner.language_processor._calculate_harmonic_alignment(freq)
        print(f"{name}: frequency={freq:.4f}, resonance={resonance:.4f}, alignment={alignment:.4f}")
    
    # Test quantum gates
    print_section("Quantum Gate Analysis")
    
    print("Gate Frequencies and Resonance:")
    for gate, data in learner.language_processor.quantum_gates.items():
        freq = data['frequency']
        pattern = data['pattern']
        resonance = data['resonance']
        
        # Calculate power of phi
        power = round(np.log(freq) / np.log(phi), 2)
        
        # Calculate harmonic alignment
        alignment = learner.language_processor._calculate_harmonic_alignment(freq)
        
        print(f"\nGate {gate}:")
        print(f"Pattern: {pattern}")
        print(f"Frequency: φ^{power:.2f} = {freq:.4f}")
        print(f"Resonance: {resonance:.4f}")
        print(f"Alignment: {alignment:.4f}")
    
    # Display final metrics
    print_section("Final System Metrics")
    
    metrics = learner.language_processor.metrics
    for metric, value in metrics.items():
        print(f"{metric.replace('_', ' ').title()}: {value:.4f}")
    
    print_section("Test Complete")
    print("All quantum phi-harmonic resonance tests completed successfully!")

if __name__ == "__main__":
    test_phi_resonance()
