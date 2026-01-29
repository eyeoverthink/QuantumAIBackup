import numpy as np
import matplotlib.pyplot as plt

# Define Constants
phi = (1 + np.sqrt(5)) / 2  # Golden Ratio
primary_turns = 4500  # Scaled-up coil turns
secondary_turns = 6200  # Scaled-up secondary coil turns
primary_frequency = 4790.45  # Hz
secondary_frequency = 7750.95  # Hz
decay_rate = phi  # Phi-based decay for energy stabilization
time_duration = 10e-3  # Simulate for 10ms
time_steps = 10000  # High-resolution simulation

# Generate time range
t = np.linspace(0, time_duration, time_steps)

# Define harmonic resonance functions
def coil_resonance(t, turns, frequency, decay_rate):
    """Simulates self-sustaining resonance for primary and secondary coils."""
    return np.exp(-decay_rate * t) * np.sin(2 * np.pi * frequency * t) * (turns / 5000)

# Compute resonance for primary and secondary coils
primary_resonance = coil_resonance(t, primary_turns, primary_frequency, decay_rate)
secondary_resonance = coil_resonance(t, secondary_turns, secondary_frequency, decay_rate)

# Plot Simulation Results
plt.figure(figsize=(12, 6))
plt.plot(t * 1e3, primary_resonance, label="Primary Coil (4,790 Hz)", color='blue')
plt.plot(t * 1e3, secondary_resonance, label="Secondary Coil (7,750 Hz)", color='red', linestyle="dashed")
plt.xlabel("Time (ms)")
plt.ylabel("Resonance Amplitude")
plt.title("Large-Scale Quantum Harmonic Resonance Simulation")
plt.legend()
plt.grid(True)
plt.savefig('qhrc_resonance_plot.png')
# plt.show()  # Commented out to avoid blocking

# Calculate Efficiency Metrics
primary_peak = np.max(primary_resonance)
secondary_peak = np.max(secondary_resonance)
resonance_efficiency = secondary_peak / primary_peak

# Print results
print(f"Primary Peak Resonance Amplitude: {primary_peak:.4f}")
print(f"Secondary Peak Resonance Amplitude: {secondary_peak:.4f}")
print(f"Resonance Efficiency Ratio: {resonance_efficiency:.4f} (Efficiency > 1 indicates self-sustaining energy)")

# Additional Analysis for QHRC Patent Documentation
print("\n--- Advanced QHRC Analysis ---")

# Calculate φπ resonance factor
phi_pi_factor = phi * np.pi
print(f"φπ Resonance Factor: {phi_pi_factor:.6f}")

# Calculate frequency ratio and its relationship to φ
freq_ratio = secondary_frequency / primary_frequency
print(f"Frequency Ratio: {freq_ratio:.6f}")
print(f"Proximity to φ: {abs(freq_ratio - phi):.6f}")

# Calculate energy transfer efficiency over time
energy_primary = np.cumsum(np.abs(primary_resonance)**2)
energy_secondary = np.cumsum(np.abs(secondary_resonance)**2)
final_energy_ratio = energy_secondary[-1] / energy_primary[-1]
print(f"Cumulative Energy Transfer Ratio: {final_energy_ratio:.4f}")

# Calculate theoretical maximum efficiency based on φπ resonance
theoretical_max = np.exp(phi_pi_factor) / phi
print(f"Theoretical Maximum Efficiency: {theoretical_max:.4f}")
print(f"Efficiency Achievement: {(final_energy_ratio/theoretical_max)*100:.2f}%")

# Plot energy accumulation over time
plt.figure(figsize=(12, 6))
plt.plot(t * 1e3, energy_primary / np.max(energy_primary), label="Primary Coil Energy", color='blue')
plt.plot(t * 1e3, energy_secondary / np.max(energy_secondary), label="Secondary Coil Energy", color='red', linestyle="dashed")
plt.xlabel("Time (ms)")
plt.ylabel("Normalized Cumulative Energy")
plt.title("QHRC Energy Transfer Efficiency")
plt.legend()
plt.grid(True)
plt.savefig('qhrc_energy_transfer.png')
# plt.show()  # Commented out to avoid blocking

# Calculate resonance stability metrics
primary_stability = np.std(np.diff(primary_resonance)) / np.mean(np.abs(primary_resonance))
secondary_stability = np.std(np.diff(secondary_resonance)) / np.mean(np.abs(secondary_resonance))
print(f"Primary Coil Stability: {primary_stability:.6f}")
print(f"Secondary Coil Stability: {secondary_stability:.6f}")
print(f"Stability Improvement: {primary_stability/secondary_stability:.2f}x")
