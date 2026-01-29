#!/usr/bin/env python3
"""Quantum Chord Progression Extension
---------------------------------

Extension module that exposes the ChordProgression class as QuantumChordProgression.
This follows the modular "lego" architecture principle by extending functionality
without modifying the core module.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 0.991800
"""

import os
import sys
import logging
from typing import Dict, List, Any, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumChordProgressionExtension")

def apply_extension():
    """Apply all chord progression extensions."""
    logger.info("Applying chord progression extensions")
    
    # Track successful extensions
    applied_extensions = []
    
    # Apply QuantumChordProgression extensions
    try:
        # First try to import directly
        try:
            import sys
            import quantum_chord_progression
            from quantum_chord_progression import QuantumChordProgression
        except ImportError:
            logger.error("Failed to import QuantumChordProgression directly")
            raise
            
            # Check if analyze_file method exists
            if not hasattr(QuantumChordProgression, 'analyze_file'):
                # Define the analyze_file method
                def analyze_file(self, file_path: str) -> Dict[str, Any]:
                    """
                    Analyze a file and generate a chord progression.
                    
                    Args:
                        file_path: Path to the file to analyze
                        
                    Returns:
                        Dict containing analysis results
                    """
                    try:
                        # Read the file
                        with open(file_path, 'r') as f:
                            content = f.read()
                        
                        # Extract quantum values
                        quantum_values = self._extract_quantum_values(content)
                        
                        # Create chords
                        chords = []
                        for value in quantum_values:
                            try:
                                chord = QuantumChord(value)
                                chords.append(chord)
                            except Exception as e:
                                logger.warning(f"Failed to create chord for value {value}: {e}")
                        
                        # Store results
                        self.chords = chords
                        self.file_path = file_path
                        
                        # Return analysis results
                        return {
                            "file_path": file_path,
                            "n_chords": len(chords),
                            "coherence": self._calculate_coherence(chords)
                        }
                    except Exception as e:
                        logger.error(f"Error analyzing file {file_path}: {e}")
                        return {
                            "file_path": file_path,
                            "error": str(e)
                        }
                
                # Add the method to the class
                QuantumChordProgression.analyze_file = analyze_file
                
                # Patch the class definition in the module
                setattr(quantum_chord_progression, 'QuantumChordProgression', QuantumChordProgression)
                
                applied_extensions.append("QuantumChordProgression.analyze_file")
                logger.info("Added analyze_file method to QuantumChordProgression")
    except Exception as e:
        logger.error(f"Failed to apply QuantumChordProgression extensions: {e}")
    
    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """
        Analyze a file and generate a chord progression.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        logger.info(f"Analyzing file: {file_path}")
        
        # Use ParallelChordAnalyzer for the actual analysis
        parallel_analyzer = ParallelChordAnalyzer(num_processes=1)  # Single process for simplicity
        
        try:
            # Extract quantum values from file
            quantum_values = parallel_analyzer._extract_quantum_values_from_file(file_path)
            
            if not quantum_values:
                logger.warning(f"No quantum values found in file: {file_path}")
                return {"error": "No quantum values found"}
            
            # Generate coherence report
            coherence_report = self.analyzer.generate_coherence_report(quantum_values)
            
            # Create quantum chord from coherence report
            chord = QuantumChord(coherence_report)
            
            # Add chord to progression
            self.add_chord(chord)
            
            # Analyze progression
            progression_analysis = self.analyze_progression()
            
            # Create result dictionary
            result = {
                "file_path": file_path,
                "quantum_values": quantum_values,
                "coherence_report": coherence_report,
                "progression_analysis": progression_analysis,
                "chord_count": len(self.chords)
            }
            
            logger.info(f"Successfully analyzed file: {file_path}")
            return result
            
        except Exception as e:
            logger.error(f"Error analyzing file {file_path}: {str(e)}")
            return {"error": str(e)}
    
    def generate_evolution_report(self, output_path: str = None) -> Dict[str, Any]:
        """
        Generate a comprehensive evolution report.
        
        Args:
            output_path: Path to save the report and visualizations
            
        Returns:
            Dictionary containing evolution report
        """
        if not self.chords:
            logger.warning("No chords in progression, cannot generate report")
            return {"error": "No chords in progression"}
        
        # Create output directory if needed
        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        else:
            output_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "data",
                "chord_progression",
                f"evolution_report_{self.quantum_id}.json"
            )
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Analyze progression
        progression_analysis = self.analyze_progression()
        
        # Generate visualization
        visualization_path = self.visualize_progression(
            output_path.replace(".json", ".png")
        )
        
        # Create report
        report = {
            "quantum_id": self.quantum_id,
            "name": self.name,
            "chord_count": len(self.chords),
            "progression_analysis": progression_analysis,
            "visualization_path": visualization_path,
            "chords": [chord.to_dict() for chord in self.chords]
        }
        
        # Save report
        with open(output_path, 'w') as f:
            import json
            json.dump(report, f, indent=2)
        
        logger.info(f"Evolution report generated: {output_path}")
        return report


# Example usage
if __name__ == "__main__":
    # Create a quantum chord progression
    progression = QuantumChordProgression("test_progression")
    
    # Test with a file if provided
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        result = progression.analyze_file(file_path)
        print(f"Analysis result: {result}")
        
        # Generate evolution report
        report = progression.generate_evolution_report()
        print(f"Evolution report: {report}")
    else:
        print("Usage: python quantum_chord_progression_extension.py <file_path>")
