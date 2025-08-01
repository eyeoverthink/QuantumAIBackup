
import numpy as np
import matplotlib.pyplot as plt
import torch
import math

# === PHI Constant ===
PHI = (1 + np.sqrt(5)) / 2

# === Core Constants ===
pi = np.pi
i = complex(0, 1)

# === Define Fields ===

def psi_source(r):
    return sum([PHI**-n * np.exp(2j * pi * PHI * r) / r for n in range(1, 5)])

def bridge_field(x):
    return np.exp(2j * pi * PHI * x / 7) * np.exp(-x / PHI)

def psi_target(r):
    return psi_source(r) * np.exp(1j * pi / PHI)

# === Quantum Tunnel Formation Γ ===
def gamma(x, t):
    return PHI * psi_source(x) * psi_target(x) * np.exp(2j * pi * (PHI * x + np.sqrt(PHI)) / 7) * np.exp(-x / (7 * PHI))

# === Probability Function ===
def teleportation_probability(coherence, distance, resonance, stability):
    D = 1 / (1 + (distance / PHI**2)**2)
    S = abs(np.cos(2 * pi / PHI))
    R = abs(np.sum([gamma(x, 1) * bridge_field(x) * np.exp(2j * pi / PHI) for x in np.linspace(0.1, 1.0, 10)]))
    return min(1.0, PHI * coherence * D * R * S * (1 + 1 / PHI))

# === Visualization ===
r_values = np.linspace(0.1, 1.0, 300)
psi_s_vals = np.real([psi_source(r) for r in r_values])
psi_t_vals = np.real([psi_target(r) for r in r_values])
gamma_vals = np.real([gamma(r, 1) for r in r_values])

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(r_values, psi_s_vals, label='Ψ Source')
plt.plot(r_values, psi_t_vals, label='Ψ Target', linestyle='--')
plt.title('Phi-Resonant Fields')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(r_values, gamma_vals, label='Γ (Tunnel Field)', color='green')
plt.title('Quantum Tunnel Formation')

plt.subplot(3, 1, 3)
prob = teleportation_probability(coherence=0.96, distance=0.5, resonance=1.0, stability=0.99)
plt.bar(['Teleportation Probability'], [prob], color='purple')
plt.ylim(0, 1.1)
plt.title('Teleportation Probability')

plt.tight_layout()
plt.show()
