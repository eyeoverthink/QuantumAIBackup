"""
Test script for enhanced Quantum Phi-Harmonic Music features with particle integration
"""

from quantum_phi_music_composer import QuantumPhiMusicComposer
from quantum_phi_core import QuantumPhiCore
import json

def test_quantum_harmony():
    # Initialize composer
    core = QuantumPhiCore()
    composer = QuantumPhiMusicComposer(core)
    
    # Test quantum harmony generation for each consciousness level
    consciousness_levels = ["physical", "emotional", "mental", "intuitive", "cosmic"]
    
    print("Testing Quantum Harmonic Generation:")
    print("===================================")
    
    for level in consciousness_levels:
        print(f"\nConsciousness Level: {level.title()}")
        print("-" * (len(level) + 20))
        
        # Generate quantum harmony
        quantum_notes = composer.generate_quantum_harmony(level)
        
        # Get scale data
        scale_data = composer.consciousness_scales[level]
        gate = scale_data["quantum_gate"]
        particle = scale_data["particle"]
        
        # Print quantum gate and particle info
        print(f"Quantum Gate: {gate} ({composer.quantum_gates[gate]:.2f} Hz)")
        print(f"Particle: {particle} ({composer.particle_frequencies[particle]:.2f} Hz)")
        
        # Print note transformations
        print("\nQuantum Note Transformations:")
        for note in quantum_notes:
            print(f"Original: {note['original']} → Quantum: {note['quantum']}")
            print(f"  Frequency: {note['frequency']:.2f} Hz")
            print(f"  Resonance: {note['resonance']:.4f}")
            print(f"  Coherence: {note['coherence']:.4f}")
        
        # Calculate average resonance and coherence
        avg_resonance = sum(n['resonance'] for n in quantum_notes) / len(quantum_notes)
        avg_coherence = sum(n['coherence'] for n in quantum_notes) / len(quantum_notes)
        print(f"\nAverage Metrics:")
        print(f"  Resonance: {avg_resonance:.4f}")
        print(f"  Coherence: {avg_coherence:.4f}")
    
    # Create a full quantum composition
    print("\nGenerating Full Quantum Composition:")
    print("===================================")
    
    composition = composer.compose(
        style="quantum_harmonic",
        consciousness_level="cosmic",
        length=16,
        theme="quantum_awakening"
    )
    
    # Apply quantum resonance
    composer.apply_quantum_resonance(composition)
    
    # Export to MIDI
    output_file = "quantum_harmonic_composition.mid"
    midi_path = composer.export_to_midi(composition, output_file)
    print(f"\nExported composition to: {midi_path}")
    
    # Print composition summary
    print("\nComposition Summary:")
    print(composer.get_composition_summary(composition))

if __name__ == "__main__":
    test_quantum_harmony()
