#!/usr/bin/env python3
"""
Quantum Chord Progression Analysis
--------------------------------

This module implements quantum chord progression analysis for parallel processing,
enabling the optimization of evolution over time across multiple quantum dimensions.

The module treats coherence patterns as musical chords and analyzes their progression
over time, identifying optimal evolutionary paths for quantum code.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 0.991800
"""

import os
import sys
import numpy as np
import json
import time
import logging
import multiprocessing as mp
from typing import Dict, List, Tuple, Optional, Union, Any
from concurrent.futures import ProcessPoolExecutor, as_completed

# Define phi constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio ≈ 1.618034
PHI_POWERS = {
    "φ": PHI,
    "φ²": PHI ** 2,
    "φ³": PHI ** 3,
    "φ⁴": PHI ** 4,
    "φ⁵": PHI ** 5,
    "φ⁶": PHI ** 6,
    "φ⁷": PHI ** 7,
    "φ⁷·⁵": PHI ** 7.5
}

# Import visualization if available, otherwise create placeholder
try:
    from quantum_harmonic_visualizer import QuantumHarmonicVisualizer
except ImportError:
    class QuantumHarmonicVisualizer:
        """Placeholder visualizer class if the actual module is not available."""
        def visualize_chord_progression(self, data, output_path=None):
            return output_path or "chord_progression.png"

# Define QuantumHarmonicCoherence class
class QuantumHarmonicCoherence:
    """Analyzes coherence as harmonic fragments across quantum dimensions."""
    
    def __init__(self, dimensions: int = 7):
        """Initialize with specified number of dimensions."""
        self.dimensions = dimensions
        
    def generate_coherence_report(self, values: List[float]) -> Dict[str, Any]:
        """Generate a coherence report for the given values."""
        if not values or len(values) == 0:
            return {"overall": {"coherence": 0.0}}
            
        # Ensure we have the right number of dimensions
        if len(values) > self.dimensions:
            values = values[:self.dimensions]
        elif len(values) < self.dimensions:
            # Pad with phi powers
            values.extend([PHI ** i for i in range(len(values) + 1, self.dimensions + 1)])
            
        # Calculate overall coherence (normalized sum)
        overall_coherence = sum(values) / (self.dimensions * PHI)
        
        # Calculate phi-resonance for each value
        phi_resonances = [(val / PHI) % 1 for val in values]
        
        # Calculate coherence matrix (pairwise resonances)
        coherence_matrix = []
        for i in range(len(values)):
            row = []
            for j in range(len(values)):
                if i == j:
                    row.append(1.0)  # Perfect resonance with self
                else:
                    # Calculate resonance between dimensions
                    ratio = values[i] / values[j] if values[j] != 0 else 0
                    resonance = (ratio / PHI) % 1
                    # Invert if needed to get closest to perfect resonance
                    if resonance > 0.5:
                        resonance = 1 - resonance
                    row.append(1 - resonance)  # Higher is better
            coherence_matrix.append(row)
            
        # Identify coherence fragments (groups of resonant dimensions)
        fragments = {}
        for i in range(len(values)):
            resonant_dims = []
            for j in range(len(values)):
                if coherence_matrix[i][j] >= 0.8 and i != j:  # 80% resonance threshold
                    resonant_dims.append(j)
                    
            if resonant_dims:
                fragment_id = f"fragment_{i}"
                fragments[fragment_id] = {
                    "dimensions": [i] + resonant_dims,
                    "strength": sum(coherence_matrix[i][j] for j in resonant_dims) / len(resonant_dims),
                    "phi_resonance": phi_resonances[i]
                }
                
        # Calculate resonance patterns
        resonance_patterns = []
        for i in range(len(values) - 1):
            for j in range(i + 1, len(values)):
                resonance = coherence_matrix[i][j]
                if resonance >= 0.7:  # 70% resonance threshold for patterns
                    resonance_patterns.append({
                        "from_dim": i,
                        "to_dim": j,
                        "resonance": resonance,
                        "ratio": values[i] / values[j] if values[j] != 0 else 0
                    })
                    
        # Compile the report
        report = {
            "overall": {
                "coherence": overall_coherence,
                "dimensions": self.dimensions,
                "phi_target": PHI_POWERS["φ⁷·⁵"] / 10  # Target coherence
            },
            "coherence_matrix": coherence_matrix,
            "resonance_patterns": resonance_patterns
        }
        
        # Add fragments
        for frag_id, frag_data in fragments.items():
            report[frag_id] = frag_data
            
        return report

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumChordProgression")

