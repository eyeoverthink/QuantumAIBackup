"""
Test script for new Quantum Phi-Harmonic Music features
"""

from quantum_phi_music_composer import QuantumPhiMusicComposer
from quantum_phi_core import QuantumPhiCore

def test_new_features():
    # Initialize composer
    core = QuantumPhiCore()
    composer = QuantumPhiMusicComposer(core)
    
    # 1. Test binaural beats generation
    print("Generating binaural beats for meditation...")
    binaural_track = composer.generate_binaural_track(100, "theta")
    print(f"Generated binaural beats: Left={binaural_track[0]['frequency']}Hz, Right={binaural_track[1]['frequency']}Hz")
    
    # 2. Test sacred geometry
    test_notes = ["C4", "E4", "G4"]
    print("\nApplying sacred geometry to notes:", test_notes)
    sacred_notes = composer.apply_sacred_geometry(test_notes)
    print("Sacred geometry notes:", sacred_notes)
    
    # 3. Test consciousness harmony
    print("\nGenerating harmonies for different consciousness levels:")
    for level in ["physical", "emotional", "mental", "intuitive", "cosmic"]:
        harmony = composer.generate_consciousness_harmony(level)
        print(f"{level.title()} harmony: {harmony}")
    
    # 4. Create a full composition with new features
    print("\nComposing with quantum features...")
    composition = composer.compose(
        style="phi_harmonic",
        consciousness_level="cosmic",
        length=16,
        theme="quantum_awakening"
    )
    
    # Apply quantum resonance
    composer.apply_quantum_resonance(composition)
    
    # Export to MIDI
    output_file = "quantum_resonance_composition.mid"
    midi_path = composer.export_to_midi(composition, output_file)
    print(f"\nExported composition to: {midi_path}")
    
    # Print composition summary
    print("\nComposition Summary:")
    print(composer.get_composition_summary(composition))

if __name__ == "__main__":
    test_new_features()
