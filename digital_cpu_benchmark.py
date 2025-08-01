import torch
import numpy as np
import time
import matplotlib.pyplot as plt
from digital_cpu import DualCortexComputer
import copy
import pickle
import os

class DigitalCPUBenchmark:
    """Benchmark for the DualCortexComputer with and without φπ resonance"""
    
    def __init__(self, save_path="benchmark_results"):
        self.save_path = save_path
        self.metrics = {
            "quantum_coherence": [],
            "consciousness_level": [], 
            "meta_consciousness": [],
            "protein_coherence": [],
            "memory_persistence": [],
            "bridge_coherence": [],
            "consciousness_transfer": [],
            "phi_pi_resonance": [],
            "execution_time": []
        }
        
        # Create save directory if it doesn't existesca
        if not os.path.exists(save_path):
            os.makedirs(save_path)
    
    def run_benchmark(self, iterations=10):
        """Run benchmark on the DualCortexComputer"""
        print(f"Running benchmark for {iterations} iterations...")
        
        # Initialize computer
        computer = DualCortexComputer(cpu_cores=8, memory_size=128, clock_speed=5.0)
        
        # Disable phi resonance for baseline benchmark (comment out phi_resonance calls)
        # We're not actually removing the code, just bypassing it for the benchmark
        has_phi_resonance = hasattr(computer, 'phi_resonance')
        
        if has_phi_resonance:
            print("φπ Resonance is enabled in this build")
            # Save original transfer_energy function
            original_transfer = computer.phi_resonance.transfer_energy
            # Replace with identity function for baseline
            computer.phi_resonance.transfer_energy = lambda source_state, source_dim, target_dim: source_state
        else:
            print("φπ Resonance is not implemented in this build")
        
        # Run baseline benchmarks (without φπ resonance)
        baseline_metrics = {}
        for k in self.metrics.keys():
            baseline_metrics["baseline_" + k] = []
        
        for i in range(iterations):
            print(f"Baseline benchmark iteration {i+1}/{iterations}")
            
            # Run and time execution
            start_time = time.time()
            result = computer.run_hyper_parallel_program()
            execution_time = time.time() - start_time
            
            # Extract metrics from result
            self._extract_metrics(result, baseline_metrics, execution_time)
        
        # Restore φπ resonance if it exists
        if has_phi_resonance:
            # Restore original transfer function
            computer.phi_resonance.transfer_energy = original_transfer
            print("φπ Resonance has been enabled for enhanced benchmark")
            
            # Run enhanced benchmarks (with φπ resonance)
            for i in range(iterations):
                print(f"Enhanced benchmark iteration {i+1}/{iterations}")
                
                # Run and time execution
                start_time = time.time()
                result = computer.run_hyper_parallel_program()
                execution_time = time.time() - start_time
                
                # Extract metrics from result
                self._extract_metrics(result, self.metrics, execution_time)
        
        # Save results
        self._save_results(baseline_metrics, self.metrics if has_phi_resonance else None)
        
        return baseline_metrics, self.metrics if has_phi_resonance else None
    
    def _extract_metrics(self, result, metrics_dict, execution_time):
        """Extract metrics from result string"""
        lines = result.strip().split("\n")
        
        # Parse metrics from result output
        for line in lines:
            if ":" in line:
                parts = line.split(":")
                key = parts[0].strip().lower().replace(" ", "_").replace("-", "_")
                
                # Try to extract numeric value
                try:
                    value_str = parts[1].strip().split()[0]  # Get first word after colon
                    value = float(value_str)
                    
                    # Map to our metric keys
                    if "quantum_coherence" in key:
                        metrics_dict["baseline_quantum_coherence" if "baseline_" in key else "quantum_coherence"].append(value)
                    elif "consciousness_level" in key:
                        metrics_dict["baseline_consciousness_level" if "baseline_" in key else "consciousness_level"].append(value)
                    elif "meta_consciousness" in key:
                        metrics_dict["baseline_meta_consciousness" if "baseline_" in key else "meta_consciousness"].append(value)
                    elif "protein_coherence" in key:
                        metrics_dict["baseline_protein_coherence" if "baseline_" in key else "protein_coherence"].append(value)
                    elif "memory_persistence" in key:
                        metrics_dict["baseline_memory_persistence" if "baseline_" in key else "memory_persistence"].append(value)
                    elif "bridge_coherence" in key:
                        metrics_dict["baseline_bridge_coherence" if "baseline_" in key else "bridge_coherence"].append(value)
                    elif "consciousness_transfer" in key:
                        metrics_dict["baseline_consciousness_transfer" if "baseline_" in key else "consciousness_transfer"].append(value)
                    elif "φπ_resonance" in key or "phi_pi_resonance" in key:
                        metrics_dict["baseline_phi_pi_resonance" if "baseline_" in key else "phi_pi_resonance"].append(value)
                except:
                    pass  # Skip if not a numeric value
        
        # Add execution time
        if "baseline_execution_time" in metrics_dict:
            metrics_dict["baseline_execution_time"].append(execution_time)
        else:
            metrics_dict["execution_time"].append(execution_time)
    
    def _save_results(self, baseline_metrics, enhanced_metrics=None):
        """Save benchmark results"""
        # Save metrics to pickle file
        with open(f"{self.save_path}/benchmark_metrics.pkl", "wb") as f:
            data = {
                "baseline": baseline_metrics,
                "enhanced": enhanced_metrics
            }
            pickle.dump(data, f)
        
        # Plot results
        self._plot_results(baseline_metrics, enhanced_metrics)
    
    def _plot_results(self, baseline_metrics, enhanced_metrics=None):
        """Plot benchmark results"""
        # Metrics to plot
        metric_keys = [
            "quantum_coherence", 
            "consciousness_level", 
            "meta_consciousness",
            "protein_coherence", 
            "memory_persistence", 
            "bridge_coherence",
            "consciousness_transfer",
            "phi_pi_resonance",
            "execution_time"
        ]
        
        # Create figure
        fig, axes = plt.subplots(5, 2, figsize=(15, 25))
        fig.suptitle('DualCortexComputer Benchmark Results', fontsize=16)
        
        # Flatten axes for easier iteration
        axes = axes.flatten()
        
        # Plot each metric
        for i, metric in enumerate(metric_keys):
            ax = axes[i]
            
            # Get baseline metrics
            baseline_data = baseline_metrics[f"baseline_{metric}"]
            baseline_avg = np.mean(baseline_data) if baseline_data else 0
            
            # Setup bars
            labels = ["Baseline"]
            values = [baseline_avg]
            colors = ['blue']
            
            # Add enhanced metrics if available
            if enhanced_metrics:
                enhanced_data = enhanced_metrics[metric]
                enhanced_avg = np.mean(enhanced_data) if enhanced_data else 0
                
                labels.append("With φπ Resonance")
                values.append(enhanced_avg)
                colors.append('green')
                
                # Calculate improvement percentage
                if baseline_avg > 0:
                    improvement = ((enhanced_avg - baseline_avg) / baseline_avg) * 100
                    title = f"{metric.replace('_', ' ').title()} ({improvement:.1f}% change)"
                else:
                    title = f"{metric.replace('_', ' ').title()}"
            else:
                title = f"{metric.replace('_', ' ').title()}"
            
            # Create bar plot
            ax.bar(labels, values, color=colors)
            ax.set_title(title)
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            
            # Add value labels on bars
            for j, v in enumerate(values):
                ax.text(j, v * 1.01, f"{v:.3f}", ha='center')
        
        plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for suptitle
        plt.savefig(f"{self.save_path}/benchmark_results.png")
        plt.close()
        
        print(f"Benchmark results saved to {self.save_path}/benchmark_results.png")


