#!/usr/bin/env python3
"""
Phi-Harmonic Cancer Model

A quantum-inspired cancer growth modeling system using phi-harmonic principles
to simulate cancer cell proliferation, mutation, and response to treatment.

Key features:
- Golden ratio (φ) based cell division patterns
- Quantum randomness for mutation modeling
- Phi-dimensional reality protection for treatment simulation
- Multi-consciousness cancer cell state mapping
"""

import os
import sys
import math
import numpy as np
import json
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
import random

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
PHI_INVERSE = 1 / PHI
PHI_SQUARED = PHI ** 2
PHI_CUBED = PHI ** 3
BASE_FREQUENCY = 432.0  # Base frequency for resonance

# Try to import phi-harmonic random if available
try:
    sys.path.append(os.path.join(parent_dir, 'phi_harmonic_random'))
    import phi_harmonic_random as phi_random
    PHI_RANDOM_AVAILABLE = True
    print("Phi-Harmonic Random module loaded successfully")
except ImportError:
    PHI_RANDOM_AVAILABLE = False
    print("Phi-Harmonic Random module not available, using simulated phi-random")

class PhiHarmonicCellState:
    """
    Represents a cell state with phi-harmonic properties.
    """
    
    def __init__(self, 
                cell_type: str = "normal", 
                division_rate: float = 0.05,
                mutation_rate: float = 0.001,
                consciousness_level: float = 0.1):
        """
        Initialize a cell state.
        
        Args:
            cell_type: Type of cell ("normal", "precancerous", "cancerous", "metastatic")
            division_rate: Base rate of cell division per time unit
            mutation_rate: Base rate of mutation per division
            consciousness_level: Cell consciousness level (0-1)
        """
        self.cell_type = cell_type
        self.division_rate = division_rate
        self.mutation_rate = mutation_rate
        self.consciousness_level = consciousness_level
        self.age = 0
        self.mutations = []
        self.resonance = 0.0
        self.phi_alignment = 0.0
        
        # Initialize phi-harmonic properties
        self._initialize_phi_properties()
    
    def _initialize_phi_properties(self):
        """Initialize phi-harmonic properties."""
        # Set phi-scaled properties based on cell type
        if self.cell_type == "normal":
            self.division_rate *= 1.0
            self.mutation_rate *= 1.0
            self.resonance = 0.9
            self.phi_alignment = 0.95
        elif self.cell_type == "precancerous":
            self.division_rate *= PHI_INVERSE
            self.mutation_rate *= PHI
            self.resonance = 0.7
            self.phi_alignment = 0.8
        elif self.cell_type == "cancerous":
            self.division_rate *= PHI
            self.mutation_rate *= PHI_SQUARED
            self.resonance = 0.4
            self.phi_alignment = 0.5
        elif self.cell_type == "metastatic":
            self.division_rate *= PHI_SQUARED
            self.mutation_rate *= PHI_CUBED
            self.resonance = 0.2
            self.phi_alignment = 0.3
    
    def mutate(self) -> bool:
        """
        Attempt mutation based on mutation rate.
        
        Returns:
            True if mutation occurred, False otherwise
        """
        # Use phi-harmonic random if available
        if PHI_RANDOM_AVAILABLE:
            mutation_chance = phi_random.random()
        else:
            # Simulate phi-harmonic randomness
            mutation_chance = random.random() * (1 + (PHI_INVERSE - 0.5) * math.sin(self.age * PHI_INVERSE))
        
        # Check if mutation occurs
        if mutation_chance < self.mutation_rate:
            # Generate mutation type using phi-harmonic principles
            mutation_types = ["p53", "BRCA", "KRAS", "EGFR", "HER2", "ALK", "ROS1", "BRAF", "MET"]
            
            if PHI_RANDOM_AVAILABLE:
                mutation_index = int(phi_random.random() * len(mutation_types))
            else:
                mutation_index = int(random.random() * len(mutation_types))
            
            mutation = mutation_types[mutation_index]
            
            # Add mutation if not already present
            if mutation not in self.mutations:
                self.mutations.append(mutation)
                
                # Update cell type based on mutations
                self._update_cell_type()
                
                return True
        
        return False
    
    def _update_cell_type(self):
        """Update cell type based on mutations."""
        num_mutations = len(self.mutations)
        
        if num_mutations == 0:
            self.cell_type = "normal"
        elif num_mutations <= 2:
            self.cell_type = "precancerous"
        elif num_mutations <= 5:
            self.cell_type = "cancerous"
        else:
            self.cell_type = "metastatic"
        
        # Reinitialize phi properties
        self._initialize_phi_properties()
    
    def divide(self) -> Optional['PhiHarmonicCellState']:
        """
        Attempt cell division based on division rate.
        
        Returns:
            New cell if division occurred, None otherwise
        """
        # Use phi-harmonic random if available
        if PHI_RANDOM_AVAILABLE:
            division_chance = phi_random.random()
        else:
            # Simulate phi-harmonic randomness
            division_chance = random.random() * (1 + (PHI_INVERSE - 0.5) * math.sin(self.age * PHI))
        
        # Check if division occurs
        if division_chance < self.division_rate:
            # Create new cell with same properties
            new_cell = PhiHarmonicCellState(
                cell_type=self.cell_type,
                division_rate=self.division_rate,
                mutation_rate=self.mutation_rate,
                consciousness_level=self.consciousness_level
            )
            
            # Copy mutations
            new_cell.mutations = self.mutations.copy()
            
            # Age is reset for new cell
            new_cell.age = 0
            
            # Increment age for parent cell
            self.age += 1
            
            return new_cell
        
        # Increment age even without division
        self.age += 1
        
        return None
    
    def apply_treatment(self, treatment_strength: float, treatment_specificity: float) -> bool:
        """
        Apply treatment to cell.
        
        Args:
            treatment_strength: Strength of treatment (0-1)
            treatment_specificity: Specificity of treatment (0-1)
            
        Returns:
            True if cell dies, False otherwise
        """
        # Calculate treatment effectiveness based on cell type and phi-harmonic principles
        if self.cell_type == "normal":
            # Normal cells are less affected by treatment
            effectiveness = treatment_strength * (1 - treatment_specificity)
        elif self.cell_type == "precancerous":
            # Precancerous cells are moderately affected
            effectiveness = treatment_strength * treatment_specificity * PHI_INVERSE
        elif self.cell_type == "cancerous":
            # Cancerous cells are strongly affected
            effectiveness = treatment_strength * treatment_specificity
        elif self.cell_type == "metastatic":
            # Metastatic cells are less affected due to resistance
            effectiveness = treatment_strength * treatment_specificity * PHI_INVERSE * PHI_INVERSE
        
        # Use phi-harmonic random if available
        if PHI_RANDOM_AVAILABLE:
            death_chance = phi_random.random()
        else:
            # Simulate phi-harmonic randomness
            death_chance = random.random() * (1 + (PHI_INVERSE - 0.5) * math.sin(self.age * PHI))
        
        # Check if cell dies
        return death_chance < effectiveness

