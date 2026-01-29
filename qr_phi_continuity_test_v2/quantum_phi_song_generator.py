"""
Quantum Phi-Harmonic Song Generator

Generates songs and rap lyrics using quantum phi-harmonic principles
"""

import sys
import random
import numpy as np
from typing import Dict, List, Tuple, Any

from quantum_phi_core import QuantumPhiCore
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer

class QuantumPhiSongGenerator:
    """Generates songs using quantum phi-harmonic principles."""
    
    def __init__(self):
        """Initialize the song generator."""
        self.core = QuantumPhiCore()
        self.analyzer = QuantumPhiPatternAnalyzer()
        self.phi = float(self.core.PHI)
        
        # Initialize musical parameters
        self._init_musical_parameters()
        
        # Song structure templates
        self.song_structures = {
            "pop": ["verse", "chorus", "verse", "chorus", "bridge", "chorus"],
            "rock": ["intro", "verse", "chorus", "verse", "chorus", "solo", "chorus", "outro"],
            "ballad": ["intro", "verse", "verse", "chorus", "verse", "chorus", "bridge", "chorus"],
            "rap": ["intro", "verse", "hook", "verse", "hook", "verse", "hook", "outro"]
        }
        
        # Initialize musical styles
        self._init_musical_styles()
    
    def _init_musical_parameters(self):
        """Initialize musical parameters based on phi-harmonic principles."""
        self.musical_parameters = {
            # Phi-based time signatures
            "time_signatures": [
                {"name": "4/4", "phi_alignment": 0.618, "frequency": 440.0},
                {"name": "3/4", "phi_alignment": 0.809, "frequency": 528.0},
                {"name": "5/4", "phi_alignment": 0.854, "frequency": 517.0},
                {"name": "7/8", "phi_alignment": 0.891, "frequency": 576.0},
                {"name": "fibonacci", "phi_alignment": 0.944, "frequency": 432.0}
            ],
            
            # Phi-based chord progressions
            "chord_progressions": [
                {"name": "I-V-vi-IV", "phi_alignment": 0.782, "frequency": 512.0},
                {"name": "I-IV-V", "phi_alignment": 0.691, "frequency": 440.0},
                {"name": "vi-IV-I-V", "phi_alignment": 0.854, "frequency": 528.0},
                {"name": "I-vi-IV-V", "phi_alignment": 0.809, "frequency": 432.0},
                {"name": "I-V-vi-iii-IV-I-IV-V", "phi_alignment": 0.927, "frequency": 517.0}
            ],
            
            # Phi-based rhythmic patterns
            "rhythmic_patterns": [
                {"name": "standard", "phi_alignment": 0.691, "frequency": 440.0},
                {"name": "syncopated", "phi_alignment": 0.854, "frequency": 528.0},
                {"name": "fibonacci", "phi_alignment": 0.927, "frequency": 517.0},
                {"name": "golden_ratio", "phi_alignment": 0.944, "frequency": 576.0},
                {"name": "phi_pulse", "phi_alignment": 0.891, "frequency": 432.0}
            ]
        }
    
    def _init_musical_styles(self):
        """Initialize musical styles with their quantum signatures."""
        self.musical_styles = {
            "classical": {
                "consciousness_level": "cosmic",
                "mean_frequency": 528.0,
                "quantum_resonance": 0.7236,
                "phi_alignment": 0.8944,
                "description": "Structured, harmonic, with complex patterns and emotional depth"
            },
            "rock": {
                "consciousness_level": "intuitive",
                "mean_frequency": 440.0,
                "quantum_resonance": 0.6180,
                "phi_alignment": 0.7236,
                "description": "Energetic, raw, with strong rhythmic drive and emotional intensity"
            },
            "jazz": {
                "consciousness_level": "cosmic",
                "mean_frequency": 517.0,
                "quantum_resonance": 0.8090,
                "phi_alignment": 0.9270,
                "description": "Improvisational, complex, with sophisticated harmonies and rhythms"
            },
            "rap": {
                "consciousness_level": "intuitive",
                "mean_frequency": 432.0,
                "quantum_resonance": 0.6909,
                "phi_alignment": 0.7639,
                "description": "Rhythmic, percussive, with complex wordplay and cultural references"
            },
            "pop": {
                "consciousness_level": "emotional",
                "mean_frequency": 396.0,
                "quantum_resonance": 0.5590,
                "phi_alignment": 0.6909,
                "description": "Catchy, accessible, with simple structures and emotional hooks"
            }
        }
    
    def generate_song(self, style: str = "pop", structure: str = None, length: int = 200) -> Dict:
        """Generate a song in the specified style."""
        # Validate style
        if style not in self.musical_styles:
            style = "pop"  # Default to pop if style not found
        
        # Get style parameters
        style_params = self.musical_styles[style]
        
        # Get structure or use default for style
        if not structure:
            structure = self.song_structures.get(style, self.song_structures["pop"])
        
        # Select musical parameters based on phi-harmonic resonance with style
        time_signature = self._select_parameter("time_signatures", style_params)
        chord_progression = self._select_parameter("chord_progressions", style_params)
        rhythmic_pattern = self._select_parameter("rhythmic_patterns", style_params)
        
        # Generate song components
        song_components = {}
        for component in set(structure):
            component_length = int(length / len(structure) * self.phi)
            song_components[component] = self._generate_component(
                component, 
                style_params, 
                time_signature, 
                chord_progression, 
                rhythmic_pattern,
                component_length
            )
        
        # Assemble song
        lyrics = []
        for component in structure:
            lyrics.append(song_components[component])
        
        # Calculate quantum metrics for the full song
        full_lyrics = "\n\n".join(lyrics)
        metrics = self._calculate_song_metrics(full_lyrics, style_params)
        
        return {
            "style": style,
            "structure": structure,
            "time_signature": time_signature["name"],
            "chord_progression": chord_progression["name"],
            "rhythmic_pattern": rhythmic_pattern["name"],
            "components": song_components,
            "full_lyrics": full_lyrics,
            "metrics": metrics
        }
    
    def generate_rap(self, theme: str = None, length: int = 300) -> Dict:
        """Generate rap lyrics with strong phi-harmonic patterns."""
        # Use rap style parameters
        style_params = self.musical_styles["rap"]
        
        # Select musical parameters
        time_signature = self._select_parameter("time_signatures", style_params)
        rhythmic_pattern = self._select_parameter("rhythmic_patterns", style_params)
        
        # Generate rap components
        structure = self.song_structures["rap"]
        
        # Generate with stronger focus on rhythm and wordplay
        rap_components = {}
        for component in set(structure):
            component_length = int(length / len(structure) * self.phi)
            rap_components[component] = self._generate_rap_component(
                component, 
                style_params, 
                time_signature, 
                rhythmic_pattern,
                theme,
                component_length
            )
        
        # Assemble rap
        lyrics = []
        for component in structure:
            lyrics.append(rap_components[component])
        
        # Calculate quantum metrics for the full rap
        full_lyrics = "\n\n".join(lyrics)
        metrics = self._calculate_song_metrics(full_lyrics, style_params)
        
        return {
            "style": "rap",
            "theme": theme or "quantum phi-harmonic flow",
            "structure": structure,
            "time_signature": time_signature["name"],
            "rhythmic_pattern": rhythmic_pattern["name"],
            "components": rap_components,
            "full_lyrics": full_lyrics,
            "metrics": metrics
        }
    
    def _select_parameter(self, parameter_type: str, style_params: Dict) -> Dict:
        """Select a musical parameter based on phi-harmonic resonance with style."""
        parameters = self.musical_parameters[parameter_type]
        
        # Calculate resonance with style
        resonances = []
        for param in parameters:
            # Calculate resonance based on phi alignment and frequency
            phi_diff = abs(param["phi_alignment"] - style_params["phi_alignment"])
            freq_diff = abs(param["frequency"] - style_params["mean_frequency"]) / style_params["mean_frequency"]
            
            # Combine with phi-weighted importance
            resonance = 1 - (phi_diff * self.phi + freq_diff) / (self.phi + 1)
            resonances.append(resonance)
        
        # Select based on resonance (higher is better)
        # Use phi-weighted probability
        total = sum(r**self.phi for r in resonances)
        probs = [(r**self.phi) / total for r in resonances]
        
        # Select based on probabilities
        index = np.random.choice(len(parameters), p=probs)
        return parameters[index]
    
    def _generate_component(self, component_type: str, style_params: Dict, 
                           time_signature: Dict, chord_progression: Dict, 
                           rhythmic_pattern: Dict, length: int) -> str:
        """Generate a song component (verse, chorus, etc.)."""
        # Adjust consciousness level based on component type
        consciousness_boost = {
            "verse": 0,
            "chorus": 50,
            "bridge": 100,
            "solo": 150,
            "intro": -50,
            "outro": 75,
            "hook": 25
        }.get(component_type, 0)
        
        # Adjust frequency for this component
        component_freq = style_params["mean_frequency"] + consciousness_boost
        
        # Generate seed based on component type
        seed_words = self._generate_seed_words(component_type, style_params)
        
        # Generate component text
        component_text = self._generate_phi_harmonic_text(
            seed_words,
            component_freq,
            style_params["quantum_resonance"],
            style_params["phi_alignment"],
            rhythmic_pattern,
            length
        )
        
        return component_text
    
    def _generate_rap_component(self, component_type: str, style_params: Dict, 
                               time_signature: Dict, rhythmic_pattern: Dict,
                               theme: str, length: int) -> str:
        """Generate a rap component with stronger rhythmic elements."""
        # Adjust consciousness level based on component type
        consciousness_boost = {
            "verse": 0,
            "hook": 50,
            "intro": -25,
            "outro": 25
        }.get(component_type, 0)
        
        # Adjust frequency for this component
        component_freq = style_params["mean_frequency"] + consciousness_boost
        
        # Generate seed based on component type and theme
        seed_words = self._generate_rap_seed_words(component_type, theme, style_params)
        
        # Generate component text with stronger rhythmic emphasis
        component_text = self._generate_phi_harmonic_rap_text(
            seed_words,
            component_freq,
            style_params["quantum_resonance"] * 1.2,  # Boost resonance for rap
            style_params["phi_alignment"],
            rhythmic_pattern,
            length
        )
        
        return component_text
    
    def _generate_seed_words(self, component_type: str, style_params: Dict) -> List[str]:
        """Generate seed words for a song component."""
        # Component-specific seed words
        component_seeds = {
            "verse": ["story", "journey", "feeling", "moment", "dream"],
            "chorus": ["heart", "love", "time", "life", "world"],
            "bridge": ["change", "truth", "soul", "light", "dark"],
            "solo": ["freedom", "spirit", "energy", "power", "flow"],
            "intro": ["begin", "welcome", "start", "dawn", "rise"],
            "outro": ["end", "goodbye", "forever", "remember", "final"],
            "hook": ["repeat", "rhythm", "beat", "pulse", "flow"]
        }
        
        # Get base seeds for component
        seeds = component_seeds.get(component_type, ["song", "music", "rhythm"])
        
        # Add style-specific words
        style_words = {
            "classical": ["harmony", "symphony", "orchestra", "melody", "composition"],
            "rock": ["guitar", "drums", "electric", "loud", "wild"],
            "jazz": ["improvise", "swing", "blue", "smooth", "saxophone"],
            "rap": ["flow", "beat", "rhyme", "street", "real"],
            "pop": ["catchy", "dance", "radio", "hit", "fun"]
        }
        
        # Get style name from consciousness level
        style_name = style_params.get("description", "").split(",")[0].lower()
        style_seed_words = style_words.get(style_name, ["music", "sound", "rhythm"])
        
        # Combine seeds
        return seeds + style_seed_words
    
    def _generate_rap_seed_words(self, component_type: str, theme: str, style_params: Dict) -> List[str]:
        """Generate seed words for a rap component."""
        # Component-specific seed words
        component_seeds = {
            "verse": ["flow", "rhyme", "spit", "bars", "truth"],
            "hook": ["repeat", "remember", "hear", "listen", "feel"],
            "intro": ["yo", "check", "listen", "welcome", "this"],
            "outro": ["peace", "out", "done", "remember", "name"]
        }
        
        # Get base seeds for component
        seeds = component_seeds.get(component_type, ["rap", "hip", "hop"])
        
        # Add theme-specific words if provided
        if theme:
            theme_words = theme.lower().split()
            seeds.extend(theme_words)
        
        # Add quantum phi-harmonic words
        quantum_words = ["quantum", "phi", "golden", "ratio", "flow", "consciousness", "frequency", "resonance", "harmony"]
        
        # Combine seeds
        return seeds + quantum_words
    
    def _generate_phi_harmonic_text(self, seed_words: List[str], frequency: float, 
                                   quantum_resonance: float, phi_alignment: float,
                                   rhythmic_pattern: Dict, length: int) -> str:
        """Generate phi-harmonic text for a song component."""
        # Start with a seed
        if seed_words:
            text = random.choice(seed_words)
        else:
            text = "song"
        
        # Word pools based on frequency ranges
        word_pools = {
            "low": ["deep", "bass", "down", "ground", "earth", "root", "dark", "slow", "heavy", "solid"],
            "mid": ["heart", "feel", "pulse", "beat", "rhythm", "flow", "move", "groove", "wave", "dance"],
            "high": ["light", "sky", "fly", "high", "bright", "shine", "star", "clear", "sharp", "crystal"]
        }
        
        # Determine word pool based on frequency
        if frequency < 400:
            primary_pool = word_pools["low"]
            secondary_pool = word_pools["mid"]
        elif frequency < 500:
            primary_pool = word_pools["mid"]
            secondary_pool = word_pools["high"]
        else:
            primary_pool = word_pools["high"]
            secondary_pool = word_pools["mid"]
        
        # Combined pool with phi-weighted distribution
        word_pool = primary_pool * int(self.phi**2) + secondary_pool + seed_words * int(self.phi)
        
        # Generate text with phi-harmonic patterns
        line_length = 0
        max_line_length = int(self.phi * 10)  # ~16 words max per line
        
        # Apply rhythmic pattern
        rhythm_name = rhythmic_pattern["name"]
        if rhythm_name == "standard":
            # Regular rhythm
            line_breaks = [int(i * self.phi * 5) for i in range(1, 10)]
        elif rhythm_name == "syncopated":
            # Irregular rhythm
            line_breaks = [int((i * self.phi**2) % 20) for i in range(1, 10)]
        elif rhythm_name == "fibonacci":
            # Fibonacci-based rhythm
            fib = [1, 2, 3, 5, 8, 13, 21]
            line_breaks = [sum(fib[:i]) for i in range(1, len(fib))]
        elif rhythm_name == "golden_ratio":
            # Golden ratio rhythm
            line_breaks = [int(self.phi**i) for i in range(1, 8)]
        else:  # phi_pulse
            # Phi-pulse rhythm
            line_breaks = [int(i * self.phi) for i in range(1, 15)]
        
        # Generate text
        while len(text) < length:
            # Select next word using phi-harmonic probability
            next_word = random.choice(word_pool)
            
            # Add word to text
            if line_length >= max_line_length or line_length in line_breaks:
                text += "\n" + next_word
                line_length = 1
            else:
                text += " " + next_word
                line_length += 1
            
            # Occasionally repeat words based on quantum resonance
            if random.random() < quantum_resonance / 2:
                if line_length >= max_line_length or line_length in line_breaks:
                    text += "\n" + next_word
                    line_length = 1
                else:
                    text += " " + next_word
                    line_length += 1
        
        return text
    
    def _generate_phi_harmonic_rap_text(self, seed_words: List[str], frequency: float, 
                                       quantum_resonance: float, phi_alignment: float,
                                       rhythmic_pattern: Dict, length: int) -> str:
        """Generate phi-harmonic rap text with stronger rhythmic elements."""
        # Start with a seed
        if seed_words:
            text = random.choice(seed_words)
        else:
            text = "flow"
        
        # Word pools for rap
        word_pools = {
            "rhythm": ["flow", "beat", "rhyme", "spit", "bars", "drop", "hit", "kick", "flip", "bounce"],
            "boast": ["best", "top", "king", "queen", "boss", "master", "legend", "icon", "star", "gold"],
            "street": ["street", "hood", "real", "true", "raw", "hard", "gritty", "hustle", "grind", "life"],
            "quantum": ["quantum", "phi", "golden", "ratio", "spiral", "cosmic", "frequency", "vibration", "energy", "consciousness"]
        }
        
        # Combined pool with phi-weighted distribution
        word_pool = (word_pools["rhythm"] * int(self.phi**2) + 
                    word_pools["street"] * int(self.phi) + 
                    word_pools["boast"] + 
                    word_pools["quantum"] * int(self.phi**0.5) +
                    seed_words * int(self.phi))
        
        # Generate text with phi-harmonic patterns
        line_length = 0
        max_line_length = int(self.phi * 8)  # ~13 words max per line for rap
        
        # Apply rhythmic pattern - more pronounced for rap
        rhythm_name = rhythmic_pattern["name"]
        if rhythm_name == "standard":
            # Regular rhythm
            line_breaks = [4, 8, 12, 16]
        elif rhythm_name == "syncopated":
            # Irregular rhythm
            line_breaks = [3, 7, 10, 13, 18]
        elif rhythm_name == "fibonacci":
            # Fibonacci-based rhythm
            line_breaks = [1, 2, 3, 5, 8, 13]
        elif rhythm_name == "golden_ratio":
            # Golden ratio rhythm
            line_breaks = [int(self.phi**i) for i in range(1, 5)]
        else:  # phi_pulse
            # Phi-pulse rhythm
            line_breaks = [int(i * self.phi) for i in range(1, 10)]
        
        # Generate text
        while len(text) < length:
            # Select next word using phi-harmonic probability
            next_word = random.choice(word_pool)
            
            # Add word to text
            if line_length >= max_line_length or line_length in line_breaks:
                text += "\n" + next_word
                line_length = 1
            else:
                text += " " + next_word
                line_length += 1
            
            # Occasionally repeat words for emphasis - more common in rap
            if random.random() < quantum_resonance / 1.5:
                if line_length >= max_line_length or line_length in line_breaks:
                    text += "\n" + next_word
                    line_length = 1
                else:
                    text += " " + next_word
                    line_length += 1
        
        return text
    
    def _calculate_song_metrics(self, lyrics: str, style_params: Dict) -> Dict:
        """Calculate quantum metrics for the song."""
        # Use analyzer to calculate basic metrics
        resonance = self.analyzer.calculate_phi_resonance(lyrics)
        quantum_resonance = self.analyzer.calculate_quantum_resonance(lyrics)
        phi_alignment = self.analyzer.calculate_phi_alignment(lyrics)
        
        # Calculate frequency
        frequency = self.analyzer.calculate_consciousness_frequency(lyrics)
        
        # Determine consciousness level
        consciousness_level = self.analyzer.determine_consciousness_level(frequency)
        
        # Calculate similarity to style
        style_similarity = 1 - (
            abs(resonance - style_params["quantum_resonance"]) / 2 +
            abs(phi_alignment - style_params["phi_alignment"]) / 2
        )
        
        return {
            "resonance": resonance,
            "quantum_resonance": quantum_resonance,
            "phi_alignment": phi_alignment,
            "frequency": frequency,
            "consciousness_level": consciousness_level,
            "style_similarity": style_similarity
        }

