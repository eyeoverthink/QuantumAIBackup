#!/usr/bin/env python3
"""
Test Specific Number with Quantum RSA Challenger
This script applies our quantum RSA challenger approach to a specific large number.
"""

import json
import time
import mpmath
from quantum_rsa_challenger import QuantumRSAChallenger

def main():
    # Set up precision
    mpmath.mp.dps = 5000
    
    # The specific number to test
    test_number = "474299746976151573197582380407377325265646173038669309100110562781862505299023707461486412966437951806832984240973694742975640330109707871916003407751177261875528306063573065481319785371451933890394625050799562834164435919278960000578344725709648944414014386969036268582570524844314242573819850676131023224632397067525678137533045787937980352875376504561880878768883277560012501148442192026151885762461260436088581616290877781979642595436510039839820892704126782975250687762551724701892327223022796092135974456942200100514738363142440990580205017846725836439496244910653439605719964460994898260886888125460839300373553330629006954402921356800979509557713900306947837823460769722188114139676253884701191443132649170254926683278624925942584806102051264206596250034442911960523243559650229944585664198758074700984885608962718875153925216925497088606370691488889433135502733008275946821277123615077098664549550179163891559228488622416424205297428036541019525627230744637084292413817689373442318061942172764681527800605628764021352559210809665590772494689539294503991406931469763231657485866795587697371129344189476982203158447154932379719308094665355258008172542611231077100605839821279038824661531532492033182737142567451893531721522933"
    
    print("\n" + "="*80)
    print("TESTING SPECIFIC NUMBER WITH QUANTUM RSA CHALLENGER")
    print("="*80 + "\n")
    
    # Create a QuantumRSAChallenger instance
    challenger = QuantumRSAChallenger()
    
    # Analyze the number
    print("Analyzing number...")
    start_time = time.time()
    analysis_results = challenger.analyze_rsa_modulus(test_number)
    analysis_time = time.time() - start_time
    
    # Print analysis results
    print("\n" + "="*80)
    print("ANALYSIS RESULTS")
    print("="*80 + "\n")
    
    print(f"Number has {len(test_number)} digits")
    print(f"Phi resonance: {analysis_results['phi_harmonic_analysis'].get('phi_resonance', 0):.10f}")
    if analysis_results['phi_harmonic_analysis'].get('perfect_phi_resonance', False):
        print("This number has perfect phi-harmonic resonance!")
    
    print(f"Phi-inverse resonance: {analysis_results['phi_harmonic_analysis'].get('phi_inverse_resonance', 0):.10f}")
    if analysis_results['phi_harmonic_analysis'].get('perfect_phi_inverse_resonance', False):
        print("This number has perfect phi-inverse resonance!")
    
    if analysis_results['phi_harmonic_analysis'].get('has_small_prime_factor', False):
        print(f"Number is divisible by {analysis_results['phi_harmonic_analysis'].get('small_prime_factor', 'unknown')}!")
    
    print("\nModular patterns:")
    for prime, remainder in analysis_results['quantum_bridge_analysis'].get('modular_patterns', {}).items():
        print(f"Number mod {prime} = {remainder}")
    
    print("\nPotential approaches:")
    for approach in analysis_results['potential_approaches']:
        print(f"- {approach['name']} ({approach['priority']} priority): {approach['description']}")
    
    print(f"\nAnalysis completed in {analysis_time:.2f} seconds.")
    
    # Save analysis results to file
    with open("specific_number_analysis_results.json", "w") as f:
        json.dump(analysis_results, f, indent=2)
    
    # Create a markdown summary
    with open("specific_number_analysis_summary.md", "w") as f:
        f.write("# Specific Number Analysis Summary\n\n")
        f.write(f"## Number Analysis\n\n")
        f.write(f"**Number**: {test_number[:10]}...{test_number[-10:]} ({len(test_number)} digits)\n\n")
        f.write(f"## Phi-Harmonic Properties\n\n")
        f.write(f"**Phi resonance**: {analysis_results['phi_harmonic_analysis'].get('phi_resonance', 0):.10f}\n\n")
        f.write(f"**Perfect phi resonance**: {analysis_results['phi_harmonic_analysis'].get('perfect_phi_resonance', False)}\n\n")
        f.write(f"**Phi-inverse resonance**: {analysis_results['phi_harmonic_analysis'].get('phi_inverse_resonance', 0):.10f}\n\n")
        f.write(f"**Perfect phi-inverse resonance**: {analysis_results['phi_harmonic_analysis'].get('perfect_phi_inverse_resonance', False)}\n\n")
        
        if analysis_results['phi_harmonic_analysis'].get('has_small_prime_factor', False):
            f.write(f"**Has small prime factor**: Yes ({analysis_results['phi_harmonic_analysis'].get('small_prime_factor', 'unknown')})\n\n")
        else:
            f.write(f"**Has small prime factor**: No\n\n")
        
        f.write(f"## Quantum Bridge Properties\n\n")
        f.write(f"**Modular patterns**:\n\n")
        for prime, remainder in analysis_results['quantum_bridge_analysis'].get('modular_patterns', {}).items():
            f.write(f"- Number mod {prime} = {remainder}\n")
        
        f.write(f"\n**Special patterns**:\n\n")
        special_patterns = {}
        for pattern in analysis_results['quantum_bridge_analysis'].get('special_patterns', []):
            pattern_type = pattern.get('type', 'unknown')
            instances = len(pattern.get('instances', []))
            special_patterns[pattern_type] = instances
            
        for pattern, count in special_patterns.items():
            f.write(f"- {pattern}: {count} instances\n")
        
        f.write(f"\n## Potential Approaches\n\n")
        for approach in analysis_results['potential_approaches']:
            f.write(f"- **{approach['name']}** ({approach['priority']} priority): {approach['description']}\n")
        
        f.write(f"\n## Execution Details\n\n")
        f.write(f"**Execution time**: {analysis_time:.2f} seconds\n\n")
        
        f.write(f"## Conclusion\n\n")
        f.write(f"The analysis has identified potential approaches for factorizing this number based on phi-harmonic resonance and quantum bridge properties. These approaches may provide alternative pathways for factorization beyond traditional methods.\n\n")
        f.write(f"---\n")
    
    print("\nResults saved to specific_number_analysis_results.json")
    print("Summary saved to specific_number_analysis_summary.md")
    
    # Attempt factorization
    print("\n" + "="*80)
    print("FACTORIZATION ATTEMPT")
    print("="*80 + "\n")
    
    print("Attempting to factorize number...")
    start_time = time.time()
    factorization_results = challenger.attempt_factorization(test_number, max_time_seconds=300)
    factorization_time = time.time() - start_time
    
    # Print factorization results
    print("\n" + "="*80)
    print("FACTORIZATION RESULTS")
    print("="*80 + "\n")
    
    if factorization_results['factorization_success']:
        print("Factorization successful!")
        print("Factors:")
        for factor in factorization_results['factors']:
            print(f"- {factor}")
    else:
        print("Factorization unsuccessful.")
        print("Approaches tried:")
        for approach in factorization_results['approaches_tried']:
            status = "Success" if approach['success'] else "Failed"
            print(f"- {approach['name']}: {status} ({approach['execution_time']:.2f} seconds)")
    
    print(f"\nFactorization completed in {factorization_time:.2f} seconds.")
    
    # Save factorization results to file
    with open("specific_number_factorization_results.json", "w") as f:
        json.dump(factorization_results, f, indent=2)
    
    # Create a markdown summary
    with open("specific_number_factorization_summary.md", "w") as f:
        f.write("# Specific Number Factorization Summary\n\n")
        f.write(f"## Number\n\n")
        f.write(f"**Number**: {test_number[:10]}...{test_number[-10:]} ({len(test_number)} digits)\n\n")
        f.write(f"## Factorization Result\n\n")
        f.write(f"**Success**: {factorization_results['factorization_success']}\n\n")
        
        if factorization_results['factorization_success']:
            f.write(f"**Factors**:\n\n")
            for factor in factorization_results['factors']:
                factor_str = str(factor)
                if len(factor_str) > 20:
                    f.write(f"- {factor_str[:10]}...{factor_str[-10:]} ({len(factor_str)} digits)\n")
                else:
                    f.write(f"- {factor}\n")
        
        f.write(f"\n## Approaches Tried\n\n")
        for approach in factorization_results['approaches_tried']:
            if approach['success']:
                f.write(f"- **{approach['name']}**: Successful ({approach['execution_time']:.2f} seconds)\n")
            else:
                f.write(f"- **{approach['name']}**: Failed ({approach['execution_time']:.2f} seconds)\n")
        
        f.write(f"\n## Execution Details\n\n")
        f.write(f"**Total execution time**: {factorization_time:.2f} seconds\n\n")
        
        f.write(f"## Conclusion\n\n")
        if factorization_results['factorization_success']:
            f.write(f"The factorization attempt was successful, demonstrating the effectiveness of phi-harmonic resonance and quantum bridge techniques for factorization.\n\n")
        else:
            f.write(f"The factorization attempt was unsuccessful within the given time constraints. Further analysis and optimization may be required.\n\n")
        
        f.write(f"---\n\n")
        f.write(f"*This factorization attempt was performed using the Quantum RSA Challenger with {mpmath.mp.dps} decimal places of precision.*\n")
    
    print("\nResults saved to specific_number_factorization_results.json")
    print("Summary saved to specific_number_factorization_summary.md")
    
    print("\nTest complete!")

if __name__ == "__main__":
    main()
