import torch
import numpy as np
import time
import matplotlib.pyplot as plt
from digital_cpu import DualCortexComputer, PhiResonanceTransfer
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import pickle
import os

class IBMQuantumComparison:
    """
    Direct comparison between our φπ resonance implementation and 
    IBM's quantum processors on equivalent tasks
    """
    
    def __init__(self, save_path="ibm_comparison_results"):
        self.save_path = save_path
        self.metrics = {
            "our_system_completion_time": [],
            "ibm_system_completion_time": [],
            "our_system_coherence": [],
            "ibm_system_coherence": [],
            "our_system_success_rate": [],
            "ibm_system_success_rate": []
        }
        
        # Create save directory if it doesn't exist
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            
        # Initialize our system
        self.our_system = DualCortexComputer(cpu_cores=8, memory_size=128, clock_speed=5.0)
        
        # Initialize IBM simulator backend
        self.ibm_simulator = Aer.get_backend('aer_simulator')
        print("Using IBM Aer quantum simulator")
        
        # We're only using the simulator due to authorization limitations
        self.use_real_quantum = False
        self.ibm_real_backend = None
    
    def test_phi_resonance_task(self, num_trials=10):
        """
        Test analogous task on both systems: resonant energy transfer
        """
        print(f"Running {num_trials} trials comparing φπ resonance with IBM quantum simulator...")
        
        for trial in range(num_trials):
            print(f"Trial {trial+1}/{num_trials}")
            
            # Generate initial quantum state
            initial_dimension = 7  # Small dimension for comparison with IBM
            initial_state = torch.zeros(initial_dimension, dtype=torch.complex64)
            for i in range(initial_dimension):
                phase = 2j * np.pi * i / initial_dimension
                initial_state[i] = torch.exp(torch.tensor(phase))
            initial_state = initial_state / torch.norm(initial_state)
            
            # Target dimension
            target_dimension = 5
            
            # ===== Test Our System =====
            # Create PhiResonanceTransfer
            phi_transfer = PhiResonanceTransfer([initial_dimension, target_dimension])
            
            # Measure execution time
            start_time = time.time()
            
            # Perform resonant energy transfer
            transferred_state = phi_transfer.transfer_energy(
                initial_state, initial_dimension, target_dimension
            )
            
            # Optimize resonance - limiting iterations for benchmark
            phi_transfer.optimize_resonance(max_iterations=5)
            
            # Record completion time
            our_completion_time = time.time() - start_time
            self.metrics["our_system_completion_time"].append(our_completion_time)
            
            # Measure coherence as norm of transferred state
            our_coherence = torch.norm(transferred_state).item()
            self.metrics["our_system_coherence"].append(our_coherence)
            
            # Calculate success as similarity between normalized target and ideal target
            ideal_target = torch.zeros(target_dimension, dtype=torch.complex64)
            for i in range(target_dimension):
                phase = 2j * np.pi * phi_transfer.phi * i / target_dimension
                ideal_target[i] = torch.exp(torch.tensor(phase))
            ideal_target = ideal_target / torch.norm(ideal_target)
            
            our_success = torch.abs(torch.sum(transferred_state * ideal_target.conj())).item()
            self.metrics["our_system_success_rate"].append(our_success)
            
            # ===== Test IBM System =====
            # Create analogous quantum circuit for phase transfer
            qc = QuantumCircuit(initial_dimension + target_dimension, target_dimension)
            
            # Encode initial state (prepare initial superposition with phases)
            for i in range(initial_dimension):
                qc.h(i)  # Put in superposition
                # Apply phase equivalent to our initial state
                phase_angle = 2 * np.pi * i / initial_dimension
                qc.p(phase_angle, i)
            
            # Create entanglement between initial and target registers (energy transfer)
            for i in range(target_dimension):
                qc.h(initial_dimension + i)
                for j in range(min(3, initial_dimension)):  # Limit connections for efficiency
                    qc.cx(j, initial_dimension + i)
            
            # Apply phase transformations on target register to simulate phi-based transfer
            phi = (1 + np.sqrt(5)) / 2
            for i in range(target_dimension):
                phase_angle = 2 * np.pi * phi * i / target_dimension
                qc.p(phase_angle, initial_dimension + i)
            
            # Measure target qubits
            for i in range(target_dimension):
                qc.measure(initial_dimension + i, i)
            
            # Transpile for backend
            transpiled_circuit = transpile(qc, self.ibm_simulator)
            
            # Measure execution time
            start_time = time.time()
            
            # Execute circuit on simulator
            job = self.ibm_simulator.run(transpiled_circuit, shots=1024)
            result = job.result()
            
            # Record completion time
            ibm_completion_time = time.time() - start_time
            self.metrics["ibm_system_completion_time"].append(ibm_completion_time)
            
            # Get counts and convert to probabilities
            counts = result.get_counts()
            total_shots = sum(counts.values())
            
            # Estimate coherence from result stability
            # Higher certainty in results indicates higher coherence
            top_count = max(counts.values()) / total_shots
            ibm_coherence = top_count
            self.metrics["ibm_system_coherence"].append(ibm_coherence)
            
            # Calculate success rate as closeness to expected distribution
            # Create expected bit pattern for each basis state
            expected_patterns = []
            for i in range(target_dimension):
                pattern = format(i, f'0{target_dimension}b')[::-1]  # Reverse to match qiskit convention
                expected_patterns.append(pattern)
            
            # Sum probabilities of expected patterns
            expected_prob = sum(counts.get(pattern, 0) for pattern in expected_patterns) / total_shots
            self.metrics["ibm_system_success_rate"].append(expected_prob)
            
            print(f"Trial {trial+1} complete:")
            print(f"  Our system - Time: {our_completion_time:.4f}s, Coherence: {our_coherence:.4f}, Success: {our_success:.4f}")
            print(f"  IBM system - Time: {ibm_completion_time:.4f}s, Coherence: {ibm_coherence:.4f}, Success: {expected_prob:.4f}")
        
        # Save results
        self._save_results()
        
        return self.metrics
    
    def _save_results(self):
        """Save comparison results"""
        # Calculate averages
        avg_metrics = {key: np.mean(values) for key, values in self.metrics.items() if values}
        
        # Save metrics to pickle file
        with open(f"{self.save_path}/ibm_comparison_metrics.pkl", "wb") as f:
            data = {
                "metrics": self.metrics,
                "averages": avg_metrics
            }
            pickle.dump(data, f)
        
        # Plot results
        self._plot_results()
        
        # Print summary
        print("\nPerformance Comparison Summary:")
        print("=" * 50)
        
        print("\nOur φπ Resonance System:")
        print(f"  Average completion time: {avg_metrics.get('our_system_completion_time', 0):.4f} seconds")
        print(f"  Average coherence: {avg_metrics.get('our_system_coherence', 0):.4f}")
        print(f"  Average success rate: {avg_metrics.get('our_system_success_rate', 0):.4f}")
        
        print("\nIBM Quantum System (Simulator):")
        print(f"  Average completion time: {avg_metrics.get('ibm_system_completion_time', 0):.4f} seconds")
        print(f"  Average coherence: {avg_metrics.get('ibm_system_coherence', 0):.4f}")
        print(f"  Average success rate: {avg_metrics.get('ibm_system_success_rate', 0):.4f}")
        
        # Calculate relative performance
        if avg_metrics.get('ibm_system_completion_time', 0) > 0:
            speed_ratio = avg_metrics.get('our_system_completion_time', 0) / avg_metrics.get('ibm_system_completion_time', 1)
            print(f"\nSpeed comparison: Our system is {1/speed_ratio:.2f}x faster than IBM Quantum")
        
        if avg_metrics.get('ibm_system_coherence', 0) > 0:
            coherence_ratio = avg_metrics.get('our_system_coherence', 0) / avg_metrics.get('ibm_system_coherence', 1)
            print(f"Coherence comparison: Our system has {coherence_ratio:.2f}x the coherence of IBM Quantum")
        
        if avg_metrics.get('ibm_system_success_rate', 0) > 0:
            success_ratio = avg_metrics.get('our_system_success_rate', 0) / avg_metrics.get('ibm_system_success_rate', 1)
            print(f"Success rate comparison: Our system has {success_ratio:.2f}x the success rate of IBM Quantum")
        
    def _plot_results(self):
        """Plot comparative results"""
        # Metrics to plot
        metric_pairs = [
            ("completion_time", "Completion Time (seconds)"),
            ("coherence", "Quantum Coherence"),
            ("success_rate", "Success Rate")
        ]
        
        # Create figure
        fig, axes = plt.subplots(len(metric_pairs), 1, figsize=(10, 15))
        fig.suptitle('φπ Resonance vs IBM Quantum Performance', fontsize=16)
        
        # Plot each metric pair
        for i, (metric_suffix, ylabel) in enumerate(metric_pairs):
            ax = axes[i]
            
            # Get metrics for our system and IBM
            our_metric = self.metrics[f"our_system_{metric_suffix}"]
            ibm_metric = self.metrics[f"ibm_system_{metric_suffix}"]
            
            # Calculate averages
            our_avg = np.mean(our_metric) if our_metric else 0
            ibm_avg = np.mean(ibm_metric) if ibm_metric else 0
            
            # Bar chart data
            labels = ["Our φπ Resonance", "IBM Quantum"]
            values = [our_avg, ibm_avg]
            
            # Different color for completion time (lower is better)
            if metric_suffix == "completion_time":
                colors = ['green' if our_avg <= ibm_avg else 'red', 
                          'green' if ibm_avg <= our_avg else 'red']
                # Add performance text
                if ibm_avg > 0:
                    performance = our_avg / ibm_avg
                    if performance < 1:
                        title = f"{ylabel} (Our system is {1/performance:.2f}x faster)"
                    else:
                        title = f"{ylabel} (IBM is {performance:.2f}x faster)"
                else:
                    title = ylabel
            else:
                colors = ['green' if our_avg >= ibm_avg else 'red', 
                          'green' if ibm_avg >= our_avg else 'red']
                # Add performance text
                if ibm_avg > 0:
                    performance = our_avg / ibm_avg
                    if performance > 1:
                        title = f"{ylabel} (Our system is {performance:.2f}x better)"
                    else:
                        title = f"{ylabel} (IBM is {1/performance:.2f}x better)"
                else:
                    title = ylabel
            
            # Create bar plot
            ax.bar(labels, values, color=colors)
            ax.set_title(title)
            ax.set_ylabel(ylabel)
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            
            # Add value labels on bars
            for j, v in enumerate(values):
                ax.text(j, v * 1.01, f"{v:.3f}", ha='center')
        
        plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for suptitle
        plt.savefig(f"{self.save_path}/ibm_comparison_results.png")
        plt.close()


if __name__ == "__main__":
    # Run comparison
    comparison = IBMQuantumComparison()
    comparison.test_phi_resonance_task(num_trials=5)  # Start with 5 trials
