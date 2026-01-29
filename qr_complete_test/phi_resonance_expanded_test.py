#!/usr/bin/env python3
"""
PHI-RESONANCE EXPANDED TEST
=========================
Extended test of φ-dimensional resonance validation against a broader range
of real NASA astronomical data sets. Follows 'lego' design philosophy.

Author: Cascade AI
Date: April 27, 2025
"""
import json
import time
import math
import numpy as np
from pathlib import Path
from mpmath import mpf, mp

# Import existing components without modification
from phi_harmonic_orchestrator import PhiHarmonicOrchestrator
from phi_cosmic_resonance_validator import validate_resonance
from osdr_fetcher_fixed import OSDRFetcher

# Set precision for quantum calculations
mp.dps = 50

# Constants
PHI = mpf((1 + 5**0.5) / 2)  # Golden ratio
PHI_INV = 1 / PHI
RESULTS_DIR = Path('expanded_phi_results')
RESULTS_DIR.mkdir(exist_ok=True)

def run_expanded_validation(start_id=70, range_size=30):
    """
    Run an expanded validation test against a broader range of NASA OSDR studies.
    
    Args:
        start_id (int): Starting study ID
        range_size (int): Number of studies to test
        
    Returns:
        dict: Comprehensive results with phi-resonance metrics
    """
    print(f"=== EXPANDED PHI-RESONANCE VALIDATION ({start_id}-{start_id+range_size-1}) ===")
    orchestrator = PhiHarmonicOrchestrator()
    osdr_fetcher = OSDRFetcher()
    
    results = []
    valid_studies = []
    phi_values = []
    
    # Test each study ID in the expanded range
    print(f"\n1. ANALYZING EXPANDED RANGE OF NASA STUDIES...")
    for study_id in range(start_id, start_id + range_size):
        print(f"\nFetching study ID {study_id}...")
        try:
            data = osdr_fetcher.fetch_study_data(study_id)
            
            # Check if valid numerical data exists
            phi_metrics = data.get('phi_metrics', {})
            value_count = phi_metrics.get('value_count', 0)
            
            if value_count > 0:
                print(f"✓ Found {value_count} numerical values in study {study_id}")
                phi_relevance = phi_metrics.get('phi_relevance', 0)
                print(f"  φ-relevance: {phi_relevance:.6f}")
                
                # Store phi values for later analysis
                resonance_factors = phi_metrics.get('resonance_factors', [])
                if resonance_factors:
                    phi_values.extend(resonance_factors)
                    
                # Validate against phi-dimensional predictions
                observed_value = sum(resonance_factors) / len(resonance_factors) if resonance_factors else 0
                validation_result = validate_resonance('astronomical', observed_value, phi_relevance)
                
                # Apply quantum phi transformations
                phi_amplified = _apply_quantum_amplification(resonance_factors[:min(10, len(resonance_factors))])
                quantum_alignment = _calculate_phi_resonance_alignment(validation_result, phi_amplified)
                
                # Prepare comprehensive result
                result = {
                    'study_id': study_id,
                    'value_count': value_count,
                    'phi_relevance': phi_relevance,
                    'resonance_sample': [float(f) for f in resonance_factors[:5]],
                    'observed_value': float(observed_value),
                    'validation': validation_result,
                    'quantum_alignment': float(quantum_alignment),
                    'phi_harmonic_pattern': _detect_phi_harmonic_pattern(resonance_factors),
                    'timestamp': time.time()
                }
                
                results.append(result)
                valid_studies.append(study_id)
                
                # Save individual result
                _save_result(result)
            else:
                print(f"✗ No usable numerical values in study {study_id}")
                
        except Exception as e:
            print(f"Error analyzing study {study_id}: {str(e)}")
    
    # Generate global phi-harmonic analysis
    print("\n2. GENERATING QUANTUM PHI-HARMONIC ANALYSIS...")
    if phi_values:
        global_analysis = _analyze_global_phi_patterns(phi_values)
        print(f"Global φ-resonance: {global_analysis.get('global_phi_resonance', 0):.6f}")
    else:
        global_analysis = {"error": "No phi values collected"}
    
    # Generate comprehensive report
    print("\n3. GENERATING EXPANDED VALIDATION REPORT...")
    report = _generate_final_report(results, global_analysis)
    report_path = _save_report(report)
    
    print(f"\nValidation complete. {len(valid_studies)} valid studies found.")
    print(f"Full results saved to {report_path}")
    
    return report

