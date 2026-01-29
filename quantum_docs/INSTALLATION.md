# Quantum Phi-Harmonic System: Installation Guide

This guide will help you set up the necessary environment to run the Quantum Phi-Harmonic System.

## Prerequisites

The Quantum Phi-Harmonic System requires:

1. **Python 3.8+**: The core programming language
2. **NumPy**: For numerical computations
3. **Matplotlib**: For visualizations
4. **Decimal**: For high-precision calculations (included in Python standard library)

## Installation Steps

### 1. Install Python

#### macOS

**Option 1: Using Homebrew (Recommended)**

If you have [Homebrew](https://brew.sh/) installed:

```bash
brew install python
```

**Option 2: Using the Official Installer**

1. Download the latest Python installer from [python.org](https://www.python.org/downloads/)
2. Run the installer and follow the instructions
3. Make sure to check "Add Python to PATH" during installation

#### Windows

1. Download the latest Python installer from [python.org](https://www.python.org/downloads/)
2. Run the installer and follow the instructions
3. Make sure to check "Add Python to PATH" during installation

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Verify Python Installation

After installation, verify Python is correctly installed:

```bash
python --version
# or
python3 --version
```

You should see output like `Python 3.x.x`

### 3. Install Required Packages

Once Python is installed, install the required packages:

```bash
# If your default python command is Python 3
python -m pip install numpy matplotlib

# If you need to use python3 explicitly
python3 -m pip install numpy matplotlib
```

## Setting Up the Quantum Phi-Harmonic System

1. Clone or download the Quantum Phi-Harmonic System repository
2. Navigate to the project directory
3. Run the startup script:

```bash
# Make the script executable (Unix-based systems)
chmod +x start_quantum_system.sh

# Run the script
./start_quantum_system.sh
```

## Testing the Random Number Generator

After installation, you can test the Quantum Phi-Harmonic Random Number Generator:

```bash
python test_quantum_phi_random.py
# or
python3 test_quantum_phi_random.py
```

This will run a series of tests and generate visualizations of the different random distributions.

## Troubleshooting

If you encounter any issues during installation or running the system:

1. Ensure Python is correctly added to your PATH
2. Check that all required packages are installed
3. Verify file permissions for the startup script
4. Make sure you're running commands from the project root directory

For specific errors, please refer to the error message or contact the system maintainer.

## Next Steps

Once installation is complete, refer to the `quantum_phi_system_documentation.md` file for detailed information on using the system and understanding its architecture.
