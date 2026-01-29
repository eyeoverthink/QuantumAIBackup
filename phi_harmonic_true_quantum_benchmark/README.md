# Phi-Harmonic True Quantum Benchmark

## Overview
This benchmark suite comprehensively tests the Phi-Harmonic Quantum Random system's ability to generate true randomness that transcends traditional computational boundaries. The system leverages golden ratio mathematics, quantum principles, and hyper-dimensional scaling to create a revolutionary approach to random number generation.

## Key Features

- **True Randomness Testing**: Evaluates the system's ability to generate true randomness across multiple epochs without new seeds
- **Hyper-Dimensional Scaling**: Tests scaling across 2-7 dimensions with phi-harmonic principles
- **Phi-Harmonic Distribution Analysis**: Analyzes distribution properties and golden ratio alignment
- **Quantum Metrics**: Measures coherence, resonance, and phi alignment precision
- **Comprehensive Visualization**: Generates detailed visualizations of all test results

## Components

### 1. Core Framework (`benchmark_core.py`)
- Base class for all benchmark modules
- Common utilities for sample generation, analysis, and visualization
- Result storage and management

### 2. Random Generation Benchmark (`random_generation_benchmark.py`)
- Tests the `PhiHarmonicRandomOrchestratorAdapter` and `QuantumPhiRandom` libraries
- Runs multi-epoch tests to evaluate true randomness
- Performs statistical tests for uniformity and randomness quality

### 3. Hyper-Dimensional Benchmark (`hyper_dimensional_benchmark.py`)
- Tests scaling across multiple dimensions
- Measures performance impact of dimensional scaling
- Evaluates quantum coherence preservation across dimensions

### 4. Benchmark Runner (`benchmark_runner.py`)
- Integrates all benchmark components
- Provides a unified interface for running the complete benchmark suite
- Generates comprehensive summary of results

## Usage

### Basic Usage
```bash
# Run all benchmarks with default settings
python benchmark_runner.py --all

# Run only random generation benchmark
python benchmark_runner.py --random

# Run only hyper-dimensional benchmark
python benchmark_runner.py --hyper
```

### Advanced Options
```bash
# Customize random benchmark
python benchmark_runner.py --random --samples 20000 --epochs 5

# Customize hyper-dimensional benchmark
python benchmark_runner.py --hyper --dimensions 2,3,4,5,6,7 --size 8

# Run all benchmarks with custom settings
python benchmark_runner.py --all --samples 20000 --epochs 5 --dimensions 2,3,4,5,6,7 --size 8
```

## Results

The benchmark generates comprehensive results in the `results` directory:
- JSON result files with all metrics and measurements
- Visualizations in the `results/visualizations` directory
- Log file with detailed benchmark execution information

## Requirements

- Python 3.13+
- NumPy, SciPy, Matplotlib
- Phi-Harmonic Quantum Random libraries
- Decimal library for high-precision calculations

## Design Philosophy

This benchmark follows the "lego" design philosophy by creating new components that work with existing ones without modifying them. It maintains quantum coherence and resonance throughout the testing process, ensuring accurate measurement of the system's capabilities.

The benchmark is designed to be:
- Modular and extensible
- Non-invasive to the core quantum system
- Comprehensive in its testing approach
- Detailed in its analysis and reporting

## Quantum Principles

The benchmark leverages key quantum principles:
- Golden ratio (φ = 1.618033988749895) as fundamental constant
- Phi-harmonic resonance for pattern generation
- Quantum coherence preservation across dimensions
- Hyper-dimensional scaling through phi-powered metrics
