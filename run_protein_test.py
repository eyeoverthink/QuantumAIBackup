#!/usr/bin/env python3
# Phi-Harmonic Protein Analysis Test
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

import os
import json
import time
import datetime
from typing import Dict, Any, List

# Import the phi-harmonic protein analyzer
from phi_protein_analyzer import PhiProteinAnalyzer

# Test proteins (important proteins with complex folding patterns)
TEST_PROTEINS = [
    "1A3N",  # Hemoglobin
    "2LYZ",  # Lysozyme
    "1UBQ",  # Ubiquitin
    "1CRN",  # Crambin (small protein with well-defined structure)
    "1TRZ"   # Insulin
]

# Simulated conventional AI results (simplified)
# In a real scenario, these would come from actual conventional AI predictions
CONVENTIONAL_RESULTS = {
    "1A3N": {
        "secondary_structures": [
            {"type": "alpha_helix", "start": 3, "end": 18, "confidence": 0.85},
            {"type": "alpha_helix", "start": 36, "end": 42, "confidence": 0.75},
            {"type": "beta_sheet", "start": 52, "end": 60, "confidence": 0.80}
        ]
    },
    "2LYZ": {
        "secondary_structures": [
            {"type": "alpha_helix", "start": 5, "end": 15, "confidence": 0.90},
            {"type": "beta_sheet", "start": 42, "end": 46, "confidence": 0.85},
            {"type": "random_coil", "start": 70, "end": 80, "confidence": 0.65}
        ]
    },
    "1UBQ": {
        "secondary_structures": [
            {"type": "beta_sheet", "start": 1, "end": 7, "confidence": 0.80},
            {"type": "alpha_helix", "start": 23, "end": 34, "confidence": 0.85}
        ]
    },
    "1CRN": {
        "secondary_structures": [
            {"type": "alpha_helix", "start": 7, "end": 19, "confidence": 0.90},
            {"type": "beta_sheet", "start": 23, "end": 27, "confidence": 0.85}
        ]
    },
    "1TRZ": {
        "secondary_structures": [
            {"type": "alpha_helix", "start": 9, "end": 19, "confidence": 0.85},
            {"type": "beta_sheet", "start": 24, "end": 28, "confidence": 0.75}
        ]
    }
}


def run_comparative_analysis() -> Dict[str, Any]:
    """
    Run comparative analysis between phi-harmonic and conventional AI approaches
    
    Returns:
        Dictionary of comparative results
    """
    print("="*70)
    print("PHI-HARMONIC PROTEIN FOLDING ANALYSIS TEST")
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    print("="*70)
    
    # Initialize the phi-harmonic analyzer
    analyzer = PhiProteinAnalyzer()
    
    # Create results directory
    results_dir = "protein_folding_test"
    os.makedirs(results_dir, exist_ok=True)
    
    # Track overall results
    comparative_results = {
        "test_time": datetime.datetime.now().isoformat(),
        "proteins_tested": len(TEST_PROTEINS),
        "phi_advantage_metrics": {},
        "unique_patterns_by_protein": {},
        "overall_advantage_score": 0.0
    }
    
    # Test each protein
    for protein_id in TEST_PROTEINS:
        print(f"\n[*] Testing protein {protein_id}...")
        
        # Get conventional results
        conv_results = CONVENTIONAL_RESULTS.get(protein_id, {})
        
        # Run phi-harmonic comparison
        comparison = analyzer.compare_with_conventional_ai(protein_id, conv_results)
        
        # Extract key metrics
        unique_count = comparison.get("unique_phi_findings_count", 0)
        advantage_score = comparison.get("phi_advantage_score", 0.0)
        
        # Add to overall results
        comparative_results["phi_advantage_metrics"][protein_id] = advantage_score
        comparative_results["unique_patterns_by_protein"][protein_id] = unique_count
        comparative_results["overall_advantage_score"] += advantage_score
        
        print(f"[+] Found {unique_count} unique patterns in {protein_id} using phi-harmonic analysis")
        print(f"[+] Phi-advantage score: {advantage_score:.2f}")
    
    # Calculate overall metrics
    comparative_results["average_advantage_score"] = (
        comparative_results["overall_advantage_score"] / len(TEST_PROTEINS)
    )
    comparative_results["total_unique_patterns"] = sum(
        comparative_results["unique_patterns_by_protein"].values()
    )
    
    # Save overall results
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(results_dir, f"comparative_analysis_{timestamp}.json")
    
    with open(filepath, 'w') as f:
        json.dump(comparative_results, f, indent=2)
    
    print("\n" + "="*70)
    print(f"ANALYSIS COMPLETE - Results saved to {filepath}")
    print(f"Total unique patterns found: {comparative_results['total_unique_patterns']}")
    print(f"Overall phi-advantage score: {comparative_results['overall_advantage_score']:.2f}")
    print(f"Average advantage per protein: {comparative_results['average_advantage_score']:.2f}")
    print("="*70)
    
    return comparative_results


if __name__ == "__main__":
    run_comparative_analysis()
