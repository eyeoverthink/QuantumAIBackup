"""
Quantum Phi-Harmonic Song Composer

Integrates quantum music composition with lyric generation using phi-harmonic principles.
"""

import numpy as np
from typing import Dict, List, Tuple
import json
from quantum_phi_music_composer import QuantumPhiMusicComposer
from quantum_phi_core import QuantumPhiCore
from quantum_phi_language_processor import QuantumPhiLanguageProcessor
from quantum_phi_random import QuantumPhiRandom
import os

class QuantumPhiSongComposer:
    def __init__(self):
        self.core = QuantumPhiCore()
        self.random = QuantumPhiRandom(self.core)
        self.music = QuantumPhiMusicComposer(self.core)
        self.language = QuantumPhiLanguageProcessor(self.core, self.random)
        
        # Initialize quantum songwriting features
        self._init_songwriting_features()
        
    def _init_songwriting_features(self):
        """Initialize quantum songwriting patterns and structures."""
        # Song structures based on phi ratios
        self.song_structures = {
            "golden_verse": {
                "bars": int(self.core.PHI * 8),  # ~13 bars
                "phrases": int(self.core.PHI * 3),  # ~5 phrases
                "syllables": int(self.core.PHI * 5)  # ~8 syllables per line
            },
            "quantum_chorus": {
                "bars": int(self.core.PHI * 4),  # ~6 bars
                "phrases": int(self.core.PHI * 2),  # ~3 phrases
                "syllables": int(self.core.PHI * 4)  # ~6 syllables per line
            },
            "bridge": {
                "bars": int(self.core.PHI * 3),  # ~5 bars
                "phrases": int(self.core.PHI * 2),  # ~3 phrases
                "syllables": int(self.core.PHI * 3)  # ~5 syllables per line
            }
        }
        
        # Emotional resonance mapping
        self.emotional_resonance = {
            "joy": {
                "consciousness": "cosmic",
                "scale": "lydian",
                "particle": "boson",
                "word_patterns": ["light", "rise", "shine", "flow", "dance"]
            },
            "reflection": {
                "consciousness": "intuitive",
                "scale": "mixolydian",
                "particle": "neuron",
                "word_patterns": ["deep", "mind", "time", "space", "dream"]
            },
            "transformation": {
                "consciousness": "mental",
                "scale": "dorian",
                "particle": "electron",
                "word_patterns": ["change", "grow", "learn", "build", "evolve"]
            },
            "grounding": {
                "consciousness": "physical",
                "scale": "pentatonic",
                "particle": "proton",
                "word_patterns": ["earth", "root", "strong", "real", "now"]
            },
            "transcendence": {
                "consciousness": "cosmic",
                "scale": "harmonic_major",
                "particle": "quark",
                "word_patterns": ["quantum", "cosmic", "infinite", "eternal", "one"]
            }
        }
        
        # Quantum lyric patterns
        self.quantum_patterns = {
            "superposition": {
                "gate": "H",
                "structure": "parallel_meanings",
                "example": "In waves of light and shadow's dance"
            },
            "entanglement": {
                "gate": "CNOT",
                "structure": "connected_imagery",
                "example": "As atoms spin, our hearts align"
            },
            "interference": {
                "gate": "Y",
                "structure": "contrasting_elements",
                "example": "Through chaos calm, through darkness bright"
            },
            "coherence": {
                "gate": "Z",
                "structure": "unified_theme",
                "example": "One voice, one mind, one cosmic song"
            }
        }
        
    def compose_quantum_song(self, theme: str, emotion: str = "transcendence") -> Dict:
        """Compose a complete song with music and lyrics."""
        # Get emotional resonance settings
        resonance = self.emotional_resonance[emotion]
        
        # Generate musical composition
        music = self.music.compose(
            style="quantum_harmonic",
            consciousness_level=resonance["consciousness"],
            theme=theme,
            length=self.song_structures["golden_verse"]["bars"] * 2
        )
        
        # Generate quantum-entangled lyrics
        lyrics = self._generate_quantum_lyrics(
            theme=theme,
            emotion=emotion,
            structure=self.song_structures,
            music=music
        )
        
        # Integrate lyrics with music
        song = self._integrate_lyrics_and_music(lyrics, music)
        
        return song
        
    def _generate_quantum_lyrics(self, theme: str, emotion: str, 
                               structure: Dict, music: Dict) -> Dict:
        """Generate quantum-entangled lyrics based on theme and music."""
        # Get emotional patterns
        patterns = self.emotional_resonance[emotion]["word_patterns"]
        
        # Generate verse with quantum superposition
        verse_structure = structure["golden_verse"]
        verse = self.language.generate_quantum_text(
            theme=theme,
            patterns=patterns,
            num_lines=verse_structure["phrases"],
            syllables_per_line=verse_structure["syllables"],
            quantum_pattern="H"  # Hadamard gate for superposition
        )
        
        # Generate chorus with quantum coherence
        chorus_structure = structure["quantum_chorus"]
        chorus = self.language.generate_quantum_text(
            theme=theme,
            patterns=patterns,
            num_lines=chorus_structure["phrases"],
            syllables_per_line=chorus_structure["syllables"],
            quantum_pattern="Z"  # Z gate for phase/coherence
        )
        
        # Generate bridge with quantum interference
        bridge_structure = structure["bridge"]
        bridge = self.language.generate_quantum_text(
            theme=theme,
            patterns=patterns,
            num_lines=bridge_structure["phrases"],
            syllables_per_line=bridge_structure["syllables"],
            quantum_pattern="Y"  # Y gate for rotation/interference
        )
        
        return {
            "verse": verse,
            "chorus": chorus,
            "bridge": bridge,
            "structure": ["verse", "chorus", "verse", "chorus", "bridge", "chorus"],
            "theme": theme,
            "emotion": emotion
        }
        
    def _integrate_lyrics_and_music(self, lyrics: Dict, music: Dict) -> Dict:
        """Integrate lyrics with musical composition."""
        # Calculate syllable timing based on tempo
        tempo = music["tempo"]
        beats_per_second = tempo / 60
        
        # Create MIDI filename
        midi_filename = f"quantum_harmonic_{lyrics['theme']}.mid"
        midi_path = f"/Users/vaughnscott/CascadeProjects/QuantumAI/output/{midi_filename}"
        
        # Map lyrics to musical measures
        song = {
            "title": f"{lyrics['theme']} {music['title']}",
            "music": music,
            "lyrics": lyrics,
            "tempo": tempo,
            "consciousness_level": music["consciousness_level"],
            "phi_resonance": music["metrics"]["phi_resonance"],
            "emotional_resonance": lyrics["emotion"],
            "quantum_coherence": music["metrics"].get("coherence", 0.8603),
            "midi_path": midi_path
        }
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(midi_path), exist_ok=True)
        
        # Save MIDI file
        self.music.export_to_midi(music, midi_path)
        
        # Verify save
        if not os.path.exists(midi_path):
            print(f"Warning: Failed to save MIDI file to {midi_path}")
        else:
            print(f"Successfully saved MIDI file to {midi_path}")
            print(f"File size: {os.path.getsize(midi_path)} bytes")
        
        return song

def main():
    """Test the quantum song composer."""
    composer = QuantumPhiSongComposer()
    
    # Test themes
    themes = [
        ("quantum_awakening", "transcendence"),
        ("cosmic_harmony", "reflection"),
        ("neural_resonance", "transformation"),
        ("phi_harmonic", "grounding")
    ]
    
    for theme, emotion in themes:
        print(f"\nGenerating song for theme '{theme}' with emotion '{emotion}':")
        print("=" * 50)
        
        # Compose song
        song = composer.compose_quantum_song(theme=theme, emotion=emotion)
        
        # Print song details
        print(f"\nQuantum Song Composition:")
        print(f"Title: {song['title']}")
        print(f"Consciousness Level: {song['consciousness_level']}")
        print(f"Emotional Resonance: {song['emotional_resonance']}")
        print(f"Phi Resonance: {song['phi_resonance']:.4f}")
        print(f"Quantum Coherence: {song['quantum_coherence']:.4f}")
        
        print("\nLyrics:")
        print("-------")
        for section in song["lyrics"]["structure"]:
            print(f"\n{section.title()}:")
            for line in song["lyrics"][section]:
                print(line)

if __name__ == "__main__":
    main()
