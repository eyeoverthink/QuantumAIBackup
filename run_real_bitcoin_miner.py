#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Real Bitcoin Miner Launcher
----------------------------
Automatically launches the φ-Real Bitcoin Miner in real mining mode
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
from phi_real_bitcoin_miner import PhiRealBitcoinMiner, RPC_USER, RPC_PASSWORD, RPC_URL, REWARD_ADDRESS

def main():
    """Launch the φ-Real Bitcoin Miner in real mining mode"""
    print("\n" + "="*80)
    print("φ-REAL BITCOIN MINER LAUNCHER")
    print("="*80)
    print("Automatically connecting to Bitcoin Core with φ-dimensional protection")
    print("Meta-Consciousness Grid and Singularity Seed fully activated")
    print("φ^75 validation seal: 4721424167835397.00")
    print("="*80 + "\n")
    
    # Create miner with default credentials
    miner = PhiRealBitcoinMiner(
        rpc_user=RPC_USER,
        rpc_password=RPC_PASSWORD,
        rpc_url=RPC_URL,
        reward_address=REWARD_ADDRESS
    )
    
    # Start mining
    miner.mine()

if __name__ == "__main__":
    main()
