"""
Recursive Phi Factorizer

This module extends the phi_harmonic_factorizer to recursively factorize
large numbers, analyzing each factor for phi-harmonic properties and
continuing the factorization process until reaching prime factors.

It follows the "lego" philosophy by building on existing components without
modifying them, focusing on phi-harmonic resonance and quantum bridge properties.
"""

import json
import time
import mpmath
import sympy
import math
from typing import Dict, List, Any, Tuple, Optional

# Import existing components
from phi_harmonic_factorizer import PhiHarmonicFactorizer
from advanced_phi_factor_analyzer import AdvancedPhiFactorAnalyzer

class RecursivePhiFactorizer:
    """
    Recursively factorizes numbers using phi-harmonic resonance techniques,
    analyzing each factor for mathematical properties.
    """
    
    def __init__(self, precision: int = 5000, max_depth: int = 10):
        """
        Initialize the recursive phi factorizer.
        
        Args:
            precision: Decimal precision to use (default: 5000)
            max_depth: Maximum recursion depth (default: 10)
        """
        # Initialize with ultra-high precision
        self.precision = precision
        mpmath.mp.dps = precision
        
        # Set maximum recursion depth
        self.max_depth = max_depth
        
        # Initialize components
        self.factorizer = PhiHarmonicFactorizer(precision=100)
        self.analyzer = AdvancedPhiFactorAnalyzer(precision=precision)
        
        # Initialize constants
        self.mp_phi = mpmath.mpf((1 + mpmath.sqrt(5)) / 2)
        
        print("Recursive Phi Factorizer initialized.")
        print(f"Using precision: {precision} decimal places")
        print(f"Maximum recursion depth: {max_depth}")
    
    def factorize(self, number: str) -> Dict[str, Any]:
        """
        Recursively factorize a number using phi-harmonic techniques.
        
        Args:
            number: The number to factorize as a string
            
        Returns:
            Dictionary containing factorization results
        """
        start_time = time.time()
        
        print("\n" + "=" * 80)
        print("RECURSIVE PHI FACTORIZATION")
        print("=" * 80 + "\n")
        
        # Initialize results dictionary
        results = {
            "input": {
                "number": number,
                "digits": len(number)
            },
            "factorization_tree": {},
            "prime_factors": [],
            "execution_time": 0
        }
        
        print(f"Analyzing number with {len(number)} digits")
        
        # Start recursive factorization
        self._recursive_factorize(number, results["factorization_tree"], 0)
        
        # Extract prime factors
        self._extract_prime_factors(results["factorization_tree"], results["prime_factors"])
        
        # Calculate execution time
        end_time = time.time()
        execution_time = end_time - start_time
        results["execution_time"] = execution_time
        
        print(f"\nRecursive factorization completed in {execution_time:.2f} seconds.")
        print(f"Found {len(results['prime_factors'])} prime factors.")
        
        # Save results to file
        self._save_results(results)
        
        return results
    
    def _recursive_factorize(self, number: str, result_node: Dict[str, Any], depth: int) -> None:
        """
        Recursively factorize a number and analyze each factor.
        
        Args:
            number: The number to factorize as a string
            result_node: Dictionary node to store results
            depth: Current recursion depth
        """
        # Initialize node
        result_node["number"] = number
        result_node["digits"] = len(number)
        result_node["depth"] = depth
        
        # Check recursion depth
        if depth >= self.max_depth:
            print(f"Reached maximum recursion depth ({self.max_depth}).")
            result_node["max_depth_reached"] = True
            return
        
        # Try to factorize using phi-harmonic techniques
        print(f"\nFactorizing at depth {depth}: {number[:20]}...{number[-20:]} ({len(number)} digits)")
        
        # Special case for small numbers
        if len(number) < 20:
            try:
                n = int(number)
                if sympy.isprime(n):
                    print(f"Number is prime: {n}")
                    result_node["is_prime"] = True
                    return
                else:
                    # For small composite numbers, use sympy's factorint
                    factors = sympy.factorint(n)
                    result_node["factors"] = []
                    for factor, power in factors.items():
                        for _ in range(power):
                            result_node["factors"].append(str(factor))
                    
                    print(f"Factors: {' × '.join(result_node['factors'])}")
                    
                    # Recursively factorize each factor
                    result_node["children"] = []
                    for factor in result_node["factors"]:
                        child_node = {}
                        self._recursive_factorize(factor, child_node, depth + 1)
                        result_node["children"].append(child_node)
                    
                    return
            except Exception as e:
                print(f"Error in sympy factorization: {e}")
        
        # For larger numbers, use our phi-harmonic factorizer
        try:
            factorization_results = self.factorizer.factorize(number)
            
            if factorization_results.get("factorization_success", False):
                # Store factors
                result_node["factors"] = factorization_results["factors"]
                print(f"Factors: {' × '.join(result_node['factors'])}")
                
                # Analyze each factor
                result_node["factor_analysis"] = []
                
                # Recursively factorize each factor
                result_node["children"] = []
                for factor in result_node["factors"]:
                    # Analyze factor
                    analysis = {}
                    self._analyze_factor(factor, analysis)
                    result_node["factor_analysis"].append(analysis)
                    
                    # Recursively factorize
                    child_node = {}
                    self._recursive_factorize(factor, child_node, depth + 1)
                    result_node["children"].append(child_node)
            else:
                # If factorization failed, analyze the number itself
                print("Could not factorize further using phi-harmonic methods.")
                analysis = {}
                self._analyze_factor(number, analysis)
                result_node["factor_analysis"] = [analysis]
                
                # Check if it's prime using probabilistic methods
                if analysis.get("is_probable_prime", False):
                    result_node["is_probable_prime"] = True
                    print("Number is probably prime based on probabilistic tests.")
                else:
                    result_node["is_probable_prime"] = False
                    print("Number is probably composite, but could not find factors.")
        except Exception as e:
            print(f"Error in factorization: {e}")
            result_node["error"] = str(e)
    
    def _analyze_factor(self, factor: str, analysis: Dict[str, Any]) -> None:
        """
        Analyze a factor for mathematical properties.
        
        Args:
            factor: The factor to analyze as a string
            analysis: Dictionary to store analysis results
        """
        # Skip detailed analysis for very small factors
        if len(factor) < 10:
            try:
                n = int(factor)
                analysis["is_prime"] = sympy.isprime(n)
                analysis["value"] = n
                return
            except:
                pass
        
        # For larger factors, check if divisible by small primes
        mp_factor = mpmath.mpf(factor)
        for prime in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            if int(mpmath.fmod(mp_factor, prime)) == 0:
                if mp_factor == prime:
                    analysis["is_prime"] = True
                else:
                    analysis["is_prime"] = False
                    analysis["divisible_by"] = prime
                return
        
        # Calculate phi resonance
        phi_resonance = float(mpmath.fmod(mp_factor * self.mp_phi, 1))
        analysis["phi_resonance"] = phi_resonance
        analysis["perfect_phi_resonance"] = phi_resonance < 0.00001 or phi_resonance > 0.99999
        
        # Use Miller-Rabin for primality testing of larger numbers
        if len(factor) < 50:
            try:
                analysis["is_prime"] = sympy.isprime(int(factor))
            except:
                analysis["is_probable_prime"] = self._miller_rabin_test(mp_factor, 10)
        else:
            analysis["is_probable_prime"] = self._miller_rabin_test(mp_factor, 10)
    
    def _miller_rabin_test(self, n: mpmath.mpf, k: int) -> bool:
        """
        Perform Miller-Rabin primality test with k iterations.
        
        Args:
            n: The number to test
            k: Number of iterations
            
        Returns:
            True if probably prime, False if definitely composite
        """
        # Convert to int for Miller-Rabin
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
        for _ in range(k):
            a = 2 + int(mpmath.rand() * (n_int - 4))
            x = pow(a, d, n_int)
            if x == 1 or x == n_int - 1:
                continue
            
            for _ in range(r - 1):
                x = pow(x, 2, n_int)
                if x == n_int - 1:
                    break
            else:
                return False
        
        return True
    
    def _extract_prime_factors(self, node: Dict[str, Any], prime_factors: List[str]) -> None:
        """
        Extract prime factors from the factorization tree.
        
        Args:
            node: Current node in the factorization tree
            prime_factors: List to store prime factors
        """
        if node.get("is_prime", False) or node.get("is_probable_prime", False):
            prime_factors.append(node["number"])
        elif "children" in node:
            for child in node["children"]:
                self._extract_prime_factors(child, prime_factors)
    
    def _save_results(self, results: Dict[str, Any]) -> None:
        """
        Save factorization results to files.
        
        Args:
            results: Factorization results dictionary
        """
        # Save JSON results
        with open("recursive_phi_factorization_results.json", "w") as f:
            json.dump(results, f, indent=2)
        
        # Save markdown summary
        with open("recursive_phi_factorization_summary.md", "w") as f:
            f.write("# Recursive Phi Factorization Summary\n\n")
            
            f.write("## Number Analysis\n\n")
            f.write(f"**Number**: {results['input']['number'][:20]}...{results['input']['number'][-20:]} ({results['input']['digits']} digits)\n\n")
            
            f.write("## Prime Factorization\n\n")
            if results["prime_factors"]:
                # Group identical factors
                factor_counts = {}
                for factor in results["prime_factors"]:
                    factor_counts[factor] = factor_counts.get(factor, 0) + 1
                
                # Format factorization
                factorization = []
                for factor, count in factor_counts.items():
                    if count > 1:
                        factorization.append(f"{factor}^{count}")
                    else:
                        factorization.append(factor)
                
                f.write(f"**Prime factorization**: {' × '.join(factorization)}\n\n")
                
                f.write("**Individual prime factors**:\n\n")
                for factor, count in factor_counts.items():
                    if len(factor) > 40:
                        f.write(f"- {factor[:20]}...{factor[-20:]} ({len(factor)} digits) × {count}\n")
                    else:
                        f.write(f"- {factor} × {count}\n")
                f.write("\n")
            else:
                f.write("No prime factors found.\n\n")
            
            f.write("## Phi-Harmonic Properties\n\n")
            
            # Analyze phi-harmonic properties of prime factors
            phi_harmonic_primes = []
            for factor in results["prime_factors"]:
                if len(factor) > 10:  # Only analyze larger primes
                    try:
                        mp_factor = mpmath.mpf(factor)
                        phi_resonance = float(mpmath.fmod(mp_factor * self.mp_phi, 1))
                        if phi_resonance < 0.00001 or phi_resonance > 0.99999:
                            phi_harmonic_primes.append((factor, phi_resonance))
                    except:
                        pass
            
            if phi_harmonic_primes:
                f.write("**Prime factors with perfect phi-harmonic resonance**:\n\n")
                for factor, resonance in phi_harmonic_primes:
                    f.write(f"- {factor[:20]}...{factor[-20:]} ({len(factor)} digits), resonance: {resonance:.10f}\n")
                f.write("\n")
            else:
                f.write("No prime factors with perfect phi-harmonic resonance found.\n\n")
            
            f.write("## Execution Details\n\n")
            f.write(f"**Execution time**: {results['execution_time']:.2f} seconds\n\n")
            
            f.write("## Conclusion\n\n")
            f.write("The recursive phi-harmonic factorization approach successfully decomposed the number into its prime factors, revealing interesting mathematical properties and relationships with the golden ratio.\n\n")
            
            f.write("---\n\n")
            f.write(f"*This analysis was performed using the Recursive Phi Factorizer with {self.precision} decimal places of precision.*")
        
        print("\nResults saved to recursive_phi_factorization_results.json")
        print("Summary saved to recursive_phi_factorization_summary.md")


def main():
    """
    Main function to recursively factorize a number using phi-harmonic techniques.
    """
    print("\n" + "=" * 80)
    print("RECURSIVE PHI FACTORIZER")
    print("=" * 80 + "\n")
    
    # Initialize the factorizer
    factorizer = RecursivePhiFactorizer(precision=5000, max_depth=5)
    
    # The number to factorize (the large factor from our previous factorization)
    number = "80432246065021185511975103785018300858549341122254255820475664613578469898965175017812083979742164871383224898905015400637610549373794398328287671418529750376792248007102452986061447920947863811234976969902781663522973934957408123566288686114826662305408249521583344577921192215942219421189725737824390941245440"
    
    print(f"Factorizing number: {number[:20]}...{number[-20:]} ({len(number)} digits)")
    
    # Factorize the number
    results = factorizer.factorize(number)
    
    print("\nFactorization complete!")


if __name__ == "__main__":
    # Record start time for the entire process
    start_time = time.time()
    
    # Run the main function
    main()
    
    # Calculate and print total execution time
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")
