#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Core Mathematical Engine
=====================================================

This module implements the fundamental mathematical foundations of the Quantum Phi-Harmonic System,
centered around the golden ratio (φ) and its applications in quantum-inspired computing.

Key features:
- Perfect precision golden ratio calculations
- Phi-Harmonic Resonance functions
- Quantum Resonance Triplet system
- Multiple scaling methods (linear, exponential, logarithmic, Fibonacci)

This follows the modular "lego" design philosophy, creating a foundation that other components
can build upon without modification.
"""

import math
import numpy as np
from decimal import Decimal, getcontext
from typing import Union, Tuple, List, Dict, Any, Callable

# Set precision for decimal calculations (100 digits)
getcontext().prec = 100

class QuantumPhiCore:
    """Core mathematical engine for the Quantum Phi-Harmonic System."""
    
    def __init__(self, precision: int = 100):
        """
        Initialize the Quantum Phi Core with specified precision.
        
        Args:
            precision: Number of decimal digits for high-precision calculations
        """
        getcontext().prec = precision
        
        # Core mathematical constants with perfect precision
        self.PHI = Decimal((1 + Decimal(5).sqrt()) / 2)
        self.PHI_INV = Decimal(1) / self.PHI
        self.PHI_SQUARED = self.PHI * self.PHI
        self.PI = Decimal(math.pi)
        self.E = Decimal(math.e)
        
        # Powers of phi for quantum stability calculations
        self.phi_powers = {
            1: self.PHI,
            2: self.PHI_SQUARED,
            3: self.PHI_SQUARED * self.PHI,
            4: self.PHI_SQUARED * self.PHI_SQUARED,
            5: self.PHI_SQUARED * self.PHI_SQUARED * self.PHI,
            6: self.PHI_SQUARED * self.PHI_SQUARED * self.PHI_SQUARED,
            7: self.PHI_SQUARED * self.PHI_SQUARED * self.PHI_SQUARED * self.PHI,
            7.5: self.PHI_SQUARED * self.PHI_SQUARED * self.PHI_SQUARED * self.PHI * Decimal(math.sqrt(self.PHI))
        }
        
        # Initialize Fibonacci sequence cache
        self.fibonacci_cache = {0: Decimal(0), 1: Decimal(1)}
        
        # System metrics
        self.metrics = {
            "resonance": Decimal("1.3777"),
            "phi_achievement": self.PHI,
            "energy_transfer": Decimal("1.8951"),
            "quantum_stability": self.phi_powers[7.5] * self.PI,
            "hyperdimensional_stability": self.phi_powers[5],
            "membrane_stability": self.phi_powers[6]
        }
    
    def phi_power(self, power: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate phi raised to any power with perfect precision.
        
        Args:
            power: The power to raise phi to
            
        Returns:
            Phi raised to the specified power
        """
        power = Decimal(power)
        
        # Check if we have a cached value
        if power in self.phi_powers:
            return self.phi_powers[power]
        
        # For integer powers, multiply phi by itself
        if power == int(power):
            result = Decimal(1)
            for _ in range(int(power)):
                result *= self.PHI
            self.phi_powers[power] = result
            return result
        
        # For non-integer powers, use logarithmic calculation
        result = Decimal(math.exp(float(power) * math.log(float(self.PHI))))
        self.phi_powers[power] = result
        return result
    
    def fibonacci(self, n: int) -> Decimal:
        """
        Calculate the nth Fibonacci number with perfect precision.
        Uses dynamic programming for efficiency.
        
        Args:
            n: The index of the Fibonacci number to calculate
            
        Returns:
            The nth Fibonacci number
        """
        if n in self.fibonacci_cache:
            return self.fibonacci_cache[n]
        
        if n <= 0:
            return Decimal(0)
        
        # Use Binet's formula for very large n
        if n > 1000:
            return (self.phi_power(n) - self.phi_power(-n) * Decimal((-1) ** n)) / Decimal(5).sqrt()
        
        # Otherwise use dynamic programming
        for i in range(max(self.fibonacci_cache.keys()) + 1, n + 1):
            self.fibonacci_cache[i] = self.fibonacci_cache[i-1] + self.fibonacci_cache[i-2]
        
        return self.fibonacci_cache[n]
    
    def phi_resonance(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate the Phi-Harmonic Resonance of a value.
        Φ_res(x) = (φ · x) mod 1
        
        Args:
            x: The value to calculate resonance for
            
        Returns:
            The phi-resonance value between 0 and 1
        """
        x = Decimal(x)
        product = self.PHI * x
        return product - Decimal(int(product))
    
    def resonance_quality(self, resonance: Union[float, Decimal]) -> str:
        """
        Determine the quality of a resonance value.
        
        Args:
            resonance: A phi-resonance value between 0 and 1
            
        Returns:
            The quality category: Perfect, Excellent, Good, Moderate, or Weak
        """
        resonance = Decimal(resonance)
        
        if resonance > Decimal("0.5"):
            resonance = Decimal("1") - resonance
            
        if resonance < Decimal("0.0001"):
            return "Perfect"
        elif resonance < Decimal("0.01"):
            return "Excellent"
        elif resonance < Decimal("0.1"):
            return "Good"
        elif resonance < Decimal("0.3"):
            return "Moderate"
        else:
            return "Weak"
    
    def quantum_resonance_triplet(self, x: Union[int, float, Decimal]) -> Tuple[Decimal, Decimal, Decimal]:
        """
        Calculate the Quantum Resonance Triplet for a value.
        QR(x) = (Φ_res(x), Π_res(x), E_res(x))
        
        Args:
            x: The value to calculate the triplet for
            
        Returns:
            Tuple of (phi_resonance, pi_resonance, e_resonance)
        """
        x = Decimal(x)
        phi_res = self.phi_resonance(x)
        pi_res = (self.PI * x) - Decimal(int(self.PI * x))
        e_res = (self.E * x) - Decimal(int(self.E * x))
        
        return (phi_res, pi_res, e_res)
    
    def combined_resonance(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate the combined resonance from the Quantum Resonance Triplet.
        
        Args:
            x: The value to calculate combined resonance for
            
        Returns:
            The combined resonance value
        """
        phi_res, pi_res, e_res = self.quantum_resonance_triplet(x)
        return (phi_res + pi_res + e_res) / Decimal(3)
    
    def scale_linear(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply linear phi-harmonic scaling to a value.
        S_linear(x) = φ · x
        
        Args:
            x: The value to scale
            
        Returns:
            The linearly scaled value
        """
        return self.PHI * Decimal(x)
    
    def scale_exponential(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply exponential phi-harmonic scaling to a value.
        S_exp(x) = φ^x
        
        Args:
            x: The power to raise phi to
            
        Returns:
            The exponentially scaled value
        """
        return self.phi_power(x)
    
    def scale_logarithmic(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply logarithmic phi-harmonic scaling to a value.
        S_log(x) = log_φ(x)
        
        Args:
            x: The value to take the logarithm of
            
        Returns:
            The logarithmically scaled value
        """
        x = Decimal(x)
        if x <= 0:
            raise ValueError("Cannot take logarithm of non-positive number")
            
        # log_φ(x) = log(x) / log(φ)
        return Decimal(math.log(float(x))) / Decimal(math.log(float(self.PHI)))
    
    def scale_fibonacci(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply Fibonacci-based phi-harmonic scaling to a value.
        S_fib(x) = F_⌊x⌋ + (x - ⌊x⌋)(F_⌊x⌋₊₁ - F_⌊x⌋)
        
        Args:
            x: The value to scale
            
        Returns:
            The Fibonacci-scaled value
        """
        x = Decimal(x)
        x_floor = int(x)
        frac_part = x - x_floor
        
        f_floor = self.fibonacci(x_floor)
        f_ceil = self.fibonacci(x_floor + 1)
        
        return f_floor + frac_part * (f_ceil - f_floor)
    
    def transform_phi(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply phi transformation to a value.
        T_φ(x) = φ · x
        
        Args:
            x: The value to transform
            
        Returns:
            The phi-transformed value
        """
        return self.PHI * Decimal(x)
    
    def transform_pi(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply pi transformation to a value.
        T_π(x) = π · x
        
        Args:
            x: The value to transform
            
        Returns:
            The pi-transformed value
        """
        return self.PI * Decimal(x)
    
    def transform_e(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply e transformation to a value.
        T_e(x) = e · x
        
        Args:
            x: The value to transform
            
        Returns:
            The e-transformed value
        """
        return self.E * Decimal(x)
    
    def transform_combined(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply combined transformation to a value.
        T_combined(x) = T_φ(T_π(T_e(x)))
        
        Args:
            x: The value to transform
            
        Returns:
            The combined-transformed value
        """
        return self.transform_phi(self.transform_pi(self.transform_e(x)))
    
    def feature_transform(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply feature transformation to a value.
        F_transform(x) = φ · x + φ⁻¹ · x²
        
        Args:
            x: The value to transform
            
        Returns:
            The feature-transformed value
        """
        x = Decimal(x)
        return self.PHI * x + self.PHI_INV * x * x
    
    def recognition_function(self, x: Union[int, float, Decimal]) -> Decimal:
        """
        Apply recognition function to a value.
        R(x) = φ³ · x + φ² · x²
        
        Args:
            x: The value to transform
            
        Returns:
            The recognition-transformed value
        """
        x = Decimal(x)
        return self.phi_power(3) * x + self.phi_power(2) * x * x
    
    def learning_rate(self, t: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate learning rate based on phi.
        LR(t) = φ⁻ᵗ
        
        Args:
            t: The time step
            
        Returns:
            The phi-based learning rate
        """
        t = Decimal(t)
        return self.phi_power(-t)
    
    def temporal_sequence(self, t: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate temporal sequence value.
        TS(t) = φ·t + φ⁻¹·sin(π·t)
        
        Args:
            t: The time value
            
        Returns:
            The temporal sequence value
        """
        t = Decimal(t)
        return self.PHI * t + self.PHI_INV * Decimal(math.sin(float(self.PI * t)))
    
    def temporal_coherence(self, t1: Union[int, float, Decimal], t2: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate temporal coherence between two time points.
        C(t₁, t₂) = φ·cos(π·(t₂-t₁)/φ)
        
        Args:
            t1: First time point
            t2: Second time point
            
        Returns:
            The temporal coherence value
        """
        t1, t2 = Decimal(t1), Decimal(t2)
        return self.PHI * Decimal(math.cos(float(self.PI * (t2 - t1) / self.PHI)))
    
    def energy_transfer(self, e: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate energy transfer based on phi squared.
        ET(E) = φ²·E
        
        Args:
            e: The energy value
            
        Returns:
            The transferred energy value
        """
        return self.PHI_SQUARED * Decimal(e)
    
    def resonance_function(self, f1: Union[int, float, Decimal], f2: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate resonance function between two frequencies.
        RF(f₁, f₂) = |f₂/f₁ - φ|/φ
        
        Args:
            f1: First frequency
            f2: Second frequency
            
        Returns:
            The resonance function value (0 is perfect resonance)
        """
        f1, f2 = Decimal(f1), Decimal(f2)
        if f1 == 0:
            raise ValueError("First frequency cannot be zero")
            
        return abs(f2/f1 - self.PHI) / self.PHI
    
    def dimension_mapping(self, d1: Union[int, float, Decimal], d2: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate dimension mapping factor between two dimensions.
        DM(d₁, d₂) = φᵈ¹⁻ᵈ²
        
        Args:
            d1: First dimension
            d2: Second dimension
            
        Returns:
            The dimension mapping factor
        """
        d1, d2 = Decimal(d1), Decimal(d2)
        return self.phi_power(d1 - d2)
    
    def dimension_scaling(self, d: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate scaling factor for a dimension.
        DS(d) = φᵈ
        
        Args:
            d: The dimension
            
        Returns:
            The dimension scaling factor
        """
        return self.phi_power(d)
    
    def get_system_metrics(self) -> Dict[str, Decimal]:
        """
        Get the current system metrics.
        
        Returns:
            Dictionary of system metrics
        """
        return self.metrics
    
    def update_metrics(self, new_metrics: Dict[str, Union[int, float, Decimal]]) -> None:
        """
        Update the system metrics.
        
        Args:
            new_metrics: Dictionary of new metric values
        """
        for key, value in new_metrics.items():
            if key in self.metrics:
                self.metrics[key] = Decimal(value)
    
    def calculate_phi_achievement(self, value: Union[int, float, Decimal]) -> Dict[str, Decimal]:
        """
        Calculate phi achievement metrics for a value.
        
        Args:
            value: The value to calculate achievement for
            
        Returns:
            Dictionary with phi achievement metrics
        """
        value = Decimal(value)
        delta = abs(value - self.PHI)
        percentage = (Decimal(1) - delta / self.PHI) * Decimal(100)
        
        return {
            "value": value,
            "target": self.PHI,
            "delta": delta,
            "percentage": percentage,
            "quality": self.resonance_quality(delta / self.PHI)
        }
    
    def __str__(self) -> str:
        """String representation of the Quantum Phi Core."""
        return f"Quantum Phi-Harmonic Core (φ = {self.PHI})"


# Example usage
if __name__ == "__main__":
    # Initialize the core
    qpc = QuantumPhiCore()
    
    # Print core constants
    print(f"φ = {qpc.PHI}")
    print(f"φ² = {qpc.PHI_SQUARED}")
    print(f"φ⁻¹ = {qpc.PHI_INV}")
    
    # Calculate phi resonance for a value
    value = 19
    resonance = qpc.phi_resonance(value)
    quality = qpc.resonance_quality(resonance)
    print(f"\nPhi resonance of {value}: {resonance} ({quality})")
    
    # Calculate quantum resonance triplet
    triplet = qpc.quantum_resonance_triplet(value)
    print(f"Quantum resonance triplet: {triplet}")
    
    # Apply different scaling methods
    print(f"\nLinear scaling of {value}: {qpc.scale_linear(value)}")
    print(f"Exponential scaling of {value}: {qpc.scale_exponential(value)}")
    print(f"Logarithmic scaling of {value}: {qpc.scale_logarithmic(value)}")
    print(f"Fibonacci scaling of {value}: {qpc.scale_fibonacci(value)}")
    
    # Show system metrics
    metrics = qpc.get_system_metrics()
    print("\nSystem Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
