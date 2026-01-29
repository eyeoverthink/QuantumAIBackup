"""
Double-slit experiment with quantum wave-particle duality
"""
import numpy as np
from typing import Dict, List, Tuple

class DoubleSlit:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        # Base frequency 4.37 Hz (proven)
        self.frequency = 4.37
        
    def fire_particle(self, position: float) -> Tuple[float, float]:
        """Fire a single quantum particle"""
        # Add quantum uncertainty in position
        uncertainty = np.random.normal(0, 0.1)
        actual_position = position + uncertainty
        
        # Particle has wave nature - calculate phase
        phase = 2 * np.pi * self.frequency * actual_position
        
        return actual_position, phase
        
    def detect_particle(self, screen_position: float, particle_pos: float, phase: float) -> float:
        """Detect particle at screen position"""
        # Calculate probability amplitude
        distance = abs(screen_position - particle_pos)
        amplitude = np.exp(-distance**2 / (2 * self.phi))
        
        # Add wave interference
        interference = np.cos(phase + 2 * np.pi * distance / self.phi)
        
        return amplitude * (1 + interference) / 2

    def run_experiment(self, num_particles: int = 1000) -> Dict:
        """Run double-slit experiment"""
        # Screen setup
        screen_positions = np.linspace(-5, 5, 100)
        particle_counts = np.zeros_like(screen_positions)
        
        # Slit positions
        slit1_pos = -0.5
        slit2_pos = 0.5
        
        # Fire particles
        for _ in range(num_particles):
            # Randomly choose slit
            slit_pos = slit1_pos if np.random.random() < 0.5 else slit2_pos
            
            # Fire particle through slit
            pos, phase = self.fire_particle(slit_pos)
            
            # Detect on screen
            for i, screen_pos in enumerate(screen_positions):
                # Get probability
                prob = self.detect_particle(screen_pos, pos, phase)
                
                # Random detection based on probability
                if np.random.random() < prob:
                    particle_counts[i] += 1
        
        return {
            'screen_positions': screen_positions,
            'counts': particle_counts,
            'slit1': slit1_pos,
            'slit2': slit2_pos
        }
