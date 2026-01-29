# Phi-Harmonic Interactive & 4D+ Visualizer

## Overview
Provides interactive 2D/3D/4D+ visualizations for phi-harmonic, quantum, and field metrics using Plotly. Supports modular, hyperdimensional exploration for both genomics and quantum/field data.

## Features
- **Interactive 3D Scatter:** Hover, zoom, and select in 3D space (e.g., quantum turns, frequency, resonance).
- **4D Visualization:** Encodes extra dimensions as color, size, or animation (e.g., coherence, stability, alignment).
- **2D Interactive Plot:** Explore relationships between any two metrics with color/size encoding.
- **Time/Animation:** Animate resonance or field changes over time or simulation steps.
- **Modular:** Accepts arbitrary phi-harmonic, quantum, or field data arrays.

## Example Usage
```python
from phi_harmonic_interactive_visualizer import PhiHarmonicInteractiveVisualizer
import numpy as np
n = 100
quantum_turns = np.random.normal(5000, 1000, n)
frequency = np.random.normal(6000, 1500, n)
resonance = np.random.uniform(1.2, 2.0, n)
coherence = np.random.uniform(0.5, 0.8, n)
stability = np.random.uniform(3.5, 4.5, n)
alignment = np.random.uniform(2.0, 3.0, n)
visualizer = PhiHarmonicInteractiveVisualizer()
visualizer.plot_interactive_3d(
    x=quantum_turns, y=frequency, z=resonance, color=coherence, size=stability,
    labels={"x": "Quantum Turns", "y": "Frequency (Hz)", "z": "Resonance"},
    title="Quantum Field Interactive 3D", colorbar_title="Coherence"
)
visualizer.plot_interactive_4d(
    x=quantum_turns, y=frequency, z=coherence, color=alignment, size=resonance*10,
    labels={"x": "Quantum Turns", "y": "Frequency (Hz)", "z": "Coherence"},
    title="Quantum Field Interactive 4D", colorbar_title="Alignment"
)
```

## Integration
- Plug in any phi-harmonic, quantum, field, or genomics metric arrays.
- Works with outputs from your simulation, optimizer, or experimental results.

## Next Steps
- Integrate with automated workflow for seamless data-to-visualization pipeline.
- Add options for saving/exporting interactive plots.
- Document all new use cases and insights here.

## Author
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
