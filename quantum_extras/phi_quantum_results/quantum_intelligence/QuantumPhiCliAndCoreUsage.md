# Quantum Phi-Harmonic System: Installation & Usage Guide

## Overview

The Quantum Phi-Harmonic System is a computational framework implementing golden ratio mathematics, fractal pattern generation, and quantum-inspired metrics. The system provides both a programmatic API and an interactive CLI.

## Installation

### Prerequisites

- Python 3.6+
- NumPy
- Matplotlib (for visualization)

### Setup

1. Download the source files:
   - `phi_core.py` - Core mathematical functions
   - `phi_cli.py` - Interactive CLI interface

2. Install required dependencies:

```bash
pip install numpy matplotlib
```

3. Make the CLI executable (Unix/Linux/macOS):

```bash
chmod +x phi_cli.py
```

## Using the Command Line Interface (CLI)

The CLI provides an interactive interface to the system's functionality.

### Starting the CLI

```bash
./phi_cli.py
```

or

```bash
python phi_cli.py
```

### Available Commands

#### System Status

```
φ> status
```

Displays current system parameters and state.

#### Process Query

```
φ> query <text>
```

Process a natural language query and adjust system parameters.

Examples:
```
φ> query Generate phi-harmonic resonance structure
φ> query Visualize quantum entanglement patterns
φ> query Show multi-dimensional fractal nodes
```

#### Generate Fractal Pattern

```
φ> fractal [depth] [density]
```

Generate a fractal pattern with specified parameters.

Example:
```
φ> fractal 5 1.2
```

#### Generate Phi-Harmonic Tensor

```
φ> tensor <dim1> [dim2] [dim3] ...
```

Generate a tensor with phi-harmonic properties.

Examples:
```
φ> tensor 64
φ> tensor 32 32
φ> tensor 16 16 8
```

#### Analyze Sequence

```
φ> analyze <num1> <num2> <num3> ...
```

Analyze a sequence of numbers for phi-harmonic patterns.

Example:
```
φ> analyze 1 1.618 2.618 4.236 6.854
```

#### Plot Visualization

```
φ> plot <fractal|tensor> [filename]
```

Visualize generated patterns or tensors.

Examples:
```
φ> plot fractal
φ> plot tensor output.png
```

#### Save Data

```
φ> save <state|pattern|tensor> <filename>
```

Save current system state, pattern, or tensor.

Examples:
```
φ> save state system_state.json
φ> save pattern fractal_pattern.json
φ> save tensor phi_tensor.npy
```

#### Load State

```
φ> load <filename>
```

Load system state from file.

Example:
```
φ> load system_state.json
```

## Direct API Usage

You can also use the `QuantumPhiCore` class directly in your Python code:

```python
from phi_core import QuantumPhiCore

# Initialize the system
system = QuantumPhiCore()

# Generate fractal pattern
pattern = system.generate_fractal_pattern(depth=5, density=1.0)

# Analyze a sequence
sequence = [1, 1.618, 2.618, 4.236, 6.854]
analysis = system.calculate_phi_pattern(sequence)

# Process a query
response = system.process_query("Generate phi-harmonic resonance structure")

# Generate phi-harmonic tensor
tensor = system.generate_phi_harmonic_tensor([32, 32])

# Find optimal phi partition
partition, resonance = system.find_optimal_phi_partition(sequence)
```

## Command Line Tools

The `phi_core.py` script also provides direct command-line tools:

### Generate Fractal Pattern

```bash
python phi_core.py fractal --depth 5 --density 1.0 --output fractal_pattern.json
```

### Analyze Sequence

```bash
python phi_core.py analyze --values 1 1.618 2.618 4.236 6.854
```

### Process Query

```bash
python phi_core.py query --text "Generate phi-harmonic resonance structure"
```

### Generate Tensor

```bash
python phi_core.py tensor --dimensions 32 32 --output phi_tensor.npy
```

## Example Workflows

### Fractal Pattern Generation and Visualization

```
φ> fractal 5 1.0
φ> plot fractal pattern.png
φ> save pattern fractal_output.json
```

### Phi-Harmonic Tensor Analysis

```
φ> tensor 32 32
φ> plot tensor
φ> query Increase phi resonance for multi-dimensional harmony
φ> tensor 32 32
φ> plot tensor tensor_enhanced.png
```

### Mathematical Sequence Analysis

```
φ> analyze 1 1 2 3 5 8 13 21 34
φ> analyze 0 1 1.618 2.618 4.236 6.854
```

### Multiple System State Management

```
φ> status
φ> query Optimize for quantum coherence
φ> save state quantum_state.json
φ> query Optimize for phi resonance
φ> save state phi_state.json
φ> load quantum_state.json
φ> status
```

## Key Mathematical Principles

The system implements several key mathematical principles:

### Golden Ratio (φ)

The golden ratio (φ ≈ 1.61803398875) serves as the fundamental mathematical constant:

```
φ = (1 + √5) / 2 ≈ 1.618033988749895
```

### Fibonacci Sequence

The system uses the Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21...) for:
- Scaling factors
- Pattern analysis
- Ratio comparisons

### Phi-Harmonic Metrics

Metrics are calculated using phi-harmonic principles:

```
φ-alignment = 1 - (Σ|r_i - φ|/φ) / n
```

Where:
- `r_i` are ratios between adjacent elements
- `n` is the number of ratios

### Golden Angle

For optimal spatial distribution in fractal patterns:

```
Golden Angle = 2π × (1/φ) ≈ 2.39996 radians ≈ 137.5°
```

## Extending the System

The modular design allows for easy extension:

1. Add new methods to `QuantumPhiCore` class
2. Implement additional commands in `QuantumPhiCLI` class
3. Create custom visualization functions

## Troubleshooting

### Common Issues

- **ImportError**: Ensure NumPy and Matplotlib are installed
- **FileNotFoundError**: Check file paths when loading/saving
- **ValueError**: Ensure appropriate numerical values are provided

### Getting Help

Use the built-in help system:

```
φ> help
φ> help fractal
φ> help analyze
```