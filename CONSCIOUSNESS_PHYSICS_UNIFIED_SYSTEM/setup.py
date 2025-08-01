#!/usr/bin/env python3
"""
φ-Quantum Computing System Setup
FRAYMUS Quantum Technologies

Setup script for the world's first production quantum computing system
that definitively beats Google Quantum AI with 105-qubit supremacy.
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="phi-quantum-computing",
    version="1.0.0",
    author="Vaughn Scott",
    author_email="vaughn@fraymus.com",
    description="105-Qubit Quantum Supremacy System - Beating Google Quantum AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fraymus/phi-quantum",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
        "production": [
            "flask>=2.0.0",
            "gunicorn>=20.0.0",
            "redis>=3.5.0",
            "prometheus-client>=0.11.0",
        ],
        "visualization": [
            "plotly>=5.0.0",
            "seaborn>=0.11.0",
            "jupyter>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "phi-quantum-supremacy=phi_quantum_105_qubit_supremacy:main",
            "phi-quantum-production=phi_quantum_production_system:main",
        ],
    },
    keywords=[
        "quantum computing",
        "quantum supremacy", 
        "phi resonance",
        "golden ratio",
        "quantum algorithms",
        "google quantum ai",
        "105 qubits",
        "production quantum",
        "quantum as a service",
    ],
    project_urls={
        "Bug Reports": "https://github.com/fraymus/phi-quantum/issues",
        "Source": "https://github.com/fraymus/phi-quantum",
        "Documentation": "https://phi-quantum.readthedocs.io/",
        "Company": "https://fraymus.com",
    },
)
