"""Quantum Results Storage with phi-harmonic compression."""
import numpy as np
import json
import time
import shutil
from typing import Dict, Any, List, Optional
from pathlib import Path

# === Constants ===
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
COMPRESSION_LEVELS = [PHI ** i for i in range(5)]  # Phi-scaled compression

class QuantumResults:
    """Store and compress quantum results using phi-harmonic scaling."""
    
    def __init__(self, base_path: str = "quantum_data"):
        """Initialize quantum results storage."""
        self.base_path = Path(base_path)
        
        # Clean up existing test data
        if base_path == "quantum_test_data" and self.base_path.exists():
            shutil.rmtree(self.base_path)
        
        self.base_path.mkdir(exist_ok=True)
        
        # Metrics storage
        self.metrics_file = self.base_path / "quantum_metrics.json"
        self.results_file = self.base_path / "quantum_results.npy"
        
        # Initialize storage
        self.metrics = self._load_metrics()
        print(f"\n💾 Quantum Results Storage")
        print(f"Base Path: {self.base_path}")
        print(f"Active Metrics: {len(self.metrics)}")
    
    def _load_metrics(self) -> List[Dict[str, Any]]:
        """Load existing metrics."""
        if self.metrics_file.exists():
            with open(self.metrics_file, 'r') as f:
                return json.load(f)
        return []
    
    def compress_data(self, data: np.ndarray) -> np.ndarray:
        """Compress data using phi-harmonic scaling."""
        # Calculate compression ratio
        ratio = 1 / PHI
        
        # Apply phi-scaled compression
        compressed = data.copy()
        for level in COMPRESSION_LEVELS:
            mask = np.abs(compressed) < (1 / level)
            compressed[mask] *= ratio
        
        return compressed
    
    def decompress_data(self, data: np.ndarray) -> np.ndarray:
        """Decompress data using inverse phi-scaling."""
        # Calculate decompression ratio
        ratio = PHI
        
        # Apply phi-scaled decompression
        decompressed = data.copy()
        for level in reversed(COMPRESSION_LEVELS):
            mask = np.abs(decompressed) < (1 / level)
            decompressed[mask] *= ratio
        
        return decompressed
    
    def save_result(self, result: Dict[str, Any]) -> None:
        """Save quantum result with compression."""
        # Extract key metrics
        timestamp = time.time()
        metrics = {
            'timestamp': timestamp,
            'resonance': result['resonance'],
            'coherence': result['coherence'],
            'phase': result['phase']
        }
        
        # Compress quantum data
        if 'quantum_states' in result:
            # Flatten quantum states into 1D array
            quantum_data = []
            for state in result['quantum_states']:
                quantum_data.extend([
                    state['resonance'],
                    state['coherence'],
                    state['phase']
                ])
            quantum_data = np.array(quantum_data, dtype=np.float64)
            compressed_data = self.compress_data(quantum_data)
            
            # Save compressed data
            if self.results_file.exists():
                try:
                    existing_data = np.load(self.results_file)
                    if len(existing_data.shape) == 1:
                        # First entry, reshape to match new data
                        existing_data = existing_data.reshape(1, -1)
                    # Ensure new data matches shape
                    compressed_data = compressed_data.reshape(1, -1)
                    if compressed_data.shape[1] != existing_data.shape[1]:
                        # Pad shorter array if needed
                        max_len = max(compressed_data.shape[1], existing_data.shape[1])
                        if compressed_data.shape[1] < max_len:
                            pad_width = ((0, 0), (0, max_len - compressed_data.shape[1]))
                            compressed_data = np.pad(compressed_data, pad_width)
                        if existing_data.shape[1] < max_len:
                            pad_width = ((0, 0), (0, max_len - existing_data.shape[1]))
                            existing_data = np.pad(existing_data, pad_width)
                    combined_data = np.vstack([existing_data, compressed_data])
                except Exception as e:
                    print(f"Error combining data: {e}")
                    print("Starting fresh data file")
                    combined_data = compressed_data.reshape(1, -1)
            else:
                combined_data = compressed_data.reshape(1, -1)
            
            np.save(self.results_file, combined_data)
            metrics['data_index'] = combined_data.shape[0] - 1
            metrics['data_shape'] = list(compressed_data.shape)
            metrics['data_size'] = len(quantum_data)
        
        # Save metrics
        self.metrics.append(metrics)
        with open(self.metrics_file, 'w') as f:
            json.dump(self.metrics, f, indent=2)
    
    def get_result(self, index: int) -> Optional[Dict[str, Any]]:
        """Retrieve and decompress quantum result."""
        if not 0 <= index < len(self.metrics):
            return None
        
        # Get metrics
        metrics = self.metrics[index].copy()
        
        # Load and decompress data if available
        if 'data_index' in metrics and self.results_file.exists():
            all_data = np.load(self.results_file)
            compressed_data = all_data[metrics['data_index']]
            compressed_data = compressed_data[:metrics['data_size']]  # Remove padding
            decompressed_data = self.decompress_data(compressed_data)
            
            # Convert back to quantum states
            quantum_states = []
            for i in range(0, len(decompressed_data), 3):
                quantum_states.append({
                    'resonance': float(decompressed_data[i]),
                    'coherence': float(decompressed_data[i + 1]),
                    'phase': float(decompressed_data[i + 2])
                })
            
            metrics['quantum_states'] = quantum_states
            del metrics['data_index']
            del metrics['data_shape']
            del metrics['data_size']
        
        return metrics
    
    def get_statistics(self) -> Dict[str, float]:
        """Calculate quantum storage statistics."""
        if not self.metrics:
            return {}
        
        # Calculate key metrics
        resonances = [m['resonance'] for m in self.metrics]
        coherences = [m['coherence'] for m in self.metrics]
        phases = [m['phase'] for m in self.metrics]
        
        # Calculate compression stats
        if self.results_file.exists():
            original_size = sum(m.get('data_size', 0) * 8  # 8 bytes per float
                              for m in self.metrics)
            compressed_size = Path(self.results_file).stat().st_size
            compression_ratio = compressed_size / original_size if original_size > 0 else 1
        else:
            compression_ratio = 1
        
        return {
            'count': len(self.metrics),
            'avg_resonance': np.mean(resonances),
            'avg_coherence': np.mean(coherences),
            'avg_phase': np.mean(phases),
            'compression_ratio': compression_ratio
        }

