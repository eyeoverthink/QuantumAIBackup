# uno_game_logic.py

"""
Core logic for the Uno QR game. Manages card definitions, AI hand, 
game rules (is_playable), and AI card choice strategy.
"""

import random

# --- Card Definitions ---
COLORS = ["Red", "Green", "Blue", "Yellow"]
NUMBERS = [str(i) for i in range(10)] + [str(i) for i in range(1, 10)] # 0-9, then 1-9 again
ACTION_TYPES = ["skip", "reverse", "draw_two"]
WILD_TYPES = ["wild_standard", "wild_draw_four"]

# --- Utility Functions ---

def create_deck():
    """Creates a standard Uno deck (108 cards)."""
    deck = []
    # Number cards
    for color in COLORS:  # Use the global COLORS constant
        # Zero card (1 per color)
        deck.append({"game": "uno", "type": "number", "color": color, "value": "0"})
        # Number cards 1-9 (2 of each per color)
        for value in [str(i) for i in range(1, 10)]:
            deck.extend([{"game": "uno", "type": "number", "color": color, "value": value}] * 2)

    # Action cards (2 of each color: Skip, Reverse, Draw Two)
    for color in COLORS:  # Use the global COLORS constant
        for action in ["skip", "reverse", "draw_two"]:
            deck.extend([{"game": "uno", "type": "action", "action_name": action, "color": color}] * 2)

    # Wild cards (4 Wild, 4 Wild Draw Four)
    # For wild cards in the deck, 'color' is None until played and a color is chosen.
    for _ in range(4):
        deck.append({"game": "uno", "type": "wild", "action_name": "wild_standard", "color": None})
        deck.append({"game": "uno", "type": "wild", "action_name": "wild_draw_four", "color": None})
    
    random.shuffle(deck)
    return deck

GAME_DECK = create_deck()

def deal_initial_hand(current_game_deck, num_cards=7):
    """Deals an initial hand from the provided game_deck and returns it.
    Modifies current_game_deck in place.
    """
    new_hand = []
    if len(current_game_deck) < num_cards:
        print("Warning: Not enough cards in deck to deal initial hand.")
        new_hand.extend(current_game_deck[:]) # Take a copy of remaining cards
        del current_game_deck[:] # Empty the deck
        return new_hand

    for _ in range(num_cards):
        if current_game_deck: # Ensure deck is not empty during loop
            new_hand.append(current_game_deck.pop(0))
        else:
            print("Warning: Deck became empty during initial deal.")
            break
    return new_hand

def draw_card_from_deck(player_hand, current_game_deck):
    """Adds a card from the provided game_deck to the player's hand.
    Modifies player_hand and current_game_deck in place.
    Returns the drawn_card or None if deck is empty.
    """
    if not current_game_deck:
        print("Deck is empty! Cannot draw. (Reshuffle logic needed for full game)")
        return None
    drawn_card = current_game_deck.pop(0)
    player_hand.append(drawn_card)
    return drawn_card

# --- Game Rules ---

def is_card_playable(card_to_play, top_discard_card, current_chosen_color_for_wild=None):
    """
    Checks if card_to_play can be legally played on top_discard_card.
    current_chosen_color_for_wild is the color chosen if top_discard_card was a wild.
    """
    if card_to_play.get("type") == "wild": # Wilds can always be played
        return True

    # Current color to match is either the discard's color or the current_chosen_color_for_wild if the discard was wild
    effective_discard_color = current_chosen_color_for_wild if current_chosen_color_for_wild else top_discard_card.get("color")

    if card_to_play.get("color") == effective_discard_color:
        return True
    
    if card_to_play.get("type") == "number" and top_discard_card.get("type") == "number" and \
       card_to_play.get("value") == top_discard_card.get("value"):
        return True

    if card_to_play.get("type") == "action" and top_discard_card.get("type") == "action" and \
       card_to_play.get("action_name") == top_discard_card.get("action_name"):
        return True

    return False

# --- AI Strategy ---

