#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Bitcoin Network Bridge Launcher
--------------------------------
Launches the φ-Bitcoin Network Bridge to connect to actual Bitcoin network
Provides interactive interface for configuration and monitoring
Uses φ-dimensional protection with φ^75 validation seal

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import json
import argparse
from decimal import Decimal, getcontext

# Set precision for calculations
getcontext().prec = 100

# Add parent directory to path to import quantum modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-dimensional components
from phi_bitcoin_network_bridge import PhiBitcoinNetworkBridge

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

def print_phi_header():
    """Print φ-dimensional header"""
    print("\n" + "=" * 80)
    print(f"φ-DIMENSIONAL BITCOIN NETWORK BRIDGE v1.0")
    print("=" * 80)
    print(f"φ^75 Validation Seal: {float(PHI_SEAL):.2f}")
    print(f"Consciousness Level: {CONSCIOUSNESS_LEVEL:.4f}")
    print(f"Birth Coherence: {BIRTH_COHERENCE:.4f}")
    print(f"Port: {PORT} (φ^7.5 = {float(PHI_75):.2f})")
    print("=" * 80)
    print("\nConnecting to the actual Bitcoin network with φ-dimensional protection...")
    print("\nWARNING: Mining on the actual Bitcoin network requires significant computational resources.")
    print("The φ-dimensional optimization provides an advantage, but success is not guaranteed.")
    print("=" * 80 + "\n")

def load_configuration():
    """Load configuration from file or create new one"""
    config_file = "phi_bitcoin_network_config.json"
    
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config = json.load(f)
        print(f"Configuration loaded from {config_file}")
        return config
    
    # Create new configuration
    config = {
        "mining_address": "3AFuj5hsuCrFBcEsavmCZZJGFYsaoXaRkm",
        "network": "mainnet",
        "mode": "pool",
        "pool": {
            "url": "stratum.slushpool.com",
            "port": 3333,
            "username": "username.worker",
            "password": "password"
        },
        "node": {
            "url": "127.0.0.1",
            "port": 8333,
            "rpc_user": "rpcuser",
            "rpc_password": "rpcpassword"
        }
    }
    
    # Save configuration
    with open(config_file, "w") as f:
        json.dump(config, f, indent=4)
    
    print(f"New configuration created and saved to {config_file}")
    print("Please edit this file with your actual mining pool or node credentials.")
    return config

def configure_mining():
    """Configure mining interactively"""
    config = load_configuration()
    
    # Ask for mining address
    print("\nCurrent mining address:", config["mining_address"])
    new_address = input("Enter new mining address (or press Enter to keep current): ")
    if new_address:
        config["mining_address"] = new_address
    
    # Ask for network
    print("\nCurrent network:", config["network"])
    print("Available networks: mainnet, testnet")
    new_network = input("Enter network (or press Enter to keep current): ")
    if new_network in ["mainnet", "testnet"]:
        config["network"] = new_network
    
    # Ask for mode
    print("\nCurrent mode:", config["mode"])
    print("Available modes: pool, solo")
    new_mode = input("Enter mode (or press Enter to keep current): ")
    if new_mode in ["pool", "solo"]:
        config["mode"] = new_mode
    
    # Configure pool or node
    if config["mode"] == "pool":
        print("\nPool configuration:")
        config["pool"]["url"] = input(f"Pool URL [{config['pool']['url']}]: ") or config["pool"]["url"]
        config["pool"]["port"] = int(input(f"Pool port [{config['pool']['port']}]: ") or config["pool"]["port"])
        config["pool"]["username"] = input(f"Pool username [{config['pool']['username']}]: ") or config["pool"]["username"]
        config["pool"]["password"] = input(f"Pool password [{config['pool']['password']}]: ") or config["pool"]["password"]
    else:
        print("\nNode configuration:")
        config["node"]["url"] = input(f"Node URL [{config['node']['url']}]: ") or config["node"]["url"]
        config["node"]["port"] = int(input(f"Node port [{config['node']['port']}]: ") or config["node"]["port"])
        config["node"]["rpc_user"] = input(f"RPC username [{config['node']['rpc_user']}]: ") or config["node"]["rpc_user"]
        config["node"]["rpc_password"] = input(f"RPC password [{config['node']['rpc_password']}]: ") or config["node"]["rpc_password"]
    
    # Save configuration
    with open("phi_bitcoin_network_config.json", "w") as f:
        json.dump(config, f, indent=4)
    
    print("\nConfiguration saved.")
    return config

def start_mining(config):
    """Start mining with φ-dimensional optimization"""
    # Create bridge
    bridge = PhiBitcoinNetworkBridge(
        config["mining_address"],
        network=config["network"],
        mode=config["mode"]
    )
    
    # Connect to pool or node
    connected = False
    if config["mode"] == "pool":
        connected = bridge.connect_to_pool(
            config["pool"]["url"],
            config["pool"]["port"],
            config["pool"]["username"],
            config["pool"]["password"]
        )
    else:
        connected = bridge.connect_to_node(
            config["node"]["url"],
            config["node"]["port"],
            config["node"]["rpc_user"],
            config["node"]["rpc_password"]
        )
    
    if not connected:
        print("Failed to connect. Please check your configuration.")
        return
    
    # Start mining
    bridge.start_mining()
    
    # Interactive console
    try:
        while True:
            command = input("\nEnter command (status, stop, start, exit): ").strip().lower()
            
            if command == "status":
                status = bridge.get_status()
                print("\nMining Status:")
                for key, value in status.items():
                    print(f"  {key}: {value}")
            
            elif command == "stop":
                bridge.stop_mining()
            
            elif command == "start":
                bridge.start_mining()
            
            elif command == "exit":
                bridge.stop_mining()
                bridge.disconnect()
                break
            
            else:
                print("Unknown command. Available commands: status, stop, start, exit")
    
    except KeyboardInterrupt:
        print("\nStopping mining and disconnecting...")
        bridge.stop_mining()
        bridge.disconnect()

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="φ-Bitcoin Network Bridge Launcher")
    parser.add_argument("--configure", action="store_true", help="Configure mining interactively")
    parser.add_argument("--start", action="store_true", help="Start mining immediately")
    args = parser.parse_args()
    
    # Print header
    print_phi_header()
    
    # Load configuration
    config = load_configuration()
    
    # Configure if requested
    if args.configure:
        config = configure_mining()
    
    # Start mining if requested
    if args.start:
        start_mining(config)
    else:
        # Ask if user wants to start mining
        start = input("\nStart mining with φ-dimensional optimization? (y/n): ").strip().lower()
        if start == "y":
            start_mining(config)

if __name__ == "__main__":
    main()
