import numpy as np
from phi_processor import PhiProcessor
import time

def test_scaling_efficiency():
    processor = PhiProcessor()
    sizes = [1000, 10000, 100000]
    
    print("Testing φ-based Processing Efficiency")
    print("====================================")
    
    for size in sizes:
        data = np.random.random(size)
        
        # Test φ-based processing
        start = time.time()
        result, efficiency = processor.meta_learn(data)
        phi_time = time.time() - start
        
        # Test traditional processing
        start = time.time()
        trad_result = np.fft.fft(data)
        trad_time = time.time() - start
        
        speedup = trad_time / phi_time
        print(f"\nData Size: {size}")
        print(f"φ Processing Time: {phi_time:.4f}s")
        print(f"Traditional Time: {trad_time:.4f}s")
        print(f"Speedup: {speedup:.2f}x")
        print(f"Efficiency: {efficiency:.2f}")
        print(f"Active Bridges: {len(processor.quantum_bridges)}")

if __name__ == "__main__":
    test_scaling_efficiency()
