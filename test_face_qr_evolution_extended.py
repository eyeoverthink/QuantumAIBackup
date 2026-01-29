#!/usr/bin/env python3
"""
Face QR Evolution Extended Testing

This script runs extended testing of the Face QR Evolution system integrated with
the camera authentication system. It performs multiple evolution cycles to observe
long-term adaptation patterns based on phi-harmonic principles.
"""

import os
import sys
import json
import time
import random
import argparse
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import Image

# Import JSON helper if available
try:
    from face_qr_json_helper import json_dump, json_dumps
    print("Using Face QR JSON Helper for test results serialization")
    USE_JSON_HELPER = True
except ImportError:
    print("Face QR JSON Helper not found, using standard JSON for test results")
    USE_JSON_HELPER = False

# Ensure the current directory is in the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import compatibility layers first to ensure proper class mapping
try:
    import face_qr_compatibility
    print("Loaded Face QR Compatibility Layer")
    
    import qr_task_worker_compatibility
    print("Loaded QR Task Worker Compatibility Layer")
except ImportError as e:
    print(f"Error importing compatibility layers: {e}")
    print("Please ensure you're running from the correct directory.")
    sys.exit(1)

# Import face_qr modules
try:
    from face_qr_evolution_extension import FaceQREvolutionExtension, patch_camera_extension
    from face_qr_camera_extension import FaceQRCameraExtension
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please ensure you're running from the correct directory.")
    sys.exit(1)

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class FaceQREvolutionTester:
    """Test harness for extended Face QR Evolution testing."""
    
    def __init__(self):
        """Initialize the tester."""
        # Apply patches to camera extension
        patch_camera_extension()
        
        # Create output directory
        self.output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evolution_test_results")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Create evolution extension with proper initialization
        try:
            self.evolution_ext = FaceQREvolutionExtension()
            
            # Ensure all required attributes are set with defaults if missing
            if not hasattr(self.evolution_ext, 'similarity_threshold') or self.evolution_ext.similarity_threshold is None:
                self.evolution_ext.similarity_threshold = 0.45
                
            if not hasattr(self.evolution_ext, 'feature_weight') or self.evolution_ext.feature_weight is None:
                self.evolution_ext.feature_weight = 0.5
                
            if not hasattr(self.evolution_ext, 'temporal_factor') or self.evolution_ext.temporal_factor is None:
                self.evolution_ext.temporal_factor = 0.2
                
            if not hasattr(self.evolution_ext, 'complexity') or self.evolution_ext.complexity is None:
                self.evolution_ext.complexity = 1.0
                
            if not hasattr(self.evolution_ext, 'resonance') or self.evolution_ext.resonance is None:
                self.evolution_ext.resonance = 0.5
                
            if not hasattr(self.evolution_ext, 'mutation_rate') or self.evolution_ext.mutation_rate is None:
                self.evolution_ext.mutation_rate = 0.1
                
            if not hasattr(self.evolution_ext, 'generation') or self.evolution_ext.generation is None:
                self.evolution_ext.generation = 1
                
            # Ensure camera extension is initialized
            if not hasattr(self.evolution_ext, 'camera_ext') or self.evolution_ext.camera_ext is None:
                from face_qr_camera_extension import FaceQRCameraExtension
                self.evolution_ext.camera_ext = FaceQRCameraExtension()
                
            print("Successfully initialized evolution extension with required attributes")
        except Exception as e:
            print(f"Error initializing evolution extension: {e}")
            print("Using default values for evolution parameters")
            
            # Create minimal evolution extension with required attributes
            from face_qr_compatibility import FaceQRCore
            self.evolution_ext = FaceQRCore()
            self.evolution_ext.similarity_threshold = 0.45
            self.evolution_ext.feature_weight = 0.5
            self.evolution_ext.temporal_factor = 0.2
            self.evolution_ext.complexity = 1.0
            self.evolution_ext.resonance = 0.5
            self.evolution_ext.mutation_rate = 0.1
            self.evolution_ext.generation = 1
            self.evolution_ext.camera_ext = None
        
        # Testing parameters
        self.current_generation = self.evolution_ext.generation
        self.test_results = []
        
        print(f"Face QR Evolution Tester initialized (starting at generation {self.current_generation})")
    
    def run_extended_test(self, face_image_path, generations=20, interactive=False):
        """
        Run extended evolution testing.
        
        Args:
            face_image_path: Path to face image
            generations: Number of generations to test
            interactive: Whether to run in interactive mode (with camera)
        """
        print(f"\n{'='*60}")
        print(f"FACE-QR EXTENDED EVOLUTION TEST - {generations} GENERATIONS")
        print(f"{'='*60}\n")
        
        print(f"Initial parameters (Generation {self.current_generation}):")
        print(f"  Similarity Threshold: {self.evolution_ext.similarity_threshold:.4f}")
        print(f"  Feature Weight: {self.evolution_ext.feature_weight:.4f}")
        print(f"  Temporal Factor: {self.evolution_ext.temporal_factor:.4f}")
        print(f"  Complexity: {self.evolution_ext.complexity:.4f}")
        print(f"  Resonance: {self.evolution_ext.resonance:.4f}")
        print(f"  Mutation Rate: {self.evolution_ext.mutation_rate:.4f}")
        
        # Generate initial QR code if needed
        qr_path = None
        if not interactive:
            print("\nGenerating initial evolved QR code...")
            _, qr_path = self.evolution_ext.generate_evolved_qr(face_image_path)
            if not qr_path:
                print("Error: Failed to generate initial QR code")
                return False
        
        # Run evolution cycles
        target_generation = self.current_generation + generations
        while self.evolution_ext.generation < target_generation:
            print(f"\n[Generation {self.evolution_ext.generation}] Running evolution cycle...")
            
            if interactive:
                # Run interactive authentication with camera
                print("Starting camera authentication with evolution...")
                success = self.evolution_ext.authenticate_with_evolution(face_image_path=face_image_path)
                
                # Record results
                self._record_test_result(success)
                
                # Wait for user to continue
                input("\nPress Enter to continue to next generation...")
            else:
                # Simulate authentication with random success probability
                # Use phi-harmonic weighting to make success more likely as system evolves
                phi_factor = ((self.evolution_ext.generation * PHI) % 1.0)
                success_probability = 0.5 + (phi_factor - 0.5) * 0.3
                
                # Bias toward success if similarity threshold is lower
                threshold_factor = 1.0 - (self.evolution_ext.similarity_threshold / 0.8)
                success_probability += threshold_factor * 0.2
                
                # Clamp to valid range
                success_probability = max(0.3, min(0.8, success_probability))
                
                # Determine success
                import random
                success = random.random() < success_probability
                
                # Generate similarity score
                if success:
                    similarity = self.evolution_ext.similarity_threshold + random.uniform(0.05, 0.2)
                else:
                    similarity = self.evolution_ext.similarity_threshold - random.uniform(0.05, 0.2)
                
                # Apply evolution
                print(f"Simulated authentication {'successful' if success else 'failed'} with similarity {similarity:.4f}")
                self.evolution_ext.evolve(authentication_success=success, similarity_score=similarity)
                
                # Record results
                self._record_test_result(success, similarity)
                
                # Generate new QR code
                if success:
                    print("Generating new evolved QR code...")
                    _, qr_path = self.evolution_ext.generate_evolved_qr(face_image_path)
        
        # Visualize results
        self._visualize_test_results()
        
        # Save test results
        self._save_test_results()
        
        print(f"\n{'='*60}")
        print(f"EXTENDED EVOLUTION TEST COMPLETE")
        print(f"{'='*60}\n")
        
        return True
    
    def _record_test_result(self, success, similarity=None):
        """Record test result."""
        if similarity is None and hasattr(self.evolution_ext.camera_ext, 'last_similarity_score'):
            similarity = self.evolution_ext.camera_ext.last_similarity_score
        
        result = {
            "generation": self.evolution_ext.generation,
            "timestamp": time.time(),
            "phi_time": (time.time() * PHI) % 1.0,
            "success": success,
            "similarity": similarity,
            "similarity_threshold": self.evolution_ext.similarity_threshold,
            "feature_weight": self.evolution_ext.feature_weight,
            "temporal_factor": self.evolution_ext.temporal_factor,
            "complexity": self.evolution_ext.complexity,
            "resonance": self.evolution_ext.resonance,
            "mutation_rate": self.evolution_ext.mutation_rate
        }
        
        self.test_results.append(result)
    
    def _visualize_test_results(self):
        """Visualize test results."""
        if not self.test_results:
            print("No test results to visualize.")
            return
        
        # Extract data
        generations = [r["generation"] for r in self.test_results]
        thresholds = [r["similarity_threshold"] for r in self.test_results]
        similarities = [r.get("similarity", 0) for r in self.test_results]
        successes = [1 if r["success"] else 0 for r in self.test_results]
        complexities = [r["complexity"] for r in self.test_results]
        resonances = [r["resonance"] for r in self.test_results]
        mutation_rates = [r["mutation_rate"] for r in self.test_results]
        
        # Create figure
        plt.figure(figsize=(14, 12))
        
        # Plot authentication results
        plt.subplot(4, 1, 1)
        plt.plot(generations, similarities, 'b-o', label="Similarity")
        plt.plot(generations, thresholds, 'r--', label="Threshold")
        plt.title("Authentication Results Over Generations")
        plt.xlabel("Generation")
        plt.ylabel("Score")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Plot success/failure
        plt.subplot(4, 1, 2)
        plt.bar(generations, successes, color=['green' if s else 'red' for s in successes])
        plt.title("Authentication Success/Failure")
        plt.xlabel("Generation")
        plt.ylabel("Success (1) / Failure (0)")
        plt.yticks([0, 1])
        plt.grid(True, alpha=0.3)
        
        # Plot complexity and resonance
        plt.subplot(4, 1, 3)
        plt.plot(generations, complexities, 'g-o', label="Complexity")
        plt.plot(generations, resonances, 'm-o', label="Resonance")
        plt.title("Evolution of Complexity and Resonance")
        plt.xlabel("Generation")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Plot mutation rate
        plt.subplot(4, 1, 4)
        plt.plot(generations, mutation_rates, 'c-o', label="Mutation Rate")
        plt.title("Evolution of Mutation Rate")
        plt.xlabel("Generation")
        plt.ylabel("Rate")
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        vis_path = os.path.join(self.output_dir, f"evolution_test_results_{timestamp}.png")
        plt.savefig(vis_path)
        print(f"\nSaved test results visualization to {vis_path}")
        
        # Show plot
        plt.show()
    
    def _save_test_results(self):
        """Save test results to file."""
        # Create results dictionary
        results = {
            "test_date": datetime.now().isoformat(),
            "initial_generation": self.current_generation,
            "final_generation": self.evolution_ext.generation,
            "results": []
        }
        
        # Process test results to ensure they're JSON serializable
        for result in self.test_results:
            processed_result = {}
            for key, value in result.items():
                # Handle numpy types
                if hasattr(value, 'item') and callable(getattr(value, 'item')):
                    processed_result[key] = value.item()
                # Handle boolean values
                elif isinstance(value, bool):
                    processed_result[key] = bool(value)
                # Handle other types
                else:
                    processed_result[key] = value
            results["results"].append(processed_result)
        
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_path = os.path.join(self.output_dir, f"evolution_test_results_{timestamp}.json")
        
        with open(results_path, 'w') as f:
            if USE_JSON_HELPER:
                json_dump(results, f, indent=2)
            else:
                # Use a custom default handler for non-serializable types
                def default_handler(obj):
                    if hasattr(obj, 'item') and callable(getattr(obj, 'item')):
                        return obj.item()
                    if isinstance(obj, np.ndarray):
                        return obj.tolist()
                    if isinstance(obj, datetime):
                        return obj.isoformat()
                    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
                
                json.dump(results, f, indent=2, default=default_handler)
        
        print(f"Saved test results to {results_path}")
    
    def analyze_adaptation_patterns(self):
        """Analyze adaptation patterns from test results."""
        if not self.test_results:
            print("No test results to analyze.")
            return
        
        print("\nAnalyzing adaptation patterns...")
        
        # Calculate success rate over time
        window_size = min(5, len(self.test_results))
        success_rates = []
        
        for i in range(len(self.test_results) - window_size + 1):
            window = self.test_results[i:i+window_size]
            success_count = sum(1 for r in window if r["success"])
            success_rate = success_count / window_size
            success_rates.append(success_rate)
        
        # Calculate threshold adaptation rate
        threshold_changes = []
        for i in range(1, len(self.test_results)):
            prev = self.test_results[i-1]["similarity_threshold"]
            curr = self.test_results[i]["similarity_threshold"]
            threshold_changes.append(curr - prev)
        
        # Calculate phi-harmonic resonance
        phi_resonances = []
        for i in range(len(self.test_results)):
            phi_time = self.test_results[i]["phi_time"]
            # Calculate resonance with golden ratio
            resonance = abs(((phi_time * PHI) % 1.0) - 0.5) * 2.0
            phi_resonances.append(resonance)
        
        # Print analysis
        print("\nAdaptation Analysis:")
        print(f"  Total generations tested: {len(self.test_results)}")
        print(f"  Overall success rate: {sum(1 for r in self.test_results if r['success']) / len(self.test_results):.2f}")
        print(f"  Final similarity threshold: {self.test_results[-1]['similarity_threshold']:.4f}")
        print(f"  Threshold adaptation: {sum(abs(c) for c in threshold_changes) / len(threshold_changes):.4f} avg change per generation")
        print(f"  Phi-harmonic resonance: {sum(phi_resonances) / len(phi_resonances):.4f} avg resonance")
        
        # Visualize adaptation patterns
        plt.figure(figsize=(12, 8))
        
        # Plot success rate over time
        plt.subplot(3, 1, 1)
        plt.plot(range(len(success_rates)), success_rates, 'b-')
        plt.title(f"Success Rate Over Time (Window Size: {window_size})")
        plt.xlabel("Generation")
        plt.ylabel("Success Rate")
        plt.ylim(0, 1)
        plt.grid(True, alpha=0.3)
        
        # Plot threshold changes
        plt.subplot(3, 1, 2)
        plt.plot(range(1, len(self.test_results)), threshold_changes, 'r-')
        plt.title("Threshold Adaptation")
        plt.xlabel("Generation")
        plt.ylabel("Threshold Change")
        plt.grid(True, alpha=0.3)
        
        # Plot phi-harmonic resonance
        plt.subplot(3, 1, 3)
        plt.plot(range(len(phi_resonances)), phi_resonances, 'g-')
        plt.title("Phi-Harmonic Resonance")
        plt.xlabel("Generation")
        plt.ylabel("Resonance")
        plt.ylim(0, 1)
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        vis_path = os.path.join(self.output_dir, f"adaptation_analysis_{timestamp}.png")
        plt.savefig(vis_path)
        print(f"\nSaved adaptation analysis to {vis_path}")
        
        # Show plot
        plt.show()

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Face QR Evolution Extended Testing")
    parser.add_argument("--face", required=True, help="Path to face image")
    parser.add_argument("--generations", type=int, default=20, help="Number of generations to test")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode with camera")
    args = parser.parse_args()
    
    # Check if face image exists
    if not os.path.exists(args.face):
        print(f"Error: Face image not found at {args.face}")
        return 1
    
    # Create tester and run extended test
    tester = FaceQREvolutionTester()
    tester.run_extended_test(args.face, args.generations, args.interactive)
    
    # Analyze adaptation patterns
    tester.analyze_adaptation_patterns()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
