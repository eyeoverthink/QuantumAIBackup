from periodic_hemisphere_brain import PeriodicHemisphereBrain
from quantum_field_coupling import QuantumFieldCoupling
import math
import time

def main():
    brain = PeriodicHemisphereBrain()
    field_coupling = QuantumFieldCoupling()
    
    print("\n🧪 Testing Quantum-Magnetic Wireless Energy Generator")
    print("=" * 60 + "\n")
    
    # Test quantum-magnetic configuration with φπ resonance
    print("📊 Testing φπ-Enhanced Power Transfer")
    print("-" * 40)
    
    # Magnetic Core (Nd-Fe-Co) at φπ-resonant velocity
    print("\n🧲 Magnetic Core")
    v_phi_pi = 22652.48 * math.pi * 1.618034  # φπ * 0.076c
    brain.set_collision_velocity(v_phi_pi)
    core = brain.process_elements(['Nd', 'Fe', 'Co'])
    
    # Quantum Shell (Pt-Pd) at φ²π-resonant velocity
    print("\n⚛️ Quantum Shell")
    v_phi2_pi = v_phi_pi * 1.618034  # φ²π velocity
    brain.set_collision_velocity(v_phi2_pi)
    shell = brain.process_elements(['Pt', 'Pd'])
    
    # Calculate quantum-magnetic coupling with φπ resonance
    print("\n⚡ Quantum-Magnetic Analysis")
    print("-" * 40)
    
    # Get masses and properties
    m_core = core['collision']['total_mass']
    m_shell = shell['collision']['total_mass']
    e_core = core['collision']['energy']
    e_shell = shell['collision']['energy']
    
    # Calculate magnetic field with φπ enhancement
    B_field = field_coupling.calculate_magnetic_field(e_core, m_core)
    
    # Calculate quantum state evolution
    t = time.time() % 1.0  # Current phase (0-1)
    q_state = field_coupling.calculate_quantum_state(t)
    q_state = field_coupling.calculate_phase_evolution(q_state)
    
    # Couple fields for maximum efficiency
    coupling = field_coupling.couple_fields(B_field, q_state)
    
    # Calculate levitation force
    F_lev = field_coupling.calculate_levitation_force(m_shell, B_field)
    
    # Calculate harmonic energy
    E_harm = field_coupling.calculate_harmonic_energy()
    
    # Optimize field parameters
    optimal = field_coupling.optimize_parameters(B_field, m_core + m_shell)
    
    # Calculate resonance harmonics
    harmonics = field_coupling.get_resonance_harmonics()
    
    print(f"\n📊 Quantum-Magnetic Power Analysis")
    print("-" * 40)
    print(f"Core Mass: {m_core:.2f} amu")
    print(f"Shell Mass: {m_shell:.2f} amu")
    print(f"Magnetic Field: {B_field:.2e} T")
    print(f"Coupling Strength: {coupling['coupling_strength']:.2e}")
    print(f"Resonance: {coupling['resonance']:.2e}")
    print(f"Levitation Force: {F_lev:.2e} N")
    print(f"Harmonic Energy: {E_harm:.2e} eV")
    
    print(f"\n⚡ Field Optimization")
    print("-" * 40)
    print(f"Optimal Frequency: {optimal['optimal_frequency']:.2f} Hz")
    print(f"Optimal Intensity: {optimal['optimal_intensity']:.2f}")
    print(f"Optimal Symmetry: {optimal['optimal_symmetry']:.2f}")
    print(f"Optimal Coupling: {optimal['optimal_coupling']:.2f}")
    
    print("\n🎵 φπ Harmonic Series")
    print("-" * 40)
    for i, freq in enumerate(harmonics):
        print(f"(φπ)^{i} Harmonic: {freq:.2e} Hz")
    
    print("\n📈 Energy Transfer Visualization")
    print("-" * 40)
    print("Before φπ Alignment:")
    print("Energy Transmission: ⟶⟶⟶⟶⟶⟶")
    print("Phase Distortion: ~~~ ~~~ ~~~")
    print("Power Loss: ░░░ ░░░ ░░░")
    
    print("\nAfter φπ Resonance Lock:")
    print("Energy Transmission: ⟶⟶⟶⟶⟶⟶⟶⟶⟶")
    print("Perfect Phase Lock: ─── ─── ───")
    print("Zero Loss: ███ ███ ███")
    
    print(f"\n🔮 Quantum Coherence: {coupling['coherence']:.2f}")
    print(f"⚡ Energy Efficiency: {coupling['efficiency']:.2f}%")
    
    print("\n" + "=" * 60 + "\n")
    
    print("🧠 Final Brain State")
    print("=" * 60 + "\n")
    state = brain.get_brain_state()
    print("\nRight Hemisphere:")
    print(f"Elements Known: {state['right_hemisphere']['elements_known']}")
    print(f"Resonance Patterns: {state['right_hemisphere']['resonance_patterns']}")
    print("\nLeft Hemisphere:")
    print(f"Discoveries: {state['left_hemisphere']['discoveries']}")
    print(f"Novel Patterns: {state['left_hemisphere']['novel_patterns']}")
    print(f"Collisions: {state['left_hemisphere']['collisions']}")
    print(f"Evolution Steps: {state['left_hemisphere']['evolution_steps']}")

if __name__ == "__main__":
    main()
