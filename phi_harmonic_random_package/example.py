"""
Example usage of the Phi-Harmonic Quantum Random Library
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import phi-harmonic random components
from phi_harmonic_random import (
    PhiHarmonicRandom,
    PhiHarmonicQuantumRandom,
    PhiHarmonicCryptoRandom,
    PhiHarmonicSimulationRandom,
    PhiHarmonicMarketRandom
)

def test_basic_random():
    """Test basic random functionality"""
    print("\n🔮 Testing Basic Phi-Harmonic Random")
    print("-" * 60)
    
    # Create random generator
    random_gen = PhiHarmonicRandom()
    
    # Generate random values
    values = [random_gen.random() for _ in range(10)]
    print(f"Random values: {[f'{v:.4f}' for v in values]}")
    
    # Generate random integers
    integers = [random_gen.randint(1, 100) for _ in range(10)]
    print(f"Random integers: {integers}")
    
    # Random choices
    choices = [random_gen.choice(['apple', 'banana', 'cherry', 'date', 'elderberry']) for _ in range(10)]
    print(f"Random choices: {choices}")
    
    # Shuffle a list
    my_list = list(range(1, 11))
    random_gen.shuffle(my_list)
    print(f"Shuffled list: {my_list}")

def test_quantum_random():
    """Test quantum random functionality"""
    print("\n🔮 Testing Quantum-Enhanced Phi-Harmonic Random")
    print("-" * 60)
    
    # Create quantum random generator
    quantum_random = PhiHarmonicQuantumRandom()
    
    # Get quantum state
    quantum_state = quantum_random.get_quantum_state()
    print(f"Quantum coherence: {quantum_state['coherence']:.6f}")
    print(f"Phi resonance: {quantum_state['phi_resonance']:.6f}")
    
    # Generate quantum random values
    values = [quantum_random.generate_quantum_random() for _ in range(10)]
    print(f"Quantum random values: {[f'{v:.4f}' for v in values]}")
    
    # Generate quantum sequence
    sequence = quantum_random.generate_quantum_sequence(10, -1, 1)
    print(f"Quantum sequence: {[f'{v:.4f}' for v in sequence]}")
    
    # Generate fibonacci pattern
    fibonacci_pattern = quantum_random.generate_fibonacci_pattern(10)
    print(f"Fibonacci pattern: {[f'{v:.4f}' for v in fibonacci_pattern]}")
    
    # Generate phi-weighted distribution
    phi_distribution = quantum_random.generate_phi_weighted_distribution(10)
    print(f"Phi-weighted distribution: {[f'{v:.4f}' for v in phi_distribution]}")

def test_crypto_random():
    """Test cryptographic random functionality"""
    print("\n🔮 Testing Cryptographic Phi-Harmonic Random")
    print("-" * 60)
    
    # Create crypto random generator
    crypto_random = PhiHarmonicCryptoRandom()
    
    # Generate cryptographic key
    key = crypto_random.generate_key(256)
    print(f"Quantum Key (hex): {key.hex()}")
    
    # Measure entropy
    entropy = crypto_random.measure_key_entropy(key)
    print(f"Key entropy: {entropy:.6f} bits/byte")
    
    # Generate nonce and salt
    nonce = crypto_random.generate_nonce(16)
    salt = crypto_random.generate_salt(16)
    print(f"Nonce (hex): {nonce.hex()}")
    print(f"Salt (hex): {salt.hex()}")

def test_simulation_random():
    """Test simulation random functionality"""
    print("\n🔮 Testing Simulation Phi-Harmonic Random")
    print("-" * 60)
    
    # Create simulation random generator
    sim_random = PhiHarmonicSimulationRandom()
    
    # Estimate Pi using Monte Carlo
    pi_estimate = sim_random.monte_carlo_pi(5000)
    print(f"Pi estimate (5,000 points): {pi_estimate:.6f}")
    print(f"Actual Pi: {np.pi:.6f}")
    print(f"Error: {abs(pi_estimate - np.pi) / np.pi * 100:.6f}%")
    
    # Generate random walk
    walk = sim_random.random_walk(steps=100, dimensions=2)
    print(f"Random walk (first 5 steps): {walk[:5]}")
    print(f"Final position: {walk[-1]}")
    
    # Roll quantum dice
    dice_rolls = sim_random.quantum_dice(sides=6, rolls=10)
    print(f"Quantum dice rolls (10d6): {dice_rolls}")

def test_market_random():
    """Test market random functionality"""
    print("\n🔮 Testing Market Phi-Harmonic Random")
    print("-" * 60)
    
    # Create market random generator
    market_random = PhiHarmonicMarketRandom()
    
    # Generate market movements
    movements = [market_random.generate_market_movement() for _ in range(10)]
    print(f"Market movements: {[f'{m*100:+.2f}%' for m in movements]}")
    
    # Simulate market
    prices = market_random.simulate_market(days=30, initial_price=100.0)
    print(f"Market simulation (first 5 days): {[f'{p:.2f}' for p in prices[:5]]}")
    print(f"Market simulation (last 5 days): {[f'{p:.2f}' for p in prices[-5:]]}")
    
    # Generate Fibonacci levels
    fib_levels = market_random.generate_fibonacci_levels(prices[-1])
    print(f"Fibonacci levels for final price:")
    for level, value in fib_levels.items():
        print(f"  - {level}: {value:.2f}")
    
    # Predict market trend
    trend = market_random.predict_market_trend(prices)
    print(f"Predicted trend: {trend}")

def visualize_distributions():
    """Visualize random distributions"""
    print("\n🔮 Visualizing Phi-Harmonic Random Distributions")
    print("-" * 60)
    
    # Create random generators
    std_random = PhiHarmonicRandom()
    quantum_random = PhiHarmonicQuantumRandom()
    
    # Generate samples
    std_samples = [std_random.random() for _ in range(10000)]
    quantum_samples = [quantum_random.generate_quantum_random() for _ in range(10000)]
    
    # Create figure
    plt.figure(figsize=(15, 10))
    
    # Plot standard distribution
    plt.subplot(2, 2, 1)
    plt.title("Phi-Harmonic Random Distribution")
    plt.hist(std_samples, bins=50, alpha=0.7)
    plt.grid(True, alpha=0.3)
    
    # Plot quantum distribution
    plt.subplot(2, 2, 2)
    plt.title("Quantum-Enhanced Random Distribution")
    plt.hist(quantum_samples, bins=50, alpha=0.7)
    plt.grid(True, alpha=0.3)
    
    # Generate fibonacci pattern
    fibonacci_pattern = quantum_random.generate_fibonacci_pattern(1000)
    
    # Plot fibonacci pattern
    plt.subplot(2, 2, 3)
    plt.title("Fibonacci Pattern")
    plt.plot(fibonacci_pattern[:100])
    plt.grid(True, alpha=0.3)
    
    # Simulate market
    market_random = PhiHarmonicMarketRandom()
    prices = market_random.simulate_market(days=100, initial_price=100.0)
    
    # Plot market simulation
    plt.subplot(2, 2, 4)
    plt.title("Market Simulation")
    plt.plot(prices)
    plt.grid(True, alpha=0.3)
    
    # Add phi-harmonic levels
    for level, value in market_random.generate_fibonacci_levels(prices[0]).items():
        if level in ["0.618", "1.618"]:
            plt.axhline(y=value, color='gray', linestyle='--', alpha=0.5, label=f"Phi {level}")
    
    plt.legend()
    plt.tight_layout()
    
    # Create output directory
    os.makedirs("phi_harmonic_random_examples", exist_ok=True)
    
    # Save figure
    plt.savefig("phi_harmonic_random_examples/distributions.png")
    print(f"Visualizations saved to phi_harmonic_random_examples/distributions.png")

def main():
    """Main function"""
    print("\n✨ Phi-Harmonic Quantum Random Library Examples")
    print("=" * 60)
    
    # Test basic random
    test_basic_random()
    
    # Test quantum random
    test_quantum_random()
    
    # Test crypto random
    test_crypto_random()
    
    # Test simulation random
    test_simulation_random()
    
    # Test market random
    test_market_random()
    
    # Visualize distributions
    visualize_distributions()
    
    print("\n✨ Examples complete")
    print("=" * 60)

if __name__ == "__main__":
    main()
