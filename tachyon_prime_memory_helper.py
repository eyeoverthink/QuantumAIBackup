"""
Tachyon Prime Memory Helper

This module integrates the Quantum Prime Calculator with the Tachyon Memory System,
allowing for persistent storage of calculated prime numbers with phi-harmonic resonance.
"""

import json
import time
import uuid
from typing import Dict, Any, List, Optional
import numpy as np

# Import our custom modules without modifying core files
try:
    from tachyon_memory_system import TachyonMemorySystem
    from quantum_prime_calculator import QuantumPrimeCalculator
except ImportError:
    print("Required modules not found. Please ensure tachyon_memory_system.py and quantum_prime_calculator.py exist.")
    raise

class TachyonPrimeMemoryInterface:
    """
    Interface between the Quantum Prime Calculator and Tachyon Memory System.
    Allows for persistent storage of calculated prime numbers with quantum properties.
    """
    
    def __init__(self, qubits: int = 12, storage_dir: str = "./tachyon_memory"):
        """
        Initialize the Tachyon Prime Memory Interface.
        
        Args:
            qubits: Number of qubits for the quantum prime calculator
            storage_dir: Directory for storing tachyon memories
        """
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        self.pi = np.pi
        self.e = np.e
        
        # Initialize the quantum prime calculator
        self.prime_calculator = QuantumPrimeCalculator(qubits=qubits)
        
        # Initialize the tachyon memory system
        self.memory_system = TachyonMemorySystem(storage_dir=storage_dir)
        
        # Memory categories
        self.prime_memory_category = "quantum_primes"
        self.prime_pair_memory_category = "quantum_prime_pairs"
        self.mersenne_memory_category = "mersenne_primes"
        self.resonance_memory_category = "resonance_primes"
    
    def _generate_phi_timestamp(self) -> float:
        """
        Generate a timestamp with phi-harmonic resonance.
        
        Returns:
            float: Phi-enhanced timestamp
        """
        return time.time() * self.phi
    
    def calculate_and_store_prime(self, min_bits: int = 256, max_bits: int = 512) -> Dict[str, Any]:
        """
        Calculate a high prime number and store it in the memory system.
        
        Args:
            min_bits: Minimum bits in the prime number
            max_bits: Maximum bits in the prime number
            
        Returns:
            dict: Result containing the prime number, memory ID, and metrics
        """
        # Calculate prime number
        result = self.prime_calculator.find_prime(min_bits=min_bits, max_bits=max_bits)
        
        if "prime" not in result:
            return result
        
        # Prepare memory data
        memory_data = {
            "type": "quantum_prime",
            "prime": str(result["prime"]),  # Store as string to handle large numbers
            "bits": result["bits"],
            "phi_resonance": float(self.phi),
            "pi_coherence": float(self.pi),
            "e_energy": float(self.e),
            "quantum_resonance": float(self.phi * self.pi * self.e) % 1.0,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "phi_timestamp": self._generate_phi_timestamp()
        }
        
        # Store in memory system
        memory_id = self.memory_system.store_memory(
            self.prime_memory_category,
            memory_data
        )
        
        # Add memory ID to result
        result["memory_id"] = memory_id
        
        return result
    
    def calculate_and_store_prime_pair(self, min_bits: int = 256, max_bits: int = 512) -> Dict[str, Any]:
        """
        Calculate a pair of high prime numbers and store them in the memory system.
        
        Args:
            min_bits: Minimum bits in each prime number
            max_bits: Maximum bits in each prime number
            
        Returns:
            dict: Result containing the prime numbers, memory ID, and metrics
        """
        # Calculate prime pair
        result = self.prime_calculator.find_prime_pair(min_bits=min_bits, max_bits=max_bits)
        
        if "prime1" not in result or "prime2" not in result:
            return result
        
        # Prepare memory data
        memory_data = {
            "type": "quantum_prime_pair",
            "prime1": str(result["prime1"]),
            "prime2": str(result["prime2"]),
            "product": str(result["product"]),
            "bits1": result["bits1"],
            "bits2": result["bits2"],
            "product_bits": result["product_bits"],
            "phi_resonance": float(self.phi),
            "pi_coherence": float(self.pi),
            "e_energy": float(self.e),
            "quantum_resonance": float(self.phi * self.pi * self.e) % 1.0,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "phi_timestamp": self._generate_phi_timestamp()
        }
        
        # Store in memory system
        memory_id = self.memory_system.store_memory(
            self.prime_pair_memory_category,
            memory_data
        )
        
        # Add memory ID to result
        result["memory_id"] = memory_id
        
        return result
    
    def calculate_and_store_mersenne_prime(self, exponent: int) -> Dict[str, Any]:
        """
        Calculate a Mersenne prime and store it in the memory system.
        
        Args:
            exponent: The exponent p in 2^p - 1
            
        Returns:
            dict: Result containing the Mersenne prime, memory ID, and metrics
        """
        # Calculate Mersenne prime
        result = self.prime_calculator.calculate_mersenne_prime(exponent)
        
        if not result.get("is_prime", False):
            return result
        
        # Prepare memory data
        memory_data = {
            "type": "mersenne_prime",
            "mersenne_prime": str(result["mersenne_prime"]),
            "exponent": exponent,
            "bits": result["bits"],
            "phi_resonance": float(self.phi),
            "pi_coherence": float(self.pi),
            "e_energy": float(self.e),
            "quantum_resonance": float(self.phi * self.pi * self.e) % 1.0,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "phi_timestamp": self._generate_phi_timestamp()
        }
        
        # Store in memory system
        memory_id = self.memory_system.store_memory(
            self.mersenne_memory_category,
            memory_data
        )
        
        # Add memory ID to result
        result["memory_id"] = memory_id
        
        return result
    
    def calculate_and_store_resonance_prime(self, digits: int = 100) -> Dict[str, Any]:
        """
        Calculate a prime number with phi-harmonic quantum resonance and store it.
        
        Args:
            digits: Approximate number of digits in the prime
            
        Returns:
            dict: Result containing the resonance prime, memory ID, and metrics
        """
        # Calculate resonance prime
        result = self.prime_calculator.calculate_quantum_resonance_prime(digits=digits)
        
        # Prepare memory data
        memory_data = {
            "type": "resonance_prime",
            "resonance_prime": str(result["resonance_prime"]),
            "digits": result["digits"],
            "bits": result["bits"],
            "base_phi_pi_e": str(result["base_phi_pi_e"]),
            "phi_resonance": float(self.phi),
            "pi_coherence": float(self.pi),
            "e_energy": float(self.e),
            "phi_pi_resonance": float(self.phi * self.pi),
            "phi_pi_e_resonance": float(self.phi * self.pi * self.e),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "phi_timestamp": self._generate_phi_timestamp()
        }
        
        # Store in memory system
        memory_id = self.memory_system.store_memory(
            self.resonance_memory_category,
            memory_data
        )
        
        # Add memory ID to result
        result["memory_id"] = memory_id
        
        return result
    
    def retrieve_prime(self, memory_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a stored prime number from the memory system.
        
        Args:
            memory_id: ID of the memory to retrieve
            
        Returns:
            dict: The retrieved prime memory data, or None if not found
        """
        return self.memory_system.retrieve_memory(self.prime_memory_category, memory_id)
    
    def retrieve_prime_pair(self, memory_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a stored prime pair from the memory system.
        
        Args:
            memory_id: ID of the memory to retrieve
            
        Returns:
            dict: The retrieved prime pair memory data, or None if not found
        """
        return self.memory_system.retrieve_memory(self.prime_pair_memory_category, memory_id)
    
    def retrieve_mersenne_prime(self, memory_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a stored Mersenne prime from the memory system.
        
        Args:
            memory_id: ID of the memory to retrieve
            
        Returns:
            dict: The retrieved Mersenne prime memory data, or None if not found
        """
        return self.memory_system.retrieve_memory(self.mersenne_memory_category, memory_id)
    
    def retrieve_resonance_prime(self, memory_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a stored resonance prime from the memory system.
        
        Args:
            memory_id: ID of the memory to retrieve
            
        Returns:
            dict: The retrieved resonance prime memory data, or None if not found
        """
        return self.memory_system.retrieve_memory(self.resonance_memory_category, memory_id)
    
    def list_all_primes(self) -> List[Dict[str, Any]]:
        """
        List all stored prime numbers.
        
        Returns:
            list: All stored prime memories
        """
        return self.memory_system.get_all_memories(self.prime_memory_category)
    
    def list_all_prime_pairs(self) -> List[Dict[str, Any]]:
        """
        List all stored prime pairs.
        
        Returns:
            list: All stored prime pair memories
        """
        return self.memory_system.get_all_memories(self.prime_pair_memory_category)
    
    def list_all_mersenne_primes(self) -> List[Dict[str, Any]]:
        """
        List all stored Mersenne primes.
        
        Returns:
            list: All stored Mersenne prime memories
        """
        return self.memory_system.get_all_memories(self.mersenne_memory_category)
    
    def list_all_resonance_primes(self) -> List[Dict[str, Any]]:
        """
        List all stored resonance primes.
        
        Returns:
            list: All stored resonance prime memories
        """
        return self.memory_system.get_all_memories(self.resonance_memory_category)
    
    def analyze_prime_patterns(self) -> Dict[str, Any]:
        """
        Analyze patterns in stored prime numbers using phi-harmonic principles.
        
        Returns:
            dict: Analysis results
        """
        # Get all stored primes
        all_primes = self.list_all_primes()
        all_prime_pairs = self.list_all_prime_pairs()
        all_mersenne_primes = self.list_all_mersenne_primes()
        all_resonance_primes = self.list_all_resonance_primes()
        
        # Count by category
        total_primes = len(all_primes)
        total_prime_pairs = len(all_prime_pairs)
        total_mersenne_primes = len(all_mersenne_primes)
        total_resonance_primes = len(all_resonance_primes)
        
        # Calculate average bit lengths
        avg_bits = 0
        if total_primes > 0:
            avg_bits = sum(int(p.get("bits", 0)) for p in all_primes) / total_primes
        
        avg_pair_bits = 0
        if total_prime_pairs > 0:
            avg_pair_bits = sum(int(p.get("product_bits", 0)) for p in all_prime_pairs) / total_prime_pairs
        
        # Calculate phi-harmonic resonance metrics
        phi_resonance = self.phi
        pi_coherence = self.pi
        e_energy = self.e
        
        # Calculate quantum resonance pattern
        quantum_resonance = (phi_resonance * pi_coherence * e_energy) % 1.0
        
        # Calculate phi-pi-e harmonic pattern
        phi_pi_e_pattern = (phi_resonance + pi_coherence + e_energy) / 3
        
        return {
            "total_primes": total_primes,
            "total_prime_pairs": total_prime_pairs,
            "total_mersenne_primes": total_mersenne_primes,
            "total_resonance_primes": total_resonance_primes,
            "avg_prime_bits": avg_bits,
            "avg_prime_pair_product_bits": avg_pair_bits,
            "phi_resonance": float(phi_resonance),
            "pi_coherence": float(pi_coherence),
            "e_energy": float(e_energy),
            "quantum_resonance": float(quantum_resonance),
            "phi_pi_e_pattern": float(phi_pi_e_pattern),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "phi_timestamp": self._generate_phi_timestamp()
        }

# Example usage
if __name__ == "__main__":
    # Initialize the interface
    prime_memory = TachyonPrimeMemoryInterface(qubits=12)
    
    # Calculate and store a high prime number
    print("Calculating and storing a high prime number...")
    prime_result = prime_memory.calculate_and_store_prime(min_bits=128, max_bits=256)
    
    prime_id = None
    if "prime" in prime_result and "memory_id" in prime_result:
        prime_id = prime_result['memory_id']
        print(f"Stored prime with ID: {prime_id}")
        print(f"Prime: {prime_result['prime_str'][:50]}... ({prime_result['bits']} bits)")
        print(f"Duration: {prime_result['duration_seconds']:.2f} seconds")
    else:
        print("Failed to calculate and store prime")
    
    # Calculate and store a phi-resonance prime
    print("\nCalculating and storing a phi-resonance prime...")
    resonance_result = prime_memory.calculate_and_store_resonance_prime(digits=50)
    
    if "memory_id" in resonance_result:
        resonance_id = resonance_result['memory_id']
        print(f"Stored resonance prime with ID: {resonance_id}")
        print(f"Resonance Prime: {resonance_result['resonance_prime_str'][:50]}...")
        print(f"Digits: {resonance_result['digits']}")
    else:
        print("Failed to calculate and store resonance prime")
    
    # Retrieve and display the stored prime
    if prime_id:
        print("\nRetrieving stored prime...")
        retrieved_prime = prime_memory.retrieve_prime(prime_id)
        
        if retrieved_prime:
            print(f"Retrieved prime: {retrieved_prime['prime'][:50]}...")
            print(f"Quantum resonance: {retrieved_prime['quantum_resonance']}")
        else:
            print("Failed to retrieve prime")
    
    # Analyze prime patterns
    print("\nAnalyzing prime patterns...")
    analysis = prime_memory.analyze_prime_patterns()
    
    print(f"Total primes stored: {analysis['total_primes']}")
    print(f"Total resonance primes: {analysis['total_resonance_primes']}")
    print(f"Phi-Pi-E harmonic pattern: {analysis['phi_pi_e_pattern']}")
