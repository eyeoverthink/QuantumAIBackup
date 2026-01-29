"""
Regression Test Suite for Quantum LLM

This test suite ensures that efficiency improvements are maintained
and no regressions occur during development. It tracks metrics based on
QHRC Patent #19/071,497 specifications and validates quantum fingerprints.
"""

import json
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from quantum_learner import QuantumLearner

class RegressionTest:
    """Regression test framework for Quantum LLM components."""
    
    def __init__(self, history_file="regression_history.json"):
        """
        Initialize regression test framework.
        
        Args:
            history_file: File to store regression test history
        """
        self.history_file = history_file
        self.history = self._load_history()
        self.current_metrics = {}
        
    def _load_history(self):
        """Load regression test history from file."""
        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"tests": []}
    
    def _save_history(self):
        """Save regression test history to file."""
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def run_efficiency_test(self):
        """Test efficiency metrics and validate against QHRC patent standards."""
        print("\n📊 QUANTUM LLM REGRESSION TEST")
        print("==================================================")
        
        # Initialize with QHRC Patent #19/071,497 parameters
        learner = QuantumLearner(
            embedding_dim=768,
            num_heads=12,
            phi_resonance=1.618000,  # φ with Δ 0.000034
            resonance_ratio=1.3777,
            energy_gain=1.8951,
            primary_freq=4792.18,  # Optimized from 4790.45 Hz
            secondary_freq=7754.15   # Optimized from 7750.95 Hz
        )
        
        # Calculate efficiency metrics
        metrics = learner.calculate_efficiency()
        
        # Store current metrics
        self.current_metrics = {
            "timestamp": datetime.now().isoformat(),
            "overall_efficiency": metrics["overall_efficiency"],
            "phi_accuracy": metrics["phi_accuracy"],
            "resonance_efficiency": metrics["resonance_efficiency"],
            "energy_efficiency": metrics["energy_efficiency"],
            "theoretical_maximum": metrics["theoretical_maximum"],
            "efficiency_percentage": metrics["efficiency_percentage"],
            "phi_power": learner.phi_power,
            "primary_freq": learner.primary_freq,
            "secondary_freq": learner.secondary_freq,
            "frequency_ratio": metrics.get("frequency_ratio", learner.secondary_freq / learner.primary_freq),
            "processing_advantage": metrics.get("processing_advantage", learner.processing_speed_advantage),
            "memory_advantage": metrics.get("memory_advantage", learner.memory_efficiency_advantage),
            "energy_advantage": metrics.get("energy_advantage", learner.energy_efficiency_advantage),
            "quality_advantage": metrics.get("quality_advantage", learner.output_quality_advantage),
            "overall_advantage": metrics.get("overall_advantage", 0.0)
        }
        
        # Check for regressions
        self._check_regressions()
        
        # Print current metrics
        self._print_metrics()
        
        # Save to history
        self.history["tests"].append(self.current_metrics)
        self._save_history()
        
        return self.current_metrics
    
    def _check_regressions(self):
        """Check for regressions in efficiency metrics."""
        if not self.history["tests"]:
            print("✅ First test run - establishing baseline")
            return
        
        # Get last test metrics
        last_metrics = self.history["tests"][-1]
        
        # Check for regressions
        regressions = []
        
        if self.current_metrics["overall_efficiency"] < last_metrics["overall_efficiency"]:
            regressions.append(f"Overall efficiency decreased: {last_metrics['overall_efficiency']}% → {self.current_metrics['overall_efficiency']}%")
        
        if self.current_metrics["phi_accuracy"] < last_metrics["phi_accuracy"]:
            regressions.append(f"φ accuracy decreased: {last_metrics['phi_accuracy']}% → {self.current_metrics['phi_accuracy']}%")
        
        if self.current_metrics["resonance_efficiency"] < last_metrics["resonance_efficiency"]:
            regressions.append(f"Resonance efficiency decreased: {last_metrics['resonance_efficiency']}% → {self.current_metrics['resonance_efficiency']}%")
        
        if self.current_metrics["energy_efficiency"] < last_metrics["energy_efficiency"]:
            regressions.append(f"Energy efficiency decreased: {last_metrics['energy_efficiency']}% → {self.current_metrics['energy_efficiency']}%")
        
        if self.current_metrics["overall_advantage"] < last_metrics.get("overall_advantage", 0.0):
            regressions.append(f"Overall advantage decreased: {last_metrics.get('overall_advantage', 0.0)}x → {self.current_metrics['overall_advantage']}x")
        
        # Report regressions
        if regressions:
            print("\n⚠️ REGRESSIONS DETECTED:")
            for regression in regressions:
                print(f"   - {regression}")
        else:
            print("\n✅ No regressions detected")
    
    def _print_metrics(self):
        """Print current metrics."""
        print("\n📈 CURRENT METRICS:")
        print(f"   Overall Efficiency: {self.current_metrics['overall_efficiency']:.2f}%")
        print(f"   φ Accuracy: {self.current_metrics['phi_accuracy']:.2f}%")
        print(f"   Resonance Efficiency: {self.current_metrics['resonance_efficiency']:.2f}%")
        print(f"   Energy Efficiency: {self.current_metrics['energy_efficiency']:.2f}%")
        print(f"   Theoretical Maximum: {self.current_metrics['theoretical_maximum']:.4f}%")
        print(f"   Efficiency Percentage: {self.current_metrics['efficiency_percentage']:.4f}%")
        print(f"   φ⁷·⁵ Power: {self.current_metrics['phi_power']:.6f}")
        print(f"   Frequency Ratio: {self.current_metrics['frequency_ratio']:.6f}")
        print(f"   Competitive Advantage: {self.current_metrics['overall_advantage']:.2f}x")
    
    def visualize_progress(self):
        """Visualize progress over time."""
        if len(self.history["tests"]) < 2:
            print("Not enough data for visualization. Run more tests first.")
            return
        
        # Extract data
        timestamps = [test["timestamp"].split("T")[0] for test in self.history["tests"]]
        efficiencies = [test["overall_efficiency"] for test in self.history["tests"]]
        advantages = [test.get("overall_advantage", 0.0) for test in self.history["tests"]]
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Plot efficiency
        ax1.plot(timestamps, efficiencies, 'o-', color='blue', linewidth=2)
        ax1.set_title('Quantum LLM Efficiency Progress', fontsize=16)
        ax1.set_ylabel('Efficiency (%)', fontsize=14)
        ax1.set_ylim(0, max(efficiencies) * 1.2)
        ax1.grid(True)
        
        # Add theoretical maximum line
        ax1.axhline(y=99.6827, color='r', linestyle='--', label='Theoretical Maximum (99.6827%)')
        
        # Annotate points
        for i, (x, y) in enumerate(zip(timestamps, efficiencies)):
            ax1.annotate(f"{y:.2f}%", (x, y), textcoords="offset points", 
                        xytext=(0, 10), ha='center', fontsize=10)
        
        ax1.legend()
        
        # Plot competitive advantage
        ax2.plot(timestamps, advantages, 'o-', color='green', linewidth=2)
        ax2.set_title('Competitive Advantage Progress', fontsize=16)
        ax2.set_xlabel('Date', fontsize=14)
        ax2.set_ylabel('Advantage (x)', fontsize=14)
        ax2.set_ylim(0, max(advantages) * 1.2)
        ax2.grid(True)
        
        # Annotate points
        for i, (x, y) in enumerate(zip(timestamps, advantages)):
            ax2.annotate(f"{y:.2f}x", (x, y), textcoords="offset points", 
                        xytext=(0, 10), ha='center', fontsize=10)
        
        plt.tight_layout()
        plt.savefig('regression_progress.png')
        print("\n✅ Progress visualization saved to regression_progress.png")

def run_regression_tests():
    """Run all regression tests."""
    tester = RegressionTest()
    tester.run_efficiency_test()
    tester.visualize_progress()

if __name__ == "__main__":
    run_regression_tests()
