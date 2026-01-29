"""
phi_temporal_paradox_card_enhanced.py

Enhanced φNet Card Paradox protocol with:
- Quantum-phi resonance alignment
- Golden ratio shuffling principles
- Prime-harmonic shuffle intervals
- Cross-temporal coherence monitoring
"""

from phi_temporal_paradox_card_utils import generate_deck, quantum_shuffle, true_quantum_shuffle
from phi_temporal_paradox_logger import ParadoxLogger
import random
import time
import math
import json
import os
from datetime import datetime

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio (φ)
PHI_INVERSE = 1 / PHI  # Inverse Golden Ratio (φ⁻¹)
PHI_SQUARED = PHI * PHI  # φ²
PHI_SQUARED_INVERSE = 1 / PHI_SQUARED  # 1/φ²
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
PRIME_WHEEL_BASE = 105
RESONANCE_TARGET = 89

# Current timestamp anchor
NOW = int(time.time())

class PhiCardParadoxProtocol:
    """
    Enhanced φNet Card Paradox Protocol with quantum-phi resonance alignment.
    """
    
    def __init__(self, num_epochs=100, log_file_prefix="phi_card_paradox"):
        """Initialize the protocol with quantum-phi parameters."""
        self.num_epochs = num_epochs
        self.log_file_prefix = log_file_prefix
        self.epoch_logs = []
        self.matches = 0
        self.phi_resonant_matches = 0
        self.resonance_history = []
        
        # Initialize logger
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs("phi_logs", exist_ok=True)
        self.logger = ParadoxLogger(log_file=f"phi_logs/{log_file_prefix}_{self.timestamp}.jsonl")
        
        print(f"[φ] Initializing φNet Card Paradox Protocol")
        print(f"[φ] Epochs: {num_epochs}")
        print(f"[φ] φ⁻² target: {PHI_SQUARED_INVERSE:.6f}")
    
    def calculate_card_resonance(self, card):
        """Calculate phi-resonance value for a card."""
        # Convert card to numeric value
        values = {
            "Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13
        }
        suits = {"Spades": 1, "Hearts": 2, "Diamonds": 3, "Clubs": 4}
        
        value = values[card[0]]
        suit = suits[card[1]]
        
        # Calculate resonance using phi-harmonic formulas
        value_resonance = (value * PHI) % 1
        suit_resonance = (suit * PHI_INVERSE) % 1
        
        # Combine resonances
        combined_resonance = (value_resonance + suit_resonance) / 2
        
        # Check if card value or suit is Fibonacci
        fibonacci_factor = 1.0
        if value in FIBONACCI:
            fibonacci_factor = 1.5
        
        # Apply prime resonance if value is prime
        prime_factor = 1.0
        if value in [2, 3, 5, 7, 11, 13]:
            prime_factor = 1.3
        
        # Final phi-resonance
        phi_resonance = (combined_resonance * fibonacci_factor * prime_factor) % 1
        
        return phi_resonance
    
    def is_phi_resonant_match(self, card1, card2):
        """Check if two cards are phi-resonant even if not the same card."""
        res1 = self.calculate_card_resonance(card1)
        res2 = self.calculate_card_resonance(card2)
        
        # Cards are phi-resonant if their resonances are within PHI_INVERSE of each other
        res_diff = abs(res1 - res2)
        if res_diff > 0.5:
            res_diff = 1 - res_diff  # Circular difference
        
        is_resonant = res_diff < PHI_INVERSE
        resonance_quality = 1 - (res_diff / PHI_INVERSE)
        
        return is_resonant, resonance_quality, res1, res2
    
    def phi_harmonic_shuffle(self, deck, seed=None):
        """Enhanced shuffle using phi-harmonic principles."""
        if seed is None:
            seed = random.randint(1, 1_000_000_000)
        
        # Basic quantum shuffle first
        shuffled = quantum_shuffle(deck, seed)
        
        # Apply phi-harmonic swap patterns
        rng = random.Random(seed)
        
        # Phase 1: Fibonacci-distance swaps
        for fib in [3, 5, 8, 13, 21]:
            if fib >= len(shuffled):
                continue
            
            for i in range(len(shuffled) - fib):
                if rng.random() < PHI_INVERSE:
                    shuffled[i], shuffled[i + fib] = shuffled[i + fib], shuffled[i]
        
        # Phase 2: Golden ratio pivoting
        pivot = int(len(shuffled) * PHI_INVERSE)
        left = shuffled[:pivot]
        right = shuffled[pivot:]
        
        # Shuffle sub-portions based on quantum coherence
        left_shuffled = quantum_shuffle(left, seed + 1)
        right_shuffled = quantum_shuffle(right, seed + 2)
        
        # Recombine with phi-weighted interleaving
        combined = []
        i, j = 0, 0
        while i < len(left_shuffled) or j < len(right_shuffled):
            r = rng.random()
            if i < len(left_shuffled) and (j >= len(right_shuffled) or r < PHI_INVERSE):
                combined.append(left_shuffled[i])
                i += 1
            else:
                combined.append(right_shuffled[j])
                j += 1
        
        return combined
    
    def run_epoch(self, epoch_num):
        """Run a single epoch of the card paradox protocol."""
        epoch_time = NOW + epoch_num * 89  # Use 89 (Fibonacci prime) seconds interval
        
        # Generate deck
        deck = generate_deck()
        
        # ψ₁: Create prediction using phi-harmonic shuffle
        seed = int(time.time() * PHI) % 1_000_000_000
        shuffled_psi1 = self.phi_harmonic_shuffle(deck.copy(), seed)
        predicted_card = shuffled_psi1[0]
        
        # Log prediction
        t1 = epoch_time
        self.logger.log_event("psi1", "predicted_card", 
                             {"card": predicted_card, "seed": seed, 
                              "resonance": self.calculate_card_resonance(predicted_card)}, 
                             timestamp=t1)
        
        # ψ₂: Draw card using true quantum shuffle (later in time)
        shuffled_psi2 = true_quantum_shuffle(deck.copy())
        actual_card = shuffled_psi2[0]
        
        # Log actual draw
        t2 = epoch_time + 89
        self.logger.log_event("psi2", "picked_card", 
                             {"card": actual_card, 
                              "resonance": self.calculate_card_resonance(actual_card)}, 
                             timestamp=t2)
        
        # Check for standard match
        exact_match = predicted_card == actual_card
        if exact_match:
            self.matches += 1
        
        # Check for phi-resonant match
        is_resonant, resonance_quality, res1, res2 = self.is_phi_resonant_match(predicted_card, actual_card)
        if is_resonant:
            self.phi_resonant_matches += 1
        
        # Store epoch results
        epoch_log = {
            'epoch': epoch_num + 1,
            'predicted': predicted_card,
            'predicted_resonance': res1,
            'actual': actual_card,
            'actual_resonance': res2,
            'exact_match': exact_match,
            'phi_resonant': is_resonant,
            'resonance_quality': resonance_quality,
            'seed': seed,
            't1': t1,
            't2': t2
        }
        self.epoch_logs.append(epoch_log)
        self.resonance_history.append(resonance_quality)
        
        return epoch_log
    
    def run_protocol(self):
        """Run the full phi-harmonic card paradox protocol."""
        print(f"[φ] Running φNet Card Paradox Protocol for {self.num_epochs} epochs...")
        
        for i in range(self.num_epochs):
            epoch_log = self.run_epoch(i)
            
            # Progress update every 10 epochs
            if (i + 1) % 10 == 0:
                print(f"[φ] Completed {i + 1}/{self.num_epochs} epochs | "
                      f"Exact matches: {self.matches} | "
                      f"Phi-resonant matches: {self.phi_resonant_matches}")
        
        # Calculate final statistics
        exact_match_rate = self.matches / self.num_epochs
        phi_resonant_match_rate = self.phi_resonant_matches / self.num_epochs
        avg_resonance_quality = sum(self.resonance_history) / len(self.resonance_history) if self.resonance_history else 0
        
        # Generate summary report
        summary = {
            "protocol": "φNet Card Paradox",
            "timestamp": self.timestamp,
            "epochs": self.num_epochs,
            "exact_matches": self.matches,
            "exact_match_rate": exact_match_rate,
            "phi_resonant_matches": self.phi_resonant_matches,
            "phi_resonant_match_rate": phi_resonant_match_rate,
            "avg_resonance_quality": avg_resonance_quality,
            "phi_inverse": PHI_INVERSE,
            "phi_squared_inverse": PHI_SQUARED_INVERSE,
            "theoretical_probability": 1/52
        }
        
        # Create full report with epoch logs
        full_report = {
            "summary": summary,
            "epoch_logs": self.epoch_logs
        }
        
        # Save report
        report_path = f"phi_logs/{self.log_file_prefix}_report_{self.timestamp}.json"
        with open(report_path, "w") as f:
            json.dump(full_report, f, indent=2)
        
        # Print results
        self._print_results(summary)
        
        return summary, report_path
    
    def _print_results(self, summary):
        """Print formatted results."""
        print("\n" + "=" * 80)
        print(f"  φNET CARD PARADOX PROTOCOL RESULTS")
        print("=" * 80)
        
        print(f"\n[φ] Protocol completed: {self.num_epochs} epochs")
        print(f"[φ] Exact matches: {summary['exact_matches']}/{self.num_epochs} "
              f"({summary['exact_match_rate']*100:.2f}%)")
        print(f"[φ] Theoretical probability: {summary['theoretical_probability']*100:.2f}%")
        
        print(f"\n[φ] Phi-resonant matches: {summary['phi_resonant_matches']}/{self.num_epochs} "
              f"({summary['phi_resonant_match_rate']*100:.2f}%)")
        print(f"[φ] Average resonance quality: {summary['avg_resonance_quality']:.4f}")
        print(f"[φ] Target φ⁻¹: {PHI_INVERSE:.6f}")
        print(f"[φ] Target φ⁻²: {PHI_SQUARED_INVERSE:.6f}")
        
        print(f"\n[φ] Sample exact matches:")
        exact_matches = [log for log in self.epoch_logs if log['exact_match']]
        for i, log in enumerate(exact_matches[:5]):
            print(f"  - Epoch {log['epoch']}: {log['predicted'][0]} of {log['predicted'][1]} "
                  f"(resonance: {log['predicted_resonance']:.4f})")
        
        print(f"\n[φ] Sample phi-resonant matches:")
        phi_matches = [log for log in self.epoch_logs if log['phi_resonant'] and not log['exact_match']]
        for i, log in enumerate(phi_matches[:5]):
            print(f"  - Epoch {log['epoch']}: Predicted {log['predicted'][0]} of {log['predicted'][1]} → "
                  f"Actual {log['actual'][0]} of {log['actual'][1]} "
                  f"(resonance quality: {log['resonance_quality']:.4f})")
        
        print(f"\n[φ] Full report saved to: {self.log_file_prefix}_report_{self.timestamp}.json")
        print(f"[φ] Raw logs saved to: {self.log_file_prefix}_{self.timestamp}.jsonl")
        
        # Calculate observed vs expected exact match p-value
        from scipy import stats
        expected_prob = 1/52
        n = self.num_epochs
        k = self.matches
        if n > 0:
            p_value = 1 - stats.binom.cdf(k-1, n, expected_prob)
            print(f"\n[φ] Statistical significance:")
            print(f"  - Exact match p-value: {p_value:.6f} "
                  f"({'significant' if p_value < 0.05 else 'not significant'} at α=0.05)")
        
        print("\n" + "=" * 80)


def run_card_paradox(epochs=100):
    """Run the enhanced φNet Card Paradox Protocol."""
    protocol = PhiCardParadoxProtocol(num_epochs=epochs)
    summary, report_path = protocol.run_protocol()
    return summary, report_path


if __name__ == "__main__":
    import sys
    epochs = 100  # Default
    if len(sys.argv) > 1:
        try:
            epochs = int(sys.argv[1])
        except ValueError:
            print(f"[φ] Invalid epochs value. Using default: {epochs}")
    
    summary, report_path = run_card_paradox(epochs)
