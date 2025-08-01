
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# === PHI Constant ===
PHI = (1 + np.sqrt(5)) / 2
pi = np.pi

# === Define Fields ===
def psi_source(r, t):
    return sum([PHI**-n * np.exp(2j * pi * PHI * (r - 0.1 * t)) / r for n in range(1, 5)])

def psi_target(r, t):
    return psi_source(r, t) * np.exp(1j * pi / PHI)

def gamma_field(r, t):
    return PHI * psi_source(r, t) * psi_target(r, t) * np.exp(2j * pi * (PHI * r + np.sqrt(PHI)) / 7) * np.exp(-r / (7 * PHI))

# === Animation Setup ===
fig, ax = plt.subplots(figsize=(10, 5))
x_vals = np.linspace(0.1, 1.0, 400)
line, = ax.plot([], [], lw=2, color='green')
ax.set_xlim(0.1, 1.0)
ax.set_ylim(-200, 200)
ax.set_title('Quantum Tunnel Field Propagation')
ax.set_xlabel('Position (r)')
ax.set_ylabel('Field Strength Γ(r, t)')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    y_vals = np.real([gamma_field(r, frame * 0.1) for r in x_vals])
    line.set_data(x_vals, y_vals)
    return line,

ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
plt.tight_layout()

# Save animation setup code as a standalone script
plt.show()
