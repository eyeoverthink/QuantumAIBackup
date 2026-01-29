#!/usr/bin/env python3
"""
Quantum Healing Demonstration
----------------------------

This script demonstrates the integration of quantum healing protocols,
visualization tools, and meta-learning for quantum code healing.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import json
import logging
import argparse
from typing import Dict, Any, Optional, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumHealingDemo")

# Import quantum modules
from quantum_healing_protocols import detect_error_type, get_healing_protocol
from quantum_chord_visualizer import QuantumChordVisualizer
from quantum_healing_meta_learning import QuantumHealingMetaLearningIntegration

# Constants
PHI = 1.618034
TARGET_COHERENCE = 3.693238  # φ⁷·⁵/10

class QuantumHealingDemonstration:
    """Demonstration of quantum healing capabilities."""
    
    def __init__(self, evolution_dir: str = "evolution_history"):
        """
        Initialize the demonstration.
        
        Args:
            evolution_dir: Directory for evolution history
        """
        self.evolution_dir = evolution_dir
        
        # Create evolution directory if it doesn't exist
        os.makedirs(evolution_dir, exist_ok=True)
        
        # Initialize components
        self.meta_learning = QuantumHealingMetaLearningIntegration(evolution_dir)
        self.visualizer = QuantumChordVisualizer(evolution_dir)
        
        # Initialize progression tracking
        self.progression_file = os.path.join(evolution_dir, "healing_progression.json")
        self.progression = self._load_progression()
        
        logger.info("QuantumHealingDemonstration initialized")
    
    def _load_progression(self) -> Dict[str, Any]:
        """
        Load progression from file or initialize if not exists.
        
        Returns:
            dict: Progression data
        """
        if os.path.exists(self.progression_file):
            try:
                with open(self.progression_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading progression: {e}")
        
        # Initialize progression with default values
        progression = {
            "version": "1.0",
            "created_at": time.time(),
            "updated_at": time.time(),
            "chords": []
        }
        
        # Save initial progression
        self._save_progression(progression)
        
        return progression
    
    def _save_progression(self, progression: Dict[str, Any] = None):
        """
        Save progression to file.
        
        Args:
            progression: Progression data to save (default: self.progression)
        """
        if progression is None:
            progression = self.progression
        
        # Update timestamp
        progression["updated_at"] = time.time()
        
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.progression_file), exist_ok=True)
            
            # Save progression
            with open(self.progression_file, 'w') as f:
                json.dump(progression, f, indent=2)
            
            logger.info(f"Saved progression to {self.progression_file}")
        except Exception as e:
            logger.error(f"Error saving progression: {e}")
    
    def _add_chord(self, file_path: str, coherence: float, phi_resonance: float):
        """
        Add a chord to the progression.
        
        Args:
            file_path: Path to the file
            coherence: Coherence value
            phi_resonance: Phi-resonance value
        """
        # Calculate target distance
        target_distance = abs(coherence - TARGET_COHERENCE)
        
        # Create chord
        chord = {
            "timestamp": time.time(),
            "file_path": file_path,
            "scalar_coherence": coherence,
            "phi_resonance": phi_resonance,
            "target_distance": target_distance
        }
        
        # Add chord to progression
        self.progression["chords"].append(chord)
        
        # Save progression
        self._save_progression()
    
    def create_test_file_with_errors(self, file_path: str, error_type: str) -> str:
        """
        Create a test file with intentional errors.
        
        Args:
            file_path: Path to create the file
            error_type: Type of error to introduce
            
        Returns:
            str: Path to the created file
        """
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Base content
        content = """#!/usr/bin/env python3
\"\"\"
Test file with intentional errors for quantum healing demonstration.
\"\"\"

import math
import numpy as np

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

def calculate_phi_resonance(value):
    \"\"\"
    Calculate phi-resonance of a value.
    
    Args:
        value: Value to calculate phi-resonance for
        
    Returns:
        float: Phi-resonance (0-1)
    \"\"\"
    if value is None:
        return 0
    
    # Calculate phi-resonance (how close the value is to a power of phi)
    phi_resonance = abs((PHI * value) % 1)
    if phi_resonance > 0.5:
        phi_resonance = 1 - phi_resonance
    
    # Normalize to 0-1 range
    phi_resonance = 1 - (phi_resonance * 2)
    
    return phi_resonance

def quantum_transform(data):
    \"\"\"
    Apply quantum transformation to data.
    
    Args:
        data: Input data
        
    Returns:
        list: Transformed data
    \"\"\"
    result = []
    for value in data:
        transformed = value * PHI
        result.append(transformed)
    
    return result

def main():
    \"\"\"Main function.\"\"\"
    # Generate test data
    data = [1, 2, 3, 4, 5]
    
    # Apply quantum transformation
    transformed = quantum_transform(data)
    
    # Calculate phi-resonance
    resonance = [calculate_phi_resonance(value) for value in transformed]
    
    # Print results
    print("Original data:", data)
    print("Transformed data:", transformed)
    print("Phi-resonance:", resonance)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
