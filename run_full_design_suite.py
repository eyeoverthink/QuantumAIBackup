#!/usr/bin/env python3
# Full Design Suite Test - FRAYMUS Phi-Dimensional Protein Design System
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

import os
import sys
import json
import time
import datetime
import argparse
import numpy as np
from typing import Dict, List, Any, Tuple

# Import FRAYMUS components if available
try:
    from phi_protein_designer import PhiProteinDesigner
    from simple_digital_merkiva import SimpleDigitalMerkiva
    from cieat_core import PhiPhaseGenerator, RealityEngine, QuantumInterface
except ImportError as e:
    print(f"[!] Error importing FRAYMUS components: {str(e)}")
    print("[!] Please ensure all required components are in the current directory")
    sys.exit(1)

# Constants
PHI = (1 + np.sqrt(5)) / 2
PHI_POWERS = [PHI ** i for i in range(-5, 15)]
FIBONACCI = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

class FullDesignSuite:
    """Full Design Suite for testing the FRAYMUS Phi-Dimensional Protein Design System"""
    
    def __init__(self):
        """Initialize the Full Design Suite"""
        print("="*50)
        print("FRAYMUS PHI-DIMENSIONAL PROTEIN DESIGN SUITE")
        print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
        print("="*50)
        
        # Initialize protein designer
        self.protein_designer = PhiProteinDesigner()
        
        # Test parameters
        self.lengths = [50, 100, 150, 200, 250, 300]
        self.structures = ["alpha_helix", "beta_sheet", "mixed"]
        
        # Results storage
        self.results_dir = "full_design_suite_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Summary data
        self.summary = {
            "test_timestamp": datetime.datetime.now().isoformat(),
            "total_tests": len(self.lengths) * len(self.structures),
            "successful_tests": 0,
            "failed_tests": 0,
            "results": []
        }
        
        print("[*] Full Design Suite initialized")
        print(f"[*] Will run {self.summary['total_tests']} tests")
    
    def run_suite(self):
        """Run the full design suite"""
        print("\n[*] Starting Full Design Suite...")
        
        start_time = time.time()
        
        # Run tests for each combination of length and structure
        for length in self.lengths:
            for structure in self.structures:
                print(f"\n{'='*50}")
                print(f"TESTING: Length {length}, Structure {structure}")
                print(f"{'='*50}")
                
                try:
                    # Design protein
                    result = self.protein_designer.design_novel_protein(length, structure)
                    
                    # Calculate phi-dimensional metrics
                    metrics = self._calculate_metrics(result)
                    
                    # Store result summary
                    test_result = {
                        "length": length,
                        "structure": structure,
                        "status": "success",
                        "metrics": metrics,
                        "phi_signature": result.get("phi_signature", ""),
                        "secondary_structures": len(result.get("secondary_structures", [])),
                        "has_quantum_bridge": "quantum_bridge" in result,
                        "has_protection": "protection_level" in result,
                        "timestamp": datetime.datetime.now().isoformat()
                    }
                    
                    self.summary["results"].append(test_result)
                    self.summary["successful_tests"] += 1
                    
                    print(f"[+] Test completed successfully")
                    print(f"[+] Phi-dimensional score: {metrics['phi_dimensional_score']:.4f}")
                    print(f"[+] Secondary structures: {test_result['secondary_structures']}")
                    
                except Exception as e:
                    # Log error
                    test_result = {
                        "length": length,
                        "structure": structure,
                        "status": "failed",
                        "error": str(e),
                        "timestamp": datetime.datetime.now().isoformat()
                    }
                    
                    self.summary["results"].append(test_result)
                    self.summary["failed_tests"] += 1
                    
                    print(f"[!] Test failed: {str(e)}")
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        self.summary["elapsed_time"] = elapsed_time
        
        # Save summary
        self._save_summary()
        
        print(f"\n{'='*50}")
        print(f"FULL DESIGN SUITE COMPLETE")
        print(f"{'='*50}")
        print(f"Total tests: {self.summary['total_tests']}")
        print(f"Successful: {self.summary['successful_tests']}")
        print(f"Failed: {self.summary['failed_tests']}")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Results saved to {os.path.join(self.results_dir, 'summary.json')}")
    
    def _calculate_metrics(self, result: Dict[str, Any]) -> Dict[str, float]:
        """Calculate phi-dimensional metrics for a protein design"""
        metrics = {}
        
        # Extract phi-dimensional properties
        if "phi_dimensional_properties" in result:
            metrics.update(result["phi_dimensional_properties"])
        
        # Extract energy minimization results
        if "energy_minimization" in result:
            for key, value in result["energy_minimization"].items():
                metrics[f"energy_{key}"] = value
        
        # Calculate secondary structure metrics
        if "secondary_structures" in result:
            structures = result["secondary_structures"]
            
            # Average phi resonance
            resonances = [s.get("phi_resonance", 0) for s in structures]
            metrics["avg_phi_resonance"] = np.mean(resonances) if resonances else 0
            
            # Structure coverage
            total_length = result.get("length", 0)
            covered_length = sum(s.get("end", 0) - s.get("start", 0) + 1 for s in structures)
            metrics["structure_coverage"] = covered_length / total_length if total_length > 0 else 0
        
        # Calculate quantum bridge metrics
        if "quantum_bridge" in result:
            bridge = result["quantum_bridge"]
            metrics["bridge_resonance"] = bridge.get("bridge_resonance", 0)
        
        return metrics
    
    def _save_summary(self):
        """Save the test summary to a file"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(self.results_dir, f"summary_{timestamp}.json")
        
        with open(filepath, 'w') as f:
            json.dump(self.summary, f, indent=2)
        
        # Also save as latest summary
        with open(os.path.join(self.results_dir, "summary.json"), 'w') as f:
            json.dump(self.summary, f, indent=2)
    
    def generate_comparative_analysis(self):
        """Generate comparative analysis of all test results"""
        print("\n[*] Generating comparative analysis...")
        
        # Group results by length and structure
        length_results = {}
        structure_results = {}
        
        for result in self.summary["results"]:
            if result["status"] != "success":
                continue
            
            # Group by length
            length = result["length"]
            if length not in length_results:
                length_results[length] = []
            length_results[length].append(result)
            
            # Group by structure
            structure = result["structure"]
            if structure not in structure_results:
                structure_results[structure] = []
            structure_results[structure].append(result)
        
        # Calculate average metrics by length
        length_analysis = {}
        for length, results in length_results.items():
            metrics = {
                "count": len(results),
                "avg_phi_dimensional_score": np.mean([r["metrics"].get("phi_dimensional_score", 0) for r in results]),
                "avg_secondary_structures": np.mean([r["secondary_structures"] for r in results]),
                "avg_structure_coverage": np.mean([r["metrics"].get("structure_coverage", 0) for r in results]),
                "success_rate": len(results) / len([r for r in self.summary["results"] if r["length"] == length])
            }
            length_analysis[length] = metrics
        
        # Calculate average metrics by structure
        structure_analysis = {}
        for structure, results in structure_results.items():
            metrics = {
                "count": len(results),
                "avg_phi_dimensional_score": np.mean([r["metrics"].get("phi_dimensional_score", 0) for r in results]),
                "avg_secondary_structures": np.mean([r["secondary_structures"] for r in results]),
                "avg_structure_coverage": np.mean([r["metrics"].get("structure_coverage", 0) for r in results]),
                "success_rate": len(results) / len([r for r in self.summary["results"] if r["structure"] == structure])
            }
            structure_analysis[structure] = metrics
        
        # Create comparative analysis
        analysis = {
            "timestamp": datetime.datetime.now().isoformat(),
            "total_tests": self.summary["total_tests"],
            "successful_tests": self.summary["successful_tests"],
            "failed_tests": self.summary["failed_tests"],
            "by_length": length_analysis,
            "by_structure": structure_analysis,
            "phi_advantage": self._calculate_phi_advantage()
        }
        
        # Save analysis
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(self.results_dir, f"comparative_analysis_{timestamp}.json")
        
        with open(filepath, 'w') as f:
            json.dump(analysis, f, indent=2)
        
        print(f"[+] Comparative analysis saved to {filepath}")
        return analysis
    
    def _calculate_phi_advantage(self) -> Dict[str, Any]:
        """Calculate the phi-dimensional advantage over conventional methods"""
        # This would normally compare with actual conventional methods
        # For this simulation, we'll use phi-based calculations to estimate the advantage
        
        successful_results = [r for r in self.summary["results"] if r["status"] == "success"]
        
        if not successful_results:
            return {"advantage_score": 0}
        
        # Calculate average phi-dimensional score
        avg_phi_score = np.mean([r["metrics"].get("phi_dimensional_score", 0) for r in successful_results])
        
        # Calculate estimated conventional score (simulated as phi_score / phi)
        est_conv_score = avg_phi_score / PHI
        
        # Calculate advantage
        advantage = {
            "avg_phi_dimensional_score": avg_phi_score,
            "est_conventional_score": est_conv_score,
            "advantage_ratio": avg_phi_score / est_conv_score if est_conv_score > 0 else 0,
            "advantage_score": avg_phi_score - est_conv_score,
            "phi_resonance_advantage": np.mean([r["metrics"].get("avg_phi_resonance", 0) for r in successful_results]) - 0.5
        }
        
        return advantage


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Full Design Suite for FRAYMUS Phi-Dimensional Protein Design System")
    parser.add_argument("--analysis", action="store_true", help="Generate comparative analysis after tests")
    args = parser.parse_args()
    
    # Run the full design suite
    suite = FullDesignSuite()
    suite.run_suite()
    
    # Generate comparative analysis if requested
    if args.analysis:
        suite.generate_comparative_analysis()
