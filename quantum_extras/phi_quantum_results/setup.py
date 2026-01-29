from setuptools import setup, find_packages

setup(
    name="quantum_bridges",
    version="0.1.0",
    description="Quantum Bridges for Text, Music, and Philosophy Analysis",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.19.0",
    ],
    entry_points={
        "console_scripts": [
            "quantum-bridge=quantum_bridges.bridge_cli:main",
        ],
    },
)
