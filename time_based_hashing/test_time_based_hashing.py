import time
import datetime
from time_based_hashing.phi_hash import PhiHasher
from time_based_hashing.hash_chain import HashChain

def run_hashing_test():
    """Demonstrates the Time-Based Cryptographic Hashing system."""
    print("--- Time-Based Hashing Test ---")

    # 1. Demonstrate time-sensitivity of a single hash
    print("\n--- 1. Time-Sensitivity Demo ---")
    data = "QuantumAI Project"
    hasher1 = PhiHasher(data)
    time.sleep(0.01) # Ensure a different timestamp
    hasher2 = PhiHasher(data)
    print(f"Data: '{data}'")
    print(f"Hash 1 ({hasher1.timestamp.isoformat()}): {hasher1.get_hash()}")
    print(f"Hash 2 ({hasher2.timestamp.isoformat()}): {hasher2.get_hash()}")
    print(f"Hashes are different: {hasher1.get_hash() != hasher2.get_hash()}")

    # 2. Create and validate a HashChain
    print("\n--- 2. HashChain Creation and Validation ---")
    chain = HashChain()
    chain.add_block("Transaction A: 10 QC")
    time.sleep(0.01)
    chain.add_block("Transaction B: 5 QC")
    time.sleep(0.01)
    chain.add_block("Transaction C: 12 QC")

    print("Generated HashChain:")
    print(chain.to_json())
    print(f"\nIs chain valid? {chain.is_chain_valid()}")

    # 3. Tamper with the chain and re-validate
    print("\n--- 3. Tampering Simulation ---")
    print("Simulating an attack by changing data in Block 1...")
    
    # Directly modifying the chain data
    chain.chain[1]['data'] = "Transaction A: 1000 QC (TAMPERED)"

    print("\nTampered HashChain:")
    print(chain.to_json())
    print(f"\nIs chain valid after tampering? {chain.is_chain_valid()}")
    print("\nTest complete.")

if __name__ == "__main__":
    run_hashing_test()
