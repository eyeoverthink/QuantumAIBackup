#!/usr/bin/env python3
"""
Quantum Orchestrator Healing Chord Extension
-------------------------------------------

This module extends the QuantumAI orchestrator with chord progression analysis
capabilities for healing protocols. It provides a non-invasive wrapper around
the orchestrator that adds chord progression analysis before and after healing.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 0.991800
"""

import os
import sys
import json
import time
import logging
import importlib
from typing import Dict, List, Tuple, Optional, Any, Callable
from datetime import datetime

# Import quantum chord progression
try:
    from quantum_chord_progression import (
        ParallelChordAnalyzer,
        QuantumChord,
        ChordProgression,
        PHI,
        PHI_POWERS
    )
except ImportError:
    # Define fallback constants if module not available
    PHI = 1.618034
    PHI_POWERS = {
        "φ": 1.618034,
        "φ²": 2.618034,
        "φ³": 4.236068,
        "φ⁷·⁵": 36.932381
    }

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumOrchestratorHealingChordExtension")

class QuantumOrchestratorHealingChordExtension:
    """
    Extends the QuantumAI orchestrator with chord progression analysis for healing protocols.
    
    This class provides a non-invasive wrapper around the orchestrator that adds
    chord progression analysis before and after healing.
    """
    
    def __init__(self, target_file: str):
        """
        Initialize the extension with a target file.
        
        Args:
            target_file: Path to the target file to heal
        """
        self.target_file = target_file
        self.last_error_str = ""  # Store last error message for healing protocols
        
        # Initialize chord progression analyzer
        try:
            self.analyzer = ParallelChordAnalyzer()
            self.chord_progression = ChordProgression("healing_progression")
            self.chord_progression.create_target_from_phi()
        except NameError:
            logger.warning("ParallelChordAnalyzer not available, using limited functionality")
            self.analyzer = None
            self.chord_progression = None
        
        # Create evolution history directory if it doesn't exist
        self.evolution_dir = "evolution_history"
        os.makedirs(self.evolution_dir, exist_ok=True)
        
        # Load existing progression if available
        self.progression_path = os.path.join(self.evolution_dir, "healing_progression.json")
        if self.chord_progression and os.path.exists(self.progression_path):
            try:
                self.chord_progression = ChordProgression.load_from_file(self.progression_path)
            except Exception as e:
                logger.warning(f"Could not load existing chord progression: {e}")
                # Keep the default progression created earlier
        
        logger.info("QuantumOrchestratorHealingChordExtension initialized")
    
    def heal_unclosed_paren(self) -> bool:
        """
        Heal unclosed parenthesis in the target file with chord progression analysis.
        
        Returns:
            bool: True if healing was successful, False otherwise
        """
        logger.info("Executing protocol: heal_unclosed_paren")
        
        # Analyze file before healing
        before_analysis = self._analyze_file(self.target_file)
        before_chord = None
        if before_analysis and 'chord' in before_analysis:
            before_chord = QuantumChord.from_dict(before_analysis['chord'])
        
        # Perform healing
        result = False
        try:
            with open(self.target_file, 'r') as f:
                lines = f.readlines()
            
            for i, line in enumerate(lines):
                open_paren = 0
                in_string = False
                string_char = ''
                
                for char in line:
                    if (char == '"' or char == "'") and not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char and in_string:
                        in_string = False
                        string_char = ''
                    
                    if not in_string:
                        if char == '(':
                            open_paren += 1
                        elif char == ')':
                            open_paren -= 1
                
                if open_paren > 0:
                    lines[i] = line.rstrip() + ')\n'
                    with open(self.target_file, 'w') as f:
                        f.writelines(lines)
                    logger.info(f"Applied healing (parenthesis) to line {i+1}.")
                    result = True
                    break
        
        except Exception as e:
            logger.error(f"Error in heal_unclosed_paren: {e}")
            return False
        
        # Analyze file after healing
        if result:
            after_analysis = self._analyze_file(self.target_file)
            after_chord = None
            if after_analysis and 'chord' in after_analysis:
                after_chord = QuantumChord.from_dict(after_analysis['chord'])
            
            # Record healing event
            if before_chord and after_chord:
                self._record_healing_event(self.target_file, before_chord, after_chord)
                
                # Add to chord progression
                if self.chord_progression:
                    self.chord_progression.add_chord(after_chord)
                    self.chord_progression.save_to_file(self.progression_path)
                
                # Check if optimization is needed
                if after_chord.target_distance > 0.2:  # If far from target
                    self._optimize_file_resonance(self.target_file, after_chord)
        
        return result
    
    def _analyze_file(self, file_path: str) -> Dict[str, Any]:
        """
        Analyze a file using the chord progression analyzer.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        try:
            if self.analyzer:
                return self.analyzer._analyze_single_file(file_path)
            else:
                # Fallback analysis if analyzer not available
                return self._fallback_analyze_file(file_path)
        except Exception as e:
            logger.error(f"Error analyzing file {file_path}: {e}")
            return None
    
    def _fallback_analyze_file(self, file_path: str) -> Dict[str, Any]:
        """
        Fallback analysis if chord progression analyzer not available.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            Dictionary containing basic analysis results
        """
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Extract quantum values
            coherence = 0.75  # Default
            phi_resonance = 0.618034  # Default (φ⁻¹)
            
            # Look for coherence value
            import re
            coherence_match = re.search(r'coherence\s*=\s*(0\.\d+)', content)
            if coherence_match:
                coherence = float(coherence_match.group(1))
            
            # Create basic chord
            chord = {
                "scalar_coherence": coherence,
                "phi_resonance": phi_resonance,
                "target_distance": abs(0.991800 - coherence)  # Distance to φ⁷·⁵/10
            }
            
            return {
                "file_path": file_path,
                "chord": chord
            }
        except Exception as e:
            logger.error(f"Error in fallback analysis for {file_path}: {e}")
            return None
    
    def _record_healing_event(self, file_path: str, before_chord: Any, after_chord: Any):
        """
        Record a healing event in the evolution history.
        
        Args:
            file_path: Path to the healed file
            before_chord: Chord before healing
            after_chord: Chord after healing
        """
        # Helper function to convert numpy types to Python native types
        def convert_numpy_types(obj):
            import numpy as np
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, np.bool_):
                return bool(obj)
            elif isinstance(obj, dict):
                return {k: convert_numpy_types(v) for k, v in obj.items()}
            elif isinstance(obj, (list, tuple)):
                return [convert_numpy_types(i) for i in obj]
            else:
                return obj
        
        # Create event data
        coherence_improvement = 0
        phi_resonance_improvement = 0
        target_distance_improvement = 0
        
        # Safely extract values
        if hasattr(after_chord, 'scalar_coherence') and hasattr(before_chord, 'scalar_coherence'):
            coherence_improvement = float(after_chord.scalar_coherence) - float(before_chord.scalar_coherence)
        
        if hasattr(after_chord, 'phi_resonance') and hasattr(before_chord, 'phi_resonance'):
            phi_resonance_improvement = float(after_chord.phi_resonance) - float(before_chord.phi_resonance)
        
        if hasattr(after_chord, 'target_distance') and hasattr(before_chord, 'target_distance'):
            target_distance_improvement = float(before_chord.target_distance) - float(after_chord.target_distance)
        
        # Convert chord objects to serializable dictionaries
        before_chord_dict = before_chord.to_dict() if hasattr(before_chord, 'to_dict') else before_chord
        after_chord_dict = after_chord.to_dict() if hasattr(after_chord, 'to_dict') else after_chord
        
        # Create event data with converted values
        event = {
            "timestamp": time.time(),
            "file_path": file_path,
            "before_chord": convert_numpy_types(before_chord_dict),
            "after_chord": convert_numpy_types(after_chord_dict),
            "coherence_improvement": coherence_improvement,
            "phi_resonance_improvement": phi_resonance_improvement,
            "target_distance_improvement": target_distance_improvement
        }
        
        # Save event to file
        event_file = os.path.join(
            self.evolution_dir,
            f"healing_event_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        )
        try:
            with open(event_file, 'w') as f:
                json.dump(event, f, indent=2)
            logger.info(f"Recorded healing event: {event_file}")
        except TypeError as e:
            logger.error(f"JSON serialization error: {e}")
            # Fallback to simpler event data if serialization fails
            simple_event = {
                "timestamp": time.time(),
                "file_path": file_path,
                "healing_successful": True
            }
            with open(event_file, 'w') as f:
                json.dump(simple_event, f, indent=2)
            logger.info(f"Recorded simplified healing event: {event_file}")
    
    def _optimize_file_resonance(self, file_path: str, chord: Any):
        """
        Optimize a file's resonance based on chord progression analysis.
        
        Args:
            file_path: Path to the file to optimize
            chord: Current chord of the file
        """
        logger.info(f"Optimizing resonance for {file_path}")
        
        try:
            # Read file content
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Add phi-harmonic constants if they don't exist
            phi_comment = f"# Phi-harmonic constants: φ = {PHI}, φ² = {PHI_POWERS['φ²']}, φ³ = {PHI_POWERS['φ³']}"
            if phi_comment not in content:
                lines = content.split('\n')
                # Find a good place to insert (after imports)
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') or line.startswith('from '):
                        insert_pos = i + 1
                
                # Insert phi constants
                lines.insert(insert_pos, "")
                lines.insert(insert_pos + 1, phi_comment)
                lines.insert(insert_pos + 2, f"PHI = {PHI}  # Golden ratio")
                lines.insert(insert_pos + 3, f"PHI_SQUARED = {PHI_POWERS['φ²']}  # φ²")
                lines.insert(insert_pos + 4, f"PHI_CUBED = {PHI_POWERS['φ³']}  # φ³")
                lines.insert(insert_pos + 5, f"TARGET_COHERENCE = {PHI_POWERS['φ⁷·⁵']/10}  # φ⁷·⁵/10")
                lines.insert(insert_pos + 6, "")
                
                # Write back to file
                with open(file_path, 'w') as f:
                    f.write('\n'.join(lines))
                    
                logger.info(f"Applied resonance optimization to {file_path}")
                
                # Re-analyze file
                new_analysis = self._analyze_file(file_path)
                if new_analysis and 'chord' in new_analysis:
                    new_chord = QuantumChord.from_dict(new_analysis['chord']) if self.analyzer else new_analysis['chord']
                    
                    if self.chord_progression:
                        self.chord_progression.add_chord(new_chord)
                        self.chord_progression.save_to_file(self.progression_path)
                    
                    target_distance = new_chord.target_distance if hasattr(new_chord, 'target_distance') else 0
                    phi_resonance = new_chord.phi_resonance if hasattr(new_chord, 'phi_resonance') else 0
                    
                    logger.info(f"New phi-resonance: {phi_resonance:.6f}, " +
                               f"Target distance: {target_distance:.6f}")
        except Exception as e:
            logger.error(f"Error optimizing resonance for {file_path}: {e}")
    
    def heal_missing_colon(self) -> bool:
        """
        Heal missing colon in function or class definition.
        
        Returns:
            bool: True if healing was successful, False otherwise
        """
        logger.info("Executing protocol: heal_missing_colon")
        
        # Analyze file before healing
        before_analysis = self._analyze_file(self.target_file)
        before_chord = None
        if before_analysis and 'chord' in before_analysis:
            before_chord = QuantumChord.from_dict(before_analysis['chord']) if self.analyzer else before_analysis['chord']
        
        # Perform healing
        result = False
        try:
            # Find line number from error message
            import re
            line_match = re.search(r'line (\d+)', self.last_error_str)
            if not line_match:
                return False
                
            line_num = int(line_match.group(1)) - 1  # Convert to 0-indexed
            
            with open(self.target_file, 'r') as f:
                lines = f.readlines()
                
            if line_num < len(lines):
                # Check if line is a function or class definition without colon
                if re.search(r'\b(def|class)\s+\w+\s*\([^)]*\)\s*$', lines[line_num].strip()):
                    lines[line_num] = lines[line_num].rstrip() + ':\n'
                    with open(self.target_file, 'w') as f:
                        f.writelines(lines)
                    logger.info(f"Added missing colon to line {line_num+1}.")
                    result = True
        
        except Exception as e:
            logger.error(f"Error in heal_missing_colon: {e}")
            return False
        
        # Analyze file after healing
        if result:
            after_analysis = self._analyze_file(self.target_file)
            after_chord = None
            if after_analysis and 'chord' in after_analysis:
                after_chord = QuantumChord.from_dict(after_analysis['chord']) if self.analyzer else after_analysis['chord']
            
            # Record healing event
            if before_chord and after_chord:
                self._record_healing_event(self.target_file, before_chord, after_chord)
                
                # Add to chord progression
                if self.chord_progression:
                    self.chord_progression.add_chord(after_chord)
                    self.chord_progression.save_to_file(self.progression_path)
        
        return result
        
    def run_and_heal(self, max_attempts=5):
        """
        Run and heal the target file with chord progression analysis.
        
        Args:
            max_attempts: Maximum number of healing attempts
            
        Returns:
            bool: True if healing was successful, False otherwise
        """
        logger.info(f"Running and healing {self.target_file}")
        
        for attempt in range(1, max_attempts + 1):
            logger.info(f"Healing attempt {attempt}/{max_attempts}")
            
            # Try to run the file
            try:
                # Import the file as a module
                module_name = os.path.basename(self.target_file).replace('.py', '')
                spec = importlib.util.spec_from_file_location(module_name, self.target_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                logger.info(f"✅ File ran successfully on attempt {attempt}!")
                return True
            
            except SyntaxError as e:
                logger.info(f"SyntaxError: {e}")
                self.last_error_str = str(e)
                
                # Check for unclosed parenthesis
                if "'(' was never closed" in str(e):
                    if self.heal_unclosed_paren():
                        logger.info("Healed unclosed parenthesis")
                        continue
                
                # Check for missing colon
                if "expected ':'" in str(e):
                    if self.heal_missing_colon():
                        logger.info("Healed missing colon")
                        continue
                
                # Add more healing protocols as needed
                
                logger.error(f"Failed to heal file after {attempt} attempts")
            
            except Exception as e:
                logger.error(f"Error running file: {e}")
        
        return False


# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python quantum_orchestrator_healing_chord_extension.py <target_file>")
        sys.exit(1)
    
    target_file = sys.argv[1]
    
    # Initialize extension
    extension = QuantumOrchestratorHealingChordExtension(target_file)
    
    # Run and heal
    if extension.run_and_heal():
        print(f"Successfully healed {target_file}")
        sys.exit(0)
    else:
        print(f"Failed to heal {target_file}")
        sys.exit(1)
