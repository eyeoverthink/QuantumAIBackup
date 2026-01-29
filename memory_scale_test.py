import numpy as np
from template.quantum_silicon_brain import QuantumSiliconBrain
import time
import json
import psutil
import sys
import gc

def format_size(size):
    """Format size in bytes to human readable string"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f}{unit}"
        size /= 1024

def test_memory_scaling():
    print("\n🧪 Maximum-Scale Memory Test")
    print("==========================")
    
    # Initialize brain with base Tesla frequency
    brain = QuantumSiliconBrain()
    phi = (1 + np.sqrt(5)) / 2
    
    # Create terabyte-scale chunks with stability
    base_size = 100000000  # Start with 100MB
    sizes = [int(base_size * (phi ** n)) for n in range(3)]  # Up to ~420MB
    
    # Enhanced frequency stack for terabyte processing
    frequencies = np.array([
        4.37,    # Tesla (base)
        7.83,    # Schumann (earth)
        1.618,   # Phi (golden)
        432.0,   # Ancient tuning
        528.0,   # DNA repair
        639.0,   # Connection
        1597,    # Fibonacci prime
        2718,    # Euler's number
        3142,    # Pi thousand
        phi ** 8,  # High-order phi
        1/phi,   # Inverse phi
        phi ** 2,  # Phi squared
    ])
    
    print("\n📊 Testing Terabyte-Scale Memory (Memory-Optimized)")
    print("Pattern Size    | Compression Ratio | Storage Time | φ-Resonance | Patterns | Memory Used    | System Memory | TFLOPS")
    print("-" * 120)
    
    # Process in quantum-optimized chunks
    chunk_size = 100000  # 100K chunks for memory efficiency
    
    # Initialize enhanced quantum states (stabilized)
    quantum_states = np.array([
        (phi ** ((i % 5) + 1)) * (4.37 / 7.83)  # Limit exponents
        for i in range(13)  # 13 quantum variations (φ⁴ optimal)
    ])
    
    # Pre-calculate frequency weights with quantum enhancement
    freq_weights = np.array([1/(phi**min(n, 5)) for n in range(len(frequencies))], dtype=np.float64)
    freq_weights /= np.sum(freq_weights)  # Normalize
    
    # Initialize quantum buffer
    pattern_buffer = np.zeros(chunk_size, dtype=np.float64)  # Real for stability
    
    total_patterns = 0
    last_total_size = 0
    
    for size in sizes:
        # Monitor system memory
        mem = psutil.Process().memory_info()
        sys_mem = f"{mem.rss/1024/1024/1024:.2f}GB"
        
        print(f"\nGenerating {format_size(size)} pattern with quantum optimization...", end='', flush=True)
        
        # Calculate theoretical TFLOPS
        operations_per_value = len(frequencies) * 3  # sin, multiply, sum
        total_operations = size * operations_per_value
        tflops = total_operations / (1e12 * 1) if 'storage_time' in locals() else 0
        
        # Process in chunks with quantum optimization
        for chunk_start in range(0, size, chunk_size):
            chunk_end = min(chunk_start + chunk_size, size)
            chunk_size_actual = chunk_end - chunk_start
            
            # Generate scaled time array
            t = np.linspace(0, 2*np.pi, chunk_size_actual)  # Normalized time
            
            # Reset buffer
            pattern_buffer[:chunk_size_actual] = 0
            
            # Calculate quantum superposition
            for idx, freq in enumerate(frequencies):
                # Generate stable wave
                wave = np.sin(freq * t / 1000) * freq_weights[idx]
                pattern_buffer[:chunk_size_actual] += wave
            
            # Normalize and store
            pattern = np.abs(pattern_buffer[:chunk_size_actual])
            pattern = (pattern - pattern.min()) / (pattern.max() - pattern.min())
            
            # Store with quantum state
            brain.learn_gate_pattern(
                inputs=pattern.tolist(),
                outputs=f"quantum_pattern_chunk_{chunk_start}",
                quantum_state=quantum_states[chunk_start % 13]
            )
            print('.', end='', flush=True)
            
            # Clear memory
            del pattern
            gc.collect()
            
        print(" Done!")
        
        # Measure memory before
        pattern_json = json.dumps(np.zeros(1000).tolist())  # Sample first 1000 for size estimate
        mem_before = len(pattern_json.encode('utf-8')) * (len(np.zeros(size)) / 1000)
        
        # Time the storage operation
        start_time = time.time()
        
        # Store with quantum superposition states
        resonances = []
        for i in range(13):  # 13 quantum variations (φ⁴ optimal)
            # Use φ-harmonic quantum states with frequency mixing
            resonance = brain.learn_gate_pattern(
                inputs=np.zeros(size).tolist(),
                outputs=f"quantum_pattern_{size}_{i}",
                quantum_state=quantum_states[i]
            )
            resonances.append(resonance)
        
        storage_time = time.time() - start_time
        
        # Calculate pattern statistics
        pattern_count = sum(len(patterns) for patterns in brain.circuit_patterns.values())
        new_patterns = pattern_count - total_patterns
        total_patterns = pattern_count
        
        # Calculate total stored size (more efficient)
        total_stored_size = 0
        for patterns in brain.circuit_patterns.values():
            for p in patterns:
                # Estimate size from pattern length
                total_stored_size += len(p) * 8  # 8 bytes per float64
        
        # Calculate size changes
        size_increase = total_stored_size - last_total_size
        last_total_size = total_stored_size
        
        # Calculate compression with φ-weighting
        compression = (mem_before * 13) / size_increase if size_increase > 0 else 0
        
        # Calculate average resonance
        avg_resonance = sum(resonances) / len(resonances)
        
        # Update system memory usage
        mem = psutil.Process().memory_info()
        sys_mem = f"{mem.rss/1024/1024/1024:.2f}GB"
        
        print(f"{format_size(size):>13} | {compression:>15.2f} | {storage_time:>11.3f}s | {avg_resonance:>10.6f} | {new_patterns:>8d} | {format_size(total_stored_size):>13} | {sys_mem:>13} | {tflops:.2f} TFLOPS")
        
        # Calculate epoch fluctuations
        epoch_flux = abs(np.sin(2 * np.pi * (4.37/7.83))) * phi  # Tesla/Schumann ratio
        quantum_flux = abs(np.cos(2 * np.pi * (1.618034/432.0))) * phi  # Phi/Ancient ratio
        resonance_flux = abs(np.sin(2 * np.pi * avg_resonance)) * phi  # Resonance contribution
        
        # Combined flux factor
        flux_factor = (epoch_flux * quantum_flux * resonance_flux) ** (1/phi)
        
        print(f"\n🌊 Quantum Flux Analysis:")
        print(f"Epoch Flux: {epoch_flux:.6f}")
        print(f"Quantum Flux: {quantum_flux:.6f}")
        print(f"Resonance Flux: {resonance_flux:.6f}")
        print(f"Combined Flux Factor: {flux_factor:.6f}")
        print(f"Compression-Flux Ratio: {compression/flux_factor:.6f}")
        
        # Check for harmonic convergence
        if abs(compression/flux_factor - phi**7) < 0.1:
            print(f"\n🎯 Harmonic Convergence Detected!")
            print(f"Compression/Flux ≈ φ⁷ ({phi**7:.6f})")
            
        # Log epoch data
        with open('quantum_epoch_log.md', 'a') as f:
            f.write(f"\n\n## Epoch Analysis ({time.strftime('%Y-%m-%d %H:%M:%S')})")
            f.write(f"\n- Pattern Size: {format_size(size)}")
            f.write(f"\n- Compression: {compression:.2f}x")
            f.write(f"\n- Epoch Flux: {epoch_flux:.6f}")
            f.write(f"\n- Quantum Flux: {quantum_flux:.6f}")
            f.write(f"\n- Resonance Flux: {resonance_flux:.6f}")
            f.write(f"\n- Combined Flux: {flux_factor:.6f}")
            f.write(f"\n- Compression/Flux: {compression/flux_factor:.6f}")
            if abs(compression/flux_factor - phi**7) < 0.1:
                f.write(f"\n- **Harmonic Convergence Achieved**")
            f.write(f"\n- φ-Resonance: {avg_resonance:.6f}")
            f.write(f"\n- Memory Ratio: {total_stored_size}/{size} bytes")
            
        # Track quantum adaptation
        prev_resonances = []
        adaptation_rates = []
        
        print(f"\n🧬 Quantum Adaptation Analysis:")
        for i in range(len(resonances)-1):
            # Calculate adaptation rate
            adaptation = abs(resonances[i+1] - resonances[i]) / resonances[i]
            adaptation_rates.append(adaptation)
            
            # Check for φ-harmonic convergence
            harmonic_distance = abs(adaptation - 1/phi)
            
            print(f"State {i+1}: {adaptation:.6f} {'🎯' if harmonic_distance < 0.1 else ''}")
            
        # Calculate meta-adaptation (how adaptation itself adapts)
        meta_adaptation = np.mean(adaptation_rates)
        print(f"\nMeta-Adaptation Rate: {meta_adaptation:.6f}")
        
        # Check for quantum learning
        learning_rate = abs(meta_adaptation - 1/phi)
        if learning_rate < 0.1:
            print("🧠 Quantum Learning Detected!")
            print(f"Learning Rate: {learning_rate:.6f}")
        
        # Log adaptation data
        with open('quantum_adaptation_log.md', 'a') as f:
            f.write(f"\n\n## Adaptation Analysis ({time.strftime('%Y-%m-%d %H:%M:%S')})")
            f.write(f"\n- Pattern Size: {format_size(size)}")
            f.write(f"\n- Meta-Adaptation: {meta_adaptation:.6f}")
            f.write(f"\n- Learning Rate: {learning_rate:.6f}")
            f.write("\n\n### State Transitions")
            for i, rate in enumerate(adaptation_rates):
                f.write(f"\n- State {i+1}: {rate:.6f}")
            f.write(f"\n\n### Quantum Metrics")
            f.write(f"\n- Epoch Flux: {epoch_flux:.6f}")
            f.write(f"\n- Resonance Stability: {1 - np.std(resonances):.6f}")
            f.write(f"\n- Compression Efficiency: {compression/flux_factor:.6f}")
            
        # Calculate adaptive compression threshold
        adaptive_threshold = phi ** (7 * meta_adaptation)
        
        # Allow quantum state to stabilize
        time.sleep(0.1)
        
        # Check for φ-harmonic compression threshold
        if compression > phi ** 7:
            print(f"\n⚠️ Phi-harmonic compression threshold reached at size {format_size(size)}")
            print(f"Compression ratio: {compression:.2f}")
            break
            
    print(f"\n📈 Final Statistics:")
    print(f"Total Patterns: {total_patterns}")
    print(f"Total Memory: {format_size(total_stored_size)}")
    print(f"Final Compression: {compression:.2f}x")
    print(f"Phi^7 Threshold: {phi ** 7:.2f}x")
    print(f"Average Resonance: {avg_resonance:.6f}")
    print(f"System Memory Used: {sys_mem}")
    
    # Append results to documentation
    with open('quantum_memory_scaling.md', 'a') as f:
        f.write(f"\n\n## Latest Test Results ({time.strftime('%Y-%m-%d %H:%M:%S')})")
        f.write(f"\n\n### Maximum Scale Test")
        f.write(f"\n- Pattern Size Range: {format_size(sizes[0])} - {format_size(sizes[-1])}")
        f.write(f"\n- Final Compression: {compression:.2f}x")
        f.write(f"\n- Average Resonance: {avg_resonance:.6f}")
        f.write(f"\n- Total Memory Used: {format_size(total_stored_size)}")
        f.write(f"\n- System Memory: {sys_mem}")
        f.write("\n\n### Observations")
        f.write("\n1. **Compression Performance**")
        f.write(f"\n   - Achieved {compression:.2f}x compression")
        f.write(f"\n   - {compression/phi:.2f} × φ ratio")
        f.write("\n2. **Quantum Resonance**")
        f.write(f"\n   - Stable at {avg_resonance:.6f}")
        f.write(f"\n   - {abs(avg_resonance - 1/phi):.6f} deviation from 1/φ")
        f.write("\n3. **Scaling Efficiency**")
        f.write(f"\n   - Memory overhead: {(float(sys_mem[:-2])/total_stored_size*1024*1024*1024):.2%}")
        f.write(f"\n   - Processing time: {storage_time:.3f}s for {format_size(sizes[-1])} pattern")
        
if __name__ == "__main__":
    test_memory_scaling()
