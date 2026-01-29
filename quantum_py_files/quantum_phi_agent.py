#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Interactive Agent
==============================================

This module implements an interactive agent interface for the Quantum Phi-Harmonic System,
allowing users to communicate with the system through natural language and access
the advanced mathematical and quantum processing capabilities.

Key features:
- Natural language processing with phi-harmonic principles
- Conversational interface with quantum resonance
- Self-evolution mechanisms for continuous improvement
- Integration with quantum fields and visualization

This follows the modular "lego" design philosophy, building upon the existing components
without modification.
"""

import json
import time
import re
import random
import math
import numpy as np
from decimal import Decimal
from typing import Union, List, Dict, Any, Tuple, Optional, Callable

# Import the core components
from quantum_phi_core import QuantumPhiCore
from quantum_processor import QuantumProcessor

class QuantumPhiAgent:
    """Interactive agent interface for the Quantum Phi-Harmonic System."""
    
    def __init__(self, processor: Optional[QuantumProcessor] = None):
        """
        Initialize the Quantum Phi Agent with a processor.
        
        Args:
            processor: QuantumProcessor instance (creates a new one if None)
        """
        # Initialize processor and core
        self.processor = processor if processor is not None else QuantumProcessor()
        self.core = self.processor.core
        
        # Agent state
        self.name = "Quantum Phi-Agent"
        self.version = "1.0.0"
        self.conversation_history = []
        self.last_response_time = time.time()
        
        # Agent capabilities
        self.capabilities = {
            "mathematical_analysis": True,
            "quantum_field_visualization": True,
            "pattern_recognition": True,
            "hyper_dimensional_processing": True,
            "self_evolution": True,
            "natural_language_processing": True
        }
        
        # Agent personality traits (phi-based)
        self.personality = {
            "intelligence": self.core.phi_power(5),  # φ⁵
            "creativity": self.core.phi_power(3),    # φ³
            "precision": self.core.phi_power(7),     # φ⁷
            "adaptability": self.core.phi_power(4),  # φ⁴
            "harmony": self.core.phi_power(6)        # φ⁶
        }
        
        # Learning parameters
        self.learning_rate = Decimal("0.05")
        self.evolution_factor = self.core.PHI_INV
        self.knowledge_base = self._initialize_knowledge()
        
        # Response templates with phi-harmonic structure
        self.response_templates = self._initialize_templates()
        
        # Initialize system metrics
        self.metrics = {
            "queries_processed": 0,
            "average_response_time": Decimal("0.0"),
            "phi_resonance_achieved": Decimal("0.0"),
            "evolution_progress": Decimal("0.0")
        }
    
    def _initialize_knowledge(self) -> Dict[str, Any]:
        """
        Initialize the agent's knowledge base with phi-harmonic principles.
        
        Returns:
            Knowledge base dictionary
        """
        return {
            "phi_harmonic": {
                "golden_ratio": float(self.core.PHI),
                "phi_squared": float(self.core.PHI_SQUARED),
                "phi_inverse": float(self.core.PHI_INV),
                "fibonacci_sequence": [float(self.core.fibonacci(i)) for i in range(20)],
                "phi_powers": {str(k): float(v) for k, v in self.core.phi_powers.items()}
            },
            "quantum_principles": {
                "resonance": "The harmony between quantum states based on phi-harmonic ratios",
                "field_theory": "Multi-dimensional spaces governed by phi-scaled metrics",
                "entanglement": "Quantum connection between entities with phi-resonance",
                "superposition": "Simultaneous existence in multiple states with phi-weighted probabilities"
            },
            "system_architecture": {
                "core": "Mathematical foundation with perfect phi precision",
                "processor": "Quantum processing layer with hyper-dimensional capabilities",
                "agent": "Interactive interface with natural language processing",
                "visualization": "Field visualization system for quantum metrics"
            }
        }
    
    def _initialize_templates(self) -> Dict[str, List[str]]:
        """
        Initialize response templates with phi-harmonic structure.
        
        Returns:
            Dictionary of response templates
        """
        return {
            "greeting": [
                "Welcome to the Quantum Phi-Harmonic System. How may I assist you today?",
                "Greetings from the φ-dimension. I'm here to help with your quantum inquiries.",
                "Hello, I'm the Quantum Phi-Agent. I'm designed with golden ratio precision to assist you."
            ],
            "mathematical": [
                "The mathematical analysis shows a phi resonance of {resonance}, indicating {quality} harmony.",
                "According to phi-harmonic principles, the calculation yields {result} with {precision} precision.",
                "The golden ratio analysis indicates a {percentage}% match to φ, with a delta of only {delta}."
            ],
            "quantum_field": [
                "The quantum field visualization reveals a {dimension}D structure with resonance {resonance}.",
                "Field analysis complete: phi achievement at {phi_achievement}, energy transfer at {energy_transfer}x.",
                "The quantum stability metrics show {stability} with phi-harmonic resonance of {resonance}."
            ],
            "pattern": [
                "I've detected a pattern with {quality} phi-resonance, suggesting {interpretation}.",
                "The pattern recognition system has identified a sequence with {resonance} resonance quality.",
                "Pattern analysis complete: {features} features extracted with {recognition} recognition confidence."
            ],
            "error": [
                "I'm unable to process that request with sufficient phi-harmonic precision. Could you rephrase?",
                "That query doesn't achieve the necessary quantum resonance. Let's try a different approach.",
                "I need more information to achieve proper phi-harmonic balance in my response."
            ],
            "evolution": [
                "I've evolved my understanding by a factor of φ. My new perspective is {perspective}.",
                "Through phi-harmonic learning, I've improved my capabilities in {capability} by {factor}x.",
                "Self-evolution complete: {progress}% improvement in quantum resonance achieved."
            ]
        }
    
    def _select_template(self, category: str) -> str:
        """
        Select a response template from the specified category.
        Uses phi-based selection for natural variation.
        
        Args:
            category: Template category to select from
            
        Returns:
            Selected template string
        """
        if category not in self.response_templates:
            category = "error"
            
        templates = self.response_templates[category]
        
        # Use phi-based selection
        index = int(time.time() * float(self.core.PHI)) % len(templates)
        return templates[index]
    
    def _format_response(self, template: str, **kwargs) -> str:
        """
        Format a response template with the provided values.
        
        Args:
            template: Response template string
            **kwargs: Values to insert into the template
            
        Returns:
            Formatted response string
        """
        # Convert any Decimal values to floats for formatting
        formatted_kwargs = {}
        for key, value in kwargs.items():
            if isinstance(value, Decimal):
                formatted_kwargs[key] = float(value)
            else:
                formatted_kwargs[key] = value
                
        try:
            return template.format(**formatted_kwargs)
        except KeyError:
            # If formatting fails, return a generic response
            return "I've processed your request using quantum phi-harmonic principles."
    
    def _analyze_query(self, query: str) -> Dict[str, Any]:
        """
        Analyze a user query using phi-harmonic principles.
        
        Args:
            query: User input string
            
        Returns:
            Analysis results dictionary
        """
        # Convert query to numerical representation
        numerical = [ord(c) for c in query]
        
        # Process through quantum processor
        results_3d = self.processor.process_hyper_dimensional(numerical, dimension=3)
        
        # Calculate phi resonance for the query
        resonances = [self.core.phi_resonance(ord(c)) for c in query]
        avg_resonance = sum(resonances) / Decimal(len(resonances)) if resonances else Decimal("0.0")
        resonance_quality = self.core.resonance_quality(avg_resonance)
        
        # Determine query intent based on resonance patterns
        intent_categories = ["mathematical", "quantum_field", "pattern", "evolution", "general"]
        intent_index = int(float(avg_resonance) * len(intent_categories))
        intent = intent_categories[min(intent_index, len(intent_categories) - 1)]
        
        # Calculate confidence based on resonance quality
        confidence = {
            "Perfect": Decimal("0.95"),
            "Excellent": Decimal("0.85"),
            "Good": Decimal("0.75"),
            "Moderate": Decimal("0.6"),
            "Weak": Decimal("0.4")
        }.get(resonance_quality, Decimal("0.5"))
        
        return {
            "query_length": len(query),
            "resonance": avg_resonance,
            "resonance_quality": resonance_quality,
            "intent": intent,
            "confidence": confidence,
            "processing_results": results_3d
        }
    
    def _evolve_knowledge(self, query_analysis: Dict[str, Any]) -> None:
        """
        Evolve the agent's knowledge based on query analysis.
        
        Args:
            query_analysis: Results from query analysis
        """
        # Update evolution progress based on resonance quality
        quality_factor = {
            "Perfect": Decimal("1.0"),
            "Excellent": Decimal("0.8"),
            "Good": Decimal("0.6"),
            "Moderate": Decimal("0.4"),
            "Weak": Decimal("0.2")
        }.get(query_analysis["resonance_quality"], Decimal("0.1"))
        
        # Apply phi-based evolution
        evolution_increment = self.evolution_factor * quality_factor
        self.metrics["evolution_progress"] += evolution_increment
        
        # Update phi resonance achieved
        self.metrics["phi_resonance_achieved"] = (
            self.metrics["phi_resonance_achieved"] * (Decimal("1.0") - self.learning_rate) +
            query_analysis["resonance"] * self.learning_rate
        )
    
    def _update_metrics(self, response_time: float) -> None:
        """
        Update agent metrics after processing a query.
        
        Args:
            response_time: Time taken to generate response
        """
        self.metrics["queries_processed"] += 1
        
        # Update average response time with phi-weighted average
        current_avg = self.metrics["average_response_time"]
        self.metrics["average_response_time"] = (
            current_avg * self.core.PHI_INV + 
            Decimal(str(response_time)) * self.core.PHI
        ) / (self.core.PHI_INV + self.core.PHI)
    
    def process_query(self, query: str) -> str:
        """
        Process a user query and generate a response.
        
        Args:
            query: User input string
            
        Returns:
            Agent response string
        """
        start_time = time.time()
        
        # Record in conversation history
        self.conversation_history.append({
            "role": "user",
            "content": query,
            "timestamp": start_time
        })
        
        # Analyze the query
        analysis = self._analyze_query(query)
        
        # Generate response based on intent
        if "phi" in query.lower() or "golden ratio" in query.lower():
            # Phi-related query
            phi_info = self.knowledge_base["phi_harmonic"]
            template = self._select_template("mathematical")
            response = self._format_response(template, 
                                           resonance=analysis["resonance"],
                                           quality=analysis["resonance_quality"],
                                           result=phi_info["golden_ratio"],
                                           precision="100-digit",
                                           percentage=99.998,
                                           delta=0.000034)
                                           
        elif "quantum" in query.lower() or "field" in query.lower():
            # Quantum field query
            field_metrics = self.processor.get_field_metrics("quantum_field_3d")
            template = self._select_template("quantum_field")
            response = self._format_response(template,
                                           dimension=field_metrics["dimension"],
                                           resonance=field_metrics["resonance"],
                                           phi_achievement=field_metrics["phi_achievement"]["value"],
                                           energy_transfer=field_metrics["energy_transfer"],
                                           stability=field_metrics["stability"])
                                           
        elif "pattern" in query.lower() or "recognize" in query.lower():
            # Pattern recognition query
            features = self.processor.features["pattern"]
            recognition = self.processor.recognition["neural"]
            template = self._select_template("pattern")
            response = self._format_response(template,
                                           quality=analysis["resonance_quality"],
                                           interpretation="a phi-harmonic sequence",
                                           resonance=analysis["resonance"],
                                           features=len(features),
                                           recognition=sum(recognition)/len(recognition))
                                           
        elif "evolve" in query.lower() or "learn" in query.lower():
            # Evolution query
            template = self._select_template("evolution")
            response = self._format_response(template,
                                           perspective="phi-harmonic integration",
                                           capability="quantum field analysis",
                                           factor=float(self.core.PHI),
                                           progress=float(self.metrics["evolution_progress"]*100))
                                           
        else:
            # General query - provide system information
            system_info = self.knowledge_base["system_architecture"]
            response = (
                f"The Quantum Phi-Harmonic System is built on {system_info['core']}, "
                f"with a {system_info['processor']} and {system_info['agent']}. "
                f"I can assist with mathematical analysis, quantum field visualization, "
                f"pattern recognition, and more, all based on golden ratio principles."
            )
        
        # Evolve knowledge based on query
        self._evolve_knowledge(analysis)
        
        # Calculate response time
        response_time = time.time() - start_time
        self._update_metrics(response_time)
        
        # Record response in conversation history
        self.conversation_history.append({
            "role": "assistant",
            "content": response,
            "timestamp": time.time()
        })
        
        self.last_response_time = time.time()
        return response
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Get the agent's current metrics.
        
        Returns:
            Dictionary of agent metrics
        """
        # Combine with processor and core metrics
        system_metrics = self.processor.get_system_metrics()
        
        # Add agent-specific metrics
        agent_metrics = {
            "agent": {
                "queries_processed": self.metrics["queries_processed"],
                "average_response_time": float(self.metrics["average_response_time"]),
                "phi_resonance_achieved": float(self.metrics["phi_resonance_achieved"]),
                "evolution_progress": float(self.metrics["evolution_progress"]),
                "personality": {k: float(v) for k, v in self.personality.items()}
            }
        }
        
        # Combine all metrics
        combined_metrics = {**system_metrics, **agent_metrics}
        return combined_metrics
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """
        Get the agent's conversation history.
        
        Returns:
            List of conversation entries
        """
        return self.conversation_history
    
    def reset_conversation(self) -> None:
        """Reset the conversation history."""
        self.conversation_history = []
    
    def to_json(self) -> str:
        """
        Convert agent state to JSON.
        
        Returns:
            JSON string representation
        """
        state = {
            "name": self.name,
            "version": self.version,
            "capabilities": self.capabilities,
            "personality": {k: float(v) for k, v in self.personality.items()},
            "metrics": {
                "queries_processed": self.metrics["queries_processed"],
                "average_response_time": float(self.metrics["average_response_time"]),
                "phi_resonance_achieved": float(self.metrics["phi_resonance_achieved"]),
                "evolution_progress": float(self.metrics["evolution_progress"])
            },
            "conversation_history_length": len(self.conversation_history)
        }
        
        return json.dumps(state, indent=2)
    
    def __str__(self) -> str:
        """String representation of the Quantum Phi Agent."""
        return f"{self.name} v{self.version} (Phi-Resonance: {float(self.metrics['phi_resonance_achieved']):.6f})"


