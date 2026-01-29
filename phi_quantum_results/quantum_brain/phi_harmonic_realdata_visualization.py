#!/usr/bin/env python3
"""
Phi-Harmonic Real Data Visualization

Loads real cancer research/model data (from CSV), preprocesses it, and visualizes key features using the Enhanced Phi-Harmonic Visualizer.

- Modular: Does not modify any core files, only imports and references them.
- Data-driven: Uses real-world cancer model data for phi-harmonic, resonance, and quantum visualizations.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import numpy as np
import pandas as pd
import requests
from io import StringIO

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

from phi_harmonic_enhanced_visualizer import PhiHarmonicEnhancedVisualizer

# Download the dataset (if not present locally)
csv_url = "https://raw.githubusercontent.com/Datascience67/datasets/master/cancer.csv"
local_csv = os.path.join(current_dir, "cancer.csv")
if not os.path.exists(local_csv):
    print("Downloading cancer.csv dataset...")
    r = requests.get(csv_url)
    with open(local_csv, "w") as f:
        f.write(r.text)

# Load dataset
print("Loading cancer.csv dataset...")
df = pd.read_csv(local_csv)

# Preprocess: select relevant numeric columns and normalize
def normalize(series):
    return (series - series.min()) / (series.max() - series.min() + 1e-8)

# Example feature extraction
phi_feature = normalize(df["tumor-size"])
resonance_triplets = list(zip(normalize(df["tumor-size"]), normalize(df["inv-nodes"]), normalize(df["deg-malig"])))
quantum_state = normalize(df["tumor-size"]).values + 1j * normalize(df["inv-nodes"]).values
fib_times = list(range(len(df)))
effectiveness = normalize(df["deg-malig"]).values

# Initialize visualizer
visualizer = PhiHarmonicEnhancedVisualizer()

if __name__ == "__main__":
    print("=== Phi-Harmonic Real Data Visualization ===")
    print("1. Phi Spiral Visualization (tumor size)...")
    visualizer.plot_phi_spiral(phi_feature, title="Real Data Phi Spiral (Tumor Size)")

    print("2. Quantum Resonance Map (tumor, nodes, malignancy)...")
    visualizer.plot_resonance_map(resonance_triplets, title="Real Data Quantum Resonance Map")

    print("3. Quantum State Projection (tumor size + inv-nodes)...")
    visualizer.plot_quantum_state_projection(quantum_state, title="Real Data Quantum State Projection")

    print("4. Fibonacci Treatment Timeline (malignancy effectiveness)...")
    # For demonstration, downsample to Fibonacci indices
    fib_indices = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    fib_effectiveness = [effectiveness[i] for i in fib_indices if i < len(effectiveness)]
    visualizer.plot_fibonacci_treatment_timeline(fib_indices[:len(fib_effectiveness)], fib_effectiveness, title="Real Data Fibonacci Timeline")

    print("All real data visualizations complete.")
