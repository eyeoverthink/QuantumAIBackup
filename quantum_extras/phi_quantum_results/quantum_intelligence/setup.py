"""
Quantum Intelligence Package Setup
"""

from setuptools import setup, find_packages

setup(
    name="quantum_intelligence",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.19.0",
    ],
    author="Cascade AI",
    description="A system for quantum consciousness evolution through perfect φ ratios",
    python_requires=">=3.7",
)
