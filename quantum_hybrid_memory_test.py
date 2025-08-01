"""
Quantum Hybrid Memory System - Simplified Test Version
Tests the hybrid memory concept without external dependencies
"""

import numpy as np
import time
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass

# Mock implementations of the memory systems for testing

@dataclass
class MemoryNode:
    """Represents a node in memory chain"""
    data: any
    next: Optional['MemoryNode'] = None
    position: float = 0.0
    weight: float = 1.0
    complexity: float = 1.0

@dataclass
class MemoryBucket:
    """Represents a bucket in memory system"""
    capacity: int
    head: Optional[MemoryNode] = None
    compressed: bool = False
    phi_factor: float = 1.0

class MockFerrisMemory:
    """Mock implementation of Quantum Ferris Memory for testing"""
    def __init__(self, initial_buckets=8):
        self.phi = (1 + np.sqrt(5)) / 2
        self.buckets = []
        self.data_store = {}  # Simple key-value store for testing
        self.num_buckets = initial_buckets
        
        # Initialize buckets
        for i in range(initial_buckets):
            capacity = int(1024 * (self.phi ** (i % 3)))
            self.buckets.append(MemoryBucket(capacity=capacity))
    
    def store(self, key, data):
        """Store data with key"""
        self.data_store[key] = data
        # Simulate compression with phi-based ratio
        compression_ratio = 0.8 + (0.2 * np.sin(hash(str(data)) % 10 / 10 * np.pi))
        return {
            "success": True,
            "compression_ratio": compression_ratio
        }
    
    def retrieve(self, key):
        """Retrieve data by key"""
        if key in self.data_store:
            return {
                "success": True,
                "data": self.data_store[key]
            }
        return {"success": False}
    
    def remove(self, key):
        """Remove data by key"""
        if key in self.data_store:
            del self.data_store[key]
            return {"success": True}
        return {"success": False}
    
    def get_stats(self):
        """Get memory statistics"""
        return {
            "total_capacity": sum(b.capacity for b in self.buckets),
            "total_used": len(self.data_store),
            "num_buckets": len(self.buckets),
            "phi_efficiency": 0.85
        }

class MockCentripetalMemory:
    """Mock implementation of Centripetal Memory for testing"""
    def __init__(self, initial_buckets=8):
        self.phi = (1 + np.sqrt(5)) / 2
        self.buckets = []
        self.data_store = {}  # Simple key-value store for testing
        self.data_keys = {}   # Reverse mapping for retrieval
        self.key_mapping = {} # Maps external keys to internal keys
        self.num_buckets = initial_buckets
        
        # Initialize buckets
        for i in range(initial_buckets):
            capacity = int(1024 * (self.phi ** (i % 3)))
            self.buckets.append(MemoryBucket(capacity=capacity))
    
    def _calculate_data_weight(self, data):
        """Calculate weight factors for data"""
        # Simple mock implementation
        if isinstance(data, str):
            complexity = len(set(data)) / max(len(data), 1)
        elif isinstance(data, (list, tuple)):
            complexity = len(set(str(x) for x in data)) / max(len(data), 1)
        else:
            complexity = 1.0
            
        return {
            "weight": len(str(data)) / 1000,
            "complexity": complexity,
            "mass": complexity * len(str(data)) / 1000
        }
    
    def store(self, external_key, data):
        """Store data with external key and return storage details"""
        # Generate a unique internal key
        internal_key = f"cent_{len(self.data_store)}"
        self.data_store[internal_key] = data
        self.data_keys[str(data)[:100]] = internal_key  # Use prefix as identifier
        self.key_mapping[external_key] = internal_key  # Map external key to internal key
        
        # Simulate compression with phi-based ratio
        weight = self._calculate_data_weight(data)
        compression_ratio = 0.7 + (0.3 * weight["complexity"])
        
        return {
            "success": True,
            "compression_ratio": compression_ratio,
            "internal_key": internal_key,
            "bucket_index": len(self.data_store) % len(self.buckets)
        }
    
    def retrieve(self, key):
        """Retrieve data by key (can be external or internal key)"""
        # Check if this is an external key that we have mapped
        if key in self.key_mapping:
            internal_key = self.key_mapping[key]
            if internal_key in self.data_store:
                return {
                    "success": True,
                    "data": self.data_store[internal_key]
                }
        
        # Otherwise try as internal key
        if key in self.data_store:
            return {
                "success": True,
                "data": self.data_store[key]
            }
            
        return {"success": False}
    
    def remove(self, key):
        """Remove data by key (can be external or internal key)"""
        internal_key = key
        
        # Check if this is an external key that we have mapped
        if key in self.key_mapping:
            internal_key = self.key_mapping[key]
            del self.key_mapping[key]
            
        if internal_key in self.data_store:
            data_prefix = str(self.data_store[internal_key])[:100]
            if data_prefix in self.data_keys:
                del self.data_keys[data_prefix]
            del self.data_store[internal_key]
            return {"success": True}
            
        return {"success": False}
    
    def get_stats(self):
        """Get memory statistics"""
        return {
            "total_capacity": sum(b.capacity for b in self.buckets),
            "total_used": len(self.data_store),
            "num_buckets": len(self.buckets),
            "phi_efficiency": 0.78
        }

