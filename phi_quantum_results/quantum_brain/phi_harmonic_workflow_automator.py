#!/usr/bin/env python3
"""
Phi-Harmonic Workflow Automator

Automates ingestion, analysis, visualization, and documentation for any omics/clinical/quantum/field dataset.
- Modular: Plug-and-play preprocessing, analysis, visualization, and metrics.
- Outputs all results to a new results directory and markdown summary.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import argparse
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

from phi_harmonic_genomics_visualizer import PhiHarmonicGenomicsVisualizer
from phi_harmonic_interactive_visualizer_extension import PhiHarmonicInteractiveVisualizerExtension

# --- Modular Workflow Functions ---
def preprocess_csv(file_path, feature_cols=None):
    df = pd.read_csv(file_path)
    if feature_cols is None:
        feature_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if not feature_cols:
            # Encode all columns if none are numeric
            feature_cols = df.columns.tolist()
    le = LabelEncoder()
    for col in feature_cols:
        if df[col].dtype == object:
            df[col] = le.fit_transform(df[col].astype(str))
    matrix = df[feature_cols].values
    return matrix, df

def run_analysis(matrix, df, results_dir):
    # PCA for 2D projection
    pca = PCA(n_components=2)
    proj = pca.fit_transform(matrix)
    # KMeans clustering (k=2 for demo)
    kmeans = KMeans(n_clusters=2, random_state=42)
    cluster_labels = kmeans.fit_predict(proj)
    sil_score = silhouette_score(proj, cluster_labels)
    # Try to find a binary label column for ARI
    ari = None
    y_true = None
    for col in df.columns:
        if len(set(df[col])) == 2:
            y_true = df[col].values
            ari = adjusted_rand_score(y_true, cluster_labels)
            break
    # Save metrics
    metrics = {
        "silhouette_score": sil_score,
        "adjusted_rand_index": ari,
        "binary_label_column": col if y_true is not None else None
    }
    with open(os.path.join(results_dir, "metrics.txt"), "w") as f:
        for k, v in metrics.items():
            f.write(f"{k}: {v}\n")
    return proj, cluster_labels, metrics

def run_visualizations(matrix, proj, cluster_labels, results_dir):
    # Use the headless extension to save plots as HTML files
    interactive = PhiHarmonicInteractiveVisualizerExtension(results_dir=results_dir)
    # 2D interactive
    interactive.plot_interactive_2d(
        x=proj[:,0], y=proj[:,1], color=cluster_labels,
        title="Automated Clustering: 2D PCA", colorbar_title="Cluster", filename="pca_2d.html"
    )
    # 3D/4D demo if matrix has >=3 features
    if matrix.shape[1] >= 3:
        interactive.plot_interactive_3d(
            x=matrix[:,0], y=matrix[:,1], z=matrix[:,2], color=cluster_labels,
            title="Automated Clustering: 3D", colorbar_title="Cluster", filename="cluster_3d.html"
        )

def write_documentation(results_dir, metrics, feature_cols, input_file):
    doc_path = os.path.join(results_dir, "workflow_summary.md")
    with open(doc_path, "w") as f:
        f.write(f"# Phi-Harmonic Workflow Automation Summary\n\n")
        f.write(f"**Input file:** {input_file}\n\n")
        f.write(f"**Features used:** {feature_cols}\n\n")
        f.write(f"**Metrics:**\n")
        for k, v in metrics.items():
            f.write(f"- {k}: {v}\n")
        f.write(f"\nAll plots and results saved in this directory.\n")

# --- Main CLI Entrypoint ---
def main():
    parser = argparse.ArgumentParser(description="Phi-Harmonic Workflow Automator")
    parser.add_argument("--input", required=True, help="Path to input CSV/TSV file")
    parser.add_argument("--features", nargs="*", help="List of feature columns to use")
    parser.add_argument("--results_dir", default=None, help="Directory to save results")
    args = parser.parse_args()
    # Prepare results directory
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_dir = args.results_dir or f"results_{now}"
    os.makedirs(results_dir, exist_ok=True)
    # Preprocess
    matrix, df = preprocess_csv(args.input, feature_cols=args.features)
    # Analysis
    proj, cluster_labels, metrics = run_analysis(matrix, df, results_dir)
    # Visualizations
    run_visualizations(matrix, proj, cluster_labels, results_dir)
    # Documentation
    write_documentation(results_dir, metrics, args.features or df.columns.tolist(), args.input)
    print(f"Workflow complete. Results saved to {results_dir}")

if __name__ == "__main__":
    main()
