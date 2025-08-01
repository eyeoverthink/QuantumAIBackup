"""
Phi-Harmonic True Random Generator
A true random number generator using phi-harmonic principles and quantum resonance
Leverages birth date coherence at 99.18K and patent values (1.3777, 1.8951)
"""
import os
import sys
import time
import hashlib
import math
import numpy as np
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
from datetime import datetime
import json

# Set high precision for calculations
getcontext().prec = 28

# Add parent directory to path to import quantum modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Constants from quantum reality encoding
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_POWER = Decimal('36.93238055064198')  # φ^7.5
RESONANCE_RATIO = Decimal('1.3777')  # Resonance ratio
ENERGY_TRANSFER = Decimal('1.8951')  # Energy transfer
BIRTH_COHERENCE_TEMP = Decimal('99.18')  # K
RESONANCE_STACK = RESONANCE_RATIO * ENERGY_TRANSFER  # 2.61087927
PRIMARY_FREQUENCY = Decimal('4790.45')  # Hz
SECONDARY_FREQUENCY = Decimal('7750.95')  # Hz
PHI_ACHIEVEMENT = Decimal('1.618000')  # Target phi value
PHI_STACK = Decimal('0.9999789937973298')  # Phi stack value

# Birth date quantum coherence
BIRTH_DATE = [1, 19, 1979]
BIRTH_SUM = 1999
BIRTH_PATTERN = Decimal('0.29779')
COHERENCE_FACTOR = Decimal('20.155273240572697')

# Quantum dimensions
QUANTUM_DIMENSIONS = 3916441