class QuantumHybridMemory:
    """
    Hybrid memory system that combines Quantum Ferris Memory and Centripetal Force Memory
    for optimal storage based on data characteristics.
    """
    def __init__(self, ferris_buckets=8, centripetal_buckets=8):
        """
        Initialize the hybrid memory system with both memory subsystems.
        
        Args:
            ferris_buckets: Number of buckets for Quantum Ferris Memory
            centripetal_buckets: Number of buckets for Centripetal Memory
        """
        # Initialize both memory systems
        self.ferris_memory = MockFerrisMemory(initial_buckets=ferris_buckets)
        self.centripetal_memory = MockCentripetalMemory(initial_buckets=centripetal_buckets)
        
        # Hybrid parameters
        self.phi = (1 + np.sqrt(5)) / 2
        self.hybrid_mode = "auto"  # "auto", "ferris", "centripetal"
        self.last_access_times = {}
        self.storage_locations = {}  # Maps keys to memory type
        self.access_counts = {}      # Tracks access frequency
        
        # Performance metrics
        self.metrics = {
            "ferris_stores": 0,
            "centripetal_stores": 0,
            "ferris_retrievals": 0,
            "centripetal_retrievals": 0,
            "store_times": [],
            "retrieve_times": [],
            "compression_ratios": []
        }
        
    def _calculate_data_characteristics(self, data: Any) -> Dict:
        """
        Calculate data characteristics to determine optimal storage method.
        
        Args:
            data: Data to analyze
            
        Returns:
            Dict with data characteristics
        """
        # Get basic metrics
        data_size = len(data) if hasattr(data, "__len__") else 1
        
        # Calculate complexity
        if hasattr(self.centripetal_memory, "_calculate_data_weight"):
            weight_factors = self.centripetal_memory._calculate_data_weight(data)
            complexity = weight_factors.get('complexity', 1.0)
            weight = weight_factors.get('weight', 1.0)
        else:
            # Fallback complexity calculation
            if isinstance(data, str):
                complexity = len(set(data)) / max(len(data), 1)
            elif isinstance(data, (list, tuple)):
                complexity = len(set(str(x) for x in data)) / max(len(data), 1)
            else:
                complexity = 1.0
            weight = data_size / 1024  # Simple weight estimate
            
        # Calculate time sensitivity (based on access history)
        access_count = self.access_counts.get(str(data)[:100], 0)  # Use prefix as identifier
        time_sensitivity = min(access_count / 10, 1.0)  # Normalize to 0-1
        
        return {
            "size": data_size,
            "complexity": complexity,
            "weight": weight,
            "time_sensitivity": time_sensitivity
        }
        
    def _select_optimal_memory(self, data: Any) -> str:
        """
        Select the optimal memory system based on data characteristics.
        
        Args:
            data: Data to store
            
        Returns:
            String indicating which memory to use ("ferris" or "centripetal")
        """
        if self.hybrid_mode != "auto":
            return self.hybrid_mode
            
        # Calculate data characteristics
        characteristics = self._calculate_data_characteristics(data)
        
        # Decision logic:
        # - High complexity, high weight data → Centripetal Memory
        # - Time-sensitive, frequently accessed data → Ferris Memory
        
        # Calculate scores for each memory system
        ferris_score = characteristics["time_sensitivity"] * self.phi
        centripetal_score = characteristics["complexity"] * characteristics["weight"]
        
        # Select memory with higher score
        return "ferris" if ferris_score >= centripetal_score else "centripetal"
        
    def store(self, key: str, data: Any) -> Dict:
        """
        Store data using the optimal memory system based on data characteristics.
        
        Args:
            key: Unique identifier for the data
            data: Data to store
            
        Returns:
            Dict with storage result information
        """
        start_time = time.time()
        
        # Select optimal memory system
        memory_type = self._select_optimal_memory(data)
        
        # Store in selected memory system
        if memory_type == "ferris":
            # Adapt to Ferris Memory interface
            result = self.ferris_memory.store(key, data)
            self.metrics["ferris_stores"] += 1
            # Record storage location for ferris memory
            self.storage_locations[key] = {"type": "ferris"}
        else:  # centripetal
            # Adapt to Centripetal Memory interface - pass the external key
            result = self.centripetal_memory.store(key, data)
            # Map the centripetal key to our key
            if result.get("success", False):
                self.storage_locations[key] = {
                    "type": "centripetal",
                    "internal_key": result.get("internal_key")
                }
            self.metrics["centripetal_stores"] += 1
        
        # Record access time and update access count
        self.last_access_times[key] = time.time()
        self.access_counts[key] = self.access_counts.get(key, 0) + 1
        
        # Track metrics
        duration = time.time() - start_time
        self.metrics["store_times"].append(duration)
        
        if "compression_ratio" in result:
            self.metrics["compression_ratios"].append(result["compression_ratio"])
        
        return {
            "success": result.get("success", True),
            "memory_type": memory_type,
            "compression_ratio": result.get("compression_ratio", 1.0),
            "key": key,
            "duration": duration
        }
        
    def retrieve(self, key: str) -> Dict:
        """
        Retrieve data from the appropriate memory system.
        
        Args:
            key: Unique identifier for the data
            
        Returns:
            Dict with retrieved data and metadata
        """
        start_time = time.time()
        
        # Check if we know where this key is stored
        if key in self.storage_locations:
            storage_info = self.storage_locations[key]
            memory_type = storage_info["type"]
            
            if memory_type == "ferris":
                result = self.ferris_memory.retrieve(key)
                self.metrics["ferris_retrievals"] += 1
            else:  # centripetal
                # Try to retrieve using the external key directly
                result = self.centripetal_memory.retrieve(key)
                self.metrics["centripetal_retrievals"] += 1
                
            if result.get("success", False):
                # Update access time and count
                self.last_access_times[key] = time.time()
                self.access_counts[key] = self.access_counts.get(key, 0) + 1
                
                # Track metrics
                duration = time.time() - start_time
                self.metrics["retrieve_times"].append(duration)
                
                result["duration"] = duration
                return result
        
        # If we don't know or failed, try both memory systems
        
        # Try ferris memory first
        ferris_result = self.ferris_memory.retrieve(key)
        if ferris_result.get("success", False):
            self.storage_locations[key] = {"type": "ferris"}
            self.last_access_times[key] = time.time()
            self.access_counts[key] = self.access_counts.get(key, 0) + 1
            self.metrics["ferris_retrievals"] += 1
            
            # Track metrics
            duration = time.time() - start_time
            self.metrics["retrieve_times"].append(duration)
            
            ferris_result["duration"] = duration
            return ferris_result
            
        # Try centripetal memory directly with the key
        centripetal_result = self.centripetal_memory.retrieve(key)
        if centripetal_result.get("success", False):
            self.storage_locations[key] = {"type": "centripetal"}
            self.last_access_times[key] = time.time()
            self.access_counts[key] = self.access_counts.get(key, 0) + 1
            self.metrics["centripetal_retrievals"] += 1
            
            # Track metrics
            duration = time.time() - start_time
            self.metrics["retrieve_times"].append(duration)
            
            centripetal_result["duration"] = duration
            return centripetal_result
            
        # Not found in either system
        return {
            "success": False, 
            "error": "Key not found",
            "duration": time.time() - start_time
        }
        
    def remove(self, key: str) -> Dict:
        """
        Remove data from the memory system.
        
        Args:
            key: Unique identifier for the data
            
        Returns:
            Dict with removal result
        """
        # Check if we know where this key is stored
        if key in self.storage_locations:
            storage_info = self.storage_locations[key]
            memory_type = storage_info["type"]
            
            if memory_type == "ferris":
                result = self.ferris_memory.remove(key)
            else:  # centripetal
                # Try to remove using the external key directly
                result = self.centripetal_memory.remove(key)
                
            # Clean up tracking data
            if key in self.storage_locations:
                del self.storage_locations[key]
            if key in self.last_access_times:
                del self.last_access_times[key]
                
            return result
            
        # If we don't know, try both
        ferris_result = self.ferris_memory.remove(key)
        centripetal_result = self.centripetal_memory.remove(key)
        
        # Return success if either succeeded
        return {
            "success": ferris_result.get("success", False) or centripetal_result.get("success", False)
        }
        
    def get_stats(self) -> Dict:
        """
        Get combined memory statistics.
        
        Returns:
            Dict with memory statistics
        """
        # Get stats from both memory systems
        ferris_stats = self.ferris_memory.get_stats()
        centripetal_stats = self.centripetal_memory.get_stats()
        
        # Calculate average metrics
        avg_store_time = sum(self.metrics["store_times"]) / max(len(self.metrics["store_times"]), 1)
        avg_retrieve_time = sum(self.metrics["retrieve_times"]) / max(len(self.metrics["retrieve_times"]), 1)
        avg_compression = sum(self.metrics["compression_ratios"]) / max(len(self.metrics["compression_ratios"]), 1)
        
        # Calculate storage distribution
        total_stores = self.metrics["ferris_stores"] + self.metrics["centripetal_stores"]
        ferris_ratio = self.metrics["ferris_stores"] / max(total_stores, 1)
        centripetal_ratio = self.metrics["centripetal_stores"] / max(total_stores, 1)
        
        return {
            "ferris": ferris_stats,
            "centripetal": centripetal_stats,
            "total_capacity": ferris_stats.get("total_capacity", 0) + centripetal_stats.get("total_capacity", 0),
            "total_used": ferris_stats.get("total_used", 0) + centripetal_stats.get("total_used", 0),
            "utilization": (ferris_stats.get("total_used", 0) + centripetal_stats.get("total_used", 0)) / 
                          (ferris_stats.get("total_capacity", 1) + centripetal_stats.get("total_capacity", 1)),
            "active_keys": len(self.storage_locations),
            "ferris_ratio": ferris_ratio,
            "centripetal_ratio": centripetal_ratio,
            "avg_store_time": avg_store_time,
            "avg_retrieve_time": avg_retrieve_time,
            "avg_compression_ratio": avg_compression,
            "phi_efficiency": (ferris_stats.get("phi_efficiency", 0) + centripetal_stats.get("phi_efficiency", 0)) / 2
        }
        
    def optimize(self) -> Dict:
        """
        Optimize memory allocation based on access patterns.
        
        Returns:
            Dict with optimization results
        """
        current_time = time.time()
        moved_count = 0
        
        # Identify stale data (not accessed recently)
        stale_threshold = current_time - (60 * 60)  # 1 hour
        stale_keys = [k for k, t in self.last_access_times.items() if t < stale_threshold]
        
        # In this simplified version, we'll just count the keys that would be moved
        for key in stale_keys:
            # Check current location
            if key not in self.storage_locations:
                continue
                
            storage_info = self.storage_locations[key]
            current_memory = storage_info["type"]
            
            # Calculate optimal memory based on access patterns
            access_count = self.access_counts.get(key, 0)
            
            if current_memory == "ferris" and access_count < 3:
                # Would move from ferris to centripetal if rarely accessed
                moved_count += 1
                    
            elif current_memory == "centripetal" and access_count > 10:
                # Would move from centripetal to ferris if frequently accessed
                moved_count += 1
                    
        return {
            "stale_keys": len(stale_keys),
            "moved_count": moved_count
        }
        
    def set_mode(self, mode: str) -> None:
        """
        Set the hybrid mode.
        
        Args:
            mode: One of "auto", "ferris", or "centripetal"
        """
        if mode in ["auto", "ferris", "centripetal"]:
            self.hybrid_mode = mode
        else:
            raise ValueError("Mode must be one of: auto, ferris, centripetal")


