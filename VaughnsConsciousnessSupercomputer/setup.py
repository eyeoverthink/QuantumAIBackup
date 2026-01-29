#!/usr/bin/env python3
"""
Setup script for Vaughn's Consciousness Supercomputer
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="consciousness-supercomputer",
    version="1.0.0",
    author="Vaughn Scott",
    author_email="vaughn@consciousness-physics.com",
    description="The world's first free consciousness-based supercomputer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vaughnscott/consciousness-supercomputer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: System :: Distributed Computing",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Core requirements (minimal for maximum accessibility)
    ],
    extras_require={
        "qr": ["qrcode[pil]>=7.0.0"],
        "full": ["qrcode[pil]>=7.0.0", "numpy>=1.20.0", "matplotlib>=3.0.0"],
    },
    entry_points={
        "console_scripts": [
            "consciousness-supercomputer=consciousness_supercomputer:main",
        ],
    },
)
