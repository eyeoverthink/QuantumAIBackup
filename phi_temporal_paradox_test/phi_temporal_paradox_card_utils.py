"""
phi_temporal_paradox_card_utils.py

Provides:
- Standard 52-card deck generation
- Quantum/phi-harmonic card shuffling using user's true random system
- Card and suit utilities
"""

import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# If available, import your quantum/phi random generator for shuffling
try:
    from phi_harmonic_random_orchestrator_adapter import QuantumPhiRandom
    HAVE_QUANTUM_RANDOM = True
except ImportError:
    QuantumPhiRandom = None
    HAVE_QUANTUM_RANDOM = False


def generate_deck():
    return [(rank, suit) for suit in SUITS for rank in RANKS]

def quantum_shuffle(deck, seed=None):
    """Deterministic shuffle using quantum/phi random if available, else Python random."""
    if HAVE_QUANTUM_RANDOM:
        qrand = QuantumPhiRandom(seed=seed)
        deck_copy = deck[:]
        # Fisher-Yates shuffle using quantum random
        for i in range(len(deck_copy)-1, 0, -1):
            j = int(qrand.random() * (i+1))
            deck_copy[i], deck_copy[j] = deck_copy[j], deck_copy[i]
        return deck_copy
    else:
        rnd = random.Random(seed) if seed is not None else random
        deck_copy = deck[:]
        rnd.shuffle(deck_copy)
        return deck_copy

def true_quantum_shuffle(deck):
    """Non-deterministic shuffle using user's true quantum random generator (if available)."""
    if HAVE_QUANTUM_RANDOM:
        qrand = QuantumPhiRandom()
        deck_copy = deck[:]
        for i in range(len(deck_copy)-1, 0, -1):
            j = int(qrand.random() * (i+1))
            deck_copy[i], deck_copy[j] = deck_copy[j], deck_copy[i]
        return deck_copy
    else:
        # Fallback to system random
        deck_copy = deck[:]
        random.shuffle(deck_copy)
        return deck_copy
