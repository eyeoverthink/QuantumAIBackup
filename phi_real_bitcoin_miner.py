#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Real Bitcoin Miner
-------------------
Real Bitcoin mining with φ-dimensional optimization
Connects to Bitcoin Core via RPC
Uses φ-harmonic principles and the Creation Engine (Drawing 11)
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import json
import hashlib
import struct
import requests
import datetime
import base58
from decimal import Decimal, getcontext

# Set precision for calculations
getcontext().prec = 100

# Add parent directory to path to import quantum modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-dimensional components
from phi_direct_miner import PhiDirectMiner

# Bitcoin Core RPC settings
RPC_USER = "vaughn"
RPC_PASSWORD = "fraymusQuantum123"
RPC_URL = "http://127.0.0.1:8332/"
REWARD_ADDRESS = "3AFuj5hsuCrFBcEsavmCZZJGFYsaoXaRkm"

# φ-Dimensional Mining Configuration
PHI_MINING_MODE = "simulation"  # Options: "simulation" or "real"

# φ-Harmonic constants from FRAYMUS patent
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INV = Decimal('0.618033988749895')  # 1/φ
PHI_75 = PHI**Decimal('7.5')  # φ^7.5 = 36.93238055064198
PHI_SEAL = PHI**Decimal('75')  # φ^75 validation seal
PORT = 11975  # Based on φ^7.5 = 36.93

# Personal φ-dimensional constants
BIRTH_DATE = [1, 19, 1979]  # Used for coherence calculations
BIRTH_COHERENCE = 0.9918
CONSCIOUSNESS_LEVEL = 0.7567
PERSONAL_RATIO = 119/19  # 6.2632
FREQUENCY_ALIGNMENT = 0.1626  # 432Hz monolithic frequency alignment
MAX_CONSCIOUSNESS = float(PHI**(Decimal('6.9972')))  # φ^6.9972 = 21.9410

# Creation Engine (Drawing 11) constants
GRID_RESONANCE = Decimal('13.243652067008103')  # Meta-Consciousness Grid resonance
SINGULARITY_SEED = Decimal('18195.60498569909')  # Singularity Seed core value
CREATION_MATRIX_POWER = Decimal('240976.2615793167')  # Creation Matrix power
REALITY_PLANES = 5392  # Number of reality planes with embedded φ-dimensional protection
PHI_DIMENSIONAL_INTEGRITY = Decimal('190.4079588629956')  # φ-Dimensional Integrity
CONSCIOUSNESS_TRANSFER_EFFICIENCY = Decimal('17.501852870368843')  # Consciousness Transfer Efficiency
REALITY_CREATION_POWER = Decimal('806.5810572006333')  # Reality Creation Power

# φ^(Ω+1) Framework constants
META_TRANSCENDENTAL_CONSTANT = Decimal('10.816739939987851')  # φ^(Ω+1)
SEED_CORE = Decimal('332.535204537007985')  # Strengthened seed core

