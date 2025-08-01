"""
Centripetal Force Memory System Adapter
======================================
Implements memory compression through centripetal force dynamics
without external dependencies.
"""

import numpy as np
import time
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass

# Import adapters instead of originals
from quantum_phi_scaling_adapter import get_quantum_phi_scaling
from data_weight_adapter import get_data_weight_calculator

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI          # Inverse golden ratio

@dataclass
class MemoryNode:
    """Represents a node in the centripetal memory chain"""
    data: Any
    next: Optional['MemoryNode'] = None
    position: float = 0.0  # Radial position
    velocity: float = 0.0  # Angular velocity
    mass: float = 1.0     # Data "mass" based on weight
    weight: float = 0.0   # Physical weight equivalent


class MemoryBucket:
    """A bucket in the centripetal memory system"""
    def __init__(self, bucket_id: int):
        self.bucket_id = bucket_id
        self.head = None
        self.tail = None
        self.size = 0
        self.radius = PHI * (bucket_id + 1)  # φ-harmonic radius
        self.angular_velocity = PHI_INV / self.radius  # φ-harmonic velocity
        
        # φ-harmonic parameters
        self.centripetal_force = PHI / (self.radius**2)
        self.compression_ratio = 1 - PHI_INV * (bucket_id / 10)
        
    def add_node(self, data: Any, weight: float = 1.0) -> MemoryNode:
        """Add a node to the bucket"""
        # Create new node
        node = MemoryNode(
            data=data,
            position=self.radius,
            velocity=self.angular_velocity,
            mass=weight,
            weight=weight
        )
        
        # Add to linked list
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size += 1
        return node
    
    def compress(self) -> float:
        """Compress the bucket using centripetal force"""
        if self.size == 0:
            return 0.0
        
        # Apply centripetal force to all nodes
        compression = 0.0
        current = self.head
        
        while current:
            # Calculate centripetal force
            force = self.centripetal_force * current.mass
            
            # Apply force to node
            current.velocity += force * PHI_INV
            current.position -= current.velocity * PHI_INV
            
            # Calculate compression
            compression += (self.radius - current.position) / self.radius
            
            current = current.next
        
        # Average compression
        return compression / self.size
    
    def get_data(self) -> List[Any]:
        """Get all data in the bucket"""
        data = []
        current = self.head
        
        while current:
            data.append(current.data)
            current = current.next
        
        return data


class CentripetalMemoryAdapter:
    """Centripetal memory system using φ-harmonic dynamics"""
    
    def __init__(self, initial_buckets: int = 4):
        """
        Initialize the centripetal memory system
        
        Args:
            initial_buckets: Initial number of buckets
        """
        self.buckets = [MemoryBucket(i) for i in range(initial_buckets)]
        self.bucket_count = initial_buckets
        self.phi = PHI
        self.total_nodes = 0
        self.total_weight = 0.0
        self.compression_ratio = 0.0
        
        # Initialize quantum scaling and data weight using adapters
        try:
            self.quantum_scaling = get_quantum_phi_scaling()
            self.data_weight = get_data_weight_calculator()
        except Exception:
            self.quantum_scaling = None
            self.data_weight = None
    
    def add_memory(self, data: Any, weight: float = None, bucket_id: int = None) -> Dict:
        """
        Add a memory to the system
        
        Args:
            data: Data to store
            weight: Weight of the data (calculated if None)
            bucket_id: Specific bucket to store in (auto-selected if None)
            
        Returns:
            Dictionary with memory metrics
        """
        # Calculate weight if not provided
        if weight is None:
            if self.data_weight:
                weight = self.data_weight.calculate_weight(data)
            else:
                # Default weight calculation
                if isinstance(data, dict):
                    weight = len(str(data)) * PHI_INV
                elif isinstance(data, (list, tuple)):
                    weight = len(data) * PHI_INV
                else:
                    weight = 1.0
        
        # Select bucket if not provided
        if bucket_id is None:
            # Use φ-harmonic distribution
            if self.quantum_scaling:
                # Use quantum scaling to determine optimal bucket
                metrics = self.quantum_scaling.calculate_phi_metrics(weight)
                bucket_id = int(metrics['phi_ratio'] * self.bucket_count) % self.bucket_count
            else:
                # Simple distribution based on weight
                bucket_id = int(weight * PHI) % self.bucket_count
        
        # Ensure valid bucket_id
        bucket_id = max(0, min(bucket_id, self.bucket_count - 1))
        
        # Add to bucket
        node = self.buckets[bucket_id].add_node(data, weight)
        
        # Update metrics
        self.total_nodes += 1
        self.total_weight += weight
        
        # Compress bucket
        compression = self.buckets[bucket_id].compress()
        
        # Update overall compression ratio
        self.compression_ratio = (self.compression_ratio * (self.total_nodes - 1) + compression) / self.total_nodes
        
        return {
            'bucket_id': bucket_id,
            'weight': weight,
            'compression': compression,
            'total_nodes': self.total_nodes,
            'total_weight': self.total_weight,
            'overall_compression': self.compression_ratio
        }
    
    def get_memories(self, bucket_id: Optional[int] = None) -> List[Any]:
        """
        Get memories from the system
        
        Args:
            bucket_id: Specific bucket to retrieve from (all if None)
            
        Returns:
            List of memories
        """
        if bucket_id is not None:
            # Ensure valid bucket_id
            bucket_id = max(0, min(bucket_id, self.bucket_count - 1))
            return self.buckets[bucket_id].get_data()
        else:
            # Get all memories
            memories = []
            for bucket in self.buckets:
                memories.extend(bucket.get_data())
            return memories
    
    def compress_all(self) -> Dict:
        """
        Compress all buckets
        
        Returns:
            Dictionary with compression metrics
        """
        total_compression = 0.0
        
        for bucket in self.buckets:
            compression = bucket.compress()
            total_compression += compression
        
        # Update overall compression ratio
        if self.bucket_count > 0:
            self.compression_ratio = total_compression / self.bucket_count
        
        return {
            'total_nodes': self.total_nodes,
            'total_weight': self.total_weight,
            'overall_compression': self.compression_ratio,
            'bucket_count': self.bucket_count
        }
    
    def add_bucket(self) -> int:
        """
        Add a new bucket to the system
        
        Returns:
            ID of the new bucket
        """
        new_id = self.bucket_count
        self.buckets.append(MemoryBucket(new_id))
        self.bucket_count += 1
        return new_id
    
    def get_metrics(self) -> Dict:
        """
        Get metrics for the memory system
        
        Returns:
            Dictionary with system metrics
        """
        bucket_sizes = [bucket.size for bucket in self.buckets]
        
        # Calculate φ-harmonic metrics if available
        if self.quantum_scaling:
            phi_metrics = self.quantum_scaling.calculate_phi_metrics(self.compression_ratio)
        else:
            # Simple φ metrics
            phi_ratio = abs(1 - self.compression_ratio/PHI)
            phi_metrics = {
                'phi_ratio': phi_ratio,
                'resonance': 1 - phi_ratio,
                'efficiency': (1 - phi_ratio) * PHI
            }
        
        return {
            'total_nodes': self.total_nodes,
            'total_weight': self.total_weight,
            'bucket_count': self.bucket_count,
            'bucket_sizes': bucket_sizes,
            'overall_compression': self.compression_ratio,
            'phi_metrics': phi_metrics
        }


# Create singleton instance for compatibility with original
centripetal_memory = CentripetalMemoryAdapter()


def get_centripetal_memory():
    """Get the CentripetalMemoryAdapter instance"""
    return centripetal_memory
