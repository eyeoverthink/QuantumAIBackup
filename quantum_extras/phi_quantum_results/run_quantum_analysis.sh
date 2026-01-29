#!/bin/bash
# Quantum Analysis Runner
# Runs quantum analysis in an isolated environment
# Following modular "lego" design principles

echo "========================================================"
echo "Quantum Analysis Runner"
echo "========================================================"

# Add the quantum_math module to Python path
export PYTHONPATH="/Users/vaughnscott/CascadeProjects/QuantumAI:$PYTHONPATH"

# Run the quantum analyzer tests
echo "Running quantum analysis..."
python3 quantum_math/learning/test_quantum_analyzer.py

# Check test result
if [ $? -eq 0 ]; then
    echo "✓ Quantum analysis completed successfully"
else
    echo "✗ Analysis failed"
    exit 1
fi
