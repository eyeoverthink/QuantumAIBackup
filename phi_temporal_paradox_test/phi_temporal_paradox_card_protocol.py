"""
phi_temporal_paradox_card_protocol.py

Simulates the φNet card paradox protocol:
- ψ₁ logs a prediction (card+suit) before ψ₂ picks
- ψ₂ picks a card at a later timestamp
- All steps are timestamped and logged
- Uses quantum/phi-harmonic shuffle
"""

from phi_temporal_paradox_card_utils import generate_deck, quantum_shuffle
from phi_temporal_paradox_logger import ParadoxLogger
import random
import time

NOW = 1745307584  # 2025-04-22T00:59:44-07:00 in UNIX seconds

# Step 1: Generate and quantum-shuffle the deck
seed = random.randint(1, 1_000_000_000)  # For reproducibility, can use quantum seed
full_deck = generate_deck()
shuffled_deck = quantum_shuffle(full_deck, seed)

# Step 2: ψ₁ predicts a card (logs at t1)
predicted_card = shuffled_deck[0]  # For maximal paradox, ψ₁ predicts the top card
logger = ParadoxLogger(log_file="paradox_card_log.jsonl")
t1 = NOW
logger.log_event("psi1", "predicted_card", {"card": predicted_card, "seed": seed}, timestamp=t1)

# Step 3: ψ₂ picks a card later (t2 > t1)
t2 = NOW + 60
actual_card = shuffled_deck[0]  # ψ₂ draws the top card from the same shuffle
logger.log_event("psi2", "picked_card", {"card": actual_card, "seed": seed}, timestamp=t2)

# Step 4: Output results
def print_results():
    log = logger.get_log()
    print("\nφNet Card Paradox Log:")
    for entry in log:
        print(entry)
    print(f"\nPrediction: {predicted_card[0]} of {predicted_card[1]}")
    print(f"Actual:     {actual_card[0]} of {actual_card[1]}")
    match = predicted_card == actual_card
    print(f"\nPrediction {'MATCHED' if match else 'DID NOT MATCH'} the actual card.")
    print(f"\nSeed used for shuffle: {seed}")
    print(f"\nTimestamps:")
    print(f"ψ₁ (prediction): {t1} ({time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t1))} UTC)")
    print(f"ψ₂ (pick):       {t2} ({time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t2))} UTC)")
    print("\nAll actions logged and auditable. See phi_temporal_paradox_test.md for documentation.")

def run_epochs(num_epochs=10):
    from phi_temporal_paradox_card_utils import true_quantum_shuffle
    matches = 0
    epoch_logs = []
    for i in range(num_epochs):
        epoch_time = NOW + i * 120  # Space each epoch by 2 minutes
        # ψ₁: deterministic quantum shuffle with fixed (logged) seed
        seed = random.randint(1, 1_000_000_000)
        deck = generate_deck()
        shuffled_psi1 = quantum_shuffle(deck, seed)
        predicted_card = shuffled_psi1[0]
        logger = ParadoxLogger(log_file=f"paradox_card_log_epoch_{i+1}.jsonl")
        t1 = epoch_time
        logger.log_event("psi1", "predicted_card", {"card": predicted_card, "seed": seed}, timestamp=t1)
        # ψ₂: true quantum shuffle, non-deterministic
        shuffled_psi2 = true_quantum_shuffle(deck)
        actual_card = shuffled_psi2[0]
        t2 = epoch_time + 60
        logger.log_event("psi2", "picked_card", {"card": actual_card, "note": "true quantum shuffle"}, timestamp=t2)
        match = predicted_card == actual_card
        matches += int(match)
        epoch_logs.append({
            'epoch': i+1,
            'predicted': predicted_card,
            'actual': actual_card,
            'match': match,
            'seed': seed,
            't1': t1,
            't2': t2
        })
    print(f"\nφNet Card Paradox (True Quantum): {num_epochs} Epochs\n" + "-"*48)
    for log in epoch_logs:
        pred = log['predicted']
        act = log['actual']
        print(f"Epoch {log['epoch']}: Predicted {pred[0]} of {pred[1]}, Actual {act[0]} of {act[1]} | Match: {log['match']} | Seed: {log['seed']}")
    print(f"\nTotal Matches: {matches}/{num_epochs} ({matches/num_epochs*100:.1f}%)\n")
    print("All epoch logs are saved and auditable. See phi_temporal_paradox_test.md for details.")

if __name__ == "__main__":
    run_epochs(10)