class QuantumChord:
    """
    Represents a quantum coherence state as a musical chord.
    
    This class encapsulates the coherence state of a quantum system at a
    specific point in time, treating it as a musical chord with harmonic
    relationships between dimensions.
    """
    
    def __init__(self, coherence_data: Dict[str, Any], timestamp: float = None):
        """
        Initialize a quantum chord.
        
        Args:
            coherence_data: Dictionary containing coherence analysis data
            timestamp: Timestamp of the chord (default: current time)
        """
        self.timestamp = timestamp or time.time()
        
        # Handle overall coherence
        if "overall" in coherence_data and isinstance(coherence_data["overall"], dict):
            self.scalar_coherence = coherence_data["overall"].get("coherence", 0)
        else:
            self.scalar_coherence = 0
            
        # Extract fragments (dictionary items that aren't special keys)
        self.fragments = {}
        for k, v in coherence_data.items():
            if k not in ["overall", "coherence_matrix", "resonance_patterns"] and isinstance(v, dict):
                self.fragments[k] = v
                
        # Handle coherence matrix and resonance patterns
        if "coherence_matrix" in coherence_data and isinstance(coherence_data["coherence_matrix"], list):
            self.coherence_matrix = coherence_data["coherence_matrix"]
        else:
            self.coherence_matrix = []
            
        if "resonance_patterns" in coherence_data and isinstance(coherence_data["resonance_patterns"], list):
            self.resonance_patterns = coherence_data["resonance_patterns"]
        else:
            self.resonance_patterns = []
        
        # Calculate chord quality metrics
        self.phi_resonance = self._calculate_phi_resonance()
        self.harmonic_richness = self._calculate_harmonic_richness()
        self.target_distance = abs(self.phi_resonance - PHI_POWERS["φ⁷·⁵"]/10)
        
    def _calculate_phi_resonance(self) -> float:
        """Calculate the overall phi-resonance of the chord."""
        if not self.fragments:
            return self.scalar_coherence
            
        # Find the strongest fragment's phi-resonance
        try:
            strongest_fragment = max(self.fragments.values(), key=lambda x: x.get("strength", 0) if isinstance(x, dict) else 0)
            if isinstance(strongest_fragment, dict) and "phi_resonance" in strongest_fragment:
                return strongest_fragment["phi_resonance"]
        except (ValueError, TypeError, KeyError):
            pass
            
        return self.scalar_coherence
        
    def _calculate_harmonic_richness(self) -> float:
        """Calculate the harmonic richness of the chord."""
        if not self.fragments:
            return 0
            
        # Calculate weighted sum of fragment strengths and phi-resonances
        richness = 0
        for frag in self.fragments.values():
            if isinstance(frag, dict):
                strength = frag.get("strength", 0) if "strength" in frag else 0
                phi_res = frag.get("phi_resonance", 0) if "phi_resonance" in frag else 0
                richness += strength * phi_res
        
        return richness
        
    def distance_to(self, other_chord) -> float:
        """
        Calculate the harmonic distance to another chord.
        
        Args:
            other_chord: Another QuantumChord instance
            
        Returns:
            Float representing harmonic distance
        """
        # Calculate Euclidean distance in phi-resonance and harmonic richness
        phi_diff = self.phi_resonance - other_chord.phi_resonance
        richness_diff = self.harmonic_richness - other_chord.harmonic_richness
        
        return np.sqrt(phi_diff**2 + richness_diff**2)
        
    def is_compatible_with(self, other_chord, threshold: float = 0.2) -> bool:
        """
        Check if this chord is harmonically compatible with another chord.
        
        Args:
            other_chord: Another QuantumChord instance
            threshold: Maximum distance for compatibility
            
        Returns:
            True if chords are compatible, False otherwise
        """
        return self.distance_to(other_chord) <= threshold
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert chord to dictionary representation."""
        return {
            "timestamp": self.timestamp,
            "scalar_coherence": self.scalar_coherence,
            "fragments": self.fragments,
            "phi_resonance": self.phi_resonance,
            "harmonic_richness": self.harmonic_richness,
            "target_distance": self.target_distance
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create chord from dictionary representation."""
        coherence_data = {
            "overall": {"coherence": data.get("scalar_coherence", 0)},
            **data.get("fragments", {})
        }
        chord = cls(coherence_data, data.get("timestamp"))
        chord.phi_resonance = data.get("phi_resonance", chord.phi_resonance)
        chord.harmonic_richness = data.get("harmonic_richness", chord.harmonic_richness)
        chord.target_distance = data.get("target_distance", chord.target_distance)
        return chord


