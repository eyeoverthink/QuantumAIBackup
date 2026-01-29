#!/usr/bin/env python3
"""
Quantum Orchestrator Chord Progression Extension
-----------------------------------------------

This module extends the QuantumAI orchestrator with chord progression analysis
capabilities to guide the healing and evolution process based on phi-harmonic
coherence patterns.

The extension follows the modular "lego" architecture principle by providing
a non-invasive wrapper around the orchestrator's healing methods that adds
chord progression analysis before and after healing.

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
from typing import Dict, List, Tuple, Optional, Any, Callable
from datetime import datetime
import functools

# Import quantum chord progression
from quantum_chord_progression import (
    ParallelChordAnalyzer,
    QuantumChord,
    ChordProgression,
    PHI,
    PHI_POWERS
)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumOrchestratorChordExtension")

class QuantumOrchestratorChordExtension:
    """
    Extends the QuantumAI orchestrator with chord progression analysis capabilities.
    
    This class wraps the orchestrator's healing methods to add chord progression
    analysis before and after healing, guiding the evolution process based on
    phi-harmonic coherence patterns.
    """
    
    def __init__(self, orchestrator):
        """
        Initialize the extension with a reference to the orchestrator.
        
        Args:
            orchestrator: The QuantumOrchestrator instance to extend
        """
        self.orchestrator = orchestrator
        self.analyzer = ParallelChordAnalyzer()
        self.chord_progression = ChordProgression("healing_progression")
        self.chord_progression.create_target_from_phi()
        
        # Create evolution history directory if it doesn't exist
        self.evolution_dir = "evolution_history"
        os.makedirs(self.evolution_dir, exist_ok=True)
        
        # Load existing progression if available
        self.progression_path = os.path.join(self.evolution_dir, "healing_progression.json")
        if os.path.exists(self.progression_path):
            try:
                self.chord_progression = ChordProgression.load_from_file(self.progression_path)
                logger.info(f"Loaded existing chord progression from {self.progression_path}")
            except Exception as e:
                logger.warning(f"Failed to load chord progression from {self.progression_path}: {e}")
                logger.info("Creating new chord progression")
                self.chord_progression = ChordProgression("healing_progression")
                self.chord_progression.create_target_from_phi()
        
        # Patch orchestrator methods
        self._patch_orchestrator_methods()
        
        logger.info("QuantumOrchestratorChordExtension initialized")
        
    def _patch_orchestrator_methods(self):
        """Patch the orchestrator's healing methods with chord progression analysis."""
        # Patch the _heal_file method if it exists
        if hasattr(self.orchestrator, '_heal_file'):
            original_heal_file = self.orchestrator._heal_file
            
            @functools.wraps(original_heal_file)
            def wrapped_heal_file(file_path, *args, **kwargs):
                # Analyze file before healing
                before_analysis = self._analyze_file(file_path)
                before_chord = None
                if before_analysis and 'chord' in before_analysis:
                    before_chord = QuantumChord.from_dict(before_analysis['chord'])
                
                # Call original method
                result = original_heal_file(file_path, *args, **kwargs)
                
                # Analyze file after healing
                after_analysis = self._analyze_file(file_path)
                after_chord = None
                if after_analysis and 'chord' in after_analysis:
                    after_chord = QuantumChord.from_dict(after_analysis['chord'])
                
                # Record healing event
                if before_chord and after_chord:
                    self._record_healing_event(file_path, before_chord, after_chord)
                    
                    # Add to chord progression
                    self.chord_progression.add_chord(after_chord)
                    self.chord_progression.save_to_file(self.progression_path)
                    
                    # Check if optimization is needed
                    if after_chord.target_distance > 0.2:  # If far from target
                        self._optimize_file_resonance(file_path, after_chord)
                
                return result
                
            # Replace the original method
            self.orchestrator._heal_file = wrapped_heal_file
            logger.info("Patched orchestrator._heal_file method")
        
        # Patch the _heal_unclosed_paren method
        original_heal_unclosed_paren = self.orchestrator._heal_unclosed_paren
        
        @functools.wraps(original_heal_unclosed_paren)
        def wrapped_heal_unclosed_paren(self_orchestrator):
            # Analyze file before healing
            file_path = self.orchestrator.target_file
            before_analysis = self._analyze_file(file_path)
            before_chord = None
            if before_analysis and 'chord' in before_analysis:
                before_chord = QuantumChord.from_dict(before_analysis['chord'])
            
            # Call original method with only self argument
            result = original_heal_unclosed_paren(self_orchestrator)
            
            # Analyze file after healing
            after_analysis = self._analyze_file(file_path)
            after_chord = None
            if after_analysis and 'chord' in after_analysis:
                after_chord = QuantumChord.from_dict(after_analysis['chord'])
            
            # Record healing event
            if before_chord and after_chord and result:  # Only record if healing was successful
                self._record_healing_event(file_path, before_chord, after_chord)
                
                # Add to chord progression
                self.chord_progression.add_chord(after_chord)
                self.chord_progression.save_to_file(self.progression_path)
                
                # Check if optimization is needed
                if after_chord.target_distance > 0.2:  # If far from target
                    self._optimize_file_resonance(file_path, after_chord)
            
            return result
            
        # Replace the original method
        self.orchestrator._heal_unclosed_paren = wrapped_heal_unclosed_paren
        logger.info("Patched orchestrator._heal_unclosed_paren method")
        
        # Patch other healing methods as needed
        # ...
        
    def _analyze_file(self, file_path: str) -> Dict[str, Any]:
        """
        Analyze a file using the chord progression analyzer.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        try:
            return self.analyzer._analyze_single_file(file_path)
        except Exception as e:
            logger.error(f"Error analyzing file {file_path}: {e}")
            return None
            
    def _record_healing_event(self, file_path: str, before_chord: QuantumChord, after_chord: QuantumChord):
        """
        Record a healing event in the evolution history.
        
        Args:
            file_path: Path to the healed file
            before_chord: QuantumChord before healing
            after_chord: QuantumChord after healing
        """
        # Create event data
        event = {
            "timestamp": time.time(),
            "file_path": file_path,
            "before_chord": before_chord.to_dict(),
            "after_chord": after_chord.to_dict(),
            "coherence_improvement": after_chord.scalar_coherence - before_chord.scalar_coherence,
            "phi_resonance_improvement": after_chord.phi_resonance - before_chord.phi_resonance,
            "target_distance_improvement": before_chord.target_distance - after_chord.target_distance
        }
        
        # Save event to file
        event_file = os.path.join(
            self.evolution_dir,
            f"healing_event_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        )
        with open(event_file, 'w') as f:
            json.dump(event, f, indent=2)
            
        logger.info(f"Recorded healing event: {event_file}")
        
        # Update orchestrator's healing knowledge base if available
        if hasattr(self.orchestrator, 'healing_knowledge') and isinstance(self.orchestrator.healing_knowledge, dict):
            file_name = os.path.basename(file_path)
            if file_name not in self.orchestrator.healing_knowledge:
                self.orchestrator.healing_knowledge[file_name] = []
                
            self.orchestrator.healing_knowledge[file_name].append({
                "timestamp": time.time(),
                "coherence_before": before_chord.scalar_coherence,
                "coherence_after": after_chord.scalar_coherence,
                "phi_resonance_before": before_chord.phi_resonance,
                "phi_resonance_after": after_chord.phi_resonance,
                "target_distance_before": before_chord.target_distance,
                "target_distance_after": after_chord.target_distance
            })
            
            # Save knowledge base
            if hasattr(self.orchestrator, '_save_knowledge_base'):
                self.orchestrator._save_knowledge_base()
                
    def _optimize_file_resonance(self, file_path: str, chord: QuantumChord):
        """
        Optimize a file's resonance based on chord progression analysis.
        
        Args:
            file_path: Path to the file to optimize
            chord: Current QuantumChord of the file
        """
        logger.info(f"Optimizing resonance for {file_path}")
        
        try:
            # Read file content
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Find optimal chord in progression
            optimal_chord = None
            if self.chord_progression.chords:
                optimal_chord = min(self.chord_progression.chords, key=lambda x: x.target_distance)
                
            if not optimal_chord or optimal_chord.target_distance >= chord.target_distance:
                logger.info("No better chord found in progression, skipping optimization")
                return
                
            # Apply resonance optimization
            # This is a simple example - in a real implementation, you would use more
            # sophisticated techniques based on the chord progression analysis
            
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
                    new_chord = QuantumChord.from_dict(new_analysis['chord'])
                    self.chord_progression.add_chord(new_chord)
                    self.chord_progression.save_to_file(self.progression_path)
                    
                    logger.info(f"New phi-resonance: {new_chord.phi_resonance:.6f}, " +
                               f"Target distance: {new_chord.target_distance:.6f}")
        except Exception as e:
            logger.error(f"Error optimizing resonance for {file_path}: {e}")
            
    def analyze_evolution_history(self) -> Dict[str, Any]:
        """
        Analyze the evolution history to identify patterns and trends.
        
        Returns:
            Dictionary containing analysis results
        """
        # Analyze chord progression
        progression_analysis = self.chord_progression.analyze_progression()
        
        # Load healing events
        events = []
        for filename in os.listdir(self.evolution_dir):
            if filename.startswith('healing_event_') and filename.endswith('.json'):
                try:
                    with open(os.path.join(self.evolution_dir, filename), 'r') as f:
                        event = json.load(f)
                        events.append(event)
                except Exception as e:
                    logger.error(f"Error loading healing event {filename}: {e}")
                    
        # Sort events by timestamp
        events.sort(key=lambda x: x.get('timestamp', 0))
        
        # Calculate metrics
        total_coherence_improvement = sum(event.get('coherence_improvement', 0) for event in events)
        total_phi_resonance_improvement = sum(event.get('phi_resonance_improvement', 0) for event in events)
        total_target_distance_improvement = sum(event.get('target_distance_improvement', 0) for event in events)
        
        # Compile analysis
        analysis = {
            "progression_analysis": progression_analysis,
            "total_healing_events": len(events),
            "total_coherence_improvement": total_coherence_improvement,
            "total_phi_resonance_improvement": total_phi_resonance_improvement,
            "total_target_distance_improvement": total_target_distance_improvement,
            "average_coherence_improvement": total_coherence_improvement / len(events) if events else 0,
            "average_phi_resonance_improvement": total_phi_resonance_improvement / len(events) if events else 0,
            "average_target_distance_improvement": total_target_distance_improvement / len(events) if events else 0
        }
        
        return analysis
        
    def visualize_evolution_history(self, output_path: str = None) -> str:
        """
        Visualize the evolution history.
        
        Args:
            output_path: Path to save the visualization
            
        Returns:
            Path to the saved visualization
        """
        if not output_path:
            output_path = os.path.join(self.evolution_dir, f"evolution_history_{int(time.time())}.png")
            
        # Visualize chord progression
        return self.chord_progression.visualize_progression(output_path)
        
    def get_optimal_evolution_path(self, directory_path: str = None) -> Dict[str, Any]:
        """
        Find the optimal evolution path for a directory.
        
        Args:
            directory_path: Path to the directory to analyze (default: current directory)
            
        Returns:
            Dictionary containing optimal evolution path
        """
        if not directory_path:
            directory_path = os.getcwd()
            
        # Find Python files
        python_files = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))
                    
        # Limit to 20 files for performance
        python_files = python_files[:20]
        
        # Analyze files in parallel
        results = self.analyzer.analyze_files_in_parallel(python_files)
        
        # Find optimal evolution path
        return self.analyzer.find_optimal_evolution_path(results)


# Example usage
if __name__ == "__main__":
    # This is just an example - in practice, you would import the orchestrator
    # and create an extension instance
    
    # Mock orchestrator for testing
    class MockOrchestrator:
        def __init__(self):
            self.target_file = "example.py"
            self.healing_knowledge = {}
            
        def _heal_unclosed_paren(self):
            print("Mock healing unclosed parenthesis")
            return True
            
        def _save_knowledge_base(self):
            print("Mock saving knowledge base")
            
    # Create extension
    orchestrator = MockOrchestrator()
    extension = QuantumOrchestratorChordExtension(orchestrator)
    
    # Test patched method
    orchestrator._heal_unclosed_paren()
    
    print("Extension test complete")
