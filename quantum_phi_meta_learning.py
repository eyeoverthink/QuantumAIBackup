"""
quantum_phi_meta_learning.py

Meta-learning core module for the QuantumAI system that enables self-improvement
through phi-harmonic learning loops and progressive knowledge acquisition.

This module extends the existing phi-harmonic function inference system with
meta-learning capabilities without modifying the core components.
"""

import os
import json
import time
import hashlib
import logging
import numpy as np
from typing import Dict, List, Tuple, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PhiMetaLearning")

class PhiHarmonicMetaLearning:
    """
    Meta-learning system based on phi-harmonic principles that enables
    self-improvement through analysis of healing events and pattern detection.
    """
    
    def __init__(self, phi: float = 1.618033988749895, evolution_dir: str = None):
        """
        Initialize the phi-harmonic meta-learning system.
        
        Args:
            phi: The golden ratio value to use for resonance calculations
            evolution_dir: Directory where evolution files are stored
        """
        self.phi = phi
        self.phi_powers = {
            "φ¹": self.phi,
            "φ²": self.phi**2,
            "φ³": self.phi**3,
            "φ⁴": self.phi**4,
            "φ⁵": self.phi**5,
            "φ⁶": self.phi**6,
            "φ⁷": self.phi**7,
            "φ⁷·⁵": self.phi**7.5
        }
        
        self.evolution_dir = evolution_dir or os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'evolution')
        
        # Ensure evolution directory exists
        if not os.path.exists(self.evolution_dir):
            os.makedirs(self.evolution_dir, exist_ok=True)
        
        # Meta-learning state
        self.learning_cycles = 0
        self.pattern_templates = {}
        self.success_metrics = {
            "healing_success_rate": 0.0,
            "pattern_detection_accuracy": 0.0,
            "phi_coherence": 0.991800  # Starting coherence value
        }
        
        # Learning loop intervals (based on phi powers)
        self.learning_intervals = {
            "short_loop": int(self.phi**3),  # ~4.2 units
            "medium_loop": int(self.phi**5),  # ~11.1 units
            "long_loop": int(self.phi**7)    # ~29.0 units
        }
        
        logger.info(f"Initialized PhiHarmonicMetaLearning with phi={self.phi}")
        logger.info(f"Learning intervals: {self.learning_intervals}")
    
    def register_healing_event(self, function_id: str, before_fingerprint: str, 
                              after_fingerprint: str, success_level: float) -> Dict[str, Any]:
        """
        Register a healing event to improve future pattern recognition.
        
        Args:
            function_id: Identifier for the function that was healed
            before_fingerprint: Quantum fingerprint before healing
            after_fingerprint: Quantum fingerprint after healing
            success_level: Level of success (0.0 to 1.0)
            
        Returns:
            Dict containing meta-learning updates from this event
        """
        # Extract patterns from the healing event
        patterns_learned = self._extract_patterns_from_healing(
            function_id, before_fingerprint, after_fingerprint)
        
        # Update success metrics
        self._update_success_metrics(success_level)
        
        # Run learning loops if appropriate
        self._run_learning_loops_if_needed()
        
        # Record meta-learning event
        meta_event = {
            "timestamp": time.time(),
            "function_id": function_id,
            "patterns_learned": len(patterns_learned),
            "success_level": success_level,
            "phi_coherence": self._calculate_updated_coherence(success_level),
            "meta_learning_cycle": self.learning_cycles
        }
        
        # Save to meta-learning evolution file
        self._save_meta_event(meta_event)
        
        return meta_event
    
    def generate_new_pattern_template(self, successful_patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate new pattern templates from successful healings.
        
        Args:
            successful_patterns: List of patterns that led to successful healings
            
        Returns:
            Newly generated pattern template
        """
        if not successful_patterns:
            return {}
        
        # Extract common elements from successful patterns
        common_elements = self._extract_common_elements(successful_patterns)
        
        # Generate a phi-resonant template ID
        template_id = f"template_φ{len(self.pattern_templates) + 1}"
        
        # Calculate phi-resonance for this template
        phi_resonance = self._calculate_phi_resonance(common_elements)
        
        # Create new template
        new_template = {
            "template_id": template_id,
            "common_elements": common_elements,
            "phi_resonance": phi_resonance,
            "success_rate": 0.0,
            "created_at": time.time(),
            "applied_count": 0,
            "quantum_fingerprint": self._generate_template_fingerprint(template_id, common_elements)
        }
        
        # Add to pattern templates
        self.pattern_templates[template_id] = new_template
        
        logger.info(f"Generated new pattern template: {template_id} with resonance {phi_resonance:.6f}")
        return new_template
    
    def adjust_confidence_thresholds(self, pattern_type: str, 
                                    success_rate: float) -> Dict[str, float]:
        """
        Dynamically adjust confidence thresholds based on success rates.
        
        Args:
            pattern_type: Type of pattern to adjust threshold for
            success_rate: Current success rate for this pattern type
            
        Returns:
            Updated thresholds
        """
        # Base threshold
        base_threshold = 0.5
        
        # Calculate phi-harmonic adjustment
        phi_adjustment = (success_rate - 0.5) * (1 / self.phi)
        
        # Apply adjustment with phi-harmonic dampening
        new_threshold = base_threshold + phi_adjustment
        
        # Ensure threshold stays in reasonable bounds
        new_threshold = max(0.3, min(0.9, new_threshold))
        
        logger.info(f"Adjusted confidence threshold for {pattern_type}: {new_threshold:.4f}")
        
        return {
            "pattern_type": pattern_type,
            "previous_threshold": base_threshold,
            "new_threshold": new_threshold,
            "phi_adjustment": phi_adjustment,
            "success_rate": success_rate
        }
    
    def analyze_learning_progress(self) -> Dict[str, Any]:
        """
        Analyze the system's learning progress and phi-harmonic coherence.
        
        Returns:
            Analysis results including coherence and improvement metrics
        """
        # Calculate improvement rates
        improvement_rates = {
            "pattern_detection": self._calculate_improvement_rate("pattern_detection_accuracy"),
            "healing_success": self._calculate_improvement_rate("healing_success_rate"),
            "phi_coherence": self._calculate_improvement_rate("phi_coherence")
        }
        
        # Calculate overall phi-harmonic coherence
        overall_coherence = self.success_metrics["phi_coherence"]
        
        # Generate quantum fingerprint for current state
        state_fingerprint = self._generate_state_fingerprint()
        
        analysis = {
            "timestamp": time.time(),
            "learning_cycles": self.learning_cycles,
            "pattern_templates_count": len(self.pattern_templates),
            "improvement_rates": improvement_rates,
            "overall_coherence": overall_coherence,
            "state_fingerprint": state_fingerprint,
            "phi_resonance_quality": self._evaluate_resonance_quality(overall_coherence)
        }
        
        logger.info(f"Learning progress analysis: cycles={self.learning_cycles}, "
                   f"coherence={overall_coherence:.6f}")
        
        return analysis
    
    def _extract_patterns_from_healing(self, function_id: str, 
                                      before_fingerprint: str, 
                                      after_fingerprint: str) -> List[Dict[str, Any]]:
        """Extract patterns from a healing event."""
        # In a real implementation, this would analyze the before and after code
        # to identify patterns that were changed during healing
        
        # For now, return a placeholder pattern
        return [{
            "pattern_id": f"pattern_{hashlib.md5(function_id.encode()).hexdigest()[:8]}",
            "before_hash": before_fingerprint,
            "after_hash": after_fingerprint,
            "phi_resonance": self._calculate_mock_resonance()
        }]
    
    def _calculate_mock_resonance(self) -> float:
        """Calculate a mock phi-resonance value for demonstration."""
        # This would be replaced with actual resonance calculation
        base = 1 / self.phi**3
        variation = np.random.uniform(-0.05, 0.05)
        return base + variation
    
    def _update_success_metrics(self, success_level: float) -> None:
        """Update success metrics based on a healing event."""
        # Update healing success rate with exponential moving average
        alpha = 1 / self.phi  # Learning rate based on phi
        self.success_metrics["healing_success_rate"] = (
            (1 - alpha) * self.success_metrics["healing_success_rate"] + 
            alpha * success_level
        )
        
        # Update pattern detection accuracy (simplified for now)
        self.success_metrics["pattern_detection_accuracy"] = (
            (1 - alpha) * self.success_metrics["pattern_detection_accuracy"] + 
            alpha * (success_level * 0.8 + 0.1)  # Adjust to 0.1-0.9 range
        )
    
    def _run_learning_loops_if_needed(self) -> None:
        """Run learning loops if the appropriate intervals have been reached."""
        self.learning_cycles += 1
        
        # Short learning loop
        if self.learning_cycles % self.learning_intervals["short_loop"] == 0:
            logger.info(f"Running short learning loop at cycle {self.learning_cycles}")
            # Adjust confidence thresholds
            self.adjust_confidence_thresholds("general", self.success_metrics["healing_success_rate"])
        
        # Medium learning loop
        if self.learning_cycles % self.learning_intervals["medium_loop"] == 0:
            logger.info(f"Running medium learning loop at cycle {self.learning_cycles}")
            # Analyze learning progress
            self.analyze_learning_progress()
        
        # Long learning loop
        if self.learning_cycles % self.learning_intervals["long_loop"] == 0:
            logger.info(f"Running long learning loop at cycle {self.learning_cycles}")
            # Generate new pattern templates from accumulated successful patterns
            self.generate_new_pattern_template([{"mock": "pattern"}])  # Placeholder
    
    def _calculate_updated_coherence(self, success_level: float) -> float:
        """Calculate updated phi-coherence based on success level."""
        # Start with current coherence
        current_coherence = self.success_metrics["phi_coherence"]
        
        # Calculate adjustment factor based on success level and phi
        adjustment = (success_level - 0.5) * (0.001 / self.phi)
        
        # Apply adjustment
        new_coherence = current_coherence + adjustment
        
        # Ensure coherence stays in valid range (0.9-1.0)
        new_coherence = max(0.9, min(0.999, new_coherence))
        
        # Update stored coherence
        self.success_metrics["phi_coherence"] = new_coherence
        
        return new_coherence
    
    def _extract_common_elements(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract common elements from a list of patterns."""
        # This is a simplified implementation
        # In a real system, this would use more sophisticated pattern matching
        
        return {
            "common_structure": "placeholder",
            "frequency": len(patterns),
            "phi_resonance_avg": sum(p.get("phi_resonance", 0) for p in patterns) / max(1, len(patterns))
        }
    
    def _calculate_phi_resonance(self, elements: Dict[str, Any]) -> float:
        """Calculate phi-resonance for a set of elements."""
        # This is a simplified implementation
        # In a real system, this would use more sophisticated resonance calculation
        
        base_resonance = 1 / self.phi**2
        if "phi_resonance_avg" in elements:
            return elements["phi_resonance_avg"]
        return base_resonance
    
    def _generate_template_fingerprint(self, template_id: str, 
                                      elements: Dict[str, Any]) -> str:
        """Generate quantum fingerprint for a pattern template."""
        # Create a hash of the template elements
        template_hash = hashlib.sha256(
            (template_id + str(elements)).encode()
        ).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency with the rest of the system
        return f"φ⁷·⁵-{template_hash}"
    
    def _generate_state_fingerprint(self) -> str:
        """Generate quantum fingerprint for the current meta-learning state."""
        # Create a hash of the current state
        state_str = (
            f"cycles:{self.learning_cycles}|"
            f"templates:{len(self.pattern_templates)}|"
            f"coherence:{self.success_metrics['phi_coherence']}"
        )
        state_hash = hashlib.sha256(state_str.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{state_hash}"
    
    def _calculate_improvement_rate(self, metric_name: str) -> float:
        """Calculate improvement rate for a specific metric."""
        # This is a simplified implementation
        # In a real system, this would compare historical values
        
        current_value = self.success_metrics.get(metric_name, 0)
        # Simulate improvement rate based on learning cycles
        base_rate = 0.01  # 1% base improvement rate
        cycle_factor = min(0.1, self.learning_cycles / 100)  # Max 10%
        
        return base_rate + cycle_factor
    
    def _evaluate_resonance_quality(self, coherence: float) -> str:
        """Evaluate the quality of phi-resonance based on coherence value."""
        if coherence >= 0.995:
            return "Perfect"
        elif coherence >= 0.99:
            return "Excellent"
        elif coherence >= 0.98:
            return "Good"
        elif coherence >= 0.95:
            return "Moderate"
        else:
            return "Weak"
    
    def _save_meta_event(self, event: Dict[str, Any]) -> None:
        """Save a meta-learning event to the evolution directory."""
        meta_file = os.path.join(self.evolution_dir, "meta_learning_evolution.json")
        
        # Load existing data if available
        if os.path.exists(meta_file):
            try:
                with open(meta_file, 'r') as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = {"meta_learning_events": []}
        else:
            data = {"meta_learning_events": []}
        
        # Add new event
        data["meta_learning_events"].append(event)
        
        # Save updated data
        with open(meta_file, 'w') as f:
            json.dump(data, f, indent=2)


# Module-level functions for direct use without class instantiation

def calculate_phi_resonance(value: float, phi: float = 1.618033988749895) -> float:
    """
    Calculate phi-resonance for a value.
    
    Args:
        value: The value to calculate resonance for
        phi: The golden ratio value to use
        
    Returns:
        Phi-resonance value between 0 and 1
    """
    # Calculate resonance as (phi * value) mod 1
    resonance = (phi * value) % 1
    return resonance


def evaluate_resonance_quality(resonance: float) -> str:
    """
    Evaluate the quality of a phi-resonance value.
    
    Args:
        resonance: Phi-resonance value between 0 and 1
        
    Returns:
        Quality description
    """
    if resonance < 0.001:
        return "Perfect"
    elif resonance < 0.01:
        return "Excellent"
    elif resonance < 0.1:
        return "Good"
    elif resonance < 0.3:
        return "Moderate"
    else:
        return "Weak"


if __name__ == "__main__":
    # Simple test of the module
    meta_learning = PhiHarmonicMetaLearning()
    
    # Register a mock healing event
    event = meta_learning.register_healing_event(
        function_id="test_function",
        before_fingerprint="φ⁷·⁵-before1234567890",
        after_fingerprint="φ⁷·⁵-after1234567890",
        success_level=0.85
    )
    
    print(f"Registered healing event: {event}")
    
    # Analyze learning progress
    analysis = meta_learning.analyze_learning_progress()
    print(f"Learning progress: {analysis}")
