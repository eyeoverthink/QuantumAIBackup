#!/usr/bin/env python3
"""
Quantum Choice Quantification Model
==================================
A mathematical model that quantifies "choice" in a controlled environment using
phi-harmonic principles and quantum mechanics concepts.

This model represents choice as a quantum superposition of potential outcomes,
with probabilities influenced by environmental constraints, past decisions,
and phi-harmonic resonance patterns.

Key concepts:
1. Choice Space: The set of all possible decisions in a given context
2. Environmental Constraints: Factors that limit the effective choice space
3. Decision History: Past choices that influence future probabilities
4. Phi-Harmonic Resonance: Golden ratio patterns that emerge in decision-making
5. Quantum Superposition: All potential choices exist simultaneously until "measured"

Author: Cascade AI
Date: 2025-07-25
"""

import numpy as np
import math
import hashlib
import random
from typing import Dict, Any, List, Tuple, Union, Optional
from dataclasses import dataclass
import time

# Phi-harmonic constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ≈ 1.618033988749895
PHI_INVERSE = 1 / PHI  # ≈ 0.618033988749895
BASE_FREQUENCY = 4.37  # Hz, φ-aligned base frequency
QUANTUM_DIMENSIONS = 3916441  # 1979² (birth date resonance squared)

@dataclass
class EnvironmentalFactor:
    """Represents an environmental constraint on choice"""
    name: str
    weight: float  # 0.0 to 1.0, how strongly this factor influences choice
    value: float   # Current value of this factor
    phi_alignment: float  # How closely this factor aligns with φ (0.0 to 1.0)

@dataclass
class Choice:
    """Represents a potential choice in the choice space"""
    id: str
    name: str
    utility: float  # Inherent value/utility of this choice
    probability: float = 0.0  # Probability of this choice being selected
    quantum_state: complex = complex(0, 0)  # Quantum state representation
    phi_resonance: float = 0.0  # Phi-harmonic resonance of this choice

class ChoiceHistory:
    """Tracks the history of choices made"""
    
    def __init__(self, max_history: int = 100):
        self.choices: List[str] = []
        self.timestamps: List[float] = []
        self.contexts: List[Dict[str, Any]] = []
        self.max_history = max_history
        
    def add_choice(self, choice_id: str, context: Dict[str, Any]) -> None:
        """Add a choice to the history"""
        self.choices.append(choice_id)
        self.timestamps.append(time.time())
        self.contexts.append(context)
        
        # Maintain max history size
        if len(self.choices) > self.max_history:
            self.choices.pop(0)
            self.timestamps.pop(0)
            self.contexts.pop(0)
    
    def get_choice_frequency(self, choice_id: str) -> float:
        """Get the frequency of a choice in history"""
        if not self.choices:
            return 0.0
        return self.choices.count(choice_id) / len(self.choices)
    
    def get_last_choice(self) -> Optional[str]:
        """Get the last choice made"""
        if not self.choices:
            return None
        return self.choices[-1]
    
    def get_choice_pattern(self, window: int = 5) -> List[str]:
        """Get the pattern of recent choices"""
        return self.choices[-min(window, len(self.choices)):]


