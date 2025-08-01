"""
Centripetal Force Memory System
Implements memory compression through centripetal force dynamics
"""

import numpy as np
import time
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from quantum_phi_scaling import QuantumPhiScaling
from data_weight import DataWeightCalculator

@dataclass
class MemoryNode:
    """Represents a node in the centripetal memory chain"""
    data: any
    next: Optional['MemoryNode'] = None
    position: float = 0.0  # Radial position
    velocity: float = 0.0  # Angular velocity
    mass: float = 1.0     # Data "mass" based on weight
    weight: float = 0.0   # Physical weight equivalent
    complexity: float = 1.0  # Data complexity factor

@dataclass
class MemoryBucket:
    """Represents a bucket in the centripetal memory system"""
    capacity: int
    head: Optional[MemoryNode] = None
    compressed: bool = False
    phi_factor: float = 1.0
    angular_velocity: float = 0.0
    centripetal_force: float = 0.0
    weight_factor: float = 1.0
    complexity_factor: float = 1.0

class CentripetalMemory:
    def __init__(self, initial_buckets: int = 8):
        self.phi = (1 + np.sqrt(5)) / 2
        self.scaler = QuantumPhiScaling()
        self.weight_calc = DataWeightCalculator()
        
        # Centripetal force parameters
        self.gravity_constant = 1.0
        self.force_threshold = 1.0 / self.phi
        self.stability_factor = self.phi
        
        # Initialize buckets with φ-harmonic capacities
        self.num_buckets = initial_buckets
        self.buckets: List[MemoryBucket] = []
        self._initialize_buckets()
        
        # System parameters
        self.total_mass = 0.0
        self.system_radius = 1.0
        self.current_time = 0.0
        
    def _calculate_data_weight(self, data: any) -> Dict:
        """Calculate weight factors for data"""
        # Get weight factors
        factors = self.weight_calc.get_weight_factors(data)
        
        # Calculate effective weight
        effective_weight = factors['digital_weight'] * factors['weight_ratio']
        
        return {
            'weight': effective_weight,
            'complexity': factors['complexity_factor'],
            'mass': effective_weight * factors['complexity_factor']
        }
        
    def _calculate_centripetal_force(self, node: MemoryNode) -> float:
        """Calculate centripetal force on a node with weight-based factors"""
        # Centripetal force: F = m * v² / r
        force = node.mass * (node.velocity ** 2) / (node.position + 1e-10)
        
        # Add gravitational attraction with weight scaling
        force += self.gravity_constant * node.mass / (node.position + 1e-10) * node.weight
        
        # Add weight-based resonance force
        resonance = abs(1 - abs(node.velocity / (self.phi * node.weight)))
        force += node.mass * resonance * node.weight * self.phi
        
        # Add angular momentum with weight consideration
        angular_momentum = node.mass * node.velocity * node.position * node.weight
        force += angular_momentum * node.weight * self.phi
        
        # Add quantum tunneling effect
        tunneling = np.exp(-node.weight * node.position) * self.phi
        force += node.mass * tunneling * self.phi
        
        # Add entropy-based force
        entropy = self._calculate_entropy(node.data)
        force += node.mass * entropy * node.weight * self.phi
        
        # Add quantum resonance force
        resonance = self._calculate_resonance(node.data)
        force += node.mass * resonance * node.weight * self.phi
        
        return force
        
    def _calculate_entropy(self, data: any) -> float:
        """Calculate data entropy as a force factor"""
        if isinstance(data, str):
            # String entropy
            unique_chars = len(set(data))
            entropy = (unique_chars / len(data)) if len(data) > 0 else 0
        elif isinstance(data, (list, dict)):
            # Structured data entropy
            entropy = len(set(str(x) for x in data)) / len(data) if data else 0
        else:
            # Binary entropy
            entropy = 1.0
            
        return entropy * self.phi
        
    def _calculate_resonance(self, data: any) -> float:
        """Calculate quantum resonance as a force factor"""
        if isinstance(data, str):
            # String resonance (based on character frequencies)
            freqs = [data.count(c) for c in set(data)]
            resonance = sum(f * f for f in freqs) / len(data) if len(data) > 0 else 0
        elif isinstance(data, (list, dict)):
            # Structured data resonance (based on value distribution)
            values = [x for x in data if isinstance(x, (int, float))]
            resonance = np.std(values) / len(values) if values else 0
        else:
            # Binary resonance (based on bit patterns)
            bits = bin(data)[2:] if isinstance(data, int) else ''
            resonance = bits.count('1') / len(bits) if bits else 0
            
        return resonance * self.phi
        
    def _update_node_position(self, node: MemoryNode, dt: float):
        """Update node position with weight-based dynamics"""
        if not node:  
            return
            
        # Calculate force
        force = self._calculate_centripetal_force(node)
        
        # Update velocity with weight scaling
        node.velocity += force * dt / node.mass
        
        # Apply damping with weight scaling
        damping = 0.1 * node.weight
        node.velocity *= (1 - damping * dt)
        
        # Update position with weight scaling
        node.position += node.velocity * dt * node.weight
        
        # Apply weight-based damping with resonance
        resonance = abs(1 - abs(node.velocity / (self.phi * node.weight)))
        damping = 1 - (1 / self.phi) * resonance * node.weight
        node.velocity *= damping
        
    def _compress_chain(self, head: MemoryNode) -> Tuple[MemoryNode, float]:
        """Compress chain using weight-based centripetal force dynamics"""
        if not head:
            return head, 0.0
            
        # Calculate total mass and resonance
        total_mass = 0.0
        total_force = 0.0
        max_resonance = 0.0
        
        current = head
        while current:
            # Calculate weight factors
            weight_factors = self._calculate_data_weight(current.data)
            current.weight = weight_factors['weight']
            current.complexity = weight_factors['complexity']
            current.mass = weight_factors['mass']
            
            # Update total mass
            total_mass += current.mass
            
            # Calculate resonance
            resonance = abs(1 - (current.position % self.phi) / self.phi)
            max_resonance = max(max_resonance, resonance)
            
            current = current.next
        
        # Simulate centripetal force dynamics with weight scaling
        dt = 0.1
        steps = int(1 / dt)
        
        current = head
        for _ in range(steps):
            if current:  
                self._update_node_position(current, dt)
                if current.next:
                    self._update_node_position(current.next, dt)
                
                # Calculate compression force with weight scaling
                if current.next:
                    force = self._calculate_centripetal_force(current)
                    total_force += abs(force)
                    
                current = current.next
            else:
                break  
            
        # Calculate compression efficiency with weight scaling
        raw_efficiency = (total_force / (total_mass * self.phi) * max_resonance) if total_mass > 0 else 1.0
        # Normalize efficiency to 0-1 range
        efficiency = min(max(raw_efficiency, 0), 1)
        return head, efficiency
        
    def _initialize_buckets(self):
        """Initialize buckets with φ-harmonic capacities and centripetal force"""
        base_capacity = 1024
        for i in range(self.num_buckets):
            # Capacity follows φ series
            capacity = int(base_capacity * (self.phi ** (i % 3)))
            # Initial angular velocity based on position
            angular_velocity = self.phi ** (i % 3)
            bucket = MemoryBucket(
                capacity=capacity,
                angular_velocity=angular_velocity
            )
            self.buckets.append(bucket)
            
    def _find_optimal_bucket(self, data_size: int) -> Optional[MemoryBucket]:
        """Find optimal bucket based on weight and centripetal force dynamics"""
        best_bucket = None
        best_score = float('inf')
        
        for bucket in self.buckets:
            # Calculate force score
            force_score = abs(bucket.centripetal_force - (data_size * self.phi))
            
            # Calculate capacity score
            used = self._count_nodes(bucket.head)
            remaining = bucket.capacity - used
            
            if remaining >= data_size:
                score = force_score + abs(1 - (used + data_size)/(bucket.capacity * self.phi))
                if score < best_score:
                    best_score = score
                    best_bucket = bucket
                    
        return best_bucket
        
    def _count_nodes(self, head: Optional[MemoryNode]) -> int:
        """Count the number of nodes in a linked list"""
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count

    def store(self, key: str, data: any) -> Dict:
        """Store data in the centripetal memory system with weight-based compression
        
        Args:
            key: The key to store the data under
            data: The data to store
            
        Returns:
            Dict containing success status and storage details
        """
        if data is None:
            return {'success': False, 'error': 'Empty data'}
            
        # Find optimal bucket based on weight and centripetal force
        bucket = self._find_optimal_bucket(len(data))
        if not bucket:
            # Create new bucket with increased capacity
            new_capacity = max(len(data), int(self.buckets[-1].capacity * self.phi))
            new_bucket = MemoryBucket(
                capacity=new_capacity,
                angular_velocity=self.phi * self.buckets[-1].angular_velocity
            )
            self.buckets.append(new_bucket)
            bucket = new_bucket
            
        # Create node chain with weight factors
        prev_node = None
        head = None
        for item in data:
            node = MemoryNode(data=item)
            if not head:
                head = node
            if prev_node:
                prev_node.next = node
            prev_node = node
            
        # Compress chain using weight-based centripetal force
        compressed_head, efficiency = self._compress_chain(head)
        bucket.head = compressed_head
        bucket.compressed = True
        bucket.phi_factor = efficiency
        
        # Calculate bucket weight factors
        bucket.weight_factor = self._calculate_data_weight(data)['weight']
        bucket.complexity_factor = self._calculate_data_weight(data)['complexity']
        
        return {
            'success': True,
            'bucket_index': self.buckets.index(bucket),
            'compression_ratio': efficiency,
            'angular_velocity': bucket.angular_velocity,
            'centripetal_force': bucket.centripetal_force,
            'weight_factor': bucket.weight_factor,
            'complexity_factor': bucket.complexity_factor
        }
        
    def get_stats(self) -> Dict:
        """Get current memory system statistics"""
        total_capacity = sum(b.capacity for b in self.buckets)
        total_used = sum(self._count_nodes(b.head) for b in self.buckets)
        compressed_buckets = sum(1 for b in self.buckets if b.compressed)
        
        # Calculate φ-harmonic efficiency
        efficiencies = []
        for bucket in self.buckets:
            if bucket.compressed:
                efficiencies.append(bucket.phi_factor)
                
        return {
            'total_capacity': total_capacity,
            'total_used': total_used,
            'utilization': total_used / total_capacity if total_capacity > 0 else 0,
            'num_buckets': len(self.buckets),
            'compressed_buckets': compressed_buckets,
            'total_mass': self.total_mass,
            'system_radius': self.system_radius,
            'phi_efficiency': np.mean(efficiencies) if efficiencies else 0
        }
        
    def retrieve(self, key: str) -> Dict:
        """Retrieve data from the centripetal memory system using phi-harmonic search
        
        Args:
            key: The key to search for in the memory system
            
        Returns:
            Dict containing success status and retrieved data
        """
        # Implement phi-harmonic search across buckets
        for bucket_idx, bucket in enumerate(self.buckets):
            current = bucket.head
            while current:
                # Check if this node contains the key
                if hasattr(current.data, 'get') and current.data.get('key') == key:
                    # Found the key in a dictionary
                    return {
                        'success': True,
                        'data': current.data.get('value'),
                        'bucket_idx': bucket_idx,
                        'phi_factor': bucket.phi_factor,
                        'weight_factor': current.weight
                    }
                elif isinstance(current.data, tuple) and len(current.data) >= 2 and current.data[0] == key:
                    # Found the key in a tuple (key, value)
                    return {
                        'success': True,
                        'data': current.data[1],
                        'bucket_idx': bucket_idx,
                        'phi_factor': bucket.phi_factor,
                        'weight_factor': current.weight
                    }
                elif str(current.data) == key or (hasattr(current.data, '__str__') and str(current.data) == key):
                    # Direct string match
                    return {
                        'success': True,
                        'data': current.data,
                        'bucket_idx': bucket_idx,
                        'phi_factor': bucket.phi_factor,
                        'weight_factor': current.weight
                    }
                
                current = current.next
        
        # Key not found
        return {
            'success': False,
            'error': f"Key '{key}' not found in centripetal memory",
            'phi_factor': self.phi
        }