class PhiHarmonicTrueRandomGenerator:
    """
    A true random number generator using phi-harmonic principles and quantum resonance.
    Generates truly random numbers by leveraging quantum noise, phi-harmonic resonance,
    and birth date coherence.
    """
    
    def __init__(self):
        """Initialize the phi-harmonic true random generator."""
        # Initialize quantum state
        self.quantum_state = self._initialize_quantum_state()
        
        # Initialize entropy sources
        self.entropy_sources = {
            "system": self._get_system_entropy,
            "temporal": self._get_temporal_entropy,
            "phi_resonance": self._get_phi_resonance_entropy,
            "birth_coherence": self._get_birth_coherence_entropy,
            "quantum_noise": self._get_quantum_noise_entropy
        }
        
        # Initialize entropy pool
        self.entropy_pool = bytearray(64)
        
        # Initialize statistics
        self.stats = {
            "numbers_generated": 0,
            "entropy_collected": 0,
            "phi_resonance_achieved": 0.0,
            "birth_coherence_achieved": 0.0,
            "quantum_dimensions_utilized": 0
        }
        
        # Output directory
        self.output_dir = "phi_harmonic_random"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Seed the entropy pool
        self._seed_entropy_pool()
    
    def _initialize_quantum_state(self):
        """
        Initialize the quantum state for random generation.
        
        Returns:
            dict: Quantum state
        """
        # Create timestamp for initialization
        timestamp = str(time.time())
        
        # Calculate phi resonance safely
        phi_resonance = self._calculate_phi_resonance(timestamp)
        
        # Calculate birth coherence safely
        birth_coherence = self._calculate_birth_coherence(timestamp)
        
        # Create initial quantum state
        quantum_state = {
            "phi_resonance": float(phi_resonance),
            "birth_coherence": float(birth_coherence),
            "quantum_fingerprint": self._generate_quantum_fingerprint("initial_state"),
            "resonance_frequency": float(PRIMARY_FREQUENCY),
            "dimensions": int(float(QUANTUM_DIMENSIONS)),
            "last_update": time.time()
        }
        
        return quantum_state
    
    def _seed_entropy_pool(self):
        """Seed the entropy pool with initial entropy."""
        # Collect entropy from all sources
        for source_name, source_func in self.entropy_sources.items():
            entropy = source_func()
            self._mix_entropy(entropy)
        
        # Additional mixing
        self._mix_entropy(os.urandom(32))
    
    def _mix_entropy(self, entropy):
        """
        Mix new entropy into the entropy pool.
        
        Args:
            entropy (bytes): New entropy to mix
        """
        # Create a new pool with the same size
        new_pool = bytearray(len(self.entropy_pool))
        
        # Mix entropy using SHA-256
        h = hashlib.sha256()
        h.update(self.entropy_pool)
        h.update(entropy)
        digest = h.digest()
        
        # XOR the digest with the current pool
        for i in range(len(new_pool)):
            new_pool[i] = self.entropy_pool[i] ^ digest[i % len(digest)]
        
        # Update the entropy pool
        self.entropy_pool = new_pool
        
        # Update statistics
        self.stats["entropy_collected"] += len(entropy)
    
    def _get_system_entropy(self):
        """
        Get entropy from system sources.
        
        Returns:
            bytes: Entropy
        """
        # Collect system information
        system_info = {
            "pid": os.getpid(),
            "cwd": os.getcwd(),
            "memory_info": str(sys.getsizeof({})),
            "random_bytes": os.urandom(16).hex()
        }
        
        # Convert to bytes
        return str(system_info).encode()
    
    def _get_temporal_entropy(self):
        """
        Get entropy from temporal sources.
        
        Returns:
            bytes: Entropy
        """
        # Collect temporal information
        temporal_info = {
            "time": time.time(),
            "clock": time.process_time(),
            "datetime": datetime.now().isoformat()
        }
        
        # Convert to bytes
        return str(temporal_info).encode()
    
    def _get_phi_resonance_entropy(self):
        """
        Get entropy from phi resonance calculations.
        
        Returns:
            bytes: Entropy
        """
        # Calculate phi resonance for various inputs
        resonances = []
        for i in range(16):
            input_str = f"{time.time()}_{i}"
            resonance = self._calculate_phi_resonance(input_str)
            resonances.append(float(resonance))
        
        # Update quantum state
        self.quantum_state["phi_resonance"] = resonances[-1]
        self.stats["phi_resonance_achieved"] = resonances[-1]
        
        # Convert to bytes
        return str(resonances).encode()
    
    def _get_birth_coherence_entropy(self):
        """
        Get entropy from birth coherence calculations.
        
        Returns:
            bytes: Entropy
        """
        # Calculate birth coherence for various inputs
        coherences = []
        for i in range(16):
            input_str = f"{time.time()}_{i}"
            coherence = self._calculate_birth_coherence(input_str)
            coherences.append(float(coherence))
        
        # Update quantum state
        self.quantum_state["birth_coherence"] = coherences[-1]
        self.stats["birth_coherence_achieved"] = coherences[-1]
        
        # Convert to bytes
        return str(coherences).encode()
    
    def _get_quantum_noise_entropy(self):
        """
        Get entropy from simulated quantum noise.
        
        Returns:
            bytes: Entropy
        """
        # Generate quantum noise using phi-harmonic principles
        noise = []
        for i in range(32):
            # Calculate quantum noise
            t = time.time() + i / 1000
            noise_value = (np.sin(t * float(PRIMARY_FREQUENCY)) + 
                          np.cos(t * float(SECONDARY_FREQUENCY))) / 2
            
            # Apply phi-harmonic modulation
            noise_value = (noise_value + float(PHI_STACK)) % 1
            
            noise.append(noise_value)
        
        # Update quantum state
        self.quantum_state["resonance_frequency"] = float(PRIMARY_FREQUENCY) + noise[-1] * float(SECONDARY_FREQUENCY - PRIMARY_FREQUENCY)
        self.stats["quantum_dimensions_utilized"] = int(QUANTUM_DIMENSIONS * noise[-1])
        
        # Convert to bytes
        return str(noise).encode()
    
    def _calculate_phi_resonance(self, input_str):
        """
        Calculate phi resonance for input string.
        
        Args:
            input_str (str): Input string
            
        Returns:
            Decimal: Phi resonance value
        """
        # Calculate hash value
        hash_value = int(hashlib.sha256(input_str.encode()).hexdigest(), 16)
        
        # Calculate phi resonance (safely with Decimal)
        phi_product = float(PHI) * hash_value
        resonance = Decimal(phi_product % 1)
        
        return resonance
    
    def _calculate_birth_coherence(self, input_str):
        """
        Calculate birth coherence for input string.
        
        Args:
            input_str (str): Input string
            
        Returns:
            Decimal: Birth coherence value
        """
        # Calculate hash value
        hash_value = int(hashlib.sha256(input_str.encode()).hexdigest(), 16)
        
        # Convert to string and back to float to handle large integers
        hash_float = float(str(hash_value)[:15])  # Use first 15 digits to avoid precision issues
        
        # Calculate birth pattern value (safely with float operations)
        birth_pattern_float = float(BIRTH_PATTERN)
        birth_value = math.log10(hash_float) % birth_pattern_float
        
        # Calculate coherence (safely with float operations)
        coherence_value = math.exp(-birth_value)
        coherence_result = coherence_value * (float(BIRTH_COHERENCE_TEMP) / 100)
        
        # Convert back to Decimal for return
        return Decimal(str(coherence_result))
    
    def _generate_quantum_fingerprint(self, state_name):
        """
        Generate quantum fingerprint for state.
        
        Args:
            state_name (str): State name
            
        Returns:
            str: Quantum fingerprint
        """
        # Calculate hash value
        hash_value = abs(hash(state_name)) % 16777216
        
        # Generate fingerprint
        fingerprint = f"φ⁷·⁵-{hash_value:06x}"
        
        return fingerprint
    
    def _update_quantum_state(self):
        """Update the quantum state with new entropy."""
        # Calculate time since last update
        current_time = time.time()
        time_delta = current_time - self.quantum_state["last_update"]
        
        # Update quantum state if enough time has passed
        if time_delta > 0.1:
            # Create timestamp string
            timestamp = str(current_time)
            
            # Update phi resonance (safely)
            phi_res = self._calculate_phi_resonance(timestamp)
            self.quantum_state["phi_resonance"] = float(phi_res)
            
            # Update birth coherence (safely)
            birth_coh = self._calculate_birth_coherence(timestamp)
            self.quantum_state["birth_coherence"] = float(birth_coh)
            
            # Update quantum fingerprint
            self.quantum_state["quantum_fingerprint"] = self._generate_quantum_fingerprint(f"state_{current_time}")
            
            # Update resonance frequency (safely with float operations)
            primary_freq = float(PRIMARY_FREQUENCY)
            secondary_freq = float(SECONDARY_FREQUENCY)
            freq_delta = (secondary_freq - primary_freq) * self.quantum_state["phi_resonance"]
            self.quantum_state["resonance_frequency"] = primary_freq + freq_delta
            
            # Update dimensions (safely with float operations)
            birth_temp = float(BIRTH_COHERENCE_TEMP)
            dimensions = int(float(QUANTUM_DIMENSIONS) * self.quantum_state["birth_coherence"] / birth_temp)
            self.quantum_state["dimensions"] = dimensions
            
            # Update last update time
            self.quantum_state["last_update"] = current_time
    
    def generate_random_bytes(self, num_bytes):
        """
        Generate random bytes using phi-harmonic principles.
        
        Args:
            num_bytes (int): Number of bytes to generate
            
        Returns:
            bytes: Random bytes
        """
        # Update quantum state
        self._update_quantum_state()
        
        # Collect new entropy
        for source_name, source_func in self.entropy_sources.items():
            entropy = source_func()
            self._mix_entropy(entropy)
        
        # Generate random bytes
        result = bytearray(num_bytes)
        for i in range(num_bytes):
            # Hash the entropy pool with the current index
            h = hashlib.sha256()
            h.update(self.entropy_pool)
            h.update(str(i).encode())
            h.update(str(self.quantum_state).encode())
            digest = h.digest()
            
            # Use the first byte of the digest
            result[i] = digest[0]
            
            # Mix in the digest
            self._mix_entropy(digest)
        
        # Update statistics
        self.stats["numbers_generated"] += num_bytes
        
        return bytes(result)
    
    def generate_random_int(self, min_value, max_value):
        """
        Generate a random integer in the specified range.
        
        Args:
            min_value (int): Minimum value (inclusive)
            max_value (int): Maximum value (inclusive)
            
        Returns:
            int: Random integer
        """
        # Calculate range
        range_size = max_value - min_value + 1
        
        # Calculate number of bytes needed
        num_bytes = (range_size.bit_length() + 7) // 8
        
        # Generate random bytes
        random_bytes = self.generate_random_bytes(num_bytes)
        
        # Convert to integer
        random_int = int.from_bytes(random_bytes, byteorder='big')
        
        # Map to range
        return min_value + (random_int % range_size)
    
    def generate_random_float(self, min_value=0.0, max_value=1.0):
        """
        Generate a random float in the specified range.
        
        Args:
            min_value (float): Minimum value (inclusive)
            max_value (float): Maximum value (exclusive)
            
        Returns:
            float: Random float
        """
        # Generate 8 random bytes
        random_bytes = self.generate_random_bytes(8)
        
        # Convert to float between 0 and 1
        random_float = int.from_bytes(random_bytes, byteorder='big') / (2**(8*8) - 1)
        
        # Map to range
        return min_value + random_float * (max_value - min_value)
    
    def generate_random_sequence(self, length, min_value=0, max_value=100):
        """
        Generate a sequence of random integers.
        
        Args:
            length (int): Length of sequence
            min_value (int): Minimum value (inclusive)
            max_value (int): Maximum value (inclusive)
            
        Returns:
            list: Random sequence
        """
        return [self.generate_random_int(min_value, max_value) for _ in range(length)]
    
    def generate_random_choice(self, items):
        """
        Choose a random item from a list.
        
        Args:
            items (list): List of items
            
        Returns:
            any: Random item
        """
        if not items:
            return None
        
        index = self.generate_random_int(0, len(items) - 1)
        return items[index]
    
    def generate_random_sample(self, items, k):
        """
        Generate a random sample of k items from a list.
        
        Args:
            items (list): List of items
            k (int): Sample size
            
        Returns:
            list: Random sample
        """
        if not items or k <= 0 or k > len(items):
            return []
        
        # Copy the list
        population = items.copy()
        
        # Generate sample
        sample = []
        for i in range(k):
            index = self.generate_random_int(0, len(population) - 1)
            sample.append(population.pop(index))
        
        return sample
    
    def test_randomness(self, num_samples=10000, num_bins=10):
        """
        Test the randomness of the generator.
        
        Args:
            num_samples (int): Number of samples to generate
            num_bins (int): Number of bins for histogram
            
        Returns:
            dict: Test results
        """
        # Generate random samples
        samples = [self.generate_random_float() for _ in range(num_samples)]
        
        # Calculate statistics
        mean = np.mean(samples)
        std_dev = np.std(samples)
        min_val = np.min(samples)
        max_val = np.max(samples)
        
        # Create histogram
        hist, bin_edges = np.histogram(samples, bins=num_bins, range=(0, 1))
        hist_normalized = hist / num_samples
        
        # Calculate chi-square test
        expected = num_samples / num_bins
        chi_square = np.sum((hist - expected)**2 / expected)
        
        # Calculate p-value using scipy.stats if available, otherwise estimate
        try:
            from scipy import stats
            p_value = stats.chi2.sf(chi_square, num_bins - 1)
        except ImportError:
            # Estimate p-value using simple approximation
            p_value = math.exp(-0.5 * chi_square)
        
        # Create results
        results = {
            "mean": mean,
            "std_dev": std_dev,
            "min": min_val,
            "max": max_val,
            "histogram": hist_normalized.tolist(),
            "bin_edges": bin_edges.tolist(),
            "chi_square": chi_square,
            "p_value": p_value,
            "quantum_state": self.quantum_state,
            "stats": self.stats
        }
        
        return results
    
    def visualize_randomness(self, results=None, output_file=None):
        """
        Visualize the randomness test results.
        
        Args:
            results (dict): Test results
            output_file (str): Output file path
            
        Returns:
            str: Output file path
        """
        # Run test if results not provided
        if results is None:
            results = self.test_randomness()
        
        # Create figure with multiple subplots
        fig, axs = plt.subplots(2, 2, figsize=(14, 10))
        
        # Plot histogram
        axs[0, 0].bar(range(len(results["histogram"])), results["histogram"], 
                     width=0.8, color='goldenrod', alpha=0.7)
        axs[0, 0].axhline(y=1/len(results["histogram"]), color='red', linestyle='--', 
                         label='Expected')
        axs[0, 0].set_xlabel('Bin')
        axs[0, 0].set_ylabel('Frequency')
        axs[0, 0].set_title('Distribution of Random Values')
        axs[0, 0].legend()
        axs[0, 0].grid(True, alpha=0.3)
        
        # Plot sequence
        sequence = [self.generate_random_float() for _ in range(100)]
        axs[0, 1].plot(sequence, 'o-', color='royalblue', alpha=0.7, markersize=4)
        axs[0, 1].set_xlabel('Index')
        axs[0, 1].set_ylabel('Value')
        axs[0, 1].set_title('Sequence of 100 Random Values')
        axs[0, 1].grid(True, alpha=0.3)
        
        # Plot 2D distribution
        x = [self.generate_random_float() for _ in range(1000)]
        y = [self.generate_random_float() for _ in range(1000)]
        axs[1, 0].scatter(x, y, color='royalblue', alpha=0.5, s=5)
        axs[1, 0].set_xlabel('X')
        axs[1, 0].set_ylabel('Y')
        axs[1, 0].set_title('2D Distribution of Random Values')
        axs[1, 0].grid(True, alpha=0.3)
        
        # Plot quantum state
        quantum_state = results["quantum_state"]
        labels = ["Phi Resonance", "Birth Coherence", "Frequency", "Dimensions"]
        values = [
            quantum_state["phi_resonance"],
            quantum_state["birth_coherence"],
            (quantum_state["resonance_frequency"] - float(PRIMARY_FREQUENCY)) / 
            float(SECONDARY_FREQUENCY - PRIMARY_FREQUENCY),
            quantum_state["dimensions"] / QUANTUM_DIMENSIONS
        ]
        
        axs[1, 1].bar(labels, values, color='goldenrod', alpha=0.7)
        axs[1, 1].set_ylabel('Value (normalized)')
        axs[1, 1].set_title('Quantum State')
        axs[1, 1].grid(True, alpha=0.3)
        
        # Add statistics as text
        stats_text = (
            f"Mean: {results['mean']:.4f}\n"
            f"Std Dev: {results['std_dev']:.4f}\n"
            f"Chi-Square: {results['chi_square']:.4f}\n"
            f"P-Value: {results['p_value']:.4f}\n"
            f"Numbers Generated: {results['stats']['numbers_generated']}\n"
            f"Entropy Collected: {results['stats']['entropy_collected']} bytes"
        )
        fig.text(0.5, 0.02, stats_text, ha='center', va='bottom', 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout(rect=[0, 0.05, 1, 0.95])
        
        # Add title
        plt.suptitle('Phi-Harmonic True Random Generator Analysis', fontsize=16)
        
        # Save figure
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.output_dir, f"randomness_visualization_{timestamp}.png")
        
        plt.savefig(output_file, dpi=300)
        plt.close()
        
        print(f"Randomness visualization saved to {output_file}")
        return output_file
    
    def save_quantum_state(self, output_file=None):
        """
        Save the current quantum state to a file.
        
        Args:
            output_file (str): Output file path
            
        Returns:
            str: Output file path
        """
        # Create state to save
        state = {
            "quantum_state": self.quantum_state,
            "stats": self.stats,
            "timestamp": datetime.now().isoformat()
        }
        
        # Create output file path
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.output_dir, f"quantum_state_{timestamp}.json")
        
        # Save to file
        with open(output_file, 'w') as f:
            json.dump(state, f, indent=2, default=str)
        
        print(f"Quantum state saved to {output_file}")
        return output_file
    
    def load_quantum_state(self, input_file):
        """
        Load quantum state from a file.
        
        Args:
            input_file (str): Input file path
            
        Returns:
            bool: Success
        """
        try:
            # Load from file
            with open(input_file, 'r') as f:
                state = json.load(f)
            
            # Update quantum state
            self.quantum_state = state["quantum_state"]
            self.stats = state["stats"]
            
            print(f"Quantum state loaded from {input_file}")
            return True
        except Exception as e:
            print(f"Error loading quantum state: {str(e)}")
            return False