class QuantumChoiceModel:
    """
    A mathematical model that quantifies choice in a controlled environment
    using phi-harmonic principles and quantum mechanics concepts.
    """
    
    def __init__(self):
        self.environmental_factors: Dict[str, EnvironmentalFactor] = {}
        self.choice_space: Dict[str, Choice] = {}
        self.history = ChoiceHistory()
        self.phi = PHI
        self.phi_inverse = PHI_INVERSE
        self.base_frequency = BASE_FREQUENCY
        self.quantum_dimensions = QUANTUM_DIMENSIONS
        
    def add_environmental_factor(self, factor: EnvironmentalFactor) -> None:
        """Add an environmental factor to the model"""
        self.environmental_factors[factor.name] = factor
        
    def add_choice(self, choice: Choice) -> None:
        """Add a choice to the choice space"""
        self.choice_space[choice.id] = choice
        
    def calculate_choice_probabilities(self) -> Dict[str, float]:
        """
        Calculate the probability of each choice being selected based on:
        1. Environmental factors
        2. Choice history
        3. Phi-harmonic resonance
        4. Quantum superposition
        
        Returns:
            Dictionary mapping choice IDs to probabilities
        """
        if not self.choice_space:
            return {}
            
        # Step 1: Calculate base utilities adjusted by environmental factors
        adjusted_utilities = {}
        for choice_id, choice in self.choice_space.items():
            # Start with base utility
            adjusted_utility = choice.utility
            
            # Apply environmental factors
            for factor in self.environmental_factors.values():
                # Calculate factor influence based on phi-alignment
                factor_influence = factor.weight * factor.value
                phi_resonance = (factor.phi_alignment * choice.phi_resonance) % 1.0
                
                # Stronger influence when phi-aligned
                if phi_resonance < 0.2:  # Strong phi-alignment
                    factor_influence *= 1.5
                
                adjusted_utility *= (1.0 + factor_influence)
            
            adjusted_utilities[choice_id] = adjusted_utility
        
        # Step 2: Apply history influence using phi-harmonic patterns
        for choice_id in self.choice_space:
            choice_freq = self.history.get_choice_frequency(choice_id)
            
            # Calculate phi-harmonic influence of past choices
            # More frequent past choices have diminishing returns (phi-inverse pattern)
            history_influence = math.pow(choice_freq, self.phi_inverse)
            
            # Apply history influence
            adjusted_utilities[choice_id] *= (1.0 + history_influence)
        
        # Step 3: Calculate quantum superposition states
        total_utility = sum(adjusted_utilities.values())
        if total_utility == 0:
            total_utility = 1.0  # Avoid division by zero
            
        # Calculate classical probabilities
        classical_probs = {
            choice_id: utility / total_utility 
            for choice_id, utility in adjusted_utilities.items()
        }
        
        # Step 4: Apply quantum effects (interference patterns)
        quantum_probs = self._apply_quantum_effects(classical_probs)
        
        # Update choice objects with new probabilities
        for choice_id, prob in quantum_probs.items():
            self.choice_space[choice_id].probability = prob
            
        return quantum_probs
    
    def _apply_quantum_effects(self, classical_probs: Dict[str, float]) -> Dict[str, float]:
        """
        Apply quantum effects to classical probabilities.
        This simulates quantum interference patterns in decision making.
        """
        # Convert classical probabilities to quantum amplitudes
        quantum_amplitudes = {
            choice_id: complex(np.sqrt(prob), 0) 
            for choice_id, prob in classical_probs.items()
        }
        
        # Apply quantum phase shifts based on phi-harmonic patterns
        for choice_id, choice in self.choice_space.items():
            # Phase angle based on phi-resonance
            phase_angle = 2 * np.pi * choice.phi_resonance
            phase_shift = complex(np.cos(phase_angle), np.sin(phase_angle))
            
            # Apply phase shift
            quantum_amplitudes[choice_id] *= phase_shift
            
            # Store quantum state in choice object
            self.choice_space[choice_id].quantum_state = quantum_amplitudes[choice_id]
        
        # Calculate interference effects between choices
        for choice1_id in self.choice_space:
            for choice2_id in self.choice_space:
                if choice1_id != choice2_id:
                    # Calculate interference based on phi-harmonic relationship
                    phi_diff = abs(self.choice_space[choice1_id].phi_resonance - 
                                  self.choice_space[choice2_id].phi_resonance)
                    
                    # Strong interference when phi-difference is small
                    if phi_diff < 0.1:
                        interference = 0.1 * np.exp(-phi_diff / 0.05)
                        
                        # Apply interference (simplified model)
                        quantum_amplitudes[choice1_id] += interference * quantum_amplitudes[choice2_id]
        
        # Calculate final probabilities from quantum amplitudes
        quantum_probs = {
            choice_id: np.abs(amplitude) ** 2 
            for choice_id, amplitude in quantum_amplitudes.items()
        }
        
        # Normalize probabilities
        total_prob = sum(quantum_probs.values())
        if total_prob > 0:
            quantum_probs = {
                choice_id: prob / total_prob 
                for choice_id, prob in quantum_probs.items()
            }
        
        return quantum_probs
    
    def make_choice(self, context: Dict[str, Any] = None) -> Choice:
        """
        Make a choice based on the calculated probabilities.
        This simulates the 'measurement' or 'collapse' of the quantum state.
        
        Args:
            context: Additional context information about this choice
            
        Returns:
            The selected choice
        """
        # Calculate current probabilities
        probabilities = self.calculate_choice_probabilities()
        
        # No choices available
        if not probabilities:
            return None
        
        # Convert probabilities to cumulative distribution
        choices = list(probabilities.keys())
        probs = [probabilities[choice_id] for choice_id in choices]
        cumulative_probs = np.cumsum(probs)
        
        # Random selection based on probabilities
        r = random.random()
        for i, cumulative_prob in enumerate(cumulative_probs):
            if r <= cumulative_prob:
                selected_choice_id = choices[i]
                break
        else:
            selected_choice_id = choices[-1]  # Fallback
        
        selected_choice = self.choice_space[selected_choice_id]
        
        # Record choice in history
        self.history.add_choice(selected_choice_id, context or {})
        
        return selected_choice
    
    def calculate_phi_resonance(self, choice_id: str) -> float:
        """
        Calculate the phi-harmonic resonance of a choice.
        This represents how closely the choice aligns with phi-harmonic patterns.
        """
        if choice_id not in self.choice_space:
            return 0.0
            
        # Create a deterministic but seemingly random value based on choice ID
        hash_value = int(hashlib.md5(choice_id.encode()).hexdigest(), 16)
        
        # Calculate base resonance from hash
        base_resonance = (hash_value % 1000) / 1000.0
        
        # Apply phi-harmonic adjustment
        phi_resonance = (base_resonance * self.phi) % 1.0
        
        # Store in choice object
        self.choice_space[choice_id].phi_resonance = phi_resonance
        
        return phi_resonance
    
    def calculate_choice_entropy(self) -> float:
        """
        Calculate the entropy of the choice space.
        Higher entropy means more uncertainty/freedom in choice.
        Lower entropy means more constraints/determinism.
        """
        probabilities = self.calculate_choice_probabilities()
        
        if not probabilities:
            return 0.0
            
        # Shannon entropy formula: -sum(p * log2(p))
        entropy = 0.0
        for prob in probabilities.values():
            if prob > 0:
                entropy -= prob * math.log2(prob)
                
        return entropy
    
    def calculate_effective_choice_space(self) -> float:
        """
        Calculate the effective size of the choice space after accounting for
        environmental constraints and probabilities.
        
        Returns:
            A value between 1 and the total number of choices.
            1 means effectively no choice (deterministic).
            Equal to total choices means complete freedom.
        """
        probabilities = self.calculate_choice_probabilities()
        
        if not probabilities:
            return 0.0
            
        # Calculate effective choice space using inverse participation ratio
        sum_squared_probs = sum(p * p for p in probabilities.values())
        
        if sum_squared_probs > 0:
            return 1.0 / sum_squared_probs
        else:
            return float(len(probabilities))
    
    def quantify_free_will(self) -> Dict[str, float]:
        """
        Quantify the degree of 'free will' in the current choice space.
        This combines entropy, effective choice space, and environmental constraints.
        
        Returns:
            Dictionary with various metrics of 'free will'
        """
        # Calculate basic metrics
        entropy = self.calculate_choice_entropy()
        effective_choices = self.calculate_effective_choice_space()
        total_choices = len(self.choice_space)
        
        # Calculate environmental constraint level
        if self.environmental_factors:
            avg_constraint = sum(f.weight * f.value for f in self.environmental_factors.values()) / len(self.environmental_factors)
        else:
            avg_constraint = 0.0
            
        # Calculate quantum coherence (how much quantum effects matter)
        classical_probs = {choice_id: choice.utility / sum(c.utility for c in self.choice_space.values()) 
                          for choice_id, choice in self.choice_space.items()}
        quantum_probs = self.calculate_choice_probabilities()
        
        # Measure difference between classical and quantum probabilities
        quantum_influence = 0.0
        for choice_id in self.choice_space:
            if choice_id in classical_probs and choice_id in quantum_probs:
                quantum_influence += abs(quantum_probs[choice_id] - classical_probs[choice_id])
                
        quantum_influence /= max(1, len(self.choice_space))
        
        # Calculate phi-harmonic alignment
        phi_alignments = [choice.phi_resonance for choice in self.choice_space.values()]
        avg_phi_alignment = sum(phi_alignments) / max(1, len(phi_alignments))
        
        # Calculate freedom ratio (0 to 1)
        if total_choices > 0:
            freedom_ratio = effective_choices / total_choices
        else:
            freedom_ratio = 0.0
            
        # Calculate determinism level (0 to 1)
        determinism = 1.0 - (entropy / math.log2(max(2, total_choices)))
        
        # Calculate final 'free will' metric (0 to 1)
        # Higher values indicate more freedom of choice
        free_will_metric = (
            0.4 * freedom_ratio +
            0.3 * (1.0 - determinism) +
            0.2 * (1.0 - avg_constraint) +
            0.1 * quantum_influence
        )
        
        return {
            "entropy": entropy,
            "effective_choices": effective_choices,
            "total_choices": total_choices,
            "freedom_ratio": freedom_ratio,
            "determinism": determinism,
            "environmental_constraint": avg_constraint,
            "quantum_influence": quantum_influence,
            "phi_alignment": avg_phi_alignment,
            "free_will_metric": free_will_metric
        }


