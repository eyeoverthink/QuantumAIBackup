import numpy as np
from decimal import Decimal
import math
import sys
sys.path.append('../QHRCSystem/core')
sys.path.append('../QHRCUnified/core')
sys.path.append('../PhiResonanceSystem/core')

from brain_bridges import BrainBridge
from qhrc_phi_harmonics import PhiHarmonicProcessor
from phi_resonance_core import PhiResonanceCore

class QuantumUnifiedBrainChess:
    def __init__(self):
        self.phi = float((1 + np.sqrt(5)) / 2)
        self.base_freq = float(Decimal('4.37'))
        self.winning_resonance = 0.96
        
        # Initialize all brain components
        self.brain_bridge = BrainBridge()
        self.phi_processor = PhiHarmonicProcessor()
        self.resonance_core = PhiResonanceCore()
        
        # Neural bridge connections
        self.neural_bridges = {
            'spatial': self.brain_bridge.create_bridge('spatial'),
            'temporal': self.brain_bridge.create_bridge('temporal'),
            'strategic': self.brain_bridge.create_bridge('strategic'),
            'quantum': self.brain_bridge.create_bridge('quantum')
        }
        
    def analyze_position_with_all_brains(self, position):
        """Analyze chess position using all quantum brains"""
        x, y = position
        
        # Get resonance from each brain
        spatial_res = self.neural_bridges['spatial'].process(
            self.phi_processor.calculate_spatial_resonance(x, y)
        )
        
        temporal_res = self.neural_bridges['temporal'].process(
            self.phi_processor.calculate_temporal_resonance(x, y)
        )
        
        strategic_res = self.neural_bridges['strategic'].process(
            self.resonance_core.calculate_strategic_weight(x, y)
        )
        
        quantum_res = self.neural_bridges['quantum'].process(
            self.calculate_quantum_potential(x, y)
        )
        
        # Combine all brain outputs using phi-harmonic weighting
        combined_resonance = (
            spatial_res * self.phi +
            temporal_res * self.phi**2 +
            strategic_res * self.phi**3 +
            quantum_res * self.phi**4
        ) / (self.phi + self.phi**2 + self.phi**3 + self.phi**4)
        
        return combined_resonance
        
    def calculate_quantum_potential(self, x, y):
        """Calculate quantum potential using 4.37 Hz resonance"""
        base_potential = abs(math.sin(x * self.phi)) * abs(math.cos(y * self.phi))
        resonance_factor = self.base_freq * base_potential
        return float(resonance_factor)
        
    def evaluate_move_with_unified_brains(self, move):
        """Evaluate chess move using all quantum brains"""
        from_file, from_rank, to_file, to_rank = move
        
        # Convert chess coordinates
        from_pos = (ord(from_file) - ord('a'), 8 - from_rank)
        to_pos = (ord(to_file) - ord('a'), 8 - to_rank)
        
        # Get unified brain analysis
        from_resonance = self.analyze_position_with_all_brains(from_pos)
        to_resonance = self.analyze_position_with_all_brains(to_pos)
        
        # Calculate move strength using all brain inputs
        move_strength = (to_resonance * self.phi) - (from_resonance * 0.5)
        
        # Apply reality seal from quantum core
        reality_factor = abs(math.sin(self.base_freq * move_strength))
        
        return move_strength * reality_factor
        
    def find_best_move_unified(self):
        """Find best first move using all quantum brains"""
        first_moves = [
            ('e', 2, 'e', 4),  # e4
            ('d', 2, 'd', 4),  # d4
            ('c', 2, 'c', 4),  # c4
            ('g', 1, 'f', 3),  # Nf3
            ('b', 1, 'c', 3),  # Nc3
            ('e', 2, 'e', 3),  # e3
            ('d', 2, 'd', 3),  # d3
            ('f', 2, 'f', 4),  # f4
            ('b', 2, 'b', 3),  # b3
            ('g', 2, 'g', 3),  # g3
        ]
        
        best_move = None
        best_score = float('-inf')
        
        results = []
        for move in first_moves:
            # Get unified brain evaluation
            score = self.evaluate_move_with_unified_brains(move)
            results.append((move, score))
            
            if score > best_score:
                best_score = score
                best_move = move
                
        # Sort results by score
        results.sort(key=lambda x: x[1], reverse=True)
        
        return results, best_move, best_score

# Run unified brain analysis
analyzer = QuantumUnifiedBrainChess()
results, best_move, best_score = analyzer.find_best_move_unified()

print("\nUnified Quantum Brain Chess Analysis")
print("====================================")
print(f"\nBrain Components Active:")
print("- Spatial Brain Bridge")
print("- Temporal Brain Bridge")
print("- Strategic Brain Bridge")
print("- Quantum Brain Bridge")
print("\nMove Analysis (All Brains Combined):")
print("------------------------------------")
for move, score in results:
    print(f"Move {move[0]}{move[1]}-{move[2]}{move[3]}: {score:.4f}")
    
print(f"\nBest Move: {best_move[0]}{best_move[1]}-{best_move[2]}{best_move[3]}")
print(f"Unified Brain Score: {best_score:.4f}")

if best_score >= analyzer.winning_resonance:
    print("\n🌟 QUANTUM BREAKTHROUGH!")
    print("All brain bridges confirm optimal resonance!")
    print(f"Resonance exceeds proven {analyzer.winning_resonance} threshold")
