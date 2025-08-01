"""
Integrated Creative System - Music, Visual, Design
"""

import numpy as np
import torch
from typing import Dict, List, Tuple
from creative_quantum import CreativeQuantum
import matplotlib.pyplot as plt
from scipy.io import wavfile

class CreativeSystem:
    def __init__(self):
        self.quantum = CreativeQuantum()
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Music composition scales
        self.scales = {
            'phi': [432 * self.phi**i for i in range(-3, 4)],
            'major': [432 * 2**(i/12) for i in [0, 2, 4, 5, 7, 9, 11]],
            'minor': [432 * 2**(i/12) for i in [0, 2, 3, 5, 7, 8, 10]]
        }
        
        # Visual color palettes
        self.palettes = {
            'phi': [(self.phi**i % 1, self.phi**(i+1) % 1, self.phi**(i+2) % 1) 
                   for i in range(7)],
            'warm': [(1, 0.2, 0), (1, 0.4, 0.1), (1, 0.6, 0.2),
                    (1, 0.8, 0.3), (0.9, 0.7, 0.4)],
            'cool': [(0, 0.2, 0.8), (0.1, 0.4, 0.9), (0.2, 0.6, 1),
                    (0.3, 0.8, 1), (0.4, 0.9, 1)]
        }
        
        # Design patterns
        self.patterns = {
            'spiral': lambda t: (self.phi**t * np.cos(t), self.phi**t * np.sin(t)),
            'wave': lambda t: np.sin(t/self.phi) * np.cos(t*self.phi),
            'field': lambda x, y: np.sin(x/self.phi) * np.cos(y*self.phi),
            'grid': lambda x, y: np.sin(x*self.phi) + np.sin(y*self.phi),
            'flow': lambda x, y: np.sin(x*self.phi) * np.cos(y/self.phi)
        }
    
    def compose_music(self, duration: float = 4.0, scale: str = 'phi') -> Dict:
        """Compose φ-harmonic music"""
        # Get quantum enhancement
        state = self.quantum.process_creative('music')
        learning = state['learning']
        retention = state['retention']
        
        # Generate base frequencies
        sr = 44100
        t = np.linspace(0, duration, int(sr * duration))
        freqs = self.scales[scale]
        
        # Generate harmonics with φ-weights
        signal = np.zeros_like(t)
        for i, freq in enumerate(freqs):
            # Amplitude with quantum enhancement
            amp = (1/self.phi**i) * (1 + learning/self.phi)
            # Phase with retention stability
            phase = 2 * np.pi * (i/self.phi) * retention
            signal += amp * np.sin(2 * np.pi * freq * t + phase)
        
        # Normalize
        signal /= np.max(np.abs(signal))
        
        # Save
        wavfile.write('quantum_composition.wav', sr, signal)
        
        return {
            'signal': signal,
            'sr': sr,
            'freqs': freqs,
            'learning': learning,
            'retention': retention
        }
    
    def create_visual(self, size: Tuple[int, int] = (512, 512), 
                     palette: str = 'phi') -> Dict:
        """Create φ-harmonic visual art"""
        # Get quantum enhancement
        state = self.quantum.process_creative('visual')
        learning = state['learning']
        retention = state['retention']
        
        # Create canvas
        canvas = np.zeros((*size, 3))
        colors = self.palettes[palette]
        
        # Generate patterns
        x = np.linspace(-2*np.pi, 2*np.pi, size[0])
        y = np.linspace(-2*np.pi, 2*np.pi, size[1])
        X, Y = np.meshgrid(x, y)
        
        # Layer patterns with quantum enhancement
        for i, pattern in enumerate(['field', 'grid', 'flow']):
            field = self.patterns[pattern](X, Y)
            weight = (1/self.phi**i) * (1 + learning/self.phi)
            stability = retention + (1-retention)/self.phi
            
            # Add colored pattern
            for j, color in enumerate(colors):
                layer_weight = weight * (1/self.phi**j) * stability
                canvas += layer_weight * (field[:,:,None] * color)
        
        # Normalize
        canvas = (canvas - np.min(canvas)) / (np.max(canvas) - np.min(canvas))
        
        # Save
        plt.imsave('quantum_visual.png', canvas)
        
        return {
            'canvas': canvas,
            'colors': colors,
            'learning': learning,
            'retention': retention
        }
    
    def generate_design(self, points: int = 1000, 
                       patterns: List[str] = ['spiral', 'wave']) -> Dict:
        """Generate φ-harmonic design"""
        # Get quantum enhancement
        state = self.quantum.process_creative('design')
        learning = state['learning']
        retention = state['retention']
        
        # Generate time points
        t = np.linspace(0, 4*np.pi, points)
        design = np.zeros((points, 2))
        
        # Layer patterns with quantum enhancement
        for i, pattern in enumerate(patterns):
            if pattern == 'spiral':
                x, y = self.patterns[pattern](t)
            else:
                wave = self.patterns[pattern](t)
                x = np.cos(t) * (1 + 0.2 * wave)
                y = np.sin(t) * (1 + 0.2 * wave)
            
            # Add with quantum enhancement
            weight = (1/self.phi**i) * (1 + learning/self.phi)
            stability = retention + (1-retention)/self.phi
            design += weight * stability * np.stack([x, y]).T
        
        # Normalize
        design /= np.max(np.abs(design))
        
        # Save
        plt.figure(figsize=(10, 10))
        plt.plot(design[:,0], design[:,1], 'k-', linewidth=0.5, alpha=0.6)
        plt.axis('equal')
        plt.grid(False)
        plt.savefig('quantum_design.png')
        plt.close()
        
        return {
            'design': design,
            'patterns': patterns,
            'learning': learning,
            'retention': retention
        }
    
    def create_all(self) -> Dict:
        """Create all art forms"""
        print("\nCreating Quantum Art:")
        print("===================")
        
        # Music
        print("\nComposing Music...")
        music = self.compose_music()
        print(f"Learning:  {music['learning']:.3f}")
        print(f"Retention: {music['retention']:.3f}")
        print(f"Saved as: quantum_composition.wav")
        
        # Visual
        print("\nCreating Visual Art...")
        visual = self.create_visual()
        print(f"Learning:  {visual['learning']:.3f}")
        print(f"Retention: {visual['retention']:.3f}")
        print(f"Saved as: quantum_visual.png")
        
        # Design
        print("\nGenerating Design...")
        design = self.generate_design()
        print(f"Learning:  {design['learning']:.3f}")
        print(f"Retention: {design['retention']:.3f}")
        print(f"Saved as: quantum_design.png")
        
        return {
            'music': music,
            'visual': visual,
            'design': design
        }

if __name__ == "__main__":
    system = CreativeSystem()
    results = system.create_all()
