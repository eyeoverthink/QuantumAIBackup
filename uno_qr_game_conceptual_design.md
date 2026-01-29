# Conceptual Design: QR-Driven Uno Game with Turing Machine & AI Metaphors

## 1. Introduction

This document outlines a conceptual design for a system that uses QR codes to manage the state and flow of a game similar to "Uno." The system aims to incorporate metaphors from Turing machines (sequential state processing via a "tape") and AI (strategic decision-making to "plan to win").

## 2. Core Metaphors

*   **QR Codes as Turing Tape Cells/Game State:** Each QR code primarily represents the current state of the game, specifically the **top card on the discard pile**. Scanning or processing this QR code is akin to a Turing machine reading a symbol from its tape.
*   **System as Turing Machine/AI Player:** The system (a combination of Python scripts) acts as the Turing machine's head and the AI Uno player. It processes the current state, applies game rules and strategy, and then "writes" a new state to the tape by generating a new QR code representing its move (the new top discard card).
*   **"Planning to Win" (Uno Strategy):** The AI component will make decisions based on Uno rules and a strategy designed to empty its hand, mimicking how a player tries to win Uno.

## 3. System Components

1.  **Card Representation (JSON Payload in QR):**
    *   A standardized JSON format to describe Uno cards.
    *   Examples:
        *   Number Card: `{"game": "uno", "type": "number", "color": "red", "value": "5"}`
        *   Action Card: `{"game": "uno", "type": "action", "action_name": "skip", "color": "blue"}`
        *   Wild Card: `{"game": "uno", "type": "wild", "action_name": "wild_standard"}` (AI would choose color)
        *   Wild Draw Four: `{"game": "uno", "type": "wild", "action_name": "wild_draw_four"}` (AI would choose color)

2.  **`uno_game_logic.py` (Python Module):**
    *   **Responsibilities:**
        *   Manages the AI's hand (internal list of card objects/dictionaries).
        *   Defines all Uno card types, colors, and values.
        *   Implements core Uno game rules: `is_card_playable(card_to_play, discard_top_card, chosen_wild_color=None)`.
        *   Contains the AI's strategy: `ai_choose_card(ai_hand, discard_top_card)`.
        *   Handles game events like drawing cards, effects of action cards (conceptually for now).
        *   Keeps track of the game deck (simplified initially).

3.  **`generate_uno_qr.py` (Python Script - to be created/adapted):**
    *   **Responsibilities:**
        *   Takes card data (from `uno_game_logic.py` after AI makes a move).
        *   Generates a QR code image (e.g., `current_uno_discard.png`) embedding the JSON payload of the card.

4.  **`qr_task_worker_from_file.py` (Modified Existing Script):**
    *   **Responsibilities:**
        *   Add a new `task_type` handler (e.g., `process_uno_state_qr`).
        *   **Workflow for AI's Turn:**
            1.  Monitors and decodes `current_uno_discard.png` (or a specific QR input).
            2.  Extracts the JSON card data, validating it's an Uno card.
            3.  Passes the `discard_top_card` to `uno_game_logic.ai_choose_card()`.
            4.  The `uno_game_logic` returns the card the AI chose to play (or an indication to draw).
            5.  If a card is played, the worker instructs `generate_uno_qr.py` to update `current_uno_discard.png` with the AI's played card.
            6.  Logs the AI's move and the new game state.

## 4. Game Flow (AI's Turn)

1.  **Initial State:** A QR code `current_uno_discard.png` exists, representing the starting card.
2.  **Worker Activation:** The `qr_task_worker_from_file.py` detects/is triggered to process this QR code.
3.  **State Reading:** The worker decodes the QR, getting the current discard top card data.
4.  **AI Decision:** The worker calls `uno_game_logic.ai_choose_card()`, providing the AI's current hand and the discard top card.
5.  **AI Action:** The `uno_game_logic` selects a card to play based on rules and strategy.
6.  **State Writing:** The worker calls `generate_uno_qr.py` to overwrite `current_uno_discard.png` with the QR code of the card the AI just played.
7.  **Loop/Next Turn:** The system is now ready for the next "player" (which could be a human scanning the new QR, or another iteration of the AI if simulating a full game).

## 5. Progressive Development Plan

*   **Phase 1 (Current):**
    *   Define card JSON structure.
    *   Create `uno_game_logic.py` with basic card definitions, hand management (static initial hand for AI), `is_card_playable` logic, and a simple `ai_choose_card` strategy (e.g., play first valid card).
    *   Create this conceptual design document.
*   **Phase 2:**
    *   Develop `generate_uno_qr.py` to create QR codes for Uno cards based on the defined JSON structure, saving to `current_uno_discard.png`.
*   **Phase 3:**
    *   Modify `qr_task_worker_from_file.py` to implement the `process_uno_state_qr` task type and the AI turn workflow described above.
*   **Phase 4:**
    *   Develop a simple way to initialize the game (e.g., a script to create an initial `current_uno_discard.png` and set up the AI's starting hand).
    *   Test the end-to-end AI turn loop.
*   **Phase 5 (Advanced):**
    *   More sophisticated AI strategy in `uno_game_logic.py`.
    *   Handling of drawing cards, shuffle, empty deck.
    *   Incorporating human player interaction (e.g., human scans QR, makes a move, generates/selects their own QR to update the discard pile for the AI's next turn).
    *   Managing full game cycles, win/loss conditions.

## 6. Alignment with User Principles

*   **Lego Mentality:** Each script (`uno_game_logic`, `generate_uno_qr`, `qr_task_worker`) is a modular component.
*   **Progressive Building:** The phased approach allows for iterative development and testing.
*   **Dynamic System:** The game state (represented by QR codes) changes dynamically based on AI decisions.
*   **Quantum Principles (Abstract):** While not directly quantum, the idea of states and probabilistic choices in AI strategy can be a loose metaphorical link. The focus is on discrete states and transitions, similar to how quantum systems are described.