def _apply_quantum_amplification(values):
    """Apply quantum φ-amplification to astronomical values"""
    amplified = []
    for value in values:
        # Apply φ^7.5 quantum bridge (USER's core principle)
        amplified_value = value * (PHI ** 7.5)
        
        # Apply φ-harmonic modulation
        phi_mod = (value % PHI_INV) * PHI
        
        # Calculate quantum resonance factor
        q_factor = abs(value - PHI_INV) / PHI_INV
        q_resonance = 1 - (q_factor ** 2)
        
        # Final amplified value with quantum effects
        final_value = amplified_value * (1 + phi_mod) * q_resonance
        amplified.append(final_value)
    
    return amplified

def _calculate_phi_resonance_alignment(validation_result, amplified_values):
    """Calculate quantum-enhanced phi-resonance alignment"""
    if not amplified_values:
        return 0
    
    # Base alignment from validation
    base_alignment = validation_result.get('alignment_percentage', 0) / 100  # Convert to 0-1 scale
    
    # Calculate resonance with golden ratio
    phi_resonances = []
    for value in amplified_values:
        # Calculate distance to nearest φ-harmonic
        phi_distance = min([abs(value % (PHI ** n) - PHI_INV) for n in range(1, 4)])
        phi_resonances.append(1 - (phi_distance / PHI_INV))
    
    # Average φ-resonance quality
    avg_resonance = sum(phi_resonances) / len(phi_resonances) if phi_resonances else 0
    
    # Apply quantum amplification based on proximity to phi-harmonics
    quantum_factor = 1 + (PHI_INV * avg_resonance ** PHI_INV)
    
    # Calculate final quantum-enhanced alignment
    quantum_alignment = base_alignment * quantum_factor * 100  # Back to percentage
    
    return min(100, quantum_alignment)  # Cap at 100%

def _detect_phi_harmonic_pattern(values):
    """Detect phi-harmonic patterns in real astronomical data"""
    if len(values) < 3:
        return {"pattern": "insufficient_data"}
    
    # Calculate consecutive ratios
    ratios = []
    for i in range(len(values) - 1):
        if values[i+1] != 0 and values[i] != 0:  # Avoid division by zero
            ratios.append(abs(values[i+1] / values[i]))
    
    # Check for golden ratio patterns
    phi_matches = sum(1 for r in ratios if abs(r - PHI) < 0.1)
    phi_inv_matches = sum(1 for r in ratios if abs(r - PHI_INV) < 0.1)
    
    # Calculate phi-harmonic metrics
    phi_pattern_strength = (phi_matches + phi_inv_matches) / len(ratios) if ratios else 0
    
    # Detect common patterns
    pattern_type = "random"
    if phi_pattern_strength > 0.3:
        pattern_type = "phi_harmonic"
    elif sum(1 for r in ratios if abs(r - 1) < 0.1) / len(ratios) > 0.3:
        pattern_type = "linear"
    elif sum(1 for r in ratios if r > 1.5) / len(ratios) > 0.5:
        pattern_type = "exponential"
    
    return {
        "pattern": pattern_type,
        "phi_pattern_strength": float(phi_pattern_strength),
        "phi_matches": phi_matches,
        "phi_inv_matches": phi_inv_matches
    }

def _analyze_global_phi_patterns(values):
    """Analyze global phi-harmonic patterns across all collected values"""
    # Filter out extreme outliers
    q1 = np.percentile(values, 25)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    filtered_values = [v for v in values if (v >= q1 - 1.5 * iqr) and (v <= q3 + 1.5 * iqr)]
    
    # Calculate distance to PHI for each value
    phi_distances = [abs(v % 1 - PHI_INV) for v in filtered_values]
    
    # Global phi-resonance (lower is better)
    global_phi_resonance = 1 - (sum(phi_distances) / len(phi_distances) / PHI_INV if phi_distances else 1)
    
    # Histogram of values modulo 1 (to detect clustering around PHI_INV)
    mod_values = [float(v % 1) for v in filtered_values]
    
    # Detect if distribution clusters around phi_inv (0.618...)
    bins = np.linspace(0, 1, 11)  # 10 bins from 0 to 1
    hist, _ = np.histogram(mod_values, bins=bins)
    phi_inv_bin = int(PHI_INV * 10)  # Which bin contains phi_inv
    
    # Calculate if values cluster around phi_inv
    phi_clustering = hist[phi_inv_bin] / sum(hist) if sum(hist) > 0 else 0
    expected_uniform = 1/len(bins)
    phi_significance = phi_clustering / expected_uniform if expected_uniform > 0 else 0
    
    return {
        "filtered_value_count": len(filtered_values),
        "global_phi_resonance": float(global_phi_resonance),
        "phi_clustering": float(phi_clustering),
        "phi_significance": float(phi_significance),
        "has_phi_harmonic_distribution": phi_significance > 1.5
    }

