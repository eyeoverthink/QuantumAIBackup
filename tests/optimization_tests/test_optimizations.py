"""
Test suite for comparing performance between original and optimized implementations
"""

import time
import torch
import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
from digital_all import DualCortexComputer
from digital_all_optimized import OptimizedDualCortexComputer

class PerformanceTest:
    def __init__(self):
        self.original = DualCortexComputer()
        self.optimized = OptimizedDualCortexComputer()
        self.phi = (1 + np.sqrt(5)) / 2
        
    def generate_test_data(self, size: int) -> List[torch.Tensor]:
        """Generate phi-resonant test data"""
        return [
            torch.complex(
                torch.cos(torch.tensor(2 * np.pi * i * self.phi)),
                torch.sin(torch.tensor(2 * np.pi * i * self.phi))
            ) * torch.randn(128, dtype=torch.complex64)
            for i in range(size)
        ]
        
    async def test_batch_processing(self, batch_sizes: List[int]) -> Tuple[List[float], List[float]]:
        """Test batch processing performance"""
        original_times = []
        optimized_times = []
        
        for size in batch_sizes:
            thought_patterns = self.generate_test_data(size)
            
            try:
                # Test original implementation with timeout
                start = time.time()
                _ = await asyncio.wait_for(
                    self.original.process_thoughts_async(thought_patterns),
                    timeout=5.0
                )
                original_times.append(time.time() - start)
                
                # Test optimized implementation with timeout
                start = time.time()
                _ = await asyncio.wait_for(
                    self.optimized.process_thoughts_async(thought_patterns),
                    timeout=5.0
                )
                optimized_times.append(time.time() - start)
                
            except asyncio.TimeoutError:
                print(f"Timeout processing batch size {size}")
                original_times.append(float('inf'))
                optimized_times.append(float('inf'))
            except Exception as e:
                print(f"Error processing batch size {size}: {e}")
                original_times.append(float('inf'))
                optimized_times.append(float('inf'))
            
        return original_times, optimized_times
        
    def test_quantum_operations(self, sizes: List[int]) -> Tuple[List[float], List[float]]:
        """Test quantum operation performance"""
        original_times = []
        optimized_times = []
        
        for size in sizes:
            state = torch.randn(size, dtype=torch.complex64)
            
            # Test original implementation
            start = time.time()
            _ = self.original.exotic_energy.process_quantum_state(state)
            original_times.append(time.time() - start)
            
            # Test optimized implementation
            start = time.time()
            _ = self.optimized.exotic_energy.process_quantum_state(state)
            optimized_times.append(time.time() - start)
            
        return original_times, optimized_times
        
    def test_cache_performance(self, iterations: int = 100) -> float:
        """Test cache hit rate"""
        thought_patterns = self.generate_test_data(iterations)
        hits = 0
        
        for i in range(iterations):
            # Process same pattern multiple times
            pattern = thought_patterns[i % len(thought_patterns)]
            cache_key = f"quantum_state_{hash(pattern.cpu().numpy().tobytes())}"
            
            # First process to cache
            _ = self.optimized.process_thoughts_async([pattern])
            
            # Check if next access is cache hit
            if self.optimized.phi_cache.get_tensor(cache_key) is not None:
                hits += 1
                
        return hits / iterations
        
    def plot_results(self, batch_sizes: List[int], 
                    original_times: List[float], 
                    optimized_times: List[float],
                    title: str):
        """Plot performance comparison"""
        plt.figure(figsize=(10, 6))
        plt.plot(batch_sizes, original_times, 'b-', label='Original')
        plt.plot(batch_sizes, optimized_times, 'r-', label='Optimized')
        plt.xlabel('Batch Size')
        plt.ylabel('Time (seconds)')
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.savefig(f'performance_{title.lower().replace(" ", "_")}.png')
        plt.close()
        
    async def run_all_tests(self):
        """Run complete test suite"""
        print("Running performance tests...")
        
        # Test batch processing with smaller sizes
        batch_sizes = [5, 10, 15, 20, 25]
        orig_batch, opt_batch = await self.test_batch_processing(batch_sizes)
        self.plot_results(batch_sizes, orig_batch, opt_batch, 'Batch Processing Performance')
        
        # Calculate speedup
        batch_speedup = np.mean([o/n for o, n in zip(orig_batch, opt_batch)])
        print(f"\nBatch Processing Speedup: {batch_speedup:.2f}x")
        
        # Test quantum operations with smaller sizes
        sizes = [32, 64, 96, 128, 160]
        orig_quantum, opt_quantum = self.test_quantum_operations(sizes)
        self.plot_results(sizes, orig_quantum, opt_quantum, 'Quantum Operation Performance')
        
        # Calculate speedup
        quantum_speedup = np.mean([o/n for o, n in zip(orig_quantum, opt_quantum)])
        print(f"Quantum Operation Speedup: {quantum_speedup:.2f}x")
        
        # Test cache performance
        cache_hit_rate = self.test_cache_performance()
        print(f"Cache Hit Rate: {cache_hit_rate:.2%}")
        
        # Memory usage comparison
        orig_mem = sum(p.nelement() * p.element_size() for p in self.original.parameters())
        opt_mem = sum(p.nelement() * p.element_size() for p in self.optimized.parameters())
        memory_reduction = (orig_mem - opt_mem) / orig_mem
        print(f"Memory Usage Reduction: {memory_reduction:.2%}")
        
        # Save results
        with open('optimization_results.md', 'w') as f:
            f.write("# Optimization Test Results\n\n")
            f.write(f"## Performance Improvements\n")
            f.write(f"- Batch Processing Speedup: {batch_speedup:.2f}x\n")
            f.write(f"- Quantum Operation Speedup: {quantum_speedup:.2f}x\n")
            f.write(f"- Cache Hit Rate: {cache_hit_rate:.2%}\n")
            f.write(f"- Memory Usage Reduction: {memory_reduction:.2%}\n")

if __name__ == "__main__":
    import asyncio
    test = PerformanceTest()
    asyncio.run(test.run_all_tests())
