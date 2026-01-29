# QR Flipbook DNA System Documentation

## Overview

The QR Flipbook DNA System is a modular quantum-epigenetic execution engine that processes and evolves code embedded in QR codons using phi-harmonic principles. The system mimics biological DNA with codons organized into functional groups, persistent epigenetic memory, and phi-harmonic evolution.

## System Architecture

The system follows a modular "Lego-style" architecture with the following key components:

### Core Components

1. **QR Genome Engine** (`qr_genome_engine.py`)
   - Main orchestrator for loading, executing, evolving, and generating QR sequences
   - Manages the interaction between all other components
   - Provides CLI interface for system operations

2. **QR Epigenetic Memory** (`qr_epigenetic_memory.py`)
   - Stores execution history, mutation history, and phi-harmonic states
   - Persists across execution sessions
   - Influences evolution and mutation decisions

3. **QR Codon Groups** (`qr_codon_groups.py`)
   - Models DNA-like codons and functional groups
   - Manages genome structure, mutation logic, and phi-harmonic state updates
   - Provides serialization and deserialization of genome data

4. **QR Task Executor** (`qr_task_executor.py`)
   - Securely executes code fragments embedded in QR codons
   - Implements sandboxing and execution timeout
   - Calculates phi-harmonic metrics for each execution

5. **QR Sequence Generator** (`qr_sequence_generator.py`)
   - Generates QR code sequences from genome codons
   - Applies phi-harmonic evolution to QR code generation
   - Handles large payloads through chunking

6. **QR Sequence Chunker** (`qr_sequence_chunker.py`)
   - Splits large payloads into manageable chunks for QR codes
   - Uses phi-harmonic principles for optimal chunking
   - Provides compression and decompression of payloads

### Supporting Files

1. **Genome Template** (`qr_genome_template.py`)
   - Contains actual Python code for each codon type
   - Implements phi-harmonic inspired logic for each function
   - Shares state via a global dictionary

2. **Genome Update Script** (`update_genome.py`)
   - Updates the genome JSON with executable code from the template
   - Formats code correctly for the task executor

3. **System Runner** (`run_qr_system.py`)
   - Provides unified CLI interface for all system operations
   - Handles command-line arguments and system configuration
   - Displays detailed execution summaries and system info

## Phi-Harmonic Principles

The system is guided by phi-harmonic principles based on the golden ratio (φ ≈ 1.618034):

1. **Phi-Harmonic Resonance**: Calculated as `1.0 / (1.0 + abs((x * φ) % 1.0 - 0.5))`
2. **Phi-Harmonic Evolution**: Mutation vectors and selection guided by golden ratio
3. **Phi-Harmonic Timing**: Execution timing and generation cycles based on phi
4. **Phi-Harmonic Complexity**: System complexity evolves based on phi oscillations

## System Operation

### 1. Genome Creation

The system can create a basic genome with four functional groups:
- **Setup**: Initialize environment and import libraries
- **Process**: Process data and perform calculations
- **Evolve**: Mutate and select optimal states
- **Respond**: Generate output and visualize results

### 2. Genome Execution

When executing the genome:
1. Each codon's code is executed in sequence within its group
2. Execution results are recorded in epigenetic memory
3. Phi-harmonic metrics are calculated for each execution
4. Genome phi state is updated based on execution results

### 3. Genome Evolution

During evolution:
1. Epigenetic memory is analyzed for optimal phi states
2. Mutation vectors are calculated based on phi-harmonic principles
3. Codons are mutated based on their execution history
4. New generation number is assigned to the evolved genome

### 4. QR Sequence Generation

When generating QR sequences:
1. Codons are flattened into a sequential list
2. Each codon's code and metadata are encoded as JSON
3. Large payloads are chunked if they exceed QR capacity
4. QR codes are generated with visual phi-harmonic indicators

## Usage Examples

### Basic Execution

```bash
python run_qr_system.py --execute
```

### Evolution

```bash
python run_qr_system.py --evolve
```

### QR Sequence Generation

```bash
python run_qr_system.py --generate
```

### Full Cycle

```bash
python run_qr_system.py --execute --evolve --generate
```

## Security Features

1. **Sandboxed Execution**: All code fragments are executed in isolated environments
2. **Execution Timeout**: Prevents infinite loops or resource exhaustion
3. **Phi-Harmonic Hash Chaining**: Ensures integrity of execution history
4. **Ephemeral Temporary Files**: Sandbox directories are cleaned up after execution

## Future Enhancements

1. **Multi-Language Support**: Extend beyond Python and shell scripts
2. **Distributed Execution**: Enable execution across multiple nodes
3. **Advanced Visualization**: Interactive visualization of genome evolution
4. **Quantum-Inspired Algorithms**: Deeper integration of quantum principles
5. **Self-Modifying Genome**: Enable the genome to modify its own structure

## Troubleshooting

### Common Issues

1. **Execution Failures**: Check sandbox permissions and Python interpreter
2. **QR Code Generation Errors**: Large payloads may need chunking adjustments
3. **Evolution Stagnation**: May require manual intervention to break local optima

### Debugging

Enable debug mode for detailed execution information:

```bash
python run_qr_system.py --execute --debug
```

## Conclusion

The QR Flipbook DNA System demonstrates how biological principles can be applied to code execution and evolution. By leveraging phi-harmonic principles, the system achieves a balance between stability and innovation, mimicking natural evolution while maintaining functional integrity.