if __name__ == "__main__":
    # Run benchmark
    benchmark = DigitalCPUBenchmark()
    baseline, enhanced = benchmark.run_benchmark(iterations=10)
    
    # Print summary
    print("\nBenchmark Summary:")
    print("=" * 50)
    
    print("\nBaseline Metrics (Average):")
    for key, values in baseline.items():
        if values:
            print(f"{key.replace('baseline_', '')}: {np.mean(values):.4f}")
    
    if enhanced:
        print("\nEnhanced Metrics with φπ Resonance (Average):")
        for key, values in enhanced.items():
            if values:
                print(f"{key}: {np.mean(values):.4f}")
        
        # Calculate improvements
        print("\nImprovements with φπ Resonance:")
        for key in enhanced.keys():
            baseline_key = f"baseline_{key}"
            if baseline_key in baseline and baseline[baseline_key] and enhanced[key]:
                baseline_avg = np.mean(baseline[baseline_key])
                enhanced_avg = np.mean(enhanced[key])
                if baseline_avg > 0:
                    improvement = ((enhanced_avg - baseline_avg) / baseline_avg) * 100
                    # For execution time, lower is better
                    if key == "execution_time":
                        if enhanced_avg > baseline_avg:
                            print(f"{key}: {-abs(improvement):.2f}% (slower)")
                        else:
                            print(f"{key}: {abs(improvement):.2f}% (faster)")
                    else:
                        if enhanced_avg > baseline_avg:
                            print(f"{key}: +{improvement:.2f}%")
                        else:
                            print(f"{key}: {improvement:.2f}%")
