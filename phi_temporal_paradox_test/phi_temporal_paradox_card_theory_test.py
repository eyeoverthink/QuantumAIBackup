"""
phi_temporal_paradox_card_theory_test.py

Tests the theory: "If you see it, it happens; if not, it lingers. Guessing a number implies exuding that you know it, not guessing."

- Case A: Observed prediction (ψ₁'s prediction is revealed before ψ₂ draws)
- Case B: Unobserved prediction (ψ₁'s prediction is only revealed after ψ₂ draws)
- ψ₂ always uses true quantum shuffle (tru random)
- Logs and compares match rates for both cases over many epochs
"""

from phi_temporal_paradox_card_utils import generate_deck, quantum_shuffle, true_quantum_shuffle
from phi_temporal_paradox_logger import ParadoxLogger
import random
import time

NOW = 1745308049  # 2025-04-22T01:07:29-07:00 in UNIX seconds

EPOCHS = 100
observed_matches = 0
unobserved_matches = 0
observed_logs = []
unobserved_logs = []

for i in range(EPOCHS):
    epoch_time = NOW + i * 120
    seed = random.randint(1, 1_000_000_000)
    deck = generate_deck()
    # ψ₁ predicts top card from deterministic quantum shuffle
    shuffled_psi1 = quantum_shuffle(deck, seed)
    predicted_card = shuffled_psi1[0]
    # ψ₂ draws top card from true quantum shuffle
    shuffled_psi2 = true_quantum_shuffle(deck)
    actual_card = shuffled_psi2[0]
    # Case A: Observed (prediction logged before draw)
    logger_obs = ParadoxLogger(log_file=f"paradox_card_theory_observed_epoch_{i+1}.jsonl")
    t1 = epoch_time
    t2 = epoch_time + 60
    logger_obs.log_event("psi1", "predicted_card_observed", {"card": predicted_card, "seed": seed}, timestamp=t1)
    logger_obs.log_event("psi2", "picked_card", {"card": actual_card, "note": "true quantum shuffle"}, timestamp=t2)
    match_obs = predicted_card == actual_card
    observed_matches += int(match_obs)
    observed_logs.append({
        'epoch': i+1,
        'predicted': predicted_card,
        'actual': actual_card,
        'match': match_obs,
        'seed': seed,
        't1': t1,
        't2': t2
    })
    # Case B: Unobserved (prediction only revealed after draw)
    logger_unobs = ParadoxLogger(log_file=f"paradox_card_theory_unobserved_epoch_{i+1}.jsonl")
    t1b = epoch_time
    t2b = epoch_time + 60
    logger_unobs.log_event("psi2", "picked_card", {"card": actual_card, "note": "true quantum shuffle"}, timestamp=t2b)
    logger_unobs.log_event("psi1", "predicted_card_unobserved", {"card": predicted_card, "seed": seed}, timestamp=t2b+1)
    match_unobs = predicted_card == actual_card
    unobserved_matches += int(match_unobs)
    unobserved_logs.append({
        'epoch': i+1,
        'predicted': predicted_card,
        'actual': actual_card,
        'match': match_unobs,
        'seed': seed,
        't1': t1b,
        't2': t2b
    })

print(f"\nφNet Card Paradox Theory Test: {EPOCHS} Epochs\n" + "-"*48)
print(f"Observed Prediction (revealed before draw): {observed_matches}/{EPOCHS} matches ({observed_matches/EPOCHS*100:.1f}%)")
print(f"Unobserved Prediction (revealed after draw): {unobserved_matches}/{EPOCHS} matches ({unobserved_matches/EPOCHS*100:.1f}%)")

print("\nSample Observed Epochs (first 5):")
for log in observed_logs[:5]:
    pred = log['predicted']
    act = log['actual']
    print(f"Epoch {log['epoch']}: Predicted {pred[0]} of {pred[1]}, Actual {act[0]} of {act[1]} | Match: {log['match']}")

print("\nSample Unobserved Epochs (first 5):")
for log in unobserved_logs[:5]:
    pred = log['predicted']
    act = log['actual']
    print(f"Epoch {log['epoch']}: Predicted {pred[0]} of {pred[1]}, Actual {act[0]} of {act[1]} | Match: {log['match']}")

print("\nAll logs are saved and auditable. See phi_temporal_paradox_test.md for details.")
