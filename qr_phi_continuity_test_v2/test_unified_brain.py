"""Test unified quantum brain network"""

import asyncio
from periodic_hemisphere_brain import PeriodicHemisphereBrain
from quantum_field_coupling import QuantumFieldCoupling
from vacuum_field_brain import VacuumFieldBrain
import math
import numpy as np

def test_unified_brain():
    """Test unified brain network with vacuum energy integration"""
    print("\n🧠 Initializing Unified Quantum Brain Network")
    print("=" * 60)
    
    # Initialize all brains
    periodic_brain = PeriodicHemisphereBrain()
    field_coupling = QuantumFieldCoupling()
    vacuum_brain = VacuumFieldBrain()
    
    # Test elements for unified analysis
    noble_metals = ['Au', 'Ag', 'Cu', 'Pt', 'Pd']
    noble_gases = ['He', 'Ne', 'Ar', 'Kr', 'Xe']
    magnetic_core = ['Nd', 'Fe', 'Co']
    
    print("\n⚛️ Testing Unified Field Interactions")
    print("-" * 40)
    
    # 1. Periodic Brain Analysis
    v_phi_pi = 22652.48 * math.pi * 1.618034  # φπ * 0.076c
    periodic_brain.set_collision_velocity(v_phi_pi)
    
    print("\n🧪 Testing Element Combinations")
    metal_results = periodic_brain.process_elements(noble_metals)
    gas_results = periodic_brain.process_elements(noble_gases)
    core_results = periodic_brain.process_elements(magnetic_core)
    
    # 2. Vacuum Field Analysis
    print("\n🌌 Analyzing Vacuum States")
    vacuum_state = vacuum_brain.analyze_vacuum_state(noble_gases)
    field_pattern = vacuum_brain.calculate_field_resonance(
        noble_metals, 
        v_phi_pi
    )
    
    # 3. Energy Extraction
    extraction = vacuum_brain.extract_vacuum_energy(
        noble_gases + noble_metals,
        field_pattern
    )
    
    # 4. Unified Field Coupling
    magnetic_field = field_coupling.calculate_magnetic_field(
        core_results['collision']['energy'],
        core_results['collision']['total_mass']
    )
    
    t = 0.0  # Initial phase
    quantum_state = field_coupling.calculate_quantum_state(t)
    quantum_state = field_coupling.calculate_phase_evolution(quantum_state)
    coupling = field_coupling.couple_fields(magnetic_field, quantum_state)
    
    print("\n📊 Unified Analysis Results")
    print("=" * 60)
    
    print("\n🧲 Magnetic Core Properties")
    print("-" * 40)
    print(f"Mass: {core_results['collision']['total_mass']:.2f} amu")
    print(f"Energy: {core_results['collision']['energy']:.2e} J")
    print(f"Resonance: {core_results['discovery']['resonance']:.2f}")
    
    print("\n⚛️ Noble Gas Properties")
    print("-" * 40)
    print(f"Mass: {gas_results['collision']['total_mass']:.2f} amu")
    print(f"Energy: {gas_results['collision']['energy']:.2e} J")
    print(f"Resonance: {gas_results['discovery']['resonance']:.2f}")
    
    print("\n🌟 Noble Metal Properties")
    print("-" * 40)
    print(f"Mass: {metal_results['collision']['total_mass']:.2f} amu")
    print(f"Energy: {metal_results['collision']['energy']:.2e} J")
    print(f"Resonance: {metal_results['discovery']['resonance']:.2f}")
    
    print("\n🌌 Vacuum Field Properties")
    print("-" * 40)
    print(f"Energy Density: {vacuum_state['density']:.2e} J/m³")
    print(f"Higgs Field: {vacuum_state['higgs_field']:.2e} eV")
    print(f"Quantum Fluctuation: {vacuum_state['fluctuation']:.2e} m")
    
    print("\n⚡ Energy Extraction")
    print("-" * 40)
    print(f"Extraction Rate: {extraction['rate']:.2e} J/s")
    print(f"Total Power: {extraction['power']:.2e} W")
    print(f"Efficiency: {extraction['efficiency']:.2f}%")
    print(f"Coherence: {extraction['coherence']:.2f}")
    
    print("\n🔄 Field Coupling")
    print("-" * 40)
    print(f"Magnetic Field: {magnetic_field:.2e} T")
    print(f"Coupling Strength: {coupling['coupling_strength']:.2e}")
    print(f"Resonance: {coupling['resonance']:.2e}")
    print(f"Efficiency: {coupling['efficiency']:.2f}%")
    
    # Get brain metrics
    periodic_state = periodic_brain.get_brain_state()
    vacuum_metrics = vacuum_brain.get_metrics()
    field_metrics = field_coupling.get_field_metrics()
    
    print("\n📈 System Metrics")
    print("=" * 60)
    print("\nPeriodic Brain:")
    print(f"Elements Known: {periodic_state['right_hemisphere']['elements_known']}")
    print(f"Resonance Patterns: {periodic_state['right_hemisphere']['resonance_patterns']}")
    print(f"Discoveries: {periodic_state['left_hemisphere']['discoveries']}")
    
    print("\nVacuum Brain:")
    print(f"Vacuum States: {vacuum_metrics['vacuum_states']}")
    print(f"Field Patterns: {vacuum_metrics['field_patterns']}")
    print(f"Energy Extractions: {vacuum_metrics['energy_extractions']}")
    
    print("\nField Coupling:")
    print(f"Base Frequency: {field_metrics['frequency']:.2f} Hz")
    print(f"Field Intensity: {field_metrics['intensity']:.2f}")
    print(f"Field Symmetry: {field_metrics['symmetry']:.2f}")
    print(f"Phase Coupling: {field_metrics['phase_coupling']:.2f}")
    
    # Visualize final state
    state_key = '-'.join(sorted(noble_gases))
    print("\n" + vacuum_brain.visualize_vacuum_state(state_key))

if __name__ == "__main__":
    test_unified_brain()