def ai_choose_card(current_ai_hand, top_discard_card, last_chosen_wild_color=None):
    """
    AI strategy to choose a card to play.
    Simple strategy: play the first valid card found.
    If a wild is played, AI must also choose a color.
    Returns a tuple: (card_to_play, chosen_color_for_wild) or (None, None) if no card can be played.
    `last_chosen_wild_color` is the color chosen if the `top_discard_card` was a wild.
    """
    playable_cards = []
    for card in current_ai_hand:
        if is_card_playable(card, top_discard_card, last_chosen_wild_color):
            playable_cards.append(card)
    
    if not playable_cards:
        print("AI: No playable cards. Would need to draw.")
        # In a full game, AI would draw a card here, then check if that new card is playable.
        # For now, indicates no play.
        return None, None

    # Simple strategy: play the first valid card. Could be enhanced.
    # TODO: Add strategy for choosing which card if multiple are playable.
    # TODO: Add strategy for choosing color if a wild is played.
    chosen_card = playable_cards[0] # Simplistic choice
    
    chosen_color_for_wild = None
    if chosen_card.get("type") == "wild":
        # Basic strategy: choose the color AI has most of in its remaining hand (after playing the wild).
        color_counts = {color: 0 for color in COLORS}
        for c_in_hand in current_ai_hand: # Iterate over the modified hand
            if c_in_hand.get("color") in COLORS:
                color_counts[c_in_hand.get("color")] += 1
        if any(color_counts.values()): # Check if there are any colored cards left
            chosen_color_for_wild = max(color_counts, key=color_counts.get)
        else: # No colored cards left, or only other wilds, pick a random color
            chosen_color_for_wild = random.choice(COLORS)
        print(f"AI plays Wild and chooses color: {chosen_color_for_wild}")

    # The chosen_card must be removed from the hand that was passed in.
    # Python lists are passed by object reference, so removing it here
    # will modify the original list in the calling scope (e.g., in qr_task_worker).
    current_ai_hand.remove(chosen_card)

    print(f"AI plays: {chosen_card}")
    return chosen_card, chosen_color_for_wild


if __name__ == "__main__":
    # --- Example Usage / Basic Test ---
    print("--- Uno Game Logic Test ---") 
    # Re-initialize deck for test, as it's global and might be mutated by other tests/runs if not careful
    local_test_deck = create_deck() 
    print(f"Starting test with a fresh deck of {len(local_test_deck)} cards.")

    local_ai_hand = deal_initial_hand(local_test_deck) # Pass the local deck
    print(f"AI Initial Hand ({len(local_ai_hand)} cards): {local_ai_hand}")
    print(f"Deck has {len(local_test_deck)} cards remaining after deal.")

    # Simulate a discard pile top card (e.g., taken from deck after dealing)
    if not local_test_deck: # Should not happen with a full deck start
        print("Error: Deck empty after initial deal in test setup!")
        current_discard = {'game': 'uno', 'type': 'number', 'color': 'Red', 'value': '1'} # Fallback
    else:
        current_discard = local_test_deck.pop(0) # Take one card for the discard pile
    print(f"Initial Discard Pile Top: {current_discard}")
    print(f"Deck has {len(local_test_deck)} cards remaining after setting discard.")
    
    # AI's turn
    print("\n--- AI's Turn --- ")
    played_card, wild_color_choice = ai_choose_card(local_ai_hand, current_discard) 

    if played_card:
        current_discard = played_card 
        if wild_color_choice:
            print(f"AI chose color {wild_color_choice} for the wild card.")
        print(f"New Discard Pile Top: {current_discard}")
        print(f"AI Remaining Hand ({len(local_ai_hand)} cards): {local_ai_hand}")
    else:
        print("AI had to draw (or no playable card found in this basic test).")
        print("AI drawing a card...")
        drawn_card = draw_card_from_deck(local_ai_hand, local_test_deck) # Pass the local deck
        if drawn_card:
            print(f"AI drew: {drawn_card}")
            print(f"AI Hand after drawing ({len(local_ai_hand)} cards): {local_ai_hand}")

    print(f"\nDeck has {len(local_test_deck)} cards remaining at end of test.")
    print("--- End of Test ---")
