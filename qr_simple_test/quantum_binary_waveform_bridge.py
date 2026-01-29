#!/usr/bin/env python3
"""
Quantum Binary Waveform Bridge
===========================
Integrates the Quantum Binary Translator with the Quantum Waveform Generator
to create a complete phi-harmonic system that translates binary patterns to
waveforms and provides a unified UI/UX experience.

By Vaughn Scott (with Cascade Assistant)
"""

import os
import sys
import time
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, List, Optional, Tuple

# Import our quantum modules
from quantum_binary_translator import QuantumBinaryTranslator
from quantum_waveform_generator import QuantumWaveformGenerator

class QuantumBinaryWaveformBridge:
    """
    Bridge class that connects the Quantum Binary Translator with the
    Quantum Waveform Generator to provide a unified experience.
    """
    
    def __init__(self, output_dir="quantum_outputs"):
        """
        Initialize the bridge with both quantum components.
        
        Args:
            output_dir: Directory to save outputs
        """
        self.binary_translator = QuantumBinaryTranslator()
        self.waveform_generator = QuantumWaveformGenerator(output_dir=output_dir)
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Track session history
        self.session_history = []
    
    def process_binary_to_waveform(self, binary_data: str) -> Dict[str, Any]:
        """
        Process binary data through the complete pipeline:
        Binary → Analysis → Waveform → LLM Response
        
        Args:
            binary_data: Binary string to process
            
        Returns:
            Dictionary with all results from the pipeline
        """
        # Step 1: Analyze binary with Quantum Binary Translator
        binary_analysis = self.binary_translator.analyze_binary_pattern(binary_data)
        
        # Step 2: Generate LLM response from binary
        llm_response = self.binary_translator.generate_binary_llm_response(binary_data)
        
        # Step 3: Use phi-alignment from binary analysis to generate waveform
        phi_alignment = binary_analysis["phi_alignment"]
        waveform_data = self.waveform_generator.generate_waveform(phi_alignment)
        
        # Step 4: Save waveform files
        waveform_files = self.waveform_generator.save_waveform(waveform_data)
        
        # Step 5: Generate combined visualization
        visualization_path = self._generate_combined_visualization(
            binary_data, binary_analysis, waveform_data, llm_response
        )
        
        # Combine all results
        result = {
            "binary_data": binary_data,
            "binary_analysis": binary_analysis,
            "llm_response": llm_response,
            "waveform_data": {
                "phi_alignment": waveform_data["phi_alignment"],
                "frequencies": waveform_data["frequencies"][:5],  # First 5 frequencies
                "resonance": waveform_data["resonance"],
                "quantum_signature": waveform_data["quantum_signature"],
                "phi_harmonic_index": waveform_data["phi_harmonic_index"]
            },
            "files": {
                "waveform_audio": waveform_files["wav_file"],
                "waveform_visualization": waveform_files["visualization"],
                "combined_visualization": visualization_path
            },
            "timestamp": time.time()
        }
        
        # Add to session history
        self.session_history.append({
            "binary_length": len(binary_data),
            "phi_alignment": phi_alignment,
            "resonance": waveform_data["resonance"],
            "quantum_signature": waveform_data["quantum_signature"],
            "timestamp": time.time()
        })
        
        return result
    
    def text_to_binary_waveform(self, text: str) -> Dict[str, Any]:
        """
        Convert text to binary and then process through the pipeline.
        
        Args:
            text: Text to convert and process
            
        Returns:
            Dictionary with all results from the pipeline
        """
        # Convert text to binary
        binary_data = self.binary_translator.text_to_binary(text)
        
        # Process through pipeline
        return self.process_binary_to_waveform(binary_data)
    
    def _generate_combined_visualization(self, binary_data: str, binary_analysis: Dict[str, Any],
                                        waveform_data: Dict[str, Any], llm_response: Dict[str, Any]) -> str:
        """
        Generate a combined visualization of binary analysis and waveform.
        
        Args:
            binary_data: Original binary data
            binary_analysis: Results from binary analysis
            waveform_data: Results from waveform generation
            llm_response: Results from LLM response
            
        Returns:
            Path to the saved visualization file
        """
        # Create figure with golden ratio dimensions
        phi = (1 + np.sqrt(5)) / 2
        plt.figure(figsize=(10, 10/phi))
        
        # Plot binary pattern
        plt.subplot(3, 1, 1)
        binary_array = np.array([int(b) for b in binary_data[:100]])  # First 100 bits
        plt.plot(binary_array, 'o-', markersize=4)
        plt.title(f"Binary Pattern (φ-alignment: {binary_analysis['phi_alignment']:.6f})")
        plt.xlabel("Position")
        plt.ylabel("Value")
        plt.yticks([0, 1])
        plt.grid(True, alpha=0.3)
        
        # Plot waveform
        plt.subplot(3, 1, 2)
        t = np.linspace(0, waveform_data["duration"], len(waveform_data["waveform"]), endpoint=False)
        plt.plot(t[:int(len(t)/16)], waveform_data["waveform"][:int(len(t)/16)])
        plt.title(f"Quantum Waveform (Resonance: {waveform_data['resonance']:.6f} Hz)")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid(True, alpha=0.3)
        
        # Display LLM response
        plt.subplot(3, 1, 3)
        plt.axis('off')
        response_text = llm_response.get("response_text", "No response generated")
        # Truncate and format for display
        if len(response_text) > 300:
            response_text = response_text[:297] + "..."
        
        plt.text(0.05, 0.9, "LLM Response:", fontsize=10, fontweight='bold')
        plt.text(0.05, 0.7, response_text, fontsize=9, wrap=True)
        
        # Add phi-harmonic metrics
        metrics_text = (
            f"Binary Length: {binary_analysis['length']} bits\n"
            f"Ones/Zeros: {binary_analysis['ones_count']}/{binary_analysis['zeros_count']}\n"
            f"φ-Alignment: {binary_analysis['phi_alignment']:.6f}\n"
            f"Resonance: {waveform_data['resonance']:.6f} Hz\n"
            f"Quantum Signature: {waveform_data['quantum_signature']}"
        )
        plt.figtext(0.02, 0.02, metrics_text, fontsize=8)
        
        # Adjust layout
        plt.tight_layout(rect=[0, 0.05, 1, 0.95])
        
        # Save visualization
        timestamp = int(time.time())
        viz_path = os.path.join(self.output_dir, f"quantum_bridge_{timestamp}.png")
        plt.savefig(viz_path, dpi=150)
        plt.close()
        
        return viz_path
    
    def generate_session_report(self, output_path: Optional[str] = None) -> str:
        """
        Generate a report of the current session with visualizations.
        
        Args:
            output_path: Optional path to save the report
            
        Returns:
            Path to the saved report file
        """
        if not self.session_history:
            return "No session history available."
        
        # Generate default output path if not provided
        if output_path is None:
            timestamp = int(time.time())
            output_path = os.path.join(self.output_dir, f"quantum_session_report_{timestamp}.html")
        
        # Create HTML report
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Quantum Binary Waveform Session Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                h1, h2 {{ color: #2c3e50; }}
                .container {{ max-width: 1000px; margin: 0 auto; background-color: white; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
                .metrics {{ display: flex; flex-wrap: wrap; margin-bottom: 20px; }}
                .metric-box {{ background-color: #e8f4f8; border-radius: 5px; padding: 15px; margin: 10px; flex: 1; min-width: 200px; }}
                .metric-value {{ font-size: 24px; font-weight: bold; color: #3498db; }}
                .metric-label {{ font-size: 14px; color: #7f8c8d; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
                th {{ background-color: #3498db; color: white; }}
                tr:hover {{ background-color: #f5f5f5; }}
                .footer {{ margin-top: 30px; font-size: 12px; color: #7f8c8d; text-align: center; }}
                .phi-symbol {{ color: #e67e22; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Quantum Binary Waveform <span class="phi-symbol">φ</span>-Harmonic Session Report</h1>
                <p>Generated on {time.strftime('%Y-%m-%d %H:%M:%S')}</p>
                
                <div class="metrics">
                    <div class="metric-box">
                        <div class="metric-value">{len(self.session_history)}</div>
                        <div class="metric-label">Quantum Transformations</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-value">{np.mean([h['phi_alignment'] for h in self.session_history]):.6f}</div>
                        <div class="metric-label">Average <span class="phi-symbol">φ</span>-Alignment</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-value">{np.mean([h['resonance'] for h in self.session_history]):.2f} Hz</div>
                        <div class="metric-label">Average Resonance</div>
                    </div>
                </div>
                
                <h2>Session History</h2>
                <table>
                    <tr>
                        <th>#</th>
                        <th>Binary Length</th>
                        <th><span class="phi-symbol">φ</span>-Alignment</th>
                        <th>Resonance (Hz)</th>
                        <th>Quantum Signature</th>
                        <th>Timestamp</th>
                    </tr>
        """
        
        # Add rows for each session entry
        for i, entry in enumerate(self.session_history):
            html_content += f"""
                    <tr>
                        <td>{i+1}</td>
                        <td>{entry['binary_length']}</td>
                        <td>{entry['phi_alignment']:.6f}</td>
                        <td>{entry['resonance']:.6f}</td>
                        <td>{entry['quantum_signature']}</td>
                        <td>{time.strftime('%H:%M:%S', time.localtime(entry['timestamp']))}</td>
                    </tr>
            """
        
        # Close the HTML
        html_content += f"""
                </table>
                
                <h2>Phi-Harmonic Analysis</h2>
                <p>
                    This session demonstrates the quantum bridge between binary patterns and waveform generation
                    using <span class="phi-symbol">φ</span>-harmonic principles. The system maps binary patterns to
                    resonant frequencies based on their alignment with the golden ratio (<span class="phi-symbol">φ</span> ≈ 1.618034).
                </p>
                
                <div class="footer">
                    Generated by Quantum Binary Waveform Bridge | Quantum Phi-Harmonic System<br>
                    By Vaughn Scott | {time.strftime('%Y')}
                </div>
            </div>
        </body>
        </html>
        """
        
        # Write HTML to file
        with open(output_path, 'w') as f:
            f.write(html_content)
        
        return output_path


def main():
    """
    Main function to demonstrate the Quantum Binary Waveform Bridge.
    """
    parser = argparse.ArgumentParser(description="Process binary data through the Quantum Binary Waveform Bridge")
    parser.add_argument("--binary", type=str, help="Binary string to process")
    parser.add_argument("--text", type=str, help="Text to convert to binary and process")
    parser.add_argument("--output", type=str, default="quantum_outputs", help="Output directory")
    
    args = parser.parse_args()
    
    # Create bridge
    bridge = QuantumBinaryWaveformBridge(output_dir=args.output)
    
    # Process input
    if args.binary:
        result = bridge.process_binary_to_waveform(args.binary)
    elif args.text:
        result = bridge.text_to_binary_waveform(args.text)
    else:
        # Default example
        example_text = "Quantum φ-Harmonic System"
        print(f"No input provided. Using example text: '{example_text}'")
        result = bridge.text_to_binary_waveform(example_text)
    
    # Display results
    print("\n" + "="*50)
    print("Quantum Binary Waveform Bridge - Results")
    print("="*50)
    
    # Binary analysis
    print("\nBinary Analysis:")
    print(f"Length: {result['binary_analysis']['length']} bits")
    print(f"Ones/Zeros: {result['binary_analysis']['ones_count']}/{result['binary_analysis']['zeros_count']}")
    print(f"φ-Alignment: {result['binary_analysis']['phi_alignment']:.6f}")
    
    # Waveform data
    print("\nWaveform Generation:")
    print(f"Resonance: {result['waveform_data']['resonance']:.6f} Hz")
    print(f"Quantum Signature: {result['waveform_data']['quantum_signature']}")
    print(f"φ-Harmonic Index: {result['waveform_data']['phi_harmonic_index']:.6f}")
    
    # LLM response
    print("\nLLM Response:")
    print(f"Query: {result['llm_response'].get('query', 'N/A')}")
    response_text = result['llm_response'].get('response_text', 'No response generated')
    print(f"Response: {response_text[:100]}..." if len(response_text) > 100 else f"Response: {response_text}")
    
    # Files created
    print("\nFiles Created:")
    for file_type, file_path in result['files'].items():
        print(f"  {file_type}: {file_path}")
    
    # Generate session report
    report_path = bridge.generate_session_report()
    print(f"\nSession Report: {report_path}")
    
    print("\nQuantum Binary Waveform Bridge - Complete")


if __name__ == "__main__":
    main()
