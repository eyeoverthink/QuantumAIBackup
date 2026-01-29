"""
Quantum Phi-Harmonic Music Frequencies

Maps musical notes, scales, and chords to quantum phi-harmonic frequencies
and consciousness levels.
"""

import numpy as np
import math
from typing import Dict, List, Tuple, Any, Optional, Union
from enum import Enum

from quantum_phi_core import QuantumPhiCore

class QuantumPhiMusicFrequencies:
    """
    Maps musical elements to quantum phi-harmonic frequencies and consciousness levels.
    """
    
    def __init__(self, core: QuantumPhiCore = None):
        """Initialize the music frequency mapper."""
        self.core = core or QuantumPhiCore()
        self.phi = float(self.core.PHI)
        self.pi = float(self.core.PI)
        self.e = float(self.core.E)
        
        # Initialize frequency manager
        self.manager = FrequencyManager(self.core)
        
        # Initialize frequency constants
        self._init_frequency_constants()
        
        # Initialize consciousness mappings
        self._init_consciousness_mappings()
        
        # Initialize note mappings
        self._init_note_mappings()
        
        # Initialize chord mappings
        self._init_chord_mappings()
        
        # Initialize scale mappings
        self._init_scale_mappings()
        
    def _init_frequency_constants(self):
        """Initialize frequency constants based on phi-harmonic principles."""
        # A4 = 440Hz is standard tuning
        # We'll use phi-adjusted A4 as our base frequency
        self.base_freq = 432.0  # Phi-harmonic base frequency
        
        # Phi-based frequency ratios
        self.phi_ratios = {
            "phi¹": self.phi,
            "phi²": self.phi**2,
            "phi³": self.phi**3,
            "phi⁴": self.phi**4,
            "phi⁵": self.phi**5,
            "phi⁻¹": 1/self.phi,
            "phi⁻²": 1/self.phi**2,
            "phi⁻³": 1/self.phi**3,
            "phi⁻⁴": 1/self.phi**4,
            "phi⁻⁵": 1/self.phi**5,
        }
        
        # Equal temperament semitone ratio (12-TET)
        self.semitone_ratio = 2**(1/12)
        
        # Phi-harmonic semitone ratio
        self.phi_semitone_ratio = self.phi**(1/7)  # 7 is a Fibonacci number
        
        # Just intonation ratios
        self.just_ratios = {
            "unison": 1/1,
            "minor_second": 16/15,
            "major_second": 9/8,
            "minor_third": 6/5,
            "major_third": 5/4,
            "perfect_fourth": 4/3,
            "tritone": self.phi,  # Use phi for the tritone
            "perfect_fifth": 3/2,
            "minor_sixth": 8/5,
            "major_sixth": 5/3,
            "minor_seventh": 16/9,
            "major_seventh": 15/8,
            "octave": 2/1
        }
        
        # Phi-harmonic tuning system
        self.phi_ratios_intervals = {
            "unison": 1,
            "phi_second": self.phi_inverse,
            "phi_third": self.phi_inverse**2,
            "phi_fourth": self.phi_inverse**3,
            "phi_fifth": self.phi,
            "phi_sixth": self.phi**2,
            "phi_seventh": self.phi**3,
            "phi_octave": self.phi**4 / self.phi_inverse
        }
    
    def _init_note_mappings(self):
        """Initialize note frequency mappings."""
        # Standard 12-TET note names
        self.note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        
        # Calculate frequencies for all notes (10 octaves)
        self.note_frequencies = {}
        self.note_consciousness = {}
        
        # A4 is our reference note at 432 Hz
        a4_index = self.note_names.index("A") + (4 * 12)
        
        # Calculate frequencies for all notes
        for octave in range(0, 10):
            for i, note in enumerate(self.note_names):
                note_idx = i + (octave * 12)
                semitones_from_a4 = note_idx - a4_index
                
                # Standard 12-TET frequency
                std_freq = self.base_freq * (self.semitone_ratio ** semitones_from_a4)
                
                # Phi-adjusted frequency
                phi_adjustment = 1.0
                if semitones_from_a4 > 0:
                    phi_adjustment = self.phi ** (semitones_from_a4 / 12)
                elif semitones_from_a4 < 0:
                    phi_adjustment = (1 / self.phi) ** (abs(semitones_from_a4) / 12)
                
                phi_freq = std_freq * phi_adjustment
                
                # Store both frequencies
                note_with_octave = f"{note}{octave}"
                self.note_frequencies[note_with_octave] = {
                    "standard": std_freq,
                    "phi_harmonic": phi_freq,
                    "just_intonation": None,  # Will be calculated for specific keys
                    "semitones_from_a4": semitones_from_a4
                }
                
                # Determine consciousness level based on frequency
                self.note_consciousness[note_with_octave] = self._frequency_to_consciousness(phi_freq)
        
        # Calculate phi-weighted importance for each note
        self._calculate_note_importance()
    
    def _calculate_note_importance(self):
        """Calculate phi-weighted importance for each note."""
        # Notes with frequencies that are phi-harmonic with the base frequency
        # have higher importance
        for note, data in self.note_frequencies.items():
            phi_freq = data["phi_harmonic"]
            
            # Calculate ratio to base frequency
            ratio = phi_freq / self.base_freq
            
            # Find closest phi power
            phi_powers = [self.phi**n for n in range(-5, 6)]
            closest_phi_power = min(phi_powers, key=lambda x: abs(x - ratio))
            
            # Calculate phi alignment (1.0 = perfect alignment)
            phi_alignment = 1.0 - abs(ratio - closest_phi_power) / closest_phi_power
            
            # Store importance
            self.note_frequencies[note]["phi_importance"] = phi_alignment
    
    def _init_chord_mappings(self):
        """Initialize chord frequency mappings."""
        # Define chord types and their interval structures
        self.chord_types = {
            "major": [0, 4, 7],  # Root, major third, perfect fifth
            "minor": [0, 3, 7],  # Root, minor third, perfect fifth
            "diminished": [0, 3, 6],  # Root, minor third, diminished fifth
            "augmented": [0, 4, 8],  # Root, major third, augmented fifth
            "major7": [0, 4, 7, 11],  # Root, major third, perfect fifth, major seventh
            "dominant7": [0, 4, 7, 10],  # Root, major third, perfect fifth, minor seventh
            "minor7": [0, 3, 7, 10],  # Root, minor third, perfect fifth, minor seventh
            "half_diminished7": [0, 3, 6, 10],  # Root, minor third, diminished fifth, minor seventh
            "diminished7": [0, 3, 6, 9],  # Root, minor third, diminished fifth, diminished seventh
            "sus2": [0, 2, 7],  # Root, major second, perfect fifth
            "sus4": [0, 5, 7],  # Root, perfect fourth, perfect fifth
            "phi": [0, int(self.phi * 2), 7],  # Root, phi-based interval, perfect fifth
            "phi_major": [0, 4, int(self.phi * 4)],  # Root, major third, phi-adjusted fifth
            "phi_minor": [0, 3, int(self.phi * 4)],  # Root, minor third, phi-adjusted fifth
            "golden_triad": [0, int(self.phi * 3), int(self.phi * 5)]  # Golden ratio-based intervals
        }
        
        # Calculate phi-harmonic resonance for each chord type
        self.chord_resonance = {}
        for chord_name, intervals in self.chord_types.items():
            # Calculate resonance based on interval ratios
            resonance = self._calculate_chord_resonance(intervals)
            self.chord_resonance[chord_name] = resonance
    
    def _calculate_chord_resonance(self, intervals: List[int]) -> float:
        """Calculate phi-harmonic resonance for a chord."""
        if not intervals:
            return 0.0
        
        # Convert intervals to frequency ratios
        ratios = [2 ** (interval / 12) for interval in intervals]
        
        # Calculate pairwise ratios
        pairwise_ratios = []
        for i in range(len(ratios)):
            for j in range(i + 1, len(ratios)):
                pairwise_ratios.append(ratios[j] / ratios[i])
        
        # Calculate alignment with phi and its powers
        phi_powers = [self.phi**n for n in range(-3, 4)]
        alignments = []
        
        for ratio in pairwise_ratios:
            # Find closest phi power
            closest_phi_power = min(phi_powers, key=lambda x: abs(x - ratio))
            # Calculate alignment (1.0 = perfect alignment)
            alignment = 1.0 - abs(ratio - closest_phi_power) / closest_phi_power
            alignments.append(alignment)
        
        # Overall resonance is average alignment
        return sum(alignments) / len(alignments) if alignments else 0.0
    
    def _init_scale_mappings(self):
        """Initialize scale frequency mappings."""
        # Define scale types and their interval structures
        self.scale_types = {
            "major": [0, 2, 4, 5, 7, 9, 11, 12],  # Major scale
            "natural_minor": [0, 2, 3, 5, 7, 8, 10, 12],  # Natural minor scale
            "harmonic_minor": [0, 2, 3, 5, 7, 8, 11, 12],  # Harmonic minor scale
            "melodic_minor": [0, 2, 3, 5, 7, 9, 11, 12],  # Melodic minor scale (ascending)
            "dorian": [0, 2, 3, 5, 7, 9, 10, 12],  # Dorian mode
            "phrygian": [0, 1, 3, 5, 7, 8, 10, 12],  # Phrygian mode
            "lydian": [0, 2, 4, 6, 7, 9, 11, 12],  # Lydian mode
            "mixolydian": [0, 2, 4, 5, 7, 9, 10, 12],  # Mixolydian mode
            "locrian": [0, 1, 3, 5, 6, 8, 10, 12],  # Locrian mode
            "pentatonic_major": [0, 2, 4, 7, 9, 12],  # Major pentatonic scale
            "pentatonic_minor": [0, 3, 5, 7, 10, 12],  # Minor pentatonic scale
            "blues": [0, 3, 5, 6, 7, 10, 12],  # Blues scale
            "fibonacci": [0, 1, 2, 3, 5, 8, 13 % 12, 12],  # Fibonacci-based scale
            "phi": [0, int(self.phi * 2) % 12, int(self.phi * 3) % 12, 
                   int(self.phi * 4) % 12, int(self.phi * 5) % 12, 
                   int(self.phi * 6) % 12, int(self.phi * 7) % 12, 12],  # Phi-based scale
            "golden": [0, int(self.phi * 1) % 12, int(self.phi * 2) % 12,
                      int(self.phi * 3) % 12, int(self.phi * 5) % 12,
                      int(self.phi * 8) % 12, 12]  # Golden ratio scale with Fibonacci steps
        }
        
        # Calculate phi-harmonic resonance for each scale type
        self.scale_resonance = {}
        self.scale_consciousness = {}
        
        for scale_name, intervals in self.scale_types.items():
            # Calculate resonance based on interval ratios
            resonance = self._calculate_scale_resonance(intervals)
            self.scale_resonance[scale_name] = resonance
            
            # Calculate consciousness level for each scale
            consciousness = self._scale_to_consciousness(scale_name, resonance)
            self.scale_consciousness[scale_name] = consciousness
    
    def _calculate_scale_resonance(self, intervals: List[int]) -> float:
        """Calculate phi-harmonic resonance for a scale."""
        if not intervals:
            return 0.0
        
        # Convert intervals to frequency ratios
        ratios = [2 ** (interval / 12) for interval in intervals]
        
        # Calculate step ratios (adjacent notes)
        step_ratios = []
        for i in range(len(ratios) - 1):
            step_ratios.append(ratios[i + 1] / ratios[i])
        
        # Calculate alignment with phi and its powers
        phi_powers = [self.phi**n for n in range(-3, 4)]
        alignments = []
        
        for ratio in step_ratios:
            # Find closest phi power
            closest_phi_power = min(phi_powers, key=lambda x: abs(x - ratio))
            # Calculate alignment (1.0 = perfect alignment)
            alignment = 1.0 - abs(ratio - closest_phi_power) / closest_phi_power
            alignments.append(alignment)
        
        # Overall resonance is average alignment
        return sum(alignments) / len(alignments) if alignments else 0.0
    
    def _init_consciousness_mappings(self):
        """Initialize consciousness level mappings for frequencies."""
        # Consciousness bands based on frequency ranges
        self.consciousness_bands = {
            "physical": (0, 200),
            "emotional": (200, 300),
            "mental": (300, 400),
            "intuitive": (400, 500),
            "cosmic": (500, float('inf'))
        }
        
        # Phi-harmonic consciousness centers
        self.consciousness_centers = {
            "physical": 144.0,  # Base * phi^-3
            "emotional": 233.0,  # Base * phi^-2
            "mental": 377.0,  # Base * phi^-1
            "intuitive": 432.0,  # Base frequency
            "cosmic": 699.0  # Base * phi
        }
    
    def _frequency_to_consciousness(self, frequency: float) -> str:
        """Convert a frequency to a consciousness level."""
        for level, (min_f, max_f) in self.consciousness_bands.items():
            if min_f <= frequency < max_f:
                return level
        return "cosmic"  # Default to cosmic for very high frequencies
    
    def _scale_to_consciousness(self, scale_name: str, resonance: float) -> str:
        """Determine consciousness level for a scale based on resonance and structure."""
        # Base consciousness on resonance and scale structure
        if resonance > 0.9:
            return "cosmic"
        elif resonance > 0.8:
            return "intuitive"
        elif resonance > 0.7:
            return "mental"
        elif resonance > 0.6:
            return "emotional"
        else:
            return "physical"
    
    @property
    def phi_inverse(self) -> float:
        """Get the inverse of phi."""
        return 1.0 / self.phi
    
    def get_note_frequency(self, note: str, tuning: str = "phi_harmonic") -> float:
        """
        Get the frequency for a note in the specified tuning.
        
        Args:
            note: Note name with octave (e.g., 'C4', 'F#5')
            tuning: Tuning system ('standard', 'phi_harmonic', 'just_intonation')
            
        Returns:
            Frequency in Hz
        """
        return self.manager.get_note_frequency(note, tuning)
        
    def get_closest_note(self, frequency: float) -> str:
        """Find the closest musical note for a given frequency."""
        return self.manager.get_closest_note(frequency)
        
    def get_scale_notes(self, root: str, scale_type: str = "major") -> List[str]:
        """Get notes for a given scale."""
        return self.manager.get_scale_notes(root, scale_type)

    def get_note_consciousness(self, note: str) -> str:
        """
        Get the consciousness level for a note.
        
        Args:
            note: Note name with octave (e.g., 'C4', 'F#5')
            
        Returns:
            Consciousness level
        """
        if note not in self.note_consciousness:
            raise ValueError(f"Unknown note: {note}")
        
        return self.note_consciousness[note]
    
    def get_chord_notes(self, root: str, chord_type: str) -> List[str]:
        """
        Get the notes in a chord.
        
        Args:
            root: Root note with octave (e.g., 'C4', 'F#5')
            chord_type: Type of chord (e.g., 'major', 'minor', 'phi')
            
        Returns:
            List of notes in the chord
        """
        if chord_type not in self.chord_types:
            raise ValueError(f"Unknown chord type: {chord_type}")
        
        # Parse root note
        note_name = ''.join(c for c in root if c.isalpha() or c == '#')
        octave = int(''.join(c for c in root if c.isdigit()))
        
        # Get intervals for chord type
        intervals = self.chord_types[chord_type]
        
        # Calculate notes
        notes = []
        root_idx = self.note_names.index(note_name)
        
        for interval in intervals:
            # Calculate new note index
            new_idx = (root_idx + interval) % 12
            new_octave = octave + (root_idx + interval) // 12
            
            # Get note name
            new_note = f"{self.note_names[new_idx]}{new_octave}"
            notes.append(new_note)
        
        return notes
    
    def get_chord_frequencies(self, root: str, chord_type: str, 
                             tuning: str = "phi_harmonic") -> List[float]:
        """
        Get the frequencies for notes in a chord.
        
        Args:
            root: Root note with octave (e.g., 'C4', 'F#5')
            chord_type: Type of chord (e.g., 'major', 'minor', 'phi')
            tuning: Tuning system ('standard', 'phi_harmonic', 'just_intonation')
            
        Returns:
            List of frequencies in Hz
        """
        notes = self.get_chord_notes(root, chord_type)
        return [self.get_note_frequency(note, tuning) for note in notes]
    
    def get_chord_consciousness(self, root: str, chord_type: str) -> str:
        """
        Get the consciousness level for a chord.
        
        Args:
            root: Root note with octave (e.g., 'C4', 'F#5')
            chord_type: Type of chord (e.g., 'major', 'minor', 'phi')
            
        Returns:
            Consciousness level
        """
        # Get chord resonance
        resonance = self.chord_resonance.get(chord_type, 0.0)
        
        # Get root note consciousness
        root_consciousness = self.get_note_consciousness(root)
        
        # Combine resonance and root consciousness
        if resonance > 0.8:
            # High resonance elevates consciousness
            consciousness_levels = list(self.consciousness_bands.keys())
            root_idx = consciousness_levels.index(root_consciousness)
            elevated_idx = min(root_idx + 1, len(consciousness_levels) - 1)
            return consciousness_levels[elevated_idx]
        else:
            return root_consciousness
    
    def get_scale_notes(self, root: str, scale_type: str = "major") -> List[str]:
        """Get notes for a given scale."""
        return self.manager.get_scale_notes(root, scale_type)
    
    def get_scale_frequencies(self, root: str, scale_type: str, 
                             tuning: str = "phi_harmonic") -> List[float]:
        """
        Get the frequencies for notes in a scale.
        
        Args:
            root: Root note with octave (e.g., 'C4', 'F#5')
            scale_type: Type of scale (e.g., 'major', 'natural_minor', 'phi')
            tuning: Tuning system ('standard', 'phi_harmonic', 'just_intonation')
            
        Returns:
            List of frequencies in Hz
        """
        notes = self.get_scale_notes(root, scale_type)
        return [self.get_note_frequency(note, tuning) for note in notes]
    
    def get_scale_consciousness(self, scale_type: str) -> str:
        """
        Get the consciousness level for a scale.
        
        Args:
            scale_type: Type of scale (e.g., 'major', 'natural_minor', 'phi')
            
        Returns:
            Consciousness level
        """
        if scale_type not in self.scale_consciousness:
            raise ValueError(f"Unknown scale type: {scale_type}")
        
        return self.scale_consciousness[scale_type]
    
    def calculate_phi_resonance(self, frequencies: List[float]) -> float:
        """
        Calculate phi-harmonic resonance for a set of frequencies.
        
        Args:
            frequencies: List of frequencies in Hz
            
        Returns:
            Resonance value (0.0 to 1.0)
        """
        if not frequencies:
            return 0.0
        
        # Calculate pairwise ratios
        ratios = []
        for i in range(len(frequencies)):
            for j in range(i + 1, len(frequencies)):
                if frequencies[i] > 0 and frequencies[j] > 0:
                    ratios.append(frequencies[j] / frequencies[i])
        
        if not ratios:
            return 0.0
        
        # Calculate alignment with phi and its powers
        phi_powers = [self.phi**n for n in range(-3, 4)]
        alignments = []
        
        for ratio in ratios:
            # Find closest phi power
            closest_phi = min(phi_powers, key=lambda x: abs(x - ratio))
            # Calculate alignment (1.0 = perfect alignment)
            alignment = 1.0 - abs(ratio - closest_phi) / closest_phi
            alignments.append(alignment)
        
        # Overall resonance is average alignment
        return sum(alignments) / len(alignments)
    
    def get_phi_harmonic_progression(self, key: str, progression_type: str = "phi") -> List[str]:
        """
        Get a phi-harmonic chord progression in the specified key.
        
        Args:
            key: Root note of the key (e.g., 'C', 'F#')
            progression_type: Type of progression ('phi', 'fibonacci', 'golden')
            
        Returns:
            List of chord symbols
        """
        # Define progression types
        progressions = {
            "phi": ["I", "V", "vi", "IV"],  # Classic progression with phi-harmonic properties
            "fibonacci": ["I", "I", "ii", "iii", "V", "VIII"],  # Based on Fibonacci numbers
            "golden": ["I", "vi", "V", "iii", "IV", "I"],  # Golden ratio-based progression
            "cosmic": ["I", "V", "vi", "iii", "IV", "I", "IV", "V"]  # Extended phi-harmonic
        }
        
        if progression_type not in progressions:
            raise ValueError(f"Unknown progression type: {progression_type}")
        
        # Get progression pattern
        pattern = progressions[progression_type]
        
        # Define chord mapping for major key
        chord_mapping = {
            "I": f"{key}",
            "ii": f"{self._get_next_note(key, 2)}m",
            "iii": f"{self._get_next_note(key, 4)}m",
            "IV": f"{self._get_next_note(key, 5)}",
            "V": f"{self._get_next_note(key, 7)}",
            "vi": f"{self._get_next_note(key, 9)}m",
            "vii": f"{self._get_next_note(key, 11)}dim",
            "VIII": f"{key}"  # Octave
        }
        
        # Convert pattern to chord symbols
        return [chord_mapping[degree] for degree in pattern]
    
    def _get_next_note(self, note: str, semitones: int) -> str:
        """Get the note that is a specified number of semitones above the given note."""
        # Parse note
        note_name = ''.join(c for c in note if c.isalpha() or c in ['#', 'b'])
        
        # Define all note names with sharps and flats
        all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        flat_equivalents = {'Bb': 'A#', 'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#'}
        
        # Convert flat to sharp equivalent if needed
        if note_name in flat_equivalents:
            note_name = flat_equivalents[note_name]
        
        try:
            # Get index in chromatic scale
            idx = all_notes.index(note_name)
            
            # Calculate new index
            new_idx = (idx + semitones) % 12
            
            # Return new note
            return all_notes[new_idx]
        except ValueError:
            print(f"Warning: Note '{note_name}' not found in chromatic scale. Using C as default.")
            return 'C'
    
    def main(self):
        """Main function to demonstrate music frequency mapping."""
        # Create frequency mapper
        mapper = QuantumPhiMusicFrequencies()
        
        # Print information about phi-harmonic musical elements
        print("Quantum Phi-Harmonic Music Frequency Mapping")
        print("=" * 50)
        
        # Print note frequencies
        print("\nPhi-Harmonic Note Frequencies (Middle Octave):")
        for note in ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]:
            freq = mapper.get_note_frequency(note, "phi_harmonic")
            consciousness = mapper.get_note_consciousness(note)
            print(f"{note}: {freq:.2f} Hz - {consciousness.title()} consciousness")
        
        # Print chord information
        print("\nPhi-Harmonic Chord Information:")
        for chord_type in ["major", "minor", "phi", "golden_triad"]:
            resonance = mapper.chord_resonance[chord_type]
            notes = mapper.get_chord_notes("C4", chord_type)
            consciousness = mapper.get_chord_consciousness("C4", chord_type)
            print(f"C {chord_type}: {', '.join(notes)} - Resonance: {resonance:.4f} - {consciousness.title()} consciousness")
        
        # Print scale information
        print("\nPhi-Harmonic Scale Information:")
        for scale_type in ["major", "fibonacci", "phi", "golden"]:
            resonance = mapper.scale_resonance[scale_type]
            consciousness = mapper.scale_consciousness[scale_type]
            print(f"{scale_type.title()} scale - Resonance: {resonance:.4f} - {consciousness.title()} consciousness")
        
        # Print phi-harmonic chord progressions
        print("\nPhi-Harmonic Chord Progressions:")
        for prog_type in ["phi", "fibonacci", "golden", "cosmic"]:
            progression = mapper.get_phi_harmonic_progression("C", prog_type)
            print(f"{prog_type.title()} progression: {' - '.join(progression)}")


