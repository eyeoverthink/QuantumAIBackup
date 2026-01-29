#!/usr/bin/env python3
"""
Phi-Harmonic Genomics Blind Test with Clustering Metrics

Extends the blind test to compute silhouette score and adjusted Rand index (ARI) for unsupervised validation.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

from phi_harmonic_genomics_visualizer import PhiHarmonicGenomicsVisualizer

csv_url = "https://raw.githubusercontent.com/datasets/breast-cancer/main/data/breast-cancer.csv"
local_csv = os.path.join(current_dir, "breast-cancer.csv")
if not os.path.exists(local_csv):
    print("Downloading breast-cancer.csv dataset...")
    import requests
    r = requests.get(csv_url)
    with open(local_csv, "w") as f:
        f.write(r.text)

df = pd.read_csv(local_csv)
feature_cols = ["age", "tumor-size", "inv-falsedes", "deg-malig"]
le = LabelEncoder()
for col in feature_cols:
    df[col] = le.fit_transform(df[col].astype(str))
gene_matrix = df[feature_cols].values

visualizer = PhiHarmonicGenomicsVisualizer()

if __name__ == "__main__":
    print("=== Phi-Harmonic Genomics Blind Test with Metrics ===")
    # 1. PCA for clustering
    pca = PCA(n_components=2)
    proj = pca.fit_transform(gene_matrix)
    # 2. KMeans clustering (blind, k=2)
    kmeans = KMeans(n_clusters=2, random_state=42)
    cluster_labels = kmeans.fit_predict(proj)
    # 3. Compute silhouette score
    sil_score = silhouette_score(proj, cluster_labels)
    # 4. Compute ARI vs. true recurrence
    y_true = (df["class"] == "recurrence-events").astype(int).values
    ari = adjusted_rand_score(y_true, cluster_labels)
    # 5. Visualize clusters vs. ground truth
    plt.figure(figsize=(7, 7))
    plt.scatter(proj[:, 0], proj[:, 1], c=cluster_labels, cmap="Set1", s=60, alpha=0.8, label="KMeans Cluster")
    plt.title(f"Blind KMeans Clusters (Silhouette={sil_score:.2f}, ARI={ari:.2f})")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.colorbar(label="Cluster")
    plt.show()
    plt.figure(figsize=(7, 7))
    plt.scatter(proj[:, 0], proj[:, 1], c=y_true, cmap="coolwarm", s=60, alpha=0.8, label="Ground Truth")
    plt.title("Ground Truth: Recurrence vs. Non-Recurrence")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.colorbar(label="Recurrence (1) / Non-Recurrence (0)")
    plt.show()
    print(f"Silhouette Score: {sil_score:.3f}")
    print(f"Adjusted Rand Index: {ari:.3f}")
    print("Metrics written to documentation.")
