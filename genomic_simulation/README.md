# Genomic Simulation Module

This module simulates the "expression" of a digital genome (like those created by `qr_genome_phi_hanoi.py`) into a phenotype. The expression is influenced by a simulated environment.

## Core Components

- **`digital_dna.py`**: Loads and parses a genome JSON file, representing the organism's genetic code.
- **`environment.py`**: Defines the environmental conditions (e.g., resource levels, resonance fields) that influence gene expression.
- **`phenotype.py`**: Represents the observable traits of the organism that result from the interaction of its DNA and the environment.
- **`simulator.py`**: The main engine that orchestrates the simulation, taking a DNA and an Environment to produce a Phenotype.
