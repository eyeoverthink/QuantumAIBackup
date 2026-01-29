#!/usr/bin/env python3
"""
Quantum Choice Simulation Prototype
==================================
A prototype that demonstrates how the Quantum Choice Quantification Model
can be used to simulate and predict choices in a controlled environment.

This simulation creates a virtual environment with:
1. Multiple agents with different decision-making patterns
2. Environmental factors that change over time
3. A choice space that evolves based on phi-harmonic principles
4. Visualization of choice probabilities and predictions

Author: Cascade AI
Date: 2025-07-25
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import time
import hashlib
import math
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from quantum_choice_quantification import (
    QuantumChoiceModel, Choice, EnvironmentalFactor, PHI
)

# Constants
SIMULATION_STEPS = 100
NUM_AGENTS = 5
NUM_CHOICES = 7
ENVIRONMENTAL_CHANGE_RATE = 0.05  # How quickly environment changes

class ControlledEnvironment:
    """Represents a controlled environment with evolving factors"""
    
    def __init__(self, num_factors: int = 3):
        self.factors: Dict[str, EnvironmentalFactor] = {}
        self.factor_change_directions: Dict[str, float] = {}
        self.step_count = 0
        
        # Initialize environmental factors
        factor_names = [
            "time_pressure", "social_influence", "resource_constraints",
            "cognitive_load", "emotional_state", "physical_comfort",
            "information_availability", "decision_complexity"
        ]
        
        for i in range(min(num_factors, len(factor_names))):
            name = factor_names[i]
            weight = random.uniform(0.3, 0.8)
            value = random.uniform(0.2, 0.8)
            phi_alignment = random.uniform(0, 1)
            
            self.factors[name] = EnvironmentalFactor(
                name=name,
                weight=weight,
                value=value,
                phi_alignment=phi_alignment
            )
            
            # Initialize change direction (-1 to +1)
            self.factor_change_directions[name] = random.uniform(-1, 1)
    
    def update(self) -> None:
        """Update the environment for the next step"""
        self.step_count += 1
        
        # Update each environmental factor
        for name, factor in self.factors.items():
            # Calculate change amount (with phi-harmonic influence)
            change_direction = self.factor_change_directions[name]
            change_amount = change_direction * ENVIRONMENTAL_CHANGE_RATE
            
            # Apply phi-harmonic pattern to change rate
            phi_cycle = (self.step_count * PHI) % 10
            if phi_cycle < 1:  # Phi-aligned spike in change rate
                change_amount *= 2.0
            
            # Update factor value with bounds checking
            new_value = factor.value + change_amount
            if new_value < 0:
                new_value = 0
                self.factor_change_directions[name] *= -1  # Reverse direction
            elif new_value > 1:
                new_value = 1
                self.factor_change_directions[name] *= -1  # Reverse direction
                
            factor.value = new_value
            
            # Occasionally change direction
            if random.random() < 0.1:
                self.factor_change_directions[name] = random.uniform(-1, 1)
    
    def get_factors(self) -> Dict[str, EnvironmentalFactor]:
        """Get the current environmental factors"""
        return self.factors


class Agent:
    """Represents an agent making choices in the controlled environment"""
    
    def __init__(self, agent_id: str, personality_seed: int):
        self.agent_id = agent_id
        self.personality_seed = personality_seed
        self.choice_model = QuantumChoiceModel()
        self.decision_history: List[str] = []
        
        # Set a consistent random seed based on personality
        random.seed(personality_seed)
        
        # Initialize agent's personal preferences (affects utility calculations)
        self.preferences: Dict[str, float] = {}
        
    def set_choice_space(self, choices: Dict[str, Choice]) -> None:
        """Set the available choices for this agent"""
        # Clear existing choices
        self.choice_model.choice_space = {}
        
        # Add choices with personalized utilities
        for choice_id, choice in choices.items():
            # Create a copy of the choice
            personalized_choice = Choice(
                id=choice.id,
                name=choice.name,
                utility=choice.utility
            )
            
            # Apply personality-based preference adjustment
            if choice_id in self.preferences:
                preference_factor = self.preferences[choice_id]
                personalized_choice.utility *= (1.0 + preference_factor)
            
            # Add to choice model
            self.choice_model.add_choice(personalized_choice)
            
            # Calculate phi-resonance for this choice
            self.choice_model.calculate_phi_resonance(choice_id)
    
    def set_environment(self, environment: ControlledEnvironment) -> None:
        """Update the agent's perception of the environment"""
        # Clear existing environmental factors
        self.choice_model.environmental_factors = {}
        
        # Add environmental factors (with potential personality-based perception differences)
        for name, factor in environment.get_factors().items():
            # Create a copy of the factor with potential perception differences
            perceived_factor = EnvironmentalFactor(
                name=factor.name,
                weight=factor.weight,
                value=factor.value,
                phi_alignment=factor.phi_alignment
            )
            
            # Apply personality-based perception adjustment (±20%)
            random.seed(self.personality_seed + hash(name))
            perception_adjustment = random.uniform(0.8, 1.2)
            perceived_factor.value *= perception_adjustment
            perceived_factor.value = min(1.0, max(0.0, perceived_factor.value))
            
            # Add to choice model
            self.choice_model.add_environmental_factor(perceived_factor)
    
    def make_choice(self) -> Choice:
        """Make a choice based on current environment and preferences"""
        # Make choice using the quantum choice model
        choice = self.choice_model.make_choice({
            "agent_id": self.agent_id,
            "timestamp": time.time()
        })
        
        # Record choice
        if choice:
            self.decision_history.append(choice.id)
        
        return choice
    
    def generate_preferences(self, choice_ids: List[str]) -> None:
        """Generate consistent preferences for choices based on personality"""
        # Reset random seed to ensure consistent personality
        random.seed(self.personality_seed)
        
        # Generate preferences for each choice
        for choice_id in choice_ids:
            # Hash the choice ID with the personality seed for consistency
            hash_input = f"{self.personality_seed}_{choice_id}"
            hash_value = int(hashlib.md5(hash_input.encode()).hexdigest(), 16)
            
            # Generate preference (-0.5 to +1.0, skewed positive)
            preference = (hash_value % 1000) / 1000.0 * 1.5 - 0.5
            self.preferences[choice_id] = preference
    
    def get_choice_probabilities(self) -> Dict[str, float]:
        """Get the current choice probabilities for this agent"""
        return self.choice_model.calculate_choice_probabilities()
    
    def get_free_will_metrics(self) -> Dict[str, float]:
        """Get metrics about the agent's 'free will'"""
        return self.choice_model.quantify_free_will()


