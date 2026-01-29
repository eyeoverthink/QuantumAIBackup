# Time-Based Cryptographic Hashing Module

This module implements a novel cryptographic hashing system where the hash of a piece of data evolves over time, based on phi-harmonic principles.

## Core Components

- **`temporal_key.py`**: Generates a dynamic, time-sensitive key using the golden ratio (phi) and a timestamp. This key is the foundation of the evolving hash.

- **`phi_hash.py`**: The core hashing engine. It combines input data with a temporal key to produce a secure, time-dependent SHA-256 hash.

- **`hash_chain.py`**: Implements a chain of phi-hashes, where each hash is linked to the previous one, creating a secure, time-stamped ledger similar to a blockchain.
