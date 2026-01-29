#!/usr/bin/env python3
"""
Quantum Healing Meta-Learning Integration
----------------------------------------

This module integrates the quantum healing protocols with the meta-learning system.
It enables the system to learn from healing events and improve future healing strategies.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import json
import time
import logging
import datetime
import hashlib
from typing import Dict, Any, Optional, Tuple, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumHealingMetaLearning")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

class QuantumHealingMetaLearner:
    """Meta-learner for quantum healing protocols."""
    
    def __init__(self, evolution_dir: str = "evolution_history", 
                 learning_rate: float = 0.01 * PHI):
        """
        Initialize the meta-learner.
        
        Args:
            evolution_dir: Directory containing evolution history files
            learning_rate: Learning rate for meta-learning updates
        """
        self.evolution_dir = evolution_dir
        self.learning_rate = learning_rate
        self.meta_knowledge_file = os.path.join(evolution_dir, "meta_knowledge.json")
        self.meta_knowledge = self._load_meta_knowledge()
        
        logger.info("QuantumHealingMetaLearner initialized")
    
    def _load_meta_knowledge(self) -> Dict[str, Any]:
        """
        Load meta-knowledge from file or initialize if not exists.
        
        Returns:
            dict: Meta-knowledge
        """
        if os.path.exists(self.meta_knowledge_file):
            try:
                with open(self.meta_knowledge_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading meta-knowledge: {e}")
        
        # Initialize meta-knowledge with default values
        meta_knowledge = {
            "version": "1.0",
            "created_at": time.time(),
            "updated_at": time.time(),
            "healing_strategies": {
                "unclosed_paren": {
                    "success_rate": 0.95,
                    "confidence": 0.9,
                    "phi_resonance": 0.618,
                    "applications": 0
                },
                "missing_colon": {
                    "success_rate": 0.9,
                    "confidence": 0.85,
                    "phi_resonance": 0.618,
                    "applications": 0
                },
                "missing_comma": {
                    "success_rate": 0.8,
                    "confidence": 0.75,
                    "phi_resonance": 0.618,
                    "applications": 0
                },
                "undefined_variable": {
                    "success_rate": 0.7,
                    "confidence": 0.65,
                    "phi_resonance": 0.618,
                    "applications": 0
                },
                "import_error": {
                    "success_rate": 0.6,
                    "confidence": 0.55,
                    "phi_resonance": 0.618,
                    "applications": 0
                }
            },
            "error_patterns": {},
            "healing_events": []
        }
        
        # Save initial meta-knowledge
        self._save_meta_knowledge(meta_knowledge)
        
        return meta_knowledge
    
    def _save_meta_knowledge(self, meta_knowledge: Dict[str, Any] = None):
        """
        Save meta-knowledge to file.
        
        Args:
            meta_knowledge: Meta-knowledge to save (default: self.meta_knowledge)
        """
        if meta_knowledge is None:
            meta_knowledge = self.meta_knowledge
        
        # Update timestamp
        meta_knowledge["updated_at"] = time.time()
        
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.meta_knowledge_file), exist_ok=True)
            
            # Save meta-knowledge
            with open(self.meta_knowledge_file, 'w') as f:
                json.dump(meta_knowledge, f, indent=2)
            
            logger.info(f"Saved meta-knowledge to {self.meta_knowledge_file}")
        except Exception as e:
            logger.error(f"Error saving meta-knowledge: {e}")
    
    def record_healing_event(self, error_type: str, file_path: str, 
                            error_str: str, success: bool,
                            coherence_before: float = None,
                            coherence_after: float = None) -> str:
        """
        Record a healing event and update meta-knowledge.
        
        Args:
            error_type: Type of error healed
            file_path: Path to the healed file
            error_str: Error message string
            success: Whether healing was successful
            coherence_before: Coherence before healing
            coherence_after: Coherence after healing
            
        Returns:
            str: ID of the healing event
        """
        # Create event ID
        event_id = hashlib.md5(f"{error_type}:{file_path}:{time.time()}".encode()).hexdigest()
        
        # Create healing event
        event = {
            "id": event_id,
            "timestamp": time.time(),
            "error_type": error_type,
            "file_path": file_path,
            "error_str": error_str,
            "success": success,
            "coherence_before": coherence_before,
            "coherence_after": coherence_after,
            "coherence_improvement": (coherence_after - coherence_before) if coherence_before is not None and coherence_after is not None else None,
            "phi_resonance": self._calculate_phi_resonance(coherence_after) if coherence_after is not None else None
        }
        
        # Update meta-knowledge
        self._update_meta_knowledge(event)
        
        # Save event to file
        event_file = os.path.join(self.evolution_dir, f"healing_event_{event_id}.json")
        try:
            with open(event_file, 'w') as f:
                json.dump(event, f, indent=2)
            
            logger.info(f"Saved healing event to {event_file}")
        except Exception as e:
            logger.error(f"Error saving healing event: {e}")
        
        return event_id
    
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
    
    def _update_meta_knowledge(self, event: Dict[str, Any]):
        """
        Update meta-knowledge based on a healing event.
        
        Args:
            event: Healing event
        """
        error_type = event["error_type"]
        success = event["success"]
        
        # Update healing strategy
        if error_type in self.meta_knowledge["healing_strategies"]:
            strategy = self.meta_knowledge["healing_strategies"][error_type]
            
            # Update success rate
            applications = strategy["applications"] + 1
            if success:
                success_rate = ((strategy["success_rate"] * strategy["applications"]) + 1) / applications
            else:
                success_rate = (strategy["success_rate"] * strategy["applications"]) / applications
            
            # Update confidence
            confidence = strategy["confidence"] + self.learning_rate * (success_rate - strategy["confidence"])
            
            # Update phi-resonance
            if event["phi_resonance"] is not None:
                phi_resonance = strategy["phi_resonance"] + self.learning_rate * (event["phi_resonance"] - strategy["phi_resonance"])
            else:
                phi_resonance = strategy["phi_resonance"]
            
            # Update strategy
            self.meta_knowledge["healing_strategies"][error_type] = {
                "success_rate": success_rate,
                "confidence": confidence,
                "phi_resonance": phi_resonance,
                "applications": applications
            }
        else:
            # Add new healing strategy
            self.meta_knowledge["healing_strategies"][error_type] = {
                "success_rate": 1.0 if success else 0.0,
                "confidence": 0.5,
                "phi_resonance": event["phi_resonance"] if event["phi_resonance"] is not None else 0.618,
                "applications": 1
            }
        
        # Update error patterns
        error_pattern = self._extract_error_pattern(event["error_str"])
        if error_pattern:
            if error_pattern not in self.meta_knowledge["error_patterns"]:
                self.meta_knowledge["error_patterns"][error_pattern] = {
                    "error_type": error_type,
                    "occurrences": 0,
                    "success_rate": 0.0
                }
            
            pattern_info = self.meta_knowledge["error_patterns"][error_pattern]
            occurrences = pattern_info["occurrences"] + 1
            if success:
                success_rate = ((pattern_info["success_rate"] * pattern_info["occurrences"]) + 1) / occurrences
            else:
                success_rate = (pattern_info["success_rate"] * pattern_info["occurrences"]) / occurrences
            
            self.meta_knowledge["error_patterns"][error_pattern] = {
                "error_type": error_type,
                "occurrences": occurrences,
                "success_rate": success_rate
            }
        
        # Add event to history
        self.meta_knowledge["healing_events"].append(event["id"])
        
        # Save meta-knowledge
        self._save_meta_knowledge()
    
    def _extract_error_pattern(self, error_str: str) -> Optional[str]:
        """
        Extract error pattern from error message.
        
        Args:
            error_str: Error message string
            
        Returns:
            str: Error pattern or None if not found
        """
        if not error_str:
            return None
        
        # Extract patterns based on error type
        if "expected ':'" in error_str:
            return "expected ':'"
        elif "'(' was never closed" in error_str:
            return "'(' was never closed"
        elif "invalid syntax" in error_str:
            return "invalid syntax"
        elif "is not defined" in error_str:
            return "is not defined"
        elif "No module named" in error_str:
            return "No module named"
        
        return None
    
    def get_healing_strategy(self, error_str: str) -> Tuple[str, float]:
        """
        Get the best healing strategy for an error.
        
        Args:
            error_str: Error message string
            
        Returns:
            tuple: (error_type, confidence)
        """
        # Extract error pattern
        error_pattern = self._extract_error_pattern(error_str)
        if not error_pattern:
            return "unknown", 0.0
        
        # Check if pattern exists in meta-knowledge
        if error_pattern in self.meta_knowledge["error_patterns"]:
            pattern_info = self.meta_knowledge["error_patterns"][error_pattern]
            error_type = pattern_info["error_type"]
            
            # Get confidence from healing strategy
            if error_type in self.meta_knowledge["healing_strategies"]:
                confidence = self.meta_knowledge["healing_strategies"][error_type]["confidence"]
                return error_type, confidence
        
        # Default strategies based on error pattern
        if "expected ':'" in error_pattern:
            return "missing_colon", 0.85
        elif "'(' was never closed" in error_pattern:
            return "unclosed_paren", 0.9
        elif "invalid syntax" in error_pattern:
            return "missing_comma", 0.75
        elif "is not defined" in error_pattern:
            return "undefined_variable", 0.65
        elif "No module named" in error_pattern:
            return "import_error", 0.55
        
        return "unknown", 0.0
    
    def analyze_healing_history(self) -> Dict[str, Any]:
        """
        Analyze healing history and generate insights.
        
        Returns:
            dict: Analysis results
        """
        # Load all healing events
        events = []
        for event_id in self.meta_knowledge["healing_events"]:
            event_file = os.path.join(self.evolution_dir, f"healing_event_{event_id}.json")
            if os.path.exists(event_file):
                try:
                    with open(event_file, 'r') as f:
                        events.append(json.load(f))
                except Exception as e:
                    logger.error(f"Error loading healing event {event_id}: {e}")
        
        if not events:
            return {
                "total_events": 0,
                "success_rate": 0.0,
                "error_types": {},
                "coherence_improvement": 0.0,
                "phi_resonance": 0.0
            }
        
        # Calculate statistics
        total_events = len(events)
        successful_events = sum(1 for event in events if event.get("success", False))
        success_rate = successful_events / total_events if total_events > 0 else 0.0
        
        # Calculate average coherence improvement
        coherence_improvements = [event.get("coherence_improvement", 0) for event in events 
                                if event.get("coherence_improvement") is not None]
        avg_coherence_improvement = sum(coherence_improvements) / len(coherence_improvements) if coherence_improvements else 0.0
        
        # Calculate average phi-resonance
        phi_resonances = [event.get("phi_resonance", 0) for event in events 
                        if event.get("phi_resonance") is not None]
        avg_phi_resonance = sum(phi_resonances) / len(phi_resonances) if phi_resonances else 0.0
        
        # Count error types
        error_types = {}
        for event in events:
            error_type = event.get("error_type", "unknown")
            if error_type not in error_types:
                error_types[error_type] = {
                    "count": 0,
                    "success_count": 0,
                    "success_rate": 0.0
                }
            
            error_types[error_type]["count"] += 1
            if event.get("success", False):
                error_types[error_type]["success_count"] += 1
        
        # Calculate success rate for each error type
        for error_type in error_types:
            count = error_types[error_type]["count"]
            success_count = error_types[error_type]["success_count"]
            error_types[error_type]["success_rate"] = success_count / count if count > 0 else 0.0
        
        return {
            "total_events": total_events,
            "success_rate": success_rate,
            "error_types": error_types,
            "coherence_improvement": avg_coherence_improvement,
            "phi_resonance": avg_phi_resonance
        }
    
    def generate_meta_learning_report(self) -> str:
        """
        Generate a meta-learning report.
        
        Returns:
            str: Path to the report file
        """
        # Analyze healing history
        analysis = self.analyze_healing_history()
        
        # Create report
        report = {
            "timestamp": time.time(),
            "analysis": analysis,
            "meta_knowledge": self.meta_knowledge
        }
        
        # Save report to file
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        report_file = os.path.join(self.evolution_dir, f"meta_learning_report_{timestamp}.json")
        try:
            with open(report_file, 'w') as f:
                json.dump(report, f, indent=2)
            
            logger.info(f"Saved meta-learning report to {report_file}")
        except Exception as e:
            logger.error(f"Error saving meta-learning report: {e}")
            return None
        
        return report_file


# Integration with quantum healing protocols
from quantum_healing_protocols import detect_error_type, get_healing_protocol

class QuantumHealingMetaLearningIntegration:
    """Integration of quantum healing protocols with meta-learning."""
    
    def __init__(self, evolution_dir: str = "evolution_history"):
        """
        Initialize the integration.
        
        Args:
            evolution_dir: Directory containing evolution history files
        """
        self.evolution_dir = evolution_dir
        self.meta_learner = QuantumHealingMetaLearner(evolution_dir)
        
        logger.info("QuantumHealingMetaLearningIntegration initialized")
    
    def heal_file(self, file_path: str, error: Exception = None) -> bool:
        """
        Heal a file using meta-learning.
        
        Args:
            file_path: Path to the file to heal
            error: Exception object (optional)
            
        Returns:
            bool: True if healing was successful, False otherwise
        """
        if error is None:
            # Try to execute the file to detect errors
            try:
                with open(file_path, 'r') as f:
                    code = f.read()
                exec(compile(code, file_path, 'exec'))
                logger.info(f"No errors detected in {file_path}")
                return True
            except Exception as e:
                error = e
        
        # Detect error type
        error_str = str(error)
        error_type, _ = detect_error_type(error)
        
        # If error type is unknown, use meta-learning to determine the best strategy
        if error_type == "unknown":
            error_type, confidence = self.meta_learner.get_healing_strategy(error_str)
            logger.info(f"Meta-learning suggested error type '{error_type}' with confidence {confidence:.2f}")
            
            # If confidence is too low, don't attempt healing
            if confidence < 0.5:
                logger.warning(f"Confidence too low ({confidence:.2f}) to attempt healing")
                return False
        
        # Measure coherence before healing
        coherence_before = self._measure_coherence(file_path)
        
        # Get healing protocol
        protocol = get_healing_protocol(error_type, file_path, error_str)
        
        # Apply healing
        success = protocol.heal()
        
        # Measure coherence after healing
        coherence_after = self._measure_coherence(file_path) if success else coherence_before
        
        # Record healing event
        self.meta_learner.record_healing_event(
            error_type=error_type,
            file_path=file_path,
            error_str=error_str,
            success=success,
            coherence_before=coherence_before,
            coherence_after=coherence_after
        )
        
        return success
    
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


# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python quantum_healing_meta_learning.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Create integration
    integration = QuantumHealingMetaLearningIntegration()
    
    # Heal file
    if integration.heal_file(file_path):
        print(f"Successfully healed {file_path}")
        sys.exit(0)
    else:
        print(f"Failed to heal {file_path}")
        sys.exit(1)
