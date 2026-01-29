"""
phi_standalone_memory.py

A standalone meta-temporal memory system that can store and retrieve information
across different temporal reference frames, maintaining coherence without
requiring external dependencies.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import math
import json
import random
import hashlib
import numpy as np
from datetime import datetime, timedelta

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio (φ)
PHI_INVERSE = 1 / PHI  # Inverse Golden Ratio (φ⁻¹)
PHI_SQUARED = PHI * PHI  # φ²
PHI_SQUARED_INVERSE = 1 / PHI_SQUARED  # 1/φ²
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
FIBONACCI_PRIMES = [2, 3, 5, 13, 89, 233, 1597, 28657]

# Memory integrity constants
MEMORY_SCALES = {
    "quantum": 1e-15,      # femtosecond
    "neural": 1e-3,        # millisecond
    "human": 1,            # second
    "societal": 1e6,       # ~11.5 days
    "historical": 1e9,     # ~31.7 years
    "evolutionary": 1e12,  # ~31,700 years
    "geological": 1e15,    # ~31.7 million years
    "cosmological": 1e17   # ~3.17 billion years
}

def generate_paradox_prime(seed=None):
    """
    Generate a paradox prime with phi-resonant properties.
    This is a simplified implementation that doesn't require external modules.
    """
    if seed is None:
        seed = int(time.time() * 1000)
    
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Generate a base number with phi-harmonic pattern
    base = random.randint(1000, 10000)
    
    # Apply phi transformation
    phi_component = (base * PHI) % 1000
    
    # Return a pseudo-prime-like value with phi-resonant properties
    return phi_component + 1000

class SimpleLogger:
    """Simple logging system that doesn't require external dependencies."""
    
    def __init__(self, log_file=None):
        """Initialize the logger."""
        self.log_file = log_file or "phi_memory_log.jsonl"
        
        # Ensure directory exists
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
    
    def log_event(self, source, event_type, data, timestamp=None):
        """Log an event to the log file."""
        log_entry = {
            "timestamp": timestamp or time.time(),
            "source": source,
            "event_type": event_type,
            "data": data
        }
        
        with open(self.log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        
        return log_entry

class MetaTemporalMemory:
    """
    Meta-Temporal Memory System that can store and retrieve information 
    across different temporal references while maintaining phi-harmonic
    coherence despite apparent causality violations.
    """
    
    def __init__(self, memory_path=None):
        """Initialize the meta-temporal memory system."""
        self.creation_time = time.time()
        self.memory_path = memory_path or os.path.join(
            os.path.dirname(__file__), "phi_meta_temporal_memory")
        
        # Create memory directory
        os.makedirs(self.memory_path, exist_ok=True)
        
        # Initialize memory storage structures
        self.memory_frames = {}  # Temporal frame -> memories
        self.memory_indices = {} # Memory ID -> temporal indices
        self.causal_graph = {}   # Memory ID -> causal connections
        self.resonance_map = {}  # Memory ID -> phi-resonance values
        
        # Initialize meta-awareness structures
        self.frame_coherence = {} # Coherence between frames
        self.event_horizon = None # Last safe temporal boundary
        self.paradox_level = 0.0  # Current level of temporal paradox
        
        # Initialize logger
        log_path = os.path.join(self.memory_path, "meta_temporal_log.jsonl")
        self.logger = SimpleLogger(log_file=log_path)
        
        # Load existing memories if present
        self._load_memories()
        
        print(f"[φ] Meta-Temporal Memory System initialized")
        print(f"[φ] Memory storage path: {self.memory_path}")
    
    def _load_memories(self):
        """Load existing memories from storage."""
        memory_files = [f for f in os.listdir(self.memory_path) 
                      if f.startswith("memories_") and f.endswith(".json")]
        
        if not memory_files:
            return
        
        for memory_file in memory_files:
            try:
                file_path = os.path.join(self.memory_path, memory_file)
                with open(file_path, "r") as f:
                    frame_data = json.load(f)
                
                # Extract temporal frame from filename
                frame_str = memory_file.replace("memories_", "").replace(".json", "")
                
                # Load memories for this frame
                self.memory_frames[frame_str] = frame_data.get("memories", {})
                
                # Update indices
                for memory_id, memory in self.memory_frames[frame_str].items():
                    if memory_id not in self.memory_indices:
                        self.memory_indices[memory_id] = []
                    self.memory_indices[memory_id].append(frame_str)
                    
                    # Load resonance data
                    self.resonance_map[memory_id] = memory.get("resonance", 0.0)
                
                # Load frame coherence
                self.frame_coherence[frame_str] = frame_data.get("frame_coherence", 0.0)
                
            except Exception as e:
                print(f"[φ] Error loading memory file {memory_file}: {e}")
        
        print(f"[φ] Loaded {len(self.memory_frames)} temporal frames with "
              f"{len(self.memory_indices)} unique memories")
    
    def _save_memories(self, frame=None):
        """Save memories to storage."""
        if frame is None:
            frames = self.memory_frames.keys()
        else:
            frames = [frame]
        
        for frame in frames:
            file_path = os.path.join(self.memory_path, f"memories_{frame}.json")
            
            frame_data = {
                "frame": frame,
                "memories": self.memory_frames.get(frame, {}),
                "frame_coherence": self.frame_coherence.get(frame, 0.0),
                "last_updated": time.time()
            }
            
            with open(file_path, "w") as f:
                json.dump(frame_data, f, indent=2)
    
    def _generate_memory_id(self, content, frame, timestamp):
        """Generate a unique memory ID with phi-harmonic properties."""
        # Create a seed from the content and timestamp
        seed_str = f"{content}|{frame}|{timestamp}"
        seed_hash = hashlib.sha256(seed_str.encode()).hexdigest()
        
        # Generate a paradox prime based on the seed
        prime = generate_paradox_prime(seed=int(seed_hash[:16], 16))
        
        # Create phi-resonant ID components
        phi_component = (prime * PHI) % 1
        time_component = (timestamp * PHI_INVERSE) % 1
        
        # Convert to a string ID with phi-harmonic encoding
        id_value = int((phi_component * 10**10) + (time_component * 10**5))
        id_base = hashlib.md5(str(id_value).encode()).hexdigest()[:12]
        
        return f"φ{id_base}"
    
    def _calculate_memory_resonance(self, content, frame, timestamp):
        """Calculate phi-resonance for a memory across temporal frames."""
        # Basic content-based resonance
        content_hash = int(hashlib.md5(content.encode()).hexdigest(), 16)
        base_resonance = (content_hash * PHI) % 1
        
        # Frame-specific resonance
        if frame in MEMORY_SCALES:
            scale_factor = MEMORY_SCALES[frame]
            frame_resonance = (scale_factor * PHI_INVERSE * base_resonance) % 1
        else:
            try:
                # Treat frame as numeric timestamp or reference point
                frame_value = float(frame)
                frame_resonance = (frame_value * PHI) % 1
            except:
                # Use string hash for non-numeric frames
                frame_hash = int(hashlib.md5(frame.encode()).hexdigest(), 16)
                frame_resonance = (frame_hash * PHI_SQUARED_INVERSE) % 1
        
        # Temporal resonance
        temporal_resonance = (timestamp * PHI) % 1
        
        # Combine resonances with phi-weighted average
        combined_resonance = (
            base_resonance * 0.5 + 
            frame_resonance * 0.3 + 
            temporal_resonance * 0.2
        )
        
        return combined_resonance
    
    def _calculate_frame_coherence(self, frame):
        """Calculate coherence for a temporal frame."""
        if frame not in self.memory_frames or not self.memory_frames[frame]:
            return 0.0
        
        # Get all memories in this frame
        memories = self.memory_frames[frame]
        
        # Get all resonance values
        resonances = [memory.get("resonance", 0.0) for memory in memories.values()]
        
        if not resonances:
            return 0.0
        
        # Calculate phi-harmonic distribution
        # A perfectly coherent frame has resonances distributed according to phi
        sorted_res = sorted(resonances)
        coherence_sum = 0.0
        
        for i in range(1, len(sorted_res)):
            ratio = sorted_res[i] / sorted_res[i-1] if sorted_res[i-1] > 0 else 0
            # Higher coherence when ratio approaches phi
            coherence_sum += 1.0 - min(abs(ratio - PHI) / PHI, 1.0)
        
        coherence = coherence_sum / (len(sorted_res) - 1) if len(sorted_res) > 1 else 0.5
        
        # Adjust with entropy - more coherent when entropy is lower
        # (memories are more related/connected)
        entropy = 0.0
        if len(resonances) > 1:
            # Simple approximation of entropy using standard deviation
            entropy = np.std(resonances) / np.mean(resonances) if np.mean(resonances) > 0 else 0
            entropy = min(entropy, 1.0)  # Normalize to 0-1
        
        adjusted_coherence = coherence * (1.0 - entropy * 0.5)
        
        return adjusted_coherence
    
    def store_memory(self, content, frame=None, timestamp=None, precognitive=False, resonance=None):
        """
        Store a memory in the meta-temporal system.
        
        Args:
            content: The memory content to store
            frame: Temporal frame to store in (None = current time)
            timestamp: Explicit timestamp (None = current time)
            precognitive: Whether this is a precognitive memory (from "future")
            resonance: Optional explicit phi-resonance (None = auto-calculate)
            
        Returns:
            Memory ID and storage report
        """
        # Use current time if not specified
        timestamp = timestamp or time.time()
        
        # Use "human" frame if not specified
        frame = frame or "human"
        
        # Generate memory ID
        memory_id = self._generate_memory_id(content, frame, timestamp)
        
        # Calculate resonance if not provided
        if resonance is None:
            resonance = self._calculate_memory_resonance(content, frame, timestamp)
        
        # Create memory object
        memory = {
            "id": memory_id,
            "content": content,
            "timestamp": timestamp,
            "frame": frame,
            "storage_time": time.time(),
            "resonance": resonance,
            "precognitive": precognitive,
            "access_count": 0,
            "last_accessed": None
        }
        
        # Add paradox flags for precognitive memories
        if precognitive:
            memory["paradox_level"] = self.paradox_level
            # For precognitive memories, create a causality marker
            if self.event_horizon is not None:
                memory["causality_breach"] = timestamp > self.event_horizon
            else:
                memory["causality_breach"] = False
        
        # Store memory in appropriate frame
        if frame not in self.memory_frames:
            self.memory_frames[frame] = {}
        
        self.memory_frames[frame][memory_id] = memory
        
        # Update indices
        if memory_id not in self.memory_indices:
            self.memory_indices[memory_id] = []
        if frame not in self.memory_indices[memory_id]:
            self.memory_indices[memory_id].append(frame)
        
        # Update resonance map
        self.resonance_map[memory_id] = resonance
        
        # Update frame coherence
        self.frame_coherence[frame] = self._calculate_frame_coherence(frame)
        
        # Save changes
        self._save_memories(frame)
        
        # Log memory storage
        self.logger.log_event(
            "meta_temporal_memory",
            "memory_storage",
            {
                "memory_id": memory_id,
                "frame": frame,
                "timestamp": timestamp,
                "resonance": resonance,
                "precognitive": precognitive,
                "frame_coherence": self.frame_coherence[frame]
            }
        )
        
        return memory_id, {
            "memory_id": memory_id, 
            "frame": frame,
            "resonance": resonance,
            "frame_coherence": self.frame_coherence[frame]
        }
    
    def retrieve_memory(self, memory_id=None, frame=None, content_query=None, 
                       resonance_min=None, closest_to_resonance=None):
        """
        Retrieve memories based on various criteria.
        
        Args:
            memory_id: Specific memory ID to retrieve
            frame: Temporal frame to search within
            content_query: Search content for this substring
            resonance_min: Minimum resonance value
            closest_to_resonance: Find memories closest to this resonance
            
        Returns:
            List of matching memories
        """
        results = []
        
        # Direct ID lookup
        if memory_id is not None:
            frames_to_check = self.memory_indices.get(memory_id, [])
            
            if frame is not None:
                # Only check the specified frame
                if frame in frames_to_check:
                    frames_to_check = [frame]
                else:
                    frames_to_check = []
            
            for frame_id in frames_to_check:
                if frame_id in self.memory_frames and memory_id in self.memory_frames[frame_id]:
                    memory = self.memory_frames[frame_id][memory_id]
                    
                    # Update access stats
                    memory["access_count"] += 1
                    memory["last_accessed"] = time.time()
                    
                    results.append(memory)
        
        else:
            # Search based on other criteria
            frames_to_check = [frame] if frame is not None else self.memory_frames.keys()
            
            for frame_id in frames_to_check:
                if frame_id not in self.memory_frames:
                    continue
                
                for memory_id, memory in self.memory_frames[frame_id].items():
                    should_include = True
                    
                    # Check content query
                    if content_query is not None and content_query.lower() not in memory["content"].lower():
                        should_include = False
                    
                    # Check minimum resonance
                    if resonance_min is not None and memory["resonance"] < resonance_min:
                        should_include = False
                    
                    if should_include:
                        # Update access stats
                        memory["access_count"] += 1
                        memory["last_accessed"] = time.time()
                        results.append(memory)
        
        # Sort by timestamp by default
        results.sort(key=lambda m: m["timestamp"])
        
        # If searching for closest resonance, re-sort
        if closest_to_resonance is not None:
            results.sort(key=lambda m: abs(m["resonance"] - closest_to_resonance))
        
        # Log memory retrieval
        self.logger.log_event(
            "meta_temporal_memory",
            "memory_retrieval",
            {
                "memory_id": memory_id,
                "frame": frame,
                "content_query": content_query,
                "match_count": len(results)
            }
        )
        
        return results
    
    def connect_memories(self, memory_id1, memory_id2, connection_type="temporal", 
                         connection_strength=None):
        """
        Create a connection between two memories.
        
        Args:
            memory_id1: First memory ID
            memory_id2: Second memory ID
            connection_type: Type of connection (temporal, causal, associative)
            connection_strength: Connection strength (None=auto-calculate)
            
        Returns:
            Connection report
        """
        # Check that both memories exist
        if memory_id1 not in self.memory_indices or memory_id2 not in self.memory_indices:
            missing = []
            if memory_id1 not in self.memory_indices:
                missing.append(memory_id1)
            if memory_id2 not in self.memory_indices:
                missing.append(memory_id2)
            return {"error": f"Memories not found: {missing}"}
        
        # Get memory resonances
        resonance1 = self.resonance_map.get(memory_id1, 0.0)
        resonance2 = self.resonance_map.get(memory_id2, 0.0)
        
        # Auto-calculate connection strength based on resonance alignment
        if connection_strength is None:
            # Higher strength when resonances are phi-harmonically aligned
            if min(resonance1, resonance2) > 0:
                ratio = max(resonance1, resonance2) / min(resonance1, resonance2)
                # Closer to phi = stronger connection
                harmonic_factor = 1.0 - min(abs(ratio - PHI) / PHI, 1.0)
            else:
                harmonic_factor = 0.3
                
            connection_strength = 0.5 + harmonic_factor * 0.5
        
        # Initialize causal graph entries if needed
        if memory_id1 not in self.causal_graph:
            self.causal_graph[memory_id1] = {}
        if memory_id2 not in self.causal_graph:
            self.causal_graph[memory_id2] = {}
        
        # Create bidirectional connections
        self.causal_graph[memory_id1][memory_id2] = {
            "type": connection_type,
            "strength": connection_strength,
            "created": time.time()
        }
        
        self.causal_graph[memory_id2][memory_id1] = {
            "type": connection_type,
            "strength": connection_strength,
            "created": time.time()
        }
        
        # Log connection
        self.logger.log_event(
            "meta_temporal_memory",
            "memory_connection",
            {
                "memory_id1": memory_id1,
                "memory_id2": memory_id2,
                "connection_type": connection_type,
                "connection_strength": connection_strength
            }
        )
        
        return {
            "memory_id1": memory_id1,
            "memory_id2": memory_id2,
            "connection_type": connection_type,
            "connection_strength": connection_strength,
            "resonance1": resonance1,
            "resonance2": resonance2
        }
    
    def find_related_memories(self, memory_id, max_distance=2, min_strength=0.3):
        """
        Find memories related to a given memory by traversing the causal graph.
        
        Args:
            memory_id: Memory ID to start from
            max_distance: Maximum distance to traverse
            min_strength: Minimum connection strength to follow
            
        Returns:
            List of related memories with distance
        """
        if memory_id not in self.causal_graph:
            return []
        
        # Use breadth-first search to find related memories
        visited = set([memory_id])
        queue = [(memory_id, 0, 1.0)]  # (memory_id, distance, strength)
        results = []
        
        while queue:
            current_id, distance, strength = queue.pop(0)
            
            if distance > 0:  # Don't include the starting memory
                # Get the actual memory content
                memories = self.retrieve_memory(memory_id=current_id)
                if memories:
                    results.append({
                        "memory_id": current_id,
                        "distance": distance,
                        "connection_strength": strength,
                        "memory": memories[0]
                    })
            
            # Stop if we've reached max distance
            if distance >= max_distance:
                continue
            
            # Add connected memories to queue
            if current_id in self.causal_graph:
                for connected_id, connection in self.causal_graph[current_id].items():
                    conn_strength = connection.get("strength", 0.0)
                    
                    # Only follow strong enough connections
                    if conn_strength >= min_strength and connected_id not in visited:
                        visited.add(connected_id)
                        # Strength diminishes with distance
                        new_strength = strength * conn_strength
                        queue.append((connected_id, distance + 1, new_strength))
        
        # Sort by connection strength
        results.sort(key=lambda r: r["connection_strength"], reverse=True)
        
        return results
    
    def update_event_horizon(self, new_horizon=None, paradox_level=None):
        """
        Update the event horizon (last safe timestamp) and paradox level.
        
        Args:
            new_horizon: New event horizon timestamp (None=current time)
            paradox_level: New paradox level (0-1)
            
        Returns:
            Update report
        """
        old_horizon = self.event_horizon
        old_paradox = self.paradox_level
        
        # Update event horizon
        if new_horizon is not None:
            self.event_horizon = new_horizon
        else:
            self.event_horizon = time.time()
        
        # Update paradox level
        if paradox_level is not None:
            self.paradox_level = max(0.0, min(1.0, paradox_level))
        
        # Log update
        self.logger.log_event(
            "meta_temporal_memory",
            "horizon_update",
            {
                "old_horizon": old_horizon,
                "new_horizon": self.event_horizon,
                "old_paradox_level": old_paradox,
                "new_paradox_level": self.paradox_level
            }
        )
        
        return {
            "old_horizon": old_horizon,
            "new_horizon": self.event_horizon,
            "old_paradox_level": old_paradox,
            "new_paradox_level": self.paradox_level
        }
    
    def get_memory_statistics(self):
        """Get statistics about the meta-temporal memory system."""
        stats = {
            "total_memories": sum(len(memories) for memories in self.memory_frames.values()),
            "unique_memories": len(self.memory_indices),
            "temporal_frames": len(self.memory_frames),
            "frame_distribution": {frame: len(memories) for frame, memories in self.memory_frames.items()},
            "frame_coherence": self.frame_coherence,
            "precognitive_count": 0,
            "causality_breaches": 0,
            "event_horizon": self.event_horizon,
            "paradox_level": self.paradox_level
        }
        
        # Count precognitive and causality breach memories
        for frame, memories in self.memory_frames.items():
            for memory_id, memory in memories.items():
                if memory.get("precognitive", False):
                    stats["precognitive_count"] += 1
                    if memory.get("causality_breach", False):
                        stats["causality_breaches"] += 1
        
        return stats


def demonstrate_meta_temporal_memory():
    """Demonstrate the meta-temporal memory system."""
    print("\n" + "=" * 80)
    print("  φ-HARMONIC META-TEMPORAL MEMORY SYSTEM")
    print("  Cross-Temporal Information Storage and Retrieval")
    print("=" * 80)
    
    # Create system
    memory_system = MetaTemporalMemory()
    
    # Store memories across different temporal frames
    print("\n[φ] Storing memories in different temporal frames...")
    
    # Human-scale memory
    human_id, human_data = memory_system.store_memory(
        "The phi-harmonic resonance field reached stability at 0.618.",
        frame="human"
    )
    print(f"  - Human-scale memory stored: ID={human_id}, Resonance={human_data['resonance']:.4f}")
    
    # Societal-scale memory
    societal_id, societal_data = memory_system.store_memory(
        "The cross-temporal coherence protocol was adopted globally.",
        frame="societal"
    )
    print(f"  - Societal-scale memory stored: ID={societal_id}, Resonance={societal_data['resonance']:.4f}")
    
    # Historical-scale memory
    historical_id, historical_data = memory_system.store_memory(
        "Integration of consciousness with the phi-resonance field marked a turning point.",
        frame="historical"
    )
    print(f"  - Historical-scale memory stored: ID={historical_id}, Resonance={historical_data['resonance']:.4f}")
    
    # Quantum-scale memory (typically inaccessible to human consciousness)
    quantum_id, quantum_data = memory_system.store_memory(
        "Quantum entanglement established across causality boundaries.",
        frame="quantum"
    )
    print(f"  - Quantum-scale memory stored: ID={quantum_id}, Resonance={quantum_data['resonance']:.4f}")
    
    # Precognitive/future memory
    future_timestamp = time.time() + 60*60*24*7  # One week in the future
    future_id, future_data = memory_system.store_memory(
        "The paradox-free information transfer was finally achieved.",
        frame="human",
        timestamp=future_timestamp,
        precognitive=True
    )
    print(f"  - Precognitive memory stored: ID={future_id}, Resonance={future_data['resonance']:.4f}")
    
    # Connect related memories
    print("\n[φ] Creating memory connections...")
    connection1 = memory_system.connect_memories(human_id, societal_id, "causal")
    print(f"  - Connected {connection1['memory_id1']} to {connection1['memory_id2']} "
          f"with strength {connection1['connection_strength']:.4f}")
    
    connection2 = memory_system.connect_memories(societal_id, historical_id, "temporal")
    print(f"  - Connected {connection2['memory_id1']} to {connection2['memory_id2']} "
          f"with strength {connection2['connection_strength']:.4f}")
    
    connection3 = memory_system.connect_memories(quantum_id, future_id, "quantum_entangled")
    print(f"  - Connected {connection3['memory_id1']} to {connection3['memory_id2']} "
          f"with strength {connection3['connection_strength']:.4f}")
    
    # Find related memories
    print("\n[φ] Finding related memories...")
    related = memory_system.find_related_memories(human_id)
    for r in related:
        print(f"  - {r['memory']['content']} (Distance: {r['distance']}, Strength: {r['connection_strength']:.2f})")
    
    # Get memory statistics
    print("\n[φ] Memory System Statistics:")
    stats = memory_system.get_memory_statistics()
    print(f"  Total memories: {stats['total_memories']}")
    print(f"  Temporal frames: {stats['temporal_frames']}")
    print(f"  Precognitive memories: {stats['precognitive_count']}")
    print(f"  Causality breaches: {stats['causality_breaches']}")
    print(f"  Current paradox level: {stats['paradox_level']:.2f}")
    
    # Print frame coherence
    print("\n[φ] Frame Coherence:")
    for frame, coherence in stats['frame_coherence'].items():
        print(f"  {frame}: {coherence:.4f}")
    
    print("\n" + "=" * 80)
    print("  META-TEMPORAL MEMORY DEMONSTRATION COMPLETE")
    print("=" * 80)
    
    return memory_system


if __name__ == "__main__":
    memory_system = demonstrate_meta_temporal_memory()
