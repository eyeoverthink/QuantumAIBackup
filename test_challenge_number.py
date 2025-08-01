#!/usr/bin/env python3
"""
Test script for analyzing and factorizing a specific challenge RSA number.
This script follows the 'lego' philosophy by building on existing components
without modifying them.
"""

import json
import time
import mpmath
import sympy
from datetime import datetime
from quantum_rsa_challenger import QuantumRSAChallenger

# Set mpmath precision
mpmath.mp.dps = 5000  # Set precision to 5000 decimal places

def main():
    """
    Main function to analyze and attempt to factorize the challenge number.
    """
    print("=" * 80)
    print("ANALYZING CHALLENGE RSA NUMBER")
    print("=" * 80)
    print()

    # Initialize the Quantum RSA Challenger
    challenger = QuantumRSAChallenger()
    
    # The challenge number
    challenge_number = "680981857830123043521643190942698893887610580385930663689857535732817152503519672132400835886294053517740915812301113596826528876373028953378455161114501215677869107870874058414675602939915375915692290836708180120486339395907137969396278916473685318083144622838051629752781700878903892519885721335073664155797101269608455506979383616397772355314499561208860048810041431231219093940565998622599085881124851003734369153467606907580035118077014675455851465035484020703935059653116584360141326416018527952933400184265784217571263956455995306341518309093634367192235410797715824058879868015659094786312704274814833605734014103410900062432899935384040078821434782493881790250431519835714594162476628058123726999071789973141350654265862071103097794683416812643533685240999964854484293394715883387852074413552918966785078838086031919891566952843667448830208001158128185323566873544041266469360105780525297205393949514852893299023639807258619303040953870485726023836957821514790305209052347756431789849196482498404285868940667800347024540291885468791324255479985427653789218908234183319222394314107718418221713399553654528117308676350073313077635294233257620810061146398282351808045796688243650859915921048773817111140780659648915234037107201"
    
    # Save the challenge number to a file
    with open("challenge_number.txt", "w") as f:
        f.write(challenge_number)
    
    print(f"Challenge number saved to challenge_number.txt ({len(challenge_number)} digits)")
    print()
    
    # First, check if the number has phi-harmonic properties
    print("=" * 80)
    print("ANALYZING PHI-HARMONIC PROPERTIES")
    print("=" * 80)
    print()
    
    # Analyze the number using the Quantum RSA Challenger
    print("Analyzing number...")
    analysis_start_time = time.time()
    analysis_results = challenger.analyze_rsa_modulus(challenge_number)
    analysis_end_time = time.time()
    analysis_time = analysis_end_time - analysis_start_time
    
    # Save the analysis results to a JSON file
    with open("challenge_analysis_results.json", "w") as f:
        json.dump(analysis_results, f, indent=4)
    
    # Create a markdown summary of the analysis
    with open("challenge_analysis_summary.md", "w") as f:
        f.write("# Challenge Number Analysis Summary\n\n")
        f.write(f"Analysis performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## Number Properties\n\n")
        f.write(f"- Number has {len(challenge_number)} digits\n")
        
        # Phi resonance
        phi_resonance = analysis_results["phi_harmonic_analysis"]["phi_resonance"]
        f.write(f"- Phi resonance: {phi_resonance:.10f}\n")
        if phi_resonance < 1e-9:
            f.write("- This number has perfect phi-harmonic resonance!\n")
        elif phi_resonance < 0.01:
            f.write("- This number has strong phi-harmonic resonance\n")
        else:
            f.write("- This number does not have significant phi-harmonic resonance\n")
        
        # Phi-inverse resonance
        phi_inverse_resonance = analysis_results["phi_harmonic_analysis"]["phi_inverse_resonance"]
        f.write(f"- Phi-inverse resonance: {phi_inverse_resonance:.10f}\n")
        if phi_inverse_resonance < 1e-9:
            f.write("- This number has perfect phi-inverse resonance!\n")
        elif phi_inverse_resonance < 0.01:
            f.write("- This number has strong phi-inverse resonance\n")
        else:
            f.write("- This number does not have significant phi-inverse resonance\n")
        
        # Check divisibility by small primes
        if analysis_results["phi_harmonic_analysis"]["has_small_prime_factor"]:
            f.write("- Number has at least one small prime factor!\n")
        
        # Modular patterns
        f.write("\n## Modular Patterns\n\n")
        for prime, remainder in analysis_results["quantum_bridge_analysis"]["modular_patterns"].items():
            f.write(f"- Number mod {prime} = {remainder}\n")
        
        # Potential approaches
        f.write("\n## Potential Approaches\n\n")
        for approach in analysis_results["potential_approaches"]:
            f.write(f"- {approach['name']} ({approach['priority']} priority): {approach['description']}\n")
        
        f.write(f"\nAnalysis completed in {analysis_time:.2f} seconds.\n")
    
    print("=" * 80)
    print("ANALYSIS RESULTS")
    print("=" * 80)
    print()
    
    print(f"Number has {len(challenge_number)} digits")
    
    # Phi resonance
    phi_resonance = analysis_results["phi_harmonic_analysis"]["phi_resonance"]
    print(f"Phi resonance: {phi_resonance:.10f}")
    if phi_resonance < 1e-9:
        print("This number has perfect phi-harmonic resonance!")
    elif phi_resonance < 0.01:
        print("This number has strong phi-harmonic resonance")
    else:
        print("This number does not have significant phi-harmonic resonance")
    
    # Phi-inverse resonance
    phi_inverse_resonance = analysis_results["phi_harmonic_analysis"]["phi_inverse_resonance"]
    print(f"Phi-inverse resonance: {phi_inverse_resonance:.10f}")
    if phi_inverse_resonance < 1e-9:
        print("This number has perfect phi-inverse resonance!")
    elif phi_inverse_resonance < 0.01:
        print("This number has strong phi-inverse resonance")
    else:
        print("This number does not have significant phi-inverse resonance")
    
    # Check divisibility by small primes
    if analysis_results["phi_harmonic_analysis"]["has_small_prime_factor"]:
        print("Number has at least one small prime factor!")
    
    print()
    print("Modular patterns:")
    for prime, remainder in analysis_results["quantum_bridge_analysis"]["modular_patterns"].items():
        print(f"Number mod {prime} = {remainder}")
    
    print()
    print("Potential approaches:")
    for approach in analysis_results["potential_approaches"]:
        print(f"- {approach['name']} ({approach['priority']} priority): {approach['description']}")
    
    print()
    print(f"Analysis completed in {analysis_time:.2f} seconds.")
    print()
    print(f"Results saved to challenge_analysis_results.json")
    print(f"Summary saved to challenge_analysis_summary.md")
    print()
    
    # Now attempt to factorize the number
    print("=" * 80)
    print("FACTORIZATION ATTEMPT")
    print("=" * 80)
    print()
    
    print("Attempting to factorize challenge number...")
    factorization_start_time = time.time()
    factorization_results = challenger.attempt_factorization(challenge_number, max_time_seconds=1800)  # 30 minutes max
    factorization_end_time = time.time()
    factorization_time = factorization_end_time - factorization_start_time
    
    # Save the factorization results to a JSON file
    with open("challenge_factorization_results.json", "w") as f:
        json.dump(factorization_results, f, indent=4)
    
    # Create a markdown summary of the factorization
    with open("challenge_factorization_summary.md", "w") as f:
        f.write("# Challenge Number Factorization Summary\n\n")
        f.write(f"Factorization performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        if factorization_results["factorization_success"]:
            f.write("## Factorization Successful!\n\n")
            f.write("Factors:\n")
            for factor in factorization_results["factors"]:
                f.write(f"- {factor}\n")
        else:
            f.write("## Factorization Unsuccessful\n\n")
            f.write("The factorization attempt did not succeed within the time limit.\n\n")
            if "attempted_approaches" in factorization_results:
                f.write("### Attempted Approaches\n\n")
                for approach, details in factorization_results["attempted_approaches"].items():
                    f.write(f"#### {approach}\n")
                    f.write(f"- Status: {details['status']}\n")
                    f.write(f"- Execution time: {details['execution_time']:.2f} seconds\n")
                    if "partial_factors" in details and details["partial_factors"]:
                        f.write("- Partial factors:\n")
                        for factor in details["partial_factors"]:
                            f.write(f"  - {factor}\n")
                    f.write("\n")
        
        f.write(f"\nFactorization completed in {factorization_time:.2f} seconds.\n")
    
    print("=" * 80)
    print("FACTORIZATION RESULTS")
    print("=" * 80)
    print()
    
    if factorization_results["factorization_success"]:
        print("Factorization successful!")
        print("Factors:")
        for factor in factorization_results["factors"]:
            print(f"- {factor}")
    else:
        print("Factorization unsuccessful")
        print("The factorization attempt did not succeed within the time limit.")
        print()
        if "attempted_approaches" in factorization_results:
            print("Attempted Approaches:")
            for approach, details in factorization_results["attempted_approaches"].items():
                print(f"Approach: {approach}")
                print(f"- Status: {details['status']}")
                print(f"- Execution time: {details['execution_time']:.2f} seconds")
                if "partial_factors" in details and details["partial_factors"]:
                    print("- Partial factors:")
                    for factor in details["partial_factors"]:
                        print(f"  - {factor}")
                print()
    
    print()
    print(f"Factorization completed in {factorization_time:.2f} seconds.")
    print()
    print(f"Results saved to challenge_factorization_results.json")
    print(f"Summary saved to challenge_factorization_summary.md")
    
    # Try direct factorization using sympy as a backup
    try_sympy_factorization(challenge_number)
    
    print()
    print("Test complete!")

def try_sympy_factorization(number_str):
    """
    Try to factorize the number using sympy's direct factorization methods.
    This is a backup approach in case our specialized methods don't work.
    
    Args:
        number_str: The number to factorize as a string
    """
    print("=" * 80)
    print("SYMPY FACTORIZATION ATTEMPT")
    print("=" * 80)
    print()
    
    print("Attempting direct factorization using sympy...")
    
    # Convert to integer
    n = int(number_str)
    
    # Try basic tests first
    if sympy.isprime(n):
        print("The number is prime according to sympy!")
        return
    
    # Try to find small factors first
    for i in range(2, 1000):
        if n % i == 0:
            print(f"Found factor: {i}")
            print(f"Complementary factor: {n // i}")
            
            # Check if the complementary factor is prime
            if sympy.isprime(n // i):
                print(f"The complementary factor is prime!")
            else:
                print(f"The complementary factor is composite.")
            
            return
    
    # Try sympy's factorization
    try:
        print("Attempting sympy factorization (this may take a while)...")
        factorization_start_time = time.time()
        factors = sympy.factorint(n, limit=10000)  # Set a reasonable limit
        factorization_end_time = time.time()
        
        print(f"Factorization completed in {factorization_end_time - factorization_start_time:.2f} seconds.")
        print("Factors:")
        for base, exp in factors.items():
            print(f"- {base}^{exp}")
    except Exception as e:
        print(f"Sympy factorization failed: {e}")
        print("The number may be too large for direct factorization.")

if __name__ == "__main__":
    main()
