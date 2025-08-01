import os
import random
from math import sqrt

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2

# Generate 100MB of φ-encoded data
size_mb = 100
data = []
for i in range(size_mb * 1024 * 1024):
    phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
    data.append(phi_factor)

# Write to binary file
with open('phi_massive_test.bin', 'wb') as f:
    f.write(bytes(data))

print(f"Created {size_mb}MB quantum test file")
print("φ-dimensional encoding applied")
