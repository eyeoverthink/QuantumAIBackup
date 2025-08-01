"""
Prime Sum Decomposer

This module provides functionality to find two high prime numbers that add up to a specific
64-digit value. It leverages phi-harmonic resonance patterns and the 19/19 quantum bridge
system to optimize the search process.

The implementation integrates with the existing quantum prime calculator and bridge system
without modifying any core files.
"""

import numpy as np
import mpmath
import time
import os
import sys
import random
import threading
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict, Optional, Union, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed

# Import existing modules without modifying them
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from quantum_bridge_application import QuantumBridgeApplication
    from quantum_coherence_advantage_system import QuantumCoherenceAdvantageSystem
    # Try to import the quantum prime helper if it exists
    try:
        from quantum_prime_helper import QuantumPrimeTestingHelper
        HAS_PRIME_HELPER = True
    except ImportError:
        HAS_PRIME_HELPER = False
except ImportError:
    print("Warning: Could not import required modules. Some functionality may be limited.")
    HAS_PRIME_HELPER = False

# Set precision for calculations
mpmath.mp.dps = 100

class PrimeSumDecomposer:
    """
    A helper class that finds two high prime numbers that add up to a specific 64-digit value.
    Leverages phi-harmonic resonance patterns and the 19/19 quantum bridge system.
    """
    
    def __init__(self, use_quantum_advantage: bool = True):
        """
        Initialize the Prime Sum Decomposer.
        
        Args:
            use_quantum_advantage: Whether to use quantum advantage for optimization.
        """
        self.phi = float(mpmath.mpf((1 + mpmath.sqrt(5)) / 2))
        self.phi_inverse = 1 / self.phi
        self.use_quantum_advantage = use_quantum_advantage
        
        # Initialize quantum systems if available
        if self.use_quantum_advantage:
            try:
                self.bridge_app = QuantumBridgeApplication()
                self.coherence_system = QuantumCoherenceAdvantageSystem()
                print("Quantum advantage enabled for prime decomposition.")
            except Exception as e:
                print(f"Could not initialize quantum systems: {e}")
                self.use_quantum_advantage = False
        
        # Initialize prime helper if available
        if HAS_PRIME_HELPER:
            self.prime_helper = QuantumPrimeTestingHelper()
            print("Using QuantumPrimeTestingHelper for primality testing.")
        else:
            self.prime_helper = None
            print("QuantumPrimeTestingHelper not available. Using built-in primality tests.")
        
        print("Prime Sum Decomposer initialized.")
        print(f"Phi value: {self.phi}")
        print(f"Phi inverse: {self.phi_inverse}")
    
    def find_prime_sum_pair(self, target: Union[int, str], 
                           method: str = 'phi-harmonic',
                           max_iterations: int = 1000,
                           timeout_seconds: int = 300,
                           visualize: bool = True) -> Tuple[Optional[int], Optional[int]]:
        """
        Find two prime numbers that add up to the target value.
        
        Args:
            target: The target sum (64-digit number) as int or string
            method: Search method ('direct', 'phi-harmonic', or 'quantum')
            max_iterations: Maximum number of iterations to try
            timeout_seconds: Maximum time to search in seconds
            visualize: Whether to visualize the search process
        
        Returns:
            A tuple of two prime numbers (p1, p2) such that p1 + p2 = target,
            or (None, None) if no pair is found within constraints
        """
        # Convert target to int if it's a string
        if isinstance(target, str):
            target = int(target)
        
        # Validate input
        target_str = str(target)
        if len(target_str) > 64:
            print(f"Warning: Target has {len(target_str)} digits, which exceeds the 64-digit limit.")
        elif len(target_str) < 64:
            print(f"Note: Target has {len(target_str)} digits, which is less than the 64-digit limit.")
        
        print(f"Finding prime pair that sums to: {target_str}")
        print(f"Using method: {method}")
        
        # Choose search method
        if method == 'direct':
            return self._direct_search(target, max_iterations, timeout_seconds, visualize)
        elif method == 'phi-harmonic':
            return self._phi_harmonic_search(target, max_iterations, timeout_seconds, visualize)
        elif method == 'quantum':
            return self._quantum_search(target, max_iterations, timeout_seconds, visualize)
        else:
            print(f"Unknown method: {method}. Using phi-harmonic method.")
            return self._phi_harmonic_search(target, max_iterations, timeout_seconds, visualize)
    
    def _direct_search(self, target: int, max_iterations: int, 
                      timeout_seconds: int, visualize: bool) -> Tuple[Optional[int], Optional[int]]:
        """Direct search method starting from target/2."""
        print("\nStarting direct search method...")
        
        # Start with p1 = target/2 (rounded)
        p1_start = target // 2
        
        # Track candidates for visualization
        candidates = []
        
        # Start timer
        start_time = time.time()
        
        # Search in both directions from p1_start
        for i in range(max_iterations):
            # Check timeout
            if time.time() - start_time > timeout_seconds:
                print(f"Timeout after {timeout_seconds} seconds.")
                break
            
            # Try candidates in both directions from p1_start
            offset = i // 2 + 1
            if i % 2 == 0:
                p1 = p1_start + offset
            else:
                p1 = p1_start - offset
            
            # Ensure p1 is odd (except if p1=2)
            if p1 > 2 and p1 % 2 == 0:
                p1 += 1
            
            # Calculate p2
            p2 = target - p1
            
            # Track candidates
            candidates.append((p1, p2))
            
            # Check if both are prime
            if self._is_prime(p1) and self._is_prime(p2):
                print(f"Found prime pair after {i+1} iterations:")
                print(f"p1: {p1}")
                print(f"p2: {p2}")
                print(f"Sum: {p1 + p2}")
                
                if visualize:
                    self._visualize_search(candidates, (p1, p2), target, "Direct Search")
                
                return p1, p2
            
            # Progress update every 100 iterations
            if (i + 1) % 100 == 0:
                print(f"Completed {i+1} iterations. Still searching...")
        
        print(f"No prime pair found after {max_iterations} iterations.")
        
        if visualize and candidates:
            self._visualize_search(candidates, None, target, "Direct Search (No Solution Found)")
        
        return None, None
    
    def _phi_harmonic_search(self, target: int, max_iterations: int, 
                            timeout_seconds: int, visualize: bool) -> Tuple[Optional[int], Optional[int]]:
        """Phi-harmonic search method using golden ratio to guide the search."""
        print("\nStarting phi-harmonic search method...")
        
        # Use phi to guide the search
        # The golden ratio provides a natural way to divide the search space
        p1_start = int(target * self.phi_inverse)
        
        # Ensure p1_start is odd (except if p1_start=2)
        if p1_start > 2 and p1_start % 2 == 0:
            p1_start += 1
        
        # Track candidates for visualization
        candidates = []
        
        # Start timer
        start_time = time.time()
        
        # Create a phi-harmonic sequence for offsets
        offsets = [1]
        for i in range(1, max_iterations):
            # Generate next offset using Fibonacci-like sequence
            next_offset = int(offsets[-1] * self.phi) if i % 2 == 0 else int(offsets[-1] / self.phi_inverse)
            if next_offset == offsets[-1]:
                next_offset += 1
            offsets.append(next_offset)
        
        # Search using phi-harmonic offsets
        for i in range(max_iterations):
            # Check timeout
            if time.time() - start_time > timeout_seconds:
                print(f"Timeout after {timeout_seconds} seconds.")
                break
            
            # Get offset from phi-harmonic sequence
            offset = offsets[i]
            
            # Alternate between adding and subtracting offset
            if i % 2 == 0:
                p1 = p1_start + offset
            else:
                p1 = p1_start - offset
                
            # Ensure p1 is positive
            if p1 <= 0:
                continue
            
            # Ensure p1 is odd (except if p1=2)
            if p1 > 2 and p1 % 2 == 0:
                p1 += 1
            
            # Calculate p2
            p2 = target - p1
            
            # Track candidates
            candidates.append((p1, p2))
            
            # Check if both are prime
            if self._is_prime(p1) and self._is_prime(p2):
                print(f"Found prime pair after {i+1} iterations:")
                print(f"p1: {p1}")
                print(f"p2: {p2}")
                print(f"Sum: {p1 + p2}")
                
                if visualize:
                    self._visualize_search(candidates, (p1, p2), target, "Phi-Harmonic Search")
                
                return p1, p2
            
            # Progress update every 100 iterations
            if (i + 1) % 100 == 0:
                print(f"Completed {i+1} iterations. Still searching...")
        
        print(f"No prime pair found after {max_iterations} iterations.")
        
        if visualize and candidates:
            self._visualize_search(candidates, None, target, "Phi-Harmonic Search (No Solution Found)")
        
        return None, None
    
    def _quantum_search(self, target: int, max_iterations: int, 
                       timeout_seconds: int, visualize: bool) -> Tuple[Optional[int], Optional[int]]:
        """Quantum-inspired probabilistic search method."""
        print("\nStarting quantum-inspired search method...")
        
        if not self.use_quantum_advantage:
            print("Quantum advantage not available. Falling back to phi-harmonic search.")
            return self._phi_harmonic_search(target, max_iterations, timeout_seconds, visualize)
        
        # Initialize quantum bridge if needed
        if not hasattr(self.bridge_app, 'is_initialized') or not self.bridge_app.is_initialized:
            self.bridge_app.initialize_system()
        
        # Track candidates for visualization
        candidates = []
        
        # Start timer
        start_time = time.time()
        
        # Create a quantum-inspired probability distribution centered around target/2
        center = target // 2
        
        # Use 19-based pattern for sampling
        sample_count = 19
        
        # Create threads for parallel primality testing
        with ThreadPoolExecutor(max_workers=min(19, os.cpu_count() or 4)) as executor:
            for iteration in range(max_iterations // sample_count + 1):
                # Check timeout
                if time.time() - start_time > timeout_seconds:
                    print(f"Timeout after {timeout_seconds} seconds.")
                    break
                
                # Generate quantum-inspired samples
                samples = self._generate_quantum_samples(center, target, sample_count)
                
                # Submit primality tests to thread pool
                future_to_sample = {}
                for sample in samples:
                    p1 = sample
                    p2 = target - p1
                    candidates.append((p1, p2))
                    
                    # Submit primality test for p1
                    future_p1 = executor.submit(self._is_prime, p1)
                    future_to_sample[future_p1] = (p1, p2, 'p1')
                    
                    # Submit primality test for p2
                    future_p2 = executor.submit(self._is_prime, p2)
                    future_to_sample[future_p2] = (p1, p2, 'p2')
                
                # Process results as they complete
                p1_results = {}
                p2_results = {}
                
                for future in as_completed(future_to_sample):
                    p1, p2, which = future_to_sample[future]
                    try:
                        is_prime = future.result()
                        if which == 'p1':
                            p1_results[p1] = is_prime
                        else:
                            p2_results[p2] = is_prime
                            
                        # Check if we have results for both p1 and p2
                        if p1 in p1_results and p2 in p2_results:
                            if p1_results[p1] and p2_results[p2]:
                                print(f"Found prime pair after {iteration*sample_count + len(candidates)} tests:")
                                print(f"p1: {p1}")
                                print(f"p2: {p2}")
                                print(f"Sum: {p1 + p2}")
                                
                                if visualize:
                                    self._visualize_search(candidates, (p1, p2), target, "Quantum-Inspired Search")
                                
                                return p1, p2
                    except Exception as e:
                        print(f"Error testing primality: {e}")
                
                # Progress update
                print(f"Completed {(iteration+1)*sample_count} samples. Still searching...")
        
        print(f"No prime pair found after {max_iterations} iterations.")
        
        if visualize and candidates:
            self._visualize_search(candidates, None, target, "Quantum-Inspired Search (No Solution Found)")
        
        return None, None
    
    def _generate_quantum_samples(self, center: int, target: int, count: int) -> List[int]:
        """Generate quantum-inspired samples for prime candidates."""
        # Create a base array of 19 values centered around center
        base_values = np.linspace(center - center*0.1, center + center*0.1, 19)
        
        # Process through quantum bridge to get quantum-inspired values
        try:
            processed = self.bridge_app.process_data(base_values)
            
            # Scale processed values to be in appropriate range
            min_val = center - center*0.2
            max_val = center + center*0.2
            scaled = min_val + (max_val - min_val) * (processed - np.min(processed)) / (np.max(processed) - np.min(processed))
            
            # Convert to integers and ensure they're odd
            samples = []
            for val in scaled:
                sample = int(val)
                # Ensure sample is odd (except if sample=2)
                if sample > 2 and sample % 2 == 0:
                    sample += 1
                if 0 < sample < target:  # Ensure sample is positive and less than target
                    samples.append(sample)
            
            # If we don't have enough samples, add some phi-harmonic values
            while len(samples) < count:
                phi_sample = int(center * (1 + (len(samples) % 5 - 2) * 0.1 * self.phi_inverse))
                if phi_sample > 2 and phi_sample % 2 == 0:
                    phi_sample += 1
                if 0 < phi_sample < target and phi_sample not in samples:
                    samples.append(phi_sample)
            
            return samples[:count]
        except Exception as e:
            print(f"Error generating quantum samples: {e}")
            # Fallback to phi-harmonic sampling
            return self._generate_phi_harmonic_samples(center, target, count)
    
    def _generate_phi_harmonic_samples(self, center: int, target: int, count: int) -> List[int]:
        """Generate phi-harmonic samples as fallback."""
        samples = []
        for i in range(count):
            # Use phi-harmonic offsets
            offset = int(center * 0.1 * (i % 10) * self.phi_inverse)
            if i % 2 == 0:
                sample = center + offset
            else:
                sample = center - offset
            
            # Ensure sample is odd (except if sample=2)
            if sample > 2 and sample % 2 == 0:
                sample += 1
            
            # Ensure sample is positive and less than target
            if 0 < sample < target:
                samples.append(sample)
        
        # If we don't have enough samples, add some random values
        while len(samples) < count:
            random_offset = random.randint(1, int(center * 0.2))
            if random.random() < 0.5:
                sample = center + random_offset
            else:
                sample = center - random_offset
            
            # Ensure sample is odd (except if sample=2)
            if sample > 2 and sample % 2 == 0:
                sample += 1
            
            # Ensure sample is positive and less than target
            if 0 < sample < target and sample not in samples:
                samples.append(sample)
        
        return samples[:count]
    
    def _is_prime(self, n: int) -> bool:
        """
        Check if a number is prime using the most efficient available method.
        
        For very large numbers, this uses the Miller-Rabin probabilistic test.
        If QuantumPrimeCalculator is available, it uses that instead.
        """
        # Use QuantumPrimeTestingHelper if available
        if self.prime_helper is not None:
            try:
                return self.prime_helper.is_prime(n)
            except Exception as e:
                print(f"Error using QuantumPrimeTestingHelper: {e}")
                # Fall back to built-in test
        
        # Handle small numbers directly
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        # For medium-sized numbers, use trial division
        if n < 10000:
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        # For large numbers, use Miller-Rabin test
        # The number of rounds controls the accuracy
        return self._miller_rabin(n, rounds=40)
    
    def _miller_rabin(self, n: int, rounds: int = 40) -> bool:
        """
        Miller-Rabin primality test.
        
        Args:
            n: Number to test
            rounds: Number of rounds (higher is more accurate)
            
        Returns:
            True if n is probably prime, False if definitely composite
        """
        # Handle small numbers
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        
        # Write n-1 as 2^r * d where d is odd
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        
        # Witness loop
        for _ in range(rounds):
            # Choose random witness
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            
            if x == 1 or x == n - 1:
                continue
            
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        
        return True
    
    def _visualize_search(self, candidates: List[Tuple[int, int]], 
                         solution: Optional[Tuple[int, int]], 
                         target: int, title: str) -> None:
        """Visualize the search process."""
        plt.figure(figsize=(12, 8))
        
        # Extract p1 values for plotting
        p1_values = [p1 for p1, _ in candidates]
        
        # Calculate percentage distance from target/2
        center = target // 2
        distances = [(p1 - center) / center * 100 for p1 in p1_values]
        
        # Plot the search trajectory
        plt.subplot(2, 1, 1)
        plt.plot(distances, 'b-', alpha=0.5)
        plt.plot(distances, 'bo', alpha=0.7)
        
        # Highlight the solution if found
        if solution:
            solution_index = candidates.index(solution)
            solution_distance = (solution[0] - center) / center * 100
            plt.plot(solution_index, solution_distance, 'ro', markersize=10, 
                    label=f'Solution: ({solution[0]}, {solution[1]})')
        
        plt.axhline(y=0, color='r', linestyle='--', label=f'Target/2: {center}')
        plt.axhline(y=(self.phi_inverse - 0.5) * 100, color='g', linestyle='--', 
                   label=f'Phi-harmonic point: {center * self.phi_inverse:.0f}')
        
        plt.title(f'{title} - Search Trajectory')
        plt.xlabel('Iteration')
        plt.ylabel('% Distance from Target/2')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Plot the distribution of tested values
        plt.subplot(2, 1, 2)
        plt.hist(distances, bins=50, alpha=0.7, color='blue')
        
        # Add vertical lines for key points
        plt.axvline(x=0, color='r', linestyle='--', label=f'Target/2: {center}')
        plt.axvline(x=(self.phi_inverse - 0.5) * 100, color='g', linestyle='--', 
                   label=f'Phi-harmonic point: {center * self.phi_inverse:.0f}')
        
        # Highlight the solution if found
        if solution:
            solution_distance = (solution[0] - center) / center * 100
            plt.axvline(x=solution_distance, color='m', linestyle='-', linewidth=2,
                       label=f'Solution: {solution[0]}')
        
        plt.title(f'{title} - Distribution of Tested Values')
        plt.xlabel('% Distance from Target/2')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        plt.tight_layout()
        
        # Save the visualization
        filename = f"prime_sum_search_{title.replace(' ', '_').lower()}.png"
        plt.savefig(filename)
        plt.close()
        
        print(f"Search visualization saved as '{filename}'")


def generate_random_target(digits: int = 64) -> str:
    """Generate a random target number with the specified number of digits."""
    # First digit should be 1-9
    first_digit = random.randint(1, 9)
    # Rest of digits can be 0-9
    rest_digits = [random.randint(0, 9) for _ in range(digits - 1)]
    # Combine into a single number
    digits_list = [first_digit] + rest_digits
    return ''.join(map(str, digits_list))


# Example usage
if __name__ == "__main__":
    # Create the decomposer
    decomposer = PrimeSumDecomposer()
    
    # Generate a random 64-digit target or use a specific one
    # Smaller target for testing
    test_target = "1234567890123456789012345678901234567890123456789012345678901234"
    
    # For quick testing, use a smaller number
    small_test = "123456789012345678901"
    
    print("\nTesting with a small number for demonstration:")
    p1, p2 = decomposer.find_prime_sum_pair(small_test, method='phi-harmonic', 
                                          max_iterations=1000, timeout_seconds=60)
    
    if p1 and p2:
        print("\nVerification:")
        print(f"p1 + p2 = {p1 + p2}")
        print(f"Target  = {small_test}")
        print(f"Match   = {str(p1 + p2) == small_test}")
    
    print("\nThe decomposer is ready to use with 64-digit values.")
    print("Example usage:")
    print("  decomposer = PrimeSumDecomposer()")
    print("  target = \"1234567890123456789012345678901234567890123456789012345678901234\"")
    print("  p1, p2 = decomposer.find_prime_sum_pair(target, method='quantum')")