class ChoiceSimulation:
    """Simulates choices in a controlled environment"""
    
    def __init__(self, num_agents: int = 5, num_choices: int = 7, num_factors: int = 3):
        self.environment = ControlledEnvironment(num_factors)
        self.agents: Dict[str, Agent] = {}
        self.choices: Dict[str, Choice] = {}
        self.step_count = 0
        self.choice_history: Dict[str, List[str]] = {}  # Agent ID -> list of choices
        self.prediction_accuracy: List[float] = []
        
        # Create choices
        for i in range(num_choices):
            choice_id = f"choice_{i}"
            choice = Choice(
                id=choice_id,
                name=f"Option {i+1}",
                utility=random.uniform(0.3, 1.0)
            )
            self.choices[choice_id] = choice
        
        # Create agents
        for i in range(num_agents):
            agent_id = f"agent_{i}"
            # Use a different personality seed for each agent
            personality_seed = int(hashlib.md5(agent_id.encode()).hexdigest(), 16)
            
            agent = Agent(agent_id, personality_seed)
            agent.generate_preferences(list(self.choices.keys()))
            agent.set_choice_space(self.choices)
            agent.set_environment(self.environment)
            
            self.agents[agent_id] = agent
            self.choice_history[agent_id] = []
    
    def step(self) -> Dict[str, Any]:
        """Run one step of the simulation"""
        self.step_count += 1
        
        # Update environment
        self.environment.update()
        
        # Update agents' perception of environment
        for agent in self.agents.values():
            agent.set_environment(self.environment)
        
        # Make predictions before choices are made
        predictions = self._predict_choices()
        
        # Make choices
        choices = {}
        for agent_id, agent in self.agents.items():
            choice = agent.make_choice()
            choices[agent_id] = choice.id if choice else None
            self.choice_history[agent_id].append(choice.id if choice else "none")
        
        # Calculate prediction accuracy
        accuracy = self._calculate_prediction_accuracy(predictions, choices)
        self.prediction_accuracy.append(accuracy)
        
        return {
            "step": self.step_count,
            "choices": choices,
            "predictions": predictions,
            "accuracy": accuracy,
            "environment": {name: factor.value for name, factor in self.environment.factors.items()},
            "free_will_metrics": {agent_id: agent.get_free_will_metrics() for agent_id, agent in self.agents.items()}
        }
    
    def _predict_choices(self) -> Dict[str, str]:
        """Predict what choices agents will make"""
        predictions = {}
        
        for agent_id, agent in self.agents.items():
            # Get probabilities
            probabilities = agent.get_choice_probabilities()
            
            # Find most likely choice
            if probabilities:
                most_likely_choice = max(probabilities.items(), key=lambda x: x[1])[0]
                predictions[agent_id] = most_likely_choice
            else:
                predictions[agent_id] = None
                
        return predictions
    
    def _calculate_prediction_accuracy(self, predictions: Dict[str, str], 
                                      actual_choices: Dict[str, str]) -> float:
        """Calculate the accuracy of predictions"""
        if not predictions or not actual_choices:
            return 0.0
            
        correct = 0
        total = 0
        
        for agent_id, predicted_choice in predictions.items():
            if agent_id in actual_choices:
                total += 1
                if predicted_choice == actual_choices[agent_id]:
                    correct += 1
        
        return correct / max(1, total)
    
    def run_simulation(self, steps: int = SIMULATION_STEPS) -> Dict[str, Any]:
        """Run the simulation for a specified number of steps"""
        results = []
        
        for _ in range(steps):
            step_result = self.step()
            results.append(step_result)
            
        return {
            "steps": steps,
            "results": results,
            "final_accuracy": np.mean(self.prediction_accuracy),
            "accuracy_trend": self.prediction_accuracy,
            "choice_history": self.choice_history,
            "final_free_will_metrics": {
                agent_id: agent.get_free_will_metrics() 
                for agent_id, agent in self.agents.items()
            }
        }
    
    def visualize_results(self, results: Dict[str, Any]) -> None:
        """Visualize the simulation results"""
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Prediction accuracy over time
        plt.subplot(2, 2, 1)
        plt.plot(results["accuracy_trend"])
        plt.title("Prediction Accuracy Over Time")
        plt.xlabel("Simulation Step")
        plt.ylabel("Accuracy")
        plt.grid(True)
        
        # Plot 2: Environmental factors over time
        plt.subplot(2, 2, 2)
        env_data = {}
        for step_result in results["results"]:
            for factor_name, value in step_result["environment"].items():
                if factor_name not in env_data:
                    env_data[factor_name] = []
                env_data[factor_name].append(value)
        
        for factor_name, values in env_data.items():
            plt.plot(values, label=factor_name)
        plt.title("Environmental Factors Over Time")
        plt.xlabel("Simulation Step")
        plt.ylabel("Factor Value")
        plt.legend()
        plt.grid(True)
        
        # Plot 3: Free will metrics over time
        plt.subplot(2, 2, 3)
        free_will_data = {}
        for step_result in results["results"]:
            for agent_id, metrics in step_result["free_will_metrics"].items():
                key = f"{agent_id}_free_will"
                if key not in free_will_data:
                    free_will_data[key] = []
                free_will_data[key].append(metrics["free_will_metric"])
        
        for key, values in free_will_data.items():
            plt.plot(values, label=key)
        plt.title("'Free Will' Metrics Over Time")
        plt.xlabel("Simulation Step")
        plt.ylabel("Free Will Metric")
        plt.legend()
        plt.grid(True)
        
        # Plot 4: Choice distribution
        plt.subplot(2, 2, 4)
        choice_counts = {}
        for agent_id, choices in results["choice_history"].items():
            for choice in choices:
                if choice not in choice_counts:
                    choice_counts[choice] = 0
                choice_counts[choice] += 1
        
        plt.bar(choice_counts.keys(), choice_counts.values())
        plt.title("Choice Distribution")
        plt.xlabel("Choice")
        plt.ylabel("Frequency")
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig("quantum_choice_simulation_results.png")
        plt.close()
        
        # Create a second figure for agent-specific analysis
        plt.figure(figsize=(15, 10))
        
        # For each agent, plot their choice history
        num_agents = len(results["choice_history"])
        cols = 2
        rows = (num_agents + 1) // cols
        
        for i, (agent_id, choices) in enumerate(results["choice_history"].items()):
            plt.subplot(rows, cols, i + 1)
            
            # Convert choices to numeric values for visualization
            choice_values = []
            unique_choices = sorted(set(choices))
            choice_map = {choice: idx for idx, choice in enumerate(unique_choices)}
            
            for choice in choices:
                choice_values.append(choice_map[choice])
            
            plt.plot(choice_values, 'o-')
            plt.title(f"Agent {agent_id} Choice History")
            plt.xlabel("Simulation Step")
            plt.ylabel("Choice")
            plt.yticks(range(len(unique_choices)), unique_choices)
            plt.grid(True)
        
        plt.tight_layout()
        plt.savefig("quantum_choice_agent_analysis.png")
        plt.close()
        
        print(f"Final prediction accuracy: {results['final_accuracy']:.2%}")
        print("Free will metrics for each agent:")
        for agent_id, metrics in results["final_free_will_metrics"].items():
            print(f"  {agent_id}: {metrics['free_will_metric']:.4f}")


