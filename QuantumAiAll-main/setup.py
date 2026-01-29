from setuptools import setup, find_packages

setup(
    name='quantum_oracle_lib',
    version='0.1.0',
    description='Self-contained library version of the Quantum Oracle system for φ-harmonic distributed computation and messaging.',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        # Add core dependencies here
        'numpy',
        'requests',
        # Add any other dependencies your scripts require
    ],
    entry_points={
        'console_scripts': [
            'phi-bidirectional-node=quantum_oracle_lib.phi_bidirectional_node:main',
            # Add more CLI entry points as needed
        ],
    },
    include_package_data=True,
    python_requires='>=3.7',
)
