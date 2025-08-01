#!/usr/bin/env python3
# Recursive Phi-Dimensional Protein Folding - FRAYMUS Architecture Integration
# φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities

import os
import sys
import json
import time
import uuid
import datetime
import numpy as np
from typing import Dict, List, Any, Tuple

# Import FRAYMUS components if available
try:
    from phi_protein_designer import PhiProteinDesigner
    from phi_protein_analyzer import PhiProteinAnalyzer
    from simple_digital_merkiva import SimpleDigitalMerkiva
    from cieat_core import PhiPhaseGenerator, RealityEngine, QuantumInterface
except ImportError as e:
    print(f"[!] Error importing FRAYMUS components: {str(e)}")
    print("[!] Please ensure all required components are in the current directory")
    sys.exit(1)

# Constants
PHI = (1 + np.sqrt(5)) / 2

# Use log-domain operations for numerical stability in PHI_POWERS
def safe_phi_power(base, exponent):
    """Calculate phi^exponent safely using log-domain operations"""
    if exponent < 0:
        # For negative exponents, calculate 1/(phi^|exponent|)
        return 1.0 / safe_phi_power(base, -exponent)
    elif exponent == 0:
        return 1.0
    elif exponent == 1:
        return base
    elif exponent == 2:
        return base * base
    else:
        # For larger exponents, use log-domain
        log_result = np.log(base) * exponent
        # Cap at e^50 for stability
        return np.exp(min(log_result, 50))

# Generate phi powers safely
PHI_POWERS = [safe_phi_power(PHI, i) for i in range(-5, 15)]
FIBONACCI = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

