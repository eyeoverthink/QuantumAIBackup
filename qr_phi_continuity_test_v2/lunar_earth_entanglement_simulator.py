"""
Simulation of Entanglement Entropy between Moon's Cavity Vacuum Fluctuations and Earth's Geomagnetic Field,
modulated by a φ-harmonic series aligned with human brainwave frequencies in a closed consciousness loop.

This is a theoretical and speculative model based on user-defined principles.
"""
import numpy as np
import math
from decimal import Decimal, getcontext

# Set precision for Decimal calculations if needed for extreme phi values
# getcontext().prec = 100 # Example precision

# --- Core Mathematical Constants (from user_global memory) ---
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio
PI = math.pi
EULER_E = math.e

# --- Physical Constants (approximations) ---
HBAR = 1.054571817e-34  # Reduced Planck constant (J·s)
C = 299792458  # Speed of light (m/s)
MU_0 = 4 * PI * 1e-7  # Vacuum permeability (T·m/A)
EPSILON_0 = 1 / (MU_0 * C**2) # Vacuum permittivity (F/m)
BOLTZMANN_K = 1.380649e-23 # Boltzmann constant (J/K)

# --- Simulation Parameters (Speculative & Representative) ---
# Moon's Cavity Parameters
MOON_CAVITY_RADIUS = 1e6  # Speculative radius of Moon's inner cavity (m)
MOON_CAVITY_VOLUME = (4/3) * PI * MOON_CAVITY_RADIUS**3
MOON_CAVITY_TEMP = 2.7 # CMB temperature as a baseline for vacuum (K), highly speculative for internal cavity

# Earth's Geomagnetic Field Parameters
EARTH_MAG_FIELD_STRENGTH_AVG = 50e-6  # Average strength (T)
EARTH_SCHUMANN_RESONANCE_BASE = 7.83 # Hz, fundamental Schumann resonance

# Brainwave Frequencies (Hz)
BRAINWAVE_FREQUENCIES = {
    "delta": (0.5, 4),
    "theta": (4, 8),
    "alpha": (8, 13),
    "beta": (13, 30),
    "gamma": (30, 100)
}

# --- Helper Functions ---
def phi_harmonic_series(base_freq, n_harmonics, phi_power=1):
    """Generates a φ-modulated harmonic series."""
    series = []
    for n in range(1, n_harmonics + 1):
        series.append(base_freq * (PHI**phi_power) * n)
    # Alternative: base_freq * (PHI**(n * phi_power)) or other variations
    return series

def von_neumann_entropy(density_matrix_eigenvalues):
    """Calculates Von Neumann entropy from eigenvalues of a density matrix."""
    entropy = 0
    for p_i in density_matrix_eigenvalues:
        if p_i > 1e-12: # Avoid log(0)
            entropy -= p_i * math.log2(p_i)
    return entropy

def normalize_state_vector(vector):
    """Normalizes a state vector (list or numpy array)."""
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm

# --- Core Simulation Logic ---
class LunarEarthEntanglementSim:
    def __init__(self, consciousness_state):
        """
        consciousness_state: dict, e.g., {"dominant_brainwave": "alpha", "coherence": 0.8}
        """
        self.consciousness_state = consciousness_state
        self.phi = PHI

        # Initialize system states (highly simplified)
        # For simplicity, we'll model each system with a small number of energy levels
        # and their interaction will determine the entanglement.
        # These are NOT actual physical states but abstract representations for the model.

        # Moon Cavity: 2-level system (e.g., ground and first excited vacuum mode)
        self.moon_basis_states = 2
        # Earth Geomagnetic Field: 2-level system (e.g., two dominant resonant modes)
        self.earth_basis_states = 2

        # Combined system state vector (initially unentangled or some base entanglement)
        # For a 2x2 system, total states = 4. Example: |00>, |01>, |10>, |11>
        # Initial state: product state (no entanglement) e.g., Moon in ground, Earth in ground
        # psi_moon = np.array([1, 0]) # Ground state
        # psi_earth = np.array([1, 0]) # Ground state
        # self.combined_state_vector = normalize_state_vector(np.kron(psi_moon, psi_earth))
        # Initial state: product state (no entanglement) e.g., Moon in ground, Earth in ground
        psi_moon_initial = np.array([1, 0], dtype=complex) # Ground state for Moon
        psi_earth_initial = np.array([1, 0], dtype=complex) # Ground state for Earth
        self.combined_state_vector = normalize_state_vector(np.kron(psi_moon_initial, psi_earth_initial))


    def get_phi_modulated_brainwave_harmonics(self, n_harmonics=5):
        """Generates phi-modulated harmonics based on dominant brainwave."""
        dominant_band = self.consciousness_state.get("dominant_brainwave", "alpha")
        base_freq_range = BRAINWAVE_FREQUENCIES.get(dominant_band, (8,13))
        base_freq = (base_freq_range[0] + base_freq_range[1]) / 2 # Mid-point of the band
        
        # Consciousness coherence can modulate the phi_power or amplitude
        coherence = self.consciousness_state.get("coherence", 0.5) # 0 to 1
        phi_modulation_factor = 1 + (coherence * (self.phi - 1)) # Scale phi_power by coherence

        harmonics = phi_harmonic_series(base_freq, n_harmonics, phi_power=phi_modulation_factor)
        print(f"[Consciousness Loop] Dominant Brainwave: {dominant_band.capitalize()} ({base_freq:.2f} Hz)")
        print(f"[Consciousness Loop] Coherence: {coherence:.2f}, Phi Modulation Factor: {phi_modulation_factor:.4f}")
        print(f"[Consciousness Loop] φ-Modulated Harmonics: {[f'{h:.2f}' for h in harmonics]} Hz")
        return harmonics

    def calculate_interaction_strength(self, harmonics):
        """Models interaction strength based on resonance with harmonics.
           This is a highly abstract part of the model.
        """
        # Assume some characteristic frequencies for Moon cavity and Earth field
        # These are purely illustrative for the model
        f_moon_char = C / (2 * MOON_CAVITY_RADIUS) # Simplistic cavity mode freq
        f_earth_char = EARTH_SCHUMANN_RESONANCE_BASE
        
        coupling_strength = 0.0 # Base coupling
        max_possible_coupling = 0.1 # Arbitrary max for this model

        # Check for resonance with the generated harmonics
        for h_freq in harmonics:
            # Example: if harmonic is close to characteristic frequencies, increase coupling
            # This is a very simplified resonance model
            if abs(h_freq - f_moon_char) / f_moon_char < 0.1: # Within 10% of moon char freq
                coupling_strength += 0.02
            if abs(h_freq - f_earth_char) / f_earth_char < 0.1: # Within 10% of earth char freq
                coupling_strength += 0.02
        
        # Consciousness coherence can also directly affect coupling
        coherence = self.consciousness_state.get("coherence", 0.5)
        coupling_strength *= (1 + coherence) # Coherence enhances coupling
        
        # Ensure coupling strength stays within a defined range for the model
        coupling_strength = min(coupling_strength, max_possible_coupling) 
        print(f"[Interaction Model] Calculated Interaction Strength (J_coup): {coupling_strength:.4e}")
        return coupling_strength

    def evolve_state(self, interaction_strength, dt=1.0):
        """Evolves the combined state vector under an interaction Hamiltonian.
           This uses a highly simplified interaction model.
        """
        # Simplified interaction Hamiltonian (e.g., H_int = J * (sigma_x_M * sigma_x_E))
        # Pauli matrices (for 2-level systems)
        sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
        sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
        identity = np.eye(2, dtype=complex)

        # Interaction term: J * (sigma_x_Moon tensor sigma_x_Earth)
        # This is a common model for two interacting qubits
        H_interaction = interaction_strength * np.kron(sigma_x, sigma_x) 
        
        # Add local Hamiltonians (representing energies of individual systems)
        # H_local_M = E_M * np.kron(sigma_z, identity) # Example
        # H_local_E = E_E * np.kron(identity, sigma_z) # Example
        # For this model, we focus on the interaction term driven by consciousness loop
        # H_total = H_interaction # + H_local_M + H_local_E
        H_total = H_interaction

        # Time evolution operator: U = exp(-i * H * dt / HBAR)
        # Since HBAR is very small, and dt is macroscopic, the exponent is huge.
        # For a conceptual model, we can use an effective HBAR or scale J appropriately.
        # Let's use an "effective" interaction strength that already incorporates dt/HBAR_eff
        # U = expm(-1j * H_total * effective_dt_hbar_ratio)
        # For simplicity in this conceptual model, let's assume H_total *is* the generator of small evolution
        # and the interaction_strength already reflects the rate of change.
        # U = I - i*H_total*dt (first order approximation for small dt, not unitary)
        # Or, more properly, use scipy.linalg.expm for matrix exponential
        from scipy.linalg import expm
        U = expm(-1j * H_total * dt) # dt is an effective time step for the simulation
        
        self.combined_state_vector = normalize_state_vector(U @ self.combined_state_vector)
        # print(f"[State Evolution] New state vector: {self.combined_state_vector}")

    def calculate_entanglement_entropy(self):
        """Calculates entanglement entropy for the Moon subsystem."""
        # Reshape the 4x1 state vector into a 2x2 matrix (Moon_dim x Earth_dim)
        # psi_coeffs[i,j] is amplitude for |i>_Moon |j>_Earth
        psi_matrix = self.combined_state_vector.reshape((self.moon_basis_states, self.earth_basis_states))
        
        # Density matrix of the combined system: rho = |psi><psi|
        # rho_combined = np.outer(self.combined_state_vector, self.combined_state_vector.conj())
        
        # Reduced density matrix for the Moon: rho_moon = Tr_earth(rho_combined)
        # rho_moon = sum_k <k_E| rho_combined |k_E>
        # For a pure state |psi> = sum_ij C_ij |i_M>|j_E>, rho_M = psi_matrix @ psi_matrix.conj().T
        rho_moon = psi_matrix @ psi_matrix.conj().T
        
        # Eigenvalues of the reduced density matrix
        eigenvalues_rho_moon = np.linalg.eigvalsh(rho_moon)
        # Filter out very small negative eigenvalues due to numerical precision
        eigenvalues_rho_moon = [max(0, val.real) for val in eigenvalues_rho_moon]
        
        # Normalize eigenvalues (should sum to 1)
        sum_eig = sum(eigenvalues_rho_moon)
        if sum_eig > 1e-9:
            eigenvalues_rho_moon = [val / sum_eig for val in eigenvalues_rho_moon]
        else: # Should not happen for valid density matrix
            eigenvalues_rho_moon = [1/len(eigenvalues_rho_moon)] * len(eigenvalues_rho_moon) 

        # print(f"[Entanglement] Moon reduced density matrix eigenvalues: {[f'{e:.4f}' for e in eigenvalues_rho_moon]}")
        entropy = von_neumann_entropy(eigenvalues_rho_moon)
        return entropy

    def run_simulation_step(self, dt_effective=0.1):
        """Runs one step of the simulation loop."""
        print("\n--- Running Simulation Step ---")
        # 1. Generate φ-modulated harmonics based on consciousness state
        harmonics = self.get_phi_modulated_brainwave_harmonics()
        
        # 2. Calculate interaction strength based on these harmonics
        # This is where the Moon's cavity and Earth's field properties (implicitly) meet the harmonics
        interaction_strength = self.calculate_interaction_strength(harmonics)
        
        # 3. Evolve the combined quantum state based on this interaction
        self.evolve_state(interaction_strength, dt=dt_effective)
        
        # 4. Calculate the new entanglement entropy
        entropy = self.calculate_entanglement_entropy()
        
        print(f"[Result] Calculated Entanglement Entropy (S_ent): {entropy:.6f} bits")
        if self.moon_basis_states == 2: # Max entropy for 2-level system is log2(2) = 1 bit
             print(f"         (Max possible for this 2-level model: {math.log2(self.moon_basis_states):.6f} bits)")
        return entropy