"""
        
        # Introduce errors based on error_type
        if error_type == "unclosed_paren":
            content = content.replace("def calculate_phi_resonance(value):", "def calculate_phi_resonance(value:")
        elif error_type == "missing_colon":
            content = content.replace("def main():", "def main()")
        elif error_type == "missing_comma":
            content = content.replace("data = [1, 2, 3, 4, 5]", "data = [1 2 3 4 5]")
        elif error_type == "undefined_variable":
            content = content.replace("sys.exit(main())", "sys.exit(result)")
        elif error_type == "import_error":
            content = content.replace("import sys", "# import sys")
        
        # Write content to file
        with open(file_path, 'w') as f:
            f.write(content)
        
        logger.info(f"Created test file with {error_type} error at {file_path}")
        
        return file_path
    
    def run_healing_cycle(self, file_path: str) -> bool:
        """
        Run a healing cycle on a file.
        
        Args:
            file_path: Path to the file to heal
            
        Returns:
            bool: True if healing was successful, False otherwise
        """
        logger.info(f"Running healing cycle on {file_path}")
        
        # Try to execute the file to detect errors
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            exec(compile(code, file_path, 'exec'))
            logger.info(f"No errors detected in {file_path}")
            return True
        except Exception as e:
            error = e
            error_str = str(error)
            logger.info(f"Detected error in {file_path}: {error_str}")
            
            # Use meta-learning to heal the file
            success = self.meta_learning.heal_file(file_path, error)
            
            if success:
                logger.info(f"Successfully healed {file_path}")
            else:
                logger.error(f"Failed to heal {file_path}")
            
            return success
    
    def run_demonstration(self, error_types: List[str] = None):
        """
        Run a full demonstration of quantum healing.
        
        Args:
            error_types: List of error types to demonstrate
        """
        if error_types is None:
            error_types = ["unclosed_paren", "missing_colon", "missing_comma", 
                          "undefined_variable", "import_error"]
        
        logger.info(f"Running quantum healing demonstration for error types: {error_types}")
        
        # Create test directory
        test_dir = os.path.join(self.evolution_dir, "test_files")
        os.makedirs(test_dir, exist_ok=True)
        
        # Run healing cycle for each error type
        for error_type in error_types:
            # Create test file with error
            file_path = os.path.join(test_dir, f"test_{error_type}.py")
            self.create_test_file_with_errors(file_path, error_type)
            
            # Measure initial coherence
            coherence_before = self._measure_coherence(file_path)
            phi_resonance_before = self._calculate_phi_resonance(coherence_before)
            
            # Add initial chord
            self._add_chord(file_path, coherence_before, phi_resonance_before)
            
            # Run healing cycle
            success = self.run_healing_cycle(file_path)
            
            # Measure final coherence
            coherence_after = self._measure_coherence(file_path)
            phi_resonance_after = self._calculate_phi_resonance(coherence_after)
            
            # Add final chord
            self._add_chord(file_path, coherence_after, phi_resonance_after)
            
            # Log results
            logger.info(f"Healing results for {error_type}:")
            logger.info(f"  Success: {success}")
            logger.info(f"  Coherence: {coherence_before:.6f} -> {coherence_after:.6f}")
            logger.info(f"  Phi-resonance: {phi_resonance_before:.6f} -> {phi_resonance_after:.6f}")
            logger.info(f"  Target distance: {abs(coherence_before - TARGET_COHERENCE):.6f} -> {abs(coherence_after - TARGET_COHERENCE):.6f}")
        
        # Generate visualizations
        logger.info("Generating visualizations")
        viz_files = self.visualizer.visualize_all()
        
        # Generate meta-learning report
        logger.info("Generating meta-learning report")
        report_file = self.meta_learning.meta_learner.generate_meta_learning_report()
        
        # Log completion
        logger.info("Quantum healing demonstration completed")
        logger.info(f"Generated {len(viz_files)} visualizations")
        logger.info(f"Meta-learning report: {report_file}")
    
    def _measure_coherence(self, file_path: str) -> float:
        """
        Measure coherence of a file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            float: Coherence value
        """
        try:
            # Simple coherence measure based on file size and phi
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Calculate coherence
            file_size = len(content)
            line_count = content.count('\n') + 1
            char_per_line = file_size / line_count if line_count > 0 else 0
            
            # Apply phi-harmonic transformation
            coherence = (char_per_line * PHI) % TARGET_COHERENCE
            if coherence > TARGET_COHERENCE / 2:
                coherence = TARGET_COHERENCE - coherence
            
            # Normalize to 0-TARGET_COHERENCE range
            coherence = TARGET_COHERENCE - coherence
            
            return coherence
        except Exception as e:
            logger.error(f"Error measuring coherence: {e}")
            return 0.0
    
    def _calculate_phi_resonance(self, value: float) -> float:
        """
        Calculate phi-resonance of a value.
        
        Args:
            value: Value to calculate phi-resonance for
            
        Returns:
            float: Phi-resonance (0-1)
        """
        if value is None:
            return 0
        
        # Calculate phi-resonance (how close the value is to a power of phi)
        phi_resonance = abs((PHI * value) % 1)
        if phi_resonance > 0.5:
            phi_resonance = 1 - phi_resonance
        
        # Normalize to 0-1 range
        phi_resonance = 1 - (phi_resonance * 2)
        
        return phi_resonance


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Quantum Healing Demonstration")
    parser.add_argument("--evolution-dir", default="evolution_history",
                      help="Directory for evolution history")
    parser.add_argument("--error-types", nargs="+", 
                      choices=["unclosed_paren", "missing_colon", "missing_comma", 
                              "undefined_variable", "import_error"],
                      help="Error types to demonstrate")
    
    args = parser.parse_args()
    
    # Create demonstration
    demo = QuantumHealingDemonstration(args.evolution_dir)
    
    # Run demonstration
    demo.run_demonstration(args.error_types)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