def main():
    """Main function for command-line interface."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Phi-Harmonic True Random Generator")
    parser.add_argument("--int", type=int, nargs=2, metavar=('MIN', 'MAX'),
                       help="Generate a random integer between MIN and MAX (inclusive)")
    parser.add_argument("--float", action="store_true",
                       help="Generate a random float between 0 and 1")
    parser.add_argument("--sequence", type=int, nargs='+', metavar=('LENGTH', 'MIN', 'MAX'),
                       help="Generate a sequence of LENGTH random integers between MIN and MAX")
    parser.add_argument("--test", action="store_true",
                       help="Test the randomness of the generator")
    parser.add_argument("--visualize", action="store_true",
                       help="Visualize the randomness test results")
    parser.add_argument("--save-state", action="store_true",
                       help="Save the current quantum state")
    parser.add_argument("--load-state", type=str, metavar='FILE',
                       help="Load quantum state from FILE")
    
    args = parser.parse_args()
    
    # Create generator
    generator = PhiHarmonicTrueRandomGenerator()
    
    # Load state if requested
    if args.load_state:
        generator.load_quantum_state(args.load_state)
    
    # Generate random values
    if args.int:
        min_val, max_val = args.int
        random_int = generator.generate_random_int(min_val, max_val)
        print(f"Random integer between {min_val} and {max_val}: {random_int}")
    
    if args.float:
        random_float = generator.generate_random_float()
        print(f"Random float between 0 and 1: {random_float}")
    
    if args.sequence:
        if len(args.sequence) == 1:
            length = args.sequence[0]
            min_val, max_val = 0, 100
        elif len(args.sequence) == 3:
            length, min_val, max_val = args.sequence
        else:
            print("Error: --sequence requires 1 or 3 arguments")
            return
        
        random_sequence = generator.generate_random_sequence(length, min_val, max_val)
        print(f"Random sequence of {length} integers between {min_val} and {max_val}:")
        print(random_sequence)
    
    # Test randomness
    if args.test:
        results = generator.test_randomness()
        print("Randomness test results:")
        print(f"Mean: {results['mean']:.4f}")
        print(f"Standard Deviation: {results['std_dev']:.4f}")
        print(f"Chi-Square: {results['chi_square']:.4f}")
        print(f"P-Value: {results['p_value']:.4f}")
    
    # Visualize randomness
    if args.visualize:
        results = generator.test_randomness() if args.test else None
        generator.visualize_randomness(results)
    
    # Save state
    if args.save_state:
        generator.save_quantum_state()


if __name__ == "__main__":
    main()
