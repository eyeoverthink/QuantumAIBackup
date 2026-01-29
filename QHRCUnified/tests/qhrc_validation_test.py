import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd

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

# Test 1: Conservation of Energy Validation
print("=== TEST 1: CONSERVATION OF ENERGY VALIDATION ===")

def coil_resonance(t, turns, frequency, decay_rate):
    """Simulates self-sustaining resonance for primary and secondary coils."""
    return np.exp(-decay_rate * t) * np.sin(2 * np.pi * frequency * t) * (turns / 5000)

# Compute resonance for primary and secondary coils
primary_resonance = coil_resonance(t, primary_turns, primary_frequency, decay_rate)
secondary_resonance = coil_resonance(t, secondary_turns, secondary_frequency, decay_rate)

# Calculate energy in each coil over time (proportional to amplitude squared)
primary_energy = np.cumsum(np.abs(primary_resonance)**2)
secondary_energy = np.cumsum(np.abs(secondary_resonance)**2)

# Calculate total system energy
total_energy = primary_energy + secondary_energy
final_energy_ratio = secondary_energy[-1] / primary_energy[-1]

print(f"Primary Energy: {primary_energy[-1]:.4f}")
print(f"Secondary Energy: {secondary_energy[-1]:.4f}")
print(f"Energy Ratio: {final_energy_ratio:.4f}")

# Test 2: Physical Constraints Test
print("\n=== TEST 2: PHYSICAL CONSTRAINTS TEST ===")

# Test with different decay rates to see if the effect persists
decay_rates = [0.5, 1.0, phi, 2.0, 3.0]
results = []

for decay in decay_rates:
    primary = coil_resonance(t, primary_turns, primary_frequency, decay)
    secondary = coil_resonance(t, secondary_turns, secondary_frequency, decay)
    
    primary_peak = np.max(primary_resonance)
    secondary_peak = np.max(secondary)
    efficiency = secondary_peak / primary_peak
    
    primary_e = np.cumsum(np.abs(primary)**2)[-1]
    secondary_e = np.cumsum(np.abs(secondary)**2)[-1]
    energy_ratio = secondary_e / primary_e
    
    results.append({
        'Decay Rate': decay,
        'Primary Peak': primary_peak,
        'Secondary Peak': secondary_peak,
        'Efficiency Ratio': efficiency,
        'Energy Ratio': energy_ratio
    })

results_df = pd.DataFrame(results)
print(results_df)

# Test 3: Frequency Sensitivity Analysis
print("\n=== TEST 3: FREQUENCY SENSITIVITY ANALYSIS ===")

# Test slight deviations from the golden ratio frequency relationship
freq_ratios = [1.5, 1.6, 1.618, 1.62, 1.7]
freq_results = []

for ratio in freq_ratios:
    test_secondary_freq = primary_frequency * ratio
    
    primary = coil_resonance(t, primary_turns, primary_frequency, decay_rate)
    secondary = coil_resonance(t, secondary_turns, test_secondary_freq, decay_rate)
    
    primary_peak = np.max(primary)
    secondary_peak = np.max(secondary)
    efficiency = secondary_peak / primary_peak
    
    primary_e = np.cumsum(np.abs(primary)**2)[-1]
    secondary_e = np.cumsum(np.abs(secondary)**2)[-1]
    energy_ratio = secondary_e / primary_e
    
    proximity_to_phi = abs(ratio - phi)
    
    freq_results.append({
        'Frequency Ratio': ratio,
        'Proximity to φ': proximity_to_phi,
        'Efficiency Ratio': efficiency,
        'Energy Ratio': energy_ratio
    })

freq_results_df = pd.DataFrame(freq_results)
print(freq_results_df)

# Test 4: Realistic Energy Loss Model
print("\n=== TEST 4: REALISTIC ENERGY LOSS MODEL ===")

# Define a more realistic physical model with losses
def realistic_coil_system(t, y, primary_f, secondary_f, coupling, loss_factor):
    """
    More realistic coupled coil system with losses
    y[0] = primary amplitude
    y[1] = primary velocity
    y[2] = secondary amplitude
    y[3] = secondary velocity
    """
    # Primary coil
    dydt0 = y[1]
    dydt1 = -((2*np.pi*primary_f)**2) * y[0] - loss_factor * y[1] + coupling * y[2]
    
    # Secondary coil
    dydt2 = y[3]
    dydt3 = -((2*np.pi*secondary_f)**2) * y[2] - loss_factor * y[3] + coupling * y[0]
    
    return [dydt0, dydt1, dydt2, dydt3]

# Initial conditions - only primary coil has initial energy
y0 = [1.0, 0.0, 0.0, 0.0]

# Test with different coupling coefficients and loss factors
couplings = [0.1, 0.3, phi/10, 0.5, 0.7]
loss_factors = [0.1, 0.3, 0.5, 0.7, 1.0]

realistic_results = []

for coupling in couplings:
    for loss in loss_factors:
        # Solve the differential equations
        sol = solve_ivp(
            lambda t, y: realistic_coil_system(t, y, primary_frequency, secondary_frequency, coupling, loss),
            [0, time_duration],
            y0,
            method='RK45',
            t_eval=t
        )
        
        # Extract primary and secondary amplitudes
        primary_amp = sol.y[0]
        secondary_amp = sol.y[2]
        
        # Calculate peaks and energy
        primary_peak = np.max(np.abs(primary_amp))
        secondary_peak = np.max(np.abs(secondary_amp))
        efficiency = secondary_peak / primary_peak
        
        # Calculate energy (proportional to amplitude squared)
        primary_energy = np.sum(primary_amp**2)
        secondary_energy = np.sum(secondary_amp**2)
        energy_ratio = secondary_energy / primary_energy
        
        realistic_results.append({
            'Coupling': coupling,
            'Loss Factor': loss,
            'Primary Peak': primary_peak,
            'Secondary Peak': secondary_peak,
            'Efficiency Ratio': efficiency,
            'Energy Ratio': energy_ratio
        })

# Convert to DataFrame and display top results
realistic_df = pd.DataFrame(realistic_results)
print("Top 5 most efficient configurations:")
print(realistic_df.sort_values('Efficiency Ratio', ascending=False).head(5))

print("\n=== CONCLUSION ===")
print("1. Original model efficiency ratio: 1.3777")
print(f"2. Best realistic model efficiency ratio: {realistic_df['Efficiency Ratio'].max():.4f}")
print(f"3. Frequency ratio sensitivity: Optimal at {freq_results_df.loc[freq_results_df['Efficiency Ratio'].idxmax(), 'Frequency Ratio']:.6f}")

# Save results to CSV for further analysis
results_df.to_csv('qhrc_decay_test_results.csv', index=False)
freq_results_df.to_csv('qhrc_frequency_test_results.csv', index=False)
realistic_df.to_csv('qhrc_realistic_model_results.csv', index=False)

print("\nValidation tests complete. Results saved to CSV files.")
