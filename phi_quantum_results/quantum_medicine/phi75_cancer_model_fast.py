#!/usr/bin/env python3
"""
Phi75 Cancer Model (Fast Version)

An optimized quantum-inspired cancer growth modeling system using Vaughn Scott's 
phi75 quantum random principles with performance improvements to prevent freezing.
"""

import os
import sys
import math
import numpy as np
import json
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Any, Optional
import time

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI
PHI_SQUARED = PHI ** 2
PHI_CUBED = PHI ** 3
PHI_75 = PHI ** 7.5
PHI_SEAL = PHI ** 75

# Cell type constants
NORMAL = 0
PRECANCEROUS = 1
CANCEROUS = 2
METASTATIC = 3
CELL_TYPES = ["normal", "precancerous", "cancerous", "metastatic"]

# Population limits to prevent freezing
MAX_TOTAL_CELLS = 100000
MAX_CELLS_PER_TYPE = 50000

class Phi75CancerModelFast:
    """
    Optimized Phi75 Cancer Model for simulating cancer growth and treatment.
    Uses aggregated cell populations instead of individual cells for performance.
    """
    
    def __init__(self, 
                initial_normal_cells: int = 10000,
                initial_precancerous_cells: int = 100,
                initial_cancerous_cells: int = 10,
                time_units: int = 100):
        """Initialize the optimized cancer model."""
        self.phi = PHI
        self.time_units = time_units
        self.current_time = 0
        self.phi_seal = PHI_SEAL
        
        # Initialize cell populations as counts (not individual objects)
        self.cell_counts = [
            initial_normal_cells,      # Normal
            initial_precancerous_cells, # Precancerous
            initial_cancerous_cells,    # Cancerous
            0                          # Metastatic
        ]
        
        # Cell properties by type
        self.division_rates = [
            0.05,                # Normal
            0.05 * PHI_INV,      # Precancerous
            0.05 * PHI,          # Cancerous
            0.05 * PHI_SQUARED   # Metastatic
        ]
        
        self.mutation_rates = [
            0.001,               # Normal
            0.001 * PHI,         # Precancerous
            0.001 * PHI_SQUARED, # Cancerous
            0.001 * PHI_CUBED    # Metastatic
        ]
        
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
        
        # Initialize quantum metrics
        self.quantum_metrics = {
            "phi_resonance": PHI,
            "consciousness_alignment": 0.7567 * PHI_INV,
            "quantum_tunneling_rate": 0.7567 * PHI_INV,
            "reality_integrity": 0.9,
            "phi_dimensional_scaling": PHI_75
        }
        
        print(f"Phi75 Cancer Model (Fast) initialized with φ = {self.phi}")
        print(f"Validation seal: φ^75 = {self.phi_seal:.2f}")
        print(f"Initial cells: {sum(self.cell_counts)}")
        print(f"  Normal: {self.cell_counts[NORMAL]}")
        print(f"  Precancerous: {self.cell_counts[PRECANCEROUS]}")
        print(f"  Cancerous: {self.cell_counts[CANCEROUS]}")
        print(f"  Metastatic: {self.cell_counts[METASTATIC]}")
    
    def _phi_random(self) -> float:
        """Generate a phi-harmonic random number."""
        # Simple phi-harmonic random implementation
        t = time.time() * PHI
        return ((t * PHI) % 1 + PHI_INV) % 1
    
    def simulate_time_step(self, 
                          treatment_strength: float = 0.0,
                          treatment_specificity: float = 0.9):
        """
        Simulate one time step of the model using aggregated calculations.
        
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
        
        # Calculate new cells from division (using statistical approach)
        new_cells = [0, 0, 0, 0]
        for cell_type in range(4):
            # Calculate expected number of new cells
            division_rate = self.division_rates[cell_type]
            expected_new = self.cell_counts[cell_type] * division_rate
            
            # Add randomness with phi-harmonic variation
            random_factor = 0.8 + 0.4 * self._phi_random()
            new_cells[cell_type] = int(expected_new * random_factor)
        
        # Calculate mutations (using statistical approach)
        mutations = [0, 0, 0, 0]  # Cells moving to next type
        for cell_type in range(3):  # Metastatic cells don't mutate further
            # Calculate expected number of mutations
            mutation_rate = self.mutation_rates[cell_type]
            expected_mutations = self.cell_counts[cell_type] * mutation_rate
            
            # Add randomness with phi-harmonic variation
            random_factor = 0.8 + 0.4 * self._phi_random()
            mutations[cell_type] = int(expected_mutations * random_factor)
        
        # Apply treatment effects (using statistical approach)
        if treatment_strength > 0:
            deaths = [0, 0, 0, 0]
            for cell_type in range(4):
                # Calculate treatment effectiveness
                if cell_type == NORMAL:
                    effectiveness = treatment_strength * (1 - treatment_specificity)
                elif cell_type == PRECANCEROUS:
                    effectiveness = treatment_strength * treatment_specificity * PHI_INV
                elif cell_type == CANCEROUS:
                    effectiveness = treatment_strength * treatment_specificity
                else:  # METASTATIC
                    effectiveness = treatment_strength * treatment_specificity * PHI_INV * PHI_INV
                
                # Calculate expected deaths
                expected_deaths = self.cell_counts[cell_type] * effectiveness
                
                # Add randomness with phi-harmonic variation
                random_factor = 0.8 + 0.4 * self._phi_random()
                deaths[cell_type] = int(expected_deaths * random_factor)
        else:
            deaths = [0, 0, 0, 0]
        
        # Update cell populations
        new_counts = [0, 0, 0, 0]
        
        # Normal cells: gain from division, lose from mutation and treatment
        new_counts[NORMAL] = (
            self.cell_counts[NORMAL] + 
            new_cells[NORMAL] - 
            mutations[NORMAL] - 
            deaths[NORMAL]
        )
        
        # Precancerous cells: gain from normal mutation and division, lose from mutation and treatment
        new_counts[PRECANCEROUS] = (
            self.cell_counts[PRECANCEROUS] + 
            mutations[NORMAL] + 
            new_cells[PRECANCEROUS] - 
            mutations[PRECANCEROUS] - 
            deaths[PRECANCEROUS]
        )
        
        # Cancerous cells: gain from precancerous mutation and division, lose from mutation and treatment
        new_counts[CANCEROUS] = (
            self.cell_counts[CANCEROUS] + 
            mutations[PRECANCEROUS] + 
            new_cells[CANCEROUS] - 
            mutations[CANCEROUS] - 
            deaths[CANCEROUS]
        )
        
        # Metastatic cells: gain from cancerous mutation and division, lose from treatment
        new_counts[METASTATIC] = (
            self.cell_counts[METASTATIC] + 
            mutations[CANCEROUS] + 
            new_cells[METASTATIC] - 
            deaths[METASTATIC]
        )
        
        # Ensure no negative counts
        for i in range(4):
            new_counts[i] = max(0, new_counts[i])
        
        # Apply population limits to prevent freezing
        total_cells = sum(new_counts)
        if total_cells > MAX_TOTAL_CELLS:
            # Scale down all populations proportionally
            scale_factor = MAX_TOTAL_CELLS / total_cells
            for i in range(4):
                new_counts[i] = int(new_counts[i] * scale_factor)
        
        # Apply per-type limits
        for i in range(4):
            if new_counts[i] > MAX_CELLS_PER_TYPE:
                new_counts[i] = MAX_CELLS_PER_TYPE
        
        # Update cell counts
        self.cell_counts = new_counts
        
        # Update history
        self.history["normal"].append(self.cell_counts[NORMAL])
        self.history["precancerous"].append(self.cell_counts[PRECANCEROUS])
        self.history["cancerous"].append(self.cell_counts[CANCEROUS])
        self.history["metastatic"].append(self.cell_counts[METASTATIC])
        self.history["total"].append(sum(self.cell_counts))
        
        # Increment time
        self.current_time += 1
        
        # Update quantum metrics occasionally
        if self.current_time % 10 == 0:
            # Simple update based on phi-harmonic principles
            self.quantum_metrics["phi_resonance"] = PHI * (0.9 + 0.2 * self._phi_random())
            self.quantum_metrics["consciousness_alignment"] = 0.7567 * PHI_INV * (0.9 + 0.2 * self._phi_random())
            self.quantum_metrics["quantum_tunneling_rate"] = 0.7567 * PHI_INV * (0.9 + 0.2 * self._phi_random())
            self.quantum_metrics["reality_integrity"] = 0.9 * (0.9 + 0.2 * self._phi_random())
            self.quantum_metrics["phi_dimensional_scaling"] = PHI_75 * (0.9 + 0.2 * self._phi_random())
    
    def run_simulation(self, 
                      treatment_schedule: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Run the complete simulation.
        
        Args:
            treatment_schedule: List of treatment events
                
        Returns:
            Simulation results
        """
        start_time = time.time()
        print(f"\nRunning Phi75 Cancer Simulation (Fast) for {self.time_units} time units")
        print(f"Validation seal: φ^75 = {self.phi_seal:.2f}")
        
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
                print(f"Time {t}: Total cells={sum(self.cell_counts)}, "
                      f"Normal={self.cell_counts[NORMAL]}, "
                      f"Precancerous={self.cell_counts[PRECANCEROUS]}, "
                      f"Cancerous={self.cell_counts[CANCEROUS]}, "
                      f"Metastatic={self.cell_counts[METASTATIC]}")
        
        elapsed_time = time.time() - start_time
        print(f"Simulation completed in {elapsed_time:.2f} seconds")
        
        # Prepare results
        results = {
            "history": self.history,
            "treatment_history": self.treatment_history,
            "final_cell_counts": {
                "normal": self.cell_counts[NORMAL],
                "precancerous": self.cell_counts[PRECANCEROUS],
                "cancerous": self.cell_counts[CANCEROUS],
                "metastatic": self.cell_counts[METASTATIC]
            },
            "total_cells": sum(self.cell_counts),
            "phi": self.phi,
            "phi_seal": self.phi_seal,
            "time_units": self.time_units,
            "quantum_metrics": self.quantum_metrics,
            "elapsed_time": elapsed_time
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
        plt.title("Phi75 Cancer Model Simulation (Fast)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Add phi-harmonic annotation
        plt.figtext(0.02, 0.02, f"φ = {PHI:.6f} | φ^75 = {PHI_SEAL:.2f}", fontsize=8)
        
        # Add quantum metrics annotation
        quantum_metrics = results.get("quantum_metrics", {})
        if quantum_metrics:
            metrics_text = "Quantum Metrics:\n"
            for key, value in quantum_metrics.items():
                metrics_text += f"{key}: {value:.4f}\n"
            plt.figtext(0.02, 0.1, metrics_text, fontsize=6)
        
        # Save or display
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            print(f"Plot saved to {save_path}")
        else:
            plt.show()

def generate_phi_harmonic_schedule(time_units: int, 
                                 max_treatments: int = 5) -> List[Dict[str, Any]]:
    """
    Generate a treatment schedule based on phi-harmonic intervals.
    
    Args:
        time_units: Total time units for simulation
        max_treatments: Maximum number of treatments
        
    Returns:
        Treatment schedule
    """
    # Calculate phi-harmonic treatment times using Fibonacci sequence
    fib = [1, 1]
    while fib[-1] < time_units:
        fib.append(fib[-1] + fib[-2])
    
    treatment_times = [t for t in fib if t < time_units]
    
    # Limit to max treatments
    if len(treatment_times) > max_treatments:
        # Use phi-scaled selection
        phi_indices = [int(i * PHI) % len(treatment_times) for i in range(max_treatments)]
        treatment_times = [treatment_times[i] for i in sorted(set(phi_indices))]
    
    # Create schedule with phi-harmonic variations
    schedule = []
    for i, time in enumerate(treatment_times):
        # Vary strength and specificity using phi-harmonic principles
        strength_variation = 0.1 * math.sin(i * PHI)
        specificity_variation = 0.05 * math.sin(i * PHI_SQUARED)
        
        schedule.append({
            "time": time,
            "strength": min(1.0, max(0.1, 0.7 + strength_variation)),
            "specificity": min(1.0, max(0.5, 0.9 + specificity_variation))
        })
    
    return schedule

# For direct execution
if __name__ == "__main__":
    # Create output directory if it doesn't exist
    output_dir = os.path.join(current_dir, "cancer_simulations")
    os.makedirs(output_dir, exist_ok=True)
    
    # Set model parameters
    initial_normal_cells = 10000
    initial_precancerous_cells = 100
    initial_cancerous_cells = 10
    time_units = 100
    
    # Run simulation without treatment
    print("\n=== Simulation Without Treatment ===")
    model_no_treatment = Phi75CancerModelFast(
        initial_normal_cells=initial_normal_cells,
        initial_precancerous_cells=initial_precancerous_cells,
        initial_cancerous_cells=initial_cancerous_cells,
        time_units=time_units
    )
    results_no_treatment = model_no_treatment.run_simulation()
    
    # Save and plot results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save no treatment results
    no_treatment_plot_path = os.path.join(output_dir, f"phi75_cancer_no_treatment_fast_{timestamp}.png")
    model_no_treatment.plot_results(results_no_treatment, no_treatment_plot_path)
    
    no_treatment_data_path = os.path.join(output_dir, f"phi75_cancer_no_treatment_fast_{timestamp}.json")
    with open(no_treatment_data_path, 'w') as f:
        json.dump(results_no_treatment, f, indent=2)
    
    # Generate treatment schedule
    treatment_schedule = generate_phi_harmonic_schedule(time_units, max_treatments=5)
    
    # Run simulation with treatment
    print("\n=== Simulation With Treatment ===")
    model_with_treatment = Phi75CancerModelFast(
        initial_normal_cells=initial_normal_cells,
        initial_precancerous_cells=initial_precancerous_cells,
        initial_cancerous_cells=initial_cancerous_cells,
        time_units=time_units
    )
    results_with_treatment = model_with_treatment.run_simulation(treatment_schedule)
    
    # Save and plot treatment results
    treatment_plot_path = os.path.join(output_dir, f"phi75_cancer_treatment_fast_{timestamp}.png")
    model_with_treatment.plot_results(results_with_treatment, treatment_plot_path)
    
    treatment_data_path = os.path.join(output_dir, f"phi75_cancer_treatment_fast_{timestamp}.json")
    with open(treatment_data_path, 'w') as f:
        json.dump(results_with_treatment, f, indent=2)
    
    print("\n=== Simulation Complete ===")
    print(f"Results saved to {output_dir}")
    
    # Compare final results
    no_treatment_final = results_no_treatment["final_cell_counts"]
    treatment_final = results_with_treatment["final_cell_counts"]
    
    print("\nFinal Cell Counts Comparison:")
    print("                  No Treatment    With Treatment")
    print(f"Normal:          {no_treatment_final['normal']:8d}        {treatment_final['normal']:8d}")
    print(f"Precancerous:    {no_treatment_final['precancerous']:8d}        {treatment_final['precancerous']:8d}")
    print(f"Cancerous:       {no_treatment_final['cancerous']:8d}        {treatment_final['cancerous']:8d}")
    print(f"Metastatic:      {no_treatment_final['metastatic']:8d}        {treatment_final['metastatic']:8d}")
    print(f"Total:           {results_no_treatment['total_cells']:8d}        {results_with_treatment['total_cells']:8d}")
    
    # Print performance metrics
    print(f"\nNo Treatment simulation time: {results_no_treatment['elapsed_time']:.2f} seconds")
    print(f"With Treatment simulation time: {results_with_treatment['elapsed_time']:.2f} seconds")
