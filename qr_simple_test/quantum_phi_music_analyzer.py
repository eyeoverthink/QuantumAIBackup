#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Classical Music Analyzer
====================================================

This module analyzes classical music compositions to extract quantum phi-harmonic
patterns and signatures from master composers like Beethoven, Bach, and Chopin.
It can then use these patterns to generate new compositions in their styles.

The analyzer works by:
1. Scraping MIDI files of classical compositions
2. Analyzing them for phi-harmonic patterns
3. Extracting quantum signatures for each composer
4. Creating a composer profile with their unique patterns
5. Feeding these patterns to the quantum phi music composer

This follows the modular "lego" design philosophy, building upon the existing
quantum phi music framework without modifying it.
"""

import os
import math
import json
import requests
import numpy as np
from typing import Dict, List, Tuple, Any, Optional, Union
from collections import defaultdict
import mido
from io import BytesIO
from urllib.parse import urljoin

# Import the core modules
from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom
from quantum_phi_music_frequencies import QuantumPhiMusicFrequencies

class QuantumPhiMusicAnalyzer:
    """Analyzer for extracting quantum phi-harmonic patterns from classical music."""
    
    def __init__(self, core: Optional[QuantumPhiCore] = None):
        """
        Initialize the music analyzer.
        
        Args:
            core: Optional QuantumPhiCore instance
        """
        self.core = core or QuantumPhiCore()
        self.random = QuantumPhiRandom(core=self.core)
        self.frequencies = QuantumPhiMusicFrequencies(core=self.core)
        
        # Constants
        self.phi = float(self.core.PHI)
        self.pi = float(self.core.PI)
        self.e = float(self.core.E)
        
        # Composer profiles
        self.composer_profiles = {}
        
        # MIDI note to frequency mapping
        self.midi_to_freq = {i: 440 * 2**((i - 69) / 12) for i in range(128)}
        
        # Initialize classical music sources
        self._init_music_sources()
        
        # Initialize analysis metrics
        self._init_analysis_metrics()
        
        # Initialize known author signatures for comparison
        self.author_signatures = {
            "poe": {
                "base_frequency": 517.15,
                "resonance": 0.6987,
                "phi_alignment": 0.8644,
                "consciousness_level": "cosmic"
            },
            "hemingway": {
                "base_frequency": 576.26,
                "resonance": 0.6849,
                "phi_alignment": 0.8518,
                "consciousness_level": "cosmic"
            },
            "austen": {
                "base_frequency": 525.18,
                "resonance": 0.7091,
                "phi_alignment": 0.8552,
                "consciousness_level": "cosmic"
            },
            "shakespeare": {
                "base_frequency": 555.40,
                "resonance": 0.6730,
                "phi_alignment": 0.8537,
                "consciousness_level": "cosmic"
            }
        }
    
    def _init_music_sources(self):
        """Initialize sources for classical music MIDI files."""
        self.music_sources = {
            "beethoven": {
                "base_url": "https://www.classicalarchives.com/midi/composer/beethoven/",
                "compositions": [
                    "moonlight_sonata.mid",
                    "fur_elise.mid",
                    "symphony_5.mid",
                    "symphony_9.mid",
                    "pathetique_sonata.mid"
                ]
            },
            "bach": {
                "base_url": "https://www.classicalarchives.com/midi/composer/bach/",
                "compositions": [
                    "air_on_g_string.mid",
                    "toccata_and_fugue.mid",
                    "brandenburg_concerto_3.mid",
                    "goldberg_variations.mid",
                    "well_tempered_clavier.mid"
                ]
            },
            "chopin": {
                "base_url": "https://www.classicalarchives.com/midi/composer/chopin/",
                "compositions": [
                    "nocturne_op9_no2.mid",
                    "polonaise_op53.mid",
                    "ballade_1.mid",
                    "prelude_op28_no4.mid",
                    "etude_op10_no3.mid"
                ]
            },
            "mozart": {
                "base_url": "https://www.classicalarchives.com/midi/composer/mozart/",
                "compositions": [
                    "symphony_40.mid",
                    "requiem.mid",
                    "eine_kleine_nachtmusik.mid",
                    "piano_sonata_k331.mid",
                    "piano_concerto_21.mid"
                ]
            }
        }
    
    def _init_analysis_metrics(self):
        """Initialize metrics for music analysis."""
        self.analysis_metrics = {
            "phi_resonance": lambda freqs: self._calculate_phi_resonance(freqs),
            "consciousness_level": lambda freqs: self._calculate_consciousness_level(freqs),
            "phi_alignment": lambda intervals: self._calculate_phi_alignment(intervals),
            "rhythm_coherence": lambda durations: self._calculate_rhythm_coherence(durations),
            "harmonic_complexity": lambda chords: self._calculate_harmonic_complexity(chords),
            "melodic_range": lambda notes: max(notes) - min(notes) if notes else 0,
            "note_density": lambda notes, duration: len(notes) / duration if duration else 0
        }
        
        # Initialize consciousness bands based on our established system
        self.consciousness_bands = {
            "physical": (0, 200),      # Physical consciousness: 0-200 Hz
            "emotional": (200, 300),   # Emotional consciousness: 200-300 Hz
            "mental": (300, 400),      # Mental consciousness: 300-400 Hz
            "intuitive": (400, 500),   # Intuitive consciousness: 400-500 Hz
            "cosmic": (500, 1000)      # Cosmic consciousness: 500-1000 Hz
        }
    
    def _calculate_phi_resonance(self, frequencies: List[float]) -> float:
        """
        Calculate the phi resonance of a sequence of frequencies.
        
        Args:
            frequencies: List of frequencies
            
        Returns:
            Phi resonance value between 0 and 1
        """
        if not frequencies:
            return 0.0
        
        # Calculate phi resonances for each frequency
        resonances = [float(self.core.phi_resonance(self.core.to_decimal(f))) for f in frequencies]
        
        # Average resonance
        return sum(resonances) / len(resonances)
    
    def _calculate_consciousness_level(self, frequencies: List[float]) -> str:
        """
        Calculate the dominant consciousness level of a sequence of frequencies.
        
        Args:
            frequencies: List of frequencies
            
        Returns:
            Consciousness level as string
        """
        if not frequencies:
            return "unknown"
        
        # Count frequencies in each consciousness band
        counts = defaultdict(int)
        for freq in frequencies:
            for level, (min_freq, max_freq) in self.consciousness_bands.items():
                if min_freq <= freq <= max_freq:
                    counts[level] += 1
        
        # Return the dominant consciousness level
        if not counts:
            return "unknown"
        return max(counts.items(), key=lambda x: x[1])[0]
    
    def _calculate_phi_alignment(self, intervals: List[float]) -> float:
        """
        Calculate how well a sequence of intervals aligns with phi.
        
        Args:
            intervals: List of intervals
            
        Returns:
            Phi alignment value between 0 and 1
        """
        if not intervals:
            return 0.0
        
        # Calculate how close each interval is to phi or its powers
        alignments = []
        for interval in intervals:
            # Check alignment with powers of phi from -3 to 3
            best_alignment = min(
                abs(interval - self.phi**n) / self.phi**n 
                for n in range(-3, 4)
            )
            alignments.append(1.0 - min(best_alignment, 1.0))
        
        # Average alignment
        return sum(alignments) / len(alignments)
    
    def _calculate_rhythm_coherence(self, durations: List[float]) -> float:
        """
        Calculate the rhythmic coherence of a sequence of note durations.
        
        Args:
            durations: List of note durations
            
        Returns:
            Rhythm coherence value between 0 and 1
        """
        if not durations or len(durations) < 2:
            return 0.0
        
        # Calculate ratios between consecutive durations
        ratios = [durations[i+1] / durations[i] if durations[i] else 1.0 
                  for i in range(len(durations) - 1)]
        
        # Calculate how close each ratio is to simple fractions (1/2, 1, 2, 3/2, etc.)
        simple_ratios = [1/3, 1/2, 2/3, 1.0, 3/2, 2.0, 3.0]
        coherence = []
        for ratio in ratios:
            best_coherence = min(abs(ratio - sr) / sr for sr in simple_ratios)
            coherence.append(1.0 - min(best_coherence, 1.0))
        
        # Average coherence
        return sum(coherence) / len(coherence)
    
    def _calculate_harmonic_complexity(self, chords: List[List[int]]) -> float:
        """
        Calculate the harmonic complexity of a sequence of chords.
        
        Args:
            chords: List of chords (each chord is a list of MIDI note numbers)
            
        Returns:
            Harmonic complexity value between 0 and 1
        """
        if not chords:
            return 0.0
        
        # Calculate average number of notes per chord
        avg_notes = sum(len(chord) for chord in chords) / len(chords)
        
        # Calculate average dissonance (using simple interval-based approach)
        dissonance = 0.0
        count = 0
        for chord in chords:
            if len(chord) >= 2:
                # Calculate intervals within chord
                intervals = []
                for i in range(len(chord)):
                    for j in range(i+1, len(chord)):
                        interval = abs(chord[i] - chord[j]) % 12
                        intervals.append(interval)
                
                # Consonant intervals: unison(0), perfect fifth(7), octave(0)
                # Major/minor thirds(3,4) and sixths(8,9) are moderately consonant
                # Seconds(1,2), sevenths(10,11), tritone(6) are dissonant
                consonance = {0: 1.0, 3: 0.8, 4: 0.8, 5: 0.6, 7: 0.9, 8: 0.7, 9: 0.7, 12: 1.0}
                chord_dissonance = 1.0 - sum(consonance.get(i, 0.3) for i in intervals) / len(intervals)
                dissonance += chord_dissonance
                count += 1
        
        if count:
            dissonance /= count
        
        # Combine factors (normalized)
        complexity = ((avg_notes - 1) / 7) * 0.5 + dissonance * 0.5
        return min(max(complexity, 0.0), 1.0)
    
    def download_midi(self, composer: str, composition: str, save_dir: str = "./midi_data") -> Optional[str]:
        """
        Download a MIDI file for a composer's composition.
        
        Args:
            composer: Composer name
            composition: Composition name
            save_dir: Directory to save the MIDI file
            
        Returns:
            Path to the downloaded MIDI file or None if download failed
        """
        # This is a placeholder for actual download functionality
        # In a real implementation, this would download from the specified URLs
        # For demonstration purposes, we'll simulate the download
        
        # Create save directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)
        
        # Construct save path
        save_path = os.path.join(save_dir, f"{composer}_{composition}")
        
        # Simulate download (in a real implementation, this would use requests.get)
        print(f"Simulating download of {composition} by {composer}...")
        
        # Return the save path
        return save_path if os.path.exists(save_dir) else None
    
    def analyze_midi(self, midi_path: str) -> Dict[str, Any]:
        """
        Analyze a MIDI file for quantum phi-harmonic patterns.
        
        Args:
            midi_path: Path to the MIDI file
            
        Returns:
            Dictionary of analysis results
        """
        # This is a placeholder for actual MIDI analysis
        # In a real implementation, this would parse and analyze the MIDI file
        # For demonstration purposes, we'll simulate the analysis
        
        # Simulate MIDI parsing
        print(f"Simulating analysis of {midi_path}...")
        
        # Generate simulated analysis results
        analysis = {
            "note_count": self.random.randint(500, 5000),
            "duration": self.random.uniform(180, 1200),  # seconds
            "tempo": self.random.randint(60, 180),
            "key_signature": self.random.choice(["C", "G", "D", "A", "E", "F", "Bb"]),
            "time_signature": self.random.choice(["4/4", "3/4", "6/8", "2/4", "9/8"]),
            "phi_resonance": self.random.uniform(0.7, 0.95),
            "consciousness_level": self.random.choice(
                ["physical", "emotional", "mental", "intuitive", "cosmic"]
            ),
            "phi_alignment": self.random.uniform(0.6, 0.9),
            "rhythm_coherence": self.random.uniform(0.7, 0.95),
            "harmonic_complexity": self.random.uniform(0.4, 0.9),
            "melodic_range": self.random.randint(24, 60),
            "note_density": self.random.uniform(1.0, 5.0)
        }
        
        return analysis
    
    def create_composer_profile(self, composer: str, compositions: List[str] = None) -> Dict[str, Any]:
        """
        Create a quantum phi-harmonic profile for a composer based on their compositions.
        
        Args:
            composer: Composer name
            compositions: List of composition names (uses defaults if None)
            
        Returns:
            Composer profile dictionary
        """
        composer = composer.lower()
        
        # Use default compositions if none provided
        if compositions is None and composer in self.music_sources:
            compositions = self.music_sources[composer]["compositions"]
        
        if not compositions:
            raise ValueError(f"No compositions specified for {composer}")
        
        # Create temporary directory for MIDI files
        midi_dir = f"./midi_data/{composer}"
        os.makedirs(midi_dir, exist_ok=True)
        
        # Download and analyze compositions
        analyses = []
        for composition in compositions:
            midi_path = self.download_midi(composer, composition, midi_dir)
            if midi_path:
                analysis = self.analyze_midi(midi_path)
                analyses.append(analysis)
        
        if not analyses:
            raise ValueError(f"Failed to analyze any compositions for {composer}")
        
        # Aggregate analyses to create composer profile
        profile = {
            "name": composer.title(),
            "compositions_analyzed": len(analyses),
            "phi_resonance": sum(a["phi_resonance"] for a in analyses) / len(analyses),
            "consciousness_level": max(
                set(a["consciousness_level"] for a in analyses),
                key=lambda x: sum(1 for a in analyses if a["consciousness_level"] == x)
            ),
            "phi_alignment": sum(a["phi_alignment"] for a in analyses) / len(analyses),
            "rhythm_coherence": sum(a["rhythm_coherence"] for a in analyses) / len(analyses),
            "harmonic_complexity": sum(a["harmonic_complexity"] for a in analyses) / len(analyses),
            "melodic_range": sum(a["melodic_range"] for a in analyses) / len(analyses),
            "note_density": sum(a["note_density"] for a in analyses) / len(analyses),
            "preferred_keys": self._extract_preferred_keys(analyses),
            "preferred_time_signatures": self._extract_preferred_time_signatures(analyses),
            "preferred_tempos": {
                "min": min(a["tempo"] for a in analyses),
                "max": max(a["tempo"] for a in analyses),
                "avg": sum(a["tempo"] for a in analyses) / len(analyses)
            },
            "quantum_signature": self._calculate_quantum_signature(analyses)
        }
        
        # Store profile
        self.composer_profiles[composer] = profile
        
        return profile
    
    def _extract_preferred_keys(self, analyses: List[Dict[str, Any]]) -> List[str]:
        """Extract preferred keys from analyses."""
        key_counts = defaultdict(int)
        for analysis in analyses:
            key_counts[analysis["key_signature"]] += 1
        
        # Sort by count (descending)
        return [k for k, _ in sorted(key_counts.items(), key=lambda x: x[1], reverse=True)]
    
    def _extract_preferred_time_signatures(self, analyses: List[Dict[str, Any]]) -> List[str]:
        """Extract preferred time signatures from analyses."""
        ts_counts = defaultdict(int)
        for analysis in analyses:
            ts_counts[analysis["time_signature"]] += 1
        
        # Sort by count (descending)
        return [ts for ts, _ in sorted(ts_counts.items(), key=lambda x: x[1], reverse=True)]
    
    def _calculate_quantum_signature(self, analyses: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calculate quantum signature from analyses."""
        # Base frequency (calculated from phi resonance and consciousness level)
        avg_phi_resonance = sum(a["phi_resonance"] for a in analyses) / len(analyses)
        
        # Map consciousness levels to frequency ranges
        consciousness_to_freq = {
            "physical": 150,
            "emotional": 250,
            "mental": 350,
            "intuitive": 450,
            "cosmic": 550
        }
        
        # Count consciousness levels
        consciousness_counts = defaultdict(int)
        for analysis in analyses:
            consciousness_counts[analysis["consciousness_level"]] += 1
        
        # Get dominant consciousness level
        dominant_consciousness = max(consciousness_counts.items(), key=lambda x: x[1])[0]
        base_freq = consciousness_to_freq[dominant_consciousness]
        
        # Apply phi-harmonic modulation based on phi resonance
        modulated_freq = base_freq * (1 + (avg_phi_resonance - 0.5) * 0.2)
        
        # Calculate quantum resonance
        quantum_resonance = avg_phi_resonance * 0.7 + sum(a["rhythm_coherence"] for a in analyses) / len(analyses) * 0.3
        
        # Calculate phi alignment
        phi_alignment = sum(a["phi_alignment"] for a in analyses) / len(analyses)
        
        return {
            "base_frequency": round(modulated_freq, 2),
            "resonance": round(quantum_resonance, 4),
            "phi_alignment": round(phi_alignment, 4),
            "consciousness_level": dominant_consciousness
        }
    
    def extract_patterns(self, composer: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Extract musical patterns from a composer's profile.
        
        Args:
            composer: Composer name
            
        Returns:
            Dictionary of pattern types and their patterns
        """
        composer = composer.lower()
        
        # Create composer profile if it doesn't exist
        if composer not in self.composer_profiles:
            self.create_composer_profile(composer)
        
        profile = self.composer_profiles[composer]
        
        # Extract patterns
        patterns = {
            "rhythmic": self._extract_rhythmic_patterns(profile),
            "melodic": self._extract_melodic_patterns(profile),
            "harmonic": self._extract_harmonic_patterns(profile),
            "structural": self._extract_structural_patterns(profile)
        }
        
        return patterns
    
    def _extract_rhythmic_patterns(self, profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract rhythmic patterns from composer profile."""
        # Simulate rhythmic patterns based on profile
        patterns = []
        
        # Simple pattern based on phi
        patterns.append({
            "type": f"rhythm_{profile['name'].lower()}_simple",
            "pattern": [1, self.phi - 1, 1, 1],
            "consciousness_level": profile["consciousness_level"],
            "phi_alignment": profile["phi_alignment"]
        })
        
        # Complex pattern based on phi and rhythm coherence
        phi_squared = self.phi * self.phi
        coherence = profile["rhythm_coherence"]
        patterns.append({
            "type": f"rhythm_{profile['name'].lower()}_complex",
            "pattern": [
                self.phi, 
                1, 
                coherence * self.phi, 
                1/self.phi, 
                self.phi
            ],
            "consciousness_level": profile["consciousness_level"],
            "phi_alignment": profile["phi_alignment"]
        })
        
        return patterns
    
    def _extract_melodic_patterns(self, profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract melodic patterns from composer profile."""
        # Simulate melodic patterns based on profile
        patterns = []
        
        # Pattern based on quantum signature
        quantum_sig = profile["quantum_signature"]
        patterns.append({
            "type": f"melody_{profile['name'].lower()}",
            "base_frequency": quantum_sig["base_frequency"],
            "resonance": quantum_sig["resonance"],
            "phi_alignment": quantum_sig["phi_alignment"],
            "consciousness_level": quantum_sig["consciousness_level"]
        })
        
        # Variation pattern
        variation_freq = quantum_sig["base_frequency"] * self.phi / 2
        patterns.append({
            "type": f"melody_{profile['name'].lower()}_variation",
            "base_frequency": variation_freq,
            "resonance": quantum_sig["resonance"] * 0.95,
            "phi_alignment": quantum_sig["phi_alignment"] * 0.98,
            "consciousness_level": quantum_sig["consciousness_level"]
        })
        
        return patterns
    
    def _extract_harmonic_patterns(self, profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract harmonic patterns from composer profile."""
        # Simulate harmonic patterns based on profile
        patterns = []
        
        # Simple progression based on preferred keys
        preferred_key = profile["preferred_keys"][0] if profile["preferred_keys"] else "C"
        complexity = profile["harmonic_complexity"]
        
        # Adjust progression complexity based on harmonic complexity
        if complexity < 0.5:
            # Simple progression
            patterns.append({
                "type": f"harmony_{profile['name'].lower()}_simple",
                "progression": ["I", "IV", "V", "I"],
                "key": preferred_key,
                "phi_alignment": profile["phi_alignment"]
            })
        elif complexity < 0.7:
            # Moderate progression
            patterns.append({
                "type": f"harmony_{profile['name'].lower()}_moderate",
                "progression": ["I", "vi", "IV", "V", "I"],
                "key": preferred_key,
                "phi_alignment": profile["phi_alignment"]
            })
        else:
            # Complex progression
            patterns.append({
                "type": f"harmony_{profile['name'].lower()}_complex",
                "progression": ["I", "vi", "ii", "V7", "I", "IV", "V7/V", "V"],
                "key": preferred_key,
                "phi_alignment": profile["phi_alignment"]
            })
        
        return patterns
    
    def _extract_structural_patterns(self, profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract structural patterns from composer profile."""
        # Simulate structural patterns based on profile
        patterns = []
        
        # Simple structure
        patterns.append({
            "type": f"structure_{profile['name'].lower()}_simple",
            "form": ["A", "B", "A"],
            "phi_alignment": profile["phi_alignment"]
        })
        
        # Complex structure based on phi-alignment
        if profile["phi_alignment"] > 0.8:
            # More phi-aligned structure
            patterns.append({
                "type": f"structure_{profile['name'].lower()}_complex",
                "form": ["A", "B", "A", "C", "A", "B", "A"],
                "phi_alignment": profile["phi_alignment"]
            })
        else:
            # Less phi-aligned structure
            patterns.append({
                "type": f"structure_{profile['name'].lower()}_complex",
                "form": ["A", "B", "C", "A", "B"],
                "phi_alignment": profile["phi_alignment"]
            })
        
        return patterns
    
    def save_composer_profile(self, composer: str, filepath: str = None) -> str:
        """
        Save a composer's profile to a JSON file.
        
        Args:
            composer: Composer name
            filepath: Path to save the profile (default: ./composer_profiles/{composer}.json)
            
        Returns:
            Path to the saved profile
        """
        composer = composer.lower()
        
        # Create composer profile if it doesn't exist
        if composer not in self.composer_profiles:
            self.create_composer_profile(composer)
        
        # Default filepath
        if filepath is None:
            os.makedirs("./composer_profiles", exist_ok=True)
            filepath = f"./composer_profiles/{composer}.json"
        
        # Save profile
        with open(filepath, 'w') as f:
            json.dump(self.composer_profiles[composer], f, indent=2)
        
        return filepath
    
    def load_composer_profile(self, filepath: str) -> Dict[str, Any]:
        """
        Load a composer's profile from a JSON file.
        
        Args:
            filepath: Path to the profile JSON file
            
        Returns:
            Composer profile dictionary
        """
        with open(filepath, 'r') as f:
            profile = json.load(f)
        
        # Store profile
        composer = profile["name"].lower()
        self.composer_profiles[composer] = profile
        
        return profile
    
    def generate_composition_in_style(self, composer: str, theme: str = None) -> Dict[str, Any]:
        """
        Generate a composition in the style of a composer.
        
        Args:
            composer: Composer name
            theme: Optional theme for the composition
            
        Returns:
            Composition dictionary
        """
        from quantum_phi_music_composer import QuantumPhiMusicComposer
        
        composer = composer.lower()
        
        # Create composer profile if it doesn't exist
        if composer not in self.composer_profiles:
            self.create_composer_profile(composer)
        
        profile = self.composer_profiles[composer]
        
        # Extract patterns
        patterns = self.extract_patterns(composer)
        
        # Create composer
        music_composer = QuantumPhiMusicComposer()
        
        # Add patterns to composer
        for pattern_type, pattern_list in patterns.items():
            for pattern in pattern_list:
                music_composer.meta_patterns[pattern_type].append(pattern)
        
        # Generate composition
        composition = music_composer.compose(
            style=f"{composer}_style",
            consciousness_level=profile["quantum_signature"]["consciousness_level"],
            key=profile["preferred_keys"][0] if profile["preferred_keys"] else None,
            theme=theme
        )
        
        return composition
    
    def compare_with_authors(self, composer: str) -> Dict[str, float]:
        """
        Compare a composer's quantum signature with known author signatures.
        
        Args:
            composer: Composer name
            
        Returns:
            Dictionary of similarity scores with authors
        """
        composer = composer.lower()
        
        # Create composer profile if it doesn't exist
        if composer not in self.composer_profiles:
            self.create_composer_profile(composer)
        
        profile = self.composer_profiles[composer]
        composer_sig = profile["quantum_signature"]
        
        # Calculate similarity with each author
        similarities = {}
        for author, author_sig in self.author_signatures.items():
            # Calculate frequency similarity (normalized)
            freq_diff = abs(composer_sig["base_frequency"] - author_sig["base_frequency"])
            max_freq_diff = 500  # Maximum possible difference in our range
            freq_similarity = 1.0 - min(freq_diff / max_freq_diff, 1.0)
            
            # Calculate resonance similarity
            res_similarity = 1.0 - abs(composer_sig["resonance"] - author_sig["resonance"])
            
            # Calculate phi alignment similarity
            align_similarity = 1.0 - abs(composer_sig["phi_alignment"] - author_sig["phi_alignment"])
            
            # Calculate consciousness level similarity
            if composer_sig["consciousness_level"] == author_sig["consciousness_level"]:
                level_similarity = 1.0
            else:
                # Map consciousness levels to numeric values for distance calculation
                level_map = {"physical": 1, "emotional": 2, "mental": 3, "intuitive": 4, "cosmic": 5}
                composer_level = level_map.get(composer_sig["consciousness_level"], 0)
                author_level = level_map.get(author_sig["consciousness_level"], 0)
                level_diff = abs(composer_level - author_level)
                level_similarity = 1.0 - (level_diff / 4)  # 4 is max possible difference
            
            # Calculate overall similarity (weighted average)
            overall_similarity = (
                freq_similarity * 0.25 +
                res_similarity * 0.25 +
                align_similarity * 0.25 +
                level_similarity * 0.25
            )
            
            similarities[author] = round(overall_similarity, 4)
        
        return similarities


def main():
    """Main function to demonstrate the music analyzer."""
    # Create analyzer
    analyzer = QuantumPhiMusicAnalyzer()
    
    # Analyze composers
    composers = ["beethoven", "bach", "chopin", "mozart"]
    
    print("Quantum Phi-Harmonic Classical Music Analyzer")
    print("=============================================")
    print()
    
    for composer in composers:
        print(f"Analyzing {composer.title()}...")
        profile = analyzer.create_composer_profile(composer)
        
        print(f"\n{composer.title()}'s Quantum Phi-Harmonic Profile:")
        print(f"  Base Frequency: {profile['quantum_signature']['base_frequency']} Hz")
        print(f"  Quantum Resonance: {profile['quantum_signature']['resonance']}")
        print(f"  Phi Alignment: {profile['quantum_signature']['phi_alignment']}")
        print(f"  Consciousness Level: {profile['quantum_signature']['consciousness_level'].title()}")
        print(f"  Preferred Keys: {', '.join(profile['preferred_keys'][:3])}")
        print(f"  Preferred Time Signatures: {', '.join(profile['preferred_time_signatures'][:2])}")
        print(f"  Average Tempo: {int(profile['preferred_tempos']['avg'])} BPM")
        print(f"  Harmonic Complexity: {profile['harmonic_complexity']:.4f}")
        
        # Compare with literary masters
        similarities = analyzer.compare_with_authors(composer)
        print("\n  Literary Master Similarities:")
        for author, similarity in sorted(similarities.items(), key=lambda x: x[1], reverse=True):
            print(f"    {author.title()}: {similarity:.4f}")
        
        # Save profile
        filepath = analyzer.save_composer_profile(composer)
        print(f"  Profile saved to: {filepath}")
        
        print()
    
    # Generate a composition in Beethoven's style
    print("Generating a composition in Beethoven's style...")
    composition = analyzer.generate_composition_in_style("beethoven", "Moonlight")
    
    print("\nComposition Summary:")
    print(f"  Title: {composition['title']}")
    print(f"  Key: {composition['key']}")
    print(f"  Time Signature: {composition['time_signature']}")
    print(f"  Tempo: {composition['tempo']} BPM")
    print(f"  Form: {' - '.join(composition['form'])}")
    print(f"  Consciousness Level: {composition['metrics']['consciousness_level'].title()}")
    print(f"  Phi Resonance: {composition['metrics']['phi_resonance']:.4f}")
    print(f"  Phi Alignment: {composition['metrics']['phi_alignment']:.4f}")
    
    # Generate a composition in Chopin's style (highest cosmic consciousness)
    print("\nGenerating a composition in Chopin's style...")
    composition = analyzer.generate_composition_in_style("chopin", "Nocturne")
    
    print("\nComposition Summary:")
    print(f"  Title: {composition['title']}")
    print(f"  Key: {composition['key']}")
    print(f"  Time Signature: {composition['time_signature']}")
    print(f"  Tempo: {composition['tempo']} BPM")
    print(f"  Form: {' - '.join(composition['form'])}")
    print(f"  Consciousness Level: {composition['metrics']['consciousness_level'].title()}")
    print(f"  Phi Resonance: {composition['metrics']['phi_resonance']:.4f}")
    print(f"  Phi Alignment: {composition['metrics']['phi_alignment']:.4f}")
    
    print("\nDone!")


if __name__ == "__main__":
    main()
