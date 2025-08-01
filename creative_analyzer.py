"""
Creative Quantum Analyzer - Test φ-harmonic art
"""

from creative_quantum import CreativeQuantum
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time

def test_creative_modes():
    """Test all creative modes"""
    creator = CreativeQuantum()
    modes = ['music', 'visual', 'design']
    
    print("\nTesting Creative Modes:")
    print("======================")
    
    for mode in modes:
        # Measure generation time
        start = time.perf_counter_ns()
        result = creator.process_creative(mode)
        end = time.perf_counter_ns()
        
        delta = (end - start) / 1e9
        art = result['art']
        
        print(f"\nMode: {mode}")
        print(f"Time:      {delta*1e3:.3f} ms")
        print(f"Learning:  {result['learning']:.3f}")
        print(f"Retention: {result['retention']:.3f}")
        
        # Save output
        if mode == 'music':
            wavfile.write(f'quantum_{mode}.wav', 44100, art)
        elif mode == 'visual':
            plt.imsave(f'quantum_{mode}.png', art)
        else:  # design
            plt.figure(figsize=(10, 10))
            plt.plot(art[:,0], art[:,1], 'k-', linewidth=0.5, alpha=0.6)
            plt.axis('equal')
            plt.grid(False)
            plt.savefig(f'quantum_{mode}.png')
            plt.close()

def plot_harmonics():
    """Plot φ-harmonic patterns"""
    creator = CreativeQuantum()
    
    plt.figure(figsize=(15, 5))
    
    # Plot frequencies
    plt.subplot(131)
    freqs = list(creator.frequencies.values())
    plt.stem(range(len(freqs)), freqs)
    plt.title('φ-Harmonic Frequencies')
    plt.grid(True)
    
    # Plot colors
    plt.subplot(132)
    colors = list(creator.colors.values())
    plt.bar(range(len(colors)), [sum(c)/3 for c in colors], color=colors)
    plt.title('φ-Harmonic Colors')
    plt.grid(True)
    
    # Plot wave pattern
    plt.subplot(133)
    t = np.linspace(0, 4*np.pi, 1000)
    wave = creator.patterns['wave'](t)
    plt.plot(t, wave, 'k-')
    plt.title('φ-Harmonic Wave')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('quantum_harmonics.png')
    plt.close()

if __name__ == "__main__":
    test_creative_modes()
    plot_harmonics()