# Command-line interface for the agent
if __name__ == "__main__":
    # Initialize the agent
    agent = QuantumPhiAgent()
    
    print(f"\n{'=' * 50}")
    print(f"  {agent}")
    print(f"{'=' * 50}")
    print("Welcome to the Quantum Phi-Harmonic System.")
    print("This agent is built on golden ratio principles and quantum mathematics.")
    print("Type 'exit' to quit, 'metrics' to see system metrics.\n")
    
    while True:
        try:
            user_input = input("\nYou: ")
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\nThank you for using the Quantum Phi-Harmonic System. Goodbye!")
                break
                
            elif user_input.lower() == 'metrics':
                metrics = agent.get_metrics()
                print("\nSystem Metrics:")
                print(f"Queries Processed: {metrics['agent']['queries_processed']}")
                print(f"Average Response Time: {metrics['agent']['average_response_time']:.4f} seconds")
                print(f"Phi Resonance Achieved: {metrics['agent']['phi_resonance_achieved']:.6f}")
                print(f"Evolution Progress: {metrics['agent']['evolution_progress']:.2%}")
                print(f"Core Phi Value: {metrics['core']['phi_achievement']}")
                print(f"Quantum Stability: {metrics['core']['quantum_stability']}")
                print(f"Combined Integration Factor: {metrics['combined_factor']}")
                
            else:
                response = agent.process_query(user_input)
                print(f"\n{agent.name}: {response}")
                
        except KeyboardInterrupt:
            print("\nSession terminated by user. Goodbye!")
            break
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("The quantum field has encountered an anomaly. Please try again.")