class FrequencyManager:
    """
    Manages frequency calculations and note mappings for the quantum music system.
    """

    def __init__(self, core):
        self.core = core
        self.phi = float(core.PHI)
        
        # Standard note frequencies (A4 = 440 Hz)
        self.base_freq = 440.0
        self.note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        # Initialize frequency mappings
        self._init_frequency_mappings()
        
    def _init_frequency_mappings(self):
        """Initialize frequency to note mappings."""
        self.note_to_freq = {}
        self.freq_to_note = {}
        
        # Generate frequencies for notes from C0 to B8
        for octave in range(9):
            for i, note in enumerate(self.note_names):
                # Calculate frequency using equal temperament formula
                n = i - 9  # Steps from A4 (A4 is the 10th note in octave 4)
                n += (octave - 4) * 12  # Adjust for octave
                freq = self.base_freq * (2 ** (n/12))
                
                note_name = f"{note}{octave}"
                self.note_to_freq[note_name] = freq
                self.freq_to_note[freq] = note_name
    
    def get_note_frequency(self, note: str, tuning: str = "standard") -> float:
        """Get frequency for a given note."""
        if tuning == "standard":
            return self.note_to_freq.get(note, 440.0)
        elif tuning == "phi_harmonic":
            base_freq = self.note_to_freq.get(note, 440.0)
            return base_freq * self.phi
        else:
            return self.note_to_freq.get(note, 440.0)
    
    def get_closest_note(self, frequency: float) -> str:
        """Find the closest musical note for a given frequency."""
        if frequency <= 0:
            return "A4"  # Default to A4 for invalid frequencies
            
        # Calculate the number of semitones from A4 (440 Hz)
        n = round(12 * math.log2(frequency / self.base_freq))
        
        # Calculate the octave and note index
        octave = 4 + (n + 9) // 12  # A4 is in octave 4
        note_idx = (n + 9) % 12  # A is index 9 in note_names
        
        # Ensure octave is in valid range
        octave = max(0, min(8, octave))
        
        # Construct note name
        note = self.note_names[note_idx]
        return f"{note}{octave}"
    
    def get_scale_notes(self, root_note: str, scale_type: str = "major") -> List[str]:
        """Get notes for a given scale."""
        # Scale patterns (steps between notes)
        scale_patterns = {
            "major": [2, 2, 1, 2, 2, 2, 1],
            "natural_minor": [2, 1, 2, 2, 1, 2, 2],
            "harmonic_minor": [2, 1, 2, 2, 1, 3, 1],
            "pentatonic": [2, 2, 3, 2, 3],
            "phi": [int(self.phi) % 2, 2, 1, int(self.phi**2) % 2, 2, 1],
            "fibonacci": [1, 1, 2, 3, 5 % 2],
            "golden": [int(self.phi * 2) % 3, int(self.phi**2) % 3, int(self.phi**3) % 3]
        }
        
        pattern = scale_patterns.get(scale_type, scale_patterns["major"])
        
        # Parse root note
        note = root_note[:-1]  # Remove octave number
        octave = int(root_note[-1])
        current_idx = self.note_names.index(note)
        
        # Generate scale
        scale = [root_note]
        for step in pattern:
            current_idx += step
            new_octave = octave + (current_idx // 12)
            new_note = self.note_names[current_idx % 12]
            scale.append(f"{new_note}{new_octave}")
            
        return scale


if __name__ == "__main__":
    QuantumPhiMusicFrequencies().main()
