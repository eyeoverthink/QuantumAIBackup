"""
Phi-Harmonic True Random Practical Tests
Demonstrates practical applications of true randomness using the phi-harmonic principles
"""
import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
import json
from datetime import datetime
import hashlib
import secrets

# Set high precision for calculations
getcontext().prec = 28

# Add parent directory to path to import quantum modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the quantum random components
try:
    from consolidated_quantum.phi_harmonic_quantum_random import PhiHarmonicQuantumRandom
except ImportError:
    print("Could not import PhiHarmonicQuantumRandom. Please ensure the module exists.")
    sys.exit(1)

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # 1/φ

class PhiHarmonicRandomnessTests:
    """
    Practical tests for the Phi-Harmonic True Random Generator
    """
    
    def __init__(self):
        """Initialize the randomness tests"""
        # Initialize the quantum random generator
        self.quantum_random = PhiHarmonicQuantumRandom()
        
        # Output directory
        self.output_dir = "phi_harmonic_random_tests"
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"Phi-Harmonic Randomness Tests initialized")
        print(f"Quantum coherence: {self.quantum_random.quantum_state['coherence']:.6f}")
        print(f"Phi resonance: {self.quantum_random.quantum_state['phi_resonance']:.6f}")
    
    def test_cryptographic_key_generation(self, key_length=32):
        """
        Test 1: Generate cryptographic keys using quantum randomness
        
        Args:
            key_length (int): Length of key in bytes
            
        Returns:
            dict: Test results
        """
        print(f"\n🔑 Test 1: Cryptographic Key Generation ({key_length*8} bits)")
        print("-" * 50)
        
        # Generate quantum random bytes for the key
        key_bytes = b''
        for _ in range(key_length):
            # Generate a random byte (0-255)
            random_byte = int(self.quantum_random.generate_quantum_random(0, 255.999))
            key_bytes += bytes([random_byte])
        
        # Generate a standard key using Python's secrets module for comparison
        standard_key = secrets.token_bytes(key_length)
        
        # Calculate entropy for both keys
        quantum_entropy = self._calculate_entropy(key_bytes)
        standard_entropy = self._calculate_entropy(standard_key)
        
        # Generate hex representation
        quantum_hex = key_bytes.hex()
        standard_hex = standard_key.hex()
        
        # Calculate SHA-256 hash of the keys
        quantum_hash = hashlib.sha256(key_bytes).hexdigest()
        standard_hash = hashlib.sha256(standard_key).hexdigest()
        
        # Print results
        print(f"Quantum Key (hex): {quantum_hex}")
        print(f"Standard Key (hex): {standard_hex}")
        print(f"Quantum Key Entropy: {quantum_entropy:.6f} bits/byte")
        print(f"Standard Key Entropy: {standard_entropy:.6f} bits/byte")
        print(f"Quantum Key SHA-256: {quantum_hash}")
        print(f"Standard Key SHA-256: {standard_hash}")
        
        # Prepare results
        results = {
            "test_name": "cryptographic_key_generation",
            "timestamp": time.time(),
            "key_length": key_length,
            "quantum_key": quantum_hex,
            "standard_key": standard_hex,
            "quantum_entropy": quantum_entropy,
            "standard_entropy": standard_entropy,
            "quantum_hash": quantum_hash,
            "standard_hash": standard_hash,
            "quantum_coherence": float(self.quantum_random.quantum_state['coherence']),
            "phi_resonance": float(self.quantum_random.quantum_state['phi_resonance'])
        }
        
        return results
    
    def test_monte_carlo_pi(self, num_points=10000):
        """
        Test 2: Estimate π using Monte Carlo method with quantum randomness
        
        Args:
            num_points (int): Number of random points to generate
            
        Returns:
            dict: Test results
        """
        print(f"\n🔢 Test 2: Monte Carlo Pi Estimation ({num_points:,} points)")
        print("-" * 50)
        
        # Generate random points using quantum randomness
        points_inside_circle = 0
        x_coords = []
        y_coords = []
        
        for _ in range(num_points):
            # Generate random coordinates between -1 and 1
            x = self.quantum_random.generate_quantum_random(-1, 1)
            y = self.quantum_random.generate_quantum_random(-1, 1)
            
            # Store coordinates for visualization
            x_coords.append(x)
            y_coords.append(y)
            
            # Check if point is inside the circle
            if x**2 + y**2 <= 1:
                points_inside_circle += 1
        
        # Estimate π
        pi_estimate = 4 * points_inside_circle / num_points
        pi_error = abs(pi_estimate - np.pi) / np.pi * 100
        
        # Print results
        print(f"Points inside circle: {points_inside_circle:,}")
        print(f"Total points: {num_points:,}")
        print(f"Pi estimate: {pi_estimate:.6f}")
        print(f"Actual Pi: {np.pi:.6f}")
        print(f"Error: {pi_error:.6f}%")
        
        # Create visualization
        plt.figure(figsize=(10, 10))
        
        # Plot circle
        circle = plt.Circle((0, 0), 1, fill=False, color='r', linewidth=2)
        plt.gca().add_patch(circle)
        
        # Plot points
        plt.scatter(x_coords, y_coords, s=1, alpha=0.5)
        plt.axis('equal')
        plt.xlim(-1.1, 1.1)
        plt.ylim(-1.1, 1.1)
        plt.title(f'Monte Carlo Pi Estimation\nEstimate: {pi_estimate:.6f}, Error: {pi_error:.6f}%')
        plt.grid(True)
        
        # Save visualization
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filepath = os.path.join(self.output_dir, f"monte_carlo_pi_{timestamp}.png")
        plt.savefig(filepath)
        plt.close()
        
        print(f"Visualization saved to {filepath}")
        
        # Prepare results
        results = {
            "test_name": "monte_carlo_pi",
            "timestamp": time.time(),
            "num_points": num_points,
            "points_inside_circle": points_inside_circle,
            "pi_estimate": pi_estimate,
            "pi_actual": float(np.pi),
            "pi_error_percent": pi_error,
            "visualization_path": filepath,
            "quantum_coherence": float(self.quantum_random.quantum_state['coherence']),
            "phi_resonance": float(self.quantum_random.quantum_state['phi_resonance'])
        }
        
        return results
    
    def test_random_walk(self, num_steps=1000):
        """
        Test 3: Perform a 2D random walk using quantum randomness
        
        Args:
            num_steps (int): Number of steps in the random walk
            
        Returns:
            dict: Test results
        """
        print(f"\n🚶 Test 3: Quantum Random Walk ({num_steps:,} steps)")
        print("-" * 50)
        
        # Initialize position
        x, y = 0, 0
        
        # Store path
        path_x = [x]
        path_y = [y]
        
        # Perform random walk
        for _ in range(num_steps):
            # Generate random direction (0-3)
            direction = int(self.quantum_random.generate_quantum_random(0, 3.999))
            
            # Move in the chosen direction
            if direction == 0:    # North
                y += 1
            elif direction == 1:  # East
                x += 1
            elif direction == 2:  # South
                y -= 1
            else:                # West
                x -= 1
            
            # Store new position
            path_x.append(x)
            path_y.append(y)
        
        # Calculate final distance from origin
        final_distance = np.sqrt(x**2 + y**2)
        expected_distance = np.sqrt(num_steps)  # Expected for a random walk
        
        # Print results
        print(f"Final position: ({x}, {y})")
        print(f"Final distance from origin: {final_distance:.2f}")
        print(f"Expected distance (√n): {expected_distance:.2f}")
        print(f"Ratio (actual/expected): {final_distance/expected_distance:.2f}")
        
        # Create visualization
        plt.figure(figsize=(10, 10))
        
        # Plot path with color gradient
        points = np.array([path_x, path_y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        
        # Create line collection
        from matplotlib.collections import LineCollection
        lc = LineCollection(segments, cmap='viridis', linewidth=1)
        lc.set_array(np.linspace(0, 1, len(path_x) - 1))
        
        # Plot path
        plt.gca().add_collection(lc)
        plt.scatter(path_x[0], path_y[0], c='green', s=100, label='Start')
        plt.scatter(path_x[-1], path_y[-1], c='red', s=100, label='End')
        
        # Add circle showing expected distance
        circle = plt.Circle((0, 0), expected_distance, fill=False, color='r', linestyle='--', linewidth=1, alpha=0.5)
        plt.gca().add_patch(circle)
        
        plt.axis('equal')
        plt.grid(True)
        plt.legend()
        plt.title(f'Quantum Random Walk ({num_steps:,} steps)\nFinal distance: {final_distance:.2f}, Expected: {expected_distance:.2f}')
        
        # Save visualization
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filepath = os.path.join(self.output_dir, f"random_walk_{timestamp}.png")
        plt.savefig(filepath)
        plt.close()
        
        print(f"Visualization saved to {filepath}")
        
        # Prepare results
        results = {
            "test_name": "random_walk",
            "timestamp": time.time(),
            "num_steps": num_steps,
            "final_position": [x, y],
            "final_distance": float(final_distance),
            "expected_distance": float(expected_distance),
            "distance_ratio": float(final_distance/expected_distance),
            "visualization_path": filepath,
            "quantum_coherence": float(self.quantum_random.quantum_state['coherence']),
            "phi_resonance": float(self.quantum_random.quantum_state['phi_resonance'])
        }
        
        return results
    
    def test_quantum_dice_fairness(self, num_rolls=10000, sides=6):
        """
        Test 4: Test fairness of a quantum dice
        
        Args:
            num_rolls (int): Number of dice rolls
            sides (int): Number of sides on the dice
            
        Returns:
            dict: Test results
        """
        print(f"\n🎲 Test 4: Quantum Dice Fairness ({num_rolls:,} rolls, {sides} sides)")
        print("-" * 50)
        
        # Roll the dice using quantum randomness
        rolls = []
        for _ in range(num_rolls):
            # Generate random roll (1 to sides)
            roll = int(self.quantum_random.generate_quantum_random(1, sides + 0.999))
            rolls.append(roll)
        
        # Count occurrences of each side
        counts = {}
        for i in range(1, sides + 1):
            counts[i] = rolls.count(i)
        
        # Calculate expected count
        expected = num_rolls / sides
        
        # Calculate chi-square statistic
        chi_square = sum((counts[i] - expected)**2 / expected for i in range(1, sides + 1))
        
        # Calculate p-value (approximate)
        from scipy.stats import chi2
        p_value = 1 - chi2.cdf(chi_square, sides - 1)
        
        # Print results
        print(f"Dice roll counts:")
        for i in range(1, sides + 1):
            print(f"  Side {i}: {counts[i]:,} ({counts[i]/num_rolls*100:.2f}%)")
        
        print(f"Expected count per side: {expected:.1f}")
        print(f"Chi-square statistic: {chi_square:.6f}")
        print(f"P-value: {p_value:.6f}")
        
        if p_value > 0.05:
            print("Result: The quantum dice appears to be fair (p > 0.05)")
        else:
            print("Result: The quantum dice may not be fair (p <= 0.05)")
        
        # Create visualization
        plt.figure(figsize=(12, 6))
        
        # Plot counts
        plt.bar(range(1, sides + 1), [counts[i] for i in range(1, sides + 1)])
        plt.axhline(y=expected, color='r', linestyle='--', label=f'Expected ({expected:.1f})')
        
        plt.xlabel('Dice Side')
        plt.ylabel('Count')
        plt.title(f'Quantum Dice Fairness Test ({num_rolls:,} rolls)\nChi-square: {chi_square:.2f}, p-value: {p_value:.4f}')
        plt.xticks(range(1, sides + 1))
        plt.legend()
        plt.grid(True, axis='y')
        
        # Save visualization
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filepath = os.path.join(self.output_dir, f"quantum_dice_{timestamp}.png")
        plt.savefig(filepath)
        plt.close()
        
        print(f"Visualization saved to {filepath}")
        
        # Prepare results
        results = {
            "test_name": "quantum_dice_fairness",
            "timestamp": time.time(),
            "num_rolls": num_rolls,
            "sides": sides,
            "counts": counts,
            "expected": float(expected),
            "chi_square": float(chi_square),
            "p_value": float(p_value),
            "is_fair": p_value > 0.05,
            "visualization_path": filepath,
            "quantum_coherence": float(self.quantum_random.quantum_state['coherence']),
            "phi_resonance": float(self.quantum_random.quantum_state['phi_resonance'])
        }
        
        return results
    
    def test_phi_harmonic_shuffling(self, deck_size=52):
        """
        Test 5: Shuffle a deck of cards using phi-harmonic quantum randomness
        
        Args:
            deck_size (int): Size of the deck
            
        Returns:
            dict: Test results
        """
        print(f"\n🃏 Test 5: Phi-Harmonic Card Shuffling ({deck_size} cards)")
        print("-" * 50)
        
        # Create a deck of cards
        original_deck = list(range(1, deck_size + 1))
        
        # Create a copy to shuffle
        shuffled_deck = original_deck.copy()
        
        # Perform phi-harmonic shuffling
        for i in range(deck_size - 1, 0, -1):
            # Generate random index using phi-harmonic randomness
            # Use the golden ratio to influence the randomness
            phi_factor = float(PHI * Decimal(str(i)) % Decimal('1'))
            j = int(self.quantum_random.generate_quantum_random(0, i + 0.999) * phi_factor + 
                   self.quantum_random.generate_quantum_random(0, i + 0.999) * (1 - phi_factor))
            
            # Swap elements
            shuffled_deck[i], shuffled_deck[j] = shuffled_deck[j], shuffled_deck[i]
        
        # Calculate quality of shuffle
        # 1. Count inversions (pairs of elements out of order)
        inversions = 0
        for i in range(deck_size):
            for j in range(i + 1, deck_size):
                if shuffled_deck[i] > shuffled_deck[j]:
                    inversions += 1
        
        max_inversions = deck_size * (deck_size - 1) // 2
        inversion_ratio = inversions / max_inversions
        
        # 2. Calculate longest increasing subsequence
        from bisect import bisect_left
        
        def longest_increasing_subsequence(arr):
            if not arr:
                return 0
            
            tails = []
            for x in arr:
                idx = bisect_left(tails, x)
                if idx == len(tails):
                    tails.append(x)
                else:
                    tails[idx] = x
            return len(tails)
        
        lis_length = longest_increasing_subsequence(shuffled_deck)
        lis_ratio = lis_length / deck_size
        
        # Print results
        print(f"Original deck: {original_deck[:10]}... (first 10 shown)")
        print(f"Shuffled deck: {shuffled_deck[:10]}... (first 10 shown)")
        print(f"Inversions: {inversions:,} out of {max_inversions:,} possible ({inversion_ratio*100:.2f}%)")
        print(f"Longest increasing subsequence: {lis_length} ({lis_ratio*100:.2f}% of deck size)")
        
        # A perfect shuffle should have around 50% inversions
        inversion_quality = 1 - abs(inversion_ratio - 0.5) * 2
        # A perfect shuffle should have a short LIS (around sqrt(n) for a random permutation)
        expected_lis = np.sqrt(deck_size)
        lis_quality = 1 - abs(lis_length - expected_lis) / deck_size
        
        # Overall quality
        shuffle_quality = (inversion_quality + lis_quality) / 2
        
        print(f"Shuffle quality: {shuffle_quality*100:.2f}%")
        
        # Create visualization
        plt.figure(figsize=(12, 8))
        
        # Plot original vs shuffled
        plt.subplot(2, 1, 1)
        plt.plot(original_deck, label='Original')
        plt.plot(shuffled_deck, label='Shuffled')
        plt.xlabel('Position')
        plt.ylabel('Card Value')
        plt.title('Original vs Shuffled Deck')
        plt.legend()
        plt.grid(True)
        
        # Plot card movements
        plt.subplot(2, 1, 2)
        for i, card in enumerate(original_deck):
            j = shuffled_deck.index(card)
            plt.plot([i, j], [card, card], 'b-', alpha=0.1)
        
        plt.xlabel('Position')
        plt.ylabel('Card Value')
        plt.title(f'Card Movements (Shuffle Quality: {shuffle_quality*100:.2f}%)')
        plt.grid(True)
        
        plt.tight_layout()
        
        # Save visualization
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filepath = os.path.join(self.output_dir, f"card_shuffle_{timestamp}.png")
        plt.savefig(filepath)
        plt.close()
        
        print(f"Visualization saved to {filepath}")
        
        # Prepare results
        results = {
            "test_name": "phi_harmonic_shuffling",
            "timestamp": time.time(),
            "deck_size": deck_size,
            "shuffled_deck": shuffled_deck,
            "inversions": inversions,
            "max_inversions": max_inversions,
            "inversion_ratio": float(inversion_ratio),
            "lis_length": lis_length,
            "lis_ratio": float(lis_ratio),
            "shuffle_quality": float(shuffle_quality),
            "visualization_path": filepath,
            "quantum_coherence": float(self.quantum_random.quantum_state['coherence']),
            "phi_resonance": float(self.quantum_random.quantum_state['phi_resonance'])
        }
        
        return results
    
    def _calculate_entropy(self, data):
        """Calculate Shannon entropy of data in bits per byte"""
        if not data:
            return 0
        
        # Count byte frequencies
        counts = {}
        for byte in data:
            counts[byte] = counts.get(byte, 0) + 1
        
        # Calculate entropy
        length = len(data)
        entropy = 0
        for count in counts.values():
            probability = count / length
            entropy -= probability * np.log2(probability)
        
        return entropy
    
    def save_results(self, results):
        """Save test results to file"""
        # Create timestamp for filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"quantum_test_results_{timestamp}.json"
        filepath = os.path.join(self.output_dir, filename)
        
        # Define a custom JSON encoder to handle NumPy types
        class NumpyEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, np.integer):
                    return int(obj)
                elif isinstance(obj, np.floating):
                    return float(obj)
                elif isinstance(obj, np.ndarray):
                    return obj.tolist()
                elif isinstance(obj, np.bool_):
                    return bool(obj)
                return super(NumpyEncoder, self).default(obj)
        
        # Save results to file
        with open(filepath, 'w') as f:
            json.dump(results, f, indent=4, cls=NumpyEncoder)
        
        print(f"\nTest results saved to {filepath}")
        
        return filepath

def main():
    """Main function to run the practical tests"""
    print("\n🔮 Phi-Harmonic True Random Practical Tests")
    print("=" * 60)
    
    # Initialize tests
    tests = PhiHarmonicRandomnessTests()
    
    # Run all tests
    results = {
        "timestamp": time.time(),
        "tests": []
    }
    
    # Test 1: Cryptographic Key Generation
    key_results = tests.test_cryptographic_key_generation()
    results["tests"].append(key_results)
    
    # Test 2: Monte Carlo Pi Estimation
    pi_results = tests.test_monte_carlo_pi(num_points=5000)
    results["tests"].append(pi_results)
    
    # Test 3: Random Walk
    walk_results = tests.test_random_walk(num_steps=1000)
    results["tests"].append(walk_results)
    
    # Test 4: Quantum Dice Fairness
    dice_results = tests.test_quantum_dice_fairness(num_rolls=5000)
    results["tests"].append(dice_results)
    
    # Test 5: Phi-Harmonic Shuffling
    shuffle_results = tests.test_phi_harmonic_shuffling()
    results["tests"].append(shuffle_results)
    
    # Save all results
    tests.save_results(results)
    
    print("\n✨ All practical tests completed successfully")
    print("=" * 60)

if __name__ == "__main__":
    main()