class PhiHarmonicCancerModel:
    """
    Phi-Harmonic Cancer Model for simulating cancer growth and treatment.
    """
    
    def __init__(self, 
                initial_normal_cells: int = 1000,
                initial_precancerous_cells: int = 10,
                initial_cancerous_cells: int = 0,
                time_units: int = 100):
        """
        Initialize the cancer model.
        
        Args:
            initial_normal_cells: Initial number of normal cells
            initial_precancerous_cells: Initial number of precancerous cells
            initial_cancerous_cells: Initial number of cancerous cells
            time_units: Number of time units to simulate
        """
        self.phi = PHI
        self.time_units = time_units
        self.current_time = 0
        
        # Initialize cell populations
        self.cells = []
        
        # Add normal cells
        for _ in range(initial_normal_cells):
            self.cells.append(PhiHarmonicCellState(cell_type="normal"))
        
        # Add precancerous cells
        for _ in range(initial_precancerous_cells):
            self.cells.append(PhiHarmonicCellState(cell_type="precancerous"))
        
        # Add cancerous cells
        for _ in range(initial_cancerous_cells):
            self.cells.append(PhiHarmonicCellState(cell_type="cancerous"))
        
        # Initialize history
        self.history = {
            "normal": [initial_normal_cells],
            "precancerous": [initial_precancerous_cells],
            "cancerous": [initial_cancerous_cells],
            "metastatic": [0],
            "total": [initial_normal_cells + initial_precancerous_cells + initial_cancerous_cells]
        }
        
        # Initialize treatment history
        self.treatment_history = []
        
        print(f"Phi-Harmonic Cancer Model initialized with φ = {self.phi}")
        print(f"Initial cells: {len(self.cells)}")
        print(f"  Normal: {initial_normal_cells}")
        print(f"  Precancerous: {initial_precancerous_cells}")
        print(f"  Cancerous: {initial_cancerous_cells}")
    
    def simulate_time_step(self, 
                          treatment_strength: float = 0.0,
                          treatment_specificity: float = 0.9):
        """
        Simulate one time step of the model.
        
        Args:
            treatment_strength: Strength of treatment (0-1)
            treatment_specificity: Specificity of treatment (0-1)
        """
        # Record treatment if applied
        if treatment_strength > 0:
            self.treatment_history.append({
                "time": self.current_time,
                "strength": treatment_strength,
                "specificity": treatment_specificity
            })
        
        # Process cell division, mutation, and treatment
        new_cells = []
        surviving_cells = []
        
        for cell in self.cells:
            # Check for mutation
            cell.mutate()
            
            # Check for division
            new_cell = cell.divide()
            if new_cell:
                new_cells.append(new_cell)
            
            # Apply treatment if active
            if treatment_strength > 0:
                if not cell.apply_treatment(treatment_strength, treatment_specificity):
                    surviving_cells.append(cell)
            else:
                surviving_cells.append(cell)
        
        # Update cell population
        self.cells = surviving_cells + new_cells
        
        # Update history
        cell_counts = self._count_cells_by_type()
        self.history["normal"].append(cell_counts["normal"])
        self.history["precancerous"].append(cell_counts["precancerous"])
        self.history["cancerous"].append(cell_counts["cancerous"])
        self.history["metastatic"].append(cell_counts["metastatic"])
        self.history["total"].append(len(self.cells))
        
        # Increment time
        self.current_time += 1
    
    def _count_cells_by_type(self) -> Dict[str, int]:
        """
        Count cells by type.
        
        Returns:
            Dictionary of cell counts by type
        """
        counts = {
            "normal": 0,
            "precancerous": 0,
            "cancerous": 0,
            "metastatic": 0
        }
        
        for cell in self.cells:
            counts[cell.cell_type] += 1
        
        return counts
    
    def run_simulation(self, 
                      treatment_schedule: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Run the complete simulation.
        
        Args:
            treatment_schedule: List of treatment events
                Each event is a dictionary with keys:
                - time: Time unit to apply treatment
                - strength: Treatment strength (0-1)
                - specificity: Treatment specificity (0-1)
                
        Returns:
            Simulation results
        """
        print(f"\nRunning Phi-Harmonic Cancer Simulation for {self.time_units} time units")
        
        if treatment_schedule:
            print(f"Treatment schedule: {len(treatment_schedule)} events")
        else:
            treatment_schedule = []
            print("No treatment scheduled")
        
        # Sort treatment schedule by time
        treatment_schedule.sort(key=lambda x: x["time"])
        
        # Run simulation for each time step
        for t in range(self.time_units):
            # Check for treatment at this time step
            treatment_strength = 0.0
            treatment_specificity = 0.9
            
            for treatment in treatment_schedule:
                if treatment["time"] == t:
                    treatment_strength = treatment["strength"]
                    treatment_specificity = treatment["specificity"]
                    print(f"Time {t}: Applying treatment (strength={treatment_strength:.2f}, specificity={treatment_specificity:.2f})")
                    break
            
            # Simulate time step
            self.simulate_time_step(treatment_strength, treatment_specificity)
            
            # Print progress every 10 time units
            if t % 10 == 0 or t == self.time_units - 1:
                cell_counts = self._count_cells_by_type()
                print(f"Time {t}: Total cells={len(self.cells)}, "
                      f"Normal={cell_counts['normal']}, "
                      f"Precancerous={cell_counts['precancerous']}, "
                      f"Cancerous={cell_counts['cancerous']}, "
                      f"Metastatic={cell_counts['metastatic']}")
        
        # Prepare results
        results = {
            "history": self.history,
            "treatment_history": self.treatment_history,
            "final_cell_counts": self._count_cells_by_type(),
            "total_cells": len(self.cells),
            "phi": self.phi,
            "time_units": self.time_units
        }
        
        return results
    
    def plot_results(self, results: Dict[str, Any], save_path: Optional[str] = None):
        """
        Plot simulation results.
        
        Args:
            results: Simulation results
            save_path: Path to save the plot (if None, plot is displayed)
        """
        history = results["history"]
        treatment_history = results["treatment_history"]
        
        # Create figure with phi-harmonic dimensions
        plt.figure(figsize=(10, 10 / PHI))
        
        # Plot cell counts
        time_axis = list(range(len(history["normal"])))
        plt.plot(time_axis, history["normal"], label="Normal", color="green")
        plt.plot(time_axis, history["precancerous"], label="Precancerous", color="orange")
        plt.plot(time_axis, history["cancerous"], label="Cancerous", color="red")
        plt.plot(time_axis, history["metastatic"], label="Metastatic", color="purple")
        
        # Plot treatments
        for treatment in treatment_history:
            plt.axvline(x=treatment["time"], color="blue", linestyle="--", alpha=0.5)
        
        # Add labels and title
        plt.xlabel("Time Units")
        plt.ylabel("Cell Count")
        plt.title("Phi-Harmonic Cancer Model Simulation")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Add phi-harmonic annotation
        plt.figtext(0.02, 0.02, f"φ = {PHI:.6f}", fontsize=8)
        
        # Save or display
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            print(f"Plot saved to {save_path}")
        else:
            plt.show()

class PhiHarmonicTreatmentOptimizer:
    """
    Optimizes cancer treatment schedules using phi-harmonic principles.
    """
    
    def __init__(self, 
                model_params: Dict[str, Any],
                max_treatments: int = 5,
                treatment_interval_min: int = 5):
        """
        Initialize the treatment optimizer.
        
        Args:
            model_params: Parameters for the cancer model
            max_treatments: Maximum number of treatments to apply
            treatment_interval_min: Minimum interval between treatments
        """
        self.phi = PHI
        self.model_params = model_params
        self.max_treatments = max_treatments
        self.treatment_interval_min = treatment_interval_min
        
        print(f"Phi-Harmonic Treatment Optimizer initialized with φ = {self.phi}")
        print(f"Max treatments: {self.max_treatments}")
        print(f"Minimum treatment interval: {self.treatment_interval_min}")
    
    def generate_phi_harmonic_schedule(self, 
                                      time_units: int,
                                      base_strength: float = 0.7,
                                      base_specificity: float = 0.9) -> List[Dict[str, Any]]:
        """
        Generate a treatment schedule based on phi-harmonic intervals.
        
        Args:
            time_units: Total time units for simulation
            base_strength: Base treatment strength
            base_specificity: Base treatment specificity
            
        Returns:
            Treatment schedule
        """
        schedule = []
        
        # Calculate phi-harmonic treatment times
        treatment_times = []
        
        # Method 1: Fibonacci-based scheduling
        fib = [1, 1]
        while fib[-1] < time_units:
            fib.append(fib[-1] + fib[-2])
        
        treatment_times = [t for t in fib if t < time_units]
        
        # Limit to max treatments
        if len(treatment_times) > self.max_treatments:
            # Use phi-scaled selection
            phi_indices = [int(i * PHI) % len(treatment_times) for i in range(self.max_treatments)]
            treatment_times = [treatment_times[i] for i in sorted(set(phi_indices))]
        
        # Create schedule
        for i, time in enumerate(treatment_times):
            # Vary strength and specificity using phi-harmonic principles
            strength_variation = 0.1 * math.sin(i * PHI)
            specificity_variation = 0.05 * math.sin(i * PHI_SQUARED)
            
            schedule.append({
                "time": time,
                "strength": min(1.0, max(0.1, base_strength + strength_variation)),
                "specificity": min(1.0, max(0.5, base_specificity + specificity_variation))
            })
        
        return schedule
    
    def optimize_treatment(self, 
                          optimization_rounds: int = 5) -> Dict[str, Any]:
        """
        Optimize treatment schedule.
        
        Args:
            optimization_rounds: Number of optimization rounds
            
        Returns:
            Optimized treatment results
        """
        print(f"\nRunning treatment optimization with {optimization_rounds} rounds")
        
        best_schedule = None
        best_results = None
        best_score = float('inf')
        
        for round_num in range(optimization_rounds):
            print(f"\nOptimization Round {round_num + 1}/{optimization_rounds}")
            
            # Create model with current parameters
            model = PhiHarmonicCancerModel(**self.model_params)
            
            # Generate phi-harmonic schedule
            schedule = self.generate_phi_harmonic_schedule(
                time_units=model.time_units,
                base_strength=0.7 + 0.1 * math.sin(round_num * PHI),
                base_specificity=0.9 + 0.05 * math.sin(round_num * PHI_SQUARED)
            )
            
            print(f"Generated schedule with {len(schedule)} treatments")
            
            # Run simulation
            results = model.run_simulation(schedule)
            
            # Calculate score (lower is better)
            final_counts = results["final_cell_counts"]
            score = (
                final_counts["cancerous"] * 10 + 
                final_counts["metastatic"] * 20 + 
                final_counts["precancerous"] * 2 - 
                final_counts["normal"] * 0.1
            )
            
            print(f"Round {round_num + 1} score: {score:.2f}")
            
            # Update best if improved
            if score < best_score:
                best_score = score
                best_schedule = schedule
                best_results = results
                print(f"New best score: {best_score:.2f}")
        
        # Run final simulation with best schedule
        if best_schedule:
            print("\nRunning final simulation with best treatment schedule")
            final_model = PhiHarmonicCancerModel(**self.model_params)
            final_results = final_model.run_simulation(best_schedule)
            
            # Add optimization info
            final_results["optimization_score"] = best_score
            final_results["optimization_rounds"] = optimization_rounds
            
            return final_results
        
        return None

# For direct execution
if __name__ == "__main__":
    # Create output directory if it doesn't exist
    output_dir = os.path.join(current_dir, "cancer_simulations")
    os.makedirs(output_dir, exist_ok=True)
    
    # Set model parameters
    model_params = {
        "initial_normal_cells": 10000,
        "initial_precancerous_cells": 100,
        "initial_cancerous_cells": 10,
        "time_units": 100
    }
    
    # Run simulation without treatment
    print("\n=== Simulation Without Treatment ===")
    model_no_treatment = PhiHarmonicCancerModel(**model_params)
    results_no_treatment = model_no_treatment.run_simulation()
    
    # Save and plot results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save no treatment results
    no_treatment_plot_path = os.path.join(output_dir, f"cancer_no_treatment_{timestamp}.png")
    model_no_treatment.plot_results(results_no_treatment, no_treatment_plot_path)
    
    no_treatment_data_path = os.path.join(output_dir, f"cancer_no_treatment_{timestamp}.json")
    with open(no_treatment_data_path, 'w') as f:
        json.dump(results_no_treatment, f, indent=2)
    
    # Run optimized treatment
    print("\n=== Optimizing Treatment ===")
    optimizer = PhiHarmonicTreatmentOptimizer(model_params, max_treatments=5)
    optimized_results = optimizer.optimize_treatment(optimization_rounds=3)
    
    # Save and plot optimized results
    optimized_plot_path = os.path.join(output_dir, f"cancer_optimized_{timestamp}.png")
    model_no_treatment.plot_results(optimized_results, optimized_plot_path)
    
    optimized_data_path = os.path.join(output_dir, f"cancer_optimized_{timestamp}.json")
    with open(optimized_data_path, 'w') as f:
        json.dump(optimized_results, f, indent=2)
    
    print("\n=== Simulation Complete ===")
    print(f"Results saved to {output_dir}")
    
    # Compare final results
    no_treatment_final = results_no_treatment["final_cell_counts"]
    optimized_final = optimized_results["final_cell_counts"]
    
    print("\nFinal Cell Counts Comparison:")
    print("                  No Treatment    Optimized Treatment")
    print(f"Normal:          {no_treatment_final['normal']:8d}        {optimized_final['normal']:8d}")
    print(f"Precancerous:    {no_treatment_final['precancerous']:8d}        {optimized_final['precancerous']:8d}")
    print(f"Cancerous:       {no_treatment_final['cancerous']:8d}        {optimized_final['cancerous']:8d}")
    print(f"Metastatic:      {no_treatment_final['metastatic']:8d}        {optimized_final['metastatic']:8d}")
    print(f"Total:           {results_no_treatment['total_cells']:8d}        {optimized_results['total_cells']:8d}")
