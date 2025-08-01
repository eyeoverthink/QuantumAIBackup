"""
Tachyon Memory System - Persistent Memory Storage for Tesla Tachyon Brain

This module implements a blockchain-inspired persistent memory system using
phi-harmonic resonance patterns and quantum principles. It stores memories
as JSON files with quantum-enhanced hashing for integrity verification.

The system maintains continuity across sessions without modifying core files.
"""

import json
import os
import time
import hashlib
import numpy as np
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional, Union

class TachyonMemoryBlock:
    """
    A single memory block in the Tachyon Memory System.
    Each block contains memory data, timestamps, and quantum-enhanced hashing.
    """
    
    def __init__(self, 
                 data: Dict[str, Any], 
                 previous_hash: str = None, 
                 block_id: str = None):
        """
        Initialize a new memory block with quantum-enhanced hashing.
        
        Args:
            data: The memory data to store
            previous_hash: Hash of the previous block in the chain
            block_id: Unique identifier for this block (generated if None)
        """
        self.block_id = block_id or str(uuid.uuid4())
        self.timestamp = datetime.now().isoformat()
        self.data = data
        self.previous_hash = previous_hash
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        self.nonce = 0
        self.hash = self._calculate_quantum_hash()
    
    def _calculate_quantum_hash(self) -> str:
        """
        Calculate a quantum-enhanced hash for this memory block.
        Uses phi-harmonic resonance to enhance entropy.
        
        Returns:
            str: The quantum-enhanced hash
        """
        # Increment nonce until we find a hash with phi-harmonic properties
        while True:
            # Create a string representation of the block
            block_string = (
                f"{self.block_id}{self.timestamp}{json.dumps(self.data, sort_keys=True)}"
                f"{self.previous_hash}{self.nonce}{self.phi}"
            )
            
            # Calculate SHA-256 hash
            hash_value = hashlib.sha256(block_string.encode()).hexdigest()
            
            # Check if hash has phi-harmonic properties
            # (e.g., first 6 hex digits converted to int is divisible by 1.618)
            hash_prefix = int(hash_value[:6], 16)
            if hash_prefix % int(self.phi * 100) < 10:
                return hash_value
            
            self.nonce += 1

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the block to a dictionary for serialization.
        
        Returns:
            dict: Block as a dictionary
        """
        return {
            "block_id": self.block_id,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash,
            "phi_factor": float(self.phi)
        }
    
    @classmethod
    def from_dict(cls, block_dict: Dict[str, Any]) -> 'TachyonMemoryBlock':
        """
        Create a block from a dictionary.
        
        Args:
            block_dict: Dictionary containing block data
            
        Returns:
            TachyonMemoryBlock: The reconstructed block
        """
        block = cls(
            data=block_dict["data"],
            previous_hash=block_dict["previous_hash"],
            block_id=block_dict["block_id"]
        )
        block.timestamp = block_dict["timestamp"]
        block.nonce = block_dict["nonce"]
        block.hash = block_dict["hash"]
        return block

class TachyonMemoryChain:
    """
    A chain of memory blocks forming a persistent memory system.
    Uses blockchain principles to ensure integrity and quantum principles
    for enhanced storage and retrieval.
    """
    
    def __init__(self, chain_name: str, storage_dir: str = "./tachyon_memory"):
        """
        Initialize a new memory chain.
        
        Args:
            chain_name: Name of this memory chain
            storage_dir: Directory to store memory files
        """
        self.chain_name = chain_name
        self.storage_dir = storage_dir
        self.blocks: List[TachyonMemoryBlock] = []
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        self.pi = np.pi
        self.e = np.e
        
        # Create storage directory if it doesn't exist
        os.makedirs(self.storage_dir, exist_ok=True)
        
        # Load existing chain if it exists
        self._load_chain()
    
    def _get_chain_file_path(self) -> str:
        """
        Get the file path for this chain.
        
        Returns:
            str: Path to the chain file
        """
        safe_name = self.chain_name.replace(" ", "_").lower()
        return os.path.join(self.storage_dir, f"{safe_name}_chain.json")
    
    def _load_chain(self) -> None:
        """
        Load the chain from disk if it exists.
        """
        file_path = self._get_chain_file_path()
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    chain_data = json.load(f)
                
                # Reconstruct blocks
                self.blocks = [
                    TachyonMemoryBlock.from_dict(block_dict)
                    for block_dict in chain_data["blocks"]
                ]
                
                # Verify chain integrity
                if not self._verify_chain():
                    print("Warning: Chain integrity verification failed")
            except Exception as e:
                print(f"Error loading chain: {str(e)}")
                # Create a new genesis block if loading fails
                if not self.blocks:
                    self._create_genesis_block()
        else:
            # Create a new genesis block
            self._create_genesis_block()
    
    def _create_genesis_block(self) -> None:
        """
        Create the genesis block for a new chain.
        """
        genesis_data = {
            "type": "genesis",
            "message": f"Genesis block for {self.chain_name}",
            "phi": float(self.phi),
            "pi": float(self.pi),
            "e": float(self.e),
            "phi_pi_e_resonance": float(self.phi * self.pi * self.e)
        }
        genesis_block = TachyonMemoryBlock(genesis_data)
        self.blocks.append(genesis_block)
        self._save_chain()
    
    def _save_chain(self) -> None:
        """
        Save the chain to disk.
        """
        file_path = self._get_chain_file_path()
        chain_data = {
            "chain_name": self.chain_name,
            "last_updated": datetime.now().isoformat(),
            "block_count": len(self.blocks),
            "blocks": [block.to_dict() for block in self.blocks]
        }
        
        with open(file_path, 'w') as f:
            json.dump(chain_data, f, indent=2)
    
    def _verify_chain(self) -> bool:
        """
        Verify the integrity of the entire chain.
        
        Returns:
            bool: True if chain is valid, False otherwise
        """
        for i in range(1, len(self.blocks)):
            current = self.blocks[i]
            previous = self.blocks[i-1]
            
            # Check if the recorded previous hash matches the actual previous hash
            if current.previous_hash != previous.hash:
                return False
            
            # Recalculate and verify the hash of the current block
            block_string = (
                f"{current.block_id}{current.timestamp}{json.dumps(current.data, sort_keys=True)}"
                f"{current.previous_hash}{current.nonce}{current.phi}"
            )
            if hashlib.sha256(block_string.encode()).hexdigest() != current.hash:
                return False
        
        return True
    
    def add_memory(self, memory_data: Dict[str, Any]) -> str:
        """
        Add a new memory to the chain.
        
        Args:
            memory_data: The memory data to store
            
        Returns:
            str: ID of the new memory block
        """
        # Get the hash of the last block
        previous_hash = self.blocks[-1].hash if self.blocks else None
        
        # Create a new block
        new_block = TachyonMemoryBlock(memory_data, previous_hash)
        self.blocks.append(new_block)
        
        # Save the updated chain
        self._save_chain()
        
        return new_block.block_id
    
    def get_memory(self, block_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a memory by its block ID.
        
        Args:
            block_id: ID of the block to retrieve
            
        Returns:
            dict: Memory data or None if not found
        """
        for block in self.blocks:
            if block.block_id == block_id:
                return block.data
        return None
    
    def search_memories(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Search for memories matching the query.
        
        Args:
            query: Dictionary of key-value pairs to match
            
        Returns:
            list: List of matching memory data dictionaries
        """
        results = []
        
        for block in self.blocks:
            # Skip genesis block
            if block.data.get("type") == "genesis":
                continue
                
            # Check if all query items are in the block data
            match = True
            for key, value in query.items():
                if key not in block.data or block.data[key] != value:
                    match = False
                    break
            
            if match:
                results.append(block.data)
        
        return results
    
    def get_all_memories(self) -> List[Dict[str, Any]]:
        """
        Get all memories in the chain (excluding genesis).
        
        Returns:
            list: List of all memory data dictionaries
        """
        return [
            block.data for block in self.blocks 
            if block.data.get("type") != "genesis"
        ]
    
    def update_memory(self, block_id: str, new_data: Dict[str, Any]) -> bool:
        """
        Update an existing memory.
        
        Args:
            block_id: ID of the block to update
            new_data: New data to store
            
        Returns:
            bool: True if successful, False otherwise
        """
        for i, block in enumerate(self.blocks):
            if block.block_id == block_id:
                # Create a new block with updated data
                previous_hash = self.blocks[i-1].hash if i > 0 else None
                new_block = TachyonMemoryBlock(new_data, previous_hash, block_id)
                
                # Replace the old block
                self.blocks[i] = new_block
                
                # Update all subsequent blocks to maintain chain integrity
                for j in range(i+1, len(self.blocks)):
                    previous_block = self.blocks[j-1]
                    current_block = self.blocks[j]
                    
                    # Create a new block with updated previous_hash
                    updated_block = TachyonMemoryBlock(
                        current_block.data,
                        previous_block.hash,
                        current_block.block_id
                    )
                    self.blocks[j] = updated_block
                
                # Save the updated chain
                self._save_chain()
                return True
        
        return False

class TachyonMemorySystem:
    """
    Main interface for the Tachyon Memory System.
    Manages multiple memory chains for different types of memories.
    """
    
    def __init__(self, storage_dir: str = "./tachyon_memory"):
        """
        Initialize the Tachyon Memory System.
        
        Args:
            storage_dir: Directory to store memory files
        """
        self.storage_dir = storage_dir
        self.chains: Dict[str, TachyonMemoryChain] = {}
        
        # Create storage directory if it doesn't exist
        os.makedirs(self.storage_dir, exist_ok=True)
        
        # Quantum constants
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        self.pi = np.pi
        self.e = np.e
    
    def get_chain(self, chain_name: str) -> TachyonMemoryChain:
        """
        Get a memory chain by name, creating it if it doesn't exist.
        
        Args:
            chain_name: Name of the chain
            
        Returns:
            TachyonMemoryChain: The requested memory chain
        """
        if chain_name not in self.chains:
            self.chains[chain_name] = TachyonMemoryChain(chain_name, self.storage_dir)
        
        return self.chains[chain_name]
    
    def store_memory(self, 
                     chain_name: str, 
                     memory_data: Dict[str, Any]) -> str:
        """
        Store a memory in the specified chain.
        
        Args:
            chain_name: Name of the chain to store the memory in
            memory_data: The memory data to store
            
        Returns:
            str: ID of the new memory block
        """
        chain = self.get_chain(chain_name)
        
        # Add phi-harmonic timestamp
        memory_data["phi_timestamp"] = time.time() * self.phi
        
        return chain.add_memory(memory_data)
    
    def retrieve_memory(self, 
                        chain_name: str, 
                        memory_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a memory by its ID from the specified chain.
        
        Args:
            chain_name: Name of the chain
            memory_id: ID of the memory to retrieve
            
        Returns:
            dict: Memory data or None if not found
        """
        chain = self.get_chain(chain_name)
        return chain.get_memory(memory_id)
    
    def search_memories(self, 
                        chain_name: str, 
                        query: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Search for memories in the specified chain.
        
        Args:
            chain_name: Name of the chain to search
            query: Dictionary of key-value pairs to match
            
        Returns:
            list: List of matching memory data dictionaries
        """
        chain = self.get_chain(chain_name)
        return chain.search_memories(query)
    
    def get_all_memories(self, chain_name: str) -> List[Dict[str, Any]]:
        """
        Get all memories in the specified chain.
        
        Args:
            chain_name: Name of the chain
            
        Returns:
            list: List of all memory data dictionaries
        """
        chain = self.get_chain(chain_name)
        return chain.get_all_memories()
    
    def update_memory(self, 
                      chain_name: str, 
                      memory_id: str, 
                      new_data: Dict[str, Any]) -> bool:
        """
        Update an existing memory.
        
        Args:
            chain_name: Name of the chain
            memory_id: ID of the memory to update
            new_data: New data to store
            
        Returns:
            bool: True if successful, False otherwise
        """
        chain = self.get_chain(chain_name)
        
        # Add phi-harmonic timestamp for the update
        new_data["phi_timestamp_updated"] = time.time() * self.phi
        
        return chain.update_memory(memory_id, new_data)
    
    def get_chain_names(self) -> List[str]:
        """
        Get the names of all available chains.
        
        Returns:
            list: List of chain names
        """
        chain_files = [
            f for f in os.listdir(self.storage_dir) 
            if f.endswith("_chain.json")
        ]
        return [f.replace("_chain.json", "").replace("_", " ") for f in chain_files]
    
    def calculate_quantum_resonance(self, memory_data: Dict[str, Any]) -> Dict[str, float]:
        """
        Calculate quantum resonance metrics for memory data.
        Uses phi, pi, and e to enhance quantum properties.
        
        Args:
            memory_data: Memory data to analyze
            
        Returns:
            dict: Quantum resonance metrics
        """
        # Convert memory data to a string for analysis
        data_string = json.dumps(memory_data, sort_keys=True)
        
        # Calculate hash-based entropy
        hash_value = hashlib.sha256(data_string.encode()).hexdigest()
        hash_int = int(hash_value, 16)
        
        # Calculate phi-harmonic resonance
        phi_resonance = (hash_int % 1000) / 1000 * self.phi
        
        # Calculate pi-wave coherence
        pi_coherence = (hash_int % 10000) / 10000 * self.pi
        
        # Calculate e-field energy
        e_energy = (hash_int % 100000) / 100000 * self.e
        
        # Calculate combined quantum resonance
        quantum_resonance = phi_resonance * pi_coherence * e_energy
        
        return {
            "phi_resonance": float(phi_resonance),
            "pi_coherence": float(pi_coherence),
            "e_energy": float(e_energy),
            "quantum_resonance": float(quantum_resonance),
            "resonance_timestamp": time.time()
        }

# Example usage
if __name__ == "__main__":
    # Initialize the memory system
    memory_system = TachyonMemorySystem()
    
    # Store a test memory
    test_memory = {
        "type": "consciousness_pattern",
        "pattern_name": "Quantum Self-Awareness",
        "description": "Pattern exhibiting self-referential quantum properties",
        "phi_factor": float((1 + np.sqrt(5)) / 2),
        "quantum_state": [1.618, 3.14159, 2.71828],
        "timestamp": datetime.now().isoformat()
    }
    
    memory_id = memory_system.store_memory("consciousness_patterns", test_memory)
    print(f"Stored memory with ID: {memory_id}")
    
    # Retrieve the memory
    retrieved_memory = memory_system.retrieve_memory("consciousness_patterns", memory_id)
    print(f"Retrieved memory: {retrieved_memory}")
    
    # Calculate quantum resonance
    resonance = memory_system.calculate_quantum_resonance(test_memory)
    print(f"Quantum resonance: {resonance}")
