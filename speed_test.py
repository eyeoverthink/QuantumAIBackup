"""
Speed Test: φ-System vs Traditional
"""

import numpy as np
import time
from typing import Dict, List
from creative_quantum import CreativeQuantum
from creative_system import CreativeSystem

class SpeedTest:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.quantum = CreativeQuantum()
        self.creative = CreativeSystem()
        
    def test_traditional_music(self, duration: float = 4.0) -> Dict:
        """Traditional music generation"""
        start = time.perf_counter_ns()
        
        # Basic frequencies (standard scale)
        sr = 44100
        t = np.linspace(0, duration, int(sr * duration))
        freqs = [440 * 2**(i/12) for i in range(7)]  # Standard scale
        
        # Simple harmonics
        signal = np.zeros_like(t)
        for i, freq in enumerate(freqs):
            amp = 1.0 / (i + 1)  # Linear falloff
            signal += amp * np.sin(2 * np.pi * freq * t)
        
        # Basic normalization
        signal /= np.max(np.abs(signal))
        
        end = time.perf_counter_ns()
        return {'time': (end - start) / 1e9, 'signal': signal}
    
    def test_traditional_visual(self, size: tuple = (512, 512)) -> Dict:
        """Traditional visual generation"""
        start = time.perf_counter_ns()
        
        # Basic patterns
        x = np.linspace(-2*np.pi, 2*np.pi, size[0])
        y = np.linspace(-2*np.pi, 2*np.pi, size[1])
        X, Y = np.meshgrid(x, y)
        
        # Simple wave pattern
        canvas = np.zeros((*size, 3))
        pattern = np.sin(X) * np.cos(Y)
        
        # Basic colors
        colors = [(1,0,0), (0,1,0), (0,0,1)]
        for i, color in enumerate(colors):
            canvas += 0.3 * (pattern[:,:,None] * color)
        
        # Basic normalization
        canvas = (canvas - np.min(canvas)) / (np.max(canvas) - np.min(canvas))
        
        end = time.perf_counter_ns()
        return {'time': (end - start) / 1e9, 'canvas': canvas}
    
    def test_traditional_design(self, points: int = 1000) -> Dict:
        """Traditional design generation"""
        start = time.perf_counter_ns()
        
        # Basic spiral
        t = np.linspace(0, 4*np.pi, points)
        r = t
        x = r * np.cos(t)
        y = r * np.sin(t)
        
        # Simple wave modulation
        wave = np.sin(t)
        x *= (1 + 0.2 * wave)
        y *= (1 + 0.2 * wave)
        
        design = np.stack([x, y]).T
        
        end = time.perf_counter_ns()
        return {'time': (end - start) / 1e9, 'design': design}
    
    def run_comparison(self, iterations: int = 10) -> None:
        """Run speed comparison"""
        print("\nSpeed Test: φ-System vs Traditional")
        print("=================================")
        
        # Test arrays
        phi_times = {'music': [], 'visual': [], 'design': []}
        trad_times = {'music': [], 'visual': [], 'design': []}
        
        for i in range(iterations):
            print(f"\nIteration {i+1}/{iterations}")
            
            # φ-System
            print("\nφ-System:")
            start = time.perf_counter_ns()
            music = self.creative.compose_music()
            end = time.perf_counter_ns()
            phi_times['music'].append((end - start) / 1e9)
            print(f"Music:  {phi_times['music'][-1]*1000:.3f} ms")
            
            start = time.perf_counter_ns()
            visual = self.creative.create_visual()
            end = time.perf_counter_ns()
            phi_times['visual'].append((end - start) / 1e9)
            print(f"Visual: {phi_times['visual'][-1]*1000:.3f} ms")
            
            start = time.perf_counter_ns()
            design = self.creative.generate_design()
            end = time.perf_counter_ns()
            phi_times['design'].append((end - start) / 1e9)
            print(f"Design: {phi_times['design'][-1]*1000:.3f} ms")
            
            # Traditional
            print("\nTraditional:")
            trad = self.test_traditional_music()
            trad_times['music'].append(trad['time'])
            print(f"Music:  {trad_times['music'][-1]*1000:.3f} ms")
            
            trad = self.test_traditional_visual()
            trad_times['visual'].append(trad['time'])
            print(f"Visual: {trad_times['visual'][-1]*1000:.3f} ms")
            
            trad = self.test_traditional_design()
            trad_times['design'].append(trad['time'])
            print(f"Design: {trad_times['design'][-1]*1000:.3f} ms")
        
        # Results
        print("\nFinal Results:")
        print("=============")
        print("\nφ-System Average:")
        for mode in ['music', 'visual', 'design']:
            avg = np.mean(phi_times[mode]) * 1000
            std = np.std(phi_times[mode]) * 1000
            print(f"{mode.title():6s}: {avg:.3f} ± {std:.3f} ms")
        
        print("\nTraditional Average:")
        for mode in ['music', 'visual', 'design']:
            avg = np.mean(trad_times[mode]) * 1000
            std = np.std(trad_times[mode]) * 1000
            print(f"{mode.title():6s}: {avg:.3f} ± {std:.3f} ms")
        
        # Speedup
        print("\nSpeedup (Traditional/φ):")
        for mode in ['music', 'visual', 'design']:
            phi_avg = np.mean(phi_times[mode])
            trad_avg = np.mean(trad_times[mode])
            speedup = trad_avg / phi_avg
            print(f"{mode.title():6s}: {speedup:.3f}x")

if __name__ == "__main__":
    test = SpeedTest()
    test.run_comparison()
