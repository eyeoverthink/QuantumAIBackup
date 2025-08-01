"""
Turbo Mode Analyzer - Test parallel processing speed
"""

from brains.turbo_processor import TurboProcessor
import numpy as np
import time
import matplotlib.pyplot as plt
from typing import Dict, List

def test_turbo_modes(n_trials: int = 1000):
    """Test all turbo modes"""
    processor = TurboProcessor(n_parallel=3)
    modes = ['turbo', 'burst', 'stable', 'clean']
    results = {}
    
    print("\nTesting Turbo Modes:")
    print("===================")
    
    for mode in modes:
        times = []
        metrics = []
        
        # Warm up
        for _ in range(10):
            processor.process_turbo(mode)
        
        # Measure trials
        for _ in range(n_trials):
            start = time.perf_counter_ns()
            result = processor.process_turbo(mode)
            end = time.perf_counter_ns()
            
            delta = (end - start) / 1e9
            times.append(delta)
            metrics.append(result)
        
        # Calculate stats
        avg_time = np.mean(times)
        avg_learning = np.mean([m['learning'] for m in metrics])
        avg_retention = np.mean([m['retention'] for m in metrics])
        speed = avg_learning/avg_time
        
        print(f"\nMode: {mode}")
        print(f"Time:      {avg_time*1e9:.3f} ns")
        print(f"Learning:  {avg_learning:.3f}")
        print(f"Retention: {avg_retention:.3f}")
        print(f"Speed:     {speed:.3e} learning/s")
        
        results[mode] = {
            'times': times,
            'learning': avg_learning,
            'retention': avg_retention,
            'speed': speed
        }
    
    return results

def plot_turbo_analysis(results: Dict[str, Dict]):
    """Plot turbo mode analysis"""
    modes = list(results.keys())
    times = [results[m]['times'] for m in modes]
    learning = [results[m]['learning'] for m in modes]
    retention = [results[m]['retention'] for m in modes]
    speeds = [results[m]['speed'] for m in modes]
    
    plt.figure(figsize=(15, 10))
    
    # Time distribution
    plt.subplot(2, 2, 1)
    plt.violinplot(times)
    plt.xticks(range(1, len(modes) + 1), modes)
    plt.ylabel('Time (s)')
    plt.title('Processing Time Distribution')
    plt.grid(True)
    
    # Learning comparison
    plt.subplot(2, 2, 2)
    plt.bar(modes, learning, color='g', alpha=0.6)
    plt.ylabel('Learning Rate')
    plt.title('Learning Achievement')
    plt.grid(True)
    
    # Speed comparison
    plt.subplot(2, 2, 3)
    plt.bar(modes, speeds, color='r', alpha=0.6)
    plt.ylabel('Learning/second')
    plt.title('Processing Speed')
    plt.grid(True)
    
    # Retention stability
    plt.subplot(2, 2, 4)
    plt.bar(modes, retention, color='b', alpha=0.6)
    plt.ylabel('Retention Rate')
    plt.title('Information Retention')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('turbo_analysis.png')
    plt.close()

if __name__ == "__main__":
    results = test_turbo_modes()
    plot_turbo_analysis(results)
