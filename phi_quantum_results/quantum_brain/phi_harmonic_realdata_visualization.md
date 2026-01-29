# Phi-Harmonic Real Data Visualization

## Overview
This workflow demonstrates how to load, preprocess, and visualize real-world cancer research/model data using the Enhanced Phi-Harmonic Visualizer. It is modular, non-destructive, and follows the "lego" design principle.

## Data Source
- **Dataset:** [cancer.csv](https://github.com/Datascience67/datasets/blob/master/cancer.csv)
- **Fields:** Class, age, menopause, tumor-size, inv-nodes, node-caps, deg-malig, breast, breast-quad, irradiat

## Workflow
1. **Download/Load Data:** Automatically fetches the CSV if not present locally.
2. **Preprocess:** Normalizes relevant features; extracts phi, resonance, and quantum features.
3. **Visualize:**
   - Phi Spiral: Tumor size
   - Quantum Resonance Map: Tumor size, invaded nodes, degree of malignancy
   - Quantum State Projection: Tumor size + invaded nodes
   - Fibonacci Timeline: Degree of malignancy (downsampled to Fibonacci indices)

## Extending the Workflow
- You can map any column or derived feature to phi-harmonic visualizations.
- Integrate with other real datasets by updating the CSV path and feature mapping.
- Document new mappings and results in this markdown file.

## Next Steps
- Integrate more complex datasets (e.g., genomics, time series, treatment outcomes).
- Add interactive and multi-dimensional visualizations.
- Use this workflow as a template for future real-data integrations.

## Author
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
