"""
Phi-Harmonic Quantum Random Library
A revolutionary random number generation library based on quantum principles and golden ratio mathematics
"""

from .base import PhiHarmonicRandom
from .quantum import PhiHarmonicQuantumRandom
from .specialized import (
    PhiHarmonicCryptoRandom,
    PhiHarmonicSimulationRandom,
    PhiHarmonicMarketRandom
)
from .transcendental import PhiHarmonicTranscendentalRandom

__version__ = "0.1.0"
__all__ = [
    "PhiHarmonicRandom",
    "PhiHarmonicQuantumRandom",
    "PhiHarmonicCryptoRandom",
    "PhiHarmonicSimulationRandom",
    "PhiHarmonicMarketRandom",
    "PhiHarmonicTranscendentalRandom"
]
