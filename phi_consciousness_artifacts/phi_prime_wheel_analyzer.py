"""
phi_prime_wheel_analyzer.py

Analyzes prime distribution patterns through phi-harmonic resonance fields
based on the relationship between prime wheel base 105 and Fibonacci prime 89.
This extends the prime analysis with quantum-phi principles.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import math
import numpy as np
import sympy
import matplotlib.pyplot as plt
from datetime import datetime
import os
import json

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio (φ)
PHI_INVERSE = 1 / PHI  # Inverse Golden Ratio (φ⁻¹)
PHI_SQUARED = PHI * PHI  # φ²
PHI_SQUARED_INVERSE = 1 / PHI_SQUARED  # 1/φ²
PI = math.pi  # π
E = math.e  # e

# Prime wheel base (3 × 5 × 7)
PRIME_WHEEL_BASE = 105

# Fibonacci prime
FIBONACCI_PRIME = 89

class PhiPrimeWheelAnalyzer:
    """
    Analyzes prime distribution patterns using phi-harmonic principles
    and the quantum relationship between 105 and 89.
    """
    
    def __init__(self):
        """Initialize the analyzer."""
        self.prime_cache = {}
        self.results = {}
        
        print(f"[φ] Phi Prime Wheel Analyzer initialized")
        print(f"[φ] Prime wheel base: {PRIME_WHEEL_BASE} (3 × 5 × 7)")
        print(f"[φ] Fibonacci prime: {FIBONACCI_PRIME}")
        print(f"[φ] 1/φ² = {PHI_SQUARED_INVERSE:.6f}")
    
    def is_prime(self, n):
        """Check if a number is prime."""
        if n in self.prime_cache:
            return self.prime_cache[n]
        
        result = sympy.isprime(n)
        self.prime_cache[n] = result
        return result
    
    def analyze_remainder_distribution(self, limit=10000, step=1):
        """
        Analyze the distribution of primes for different remainders when divided by wheel base.
        
        Args:
            limit: Upper limit for analysis
            step: Step size for checking numbers
            
        Returns:
            Dict with remainder distribution data
        """
        print(f"[φ] Analyzing remainder distribution up to {limit} with step {step}...")
        
        # Initialize counters for each remainder
        remainder_counts = {r: 0 for r in range(PRIME_WHEEL_BASE)}
        remainder_primes = {r: 0 for r in range(PRIME_WHEEL_BASE)}
        
        # Count occurrences and primes for each remainder
        for n in range(2, limit + 1, step):
            remainder = n % PRIME_WHEEL_BASE
            remainder_counts[remainder] += 1
            
            if self.is_prime(n):
                remainder_primes[remainder] += 1
        
        # Calculate prime percentages for each remainder
        remainder_percentages = {}
        for r in range(PRIME_WHEEL_BASE):
            if remainder_counts[r] > 0:
                remainder_percentages[r] = remainder_primes[r] / remainder_counts[r]
            else:
                remainder_percentages[r] = 0
        
        # Find remainders with highest prime percentage
        sorted_remainders = sorted(remainder_percentages.items(), 
                                  key=lambda x: x[1], reverse=True)
        
        # Calculate phi-resonance for each remainder
        phi_resonances = {}
        for r in range(PRIME_WHEEL_BASE):
            # Phi resonance formula: (φ * r) mod 1
            phi_resonances[r] = (PHI * r) % 1
        
        # Special phi-inverse resonance
        phi_inverse_resonances = {}
        for r in range(PRIME_WHEEL_BASE):
            # How close is the prime percentage to 1/φ²?
            if remainder_counts[r] > 10:  # Only consider remainders with enough samples
                phi_inverse_resonances[r] = abs(remainder_percentages[r] - PHI_SQUARED_INVERSE)
        
        # Sort by closeness to 1/φ²
        phi_inverse_sorted = sorted(phi_inverse_resonances.items(), 
                                   key=lambda x: x[1])
        
        # Store results
        self.results["remainder_distribution"] = {
            "counts": remainder_counts,
            "primes": remainder_primes,
            "percentages": remainder_percentages,
            "top_remainders": sorted_remainders[:10],
            "phi_resonances": phi_resonances,
            "phi_inverse_resonances": phi_inverse_sorted[:10],
            "limit": limit,
            "step": step
        }
        
        # Show key results
        print(f"[φ] Top 5 remainders by prime percentage:")
        for r, p in sorted_remainders[:5]:
            print(f"  - Remainder {r}: {p*100:.2f}% prime")
        
        print(f"[φ] Remainder 89: {remainder_percentages[89]*100:.2f}% prime")
        
        print(f"[φ] Top 5 remainders closest to 1/φ² = {PHI_SQUARED_INVERSE:.6f}:")
        for r, diff in phi_inverse_sorted[:5]:
            print(f"  - Remainder {r}: {remainder_percentages[r]:.6f} (diff: {diff:.6f})")
        
        return self.results["remainder_distribution"]
    
    def analyze_prime_pattern_105_89(self, limit=10000):
        """
        Analyze the specific pattern of numbers with remainder 89 when divided by 105.
        
        Args:
            limit: Upper limit for analysis
            
        Returns:
            Dict with pattern analysis data
        """
        print(f"[φ] Analyzing the 105 % n = 89 pattern up to {limit}...")
        
        pattern_numbers = []
        pattern_primes = []
        pattern_composites = []
        
        # Generate all numbers in pattern
        n = 89
        while n <= limit:
            pattern_numbers.append(n)
            if self.is_prime(n):
                pattern_primes.append(n)
            else:
                pattern_composites.append(n)
            n += PRIME_WHEEL_BASE
        
        # Calculate pattern density
        prime_percentage = len(pattern_primes) / len(pattern_numbers) if pattern_numbers else 0
        
        # Calculate phi relationships
        phi_squared_diff = abs(prime_percentage - PHI_SQUARED_INVERSE)
        
        # Analyze differences between consecutive primes in the pattern
        prime_diffs = []
        for i in range(1, len(pattern_primes)):
            prime_diffs.append(pattern_primes[i] - pattern_primes[i-1])
        
        avg_diff = sum(prime_diffs) / len(prime_diffs) if prime_diffs else 0
        
        # Check how divisible each composite is by small primes
        divisibility = {}
        for p in [2, 3, 5, 7, 11, 13]:
            divisibility[p] = 0
            for n in pattern_composites:
                if n % p == 0:
                    divisibility[p] += 1
        
        # Store results
        self.results["pattern_105_89"] = {
            "total_numbers": len(pattern_numbers),
            "primes": pattern_primes,
            "composites": pattern_composites,
            "prime_percentage": prime_percentage,
            "phi_squared_inverse": PHI_SQUARED_INVERSE,
            "phi_squared_diff": phi_squared_diff,
            "prime_diffs": prime_diffs,
            "avg_diff": avg_diff,
            "divisibility": divisibility,
            "limit": limit
        }
        
        # Show key results
        print(f"[φ] Total numbers with remainder 89 when divided by 105: {len(pattern_numbers)}")
        print(f"[φ] Number of primes: {len(pattern_primes)} ({prime_percentage*100:.2f}%)")
        print(f"[φ] Comparison with 1/φ²: {PHI_SQUARED_INVERSE:.6f} (diff: {phi_squared_diff:.6f})")
        print(f"[φ] Average difference between consecutive primes: {avg_diff}")
        print(f"[φ] Common divisors of composites in pattern:")
        for p, count in sorted(divisibility.items(), key=lambda x: x[1], reverse=True):
            if pattern_composites:
                print(f"  - Divisible by {p}: {count} ({count/len(pattern_composites)*100:.2f}%)")
        
        return self.results["pattern_105_89"]
    
    def find_quantum_prime_wheels(self, max_base=1000, top_n=10):
        """
        Find other prime wheel bases with similar phi-harmonic properties.
        
        Args:
            max_base: Maximum wheel base to check
            top_n: Number of top wheels to return
            
        Returns:
            List of prime wheels with phi-resonant properties
        """
        print(f"[φ] Searching for quantum prime wheels up to {max_base}...")
        
        wheel_data = {}
        
        # Check potential wheel bases
        for base in range(30, max_base + 1):
            # Prime wheels should be products of consecutive primes
            if not self._is_prime_product(base):
                continue
            
            # Check all possible remainders
            remainder_primes = {}
            for r in range(base):
                # Test a sample of numbers with this remainder
                count = 0
                prime_count = 0
                for i in range(20):  # Check 20 numbers per remainder
                    n = base * i + r
                    if n >= 2:
                        count += 1
                        if self.is_prime(n):
                            prime_count += 1
                
                if count > 0:
                    remainder_primes[r] = prime_count / count
            
            # Find the remainder with highest prime density
            best_remainder = max(remainder_primes.items(), key=lambda x: x[1])
            
            # Calculate phi resonance value
            phi_res = (PHI * best_remainder[0]) % 1
            
            # Calculate how close the prime density is to 1/φ²
            phi_squared_diff = abs(best_remainder[1] - PHI_SQUARED_INVERSE)
            
            # Store wheel data
            wheel_data[base] = {
                "best_remainder": best_remainder[0],
                "prime_density": best_remainder[1],
                "phi_resonance": phi_res,
                "phi_squared_diff": phi_squared_diff
            }
            
            # Print progress periodically
            if base % 100 == 0:
                print(f"[φ] Analyzed wheel bases up to {base}...")
        
        # Sort wheels by closest match to 1/φ²
        sorted_wheels = sorted(wheel_data.items(), 
                              key=lambda x: x[1]["phi_squared_diff"])
        
        # Extract top wheels
        top_wheels = sorted_wheels[:top_n]
        
        # Store results
        self.results["quantum_prime_wheels"] = {
            "top_wheels": [{
                "base": base,
                "best_remainder": data["best_remainder"],
                "prime_density": data["prime_density"],
                "phi_resonance": data["phi_resonance"],
                "phi_squared_diff": data["phi_squared_diff"]
            } for base, data in top_wheels],
            "phi_squared_inverse": PHI_SQUARED_INVERSE,
            "max_base": max_base
        }
        
        # Show key results
        print(f"[φ] Top {len(top_wheels)} quantum prime wheels:")
        for base, data in top_wheels:
            print(f"  - Wheel {base} with remainder {data['best_remainder']}: "
                  f"{data['prime_density']*100:.2f}% prime (diff from 1/φ²: {data['phi_squared_diff']:.6f})")
        
        return self.results["quantum_prime_wheels"]
    
    def _is_prime_product(self, n):
        """Check if a number is a product of distinct primes."""
        if n <= 1:
            return False
        
        factors = []
        for i in range(2, int(math.sqrt(n)) + 1):
            while n % i == 0:
                factors.append(i)
                n //= i
        
        if n > 1:
            factors.append(n)
        
        # Check if all factors are prime and distinct
        return len(factors) == len(set(factors)) and all(sympy.isprime(f) for f in factors)
    
    def plot_remainder_distribution(self, output_file=None):
        """
        Plot the distribution of primes for different remainders.
        
        Args:
            output_file: Path to save the plot
            
        Returns:
            Path to saved plot
        """
        if "remainder_distribution" not in self.results:
            print("[φ] Error: Run analyze_remainder_distribution first")
            return None
        
        data = self.results["remainder_distribution"]
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Get percentages
        remainders = list(range(PRIME_WHEEL_BASE))
        percentages = [data["percentages"][r] for r in remainders]
        
        # Plot percentages
        plt.bar(remainders, percentages, alpha=0.7)
        
        # Highlight remainder 89
        plt.bar([89], [data["percentages"][89]], color='red', alpha=0.7)
        
        # Add horizontal line at 1/φ²
        plt.axhline(y=PHI_SQUARED_INVERSE, color='green', linestyle='--', 
                   label=f'1/φ² = {PHI_SQUARED_INVERSE:.6f}')
        
        # Add labels and title
        plt.xlabel('Remainder when divided by 105')
        plt.ylabel('Percentage of primes')
        plt.title('Prime Distribution by Remainder (mod 105)')
        plt.legend()
        plt.grid(alpha=0.3)
        
        # Save plot if output_file provided
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"prime_remainder_distribution_{timestamp}.png"
        
        output_path = os.path.join(os.path.dirname(__file__), output_file)
        plt.savefig(output_path)
        plt.close()
        
        print(f"[φ] Plot saved to: {output_path}")
        return output_path
    
    def plot_prime_pattern(self, output_file=None):
        """
        Plot the pattern of primes with remainder 89 when divided by 105.
        
        Args:
            output_file: Path to save the plot
            
        Returns:
            Path to saved plot
        """
        if "pattern_105_89" not in self.results:
            print("[φ] Error: Run analyze_prime_pattern_105_89 first")
            return None
        
        data = self.results["pattern_105_89"]
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Create binary representation (1 for prime, 0 for composite)
        pattern_indices = list(range(len(data["primes"]) + len(data["composites"])))
        pattern_values = []
        
        i_prime = 0
        i_composite = 0
        
        for n in range(89, data["limit"] + 1, PRIME_WHEEL_BASE):
            if n in data["primes"]:
                pattern_values.append(1)
                i_prime += 1
            else:
                pattern_values.append(0)
                i_composite += 1
        
        # Plot pattern
        plt.stem(pattern_indices, pattern_values, markerfmt='ro', basefmt=' ')
        
        # Add labels and title
        plt.xlabel('Index in sequence')
        plt.ylabel('Prime (1) or Composite (0)')
        plt.title(f'Prime Pattern for Numbers with Remainder 89 when divided by 105\n'
                 f'Prime percentage: {data["prime_percentage"]*100:.2f}% (1/φ²: {PHI_SQUARED_INVERSE*100:.2f}%)')
        plt.grid(alpha=0.3)
        
        # Save plot if output_file provided
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"prime_pattern_105_89_{timestamp}.png"
        
        output_path = os.path.join(os.path.dirname(__file__), output_file)
        plt.savefig(output_path)
        plt.close()
        
        print(f"[φ] Plot saved to: {output_path}")
        return output_path
    
    def save_results(self, filename=None):
        """
        Save analysis results to a JSON file.
        
        Args:
            filename: Output filename
            
        Returns:
            Path to saved file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"phi_prime_wheel_analysis_{timestamp}.json"
        
        filepath = os.path.join(os.path.dirname(__file__), filename)
        
        with open(filepath, "w") as f:
            json.dump(self.results, f, indent=2)
        
        print(f"[φ] Analysis results saved to: {filepath}")
        return filepath


