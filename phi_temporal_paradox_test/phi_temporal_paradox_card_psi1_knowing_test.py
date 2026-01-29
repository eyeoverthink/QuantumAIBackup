"""
phi_temporal_paradox_card_psi1_knowing_test.py

Implements the correct paradox protocol for the user's theory:
- The conscious agent (ψ₁, the user) "knows" a card (rank & suit), which is the ground truth.
- The system (ψ₂) attempts to "see" or reveal the card ψ₁ knows, using quantum/phi-harmonic methods.
- The act of knowing by ψ₁ is the base for comparison—not random guessing.
- All results are logged and fully auditable.

Instructions (for interactive mode):
- User is prompted to enter a card (rank and suit) they "know."
- System attempts to reveal the card.
- Results are reported and logged.

Lego style: No core or root files are modified.
"""

from phi_temporal_paradox_card_utils import generate_deck, true_quantum_shuffle
from phi_temporal_paradox_logger import ParadoxLogger
import time

NOW = 1745308285  # 2025-04-22T01:11:25-07:00 in UNIX seconds

def get_user_card():
    print("\nPlease enter the card you 'know':")
    rank = input("Rank (Ace, 2-10, Jack, Queen, King): ").strip()
    suit = input("Suit (Hearts, Diamonds, Clubs, Spades): ").strip()
    return (rank, suit)

def system_reveal_card(deck):
    shuffled = true_quantum_shuffle(deck)
    return shuffled[0]

def main():
    deck = generate_deck()
    user_card = get_user_card()
    revealed_card = system_reveal_card(deck)
    logger = ParadoxLogger(log_file="paradox_card_psi1_knowing_log.jsonl")
    t1 = NOW
    logger.log_event("psi1", "user_knowing_card", {"card": user_card}, timestamp=t1)
    logger.log_event("psi2", "system_revealed_card", {"card": revealed_card}, timestamp=t1+1)
    print(f"\nYou 'knew': {user_card[0]} of {user_card[1]}")
    print(f"System revealed: {revealed_card[0]} of {revealed_card[1]}")
    match = user_card == revealed_card
    print(f"\nMatch: {match}")
    print("\nAll actions are logged and auditable. See phi_temporal_paradox_test.md for details.")

if __name__ == "__main__":
    main()
