#!/usr/bin/env python3
"""
Phi-Harmonic Genomics Blind Test

Performs a blind, unsupervised analysis of real breast cancer data using phi-harmonic, quantum, and hyperdimensional principles.
Compares discovered patterns to ground truth (recurrence vs. non-recurrence) for scientific validation.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

from phi_harmonic_genomics_visualizer import PhiHarmonicGenomicsVisualizer

# Download the dataset if not present
csv_url = "https://raw.githubusercontent.com/datasets/breast-cancer/main/data/breast-cancer.csv"
local_csv = os.path.join(current_dir, "breast-cancer.csv")
if not os.path.exists(local_csv):
    print("Downloading breast-cancer.csv dataset...")
    import requests
    r = requests.get(csv_url)
    with open(local_csv, "w") as f:
        f.write(r.text)

# Load dataset
df = pd.read_csv(local_csv)

# Preprocess: encode categorical features numerically for analysis
feature_cols = ["age", "tumor-size", "inv-falsedes", "deg-malig"]
le = LabelEncoder()
for col in feature_cols:
    df[col] = le.fit_transform(df[col].astype(str))

# Blind test: select features, ignore class labels during analysis
gene_matrix = df[feature_cols].values

# Run phi-harmonic visualizations
visualizer = PhiHarmonicGenomicsVisualizer()

if __name__ == "__main__":
    print("=== Phi-Harmonic Genomics Blind Test ===")
    # 1. Spiral (first sample)
    visualizer.plot_phi_spiral(gene_matrix[0], title="Blind Test: Sample 0 Spiral")
    # 2. Hyperdimensional projection (PCA)
    visualizer.plot_hyperdimensional_projection(gene_matrix, method="pca", title="Blind Test: PCA")
    # 3. Hyperdimensional projection (t-SNE)
    visualizer.plot_hyperdimensional_projection(gene_matrix, method="tsne", title="Blind Test: t-SNE")
    # 4. Resonance map
    visualizer.plot_resonance_map(gene_matrix, title="Blind Test: Resonance Map")

    # Compare to ground truth (recurrence)
    y_true = (df["class"] == "recurrence-events").astype(int).values
    # Run PCA for visualization
    pca = PCA(n_components=2)
    proj = pca.fit_transform(gene_matrix)
    plt.figure(figsize=(7, 7))
    plt.scatter(proj[:, 0], proj[:, 1], c=y_true, cmap="coolwarm", s=60, alpha=0.8)
    plt.title("Ground Truth: Recurrence vs. Non-Recurrence")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.colorbar(label="Recurrence (1) / Non-Recurrence (0)")
    plt.show()

    print("Blind test complete. Visualize and compare clustering to ground truth.")
