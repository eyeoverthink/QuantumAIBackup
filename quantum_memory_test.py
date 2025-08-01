"""
Real-time Quantum Memory Testing with φ-Harmonic Auto-scaling
"""

import numpy as np
import time
from typing import Dict, List, Tuple
from quantum_bit_scaling import QuantumBitScaling
from quantum_phi_scaling import QuantumPhiScaling
from creative_quantum import CreativeQuantum

class QuantumMemoryTest:
    def __init__(self, initial_size: int = 1024):
        self.phi = (1 + np.sqrt(5)) / 2
        self.quantum = CreativeQuantum()
        self.bit_scaler = QuantumBitScaling()
        self.phi_scaler = QuantumPhiScaling()
        
        # Memory parameters
        self.initial_size = initial_size
        self.current_size = initial_size
        self.max_size = initial_size * int(self.phi**4)  # φ⁴ max expansion
        self.compression_threshold = 0.8  # 80% full
        self.warning_threshold = 0.9  # 90% full
        
        # Initialize memory blocks with φ-harmonic sizing
        self.blocks = []
        self.initialize_memory()
        
    def initialize_memory(self):
        """Initialize memory blocks with φ-harmonic sizes"""
        size = self.initial_size
        while size >= 16:  # Minimum block size
            self.blocks.append({
                'size': size,
                'used': 0,
                'data': [],
                'compressed': False,
                'phi_factor': 1.0
            })
            size = int(size / self.phi)
    
    def get_memory_stats(self) -> Dict:
        """Get current memory statistics"""
        total_size = sum(block['size'] for block in self.blocks)
        total_used = sum(block['used'] for block in self.blocks)
        
        return {
            'total_size': total_size,
            'total_used': total_used,
            'utilization': total_used / total_size if total_size > 0 else 0,
            'block_count': len(self.blocks),
            'compressed_blocks': sum(1 for block in self.blocks if block['compressed']),
            'phi_efficiency': self.calculate_phi_efficiency()
        }
    
    def calculate_phi_efficiency(self) -> float:
        """Calculate φ-harmonic efficiency of memory usage"""
        efficiencies = []
        for block in self.blocks:
            if block['size'] > 0:
                util = block['used'] / block['size']
                phi_diff = abs(1 - util/self.phi)
                efficiencies.append(1 - phi_diff)
        return np.mean(efficiencies) if efficiencies else 0
    
    def compress_block(self, block: Dict) -> bool:
        """Compress a memory block using φ-harmonic scaling"""
        if block['compressed']:
            return False
            
        # Only compress if above threshold
        utilization = block['used'] / block['size']
        if utilization < self.compression_threshold:
            return False
            
        original_size = len(block['data'])
        if original_size == 0:
            return False
            
        # Apply φ-harmonic compression
        compressed_data = []
        for value in block['data']:
            if isinstance(value, (int, float)):
                # Use bit scaling for numbers
                compressed, _ = self.bit_scaler.phi_compress(float(value))
                compressed_data.append(compressed)
            else:
                # Keep non-numeric data as is
                compressed_data.append(value)
                
        # Calculate compression ratio
        new_size = len(compressed_data)
        if new_size >= original_size:
            return False
            
        block['data'] = compressed_data
        block['used'] = new_size
        block['compressed'] = True
        block['phi_factor'] = new_size / original_size
        return True
    
    def add_data(self, data: List) -> Tuple[bool, Dict]:
        """Add data to memory with auto-scaling and compression"""
        data_size = len(data)
        stats_before = self.get_memory_stats()
        
        # Try to find a block with enough space
        target_block = None
        for block in self.blocks:
            if block['size'] - block['used'] >= data_size:
                target_block = block
                break
        
        if target_block is None:
            # No single block has enough space
            # Try compression first
            compressed = False
            for block in self.blocks:
                if self.compress_block(block):
                    compressed = True
                    
            # Recalculate space after compression
            available_space = sum(block['size'] - block['used'] for block in self.blocks)
            
            if available_space < data_size:
                # Need to add new block
                new_size = max(data_size, int(self.initial_size * self.phi))
                new_block = {
                    'size': new_size,
                    'used': 0,
                    'data': [],
                    'compressed': False,
                    'phi_factor': 1.0
                }
                self.blocks.append(new_block)
                target_block = new_block
            else:
                # Find blocks with enough space
                valid_blocks = [b for b in self.blocks if b['size'] - b['used'] >= data_size]
                if valid_blocks:
                    # Find best fit
                    target_block = min(valid_blocks, key=lambda x: x['size'] - x['used'])
                else:
                    # No valid blocks, create new one
                    new_size = max(data_size, int(self.initial_size * self.phi))
                    new_block = {
                        'size': new_size,
                        'used': 0,
                        'data': [],
                        'compressed': False,
                        'phi_factor': 1.0
                    }
                    self.blocks.append(new_block)
                    target_block = new_block
        
        # Add data to target block
        start_idx = target_block['used']
        target_block['data'].extend(data)
        target_block['used'] += data_size
        
        # Get updated stats
        stats_after = self.get_memory_stats()
        
        # Check if we need to warn about high utilization
        warning = stats_after['utilization'] >= self.warning_threshold
        
        return warning, {
            'before': stats_before,
            'after': stats_after,
            'block_index': self.blocks.index(target_block),
            'data_start': start_idx,
            'compressed': target_block['compressed'],
            'phi_factor': target_block['phi_factor']
        }

