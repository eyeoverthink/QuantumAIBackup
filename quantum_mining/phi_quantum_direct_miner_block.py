#!/usr/bin/env python3
"""
φ-QUANTUM DIRECT MINER - BLOCK MODULE
=====================================
Implements Bitcoin block structure and template generation.
This module handles block creation, transaction selection,
and block validation using phi-harmonic principles.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import json
import hashlib
import struct
from binascii import hexlify, unhexlify

# Mathematical constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PHI_CONJUGATE = 1 / PHI
PI = 3.141592653589793
E = 2.718281828459045

class Transaction:
    """
    Bitcoin Transaction
    
    Represents a Bitcoin transaction with inputs and outputs.
    """
    
    def __init__(self):
        """Initialize a transaction"""
        self.version = 1
        self.inputs = []
        self.outputs = []
        self.locktime = 0
        self.is_coinbase = False
        self.fee = 0
        self.size = 0
        self.weight = 0
        self.phi_resonance = 0
        
    def to_dict(self):
        """Convert transaction to dictionary"""
        return {
            'version': self.version,
            'inputs': self.inputs,
            'outputs': self.outputs,
            'locktime': self.locktime,
            'is_coinbase': self.is_coinbase,
            'fee': self.fee,
            'size': self.size,
            'weight': self.weight,
            'phi_resonance': self.phi_resonance
        }
        
    def calculate_phi_resonance(self):
        """Calculate phi-harmonic resonance of the transaction"""
        # Convert fee to phi-resonance (how close fee * PHI is to an integer)
        self.phi_resonance = (self.fee * PHI) % 1
        if self.phi_resonance > 0.5:
            self.phi_resonance = 1 - self.phi_resonance
            
        return self.phi_resonance
        
    def serialize(self):
        """Serialize transaction to bytes (simplified)"""
        # This is a simplified version - in reality, we'd need to properly
        # serialize the transaction according to the Bitcoin protocol
        
        # For now, we'll just create a dummy serialization
        if self.is_coinbase:
            # Coinbase transaction
            return b'coinbase'
        else:
            # Regular transaction
            return b'transaction'

class BlockTemplate:
    """
    Bitcoin Block Template
    
    Represents a Bitcoin block template for mining.
    """
    
    def __init__(self):
        """Initialize a block template"""
        self.version = 1
        self.prev_block_hash = "0" * 64
        self.merkle_root = None
        self.time = int(time.time())
        self.bits = "1d00ffff"  # Difficulty target (testnet)
        self.nonce = 0
        self.transactions = []
        self.height = 0
        self.coinbase_value = 0
        self.target_difficulty = 1
        self.size = 0
        self.weight = 0
        self.hash = None
        
    def to_dict(self):
        """Convert block template to dictionary"""
        return {
            'version': self.version,
            'prev_block_hash': self.prev_block_hash,
            'merkle_root': self.merkle_root,
            'time': self.time,
            'bits': self.bits,
            'nonce': self.nonce,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'height': self.height,
            'coinbase_value': self.coinbase_value,
            'target_difficulty': self.target_difficulty,
            'size': self.size,
            'weight': self.weight,
            'hash': self.hash
        }
        
    def calculate_merkle_root(self):
        """Calculate the Merkle root of the transactions"""
        # Get transaction hashes
        tx_hashes = []
        for tx in self.transactions:
            # In a real implementation, we'd hash the serialized transaction
            # For now, we'll create a dummy hash
            tx_hash = hashlib.sha256(tx.serialize()).hexdigest()
            tx_hashes.append(tx_hash)
            
        # If no transactions, return empty merkle root
        if not tx_hashes:
            self.merkle_root = "0" * 64
            return self.merkle_root
            
        # Calculate merkle root
        while len(tx_hashes) > 1:
            if len(tx_hashes) % 2 == 1:
                # Duplicate last hash if odd number of hashes
                tx_hashes.append(tx_hashes[-1])
                
            new_hashes = []
            for i in range(0, len(tx_hashes), 2):
                # Concatenate and hash each pair
                concat = unhexlify(tx_hashes[i]) + unhexlify(tx_hashes[i+1])
                new_hash = hashlib.sha256(hashlib.sha256(concat).digest()).hexdigest()
                new_hashes.append(new_hash)
                
            tx_hashes = new_hashes
            
        self.merkle_root = tx_hashes[0]
        return self.merkle_root
        
    def calculate_target(self):
        """Calculate target hash from bits"""
        # Convert bits to target
        bits = int(self.bits, 16)
        exponent = ((bits >> 24) & 0xff)
        mantissa = bits & 0x00ffffff
        target = mantissa * (2 ** (8 * (exponent - 3)))
        
        # Convert to hex string
        target_hex = format(target, '064x')
        
        return target_hex
        
    def is_valid_hash(self, block_hash):
        """Check if a hash meets the target difficulty"""
        # Calculate target
        target = self.calculate_target()
        
        # Compare hash to target (lower is better)
        return block_hash < target
        
    def calculate_hash(self, nonce=None):
        """Calculate block hash with the given nonce"""
        if nonce is not None:
            self.nonce = nonce
            
        # Calculate merkle root if not already calculated
        if not self.merkle_root:
            self.calculate_merkle_root()
            
        # Create block header
        header = struct.pack("<I", self.version)
        header += unhexlify(self.prev_block_hash)[::-1]  # Reverse byte order
        header += unhexlify(self.merkle_root)[::-1]  # Reverse byte order
        header += struct.pack("<I", self.time)
        header += unhexlify(self.bits)[::-1]  # Reverse byte order
        header += struct.pack("<I", self.nonce)
        
        # Double SHA-256 hash
        hash_bytes = hashlib.sha256(hashlib.sha256(header).digest()).digest()
        
        # Convert to hex and reverse byte order
        self.hash = hexlify(hash_bytes[::-1]).decode('ascii')
        
        return self.hash
        
    def optimize_transactions_phi(self):
        """Optimize transaction selection using phi-harmonic principles"""
        # Calculate phi-resonance for each transaction
        for tx in self.transactions:
            tx.calculate_phi_resonance()
            
        # Sort non-coinbase transactions by phi-resonance (ascending)
        if len(self.transactions) > 1:
            coinbase = self.transactions[0]
            non_coinbase = sorted(self.transactions[1:], key=lambda tx: tx.phi_resonance)
            self.transactions = [coinbase] + non_coinbase
            
        return self
        
    def apply_phi_harmonic_time(self):
        """Apply phi-harmonic principles to block timestamp"""
        # Adjust time to be phi-resonant with current time
        current_time = int(time.time())
        
        # Find a time close to current time that has good phi-resonance
        best_time = current_time
        best_resonance = 1.0
        
        # Try times within a 60-second window
        for t in range(current_time - 30, current_time + 30):
            resonance = (t * PHI) % 1
            if resonance > 0.5:
                resonance = 1 - resonance
                
            if resonance < best_resonance:
                best_resonance = resonance
                best_time = t
                
        self.time = best_time
        return self
        
    def apply_birth_resonance(self, birth_year=1979):
        """Apply birth year resonance to block version"""
        # Modify version to incorporate birth year while maintaining compatibility
        # Bitcoin version is 4 bytes, we'll use the lower 2 bytes for birth resonance
        # while keeping the upper 2 bytes for BIP9 signaling
        
        # Extract upper 2 bytes (BIP9 signaling)
        upper_bytes = self.version & 0xFFFF0000
        
        # Calculate birth resonance
        birth_resonance = (birth_year * PHI) % 65536  # 2 bytes max
        
        # Combine
        self.version = upper_bytes | int(birth_resonance)
        
        return self