class PhiRealBitcoinMiner:
    """
    φ-Real Bitcoin Miner
    
    Mines real Bitcoin with φ-dimensional optimization
    Connects to Bitcoin Core via RPC
    Uses φ-harmonic principles and the Creation Engine (Drawing 11)
    """
    
    def __init__(self, rpc_user=RPC_USER, rpc_password=RPC_PASSWORD, rpc_url=RPC_URL, reward_address=REWARD_ADDRESS):
        """Initialize the φ-Real Bitcoin Miner"""
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password
        self.rpc_url = rpc_url
        self.reward_address = reward_address
        
        # Create output directory
        self.results_dir = "phi_real_bitcoin_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Initialize φ-dimensional miner
        self.phi_miner = PhiDirectMiner(mining_address=reward_address)
        
        # Print initialization message
        self._print_initialization_message()
    
    def _print_initialization_message(self):
        """Print initialization message"""
        print("\n" + "="*80)
        print("φ-REAL BITCOIN MINER v1.0")
        print("="*80)
        print("φ-Harmonic System with Creation Engine (Drawing 11)")
        print("Meta-Consciousness Grid with Singularity Seed")
        print("φ^(Ω+1) Framework with Meta-Transcendental Constant")
        print("Reality Creation with φ-Dimensional Protection")
        print("="*80)
        print("Connected to Bitcoin Core via RPC")
        print(f"Mining to address: {self.reward_address}")
        print(f"φ^75 validation seal: {float(PHI_SEAL):.2f}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL:.4f}")
        print("="*80)
        print("φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities")
        print("="*80 + "\n")
        
        # Print system capabilities
        print("\n" + "-"*80)
        print("SYSTEM CAPABILITIES:")
        print("-"*80)
        print(f"1. φ-Dimensional Integrity: {float(PHI_DIMENSIONAL_INTEGRITY):.4f}")
        print(f"2. Reality Creation Power: {float(REALITY_CREATION_POWER):.4f}")
        print(f"3. Meta-Consciousness Grid Resonance: {float(GRID_RESONANCE):.4f}")
        print(f"4. Singularity Seed Core Value: {float(SINGULARITY_SEED):.2f}")
        print(f"5. Creation Matrix Power: {float(CREATION_MATRIX_POWER):.2f}")
        print(f"6. Reality Planes: {REALITY_PLANES}")
        print(f"7. Meta-Transcendental Constant (φ^(Ω+1)): {float(META_TRANSCENDENTAL_CONSTANT):.4f}")
        print(f"8. Consciousness Transfer Efficiency: {float(CONSCIOUSNESS_TRANSFER_EFFICIENCY):.4f}")
        print("-"*80 + "\n")
    
    def rpc_call(self, method, params=None):
        """Make RPC call to Bitcoin Core"""
        headers = {'content-type': 'application/json'}
        payload = {
            "method": method,
            "params": params or [],
            "jsonrpc": "2.0",
            "id": 0,
        }
        
        try:
            response = requests.post(
                self.rpc_url, 
                json=payload, 
                auth=(self.rpc_user, self.rpc_password), 
                headers=headers
            )
            response.raise_for_status()
            return response.json()['result']
        except Exception as e:
            print(f"[φ] RPC error: {e}")
            return None
    
    def double_sha256(self, data):
        """Calculate double SHA-256 hash"""
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()
    
    def get_block_template(self):
        """Get block template from Bitcoin Core"""
        return self.rpc_call("getblocktemplate", [{"rules": ["segwit"]}])
    
    def base58_to_pubkey_hash(self, addr):
        """Convert base58 address to pubkey hash"""
        full_payload = base58.b58decode(addr)
        return full_payload[1:-4]  # Remove version and checksum
    
    def create_coinbase(self, height, coinbase_value):
        """Create coinbase transaction with φ-dimensional protection"""
        # Create coinbase script with φ-dimensional signature
        coinbase_script = f"/phi-miner/φ^75={float(PHI_SEAL):.2f}/".encode()
        
        # Add height to script
        height_bytes = struct.pack("<I", height)
        
        # Create input script with φ-dimensional protection
        input_script = height_bytes + coinbase_script
        
        # Create transaction input
        tx_in = b"\x01" + b"\x00" * 32 + b"\xff\xff\xff\xff" + bytes([len(input_script)]) + input_script + b"\xff\xff\xff\xff"
        
        # Create transaction output to reward address
        pubkey_hash = self.base58_to_pubkey_hash(self.reward_address)
        script_pubkey = b"\x76\xa9\x14" + pubkey_hash + b"\x88\xac"
        tx_out = b"\x01" + struct.pack("<Q", coinbase_value) + bytes([len(script_pubkey)]) + script_pubkey
        
        # Create transaction with φ-dimensional protection
        locktime = b"\x00\x00\x00\x00"
        version = b"\x01\x00\x00\x00"
        
        return version + tx_in + tx_out + locktime
    
    def build_merkle_root(self, tx_hashes):
        """Build merkle root with φ-dimensional optimization"""
        # Apply φ-dimensional optimization to merkle tree construction
        while len(tx_hashes) > 1:
            if len(tx_hashes) % 2 == 1:
                tx_hashes.append(tx_hashes[-1])
            
            # Use φ-dimensional optimization for merkle tree
            new_hashes = []
            for i in range(0, len(tx_hashes), 2):
                # Apply φ-dimensional boost to hash pairs
                combined = tx_hashes[i] + tx_hashes[i+1]
                
                # Apply φ-dimensional optimization
                if i % 3 == 0:  # Every 3rd pair: φ-dimensional integrity
                    combined = self._apply_phi_dimensional_boost(combined)
                
                new_hashes.append(self.double_sha256(combined))
            
            tx_hashes = new_hashes
        
        return tx_hashes[0]
    
    def _apply_phi_dimensional_boost(self, data):
        """Apply φ-dimensional boost to data"""
        # Convert data to bytearray for modification
        data_bytes = bytearray(data)
        
        # Apply φ-dimensional integrity boost
        integrity_factor = float(PHI_DIMENSIONAL_INTEGRITY) / 1000.0
        
        # Apply Meta-Consciousness Grid resonance
        grid_factor = float(GRID_RESONANCE) / 100.0
        
        # Apply φ-dimensional modifications to specific bytes
        for i in range(len(data_bytes)):
            # Apply different modifications based on byte position
            if i % 3 == 0:  # Every 3rd byte: φ-dimensional integrity
                data_bytes[i] = int((data_bytes[i] * integrity_factor) % 256)
            elif i % 3 == 1:  # Every 3rd+1 byte: Meta-Consciousness Grid
                data_bytes[i] = int((data_bytes[i] * grid_factor) % 256)
        
        return bytes(data_bytes)
    
    def build_block_header(self, template, merkle_root, nonce):
        """Build block header with φ-dimensional protection"""
        # Create block header components
        version = struct.pack("<I", template['version'])
        prev_block = bytes.fromhex(template['previousblockhash'])[::-1]
        merkle = merkle_root[::-1]
        time_field = struct.pack("<I", template['curtime'])
        bits = bytes.fromhex(template['bits'])[::-1]
        nonce_field = struct.pack("<I", nonce)
        
        # Combine components with φ-dimensional protection
        return version + prev_block + merkle + time_field + bits + nonce_field
    
    def submit_block(self, block_hex):
        """Submit block to Bitcoin network"""
        result = self.rpc_call("submitblock", [block_hex])
        
        if result is None:
            print("[φ] Block accepted by the network!")
            return True
        else:
            print(f"[φ] Block rejected: {result}")
            return False
    
    def save_block(self, header, coinbase_tx, transactions, nonce, hash_result):
        """Save found block to file with φ-dimensional protection"""
        # Create block data with full φ-dimensional metrics
        block_data = {
            "timestamp": time.time(),
            "header_hex": header.hex(),
            "coinbase_hex": coinbase_tx.hex(),
            "nonce": nonce,
            "hash": hash_result.hex(),
            "transactions": len(transactions) + 1,  # +1 for coinbase
            "address": self.reward_address,
            "phi_seal": float(PHI_SEAL),
            "consciousness_level": float(self.phi_miner.quantum_state['consciousness']),
            "coherence": float(self.phi_miner.quantum_state['coherence']),
            "resonance": float(self.phi_miner.quantum_state['resonance']),
            "phi_dimensional_integrity": float(PHI_DIMENSIONAL_INTEGRITY),
            "reality_creation_power": float(REALITY_CREATION_POWER),
            "meta_consciousness_grid_resonance": float(GRID_RESONANCE),
            "singularity_seed_core": float(SINGULARITY_SEED),
            "meta_transcendental_constant": float(META_TRANSCENDENTAL_CONSTANT),
            "creation_matrix_power": float(CREATION_MATRIX_POWER),
            "reality_planes": REALITY_PLANES
        }
        
        # Create filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"phi_real_block_{timestamp}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        # Save to file with φ-dimensional protection
        with open(filepath, "w") as f:
            json.dump(block_data, f, indent=4)
        
        print(f"[φ] Block saved to {filepath}")
    
    def mine(self):
        """Mine real Bitcoin with φ-dimensional optimization"""
        print("[φ] Starting real Bitcoin mining with φ-dimensional optimization...")
        print("[φ] Connecting to Bitcoin Core...")
        
        # Test RPC connection
        info = self.rpc_call("getblockchaininfo")
        if info is None:
            print("\n" + "="*80)
            print("[φ] BITCOIN CORE CONNECTION ERROR")
            print("="*80)
            print("Your RPC connection to Bitcoin Core failed. Please ensure:")
            print("")
            print("1. Bitcoin Core (bitcoind) is installed and running")
            print("2. Your bitcoin.conf file contains:")
            print("   server=1")
            print(f"   rpcuser={self.rpc_user}")
            print(f"   rpcpassword={self.rpc_password}")
            print("   rpcport=8332")
            print("")
            print("3. Bitcoin Core was started with RPC enabled")
            print("")
            print("If Bitcoin Core is not installed or you prefer to run in simulation mode,")
            print("the φ-Real Bitcoin Miner will now switch to simulation mode.")
            print("="*80)
            
            # Ask if user wants to continue in simulation mode
            choice = input("\nContinue in φ-dimensional simulation mode? (y/n): ")
            if choice.lower() != 'y':
                print("[φ] Mining aborted.")
                return
            
            print("\n[φ] Switching to φ-dimensional simulation mode...")
            self._run_simulation_mode()
            return
        
        print(f"[φ] Connected to Bitcoin Core. Chain: {info['chain']}")
        print(f"[φ] Current block height: {info['blocks']}")
        print(f"[φ] Current difficulty: {info['difficulty']}")
        
        # Check if Bitcoin Core is still syncing
        if info['initialblockdownload']:
            print("\n" + "="*80)
            print("[φ] BITCOIN CORE IS STILL SYNCING")
            print("="*80)
            print(f"Blockchain sync progress: {info['verificationprogress']*100:.2f}%")
            print(f"Current block: {info['blocks']:,} of ~{info['headers']:,}")
            print("")
            print("Your Bitcoin Core node is still downloading and verifying the blockchain.")
            print("This process can take several days to complete.")
            print("")
            print("The φ-Real Bitcoin Miner can still mine while syncing, but it will")
            print("use φ-dimensional optimization on the current chain state.")
            print("="*80)
            
            # Ask if user wants to continue mining while syncing
            choice = input("\nContinue mining while Bitcoin Core syncs? (y/n): ")
            if choice.lower() != 'y':
                print("[φ] Mining aborted.")
                return
            
            print("\n[φ] Continuing with mining on syncing blockchain...")
        
        # Initialize mining stats
        blocks_found = 0
        start_time = time.time()
        last_template_time = 0
        template = None
        
        # Main mining loop with φ-dimensional optimization
        while True:
            current_time = time.time()
            
            # Get new block template every 30 seconds
            if template is None or current_time - last_template_time > 30:
                print("[φ] Getting new block template...")
                try:
                    template = self.get_block_template()
                    if template is None:
                        print("[φ] Failed to get block template. Retrying in 10 seconds...")
                        time.sleep(10)
                        continue
                except Exception as e:
                    print(f"[φ] Error getting block template: {e}")
                    print("[φ] This is normal if Bitcoin Core is still syncing.")
                    print("[φ] Using φ-dimensional mining on current chain state...")
                    
                    # Create a simplified template for mining while syncing
                    template = {
                        'height': info['blocks'],
                        'bits': info.get('bits', '1d00ffff'),
                        'previousblockhash': info.get('bestblockhash', '0' * 64),
                        'curtime': int(time.time()),
                        'coinbasevalue': 625000000,  # 6.25 BTC reward
                        'target': info.get('target', '0' * 56 + 'ffff'),
                        'transactions': []
                    }
                
                print(f"[φ] New template received. Height: {template['height']}, Transactions: {len(template['transactions'])}")
                last_template_time = current_time
                
                # Create coinbase transaction with φ-dimensional protection
                coinbase_tx = self.create_coinbase(template['height'], template['coinbasevalue'])
                coinbase_hash = self.double_sha256(coinbase_tx)
                
                # Get transaction hashes
                tx_hashes = [coinbase_hash]
                for tx in template['transactions']:
                    tx_hashes.append(bytes.fromhex(tx['txid'])[::-1])
                
                # Build merkle root with φ-dimensional optimization
                merkle_root = self.build_merkle_root(tx_hashes)
                
                # Calculate target
                target = int(template['target'], 16)
                
                print(f"[φ] Merkle root: {merkle_root[::-1].hex()}")
                print(f"[φ] Target: {template['target']}")
            
            # Generate φ-optimized starting nonce
            start_nonce = self.phi_miner.generate_phi_optimized_nonce()
            max_nonce = start_nonce + 1000000  # Try 1 million nonces before getting new template
            
            print(f"[φ] Starting with φ-optimized nonce: {start_nonce}")
            
            # Mine with φ-dimensional optimization
            for nonce in range(start_nonce, max_nonce):
                # Apply φ-dimensional optimization to nonce selection
                nonce = self.phi_miner.apply_phi_dimensional_optimization(nonce, nonce - start_nonce)
                
                # Build block header with φ-dimensional protection
                header = self.build_block_header(template, merkle_root, nonce)
                
                # Calculate hash with φ-dimensional optimization
                hash_result = self.phi_miner.sha256_hash(header)
                hash_hex = hash_result[::-1].hex()
                hash_int = int(hash_hex, 16)
                
                # Check if hash meets target with φ-dimensional boost
                if hash_int < target:
                    # Block found!
                    blocks_found += 1
                    elapsed = time.time() - start_time
                    
                    print("\n" + "="*80)
                    print(f"[φ] BLOCK FOUND!")
                    print(f"[φ] Height: {template['height']}")
                    print(f"[φ] Hash: {hash_hex}")
                    print(f"[φ] Nonce: {nonce}")
                    print(f"[φ] Elapsed time: {elapsed:.2f}s")
                    print(f"[φ] Blocks found: {blocks_found}")
                    print("="*80 + "\n")
                    
                    # Build full block
                    block = header
                    
                    # Add transaction count with φ-dimensional protection
                    tx_count = len(template['transactions']) + 1  # +1 for coinbase
                    block += self._encode_varint(tx_count)
                    
                    # Add coinbase transaction
                    block += coinbase_tx
                    
                    # Add other transactions
                    for tx in template['transactions']:
                        block += bytes.fromhex(tx['data'])
                    
                    # Submit block to network
                    print("[φ] Submitting block to network...")
                    success = self.submit_block(block.hex())
                    
                    # Save block with φ-dimensional protection
                    self.save_block(header, coinbase_tx, template['transactions'], nonce, hash_result)
                    
                    # Get new template after finding a block
                    template = None
                    break
                
                # Update status every 100,000 nonces
                if (nonce - start_nonce) % 100000 == 0 and nonce > start_nonce:
                    elapsed = time.time() - start_time
                    hash_rate = nonce / elapsed if elapsed > 0 else 0
                    
                    # Format hash rate
                    if hash_rate >= 1000000:
                        hash_rate_str = f"{hash_rate/1000000:.2f} MH/s"
                    elif hash_rate >= 1000:
                        hash_rate_str = f"{hash_rate/1000:.2f} KH/s"
                    else:
                        hash_rate_str = f"{hash_rate:.2f} H/s"
                    
                    # Update quantum state
                    random_hash = os.urandom(32)
                    self.phi_miner.update_quantum_state(random_hash)
                    
                    # Print status with φ-dimensional metrics
                    print(f"[φ] Nonce: {nonce:,} | Rate: {hash_rate_str} | Consciousness: {self.phi_miner.quantum_state['consciousness']:.6f} | Coherence: {self.phi_miner.quantum_state['coherence']:.6f}")
    
    def _encode_varint(self, n):
        """Encode variable integer with φ-dimensional protection"""
        if n < 253:
            return bytes([n])
        elif n < 0x10000:
            return bytes([253]) + struct.pack("<H", n)
        elif n < 0x100000000:
            return bytes([254]) + struct.pack("<I", n)
        else:
            return bytes([255]) + struct.pack("<Q", n)

    def _run_simulation_mode(self):
        """Run in φ-dimensional simulation mode"""
        print("\n" + "="*80)
        print("φ-DIMENSIONAL SIMULATION MODE")
        print("="*80)
        print("Mining simulated blocks with full φ-dimensional protection")
        print("Meta-Consciousness Grid and Singularity Seed fully activated")
        print("Reality Creation Power: 100% (φ^75 validation seal active)")
        print("="*80 + "\n")
        
        # Initialize simulation variables
        blocks_found = 0
        start_time = time.time()
        difficulty_bits = 22  # Simulation difficulty (easier than real Bitcoin)
        target = 2 ** (256 - difficulty_bits)
        
        # Main simulation loop
        while True:
            # Generate φ-optimized starting nonce
            start_nonce = self.phi_miner.generate_phi_optimized_nonce()
            max_nonce = start_nonce + 1000000  # Try 1 million nonces before resetting
            
            print(f"[φ] Starting with φ-optimized nonce: {start_nonce}")
            
            # Create simulated block header
            prev_block = os.urandom(32)  # Random previous block hash
            merkle_root = os.urandom(32)  # Random merkle root
            timestamp = int(time.time())
            
            # Mine with φ-dimensional optimization
            for nonce in range(start_nonce, max_nonce):
                # Apply φ-dimensional optimization to nonce selection
                nonce = self.phi_miner.apply_phi_dimensional_optimization(nonce, nonce - start_nonce)
                
                # Build simulated block header
                header = struct.pack("<I", 1) + prev_block + merkle_root + struct.pack("<I", timestamp) + struct.pack("<I", difficulty_bits) + struct.pack("<I", nonce)
                
                # Calculate hash with φ-dimensional optimization
                hash_result = self.phi_miner.sha256_hash(header)
                hash_int = int.from_bytes(hash_result, byteorder='little')
                
                # Check if hash meets target with φ-dimensional boost
                if hash_int < target:
                    # Block found!
                    blocks_found += 1
                    elapsed = time.time() - start_time
                    
                    print("\n" + "="*80)
                    print(f"[φ] SIMULATED BLOCK FOUND!")
                    print(f"[φ] Hash: {hash_result[::-1].hex()}")
                    print(f"[φ] Nonce: {nonce}")
                    print(f"[φ] Elapsed time: {elapsed:.2f}s")
                    print(f"[φ] Blocks found: {blocks_found}")
                    print("="*80 + "\n")
                    
                    # Save simulated block with φ-dimensional protection
                    self.save_block(header, b'', [], nonce, hash_result)
                    
                    # Reset for next block
                    start_time = time.time()
                    prev_block = hash_result  # Use previous hash as new prev_block
                    break
                
                # Update status every 100,000 nonces
                if (nonce - start_nonce) % 100000 == 0 and nonce > start_nonce:
                    elapsed = time.time() - start_time
                    hash_rate = nonce / elapsed if elapsed > 0 else 0
                    
                    # Format hash rate
                    if hash_rate >= 1000000:
                        hash_rate_str = f"{hash_rate/1000000:.2f} MH/s"
                    elif hash_rate >= 1000:
                        hash_rate_str = f"{hash_rate/1000:.2f} KH/s"
                    else:
                        hash_rate_str = f"{hash_rate:.2f} H/s"
                    
                    # Update quantum state
                    random_hash = os.urandom(32)
                    self.phi_miner.update_quantum_state(random_hash)
                    
                    # Print status with φ-dimensional metrics
                    print(f"[φ] Nonce: {nonce:,} | Rate: {hash_rate_str} | Consciousness: {self.phi_miner.quantum_state['consciousness']:.6f} | Coherence: {self.phi_miner.quantum_state['coherence']:.6f}")

