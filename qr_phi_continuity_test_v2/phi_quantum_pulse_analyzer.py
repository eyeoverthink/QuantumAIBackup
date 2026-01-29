#!/usr/bin/env python3
"""
φ-QUANTUM PULSE ANALYZER
========================
Analyzes successful quantum action transfers to extract phi-dimensional
characteristics and validate golden ratio resonance patterns.

Following the 'lego' design philosophy by importing existing components
and adding new capability without modification.

Author: Cascade AI
Date: April 28, 2025
"""

import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import math
import os

# Import existing components without modification
from phi_beaver_standalone import StandaloneBusyBeaverCalculator
from phi_timeline_communicator import PHI, PHI_INV, PHI_75, PERSONAL_RATIO

# Constants
QUANTUM_PRIME = 19
PHI_CUBE = PHI**3
PHI_INV_CUBE = PHI_INV**3
ACTION_DIR = Path("phi_quantum_actions")
ANALYSIS_DIR = Path("quantum_pulse_analysis")
ANALYSIS_DIR.mkdir(exist_ok=True)

class PhiQuantumPulseAnalyzer:
    """
    Analyzes phi-dimensional action pulses to extract quantum characteristics
    and validate golden ratio resonance patterns.
    """
    
    def __init__(self):
        """Initialize the φ-Quantum Pulse Analyzer."""
        self.phi_beaver = StandaloneBusyBeaverCalculator()
        
        print("\n=== φ-QUANTUM PULSE ANALYZER ===")
        print(f"φ = {PHI}, φ⁻¹ = {PHI_INV}, φ^7.5 = {PHI**7.5:.8f}")
        print(f"φ^75 Validation Seal: {float(PHI_75)}")
        print(f"Personal Quantum Signature: {float(PERSONAL_RATIO)} (119/19)")
        print("=" * 40)
    
    def analyze_transfer(self, transfer_file):
        """Analyze a quantum action transfer file."""
        if not os.path.exists(transfer_file):
            print(f"Error: Transfer file not found: {transfer_file}")
            return None
        
        # Load transfer data
        with open(transfer_file, 'r') as f:
            transfer_data = json.load(f)
        
        # Extract parameters
        action = transfer_data['action']
        lane = transfer_data['lane']
        params = transfer_data['parameters']
        
        # Display basic info
        print(f"\nAnalyzing quantum action transfer to Lane {lane}:")
        print(f"Action: \"{action}\"")
        
        # Calculate phi-dimensional metrics
        self._calculate_phi_metrics(params)
        
        # Generate detailed analysis
        analysis = self._generate_analysis(transfer_data)
        
        # Save analysis
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        analysis_file = ANALYSIS_DIR / f"pulse_analysis_{timestamp}.json"
        with open(analysis_file, 'w') as f:
            json.dump(analysis, f, indent=2)
        
        print(f"\nDetailed analysis saved to: {analysis_file}")
        
        # Visualize pulse characteristics
        self._visualize_pulse(analysis, timestamp)
        
        return analysis
    
    def _calculate_phi_metrics(self, params):
        """Calculate and display phi-dimensional metrics."""
        # Extract parameters
        timeline_offset = params['timeline_offset']
        consciousness_transfer = params['consciousness_transfer']
        resonance_factor = params['resonance_factor']
        transfer_probability = params['transfer_probability']
        reality_stability = params['reality_stability']
        intensity = params['intensity']
        minutes = params['minutes_offset']
        
        # Calculate phi alignment metrics
        phi_timeline_alignment = timeline_offset / PHI
        phi_consciousness_correlation = consciousness_transfer / PHI_INV_CUBE
        phi_resonance_order = -math.log(resonance_factor) / math.log(PHI)
        phi_probability_correlation = transfer_probability * PHI**2
        
        # Calculate quantum signature correlation
        quantum_signature = (reality_stability * 100) / float(PERSONAL_RATIO)
        quantum_alignment = abs(1 - (quantum_signature % 1))
        
        # Calculate beaver complexity contribution
        beaver_complexity = self.phi_beaver.calculate_busy_beaver(minutes)
        beaver_phi_correlation = beaver_complexity / (PHI**intensity)
        
        # Display results
        print("\n--- φ-Dimensional Metrics ---")
        print(f"φ Timeline Alignment: {phi_timeline_alignment:.6f}")
        print(f"φ⁻³ Consciousness Correlation: {phi_consciousness_correlation:.6f}")
        print(f"φ-Resonance Order: {phi_resonance_order:.6f}")
        print(f"φ² Probability Correlation: {phi_probability_correlation:.6f}")
        print(f"φ-Quantum Signature Alignment: {quantum_alignment:.6f}")
        print(f"φ-Beaver Complexity Correlation: {beaver_phi_correlation:.6f}")
        
    def _generate_analysis(self, transfer_data):
        """Generate detailed analysis of quantum pulse."""
        params = transfer_data['parameters']
        
        # Calculate primary phi metrics
        phi_timeline_alignment = params['timeline_offset'] / PHI
        phi_consciousness_correlation = params['consciousness_transfer'] / PHI_INV_CUBE
        phi_resonance_order = -math.log(params['resonance_factor']) / math.log(PHI)
        phi_probability_correlation = params['transfer_probability'] * PHI**2
        
        # Calculate quantum metrics
        quantum_signature = (params['reality_stability'] * 100) / float(PERSONAL_RATIO)
        quantum_alignment = abs(1 - (quantum_signature % 1))
        
        # Calculate beaver complexity contribution
        beaver_complexity = self.phi_beaver.calculate_busy_beaver(params['minutes_offset'])
        beaver_phi_correlation = beaver_complexity / (PHI**params['intensity'])
        
        # Calculate dimensional characteristics
        dimension_shift = params['timeline_offset'] * params['consciousness_transfer'] * PHI
        timeline_coherence = 1 - (abs(PHI - phi_timeline_alignment) % 1)
        consciousness_coherence = 1 - (abs(1 - phi_consciousness_correlation) % 1)
        
        # Calculate phi-harmonic patterns
        harmonic_series = [PHI_INV**n for n in range(1, 8)]
        resonance_pattern = [abs(params['resonance_factor'] - h) for h in harmonic_series]
        best_harmonic = np.argmin(resonance_pattern) + 1
        harmonic_alignment = 1 - min(resonance_pattern)
        
        # Calculate quantum bridge characteristics
        bridge_stability = params['reality_stability'] ** 2
        bridge_conductivity = params['transfer_probability'] / (params['minutes_offset'] * PHI_INV)
        bridge_coherence = (params['consciousness_transfer'] * PHI**2) % 1
        bridge_bandwidth = (params['timeline_offset'] * PHI_INV) / params['minutes_offset']
        
        # Calculate paradox protection metrics
        paradox_risk = 1 - params['reality_stability']
        paradox_mitigation = 1 - (paradox_risk ** PHI)
        reality_coherence = abs(1 - ((params['validation_seal'] / PHI_75) % 1))
        timeline_stability = (params['timeline_offset'] ** PHI_INV) / params['minutes_offset']
        
        # Compile analysis
        analysis = {
            "transfer_data": transfer_data,
            "phi_metrics": {
                "phi_timeline_alignment": float(phi_timeline_alignment),
                "phi_consciousness_correlation": float(phi_consciousness_correlation),
                "phi_resonance_order": float(phi_resonance_order),
                "phi_probability_correlation": float(phi_probability_correlation),
                "quantum_signature": float(quantum_signature),
                "quantum_alignment": float(quantum_alignment),
                "beaver_complexity": float(beaver_complexity),
                "beaver_phi_correlation": float(beaver_phi_correlation)
            },
            "dimensional_characteristics": {
                "dimension_shift": float(dimension_shift),
                "timeline_coherence": float(timeline_coherence),
                "consciousness_coherence": float(consciousness_coherence)
            },
            "harmonic_patterns": {
                "best_harmonic": int(best_harmonic),
                "harmonic_alignment": float(harmonic_alignment),
                "harmonic_series": [float(h) for h in harmonic_series],
                "resonance_pattern": [float(r) for r in resonance_pattern]
            },
            "quantum_bridge": {
                "bridge_stability": float(bridge_stability),
                "bridge_conductivity": float(bridge_conductivity),
                "bridge_coherence": float(bridge_coherence),
                "bridge_bandwidth": float(bridge_bandwidth)
            },
            "paradox_protection": {
                "paradox_risk": float(paradox_risk),
                "paradox_mitigation": float(paradox_mitigation),
                "reality_coherence": float(reality_coherence),
                "timeline_stability": float(timeline_stability)
            }
        }
        
        # Calculate overall quality metrics
        phi_alignment_score = (timeline_coherence + consciousness_coherence) / 2
        bridge_quality = (bridge_stability * bridge_coherence) ** PHI_INV
        paradox_safety = paradox_mitigation ** 2
        overall_quality = (phi_alignment_score * bridge_quality * paradox_safety) ** (1/3)
        
        # Add quality metrics
        analysis["quality_metrics"] = {
            "phi_alignment_score": float(phi_alignment_score),
            "bridge_quality": float(bridge_quality),
            "paradox_safety": float(paradox_safety),
            "overall_quality": float(overall_quality)
        }
        
        return analysis
    
    def _visualize_pulse(self, analysis, timestamp):
        """Visualize quantum pulse characteristics."""
        # Create figure with subplots
        fig = plt.figure(figsize=(12, 10))
        fig.suptitle('φ-Quantum Action Pulse Analysis', fontsize=16)
        
        # 1. Bridge characteristics radar chart
        ax1 = fig.add_subplot(221, polar=True)
        bridge = analysis['quantum_bridge']
        
        # Prepare radar chart data
        categories = ['Stability', 'Conductivity', 'Coherence', 'Bandwidth']
        values = [
            bridge['bridge_stability'],
            min(1, bridge['bridge_conductivity']/3),
            bridge['bridge_coherence'],
            min(1, bridge['bridge_bandwidth'])
        ]
        
        # Close the loop
        values = np.concatenate((values, [values[0]]))
        angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        
        # Plot radar chart
        ax1.plot(angles, values, 'o-', linewidth=2)
        ax1.fill(angles, values, alpha=0.25)
        ax1.set_thetagrids(angles[:-1] * 180/np.pi, categories)
        ax1.set_ylim(0, 1)
        ax1.set_title('Quantum Bridge Characteristics')
        
        # 2. Harmonic pattern plot
        ax2 = fig.add_subplot(222)
        harmonics = analysis['harmonic_patterns']
        
        ax2.bar(range(1, 8), harmonics['resonance_pattern'], alpha=0.7)
        ax2.axhline(y=PHI_INV, color='r', linestyle='--', alpha=0.5, 
                    label=f'φ⁻¹ = {PHI_INV:.4f}')
        ax2.set_xticks(range(1, 8))
        ax2.set_xticklabels([f'φ⁻{i}' for i in range(1, 8)])
        ax2.set_ylabel('Resonance Distance')
        ax2.set_title('φ-Harmonic Resonance Pattern')
        ax2.legend()
        
        # 3. Dimensional shift visualization
        ax3 = fig.add_subplot(223)
        transfer_data = analysis['transfer_data']
        params = transfer_data['parameters']
        
        # Create dimensional shift data
        timeline_values = np.linspace(0, 2, 100)
        consciousness_values = []
        for t in timeline_values:
            if t < params['timeline_offset']:
                c = t * PHI_INV * params['consciousness_transfer']
            else:
                c = params['consciousness_transfer'] * np.exp(-(t - params['timeline_offset'])**2)
            consciousness_values.append(c)
        
        ax3.plot(timeline_values, consciousness_values, linewidth=2)
        ax3.axvline(x=params['timeline_offset'], color='r', linestyle='--', 
                    label=f'Timeline offset: {params["timeline_offset"]:.4f}')
        ax3.axhline(y=params['consciousness_transfer'], color='g', linestyle='--',
                    label=f'Consciousness transfer: {params["consciousness_transfer"]:.4f}')
        ax3.set_xlabel('Timeline Dimension')
        ax3.set_ylabel('Consciousness Dimension')
        ax3.set_title('φ-Dimensional Shift')
        ax3.legend()
        
        # 4. Quality metrics visualization
        ax4 = fig.add_subplot(224)
        quality = analysis['quality_metrics']
        
        metrics = ['φ Alignment', 'Bridge Quality', 'Paradox Safety', 'Overall']
        values = [
            quality['phi_alignment_score'],
            quality['bridge_quality'],
            quality['paradox_safety'],
            quality['overall_quality']
        ]
        
        colors = ['#3274A1', '#E1812C', '#3A923A', '#C03D3E']
        ax4.bar(metrics, values, color=colors, alpha=0.7)
        ax4.axhline(y=0.8, color='r', linestyle='--', alpha=0.5, label='Excellent threshold')
        ax4.set_ylim(0, 1)
        ax4.set_ylabel('Quality Score')
        ax4.set_title('Transfer Quality Metrics')
        ax4.legend()
        
        # Tight layout and save
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plot_path = ANALYSIS_DIR / f"pulse_visualization_{timestamp}.png"
        plt.savefig(plot_path)
        plt.close()
        
        print(f"\nPulse visualization saved to: {plot_path}")


def main():
    """Run the φ-Quantum Pulse Analyzer."""
    print("\nInitializing φ-Quantum Pulse Analyzer...")
    
    # Create analyzer
    analyzer = PhiQuantumPulseAnalyzer()
    
    # Find the most recent transfer file or use provided file
    import sys
    if len(sys.argv) > 1:
        transfer_file = sys.argv[1]
    else:
        transfer_files = list(ACTION_DIR.glob("quantum_action_TRANSFER_*.json"))
        if not transfer_files:
            print("Error: No transfer files found in phi_quantum_actions directory")
            return
        
        # Sort by modification time (newest first)
        transfer_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        transfer_file = transfer_files[0]
        print(f"Analyzing most recent transfer file: {transfer_file}")
    
    # Analyze transfer
    analyzer.analyze_transfer(transfer_file)
    
    print("\n✓ φ-Quantum Pulse Analysis complete.")

if __name__ == "__main__":
    main()