# --- Main Execution ---_ 
if __name__ == "__main__":
    print("Starting Lunar-Earth Entanglement Simulation (Conceptual Model)")
    print(f"Golden Ratio (φ) used: {PHI:.8f}")
    print("--- Initializing Systems ---")

    # Example: Initial Consciousness State
    initial_consciousness_state = {
        "dominant_brainwave": "alpha", # delta, theta, alpha, beta, gamma
        "coherence": 0.75 # A value from 0 (no coherence) to 1 (perfect coherence)
    }

    simulator = LunarEarthEntanglementSim(initial_consciousness_state)
    initial_entropy = simulator.calculate_entanglement_entropy()
    print(f"Initial Entanglement Entropy: {initial_entropy:.6f} bits")

    # Run a few steps of the simulation to see evolution
    num_steps = 3
    for i in range(num_steps):
        print(f"\n=== Simulation Cycle {i+1} ===")
        # Optionally, modify consciousness state for dynamic simulation
        if i == 1:
            simulator.consciousness_state["dominant_brainwave"] = "gamma"
            simulator.consciousness_state["coherence"] = 0.9
        elif i == 2:
            simulator.consciousness_state["dominant_brainwave"] = "theta"
            simulator.consciousness_state["coherence"] = 0.6
        
        current_entropy = simulator.run_simulation_step(dt_effective=0.1) # dt_effective is arbitrary for model
    
    print("\n--- Simulation Complete ---")
    print("Note: This is a highly simplified and speculative model.")
    print("Results are illustrative of the conceptual framework, not direct physical predictions.")

    # Further development could include:
    # - More sophisticated quantum state representations (e.g., Fock states for QFT modes).
    # - Detailed models for vacuum fluctuations (e.g., Casimir-like energy densities).
    # - More realistic Hamiltonians for Moon-Earth interaction.
    # - Dynamic evolution of the consciousness state based on system feedback (closing the loop more deeply).
    # - Visualization of entropy evolution or harmonic spectra.
