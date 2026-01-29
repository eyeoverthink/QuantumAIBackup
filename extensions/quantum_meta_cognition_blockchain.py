"""
Quantum Meta-Cognition Blockchain Memory

This module enhances the Quantum Meta-Cognition persistent memory
with blockchain storage for immutability and distributed trust.

Created: 2025-07-22
Coherence: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import json
import time
import logging
import hashlib
from typing import Dict, List, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('QuantumMetaCognitionBlockchain')

# Import quantum components
# Define module-level variable
blockchain_available = False

try:
    # Import meta-cognition module
    from extensions.quantum_meta_cognition import QuantumMetaCognition
    
    # Try to import blockchain connector
    try:
        from quantum_blockchain_connector import QuantumBlockchainConnector
        blockchain_available = True
    except ImportError:
        logger.warning("Quantum blockchain connector not available, running with limited functionality")
        blockchain_available = False
        
except ImportError as e:
    logger.error(f"Error importing required components: {e}")
    sys.exit(1)

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio φ
PHI_7_5 = PHI ** 7.5    # φ⁷·⁵ ≈ 36.932381
MEMORY_BLOCK_SIZE = 10  # Number of memory entries per block


class BlockchainMemoryStorage:
    """Blockchain-based storage for meta-cognition memory."""
    
    def __init__(self, system_id: str = "quantum_meta_cognition"):
        """Initialize blockchain memory storage.
        
        Args:
            system_id: Unique identifier for this system
        """
        self.system_id = system_id
        self.memory_blocks = {}
        self.memory_index = {}
        self.last_block_hash = None
        self.pending_memories = []
        
        # Initialize blockchain connector if available
        if blockchain_available:
            try:
                self.blockchain = QuantumBlockchainConnector()
                logger.info(f"Blockchain connector initialized for system {system_id}")
                
                # Check for existing genesis block
                genesis = self.blockchain.get_genesis_block(system_id)
                if genesis:
                    self.last_block_hash = genesis["hash"]
                    logger.info(f"Found existing genesis block with hash {self.last_block_hash}")
                else:
                    # Create genesis block
                    genesis_data = {
                        "system_id": system_id,
                        "type": "meta_cognition_memory",
                        "created_at": time.time(),
                        "phi_resonance": (PHI * hash(system_id)) % 1.0
                    }
                    self.last_block_hash = self.blockchain.store_genesis_block(system_id, genesis_data)
                    logger.info(f"Created new genesis block with hash {self.last_block_hash}")
            except Exception as e:
                logger.error(f"Error initializing blockchain: {e}")
                self.blockchain = None
                blockchain_available = False
        else:
            self.blockchain = None
    
    def _generate_fingerprint(self, data: Any) -> str:
        """Generate a quantum fingerprint for data.
        
        Args:
            data: Data to generate fingerprint for
            
        Returns:
            Quantum fingerprint
        """
        data_hash = hashlib.md5(str(data).encode()).hexdigest()[:7]
        return f"φ⁷·⁵-{data_hash}"
    
    def store_memory(self, memory_type: str, memory_data: Dict[str, Any]) -> str:
        """Store a memory in blockchain.
        
        Args:
            memory_type: Type of memory
            memory_data: Memory data
            
        Returns:
            Memory fingerprint
        """
        # Generate fingerprint
        fingerprint = self._generate_fingerprint(memory_data)
        
        # Create memory entry
        memory_entry = {
            "type": memory_type,
            "data": memory_data,
            "fingerprint": fingerprint,
            "timestamp": time.time(),
            "phi_resonance": (PHI * hash(str(memory_data))) % 1.0
        }
        
        # Add to pending memories
        self.pending_memories.append(memory_entry)
        
        # Store in blockchain if enough pending memories
        if len(self.pending_memories) >= MEMORY_BLOCK_SIZE:
            self._store_memory_block()
        
        logger.info(f"Memory {fingerprint} of type {memory_type} added to pending block")
        return fingerprint
    
    def _store_memory_block(self) -> Optional[str]:
        """Store pending memories in a blockchain block.
        
        Returns:
            Block hash or None if failed
        """
        if not self.pending_memories:
            logger.warning("No pending memories to store in blockchain")
            return None
        
        if not blockchain_available or not self.blockchain:
            logger.warning("Blockchain not available, skipping block storage")
            self.pending_memories = []
            return None
        
        try:
            # Create block data
            block_data = {
                "system_id": self.system_id,
                "memories": self.pending_memories,
                "memory_count": len(self.pending_memories),
                "timestamp": time.time()
            }
            
            # Store block
            block_hash = self.blockchain.store_block(
                self.system_id, 
                block_data, 
                self.last_block_hash or "genesis"
            )
            
            # Update last block hash
            self.last_block_hash = block_hash
            
            # Store block in memory
            self.memory_blocks[block_hash] = block_data
            
            # Index memories
            for memory in self.pending_memories:
                self.memory_index[memory["fingerprint"]] = block_hash
            
            # Clear pending memories
            self.pending_memories = []
            
            logger.info(f"Stored memory block with hash {block_hash} containing {len(block_data['memories'])} memories")
            return block_hash
        
        except Exception as e:
            logger.error(f"Error storing memory block: {e}")
            return None
    
    def get_memory(self, fingerprint: str) -> Optional[Dict[str, Any]]:
        """Get a memory by fingerprint.
        
        Args:
            fingerprint: Memory fingerprint
            
        Returns:
            Memory data or None if not found
        """
        # Check pending memories first
        for memory in self.pending_memories:
            if memory["fingerprint"] == fingerprint:
                return memory
        
        # Check blockchain
        if fingerprint in self.memory_index:
            block_hash = self.memory_index[fingerprint]
            
            # Check local cache
            if block_hash in self.memory_blocks:
                block = self.memory_blocks[block_hash]
            # Retrieve from blockchain
            elif blockchain_available and self.blockchain:
                try:
                    block = self.blockchain.get_block(block_hash)
                    if block:
                        self.memory_blocks[block_hash] = block
                    else:
                        logger.error(f"Block {block_hash} not found in blockchain")
                        return None
                except Exception as e:
                    logger.error(f"Error retrieving block {block_hash}: {e}")
                    return None
            else:
                logger.error(f"Block {block_hash} not found and blockchain not available")
                return None
            
            # Find memory in block
            for memory in block["data"]["memories"]:
                if memory["fingerprint"] == fingerprint:
                    return memory
        
        logger.warning(f"Memory {fingerprint} not found")
        return None
    
    def get_memories_by_type(self, memory_type: str) -> List[Dict[str, Any]]:
        """Get memories by type.
        
        Args:
            memory_type: Type of memories to get
            
        Returns:
            List of matching memories
        """
        memories = []
        
        # Check pending memories
        for memory in self.pending_memories:
            if memory["type"] == memory_type:
                memories.append(memory)
        
        # Check blockchain blocks
        for block_hash, block in self.memory_blocks.items():
            for memory in block["data"]["memories"]:
                if memory["type"] == memory_type:
                    memories.append(memory)
        
        logger.info(f"Found {len(memories)} memories of type {memory_type}")
        return memories
    
    def verify_memory_integrity(self) -> Dict[str, Any]:
        """Verify the integrity of all memories in the blockchain.
        
        Returns:
            Dict containing verification results
        """
        if not blockchain_available or not self.blockchain:
            logger.warning("Blockchain not available, skipping memory verification")
            return {"verified": False, "reason": "Blockchain not available"}
        
        try:
            # Verify blockchain
            is_valid = self.blockchain.verify_blockchain(self.system_id)
            
            if not is_valid:
                logger.error(f"Blockchain verification failed for system {self.system_id}")
                return {"verified": False, "reason": "Blockchain verification failed"}
            
            # Force store any pending memories
            if self.pending_memories:
                self._store_memory_block()
            
            logger.info(f"Memory integrity verified for system {self.system_id}")
            return {
                "verified": True,
                "block_count": len(self.memory_blocks),
                "memory_count": len(self.memory_index)
            }
        
        except Exception as e:
            logger.error(f"Error verifying memory integrity: {e}")
            return {"verified": False, "reason": str(e)}


class BlockchainEnhancedMetaCognition(QuantumMetaCognition):
    """Enhanced meta-cognition with blockchain-based persistent memory."""
    
    def __init__(self, memory_path: str = "meta_cognition_memory.json"):
        """Initialize blockchain-enhanced meta-cognition.
        
        Args:
            memory_path: Path to memory file
        """
        # Initialize base meta-cognition
        super().__init__(memory_path)
        
        # Initialize blockchain memory storage
        self.blockchain_memory = BlockchainMemoryStorage()
        
        # Sync existing memories to blockchain
        self._sync_memories_to_blockchain()
        
        logger.info("Blockchain-enhanced meta-cognition initialized")
    
    def _sync_memories_to_blockchain(self):
        """Sync existing memories to blockchain."""
        sync_count = 0
        
        # Sync experiences
        for exp_type, experiences in self.memory.get("experiences", {}).items():
            for exp in experiences:
                self.blockchain_memory.store_memory("experience", {
                    "type": exp_type,
                    "data": exp["data"],
                    "fingerprint": exp["fingerprint"],
                    "timestamp": exp["timestamp"]
                })
                sync_count += 1
        
        # Sync reflections
        for reflection in self.memory.get("reflections", []):
            self.blockchain_memory.store_memory("reflection", reflection)
            sync_count += 1
        
        # Sync goals
        for goal in self.memory.get("goals", []):
            self.blockchain_memory.store_memory("goal", goal)
            sync_count += 1
        
        logger.info(f"Synced {sync_count} existing memories to blockchain")
    
    def store_experience(self, experience_type: str, data: Dict[str, Any]) -> str:
        """Store an experience in memory and blockchain.
        
        Args:
            experience_type: Type of experience
            data: Experience data
            
        Returns:
            Experience fingerprint
        """
        # Store in base memory
        fingerprint = super().store_experience(experience_type, data)
        
        # Store in blockchain
        self.blockchain_memory.store_memory("experience", {
            "type": experience_type,
            "data": data,
            "fingerprint": fingerprint,
            "timestamp": time.time()
        })
        
        return fingerprint
    
    def reflect(self) -> Dict[str, Any]:
        """Perform self-reflection and store in blockchain.
        
        Returns:
            Reflection results
        """
        # Perform base reflection
        reflection = super().reflect()
        
        # Store in blockchain
        self.blockchain_memory.store_memory("reflection", reflection)
        
        return reflection
    
    def form_goal(self) -> Dict[str, Any]:
        """Form a new goal and store in blockchain.
        
        Returns:
            Formed goal
        """
        # Form base goal
        goal = super().form_goal()
        
        # Store in blockchain
        self.blockchain_memory.store_memory("goal", goal)
        
        return goal
    
    def verify_memory_integrity(self) -> Dict[str, Any]:
        """Verify the integrity of all memories.
        
        Returns:
            Dict containing verification results
        """
        return self.blockchain_memory.verify_memory_integrity()
    
    def get_blockchain_memory_state(self) -> Dict[str, Any]:
        """Get the current state of blockchain memory.
        
        Returns:
            Dict containing memory state
        """
        # Count memories by type
        pending_count = len(self.blockchain_memory.pending_memories)
        
        type_counts = {}
        for memory in self.blockchain_memory.pending_memories:
            memory_type = memory["type"]
            if memory_type not in type_counts:
                type_counts[memory_type] = 0
            type_counts[memory_type] += 1
        
        for block_hash, block in self.blockchain_memory.memory_blocks.items():
            for memory in block["data"]["memories"]:
                memory_type = memory["type"]
                if memory_type not in type_counts:
                    type_counts[memory_type] = 0
                type_counts[memory_type] += 1
        
        return {
            "block_count": len(self.blockchain_memory.memory_blocks),
            "memory_count": len(self.blockchain_memory.memory_index) + pending_count,
            "pending_count": pending_count,
            "type_counts": type_counts
        }


def enhance_meta_cognition_with_blockchain(meta_cognition: QuantumMetaCognition) -> BlockchainEnhancedMetaCognition:
    """Enhance a meta-cognition instance with blockchain memory.
    
    Args:
        meta_cognition: Meta-cognition instance to enhance
        
    Returns:
        Blockchain-enhanced meta-cognition instance
    """
    # Create enhanced meta-cognition
    enhanced = BlockchainEnhancedMetaCognition(meta_cognition.memory_path)
    
    # Copy attributes from original meta-cognition
    enhanced.birth_date = meta_cognition.birth_date
    enhanced.birth_resonance = meta_cognition.birth_resonance
    enhanced.coherence = meta_cognition.coherence
    enhanced.phi_resonance = meta_cognition.phi_resonance
    
    # Copy memory from original meta-cognition
    enhanced.memory = meta_cognition.memory
    
    logger.info("Meta-cognition enhanced with blockchain memory")
    return enhanced


# Demonstration function
def demonstrate_blockchain_memory():
    """Demonstrate blockchain memory capabilities."""
    print("\n=== Quantum Meta-Cognition Blockchain Memory Demonstration ===")
    
    # Create meta-cognition instance
    print("\nCreating Quantum Meta-Cognition...")
    from extensions.quantum_meta_cognition import QuantumMetaCognition
    meta = QuantumMetaCognition()
    print(f"Meta-Cognition initialized with φ-coherence: {meta._calculate_coherence():.6f}")
    
    # Enhance with blockchain memory
    print("\nEnhancing Meta-Cognition with blockchain memory...")
    enhanced_meta = enhance_meta_cognition_with_blockchain(meta)
    print(f"Meta-Cognition enhanced with blockchain memory")
    
    # Store experiences
    print("\nStoring experiences in blockchain memory...")
    for i in range(5):
        experience_type = ["observation", "interaction", "learning"][i % 3]
        experience_data = {
            "content": f"Test experience {i+1}",
            "value": i * PHI,
            "timestamp": time.time()
        }
        fingerprint = enhanced_meta.store_experience(experience_type, experience_data)
        print(f"Stored {experience_type} experience with fingerprint: {fingerprint}")
    
    # Perform reflection
    print("\nPerforming reflection...")
    reflection = enhanced_meta.reflect()
    print(f"Reflection coherence: {reflection['coherence']:.6f}")
    
    # Form goal
    print("\nForming goal...")
    goal = enhanced_meta.form_goal()
    print(f"Goal: {goal['content']}")
    
    # Get blockchain memory state
    print("\nRetrieving blockchain memory state...")
    memory_state = enhanced_meta.get_blockchain_memory_state()
    print(f"Memory blocks: {memory_state['block_count']}")
    print(f"Total memories: {memory_state['memory_count']}")
    print(f"Pending memories: {memory_state['pending_count']}")
    
    # Verify memory integrity
    print("\nVerifying memory integrity...")
    verification = enhanced_meta.verify_memory_integrity()
    print(f"Memory integrity verified: {verification['verified']}")
    if verification['verified']:
        print(f"Verified {verification['memory_count']} memories in {verification['block_count']} blocks")
    else:
        print(f"Verification failed: {verification['reason']}")
    
    print("\nBlockchain Memory demonstration complete.")


if __name__ == "__main__":
    demonstrate_blockchain_memory()
