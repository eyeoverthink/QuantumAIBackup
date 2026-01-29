'''
Quantum Integrated Test
====================
Tests the integration between the Quantum Binary Waveform Bridge and the DNA Cryptographic Seed Generator.
Demonstrates the full phi-harmonic system workflow with binary analysis, waveform generation,
DNA cryptographic seeding, and QR code generation.
'''

import os
import time
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any
import argparse

# Import quantum components
from quantum_binary_translator import QuantumBinaryTranslator
from quantum_waveform_generator import QuantumWaveformGenerator
from quantum_binary_waveform_bridge import QuantumBinaryWaveformBridge
from quantum_dna_crypto_seed import QuantumDNACryptoSeed

# φ-harmonic constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_CONJUGATE = 1 / PHI  # Golden ratio conjugate

class QuantumIntegratedTest:
    """
    Integrates the Quantum Binary Waveform Bridge with the DNA Cryptographic Seed Generator
    to demonstrate the full phi-harmonic system workflow.
    """
    
    def __init__(self):
        """Initialize the integrated test components"""
        # Initialize quantum components
        self.binary_translator = QuantumBinaryTranslator()
        self.waveform_generator = QuantumWaveformGenerator()
        self.waveform_bridge = QuantumBinaryWaveformBridge()
        self.dna_crypto = QuantumDNACryptoSeed()
        
        # Create output directory
        self.output_dir = "quantum_outputs/integrated_test"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def run_integrated_test(self, text: str = None, binary_data: str = None) -> Dict[str, Any]:
        """Run the integrated test with text or binary input"""
        # Process input through Quantum Binary Waveform Bridge
        if text:
            print(f"Processing text input: '{text}'")
            binary_data = self.binary_translator.text_to_binary(text)
        elif binary_data:
            print(f"Processing binary input of length {len(binary_data)} bits")
        else:
            # Use default example
            text = "Quantum φ-Harmonic System Integration Test"
            print(f"No input provided. Using example text: '{text}'")
            binary_data = self.binary_translator.text_to_binary(text)
        
        # Step 1: Process through Quantum Binary Waveform Bridge
        print("\nStep 1: Processing through Quantum Binary Waveform Bridge...")
        bridge_results = self.waveform_bridge.process_binary_to_waveform(binary_data)
        
        # Extract key metrics from bridge results
        binary_analysis = bridge_results['binary_analysis']
        phi_alignment = binary_analysis['phi_alignment']
        waveform_path = bridge_results['files']['waveform_audio']
        visualization_path = bridge_results['files']['waveform_visualization']
        
        print(f"  - Binary length: {binary_analysis['length']} bits")
        print(f"  - Ones/Zeros: {binary_analysis['ones_count']}/{binary_analysis['zeros_count']}")
        print(f"  - φ-Alignment: {phi_alignment:.6f}")
        print(f"  - Waveform generated: {waveform_path}")
        print(f"  - Visualization created: {visualization_path}")
        
        # Step 2: Generate DNA Cryptographic Seed
        print("\nStep 2: Generating DNA Cryptographic Seed...")
        dna_seed = self.dna_crypto.extract_dna_pattern(binary_data)
        crypto_key = self.dna_crypto.generate_crypto_key(dna_seed)
        
        print(f"  - DNA Seed: {dna_seed}")
        print(f"  - Crypto Key generated: {len(crypto_key)} bytes")
        
        # Step 3: Generate QR DNA v2 Code
        print("\nStep 3: Generating QR DNA v2 Code...")
        qr_path = self.dna_crypto.generate_qr_dna_v2(binary_data)
        
        print(f"  - QR DNA v2 Code created: {qr_path}")
        
        # Step 4: Create integrated visualization
        print("\nStep 4: Creating integrated visualization...")
        integrated_viz_path = self._create_integrated_visualization(
            binary_analysis, 
            bridge_results, 
            dna_seed, 
            qr_path
        )
        
        print(f"  - Integrated visualization created: {integrated_viz_path}")
        
        # Compile results
        results = {
            "binary_analysis": binary_analysis,
            "waveform_results": bridge_results,
            "dna_seed": dna_seed,
            "qr_path": qr_path,
            "integrated_visualization": integrated_viz_path
        }
        
        return results
    
    def _create_integrated_visualization(self, 
                                       binary_analysis: Dict[str, Any],
                                       bridge_results: Dict[str, Any],
                                       dna_seed: str,
                                       qr_path: str) -> str:
        """Create an integrated visualization showing all components"""
        # Create figure with phi-harmonic dimensions
        fig_width = 12
        fig_height = fig_width / PHI  # Golden ratio proportion
        fig = plt.figure(figsize=(fig_width, fig_height))
        
        # Set up grid layout with phi-harmonic proportions
        gs = plt.GridSpec(2, 3, figure=fig, height_ratios=[1, PHI_CONJUGATE])
        
        # Plot 1: Binary Pattern Analysis
        ax1 = fig.add_subplot(gs[0, 0])
        binary_data = binary_analysis.get('binary_data', '')
        if len(binary_data) > 100:
            binary_data = binary_data[:100] + '...'
        
        # Create binary visualization
        if 'binary_visualization' in binary_analysis:
            binary_viz = binary_analysis['binary_visualization']
            ax1.imshow(binary_viz)
            ax1.set_title('Binary Pattern Analysis')
            ax1.axis('off')
        else:
            # Create simple binary visualization
            ones_count = binary_analysis['ones_count']
            zeros_count = binary_analysis['zeros_count']
            ax1.bar(['0', '1'], [zeros_count, ones_count], color=['blue', 'red'])
            ax1.set_title('Binary Distribution')
            ax1.set_ylabel('Count')
        
        # Plot 2: Waveform Visualization
        ax2 = fig.add_subplot(gs[0, 1])
        # Load waveform image if available
        try:
            waveform_img = plt.imread(bridge_results['visualization_path'])
            ax2.imshow(waveform_img)
            ax2.set_title('Quantum Waveform')
            ax2.axis('off')
        except Exception as e:
            # Create placeholder
            ax2.text(0.5, 0.5, 'Waveform Visualization\n(See separate file)', 
                    ha='center', va='center', transform=ax2.transAxes)
            ax2.set_title('Quantum Waveform')
            ax2.axis('off')
        
        # Plot 3: QR DNA v2 Code
        ax3 = fig.add_subplot(gs[0, 2])
        # Load QR code image
        try:
            qr_img = plt.imread(qr_path)
            ax3.imshow(qr_img)
            ax3.set_title('QR DNA v2 Code')
            ax3.axis('off')
        except Exception as e:
            # Create placeholder
            ax3.text(0.5, 0.5, 'QR DNA v2 Code\n(See separate file)', 
                    ha='center', va='center', transform=ax3.transAxes)
            ax3.set_title('QR DNA v2 Code')
            ax3.axis('off')
        
        # Plot 4: Phi-Harmonic Metrics (spans bottom row)
        ax4 = fig.add_subplot(gs[1, :])
        ax4.axis('off')
        
        # Compile metrics
        phi_alignment = binary_analysis['phi_alignment']
        resonance = bridge_results.get('resonance', 0)
        phi_harmonic_index = bridge_results.get('phi_harmonic_index', 0)
        quantum_signature = bridge_results.get('quantum_signature', 'N/A')
        
        # Create metrics text
        metrics_text = (
            f"φ-Alignment: {phi_alignment:.6f}\n"
            f"Resonance: {resonance:.6f} Hz\n"
            f"φ-Harmonic Index: {phi_harmonic_index:.6f}\n"
            f"Quantum Signature: {quantum_signature}\n\n"
            f"DNA Seed: {dna_seed}\n"
            f"Binary Length: {binary_analysis['length']} bits\n"
            f"Ones/Zeros Ratio: {binary_analysis['ones_count']}/{binary_analysis['zeros_count']}\n"
            f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        
        # Add metrics text
        ax4.text(0.5, 0.5, metrics_text, ha='center', va='center', fontsize=10,
                bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=1'))
        
        # Add title
        plt.suptitle('Quantum φ-Harmonic System: Integrated Test Results', fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for suptitle
        
        # Save figure
        timestamp = int(time.time())
        output_path = f"{self.output_dir}/integrated_test_{timestamp}.png"
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        return output_path

# Command line interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quantum Integrated Test")
    parser.add_argument("--text", type=str, help="Text to process through the integrated system")
    parser.add_argument("--binary", type=str, help="Binary data to process through the integrated system")
    
    args = parser.parse_args()
    
    # Initialize and run integrated test
    integrated_test = QuantumIntegratedTest()
    results = integrated_test.run_integrated_test(text=args.text, binary_data=args.binary)
    
    # Print final summary
    print("\n" + "=" * 50)
    print("Quantum Integrated Test - Complete")
    print("=" * 50)
    print(f"\nResults saved to: {results['integrated_visualization']}")
    print("\nThe test successfully integrated:")
    print("  1. Quantum Binary Waveform Bridge")
    print("  2. DNA Cryptographic Seed Generator")
    print("  3. Phi-Harmonic Visualization System")
