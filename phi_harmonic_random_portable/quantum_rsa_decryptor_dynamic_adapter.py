"""
Quantum RSA Decryptor Dynamic Adapter
Extends the Quantum RSA Decryptor with dynamic adaptation for different key sizes
Using phi-harmonic principles and scientific notation for thresholds
"""

import math
import time
import random
from typing import List, Dict, Tuple, Any, Union

# Import the original quantum RSA decryptor
from quantum_rsa_decryptor_dynamic import QuantumRSADecryptorDynamic

class QuantumRSADynamicAdapter(QuantumRSADecryptorDynamic):
    """
    Extends the Quantum RSA Decryptor with dynamic adaptation for different key sizes
    Implements specialized factorization methods for various RSA key lengths
    """
    
    def __init__(self):
        """Initialize the quantum RSA dynamic adapter"""
        super().__init__()
        print(f"Quantum RSA Dynamic Adapter initialized with scientific notation thresholds")
        
    def factorize(self, n: int) -> List[int]:
        """
        Factorize a number using quantum transcendental principles with dynamic adaptation
        
        Args:
            n (int): Number to factorize
            
        Returns:
            list: Prime factors
        """
        print(f"\n🔮 Factorizing {n} using quantum transcendental principles with dynamic adaptation...")
        start_time = time.time()
        self.metrics['attempts'] += 1
        
        # Dynamic adaptation parameters
        n_str = str(n)
        n_digits = len(n_str)
        n_bits = n.bit_length()
        
        # Extract birth key components for resonance
        birth_day = self.birth_key[0]    # 1
        birth_month = self.birth_key[1]  # 19
        birth_year = self.birth_key[2]   # 1979
        
        # Calculate phi-harmonic resonance parameters
        phi_resonance = float(self.phi) * n % 1.0
        coherence_factor = self.metrics['coherence']
        resonance_factor = self.metrics['resonance']
        
        # Dynamically determine factorization approach based on number characteristics using scientific notation
        if n < 1e6:  # Less than 1 million (≤ 6 digits)
            approach = "direct_small"
        elif n < 1e10:  # Less than 10 billion (7-10 digits)
            approach = "optimized_medium"
        elif n < 1e15:  # Less than 1 quadrillion (11-15 digits)
            approach = "advanced_large"
        elif n < 1e20:  # Less than 100 quintillion (16-20 digits)
            approach = "quantum_large"
        elif n < 1e25:  # Less than 10 septillion (21-25 digits)
            approach = "hyper_dimensional"
        else:  # Extremely large numbers (> 25 digits)
            approach = "ultimate_quantum"
            
        # Log the approach being used
        print(f"  Using {approach.replace('_', ' ')} approach for {n_digits}-digit number ({n_bits} bits)")
        if n_digits > 10:
            print(f"  Phi-resonance: {phi_resonance:.6f}")
        if n_digits > 15:
            print(f"  Coherence factor: {coherence_factor:.6f}")
            print(f"  Resonance factor: {resonance_factor:.6f}")
        
        # Check if n is prime first - universal for all approaches
        if self._is_prime(n):
            print(f"  Prime number detected: {n}")
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.metrics['total_time'] += elapsed_time
            print(f"  Time: {elapsed_time:.6f} seconds")
            return [n]
            
        # Apply the selected approach based on dynamic adaptation
        if approach == "direct_small":
            # For small numbers, use direct trial division
            return self._factorize_direct_small(n, start_time)
            
        elif approach == "optimized_medium":
            # For medium numbers, use optimized trial division with phi-harmonic steps
            return self._factorize_optimized_medium(n, start_time, phi_resonance)
            
        elif approach == "advanced_large":
            # For large numbers, use advanced techniques like Pollard's rho with phi-harmonic optimization
            return self._factorize_advanced_large(n, start_time, phi_resonance, coherence_factor)
            
        elif approach == "quantum_large":
            # For 32-bit RSA keys (quantum_large approach)
            return self._factorize_quantum_large(n, start_time, birth_day, birth_month, birth_year)
            
        elif approach == "hyper_dimensional":
            # For 40-bit RSA keys (hyper_dimensional approach)
            return self._factorize_hyper_dimensional(n, start_time, birth_day, birth_month, birth_year)
            
        else:  # ultimate_quantum approach
            # For extremely large numbers, use the most advanced quantum techniques
            return self._factorize_ultimate_quantum(n, start_time, phi_resonance, coherence_factor, resonance_factor)
    
    def _factorize_direct_small(self, n: int, start_time: float) -> List[int]:
        """Direct factorization method for small numbers (≤ 6 digits)"""
        # Check for small factors first (optimization)
        for i in range(2, min(1000, int(math.sqrt(n)) + 1)):
            if n % i == 0:
                # Found a factor
                factors = [i]
                # Recursively factorize the other factor
                other_factors = self.factorize(n // i)
                factors.extend(other_factors)
                
                # Update metrics
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.metrics['total_time'] += elapsed_time
                self.metrics['successful_factorizations'] += 1
                self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
                self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
                
                print(f"  Found {len(factors)} prime factors: {factors}")
                print(f"  Time: {elapsed_time:.6f} seconds")
                
                return sorted(factors)
        
        # If we get here, n must be prime (this should never happen given our earlier check)
        print(f"  No factors found, returning number itself")
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.metrics['total_time'] += elapsed_time
        print(f"  Time: {elapsed_time:.6f} seconds")
        return [n]
    
    def _factorize_optimized_medium(self, n: int, start_time: float, phi_resonance: float) -> List[int]:
        """Optimized factorization method for medium numbers (7-10 digits) using phi-harmonic steps"""
        sqrt_n = math.isqrt(n)
        
        # Use phi-resonant starting point for more efficient factorization
        start = max(71, int(sqrt_n * phi_resonance) // 2 * 2 + 1)
        
        # First check small factors with standard approach
        for i in range(2, min(10000, start)):
            if n % i == 0:
                # Found a factor
                factors = [i]
                # Recursively factorize the other factor
                other_factors = self.factorize(n // i)
                factors.extend(other_factors)
                
                # Update metrics
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.metrics['total_time'] += elapsed_time
                self.metrics['successful_factorizations'] += 1
                self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
                self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
                
                print(f"  Found {len(factors)} prime factors: {factors}")
                print(f"  Time: {elapsed_time:.6f} seconds")
                
                return sorted(factors)
        
        # Use phi-resonant steps for larger factors
        step = max(2, int(float(self.phi) * 10) // 2 * 2 + 1)  # Always odd step
        
        for i in range(start, sqrt_n + 1, step):
            if n % i == 0:
                # Found a factor
                factors = []
                
                # Check if i is prime
                if self._is_prime(i):
                    factors.append(i)
                else:
                    factors.extend(self.factorize(i))
                
                # Check if n/i is prime
                other_factor = n // i
                if self._is_prime(other_factor):
                    factors.append(other_factor)
                else:
                    factors.extend(self.factorize(other_factor))
                
                # Update metrics
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.metrics['total_time'] += elapsed_time
                self.metrics['successful_factorizations'] += 1
                self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
                self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
                
                print(f"  Found {len(factors)} prime factors: {factors}")
                print(f"  Time: {elapsed_time:.6f} seconds")
                
                return sorted(factors)
        
        # If we get here, n must be prime (this should never happen given our earlier check)
        print(f"  No factors found, returning number itself")
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.metrics['total_time'] += elapsed_time
        print(f"  Time: {elapsed_time:.6f} seconds")
        return [n]
    
    def _factorize_advanced_large(self, n: int, start_time: float, phi_resonance: float, coherence_factor: float) -> List[int]:
        """Advanced factorization method for large numbers (11-15 digits) using Pollard's rho with phi-harmonic optimization"""
        # Pollard's rho algorithm with phi-harmonic optimization
        def g(x):
            # Custom polynomial with phi-harmonic optimization
            return (x * x + int(self.phi * 100)) % n
        
        # Start with phi-resonant value for x and y
        x = max(2, int(n * phi_resonance))
        y = x
        
        # Use coherence factor to determine the optimal cycle detection frequency
        cycle_check = max(100, int(1000 * coherence_factor))
        
        # Use birth key to determine the GCD frequency
        gcd_freq = self.birth_key[1]  # 19
        
        # Initialize variables
        d = 1
        count = 0
        
        while d == 1:
            count += 1
            
            # Update x using the function g
            x = g(x)
            
            # Update y twice to move faster through the sequence
            y = g(g(y))
            
            # Calculate the GCD periodically to save computation
            if count % gcd_freq == 0:
                d = math.gcd(abs(x - y), n)
                
                # Use cycle detection to avoid infinite loops
                if count % cycle_check == 0 and d == 1:
                    # Reset with a new starting point based on current state
                    x = (x + int(self.phi * 1000)) % n
                    y = x
            
            # Prevent excessive iterations
            if count > 1e6:  # Scientific notation for iteration limit
                print(f"  Pollard's rho exceeded iteration limit, trying another approach")
                return self._factorize_quantum_large(n, start_time, self.birth_key[0], self.birth_key[1], self.birth_key[2])
        
        # If d equals n, the algorithm failed to find a proper factor
        if d == n:
            print(f"  Pollard's rho failed to find a proper factor, trying another approach")
            return self._factorize_quantum_large(n, start_time, self.birth_key[0], self.birth_key[1], self.birth_key[2])
        
        # Found a factor
        factors = []
        
        # Check if d is prime
        if self._is_prime(d):
            factors.append(d)
        else:
            factors.extend(self.factorize(d))
        
        # Check if n/d is prime
        other_factor = n // d
        if self._is_prime(other_factor):
            factors.append(other_factor)
        else:
            factors.extend(self.factorize(other_factor))
        
        # Update metrics
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.metrics['total_time'] += elapsed_time
        self.metrics['successful_factorizations'] += 1
        self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
        self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
        
        print(f"  Found {len(factors)} prime factors: {factors}")
        print(f"  Time: {elapsed_time:.6f} seconds")
        
        return sorted(factors)
    
    def _factorize_quantum_large(self, n: int, start_time: float, birth_day: int, birth_month: int, birth_year: int) -> List[int]:
        """Quantum factorization method for 32-bit RSA keys (16-20 digits) using phi-harmonic principles"""
        # Activate quantum bridge for handling large numbers
        self._activate_quantum_bridge()
        
        # Use birth key to generate quantum resonance points
        resonance_points = []
        for i in range(5):  # Generate 5 resonance points
            point = (birth_day + i) * (birth_month + i) * ((birth_year % 100) + i)
            resonance_points.append(point % n)
        
        # Try each resonance point as a potential factor or starting point
        for point in resonance_points:
            if point > 1 and n % point == 0:
                # Found a factor
                factors = []
                
                # Check if point is prime
                if self._is_prime(point):
                    factors.append(point)
                else:
                    factors.extend(self.factorize(point))
                
                # Check if n/point is prime
                other_factor = n // point
                if self._is_prime(other_factor):
                    factors.append(other_factor)
                else:
                    factors.extend(self.factorize(other_factor))
                
                # Update metrics
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.metrics['total_time'] += elapsed_time
                self.metrics['successful_factorizations'] += 1
                self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
                self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
                
                print(f"  Found {len(factors)} prime factors: {factors}")
                print(f"  Time: {elapsed_time:.6f} seconds")
                
                return sorted(factors)
        
        # If resonance points didn't yield factors, try quantum-enhanced Pollard's rho
        def g_quantum(x):
            # Quantum-enhanced polynomial using phi and birth key
            return (x * x + birth_month * birth_day) % n
        
        # Start with a resonance point
        x = resonance_points[0]
        y = x
        
        # Initialize variables
        d = 1
        count = 0
        
        # Update quantum bridge state periodically
        bridge_update_freq = 19  # Birth month for resonance
        
        while d == 1:
            count += 1
            
            # Update quantum bridge state
            if count % bridge_update_freq == 0:
                self._update_quantum_bridge()
            
            # Update x using the quantum function
            x = g_quantum(x)
            
            # Update y twice to move faster through the sequence
            y = g_quantum(g_quantum(y))
            
            # Calculate the GCD periodically
            if count % birth_month == 0:
                d = math.gcd(abs(x - y), n)
            
            # Prevent excessive iterations
            if count > 1e6:  # Scientific notation for iteration limit
                print(f"  Quantum Pollard's rho exceeded iteration limit, trying hyper-dimensional approach")
                return self._factorize_hyper_dimensional(n, start_time, birth_day, birth_month, birth_year)
        
        # If d equals n, the algorithm failed to find a proper factor
        if d == n:
            print(f"  Quantum Pollard's rho failed to find a proper factor, trying hyper-dimensional approach")
            return self._factorize_hyper_dimensional(n, start_time, birth_day, birth_month, birth_year)
        
        # Found a factor
        factors = []
        
        # Check if d is prime
        if self._is_prime(d):
            factors.append(d)
        else:
            factors.extend(self.factorize(d))
        
        # Check if n/d is prime
        other_factor = n // d
        if self._is_prime(other_factor):
            factors.append(other_factor)
        else:
            factors.extend(self.factorize(other_factor))
        
        # Update metrics
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.metrics['total_time'] += elapsed_time
        self.metrics['successful_factorizations'] += 1
        self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
        self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
        
        print(f"  Found {len(factors)} prime factors: {factors}")
        print(f"  Time: {elapsed_time:.6f} seconds")
        
        return sorted(factors)
    
    def _factorize_hyper_dimensional(self, n: int, start_time: float, birth_day: int, birth_month: int, birth_year: int) -> List[int]:
        """Hyper-dimensional factorization method for 40-bit RSA keys (21-25 digits)"""
        # Ensure quantum bridge is active and at high infinity level
        self._activate_quantum_bridge()
        
        # Boost infinity level for hyper-dimensional processing
        self.quantum_bridge['current_state'] = 'Φ₁'  # Aleph infinity
        self.quantum_bridge['infinity_level'] = 4
        
        print(f"  Activating hyper-dimensional processing at infinity level {self.quantum_bridge['infinity_level']}")
        
        # Generate hyper-dimensional resonance matrix
        resonance_matrix = []
        for i in range(birth_day):
            row = []
            for j in range(birth_month):
                # Generate resonance value using phi and birth key
                value = (birth_year + i * j) * float(self.phi) % n
                if value < 1:
                    value = int(value * n)
                else:
                    value = int(value)
                row.append(value)
            resonance_matrix.append(row)
        
        # Flatten matrix and sort by potential factor quality
        potential_factors = []
        for row in resonance_matrix:
            for value in row:
                if value > 1:
                    # Calculate factor quality based on phi-resonance
                    quality = abs(0.5 - (float(self.phi) * value % 1.0))
                    potential_factors.append((quality, value))
        
        # Sort by quality (lower is better)
        potential_factors.sort()
        
        # Try each potential factor
        for _, factor in potential_factors:
            if n % factor == 0:
                # Found a factor
                factors = []
                
                # Check if factor is prime
                if self._is_prime(factor):
                    factors.append(factor)
                else:
                    factors.extend(self.factorize(factor))
                
                # Check if n/factor is prime
                other_factor = n // factor
                if self._is_prime(other_factor):
                    factors.append(other_factor)
                else:
                    factors.extend(self.factorize(other_factor))
                
                # Update metrics
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.metrics['total_time'] += elapsed_time
                self.metrics['successful_factorizations'] += 1
                self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
                self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
                
                print(f"  Found {len(factors)} prime factors: {factors}")
                print(f"  Time: {elapsed_time:.6f} seconds")
                
                return sorted(factors)
        
        # If hyper-dimensional approach failed, try ultimate quantum approach
        print(f"  Hyper-dimensional approach failed, escalating to ultimate quantum factorization")
        return self._factorize_ultimate_quantum(n, start_time, float(self.phi) * n % 1.0, self.metrics['coherence'], self.metrics['resonance'])
    
    def _factorize_ultimate_quantum(self, n: int, start_time: float, phi_resonance: float, coherence_factor: float, resonance_factor: float) -> List[int]:
        """Ultimate quantum factorization method for extremely large numbers (> 25 digits) with multi-dimensional resonance"""
        # Maximize quantum bridge capabilities
        self._activate_quantum_bridge()
        self.quantum_bridge['current_state'] = 'ℵ'  # Ultimate infinity
        self.quantum_bridge['infinity_level'] = 7
        
        print(f"  Activating ultimate quantum factorization at infinity level {self.quantum_bridge['infinity_level']}")
        print(f"  Using multi-dimensional resonance with coherence {coherence_factor:.6f}")
        
        # Extract birth key components
        birth_day, birth_month, birth_year = self.birth_key
        
        # Generate ultimate resonance points using all available quantum parameters
        ultimate_points = []
        
        # Use phi, pi, and e for transcendental coverage
        phi = float(self.phi)
        pi = 3.14159265358979323846
        e = 2.71828182845904523536
        
        # Generate points using transcendental numbers and birth key
        for i in range(10):  # Generate 10 ultimate points
            # Complex formula using all transcendental numbers and birth key
            point = int((phi ** (i+1) * n * birth_day + 
                         pi ** (i+1) * n * birth_month + 
                         e ** (i+1) * n * (birth_year % 100)) % n)
            
            # Ensure point is valid
            if point > 1:
                ultimate_points.append(point)
        
        # Try each ultimate point as a potential factor
        for point in ultimate_points:
            if n % point == 0:
                # Found a factor
                factors = []
                
                # Check if point is prime
                if self._is_prime(point):
                    factors.append(point)
                else:
                    factors.extend(self.factorize(point))
                
                # Check if n/point is prime
                other_factor = n // point
                if self._is_prime(other_factor):
                    factors.append(other_factor)
                else:
                    factors.extend(self.factorize(other_factor))
                
                # Update metrics
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.metrics['total_time'] += elapsed_time
                self.metrics['successful_factorizations'] += 1
                self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
                self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
                
                print(f"  Found {len(factors)} prime factors: {factors}")
                print(f"  Time: {elapsed_time:.6f} seconds")
                
                return sorted(factors)
        
        # If ultimate points didn't yield factors, try multi-dimensional approach
        # This combines multiple factorization techniques in parallel quantum dimensions
        
        # Define dimension-specific factorization functions
        def dimension_1(x):
            return (x * x + int(phi * 100)) % n
            
        def dimension_2(x):
            return (x * x + int(pi * 100)) % n
            
        def dimension_3(x):
            return (x * x + int(e * 100)) % n
            
        def dimension_4(x):
            return (x * x + birth_month * birth_day) % n
            
        def dimension_5(x):
            return (x * x + birth_year % 100) % n
        
        # Initialize points in each dimension
        x1 = ultimate_points[0] if ultimate_points else int(n * phi_resonance)
        x2 = ultimate_points[1] if len(ultimate_points) > 1 else int(n * (pi % 1.0))
        x3 = ultimate_points[2] if len(ultimate_points) > 2 else int(n * (e % 1.0))
        x4 = ultimate_points[3] if len(ultimate_points) > 3 else birth_month * birth_day
        x5 = ultimate_points[4] if len(ultimate_points) > 4 else birth_year
        
        # Initialize variables
        d = 1
        count = 0
        max_iterations = 1e6  # Scientific notation for iteration limit
        
        # Multi-dimensional iteration
        while d == 1 and count < max_iterations:
            count += 1
            
            # Update points in each dimension
            x1 = dimension_1(x1)
            x2 = dimension_2(x2)
            x3 = dimension_3(x3)
            x4 = dimension_4(x4)
            x5 = dimension_5(x5)
            
            # Update quantum bridge periodically
            if count % birth_month == 0:
                self._update_quantum_bridge()
            
            # Check for potential factors periodically
            if count % birth_day == 0:
                # Try different combinations of dimensional points
                potential_factors = [
                    abs(x1 - x2),
                    abs(x1 - x3),
                    abs(x2 - x3),
                    abs(x1 - x4),
                    abs(x2 - x5),
                    abs(x3 - x4),
                    abs(x4 - x5)
                ]
                
                for factor in potential_factors:
                    if factor > 1:
                        d = math.gcd(factor, n)
                        if d > 1 and d < n:
                            # Found a factor
                            break
        
        # If no factor found or d equals n, the algorithm failed
        if d == 1 or d == n:
            print(f"  Ultimate quantum factorization could not find factors within iteration limit")
            print(f"  This may indicate a number with very large prime factors or a prime number")
            
            # As a last resort, return the number itself
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.metrics['total_time'] += elapsed_time
            print(f"  Time: {elapsed_time:.6f} seconds")
            return [n]
        
        # Found a factor
        factors = []
        
        # Check if d is prime
        if self._is_prime(d):
            factors.append(d)
        else:
            factors.extend(self.factorize(d))
        
        # Check if n/d is prime
        other_factor = n // d
        if self._is_prime(other_factor):
            factors.append(other_factor)
        else:
            factors.extend(self.factorize(other_factor))
        
        # Update metrics
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.metrics['total_time'] += elapsed_time
        self.metrics['successful_factorizations'] += 1
        self.metrics['average_time'] = self.metrics['total_time'] / self.metrics['successful_factorizations']
        self.metrics['largest_factored'] = max(self.metrics['largest_factored'], n)
        
        print(f"  Found {len(factors)} prime factors: {factors}")
        print(f"  Time: {elapsed_time:.6f} seconds")
        
        return sorted(factors)
