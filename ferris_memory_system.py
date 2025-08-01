"""
FERRIS MEMORY SYSTEM
===================
Implementation of the Quantum Ferris Memory System for the phi-harmonic network.
This system provides advanced memory management through quantum-based circular
memory structures that optimize data storage and retrieval.
"""

import os
import time
import math
import json
import pickle
import random
import hashlib
import threading
import numpy as np
from typing import Dict, List, Tuple, Any, Optional, Union
from datetime import datetime

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI            # Inverse golden ratio


class MemoryCell:
    """
    Quantum memory cell that stores data with phi-harmonic properties
    """
    
    def __init__(self, cell_id: str = None):
        """
        Initialize a memory cell
        
        Args:
            cell_id: Unique identifier for the cell
        """
        self.cell_id = cell_id or self._generate_cell_id()
        self.data = None
        self.quantum_state = self._initialize_quantum_state()
        self.creation_time = time.time()
        self.last_access_time = self.creation_time
        self.access_count = 0
        self.phi_resonance = 0.0
        self.entangled_cells = []
    
    def _generate_cell_id(self) -> str:
        """Generate a unique cell ID"""
        timestamp = int(time.time() * 1000)
        random_part = random.randint(0, 999999)
        return f"cell_{timestamp}_{random_part}"
    
    def _initialize_quantum_state(self) -> Dict:
        """Initialize the quantum state of the cell"""
        return {
            'superposition': random.random(),
            'entanglement': 0.0,
            'coherence': 1.0,
            'phi_phase': random.random() * 2 * math.pi
        }
    
    def store(self, data: Any) -> None:
        """
        Store data in the memory cell
        
        Args:
            data: Data to store
        """
        self.data = data
        self.last_access_time = time.time()
        self.access_count += 1
        
        # Update quantum state
        self.quantum_state['superposition'] = random.random()
        self.quantum_state['coherence'] = 1.0
        
        # Calculate phi resonance of the data
        self.phi_resonance = self._calculate_phi_resonance(data)
    
    def retrieve(self) -> Any:
        """
        Retrieve data from the memory cell
        
        Returns:
            Stored data
        """
        self.last_access_time = time.time()
        self.access_count += 1
        
        # Update quantum state (reading affects the state)
        self.quantum_state['coherence'] *= 0.99
        
        return self.data
    
    def _calculate_phi_resonance(self, data: Any) -> float:
        """
        Calculate phi-harmonic resonance of the data
        
        Args:
            data: Data to calculate resonance for
            
        Returns:
            Phi resonance value (0-1)
        """
        # Convert data to a numeric representation
        if isinstance(data, (int, float)):
            value = float(data)
        elif isinstance(data, str):
            # Use hash of string
            value = sum(ord(c) for c in data) / 1000.0
        elif isinstance(data, (list, tuple)):
            # Average of elements if numeric, otherwise hash
            if all(isinstance(x, (int, float)) for x in data):
                value = sum(data) / len(data) if data else 0.0
            else:
                value = sum(hash(str(x)) for x in data) / 1000.0
        else:
            # Use hash of string representation
            value = hash(str(data)) / 1000.0
        
        # Normalize value to 0-10 range
        normalized = abs(value) % 10
        
        # Calculate distance to phi or phi powers
        phi_values = [PHI, PHI**2, PHI**3, PHI_INV, PHI_INV**2]
        distances = [abs((normalized / p) % 1 - 0.5) * 2 for p in phi_values]
        min_distance = min(distances)
        
        # Convert distance to resonance (1 = perfect resonance, 0 = no resonance)
        resonance = 1 - min_distance
        return round(resonance, 4)
    
    def entangle_with(self, other_cell: 'MemoryCell') -> None:
        """
        Entangle this cell with another memory cell
        
        Args:
            other_cell: Cell to entangle with
        """
        if other_cell.cell_id not in self.entangled_cells:
            self.entangled_cells.append(other_cell.cell_id)
            
        if self.cell_id not in other_cell.entangled_cells:
            other_cell.entangled_cells.append(self.cell_id)
        
        # Update quantum states to reflect entanglement
        self.quantum_state['entanglement'] = len(self.entangled_cells) / 10
        other_cell.quantum_state['entanglement'] = len(other_cell.entangled_cells) / 10
    
    def get_state(self) -> Dict:
        """
        Get the current state of the memory cell
        
        Returns:
            Dictionary with cell state
        """
        age = time.time() - self.creation_time
        return {
            'cell_id': self.cell_id,
            'has_data': self.data is not None,
            'data_type': type(self.data).__name__ if self.data is not None else None,
            'age': age,
            'access_count': self.access_count,
            'last_access': time.time() - self.last_access_time,
            'phi_resonance': self.phi_resonance,
            'quantum_state': self.quantum_state,
            'entangled_count': len(self.entangled_cells)
        }


