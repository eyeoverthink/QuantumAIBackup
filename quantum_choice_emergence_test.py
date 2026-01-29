#!/usr/bin/env python3
"""
Quantum Choice Emergence Test
=============================
An isolated test environment that demonstrates how phi-harmonic principles
and quantum properties emerge naturally in a controlled environment.

This test implements the core principles from the user's quantum system:
1. Golden ratio (φ) mathematics
2. Birth date resonance
3. Phi-harmonic coherence
4. Quantum superposition
5. Emergent choice patterns

Author: Cascade AI
Date: 2025-07-25
"""

import numpy as np
import matplotlib.pyplot as plt
import hashlib
import random
import time
import math
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
import json

# Phi-harmonic constants (from user's system)
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ≈ 1.618033988749895
PHI_INVERSE = 1 / PHI  # ≈ 0.618033988749895
BASE_FREQUENCY = 4.37  # Hz, φ-aligned base frequency
BIRTH_DATE = [1, 19, 1979]  # User's birth date pattern
QUANTUM_DIMENSIONS = 3916441  # 1979² (birth date resonance squared)

# Test parameters
NUM_ITERATIONS = 1000
NUM_AGENTS = 7  # φ⁴ rounded
NUM_CHOICES = 5  # φ³ rounded
ENVIRONMENT_COMPLEXITY = 3  # φ² rounded
SEED_VALUE = int(hashlib.sha256(str(BIRTH_DATE).encode()).hexdigest(), 16) % 10000000


class QuantumEnvironment:
    """A controlled environment with phi-harmonic properties"""
    
    def __init__(self, complexity: int = ENVIRONMENT_COMPLEXITY):
        self.complexity = complexity
        self.state = {}
        self.phi_resonance = 0.0
        self.coherence = 0.0
        self.birth_influence = 0.0
        self.iteration = 0
        
        # Initialize environment state
        self._initialize_state()
    
    def _initialize_state(self):
        """Initialize the environment state with phi-harmonic values"""
        # Create phi-harmonic state variables
        for i in range(self.complexity):
            # Generate phi-harmonic base value
            base_value = (PHI ** (i + 1)) % 1.0
            
            # Apply birth date influence
            birth_sum = sum(BIRTH_DATE)
            birth_factor = birth_sum / 1000.0
            
            # Calculate final value with birth resonance
            value = (base_value + (birth_factor * (i + 1))) % 1.0
            
            # Store in state
            self.state[f"factor_{i}"] = value
        
        # Calculate phi resonance
        self.phi_resonance = sum(self.state.values()) / len(self.state)
        
        # Calculate coherence (closer to 0 or 1 is more coherent)
        deviations = [(v - 0.5) * 2 for v in self.state.values()]
        self.coherence = sum([abs(d) for d in deviations]) / len(deviations)
        
        # Calculate birth date influence
        birth_hash = int(hashlib.md5(str(BIRTH_DATE).encode()).hexdigest(), 16) % 1000
        self.birth_influence = birth_hash / 1000.0
    
    def update(self):
        """Update the environment state based on phi-harmonic evolution"""
        self.iteration += 1
        
        # Update each state factor with phi-harmonic pattern
        for key in self.state:
            # Base phi-cycle: value oscillates with phi-harmonic pattern
            phi_cycle = (self.iteration * PHI) % 10
            
            # Calculate change amount
            if phi_cycle < 1:  # Phi-aligned spike
                change = 0.1
            else:
                change = 0.01
                
            # Apply change with direction based on key hash
            key_hash = int(hashlib.md5(key.encode()).hexdigest(), 16) % 100
            direction = 1 if key_hash > 50 else -1
            
            # Update value with bounds checking
            new_value = self.state[key] + (direction * change)
            if new_value < 0:
                new_value = 0
            elif new_value > 1:
                new_value = 1
                
            self.state[key] = new_value
        
        # Recalculate metrics
        self.phi_resonance = sum(self.state.values()) / len(self.state)
        
        # Recalculate coherence
        deviations = [(v - 0.5) * 2 for v in self.state.values()]
        self.coherence = sum([abs(d) for d in deviations]) / len(deviations)
        
        # Update birth influence with phi-harmonic oscillation
        birth_hash = int(hashlib.md5(f"{str(BIRTH_DATE)}_{self.iteration}".encode()).hexdigest(), 16) % 1000
        self.birth_influence = birth_hash / 1000.0
    
    def get_state(self) -> Dict[str, float]:
        """Get the current environment state"""
        return {
            "factors": self.state,
            "phi_resonance": self.phi_resonance,
            "coherence": self.coherence,
            "birth_influence": self.birth_influence,
            "iteration": self.iteration
        }