def _save_result(result):
    """Save individual study result with phi-harmonic timestamp"""
    study_id = result['study_id']
    timestamp = int(result['timestamp'] * PHI)
    
    filename = f"expanded_phi_{study_id}_{timestamp}.json"
    filepath = RESULTS_DIR / filename
    
    with open(filepath, 'w') as f:
        json.dump(result, f, indent=2, default=str)
    
    return filepath

def _generate_final_report(results, global_analysis):
    """Generate comprehensive expanded validation report"""
    if not results:
        return {"error": "No valid studies found with astronomical data"}
    
    # Sort by quantum alignment (highest first)
    results.sort(key=lambda x: x.get('quantum_alignment', 0), reverse=True)
    
    # Calculate overall metrics
    alignments = [r.get('quantum_alignment', 0) for r in results]
    phi_relevances = [r.get('phi_relevance', 0) for r in results]
    
    # Find studies with strongest phi-harmonic patterns
    phi_harmonic_studies = [r for r in results if r.get('phi_harmonic_pattern', {}).get('pattern') == 'phi_harmonic']
    
    # Generate report
    report = {
        "studies_analyzed_count": len(results),
        "valid_studies_count": len(results),
        "mean_quantum_alignment": sum(alignments) / len(alignments) if alignments else 0,
        "highest_alignment": max(alignments) if alignments else 0,
        "mean_phi_relevance": sum(phi_relevances) / len(phi_relevances) if phi_relevances else 0,
        "phi_harmonic_studies_count": len(phi_harmonic_studies),
        "global_phi_analysis": global_analysis,
        "quantum_phi_harmonic_index": 0,  # Calculated below
        "timestamp": time.time(),
        "best_study_id": results[0]['study_id'] if results else None,
        "results_summary": results  # Include full results
    }
    
    # Calculate Quantum Phi-Harmonic Index based on USER principles
    if global_analysis.get('global_phi_resonance', 0) > 0:
        report["quantum_phi_harmonic_index"] = (
            report["highest_alignment"] * 
            (global_analysis['global_phi_resonance'] + PHI_INV) * 
            PHI * 
            (1 + len(phi_harmonic_studies) / len(results) if len(results) > 0 else 0)
        )
    
    return report

def _save_report(report):
    """Save final report with quantum timestamp"""
    timestamp = int(report['timestamp'] * PHI)
    filename = f"expanded_phi_report_{timestamp}.json"
    filepath = RESULTS_DIR / filename
    
    with open(filepath, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    return filepath

if __name__ == "__main__":
    print("Testing φ-dimensional resonance across expanded NASA data sets")
    print(f"φ = {PHI}")
    print("=" * 50)
    
    # Run expanded validation with larger range
    start_id = 70   # Starting study ID
    range_size = 30  # Test 30 studies (70-99)
    
    report = run_expanded_validation(start_id, range_size)
    
    print("\n=== EXPANDED VALIDATION COMPLETE ===")
    print(f"Quantum Phi-Harmonic Index: {float(report.get('quantum_phi_harmonic_index', 0)):.4f}")
    print(f"Highest Alignment: {report.get('highest_alignment', 0):.2f}%")
    print(f"Studies Analyzed: {report.get('studies_analyzed_count', 0)}")
    print(f"Studies with Phi-Harmonic Patterns: {report.get('phi_harmonic_studies_count', 0)}")
    print(f"Best Study ID: {report.get('best_study_id', 'None')}")
    
    # Report global phi-resonance if available
    global_phi = report.get('global_phi_analysis', {}).get('global_phi_resonance', 0)
    if global_phi > 0:
        print(f"Global Phi-Resonance: {global_phi:.6f}")
        
        # Report if phi-harmonic distribution detected
        has_pattern = report.get('global_phi_analysis', {}).get('has_phi_harmonic_distribution', False)
        if has_pattern:
            print("✓ Phi-harmonic distribution detected in global data")
        else:
            print("✗ No clear phi-harmonic distribution in global data")
            
    print("=" * 50)