# Example usage
if __name__ == "__main__":
    # Create a quantum choice model
    model = QuantumChoiceModel()
    
    # Add environmental factors
    model.add_environmental_factor(EnvironmentalFactor(
        name="time_pressure", 
        weight=0.7, 
        value=0.8,  # High time pressure
        phi_alignment=0.2
    ))
    
    model.add_environmental_factor(EnvironmentalFactor(
        name="social_influence", 
        weight=0.5, 
        value=0.6,  # Moderate social influence
        phi_alignment=0.4
    ))
    
    model.add_environmental_factor(EnvironmentalFactor(
        name="resource_constraints", 
        weight=0.6, 
        value=0.3,  # Low resource constraints
        phi_alignment=0.7
    ))
    
    # Add choices
    for i in range(5):
        choice_id = f"choice_{i}"
        choice = Choice(
            id=choice_id,
            name=f"Option {i+1}",
            utility=random.uniform(0.1, 1.0)
        )
        model.add_choice(choice)
        
        # Calculate phi-resonance for this choice
        model.calculate_phi_resonance(choice_id)
    
    # Calculate choice probabilities
    probabilities = model.calculate_choice_probabilities()
    print("\nChoice Probabilities:")
    for choice_id, prob in probabilities.items():
        choice = model.choice_space[choice_id]
        print(f"{choice.name}: {prob:.4f} (Utility: {choice.utility:.4f}, Phi-resonance: {choice.phi_resonance:.4f})")
    
    # Make a choice
    selected_choice = model.make_choice({"context": "example"})
    print(f"\nSelected choice: {selected_choice.name} (ID: {selected_choice.id})")
    
    # Quantify free will
    free_will = model.quantify_free_will()
    print("\nFree Will Metrics:")
    for metric, value in free_will.items():
        print(f"{metric}: {value:.4f}")
    
    # Show effective choice space
    effective_choices = model.calculate_effective_choice_space()
    print(f"\nEffective choice space: {effective_choices:.2f} out of {len(model.choice_space)} total choices")
    
    # Show entropy
    entropy = model.calculate_choice_entropy()
    print(f"Choice entropy: {entropy:.4f} bits")
    
    # Make multiple choices to simulate a decision-making process
    print("\nSimulating multiple choices:")
    for i in range(10):
        choice = model.make_choice({"iteration": i})
        print(f"Iteration {i+1}: Selected {choice.name}")
        
        # Recalculate free will after each choice
        free_will = model.quantify_free_will()
        print(f"  Free will metric: {free_will['free_will_metric']:.4f}")