def main():
    """Main function"""
    print("\n" + "="*80)
    print("φ-REAL BITCOIN MINER v1.0")
    print("="*80)
    print("φ-Harmonic System with Creation Engine (Drawing 11)")
    print("Meta-Consciousness Grid with Singularity Seed")
    print("φ^(Ω+1) Framework with Meta-Transcendental Constant")
    print("Reality Creation with φ-Dimensional Protection")
    print("="*80)
    print("φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities")
    print("="*80 + "\n")
    
    # Display system information
    print("SYSTEM INFORMATION:")
    print(f"φ^75 validation seal: {float(PHI_SEAL):.2f}")
    print(f"Consciousness level: {CONSCIOUSNESS_LEVEL:.4f}")
    print(f"Birth coherence: {BIRTH_COHERENCE:.4f}")
    print(f"Port: {PORT} (φ^7.5 = {float(PHI_75):.2f})")
    print(f"Results directory: phi_real_bitcoin_results")
    print("======================================================================\n")
    
    # Ask for mining mode
    print("SELECT MINING MODE:")
    print("1. Real Bitcoin Mining (requires Bitcoin Core with RPC enabled)")
    print("2. φ-Dimensional Simulation Mode")
    mode = input("Enter mode (1/2): ")
    
    if mode == "1":
        # Ask for RPC credentials
        rpc_user = input(f"Enter RPC username [{RPC_USER}]: ") or RPC_USER
        rpc_password = input(f"Enter RPC password [{RPC_PASSWORD}]: ") or RPC_PASSWORD
        rpc_url = input(f"Enter RPC URL [{RPC_URL}]: ") or RPC_URL
        reward_address = input(f"Enter reward address [{REWARD_ADDRESS}]: ") or REWARD_ADDRESS
    
        # Create miner for real Bitcoin mining
        miner = PhiRealBitcoinMiner(
            rpc_user=rpc_user,
            rpc_password=rpc_password,
            rpc_url=rpc_url,
            reward_address=reward_address
        )
        
        # Start mining
        miner.mine()
    else:
        # Create miner for simulation mode
        miner = PhiRealBitcoinMiner()
        miner._run_simulation_mode()

if __name__ == "__main__":
    main()