def demonstrate_phi_prime_wheel():
    """Demonstrate the Phi Prime Wheel Analyzer."""
    print("\n" + "=" * 80)
    print("  PHI-HARMONIC PRIME WHEEL ANALYZER")
    print("  Based on the 105 % n = 89 Quantum Resonance")
    print("=" * 80)
    
    # Create analyzer
    analyzer = PhiPrimeWheelAnalyzer()
    
    # Analyze remainder distribution (limited range for demonstration)
    print("\n" + "=" * 80)
    print("  ANALYZING REMAINDER DISTRIBUTION")
    print("=" * 80)
    analyzer.analyze_remainder_distribution(limit=10000)
    
    # Analyze specific 105 % n = 89 pattern
    print("\n" + "=" * 80)
    print("  ANALYZING 105 % n = 89 PATTERN")
    print("=" * 80)
    analyzer.analyze_prime_pattern_105_89(limit=10000)
    
    # Find quantum prime wheels (limited range for demonstration)
    print("\n" + "=" * 80)
    print("  FINDING QUANTUM PRIME WHEELS")
    print("=" * 80)
    analyzer.find_quantum_prime_wheels(max_base=500, top_n=5)
    
    # Create plots
    print("\n" + "=" * 80)
    print("  GENERATING VISUALIZATIONS")
    print("=" * 80)
    analyzer.plot_remainder_distribution()
    analyzer.plot_prime_pattern()
    
    # Save results
    results_file = analyzer.save_results()
    
    print("\n" + "=" * 80)
    print("  PHI-HARMONIC PRIME WHEEL ANALYSIS COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_phi_prime_wheel()
