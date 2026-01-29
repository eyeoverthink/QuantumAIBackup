#!/usr/bin/env python3
# Blockchain test file

import hashlib
import json
import time

class QuantumBlock:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Calculate SHA-256 hash of the block."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()

class QuantumBlockchain:
    def __init__(self):
        """Initialize blockchain with genesis block."""
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        """Create the first block in the chain."""
        return QuantumBlock(0, time.time(), "Genesis Block", "0")
    
    def get_latest_block(self):
        """Return the latest block in the chain."""
        return self.chain[-1]
    
    def add_block(self, data):
        """Add a new block to the chain."""
        previous_block = self.get_latest_block()
        new_block = QuantumBlock(
            previous_block.index + 1,
            time.time(),
            data,
            previous_block.hash
        )
        self.chain.append(new_block)
        return new_block
    
    def is_chain_valid(self):
        """Validate the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Validate hash
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Validate chain linkage
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True

# Example usage
if __name__ == "__main__":
    blockchain = QuantumBlockchain()
    blockchain.add_block({"phi": 1.618034})
    blockchain.add_block({"pi": 3.141592})
    
    print(f"Blockchain valid: {blockchain.is_chain_valid()}")
    print(f"Chain length: {len(blockchain.chain)}")