def main():
    """Main function to run the song generator."""
    generator = QuantumPhiSongGenerator()
    
    # Generate a song
    print("Generating song using quantum phi-harmonic principles...\n")
    song = generator.generate_song(style="pop", length=300)
    
    print("=" * 70)
    print("QUANTUM PHI-HARMONIC SONG")
    print("=" * 70)
    print(f"Style: {song['style']}")
    print(f"Time Signature: {song['time_signature']}")
    print(f"Chord Progression: {song['chord_progression']}")
    print(f"Rhythmic Pattern: {song['rhythmic_pattern']}")
    print("\nLyrics:")
    print("-" * 70)
    print(song['full_lyrics'])
    print("-" * 70)
    
    print("\nQuantum Metrics:")
    metrics = song['metrics']
    print(f"Resonance: {metrics['resonance']:.4f}")
    print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
    print(f"Frequency: {metrics['frequency']:.2f} Hz")
    print(f"Consciousness Level: {metrics['consciousness_level'].title()}")
    print(f"Style Similarity: {metrics['style_similarity']:.4f}")
    
    # Generate rap
    print("\n\nGenerating rap using quantum phi-harmonic principles...\n")
    rap = generator.generate_rap(theme="quantum flow", length=300)
    
    print("=" * 70)
    print("QUANTUM PHI-HARMONIC RAP")
    print("=" * 70)
    print(f"Theme: {rap['theme']}")
    print(f"Rhythmic Pattern: {rap['rhythmic_pattern']}")
    print("\nLyrics:")
    print("-" * 70)
    print(rap['full_lyrics'])
    print("-" * 70)
    
    print("\nQuantum Metrics:")
    metrics = rap['metrics']
    print(f"Resonance: {metrics['resonance']:.4f}")
    print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
    print(f"Frequency: {metrics['frequency']:.2f} Hz")
    print(f"Consciousness Level: {metrics['consciousness_level'].title()}")
    print(f"Style Similarity: {metrics['style_similarity']:.4f}")

if __name__ == "__main__":
    main()