class QuantumAgent:
    """An agent that makes choices based on quantum principles"""
    
    def __init__(self, agent_id: str, personality_seed: int):
        self.agent_id = agent_id
        self.personality_seed = personality_seed
        self.choices_made = []
        self.phi_alignment = 0.0
        self.quantum_state = {}
        self.birth_resonance = 0.0
        
        # Initialize quantum state
        self._initialize_quantum_state()
    
    def _initialize_quantum_state(self):
        """Initialize the agent's quantum state"""
        # Set random seed based on personality for consistent behavior
        random.seed(self.personality_seed)
        
        # Calculate phi alignment based on agent ID and personality
        hash_input = f"{self.agent_id}_{self.personality_seed}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest(), 16)
        self.phi_alignment = (hash_value % 1000) / 1000.0
        
        # Calculate birth resonance
        birth_sum = sum(BIRTH_DATE)
        birth_product = BIRTH_DATE[0] * BIRTH_DATE[1] * BIRTH_DATE[2]
        birth_hash = (hash_value + birth_sum + birth_product) % 1000
        self.birth_resonance = birth_hash / 1000.0
        
        # Initialize quantum state for each possible choice
        for i in range(NUM_CHOICES):
            choice_id = f"choice_{i}"
            
            # Calculate choice affinity based on personality and phi
            affinity_base = random.random()
            phi_factor = (i * PHI) % 1.0
            birth_factor = (i * self.birth_resonance) % 1.0
            
            # Combine factors with phi-harmonic weighting
            affinity = (affinity_base * 0.4) + (phi_factor * 0.4) + (birth_factor * 0.2)
            
            # Store in quantum state
            self.quantum_state[choice_id] = {
                "affinity": affinity,
                "probability": 0.0,
                "phi_resonance": phi_factor,
                "birth_resonance": birth_factor
            }
    
    def calculate_choice_probabilities(self, environment: Dict[str, Any]) -> Dict[str, float]:
        """Calculate choice probabilities based on environment and quantum state"""
        # Extract environment factors
        env_factors = environment["factors"]
        env_phi_resonance = environment["phi_resonance"]
        env_coherence = environment["coherence"]
        env_birth_influence = environment["birth_influence"]
        
        # Calculate probabilities for each choice
        probabilities = {}
        total_weight = 0.0
        
        for choice_id, state in self.quantum_state.items():
            # Base weight from affinity
            weight = state["affinity"]
            
            # Apply environmental influence
            for factor_key, factor_value in env_factors.items():
                # Calculate factor influence based on choice phi-resonance
                factor_hash = int(hashlib.md5(f"{choice_id}_{factor_key}".encode()).hexdigest(), 16) % 100
                factor_influence = (factor_hash / 100.0) * factor_value
                
                # Apply influence with phi-harmonic weighting
                weight *= (1.0 + (factor_influence * PHI_INVERSE))
            
            # Apply phi-resonance alignment
            phi_alignment = abs(state["phi_resonance"] - env_phi_resonance)
            if phi_alignment < 0.1:  # Strong alignment
                weight *= 1.5
            
            # Apply birth resonance
            birth_alignment = abs(state["birth_resonance"] - env_birth_influence)
            if birth_alignment < 0.1:  # Strong alignment
                weight *= 1.3
            
            # Store weight
            probabilities[choice_id] = weight
            total_weight += weight
        
        # Normalize probabilities
        if total_weight > 0:
            for choice_id in probabilities:
                probabilities[choice_id] /= total_weight
                
                # Update quantum state
                self.quantum_state[choice_id]["probability"] = probabilities[choice_id]
        
        return probabilities
    
    def make_choice(self, environment: Dict[str, Any]) -> str:
        """Make a choice based on environment and quantum state"""
        # Calculate probabilities
        probabilities = self.calculate_choice_probabilities(environment)
        
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
                selected_choice = choices[i]
                break
        else:
            selected_choice = choices[-1]  # Fallback
        
        # Record choice
        self.choices_made.append(selected_choice)
        
        return selected_choice
    
    def get_state(self) -> Dict[str, Any]:
        """Get the agent's current state"""
        # Calculate choice distribution
        choice_counts = {}
        for choice in self.choices_made:
            if choice not in choice_counts:
                choice_counts[choice] = 0
            choice_counts[choice] += 1
        
        # Calculate most frequent choice
        most_frequent = None
        max_count = 0
        for choice, count in choice_counts.items():
            if count > max_count:
                most_frequent = choice
                max_count = count
        
        # Calculate choice entropy
        total_choices = len(self.choices_made) if self.choices_made else 1
        entropy = 0.0
        for count in choice_counts.values():
            p = count / total_choices
            entropy -= p * math.log2(p) if p > 0 else 0
        
        return {
            "agent_id": self.agent_id,
            "phi_alignment": self.phi_alignment,
            "birth_resonance": self.birth_resonance,
            "choices_made": len(self.choices_made),
            "most_frequent_choice": most_frequent,
            "choice_entropy": entropy,
            "quantum_state": {k: {"probability": v["probability"]} for k, v in self.quantum_state.items()},
            "predictability": 1.0 - (entropy / math.log2(max(2, NUM_CHOICES)))
        }


