"""
Advanced Phi Factor Analyzer

This module extends the phi_harmonic_factorizer to perform advanced analysis
on the factors discovered, particularly examining large factors for primality
and phi-harmonic properties.

It follows the "lego" philosophy by building on existing components without
modifying them, focusing on phi-harmonic resonance and quantum bridge properties.
"""

import json
import time
import mpmath
import sympy
import math
import random
from typing import Dict, List, Any, Tuple, Optional

# Import the PhiHarmonicFactorizer as a component
from phi_harmonic_factorizer import PhiHarmonicFactorizer

class AdvancedPhiFactorAnalyzer:
    """
    Analyzes factors discovered by the PhiHarmonicFactorizer for additional
    mathematical properties and potential further factorization.
    """
    
    def __init__(self, precision: int = 5000):
        """
        Initialize the advanced phi factor analyzer.
        
        Args:
            precision: Decimal precision to use (default: 5000)
        """
        # Initialize with ultra-high precision
        self.precision = precision
        mpmath.mp.dps = precision
        
        # Initialize constants
        self.mp_phi = mpmath.mpf((1 + mpmath.sqrt(5)) / 2)
        self.mp_phi_inverse = 1 / self.mp_phi
        self.bridge_constant = mpmath.mpf(19)
        
        # Initialize the factorizer as a component
        self.factorizer = PhiHarmonicFactorizer(precision=100)
        
        print("Advanced Phi Factor Analyzer initialized.")
        print(f"Using precision: {precision} decimal places")
        print(f"Phi value: {float(self.mp_phi)}")
    
    def analyze_factor(self, factor: str) -> Dict[str, Any]:
        """
        Analyze a single factor for mathematical properties.
        
        Args:
            factor: The factor to analyze as a string
            
        Returns:
            Dictionary containing analysis results
        """
        start_time = time.time()
        
        print("\n" + "=" * 80)
        print("ADVANCED PHI FACTOR ANALYSIS")
        print("=" * 80 + "\n")
        
        # Convert to mpmath for high precision
        mp_factor = mpmath.mpf(factor)
        
        # Initialize results dictionary
        results = {
            "input": {
                "factor": factor,
                "digits": len(factor)
            },
            "phi_harmonic": {},
            "modular_patterns": {},
            "primality": {},
            "quantum_bridge": {},
            "execution_time": 0
        }
        
        print(f"Analyzing factor with {len(factor)} digits")
        
        # Calculate phi resonance
        self._calculate_phi_resonance(mp_factor, results)
        
        # Analyze modular patterns
        self._analyze_modular_patterns(mp_factor, results)
        
        # Check primality
        self._check_primality(mp_factor, results)
        
        # Analyze quantum bridge properties
        self._analyze_quantum_bridge(mp_factor, results)
        
        # Calculate execution time
        end_time = time.time()
        execution_time = end_time - start_time
        results["execution_time"] = execution_time
        
        print(f"\nAnalysis completed in {execution_time:.2f} seconds.")
        
        # Save results to file
        self._save_results(results)
        
        return results
    
    def _calculate_phi_resonance(self, mp_factor: mpmath.mpf, results: Dict[str, Any]) -> None:
        """
        Calculate phi resonance for a factor.
        
        Args:
            mp_factor: The factor as mpmath value
            results: Results dictionary to update
        """
        print("\nCalculating phi resonance...")
        
        # Calculate phi resonance
        phi_resonance = float(mpmath.fmod(mp_factor * self.mp_phi, 1))
        
        # Store the result
        results["phi_harmonic"]["resonance"] = phi_resonance
        
        # Check if it has perfect phi resonance
        is_perfect = phi_resonance < 0.00001 or phi_resonance > 0.99999
        results["phi_harmonic"]["is_perfect"] = is_perfect
        
        print(f"Phi resonance: {phi_resonance:.10f}")
        if is_perfect:
            print("This factor has perfect phi-harmonic resonance!")
            
            # Calculate phi-harmonic depth
            depth = self._calculate_phi_harmonic_depth(mp_factor)
            results["phi_harmonic"]["depth"] = depth
            print(f"Phi-harmonic depth: {depth}")
        else:
            print("This factor does not have perfect phi-harmonic resonance.")
    
    def _calculate_phi_harmonic_depth(self, mp_number: mpmath.mpf) -> int:
        """
        Calculate the phi-harmonic depth of a number.
        
        The phi-harmonic depth is the number of times the number can be
        multiplied by phi before the fractional part deviates from 0 or 1.
        
        Args:
            mp_number: The number as mpmath value
            
        Returns:
            Phi-harmonic depth
        """
        depth = 0
        current = mp_number
        
        while depth < 100:  # Limit to prevent infinite loops
            resonance = float(mpmath.fmod(current * self.mp_phi, 1))
            if resonance < 0.00001 or resonance > 0.99999:
                current = current * self.mp_phi
                depth += 1
            else:
                break
        
        return depth
    
    def _analyze_modular_patterns(self, mp_factor: mpmath.mpf, results: Dict[str, Any]) -> None:
        """
        Analyze modular patterns for mathematical insights.
        
        Args:
            mp_factor: The factor as mpmath value
            results: Results dictionary to update
        """
        print("\nAnalyzing modular patterns...")
        
        # Calculate modular values for key constants
        mod_values = {}
        
        for mod_base in [2, 3, 5, 7, 11, 13, 17, 19]:
            mod_value = int(mpmath.fmod(mp_factor, mod_base))
            mod_values[str(mod_base)] = mod_value
            print(f"Factor mod {mod_base} = {mod_value}")
        
        # Store modular values
        results["modular_patterns"] = mod_values
        
        # Check for special patterns
        mod_19 = mod_values["19"]
        
        # Based on previous findings, certain mod 19 values have special properties
        if mod_19 in [3, 17]:
            results["modular_patterns"]["special_pattern"] = "(3, 17) mod 19 pattern detected"
            print("Special pattern detected: (3, 17) mod 19")
        elif mod_19 in [7, 2, 15]:
            results["modular_patterns"]["special_pattern"] = "(7, 2, 15) mod 19 pattern detected"
            print("Special pattern detected: (7, 2, 15) mod 19")
    
    def _check_primality(self, mp_factor: mpmath.mpf, results: Dict[str, Any]) -> None:
        """
        Check if the factor is prime using probabilistic methods.
        
        Args:
            mp_factor: The factor as mpmath value
            results: Results dictionary to update
        """
        print("\nChecking primality...")
        
        # For very large numbers, we use probabilistic primality testing
        factor_str = str(int(mp_factor))
        
        # First, check if it's divisible by small primes
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
        for prime in small_primes:
            if int(mpmath.fmod(mp_factor, prime)) == 0:
                if mp_factor == prime:
                    results["primality"]["is_prime"] = True
                    results["primality"]["method"] = "direct_check"
                    print("Factor is a small prime number.")
                else:
                    results["primality"]["is_prime"] = False
                    results["primality"]["method"] = "direct_check"
                    results["primality"]["divisor"] = prime
                    print(f"Factor is divisible by {prime}, therefore not prime.")
                return
        
        # For numbers with fewer than 50 digits, use sympy's isprime
        if len(factor_str) < 50:
            try:
                is_prime = sympy.isprime(int(factor_str))
                results["primality"]["is_prime"] = is_prime
                results["primality"]["method"] = "sympy_isprime"
                print(f"Primality (sympy): {is_prime}")
                return
            except Exception as e:
                print(f"Error in sympy primality check: {e}")
        
        # For larger numbers, use Miller-Rabin with multiple bases
        print("Using Miller-Rabin probabilistic primality test...")
        
        # Number of Miller-Rabin tests to perform
        num_tests = 10
        
        # Perform Miller-Rabin tests
        is_probable_prime = True
        for _ in range(num_tests):
            # Choose a random base between 2 and factor-2
            base = random.randint(2, min(int(mp_factor) - 2, 10000))
            
            # Perform Miller-Rabin test
            if not self._miller_rabin_test(mp_factor, base):
                is_probable_prime = False
                break
        
        results["primality"]["is_probable_prime"] = is_probable_prime
        results["primality"]["method"] = f"miller_rabin_{num_tests}_tests"
        results["primality"]["confidence"] = f"99.9999% with {num_tests} tests" if is_probable_prime else "Definitely composite"
        
        print(f"Primality (Miller-Rabin): {is_probable_prime}")
        
        if is_probable_prime:
            print(f"Factor is probably prime with high confidence (99.9999% with {num_tests} tests).")
        else:
            print("Factor is definitely composite (not prime).")
            
            # If it's composite, try to find factors using our phi-harmonic factorizer
            print("Attempting to find factors using phi-harmonic methods...")
            try:
                factorization_results = self.factorizer.factorize(factor_str)
                if factorization_results.get("factorization_success", False):
                    results["primality"]["factors"] = factorization_results["factors"]
                    print(f"Factors found: {' × '.join(factorization_results['factors'])}")
                else:
                    print("Could not find factors using phi-harmonic methods.")
            except Exception as e:
                print(f"Error in factorization attempt: {e}")
    
    def _miller_rabin_test(self, n: mpmath.mpf, a: int) -> bool:
        """
        Perform a single Miller-Rabin primality test.
        
        Args:
            n: The number to test for primality
            a: The base to use for the test
            
        Returns:
            True if n passes the Miller-Rabin test with base a, False otherwise
        """
        # Convert n to int for Miller-Rabin test
        n_int = int(n)
        
        # Edge cases
        if n_int == 2 or n_int == 3:
            return True
        if n_int <= 1 or n_int % 2 == 0:
            return False
        
        # Write n-1 as d * 2^r
        r, d = 0, n_int - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        
        # Witness loop
        x = pow(a, d, n_int)
        if x == 1 or x == n_int - 1:
            return True
        
        for _ in range(r - 1):
            x = pow(x, 2, n_int)
            if x == n_int - 1:
                return True
        
        return False
    
    def _analyze_quantum_bridge(self, mp_factor: mpmath.mpf, results: Dict[str, Any]) -> None:
        """
        Analyze quantum bridge properties of the factor.
        
        Args:
            mp_factor: The factor as mpmath value
            results: Results dictionary to update
        """
        print("\nAnalyzing quantum bridge properties...")
        
        # Calculate quantum bridge value
        bridge_value = float(mp_factor / self.bridge_constant)
        results["quantum_bridge"]["bridge_value"] = bridge_value
        
        # Calculate quantum resonance
        quantum_resonance = float(mpmath.fmod(mp_factor * self.mp_phi / self.bridge_constant, 1))
        results["quantum_bridge"]["resonance"] = quantum_resonance
        
        # Check for perfect quantum resonance
        is_perfect_qr = quantum_resonance < 0.00001 or quantum_resonance > 0.99999
        results["quantum_bridge"]["is_perfect"] = is_perfect_qr
        
        print(f"Quantum bridge value: {bridge_value}")
        print(f"Quantum resonance: {quantum_resonance:.10f}")
        
        if is_perfect_qr:
            print("This factor has perfect quantum bridge resonance!")
        else:
            print("This factor does not have perfect quantum bridge resonance.")
    
    def _save_results(self, results: Dict[str, Any]) -> None:
        """
        Save analysis results to files.
        
        Args:
            results: Analysis results dictionary
        """
        # Save JSON results
        with open("advanced_phi_factor_analysis_results.json", "w") as f:
            json.dump(results, f, indent=2)
        
        # Save markdown summary
        with open("advanced_phi_factor_analysis_summary.md", "w") as f:
            f.write("# Advanced Phi Factor Analysis Summary\n\n")
            
            f.write("## Factor Analysis\n\n")
            f.write(f"**Factor**: {results['input']['factor'][:20]}...{results['input']['factor'][-20:]} ({results['input']['digits']} digits)\n\n")
            
            f.write("## Phi Harmonic Properties\n\n")
            f.write(f"**Phi resonance**: {results['phi_harmonic']['resonance']:.10f}\n\n")
            f.write(f"**Perfect phi resonance**: {results['phi_harmonic']['is_perfect']}\n\n")
            
            if results['phi_harmonic']['is_perfect']:
                f.write(f"**Phi-harmonic depth**: {results['phi_harmonic'].get('depth', 'N/A')}\n\n")
            
            f.write("## Modular Patterns\n\n")
            for mod_base, mod_value in results['modular_patterns'].items():
                if mod_base != "special_pattern":
                    f.write(f"**Mod {mod_base}**: {mod_value}\n\n")
            
            if "special_pattern" in results['modular_patterns']:
                f.write(f"**Special pattern**: {results['modular_patterns']['special_pattern']}\n\n")
            
            f.write("## Primality Analysis\n\n")
            if "is_prime" in results['primality']:
                f.write(f"**Is prime**: {results['primality']['is_prime']}\n\n")
                f.write(f"**Method**: {results['primality']['method']}\n\n")
                
                if not results['primality']['is_prime'] and "divisor" in results['primality']:
                    f.write(f"**Divisible by**: {results['primality']['divisor']}\n\n")
            
            if "is_probable_prime" in results['primality']:
                f.write(f"**Is probable prime**: {results['primality']['is_probable_prime']}\n\n")
                f.write(f"**Method**: {results['primality']['method']}\n\n")
                f.write(f"**Confidence**: {results['primality']['confidence']}\n\n")
                
                if not results['primality']['is_probable_prime'] and "factors" in results['primality']:
                    f.write("**Factors**:\n\n")
                    for factor in results['primality']['factors']:
                        f.write(f"- {factor}\n")
                    f.write("\n")
            
            f.write("## Quantum Bridge Properties\n\n")
            f.write(f"**Quantum bridge value**: {results['quantum_bridge']['bridge_value']}\n\n")
            f.write(f"**Quantum resonance**: {results['quantum_bridge']['resonance']:.10f}\n\n")
            f.write(f"**Perfect quantum resonance**: {results['quantum_bridge']['is_perfect']}\n\n")
            
            f.write("## Conclusion\n\n")
            
            # Generate conclusion based on analysis
            if results['phi_harmonic']['is_perfect'] and results['quantum_bridge']['is_perfect']:
                f.write("This factor exhibits both perfect phi-harmonic resonance and perfect quantum bridge resonance, suggesting it has special mathematical properties that connect it to fundamental constants like phi and the quantum bridge constant (19).\n\n")
            elif results['phi_harmonic']['is_perfect']:
                f.write("This factor exhibits perfect phi-harmonic resonance, suggesting a special relationship with the golden ratio.\n\n")
            elif results['quantum_bridge']['is_perfect']:
                f.write("This factor exhibits perfect quantum bridge resonance, suggesting a special relationship with the quantum bridge constant (19).\n\n")
            else:
                f.write("While this factor does not exhibit perfect resonance with either phi or the quantum bridge constant, its mathematical properties reveal interesting patterns that warrant further investigation.\n\n")
            
            if "is_probable_prime" in results['primality'] and results['primality']['is_probable_prime']:
                f.write("The factor is likely prime with high confidence, making it a significant mathematical discovery given its size and special properties.\n\n")
            elif "is_prime" in results['primality'] and results['primality']['is_prime']:
                f.write("The factor is confirmed to be prime, making it a significant mathematical discovery given its size and special properties.\n\n")
            else:
                f.write("The factor is composite, and its further decomposition may reveal additional mathematical insights.\n\n")
            
            f.write("---\n\n")
            f.write(f"*This analysis was performed using the Advanced Phi Factor Analyzer with {self.precision} decimal places of precision.*")
        
        print("\nResults saved to advanced_phi_factor_analysis_results.json")
        print("Summary saved to advanced_phi_factor_analysis_summary.md")


def main():
    """
    Main function to analyze a factor using advanced phi-harmonic techniques.
    """
    print("\n" + "=" * 80)
    print("ADVANCED PHI FACTOR ANALYZER")
    print("=" * 80 + "\n")
    
    # Initialize the analyzer
    analyzer = AdvancedPhiFactorAnalyzer(precision=5000)
    
    # The factor to analyze (the large factor from our previous factorization)
    factor = "80432246065021185511975103785018300858549341122254255820475664613578469898965175017812083979742164871383224898905015400637610549373794398328287671418529750376792248007102452986061447920947863811234976969902781663522973934957408123566288686114826662305408249521583344577921192215942219421189725737824390941245440"
    
    print(f"Analyzing factor: {factor[:20]}...{factor[-20:]} ({len(factor)} digits)")
    
    # Analyze the factor
    results = analyzer.analyze_factor(factor)
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    # Record start time for the entire process
    start_time = time.time()
    
    # Run the main function
    main()
    
    # Calculate and print total execution time
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")
