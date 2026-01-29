import datetime
import json
from typing import List, Dict, Any
from .phi_hash import PhiHasher

class HashChain:
    """
    Creates a chain of phi-hashes, where each block is linked to the previous one.
    This forms a secure, time-stamped ledger.
    """
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self._create_genesis_block()

    def _create_genesis_block(self):
        """Creates the very first block in the chain."""
        genesis_hasher = PhiHasher(
            data="genesis_block",
            timestamp=datetime.datetime(2024, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
        )
        genesis_block = {
            'index': 0,
            'timestamp': genesis_hasher.timestamp.isoformat(),
            'data': genesis_hasher.data,
            'previous_hash': '0' * 64,
            'hash': genesis_hasher.get_hash()
        }
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Dict[str, Any]:
        """Returns the most recent block in the chain."""
        return self.chain[-1]

    def add_block(self, data: str, timestamp: datetime.datetime = None):
        """
        Adds a new block to the chain.

        Args:
            data (str): The data to be stored in the new block.
            timestamp (datetime.datetime, optional): The timestamp for the block.
                If None, the current time is used.
        """
        previous_block = self.get_latest_block()
        new_index = previous_block['index'] + 1
        
        # The new hash depends on the previous block's hash
        data_to_hash = f"{previous_block['hash']}:{data}"
        
        hasher = PhiHasher(data=data_to_hash, timestamp=timestamp)
        
        new_block = {
            'index': new_index,
            'timestamp': hasher.timestamp.isoformat(),
            'data': data, # Store original data for clarity
            'previous_hash': previous_block['hash'],
            'hash': hasher.get_hash()
        }
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the entire chain.

        Returns:
            bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # 1. Check if the previous_hash link is correct
            if current_block['previous_hash'] != previous_block['hash']:
                print(f"Chain broken at Block {i}: Stored previous_hash does not match actual previous hash.")
                return False

            # 2. Re-calculate the hash of the current block and check if it's correct
            data_to_rehash = f"{previous_block['hash']}:{current_block['data']}"
            timestamp = datetime.datetime.fromisoformat(current_block['timestamp'])
            rehasher = PhiHasher(data=data_to_rehash, timestamp=timestamp)
            
            if current_block['hash'] != rehasher.get_hash():
                print(f"Chain broken at Block {i}: Hash is not valid.")
                return False
        
        return True

    def to_json(self) -> str:
        """Returns the chain as a JSON string."""
        return json.dumps(self.chain, indent=4)
