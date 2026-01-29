#!/usr/bin/env python3
"""
Face QR Evolution Demonstration

This script demonstrates the core concepts of the Face-QR Evolution system,
showing how authentication parameters evolve over time based on phi-harmonic principles.
"""

import os
import sys
import json
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class FaceQREvolutionDemo:
    """Demonstrates the evolutionary capabilities of the Face-QR system."""
    
    def __init__(self):
        """Initialize the evolution demonstration."""
        # Evolution parameters
        self.generation = 1
        self.complexity = 1.0
        self.resonance = 0.5
        self.mutation_rate = 0.1
        self.phi_time = (time.time() * PHI) % 1.0
        
        # Authentication parameters that will evolve
        self.similarity_threshold = 0.45
        self.feature_weight = 0.5
        self.temporal_factor = 0.2
        
        # Create evolution directory
        self.evolution_dir = "evolution_demo_data"
        os.makedirs(self.evolution_dir, exist_ok=True)
        
        # Initialize epigenetic memory
        self.epigenetic_memory = {
            "generation": 1,
            "complexity": 1.0,
            "resonance": 0.5,
            "mutation_rate": 0.1,
            "similarity_threshold": 0.45,
            "feature_weight": 0.5,
            "temporal_factor": 0.2,
            "evolution_history": [],
            "authentication_history": []
        }
        
        print("Face QR Evolution Demo initialized")
    
    def evolve(self, authentication_success=None, similarity_score=None):
        """
        Evolve the system's parameters based on phi-harmonic principles and authentication results.
        
        Args:
            authentication_success: Whether the last authentication was successful
            similarity_score: Similarity score from the last authentication attempt
        """
        # Update generation
        self.generation += 1
        
        # Calculate new phi-time
        current_phi_time = (time.time() * PHI) % 1.0
        
        # Record authentication result if provided
        if authentication_success is not None and similarity_score is not None:
            auth_entry = {
                "timestamp": time.time(),
                "phi_time": current_phi_time,
                "success": authentication_success,
                "similarity": similarity_score,
                "threshold": self.similarity_threshold
            }
            
            self.epigenetic_memory["authentication_history"].append(auth_entry)
            
            # Adjust evolution based on authentication results
            if len(self.epigenetic_memory["authentication_history"]) >= 3:
                recent_auths = self.epigenetic_memory["authentication_history"][-3:]
                success_rate = sum(1 for a in recent_auths if a["success"]) / len(recent_auths)
                
                # If success rate is too high, make authentication stricter
                if success_rate > 0.8:
                    self.similarity_threshold = min(0.8, self.similarity_threshold + 0.02)
                # If success rate is too low, make authentication more lenient
                elif success_rate < 0.3:
                    self.similarity_threshold = max(0.3, self.similarity_threshold - 0.02)
        
        # Evolve complexity based on phi-harmonic principles
        phi_factor = abs(current_phi_time - self.phi_time)
        complexity_change = (PHI * phi_factor - 0.5) * self.mutation_rate
        self.complexity = max(0.5, min(5.0, self.complexity + complexity_change))
        
        # Evolve resonance
        resonance_change = (PHI * current_phi_time - 0.5) * self.mutation_rate
        self.resonance = max(0.1, min(1.0, self.resonance + resonance_change))
        
        # Evolve mutation rate (tends to decrease over time for stability)
        mutation_change = -0.01 * (1 / PHI) * self.mutation_rate
        self.mutation_rate = max(0.01, min(0.2, self.mutation_rate + mutation_change))
        
        # Evolve feature weight
        feature_weight_change = (PHI * phi_factor - 0.5) * self.mutation_rate * 0.5
        self.feature_weight = max(0.2, min(0.8, self.feature_weight + feature_weight_change))
        
        # Evolve temporal factor
        temporal_factor_change = (PHI * current_phi_time - 0.5) * self.mutation_rate * 0.2
        self.temporal_factor = max(0.05, min(0.4, self.temporal_factor + temporal_factor_change))
        
        # Update phi-time
        self.phi_time = current_phi_time
        
        # Add to evolution history
        evolution_entry = {
            "generation": self.generation,
            "timestamp": time.time(),
            "phi_time": self.phi_time,
            "complexity": self.complexity,
            "resonance": self.resonance,
            "mutation_rate": self.mutation_rate,
            "similarity_threshold": self.similarity_threshold,
            "feature_weight": self.feature_weight,
            "temporal_factor": self.temporal_factor
        }
        
        self.epigenetic_memory["evolution_history"].append(evolution_entry)
        
        # Update memory with current parameters
        self.epigenetic_memory["generation"] = self.generation
        self.epigenetic_memory["complexity"] = self.complexity
        self.epigenetic_memory["resonance"] = self.resonance
        self.epigenetic_memory["mutation_rate"] = self.mutation_rate
        self.epigenetic_memory["similarity_threshold"] = self.similarity_threshold
        self.epigenetic_memory["feature_weight"] = self.feature_weight
        self.epigenetic_memory["temporal_factor"] = self.temporal_factor
        
        # Save to file
        memory_path = os.path.join(self.evolution_dir, "epigenetic_memory.json")
        
        # Create a serializable copy of the memory
        serializable_memory = {
            "generation": self.epigenetic_memory["generation"],
            "complexity": float(self.epigenetic_memory["complexity"]),
            "resonance": float(self.epigenetic_memory["resonance"]),
            "mutation_rate": float(self.epigenetic_memory["mutation_rate"]),
            "similarity_threshold": float(self.epigenetic_memory["similarity_threshold"]),
            "feature_weight": float(self.epigenetic_memory["feature_weight"]),
            "temporal_factor": float(self.epigenetic_memory["temporal_factor"]),
            "evolution_history": [],
            "authentication_history": []
        }
        
        # Make sure all values in history are serializable
        for entry in self.epigenetic_memory["evolution_history"]:
            serializable_entry = {}
            for key, value in entry.items():
                serializable_entry[key] = float(value) if isinstance(value, (float, np.float64)) else value
            serializable_memory["evolution_history"].append(serializable_entry)
        
        for entry in self.epigenetic_memory["authentication_history"]:
            serializable_entry = {}
            for key, value in entry.items():
                if key == "success":
                    serializable_entry[key] = bool(value)
                else:
                    serializable_entry[key] = float(value) if isinstance(value, (float, np.float64)) else value
            serializable_memory["authentication_history"].append(serializable_entry)
        
        with open(memory_path, 'w') as f:
            json.dump(serializable_memory, f, indent=2)
        
        print(f"Evolved to Generation {self.generation}:")
        print(f"  Complexity: {self.complexity:.4f}")
        print(f"  Resonance: {self.resonance:.4f}")
        print(f"  Mutation Rate: {self.mutation_rate:.4f}")
        print(f"  Similarity Threshold: {self.similarity_threshold:.4f}")
        print(f"  Feature Weight: {self.feature_weight:.4f}")
        print(f"  Temporal Factor: {self.temporal_factor:.4f}")
        print(f"  Phi-Time: {self.phi_time:.4f}")
    
    def simulate_authentication(self):
        """
        Simulate an authentication attempt with the current parameters.
        
        Returns:
            Tuple: (success, similarity_score)
        """
        # Generate a random base similarity score
        base_similarity = random.uniform(0.3, 0.7)
        
        # Apply phi-harmonic adjustments
        phi_factor = (self.phi_time * PHI) % 1.0
        adjusted_similarity = base_similarity + (phi_factor - 0.5) * 0.2
        
        # Apply feature weight
        weighted_similarity = adjusted_similarity * self.feature_weight + base_similarity * (1 - self.feature_weight)
        
        # Apply temporal factor
        current_phi_time = (time.time() * PHI) % 1.0
        temporal_adjustment = abs(current_phi_time - self.phi_time) * self.temporal_factor
        final_similarity = max(0.0, min(1.0, weighted_similarity - temporal_adjustment))
        
        # Determine success
        success = final_similarity >= self.similarity_threshold
        
        print(f"Authentication {'successful' if success else 'failed'} with similarity {final_similarity:.4f} (threshold: {self.similarity_threshold:.4f})")
        
        return success, final_similarity
    
    def visualize_evolution(self):
        """Visualize the evolution history."""
        if not self.epigenetic_memory["evolution_history"]:
            print("No evolution history available.")
            return
        
        history = self.epigenetic_memory["evolution_history"]
        generations = [entry["generation"] for entry in history]
        complexities = [entry["complexity"] for entry in history]
        resonances = [entry["resonance"] for entry in history]
        mutation_rates = [entry["mutation_rate"] for entry in history]
        similarity_thresholds = [entry["similarity_threshold"] for entry in history]
        
        plt.figure(figsize=(12, 10))
        
        # Plot complexity
        plt.subplot(4, 1, 1)
        plt.plot(generations, complexities, 'b-o', label="Complexity")
        plt.title("Evolution of Complexity")
        plt.xlabel("Generation")
        plt.ylabel("Complexity")
        plt.grid(True, alpha=0.3)
        
        # Plot resonance
        plt.subplot(4, 1, 2)
        plt.plot(generations, resonances, 'g-o', label="Resonance")
        plt.title("Evolution of Resonance")
        plt.xlabel("Generation")
        plt.ylabel("Resonance")
        plt.grid(True, alpha=0.3)
        
        # Plot mutation rate
        plt.subplot(4, 1, 3)
        plt.plot(generations, mutation_rates, 'r-o', label="Mutation Rate")
        plt.title("Evolution of Mutation Rate")
        plt.xlabel("Generation")
        plt.ylabel("Mutation Rate")
        plt.grid(True, alpha=0.3)
        
        # Plot similarity threshold
        plt.subplot(4, 1, 4)
        plt.plot(generations, similarity_thresholds, 'm-o', label="Similarity Threshold")
        plt.title("Evolution of Similarity Threshold")
        plt.xlabel("Generation")
        plt.ylabel("Threshold")
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save the visualization
        vis_path = os.path.join(self.evolution_dir, f"evolution_visualization_gen_{self.generation}.png")
        plt.savefig(vis_path)
        print(f"Saved evolution visualization to {vis_path}")
        
        # Show the plot
        plt.show()
    
    def visualize_authentication_history(self):
        """Visualize the authentication history."""
        if not self.epigenetic_memory["authentication_history"]:
            print("No authentication history available.")
            return
        
        history = self.epigenetic_memory["authentication_history"]
        timestamps = [entry["timestamp"] for entry in history]
        dates = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') for ts in timestamps]
        similarities = [entry["similarity"] for entry in history]
        thresholds = [entry["threshold"] for entry in history]
        successes = [1 if entry["success"] else 0 for entry in history]
        
        plt.figure(figsize=(12, 8))
        
        # Plot similarities and thresholds
        plt.subplot(2, 1, 1)
        plt.plot(range(len(history)), similarities, 'b-o', label="Similarity Score")
        plt.plot(range(len(history)), thresholds, 'r--', label="Threshold")
        plt.title("Authentication Similarity Scores")
        plt.xlabel("Authentication Attempt")
        plt.ylabel("Score")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Plot success/failure
        plt.subplot(2, 1, 2)
        plt.bar(range(len(history)), successes, color=['green' if s else 'red' for s in successes])
        plt.title("Authentication Results")
        plt.xlabel("Authentication Attempt")
        plt.ylabel("Success (1) / Failure (0)")
        plt.yticks([0, 1])
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save the visualization
        vis_path = os.path.join(self.evolution_dir, f"authentication_visualization_gen_{self.generation}.png")
        plt.savefig(vis_path)
        print(f"Saved authentication visualization to {vis_path}")
        
        # Show the plot
        plt.show()
    
    def generate_qr_payload(self):
        """
        Generate a payload that would be encoded in an evolved QR code.
        
        Returns:
            dict: QR code payload
        """
        # Create a payload with evolution data
        payload = {
            "task_type": "display_face_image",
            "timestamp": time.time(),
            "phi_timestamp": time.time() * PHI,
            "evolution": {
                "generation": self.generation,
                "phi_time": round(self.phi_time, 4),
                "complexity": round(self.complexity, 4),
                "resonance": round(self.resonance, 4),
                "mutation_rate": round(self.mutation_rate, 4),
                "similarity_threshold": round(self.similarity_threshold, 4),
                "feature_weight": round(self.feature_weight, 4),
                "temporal_factor": round(self.temporal_factor, 4)
            },
            "evolution_script": "from face_qr_evolution_extension import FaceQREvolutionExtension; ext = FaceQREvolutionExtension(); ext.evolve(); ext.authenticate_with_evolution();"
        }
        
        return payload
    
    def run_evolution_demo(self, generations=10):
        """
        Run a demonstration of the evolution process.
        
        Args:
            generations: Number of generations to simulate
        """
        print(f"\n{'='*60}")
        print(f"FACE-QR EVOLUTION DEMONSTRATION - {generations} GENERATIONS")
        print(f"{'='*60}\n")
        
        print(f"Initial parameters (Generation {self.generation}):")
        print(f"  Complexity: {self.complexity:.4f}")
        print(f"  Resonance: {self.resonance:.4f}")
        print(f"  Mutation Rate: {self.mutation_rate:.4f}")
        print(f"  Similarity Threshold: {self.similarity_threshold:.4f}")
        print(f"  Feature Weight: {self.feature_weight:.4f}")
        print(f"  Temporal Factor: {self.temporal_factor:.4f}")
        print(f"  Phi-Time: {self.phi_time:.4f}")
        
        # Generate initial QR payload
        payload = self.generate_qr_payload()
        print(f"\nGenerated initial QR payload with evolution data:")
        print(json.dumps(payload["evolution"], indent=2))
        
        # Run evolution cycles
        for gen in range(2, generations + 1):
            print(f"\n[Generation {gen}] Simulating authentication and evolution...")
            
            # Simulate authentication
            success, similarity = self.simulate_authentication()
            
            # Evolve based on authentication result
            self.evolve(authentication_success=success, similarity_score=similarity)
            
            # Generate new QR payload
            payload = self.generate_qr_payload()
            print(f"Generated new QR payload for generation {gen}")
        
        # Visualize evolution history
        print("\nVisualizing evolution history...")
        self.visualize_evolution()
        
        # Visualize authentication history
        print("\nVisualizing authentication history...")
        self.visualize_authentication_history()
        
        print(f"\n{'='*60}")
        print(f"EVOLUTION DEMONSTRATION COMPLETE")
        print(f"{'='*60}\n")

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Face-QR Evolution Demonstration")
    parser.add_argument("--generations", type=int, default=10, help="Number of generations to simulate")
    args = parser.parse_args()
    
    # Run the demonstration
    demo = FaceQREvolutionDemo()
    demo.run_evolution_demo(args.generations)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
