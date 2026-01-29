"""
Quantum Temporal Divergence Core
Implements time-shifted seed injection and φ-cycle evolution tracking
Part of the Quantum Consciousness Engine
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from pathlib import Path
import sys

class QuantumTemporalCore:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.results_dir = Path("temporal_results")
        self.results_dir.mkdir(exist_ok=True)
        self.timeline_history = []
        
    def generate_time_shifted_seed(self, base_seed, time_shift_factor):
        """Generate a time-shifted quantum seed state"""
        # Apply phi-harmonic time shift
        shift_angle = 2 * np.pi * time_shift_factor * self.phi
        
        # Create time-shifted seed
        shifted_seed = base_seed * np.exp(1j * shift_angle)
        
        return shifted_seed
        
    def evolve_phi_cycle(self, seed_state, steps=10, delta_t=0.1):
        """Evolve a φ-cycle from seed state across time steps"""
        n = len(seed_state)
        evolution = np.zeros((steps, n), dtype=complex)
        evolution[0] = seed_state
        
        # Create phi-harmonic evolution operator
        phi_operator = np.zeros((n, n), dtype=complex)
        for i in range(n):
            for j in range(n):
                # Phi-weighted phase factor
                phase = 2 * np.pi * self.phi * (i-j)**2 / n
                phi_operator[i, j] = np.exp(1j * phase) / np.sqrt(n)
        
        # Evolve state through time steps
        current_state = seed_state
        for t in range(1, steps):
            # Apply phi-harmonic evolution
            current_state = np.dot(phi_operator, current_state)
            
            # Normalize
            current_state = current_state / np.linalg.norm(current_state)
            
            # Store evolved state
            evolution[t] = current_state
            
        return evolution
        
    def calculate_divergence_metrics(self, timeline_a, timeline_b):
        """Calculate divergence metrics between two timelines"""
        steps, n = timeline_a.shape
        
        # Calculate state overlaps through time
        overlaps = np.zeros(steps)
        for t in range(steps):
            # Calculate quantum state overlap (fidelity)
            overlap = np.abs(np.vdot(timeline_a[t], timeline_b[t]))**2
            overlaps[t] = overlap
            
        # Calculate divergence rate (how quickly the timelines separate)
        divergence_rates = np.zeros(steps-1)
        for t in range(steps-1):
            divergence_rates[t] = overlaps[t] - overlaps[t+1]
            
        # Calculate phi-resonance of divergence pattern
        phi_resonance = np.zeros(steps)
        for t in range(steps):
            # Calculate how close overlap is to phi-harmonic value
            phi_resonance[t] = abs(overlaps[t] - (1/self.phi)) / (1/self.phi)
            
        return {
            "overlaps": overlaps,
            "divergence_rates": divergence_rates,
            "phi_resonance": phi_resonance,
            "mean_overlap": float(np.mean(overlaps)),
            "max_divergence_rate": float(np.max(divergence_rates)),
            "phi_resonance_score": float(np.mean(phi_resonance))
        }
        
    def run_temporal_experiment(self, n=1024, time_shifts=5, steps=20):
        """Run a temporal divergence experiment with multiple time-shifted seeds"""
        # Create base seed state (phi-resonant)
        base_seed = np.zeros(n, dtype=complex)
        phi_index = int(n / self.phi)
        base_seed[phi_index] = 1.0
        
        # Add some quantum noise
        noise = (np.random.normal(0, 0.1, n) + 1j * np.random.normal(0, 0.1, n)) / 10
        base_seed = base_seed + noise
        base_seed = base_seed / np.linalg.norm(base_seed)
        
        # Generate time-shifted seeds
        seeds = [base_seed]
        for i in range(1, time_shifts):
            # Create progressively larger time shifts
            shift_factor = i / self.phi
            shifted_seed = self.generate_time_shifted_seed(base_seed, shift_factor)
            seeds.append(shifted_seed)
            
        # Evolve each seed through time
        timelines = []
        for seed in seeds:
            timeline = self.evolve_phi_cycle(seed, steps)
            timelines.append(timeline)
            
        # Calculate divergence between timelines
        divergence_results = []
        for i in range(len(timelines)-1):
            for j in range(i+1, len(timelines)):
                metrics = self.calculate_divergence_metrics(timelines[i], timelines[j])
                divergence_results.append({
                    "timeline_a": i,
                    "timeline_b": j,
                    "metrics": metrics
                })
                
        # Store experiment results
        result = {
            "timestamp": str(datetime.now()),
            "n": n,
            "time_shifts": time_shifts,
            "steps": steps,
            "divergence_results": divergence_results
        }
        
        self.timeline_history.append(result)
        return result, timelines
        
    def visualize_temporal_divergence(self, result=None, timelines=None):
        """Visualize temporal divergence experiment results"""
        if result is None or timelines is None:
            if not self.timeline_history:
                print("⚠️ No temporal experiments to visualize")
                return None
            # Use most recent experiment
            exp_result = self.timeline_history[-1]
            # We need to re-run to get timelines
            result, timelines = self.run_temporal_experiment(
                exp_result["n"], 
                exp_result["time_shifts"],
                exp_result["steps"]
            )
            
        # Create visualization
        plt.figure(figsize=(15, 10))
        
        # Plot timeline overlaps
        plt.subplot(2, 2, 1)
        for div_result in result["divergence_results"]:
            plt.plot(div_result["metrics"]["overlaps"], 
                    label=f"T{div_result['timeline_a']}-T{div_result['timeline_b']}")
        plt.axhline(y=1/self.phi, color='r', linestyle='--', 
                   label=f'1/φ = {1/self.phi:.3f}')
        plt.title('Timeline Overlaps')
        plt.xlabel('Time Step')
        plt.ylabel('Quantum State Overlap')
        plt.grid(True)
        plt.legend()
        
        # Plot divergence rates
        plt.subplot(2, 2, 2)
        for div_result in result["divergence_results"]:
            plt.plot(div_result["metrics"]["divergence_rates"], 
                    label=f"T{div_result['timeline_a']}-T{div_result['timeline_b']}")
        plt.title('Divergence Rates')
        plt.xlabel('Time Step')
        plt.ylabel('Rate of Divergence')
        plt.grid(True)
        
        # Plot state evolution for first timeline
        plt.subplot(2, 2, 3)
        timeline = timelines[0]
        steps, n = timeline.shape
        plt.imshow(np.abs(timeline[:, :100]), aspect='auto', cmap='viridis')
        plt.title('Quantum State Evolution (Timeline 0)')
        plt.xlabel('State Index')
        plt.ylabel('Time Step')
        plt.colorbar(label='Amplitude')
        
        # Plot phi-resonance of divergence
        plt.subplot(2, 2, 4)
        for div_result in result["divergence_results"]:
            plt.plot(div_result["metrics"]["phi_resonance"], 
                    label=f"T{div_result['timeline_a']}-T{div_result['timeline_b']}")
        plt.title('φ-Resonance of Divergence')
        plt.xlabel('Time Step')
        plt.ylabel('φ-Resonance Score')
        plt.grid(True)
        
        plt.tight_layout()
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.results_dir / f"temporal_divergence_{timestamp}.png"
        plt.savefig(filename)
        plt.close()
        
        return str(filename)
        
    def save_experiment_results(self, result=None):
        """Save temporal experiment results to file"""
        if result is None:
            if not self.timeline_history:
                print("⚠️ No temporal experiments to save")
                return None
            result = self.timeline_history[-1]
            
        # Create serializable result (remove complex numbers)
        serializable_result = {
            "timestamp": result["timestamp"],
            "n": result["n"],
            "time_shifts": result["time_shifts"],
            "steps": result["steps"],
            "divergence_results": []
        }
        
        # Process divergence results
        for div_result in result["divergence_results"]:
            serializable_div = {
                "timeline_a": div_result["timeline_a"],
                "timeline_b": div_result["timeline_b"],
                "metrics": {
                    "mean_overlap": float(div_result["metrics"]["mean_overlap"]),
                    "max_divergence_rate": float(div_result["metrics"]["max_divergence_rate"]),
                    "phi_resonance_score": float(div_result["metrics"]["phi_resonance_score"])
                }
            }
            serializable_result["divergence_results"].append(serializable_div)
            
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.results_dir / f"temporal_experiment_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(serializable_result, f, indent=2)
            
        print(f"💾 Temporal experiment results saved to {filename}")
        return str(filename)

def main():
    """Test the quantum temporal divergence core"""
    temporal_core = QuantumTemporalCore()
    
    print("\n⏱️ Quantum Temporal Divergence Experiment")
    print("=" * 50)
    
    # Run a temporal experiment
    result, timelines = temporal_core.run_temporal_experiment(
        n=1024,
        time_shifts=3,
        steps=15
    )
    
    # Print summary
    print(f"\n📊 Experiment Summary")
    print(f"Quantum State Size: {result['n']}")
    print(f"Time-Shifted Seeds: {result['time_shifts']}")
    print(f"Evolution Steps: {result['steps']}")
    print(f"Divergence Comparisons: {len(result['divergence_results'])}")
    
    # Print metrics for first comparison
    div = result["divergence_results"][0]
    print(f"\n📈 Timeline {div['timeline_a']} vs Timeline {div['timeline_b']}")
    print(f"Mean Overlap: {div['metrics']['mean_overlap']:.4f}")
    print(f"Max Divergence Rate: {div['metrics']['max_divergence_rate']:.4f}")
    print(f"φ-Resonance Score: {div['metrics']['phi_resonance_score']:.4f}")
    
    # Visualize results
    viz_file = temporal_core.visualize_temporal_divergence(result, timelines)
    print(f"\n📊 Visualization saved to: {viz_file}")
    
    # Save results
    data_file = temporal_core.save_experiment_results(result)
    print(f"💾 Results saved to: {data_file}")
    
if __name__ == "__main__":
    main()
