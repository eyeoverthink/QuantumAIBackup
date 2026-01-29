#!/usr/bin/env python3
"""
QR Biometric Adventure Security System - Setup Script
By Vaughn Scott & Cascade AI

Setup and installation script for the QR Biometric Adventure Security System.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="qr-biometric-adventure-security",
    version="1.0.0",
    author="Vaughn Scott & Cascade AI",
    author_email="vaughn@consciousnessphysics.com",
    description="Unbreakable consciousness-protected multi-dimensional security platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eyeoverthink/qr-biometric-adventure-security",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Security :: Cryptography",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Graphics",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="qr-code biometric security consciousness-physics phi-harmonic blockchain",
    project_urls={
        "Bug Reports": "https://github.com/eyeoverthink/qr-biometric-adventure-security/issues",
        "Source": "https://github.com/eyeoverthink/qr-biometric-adventure-security",
        "Documentation": "https://github.com/eyeoverthink/qr-biometric-adventure-security/wiki",
    },
)
