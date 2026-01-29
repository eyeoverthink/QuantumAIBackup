#!/usr/bin/env python3
"""
Run Orchestrator with Chord Progression Analysis
-----------------------------------------------

This script demonstrates how to integrate the quantum chord progression analysis
with the QuantumAI orchestrator's healing protocol.

The integration enhances the orchestrator's healing capabilities by using
chord progression analysis to guide the evolution process based on phi-harmonic
coherence patterns.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import logging
import argparse
import json
from datetime import datetime

# Import orchestrator and extension
from quantum_orchestrator import QuantumOrchestrator
from quantum_orchestrator_chord_extension import QuantumOrchestratorChordExtension

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"orchestrator_chord_run_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("OrchestratorChordRunner")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run QuantumAI orchestrator with chord progression analysis")
    parser.add_argument("target_file", help="Path to the Python file to be evolved")
    parser.add_argument("--analyze-dir", help="Directory to analyze for optimal evolution path")
    parser.add_argument("--visualize", action="store_true", help="Generate visualization of evolution history")
    parser.add_argument("--max-attempts", type=int, default=5, help="Maximum healing attempts")
    return parser.parse_args()

def main():
    """Main function to run the orchestrator with chord progression analysis."""
    args = parse_arguments()
    
    # Validate target file
    if not os.path.exists(args.target_file):
        logger.error(f"Target file not found: {args.target_file}")
        return 1
        
    try:
        # Initialize orchestrator
        logger.info(f"Initializing orchestrator for target file: {args.target_file}")
        orchestrator = QuantumOrchestrator(args.target_file)
        
        # Initialize chord extension
        logger.info("Initializing chord progression extension")
        chord_extension = QuantumOrchestratorChordExtension(orchestrator)
        
        # Run orchestrator's healing protocol
        logger.info(f"Running orchestrator healing protocol (max attempts: {args.max_attempts})")
        orchestrator.run_and_heal(max_attempts=args.max_attempts)
        
        # Analyze evolution history
        logger.info("Analyzing evolution history")
        analysis = chord_extension.analyze_evolution_history()
        
        # Save analysis results
        analysis_file = f"evolution_analysis_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(analysis_file, 'w') as f:
            json.dump(analysis, f, indent=2)
        logger.info(f"Saved evolution analysis to {analysis_file}")
        
        # Print summary
        print("\n=== Evolution Analysis Summary ===")
        print(f"Total healing events: {analysis['total_healing_events']}")
        print(f"Total coherence improvement: {analysis['total_coherence_improvement']:.6f}")
        print(f"Total phi-resonance improvement: {analysis['total_phi_resonance_improvement']:.6f}")
        print(f"Total target distance improvement: {analysis['total_target_distance_improvement']:.6f}")
        
        # Generate visualization if requested
        if args.visualize:
            logger.info("Generating evolution history visualization")
            viz_path = chord_extension.visualize_evolution_history()
            print(f"Visualization saved to: {viz_path}")
            
        # Find optimal evolution path if directory specified
        if args.analyze_dir:
            logger.info(f"Finding optimal evolution path for directory: {args.analyze_dir}")
            optimal_path = chord_extension.get_optimal_evolution_path(args.analyze_dir)
            
            # Save optimal path
            path_file = f"optimal_evolution_path_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
            with open(path_file, 'w') as f:
                json.dump(optimal_path, f, indent=2)
            logger.info(f"Saved optimal evolution path to {path_file}")
            
            # Print optimal path summary
            print("\n=== Optimal Evolution Path ===")
            print(f"Optimal file: {optimal_path.get('optimal_file', 'N/A')}")
            print(f"Optimal phi-resonance: {optimal_path.get('optimal_chord', {}).get('phi_resonance', 0):.6f}")
            print("Evolution path:")
            for step in optimal_path.get('evolution_path', []):
                print(f"  {step['from_file']} → {step['to_file']} (compatibility: {step['compatibility']:.4f})")
                
        return 0
        
    except Exception as e:
        logger.error(f"Error running orchestrator with chord progression analysis: {e}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