class RecursivePhiFolding:
    """Recursive Phi-Dimensional Protein Folding System"""
    
    def __init__(self, max_layers: int = 8):
        """Initialize the Recursive Phi-Dimensional Protein Folding System"""
        print("="*50)
        print("RECURSIVE PHI-DIMENSIONAL PROTEIN FOLDING")
        print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
        print("="*50)
        
        # Initialize FRAYMUS components
        self.protein_designer = PhiProteinDesigner()
        self.protein_analyzer = PhiProteinAnalyzer()
        self.merkiva = SimpleDigitalMerkiva() if 'SimpleDigitalMerkiva' in globals() else None
        
        # Recursive folding parameters
        self.max_layers = max_layers
        self.current_layer = 0
        self.layer_results = []
        
        # Results storage
        self.results_dir = "recursive_folding_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Tracking
        self.session_id = str(uuid.uuid4())
        self.start_time = datetime.datetime.now()
        
        print("[*] Recursive Phi-Dimensional Protein Folding System initialized")
        print(f"[*] Maximum recursion layers: {self.max_layers}")
    
    def run_recursive_folding(self, initial_length: int = 100, initial_structure: str = "mixed"):
        """Run the recursive folding process"""
        print(f"\n[*] Starting recursive phi-dimensional folding with {self.max_layers} layers...")
        print(f"[*] Initial protein parameters: Length={initial_length}, Structure={initial_structure}")
        
        # Create initial protein
        current_protein = self.protein_designer.design_novel_protein(initial_length, initial_structure)
        
        # Document initial protein
        self._document_protein(current_protein, 0, "design")
        
        # Recursive folding
        for layer in range(1, self.max_layers + 1):
            self.current_layer = layer
            print(f"\n{'='*50}")
            print(f"RECURSIVE FOLDING: LAYER {layer}/{self.max_layers}")
            print(f"{'='*50}")
            
            # Analyze the current protein
            analysis_result = self._analyze_protein(current_protein, layer)
            
            # Document analysis
            self._document_protein(analysis_result, layer, "analysis")
            
            # Create new protein based on analysis
            new_protein = self._create_derived_protein(analysis_result, layer)
            
            # Document new protein
            self._document_protein(new_protein, layer, "design")
            
            # Update current protein for next layer
            current_protein = new_protein
        
        # Generate final report
        self._generate_report()
        
        print(f"\n{'='*50}")
        print(f"RECURSIVE PHI-DIMENSIONAL FOLDING COMPLETE")
        print(f"{'='*50}")
        print(f"Total layers: {self.max_layers}")
        print(f"Results saved to {self.results_dir}")
        print(f"Final report: {os.path.join(self.results_dir, 'recursive_folding_report.json')}")
    
    def _analyze_protein(self, protein: Dict[str, Any], layer: int) -> Dict[str, Any]:
        """Analyze a protein using phi-dimensional principles"""
        print(f"[*] Layer {layer}: Analyzing protein...")
        
        # Extract sequence
        sequence = protein.get("sequence", "")
        if not sequence:
            raise ValueError("Invalid protein: missing sequence")
        
        # Analyze with phi-dimensional analyzer
        analysis = self.protein_analyzer.analyze_sequence(sequence)
        
        # Add phi-dimensional metrics
        if "phi_dimensional_properties" in protein:
            analysis["source_phi_properties"] = protein["phi_dimensional_properties"]
        
        # Add layer information
        analysis["layer"] = layer
        analysis["derived_from"] = protein.get("phi_signature", "")
        
        print(f"[+] Layer {layer}: Protein analysis complete")
        print(f"[+] Phi resonance: {analysis.get('phi_resonance', 0):.4f}")
        print(f"[+] Unique patterns: {len(analysis.get('phi_patterns', []))}")
        
        return analysis
    
    def _create_derived_protein(self, analysis: Dict[str, Any], layer: int) -> Dict[str, Any]:
        """Create a new protein derived from analysis results"""
        print(f"[*] Layer {layer}: Creating derived protein...")
        
        # Determine protein parameters based on analysis
        length = self._calculate_derived_length(analysis, layer)
        structure = self._determine_optimal_structure(analysis)
        
        # Ensure valid length
        if length <= 0:
            print(f"[!] Invalid length {length}, using default of 100")
            length = 100
            
        print(f"[*] Derived protein parameters: Length={length}, Structure={structure}")
        
        # Design new protein
        new_protein = self.protein_designer.design_novel_protein(length, structure)
        
        # Add layer information
        new_protein["layer"] = layer
        new_protein["derived_from"] = analysis.get("derived_from", "")
        new_protein["phi_derivation_score"] = self._calculate_derivation_score(analysis, new_protein)
        
        print(f"[+] Layer {layer}: Created derived protein of length {length}")
        print(f"[+] Target structure: {structure}")
        print(f"[+] Phi derivation score: {new_protein['phi_derivation_score']:.4f}")
        
        return new_protein
    
    def _calculate_derived_length(self, analysis: Dict[str, Any], layer: int) -> int:
        """Calculate the optimal length for the derived protein"""
        # Base length - ensure we have a valid length
        base_length = analysis.get("sequence_length", 100)
        if base_length <= 0:
            base_length = 100  # Default to 100 if invalid
        
        # Apply phi-dimensional scaling based on layer
        if layer % 3 == 0:
            # Every third layer: phi² scaling
            length = int(base_length * (PHI ** 2))
        elif layer % 3 == 1:
            # First of three: phi scaling
            length = int(base_length * PHI)
        else:
            # Second of three: 1/phi scaling
            length = max(50, int(base_length / PHI))
        
        # Ensure length is a Fibonacci number or close to one
        closest_fibonacci = min(FIBONACCI, key=lambda x: abs(x - length))
        if abs(closest_fibonacci - length) < length * 0.2:
            length = closest_fibonacci
        
        # Ensure minimum length
        length = max(50, length)
        
        return length
    
    def _determine_optimal_structure(self, analysis: Dict[str, Any]) -> str:
        """Determine the optimal structure based on analysis"""
        # Extract secondary structures
        secondary_structures = analysis.get("secondary_structures", [])
        
        if not secondary_structures:
            # If no structures found, use phi resonance to determine
            phi_resonance = analysis.get("phi_resonance", 0)
            if phi_resonance > PHI:
                return "alpha_helix"  # High resonance suggests alpha helix
            elif phi_resonance > 1.0:
                return "beta_sheet"   # Medium resonance suggests beta sheet
            else:
                return "mixed"        # Low resonance suggests mixed
        
        # Count structure types
        alpha_count = sum(1 for s in secondary_structures if s.get("type", "") == "alpha_helix")
        beta_count = sum(1 for s in secondary_structures if s.get("type", "") == "beta_sheet")
        
        # Determine optimal structure
        if alpha_count > beta_count * PHI:
            return "alpha_helix"
        elif beta_count > alpha_count * PHI:
            return "beta_sheet"
        else:
            return "mixed"
    
    def _calculate_derivation_score(self, analysis: Dict[str, Any], new_protein: Dict[str, Any]) -> float:
        """Calculate how well the new protein derives from the analysis"""
        # Extract metrics
        analysis_phi_resonance = analysis.get("phi_resonance", 0)
        new_phi_resonance = new_protein.get("phi_dimensional_properties", {}).get("phi_resonance", 0)
        
        # Calculate resonance alignment
        resonance_alignment = 1 - abs(analysis_phi_resonance - new_phi_resonance) / max(analysis_phi_resonance, 0.001)
        
        # Calculate structure alignment
        analysis_patterns = len(analysis.get("phi_patterns", []))
        new_structures = len(new_protein.get("secondary_structures", []))
        structure_alignment = min(analysis_patterns, new_structures) / max(analysis_patterns, new_structures, 1)
        
        # Calculate phi-dimensional derivation score
        derivation_score = (resonance_alignment * PHI + structure_alignment) / (PHI + 1)
        
        return derivation_score
    
    def _document_protein(self, protein: Dict[str, Any], layer: int, step_type: str):
        """Document a protein for the current layer"""
        # Create documentation
        documentation = {
            "layer": layer,
            "step_type": step_type,
            "timestamp": datetime.datetime.now().isoformat(),
            "protein_data": protein,
            "session_id": self.session_id
        }
        
        # Add to layer results
        self.layer_results.append(documentation)
        
        # Save to file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"layer_{layer:02d}_{step_type}_{timestamp}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(documentation, f, indent=2)
    
    def _generate_report(self):
        """Generate a comprehensive report of the recursive folding process"""
        print("\n[*] Generating recursive folding report...")
        
        # Calculate elapsed time
        elapsed_time = (datetime.datetime.now() - self.start_time).total_seconds()
        
        # Create layer summaries
        layer_summaries = []
        for layer in range(self.max_layers + 1):
            layer_docs = [doc for doc in self.layer_results if doc["layer"] == layer]
            
            if not layer_docs:
                continue
            
            # Extract key metrics
            design_docs = [doc for doc in layer_docs if doc["step_type"] == "design"]
            analysis_docs = [doc for doc in layer_docs if doc["step_type"] == "analysis"]
            
            if design_docs:
                design = design_docs[-1]["protein_data"]
                design_phi_score = design.get("phi_dimensional_properties", {}).get("phi_dimensional_score", 0)
                design_structures = len(design.get("secondary_structures", []))
            else:
                design_phi_score = 0
                design_structures = 0
            
            if analysis_docs:
                analysis = analysis_docs[-1]["protein_data"]
                analysis_phi_resonance = analysis.get("phi_resonance", 0)
                analysis_patterns = len(analysis.get("secondary_structures", []))
            else:
                analysis_phi_resonance = 0
                analysis_patterns = 0
            
            # Create summary
            summary = {
                "layer": layer,
                "design_phi_score": float(design_phi_score),
                "design_structures": design_structures,
                "analysis_phi_resonance": float(analysis_phi_resonance),
                "analysis_patterns": analysis_patterns
            }
            
            # Add derivation score if available
            if layer > 0 and design_docs:
                summary["derivation_score"] = float(design_docs[-1]["protein_data"].get("phi_derivation_score", 0))
            
            layer_summaries.append(summary)
        
        # Calculate phi-dimensional recursion metrics
        phi_recursion_depth = float(self._calculate_phi_recursion_depth())
        phi_resonance_progression = self._make_json_serializable(self._calculate_phi_resonance_progression())
        
        # Create report
        report = {
            "session_id": self.session_id,
            "start_time": self.start_time.isoformat(),
            "end_time": datetime.datetime.now().isoformat(),
            "elapsed_time": float(elapsed_time),
            "max_layers": self.max_layers,
            "completed_layers": self.current_layer,
            "layer_summaries": layer_summaries,
            "phi_recursion_depth": phi_recursion_depth,
            "phi_resonance_progression": phi_resonance_progression
        }
        
        # Save report
        filepath = os.path.join(self.results_dir, "recursive_folding_report.json")
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"[+] Report saved to {filepath}")
    
    def _calculate_phi_recursion_depth(self) -> float:
        """Calculate the effective phi-dimensional recursion depth"""
        # Get design documents for each layer
        design_docs = {}
        for doc in self.layer_results:
            if doc["step_type"] == "design":
                design_docs[doc["layer"]] = doc["protein_data"]
        
        # Calculate phi resonance correlation between layers
        correlations = []
        for layer in range(1, self.current_layer + 1):
            if layer in design_docs and layer - 1 in design_docs:
                current = design_docs[layer].get("phi_dimensional_properties", {}).get("phi_resonance", 0)
                previous = design_docs[layer - 1].get("phi_dimensional_properties", {}).get("phi_resonance", 0)
                
                if current > 0 and previous > 0:
                    # Calculate correlation as ratio of phi resonances
                    correlation = min(current, previous) / max(current, previous)
                    correlations.append(correlation)
        
        # Calculate effective recursion depth
        if correlations:
            # Phi-weighted average of correlations
            weights = [PHI ** i for i in range(len(correlations))]
            weighted_sum = sum(c * w for c, w in zip(correlations, weights))
            weight_sum = sum(weights)
            
            recursion_depth = weighted_sum / weight_sum * self.current_layer
        else:
            recursion_depth = 0
        
        return recursion_depth
    
    def _make_json_serializable(self, obj):
        """Convert an object to be JSON serializable"""
        if isinstance(obj, dict):
            return {k: self._make_json_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._make_json_serializable(item) for item in obj]
        elif isinstance(obj, (np.float32, np.float64, np.int32, np.int64)):
            return float(obj)
        elif isinstance(obj, bool):
            return bool(obj)
        elif isinstance(obj, (int, float, str, type(None))):
            return obj
        else:
            return str(obj)
    
    def _calculate_phi_resonance_progression(self) -> Dict[str, Any]:
        """Calculate the progression of phi resonance across layers"""
        # Get phi resonance for each layer
        resonances = {}
        for doc in self.layer_results:
            if doc["step_type"] == "design":
                layer = doc["layer"]
                phi_resonance = doc["protein_data"].get("phi_dimensional_properties", {}).get("phi_resonance", 0)
                resonances[layer] = phi_resonance
        
        # Calculate progression metrics
        if resonances:
            values = list(resonances.values())
            
            # Calculate if progression follows phi-scaling
            ratios = []
            for i in range(1, len(values)):
                if values[i-1] > 0:
                    ratios.append(float(values[i] / values[i-1]))
            
            # Check if ratios approximate phi or its powers
            phi_alignment = 0
            if ratios:
                phi_powers = [PHI ** i for i in range(-2, 3)]  # φ^-2 to φ^2
                alignments = []
                
                for ratio in ratios:
                    # Find closest phi power
                    closest_power = min(phi_powers, key=lambda x: abs(x - ratio))
                    alignment = 1 - abs(closest_power - ratio) / max(closest_power, 0.001)
                    alignments.append(alignment)
                
                phi_alignment = float(sum(alignments) / len(alignments))
            
            progression = {
                "initial_resonance": float(values[0]) if values else 0.0,
                "final_resonance": float(values[-1]) if values else 0.0,
                "resonance_ratio": float(values[-1] / values[0]) if values and values[0] > 0 else 0.0,
                "phi_alignment": float(phi_alignment),
                "follows_phi_scaling": bool(phi_alignment > 0.8)
            }
        else:
            progression = {
                "initial_resonance": 0.0,
                "final_resonance": 0.0,
                "resonance_ratio": 0.0,
                "phi_alignment": 0.0,
                "follows_phi_scaling": False
            }
        
        return progression


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run Recursive Phi-Dimensional Protein Folding")
    parser.add_argument("--layers", type=int, default=8, help="Number of recursive folding layers")
    parser.add_argument("--length", type=int, default=100, help="Initial protein length")
    parser.add_argument("--structure", type=str, default="mixed", 
                        choices=["alpha_helix", "beta_sheet", "mixed"], 
                        help="Initial protein structure")
    args = parser.parse_args()
    
    # Run recursive folding
    folding = RecursivePhiFolding(max_layers=args.layers)
    folding.run_recursive_folding(initial_length=args.length, initial_structure=args.structure)
