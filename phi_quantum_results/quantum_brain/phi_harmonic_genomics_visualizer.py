#!/usr/bin/env python3
"""
Phi-Harmonic Genomics Visualizer

Visualizes high-dimensional gene expression or DNA data using phi-harmonic, quantum, and hyperdimensional principles.
- Modular: Does not modify core files; imports only as needed.
- Supports gene expression, mutation, or sequence data.
- Demonstrates spiral, resonance, and dimensionality-reduced projections.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Optional
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

class PhiHarmonicGenomicsVisualizer:
    """
    Visualizes gene expression or DNA data in phi-harmonic, quantum, and hyperdimensional forms.
    """
    def __init__(self):
        pass

    def plot_phi_spiral(self, values: np.ndarray, title: str = "Gene Expression Phi Spiral"):
        phi = (1 + 5 ** 0.5) / 2
        theta = np.linspace(0, 4 * np.pi, len(values))
        r = phi ** (theta / (2 * np.pi))
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        plt.figure(figsize=(8, 8))
        plt.scatter(x, y, c=values, cmap="viridis", s=50, alpha=0.8)
        plt.title(title)
        plt.xlabel("Phi-X")
        plt.ylabel("Phi-Y")
        plt.axis("equal")
        plt.colorbar(label="Gene Expression")
        plt.show()

    def plot_hyperdimensional_projection(self, gene_matrix: np.ndarray, method: str = "pca", title: str = "Hyperdimensional Projection"):
        if method == "pca":
            reducer = PCA(n_components=2)
        elif method == "tsne":
            reducer = TSNE(n_components=2, random_state=42)
        else:
            raise ValueError("Unknown reduction method: {}".format(method))
        proj = reducer.fit_transform(gene_matrix)
        plt.figure(figsize=(7, 7))
        plt.scatter(proj[:, 0], proj[:, 1], c=np.mean(gene_matrix, axis=1), cmap="plasma", s=50, alpha=0.8)
        plt.title(f"{title} ({method.upper()})")
        plt.xlabel("Dim 1 (phi-harmonic)")
        plt.ylabel("Dim 2 (phi-harmonic)")
        plt.grid(True)
        plt.colorbar(label="Mean Expression")
        plt.show()

    def plot_resonance_map(self, gene_matrix: np.ndarray, title: str = "Gene Quantum Resonance Map"):
        # Use first 3 principal components as phi/pi/e resonance axes
        pca = PCA(n_components=3)
        comp = pca.fit_transform(gene_matrix)
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(comp[:, 0], comp[:, 1], comp[:, 2], c=comp[:, 0], cmap="cividis", s=40, alpha=0.7)
        ax.set_xlabel("Phi Resonance (PC1)")
        ax.set_ylabel("Pi Resonance (PC2)")
        ax.set_zlabel("E Resonance (PC3)")
        ax.set_title(title)
        plt.show()

# Example usage with simulated gene expression data
if __name__ == "__main__":
    np.random.seed(42)
    # Simulate gene expression matrix: 100 samples × 50 genes
    gene_matrix = np.abs(np.random.randn(100, 50))
    visualizer = PhiHarmonicGenomicsVisualizer()
    # Plot spiral for the first sample
    visualizer.plot_phi_spiral(gene_matrix[0], title="Sample 0 Gene Expression Spiral")
    # Plot hyperdimensional projections
    visualizer.plot_hyperdimensional_projection(gene_matrix, method="pca", title="Gene PCA Projection")
    visualizer.plot_hyperdimensional_projection(gene_matrix, method="tsne", title="Gene t-SNE Projection")
    # Plot resonance map
    visualizer.plot_resonance_map(gene_matrix, title="Gene Quantum Resonance Map (PCA)")