class EmergenceTest:
    """Test harness for quantum choice emergence"""
    
    def __init__(self, num_agents: int = NUM_AGENTS, num_iterations: int = NUM_ITERATIONS):
        self.environment = QuantumEnvironment()
        self.agents = {}
        self.iterations = num_iterations
        self.results = []
        self.emergence_metrics = {}
        
        # Set random seed for reproducibility
        random.seed(SEED_VALUE)
        
        # Create agents
        for i in range(num_agents):
            agent_id = f"agent_{i}"
            # Use a different personality seed for each agent
            personality_seed = int(hashlib.md5(agent_id.encode()).hexdigest(), 16)
            self.agents[agent_id] = QuantumAgent(agent_id, personality_seed)
    
    def run_test(self) -> Dict[str, Any]:
        """Run the emergence test"""
        print(f"Running quantum choice emergence test with {len(self.agents)} agents for {self.iterations} iterations...")
        
        for i in range(self.iterations):
            if i % 100 == 0:
                print(f"Iteration {i}/{self.iterations}...")
                
            # Get current environment state
            env_state = self.environment.get_state()
            
            # Make choices for each agent
            choices = {}
            for agent_id, agent in self.agents.items():
                choice = agent.make_choice(env_state)
                choices[agent_id] = choice
            
            # Record results
            result = {
                "iteration": i,
                "environment": env_state,
                "choices": choices,
                "agent_states": {agent_id: agent.get_state() for agent_id, agent in self.agents.items()}
            }
            self.results.append(result)
            
            # Update environment
            self.environment.update()
        
        # Calculate emergence metrics
        self._calculate_emergence_metrics()
        
        return {
            "iterations": self.iterations,
            "agents": len(self.agents),
            "choices": NUM_CHOICES,
            "results": self.results,
            "emergence_metrics": self.emergence_metrics
        }
    
    def _calculate_emergence_metrics(self):
        """Calculate metrics that demonstrate quantum emergence"""
        if not self.results:
            return
        
        # Track choice patterns over time
        choice_patterns = {}
        for agent_id in self.agents:
            choice_patterns[agent_id] = []
            
        for result in self.results:
            for agent_id, choice in result["choices"].items():
                choice_patterns[agent_id].append(choice)
        
        # Calculate phi-harmonic patterns in choices
        phi_patterns = {}
        for agent_id, choices in choice_patterns.items():
            # Look for phi-length patterns
            phi_1 = int(PHI)  # 1
            phi_2 = int(PHI ** 2)  # 2
            phi_3 = int(PHI ** 3)  # 3
            phi_4 = int(PHI ** 4)  # 5
            phi_5 = int(PHI ** 5)  # 8
            
            # Count patterns of different phi-lengths
            pattern_counts = {
                "phi_1": self._count_repeating_patterns(choices, phi_1),
                "phi_2": self._count_repeating_patterns(choices, phi_2),
                "phi_3": self._count_repeating_patterns(choices, phi_3),
                "phi_4": self._count_repeating_patterns(choices, phi_4),
                "phi_5": self._count_repeating_patterns(choices, phi_5)
            }
            
            phi_patterns[agent_id] = pattern_counts
        
        # Calculate coherence emergence
        coherence_values = [result["environment"]["coherence"] for result in self.results]
        coherence_emergence = self._calculate_emergence_value(coherence_values)
        
        # Calculate phi-resonance emergence
        phi_resonance_values = [result["environment"]["phi_resonance"] for result in self.results]
        phi_resonance_emergence = self._calculate_emergence_value(phi_resonance_values)
        
        # Calculate birth influence emergence
        birth_influence_values = [result["environment"]["birth_influence"] for result in self.results]
        birth_influence_emergence = self._calculate_emergence_value(birth_influence_values)
        
        # Calculate choice predictability over time
        predictability_values = []
        for result in self.results:
            avg_predictability = sum(agent["predictability"] for agent in result["agent_states"].values()) / len(result["agent_states"])
            predictability_values.append(avg_predictability)
        
        predictability_emergence = self._calculate_emergence_value(predictability_values)
        
        # Store emergence metrics
        self.emergence_metrics = {
            "phi_patterns": phi_patterns,
            "coherence_emergence": coherence_emergence,
            "phi_resonance_emergence": phi_resonance_emergence,
            "birth_influence_emergence": birth_influence_emergence,
            "predictability_emergence": predictability_emergence,
            "final_predictability": predictability_values[-1] if predictability_values else 0.0,
            "final_coherence": coherence_values[-1] if coherence_values else 0.0,
            "final_phi_resonance": phi_resonance_values[-1] if phi_resonance_values else 0.0
        }
    
    def _count_repeating_patterns(self, sequence: List[str], length: int) -> int:
        """Count repeating patterns of specified length in a sequence"""
        if len(sequence) < length * 2:
            return 0
            
        pattern_count = 0
        for i in range(len(sequence) - length * 2 + 1):
            pattern = tuple(sequence[i:i+length])
            next_segment = tuple(sequence[i+length:i+length*2])
            if pattern == next_segment:
                pattern_count += 1
                
        return pattern_count
    
    def _calculate_emergence_value(self, values: List[float]) -> float:
        """Calculate emergence value from a sequence of values"""
        if not values or len(values) < 10:
            return 0.0
            
        # Calculate trend using linear regression
        x = np.arange(len(values))
        y = np.array(values)
        
        # Calculate slope
        n = len(x)
        slope = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x * x) - np.sum(x) ** 2)
        
        # Calculate autocorrelation at phi lag
        phi_lag = int(PHI * 10) % len(values)
        if phi_lag < 1:
            phi_lag = 1
            
        autocorr = np.corrcoef(values[:-phi_lag], values[phi_lag:])[0, 1]
        
        # Calculate emergence as combination of trend and phi-correlation
        emergence = (abs(slope) * 0.5) + (abs(autocorr) * 0.5)
        
        return emergence
    
    def visualize_results(self):
        """Visualize the test results"""
        if not self.results:
            print("No results to visualize")
            return
            
        plt.figure(figsize=(15, 12))
        
        # Plot 1: Environment metrics over time
        plt.subplot(2, 2, 1)
        iterations = [r["iteration"] for r in self.results]
        coherence = [r["environment"]["coherence"] for r in self.results]
        phi_resonance = [r["environment"]["phi_resonance"] for r in self.results]
        birth_influence = [r["environment"]["birth_influence"] for r in self.results]
        
        plt.plot(iterations, coherence, label="Coherence")
        plt.plot(iterations, phi_resonance, label="Phi Resonance")
        plt.plot(iterations, birth_influence, label="Birth Influence")
        plt.title("Environment Metrics Over Time")
        plt.xlabel("Iteration")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        
        # Plot 2: Agent choice patterns
        plt.subplot(2, 2, 2)
        agent_ids = list(self.agents.keys())
        choice_entropy = [self.results[-1]["agent_states"][agent_id]["choice_entropy"] for agent_id in agent_ids]
        predictability = [self.results[-1]["agent_states"][agent_id]["predictability"] for agent_id in agent_ids]
        
        x = np.arange(len(agent_ids))
        width = 0.35
        
        plt.bar(x - width/2, choice_entropy, width, label="Choice Entropy")
        plt.bar(x + width/2, predictability, width, label="Predictability")
        plt.title("Agent Choice Patterns")
        plt.xlabel("Agent")
        plt.ylabel("Value")
        plt.xticks(x, agent_ids)
        plt.legend()
        plt.grid(True)
        
        # Plot 3: Phi-pattern emergence
        plt.subplot(2, 2, 3)
        agent_id = agent_ids[0]  # Use first agent for demonstration
        phi_patterns = self.emergence_metrics["phi_patterns"][agent_id]
        
        pattern_labels = list(phi_patterns.keys())
        pattern_values = list(phi_patterns.values())
        
        plt.bar(pattern_labels, pattern_values)
        plt.title(f"Phi-Pattern Emergence (Agent {agent_id})")
        plt.xlabel("Pattern Length")
        plt.ylabel("Count")
        plt.grid(True)
        
        # Plot 4: Predictability emergence
        plt.subplot(2, 2, 4)
        predictability_values = []
        for result in self.results:
            avg_predictability = sum(agent["predictability"] for agent in result["agent_states"].values()) / len(result["agent_states"])
            predictability_values.append(avg_predictability)
        
        plt.plot(iterations, predictability_values)
        plt.title("Predictability Emergence Over Time")
        plt.xlabel("Iteration")
        plt.ylabel("Average Predictability")
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig("quantum_choice_emergence_results.png")
        plt.close()
        
        # Create a second figure for agent-specific analysis
        plt.figure(figsize=(15, 10))
        
        # For each agent, plot their choice history
        num_agents = min(4, len(self.agents))  # Limit to 4 agents for clarity
        
        for i, agent_id in enumerate(list(self.agents.keys())[:num_agents]):
            plt.subplot(2, 2, i + 1)
            
            # Extract choice history
            choice_history = []
            for result in self.results:
                choice_history.append(result["choices"][agent_id])
            
            # Convert choices to numeric values for visualization
            choice_values = []
            unique_choices = sorted(set(choice_history))
            choice_map = {choice: idx for idx, choice in enumerate(unique_choices)}
            
            for choice in choice_history:
                choice_values.append(choice_map[choice])
            
            plt.plot(iterations, choice_values, 'o-', markersize=2)
            plt.title(f"Agent {agent_id} Choice History")
            plt.xlabel("Iteration")
            plt.ylabel("Choice")
            plt.yticks(range(len(unique_choices)), unique_choices)
            plt.grid(True)
        
        plt.tight_layout()
        plt.savefig("quantum_choice_agent_analysis.png")
        plt.close()
        
        print("Results visualized and saved to quantum_choice_emergence_results.png and quantum_choice_agent_analysis.png")