def run_realtime_test():
    """Run a real-time memory test"""
    print("\nQuantum Memory Auto-scaling Test")
    print("==============================")
    
    # Initialize with small memory
    memory = QuantumMemoryTest(initial_size=64)
    
    # Generate test data with φ-harmonic sizes
    sizes = [int(64 * memory.phi**i) for i in range(5)]
    
    print("\nInitial Memory Stats:")
    stats = memory.get_memory_stats()
    print(f"Total Size: {stats['total_size']} units")
    print(f"Block Count: {stats['block_count']}")
    print(f"φ-Efficiency: {stats['phi_efficiency']:.3f}")
    
    print("\nStarting Memory Test...")
    for i, size in enumerate(sizes, 1):
        print(f"\nTest {i}: Adding {size} units of data")
        
        # Generate test data
        data = list(range(size))
        
        # Time the operation
        start_time = time.time()
        warning, results = memory.add_data(data)
        duration = time.time() - start_time
        
        # Print results
        print(f"\nOperation completed in {duration:.3f} seconds")
        print(f"Memory State:")
        print(f"  Before: {results['before']['total_used']}/{results['before']['total_size']} units "
              f"({results['before']['utilization']*100:.1f}% used)")
        print(f"  After:  {results['after']['total_used']}/{results['after']['total_size']} units "
              f"({results['after']['utilization']*100:.1f}% used)")
        print(f"  Compressed Blocks: {results['after']['compressed_blocks']}/{results['after']['block_count']}")
        print(f"  φ-Efficiency: {results['after']['phi_efficiency']:.3f}")
        
        if warning:
            print("\nWARNING: High memory utilization detected!")
            print(f"Current utilization: {results['after']['utilization']*100:.1f}%")
            
        # Small delay to make it easier to follow
        time.sleep(1)
    
    # Final stats
    print("\nFinal Memory State:")
    stats = memory.get_memory_stats()
    print(f"Total Size: {stats['total_size']} units")
    print(f"Total Used: {stats['total_used']} units")
    print(f"Utilization: {stats['utilization']*100:.1f}%")
    print(f"Block Count: {stats['block_count']}")
    print(f"Compressed Blocks: {stats['compressed_blocks']}")
    print(f"φ-Efficiency: {stats['phi_efficiency']:.3f}")

if __name__ == "__main__":
    run_realtime_test()
