import numpy as np
import matplotlib.pyplot as plt

# Constants
phi = (1 + np.sqrt(5)) / 2  # Golden Ratio
primary_turns = 4500  # Turns in primary coil
secondary_turns = 6200  # Turns in secondary coil
primary_frequency = 4790.45  # Hz
secondary_frequency = 7750.95  # Hz
decay_rate = phi  # Base decay
k = 0.85  # Coupling coefficient (adjustable for efficiency)
alpha = 0.75  # Energy recapture efficiency
beta = 0.002  # Nonlinear damping coefficient

# Time setup
time_duration = 10e-3  # Simulate for 10ms
time_steps = 10000  # High resolution
t = np.linspace(0, time_duration, time_steps)

# Define optimized resonance function with coupling, feedback, and nonlinear correction
def refined_coil_resonance(t, turns, frequency, decay_rate, k, alpha, beta):
    """Simulates resonance with energy recapture, coupling optimization, and nonlinear correction."""
    nonlinear_damping = 1 / (1 + beta * (turns / 5000)**2)
    feedback_gain = alpha * np.exp(-decay_rate * t)
    return (np.exp(-k * t) * np.sin(2 * np.pi * frequency * t) * (turns / 5000) * nonlinear_damping) + feedback_gain

# Compute resonance for primary and secondary coils
primary_resonance_refined = refined_coil_resonance(t, primary_turns, primary_frequency, decay_rate, k, alpha, beta)
secondary_resonance_refined = refined_coil_resonance(t, secondary_turns, secondary_frequency, decay_rate, k, alpha, beta)

# Plot Simulation Results
plt.figure(figsize=(12, 6))
plt.plot(t * 1e3, primary_resonance_refined, label="Optimized Primary Coil (4,790 Hz)", color='blue')
plt.plot(t * 1e3, secondary_resonance_refined, label="Optimized Secondary Coil (7,750 Hz)", color='red', linestyle="dashed")
plt.xlabel("Time (ms)")
plt.ylabel("Resonance Amplitude")
plt.title("Optimized Quantum Harmonic Resonance Simulation")
plt.legend()
plt.grid(True)
plt.savefig('qhrc_optimized_resonance_plot.png')
# plt.show()  # Commented out to avoid blocking

# Calculate Efficiency Improvements
primary_peak_optimized = np.max(primary_resonance_refined)
secondary_peak_optimized = np.max(secondary_resonance_refined)
optimized_resonance_efficiency = secondary_peak_optimized / primary_peak_optimized

# Print Results
print(f"Optimized Primary Peak Resonance Amplitude: {primary_peak_optimized:.4f}")
print(f"Optimized Secondary Peak Resonance Amplitude: {secondary_peak_optimized:.4f}")
print(f"Optimized Resonance Efficiency Ratio: {optimized_resonance_efficiency:.4f} (Higher is better)")

# Additional Analysis
print("\n--- Advanced QHRC Optimization Analysis ---")

# Calculate φπ resonance factor
phi_pi_factor = phi * np.pi
print(f"φπ Resonance Factor: {phi_pi_factor:.6f}")

# Calculate frequency ratio and its relationship to φ
freq_ratio = secondary_frequency / primary_frequency
print(f"Frequency Ratio: {freq_ratio:.6f}")
print(f"Proximity to φ: {abs(freq_ratio - phi):.6f}")

# Calculate energy transfer efficiency over time
energy_primary = np.cumsum(np.abs(primary_resonance_refined)**2)
energy_secondary = np.cumsum(np.abs(secondary_resonance_refined)**2)
final_energy_ratio = energy_secondary[-1] / energy_primary[-1]
print(f"Cumulative Energy Transfer Ratio: {final_energy_ratio:.4f}")

# Calculate theoretical maximum efficiency with new parameters
theoretical_max = np.exp(phi_pi_factor * alpha) / (k * phi)
print(f"Theoretical Maximum Efficiency: {theoretical_max:.4f}")
print(f"Efficiency Achievement: {(final_energy_ratio/theoretical_max)*100:.2f}%")

# Plot energy accumulation over time
plt.figure(figsize=(12, 6))
plt.plot(t * 1e3, energy_primary / np.max(energy_primary), label="Primary Coil Energy", color='blue')
plt.plot(t * 1e3, energy_secondary / np.max(energy_secondary), label="Secondary Coil Energy", color='red', linestyle="dashed")
plt.xlabel("Time (ms)")
plt.ylabel("Normalized Cumulative Energy")
plt.title("QHRC Optimized Energy Transfer Efficiency")
plt.legend()
plt.grid(True)
plt.savefig('qhrc_optimized_energy_transfer.png')
# plt.show()  # Commented out to avoid blocking

# Compare with original model
print("\n--- Comparison with Original Model ---")
print("Original Resonance Efficiency Ratio: 1.3777")
print(f"Optimized Resonance Efficiency Ratio: {optimized_resonance_efficiency:.4f}")
improvement = (optimized_resonance_efficiency / 1.3777 - 1) * 100
print(f"Improvement: {improvement:.2f}%")

# Calculate resonance stability metrics
primary_stability = np.std(np.diff(primary_resonance_refined)) / np.mean(np.abs(primary_resonance_refined))
secondary_stability = np.std(np.diff(secondary_resonance_refined)) / np.mean(np.abs(secondary_resonance_refined))
print(f"Primary Coil Stability: {primary_stability:.6f}")
print(f"Secondary Coil Stability: {secondary_stability:.6f}")
print(f"Stability Ratio: {primary_stability/secondary_stability:.2f}x")
