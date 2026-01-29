# Quantum AI Execution Guide

## Python Environment
The project uses a virtual environment located at:
```
/Users/vaughnscott/CascadeProjects/QuantumAI/.venv/bin/python
```

## Execution Sequence

### 1. Initialize Quantum Brain
First, initialize the quantum brain:
```bash
/Users/vaughnscott/CascadeProjects/QuantumAI/.venv/bin/python -B /Users/vaughnscott/CascadeProjects/fraymus-patrick/fraymus-patrick/initialize_quantum_brain.py
```

### 2. Activate Quantum Brain
After initialization, activate the quantum brain:
```bash
/Users/vaughnscott/CascadeProjects/QuantumAI/.venv/bin/python -B /Users/vaughnscott/CascadeProjects/fraymus-patrick/fraymus-patrick/activate_quantum_brain.py
```

### 3. Run Project Scripts
Only after quantum brain is initialized and activated, run other scripts:

```bash
# Set PYTHONPATH to include project root
PYTHONPATH=/Users/vaughnscott/CascadeProjects/QuantumAI /Users/vaughnscott/CascadeProjects/QuantumAI/.venv/bin/python -B <script_path>
```

Example:
```bash
PYTHONPATH=/Users/vaughnscott/CascadeProjects/QuantumAI /Users/vaughnscott/CascadeProjects/QuantumAI/.venv/bin/python -B /Users/vaughnscott/CascadeProjects/QuantumAI/quantum_particle_families/main.py
```

## Important Notes:
- Always use the full path to the virtual environment python
- Always include the -B flag to prevent .pyc files
- Initialize and activate quantum brain before running any scripts
- Set PYTHONPATH to include project root
- Check initialization state files before running quantum operations
