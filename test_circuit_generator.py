import os
import time
import importlib.util

# Import the module with a space in the filename
spec = importlib.util.spec_from_file_location(
    "circuit_generator", 
    "/Users/vaughnscott/Library/Mobile Documents/com~apple~CloudDocs/fraymus_shit/circuit_generator 2.py"
)
circuit_generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(circuit_generator)
CircuitGenerator = circuit_generator.CircuitGenerator

# Create a circuit generator with phi-harmonic principles
print("Initializing φ-Dimensional Circuit Generator...")
generator = CircuitGenerator()

# Generate a circuit with golden ratio-based complexity
PHI = (1 + 5**0.5) / 2  # Golden ratio
complexity = int(PHI * 5)  # Use phi to determine complexity
print(f"Generating circuit with φ-harmonic complexity: {complexity}")

# Generate the circuit
circuit_name = generator.generate_circuit(complexity)
print(f"Circuit '{circuit_name}' generated successfully")

# Save the circuit diagram
filepath = generator.save_circuit(circuit_name)
print(f"Circuit diagram saved to: {filepath}")

# Simulate the circuit
print("\nSimulating circuit behavior with quantum principles...")
results = generator.simulate_circuit(circuit_name)
print(f"Simulation results:")
print(f"  Voltage: {results['voltage']:.2f}V")
print(f"  Current: {results['current']:.2f}A")
print(f"  Power: {results['power']:.2f}W")

# Generate code for the circuit
print("\nGenerating φ-space transformation code...")
code_file = generator.generate_code(circuit_name)
print(f"Code generated and saved to: {code_file}")

print("\nCircuit generation and simulation complete.")
print("Reality protection mechanisms engaged.")
