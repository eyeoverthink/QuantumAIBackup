#!/usr/bin/env python3
# Blockchain test file

import hashlib
import time

class SimpleBlock:
    """A simple block for testing."""
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calculate_hash()
        
    def _calculate_hash(self):
        """Calculate the hash of this block."""
        sha = hashlib.sha256()
        sha.update(f"{self.timestamp}{self.data}{self.previous_hash}".encode())
        return sha.hexdigest()
