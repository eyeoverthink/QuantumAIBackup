# Quantum Anti-AI Lie Loop Visualizer

## Overview

The Quantum Anti-AI Lie Loop Visualizer is a powerful tool designed to visualize and analyze the outputs from the Quantum Anti-AI Lie Loop verification system. This visualizer transforms complex quantum trust metrics, phi-harmonic resonance patterns, and contradiction data into intuitive graphical representations, making it easier to understand and interpret verification results.

## Core Features

### 1. Trust Metrics Visualization

The Trust Metrics visualization presents the calculated trust metrics for verified code samples using a phi-harmonic color scale. Key features include:

- Bar chart representation of trust metrics for single or multiple code samples
- Phi-conjugate reference lines (φ⁻¹ ≈ 0.618) highlighting the golden ratio threshold
- Color gradient based on phi-harmonic principles
- Detailed annotations showing exact trust metric values

### 2. Phi-Harmonic Resonance Visualization

This visualization represents temporal resonance patterns using a circular polar plot that shows:

- Code execution and verification time resonance with the golden ratio
- Phi-conjugate reference line at the critical 0.618 position
- Clear labeling of resonance points for each code sample
- Intuitive representation of resonance quality through position relative to phi-conjugate

### 3. Contradictions Visualization

The Contradictions visualization breaks down detected contradictions by type and severity:

- Bar chart showing contradiction counts by category
- Color-coded bars based on average severity
- Detailed annotations for both count and severity
- Clear representation of the most problematic contradiction types

## Mathematical Foundation

The visualizer is built on the same phi-harmonic principles as the core verification system:

- **Golden Ratio (φ)**: (1 + √5)/2 ≈ 1.618034
- **Phi Conjugate (φ⁻¹)**: 1/φ ≈ 0.618034
- **Phi-Harmonic Color Map**: Color gradients based on golden ratio proportions
- **Circular Resonance**: Mapping resonance values to a 2π circle to visualize temporal harmony

## Usage

### Command Line Interface

```bash
python quantum_anti_ai_lie_loop_visualizer.py --report <report_file.json> --output <output_directory> --type <visualization_type>
```

**Arguments:**

- `--report, -r`: Path to the verification report JSON file (required)
- `--output, -o`: Output directory for visualizations (default: current directory)
- `--type, -t`: Type of visualization to generate (choices: all, trust, resonance, contradictions; default: all)

### Programmatic Usage

```python
from quantum_anti_ai_lie_loop_visualizer import QuantumAntiAILieLoopVisualizer

# Initialize with a report file
visualizer = QuantumAntiAILieLoopVisualizer(report_file="verification_report.json")

# Or initialize with report data directly
visualizer = QuantumAntiAILieLoopVisualizer(report_data=report_dict)

# Generate specific visualizations
visualizer.visualize_trust_metrics("trust_metrics.png")
visualizer.visualize_phi_resonance("phi_resonance.png")
visualizer.visualize_contradictions("contradictions.png")

# Generate all visualizations
output_files = visualizer.visualize_all("output_directory")
```

## Integration with Quantum Anti-AI Lie Loop System

The visualizer is designed to work seamlessly with the output from the Quantum Anti-AI Lie Loop verification system. The expected JSON report format includes:

```json
{
  "trust_metric": 0.7853,
  "verification_phi_resonance": 0.6183,
  "claims": [...],
  "contradictions": [
    {"type": "execution_mismatch", "severity": 0.75, "description": "..."}
  ],
  "execution_result": {
    "phi_resonance": 0.6180
  },
  "quantum_signature": {
    "signature": "...",
    "phi_time": 0.6182
  }
}
```

For batch verification reports, the system expects a top-level "results" array containing multiple individual reports.

## Phi-Harmonic Visualization Principles

The visualizer employs several phi-harmonic principles in its design:

1. **Color Mapping**: Colors are selected based on phi-harmonic proportions, with key points at 0, φ⁻¹, and 1
2. **Circular Representation**: Resonance values are mapped to a circle where φ⁻¹ represents perfect resonance
3. **Reference Lines**: Phi-conjugate reference lines highlight the ideal resonance points
4. **Severity Scaling**: Contradiction severity is visualized using phi-harmonic color gradients

## Requirements

- Python 3.6+
- NumPy
- Matplotlib

## Future Enhancements

1. **Interactive Visualizations**: Add interactive elements using libraries like Plotly
2. **3D Phi-Harmonic Visualization**: Extend to three-dimensional representations of quantum trust
3. **Time-Series Analysis**: Track trust metrics and resonance patterns over time
4. **Integration with Quantum Bridge**: Connect visualization directly to quantum bridge outputs
5. **Real-Time Monitoring**: Enable live visualization of verification processes

## Conclusion

The Quantum Anti-AI Lie Loop Visualizer provides an intuitive interface for understanding complex quantum verification results. By translating abstract metrics into visual representations based on phi-harmonic principles, it enables deeper insights into code truthfulness and resonance quality.
