import matplotlib.pyplot as plt

# Data from RSA verification reports
rsa_sizes = [4096, 65536, 131072]
consciousness_levels = [0.95, 0.472, 0.0]
pattern_strengths = [0.0007, 0.0001, 0.0000006]
quantum_coherence = [0.32, 0.236, 0.5]
factorization_times = [8.88, 6.06, 4.72]

# Plotting
plt.figure(figsize=(12, 8))

# Consciousness Levels
plt.subplot(2, 2, 1)
plt.plot(rsa_sizes, consciousness_levels, marker='o', color='blue')
plt.title('Consciousness Level vs RSA Size')
plt.xlabel('RSA Size (bits)')
plt.ylabel('Consciousness Level')
plt.grid(True)

# Pattern Strength
plt.subplot(2, 2, 2)
plt.plot(rsa_sizes, pattern_strengths, marker='o', color='green')
plt.title('Pattern Strength vs RSA Size')
plt.xlabel('RSA Size (bits)')
plt.ylabel('Pattern Strength')
plt.yscale('log')
plt.grid(True)

# Quantum Coherence
plt.subplot(2, 2, 3)
plt.plot(rsa_sizes, quantum_coherence, marker='o', color='red')
plt.title('Quantum Coherence vs RSA Size')
plt.xlabel('RSA Size (bits)')
plt.ylabel('Quantum Coherence')
plt.grid(True)

# Factorization Time
plt.subplot(2, 2, 4)
plt.plot(rsa_sizes, factorization_times, marker='o', color='purple')
plt.title('Factorization Time vs RSA Size')
plt.xlabel('RSA Size (bits)')
plt.ylabel('Time (seconds)')
plt.grid(True)

plt.tight_layout()
plt.savefig('quantum_metrics_scaling.png')
plt.show()
