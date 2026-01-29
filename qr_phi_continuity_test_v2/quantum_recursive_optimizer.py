"""
Quantum Recursive Self-Optimizer
Implements φ-harmonic coherence monitoring and self-improvement feedback loops
Integrates with QuantumFourierCalculator for dynamic parameter optimization
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from pathlib import Path
import sys

# Import existing quantum system components
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from quantum_fourier_calculator import QuantumFourierCalculator

class QuantumRecursiveOptimizer:
    def __init__(self, history_file="phi_optimization_history.json"):
        self.phi = (1 + np.sqrt(5)) / 2
        self.history_path = Path(history_file)
        self.optimization_history = self._load_history()
        self.qfc = QuantumFourierCalculator()
        self.coherence_threshold = 1 - (1 / (self.phi**500))  # High threshold
        self.resonance_drift_max = 1 / (self.phi**20)  # Maximum allowed drift
        
        # Parameter search spaces
        self.base_freq_range = (4.0, 5.0)  # Hz
        self.resonance_range = (0.9, 0.99)
        self.N_options = [2**n for n in range(10, 18)]  # 1K to 256K states
        
        # Learning rate decreases with iterations for convergence
        self.learning_rate = 1 / self.phi
        self.iteration = len(self.optimization_history) + 1
        
    def _load_history(self):
        """Load optimization history or create new if not exists"""
        if self.history_path.exists():
            try:
                with open(self.history_path, 'r') as f:
                    history = json.load(f)
                    print(f"📚 Loaded {len(history)} previous optimization records")
                    return history
            except json.JSONDecodeError:
                print("⚠️ History file corrupted, creating new history")
                return []
        else:
            print("📝 No history file found, creating new optimization history")
            return []
            
    def _save_history(self):
        """Save optimization history to file"""
        # Convert numpy types to native Python types for JSON serialization
        serializable_history = []
        for entry in self.optimization_history:
            serializable_entry = {}
            for k, v in entry.items():
                if isinstance(v, (np.integer, np.floating, np.ndarray)):
                    serializable_entry[k] = float(v)  # Convert to native float
                elif isinstance(v, dict):
                    # Handle nested dictionaries (like coherence_metrics)
                    serializable_entry[k] = {}
                    for mk, mv in v.items():
                        if isinstance(mv, (np.integer, np.floating, np.ndarray)):
                            serializable_entry[k][mk] = float(mv)
                        else:
                            serializable_entry[k][mk] = mv
                else:
                    serializable_entry[k] = v
            serializable_history.append(serializable_entry)
            
        with open(self.history_path, 'w') as f:
            json.dump(serializable_history, f, indent=2)
            
    def measure_coherence(self, base_freq, resonance, N):
        """Measure φ-harmonic coherence with given parameters"""
        # Store original parameters
        orig_base_freq = self.qfc.base_freq
        orig_resonance = self.qfc.resonance
        
        # Set test parameters
        self.qfc.base_freq = base_freq
        self.qfc.resonance = resonance
        
        # Initialize quantum state
        psi = self.qfc.initialize_state(N)
        
        # Compute QFT
        qft = self.qfc.quantum_fourier_transform(psi)
        
        # Calculate φ-resonance metrics
        # 1. Phi-alignment: how close frequency components align with φ-harmonics
        freqs = np.fft.fftfreq(len(qft))
        phi_harmonics = np.array([self.phi**n % 1 for n in range(1, 9)])  # First 8 φ harmonics
        
        # Calculate minimum distance to any φ-harmonic for each frequency
        phi_distances = []
        for freq_val in np.abs(freqs[:len(freqs)//2]):
            if freq_val > 0:  # Skip DC component
                min_dist = min([abs((freq_val * self.phi) % 1 - h) for h in phi_harmonics])
                phi_distances.append(min_dist)
        
        # Average alignment with φ-harmonics (lower distance = better alignment)
        phi_alignment = 1 - (np.mean(phi_distances) if phi_distances else 0)
        
        # 2. Amplitude stability - weighted by φ
        amplitudes = np.abs(qft)
        sorted_indices = np.argsort(amplitudes)[::-1]  # Sort by amplitude, descending
        top_indices = sorted_indices[:int(len(qft)/self.phi)]  # Take top φ-ratio of components
        amplitude_stability = 1 - np.std(amplitudes[top_indices]) / (np.mean(amplitudes[top_indices]) + 1e-10)
        
        # 3. Phase coherence - check if phases follow φ-harmonic progression
        phases = np.angle(qft[top_indices]) / (2 * np.pi)  # Normalize to [0,1]
        phase_diffs = np.diff(phases)
        phase_coherence = 1 - np.std(phase_diffs) / (self.phi / 10)  # Scale by φ/10
        phase_coherence = max(0, min(1, phase_coherence))  # Clamp to [0,1]
        
        # 4. Resonance quality - check energy concentration at φ-harmonic frequencies
        energy_total = np.sum(amplitudes**2)
        phi_indices = [int(len(qft) * (h % 1)) for h in phi_harmonics if h < 1]
        phi_energy = np.sum(amplitudes[phi_indices]**2) if phi_indices else 0
        resonance_quality = (phi_energy / energy_total) * self.phi if energy_total > 0 else 0
        resonance_quality = min(1, resonance_quality)  # Cap at 1
        
        # Calculate φ-weighted coherence score - using golden ratio weighting
        coherence_score = (
            phi_alignment * self.phi**3 + 
            amplitude_stability * self.phi**2 + 
            phase_coherence * self.phi + 
            resonance_quality
        ) / (self.phi**3 + self.phi**2 + self.phi + 1)
        
        # Restore original parameters
        self.qfc.base_freq = orig_base_freq
        self.qfc.resonance = orig_resonance
        
        return coherence_score, {
            "phi_alignment": float(phi_alignment),
            "amplitude_stability": float(amplitude_stability),
            "phase_coherence": float(phase_coherence),
            "resonance_quality": float(resonance_quality)
        }
        
    def _generate_parameter_candidates(self, current_best):
        """Generate candidate parameters for testing"""
        base_freq = current_best.get("base_freq", self.qfc.base_freq)
        resonance = current_best.get("resonance", self.qfc.resonance)
        N = current_best.get("N", 2**16)
        
        # Calculate exploration radius that decreases with iterations
        exploration_radius = 1 / (self.phi * self.iteration**0.5)
        
        candidates = []
        
        # Generate candidates with φ-harmonic perturbations
        for i in range(5):  # Test 5 candidates per iteration
            # φ-weighted perturbation
            freq_perturbation = (np.random.random() - 0.5) * exploration_radius * self.phi
            res_perturbation = (np.random.random() - 0.5) * exploration_radius / self.phi
            
            # New parameters with φ-harmonic constraints
            new_base_freq = base_freq + freq_perturbation
            new_base_freq = max(self.base_freq_range[0], min(self.base_freq_range[1], new_base_freq))
            
            new_resonance = resonance + res_perturbation
            new_resonance = max(self.resonance_range[0], min(self.resonance_range[1], new_resonance))
            
            # Occasionally try different N values
            if np.random.random() < 0.3:
                new_N = np.random.choice([n for n in self.N_options if n != N])
            else:
                new_N = N
                
            candidates.append({
                "base_freq": new_base_freq,
                "resonance": new_resonance,
                "N": new_N
            })
            
        return candidates
        
    def optimize_parameters(self, iterations=5):
        """Run optimization loop for specified iterations"""
        print("\n🔄 Quantum Recursive Self-Optimization")
        print("=" * 50)
        
        start_time = datetime.now()
        
        # Get current best parameters
        if self.optimization_history:
            current_best = self.optimization_history[-1]
        else:
            # Start with default parameters and measure initial coherence
            initial_coherence, initial_metrics = self.measure_coherence(
                self.qfc.base_freq, 
                self.qfc.resonance, 
                2**16
            )
            
            current_best = {
                "base_freq": self.qfc.base_freq,
                "resonance": self.qfc.resonance,
                "N": 2**16,
                "coherence_score": initial_coherence,
                "coherence_metrics": initial_metrics,
                "timestamp": str(datetime.now())
            }
            
            # Save initial state to history
            self.optimization_history.append(current_best)
            self._save_history()
            
        print(f"\n📊 Starting Parameters")
        print("-" * 30)
        print(f"Base Frequency: {current_best['base_freq']:.6f} Hz")
        print(f"Resonance: {current_best['resonance']:.6f}")
        print(f"States (N): {current_best['N']:,}")
        if 'coherence_score' in current_best:
            print(f"Coherence Score: {current_best['coherence_score']:.15f}")
            
        improvement_found = False
        coherence_history = []
        
        for i in range(iterations):
            self.iteration = len(self.optimization_history) + i + 1
            self.learning_rate = 1 / (self.phi * self.iteration**0.5)
            
            print(f"\n🔍 Iteration {i+1}/{iterations}")
            print(f"Learning Rate: {self.learning_rate:.6f}")
            
            # Generate candidate parameters
            candidates = self._generate_parameter_candidates(current_best)
            
            best_candidate = None
            best_coherence = current_best.get("coherence_score", 0)
            
            # Evaluate all candidates
            for j, candidate in enumerate(candidates):
                coherence_score, metrics = self.measure_coherence(
                    candidate["base_freq"], 
                    candidate["resonance"], 
                    candidate["N"]
                )
                
                print(f"  Candidate {j+1}: Score={coherence_score:.6f}, " + 
                      f"Freq={candidate['base_freq']:.6f}, " +
                      f"Res={candidate['resonance']:.6f}, " +
                      f"N={candidate['N']:,}")
                
                # Check if this candidate is better
                if coherence_score > best_coherence:
                    best_coherence = coherence_score
                    best_candidate = candidate.copy()
                    best_candidate["coherence_score"] = coherence_score
                    best_candidate["coherence_metrics"] = metrics
                    best_candidate["timestamp"] = str(datetime.now())
                    improvement_found = True
                    
            # Update current best if improvement found
            if best_candidate:
                current_best = best_candidate
                self.optimization_history.append(current_best)
                self._save_history()
                
                print(f"\n✨ Improvement Found!")
                print(f"New Coherence Score: {current_best['coherence_score']:.15f}")
            else:
                print("\n🔄 No improvement in this iteration")
                
            # Track coherence for plotting
            coherence_history.append(current_best["coherence_score"])
            
            # Check if we've reached optimal coherence
            if current_best["coherence_score"] > self.coherence_threshold:
                print(f"\n🎯 Optimal coherence threshold reached!")
                break
                
        # Apply the best parameters to the calculator
        self.qfc.base_freq = current_best["base_freq"]
        self.qfc.resonance = current_best["resonance"]
        
        # Calculate total improvement
        total_duration = (datetime.now() - start_time).total_seconds()
        initial_score = self.optimization_history[0]["coherence_score"] if self.optimization_history else 0
        final_score = current_best["coherence_score"]
        improvement_pct = ((final_score - initial_score) / max(initial_score, 1e-10)) * 100
        
        print("\n📈 Optimization Results")
        print("-" * 30)
        print(f"Initial Coherence: {initial_score:.15f}")
        print(f"Final Coherence: {final_score:.15f}")
        print(f"Improvement: {improvement_pct:.2f}%")
        print(f"Time Taken: {total_duration:.2f} seconds")
        
        # Plot optimization progress
        self._plot_optimization_progress(coherence_history)
        
        return current_best
        
    def _plot_optimization_progress(self, coherence_history):
        """Plot the optimization progress"""
        plt.figure(figsize=(12, 6))
        
        # Plot coherence score progress
        plt.subplot(1, 2, 1)
        plt.plot(range(1, len(coherence_history) + 1), coherence_history, 'b-o')
        plt.title('φ-Harmonic Coherence Optimization')
        plt.xlabel('Iteration')
        plt.ylabel('Coherence Score')
        plt.grid(True)
        
        # Plot parameter evolution if we have history
        if len(self.optimization_history) > 1:
            plt.subplot(1, 2, 2)
            
            iterations = range(1, len(self.optimization_history) + 1)
            base_freqs = [entry["base_freq"] for entry in self.optimization_history]
            resonances = [entry["resonance"] for entry in self.optimization_history]
            
            plt.plot(iterations, base_freqs, 'r-o', label='Base Frequency')
            plt.plot(iterations, resonances, 'g-o', label='Resonance')
            plt.title('Parameter Evolution')
            plt.xlabel('Optimization Step')
            plt.ylabel('Parameter Value')
            plt.legend()
            plt.grid(True)
            
        plt.tight_layout()
        plt.savefig('quantum_optimization_progress.png')
        plt.close()
        
    def apply_optimized_parameters(self):
        """Apply the best parameters to the quantum system"""
        if not self.optimization_history:
            print("⚠️ No optimization history available")
            return False
            
        best_params = self.optimization_history[-1]
        
        print("\n🔧 Applying Optimized Parameters")
        print("-" * 30)
        print(f"Base Frequency: {best_params['base_freq']:.6f} Hz")
        print(f"Resonance: {best_params['resonance']:.6f}")
        print(f"Recommended N: {best_params['N']:,}")
        
        # Apply parameters to calculator
        self.qfc.base_freq = best_params["base_freq"]
        self.qfc.resonance = best_params["resonance"]
        
        return True
        
    def run_optimized_qft(self):
        """Run QFT with optimized parameters"""
        # Apply best parameters
        if self.apply_optimized_parameters():
            # Run the QFT calculation
            self.qfc.run_qft_calculation()
        else:
            print("⚠️ Running with default parameters")
            self.qfc.run_qft_calculation()

def main():
    print("\n🌟 Quantum Recursive Self-Improvement Loop")
    print("=" * 50)
    print("This module monitors φ-harmonic coherence and dynamically")
    print("adjusts parameters to optimize QFT fidelity over time.")
    
    optimizer = QuantumRecursiveOptimizer()
    
    # Run optimization
    optimizer.optimize_parameters(iterations=5)
    
    # Run QFT with optimized parameters
    optimizer.run_optimized_qft()
    
if __name__ == "__main__":
    main()
