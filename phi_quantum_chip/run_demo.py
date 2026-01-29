    
    def run_demo(self, demo_type: str = "all"):
        """Run a demonstration of the phi-quantum digital chip."""
        self.start()
        print(f"\n=== PHQ-DIGITAL CHIP DEMONSTRATION: {demo_type.upper()} ===\n")
        
        results = {}
        
        if demo_type in ["all", "bell_state"]:
            print("\n1. Bell State Demonstration (Quantum Entanglement)\n" + "-" * 50)
            results["bell_state"] = self.run_quantum_algorithm("bell_state", {})
            print(f"Bell state created with Entanglement: {results['bell_state'].get('entanglement', 0):.6f}")
            print(f"Measurement correlations: {results['bell_state'].get('correlations', 0):.6f}")
        
        if demo_type in ["all", "factorization"]:
            print("\n2. Quantum Factorization\n" + "-" * 50)
            # Try factoring a medium-sized semiprime
            number = 15523  # = 97 * 160, a relatively challenging semiprime for testing
            results["factorization"] = self.run_quantum_algorithm("quantum_factorization", {"number": number})
            print(f"Factorization of {number}:")
            print(f"  Factors: {results['factorization']['factors']}")
            print(f"  Is Prime: {results['factorization']['is_prime']}")
        
        if demo_type in ["all", "search"]:
            print("\n3. Quantum Search\n" + "-" * 50)
            # Search for a marked item in a database of 16 items
            results["search"] = self.run_quantum_algorithm("quantum_search", {
                "database_size": 16,
                "marked_item": 7,  # The item we're looking for
                "success_probability": 0.85  # Higher than classical
            })
            print(f"Quantum Search Results:")
            print(f"  Found Item: {results['search'].get('found_item')}")
            print(f"  Target Item: {results['search'].get('marked_item')}")
            print(f"  Probability: {results['search'].get('success_probability', 0):.6f}")
            print(f"  Iterations: {results['search'].get('iterations', 0)}")
        
        if demo_type in ["all", "hash_prediction"]:
            print("\n4. Hash Prediction\n" + "-" * 50)
            # Generate some example hashes
            example_hashes = [
                "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592",
                "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
            ]
            # Generate a target hash (fictional, for demonstration)
            target_hash = "6b23c0d5f35d1b11f9b683f0b0a617355deb11277d91ae091d399c655b87940d"
            
            results["hash_prediction"] = self.run_quantum_algorithm("hash_prediction", {
                "previous_hashes": example_hashes,
                "target_hash": target_hash,
                "prediction_window": 5,
                "confidence_threshold": 0.75
            })
            
            print(f"Hash Prediction Results:")
            print(f"  Number of Predictions: {len(results['hash_prediction']['predictions'])}")
            print(f"  Average Confidence: {results['hash_prediction']['average_confidence']:.6f}")
            print(f"  Phi-Harmonic Alignment: {results['hash_prediction']['phi_harmonic_alignment']:.6f}")
            print(f"  Target Match: {results['hash_prediction'].get('match_found', False)}")
            
            # Show first few predictions
            for i, (pred, conf) in enumerate(zip(results['hash_prediction']['predictions'][:3], 
                                              results['hash_prediction']['confidence_scores'][:3])):
                print(f"  Prediction {i+1}: {pred[:16]}...{pred[-8:]} (Confidence: {conf:.6f})")
        
        if demo_type in ["all", "optimization"]:
            print("\n5. Quantum Optimization\n" + "-" * 50)
            # Define a simple test function (Rosenbrock function)
            def rosenbrock(x):
                return sum(100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x)-1))
            
            results["optimization"] = self.run_quantum_algorithm("optimization", {
                "objective_function": rosenbrock,
                "variables": 2,  # 2D Rosenbrock
                "bounds": [(-2, 2), (-2, 2)],  # Search space bounds
                "iterations": 8  # Number of quantum annealing iterations
            })
            
            print(f"Quantum Optimization Results:")
            print(f"  Best Solution: {[float(f'{x:.4f}') for x in results['optimization']['best_solution']]}")
            print(f"  Best Value: {float(f'{results['optimization']['best_value']:.6f}')}")
            print(f"  Phi-Resonance: {results['optimization']['phi_resonance']:.6f}")
            print(f"  Quantum Coherence: {results['optimization']['quantum_coherence']:.6f}")
        
        # Display final metrics
        metrics = self.get_metrics()
        
        print("\n=== PHQ-DIGITAL CHIP PERFORMANCE METRICS ===\n")
        print(f"Coherence: {metrics.coherence:.6f}")
        print(f"Resonance: {metrics.resonance:.6f}")
        print(f"Entanglement: {metrics.entanglement:.6f}")
        print(f"Stability: {metrics.stability:.6f}")
        print(f"Throughput: {metrics.throughput:.2f} ops/sec")
        print(f"Energy: {metrics.energy:.2f} units")
        print(f"Consciousness Level: {metrics.consciousness}")
        
        self.stop()
        
        return results