class QRCodeChoiceSimulation:
    """
    Extends the choice simulation to work with QR codes.
    This demonstrates how the choice quantification model could be integrated
    with the QR code flip book concept for IP protection.
    """
    
    def __init__(self, simulation: ChoiceSimulation):
        self.simulation = simulation
        self.qr_code_fragments = []
        self.qr_evolution_history = []
    
    def generate_qr_code_fragment(self, step_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a QR code fragment containing:
        1. Code to update the environment
        2. Code to predict agent choices
        3. Phi-harmonic metadata
        
        In a real implementation, this would generate actual QR codes.
        For this prototype, we just simulate the content.
        """
        # Create a timestamp with phi-harmonic properties
        phi_timestamp = time.time() * PHI % 1000000
        
        # Create a quantum signature for this fragment
        signature_base = f"{phi_timestamp}_{step_data['step']}"
        quantum_signature = hashlib.sha256(signature_base.encode()).hexdigest()[:16]
        
        # Create code fragment (in a real system, this would be actual Python code)
        code_fragment = {
            "type": "environment_update",
            "environment_factors": step_data["environment"],
            "predictions": step_data["predictions"],
            "actual_choices": step_data["choices"],
            "free_will_metrics": {
                agent_id: metrics["free_will_metric"]
                for agent_id, metrics in step_data["free_will_metrics"].items()
            }
        }
        
        # Create QR fragment
        qr_fragment = {
            "sequence_number": step_data["step"],
            "phi_timestamp": phi_timestamp,
            "quantum_signature": quantum_signature,
            "code_fragment": code_fragment,
            "accuracy": step_data["accuracy"]
        }
        
        self.qr_code_fragments.append(qr_fragment)
        return qr_fragment
    
    def evolve_qr_codes(self) -> Dict[str, Any]:
        """
        Simulate the evolution of QR codes based on the simulation results.
        In a real system, this would generate new QR codes with evolved code.
        """
        # Run the simulation
        results = self.simulation.run_simulation()
        
        # Generate QR code fragments for each step
        for step_result in results["results"]:
            qr_fragment = self.generate_qr_code_fragment(step_result)
            self.qr_evolution_history.append(qr_fragment)
        
        # Generate a final "evolved" QR code that contains the learned patterns
        evolved_code = self._generate_evolved_code(results)
        
        return {
            "simulation_results": results,
            "qr_evolution_history": self.qr_evolution_history,
            "evolved_code": evolved_code
        }
    
    def _generate_evolved_code(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate an evolved code fragment that represents the learned patterns.
        This simulates how the system would evolve its own code over time.
        """
        # Extract patterns from the simulation results
        agent_patterns = {}
        for agent_id, choices in results["choice_history"].items():
            # Find the most common choice for each agent
            choice_counts = {}
            for choice in choices:
                if choice not in choice_counts:
                    choice_counts[choice] = 0
                choice_counts[choice] += 1
            
            most_common_choice = max(choice_counts.items(), key=lambda x: x[1])[0]
            choice_entropy = 0.0
            total_choices = sum(choice_counts.values())
            
            for count in choice_counts.values():
                p = count / total_choices
                choice_entropy -= p * math.log2(p)
            
            agent_patterns[agent_id] = {
                "most_common_choice": most_common_choice,
                "choice_entropy": choice_entropy,
                "predictability": 1.0 - (choice_entropy / math.log2(max(2, len(choice_counts))))
            }
        
        # Extract environmental influence patterns
        env_influence = {}
        for factor_name in results["results"][0]["environment"].keys():
            # Calculate correlation between factor and prediction accuracy
            factor_values = [step["environment"][factor_name] for step in results["results"]]
            accuracy_values = results["accuracy_trend"]
            
            # Ensure arrays are the same length
            min_length = min(len(factor_values), len(accuracy_values))
            factor_values = factor_values[:min_length]
            accuracy_values = accuracy_values[:min_length]
            
            # Simple correlation calculation
            correlation = np.corrcoef(factor_values, accuracy_values)[0, 1]
            env_influence[factor_name] = correlation
        
        # Generate evolved code
        evolved_code = {
            "agent_patterns": agent_patterns,
            "environmental_influences": env_influence,
            "average_prediction_accuracy": results["final_accuracy"],
            "phi_harmonic_timestamp": time.time() * PHI,
            "quantum_signature": hashlib.sha256(str(time.time()).encode()).hexdigest()[:16],
            "evolved_code_version": "1.0"
        }
        
        return evolved_code


# Example usage
if __name__ == "__main__":
    print("Initializing Quantum Choice Simulation...")
    simulation = ChoiceSimulation(
        num_agents=NUM_AGENTS,
        num_choices=NUM_CHOICES,
        num_factors=3
    )
    
    print("Running simulation...")
    results = simulation.run_simulation(SIMULATION_STEPS)
    
    print("Visualizing results...")
    simulation.visualize_results(results)
    
    print("\nInitializing QR Code Evolution Simulation...")
    qr_simulation = QRCodeChoiceSimulation(simulation)
    
    print("Evolving QR codes...")
    qr_results = qr_simulation.evolve_qr_codes()
    
    print("\nEvolved Code Fragment:")
    for key, value in qr_results["evolved_code"].items():
        if isinstance(value, dict):
            print(f"{key}:")
            for subkey, subvalue in value.items():
                print(f"  {subkey}: {subvalue}")
        else:
            print(f"{key}: {value}")
    
    print("\nFinal Prediction Accuracy:", results["final_accuracy"])
    print("\nSimulation complete. Results saved to quantum_choice_simulation_results.png")
