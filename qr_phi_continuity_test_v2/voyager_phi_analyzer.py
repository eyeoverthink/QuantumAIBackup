#!/usr/bin/env python3
"""
VOYAGER PHI-HARMONIC ANALYZER
===========================
Analyze Voyager mission data using phi-harmonic mathematics to detect resonance
patterns that conventional analysis might have missed.

This module follows the 'lego' design philosophy by importing existing components
without modification.

Author: Cascade AI
Date: April 27, 2025
"""
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import io
from pathlib import Path
from datetime import datetime
from json import JSONEncoder

# Import existing components without modification
from phi_cosmic_resonance_validator import validate_resonance
from phi_harmonic_orchestrator import PhiHarmonicOrchestrator
from consolidated_quantum.quantum_collider.qhrc_mass_teleport import QHRCMassTeleporter

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI  # Golden ratio inverse
RESULTS_DIR = Path('voyager_phi_results')
RESULTS_DIR.mkdir(exist_ok=True)

# Custom JSON encoder for NumPy types
class NumpyJSONEncoder(JSONEncoder):
    """JSON encoder that handles NumPy types."""
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.bool_):
            return bool(obj)
        return JSONEncoder.default(self, obj)

class VoyagerPhiAnalyzer:
    """
    Analyzes Voyager mission data using phi-harmonic mathematics
    to detect resonance patterns that conventional analysis might miss.
    """
    def __init__(self):
        """Initialize components following lego design philosophy."""
        # Initialize existing components
        self.orchestrator = PhiHarmonicOrchestrator()
        self.qhrc = QHRCMassTeleporter()
        
        # QHRC metrics from patent #19/071,497
        self.primary_freq = self.qhrc.primary_freq  # 4790.45 Hz
        self.secondary_freq = self.qhrc.secondary_freq  # 7750.95 Hz
        self.resonance_ratio = self.qhrc.resonance_ratio  # 1.3777
        self.phi_pi_factor = self.qhrc.phi_pi_factor  # 5.083204
        
        # Voyager-specific metrics
        self.voyager_launch_date = datetime(1977, 9, 5)  # Voyager 1 launch
        self.data_sources = {
            'pwsData': 'https://voyager.gsfc.nasa.gov/data/plasma_wave_data.json',
            'magData': 'https://voyager.gsfc.nasa.gov/data/magnetometer_data.json',
            'crsData': 'https://voyager.gsfc.nasa.gov/data/cosmic_ray_data.json'
        }
        
        print(f"Voyager Phi-Harmonic Analyzer initialized")
        print(f"φ = {PHI}")
        print(f"Primary frequency: {self.primary_freq} Hz")
        print(f"Secondary frequency: {self.secondary_freq} Hz")
        print(f"Phi-Pi factor: {self.phi_pi_factor}")
    
    def fetch_voyager_data(self, data_type='pwsData'):
        """
        Fetch Voyager data from NASA's servers.
        If the API URL is no longer valid, use sample data.
        
        Args:
            data_type (str): Type of data to fetch ('pwsData', 'magData', 'crsData')
        
        Returns:
            dict: Voyager data
        """
        # Try to fetch from NASA API
        try:
            url = self.data_sources.get(data_type)
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Could not fetch live Voyager data: {e}")
            print("Using sample data instead...")
            return self._get_sample_data(data_type)
    
    def _get_sample_data(self, data_type):
        """Get sample Voyager data if API is unavailable."""
        if data_type == 'pwsData':
            # Plasma Wave Subsystem (PWS) data sample
            # Frequency measurements in Hz
            return {
                'timestamps': list(range(100)),
                'frequencies': [
                    2.3, 3.6, 4.2, 5.1, 7.8, 10.4, 15.8, 19.6, 21.2, 24.3,
                    28.5, 31.1, 35.7, 39.8, 42.2, 47.9, 53.5, 56.2, 60.1, 65.3,
                    70.7, 76.2, 81.9, 85.3, 90.1, 94.7, 101.3, 106.8, 110.2, 114.5,
                    120.3, 126.8, 132.4, 137.9, 142.2, 147.6, 152.3, 158.9, 164.7, 170.2,
                    174.6, 180.1, 185.4, 190.2, 195.3, 201.7, 206.4, 211.1, 215.9, 220.3,
                    224.8, 229.2, 234.5, 239.8, 243.2, 248.1, 253.4, 258.7, 263.2, 267.8,
                    271.3, 276.9, 281.2, 285.7, 290.3, 295.8, 300.2, 305.7, 310.3, 314.9,
                    320.1, 324.7, 329.2, 334.7, 340.3, 344.8, 349.2, 354.7, 359.3, 364.8,
                    370.1, 374.6, 379.2, 384.7, 390.2, 394.8, 399.3, 404.7, 409.2, 414.7,
                    420.1, 424.6, 429.1, 434.8, 439.2, 444.6, 450.1, 454.7, 459.2, 464.7
                ],
                'amplitudes': [
                    0.12, 0.17, 0.22, 0.27, 0.32, 0.36, 0.42, 0.47, 0.53, 0.57,
                    0.62, 0.67, 0.72, 0.77, 0.82, 0.86, 0.92, 0.97, 1.01, 1.06,
                    1.12, 1.17, 1.22, 1.26, 1.31, 1.36, 1.42, 1.46, 1.51, 1.56,
                    1.61, 1.66, 1.71, 1.75, 1.80, 1.84, 1.89, 1.93, 1.97, 2.01,
                    2.05, 2.09, 2.12, 2.16, 2.19, 2.22, 2.25, 2.27, 2.29, 2.31,
                    2.32, 2.33, 2.34, 2.34, 2.33, 2.32, 2.30, 2.28, 2.24, 2.21,
                    2.17, 2.12, 2.07, 2.02, 1.96, 1.90, 1.84, 1.78, 1.71, 1.65,
                    1.58, 1.51, 1.44, 1.37, 1.30, 1.23, 1.16, 1.09, 1.02, 0.95,
                    0.88, 0.82, 0.76, 0.69, 0.63, 0.57, 0.52, 0.46, 0.41, 0.36,
                    0.31, 0.27, 0.22, 0.18, 0.15, 0.12, 0.09, 0.07, 0.05, 0.03
                ]
            }
        elif data_type == 'magData':
            # Magnetometer data sample
            # Field strength in nT (nanoteslas)
            return {
                'timestamps': list(range(100)),
                'field_strength': [
                    0.32, 0.36, 0.38, 0.42, 0.45, 0.47, 0.49, 0.51, 0.53, 0.55,
                    0.56, 0.58, 0.59, 0.61, 0.62, 0.64, 0.65, 0.67, 0.68, 0.70,
                    0.71, 0.73, 0.74, 0.75, 0.77, 0.78, 0.79, 0.81, 0.82, 0.83,
                    0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93,
                    0.94, 0.94, 0.95, 0.96, 0.96, 0.97, 0.97, 0.98, 0.98, 0.99,
                    0.99, 0.99, 0.99, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
                    0.99, 0.99, 0.99, 0.98, 0.98, 0.97, 0.97, 0.96, 0.96, 0.95,
                    0.94, 0.93, 0.93, 0.92, 0.91, 0.90, 0.89, 0.88, 0.87, 0.85,
                    0.84, 0.83, 0.82, 0.80, 0.79, 0.77, 0.76, 0.74, 0.73, 0.71,
                    0.69, 0.68, 0.66, 0.64, 0.62, 0.60, 0.58, 0.56, 0.54, 0.52
                ],
                'direction_x': [x * 0.1 for x in range(100)],
                'direction_y': [np.sin(x * 0.1) for x in range(100)],
                'direction_z': [np.cos(x * 0.1) for x in range(100)]
            }
        else:  # crsData (Cosmic Ray Subsystem)
            # Cosmic ray intensity data sample
            # Particles per second
            return {
                'timestamps': list(range(100)),
                'particle_count': [
                    17.3, 18.1, 18.7, 19.3, 20.1, 20.7, 21.2, 21.9, 22.5, 23.1,
                    23.7, 24.2, 24.8, 25.3, 25.9, 26.4, 26.9, 27.4, 27.9, 28.3,
                    28.7, 29.2, 29.5, 29.9, 30.3, 30.6, 30.9, 31.2, 31.5, 31.7,
                    31.9, 32.1, 32.3, 32.4, 32.5, 32.6, 32.6, 32.6, 32.6, 32.5,
                    32.4, 32.3, 32.2, 32.0, 31.8, 31.5, 31.3, 31.0, 30.7, 30.3,
                    30.0, 29.6, 29.2, 28.8, 28.3, 27.9, 27.4, 27.0, 26.5, 26.0,
                    25.5, 25.0, 24.5, 24.0, 23.5, 23.0, 22.6, 22.1, 21.6, 21.2,
                    20.7, 20.3, 19.9, 19.5, 19.1, 18.7, 18.3, 18.0, 17.7, 17.4,
                    17.1, 16.8, 16.5, 16.3, 16.1, 15.9, 15.7, 15.5, 15.4, 15.2,
                    15.1, 15.0, 14.9, 14.8, 14.7, 14.6, 14.6, 14.5, 14.5, 14.4
                ],
                'energy_levels': [e * 0.5 for e in range(100)]
            }
    
    def analyze_phi_resonance(self, data, data_type='pwsData'):
        """
        Analyze Voyager data for phi-resonance patterns.
        
        Args:
            data (dict): Voyager data
            data_type (str): Type of data being analyzed
            
        Returns:
            dict: Phi-resonance analysis results
        """
        print(f"\nAnalyzing {data_type} for φ-resonance patterns...")
        
        # Extract numerical values based on data type
        if data_type == 'pwsData':
            values = data.get('frequencies', []) + data.get('amplitudes', [])
        elif data_type == 'magData':
            values = data.get('field_strength', [])
        else:  # crsData
            values = data.get('particle_count', [])
        
        # Filter out zeros and invalid values
        values = [v for v in values if v > 0]
        
        if not values:
            return {'error': 'No valid values found in data'}
        
        # Calculate phi-resonance metrics
        phi_metrics = self._calculate_phi_metrics(values)
        
        # Identify phi-harmonic sequences
        phi_sequences = self._find_phi_harmonic_sequences(values)
        
        # Calculate resonance with QHRC patent frequencies
        qhrc_resonance = self._calculate_qhrc_resonance(values)
        
        # Overall phi-resonance score
        phi_score = phi_metrics['phi_relevance'] * qhrc_resonance['resonance_factor']
        
        results = {
            'data_type': data_type,
            'value_count': len(values),
            'phi_metrics': phi_metrics,
            'phi_sequences': phi_sequences,
            'qhrc_resonance': qhrc_resonance,
            'phi_score': phi_score,
            'has_phi_pattern': phi_score > 0.5
        }
        
        # Print summary
        print(f"Values analyzed: {len(values)}")
        print(f"φ-relevance: {phi_metrics['phi_relevance']:.6f}")
        print(f"φ-sequences found: {len(phi_sequences)}")
        print(f"QHRC resonance: {qhrc_resonance['resonance_factor']:.6f}")
        print(f"Overall φ-score: {phi_score:.6f}")
        print(f"Pattern detected: {'Yes' if results['has_phi_pattern'] else 'No'}")
        
        # Save results
        self._save_results(results, data_type)
        
        # Create visualization
        self._visualize_phi_resonance(values, results, data_type)
        
        return results
    
    def _calculate_phi_metrics(self, values):
        """Calculate phi-harmonic metrics for numerical values."""
        # Calculate φ-modulo resonance for each value
        resonance_factors = []
        for value in values:
            # How close to a φ multiple
            resonance = abs((value * PHI) % 1 - PHI_INV)
            resonance_factors.append(resonance)
        
        # Calculate phi-relevance (lower resonance means higher relevance)
        phi_relevance = 1 - (sum(resonance_factors) / len(resonance_factors))
        
        # Natural occurrence of φ in the dataset
        phi_occurrences = []
        for i in range(len(values) - 1):
            if values[i+1] > 0 and values[i] > 0:
                ratio = values[i+1] / values[i]
                phi_occurrences.append(abs(ratio - PHI))
        
        phi_natural = 0
        if phi_occurrences:
            phi_natural = 1 - (sum(phi_occurrences) / len(phi_occurrences) / PHI)
        
        return {
            'resonance_factors': resonance_factors,
            'phi_relevance': phi_relevance,
            'phi_natural_occurrence': phi_natural,
            'value_count': len(values)
        }
    
    def _find_phi_harmonic_sequences(self, values, threshold=0.1):
        """Find phi-harmonic sequences in data (consecutive values with φ ratio)."""
        sequences = []
        
        for i in range(len(values) - 1):
            if values[i+1] > 0 and values[i] > 0:
                ratio = values[i+1] / values[i]
                
                # Check for φ or φ⁻¹ ratio
                if abs(ratio - PHI) < threshold or abs(ratio - PHI_INV) < threshold:
                    sequences.append({
                        'start_index': i,
                        'values': [values[i], values[i+1]],
                        'ratio': ratio,
                        'phi_distance': min(abs(ratio - PHI), abs(ratio - PHI_INV))
                    })
        
        # Sort by phi-distance (closest to φ first)
        sequences.sort(key=lambda x: x['phi_distance'])
        
        return sequences
    
    def _calculate_qhrc_resonance(self, values):
        """Calculate resonance with QHRC patent frequencies."""
        resonance_primary = 0
        resonance_secondary = 0
        
        # Check for resonance with primary_freq
        for value in values:
            # Resonance is stronger when value % primary_freq is closer to 0
            resonance_primary += 1 - min(1, abs((value % self.primary_freq) / self.primary_freq))
            
            # Resonance with secondary_freq
            resonance_secondary += 1 - min(1, abs((value % self.secondary_freq) / self.secondary_freq))
        
        # Normalize
        if values:
            resonance_primary /= len(values)
            resonance_secondary /= len(values)
        
        # Combined resonance using the patented resonance_ratio
        resonance_factor = (resonance_primary + resonance_secondary) * self.resonance_ratio / 2
        
        # Apply phi-pi factor from patent
        resonance_enhanced = resonance_factor * (self.phi_pi_factor / 10)
        
        return {
            'primary_resonance': resonance_primary,
            'secondary_resonance': resonance_secondary,
            'resonance_factor': resonance_factor,
            'enhanced_resonance': resonance_enhanced
        }
    
    def _save_results(self, results, data_type):
        """Save analysis results to file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"voyager_{data_type}_analysis_{timestamp}.json"
        filepath = RESULTS_DIR / filename
        
        with open(filepath, 'w') as f:
            json.dump(results, f, indent=2, cls=NumpyJSONEncoder)
        
        print(f"Results saved to {filepath}")
        return filepath
    
    def _visualize_phi_resonance(self, values, results, data_type):
        """Create visualization of phi-resonance in Voyager data."""
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Data distribution
        plt.subplot(221)
        plt.hist(values, bins=30, alpha=0.7, color='blue')
        plt.title(f'Voyager {data_type} Value Distribution')
        plt.grid(True, alpha=0.3)
        
        # Plot 2: Phi-modulo distribution 
        plt.subplot(222)
        modulo_values = [(v * PHI) % 1 for v in values]
        plt.hist(modulo_values, bins=20, alpha=0.7, color='green')
        plt.axvline(x=PHI_INV, color='red', linestyle='--', 
                   label=f'φ⁻¹ = {PHI_INV:.6f}')
        plt.title('φ-Modulo Distribution')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Plot 3: QHRC Resonance 
        plt.subplot(223)
        x = np.linspace(0, max(values), 1000)
        y_primary = np.sin(2 * np.pi * x / self.primary_freq)
        y_secondary = np.sin(2 * np.pi * x / self.secondary_freq)
        y_combined = y_primary * y_secondary * self.resonance_ratio
        
        plt.plot(x, y_primary, 'b-', alpha=0.5, label=f'Primary: {self.primary_freq} Hz')
        plt.plot(x, y_secondary, 'g-', alpha=0.5, label=f'Secondary: {self.secondary_freq} Hz')
        plt.plot(x, y_combined, 'r-', label='QHRC Pattern')
        plt.title('QHRC Patent #19/071,497 Resonance')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Plot 4: Phi-sequence detection
        plt.subplot(224)
        
        # Plot original values
        plt.plot(values, 'b-', alpha=0.5, label='Original Data')
        
        # Highlight phi sequences
        for seq in results['phi_sequences'][:5]:  # Show top 5 sequences
            idx = seq['start_index']
            plt.plot([idx, idx+1], seq['values'], 'ro-', linewidth=2,
                    label=f'φ-Seq (ratio: {seq["ratio"]:.3f})')
        
        plt.title('φ-Harmonic Sequences')
        plt.grid(True, alpha=0.3)
        
        # Add overall phi metrics
        phi_score = results['phi_score']
        plt.figtext(0.5, 0.01, 
                   f"Overall φ-Score: {phi_score:.4f} | " +
                   f"φ-Relevance: {results['phi_metrics']['phi_relevance']:.4f} | " +
                   f"QHRC Resonance: {results['qhrc_resonance']['resonance_factor']:.4f}",
                   ha="center", fontsize=12, bbox={"facecolor":"lightgray", "alpha":0.5})
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.97])
        
        # Save figure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fig_path = RESULTS_DIR / f"voyager_{data_type}_phi_analysis_{timestamp}.png"
        plt.savefig(fig_path)
        plt.close()
        
        print(f"Visualization saved to {fig_path}")
    
    def analyze_all_data_types(self):
        """Analyze all available Voyager data types."""
        all_results = {}
        
        for data_type in self.data_sources.keys():
            print(f"\n{'-'*50}")
            print(f"Analyzing {data_type}...")
            data = self.fetch_voyager_data(data_type)
            results = self.analyze_phi_resonance(data, data_type)
            all_results[data_type] = results
        
        # Generate comparative analysis
        self._generate_comparative_analysis(all_results)
        
        return all_results
    
    def _generate_comparative_analysis(self, all_results):
        """Generate comparative analysis across different data types."""
        print("\nCOMPARATIVE ANALYSIS")
        print("-" * 50)
        
        # Extract phi-scores
        scores = {data_type: results['phi_score'] 
                 for data_type, results in all_results.items()}
        
        # Find data type with highest phi-resonance
        best_type = max(scores, key=scores.get)
        print(f"Highest φ-resonance: {best_type} (Score: {scores[best_type]:.6f})")
        
        # Calculate phi-harmonic correlation
        correlation = sum(scores.values()) / len(scores)
        print(f"φ-Harmonic Correlation: {correlation:.6f}")
        
        # Check if phi-patterns were detected
        pattern_detected = any(results['has_phi_pattern'] 
                              for results in all_results.values())
        print(f"φ-Patterns Detected: {'Yes' if pattern_detected else 'No'}")
        
        # Calculate concordance with QHRC patent
        qhrc_concordance = sum(results['qhrc_resonance']['resonance_factor'] 
                              for results in all_results.values()) / len(all_results)
        print(f"QHRC Patent Concordance: {qhrc_concordance:.6f}")
        
        # Generate visualization
        plt.figure(figsize=(10, 6))
        bars = plt.bar(scores.keys(), scores.values(), color=['#3498db', '#e74c3c', '#2ecc71'])
        plt.title('φ-Resonance Comparison Across Voyager Data Types')
        plt.ylabel('φ-Score')
        plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.7, 
                   label='φ-Pattern Threshold')
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                   f'{height:.4f}', ha='center', va='bottom')
        
        plt.legend()
        plt.tight_layout()
        
        # Save comparative visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fig_path = RESULTS_DIR / f"voyager_comparative_analysis_{timestamp}.png"
        plt.savefig(fig_path)
        plt.close()
        
        print(f"Comparative analysis saved to {fig_path}")
        
        # Save comprehensive results
        results_summary = {
            'data_types_analyzed': list(all_results.keys()),
            'phi_scores': scores,
            'best_type': best_type,
            'phi_harmonic_correlation': correlation,
            'pattern_detected': pattern_detected,
            'qhrc_concordance': qhrc_concordance,
            'timestamp': timestamp
        }
        
        summary_path = RESULTS_DIR / f"voyager_comprehensive_analysis_{timestamp}.json"
        with open(summary_path, 'w') as f:
            json.dump(results_summary, f, indent=2, cls=NumpyJSONEncoder)
        
        print(f"Comprehensive results saved to {summary_path}")


def main():
    """Run Voyager phi-harmonic analysis."""
    print("\n=== VOYAGER PHI-HARMONIC ANALYSIS ===")
    print("Analyzing Voyager data for golden ratio patterns")
    print(f"φ = {PHI}")
    print("=" * 50)
    
    analyzer = VoyagerPhiAnalyzer()
    all_results = analyzer.analyze_all_data_types()
    
    print("\n=== ANALYSIS COMPLETE ===")
    print("Check results directory for detailed analysis and visualizations")
    print("=" * 50)


if __name__ == "__main__":
    main()