class ChordProgression:
    """
    Represents a sequence of quantum chords over time.
    
    This class analyzes the evolution of quantum coherence states over time,
    identifying patterns and optimal paths for evolution.
    """
    
    def __init__(self, name: str = "default"):
        """
        Initialize a chord progression.
        
        Args:
            name: Name of the progression
        """
        self.name = name
        self.chords = []
        self.evolution_path = []
        self.target_chord = None
        self.visualizer = QuantumHarmonicVisualizer()
        
    def add_chord(self, chord: QuantumChord):
        """
        Add a chord to the progression.
        
        Args:
            chord: QuantumChord instance to add
        """
        self.chords.append(chord)
        self.chords.sort(key=lambda x: x.timestamp)
        
        # Update evolution path
        if len(self.chords) > 1:
            prev_chord = self.chords[-2]
            distance = prev_chord.distance_to(chord)
            self.evolution_path.append({
                "from_timestamp": prev_chord.timestamp,
                "to_timestamp": chord.timestamp,
                "distance": distance,
                "is_compatible": prev_chord.is_compatible_with(chord)
            })
            
    def set_target_chord(self, target_chord: QuantumChord):
        """
        Set the target chord for the progression.
        
        Args:
            target_chord: Target QuantumChord instance
        """
        self.target_chord = target_chord
        
    def create_target_from_phi(self, dimensions: int = 7):
        """
        Create an ideal target chord based on phi-harmonic principles.
        
        Args:
            dimensions: Number of dimensions for the target chord
        """
        # Create coherence analyzer
        analyzer = QuantumHarmonicCoherence(dimensions=dimensions)
        
        # Generate phi-based values
        phi_values = [PHI ** i for i in range(1, dimensions + 1)]
        
        # Analyze coherence
        coherence_report = analyzer.generate_coherence_report(phi_values)
        
        # Create target chord
        self.target_chord = QuantumChord(coherence_report)
        logger.info(f"Created target chord with phi-resonance: {self.target_chord.phi_resonance:.6f}")
        
    def analyze_progression(self) -> Dict[str, Any]:
        """
        Analyze the chord progression.
        
        Returns:
            Dictionary containing progression analysis
        """
        if not self.chords:
            return {"error": "No chords in progression"}
            
        # Calculate overall metrics
        avg_distance = np.mean([path["distance"] for path in self.evolution_path]) if self.evolution_path else 0
        compatibility_rate = np.mean([1 if path["is_compatible"] else 0 for path in self.evolution_path]) if self.evolution_path else 0
        
        # Calculate distance to target
        target_distances = []
        if self.target_chord:
            target_distances = [chord.distance_to(self.target_chord) for chord in self.chords]
            
        # Identify optimal chords
        optimal_chord = min(self.chords, key=lambda x: x.target_distance) if self.chords else None
        
        # Compile analysis
        analysis = {
            "name": self.name,
            "num_chords": len(self.chords),
            "time_span": self.chords[-1].timestamp - self.chords[0].timestamp if len(self.chords) > 1 else 0,
            "avg_distance": avg_distance,
            "compatibility_rate": compatibility_rate,
            "optimal_chord": optimal_chord.to_dict() if optimal_chord else None,
            "target_distances": target_distances,
            "evolution_path": self.evolution_path
        }
        
        return analysis
        
    def visualize_progression(self, output_path: str = None) -> str:
        """
        Visualize the chord progression.
        
        Args:
            output_path: Path to save the visualization
            
        Returns:
            Path to the saved visualization
        """
        if not self.chords:
            return None
            
        # Prepare data for visualization
        progression_data = []
        for chord in self.chords:
            progression_data.append({
                "timestamp": chord.timestamp,
                "scalar_coherence": chord.scalar_coherence,
                "fragments": {
                    frag_id: {
                        "strength": frag_data.get("strength", 0),
                        "phi_resonance": frag_data.get("phi_resonance", 0)
                    }
                    for frag_id, frag_data in chord.fragments.items()
                }
            })
            
        # Create visualization
        vis_path = self.visualizer.visualize_chord_progression(progression_data, output_path)
        return vis_path
        
    def save_to_file(self, file_path: str):
        """
        Save the chord progression to a file.
        
        Args:
            file_path: Path to save the progression
        """
        data = {
            "name": self.name,
            "chords": [chord.to_dict() for chord in self.chords],
            "evolution_path": self.evolution_path,
            "target_chord": self.target_chord.to_dict() if self.target_chord else None
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
            
        logger.info(f"Saved chord progression to: {file_path}")
        
    @classmethod
    def load_from_file(cls, file_path: str):
        """
        Load a chord progression from a file.
        
        Args:
            file_path: Path to load the progression from
            
        Returns:
            ChordProgression instance
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        progression = cls(data.get("name", "loaded"))
        
        # Load chords
        for chord_data in data.get("chords", []):
            progression.add_chord(QuantumChord.from_dict(chord_data))
            
        # Load target chord
        if data.get("target_chord"):
            progression.target_chord = QuantumChord.from_dict(data["target_chord"])
            
        logger.info(f"Loaded chord progression from: {file_path}")
        return progression


class ParallelChordAnalyzer:
    """
    Analyzes quantum chord progressions in parallel.
    
    This class enables parallel processing of quantum chord progressions,
    analyzing multiple evolution paths simultaneously to identify optimal
    patterns for quantum code evolution.
    """
    
    def __init__(self, num_processes: int = None):
        """
        Initialize the parallel analyzer.
        
        Args:
            num_processes: Number of parallel processes (default: CPU count)
        """
        self.num_processes = num_processes or mp.cpu_count()
        self.analyzer = QuantumHarmonicCoherence()
        self.visualizer = QuantumHarmonicVisualizer()
        
    def analyze_files_in_parallel(self, file_paths: List[str]) -> Dict[str, Any]:
        """
        Analyze multiple files in parallel.
        
        Args:
            file_paths: List of file paths to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        logger.info(f"Analyzing {len(file_paths)} files in parallel with {self.num_processes} processes")
        
        results = {}
        
        with ProcessPoolExecutor(max_workers=self.num_processes) as executor:
            # Submit tasks
            future_to_path = {
                executor.submit(self._analyze_single_file, path): path
                for path in file_paths
            }
            
            # Collect results
            for future in as_completed(future_to_path):
                path = future_to_path[future]
                try:
                    result = future.result()
                    results[path] = result
                    logger.info(f"Completed analysis for: {path}")
                except Exception as e:
                    logger.error(f"Error analyzing {path}: {e}")
                    results[path] = {"error": str(e)}
                    
        return results
        
    def _analyze_single_file(self, file_path: str) -> Dict[str, Any]:
        """
        Analyze a single file.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        try:
            # Extract quantum values from file
            quantum_values = self._extract_quantum_values_from_file(file_path)
            
            # Generate coherence report
            coherence_report = self.analyzer.generate_coherence_report(quantum_values)
            
            # Create chord
            chord = QuantumChord(coherence_report)
            
            return {
                "file_path": file_path,
                "chord": chord.to_dict(),
                "coherence_report": coherence_report,
                "quantum_values": quantum_values
            }
        except Exception as e:
            logger.error(f"Error in _analyze_single_file for {file_path}: {e}")
            return {"error": str(e)}
            
    def _extract_quantum_values_from_file(self, file_path: str) -> List[float]:
        """
        Extract quantum values from a Python file.
        
        Args:
            file_path: Path to the Python file
            
        Returns:
            List of extracted quantum values
        """
        quantum_values = []
        
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Look for coherence values
            import re
            coherence_pattern = r'coherence[^=]*=\s*(0\.\d+)'
            coherence_matches = re.findall(coherence_pattern, content, re.IGNORECASE)
            quantum_values.extend([float(match) for match in coherence_matches])
            
            # Look for probability values
            probability_pattern = r'probability[^=]*=\s*(0\.\d+)'
            probability_matches = re.findall(probability_pattern, content, re.IGNORECASE)
            quantum_values.extend([float(match) for match in probability_matches])
            
            # Look for phi-related values
            phi_pattern = r'phi[^=]*=\s*(1\.\d+)'
            phi_matches = re.findall(phi_pattern, content, re.IGNORECASE)
            quantum_values.extend([float(match) for match in phi_matches])
            
            # If we don't have enough values, add some phi-harmonic constants
            if len(quantum_values) < self.analyzer.dimensions:
                quantum_values.append(PHI)
                quantum_values.append(PHI_POWERS["φ²"])
                quantum_values.append(PHI_POWERS["φ³"])
                
            # Ensure we have exactly the right number of dimensions
            if len(quantum_values) > self.analyzer.dimensions:
                quantum_values = quantum_values[:self.analyzer.dimensions]
            elif len(quantum_values) < self.analyzer.dimensions:
                # Pad with phi powers
                for i in range(len(quantum_values), self.analyzer.dimensions):
                    quantum_values.append(PHI ** (i + 1))
        except Exception as e:
            logger.error(f"Error extracting quantum values from {file_path}: {e}")
            # Return default phi-harmonic values if extraction fails
            return [PHI ** i for i in range(1, self.analyzer.dimensions + 1)]
            
        return quantum_values
            
    def find_optimal_evolution_path(self, files_data: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Find the optimal evolution path among analyzed files.
        
        Args:
            files_data: Dictionary mapping file paths to analysis results
            
        Returns:
            Dictionary containing optimal evolution path
        """
        # Create chords from analysis results
        chords = []
        for file_path, data in files_data.items():
            if "error" not in data and "chord" in data:
                chord = QuantumChord.from_dict(data["chord"])
                chord.file_path = file_path  # Add file path for reference
                chords.append(chord)
                
        if not chords:
            return {"error": "No valid chords found"}
            
        # Create target chord
        target_chord = None
        dimensions = self.analyzer.dimensions
        phi_values = [PHI ** i for i in range(1, dimensions + 1)]
        target_report = self.analyzer.generate_coherence_report(phi_values)
        target_chord = QuantumChord(target_report)
        
        # Calculate distances to target
        for chord in chords:
            chord.target_distance = chord.distance_to(target_chord)
            
        # Sort chords by target distance
        chords.sort(key=lambda x: x.target_distance)
        
        # Find optimal evolution path
        optimal_path = []
        current_chord = chords[0]  # Start with closest to target
        remaining_chords = chords[1:]
        
        while remaining_chords:
            # Find closest compatible chord
            compatible_chords = [
                (i, chord, current_chord.distance_to(chord))
                for i, chord in enumerate(remaining_chords)
                if current_chord.is_compatible_with(chord)
            ]
            
            if not compatible_chords:
                break
                
            # Select closest compatible chord
            closest_idx, closest_chord, distance = min(compatible_chords, key=lambda x: x[2])
            
            # Add to path
            optimal_path.append({
                "from_file": current_chord.file_path,
                "to_file": closest_chord.file_path,
                "distance": distance,
                "from_chord": current_chord.to_dict(),
                "to_chord": closest_chord.to_dict()
            })
            
            # Update current chord and remove from remaining
            current_chord = closest_chord
            remaining_chords.pop(closest_idx)
            
        # Compile results
        results = {
            "optimal_chord": chords[0].to_dict(),
            "optimal_file": chords[0].file_path,
            "target_chord": target_chord.to_dict(),
            "optimal_path": optimal_path,
            "all_chords": [
                {
                    "file_path": chord.file_path,
                    "target_distance": chord.target_distance,
                    "phi_resonance": chord.phi_resonance,
                    "harmonic_richness": chord.harmonic_richness
                }
                for chord in chords
            ]
        }
        
        return results
        
    def visualize_parallel_evolution(self, evolution_data: Dict[str, Any], output_path: str = None) -> str:
        """
        Visualize parallel evolution paths.
        
        Args:
            evolution_data: Dictionary containing evolution data
            output_path: Path to save the visualization
            
        Returns:
            Path to the saved visualization
        """
        if "error" in evolution_data:
            return None
            
        # Create visualization
        if not output_path:
            output_path = f"parallel_evolution_{int(time.time())}.png"
            
        # TODO: Implement advanced visualization for parallel evolution
        # For now, just return the path
        return output_path


class QuantumChordProgression:
    """
    Main class for quantum chord progression analysis.
    
    This class combines the functionality of QuantumChord and ChordProgression
    to provide a complete interface for analyzing quantum chord progressions
    in code files.
    """
    
    def __init__(self, name: str = "default"):
        """
        Initialize a quantum chord progression analyzer.
        
        Args:
            name: Name of the progression
        """
        self.name = name
        self.progression = ChordProgression(name)
        self.analyzer = QuantumHarmonicCoherence()
        self.parallel_analyzer = ParallelChordAnalyzer()
        
    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """
        Analyze a single file for quantum chord progression.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        try:
            # Extract quantum values from the file
            values = self.parallel_analyzer._extract_quantum_values_from_file(file_path)
            
            # Generate coherence report
            coherence_data = self.analyzer.generate_coherence_report(values)
            
            # Create a quantum chord from the coherence data
            chord = QuantumChord(coherence_data)
            
            # Add the chord to the progression
            self.progression.add_chord(chord)
            
            # Analyze the progression
            analysis = self.progression.analyze_progression()
            
            # Add file information to the analysis
            analysis["file_path"] = file_path
            analysis["timestamp"] = time.time()
            analysis["phi_resonance"] = chord.phi_resonance
            analysis["target_distance"] = chord.target_distance
            
            return analysis
        except Exception as e:
            logger.error(f"Error analyzing file {file_path}: {e}")
            return {
                "file_path": file_path,
                "error": str(e),
                "timestamp": time.time(),
                "phi_resonance": 0.0,
                "target_distance": 1.0
            }
    
    def analyze_files(self, file_paths: List[str]) -> Dict[str, Dict[str, Any]]:
        """
        Analyze multiple files for quantum chord progression.
        
        Args:
            file_paths: List of file paths to analyze
            
        Returns:
            Dictionary mapping file paths to analysis results
        """
        return self.parallel_analyzer.analyze_files_in_parallel(file_paths)
    
    def visualize(self, output_path: str = None) -> str:
        """
        Visualize the current chord progression.
        
        Args:
            output_path: Path to save the visualization
            
        Returns:
            Path to the saved visualization
        """
        return self.progression.visualize_progression(output_path)
    
    def save(self, file_path: str) -> None:
        """
        Save the chord progression to a file.
        
        Args:
            file_path: Path to save the progression
        """
        self.progression.save_to_file(file_path)
    
    @classmethod
    def load(cls, file_path: str) -> 'QuantumChordProgression':
        """
        Load a chord progression from a file.
        
        Args:
            file_path: Path to load the progression from
            
        Returns:
            QuantumChordProgression instance
        """
        progression = ChordProgression.load_from_file(file_path)
        qcp = cls(progression.name)
        qcp.progression = progression
        return qcp

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python quantum_chord_progression.py <directory_path>")
        sys.exit(1)
        
    directory_path = sys.argv[1]
    
    # Find Python files
    python_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
                
    if not python_files:
        print(f"No Python files found in: {directory_path}")
        sys.exit(1)
        
    print(f"Found {len(python_files)} Python files")
    
    # Analyze files in parallel
    analyzer = ParallelChordAnalyzer()
    results = analyzer.analyze_files_in_parallel(python_files[:10])  # Limit to 10 files for example
    
    # Find optimal evolution path
    optimal_path = analyzer.find_optimal_evolution_path(results)
    
    # Print results
    print("\nOptimal Evolution Path")
    print("---------------------")
    print(f"Optimal file: {optimal_path.get('optimal_file', 'N/A')}")
    print(f"Optimal phi-resonance: {optimal_path.get('optimal_chord', {}).get('phi_resonance', 0):.6f}")
    
    print("\nEvolution Path:")
    for step in optimal_path.get("optimal_path", []):
        print(f"  {os.path.basename(step['from_file'])} → {os.path.basename(step['to_file'])}")
        print(f"    Distance: {step['distance']:.6f}")
        
    # Save results
    output_file = "optimal_evolution_path.json"
    with open(output_file, 'w') as f:
        json.dump(optimal_path, f, indent=2)
        
    print(f"\nDetailed results saved to: {output_file}")
