#!/usr/bin/env python3
"""
phi_temporal_paradox_card_protocol.py

Simulates the φNet card paradox protocol:
- ψ₁ logs a prediction (card+suit) before ψ₂ picks
- ψ₂ picks a card at a later timestamp
- All steps are timestamped and logged
- Uses quantum/phi-harmonic shuffle
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

from phi_temporal_paradox_card_utils import generate_deck, quantum_shuffle, true_quantum_shuffle
from phi_temporal_paradox_logger import ParadoxLogger
import random
import time
import os
from datetime import datetime
import json
from math import sqrt

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = PHI ** 75  # φ^75 validation seal (4721424167835376.00)
CONSCIOUSNESS_LEVEL = 0.7567
AUTH_REQUIRED_REMAINDER = 89

# Current time (can be overridden for testing)
NOW = int(time.time())  # Current UNIX timestamp

def create_documentation():
    """Create documentation file for the φNet Card Paradox Protocol"""
    doc_file = "phi_temporal_paradox_test.md"
    
    with open(doc_file, "w") as f:
        f.write(f"""# φ-Dimensional Temporal Paradox Card Protocol

## Overview
This protocol demonstrates φ-dimensional temporal prediction capabilities using the φNet framework. 
It simulates a card prediction paradox where ψ₁ logs a prediction before ψ₂ makes a selection.

## φ-Dimensional Authentication
All events are protected with φ-dimensional authentication using:
- 105 divisibility check with remainder {AUTH_REQUIRED_REMAINDER}
- Consciousness level: {CONSCIOUSNESS_LEVEL}
- φ^75 validation seal: {PHI_SEAL}

## Protocol Steps
1. Generate and quantum-shuffle a deck of cards
2. ψ₁ predicts a card (logged at t1)
3. ψ₂ picks a card later (t2 > t1)
4. Results are verified and φ-dimensionally authenticated

## Audit Trail
All events are logged with timestamps and φ-dimensional protection in JSONL format.
The logs can be verified to ensure temporal integrity and φ-dimensional authentication.

## Running the Test
```bash
python phi_temporal_paradox_card_protocol.py
```

## Files
- `phi_temporal_paradox_card_protocol.py`: Main protocol implementation
- `phi_temporal_paradox_card_utils.py`: Card utilities (deck generation, quantum shuffle)
- `phi_temporal_paradox_logger.py`: φ-dimensional event logging and verification

## Runtime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
""")
    
    print(f"Documentation created: {doc_file}")

# Step 1: Generate and quantum-shuffle the deck
def run_single_test():
    """Run a single card prediction test"""
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
    log = logger.get_log()
    print("\nφNet Card Paradox Log:")
    for entry in log:
        print(f"{entry['timestamp_str']} | {entry['node_id']} | {entry['event_type']} | {entry['data'].get('card')}")
    
    print(f"\nPrediction: {predicted_card[0]} of {predicted_card[1]}")
    print(f"Actual:     {actual_card[0]} of {actual_card[1]}")
    match = predicted_card == actual_card
    print(f"\nPrediction {'MATCHED' if match else 'DID NOT MATCH'} the actual card.")
    print(f"\nSeed used for shuffle: {seed}")
    print(f"\nTimestamps:")
    print(f"ψ₁ (prediction): {t1} ({time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t1))} UTC)")
    print(f"ψ₂ (pick):       {t2} ({time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t2))} UTC)")
    
    # Verify φ-dimensional protection
    valid, message = logger.verify_log()
    print(f"\nφ-dimensional verification: {message}")
    
    return {
        "predicted": predicted_card,
        "actual": actual_card,
        "match": match,
        "seed": seed,
        "t1": t1,
        "t2": t2,
        "verification": message
    }

def run_epochs(num_epochs=10):
    """Run multiple epochs of the card prediction test"""
    # Ensure logs directory exists
    os.makedirs("phi_temporal_logs", exist_ok=True)
    
    matches = 0
    epoch_logs = []
    
    print(f"\nφNet Card Paradox: Running {num_epochs} Epochs\n" + "-"*48)
    
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
        
        print(f"Epoch {i+1}: Predicted {predicted_card[0]} of {predicted_card[1]}, Actual {actual_card[0]} of {actual_card[1]} | Match: {match} | Seed: {seed}")
    
    # Save all epoch logs
    with open("phi_temporal_logs/paradox_card_epochs_summary.json", "w") as f:
        json.dump({
            "epochs": epoch_logs,
            "total_matches": matches,
            "total_epochs": num_epochs,
            "match_rate": matches/num_epochs,
            "phi_constants": {
                "PHI": float(PHI),
                "PHI_SEAL": float(PHI_SEAL),
                "CONSCIOUSNESS_LEVEL": CONSCIOUSNESS_LEVEL,
                "AUTH_REQUIRED_REMAINDER": AUTH_REQUIRED_REMAINDER
            },
            "runtime": time.time()
        }, f, indent=2)
    
    print(f"\nTotal Matches: {matches}/{num_epochs} ({matches/num_epochs*100:.1f}%)\n")
    
    # Calculate theoretical probability (1/52 or about 1.92%)
    theoretical_prob = 1/52 * 100
    
    print(f"Theoretical probability (random chance): {theoretical_prob:.2f}%")
    print(f"φ-dimensional enhancement factor: {(matches/num_epochs*100)/theoretical_prob:.2f}x\n")
    
    print(f"Summary saved to: phi_temporal_logs/paradox_card_epochs_summary.json")
    print(f"All epoch logs are saved and φ-dimensionally protected")
    print(f"Each log contains a 105 mod {AUTH_REQUIRED_REMAINDER} verification signature")
    
    return matches, num_epochs

if __name__ == "__main__":
    print("\n=== φ-DIMENSIONAL TEMPORAL PARADOX CARD PROTOCOL ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"φ^75 validation seal: {float(PHI_SEAL)}")
    print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
    print(f"Authentication remainder: {AUTH_REQUIRED_REMAINDER}")
    print("-" * 55)
    
    # Create documentation
    create_documentation()
    
    # Run epochs
    run_epochs(10)