def test_storage():
    """Test quantum results storage."""
    storage = QuantumResults("quantum_test_data")
    
    # Test data
    test_result = {
        'resonance': 0.9973,
        'coherence': 1.8172,
        'phase': 1.5762,
        'quantum_states': [
            {'resonance': 0.9973, 'coherence': 1.8172, 'phase': 1.5762},
            {'resonance': 0.9973, 'coherence': 1.8172, 'phase': 1.5762}
        ]
    }
    
    print("\nTesting Quantum Storage")
    print("=" * 50)
    
    # Save result
    storage.save_result(test_result)
    print("Saved quantum result")
    
    # Retrieve result
    retrieved = storage.get_result(0)
    print("\nRetrieved Result:")
    print(f"Resonance: {retrieved['resonance']:.4f}")
    print(f"Coherence: {retrieved['coherence']:.4f}")
    print(f"Phase: {retrieved['phase']:.4f}")
    print(f"Quantum States: {len(retrieved['quantum_states'])}")
    
    # Get statistics
    stats = storage.get_statistics()
    print("\nStorage Statistics:")
    print(f"Total Results: {stats['count']}")
    print(f"Average Resonance: {stats['avg_resonance']:.4f}")
    print(f"Average Coherence: {stats['avg_coherence']:.4f}")
    print(f"Compression Ratio: {stats['compression_ratio']:.4f}")
    
    # Validate
    assert abs(retrieved['resonance'] - test_result['resonance']) < 0.01
    assert abs(retrieved['coherence'] - test_result['coherence']) < 0.01
    assert abs(retrieved['phase'] - test_result['phase']) < 0.01
    assert len(retrieved['quantum_states']) == len(test_result['quantum_states'])
    print("\nAll tests passed! ✨")

if __name__ == "__main__":
    test_storage()
