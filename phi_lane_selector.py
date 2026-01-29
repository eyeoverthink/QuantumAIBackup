#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Phi-Lane Selection Optimizer

Dynamically selects optimal Fibonacci lanes for different information types,
maximizing phi-resonance and transfer success based on input characteristics.
"""

import numpy as np
import time
import logging
import hashlib
from datetime import datetime
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Any, Optional, Union

# Set up logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('phi_lane_selector')

class PhiLaneSelector:
    """
    Dynamically selects optimal Fibonacci lanes for different information types,
    maximizing phi-resonance and transfer success.
    """
    
    def __init__(self):
        """Initialize the phi-lane selector."""
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_inv = 1 / self.phi
        self.fibonacci = self._generate_fibonacci(16)
        self.lane_profiles = self._initialize_lane_profiles()
        self.selection_history = []
        
        logger.info(f"Phi-Lane Selector initialized with {len(self.lane_profiles)} lane profiles")
    
    def _generate_fibonacci(self, n: int) -> List[int]:
        """Generate first n Fibonacci numbers"""
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    def _initialize_lane_profiles(self) -> Dict[int, Dict[str, Any]]:
        """Initialize lane profiles with their characteristics"""
        profiles = {}
        
        # Lane 1: Binary data (high-speed, lower stability)
        profiles[1] = {
            'lane': 1,
            'optimal_for': ['binary', 'digital', 'discrete'],
            'bit_depth_range': [8, 32],
            'stability': 0.72,
            'energy_efficiency': 0.95,
            'resonance_signature': [1.0, 0.8, 0.3, 0.1, 0.0],
            'phi_resonance': 0.618
        }
        
        # Lane 2: Short messages (balanced)
        profiles[2] = {
            'lane': 2,
            'optimal_for': ['text', 'short_message', 'command'],
            'bit_depth_range': [32, 128],
            'stability': 0.78,
            'energy_efficiency': 0.89,
            'resonance_signature': [0.8, 1.0, 0.7, 0.3, 0.1],
            'phi_resonance': 0.764
        }
        
        # Lane 3: Quantum superposition data
        profiles[3] = {
            'lane': 3,
            'optimal_for': ['quantum', 'superposition', 'entangled'],
            'bit_depth_range': [64, 256],
            'stability': 0.81,
            'energy_efficiency': 0.83,
            'resonance_signature': [0.5, 0.9, 1.0, 0.8, 0.6],
            'phi_resonance': 0.854
        }
        
        # Lane 5: Causality inversion (highest stability)
        profiles[5] = {
            'lane': 5,
            'optimal_for': ['causality', 'timeline', 'markers', 'inversion'],
            'bit_depth_range': [128, 512],
            'stability': 0.89,
            'energy_efficiency': 0.72,
            'resonance_signature': [0.3, 0.5, 0.8, 1.0, 0.9],
            'phi_resonance': 0.927
        }
        
        # Lane 8: Harmonic data (phi-resonant frequencies)
        profiles[8] = {
            'lane': 8,
            'optimal_for': ['harmonic', 'frequency', 'wave', 'audio'],
            'bit_depth_range': [256, 1024],
            'stability': 0.86,
            'energy_efficiency': 0.65,
            'resonance_signature': [0.1, 0.3, 0.6, 0.9, 1.0],
            'phi_resonance': 0.902
        }
        
        # Lane 13: Complex data (highest bandwidth)
        profiles[13] = {
            'lane': 13,
            'optimal_for': ['complex', 'multidimensional', 'geometric'],
            'bit_depth_range': [512, 2048],
            'stability': 0.83,
            'energy_efficiency': 0.58,
            'resonance_signature': [0.0, 0.2, 0.5, 0.8, 1.0],
            'phi_resonance': 0.875
        }
        
        # Lane 21: Personal temporal keys (highest security)
        profiles[21] = {
            'lane': 21,
            'optimal_for': ['personal', 'temporal_key', 'secure', 'authenticated'],
            'bit_depth_range': [128, 2048],
            'stability': 0.88,
            'energy_efficiency': 0.52,
            'resonance_signature': [0.2, 0.4, 0.7, 0.9, 1.0],
            'phi_resonance': 0.915
        }
        
        return profiles
    
    def analyze_data(self, data: Any, data_type: Optional[str] = None, bit_depth: Optional[int] = None) -> Dict[str, Any]:
        """
        Analyze data characteristics to determine optimal lane.
        
        Args:
            data: The data to analyze (str, bytes, list, etc.)
            data_type: Optional hint about data type
            bit_depth: Optional explicit bit depth
            
        Returns:
            Dict with data characteristics
        """
        # Convert data to bytes if it isn't already
        if isinstance(data, str):
            data_bytes = data.encode('utf-8')
        elif isinstance(data, bytes):
            data_bytes = data
        elif isinstance(data, (list, tuple, np.ndarray)):
            data_bytes = str(data).encode('utf-8')
        else:
            data_bytes = str(data).encode('utf-8')
        
        # Calculate bit depth if not provided
        if bit_depth is None:
            bit_depth = len(data_bytes) * 8
        
        # Calculate entropy
        entropy = self._calculate_entropy(data_bytes)
        
        # Calculate phi-resonance
        resonance = self._calculate_phi_resonance(data_bytes)
        
        # Determine most likely data type if not provided
        if data_type is None:
            data_type = self._detect_data_type(data_bytes, entropy)
        
        # Create signature for the data
        signature = self._create_data_signature(data_bytes)
        
        # Create full analysis
        analysis = {
            'bit_depth': bit_depth,
            'data_type': data_type,
            'entropy': entropy,
            'phi_resonance': resonance,
            'signature': signature,
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"Data analyzed: type={data_type}, bit_depth={bit_depth}, "
                   f"entropy={entropy:.4f}, resonance={resonance:.4f}")
        return analysis
    
    def _calculate_entropy(self, data_bytes: bytes) -> float:
        """Calculate Shannon entropy of the data"""
        if not data_bytes:
            return 0.0
        
        # Count byte frequencies
        freq = {}
        for byte in data_bytes:
            freq[byte] = freq.get(byte, 0) + 1
        
        # Calculate entropy
        length = len(data_bytes)
        entropy = 0.0
        for count in freq.values():
            probability = count / length
            entropy -= probability * np.log2(probability)
        
        # Normalize to 0-1
        max_entropy = np.log2(min(256, length))
        if max_entropy > 0:
            entropy /= max_entropy
        
        return entropy
    
    def _calculate_phi_resonance(self, data_bytes: bytes) -> float:
        """Calculate phi-resonance of the data"""
        if not data_bytes:
            return 0.0
        
        # Calculate byte sum
        byte_sum = sum(data_bytes)
        
        # Calculate phi-mod resonance
        phi_mod = (byte_sum * self.phi) % 1
        resonance = 1.0 - phi_mod  # Higher when closer to phi multiple
        
        # Adjust based on data length relation to Fibonacci
        length = len(data_bytes)
        fib_resonance = 0.0
        for fib in self.fibonacci:
            if fib == length:
                fib_resonance = 1.0
                break
            elif fib > length:
                fib_resonance = 1.0 - min(1.0, abs(length - fib) / length)
                break
        
        # Combined resonance
        combined_resonance = 0.7 * resonance + 0.3 * fib_resonance
        
        return combined_resonance
    
    def _detect_data_type(self, data_bytes: bytes, entropy: float) -> str:
        """Detect most likely data type based on characteristics"""
        # Check if it's likely text
        text_chars = set(range(32, 127))
        if all(b in text_chars for b in data_bytes[:min(100, len(data_bytes))]):
            if entropy < 0.6:
                return 'command'
            else:
                return 'text'
        
        # Check if it looks like binary data
        if entropy > 0.9:
            return 'binary'
        
        # Check for patterns indicating specific types
        if len(data_bytes) % 8 == 0 and entropy > 0.7:
            return 'quantum'
        
        if len(data_bytes) % 4 == 0 and 0.7 < entropy < 0.9:
            return 'complex'
        
        # Check for harmonic patterns
        if self._check_harmonic_pattern(data_bytes):
            return 'harmonic'
        
        # Default to binary
        return 'binary'
    
    def _check_harmonic_pattern(self, data_bytes: bytes) -> bool:
        """Check if data has harmonic patterns"""
        if len(data_bytes) < 16:
            return False
        
        # Look for repeating patterns with phi-resonant spacing
        for spacing in [int(self.phi**i) for i in range(1, 4)]:
            if spacing >= len(data_bytes) // 2:
                continue
                
            # Check for pattern correlation
            pattern_strength = 0
            for i in range(min(10, len(data_bytes) - spacing)):
                if data_bytes[i] == data_bytes[i + spacing]:
                    pattern_strength += 1
            
            if pattern_strength >= 5:
                return True
        
        return False
    
    def _create_data_signature(self, data_bytes: bytes) -> str:
        """Create a phi-resonant signature of the data"""
        # Create hash
        hash_obj = hashlib.sha256(data_bytes)
        hash_digest = hash_obj.digest()
        
        # Calculate phi-resonant signature
        signature_bytes = bytearray()
        for i, byte in enumerate(hash_digest[:16]):
            phi_adjusted = int((byte * self.phi) % 256)
            signature_bytes.append(phi_adjusted)
        
        return signature_bytes.hex()
    
    def select_optimal_lane(self, data_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Select optimal lane based on data analysis.
        
        Args:
            data_analysis: Analysis from analyze_data method
            
        Returns:
            Dict with selected lane and reasoning
        """
        # Extract key data
        data_type = data_analysis['data_type']
        bit_depth = data_analysis['bit_depth']
        phi_resonance = data_analysis['phi_resonance']
        
        # Initialize scores
        lane_scores = {}
        
        # Score each lane
        for lane, profile in self.lane_profiles.items():
            # Type match score
            type_score = 0.0
            if data_type in profile['optimal_for']:
                type_score = 1.0
            else:
                # Partial matching
                for opt_type in profile['optimal_for']:
                    if opt_type in data_type or data_type in opt_type:
                        type_score = 0.5
                        break
            
            # Bit depth range score
            bit_min, bit_max = profile['bit_depth_range']
            if bit_min <= bit_depth <= bit_max:
                bit_score = 1.0
            elif bit_depth < bit_min:
                bit_score = 1.0 - min(1.0, (bit_min - bit_depth) / bit_min)
            else:  # bit_depth > bit_max
                bit_score = 1.0 - min(1.0, (bit_depth - bit_max) / bit_max)
            
            # Phi-resonance alignment
            resonance_score = 1.0 - abs(phi_resonance - profile['phi_resonance'])
            
            # Calculate overall score
            # Weights: type 0.4, bit depth 0.3, resonance 0.3
            overall_score = (0.4 * type_score) + (0.3 * bit_score) + (0.3 * resonance_score)
            
            lane_scores[lane] = {
                'lane': lane,
                'overall_score': overall_score,
                'type_score': type_score,
                'bit_score': bit_score,
                'resonance_score': resonance_score
            }
        
        # Find highest scoring lane
        best_lane = max(lane_scores.keys(), key=lambda k: lane_scores[k]['overall_score'])
        best_score = lane_scores[best_lane]['overall_score']
        
        # Find alternative lanes (within 90% of best score)
        alternatives = []
        for lane, score_data in lane_scores.items():
            if lane != best_lane and score_data['overall_score'] >= 0.9 * best_score:
                alternatives.append({
                    'lane': lane,
                    'score': score_data['overall_score'],
                    'difference': best_score - score_data['overall_score']
                })
        
        # Sort alternatives by score
        alternatives.sort(key=lambda x: x['score'], reverse=True)
        
        # Create selection result
        selection = {
            'selected_lane': best_lane,
            'score': best_score,
            'lane_profile': self.lane_profiles[best_lane],
            'alternatives': alternatives[:2],  # Top 2 alternatives
            'lane_scores': lane_scores,
            'timestamp': datetime.now().isoformat()
        }
        
        # Add selection to history
        self.selection_history.append({
            'timestamp': datetime.now().isoformat(),
            'data_type': data_type,
            'bit_depth': bit_depth,
            'selected_lane': best_lane,
            'score': best_score
        })
        
        logger.info(f"Lane selected: {best_lane} with score {best_score:.4f}")
        return selection
    
    def visualize_lane_selection(self, selection: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create visualization of lane selection process.
        
        Args:
            selection: Result from select_optimal_lane
            
        Returns:
            Visualization data
        """
        try:
            # Create arrays for visualization
            lanes = list(selection['lane_scores'].keys())
            scores = [selection['lane_scores'][lane]['overall_score'] for lane in lanes]
            
            # Create directory for visualizations if it doesn't exist
            import os
            os.makedirs("phi_lane_results", exist_ok=True)
            
            # Create radar chart of lane characteristics
            plt.figure(figsize=(15, 10))
            
            # Bar chart of lane scores
            plt.subplot(2, 2, 1)
            bars = plt.bar(lanes, scores, color='skyblue')
            # Highlight selected lane
            bars[lanes.index(selection['selected_lane'])].set_color('gold')
            plt.xlabel('Fibonacci Lane')
            plt.ylabel('Selection Score')
            plt.title('Lane Selection Scores')
            plt.grid(True, axis='y', alpha=0.3)
            
            # Plot score breakdown for selected lane
            plt.subplot(2, 2, 2)
            selected = selection['selected_lane']
            score_data = selection['lane_scores'][selected]
            score_types = ['Overall', 'Type Match', 'Bit Depth', 'Phi-Resonance']
            score_values = [
                score_data['overall_score'],
                score_data['type_score'],
                score_data['bit_score'],
                score_data['resonance_score']
            ]
            plt.bar(score_types, score_values, color=['gold', 'lightgreen', 'lightblue', 'salmon'])
            plt.xlabel('Score Component')
            plt.ylabel('Score Value')
            plt.title(f'Score Breakdown for Lane {selected}')
            plt.ylim(0, 1.0)
            plt.grid(True, axis='y', alpha=0.3)
            
            # Plot lane characteristic comparison
            plt.subplot(2, 1, 2)
            lane_props = ['stability', 'energy_efficiency', 'phi_resonance']
            selected_profile = self.lane_profiles[selected]
            
            # Collect data for alternative lanes
            compare_lanes = [selected] + [alt['lane'] for alt in selection['alternatives']]
            x = np.arange(len(lane_props))
            width = 0.2
            
            # Plot characteristics for each lane
            for i, lane in enumerate(compare_lanes):
                if lane in self.lane_profiles:
                    profile = self.lane_profiles[lane]
                    values = [profile[prop] for prop in lane_props]
                    plt.bar(x + i*width, values, width, 
                           label=f'Lane {lane}',
                           alpha=0.7)
            
            plt.xlabel('Characteristic')
            plt.ylabel('Value')
            plt.title('Lane Characteristic Comparison')
            plt.xticks(x + width, lane_props)
            plt.ylim(0, 1.0)
            plt.legend()
            plt.grid(True, axis='y', alpha=0.3)
            
            # Save plot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"phi_lane_results/lane_selection_{timestamp}.png"
            plt.tight_layout()
            plt.savefig(filename)
            plt.close()
            
            visualization = {
                'lanes': lanes,
                'scores': scores,
                'selected_lane': selection['selected_lane'],
                'plot_saved': filename
            }
            
            logger.info(f"Lane selection visualization saved to {filename}")
            return visualization
            
        except Exception as e:
            logger.error(f"Error creating visualization: {str(e)}")
            return {'error': str(e)}
    
    def run_test_with_data(self, data: Any, data_type: Optional[str] = None, bit_depth: Optional[int] = None) -> Dict[str, Any]:
        """
        Run complete lane selection test with provided data.
        
        Args:
            data: Data to analyze
            data_type: Optional data type hint
            bit_depth: Optional explicit bit depth
            
        Returns:
            Complete test results
        """
        # Analyze data
        analysis = self.analyze_data(data, data_type, bit_depth)
        
        # Select optimal lane
        selection = self.select_optimal_lane(analysis)
        
        # Visualize selection
        visualization = self.visualize_lane_selection(selection)
        
        # Compile complete results
        results = {
            'data_analysis': analysis,
            'lane_selection': selection,
            'visualization': visualization,
            'timestamp': datetime.now().isoformat()
        }
        
        return results
    
    def integrate_with_orchestrator(self, orchestrator: Any) -> Dict[str, Any]:
        """
        Connect with the phi-harmonic orchestrator.
        
        Args:
            orchestrator: PhiHarmonicOrchestrator instance
            
        Returns:
            Integration status
        """
        # In a real implementation, this would register with the orchestrator
        # For now, we'll just return a status dict
        
        status = {
            'integrated': True,
            'component_name': 'lane_selector',
            'available_lanes': list(self.lane_profiles.keys()),
            'capabilities': [
                'data_analysis',
                'lane_selection',
                'phi_resonance_calculation',
                'visualization'
            ],
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"Integrated with orchestrator: {status['component_name']}")
        return status


def main():
    """Simple demonstration of the Phi-Lane Selector"""
    print("=== Phi-Lane Selector Demo ===")
    selector = PhiLaneSelector()
    
    print("\nAvailable lanes and their profiles:")
    for lane, profile in selector.lane_profiles.items():
        print(f"Lane {lane}: Optimal for {profile['optimal_for']}")
    
    # Test with different data types
    test_data = [
        {
            'data': "10110101001010101011010101001010",
            'type': 'binary',
            'name': "Binary Data"
        },
        {
            'data': "Set target coordinates to (34.05, -118.25)",
            'type': 'command',
            'name': "Command Message"
        },
        {
            'data': "The quantum harmonic oscillation exhibits phi-resonance as predicted.",
            'type': 'text',
            'name': "Text Message"
        },
        {
            'data': bytes([int((np.sin(i * np.pi * 0.1) + 1) * 127) for i in range(64)]),
            'type': 'harmonic',
            'name': "Harmonic Wave Pattern"
        },
        {
            'data': bytes([int((i * 1.618) % 256) for i in range(128)]),
            'type': 'complex',
            'name': "Complex Phi Pattern"
        }
    ]
    
    print("\nRunning tests with different data types:")
    for test in test_data:
        print(f"\nTesting with {test['name']}...")
        results = selector.run_test_with_data(test['data'], test['type'])
        analysis = results['data_analysis']
        selection = results['lane_selection']
        
        print(f"Data type: {analysis['data_type']}")
        print(f"Bit depth: {analysis['bit_depth']}")
        print(f"Phi-resonance: {analysis['phi_resonance']:.4f}")
        print(f"Selected lane: {selection['selected_lane']} (score: {selection['score']:.4f})")
        
        if selection['alternatives']:
            alt = selection['alternatives'][0]
            print(f"Top alternative: Lane {alt['lane']} (score: {alt['score']:.4f})")
        
        if 'visualization' in results and 'plot_saved' in results['visualization']:
            print(f"Visualization saved to: {results['visualization']['plot_saved']}")
    
    print("\nDemo complete")


if __name__ == "__main__":
    main()
