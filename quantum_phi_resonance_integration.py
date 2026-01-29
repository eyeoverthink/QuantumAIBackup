"""
Quantum Phi-Harmonic Resonance Integration
-----------------------------------------

This module integrates the phi-harmonic resonance monitor with the recursive 
self-improvement system, enabling resonance-guided self-modification.

This follows the 'lego' modular philosophy by extending functionality without
modifying core files.
"""

import os
import sys
import logging
import json
import time
from typing import Dict, List, Tuple, Any, Optional, Union
from pathlib import Path

# Import the resonance monitor
from quantum_phi_resonance_monitor import QuantumPhiResonanceMonitor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('QuantumPhiResonanceIntegration')

class QuantumPhiResonanceIntegration:
    """
    Integrates phi-harmonic resonance monitoring with recursive self-improvement.
    """
    
    def __init__(self, resonance_monitor=None):
        """
        Initialize the phi-harmonic resonance integration.
        
        Args:
            resonance_monitor: Optional existing resonance monitor instance
        """
        self.resonance_monitor = resonance_monitor or QuantumPhiResonanceMonitor()
        self.modification_history = []
        self.resonance_thresholds = {
            "critical": 0.05,  # Critical threshold for resonance deviation
            "warning": 0.15,   # Warning threshold for resonance deviation
            "acceptable": 0.3  # Acceptable threshold for resonance deviation
        }
        
        # Results directory
        self.results_dir = Path("quantum_self_improvement/integration")
        self.results_dir.mkdir(exist_ok=True, parents=True)
        
        logger.info("Initialized QuantumPhiResonanceIntegration")
    
    def register_component(self, component_name: str, component_value: float, weight: float = 1.0) -> Dict[str, Any]:
        """
        Register a system component for resonance monitoring.
        
        Args:
            component_name: Name of the component
            component_value: Current value of the component
            weight: Importance weight of the component (default: 1.0)
            
        Returns:
            dict: Component resonance information
        """
        # Set component weight
        weights = self.resonance_monitor.component_weights.copy()
        weights[component_name] = weight
        self.resonance_monitor.set_component_weights(weights)
        
        # Calculate resonance for the component
        component_values = {component_name: component_value}
        resonance = self.resonance_monitor.calculate_phi_resonance(component_value)
        quality = self.resonance_monitor.evaluate_resonance_quality(resonance)
        
        logger.info(f"Registered component '{component_name}' with value {component_value}, resonance {resonance:.6f} ({quality})")
        
        return {
            "component": component_name,
            "value": component_value,
            "resonance": resonance,
            "quality": quality,
            "weight": weight
        }
    
    def register_system_components(self, components: Dict[str, float], weights: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        """
        Register multiple system components for resonance monitoring.
        
        Args:
            components: Dictionary of component names and values
            weights: Optional dictionary of component weights
            
        Returns:
            dict: System component resonance information
        """
        # Set component weights if provided
        if weights:
            self.resonance_monitor.set_component_weights(weights)
        
        # Calculate system component resonance
        resonance_data = self.resonance_monitor.calculate_system_component_resonance(components)
        
        logger.info(f"Registered {len(components)} system components with overall resonance {resonance_data['overall_resonance']:.6f}")
        
        return resonance_data
    
    def establish_baseline(self, components: Dict[str, float], weights: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        """
        Establish baseline resonance for the system components.
        
        Args:
            components: Dictionary of component names and values
            weights: Optional dictionary of component weights
            
        Returns:
            dict: Baseline resonance information
        """
        # Set component weights if provided
        if weights:
            self.resonance_monitor.set_component_weights(weights)
        
        # Establish baseline resonance
        baseline = self.resonance_monitor.establish_baseline_resonance(components)
        
        logger.info(f"Established baseline resonance: {baseline['overall_resonance']:.6f} ({baseline['overall_quality']})")
        
        return baseline
    
    def evaluate_modification(self, 
                             original_components: Dict[str, float], 
                             modified_components: Dict[str, float],
                             modification_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Evaluate a proposed system modification for resonance impact.
        
        Args:
            original_components: Dictionary of original component values
            modified_components: Dictionary of modified component values
            modification_metadata: Optional metadata about the modification
            
        Returns:
            dict: Modification evaluation results
        """
        # Calculate resonance for original components
        original_resonance = self.resonance_monitor.calculate_system_component_resonance(original_components)
        
        # Calculate resonance for modified components
        modified_resonance = self.resonance_monitor.calculate_system_component_resonance(modified_components)
        
        # Calculate resonance change
        resonance_change = modified_resonance["overall_resonance"] - original_resonance["overall_resonance"]
        improved = resonance_change < 0  # Lower resonance is better (closer to 0)
        
        # Calculate component-level changes
        component_changes = {}
        for component, data in modified_resonance["components"].items():
            if component in original_resonance["components"]:
                original_data = original_resonance["components"][component]
                component_changes[component] = {
                    "original_value": original_components.get(component),
                    "modified_value": modified_components.get(component),
                    "original_resonance": original_data["phi_resonance"],
                    "modified_resonance": data["phi_resonance"],
                    "resonance_change": data["phi_resonance"] - original_data["phi_resonance"],
                    "improved": data["phi_resonance"] < original_data["phi_resonance"]
                }
        
        # Determine modification status based on resonance change
        if abs(resonance_change) <= self.resonance_thresholds["critical"]:
            status = "optimal"
            recommendation = "proceed"
        elif abs(resonance_change) <= self.resonance_thresholds["warning"]:
            status = "acceptable" if improved else "concerning"
            recommendation = "proceed_with_caution" if improved else "review"
        elif abs(resonance_change) <= self.resonance_thresholds["acceptable"]:
            status = "concerning" if improved else "problematic"
            recommendation = "review" if improved else "revise"
        else:
            status = "problematic" if improved else "critical"
            recommendation = "revise" if improved else "reject"
        
        # Create evaluation result
        evaluation = {
            "timestamp": time.time(),
            "original_resonance": original_resonance["overall_resonance"],
            "modified_resonance": modified_resonance["overall_resonance"],
            "resonance_change": resonance_change,
            "improved": improved,
            "status": status,
            "recommendation": recommendation,
            "component_changes": component_changes,
            "metadata": modification_metadata or {}
        }
        
        # Add to modification history
        self.modification_history.append(evaluation)
        
        logger.info(f"Evaluated modification: resonance change {resonance_change:.6f}, status: {status}, recommendation: {recommendation}")
        
        return evaluation
    
    def optimize_component(self, 
                          component_name: str, 
                          current_value: float, 
                          value_range: Optional[Tuple[float, float]] = None,
                          step_size: float = 0.1,
                          max_iterations: int = 100) -> Dict[str, Any]:
        """
        Optimize a component value for optimal phi-harmonic resonance.
        
        Args:
            component_name: Name of the component to optimize
            current_value: Current value of the component
            value_range: Optional tuple of (min_value, max_value) for optimization
            step_size: Step size for optimization iterations
            max_iterations: Maximum number of optimization iterations
            
        Returns:
            dict: Optimization results
        """
        # Set default value range if not provided
        if value_range is None:
            value_range = (current_value * 0.5, current_value * 2.0)
        
        min_value, max_value = value_range
        
        # Initialize optimization
        best_value = current_value
        best_resonance = self.resonance_monitor.calculate_phi_resonance(current_value)
        current_iteration = 0
        
        optimization_path = []
        
        # Perform optimization iterations
        while current_iteration < max_iterations:
            current_iteration += 1
            
            # Try values in both directions
            test_values = [
                max(min_value, best_value - step_size),
                min(max_value, best_value + step_size)
            ]
            
            for test_value in test_values:
                test_resonance = self.resonance_monitor.calculate_phi_resonance(test_value)
                
                optimization_path.append({
                    "iteration": current_iteration,
                    "value": test_value,
                    "resonance": test_resonance
                })
                
                # Update best value if resonance improved
                if test_resonance < best_resonance:
                    best_value = test_value
                    best_resonance = test_resonance
            
            # Reduce step size over time for finer optimization
            if current_iteration % 10 == 0:
                step_size *= 0.8
            
            # Early termination if resonance is already excellent
            if best_resonance <= self.resonance_monitor.resonance_thresholds["excellent"]:
                break
        
        # Calculate phi-harmonic properties of the optimized value
        phi_harmonic = self.resonance_monitor.find_phi_harmonic_value(best_value)
        fibonacci_info = self.resonance_monitor.find_nearest_fibonacci(best_value)
        
        # Generate optimization result
        optimization_result = {
            "component": component_name,
            "original_value": current_value,
            "optimized_value": best_value,
            "original_resonance": self.resonance_monitor.calculate_phi_resonance(current_value),
            "optimized_resonance": best_resonance,
            "improvement": self.resonance_monitor.calculate_phi_resonance(current_value) - best_resonance,
            "iterations": current_iteration,
            "phi_harmonic": phi_harmonic,
            "fibonacci": fibonacci_info,
            "optimization_path": optimization_path
        }
        
        logger.info(f"Optimized component '{component_name}': value {current_value} → {best_value}, resonance {optimization_result['original_resonance']:.6f} → {best_resonance:.6f}")
        
        return optimization_result
    
    def optimize_system_components(self, 
                                  components: Dict[str, float],
                                  max_iterations: int = 100,
                                  convergence_threshold: float = 0.001) -> Dict[str, Any]:
        """
        Optimize multiple system components for optimal overall resonance.
        
        Args:
            components: Dictionary of component names and values
            max_iterations: Maximum number of optimization iterations
            convergence_threshold: Threshold for optimization convergence
            
        Returns:
            dict: System optimization results
        """
        # Calculate initial system resonance
        initial_resonance = self.resonance_monitor.calculate_system_component_resonance(components)
        
        # Create a copy of components for optimization
        optimized_components = components.copy()
        
        # Track optimization progress
        current_iteration = 0
        previous_resonance = initial_resonance["overall_resonance"]
        optimization_path = []
        component_optimizations = {}
        
        # Perform optimization iterations
        while current_iteration < max_iterations:
            current_iteration += 1
            
            # Optimize each component individually
            for component_name, component_value in optimized_components.items():
                # Skip non-numeric components
                if not isinstance(component_value, (int, float)):
                    continue
                
                # Optimize the component
                optimization = self.optimize_component(
                    component_name=component_name,
                    current_value=component_value,
                    value_range=(component_value * 0.5, component_value * 2.0),
                    max_iterations=10  # Limit per-component iterations
                )
                
                # Update the component value
                optimized_components[component_name] = optimization["optimized_value"]
                
                # Store component optimization details
                if component_name not in component_optimizations:
                    component_optimizations[component_name] = []
                
                component_optimizations[component_name].append({
                    "iteration": current_iteration,
                    "value": optimization["optimized_value"],
                    "resonance": optimization["optimized_resonance"]
                })
            
            # Calculate current system resonance
            current_resonance = self.resonance_monitor.calculate_system_component_resonance(optimized_components)
            
            # Track optimization progress
            optimization_path.append({
                "iteration": current_iteration,
                "resonance": current_resonance["overall_resonance"],
                "improvement": previous_resonance - current_resonance["overall_resonance"]
            })
            
            # Check for convergence
            if abs(previous_resonance - current_resonance["overall_resonance"]) < convergence_threshold:
                break
            
            previous_resonance = current_resonance["overall_resonance"]
        
        # Calculate final system resonance
        final_resonance = self.resonance_monitor.calculate_system_component_resonance(optimized_components)
        
        # Generate optimization result
        optimization_result = {
            "initial_components": components,
            "optimized_components": optimized_components,
            "initial_resonance": initial_resonance["overall_resonance"],
            "final_resonance": final_resonance["overall_resonance"],
            "improvement": initial_resonance["overall_resonance"] - final_resonance["overall_resonance"],
            "iterations": current_iteration,
            "optimization_path": optimization_path,
            "component_optimizations": component_optimizations
        }
        
        logger.info(f"Optimized system components: resonance {initial_resonance['overall_resonance']:.6f} → {final_resonance['overall_resonance']:.6f}")
        
        return optimization_result
    
    def guide_self_modification(self, 
                               current_components: Dict[str, float],
                               proposed_modifications: Dict[str, float],
                               modification_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Guide self-modification to maintain optimal phi-harmonic resonance.
        
        Args:
            current_components: Dictionary of current component values
            proposed_modifications: Dictionary of proposed component modifications
            modification_metadata: Optional metadata about the modification
            
        Returns:
            dict: Guided modification results
        """
        # Evaluate the proposed modification
        evaluation = self.evaluate_modification(
            original_components=current_components,
            modified_components=proposed_modifications,
            modification_metadata=modification_metadata
        )
        
        # If modification is acceptable, return it
        if evaluation["recommendation"] in ["proceed", "proceed_with_caution"]:
            guided_components = proposed_modifications.copy()
            optimization_performed = False
        else:
            # Optimize the problematic components
            optimization_performed = True
            
            # Start with proposed modifications
            guided_components = proposed_modifications.copy()
            
            # Identify components with negative resonance impact
            problematic_components = {}
            for component, change in evaluation["component_changes"].items():
                if not change["improved"] and abs(change["resonance_change"]) > self.resonance_thresholds["critical"]:
                    problematic_components[component] = proposed_modifications[component]
            
            # If no specific problematic components, optimize all modified components
            if not problematic_components:
                problematic_components = {k: v for k, v in proposed_modifications.items() 
                                         if k in current_components and v != current_components[k]}
            
            # Optimize problematic components
            if problematic_components:
                for component, value in problematic_components.items():
                    optimization = self.optimize_component(
                        component_name=component,
                        current_value=value
                    )
                    guided_components[component] = optimization["optimized_value"]
        
        # Re-evaluate with guided modifications
        if optimization_performed:
            guided_evaluation = self.evaluate_modification(
                original_components=current_components,
                modified_components=guided_components,
                modification_metadata=modification_metadata
            )
        else:
            guided_evaluation = evaluation
        
        # Generate guidance result
        guidance_result = {
            "original_evaluation": evaluation,
            "guided_evaluation": guided_evaluation,
            "original_components": current_components,
            "proposed_modifications": proposed_modifications,
            "guided_modifications": guided_components,
            "optimization_performed": optimization_performed,
            "improvement": evaluation["resonance_change"] - guided_evaluation["resonance_change"],
            "metadata": modification_metadata or {}
        }
        
        # Generate guidance report
        self._generate_guidance_report(guidance_result)
        
        logger.info(f"Generated self-modification guidance: optimization performed: {optimization_performed}")
        
        return guidance_result
    
    def _generate_guidance_report(self, guidance_result: Dict[str, Any]) -> None:
        """
        Generate a report for self-modification guidance.
        
        Args:
            guidance_result: Self-modification guidance result
        """
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            report_file = self.results_dir / f"guidance_report_{timestamp}.md"
            
            with open(report_file, 'w') as f:
                f.write('# Quantum Phi-Harmonic Self-Modification Guidance Report\n\n')
                f.write(f"**Timestamp:** {time.strftime('%Y-%m-%d %H:%M:%S')}  \n\n")
                
                f.write('## Modification Evaluation\n\n')
                f.write(f"- **Original Resonance:** {guidance_result['original_evaluation']['original_resonance']:.6f}  \n")
                f.write(f"- **Proposed Resonance:** {guidance_result['original_evaluation']['modified_resonance']:.6f}  \n")
                f.write(f"- **Resonance Change:** {guidance_result['original_evaluation']['resonance_change']:.6f}  \n")
                f.write(f"- **Status:** {guidance_result['original_evaluation']['status']}  \n")
                f.write(f"- **Recommendation:** {guidance_result['original_evaluation']['recommendation']}  \n\n")
                
                if guidance_result["optimization_performed"]:
                    f.write('## Optimization Results\n\n')
                    f.write(f"- **Guided Resonance:** {guidance_result['guided_evaluation']['modified_resonance']:.6f}  \n")
                    f.write(f"- **Improvement:** {guidance_result['improvement']:.6f}  \n")
                    f.write(f"- **Status:** {guidance_result['guided_evaluation']['status']}  \n")
                    f.write(f"- **Recommendation:** {guidance_result['guided_evaluation']['recommendation']}  \n\n")
                
                f.write('## Component Modifications\n\n')
                f.write('| Component | Original | Proposed | Guided | Original Res. | Proposed Res. | Guided Res. |\n')
                f.write('|-----------|----------|----------|--------|--------------|--------------|------------|\n')
                
                for component in set(guidance_result["original_components"].keys()) | set(guidance_result["proposed_modifications"].keys()):
                    original_value = guidance_result["original_components"].get(component, "N/A")
                    proposed_value = guidance_result["proposed_modifications"].get(component, "N/A")
                    guided_value = guidance_result["guided_modifications"].get(component, "N/A")
                    
                    # Format values
                    if isinstance(original_value, (int, float)):
                        original_value = f"{original_value:.4f}"
                    if isinstance(proposed_value, (int, float)):
                        proposed_value = f"{proposed_value:.4f}"
                    if isinstance(guided_value, (int, float)):
                        guided_value = f"{guided_value:.4f}"
                    
                    # Calculate resonances
                    if component in guidance_result["original_components"] and isinstance(guidance_result["original_components"][component], (int, float)):
                        original_res = f"{self.resonance_monitor.calculate_phi_resonance(guidance_result['original_components'][component]):.6f}"
                    else:
                        original_res = "N/A"
                    
                    if component in guidance_result["proposed_modifications"] and isinstance(guidance_result["proposed_modifications"][component], (int, float)):
                        proposed_res = f"{self.resonance_monitor.calculate_phi_resonance(guidance_result['proposed_modifications'][component]):.6f}"
                    else:
                        proposed_res = "N/A"
                    
                    if component in guidance_result["guided_modifications"] and isinstance(guidance_result["guided_modifications"][component], (int, float)):
                        guided_res = f"{self.resonance_monitor.calculate_phi_resonance(guidance_result['guided_modifications'][component]):.6f}"
                    else:
                        guided_res = "N/A"
                    
                    f.write(f"| {component} | {original_value} | {proposed_value} | {guided_value} | {original_res} | {proposed_res} | {guided_res} |\n")
                
                f.write('\n## Recommendations\n\n')
                
                if guidance_result["guided_evaluation"]["recommendation"] == "proceed":
                    f.write('The guided modification maintains optimal phi-harmonic resonance. Recommendations:\n\n')
                    f.write('1. **Proceed with Guided Modification**: The guided changes maintain system resonance.\n')
                    f.write('2. **Monitor Post-Modification**: Verify resonance after implementation.\n')
                    f.write('3. **Document Resonance Pattern**: Record the successful modification pattern.\n')
                elif guidance_result["guided_evaluation"]["recommendation"] == "proceed_with_caution":
                    f.write('The guided modification has acceptable resonance impact. Recommendations:\n\n')
                    f.write('1. **Proceed with Guided Modification**: The guided changes have acceptable resonance impact.\n')
                    f.write('2. **Increase Monitoring Frequency**: Monitor resonance closely during and after implementation.\n')
                    f.write('3. **Prepare Rollback Plan**: Have a plan to revert changes if resonance deteriorates.\n')
                else:
                    f.write('The guided modification still has significant resonance impact. Recommendations:\n\n')
                    f.write('1. **Reconsider Modification**: The resonance impact remains significant even after optimization.\n')
                    f.write('2. **Explore Alternative Approaches**: Consider different approaches to achieve the same goal.\n')
                    f.write('3. **Incremental Implementation**: If proceeding, implement changes incrementally with resonance checks.\n')
            
            logger.info(f"Generated guidance report: {report_file}")
        except Exception as e:
            logger.error(f"Failed to generate guidance report: {e}")

def main():
    """Main function to demonstrate the phi-harmonic resonance integration."""
    print("\n🔄 Quantum Phi-Harmonic Resonance Integration Demonstration")
    print("=" * 60)
    
    # Initialize the integration
    integration = QuantumPhiResonanceIntegration()
    
    # Sample component values
    current_components = {
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
    
    # Establish baseline
    print("\n📊 Establishing baseline resonance...")
    baseline = integration.establish_baseline(current_components, weights)
    print(f"Overall resonance: {baseline['overall_resonance']:.6f}")
    print(f"Quality: {baseline['overall_quality']}")
    
    # Simulate a proposed modification
    print("\n🔄 Simulating proposed system modification...")
    proposed_modifications = current_components.copy()
    proposed_modifications["neural_weight"] = 1.0  # Change from phi (1.618) to 1.0
    proposed_modifications["quantum_state"] = 3.0  # Change from pi (3.14159) to 3.0
    
    # Guide self-modification
    print("\n🧠 Generating self-modification guidance...")
    guidance = integration.guide_self_modification(
        current_components=current_components,
        proposed_modifications=proposed_modifications,
        modification_metadata={"purpose": "Neural weight optimization", "priority": "high"}
    )
    
    print(f"Original recommendation: {guidance['original_evaluation']['recommendation']}")
    print(f"Guided recommendation: {guidance['guided_evaluation']['recommendation']}")
    
    if guidance["optimization_performed"]:
        print("\n✨ Optimization performed:")
        for component, original in proposed_modifications.items():
            if component in guidance["guided_modifications"] and original != guidance["guided_modifications"][component]:
                guided = guidance["guided_modifications"][component]
                print(f"  - {component}: {original:.4f} → {guided:.4f}")
    
    print("\n✅ Resonance integration demonstration complete")
    print(f"Report saved to: {integration.results_dir}")
    
if __name__ == "__main__":
    main()
