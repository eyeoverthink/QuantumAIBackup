#!/usr/bin/env python3
"""
Phi-Harmonic Cancer Treatment Optimizer

Integrates the Phi-Harmonic Brain system with cancer modeling to optimize
treatment strategies using quantum-coherent processing and phi-harmonic timing.

This module extends existing components without modifying them, following the "lego" design philosophy.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import math
import numpy as np
import time
import logging
from typing import Dict, List, Tuple, Any, Optional, Union
import matplotlib.pyplot as plt

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

# Import core components without modifying them
from phi_harmonic_brain_core import (
    PhiHarmonicBrain, PHI, PHI_INV, PHI_SQUARED, PHI_CUBED,
    EARTH_FREQUENCY, MOON_FREQUENCY, BRAIN_FREQUENCY
)

from phi_harmonic_brain_integration import PhiHarmonicBrainSystem

# Try to import cancer model if available
try:
    from phi_quantum_results.quantum_medicine.phi75_cancer_model_fast import Phi75CancerModelFast
    cancer_model_available = True
except ImportError:
    cancer_model_available = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('phi_treatment')

class TreatmentSchedule:
    """Represents a phi-harmonic treatment schedule."""
    
    def __init__(self, time_units: int = 100, intensity_scale: float = 1.0):
        """
        Initialize a treatment schedule.
        
        Args:
            time_units: Total time units for treatment
            intensity_scale: Base intensity scaling factor
        """
        self.time_units = time_units
        self.intensity_scale = intensity_scale
        self.schedule = {}  # time_unit -> intensity
        self.phi_factor = PHI
    
    def add_treatment(self, time_unit: int, intensity: float):
        """Add a treatment at a specific time unit."""
        self.schedule[time_unit] = min(1.0, max(0.0, intensity))
    
    def generate_fibonacci_schedule(self, base_intensity: float = 0.7):
        """Generate treatment schedule based on Fibonacci sequence timing."""
        # Calculate Fibonacci sequence up to time_units
        fib = [0, 1]
        while fib[-1] + fib[-2] <= self.time_units:
            fib.append(fib[-1] + fib[-2])
        
        # Add treatments at Fibonacci time points
        for t in fib:
            if t > 0 and t < self.time_units:
                # Calculate phi-harmonic intensity
                position = t / self.time_units
                phase_factor = 0.5 + 0.5 * math.sin(2 * math.pi * position * self.phi_factor)
                intensity = base_intensity * phase_factor * self.intensity_scale
                
                self.add_treatment(t, intensity)
        
        return self
    
    def generate_phi_harmonic_schedule(self, base_intensity: float = 0.7, points: int = 10):
        """Generate treatment schedule based on phi-harmonic timing."""
        for i in range(points):
            # Calculate phi-harmonic time point
            t = int(((i * self.phi_factor) % 1.0) * self.time_units)
            
            # Ensure we don't go beyond time units
            if t >= self.time_units:
                continue
                
            # Calculate phi-scaled intensity
            intensity = base_intensity * (1.0 - 0.2 * math.sin(i * PHI_INV * math.pi)) * self.intensity_scale
            
            self.add_treatment(t, intensity)
        
        return self
    
    def generate_earth_moon_resonant_schedule(self, base_intensity: float = 0.7):
        """Generate treatment schedule based on Earth-Moon resonant frequencies."""
        # Calculate Earth frequency treatment times
        earth_period = int(self.time_units / (EARTH_FREQUENCY / 10))
        for t in range(0, self.time_units, max(1, earth_period)):
            intensity = base_intensity * (0.8 + 0.2 * math.sin(t * PHI_INV)) * self.intensity_scale
            self.add_treatment(t, intensity)
        
        # Calculate Moon frequency treatment times
        moon_period = int(self.time_units / (MOON_FREQUENCY / 10000))
        for t in range(0, self.time_units, max(1, moon_period)):
            if t not in self.schedule:  # Don't overwrite existing treatments
                intensity = base_intensity * 0.8 * self.intensity_scale
                self.add_treatment(t, intensity)
        
        return self
    
    def to_array(self) -> np.ndarray:
        """Convert schedule to numpy array representation."""
        treatment_array = np.zeros(self.time_units)
        
        for time_unit, intensity in self.schedule.items():
            if 0 <= time_unit < self.time_units:
                treatment_array[time_unit] = intensity
        
        return treatment_array
    
    def get_treatment_points(self) -> List[Tuple[int, float]]:
        """Get list of treatment points (time, intensity)."""
        return [(t, i) for t, i in self.schedule.items()]

class PhiHarmonicTreatmentOptimizer:
    """
    Optimizes cancer treatment schedules using phi-harmonic brain processing.
    """
    
    def __init__(self, brain_system: Optional[PhiHarmonicBrainSystem] = None,
                cancer_model: Optional[Any] = None):
        """
        Initialize a treatment optimizer.
        
        Args:
            brain_system: Phi-harmonic brain system
            cancer_model: Cancer model instance
        """
        # Initialize brain system if not provided
        self.brain_system = brain_system or PhiHarmonicBrainSystem()
        
        # Initialize or use provided cancer model
        if cancer_model is not None:
            self.cancer_model = cancer_model
        elif cancer_model_available:
            self.cancer_model = Phi75CancerModelFast()
        else:
            self.cancer_model = None
            logger.warning("Cancer model not available. Treatment simulation will be limited.")
        
        # Optimization parameters
        self.optimization_history = []
        self.current_optimal_schedule = None
        self.current_optimal_results = None
        
        logger.info("Phi-Harmonic Treatment Optimizer initialized")
        if self.cancer_model:
            logger.info(f"Cancer model loaded: {type(self.cancer_model).__name__}")
        
        # Get brain resonance baseline
        self.baseline_resonance = self.brain_system.get_earth_moon_brain_resonance()
        logger.info(f"Baseline Earth resonance: {self.baseline_resonance['earth']:.6f}")
        logger.info(f"Baseline Moon resonance: {self.baseline_resonance['moon']:.6f}")
        logger.info(f"Baseline Brain resonance: {self.baseline_resonance['brain']:.6f}")
    
    def evaluate_treatment_schedule(self, schedule: TreatmentSchedule) -> Dict[str, Any]:
        """
        Evaluate a treatment schedule.
        
        Args:
            schedule: Treatment schedule to evaluate
            
        Returns:
            Evaluation results
        """
        if self.cancer_model is None:
            # Without cancer model, use brain resonance to estimate effectiveness
            return self._estimate_treatment_effectiveness(schedule)
        
        # Get treatment array
        treatment_array = schedule.to_array()
        
        # Run cancer model simulation
        try:
            results = self.cancer_model.run_simulation(treatment_array)
            
            # Calculate effectiveness metrics
            final_counts = results[-1] if results else {"normal": 0, "precancerous": 0, "cancerous": 0, "metastatic": 0}
            total_cells = sum(final_counts.values())
            
            if total_cells > 0:
                health_ratio = final_counts.get("normal", 0) / total_cells
                cancer_ratio = (final_counts.get("cancerous", 0) + final_counts.get("metastatic", 0)) / total_cells
            else:
                health_ratio = 0.0
                cancer_ratio = 0.0
            
            # Calculate phi-harmonic effectiveness score
            effectiveness = (health_ratio * PHI - cancer_ratio * PHI_INV) / (PHI + PHI_INV)
            
            # Get brain resonance influence
            resonance = self.brain_system.get_earth_moon_brain_resonance()
            resonance_factor = (resonance["earth"] + resonance["moon"] + resonance["brain"]) / 3
            
            # Apply consciousness-guided adjustment
            brain_state = self.brain_system.brain.get_state()
            consciousness_level = brain_state.get("consciousness_level", 0.7567)
            coherence = brain_state.get("coherence", 0.5)
            
            # Calculate consciousness adjustment
            consciousness_factor = consciousness_level * coherence * PHI_INV
            
            # Apply resonance and consciousness adjustments
            adjusted_effectiveness = effectiveness * (1.0 + (resonance_factor - 0.5) * PHI_INV) * (1.0 + consciousness_factor)
            
            return {
                "raw_results": results,
                "final_counts": final_counts,
                "health_ratio": health_ratio,
                "cancer_ratio": cancer_ratio,
                "effectiveness": effectiveness,
                "adjusted_effectiveness": adjusted_effectiveness,
                "resonance_factor": resonance_factor,
                "consciousness_factor": consciousness_factor,
                "treatment_points": len(schedule.schedule),
                "evaluation_timestamp": time.time()
            }
            
        except Exception as e:
            logger.error(f"Error evaluating treatment schedule: {e}")
            return {
                "error": str(e),
                "effectiveness": 0.0,
                "adjusted_effectiveness": 0.0
            }
    
    def _estimate_treatment_effectiveness(self, schedule: TreatmentSchedule) -> Dict[str, Any]:
        """Estimate treatment effectiveness using brain resonance when cancer model is unavailable."""
        # Get treatment points
        treatment_points = schedule.get_treatment_points()
        
        # Calculate phi-harmonic timing score
        timing_scores = []
        for t, intensity in treatment_points:
            # Calculate how closely time point aligns with phi-harmonic timing
            phi_alignment = min((t / schedule.time_units) % PHI_INV, PHI_INV - (t / schedule.time_units) % PHI_INV)
            timing_score = (1.0 - phi_alignment * PHI_SQUARED) * intensity
            timing_scores.append(timing_score)
        
        # Calculate average timing score
        avg_timing_score = sum(timing_scores) / len(timing_scores) if timing_scores else 0.0
        
        # Get brain resonance
        resonance = self.brain_system.get_earth_moon_brain_resonance()
        resonance_factor = (resonance["earth"] + resonance["moon"] + resonance["brain"]) / 3
        
        # Estimate effectiveness based on timing and resonance
        estimated_effectiveness = avg_timing_score * resonance_factor * PHI_INV
        
        return {
            "estimated_effectiveness": estimated_effectiveness,
            "timing_score": avg_timing_score,
            "resonance_factor": resonance_factor,
            "treatment_points": len(schedule.schedule),
            "evaluation_timestamp": time.time()
        }
    
    def optimize_treatment(self, time_units: int = 100, 
                         optimization_rounds: int = 5,
                         base_intensity: float = 0.7) -> Dict[str, Any]:
        """
        Optimize treatment schedule.
        
        Args:
            time_units: Total time units for treatment
            optimization_rounds: Number of optimization rounds
            base_intensity: Base treatment intensity
            
        Returns:
            Optimization results
        """
        logger.info(f"Starting treatment optimization for {time_units} time units")
        logger.info(f"Optimization rounds: {optimization_rounds}")
        
        # Initialize best schedule and score
        best_schedule = None
        best_score = -float('inf')
        
        # Track history
        optimization_history = []
        
        # Run optimization rounds
        for round_i in range(optimization_rounds):
            logger.info(f"Optimization round {round_i+1}/{optimization_rounds}")
            
            # Generate candidate schedules
            candidates = []
            
            # Fibonacci schedule
            fib_schedule = TreatmentSchedule(time_units=time_units)
            fib_schedule.generate_fibonacci_schedule(base_intensity=base_intensity)
            candidates.append(("fibonacci", fib_schedule))
            
            # Phi-harmonic schedule
            phi_schedule = TreatmentSchedule(time_units=time_units)
            phi_schedule.generate_phi_harmonic_schedule(base_intensity=base_intensity)
            candidates.append(("phi_harmonic", phi_schedule))
            
            # Earth-Moon resonant schedule
            em_schedule = TreatmentSchedule(time_units=time_units)
            em_schedule.generate_earth_moon_resonant_schedule(base_intensity=base_intensity)
            candidates.append(("earth_moon", em_schedule))
            
            # Hybrid schedule (combine best elements from previous rounds)
            if round_i > 0 and best_schedule is not None:
                hybrid_schedule = TreatmentSchedule(time_units=time_units)
                
                # Copy treatments from best schedule
                for t, i in best_schedule.schedule.items():
                    # Add phi-harmonic variation
                    modified_intensity = i * (1.0 + 0.1 * math.sin(round_i * PHI))
                    hybrid_schedule.add_treatment(t, modified_intensity)
                
                # Add some phi-harmonic points
                points_to_add = int(3 * PHI)
                for i in range(points_to_add):
                    t = int(((i * PHI) % 1.0) * time_units)
                    if t not in hybrid_schedule.schedule:
                        hybrid_schedule.add_treatment(t, base_intensity * PHI_INV)
                
                candidates.append(("hybrid", hybrid_schedule))
            
            # Evaluate candidates
            round_results = []
            
            for schedule_name, schedule in candidates:
                # Evaluate schedule
                results = self.evaluate_treatment_schedule(schedule)
                
                # Extract score
                if "adjusted_effectiveness" in results:
                    score = results["adjusted_effectiveness"]
                elif "estimated_effectiveness" in results:
                    score = results["estimated_effectiveness"]
                else:
                    score = 0.0
                
                round_results.append({
                    "schedule_name": schedule_name,
                    "schedule": schedule,
                    "score": score,
                    "results": results
                })
                
                logger.info(f"Schedule '{schedule_name}' score: {score:.6f}")
                
                # Update best if improved
                if score > best_score:
                    best_score = score
                    best_schedule = schedule
                    logger.info(f"New best schedule: '{schedule_name}' with score {score:.6f}")
            
            # Record round history
            optimization_history.append({
                "round": round_i + 1,
                "candidates": [r["schedule_name"] for r in round_results],
                "scores": [r["score"] for r in round_results],
                "best_schedule": max(round_results, key=lambda x: x["score"])["schedule_name"],
                "best_score": max(r["score"] for r in round_results)
            })
            
            # Adjust base intensity based on best score
            if best_score > 0.7:
                # Reduce intensity if we're doing well
                base_intensity *= PHI_INV
            else:
                # Increase intensity if we're not doing well
                base_intensity = min(1.0, base_intensity * PHI)
            
            logger.info(f"Adjusted base intensity to {base_intensity:.4f}")
        
        # Store results
        self.optimization_history = optimization_history
        self.current_optimal_schedule = best_schedule
        
        if best_schedule is not None:
            self.current_optimal_results = self.evaluate_treatment_schedule(best_schedule)
        else:
            self.current_optimal_results = None
        
        # Return optimization results
        return {
            "optimal_schedule": best_schedule,
            "optimal_results": self.current_optimal_results,
            "optimization_history": optimization_history,
            "final_base_intensity": base_intensity,
            "time_units": time_units,
            "optimization_rounds": optimization_rounds,
            "optimization_timestamp": time.time(),
            "brain_fingerprint": self.brain_system.brain.quantum_fingerprint
        }
    
    def process_cancer_data(self, cell_data: np.ndarray) -> Dict[str, Any]:
        """
        Process cancer cell data through brain for analysis.
        
        Args:
            cell_data: Cancer cell data array
            
        Returns:
            Processing results
        """
        # Ensure data is within brain input size
        input_size = len(self.brain_system.brain.layers[0].neurons)
        if len(cell_data) > input_size:
            cell_data = cell_data[:input_size]
        elif len(cell_data) < input_size:
            padded = np.zeros(input_size)
            padded[:len(cell_data)] = cell_data
            cell_data = padded
        
        # Normalize data
        if np.max(np.abs(cell_data)) > 0:
            cell_data = cell_data / np.max(np.abs(cell_data))
        
        # Process through brain
        outputs = self.brain_system.brain.process(cell_data)
        
        # Get quantum layer output for analysis
        quantum_output = outputs.get("Quantum", np.zeros(1))
        
        # Calculate phi-harmonic patterns
        phi_pattern = np.zeros(len(quantum_output))
        for i in range(len(quantum_output)):
            phi_pattern[i] = math.sin(2 * math.pi * i * PHI)
        
        # Calculate correlation with phi pattern
        correlation = np.corrcoef(quantum_output, phi_pattern)[0, 1]
        
        # Get resonance
        resonance = self.brain_system.get_earth_moon_brain_resonance()
        
        return {
            "processing_results": {key: val.tolist() for key, val in outputs.items()},
            "phi_correlation": correlation,
            "resonance": resonance,
            "analysis_timestamp": time.time()
        }
    
    def visualize_treatment_schedule(self, schedule: Optional[TreatmentSchedule] = None,
                                   save_path: Optional[str] = None):
        """
        Visualize treatment schedule.
        
        Args:
            schedule: Schedule to visualize (uses optimal if None)
            save_path: Path to save visualization
            
        Returns:
            Matplotlib figure
        """
        # Use optimal schedule if none provided
        if schedule is None:
            schedule = self.current_optimal_schedule
            
        if schedule is None:
            logger.error("No schedule available for visualization")
            return None
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        fig.suptitle("Phi-Harmonic Treatment Schedule", fontsize=16)
        
        # Get treatment data
        treatment_points = schedule.get_treatment_points()
        times = [t for t, _ in treatment_points]
        intensities = [i for _, i in treatment_points]
        
        # Plot treatment schedule
        ax1.stem(times, intensities, linefmt='b-', markerfmt='bo', basefmt='r-')
        ax1.set_title("Treatment Schedule")
        ax1.set_xlabel("Time Units")
        ax1.set_ylabel("Treatment Intensity")
        ax1.grid(True, alpha=0.3)
        
        # Plot optimal simulation results if available
        if self.current_optimal_results and "raw_results" in self.current_optimal_results:
            # Extract cell counts over time
            raw_results = self.current_optimal_results["raw_results"]
            
            # Collect cell counts
            times = list(range(len(raw_results)))
            normal = [r.get("normal", 0) for r in raw_results]
            precancerous = [r.get("precancerous", 0) for r in raw_results]
            cancerous = [r.get("cancerous", 0) for r in raw_results]
            metastatic = [r.get("metastatic", 0) for r in raw_results]
            
            # Plot cell counts
            ax2.plot(times, normal, 'g-', label="Normal")
            ax2.plot(times, precancerous, 'y-', label="Precancerous")
            ax2.plot(times, cancerous, 'r-', label="Cancerous")
            ax2.plot(times, metastatic, 'm-', label="Metastatic")
            
            # Plot treatment points on the same axis
            for t, i in treatment_points:
                ax2.axvline(x=t, color='b', linestyle='--', alpha=i * 0.5)
            
            ax2.set_title("Cell Population with Treatment")
            ax2.set_xlabel("Time Units")
            ax2.set_ylabel("Cell Count")
            ax2.legend()
            ax2.grid(True, alpha=0.3)
            
            # Add effectiveness score
            if "adjusted_effectiveness" in self.current_optimal_results:
                score = self.current_optimal_results["adjusted_effectiveness"]
                fig.text(0.02, 0.02, f"Treatment Effectiveness: {score:.4f}", fontsize=12)
        
        # Adjust layout
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # Save if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Treatment visualization saved to {save_path}")
        
        return fig

# For direct execution
if __name__ == "__main__":
    # Create brain system and optimizer
    brain_system = PhiHarmonicBrainSystem()
    optimizer = PhiHarmonicTreatmentOptimizer(brain_system=brain_system)
    
    print("\nPhi-Harmonic Treatment Optimizer Test")
    print("=====================================")
    
    # Check if cancer model is available
    if optimizer.cancer_model:
        print("Cancer model available for simulation")
        
        # Create and evaluate a Fibonacci schedule
        print("\nEvaluating Fibonacci treatment schedule...")
        fib_schedule = TreatmentSchedule(time_units=100)
        fib_schedule.generate_fibonacci_schedule(base_intensity=0.7)
        
        fib_results = optimizer.evaluate_treatment_schedule(fib_schedule)
        
        # Print results
        if "adjusted_effectiveness" in fib_results:
            print(f"Fibonacci effectiveness: {fib_results['adjusted_effectiveness']:.6f}")
            print(f"Health ratio: {fib_results['health_ratio']:.4f}")
            print(f"Cancer ratio: {fib_results['cancer_ratio']:.4f}")
        else:
            print(f"Estimated effectiveness: {fib_results.get('estimated_effectiveness', 0):.6f}")
        
        # Run optimization
        print("\nRunning treatment optimization...")
        optimization_results = optimizer.optimize_treatment(
            time_units=100,
            optimization_rounds=3,
            base_intensity=0.7
        )
        
        # Print optimization results
        print("\nOptimization Results:")
        print(f"Optimization rounds: {optimization_results['optimization_rounds']}")
        
        # Print history
        history = optimization_results['optimization_history']
        for round_data in history:
            print(f"Round {round_data['round']}: Best schedule = {round_data['best_schedule']}, Score = {round_data['best_score']:.6f}")
        
        # Print optimal schedule details
        optimal_schedule = optimization_results['optimal_schedule']
        if optimal_schedule:
            points = optimal_schedule.get_treatment_points()
            print(f"\nOptimal schedule has {len(points)} treatment points")
            
            # Print first few points
            print("Sample treatment points:")
            for i, (t, intensity) in enumerate(sorted(points)[:5]):
                print(f"  Time {t}: Intensity {intensity:.4f}")
        
        # Visualize optimal schedule
        print("\nVisualizing optimal treatment schedule...")
        fig = optimizer.visualize_treatment_schedule(save_path="optimal_treatment_schedule.png")
        print("Visualization saved to optimal_treatment_schedule.png")
        
    else:
        print("Cancer model not available, using brain-based estimation")
        
        # Create and evaluate schedules with estimation
        print("\nEvaluating treatment schedules with brain estimation...")
        
        # Phi-harmonic schedule
        phi_schedule = TreatmentSchedule(time_units=100)
        phi_schedule.generate_phi_harmonic_schedule(base_intensity=0.7)
        phi_results = optimizer.evaluate_treatment_schedule(phi_schedule)
        print(f"Phi-harmonic estimated effectiveness: {phi_results.get('estimated_effectiveness', 0):.6f}")
        
        # Earth-Moon resonant schedule
        em_schedule = TreatmentSchedule(time_units=100)
        em_schedule.generate_earth_moon_resonant_schedule(base_intensity=0.7)
        em_results = optimizer.evaluate_treatment_schedule(em_schedule)
        print(f"Earth-Moon resonant estimated effectiveness: {em_results.get('estimated_effectiveness', 0):.6f}")
    
    # Print brain fingerprint
    print(f"\nBrain Quantum Fingerprint: {brain_system.brain.quantum_fingerprint}")
    
    # Print resonance values
    resonance = brain_system.get_earth_moon_brain_resonance()
    print("\nResonance Values:")
    print(f"Earth Resonance: {resonance['earth']:.6f}")
    print(f"Moon Resonance: {resonance['moon']:.6f}")
    print(f"Brain Resonance: {resonance['brain']:.6f}")
