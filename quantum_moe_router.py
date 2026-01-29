"""
quantum_moe_router.py

Mixture of Experts (MoE) router module for the QuantumAI system that dynamically
selects the most appropriate expert for each function analysis task.

This module enables phi-resonant routing of functions to specialized experts,
improving pattern recognition accuracy while maintaining phi-harmonic principles.
"""

import os
import json
import time
import hashlib
import logging
import inspect
from typing import Dict, List, Tuple, Any, Optional, Union

# Import expert interface
from quantum_expert_interface import PhiHarmonicExpert, create_expert

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PhiMoERouter")

class PhiHarmonicRouter:
    """
    Routes functions to the most appropriate expert based on phi-resonance.
    
    This router implements the Mixture of Experts (MoE) architecture, where
    each expert specializes in recognizing specific code patterns with
    phi-resonant confidence levels.
    """
    
    def __init__(self, phi: float = 1.618033988749895, experts: List[PhiHarmonicExpert] = None):
        """
        Initialize the phi-harmonic router.
        
        Args:
            phi: Golden ratio value
            experts: List of pre-initialized experts (optional)
        """
        self.phi = phi
        self.experts = experts or []
        self.routing_history = {}
        self.routing_metrics = {
            "total_routings": 0,
            "successful_routings": 0,
            "phi_coherence": 0.991800  # Starting coherence value
        }
        
        # Initialize default experts if none provided
        if not self.experts:
            self._initialize_default_experts()
        
        logger.info(f"Initialized PhiHarmonicRouter with {len(self.experts)} experts")
    
    def register_expert(self, expert: PhiHarmonicExpert) -> None:
        """
        Register a new expert with the router.
        
        Args:
            expert: PhiHarmonicExpert instance to register
        """
        self.experts.append(expert)
        logger.info(f"Registered {expert.specialization} expert with {expert.resonance_level} resonance")
    
    def select_expert(self, func_code: str, func_name: str) -> Tuple[PhiHarmonicExpert, float]:
        """
        Select the most phi-resonant expert for a function.
        
        Args:
            func_code: Source code of the function
            func_name: Name of the function
            
        Returns:
            Tuple of (selected expert, match score)
            
        Raises:
            ValueError: If no experts are registered
        """
        if not self.experts:
            raise ValueError("No experts registered with the router")
        
        # Calculate match scores for each expert
        match_scores = []
        for expert in self.experts:
            match_score = expert.matches_specialization(func_code, func_name)
            match_scores.append((expert, match_score))
        
        # Select expert with highest match score
        selected_expert, highest_score = max(match_scores, key=lambda x: x[1])
        
        logger.info(f"Selected {selected_expert.specialization} expert with match score {highest_score:.4f}")
        
        return selected_expert, highest_score
    
    def route_function(self, func_code: str, func_name: str) -> Dict[str, Any]:
        """
        Route a function to the selected expert and get analysis results.
        
        Args:
            func_code: Source code of the function
            func_name: Name of the function
            
        Returns:
            Analysis results from the selected expert
        """
        # Select expert
        expert, match_score = self.select_expert(func_code, func_name)
        
        # Analyze function with selected expert
        start_time = time.time()
        analysis_result = expert.analyze_function(func_code, func_name)
        analysis_time = time.time() - start_time
        
        # Calculate phi-resonance of the routing
        routing_resonance = (self.phi * match_score) % 1
        
        # Update routing history
        routing_id = self._generate_routing_id(func_name)
        self.routing_history[routing_id] = {
            "timestamp": time.time(),
            "function_name": func_name,
            "expert_id": expert.quantum_fingerprint,
            "expert_specialization": expert.specialization,
            "match_score": match_score,
            "analysis_time": analysis_time,
            "routing_resonance": routing_resonance
        }
        
        # Update routing metrics
        self._update_routing_metrics(match_score > 0.7)
        
        # Enhance result with routing information
        enhanced_result = {
            **analysis_result,
            "routing_id": routing_id,
            "expert_id": expert.quantum_fingerprint,
            "expert_specialization": expert.specialization,
            "match_score": match_score,
            "routing_resonance": routing_resonance,
            "analysis_time": analysis_time
        }
        
        return enhanced_result
    
    def get_routing_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about the router's performance.
        
        Returns:
            Router statistics
        """
        # Calculate average match score
        if self.routing_history:
            avg_match_score = sum(r["match_score"] for r in self.routing_history.values()) / len(self.routing_history)
            avg_analysis_time = sum(r["analysis_time"] for r in self.routing_history.values()) / len(self.routing_history)
        else:
            avg_match_score = 0.0
            avg_analysis_time = 0.0
        
        # Calculate success rate
        success_rate = 0.0
        if self.routing_metrics["total_routings"] > 0:
            success_rate = self.routing_metrics["successful_routings"] / self.routing_metrics["total_routings"]
        
        return {
            "total_routings": self.routing_metrics["total_routings"],
            "successful_routings": self.routing_metrics["successful_routings"],
            "success_rate": success_rate,
            "avg_match_score": avg_match_score,
            "avg_analysis_time": avg_analysis_time,
            "phi_coherence": self.routing_metrics["phi_coherence"],
            "coherence_quality": self._evaluate_coherence_quality(),
            "expert_count": len(self.experts),
            "expert_specializations": [e.specialization for e in self.experts]
        }
    
    def _initialize_default_experts(self) -> None:
        """Initialize default experts."""
        # Create default experts
        recursive_expert = create_expert("recursive", phi=self.phi)
        functional_expert = create_expert("functional", phi=self.phi)
        
        # Register experts
        self.experts = [recursive_expert, functional_expert]
    
    def _generate_routing_id(self, func_name: str) -> str:
        """
        Generate a unique routing ID.
        
        Args:
            func_name: Function name
            
        Returns:
            Routing ID string
        """
        # Create a unique identifier for this routing
        routing_base = f"{func_name}_{time.time()}"
        
        # Generate hash
        routing_hash = hashlib.sha256(routing_base.encode()).hexdigest()[:16]
        
        return f"route_{routing_hash}"
    
    def _update_routing_metrics(self, success: bool) -> None:
        """
        Update routing metrics.
        
        Args:
            success: Whether the routing was successful
        """
        # Increment counters
        self.routing_metrics["total_routings"] += 1
        if success:
            self.routing_metrics["successful_routings"] += 1
        
        # Update phi coherence
        self._update_phi_coherence(success)
    
    def _update_phi_coherence(self, success: bool) -> None:
        """
        Update phi coherence based on routing success.
        
        Args:
            success: Whether the routing was successful
        """
        # Current coherence
        current_coherence = self.routing_metrics["phi_coherence"]
        
        # Calculate adjustment factor
        adjustment = 0.0001 * (1 if success else -1)
        
        # Apply adjustment
        new_coherence = current_coherence + adjustment
        
        # Ensure coherence stays in valid range (0.9-1.0)
        new_coherence = max(0.9, min(0.999, new_coherence))
        
        # Update stored coherence
        self.routing_metrics["phi_coherence"] = new_coherence
    
    def _evaluate_coherence_quality(self) -> str:
        """
        Evaluate the quality of phi-coherence.
        
        Returns:
            Quality description
        """
        coherence = self.routing_metrics["phi_coherence"]
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


# Module-level functions for direct use

def route_function(func_code: str, func_name: str, phi: float = 1.618033988749895) -> Dict[str, Any]:
    """
    Route a function to the most appropriate expert and get analysis results.
    
    Args:
        func_code: Source code of the function
        func_name: Name of the function
        phi: Golden ratio value
        
    Returns:
        Analysis results from the selected expert
    """
    router = PhiHarmonicRouter(phi=phi)
    return router.route_function(func_code, func_name)


if __name__ == "__main__":
    # Simple test of the module
    router = PhiHarmonicRouter()
    
    # Test functions
    test_recursive = """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
"""
    
    test_functional = """
def process_data(data):
    filtered = [x for x in data if x > 0]
    squared = map(lambda x: x**2, filtered)
    return list(squared)
"""
    
    # Route functions
    recursive_result = router.route_function(test_recursive, "factorial")
    functional_result = router.route_function(test_functional, "process_data")
    
    print(f"Recursive function routing: {recursive_result}")
    print(f"Functional function routing: {functional_result}")
    
    # Get router statistics
    stats = router.get_routing_statistics()
    print(f"Router statistics: {stats}")
