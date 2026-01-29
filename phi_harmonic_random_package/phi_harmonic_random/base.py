"""
Base Phi-Harmonic Random Generator
Provides core random generation functionality with phi-harmonic principles
"""
import math
import hashlib
from decimal import Decimal, getcontext
import numpy as np

# Set precision for calculations
getcontext().prec = 28

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # 1/φ
PHI_SQUARED = Decimal('2.618033988749895')  # φ²
PHI_INV_SQUARED = Decimal('0.381966011250105')  # 1/φ²
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]


class PhiHarmonicRandom:
    """
    Base Phi-Harmonic Random Generator
    Provides core random generation functionality with phi-harmonic principles
    """
    
    def __init__(self, seed=None):
        """
        Initialize the phi-harmonic random generator
        
        Args:
            seed (int, optional): Seed for the random generator
        """
        # Initialize state
        self._state = {
            'seed': seed if seed is not None else self._generate_phi_seed(),
            'phi_resonance': float(PHI_INVERSE),
            'coherence': 0.8,
            'iteration': 0
        }
        
        # Initialize numpy random for fallback
        self._np_random = np.random.RandomState(self._state['seed'])
        
        # Initialize the generator
        self._initialize_generator()
    
    def _generate_phi_seed(self):
        """
        Generate a seed based on phi-harmonic principles
        
        Returns:
            int: Phi-harmonic seed
        """
        # Use current timestamp and hash it
        import time
        timestamp = int(time.time() * 1000)
        
        # Apply phi transformation
        phi_transformed = int(timestamp * float(PHI)) % (2**32)
        
        # Hash the transformed value
        hash_value = int(hashlib.sha256(str(phi_transformed).encode()).hexdigest(), 16) % (2**32)
        
        return hash_value
    
    def _initialize_generator(self):
        """Initialize the random generator"""
        # Set initial state based on seed
        self._state['iteration'] = 0
        
        # Calculate initial phi resonance
        seed_decimal = Decimal(str(self._state['seed']))
        self._state['phi_resonance'] = float((seed_decimal * PHI) % Decimal('1'))
        
        # Calculate initial coherence
        self._state['coherence'] = 0.8 + 0.2 * self._state['phi_resonance']
    
    def _update_state(self):
        """Update the internal state for next random generation"""
        # Increment iteration
        self._state['iteration'] += 1
        
        # Update phi resonance using golden ratio transformation
        current_state = Decimal(str(self._state['seed'] + self._state['iteration']))
        phi_transformed = (current_state * PHI) % Decimal('1000000')
        
        # Hash the transformed value
        hash_str = hashlib.sha256(str(int(phi_transformed)).encode()).hexdigest()
        hash_value = int(hash_str, 16)
        
        # Update seed with hash value
        self._state['seed'] = hash_value % (2**32)
        
        # Update phi resonance
        # The original modulo operation can fail with very large numbers due to precision limits.
        # This new method is mathematically equivalent and more robust.
        val = Decimal(str(hash_value)) * PHI
        self._state['phi_resonance'] = float(val - val.to_integral_value(rounding='ROUND_FLOOR'))
        
        # Update coherence - maintain high coherence with slight variations
        coherence_variation = (self._state['phi_resonance'] - 0.5) * 0.1
        self._state['coherence'] = min(0.999, max(0.8, self._state['coherence'] + coherence_variation))
    
    def random(self):
        """
        Generate a random float between 0 and 1 with phi-harmonic properties
        
        Returns:
            float: Random value between 0 and 1
        """
        # Update state
        self._update_state()
        
        # Generate raw random value from state
        raw_value = (self._state['seed'] / (2**32))
        
        # Apply phi-harmonic transformation
        phi_factor = float(PHI_INVERSE) ** (self._state['iteration'] % 8)
        transformed = (raw_value + self._state['phi_resonance'] * phi_factor) % 1.0
        
        return transformed
    
    def randint(self, a, b):
        """
        Generate a random integer between a and b inclusive
        
        Args:
            a (int): Lower bound
            b (int): Upper bound
            
        Returns:
            int: Random integer between a and b inclusive
        """
        return math.floor(self.random() * (b - a + 1)) + a
    
    def choice(self, seq):
        """
        Choose a random element from a non-empty sequence
        
        Args:
            seq (sequence): Non-empty sequence
            
        Returns:
            object: Random element from the sequence
        """
        if not seq:
            raise IndexError("Cannot choose from an empty sequence")
        
        return seq[self.randint(0, len(seq) - 1)]
    
    def shuffle(self, x):
        """
        Shuffle list x in place with phi-harmonic properties
        
        Args:
            x (list): List to shuffle
        """
        # Fisher-Yates shuffle with phi-harmonic weighting
        for i in range(len(x) - 1, 0, -1):
            # Apply phi-harmonic weighting to selection
            phi_weight = float(PHI_INVERSE) ** (i % 5)
            j = math.floor((self.random() * phi_weight * i) % (i + 1))
            x[i], x[j] = x[j], x[i]
    
    def sample(self, population, k):
        """
        Return a k length list of unique elements chosen from the population
        
        Args:
            population (sequence): Population to sample from
            k (int): Number of elements to sample
            
        Returns:
            list: k unique elements from population
        """
        if not 0 <= k <= len(population):
            raise ValueError("Sample larger than population or negative")
        
        # Make a copy of the sequence
        pool = list(population)
        n = len(pool)
        
        # Algorithm R
        result = []
        for i in range(k):
            j = self.randint(0, n - i - 1)
            result.append(pool[j])
            pool[j] = pool[n - i - 1]
        
        return result
    
    def uniform(self, a, b):
        """
        Get a random number in the range [a, b)
        
        Args:
            a (float): Lower bound
            b (float): Upper bound
            
        Returns:
            float: Random float in range [a, b)
        """
        return a + (b - a) * self.random()
    
    def triangular(self, low=0.0, high=1.0, mode=None):
        """
        Generate a random number from a triangular distribution
        
        Args:
            low (float): Lower limit
            high (float): Upper limit
            mode (float, optional): Mode (peak) of the distribution
            
        Returns:
            float: Random float from triangular distribution
        """
        if mode is None:
            mode = (low + high) * 0.5
        
        u = self.random()
        c = (mode - low) / (high - low)
        
        if u > c:
            u = 1.0 - u
            c = 1.0 - c
            low, high = high, low
            
        return low + (high - low) * (u * c) ** 0.5
    
    def get_state(self):
        """
        Get the current state of the generator
        
        Returns:
            dict: Current state
        """
        return self._state.copy()
    
    def set_state(self, state):
        """
        Set the state of the generator
        
        Args:
            state (dict): State to set
        """
        self._state = state.copy()
    
    def seed(self, seed):
        """
        Seed the generator
        
        Args:
            seed (int): Seed value
        """
        self._state['seed'] = seed
        self._np_random = np.random.RandomState(seed)
        self._initialize_generator()
    
    def measure_entropy(self, data):
        """
        Measure the entropy of generated data
        
        Args:
            data (bytes): Data to measure entropy of
            
        Returns:
            float: Entropy in bits per byte
        """
        if not data:
            return 0.0
        
        # Count byte frequencies
        counts = {}
        for byte in data:
            counts[byte] = counts.get(byte, 0) + 1
        
        # Calculate entropy
        entropy = 0.0
        for count in counts.values():
            p = count / len(data)
            entropy -= p * math.log2(p)
            
        return entropy