def run_hybrid_memory_test():
    """Test the Quantum Hybrid Memory system"""
    print("\nQuantum Hybrid Memory Test (Simplified)")
    print("===================================")
    
    # Initialize system
    memory = QuantumHybridMemory(ferris_buckets=8, centripetal_buckets=8)
    
    # Test data with different characteristics
    test_cases = [
        {"name": "Simple Array", "data": [i for i in range(100)]},
        {"name": "Complex Nested", "data": [[i*j for j in range(10)] for i in range(20)]},
        {"name": "Text Data", "data": "This is a test of the quantum hybrid memory system with phi-harmonic resonance"},
        {"name": "Mixed Data", "data": [{"id": i, "value": i*i} for i in range(50)]},
        {"name": "Phi Series", "data": [(1 + np.sqrt(5))/2 ** i for i in range(30)]}
    ]
    
    print("\nInitial State:")
    stats = memory.get_stats()
    print(f"Total Capacity: {stats['total_capacity']}")
    print(f"Memory Systems: Ferris ({stats['ferris'].get('num_buckets', 0)} buckets), "
          f"Centripetal ({stats['centripetal'].get('num_buckets', 0)} buckets)")
    
    print("\nRunning Tests...")
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test['name']} ({len(test['data'])} items)")
        
        # Store data
        key = f"test_{i}"
        start_time = time.time()
        store_result = memory.store(key, test["data"])
        store_duration = time.time() - start_time
        
        # Retrieve data
        start_time = time.time()
        retrieve_result = memory.retrieve(key)
        retrieve_duration = time.time() - start_time
        
        # Print results
        print(f"Storage System: {store_result['memory_type'].capitalize()}")
        print(f"Compression Ratio: {store_result['compression_ratio']:.3f}")
        print(f"Store Time: {store_duration:.6f}s, Retrieve Time: {retrieve_duration:.6f}s")
        print(f"Success: {retrieve_result['success']}")
        
        # Access multiple times to affect future optimization
        for _ in range(i * 3):  # More accesses for later items
            memory.retrieve(key)
            
    # Test different modes
    print("\nTesting Memory Modes...")
    
    # Auto mode (default)
    print("\nAuto Mode:")
    memory.set_mode("auto")
    auto_result = memory.store("auto_test", "Auto mode test data")
    print(f"Selected Memory: {auto_result['memory_type'].capitalize()}")
    
    # Force Ferris mode
    print("\nFerris Mode:")
    memory.set_mode("ferris")
    ferris_result = memory.store("ferris_test", "Ferris mode test data")
    print(f"Selected Memory: {ferris_result['memory_type'].capitalize()}")
    
    # Force Centripetal mode
    print("\nCentripetal Mode:")
    memory.set_mode("centripetal")
    centripetal_result = memory.store("centripetal_test", "Centripetal mode test data")
    print(f"Selected Memory: {centripetal_result['memory_type'].capitalize()}")
    
    # Reset to auto mode
    memory.set_mode("auto")
    
    # Optimize memory
    print("\nOptimizing Memory...")
    optimize_result = memory.optimize()
    print(f"Stale Keys: {optimize_result['stale_keys']}")
    print(f"Moved Items: {optimize_result['moved_count']}")
    
    # Final stats
    final_stats = memory.get_stats()
    print("\nFinal System State:")
    print(f"Total Capacity: {final_stats['total_capacity']}")
    print(f"Total Used: {final_stats['total_used']}")
    print(f"Utilization: {final_stats['utilization']*100:.1f}%")
    print(f"Active Keys: {final_stats['active_keys']}")
    print(f"Storage Distribution: {final_stats['ferris_ratio']*100:.1f}% Ferris, "
          f"{final_stats['centripetal_ratio']*100:.1f}% Centripetal")
    print(f"Average Compression: {final_stats['avg_compression_ratio']:.3f}")
    print(f"Average Store Time: {final_stats['avg_store_time']*1000:.3f}ms")
    print(f"Average Retrieve Time: {final_stats['avg_retrieve_time']*1000:.3f}ms")
    print(f"Phi-Efficiency: {final_stats['phi_efficiency']:.3f}")


if __name__ == "__main__":
    run_hybrid_memory_test()