def run_centripetal_test():
    """Test the Centripetal Memory system"""
    print("\nCentripetal Memory Test")
    print("======================")
    
    # Initialize system
    memory = CentripetalMemory(initial_buckets=8)
    
    # Test data sizes following φ series
    base_size = 64
    sizes = [int(base_size * memory.phi**i) for i in range(5)]
    
    print("\nInitial State:")
    stats = memory.get_stats()
    print(f"Buckets: {stats['num_buckets']}")
    print(f"Capacity: {stats['total_capacity']}")
    print(f"System Radius: {stats['system_radius']:.3f}")
    
    print("\nRunning Tests...")
    for i, size in enumerate(sizes, 1):
        print(f"\nTest {i}: Adding {size} items")
        
        # Generate test data with φ-harmonic patterns
        data = [float(j) * memory.phi for j in range(size)]
        
        # Time the operation
        start_time = time.time()
        result = memory.store(data)
        duration = time.time() - start_time
        
        # Get updated stats
        stats = memory.get_stats()
        
        print(f"\nOperation completed in {duration:.3f} seconds")
        print(f"Storage Location: Bucket {result['bucket_index']}")
        print(f"Compression Ratio: {result['compression_ratio']:.3f}")
        print(f"Memory State:")
        print(f"  Utilization: {stats['utilization']*100:.1f}%")
        print(f"  Angular Velocity: {result['angular_velocity']:.3f} rad/s")
        print(f"  Centripetal Force: {result['centripetal_force']:.3f}")
        print(f"  φ-Efficiency: {stats['phi_efficiency']:.3f}")
        print(f"  Weight Factor: {result['weight_factor']:.3f}")
        print(f"  Complexity Factor: {result['complexity_factor']:.3f}")
        
        # Small delay to observe dynamics
        time.sleep(0.5)
        
    # Final stats
    final_stats = memory.get_stats()
    print("\nFinal System State:")
    print(f"Total Buckets: {final_stats['num_buckets']}")
    print(f"Total Capacity: {final_stats['total_capacity']}")
    print(f"Utilization: {final_stats['utilization']*100:.1f}%")
    print(f"Compressed Buckets: {final_stats['compressed_buckets']}")
    print(f"Final System Radius: {final_stats['system_radius']:.3f}")
    print(f"Final φ-Efficiency: {final_stats['phi_efficiency']:.3f}")

if __name__ == "__main__":
    run_centripetal_test()