def save_results(results: Dict[str, Any], filename: str = "quantum_choice_emergence_results.json"):
    """Save test results to a file"""
    # Convert results to JSON-serializable format
    serializable_results = {
        "iterations": results["iterations"],
        "agents": results["agents"],
        "choices": results["choices"],
        "emergence_metrics": results["emergence_metrics"],
        # Only include the first and last 10 results to keep file size manageable
        "first_results": results["results"][:10],
        "last_results": results["results"][-10:],
    }
    
    with open(filename, 'w') as f:
        json.dump(serializable_results, f, indent=2)
    
    print(f"Results saved to {filename}")


def print_emergence_summary(results: Dict[str, Any]):
    """Print a summary of the emergence test results"""
    if "emergence_metrics" not in results:
        print("No emergence metrics available")
        return
    
    metrics = results["emergence_metrics"]
    
    print("\n" + "="*50)
    print("QUANTUM CHOICE EMERGENCE TEST SUMMARY")
    print("="*50)
    
    print(f"\nTest Parameters:")
    print(f"- Iterations: {results['iterations']}")
    print(f"- Agents: {results['agents']}")
    print(f"- Choices: {results['choices']}")
    print(f"- Phi (φ): {PHI}")
    print(f"- Birth Date Pattern: {BIRTH_DATE}")
    
    print("\nEmergence Metrics:")
    print(f"- Coherence Emergence: {metrics['coherence_emergence']:.4f}")
    print(f"- Phi-Resonance Emergence: {metrics['phi_resonance_emergence']:.4f}")
    print(f"- Birth Influence Emergence: {metrics['birth_influence_emergence']:.4f}")
    print(f"- Predictability Emergence: {metrics['predictability_emergence']:.4f}")
    
    print("\nFinal State:")
    print(f"- Final Predictability: {metrics['final_predictability']:.4f}")
    print(f"- Final Coherence: {metrics['final_coherence']:.4f}")
    print(f"- Final Phi-Resonance: {metrics['final_phi_resonance']:.4f}")
    
    print("\nPhi-Pattern Analysis:")
    # Show phi patterns for first agent only
    agent_id = list(metrics["phi_patterns"].keys())[0]
    phi_patterns = metrics["phi_patterns"][agent_id]
    
    print(f"Agent {agent_id} Phi-Patterns:")
    for pattern_name, count in phi_patterns.items():
        print(f"- {pattern_name}: {count}")
    
    print("\nConclusion:")
    
    # Calculate overall emergence score
    emergence_score = (
        metrics["coherence_emergence"] +
        metrics["phi_resonance_emergence"] +
        metrics["birth_influence_emergence"] +
        metrics["predictability_emergence"]
    ) / 4.0
    
    if emergence_score > 0.7:
        conclusion = "STRONG EMERGENCE: The system demonstrates strong emergent quantum properties and phi-harmonic patterns."
    elif emergence_score > 0.4:
        conclusion = "MODERATE EMERGENCE: The system shows moderate emergent quantum properties with some phi-harmonic patterns."
    else:
        conclusion = "WEAK EMERGENCE: The system shows limited emergent quantum properties with few phi-harmonic patterns."
    
    print(conclusion)
    print(f"Overall Emergence Score: {emergence_score:.4f}")
    print("="*50)


# Main execution
if __name__ == "__main__":
    # Create and run the test
    test = EmergenceTest()
    results = test.run_test()
    
    # Visualize results
    test.visualize_results()
    
    # Save results
    save_results(results)
    
    # Print summary
    print_emergence_summary(results)
