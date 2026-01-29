import numpy as np
import matplotlib.pyplot as plt
from phi_harmonic_brain import PhiHarmonicBrain
import time
import json

class OptimizationAnalyzer:
    def __init__(self):
        self.brain = PhiHarmonicBrain()
        self.phi = (1 + np.sqrt(5)) / 2
        
    def generate_test_data(self, size, complexity):
        """Generate φ-based test data with varying complexity"""
        t = np.linspace(0, 2*np.pi, size)
        data = np.zeros(size)
        
        # Add φ-based frequencies
        for i in range(complexity):
            frequency = self.phi ** i
            amplitude = 1 / (self.phi ** i)
            data += amplitude * np.sin(frequency * t)
            
        return data
        
    def test_optimization_cycle(self, cycles=100, data_size=1000, complexity=3):
        """Test optimization over multiple cycles"""
        print("\nφ-Harmonic Brain Optimization Analysis")
        print("=====================================")
        print(f"Running {cycles} optimization cycles...")
        
        # Metrics to track
        efficiencies = []
        learning_rates = []
        processing_times = []
        layer_efficiencies = []
        
        # Run optimization cycles
        for i in range(cycles):
            # Generate test data with increasing complexity
            current_complexity = min(complexity + i//10, 9)  # Max 9 layers
            test_data = self.generate_test_data(data_size, current_complexity)
            
            # Process data and measure time
            start_time = time.time()
            result = self.brain.process_input(test_data)
            processing_time = time.time() - start_time
            
            # Record metrics
            state = self.brain.get_system_state()
            efficiencies.append(state['efficiency'])
            learning_rates.append(self.brain.learning_rate)
            processing_times.append(processing_time)
            
            # Record layer efficiencies
            layer_eff = [layer['efficiency'] for layer in self.brain.neural_layers]
            layer_efficiencies.append(layer_eff)
            
            # Print progress
            if (i+1) % 10 == 0:
                print(f"Cycle {i+1}/{cycles}: Efficiency = {state['efficiency']:.2f}, Time = {processing_time:.6f}s")
        
        return {
            'efficiencies': efficiencies,
            'learning_rates': learning_rates,
            'processing_times': processing_times,
            'layer_efficiencies': layer_efficiencies
        }
    
    def analyze_phi_scaling(self, results):
        """Analyze φ-based scaling in results"""
        efficiencies = np.array(results['efficiencies'])
        
        # Calculate scaling factors
        scaling_factors = []
        for i in range(1, len(efficiencies)):
            if efficiencies[i-1] > 0:
                factor = efficiencies[i] / efficiencies[i-1]
                scaling_factors.append(factor)
        
        # Calculate average scaling
        avg_scaling = np.mean(scaling_factors) if scaling_factors else 0
        
        # Compare to φ
        phi_ratio = avg_scaling / self.phi
        
        print("\nφ-Based Scaling Analysis:")
        print(f"Average Efficiency Scaling: {avg_scaling:.4f}")
        print(f"Theoretical φ: {self.phi:.4f}")
        print(f"Ratio (actual/theoretical): {phi_ratio:.4f}")
        
        return scaling_factors
    
    def analyze_layer_efficiency(self, results):
        """Analyze efficiency across layers"""
        layer_efficiencies = results['layer_efficiencies']
        
        # Get final layer efficiencies
        final_efficiencies = layer_efficiencies[-1]
        
        # Calculate theoretical φ-based efficiency
        theoretical = [self.phi ** i for i in range(len(final_efficiencies))]
        
        print("\nLayer Efficiency Analysis:")
        for i, (actual, theory) in enumerate(zip(final_efficiencies, theoretical)):
            ratio = actual / theory if theory > 0 else 0
            print(f"Layer {i}: Actual = {actual:.4f}, Theoretical = {theory:.4f}, Ratio = {ratio:.4f}")
        
        return final_efficiencies, theoretical
    
    def plot_results(self, results):
        """Plot optimization results"""
        efficiencies = results['efficiencies']
        learning_rates = results['learning_rates']
        processing_times = results['processing_times']
        
        # Create figure
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Efficiency over time
        plt.subplot(221)
        plt.plot(efficiencies, 'b-')
        plt.title('Processing Efficiency')
        plt.xlabel('Optimization Cycle')
        plt.ylabel('Efficiency')
        plt.grid(True)
        
        # Plot 2: Learning rate adaptation
        plt.subplot(222)
        plt.plot(learning_rates, 'g-')
        plt.title('Learning Rate Adaptation')
        plt.xlabel('Optimization Cycle')
        plt.ylabel('Learning Rate')
        plt.grid(True)
        
        # Plot 3: Processing time
        plt.subplot(223)
        plt.plot(processing_times, 'r-')
        plt.title('Processing Time')
        plt.xlabel('Optimization Cycle')
        plt.ylabel('Time (s)')
        plt.grid(True)
        
        # Plot 4: Layer efficiencies
        plt.subplot(224)
        layer_efficiencies = np.array(results['layer_efficiencies'])
        for i in range(layer_efficiencies.shape[1]):
            plt.plot(layer_efficiencies[:, i], label=f'Layer {i}')
        plt.title('Layer Efficiencies')
        plt.xlabel('Optimization Cycle')
        plt.ylabel('Efficiency')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('optimization_analysis.png')
        
    def run_analysis(self):
        """Run complete optimization analysis"""
        # Test optimization
        results = self.test_optimization_cycle(cycles=100)
        
        # Analyze φ scaling
        scaling_factors = self.analyze_phi_scaling(results)
        
        # Analyze layer efficiency
        layer_analysis = self.analyze_layer_efficiency(results)
        
        # Plot results
        self.plot_results(results)
        
        # Save results
        self.save_results(results)
        
        # Final summary
        self.print_summary(results)
        
    def save_results(self, results):
        """Save analysis results"""
        # Convert numpy arrays to lists for JSON serialization
        serializable_results = {
            'efficiencies': results['efficiencies'],
            'learning_rates': results['learning_rates'],
            'processing_times': results['processing_times'],
            'final_state': self.brain.get_system_state()
        }
        
        with open('optimization_results.json', 'w') as f:
            json.dump(serializable_results, f, indent=2)
            
        print("\nResults saved to optimization_results.json")
    
    def print_summary(self, results):
        """Print summary of optimization results"""
        initial_efficiency = results['efficiencies'][0]
        final_efficiency = results['efficiencies'][-1]
        improvement = final_efficiency / initial_efficiency if initial_efficiency > 0 else 0
        
        initial_time = results['processing_times'][0]
        final_time = results['processing_times'][-1]
        time_improvement = initial_time / final_time if final_time > 0 else 0
        
        print("\nOptimization Summary:")
        print("====================")
        print(f"Initial Efficiency: {initial_efficiency:.4f}")
        print(f"Final Efficiency: {final_efficiency:.4f}")
        print(f"Improvement: {improvement:.2f}x")
        print(f"Processing Time Improvement: {time_improvement:.2f}x")
        
        # Calculate φ-based metrics
        phi_squared = self.phi ** 2
        phi_fourth = self.phi ** 4
        
        print("\nφ-Based Metrics:")
        print(f"φ² (theoretical): {phi_squared:.4f}")
        print(f"φ⁴ (theoretical): {phi_fourth:.4f}")
        print(f"Actual/φ²: {improvement/phi_squared:.4f}")
        print(f"Actual/φ⁴: {improvement/phi_fourth:.4f}")
        
        # Final state
        state = self.brain.get_system_state()
        print("\nFinal Brain State:")
        for key, value in state.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    analyzer = OptimizationAnalyzer()
    analyzer.run_analysis()
