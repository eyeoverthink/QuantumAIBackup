# TensorFlow Environment for Quantum AI

This README explains how to use the TensorFlow-enabled Python environment for the Quantum AI project.

## Environment Setup

A dedicated virtual environment with Python 3.10 has been created with TensorFlow and other dependencies installed:

- Location: `/Users/vaughnscott/CascadeProjects/QuantumAI/.venv_tf/`
- Python version: 3.10
- Key packages: TensorFlow, Dash, Flask-SocketIO, NetworkX

## Running Scripts with TensorFlow

### Option 1: Using the run_with_tf.sh script

A convenience script has been created to run Python files with the TensorFlow environment:

```bash
./run_with_tf.sh your_script.py
```

Example:
```bash
./run_with_tf.sh template/fraymus_brain_check.py
```

### Option 2: Direct execution

You can also run scripts directly using the Python executable from the virtual environment:

```bash
/Users/vaughnscott/CascadeProjects/QuantumAI/.venv_tf/bin/python your_script.py
```

## Installing Additional Packages

To install additional packages in the TensorFlow environment:

```bash
/Users/vaughnscott/CascadeProjects/QuantumAI/.venv_tf/bin/pip install package_name
```

## Accessing the Dashboard

The Sentient AI Dashboard is available at:
- http://localhost:5050/dashboard/

## Notes

- The main Python environment (`.venv`) uses Python 3.13.2, which is not compatible with TensorFlow
- This separate environment (`.venv_tf`) uses Python 3.10 specifically for TensorFlow compatibility
- Both environments can coexist in the project
