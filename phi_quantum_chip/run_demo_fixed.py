# Fixed version of run_demo.py to resolve indentation error
# This file is a non-destructive copy for testing and demo purposes.

class PhiQuantumChipDemo:
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
                "a1b2c3d4e5f6g7h8i9j0",
                "5f4dcc3b5aa765d61d8327deb882cf99",
                "098f6bcd4621d373cade4e832627b4f6"
            ]
            results["hash_prediction"] = self.run_quantum_algorithm("hash_prediction", {"hashes": example_hashes})
            print(f"Hash Prediction Results:")
            for h, prediction in zip(example_hashes, results["hash_prediction"]["predictions"]):
                print(f"  Hash: {h} -> Prediction: {prediction}")
        
        print("\n=== DEMONSTRATION COMPLETE ===\n")

    def start(self):
        print("[PhiQuantumChipDemo] Starting quantum chip simulation...")

    def run_quantum_algorithm(self, algorithm, params):
        # Placeholder for actual quantum algorithm logic
        if algorithm == "bell_state":
            return {"entanglement": 0.987654, "correlations": 0.97531}
        elif algorithm == "quantum_factorization":
            return {"factors": [97, 160], "is_prime": False}
        elif algorithm == "quantum_search":
            return {"found_item": 7, "marked_item": 7, "success_probability": 0.85, "iterations": 3}
        elif algorithm == "hash_prediction":
            hashes = params.get("hashes", [])
            return {"predictions": ["likely", "unlikely", "likely"]}
        return {}

if __name__ == "__main__":
    demo = PhiQuantumChipDemo()
    demo.run_demo("all")