class FerrisMemoryRing:
    """
    Circular memory structure that rotates based on phi-harmonic principles
    """
    
    def __init__(self, ring_id: str = None, size: int = 8):
        """
        Initialize a memory ring
        
        Args:
            ring_id: Unique identifier for the ring
            size: Number of memory cells in the ring
        """
        self.ring_id = ring_id or f"ring_{int(time.time())}"
        self.size = max(3, size)  # Minimum size of 3
        
        # Initialize cells
        self.cells = [MemoryCell() for _ in range(self.size)]
        
        # Ring properties
        self.rotation_speed = PHI_INV  # Rotations per second
        self.current_position = 0.0    # Current rotation position (0-1)
        self.active_cell_index = 0     # Currently active cell
        
        # Start rotation thread
        self.is_running = True
        self.rotation_thread = threading.Thread(target=self._rotate, daemon=True)
        self.rotation_thread.start()
        
        # Entangle adjacent cells
        self._create_entanglements()
    
    def _create_entanglements(self) -> None:
        """Create entanglements between adjacent cells"""
        for i in range(self.size):
            # Entangle with next cell
            next_i = (i + 1) % self.size
            self.cells[i].entangle_with(self.cells[next_i])
            
            # Entangle with cell across (if even number of cells)
            if self.size % 2 == 0:
                across_i = (i + self.size // 2) % self.size
                self.cells[i].entangle_with(self.cells[across_i])
    
    def _rotate(self) -> None:
        """Rotate the memory ring based on phi-harmonic principles"""
        last_time = time.time()
        
        while self.is_running:
            # Calculate time delta
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time
            
            # Update position based on rotation speed
            self.current_position = (self.current_position + self.rotation_speed * delta_time) % 1.0
            
            # Calculate active cell based on position
            self.active_cell_index = int(self.current_position * self.size) % self.size
            
            # Sleep briefly
            time.sleep(0.01)
    
    def store(self, data: Any) -> str:
        """
        Store data in the memory ring
        
        Args:
            data: Data to store
            
        Returns:
            Cell ID where data was stored
        """
        # Find the best cell based on phi resonance
        best_cell = None
        best_resonance = -1
        
        for cell in self.cells:
            # Skip cells that already have data
            if cell.data is not None:
                continue
                
            # Calculate potential resonance
            cell.store(data)
            resonance = cell.phi_resonance
            
            if resonance > best_resonance:
                best_resonance = resonance
                best_cell = cell
            
            # Clear the data since we're just testing
            cell.data = None
        
        # If no empty cell found, use the active cell
        if best_cell is None:
            best_cell = self.cells[self.active_cell_index]
        
        # Store the data
        best_cell.store(data)
        return best_cell.cell_id
    
    def retrieve(self, cell_id: str = None) -> Tuple[Any, str]:
        """
        Retrieve data from the memory ring
        
        Args:
            cell_id: ID of the cell to retrieve from (if None, use active cell)
            
        Returns:
            Tuple of (data, cell_id)
        """
        if cell_id:
            # Find the cell with the given ID
            for cell in self.cells:
                if cell.cell_id == cell_id:
                    return cell.retrieve(), cell_id
            
            # Cell not found
            return None, None
        else:
            # Use active cell
            cell = self.cells[self.active_cell_index]
            return cell.retrieve(), cell.cell_id
    
    def get_state(self) -> Dict:
        """
        Get the current state of the memory ring
        
        Returns:
            Dictionary with ring state
        """
        return {
            'ring_id': self.ring_id,
            'size': self.size,
            'active_cell': self.active_cell_index,
            'position': self.current_position,
            'rotation_speed': self.rotation_speed,
            'cells': [cell.get_state() for cell in self.cells],
            'filled_cells': sum(1 for cell in self.cells if cell.data is not None),
            'average_resonance': sum(cell.phi_resonance for cell in self.cells) / self.size
        }
    
    def stop(self) -> None:
        """Stop the memory ring rotation"""
        self.is_running = False
        if self.rotation_thread.is_alive():
            self.rotation_thread.join(timeout=1.0)


class FerrisMemorySystem:
    """
    Complete Ferris Memory System with multiple memory rings
    """
    
    def __init__(self, system_id: str = None, base_dir: str = None):
        """
        Initialize the Ferris Memory System
        
        Args:
            system_id: Unique identifier for the memory system
            base_dir: Base directory for persistent storage
        """
        self.system_id = system_id or f"ferris_{int(time.time())}"
        self.base_dir = base_dir or os.path.join(os.getcwd(), 'ferris_memory')
        
        # Create base directory if it doesn't exist
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        
        # Create system directory
        self.system_dir = os.path.join(self.base_dir, self.system_id)
        if not os.path.exists(self.system_dir):
            os.makedirs(self.system_dir)
        
        # Initialize rings with phi-based sizes
        self.rings = {}
        self._initialize_rings()
        
        # Memory index for quick lookups
        self.memory_index = {}  # {data_hash: (ring_id, cell_id)}
        
        # Statistics
        self.stats = {
            'total_stores': 0,
            'total_retrievals': 0,
            'store_hits': 0,  # When data already exists
            'retrieval_hits': 0,  # Successful retrievals
            'start_time': time.time()
        }
        
        print(f"FerrisMemorySystem initialized: {self.system_id}")
        print(f"Storage location: {self.system_dir}")
        print(f"Rings: {len(self.rings)}")
    
    def _initialize_rings(self) -> None:
        """Initialize memory rings with phi-based sizes"""
        # Create rings with sizes based on Fibonacci sequence
        fib_sizes = [3, 5, 8, 13, 21]
        
        for i, size in enumerate(fib_sizes):
            ring_id = f"ring_{i}_{size}"
            self.rings[ring_id] = FerrisMemoryRing(ring_id=ring_id, size=size)
    
    def _hash_data(self, data: Any) -> str:
        """
        Create a hash for the data
        
        Args:
            data: Data to hash
            
        Returns:
            Hash string
        """
        # Convert data to bytes
        if isinstance(data, (str, int, float, bool)):
            data_str = str(data)
        else:
            try:
                data_str = json.dumps(data, sort_keys=True)
            except:
                data_str = str(data)
        
        # Create hash
        return hashlib.md5(data_str.encode()).hexdigest()
    
    def store(self, data: Any, force_new: bool = False) -> Dict:
        """
        Store data in the memory system
        
        Args:
            data: Data to store
            force_new: Force storing as new even if it exists
            
        Returns:
            Storage result
        """
        self.stats['total_stores'] += 1
        
        # Check if data already exists
        data_hash = self._hash_data(data)
        if not force_new and data_hash in self.memory_index:
            self.stats['store_hits'] += 1
            ring_id, cell_id = self.memory_index[data_hash]
            
            # Update access time by retrieving and storing again
            ring = self.rings[ring_id]
            existing_data, _ = ring.retrieve(cell_id)
            
            return {
                'status': 'exists',
                'data_hash': data_hash,
                'ring_id': ring_id,
                'cell_id': cell_id
            }
        
        # Find the best ring based on phi resonance
        best_ring = None
        best_resonance = -1
        
        # Test store in each ring to find best resonance
        for ring_id, ring in self.rings.items():
            # Create a temporary copy of the ring to test
            test_ring = FerrisMemoryRing(size=ring.size)
            test_ring.store(data)
            
            # Get average resonance
            state = test_ring.get_state()
            resonance = state['average_resonance']
            
            if resonance > best_resonance:
                best_resonance = resonance
                best_ring = ring_id
            
            # Stop the test ring
            test_ring.stop()
        
        # Store in the best ring
        ring = self.rings[best_ring]
        cell_id = ring.store(data)
        
        # Update index
        self.memory_index[data_hash] = (best_ring, cell_id)
        
        # Save index periodically
        if self.stats['total_stores'] % 10 == 0:
            self._save_index()
        
        return {
            'status': 'stored',
            'data_hash': data_hash,
            'ring_id': best_ring,
            'cell_id': cell_id,
            'resonance': best_resonance
        }
    
    def retrieve(self, data_hash: str = None, ring_id: str = None, cell_id: str = None) -> Tuple[Any, Dict]:
        """
        Retrieve data from the memory system
        
        Args:
            data_hash: Hash of the data to retrieve
            ring_id: ID of the ring to retrieve from
            cell_id: ID of the cell to retrieve from
            
        Returns:
            Tuple of (data, retrieval_info)
        """
        self.stats['total_retrievals'] += 1
        
        # Determine which ring and cell to retrieve from
        if data_hash and data_hash in self.memory_index:
            ring_id, cell_id = self.memory_index[data_hash]
        elif not ring_id:
            # If no specific location, use the ring with highest phi resonance
            ring_id = max(self.rings.keys(), key=lambda r: self.rings[r].get_state()['average_resonance'])
        
        # Retrieve data
        if ring_id in self.rings:
            ring = self.rings[ring_id]
            data, actual_cell_id = ring.retrieve(cell_id)
            
            if data is not None:
                self.stats['retrieval_hits'] += 1
                
                return data, {
                    'status': 'found',
                    'ring_id': ring_id,
                    'cell_id': actual_cell_id,
                    'data_hash': data_hash or self._hash_data(data)
                }
        
        return None, {
            'status': 'not_found',
            'ring_id': ring_id,
            'cell_id': cell_id,
            'data_hash': data_hash
        }
    
    def _save_index(self) -> None:
        """Save the memory index to disk"""
        index_path = os.path.join(self.system_dir, 'memory_index.pkl')
        with open(index_path, 'wb') as f:
            pickle.dump(self.memory_index, f)
    
    def _load_index(self) -> None:
        """Load the memory index from disk"""
        index_path = os.path.join(self.system_dir, 'memory_index.pkl')
        if os.path.exists(index_path):
            with open(index_path, 'rb') as f:
                self.memory_index = pickle.load(f)
    
    def get_stats(self) -> Dict:
        """
        Get memory system statistics
        
        Returns:
            Dictionary with statistics
        """
        # Calculate uptime
        uptime = time.time() - self.stats['start_time']
        
        # Calculate total capacity and usage
        total_cells = sum(ring.size for ring in self.rings.values())
        used_cells = sum(ring.get_state()['filled_cells'] for ring in self.rings.values())
        
        # Calculate hit rates
        store_hit_rate = self.stats['store_hits'] / max(1, self.stats['total_stores'])
        retrieval_hit_rate = self.stats['retrieval_hits'] / max(1, self.stats['total_retrievals'])
        
        # Calculate average resonance
        avg_resonance = sum(ring.get_state()['average_resonance'] for ring in self.rings.values()) / len(self.rings)
        
        return {
            'system_id': self.system_id,
            'uptime': uptime,
            'total_rings': len(self.rings),
            'total_capacity': total_cells,
            'used_capacity': used_cells,
            'usage_percent': (used_cells / total_cells) * 100 if total_cells > 0 else 0,
            'total_stores': self.stats['total_stores'],
            'total_retrievals': self.stats['total_retrievals'],
            'store_hit_rate': store_hit_rate,
            'retrieval_hit_rate': retrieval_hit_rate,
            'average_resonance': avg_resonance,
            'index_size': len(self.memory_index)
        }
    
    def get_state(self) -> Dict:
        """
        Get the current state of the memory system
        
        Returns:
            Dictionary with system state
        """
        return {
            'system_id': self.system_id,
            'stats': self.get_stats(),
            'rings': {ring_id: ring.get_state() for ring_id, ring in self.rings.items()}
        }
    
    def stop(self) -> None:
        """Stop the memory system"""
        # Save index
        self._save_index()
        
        # Stop all rings
        for ring in self.rings.values():
            ring.stop()
        
        print(f"FerrisMemorySystem stopped: {self.system_id}")


def create_ferris_memory(system_id: str = None, base_dir: str = None) -> FerrisMemorySystem:
    """
    Create a Ferris Memory System
    
    Args:
        system_id: Unique identifier for the memory system
        base_dir: Base directory for persistent storage
        
    Returns:
        FerrisMemorySystem instance
    """
    return FerrisMemorySystem(system_id=system_id, base_dir=base_dir)


if __name__ == "__main__":
    # Simple test
    print("Testing Ferris Memory System...")
    
    # Create memory system
    memory = create_ferris_memory(system_id="test_system")
    
    # Store some data
    print("\nStoring data...")
    result1 = memory.store("Hello, Ferris Memory!")
    print(f"Store result 1: {result1}")
    
    result2 = memory.store([1, 1, 2, 3, 5, 8, 13])
    print(f"Store result 2: {result2}")
    
    result3 = memory.store({"name": "Phi", "value": PHI})
    print(f"Store result 3: {result3}")
    
    # Retrieve data
    print("\nRetrieving data...")
    data1, info1 = memory.retrieve(data_hash=result1['data_hash'])
    print(f"Retrieved: {data1}")
    print(f"Retrieval info: {info1}")
    
    # Get stats
    print("\nMemory stats:")
    stats = memory.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Stop memory system
    memory.stop()
    
    print("\nTest completed.")
