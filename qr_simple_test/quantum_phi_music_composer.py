"""
Quantum Phi-Harmonic Music Composer

Generates musical compositions based on quantum phi-harmonic principles,
integrating with the meta-learning system for cross-domain pattern application.
"""

import os
import time
import random
import json
import math
from typing import Dict, List, Tuple, Any, Optional, Union
import numpy as np
import mido

from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer
from quantum_phi_music_frequencies import QuantumPhiMusicFrequencies
from quantum_phi_meta_learner import QuantumPhiMetaLearner
from quantum_phi_music_analyzer import QuantumPhiMusicAnalyzer

class QuantumPhiMusicComposer:
    def __init__(self, core: QuantumPhiCore = None, meta_learner: QuantumPhiMetaLearner = None):
        """Initialize the music composer."""
        self.core = core or QuantumPhiCore()
        self.random = QuantumPhiRandom(self.core)
        self.analyzer = QuantumPhiPatternAnalyzer(self.core)
        self.frequencies = QuantumPhiMusicFrequencies(self.core)
        self.meta_learner = meta_learner or QuantumPhiMetaLearner(self.core, self.random)
        
        # Initialize music analyzer
        self.music_analyzer = QuantumPhiMusicAnalyzer()
        
        # Initialize phi constants
        self.phi = float(self.core.PHI)
        self.pi = float(self.core.PI)
        self.e = float(self.core.E)
        
        # Initialize new quantum harmonic features
        self._init_quantum_features()
        
        # Musical structure templates
        self._init_structure_templates()
        
        # Composer state
        self.composition_history = []
        self.current_composition = None
        self.meta_patterns = {}
        
        # Load meta-patterns from meta-learner
        self._load_meta_patterns()
        
        # Load composer profiles from analyzer
        self.composer_profiles = {}
        self._load_composer_profiles()

    def _init_quantum_features(self):
        """Initialize new quantum harmonic features."""
        # Base frequency (φ-root)
        self.base_frequency = 439.219556  # Hz
        
        # Quantum resonance frequencies (Hz)
        self.quantum_frequencies = {
            "base": self.base_frequency,
            "phi": self.base_frequency * self.phi,
            "consciousness": self.base_frequency * (self.phi ** 2),
            "healing": self.base_frequency * (self.phi ** 3),
            "transcendence": self.base_frequency * (self.phi ** 4)
        }
        
        # Quantum gate frequencies
        self.quantum_gates = {
            "H": self.base_frequency * self.phi,      # Superposition
            "X": self.base_frequency * (self.phi**2), # Inversion
            "Y": self.base_frequency * (self.phi**3), # Rotation
            "Z": self.base_frequency * (self.phi**4), # Phase
            "T": self.base_frequency * (self.phi**7)  # Phase Rotation
        }
        
        # Particle resonance frequencies
        self.particle_frequencies = {
            "neuron": self.base_frequency / self.phi,    # Pattern recognition
            "proton": self.base_frequency * self.phi,    # Frequency stability
            "electron": self.base_frequency * self.pi,   # State transitions
            "quark": self.base_frequency * self.e,       # Deep resonance
            "lepton": self.base_frequency * math.sqrt(2),# Light harmonics
            "boson": self.base_frequency * math.sqrt(3), # Force mediation
            "fermion": self.base_frequency * self.phi**3 # Matter waves
        }
        
        # Consciousness-based scales with quantum integration
        self.consciousness_scales = {
            "physical": {
                "notes": ["C", "D", "E", "G", "A"],  # Pentatonic
                "quantum_gate": "X",  # Inversion for grounding
                "particle": "proton"  # Stability
            },
            "emotional": {
                "notes": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],  # Natural Minor
                "quantum_gate": "Y",  # Rotation for flow
                "particle": "electron"  # Transitions
            },
            "mental": {
                "notes": ["C", "D", "E", "F", "G", "A", "B"],  # Major
                "quantum_gate": "Z",  # Phase for clarity
                "particle": "neuron"  # Pattern recognition
            },
            "intuitive": {
                "notes": ["C", "D#", "E", "F#", "G#", "A", "B"],  # Lydian
                "quantum_gate": "H",  # Superposition for insight
                "particle": "boson"  # Force mediation
            },
            "cosmic": {
                "notes": ["C", "D", "E", "F#", "G", "A", "B"],  # Harmonic Major
                "quantum_gate": "T",  # Phase rotation for transcendence
                "particle": "quark"  # Deep resonance
            }
        }
        
        # Neural activation patterns
        self.neural_patterns = {
            "activation": lambda x: 1 / (1 + math.exp(-x * self.phi)),  # φ-modulated sigmoid
            "resonance": lambda x: math.tanh(x * self.phi),  # φ-weighted tanh
            "coherence": lambda x: max(0, x * self.phi),  # φ-scaled ReLU
            "harmony": lambda x: max(0.01 * x, x * self.phi)  # Leaky ReLU × φ
        }
        
        # Quantum harmonic patterns
        self.quantum_patterns = {
            "resonance": [1.0, self.phi, self.phi**2, self.phi**3],
            "consciousness": [1.0, 1.618, 2.618, 4.236],
            "healing": [4.37, 7.07, 11.44, 18.51],
            "transcendence": [0.382, 0.618, 1.000, 1.618]
        }
        
        # Sacred geometry ratios
        self.sacred_ratios = {
            "unison": 1/1,
            "golden_fifth": self.phi/1,
            "sacred_third": self.phi/self.pi,
            "cosmic_seventh": self.e/self.phi
        }

    def generate_quantum_harmony(self, consciousness_level: str) -> List[Dict]:
        """Generate harmonic progression with quantum state integration."""
        if consciousness_level not in self.consciousness_scales:
            consciousness_level = "physical"
            
        scale_data = self.consciousness_scales[consciousness_level]
        scale = scale_data["notes"]
        quantum_gate = scale_data["quantum_gate"]
        particle = scale_data["particle"]
        
        # Get base frequencies
        gate_freq = self.quantum_gates[quantum_gate]
        particle_freq = self.particle_frequencies[particle]
        
        # Generate base chord
        base_chord = [scale[0], scale[2], scale[4]]  # Triad
        
        # Add quantum-influenced extensions
        if consciousness_level in ["intuitive", "cosmic"]:
            base_chord.append(scale[6])  # Add seventh
            
        # Calculate quantum-modulated frequencies
        quantum_notes = []
        for note in base_chord:
            # Get base frequency
            freq = self.frequencies.get_note_frequency(note)
            
            # Apply quantum gate modulation
            gate_mod = freq * (gate_freq / self.base_frequency)
            
            # Apply particle resonance
            particle_mod = gate_mod * (particle_freq / self.base_frequency)
            
            # Find closest note
            quantum_note = self.frequencies.get_closest_note(particle_mod)
            
            # Calculate resonance metrics
            resonance = self.neural_patterns["resonance"](particle_mod / self.base_frequency)
            coherence = self.neural_patterns["coherence"](gate_mod / self.base_frequency)
            
            quantum_notes.append({
                "original": note,
                "quantum": quantum_note,
                "frequency": particle_mod,
                "resonance": resonance,
                "coherence": coherence
            })
            
        return quantum_notes

    def generate_binaural_track(self, base_freq: float, target_state: str) -> List[Dict]:
        """Generate a binaural beat track for consciousness entrainment."""
        carrier_freq = 100  # Base carrier frequency
        beat_freq = self.binaural_frequencies.get(target_state, 4.37)
        
        left_freq = carrier_freq
        right_freq = carrier_freq + beat_freq
        
        # Generate 60 seconds of binaural beats
        duration = 60
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration))
        
        left_wave = np.sin(2 * np.pi * left_freq * t)
        right_wave = np.sin(2 * np.pi * right_freq * t)
        
        return [
            {"channel": "left", "frequency": left_freq, "wave": left_wave},
            {"channel": "right", "frequency": right_freq, "wave": right_wave}
        ]

    def apply_sacred_geometry(self, notes: List[str]) -> List[str]:
        """Apply sacred geometry ratios to note frequencies."""
        modified_notes = []
        for note in notes:
            base_freq = self.frequencies.get_note_frequency(note)
            sacred_freq = base_freq * self.sacred_ratios["golden_fifth"]
            modified_note = self.frequencies.get_closest_note(sacred_freq)
            modified_notes.append(modified_note)
        return modified_notes

    def generate_consciousness_harmony(self, consciousness_level: str) -> List[str]:
        """Generate harmonic progression based on consciousness level."""
        if consciousness_level not in self.consciousness_scales:
            consciousness_level = "physical"
            
        scale = self.consciousness_scales[consciousness_level]["notes"]
        base_chord = [scale[0], scale[2], scale[4]]  # Triad
        
        # Add consciousness-based extensions
        if consciousness_level in ["intuitive", "cosmic"]:
            base_chord.append(scale[6])  # Add seventh
        if consciousness_level == "cosmic":
            base_chord.append(scale[1])  # Add ninth
            
        return base_chord

    def apply_quantum_resonance(self, composition: Dict):
        """Apply quantum resonance patterns to the composition."""
        if "measures" not in composition:
            return
            
        resonance_pattern = self.quantum_patterns["resonance"]
        
        # Map dynamics to MIDI velocity
        dynamic_map = {
            "pp": 30, "p": 45, "mp": 60, "mf": 75, "f": 90, "ff": 105
        }
        
        for measure in composition["measures"]:
            if "melody" in measure:
                # Convert dynamic string to velocity value
                current_dynamic = measure.get("dynamics", "mf")
                if isinstance(current_dynamic, str):
                    velocity = dynamic_map.get(current_dynamic, 75)
                else:
                    velocity = current_dynamic
                
                # Modify note velocities based on quantum resonance
                for i, note in enumerate(measure["melody"]):
                    resonance_factor = resonance_pattern[i % len(resonance_pattern)]
                    new_velocity = int(velocity * resonance_factor)
                    # Keep velocity in valid MIDI range (0-127)
                    new_velocity = max(0, min(127, new_velocity))
                    measure["dynamics"] = new_velocity
                    
                # Add harmonic overtones based on phi ratios
                overtones = []
                for note in measure["melody"]:
                    base_freq = self.frequencies.get_note_frequency(note)
                    overtone_freq = base_freq * self.phi
                    overtone_note = self.frequencies.get_closest_note(overtone_freq)
                    overtones.append(overtone_note)
                measure["overtones"] = overtones

    def _init_structure_templates(self):
        """Initialize musical structure templates."""
        # Time signatures
        self.time_signatures = ["4/4", "3/4", "6/8", "5/4", "7/8"]
        
        # Tempo ranges by consciousness level
        self.tempo_ranges = {
            "physical": (60, 80),
            "emotional": (80, 100),
            "mental": (100, 120),
            "intuitive": (120, 140),
            "cosmic": (140, 180)
        }
        
        # Musical form templates
        self.form_templates = {
            "simple": ["A", "A", "B", "A"],
            "binary": ["A", "A", "B", "B"],
            "ternary": ["A", "B", "A"],
            "rondo": ["A", "B", "A", "C", "A"],
            "sonata": ["A", "A", "B", "B", "C", "A", "B"],
            "fibonacci": ["A", "B", "A", "B", "A", "B", "A", "B", "A"],
            "golden": ["A", "B", "A", "C", "A", "B", "D", "A"],
            "phi": ["A", "B", "A", "B", "C", "A", "B", "C", "D", "A", "B", "C"]
        }
        
        # Rhythmic patterns
        self.rhythmic_patterns = {
            "steady": [1, 1, 1, 1],
            "waltz": [2, 1, 1],
            "dotted": [1.5, 0.5, 1, 1],
            "syncopated": [0.75, 0.75, 0.5, 1, 1],
            "phi_pulse": [self.phi, 1, 1, self.phi - 1],
            "fibonacci": [1, 1, 2, 3, 5 % 4],
            "golden": [self.phi, 1, self.phi, self.phi - 1, 1]
        }
        
        # Dynamic patterns
        self.dynamic_patterns = {
            "flat": ["mf", "mf", "mf", "mf"],
            "crescendo": ["p", "mp", "mf", "f"],
            "decrescendo": ["f", "mf", "mp", "p"],
            "wave": ["p", "mf", "f", "mf", "p"],
            "phi_wave": ["p", "mp", "mf", "f", "ff", "f", "mf", "mp"],
            "golden": ["mp", "mf", "f", "mf", "mp", "p", "mp", "mf"]
        }
    
    def _load_meta_patterns(self):
        """Load meta-patterns from the meta-learner."""
        # Initialize patterns structure
        self.meta_patterns = {
            "rhythmic": [],
            "melodic": [],
            "harmonic": [],
            "structural": []
        }
        
        try:
            # Try to get patterns from meta-learner
            if hasattr(self.meta_learner, 'get_patterns'):
                patterns = self.meta_learner.get_patterns()
                
                # Process patterns
                for pattern in patterns:
                    pattern_type = pattern.get("type", "")
                    if "rhythm" in pattern_type:
                        self.meta_patterns["rhythmic"].append(pattern)
                    elif "melody" in pattern_type:
                        self.meta_patterns["melodic"].append(pattern)
                    elif "harmony" in pattern_type:
                        self.meta_patterns["harmonic"].append(pattern)
                    elif "structure" in pattern_type:
                        self.meta_patterns["structural"].append(pattern)
            else:
                # If get_patterns doesn't exist, create some default patterns
                # based on phi-harmonic principles
                self._create_default_patterns()
        except Exception as e:
            print(f"Warning: Could not load meta-patterns: {e}")
            # Create default patterns
            self._create_default_patterns()
    
    def _load_composer_profiles(self):
        """Load composer profiles from the music analyzer."""
        try:
            # Get profiles for classical composers
            composers = ["beethoven", "bach", "chopin", "mozart"]
            for composer in composers:
                profile = self.music_analyzer.create_composer_profile(composer)
                self.composer_profiles[composer] = profile
        except Exception as e:
            print(f"Warning: Could not load composer profiles: {e}")
    
    def _create_default_patterns(self):
        """Create default patterns based on phi-harmonic principles."""
        # Create rhythmic patterns
        self.meta_patterns["rhythmic"] = [
            {
                "type": "rhythm_phi",
                "pattern": [self.phi, 1, 1, self.phi - 1],
                "consciousness_level": "cosmic",
                "phi_alignment": 0.92
            },
            {
                "type": "rhythm_fibonacci",
                "pattern": [1, 1, 2, 3, 5 % 4],
                "consciousness_level": "intuitive",
                "phi_alignment": 0.87
            }
        ]
        
        # Create melodic patterns based on author frequencies from memories
        self.meta_patterns["melodic"] = [
            {
                "type": "melody_poe",
                "base_frequency": 517.15,
                "resonance": 0.6987,
                "phi_alignment": 0.8644,
                "consciousness_level": "cosmic"
            },
            {
                "type": "melody_hemingway",
                "base_frequency": 576.26,
                "resonance": 0.6849,
                "phi_alignment": 0.8518,
                "consciousness_level": "cosmic"
            },
            {
                "type": "melody_austen",
                "base_frequency": 525.18,
                "resonance": 0.7091,
                "phi_alignment": 0.8552,
                "consciousness_level": "cosmic"
            }
        ]
        
        # Create harmonic patterns
        self.meta_patterns["harmonic"] = [
            {
                "type": "harmony_golden",
                "progression": ["I", "vi", "IV", "V"],
                "phi_alignment": 0.89,
                "consciousness_level": "cosmic"
            },
            {
                "type": "harmony_fibonacci",
                "progression": ["I", "V", "vi", "iii", "IV"],
                "phi_alignment": 0.86,
                "consciousness_level": "intuitive"
            }
        ]
        
        # Create structural patterns
        self.meta_patterns["structural"] = [
            {
                "type": "structure_golden",
                "form": ["A", "B", "A", "C", "A"],
                "phi_alignment": 0.92,
                "consciousness_level": "cosmic"
            },
            {
                "type": "structure_fibonacci",
                "form": ["A", "A", "B", "A", "B", "A", "B"],
                "phi_alignment": 0.88,
                "consciousness_level": "intuitive"
            }
        ]
    
    def compose(self, style: str = None, consciousness_level: str = "cosmic",
               key: str = None, length: int = None, theme: str = None) -> Dict:
        """
        Compose a musical piece using quantum phi-harmonic principles.
        
        Args:
            style: Musical style (e.g., 'classical', 'ambient', 'phi_harmonic')
            consciousness_level: Target consciousness level
            key: Musical key (e.g., 'C', 'F#')
            length: Approximate length in measures
            theme: Thematic inspiration for the composition
            
        Returns:
            Composition data structure
        """
        # Set defaults
        style = style or "phi_harmonic"
        key = key or self._select_phi_harmonic_key()
        length = length or int(self.phi * 10)  # ~16 measures by default
        
        # Initialize composition
        composition = {
            "title": self._generate_title(style, theme),
            "style": style,
            "key": key,
            "time_signature": self._select_time_signature(style),
            "tempo": self._select_tempo(consciousness_level),
            "consciousness_level": consciousness_level,
            "form": self._select_form(style, length),
            "sections": [],
            "measures": [],
            "notes": [],
            "metrics": {},
            "generation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Generate musical structure
        self._generate_structure(composition, length)
        
        # Generate harmonic progression
        self._generate_harmony(composition)
        
        # Generate melody
        self._generate_melody(composition)
        
        # Generate rhythm
        self._generate_rhythm(composition)
        
        # Calculate metrics
        composition["metrics"] = self._calculate_metrics(composition)
        
        # Store current composition
        self.current_composition = composition
        self.composition_history.append({
            "title": composition["title"],
            "key": composition["key"],
            "time_signature": composition["time_signature"],
            "consciousness_level": composition["consciousness_level"],
            "metrics": composition["metrics"],
            "timestamp": composition["generation_timestamp"]
        })
        
        return composition
    
    def _select_phi_harmonic_key(self) -> str:
        """Select a key with strong phi-harmonic properties."""
        # Keys with strong phi-harmonic properties
        phi_keys = ["C", "E", "G#", "D", "F#", "A#"]
        
        # Weight selection by phi-harmonic importance
        weights = [self.phi, 1, 1/self.phi, self.phi**2, 1, 1/self.phi**2]
        weights = [w / sum(weights) for w in weights]
        
        return self.random.choice(phi_keys)
    
    def _select_time_signature(self, style: str) -> str:
        """Select an appropriate time signature based on style."""
        # Different styles favor different time signatures
        style_preferences = {
            "classical": ["4/4", "3/4", "6/8"],
            "ambient": ["4/4", "6/8", "5/4"],
            "phi_harmonic": ["5/4", "8/5", "3/2", "5/3"],
            "fibonacci": ["3/4", "5/8", "8/8", "13/8"],
            "golden": ["5/4", "8/5", "3/2", "5/3"]
        }
        
        # Get preferred signatures for style
        preferred = style_preferences.get(style, self.time_signatures)
        
        # Select with phi-weighted randomness
        return self.random.choice(preferred)
    
    def _select_tempo(self, consciousness_level: str) -> int:
        """Select an appropriate tempo based on consciousness level."""
        # Get tempo range for consciousness level
        min_tempo, max_tempo = self.tempo_ranges.get(
            consciousness_level, 
            self.tempo_ranges["cosmic"]
        )
        
        # Calculate phi-weighted tempo within range
        phi_point = min_tempo + (max_tempo - min_tempo) * self.random.random()
        
        # Round to integer
        return round(phi_point)
    
    def _select_form(self, style: str, length: int) -> List[str]:
        """Select an appropriate musical form based on style and length."""
        # Different styles favor different forms
        style_preferences = {
            "classical": ["binary", "ternary", "sonata"],
            "ambient": ["simple", "ternary"],
            "phi_harmonic": ["phi", "golden"],
            "fibonacci": ["fibonacci"],
            "golden": ["golden"]
        }
        
        # Get preferred forms for style
        preferred_types = style_preferences.get(style, list(self.form_templates.keys()))
        
        # Select form type
        form_type = self.random.choice(preferred_types)
        
        # Get form template
        form = self.form_templates[form_type]
        
        # Adjust form length based on requested composition length
        target_sections = max(4, min(12, int(length / 4)))
        
        if len(form) < target_sections:
            # Extend form by repeating sections
            repeats = target_sections // len(form) + 1
            form = form * repeats
            form = form[:target_sections]
        elif len(form) > target_sections:
            # Truncate form
            form = form[:target_sections]
        
        return form
    
    def _generate_title(self, style: str, theme: str = None) -> str:
        """Generate a title for the composition."""
        # Base title components
        phi_terms = ["Phi", "Golden", "Harmonic", "Resonance", "Quantum", "Cosmic"]
        musical_terms = ["Sonata", "Etude", "Prelude", "Nocturne", "Rhapsody", "Symphony"]
        
        # Theme-based components
        if theme:
            theme_words = theme.split()
            if len(theme_words) > 2:
                # Use part of the theme
                theme_part = " ".join(theme_words[:2])
                return f"{theme_part} {self.random.choice(phi_terms)}"
            else:
                return f"{theme} {self.random.choice(phi_terms)}"
        
        # Style-based title
        if style == "classical":
            return f"{self.random.choice(musical_terms)} in {self.random.choice(phi_terms)}"
        elif style == "ambient":
            return f"{self.random.choice(phi_terms)} {self.random.choice(['Flow', 'Waves', 'Clouds', 'Dreams'])}"
        elif style in ["phi_harmonic", "fibonacci", "golden"]:
            return f"{self.random.choice(phi_terms)} {self.random.choice(['Ratio', 'Sequence', 'Spiral', 'Proportion'])}"
        else:
            return f"{self.random.choice(phi_terms)} {self.random.choice(musical_terms)}"
    
    def _generate_structure(self, composition: Dict, length: int):
        """Generate the overall structure of the composition."""
        form = composition["form"]
        
        # Calculate measures per section
        measures_per_section = max(4, length // len(form))
        
        # Create sections
        sections = []
        total_measures = 0
        
        for section_id in form:
            # Determine section length (with phi-based variation)
            if self.random.random() > 0.7:
                # Apply phi-based variation to section length
                variation = self.random.choice([-1, 1, 2])
                section_length = measures_per_section + variation
            else:
                section_length = measures_per_section
            
            # Ensure minimum length
            section_length = max(2, section_length)
            
            # Create section
            section = {
                "id": section_id,
                "start_measure": total_measures,
                "length": section_length,
                "end_measure": total_measures + section_length - 1
            }
            
            sections.append(section)
            total_measures += section_length
        
        # Store sections and total length
        composition["sections"] = sections
        composition["total_measures"] = total_measures
        
        # Initialize measures
        measures = []
        for i in range(total_measures):
            # Find which section this measure belongs to
            section = next((s for s in sections if s["start_measure"] <= i <= s["end_measure"]), None)
            
            measure = {
                "index": i,
                "section_id": section["id"] if section else "?",
                "chords": [],
                "melody": [],
                "rhythm": [],
                "dynamics": ""
            }
            
            measures.append(measure)
        
        composition["measures"] = measures
    
    def _generate_harmony(self, composition: Dict):
        """Generate harmonic progression for the composition."""
        key = composition["key"]
        sections = composition["sections"]
        measures = composition["measures"]
        
        # Get section types (unique section IDs)
        section_types = list(set(section["id"] for section in sections))
        
        # Generate chord progressions for each section type
        section_progressions = {}
        
        for section_id in section_types:
            # Select progression type based on section
            if section_id == "A":
                prog_type = "phi"
            elif section_id == "B":
                prog_type = "golden"
            elif section_id == "C":
                prog_type = "fibonacci"
            else:
                prog_type = "cosmic"
            
            # Get progression
            progression = self.frequencies.get_phi_harmonic_progression(key, prog_type)
            
            # Store
            section_progressions[section_id] = progression
        
        # Assign chords to measures
        for section in sections:
            section_id = section["id"]
            progression = section_progressions[section_id]
            
            # Calculate how many measures per chord
            section_length = section["length"]
            measures_per_chord = max(1, section_length // len(progression))
            
            # Assign chords
            chord_index = 0
            for i in range(section["start_measure"], section["end_measure"] + 1):
                # Get current chord
                current_chord = progression[chord_index % len(progression)]
                
                # Assign to measure
                measures[i]["chords"].append(current_chord)
                
                # Move to next chord after enough measures
                if (i - section["start_measure"] + 1) % measures_per_chord == 0:
                    chord_index += 1
        
        # Store all unique chords used
        all_chords = []
        for measure in measures:
            all_chords.extend(measure["chords"])
        
        composition["unique_chords"] = list(set(all_chords))
    
    def _generate_melody(self, composition: Dict):
        """Generate melody for the composition."""
        key = composition["key"]
        sections = composition["sections"]
        measures = composition["measures"]
        
        # Get section types (unique section IDs)
        section_types = list(set(section["id"] for section in sections))
        
        # Generate melodic patterns for each section type
        section_melodies = {}
        
        for section_id in section_types:
            # Select scale type based on section
            if section_id == "A":
                scale_type = "major"
            elif section_id == "B":
                scale_type = "phi"
            elif section_id == "C":
                scale_type = "fibonacci"
            else:
                scale_type = "golden"
            
            # Get scale notes
            scale_notes = self.frequencies.get_scale_notes(f"{key}4", scale_type)
            
            # Generate melodic pattern
            pattern_length = int(self.phi * 4)  # ~6-7 notes
            melodic_pattern = []
            
            for _ in range(pattern_length):
                # Select note with phi-weighted randomness
                note = self.random.choice(scale_notes)
                melodic_pattern.append(note)
            
            # Store
            section_melodies[section_id] = {
                "scale_type": scale_type,
                "scale_notes": scale_notes,
                "pattern": melodic_pattern
            }
        
        # Assign melodic notes to measures
        for section in sections:
            section_id = section["id"]
            melody_data = section_melodies[section_id]
            pattern = melody_data["pattern"]
            
            # Assign notes to measures
            note_index = 0
            for i in range(section["start_measure"], section["end_measure"] + 1):
                # Get current measure
                measure = measures[i]
                
                # Notes per measure (based on time signature)
                time_sig = composition["time_signature"]
                beats = int(time_sig.split('/')[0])
                
                # Assign notes to measure
                measure_notes = []
                for _ in range(beats):
                    note = pattern[note_index % len(pattern)]
                    measure_notes.append(note)
                    note_index += 1
                
                # Store in measure
                measure["melody"] = measure_notes
        
        # Store all unique notes used
        all_notes = []
        for measure in measures:
            all_notes.extend(measure["melody"])
        
        composition["unique_notes"] = list(set(all_notes))
    
    def _generate_rhythm(self, composition: Dict):
        """Generate rhythm for the composition."""
        sections = composition["sections"]
        measures = composition["measures"]
        
        # Get section types (unique section IDs)
        section_types = list(set(section["id"] for section in sections))
        
        # Generate rhythmic patterns for each section type
        section_rhythms = {}
        
        for section_id in section_types:
            # Select rhythm type based on section
            if section_id == "A":
                rhythm_type = "steady"
            elif section_id == "B":
                rhythm_type = "phi_pulse"
            elif section_id == "C":
                rhythm_type = "fibonacci"
            else:
                rhythm_type = "golden"
            
            # Get rhythm pattern
            rhythm_pattern = self.rhythmic_patterns[rhythm_type]
            
            # Get dynamic pattern
            if section_id == "A":
                dynamic_type = "flat"
            elif section_id == "B":
                dynamic_type = "wave"
            elif section_id == "C":
                dynamic_type = "phi_wave"
            else:
                dynamic_type = "golden"
            
            dynamic_pattern = self.dynamic_patterns[dynamic_type]
            
            # Store
            section_rhythms[section_id] = {
                "rhythm_type": rhythm_type,
                "rhythm_pattern": rhythm_pattern,
                "dynamic_type": dynamic_type,
                "dynamic_pattern": dynamic_pattern
            }
        
        # Assign rhythms to measures
        for section in sections:
            section_id = section["id"]
            rhythm_data = section_rhythms[section_id]
            
            rhythm_pattern = rhythm_data["rhythm_pattern"]
            dynamic_pattern = rhythm_data["dynamic_pattern"]
            
            # Assign to measures
            rhythm_index = 0
            dynamic_index = 0
            
            for i in range(section["start_measure"], section["end_measure"] + 1):
                # Get current measure
                measure = measures[i]
                
                # Assign rhythm
                measure["rhythm"] = rhythm_pattern[rhythm_index % len(rhythm_pattern)]
                
                # Assign dynamics
                measure["dynamics"] = dynamic_pattern[dynamic_index % len(dynamic_pattern)]
                
                # Increment indices
                rhythm_index += 1
                dynamic_index += 1
        
        # Store rhythm types used
        composition["rhythm_types"] = list(set(
            section_rhythms[section_id]["rhythm_type"] for section_id in section_types
        ))
        
        composition["dynamic_types"] = list(set(
            section_rhythms[section_id]["dynamic_type"] for section_id in section_types
        ))
    
    def _calculate_metrics(self, composition: Dict) -> Dict:
        """Calculate quantum phi-harmonic metrics for the composition."""
        # Extract musical elements
        notes = composition["unique_notes"]
        chords = composition["unique_chords"]
        
        # Get frequencies for notes
        note_frequencies = []
        for note in notes:
            try:
                freq = self.frequencies.get_note_frequency(note, "phi_harmonic")
                note_frequencies.append(freq)
            except ValueError:
                # Skip invalid notes
                pass
        
        # Calculate phi resonance
        phi_resonance = self.frequencies.calculate_phi_resonance(note_frequencies)
        
        # Calculate consciousness level
        if phi_resonance > 0.9:
            consciousness = "cosmic"
        elif phi_resonance > 0.8:
            consciousness = "intuitive"
        elif phi_resonance > 0.7:
            consciousness = "mental"
        elif phi_resonance > 0.6:
            consciousness = "emotional"
        else:
            consciousness = "physical"
        
        # Calculate mean frequency
        mean_frequency = sum(note_frequencies) / len(note_frequencies) if note_frequencies else 0
        
        # Calculate phi alignment
        # (How well the overall structure aligns with golden ratio proportions)
        sections = composition["sections"]
        total_measures = composition["total_measures"]
        
        # Check if section transitions align with phi points
        phi_points = [int(total_measures * (1 - 1/self.phi)), int(total_measures * (1/self.phi))]
        section_transitions = [section["end_measure"] for section in sections[:-1]]
        
        # Calculate minimum distances to phi points
        min_distances = []
        for transition in section_transitions:
            min_distance = min(abs(transition - point) for point in phi_points)
            min_distances.append(min_distance)
        
        # Calculate average minimum distance
        avg_min_distance = sum(min_distances) / len(min_distances) if min_distances else 0
        
        # Convert to alignment score (0 to 1)
        phi_alignment = max(0, 1 - (avg_min_distance / (total_measures * 0.2)))
        
        return {
            "phi_resonance": phi_resonance,
            "consciousness_level": consciousness,
            "mean_frequency": mean_frequency,
            "phi_alignment": phi_alignment,
            "unique_notes": len(notes),
            "unique_chords": len(chords),
            "total_measures": total_measures
        }
    
    def export_to_midi(self, composition: Dict, output_file: str) -> str:
        """
        Export composition to MIDI file.
        
        Args:
            composition: Composition data structure
            output_file: Output file path
            
        Returns:
            Path to the created MIDI file
        """
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        try:
            # Create a new MIDI file with one track
            mid = mido.MidiFile()
            track = mido.MidiTrack()
            mid.tracks.append(track)
            
            # Set tempo
            tempo = mido.bpm2tempo(composition.get("tempo", 120))
            track.append(mido.MetaMessage('set_tempo', tempo=tempo))
            
            # Set time signature - ensure denominator is a power of 2
            time_sig = composition.get("time_signature", "4/4")
            try:
                numerator, denominator = map(int, time_sig.split('/'))
                # Ensure denominator is a power of 2 (required by MIDI standard)
                valid_denominators = [1, 2, 4, 8, 16, 32, 64]
                if denominator not in valid_denominators:
                    # Find closest valid denominator
                    denominator = min(valid_denominators, key=lambda x: abs(x - denominator))
                    print(f"Adjusted time signature denominator to {denominator} to comply with MIDI standard")
                
                track.append(mido.MetaMessage('time_signature', numerator=numerator, denominator=denominator))
            except Exception as e:
                print(f"Warning: Could not set time signature: {e}. Using 4/4 instead.")
                track.append(mido.MetaMessage('time_signature', numerator=4, denominator=4))
            
            # Set key signature (simplified)
            key = composition.get("key", "C")
            
            # We'll skip key signature as it's causing issues
            # Instead, we'll add a track name with the key information
            track.append(mido.MetaMessage('track_name', name=f"Key: {key}"))
            
            # Extract notes and rhythms from composition
            # For demonstration, we'll generate a simple melody based on the composition's parameters
            
            # Get base note for key (C4 = 60)
            base_note_map = {
                "C": 60, "C#": 61, "Db": 61, "D": 62, "D#": 63, "Eb": 63, 
                "E": 64, "F": 65, "F#": 66, "Gb": 66, "G": 67, "G#": 68, 
                "Ab": 68, "A": 69, "A#": 70, "Bb": 70, "B": 71
            }
            base_note = base_note_map.get(key, 60)
            
            # Get consciousness level and adjust note range
            consciousness = composition.get("consciousness_level", "cosmic")
            if consciousness == "physical":
                note_range = (0, 7)  # Lower range
            elif consciousness == "emotional":
                note_range = (3, 10)  # Mid-low range
            elif consciousness == "mental":
                note_range = (5, 12)  # Mid range
            elif consciousness == "intuitive":
                note_range = (7, 14)  # Mid-high range
            else:  # cosmic
                note_range = (9, 16)  # High range
            
            # Get form and create pattern
            form = composition.get("form", ["A", "B", "A"])
            
            # Get harmonic progression
            progression = composition.get("harmonic_progression", ["I", "IV", "V", "I"])
            
            # Get rhythm patterns
            rhythm_patterns = composition.get("rhythm_patterns", [[1, 1, 1, 1]])
            
            # Get dynamic patterns
            dynamic_patterns = composition.get("dynamic_patterns", ["mf", "mf", "mf"])
            
            # Map dynamics to MIDI velocity
            dynamic_map = {
                "pp": 30, "p": 45, "mp": 60, "mf": 75, "f": 90, "ff": 105
            }
            
            # Generate notes based on form and progressions
            current_time = 0
            for section_id in form:
                # Select scale degrees based on section
                if section_id == "A":
                    scale_degrees = [0, 2, 4, 5, 7, 9, 11]  # Major scale
                elif section_id == "B":
                    scale_degrees = [0, 2, 3, 5, 7, 8, 10]  # Minor scale
                elif section_id == "C":
                    scale_degrees = [0, 2, 4, 7, 9]  # Pentatonic scale
                else:
                    scale_degrees = [0, 2, 4, 5, 7, 9, 11]  # Default to major
                
                # Select rhythm pattern
                rhythm_pattern = self.random.choice(rhythm_patterns)
                
                # Generate 8 measures for this section
                for measure in range(8):
                    # Select chord from progression
                    chord_idx = measure % len(progression)
                    chord = progression[chord_idx]
                    
                    # Map chord to scale degrees
                    chord_map = {
                        "I": [0, 4, 7], "ii": [2, 5, 9], "iii": [4, 7, 11], 
                        "IV": [5, 9, 0], "V": [7, 11, 2], "vi": [9, 0, 4], 
                        "vii°": [11, 2, 5],
                        "i": [0, 3, 7], "III": [3, 7, 10], "VI": [8, 0, 3]
                    }
                    chord_tones = chord_map.get(chord, [0, 4, 7])
                    
                    # Generate notes for this measure
                    for beat in range(len(rhythm_pattern)):
                        # Get rhythm value
                        rhythm = rhythm_pattern[beat % len(rhythm_pattern)]
                        
                        # Get dynamic
                        dynamic = dynamic_patterns[beat % len(dynamic_patterns)]
                        velocity = dynamic_map.get(dynamic, 75)
                        
                        # Select note
                        if beat % 4 == 0:  # Emphasize chord tones on strong beats
                            degree = self.random.choice(chord_tones)
                        else:
                            degree = self.random.choice(scale_degrees)
                        
                        # Calculate MIDI note
                        note_offset = note_range[0] + (degree % 12)
                        octave_offset = (degree // 12) + (note_range[1] // 12)
                        note = base_note + note_offset + (octave_offset * 12)
                        
                        # Ensure note is in valid MIDI range (0-127)
                        note = max(0, min(127, note))
                        
                        # Add note_on message
                        track.append(mido.Message('note_on', note=note, velocity=velocity, time=0))
                        
                        # Calculate duration in ticks (assuming quarter note = 480 ticks)
                        ticks_per_beat = 480
                        duration_ticks = int(rhythm * ticks_per_beat)
                        
                        # Add note_off message
                        track.append(mido.Message('note_off', note=note, velocity=0, time=duration_ticks))
                        
                        # Update current time
                        current_time += duration_ticks
            
            # Add end of track message
            track.append(mido.MetaMessage('end_of_track'))
            
            # Save MIDI file
            mid.save(output_file)
            
            return output_file
            
        except Exception as e:
            print(f"Error creating MIDI file: {e}")
            
            # Write placeholder file as fallback
            with open(output_file, 'w') as f:
                f.write(f"MIDI export placeholder for: {composition['title']}\n")
                f.write(f"Key: {composition['key']}\n")
                f.write(f"Time Signature: {composition['time_signature']}\n")
                f.write(f"Tempo: {composition['tempo']}\n")
                f.write(f"Measures: {composition.get('total_measures', 'unknown')}\n")
                f.write(f"Consciousness Level: {composition['consciousness_level']}\n")
                f.write(f"Phi Resonance: {composition['metrics'].get('phi_resonance', 'unknown')}\n")
            
            return output_file
    
    def export_to_musicxml(self, composition: Dict, output_file: str) -> str:
        """
        Export composition to MusicXML file.
        
        Args:
            composition: Composition data structure
            output_file: Output file path
            
        Returns:
            Path to the created MusicXML file
        """
        # This would use a MusicXML library to create an actual MusicXML file
        # For now, just return a placeholder message
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Write placeholder file
        with open(output_file, 'w') as f:
            f.write(f"MusicXML export placeholder for: {composition['title']}\n")
            f.write(f"Key: {composition['key']}\n")
            f.write(f"Time Signature: {composition['time_signature']}\n")
            f.write(f"Tempo: {composition['tempo']}\n")
            f.write(f"Measures: {composition['total_measures']}\n")
            f.write(f"Consciousness Level: {composition['metrics']['consciousness_level']}\n")
            f.write(f"Phi Resonance: {composition['metrics']['phi_resonance']}\n")
        
        return output_file
    
    def get_composition_summary(self, composition: Dict) -> str:
        """
        Get a human-readable summary of the composition.
        
        Args:
            composition: Composition data structure
            
        Returns:
            Summary text
        """
        summary = []
        summary.append(f"Title: {composition['title']}")
        summary.append(f"Style: {composition['style']}")
        summary.append(f"Key: {composition['key']}")
        summary.append(f"Time Signature: {composition['time_signature']}")
        summary.append(f"Tempo: {composition['tempo']} BPM")
        summary.append(f"Form: {' - '.join(composition['form'])}")
        summary.append(f"Total Measures: {composition['total_measures']}")
        summary.append("")
        summary.append("Quantum Phi-Harmonic Metrics:")
        summary.append(f"- Consciousness Level: {composition['metrics']['consciousness_level'].title()}")
        summary.append(f"- Phi Resonance: {composition['metrics']['phi_resonance']:.4f}")
        summary.append(f"- Mean Frequency: {composition['metrics']['mean_frequency']:.2f} Hz")
        summary.append(f"- Phi Alignment: {composition['metrics']['phi_alignment']:.4f}")
        
        return "\n".join(summary)


    def compose_in_composer_style(self, composer: str, theme: str = None, length: int = None) -> Dict:
        """
        Compose a musical piece in the style of a specific classical composer.
        
        Args:
            composer: Name of the composer (e.g., 'beethoven', 'bach', 'chopin', 'mozart')
            theme: Thematic inspiration for the composition
            length: Approximate length in measures
            
        Returns:
            Composition data structure
        """
        composer = composer.lower()
        
        # Check if we have the composer profile
        if composer not in self.composer_profiles:
            # Try to create it
            try:
                profile = self.music_analyzer.create_composer_profile(composer)
                self.composer_profiles[composer] = profile
            except Exception as e:
                print(f"Warning: Could not create profile for {composer}: {e}")
                # Fall back to default composition
                return self.compose(style="classical", theme=theme, length=length)
        
        # Get composer profile
        profile = self.composer_profiles[composer]
        
        # Extract key parameters from profile
        consciousness_level = profile["quantum_signature"]["consciousness_level"]
        key = profile["preferred_keys"][0] if profile["preferred_keys"] else None
        time_signature = profile["preferred_time_signatures"][0] if profile["preferred_time_signatures"] else "4/4"
        tempo = int(profile["preferred_tempos"]["avg"]) if "preferred_tempos" in profile else 120
        
        # Initialize composition
        composition = {
            "title": self._generate_title_from_composer(composer, theme),
            "style": f"{composer}_style",
            "composer_inspiration": composer,
            "key": key,
            "time_signature": time_signature,
            "tempo": tempo,
            "consciousness_level": consciousness_level,
            "form": self._select_form_from_composer(composer, length),
            "sections": [],
            "measures": [],
            "notes": [],
            "metrics": {},
            "generation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Set default length based on composer style
        if length is None:
            if composer == "beethoven":
                length = int(self.phi * 12)  # ~19 measures
            elif composer == "bach":
                length = int(self.phi * 10)  # ~16 measures
            elif composer == "chopin":
                length = int(self.phi * 8)   # ~13 measures
            elif composer == "mozart":
                length = int(self.phi * 14)  # ~23 measures
            else:
                length = int(self.phi * 10)  # ~16 measures
        
        # Generate musical structure
        self._generate_structure_from_composer(composition, composer, length)
        
        # Generate harmonic progression
        self._generate_harmony_from_composer(composition, composer)
        
        # Generate melody
        self._generate_melody_from_composer(composition, composer)
        
        # Generate rhythm
        self._generate_rhythm_from_composer(composition, composer)
        
        # Calculate metrics
        composition["metrics"] = self._calculate_metrics(composition)
        
        # Store current composition
        self.current_composition = composition
        self.composition_history.append({
            "title": composition["title"],
            "composer_inspiration": composer,
            "key": composition["key"],
            "time_signature": composition["time_signature"],
            "consciousness_level": composition["consciousness_level"],
            "metrics": composition["metrics"],
            "timestamp": composition["generation_timestamp"]
        })
        
        return composition
    
    def _generate_title_from_composer(self, composer: str, theme: str = None) -> str:
        """Generate a title based on composer style and theme."""
        composer_title_patterns = {
            "beethoven": ["Sonata", "Symphony", "Concerto", "Moonlight", "Pathetique"],
            "bach": ["Prelude", "Fugue", "Invention", "Concerto", "Suite"],
            "chopin": ["Nocturne", "Etude", "Ballade", "Polonaise", "Mazurka"],
            "mozart": ["Sonata", "Symphony", "Concerto", "Serenade", "Divertimento"]
        }
        
        # Get title patterns for composer
        patterns = composer_title_patterns.get(composer, ["Composition", "Piece", "Opus"])
        
        # Select base title
        base_title = self.random.choice(patterns)
        
        # Add theme if provided
        if theme:
            # Clean theme
            theme = theme.title()
            return f"{base_title} {theme}"
        
        # Add quantum/phi terms
        quantum_terms = ["Quantum", "Phi", "Golden", "Harmonic", "Resonant", "Cosmic"]
        quantum_term = self.random.choice(quantum_terms)
        
        return f"{base_title} {quantum_term}"
    
    def _select_form_from_composer(self, composer: str, length: int) -> List[str]:
        """Select an appropriate musical form based on composer style."""
        composer_forms = {
            "beethoven": ["sonata", "ternary", "rondo"],
            "bach": ["binary", "fugue", "ritornello"],
            "chopin": ["ternary", "rondo", "nocturne"],
            "mozart": ["sonata", "rondo", "theme_and_variations"]
        }
        
        # Get forms for composer
        forms = composer_forms.get(composer, ["simple", "binary", "ternary"])
        
        # Select form
        form_type = self.random.choice(forms)
        
        # Map to actual form structure
        form_structures = {
            "simple": ["A", "A", "B", "A"],
            "binary": ["A", "A", "B", "B"],
            "ternary": ["A", "B", "A"],
            "rondo": ["A", "B", "A", "C", "A"],
            "sonata": ["A", "A", "B", "B", "C", "A", "B"],
            "fugue": ["A", "A'", "A''", "A'''", "A"],
            "ritornello": ["A", "B", "A", "C", "A", "D", "A"],
            "nocturne": ["A", "B", "A", "Coda"],
            "theme_and_variations": ["A", "A'", "A''", "A'''", "A''''", "A"]
        }
        
        return form_structures.get(form_type, ["A", "B", "A"])
    
    def _generate_structure_from_composer(self, composition: Dict, composer: str, length: int):
        """Generate the overall structure based on composer style."""
        # Use the regular structure generation but with composer-specific adjustments
        self._generate_structure(composition, length)
        
        # Apply composer-specific adjustments
        if composer == "beethoven":
            # Beethoven often has dramatic contrasts
            for section in composition.get("sections", []):
                if "id" in section and section["id"] == "B":
                    # Check if intensity exists before multiplying
                    if "intensity" in section:
                        section["intensity"] = section["intensity"] * 1.5
                    else:
                        section["intensity"] = 0.85  # Default high intensity
                    
        elif composer == "bach":
            # Bach often has complex counterpoint
            composition["counterpoint_complexity"] = 0.85
            
        elif composer == "chopin":
            # Chopin often has rubato and expressive dynamics
            composition["rubato"] = 0.75
            composition["dynamic_range"] = 0.8
            
        elif composer == "mozart":
            # Mozart often has clear, balanced phrases
            composition["phrase_symmetry"] = 0.9
    
    def _generate_harmony_from_composer(self, composition: Dict, composer: str):
        """Generate harmonic progression based on composer style."""
        # Use the regular harmony generation but with composer-specific adjustments
        self._generate_harmony(composition)
        
        # Apply composer-specific harmonic patterns
        composer_progressions = {
            "beethoven": [
                ["I", "IV", "V", "I"],
                ["I", "V", "vi", "IV", "I"],
                ["I", "V7", "I", "V7", "vi", "IV", "V7", "I"]
            ],
            "bach": [
                ["I", "IV", "V", "I"],
                ["I", "V", "vi", "iii", "IV", "I", "IV", "V", "I"],
                ["I", "IV", "vii°", "iii", "vi", "ii", "V", "I"]
            ],
            "chopin": [
                ["I", "V7", "vi", "IV", "ii", "V7", "I"],
                ["i", "V", "VI", "III", "iv", "V", "i"],
                ["I", "V7", "I", "vi", "IV", "V7", "I"]
            ],
            "mozart": [
                ["I", "V", "I", "IV", "I", "V", "I"],
                ["I", "IV", "I", "V", "I"],
                ["I", "V7", "I", "vi", "ii", "V7", "I"]
            ]
        }
        
        # Get progressions for composer
        progressions = composer_progressions.get(composer, [["I", "IV", "V", "I"]])
        
        # Select progression
        progression = self.random.choice(progressions)
        
        # Apply to composition
        composition["harmonic_progression"] = progression
    
    def _generate_melody_from_composer(self, composition: Dict, composer: str):
        """Generate melody based on composer style."""
        # Use the regular melody generation but with composer-specific adjustments
        self._generate_melody(composition)
        
        # Apply composer-specific melodic patterns
        if composer == "beethoven":
            # Beethoven often has bold, memorable themes
            composition["melodic_range"] = (7, 12)  # Wider range
            composition["melodic_intervals"] = [2, 3, 4, 5]  # More leaps
            
        elif composer == "bach":
            # Bach often has stepwise motion with occasional leaps
            composition["melodic_range"] = (5, 9)
            composition["melodic_intervals"] = [1, 2, 3, 5]
            
        elif composer == "chopin":
            # Chopin often has ornate, expressive melodies
            composition["melodic_range"] = (8, 14)
            composition["melodic_intervals"] = [1, 2, 3, 4]
            composition["ornamentation"] = 0.8
            
        elif composer == "mozart":
            # Mozart often has clear, balanced, singable melodies
            composition["melodic_range"] = (6, 10)
            composition["melodic_intervals"] = [1, 2, 3]
            composition["phrase_symmetry"] = 0.9
    
    def _generate_rhythm_from_composer(self, composition: Dict, composer: str):
        """Generate rhythm based on composer style."""
        # Use the regular rhythm generation but with composer-specific adjustments
        self._generate_rhythm(composition)
        
        # Apply composer-specific rhythmic patterns
        composer_rhythms = {
            "beethoven": {
                "patterns": [
                    [1, 1, 1, 1],
                    [2, 1, 1],
                    [0.5, 0.5, 0.5, 0.5, 1, 1]
                ],
                "dynamics": ["f", "p", "ff", "mf", "p"]
            },
            "bach": {
                "patterns": [
                    [1, 1, 1, 1],
                    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                    [1.5, 0.5, 1, 1]
                ],
                "dynamics": ["mf", "f", "mf", "f", "mf"]
            },
            "chopin": {
                "patterns": [
                    [1, 1, 1, 1],
                    [3, 1],
                    [0.75, 0.25, 1, 1, 1]
                ],
                "dynamics": ["p", "mp", "mf", "mp", "p"]
            },
            "mozart": {
                "patterns": [
                    [1, 1, 1, 1],
                    [0.5, 0.5, 1, 1, 1],
                    [1, 0.5, 0.5, 1, 1]
                ],
                "dynamics": ["mf", "f", "mf", "p", "mf"]
            }
        }
        
        # Get rhythms for composer
        rhythms = composer_rhythms.get(composer, {
            "patterns": [[1, 1, 1, 1]],
            "dynamics": ["mf", "mf", "mf"]
        })
        
        # Apply to composition
        composition["rhythm_patterns"] = rhythms["patterns"]
        composition["dynamic_patterns"] = rhythms["dynamics"]


def main():
    """Main function to demonstrate music composition."""
    # Create composer
    composer = QuantumPhiMusicComposer()
    
    # Create output directories
    midi_dir = "midi_output"
    if not os.path.exists(midi_dir):
        os.makedirs(midi_dir)
    
    # Compose a piece in phi-harmonic style
    print("Composing a phi-harmonic musical piece...")
    composition = composer.compose(style="phi_harmonic", consciousness_level="cosmic")
    
    # Print summary
    print("\nComposition Summary:")
    print("=" * 50)
    print(composer.get_composition_summary(composition))
    
    # Export to MIDI file
    midi_file = os.path.join(midi_dir, "quantum_phi_composition.mid")
    composer.export_to_midi(composition, midi_file)
    print(f"\nExported MIDI file to: {midi_file}")
    
    # Compose pieces in classical composer styles
    composers = ["beethoven", "bach", "chopin", "mozart"]
    
    for classical_composer in composers:
        print(f"\nComposing a piece in {classical_composer.title()}'s style...")
        composition = composer.compose_in_composer_style(classical_composer)
        
        # Print summary
        print("\nComposition Summary:")
        print("=" * 50)
        print(composer.get_composition_summary(composition))
        
        # Export to MIDI file
        midi_file = os.path.join(midi_dir, f"{classical_composer}_phi_composition.mid")
        composer.export_to_midi(composition, midi_file)
        print(f"\nExported MIDI file to: {midi_file}")
    
    # Compose a piece that combines Mozart (highest literary similarity) with Austen
    print("\nComposing a Mozart-Austen fusion piece...")
    
    # Start with Mozart style
    composition = composer.compose_in_composer_style("mozart", theme="Austen Fusion")
    
    # Adjust consciousness to match Austen's signature (from memories)
    composition["consciousness_level"] = "cosmic"
    composition["metrics"]["mean_frequency"] = 525.18  # Austen's frequency
    
    # Export to MIDI file
    midi_file = os.path.join(midi_dir, "mozart_austen_fusion.mid")
    composer.export_to_midi(composition, midi_file)
    
    # Print summary
    print("\nMozart-Austen Fusion Composition:")
    print("=" * 50)
    print(composer.get_composition_summary(composition))
    print(f"\nExported MIDI file to: {midi_file}")
    
    print("\nAll compositions have been generated and exported to MIDI files.")
    print(f"MIDI files can be found in the '{midi_dir}' directory.")
    
if __name__ == "__main__":
    main()
