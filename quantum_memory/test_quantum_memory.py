import os
from quantum_memory.memory_bank import MemoryBank
from quantum_memory.memory_genome import MemoryGenome

def run_memory_test():
    """Demonstrates the functionality of the Quantum Memory system."""
    print("--- Quantum Memory System Test ---")

    # 1. Initialize the Memory Bank
    db_path = "quantum_memory_bank.json"
    if os.path.exists(db_path):
        os.remove(db_path) # Start fresh for the test
    memory_bank = MemoryBank(filepath=db_path)
    print(f"Initialized MemoryBank. Storage: {db_path}")

    # 2. Create and store some memory genomes
    print("\n--- Storing Memories ---")
    memories_to_store = [
        "The golden ratio is fundamental to nature.",
        "Quantum computing leverages superposition and entanglement.",
        "Phi-harmonic resonance can be used for data encoding.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for mem_data in memories_to_store:
        genome = MemoryGenome(data=mem_data)
        memory_bank.add_genome(genome)
        print(f"Stored: {genome}")

    print(f"\nMemoryBank now contains {len(memory_bank)} genomes.")

    # 3. Perform a query
    print("\n--- Querying Memory ---")
    query_string = "What is the role of phi in nature?"
    print(f"Querying with: '{query_string}'")

    query_genome = MemoryGenome(data=query_string)
    print(f"Query Genome Vector: {query_genome.genome_vector}")

    # 4. Get and display results
    top_results = memory_bank.query(query_data=query_string, top_k=2)

    print("\n--- Top Query Results ---")
    if not top_results:
        print("No similar memories found.")
    else:
        for i, (genome, similarity) in enumerate(top_results):
            print(f"{i+1}. Similarity: {similarity:.4f}")
            print(f"   Memory: '{genome.data}'")
            print(f"   Genome ID: {genome.genome_id}")
            print(f"   Vector: {genome.genome_vector}\n")

    # 5. Clean up the test file
    if os.path.exists(db_path):
        os.remove(db_path)
    print(f"\nTest complete. Cleaned up {db_path}.")

if __name__ == "__main__":
    run_memory_test()
