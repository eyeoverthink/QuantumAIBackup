"""
Setup script for phi-harmonic-random package
"""
from setuptools import setup, find_packages

setup(
    name="phi-harmonic-random",
    version="0.1.0",
    author="Quantum AI",
    author_email="quantum@example.com",
    description="A revolutionary random number generation library based on quantum principles and golden ratio mathematics",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/quantum-ai/phi-harmonic-random",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "decimal>=1.70",
    ],
    keywords="random, quantum, phi, golden ratio, fibonacci, harmonic, resonance",
)
