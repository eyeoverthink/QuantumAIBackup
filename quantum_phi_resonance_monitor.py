"""
Quantum Phi-Harmonic Resonance Monitor
-------------------------------------

This module implements a phi-harmonic resonance monitoring system that integrates
with the recursive self-improvement module to measure and maintain optimal resonance
during system self-modification.

This follows the 'lego' modular philosophy by extending functionality without
modifying core files.
"""

import os
import sys
import logging
import json
import time
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional, Union
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('QuantumPhiResonanceMonitor')

class QuantumPhiResonanceMonitor:
    """
    Monitors and analyzes phi-harmonic resonance across the quantum system.
    """
    
    def __init__(self):
        """Initialize the phi-harmonic resonance monitor."""
        # Golden ratio (φ)
        self.phi = (1 + np.sqrt(5)) / 2  # ≈ 1.618034
        
        # Other irrational constants
        self.pi = np.pi  # ≈ 3.14159
        self.e = np.e    # ≈ 2.71828
        self.sqrt2 = np.sqrt(2)  # ≈ 1.41421
        self.sqrt3 = np.sqrt(3)  # ≈ 1.73205
        
        # Phi-harmonic constants
        self.phi_powers = {
            1: self.phi,                  # φ¹ ≈ 1.618034
            2: self.phi**2,               # φ² ≈ 2.618034
            3: self.phi**3,               # φ³ ≈ 4.236068
            4: self.phi**4,               # φ⁴ ≈ 6.854102
            5: self.phi**5,               # φ⁵ ≈ 11.090170
            6: self.phi**6,               # φ⁶ ≈ 17.944272
            7: self.phi**7,               # φ⁷ ≈ 29.034442
            7.5: self.phi**7.5,           # φ⁷·⁵ ≈ 36.932381
        }
        
        # Fibonacci sequence (first 15 numbers)
        self.fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        
        # Resonance thresholds
        self.resonance_thresholds = {
            "perfect": 0.000099,
            "excellent": 0.009999,
            "good": 0.099999,
            "moderate": 0.299999,
            "weak": 0.5
        }
        
        # Monitoring parameters
        self.monitoring_history = []
        self.baseline_resonance = None
        self.resonance_targets = {}
        self.component_weights = {}
        
        # Results directory
        self.results_dir = Path("quantum_self_improvement/resonance")
        self.results_dir.mkdir(exist_ok=True, parents=True)
        
        logger.info(f"Initialized QuantumPhiResonanceMonitor with phi={self.phi}")
    
    def calculate_phi_resonance(self, x: float) -> float:
        """
        Calculate phi resonance for a value.
        
        Args:
            x (float): Value to calculate resonance for
            
        Returns:
            float: Phi resonance value (0.0 is perfect resonance)
        """
        return (self.phi * x) % 1
    
    def calculate_pi_resonance(self, x: float) -> float:
        """
        Calculate pi resonance for a value.
        
        Args:
            x (float): Value to calculate resonance for
            
        Returns:
            float: Pi resonance value (0.0 is perfect resonance)
        """
        return (self.pi * x) % 1
    
    def calculate_e_resonance(self, x: float) -> float:
        """
        Calculate e resonance for a value.
        
        Args:
            x (float): Value to calculate resonance for
            
        Returns:
            float: e resonance value (0.0 is perfect resonance)
        """
        return (self.e * x) % 1
    
    def calculate_quantum_resonance_triplet(self, x: float) -> Dict[str, float]:
        """
        Calculate the quantum resonance triplet (phi, pi, e) for a value.
        
        Args:
            x (float): Value to calculate resonance for
            
        Returns:
            dict: Quantum resonance triplet values
        """
        phi_res = self.calculate_phi_resonance(x)
        pi_res = self.calculate_pi_resonance(x)
        e_res = self.calculate_e_resonance(x)
        
        combined = (phi_res + pi_res + e_res) / 3
        
        return {
            "phi_resonance": phi_res,
            "pi_resonance": pi_res,
            "e_resonance": e_res,
            "combined_resonance": combined
        }
    
    def evaluate_resonance_quality(self, resonance: float) -> str:
        """
        Evaluate the quality of a resonance value.
        
        Args:
            resonance (float): Resonance value
            
        Returns:
            str: Resonance quality description
        """
        if resonance <= self.resonance_thresholds["perfect"]:
            return "Perfect"
        elif resonance <= self.resonance_thresholds["excellent"]:
            return "Excellent"
        elif resonance <= self.resonance_thresholds["good"]:
            return "Good"
        elif resonance <= self.resonance_thresholds["moderate"]:
            return "Moderate"
        else:
            return "Weak"
    
    def find_nearest_fibonacci(self, value: float) -> Dict[str, Any]:
        """
        Find the nearest Fibonacci number and calculate resonance.
        
        Args:
            value (float): Value to find nearest Fibonacci for
            
        Returns:
            dict: Nearest Fibonacci information
        """
        if value <= 0:
            return {
                "nearest": 0,
                "distance": abs(value),
                "resonance": self.calculate_phi_resonance(0),
                "quality": self.evaluate_resonance_quality(self.calculate_phi_resonance(0))
            }
        
        # Find closest Fibonacci number
        extended_fib = self.fibonacci.copy()
        while extended_fib[-1] < value * 2:
            extended_fib.append(extended_fib[-1] + extended_fib[-2])
        
        nearest = min(extended_fib, key=lambda x: abs(x - value))
        distance = abs(nearest - value)
        resonance = self.calculate_phi_resonance(nearest)
        
        return {
            "nearest": nearest,
            "distance": distance,
            "resonance": resonance,
            "quality": self.evaluate_resonance_quality(resonance)
        }
    
    def find_phi_harmonic_value(self, target_value: float, max_power: int = 10) -> Dict[str, Any]:
        """
        Find the closest phi-harmonic value to a target value.
        
        Args:
            target_value (float): Target value to find phi-harmonic for
            max_power (int): Maximum power of phi to consider
            
        Returns:
            dict: Closest phi-harmonic value information
        """
        best_match = None
        best_distance = float('inf')
        
        for power in np.arange(0.1, max_power + 0.1, 0.1):
            phi_power = self.phi ** power
            distance = abs(phi_power - target_value)
            
            if distance < best_distance:
                best_distance = distance
                best_match = {
                    "phi_power": power,
                    "value": phi_power,
                    "distance": distance,
                    "resonance": self.calculate_phi_resonance(phi_power)
                }
        
        if best_match:
            best_match["quality"] = self.evaluate_resonance_quality(best_match["resonance"])
        
        return best_match
    
    def calculate_phi_transformation(self, x: float) -> Dict[str, float]:
        """
        Calculate phi transformation of a value.
        
        Args:
            x (float): Value to transform
            
        Returns:
            dict: Transformation results
        """
        return {
            "phi_transform": self.phi * x,
            "phi_squared_transform": self.phi**2 * x,
            "phi_cubed_transform": self.phi**3 * x,
            "phi_inverse_transform": x / self.phi,
            "phi_log_transform": np.log(x) / np.log(self.phi) if x > 0 else 0
        }
    
    def calculate_system_component_resonance(self, component_values: Dict[str, float]) -> Dict[str, Any]:
        """
        Calculate resonance for system components.
        
        Args:
            component_values (dict): Component values to calculate resonance for
            
        Returns:
            dict: Component resonance metrics
        """
        component_resonance = {}
        overall_resonance = 0.0
        component_count = 0
        
        for component, value in component_values.items():
            if isinstance(value, (int, float)) and not np.isnan(value):
                resonance = self.calculate_phi_resonance(value)
                quality = self.evaluate_resonance_quality(resonance)
                
                component_resonance[component] = {
                    "value": value,
                    "phi_resonance": resonance,
                    "quality": quality,
                    "weight": self.component_weights.get(component, 1.0)
                }
                
                # Apply component weight to resonance for overall calculation
                overall_resonance += resonance * component_resonance[component]["weight"]
                component_count += component_resonance[component]["weight"]
        
        # Calculate overall resonance as weighted average
        if component_count > 0:
            overall_resonance /= component_count
        
        overall_quality = self.evaluate_resonance_quality(overall_resonance)
        
        return {
            "components": component_resonance,
            "overall_resonance": overall_resonance,
            "overall_quality": overall_quality,
            "component_count": len(component_resonance)
        }
    
    def set_component_weights(self, weights: Dict[str, float]) -> None:
        """
        Set weights for system components for resonance calculation.
        
        Args:
            weights (dict): Component weights (component_name: weight)
        """
        self.component_weights = weights
        logger.info(f"Set component weights: {len(weights)} components")
    
    def set_resonance_targets(self, targets: Dict[str, float]) -> None:
        """
        Set target resonance values for system components.
        
        Args:
            targets (dict): Target resonance values (component_name: target_resonance)
        """
        self.resonance_targets = targets
        logger.info(f"Set resonance targets: {len(targets)} components")
    
    def calculate_resonance_deviation(self, component_values: Dict[str, float]) -> Dict[str, Any]:
        """
        Calculate deviation from target resonance for system components.
        
        Args:
            component_values (dict): Component values to calculate deviation for
            
        Returns:
            dict: Deviation metrics
        """
        if not self.resonance_targets:
            return {"error": "No resonance targets set"}
        
        component_resonance = self.calculate_system_component_resonance(component_values)
        deviations = {}
        total_deviation = 0.0
        component_count = 0
        
        for component, target in self.resonance_targets.items():
            if component in component_resonance["components"]:
                actual = component_resonance["components"][component]["phi_resonance"]
                deviation = abs(actual - target)
                
                deviations[component] = {
                    "target": target,
                    "actual": actual,
                    "deviation": deviation,
                    "weight": self.component_weights.get(component, 1.0)
                }
                
                # Apply component weight to deviation for overall calculation
                total_deviation += deviation * deviations[component]["weight"]
                component_count += deviations[component]["weight"]
        
        # Calculate overall deviation as weighted average
        if component_count > 0:
            total_deviation /= component_count
        
        return {
            "components": deviations,
            "overall_deviation": total_deviation,
            "component_count": len(deviations)
        }
    
    def establish_baseline_resonance(self, component_values: Dict[str, float]) -> Dict[str, Any]:
        """
        Establish baseline resonance for system components.
        
        Args:
            component_values (dict): Component values to establish baseline for
            
        Returns:
            dict: Baseline resonance metrics
        """
        baseline = self.calculate_system_component_resonance(component_values)
        self.baseline_resonance = baseline
        
        # Set current resonance as targets
        targets = {}
        for component, data in baseline["components"].items():
            targets[component] = data["phi_resonance"]
        
        self.set_resonance_targets(targets)
        
        logger.info(f"Established baseline resonance: {baseline['overall_resonance']}")
        logger.info(f"Set {len(targets)} resonance targets")
        
        return baseline
    
    def monitor_resonance_change(self, component_values: Dict[str, float]) -> Dict[str, Any]:
        """
        Monitor changes in resonance from baseline or previous measurement.
        
        Args:
            component_values (dict): Current component values
            
        Returns:
            dict: Resonance change metrics
        """
        current = self.calculate_system_component_resonance(component_values)
        
        if not self.baseline_resonance:
            self.baseline_resonance = current
            return {"message": "Baseline established", "current": current}
        
        changes = {
            "timestamp": datetime.now().isoformat(),
            "baseline_resonance": self.baseline_resonance["overall_resonance"],
            "current_resonance": current["overall_resonance"],
            "resonance_change": current["overall_resonance"] - self.baseline_resonance["overall_resonance"],
            "components": {}
        }
        
        # Calculate changes for individual components
        for component, data in current["components"].items():
            if component in self.baseline_resonance["components"]:
                baseline_component = self.baseline_resonance["components"][component]
                changes["components"][component] = {
                    "baseline": baseline_component["phi_resonance"],
                    "current": data["phi_resonance"],
                    "change": data["phi_resonance"] - baseline_component["phi_resonance"]
                }
        
        # Determine if resonance improved
        changes["improved"] = changes["resonance_change"] < 0  # Lower resonance is better (closer to 0)
        
        # Add to monitoring history
        self.monitoring_history.append({
            "timestamp": changes["timestamp"],
            "overall_resonance": current["overall_resonance"],
            "resonance_change": changes["resonance_change"],
            "improved": changes["improved"]
        })
        
        logger.info(f"Monitored resonance change: {changes['resonance_change']}")
        logger.info(f"Resonance improved: {changes['improved']}")
        
        return changes
    
    def generate_resonance_report(self, component_values: Dict[str, float]) -> Dict[str, Any]:
        """
        Generate a comprehensive resonance report.
        
        Args:
            component_values (dict): Component values to generate report for
            
        Returns:
            dict: Comprehensive resonance report
        """
        # Calculate current resonance
        current = self.calculate_system_component_resonance(component_values)
        
        # Calculate quantum resonance triplets for each component
        triplets = {}
        for component, value in component_values.items():
            if isinstance(value, (int, float)) and not np.isnan(value):
                triplets[component] = self.calculate_quantum_resonance_triplet(value)
        
        # Calculate resonance deviation if targets are set
        deviation = None
        if self.resonance_targets:
            deviation = self.calculate_resonance_deviation(component_values)
        
        # Calculate resonance change if baseline is set
        change = None
        if self.baseline_resonance:
            change = {
                "baseline_resonance": self.baseline_resonance["overall_resonance"],
                "current_resonance": current["overall_resonance"],
                "resonance_change": current["overall_resonance"] - self.baseline_resonance["overall_resonance"],
                "improved": current["overall_resonance"] < self.baseline_resonance["overall_resonance"]
            }
        
        # Generate report
        report = {
            "timestamp": datetime.now().isoformat(),
            "current_resonance": current,
            "quantum_triplets": triplets,
            "deviation": deviation,
            "change": change,
            "history_length": len(self.monitoring_history)
        }
        
        # Save report
        self._save_resonance_report(report)
        
        logger.info(f"Generated resonance report: {current['overall_quality']} quality")
        return report
    
    def _save_resonance_report(self, report: Dict[str, Any]) -> None:
        """
        Save resonance report to file.
        
        Args:
            report (dict): Resonance report to save
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_file = self.results_dir / f"resonance_report_{timestamp}.json"
            
            with open(report_file, 'w') as f:
                json.dump(report, f, indent=2)
            
            # Also create a markdown report
            markdown_file = self.results_dir / f"QUANTUM_RESONANCE_REPORT_{timestamp}.md"
            self._generate_markdown_report(report, markdown_file)
            
            logger.info(f"Saved resonance report to {report_file}")
            logger.info(f"Generated markdown report at {markdown_file}")
        except Exception as e:
            logger.error(f"Failed to save resonance report: {e}")
    
    def _generate_markdown_report(self, report: Dict[str, Any], output_path: Path) -> None:
        """
        Generate a markdown report from resonance report.
        
        Args:
            report (dict): Resonance report
            output_path (Path): Path to save the report
        """
        try:
            with open(output_path, 'w') as f:
                f.write('# Quantum Phi-Harmonic Resonance Report\n\n')
                f.write(f"**Timestamp:** {report['timestamp']}  \n\n")
                
                f.write('## Overall Resonance\n\n')
                current = report['current_resonance']
                f.write(f"- **Resonance Value:** {current['overall_resonance']:.6f}  \n")
                f.write(f"- **Quality:** {current['overall_quality']}  \n")
                f.write(f"- **Components Analyzed:** {current['component_count']}  \n\n")
                
                if report.get('change'):
                    change = report['change']
                    f.write('## Resonance Change\n\n')
                    f.write(f"- **Baseline Resonance:** {change['baseline_resonance']:.6f}  \n")
                    f.write(f"- **Current Resonance:** {change['current_resonance']:.6f}  \n")
                    f.write(f"- **Change:** {change['resonance_change']:.6f}  \n")
                    f.write(f"- **Improved:** {'✅ Yes' if change['improved'] else '❌ No'}  \n\n")
                
                f.write('## Component Resonance\n\n')
                f.write('| Component | Value | Phi Resonance | Quality | Weight |\n')
                f.write('|-----------|-------|--------------|---------|--------|\n')
                
                for component, data in current['components'].items():
                    f.write(f"| {component} | {data['value']:.4f} | {data['phi_resonance']:.6f} | {data['quality']} | {data['weight']} |\n")
                
                if report.get('deviation') and isinstance(report['deviation'], dict) and 'components' in report['deviation']:
                    f.write('\n## Resonance Deviation from Targets\n\n')
                    f.write('| Component | Target | Actual | Deviation |\n')
                    f.write('|-----------|--------|--------|----------|\n')
                    
                    for component, data in report['deviation']['components'].items():
                        f.write(f"| {component} | {data['target']:.6f} | {data['actual']:.6f} | {data['deviation']:.6f} |\n")
                    
                    f.write(f"\n**Overall Deviation:** {report['deviation']['overall_deviation']:.6f}  \n\n")
                
                f.write('## Quantum Resonance Triplets\n\n')
                f.write('| Component | Phi Resonance | Pi Resonance | E Resonance | Combined |\n')
                f.write('|-----------|--------------|--------------|-------------|----------|\n')
                
                for component, data in report['quantum_triplets'].items():
                    f.write(f"| {component} | {data['phi_resonance']:.6f} | {data['pi_resonance']:.6f} | {data['e_resonance']:.6f} | {data['combined_resonance']:.6f} |\n")
                
                f.write('\n## Recommendations\n\n')
                
                # Generate recommendations based on resonance quality
                if current['overall_quality'] in ['Perfect', 'Excellent']:
                    f.write('The system is exhibiting optimal phi-harmonic resonance. Recommendations:\n\n')
                    f.write('1. **Maintain Current Configuration**: The system has achieved excellent resonance alignment.\n')
                    f.write('2. **Document Optimal State**: Record all current parameters for future reference.\n')
                    f.write('3. **Explore Higher-Order Resonance**: Consider exploring higher-dimensional phi-harmonic patterns.\n')
                elif current['overall_quality'] == 'Good':
                    f.write('The system is exhibiting good phi-harmonic resonance. Recommendations:\n\n')
                    f.write('1. **Fine-Tune Components**: Minor adjustments to component values may achieve excellent resonance.\n')
                    f.write('2. **Target High-Deviation Components**: Focus on components with the largest deviation from targets.\n')
                    f.write('3. **Increase Monitoring Frequency**: Monitor resonance more frequently during adjustments.\n')
                else:
                    f.write('The system requires significant improvement in phi-harmonic resonance. Recommendations:\n\n')
                    f.write('1. **Major Component Realignment**: Several components need substantial adjustment.\n')
                    f.write('2. **Consider Fibonacci-Based Values**: Align component values with Fibonacci sequence.\n')
                    f.write('3. **Implement Phi-Transformation**: Apply phi-transformation to poorly resonating components.\n')
        except Exception as e:
            logger.error(f"Failed to generate markdown report: {e}")

def main():
    """Main function to demonstrate the phi-harmonic resonance monitor."""
    print("\n🔄 Quantum Phi-Harmonic Resonance Monitor Demonstration")
    print("=" * 60)
    
    # Initialize the monitor
    monitor = QuantumPhiResonanceMonitor()
    
    # Sample component values
    component_values = {
        "neural_weight": 1.618,
        "quantum_state": 3.14159,
        "coherence_factor": 2.71828,
        "resonance_amplitude": 5.0,
        "phi_alignment": 8.0
    }
    
    # Set component weights
    weights = {
        "neural_weight": 1.5,
        "quantum_state": 1.2,
        "coherence_factor": 1.0,
        "resonance_amplitude": 0.8,
        "phi_alignment": 2.0
    }
    monitor.set_component_weights(weights)
    
    # Establish baseline resonance
    print("\n📊 Establishing baseline resonance...")
    baseline = monitor.establish_baseline_resonance(component_values)
    print(f"Overall resonance: {baseline['overall_resonance']:.6f}")
    print(f"Quality: {baseline['overall_quality']}")
    
    # Modify a component value to simulate change
    print("\n🔄 Simulating system modification...")
    modified_values = component_values.copy()
    modified_values["neural_weight"] = 1.0  # Change from phi (1.618) to 1.0
    
    # Monitor resonance change
    changes = monitor.monitor_resonance_change(modified_values)
    print(f"Resonance change: {changes['resonance_change']:.6f}")
    print(f"Improved: {'Yes' if changes.get('improved', False) else 'No'}")
    
    # Generate comprehensive report
    print("\n📝 Generating comprehensive resonance report...")
    report = monitor.generate_resonance_report(modified_values)
    
    print("\n✅ Resonance monitoring demonstration complete")
    print(f"Report saved to: {monitor.results_dir}")
    
if __name__ == "__main__":
    main()
